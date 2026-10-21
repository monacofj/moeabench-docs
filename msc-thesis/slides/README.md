# MoeaBench — apresentação de mestrado

Apresentação em LaTeX Beamer da dissertação de Fernando Ferreira da Silva (ICMC-USP).

## Estado atual

A **revisão parcial até a Fase 5** contém **94 slides**:

- Fase 2: Introdução e visão geral do MoeaBench.
- Fase 3: 14 exemplos convencionais, código, resultados e figuras vetoriais originais.
- Fase 4: fundamentos das seis métricas FAIR e dos Q-scores, com diagramas esquemáticos reproduzíveis em TikZ.
- Fase 5: exemplos clínicos da dissertação, com figuras PDF originais, e comparações externas de Q-scores extraídas do relatório de calibração v0.14.0.

**A Fase 6** (conclusões e verificação integral) ainda será desenvolvida. O PDF entregue agora não é a versão final de defesa.

## Compilação

Dentro de `msc-thesis/slides/`, execute:

```bash
make
```

Requer `latexmk`, `lualatex`, pacotes Beamer e `fontspec` e uma instalação da fonte **Noto Sans**. A apresentação usa Noto Sans deliberadamente porque Nunito não está instalada no ambiente de referência. O PDF compilado é `presentation.pdf`.

As figuras dos exemplos são PDFs vetoriais originais recuperados das fontes da monografia, não recortes de páginas. A compilação utiliza diretamente esses PDFs, sem depender de fragmentos Base64.

Os diagramas de FAIR foram desenhados especialmente para a apresentação e **não representam medições obtidas experimentalmente**. Excertos de código foram retirados dos exemplos existentes ou da documentação; a Fase 4 é uma exposição conceitual, não uma nova campanha de experimentos.

As comparações da Fase 5 referentes a DTLZ1, DTLZ2 e DPF1 utilizam o relatório histórico `calibration/audit_report.html` do MoeaBench v0.14.0. Foram redesenhadas como gráficos vetoriais próprios. Os protocolos possuem diferentes orçamentos de gerações e não são experimentos novos executados durante a criação dos slides.

## Estrutura e revisão

- `main.tex` inclui sequencialmente as seções aprovadas.
- `sections/phase4.tex` apresenta a fundamentação FAIR.
- `sections/phase5.tex` apresenta as evidências clínicas e as comparações do relatório histórico.
- `theme/academic.tex` concentra a tipografia e o estilo.
- `docs/phase4-review.md` documenta a fundamentação.
- `docs/phase5-review.md` documenta as fontes e as cautelas do relatório comparativo.
- `docs/phase3-completion.md` registra os exemplos da Fase 3.
- `sources/mb-uso/` e `sources/mb-fair/` guardam os trechos originais dos exemplos.

## Licenças

Licenças **planejadas** para publicação, ainda sujeitas a conferência dos direitos relativos às figuras e materiais da dissertação: fontes dos slides CC BY-SA 4.0; PDF final CC BY 4.0; scripts de construção GPL-3.0-or-later. Os termos do exemplar depositado na USP são independentes dos materiais desta apresentação.