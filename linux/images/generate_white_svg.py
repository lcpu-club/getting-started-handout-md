#!/usr/bin/env python3
import re
from pathlib import Path


def process_svg(input_path, output_path):
    """
    Process an SVG file to make all elements white.
    """
    with open(input_path, "r", encoding="utf-8") as f:
        content = f.read()

    content = re.sub(r'fill="[^"]*"', 'fill="#ffffff"', content)
    content = re.sub(r'stroke="[^"]*"', 'stroke="#ffffff"', content)

    tags = ["path", "circle", "rect", "polygon", "polyline", "ellipse", "line", "g"]
    for tag in tags:

        def add_fill(match):
            full_match = match.group(0)
            if "fill=" in full_match:
                return full_match

            if full_match.endswith("/>"):
                return full_match[:-2] + ' fill="#ffffff"/>'
            elif full_match.endswith(">"):
                return full_match[:-1] + ' fill="#ffffff">'
            return full_match

        content = re.sub(f"<{tag}([^>]*)>", add_fill, content)
        content = re.sub(f"<{tag}([^>]*)/>", add_fill, content)

    with open(output_path, "w", encoding="utf-8") as f:
        f.write(content)


def main():
    script_dir = Path(__file__).parent
    images_dir = script_dir

    if not images_dir.exists():
        print(f"error: directory {images_dir} not found")
        return

    svg_files = list(images_dir.glob("*.svg"))
    # filter out names containing 'white' to avoid infinite recursion
    svg_files = [file for file in svg_files if "white" not in file.name]

    if not svg_files:
        print("no SVG files found")
        return

    print(f"found {len(svg_files)} SVG files")

    for svg_file in svg_files:
        output_file = svg_file.parent / f"{svg_file.stem}-white.svg"

        try:
            process_svg(svg_file, output_file)
            print(f"✓ processed: {svg_file.name} -> {output_file.name}")
        except Exception as e:
            print(f"✗ processing failed {svg_file.name}: {e}")


if __name__ == "__main__":
    main()
