#!/usr/bin/env python3
"""Build an optional 30-minute speaking route through the complete Beamer PDF.

Original frame numbers refer to the approved master deck. This export does not
change or remove a slide from the full presentation. The 42-page subset has its
own page numbers for projection. The selection is didactic, not an empirical claim.
"""
from pathlib import Path
import sys
import fitz

SLIDES = [
    1,3,5,8,                       # Intro 4
    9,10,12,17,18,19,20,           # MoeaBench 7
    26,27,28,29,36,40,43,48,49,   # Examples 9
    56,57,59,62,63,64,66,68,69,70,72,73,  # FAIR 12
    77,82,83,84,91,                # Diagnostics 5
    95,96,97,99,102,               # Conclusion 5
]

def main():
    base = Path(__file__).resolve().parents[1]
    original = Path(sys.argv[1]) if len(sys.argv)>1 else base / 'presentation.pdf'
    output = Path(sys.argv[2]) if len(sys.argv)>2 else base / 'presentation-defesa-30min.pdf'
    full = fitz.open(original)
    assert len(full) >= max(SLIDES), f'Incomplete master PDF: {len(full)} pages'
    selected = fitz.open()
    for index in SLIDES:
        selected.insert_pdf(full, from_page=index-1, to_page=index-1)
    # Cover only the original frame-number area, never the body content.
    for i, page in enumerate(selected):
        rect = fitz.Rect(page.rect.width-38, page.rect.height-17,
                         page.rect.width-6, page.rect.height-1)
        page.draw_rect(rect, fill=(1,1,1), color=None, overlay=True)
        label = str(i+1)
        w = fitz.get_text_length(label, fontname='helv', fontsize=7.2)
        page.insert_text((page.rect.width-11-w,page.rect.height-7.2),
                         label, fontsize=7.2, fontname='helv', color=(.25,.25,.25), overlay=True)
    selected.set_metadata({
        'title':'MoeaBench - selecao de slides para defesa (aprox. 30 min)',
        'author':'Fernando Ferreira da Silva',
        'subject':'Versao curta opcional; original com todos os exemplos preservado',
    })
    selected.save(output, garbage=4, deflate=True)
    print(f'{output}: {len(selected)} pages, selected from {len(full)}-page complete deck')

if __name__=='__main__':
    main()
