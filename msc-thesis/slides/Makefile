TEX=main.tex
SRC=sections/phase2.tex sections/phase3a.tex $(wildcard sections/phase3b-*.tex) sections/phase4.tex theme/academic.tex
FIGURES=$(wildcard figures/*.pdf)
ENCODED=$(wildcard figures/*.pdf.b64)
RESTORED=$(patsubst %.b64,%,$(ENCODED)) figures/example_04_05_topology.pdf

.PHONY: all clean
all: presentation.pdf

figures/%.pdf: figures/%.pdf.b64
	base64 --decode $< > $@

figures/example_04_05_topology.pdf: figures/example_04_05_topology.pdf.b64.part1 figures/example_04_05_topology.pdf.b64.part2
	cat $^ | base64 --decode > $@

presentation.pdf: $(TEX) $(SRC) $(FIGURES) $(RESTORED)
	latexmk -lualatex -interaction=nonstopmode -halt-on-error -jobname=presentation $(TEX)

clean:
	latexmk -C -jobname=presentation $(TEX)