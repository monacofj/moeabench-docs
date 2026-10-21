# Fase 4 — fundamentos FAIR: registro de revisão

## Escopo

Revisão conceitual do capítulo 6 da dissertação, com a seguinte ordem:

1. Motivação: distintas propriedades estruturais da frente aproximada; indicadores agregados não bastam para diagnosticá-las.
2. Distinção entre aproximação P, referência discreta R e a resolução finita K.
3. Conjunto Uniform-at-K, FPS e espaçamento característico s_K.
4. Seis métricas físicas, com pergunta científica, formulação, exemplo esquemático e contraste com métricas relacionadas.
5. Calibração dependente de MOP, tamanho da frente e distribuição da referência; padrões favorável e desfavorável.
6. Q-scores de 0 a 1, modelos de transformação diferentes e interpretação por dimensão.

Fontes principais: monografia de defesa, capítulo 6, seções 6.0.1–6.0.4, equações (6.1)–(6.9), e documentação pública de moeabench. As definições das seis métricas foram conferidas contra o texto do capítulo 6.

## Esclarecimentos científicos importantes

- `P → R` é a direção de closeness; `R → P`, a de coverage e gap. São erros geométricos direcionais distintos.
- `epsilon_ideal` corrige o resíduo de discretização conforme o protocolo; não é um limite manual selecionado depois de observar o MOEA.
- Coverage depende da distribuição espacial do conjunto de referência e não deve ser descrita como invariável à sua discretização.
- Gap usa o percentil 95 de R → P, distinto da média usada por coverage.
- Regularity compara distribuições de distâncias ao vizinho mais próximo com o conjunto uniforme U_K.
- Balance compara histogramas regionais de ocupação; não equivale à regularidade de vizinhança.
- Headway é a razão entre erros longitudinais no percentil 95. Uma população inicial já próxima do GT pode ser favorecida pela sorte e produzir uma razão menos impressionante mesmo com bom resultado final.
- Medidas físicas menores são melhores. Q-scores maiores são melhores; 0,8 em coverage não representa 80% de cobertura da frente.
- Um radar com Q-scores deve ser comentado por contraste entre suas dimensões, evitando uma conclusão única de 'bom/ruim' ou média sem significado definido.

## Execução técnica

- 76 slides no PDF parcial; acrescentados 21 slides FAIR às 55 páginas anteriores.
- Tipografia Noto Sans (fontspec + LuaLaTeX), porque Nunito não está disponível no ambiente de compilação.
- Diagramas FAIR vetoriais feitos em TikZ; não são gráficos de experimentos.
- `make` foi executado e o PDF compilado. Os novos slides foram renderizados e examinados visualmente.
- Persistem avisos tipográficos *pequenos* na Fase 4 (inferiores a 3 pt) e avisos prévios nas Fases 2 e 3; não se observa corte substancial dos novos diagramas após a revisão de layout.
- O relatório de calibração `calibration/audit_report.html` representa a v0.14.0 e será usado somente na Fase 5, claramente separado do protocolo da dissertação.

## Fora do escopo

Os exemplos clínicos reais com seus códigos, radar, ECDF, densidades e histórico pertencem à Fase 5. A Fase 4 inclui apenas um perfil *ilustrativo* explicitamente marcado, para ensinar sua leitura.