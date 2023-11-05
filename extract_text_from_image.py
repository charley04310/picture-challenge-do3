from PIL import Image

def extract_text_from_image(image_path):
    image = Image.open(image_path)
    width, height = image.size

    binary_text = ""
    text = ""
    end_marker = "1111111111111110"


    for y in range(height):
        for x in range(width):
            pixel = list(image.getpixel((x, y)))

            for channel in range(3):  
                binary_text += str(pixel[channel] & 1)

                if len(binary_text) >= 16 and binary_text[-16:] == end_marker:
                    break

            if len(binary_text) >= 16 and binary_text[-16:] == end_marker:
                break

        if len(binary_text) >= 16 and binary_text[-16:] == end_marker:
            break

    binary_text = binary_text[:-16]  

    for i in range(0, len(binary_text), 8):
        byte = binary_text[i:i+8]
        text += chr(int(byte, 2))

    # return text

# Example of usage
hidden_image = "hidden_image.png"
# extracted_text = extract_text_from_image(hidden_image)

print("Text extracted from the image:")
# print(extracted_text)
