# MoeaBench — apresentação de mestrado

Apresentação em LaTeX Beamer da dissertação de Fernando Ferreira da Silva (ICMC-USP).

## Estado atual

A **Fase 6** concluiu a apresentação completa com **102 slides**. A versão integral inclui todos os 14 exemplos convencionais, os exemplos FAIR, os contrastes do relatório v0.14.0, a síntese conclusiva, as limitações e os trabalhos futuros.

Há também uma **seleção opcional de 42 slides** para apoiar uma defesa de aproximadamente 30 minutos; nenhum exemplo foi removido da versão completa. Esta seleção é uma proposta de roteiro, sujeita a ensaio cronometrado. Consulte `docs/roteiro-defesa-30min.md`.

## Compilação

Dentro de `msc-thesis/slides/`, execute:

```bash
make
```

Requer `latexmk`, `lualatex`, pacotes Beamer e `fontspec` e uma instalação da fonte **Noto Sans**. A apresentação usa Noto Sans deliberadamente porque Nunito não está instalada no ambiente de referência. O PDF integral compilado é `presentation.pdf`. A seleção curta é gerada com `make defesa` em `presentation-defesa-30min.pdf`; esse segundo alvo requer Python 3 e PyMuPDF (`fitz`).

As figuras dos exemplos são PDFs vetoriais originais recuperados das fontes da monografia, não recortes de páginas. A compilação utiliza diretamente esses PDFs, sem depender de fragmentos Base64.

Os diagramas de FAIR foram desenhados especialmente para a apresentação e **não representam medições obtidas experimentalmente**. Excertos de código foram retirados dos exemplos existentes ou da documentação; a Fase 4 é uma exposição conceitual, não uma nova campanha de experimentos.

As comparações da Fase 5 referentes a DTLZ1, DTLZ2 e DPF1 utilizam o relatório histórico `calibration/audit_report.html` do MoeaBench v0.14.0. Foram redesenhadas como gráficos vetoriais próprios. Os protocolos possuem diferentes orçamentos de gerações e não são experimentos novos executados durante a criação dos slides.

## Estrutura e revisão

- `main.tex` inclui sequencialmente as seções aprovadas.
- `sections/phase4.tex` apresenta a fundamentação FAIR.
- `sections/phase5.tex` apresenta as evidências clínicas e as comparações do relatório histórico.
- `sections/phase6.tex` reúne contribuições, limitações e trabalhos futuros do capítulo 7 da dissertação.
- `scripts/create_defense_cut.py` extrai a versão curta sem alterar o PDF integral.
- `docs/phase6-review.md` registra a revisão da síntese e os critérios de verificação.
- `docs/roteiro-defesa-30min.md` registra a seleção e a distribuição de tempo.
- `theme/academic.tex` concentra a tipografia e o estilo.
- `docs/phase4-review.md` documenta a fundamentação.
- `docs/phase5-review.md` documenta as fontes e as cautelas do relatório comparativo.
- `docs/phase3-completion.md` registra os exemplos da Fase 3.
- `sources/mb-uso/` e `sources/mb-fair/` guardam os trechos originais dos exemplos.

## Licenças

Licenças **planejadas** para publicação, ainda sujeitas a conferência dos direitos relativos às figuras e materiais da dissertação: fontes dos slides CC BY-SA 4.0; PDF final CC BY 4.0; scripts de construção GPL-3.0-or-later. Os termos do exemplar depositado na USP são independentes dos materiais desta apresentação.
