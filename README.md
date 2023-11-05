# Steganography in Python

This repository contains two Python scripts that demonstrate steganography techniques for hiding and extracting text within images. Steganography is the practice of concealing information within other data to keep it confidential. In this case, we use the least significant bit (LSB) steganography method to hide text within an image and then extract it.

## Usage

1. Hiding Text in an Image

To hide text in an image, use the `hide_text_in_image` function from the `hide_text_in_image.py` script.

```python
from PIL import Image
from hide_text_in_image import hide_text_in_image

source_image = "image.jpg"
text_to_hide = "Your text here"
hidden_image = "hidden_image.png"

hide_text_in_image(source_image, text_to_hide, hidden_image)
```

This will create a new image called `hidden_image.png` that contains the text `Your text here` hidden within it.

2. Extracting Text from an Image

To extract text from an image, use the `extract_text_from_image` function from the `extract_text_from_image.py` script.

```python
from PIL import Image
from extract_text_from_image import extract_text_from_image

hidden_image = "hidden_image.png"
extracted_text = extract_text_from_image(hidden_image)

print("Text extracted from the image:")
print(extracted_text)
```

This will print the text that was hidden within the image.

## Requirements

- Python 3
- Pillow (PIL fork)
