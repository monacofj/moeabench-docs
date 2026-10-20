# Fase 3 — lote A: exemplos 1 a 4 (capítulo 5)

Versão parcial pronta para revisão do orientador. A apresentação contém 25 slides das seções introdutórias e oito novos slides: um divisório e sete slides expositivos. A seção III será concluída em lotes posteriores, respeitando a ordem do capítulo 5.

| Exemplo | Seção | Configuração | Números e observação da monografia | Gráficos originais |
|---|---|---|---|---|
| 1: aproximação | 5.1 | DTLZ2 M=3; NSGA-III pop.50, 50 gerações | 50 ND ao final; HV 0,011207 → 0,713990 | example_01_01_topology.pdf; example_01_02_history.pdf |
| 2: dois algoritmos | 5.2 | DTLZ2 M=3; NSGA-III × SPEA2, pop.50, 50 gerações | HV 0,759872 × 0,756493; SPEA2 avançou mais rapidamente durante parte da busca | example_02_01_topology.pdf; example_02_02_history.pdf |
| 3: dominância e tempo | 5.3 | DTLZ2 M=3; NSGA-III pop.100, 100 gerações | 100 ND/0 dominadas ao final; frente de índice 5 mais afastada da referência | example_03_02_topology.pdf |
| 4: estabilidade | 5.4 | NSGA-III; cinco execuções | HV final médio 0,786496 ± 0,003830; 250 pontos reunidos e 185 ND globalmente | example_04_01_history.pdf; example_04_05_topology.pdf |

Os resultados citados foram transcritos dos arquivos `mb-uso/secoes/exemplo_01.tex` a `exemplo_04.tex`, sem reexecutar os algoritmos. Os trechos de código e as figuras correspondem à monografia. No Exemplo 2, `exp1` e `exp2` são pré-configurados e a figura provém da execução descrita na monografia.

## Critérios aplicados
- Cada exemplo apresenta configuração, código, gráfico e interpretação concreta.
- Figuras originais do acervo da dissertação; nenhuma extração de página.
- Conferência visual do PDF para eliminar conteúdo cortado.
- Compilação por `make`, utilizando LuaLaTeX.
- Parte dos PDFs vetoriais está temporariamente armazenada em representação base64 para transferência pelo conector GitHub; o `Makefile` reconstitui os arquivos bit a bit antes da compilação. Não são imagens substituídas.

## Pendências
- Lotes seguintes: exemplos 5–14 do capítulo 5.
- Revisão científica final da API e eventual reexecução de código em ambiente MoeaBench com versão controlada.
- Automatização de compilação no GitHub Actions depois de consolidar o conteúdo.
