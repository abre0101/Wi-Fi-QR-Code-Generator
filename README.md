# Wi-Fi QR Code Generator

Generate scannable QR codes for Wi-Fi networks. Works completely offline once dependencies are installed.

## Features

- 📱 Generate scannable Wi-Fi QR codes
- 🖼️ Save as PNG image
- 💻 Display in terminal
- 🔒 Supports WPA, WEP, and open networks
- 🚫 Works offline
- 🎯 Simple and fast

## Installation

```bash
py -m pip install -r requirements.txt
```

## Usage

Run the script:

```bash
py wifi_qr_generator.py
```

Follow the prompts:
1. Enter your Wi-Fi network name (SSID)
2. Enter the password
3. Select security type (WPA/WEP/nopass)
4. Specify if network is hidden

The QR code will be:
- Displayed in your terminal
- Saved as a PNG file (e.g., `wifi_MyNetwork_qr.png`)

## Example

```
Enter Wi-Fi name (SSID): MyHomeWiFi
Enter Wi-Fi password: SecurePass123
Security type (WPA/WEP/nopass) [WPA]: WPA
Hidden network? (y/n) [n]: n
```

## How It Works

The generator creates a QR code in the standard Wi-Fi format:
```
WIFI:T:WPA;S:NetworkName;P:Password;H:false;;
```

When scanned with a smartphone, it automatically prompts to connect to the network.

## Requirements

- Python 3.7+
- qrcode library (8.2+)
- Pillow (12.0+)

## Tested On

- Python 3.13.9
- Windows 11

## License

MIT
