from pathlib import Path

def read_ascii_art():
    """Baca portrait.txt dan konversi menjadi tspan SVG."""
    lines = Path("portrait.txt").read_text(encoding="utf-8").splitlines()
    
    # Konfigurasi posisi (sama dengan aslinya)
    START_X = 30
    START_Y = 79.98
    LINE_HEIGHT = 7.55
    
    tspans = []
    y = START_Y
    for line in lines:
        tspans.append(f'<tspan x="{START_X}" y="{y:.2f}" xml:space="preserve">{line}</tspan>')
        y += LINE_HEIGHT
    
    return "\n".join(tspans)

def update_svg(svg_path, new_ascii):
    """Ganti bagian ASCII art di file SVG."""
    content = Path(svg_path).read_text(encoding="utf-8")
    
    # Cari awal dan akhir bagian ASCII art
    start_marker = '<text x="30" y="0" class="ascii">'
    end_marker = '</text>'
    
    start_idx = content.find(start_marker)
    if start_idx == -1:
        print(f"ERROR: Tidak menemukan marker awal di {svg_path}")
        return False
    
    # Cari akhir dari bagian ascii (setelah start_marker, cari </text> pertama)
    end_idx = content.find(end_marker, start_idx)
    if end_idx == -1:
        print(f"ERROR: Tidak menemukan marker akhir di {svg_path}")
        return False
    
    # Ganti bagian ascii
    new_content = (
        content[:start_idx] +
        start_marker + "\n  \n" + new_ascii + "\n\n  " +
        content[end_idx:]
    )
    
    Path(svg_path).write_text(new_content, encoding="utf-8")
    print(f"Berhasil memperbarui {svg_path}")
    return True

def main():
    new_ascii = read_ascii_art()
    print(f"ASCII art: {len(new_ascii.splitlines())} baris")
    
    update_svg("light.svg", new_ascii)
    update_svg("dark.svg", new_ascii)

if __name__ == "__main__":
    main()