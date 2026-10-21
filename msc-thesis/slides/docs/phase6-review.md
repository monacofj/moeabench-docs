# Fase 6 — Síntese, limites e revisão de defesa

## Base documental

- Monografia de Fernando Ferreira da Silva, capítulo 7, páginas 131–133 (PDF de defesa): contribuição principal, limitações e trabalhos futuros.
- Capítulos 5–6 e fontes LaTeX originais da dissertação para os exemplos e a separação entre métricas clássicas e FAIR.
- `calibration/audit_report.html` do MoeaBench v0.14.0, consultado separadamente na Fase 5; orçamentos distintos, sem alegação de superioridade sob orçamento idêntico.

## Conteúdo novo (slides 95–102)

1. Abertura da síntese conclusiva.
2. Contribuição: infraestrutura experimental, não um MOEA novo.
3. Evidências dos exemplos (comparações, variação, normalização, métricas FAIR).
4. Escopo e limitações da comparação: referência e protocolo explícitos.
5. Limite de engenharia: no CPython convencional, o GIL limita threads CPU-bound Python; subprocessos consomem memória; possível evolução por C/extensões nativas com considerações de portabilidade.
6. Limites metodológicos: GT finito, sensibilidade à densidade e à calibração, frentes especiais.
7. Estudos futuros: validação, calibração, incerteza e engenharia.
8. Mensagem final.

## Verificação realizada

- Compilação com LuaLaTeX/latexmk e fonte Noto Sans, em Beamer 16:9.
- PDF mestre com 102 slides; figuras originais dos exemplos em PDF vetorial; esquemas TikZ originais identificados como esquemáticos.
- Correções de layout também nos slides 38–39 e 90–93, identificados com texto próximo do rodapé.
- Versão curta de 42 páginas é apenas uma *seleção* da apresentação completa, com numeração local; ela não elimina slides, resultados ou exemplos dos fontes mestres.
- Verificar o ritmo de apresentação **com ensaio cronometrado**: 30 minutos é um objetivo, não uma duração garantida pela seleção.

## Ponto de atenção

- Na dissertação, a descrição do GIL se refere ao problema efetivamente observado no ambiente Python; não é uma afirmação de impossibilidade universal de paralelismo com código nativo ou implementações futuras.
- Os Q-scores são calibrados em cada problema/cardinalidade e não representam uma garantia universal de desempenho.
- Os gráficos da auditoria v0.14.0 derivam de protocolo externo distinto; não representam novas execuções da dissertação.
- O destino e as licenças das figuras devem ser conferidos antes de uma republicação irrestrita.
