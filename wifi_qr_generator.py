#!/usr/bin/env python3
"""
Wi-Fi QR Code Generator
Generate scannable QR codes for Wi-Fi networks
"""

import qrcode
import sys
from pathlib import Path


def generate_wifi_qr(ssid, password, security="WPA", hidden=False):
    """
    Generate a Wi-Fi QR code
    
    Args:
        ssid: Network name
        password: Network password
        security: Security type (WPA, WEP, or nopass)
        hidden: Whether the network is hidden
    """
    # Format: WIFI:T:WPA;S:mynetwork;P:mypassword;H:false;;
    wifi_string = f"WIFI:T:{security};S:{ssid};P:{password};H:{'true' if hidden else 'false'};;"
    
    # Create QR code
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(wifi_string)
    qr.make(fit=True)
    
    return qr


def save_qr_image(qr, filename="wifi_qr.png"):
    """Save QR code as image file"""
    img = qr.make_image(fill_color="black", back_color="white")
    img.save(filename)
    print(f"✓ QR code saved as: {filename}")


def print_qr_terminal(qr):
    """Print QR code to terminal"""
    qr.print_ascii(invert=True)


def main():
    print("=" * 50)
    print("Wi-Fi QR Code Generator")
    print("=" * 50)
    
    # Get user input
    ssid = input("\nEnter Wi-Fi name (SSID): ").strip()
    if not ssid:
        print("Error: SSID cannot be empty")
        sys.exit(1)
    
    password = input("Enter Wi-Fi password: ").strip()
    
    security = input("Security type (WPA/WEP/nopass) [WPA]: ").strip().upper() or "WPA"
    if security not in ["WPA", "WEP", "NOPASS"]:
        print("Invalid security type, using WPA")
        security = "WPA"
    
    hidden = input("Hidden network? (y/n) [n]: ").strip().lower() == 'y'
    
    # Generate QR code
    print("\nGenerating QR code...")
    qr = generate_wifi_qr(ssid, password, security, hidden)
    
    # Display in terminal
    print("\nQR Code (scan with your phone):")
    print_qr_terminal(qr)
    
    # Save to file
    filename = f"wifi_{ssid.replace(' ', '_')}_qr.png"
    save_qr_image(qr, filename)
    
    print(f"\n✓ Done! Share the QR code to connect to '{ssid}'")


if __name__ == "__main__":
    main()
