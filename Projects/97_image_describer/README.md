# 97 🖼️ AI Image Describer

**Category:** 🧠 AI & Cool Tech  
**Difficulty:** ⭐⭐ Intermediate  
**Time:** 20 minutes

## What You'll Make
Show an image to an AI and it will describe what it sees! Take a photo with the Pi Camera, or use any image file, and the AI will explain everything in the picture in detail.

## What You'll Learn
- Working with image files in Python
- Sending images to an AI API (Vision AI)
- How computers "see" and understand images

## Parts You'll Need
- Raspberry Pi
- Pi Camera Module (optional — can use any image file)
- Internet connection

## Setup

### Install libraries
```bash
pip install anthropic pillow
```

### Set your API key
```bash
export ANTHROPIC_API_KEY="your-key-here"
```

### Take a photo (if using Pi Camera)
```bash
libcamera-still -o my_photo.jpg
```

### Run it!
```bash
python3 image_describer.py my_photo.jpg
```

## What It Can See
- Objects and animals
- People and what they're doing
- Text in images
- Scenes and environments
- Colours and patterns
- Emotions on faces

## Example Output
```
📷 Analysing: garden_photo.jpg
🤖 I can see a colourful garden with red roses in the foreground.
   In the background there's a wooden fence and a blue sky with
   white fluffy clouds. There's a yellow butterfly perched on
   one of the rose petals. The image looks like it was taken
   on a sunny afternoon in summer.
```

## Demo Mode
No API key? The program shows example descriptions so you can understand how it works!
