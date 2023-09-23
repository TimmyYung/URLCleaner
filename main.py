import re
import pyperclip
import time

def remove_tracking_links(url):
    # Remove tracking parameters from the URL
    url = re.sub(r'(\?|&)utm_[a-zA-Z0-9_]+=[^&]+', '', url)
    url = re.sub(r'(\?|&)fbclid=[^&]+', '', url)
    url = re.sub(r'(\?|&)gclid=[^&]+', '', url)
    url = re.sub(r'(\?|&)msclkid=[^&]+', '', url)
    url = re.sub(r'ufe=app_do%3Aamzn1\.fos\.[a-zA-Z0-9_.-]+', '', url)
    
    return url

# Initialize the previous clipboard content
previous_clipboard = ""

# Infinite loop to continuously monitor the clipboard
while True:
    # Check if the clipboard content has changed
    current_clipboard = pyperclip.paste()
    if current_clipboard != previous_clipboard:
        # Check if the copied content is a URL
        if current_clipboard.startswith("http") or current_clipboard.startswith("www"):
            # Remove tracking links from the URL
            clean_link = remove_tracking_links(current_clipboard)
            # Update the clipboard with the cleaned link
            pyperclip.copy(clean_link)
            print("Cleaned link copied to clipboard:", clean_link)
    
    # Update the previous clipboard content
    previous_clipboard = current_clipboard
    
    # Sleep for a short duration to avoid high CPU usage
    time.sleep(0.5)
