"""""
Generates a QR code image from a given URL or text.
"""
import argparse
from pathlib import Path

import qrcode

parser = argparse.ArgumentParser(description='Generate a QR code image.')
parser.add_argument('url', help='URL or text to encode in the QR code')
parser.add_argument('output_filename', help='Output file name (saved in .output/)')
args = parser.parse_args()

output_dir = Path('.output')
output_dir.mkdir(parents=True, exist_ok=True)
output_path = output_dir / Path(args.output_filename).name

qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=20,
    border=2
)

qr.add_data(args.url)
qr.make(fit=True)

img = qr.make_image(
    fill_color='black',
    back_color='white',
    )
img.save(output_path)
print(f"QR code saved to {output_path}")
