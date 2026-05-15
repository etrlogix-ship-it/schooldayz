from PIL import Image
import sys
import os

ASCII_CHARS = "@%#*+=-:. "

def convert_to_ascii(image_path, width=80):
    try:
        img = Image.open(image_path).convert("L")  # Grayscale
    except Exception as e:
        print(f"Error opening image: {e}")
        return

    # Resize maintaining aspect
    orig_w, orig_h = img.size
    aspect = orig_h / orig_w
    new_h = int(width * aspect * 0.55)  # 0.55 for font aspect ratio
    img = img.resize((width, new_h))

    pixels = list(img.getdata())
    ascii_str = ""
    for i, pixel in enumerate(pixels):
        ascii_str += ASCII_CHARS[pixel * len(ASCII_CHARS) // 256]
        if (i + 1) % width == 0:
            ascii_str += "\n"

    print(ascii_str)

    # Save to file
    output = image_path.rsplit(".", 1)[0] + "_ascii.txt"
    with open(output, "w") as f:
        f.write(ascii_str)
    print(f"\nSaved to {output}")

if len(sys.argv) < 2:
    # Demo mode - create a simple test gradient
    print("Usage: python3 ascii_photo.py <image_file>")
    print("\nDemo - gradient test:")
    for row in range(10):
        for col in range(40):
            idx = (row * 40 + col) * len(ASCII_CHARS) // 400
            print(ASCII_CHARS[idx], end="")
        print()
else:
    convert_to_ascii(sys.argv[1])
