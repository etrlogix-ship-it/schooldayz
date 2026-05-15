try:
    import requests
    HAS_REQUESTS = True
except ImportError:
    HAS_REQUESTS = False

import os

def download_file(url, filename=None):
    if not HAS_REQUESTS:
        print("Install requests: pip3 install requests --break-system-packages")
        return
    
    if not filename:
        filename = url.split("/")[-1] or "download"
    
    try:
        print(f"Downloading: {url}")
        print(f"Saving as: {filename}")
        
        r = requests.get(url, stream=True, timeout=30)
        total = int(r.headers.get("content-length", 0))
        downloaded = 0
        
        with open(filename, "wb") as f:
            for chunk in r.iter_content(chunk_size=8192):
                f.write(chunk)
                downloaded += len(chunk)
                if total > 0:
                    pct = downloaded / total * 100
                    bar = "#" * int(pct/5) + "-" * (20 - int(pct/5))
                    print(f"\r[{bar}] {pct:.1f}% ({downloaded}/{total} bytes)", end="", flush=True)
        
        print(f"\nDone! Saved as {filename} ({downloaded} bytes)")
    except Exception as e:
        print(f"\nError: {e}")

print("File Downloader")
print("===============")
print("Download files from the internet with a progress bar!")

while True:
    url = input("\nURL to download (or quit): ").strip()
    if url.lower() == "quit": break
    if not url.startswith("http"):
        print("URL must start with http:// or https://")
        continue
    name = input("Save as (Enter for auto): ").strip() or None
    download_file(url, name)
