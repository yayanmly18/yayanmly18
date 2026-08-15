from PIL import Image
from pathlib import Path

# Konfigurasi
INPUT = "foto.jpeg"
OUTPUT = "portrait.txt"
WIDTH = 100   # lebar ASCII art (karakter)
HEIGHT = 54   # tinggi ASCII art (baris)

# Karakter ASCII dari gelap ke terang
CHARS = "@%#*+=-:. "

def center_crop_square(img):
    """Crop gambar menjadi persegi dari tengah."""
    w, h = img.size
    side = min(w, h)
    left = (w - side) // 2
    top = (h - side) // 2
    return img.crop((left, top, left + side, top + side))

def resize_image(img, width, height):
    """Resize gambar ke ukuran yang diinginkan."""
    return img.resize((width, height), Image.LANCZOS)

def image_to_ascii(img, width, height):
    """Konversi gambar menjadi ASCII art."""
    img = center_crop_square(img)  # crop persegi dulu
    img = resize_image(img, width, height)
    img = img.convert("L")  # grayscale
    pixels = list(img.getdata())
    
    lines = []
    for i in range(0, len(pixels), width):
        row = pixels[i:i+width]
        line = "".join(CHARS[min(int(p * len(CHARS) / 256), len(CHARS) - 1)] for p in row)
        lines.append(line)
    return lines

def main():
    img = Image.open(INPUT)
    print(f"Ukuran asli: {img.size}")
    
    lines = image_to_ascii(img, WIDTH, HEIGHT)
    
    Path(OUTPUT).write_text("\n".join(lines), encoding="utf-8")
    print(f"ASCII art disimpan ke {OUTPUT} ({len(lines)} baris x {WIDTH} kolom)")

if __name__ == "__main__":
    main()