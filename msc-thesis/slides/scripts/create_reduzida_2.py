#!/usr/bin/env python3
"""Export versão reduzida 2 from the approved 102-slide master presentation.

The ranges are 1-based and inclusive. No frames are merged, shortened or
reordered: only the chosen pages are copied. The page number in the lower-right
corner is renumbered for the new standalone PDF, as for the 30-minute cut.
"""
from pathlib import Path
import sys
import fitz

SLIDE_RANGES = [
    (1, 25), (26, 28), (34, 36), (40, 43), (46, 49),
    (56, 76), (77, 77), (80, 84), (95, 95), (96, 96),
    (99, 99), (101, 102),
]
SLIDES = [number for start, end in SLIDE_RANGES for number in range(start, end + 1)]
assert len(SLIDES) == 71 and len(set(SLIDES)) == 71


def main():
    base = Path(__file__).resolve().parents[1]
    original = Path(sys.argv[1]) if len(sys.argv) > 1 else base / "presentation.pdf"
    output = Path(sys.argv[2]) if len(sys.argv) > 2 else base / "presentation-reduzida-2.pdf"
    with fitz.open(original) as full:
        if len(full) != 102:
            raise RuntimeError(f"Expected the approved 102-slide master; got {len(full)} pages")
        with fitz.open() as reduced:
            for n in SLIDES:
                reduced.insert_pdf(full, from_page=n - 1, to_page=n - 1)
            for i, page in enumerate(reduced):
                # Replace only the source deck's footer page number.
                rect = fitz.Rect(page.rect.width-38, page.rect.height-17,
                                 page.rect.width-6, page.rect.height-1)
                page.draw_rect(rect, fill=(1,1,1), color=None, overlay=True)
                label = str(i + 1)
                width = fitz.get_text_length(label, fontname='helv', fontsize=7.2)
                page.insert_text((page.rect.width - 11 - width, page.rect.height - 7.2),
                                 label, fontsize=7.2, fontname='helv',
                                 color=(.25,.25,.25), overlay=True)
            reduced.set_metadata({
                'title': 'MoeaBench - apresentação reduzida 2 (71 slides)',
                'author': 'Fernando Ferreira da Silva',
                'subject': 'Seleção fiel de 71 slides da apresentação de 102 slides',
            })
            reduced.save(output, garbage=4, deflate=True)
    print(f"{output}: {len(SLIDES)} selected slides from 102; ranges: {SLIDE_RANGES}")


if __name__ == '__main__':
    main()
