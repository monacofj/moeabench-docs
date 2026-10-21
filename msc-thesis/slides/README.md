# MoeaBench — apresentação de mestrado

Apresentação em LaTeX Beamer da dissertação de Fernando Ferreira da Silva (ICMC-USP).

## Estado atual

A **revisão parcial até a Fase 4** contém **76 slides**:

- Fase 2: Introdução e visão geral do MoeaBench.
- Fase 3: 14 exemplos convencionais, código, resultados e figuras vetoriais originais.
- Fase 4: fundamentos das seis métricas FAIR e dos Q-scores, com diagramas esquemáticos reproduzíveis em TikZ.

**A Fase 5** (exemplos clínicos, comparações entre diagnósticos e radares reais) **e a Fase 6** (conclusões e verificação integral) ainda serão desenvolvidas. O PDF entregue agora não é a versão final de defesa.

## Compilação

Dentro de `msc-thesis/slides/`, execute:

```bash
make
```

Requer `latexmk`, `lualatex`, pacotes Beamer e `fontspec` e uma instalação da fonte **Noto Sans**. A apresentação usa Noto Sans deliberadamente porque Nunito não está instalada no ambiente de referência. O PDF compilado é `presentation.pdf`.

As figuras dos exemplos anteriores são PDFs vetoriais originais recuperados das fontes da monografia, não recortes de páginas. Alguns recursos trazem também arquivos `.pdf.b64` ou `.part*` para permitir sua restauração automática por `make`.

Os diagramas de FAIR foram desenhados especialmente para a apresentação e **não representam medições obtidas experimentalmente**. Excertos de código foram retirados dos exemplos existentes ou da documentação; a Fase 4 é uma exposição conceitual, não uma nova campanha de experimentos.

## Estrutura e revisão

- `main.tex` inclui sequencialmente as seções aprovadas.
- `sections/phase4.tex` é a nova seção de fundamentação FAIR.
- `theme/academic.tex` concentra a tipografia e o estilo.
- `docs/phase4-review.md` documenta escopo, escolhas didáticas e verificação.
- `docs/phase3-completion.md` registra os exemplos da Fase 3.
- `sources/mb-uso/` guarda os trechos originais usados na revisão dos exemplos convencionais.

## Licenças

Licenças **planejadas** para publicação, ainda sujeitas a conferência dos direitos relativos às figuras e materiais da dissertação: fontes dos slides CC BY-SA 4.0; PDF final CC BY 4.0; scripts de construção GPL-3.0-or-later. Os termos do exemplar depositado na USP são independentes dos materiais desta apresentação.