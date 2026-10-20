TEX=main.tex
SRC=sections/phase2.tex theme/academic.tex
FIGURES=$(wildcard figures/*.pdf)

.PHONY: all clean
all: presentation.pdf
presentation.pdf: $(TEX) $(SRC) $(FIGURES)
	latexmk -lualatex -interaction=nonstopmode -halt-on-error -jobname=presentation $(TEX)
clean:
	latexmk -C -jobname=presentation $(TEX)
