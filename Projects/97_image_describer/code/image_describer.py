#!/usr/bin/env python3
"""
AI Image Describer - Project 97
Show an image to Claude AI and get a detailed description.
Requires: pip install anthropic pillow
"""

import os
import sys
import base64
import time

def load_env():
    env_file = os.path.join(os.path.dirname(__file__), ".env")
    if os.path.exists(env_file):
        with open(env_file) as f:
            for line in f:
                line = line.strip()
                if line and not line.startswith("#") and "=" in line:
                    key, val = line.split("=", 1)
                    os.environ[key.strip()] = val.strip().strip('"')

load_env()

try:
    import anthropic
    API_AVAILABLE = True
except ImportError:
    API_AVAILABLE = False

try:
    from PIL import Image
    PIL_AVAILABLE = True
except ImportError:
    PIL_AVAILABLE = False

DEMO_DESCRIPTIONS = {
    "garden": "I can see a lush garden scene with vibrant green plants and colourful flowers. There appear to be red roses and yellow daisies in bloom. A garden path winds through the scene, and in the background there's a wooden fence. The lighting suggests a warm, sunny afternoon.",
    "cat": "There's an adorable cat in this image! It appears to be a tabby with brown and orange striped fur. The cat is sitting in a relaxed pose and seems to be gazing curiously at something off-camera. Its whiskers are clearly visible and its eyes have that characteristic vertical-slit pupil.",
    "default": "This is a fascinating image! I can see various objects and elements that make up an interesting scene. The composition has good lighting and the colours are vivid. If you'd like a real description with actual AI vision, set up your API key as described in the README!"
}

def get_image_info(image_path):
    """Get basic info about an image file."""
    size = os.path.getsize(image_path)
    info = {"path": image_path, "size_kb": size // 1024, "extension": os.path.splitext(image_path)[1].lower()}
    if PIL_AVAILABLE:
        try:
            with Image.open(image_path) as img:
                info["width"]  = img.width
                info["height"] = img.height
                info["mode"]   = img.mode
        except:
            pass
    return info

def encode_image(image_path):
    """Encode image to base64 for API."""
    with open(image_path, "rb") as f:
        return base64.standard_b64encode(f.read()).decode("utf-8")

def get_media_type(extension):
    types = {".jpg": "image/jpeg", ".jpeg": "image/jpeg",
             ".png": "image/png", ".gif": "image/gif", ".webp": "image/webp"}
    return types.get(extension, "image/jpeg")

def describe_image_api(image_path, question=None):
    """Send image to Claude API for description."""
    api_key = os.environ.get("ANTHROPIC_API_KEY", "")
    if not api_key or api_key == "your-key-here":
        return None, "no_key"
    if not API_AVAILABLE:
        return None, "no_lib"

    try:
        client = anthropic.Anthropic(api_key=api_key)
        image_data = encode_image(image_path)
        ext = os.path.splitext(image_path)[1].lower()
        media_type = get_media_type(ext)

        prompt = question or "Please describe this image in detail. Tell me what you see, including objects, people, colours, setting, and anything interesting or notable."

        response = client.messages.create(
            model="claude-sonnet-4-20250514",
            max_tokens=500,
            messages=[{
                "role": "user",
                "content": [
                    {
                        "type": "image",
                        "source": {
                            "type": "base64",
                            "media_type": media_type,
                            "data": image_data,
                        }
                    },
                    {"type": "text", "text": prompt}
                ]
            }]
        )
        return response.content[0].text, "live"
    except Exception as e:
        return f"Error: {e}", "error"

def demo_description(image_path):
    """Return a demo description based on filename."""
    path_lower = image_path.lower()
    for keyword, desc in DEMO_DESCRIPTIONS.items():
        if keyword != "default" and keyword in path_lower:
            return desc
    return DEMO_DESCRIPTIONS["default"]

def print_description(text):
    """Print description with nice word wrapping."""
    words = text.split()
    line = "  "
    for word in words:
        if len(line) + len(word) > 72:
            print(line)
            line = "  " + word + " "
        else:
            line += word + " "
    if line.strip():
        print(line)

def interactive_mode():
    """Interactive mode: ask multiple questions about an image."""
    print("\n  📂 Enter image path (or press Enter for demo): ", end="")
    image_path = input().strip()

    if not image_path:
        print("  Using demo mode (no image file)")
        image_path = "demo_image.jpg"
        use_demo = True
    elif not os.path.exists(image_path):
        print(f"  ❌ File not found: {image_path}")
        print("  Using demo mode instead.")
        use_demo = True
    else:
        use_demo = False
        info = get_image_info(image_path)
        print(f"\n  📷 Image: {info['path']}")
        print(f"     Size: {info['size_kb']}KB", end="")
        if "width" in info:
            print(f"  Dimensions: {info['width']}×{info['height']}px", end="")
        print()

    print("\n  🤖 Ask questions about the image (or press Enter for full description)")
    print("  Type 'quit' to exit\n")

    while True:
        print("  Question: ", end="")
        question = input().strip()

        if question.lower() in ("quit", "q", "exit"):
            break

        if not question:
            question = None

        print(f"\n  🔍 Analysing image...\n")
        time.sleep(0.5 if use_demo else 0.1)

        if use_demo:
            description = demo_description(image_path)
            source = "demo"
        else:
            description, source = describe_image_api(image_path, question)

        if source == "no_key":
            print("  ⚠️  No API key — showing demo description:\n")
            description = demo_description(image_path)
        elif source == "no_lib":
            print("  ❌ Please run: pip install anthropic\n")
            break
        elif source == "error":
            print(f"  ❌ {description}\n")
            continue

        print(f"  🤖 Description:\n")
        print_description(description)
        print()

def batch_mode(image_paths):
    """Describe multiple images at once."""
    print(f"\n  📷 Describing {len(image_paths)} image(s)...\n")
    for path in image_paths:
        if not os.path.exists(path):
            print(f"  ❌ {path}: File not found\n")
            continue

        print(f"  {'─'*46}")
        print(f"  📷 {os.path.basename(path)}")
        description, source = describe_image_api(path)

        if source in ("no_key", "demo"):
            description = demo_description(path)
            print(f"  [Demo mode]\n")
        elif source in ("no_lib", "error"):
            print(f"  ❌ Could not describe: {description}\n")
            continue

        print_description(description)
        print()

def main():
    print("=" * 48)
    print("  🖼️  AI Image Describer - Raspberry Pi")
    print("=" * 48)

    api_key = os.environ.get("ANTHROPIC_API_KEY", "")
    if not api_key or api_key == "your-key-here":
        print("\n  ⚠️  Demo mode (no API key)")
        print("  See README for setup instructions")
    else:
        print("\n  ✅ API key found — live AI mode")
        if not API_AVAILABLE:
            print("  ❌ Missing: pip install anthropic")
            return

    # Check for command-line image arguments
    if len(sys.argv) > 1:
        batch_mode(sys.argv[1:])
    else:
        interactive_mode()

    print("  Thanks for using AI Image Describer! 🖼️")

if __name__ == "__main__":
    main()
