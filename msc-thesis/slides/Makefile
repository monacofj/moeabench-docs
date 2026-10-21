TEX=main.tex
SRC=sections/phase2.tex sections/phase3a.tex $(wildcard sections/phase3b-*.tex) sections/phase4.tex sections/phase5.tex sections/phase6.tex theme/academic.tex
FIGURES=$(wildcard figures/*.pdf)

.PHONY: all defesa reduzida2 clean
all: presentation.pdf

presentation.pdf: $(TEX) $(SRC) $(FIGURES)
	latexmk -lualatex -interaction=nonstopmode -halt-on-error -jobname=presentation $(TEX)

defesa: presentation-defesa-30min.pdf

presentation-defesa-30min.pdf: presentation.pdf scripts/create_defense_cut.py
	python3 scripts/create_defense_cut.py

reduzida2: presentation-reduzida-2.pdf

presentation-reduzida-2.pdf: presentation.pdf scripts/create_reduzida_2.py
	python3 scripts/create_reduzida_2.py

clean:
	latexmk -C -jobname=presentation $(TEX)
