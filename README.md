# URLCleaner

This Python script monitors changes in the clipboard and removes tracking links when a link is copied. It supports various types of tracking parameters commonly found in URLs, such as `utm_`, `fbclid`, `gclid`, `msclkid`, and a specific case for Amazon links.

## Prerequisites

- Python 3.x
- `pyperclip` library (install using `pip install pyperclip`)

## Usage

1. Clone the repository or download the script file (`main.py`).
2. Install the `pyperclip` library if you haven't already: `pip install pyperclip`.
3. Run the script: `python main.py`.
4. The script will continuously monitor the clipboard for changes.
5. When a link is copied, the script will remove any tracking parameters and update the clipboard with the cleaned link.
6. The cleaned link will be printed in the console.

### Windows

1. Press `Win + R` to open the Run dialog.
2. Type `shell:startup` and press Enter.
3. Copy the `main.py` script to the Startup folder that opens.
4. The script will now run every time you start your computer.

## Supported Tracking Parameters

- `utm_`: Commonly used by Google Analytics for campaign tracking.
- `fbclid`: Facebook click identifier.
- `gclid`: Google click identifier.
- `msclkid`: Microsoft click identifier.
- Amazon tracking parameter: `ufe=app_do%3Aamzn1.fos.[random_string]`.# URLCleaner

## Notes

- The script runs indefinitely until you manually stop it (press `Ctrl+C` in the terminal).
