try:
    import qrcode
    HAS_QR = True
except ImportError:
    HAS_QR = False

def ascii_qr(text):
    """Very simple QR-like pattern for demo"""
    import hashlib
    h = int(hashlib.md5(text.encode()).hexdigest()[:8], 16)
    size = 15
    print(f"\nSimulated QR for: {text}")
    print("+" + "-" * (size*2) + "+")
    for r in range(size):
        row = "|"
        for c in range(size):
            # Corner markers
            if (r < 3 and c < 3) or (r < 3 and c > size-4) or (r > size-4 and c < 3):
                row += "██"
            else:
                val = (h >> ((r*size+c) % 32)) & 1
                row += "██" if val else "  "
        print(row + "|")
    print("+" + "-" * (size*2) + "+")
    print("(Note: This is a demo pattern, not a real QR code)")

print("QR Code Generator")
print("=================")

if not HAS_QR:
    print("For real QR codes: pip3 install qrcode[pil] --break-system-packages")
    print("Using demo mode for now.")

while True:
    text = input("\nText or URL for QR code (or quit): ").strip()
    if text.lower() == "quit": break
    
    if HAS_QR:
        qr = qrcode.QRCode(border=1)
        qr.add_data(text)
        qr.make(fit=True)
        qr.print_ascii()
        fname = f"qr_{text[:20].replace(' ','_').replace('/','-')}.png"
        img = qr.make_image(fill_color="black", back_color="white")
        img.save(fname)
        print(f"Saved as {fname}")
    else:
        ascii_qr(text)
