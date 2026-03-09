# QR Code Generator

Simple Python CLI tool to generate a QR code image from a URL or any text string.

## Requirements

- Python 3.8+
- `qrcode` package (with Pillow support)

Install dependency:

```bash
pip install "qrcode[pil]"
```

## Usage

Run the script with:

```bash
python url_gen.py <url_or_text> <output_filename>
```

Example:

```bash
python url_gen.py "https://example.com" "example-qr.png"
```

## Output

- Files are always saved in the `.output/` directory.
- The script uses only the file name part of `output_filename`.
- If `.output/` does not exist, it is created automatically.

After generation, the script prints the saved path, for example:

```text
QR code saved to .output/example-qr.png
```

## Notes

- Input can be a URL or plain text.
- Current QR generation settings in `url_gen.py`:
	- `version=1`
	- `error_correction=ERROR_CORRECT_L`
	- `box_size=20`
	- `border=2`