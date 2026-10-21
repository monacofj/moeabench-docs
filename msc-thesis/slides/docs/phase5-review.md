# Fase 5 — exemplos FAIR e comparações

Fontes originais: mb-fair/secoes/exemplo_11.tex, exemplo_12.tex, exemplo_13.tex, exemplo_14.tex e exemplo_18.tex; figuras PDF vetoriais originais de mb-fair/figuras. A seção 6.0.6.5 não corresponde às figuras do apêndice.

Comparações externas: calibration/audit_report.html no repositório monacofj/moeabench, rotulado na página como **v0.14.0**. Os gráficos de comparação `audit_*_qscores.pdf` são novos gráficos vetoriais gerados a partir dos valores numéricos do relatório, não figuras da dissertação. Os Q-scores são valores do relatório, não de execução local atual.

O relatório informa 30 execuções independentes e diferentes quantidades de gerações por algoritmo. Portanto, a leitura é descritiva das diferenças clínicas do protocolo, **não** uma comparação de desempenho sob orçamento idêntico. Os gráficos DTLZ1/DTLZ2/DPF1 mantêm todos os seis eixos da matriz, mapeando a dimensão chamada `CONTINUITY` no relatório para a legenda `Gap / continuidade`; verificar terminologia na eventual atualização do relatório.

Exemplo 11: DPF1/NSGA-III 18 ND e 74 dominadas; DPF2/MOEA-D 90 ND e 2 dominadas. GT distinto entre os dois problemas.

Exemplo 12: medidas físicas explicitamente rotuladas e não confundidas com Q-scores.

Exemplo 13: DTLZ1 Q-scores 0.883,0,0,0,0,0.999 (monografia) e gráfico original.

Exemplo 14: radar, duas ECDFs, duas distribuições e dois históricos de uma mesma execução DTLZ2.

Exemplo 18: código 6.6 de calibração sidecar em DTLZ2 M=4 (sem imagens do apêndice).

Todos os textos de leitura dos resultados são inferências descritivas ancoradas nas figuras e nos números; nenhuma figura genérica foi atribuída a dados experimentais.
