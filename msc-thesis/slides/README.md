# Apresentação de mestrado — MoeaBench

Apresentação em LaTeX Beamer da dissertação de Fernando Ferreira da Silva, ICMC-USP.

## Estado

A versão parcial compilável contém **33 slides**: 25 da Introdução e Visão Geral (Fase 2) e oito do primeiro lote de exemplos convencionais (Fase 3A, incluindo o divisório). Os exemplos 5–14, as métricas FAIR e a conclusão serão trabalhados em fases posteriores.

## Compilação

Execute `make` dentro de `msc-thesis/slides`, com LuaLaTeX e latexmk. O resultado é `presentation.pdf`. O tema utiliza Nunito quando disponível e Noto Sans como alternativa.

As figuras são os PDFs vetoriais originais de `mb-uso/figuras/`, nunca recortes de páginas. Alguns arquivos estão armazenados como `.pdf.b64` e outros em partes devido a limitações de transferência; o `Makefile` restaura os PDFs originais automaticamente. Na compilação, os bytes reconstituídos foram conferidos com os arquivos originais.

## Proveniência e revisão

Os quatro exemplos iniciais seguem `mb-uso/secoes/exemplo_01.tex` a `exemplo_04.tex` (capítulo 5 da monografia). Seus resultados foram transcritos dos fontes, sem novas execuções dos algoritmos.

Consulte `docs/phase-3a-review.md` e `docs/review-issues.md` para a correspondência dos resultados e pendências.

## Licenças

Planejamento: fontes da apresentação CC BY-SA 4.0; PDF final CC BY 4.0; scripts GPL-3.0-or-later. A autorização de reutilização das figuras acadêmicas deve ser verificada separadamente. O licenciamento da dissertação depositada na USP é independente deste projeto.
