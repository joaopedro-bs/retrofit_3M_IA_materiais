# Parecer Consolidado - Merge das Revisões Holísticas

Base mergeada:
- `claude_opus_4.8_v1_revisao_holistica_final.md`
- `gpt5_codex_v1_revisao_holistica_final.md`

Data: 2026-06-09

## Decisões de Merge e Conflitos

### Conflitos bloqueantes

Não há conflito bloqueante entre os dois pareceres. Ambos convergem nos pontos principais: o fio condutor está sólido, a contribuição central é preservável, e a revisão necessária é de calibragem acadêmica, não de reconstrução.

### Conflito resolvido: referências externas ao SLR

O parecer GPT apontou como risco a presença de referências externas ao catálogo da scoping review. Esse ponto fica resolvido pela decisão dos autores: as referências externas não são problema, pois funcionam como arcabouços teóricos necessários à construção do artigo/manografia. Portanto:

- manter referências externas como Costa, Prat, Stollenwerk, Jarrahi, Pan, Birkstedt, Orlikowski, Bender, Edmondson, Argyris, Foucault, AI Act, Ng e Dell'Acqua quando elas sustentarem arcabouços teóricos;
- não substituir mecanicamente essas referências por itens do catálogo;
- quando for útil para rastreabilidade metodológica, explicitar que a scoping review forneceu o corpus temático de evidências, enquanto arcabouços fundacionais complementares foram mobilizados para sustentação conceitual.

### Conflito resolvido: `mora2025model` vs. `S1A05`

O artigo de Mora-Mora et al. aparece no catálogo como `S1A05`, mas no LaTeX é citado como `mora2025model`. Não é obrigatório trocar a chave se `references.bib` já compila corretamente. A recomendação consolidada é apenas verificar se a entrada bibliográfica corresponde exatamente ao item `S1A05` do catálogo e, se conveniente, comentar no método que Mora-Mora et al. integra o corpus local.

### Atenção: candidatos de RAG/KG

O parecer Claude sugere `S9A09`; o parecer GPT sugere também `S4A05`, `S4A07`, `S9A06`, `S10A03` e `S10A05`. Para reduzir risco de ancoragem em metadado frágil, a prioridade consolidada para RAG/KG é:

1. `S4A05` - revisão sistemática sobre RAG/LLMs para Enterprise KM.
2. `S4A07` - aplicação de GenAI como sistema KG Q&A empresarial.
3. `S9A06` - Enterprise Knowledge Graphs para KM.
4. `S10A03` - survey/benchmarking de métodos de retrieval para enterprise RAG.

Use `S9A09` apenas se o PDF/ficha local confirmar aderência e qualidade suficiente.

### Decisão autoral: implementação técnica do SLR

Apesar da recomendação dos revisores para condensar ou mover a implementação técnica do `SLR-RAG Agentic Pipeline`, os autores decidiram manter essa seção como está por enquanto. A decisão final será discutida com as orientadoras: manter no corpo do artigo, derivar para apêndice, transformar em artigo separado ou outra solução. Portanto, nesta rodada, não editar a granularidade técnica da implementação do SLR. Apenas corrigir imprecisões factuais ou terminológicas que não reduzam o conteúdo técnico.

## Diagnóstico Consolidado

O artigo tem um golden thread forte:

1. UCs como dispositivos institucionais de Gestão do Conhecimento.
2. Modelo 3M clássico como arquitetura tripartite ancorada em Prat.
3. Limitação dos modelos de UC que tratam tecnologia como infraestrutura passiva.
4. IA generativa/agêntica como ruptura sociotécnica nos processos de GC.
5. Retrofit 3M 5.0: `Motive 5.0`, `Model 5.0`, `Moment 5.0`.
6. Transição SECI/GRAI e dupla ontologia da IA: ferramenta + agente.
7. Validação conceitual comparativa em cinco dimensões.
8. Discussão das implicações epistemológicas, trabalhistas, éticas e pedagógicas.

A arquitetura está madura. As correções necessárias são de precisão, redução de redundância, calibragem metodológica e secagem do estilo.

## Prioridades de Correção

### P0 - Integridade metodológica e factual

1. Corrigir a ambiguidade numérica da triagem em `metodologia.tex`: o texto atual fala em "114 entradas únicas e aprovadas", mas depois reduz para 93 aprovadas. A formulação correta é: 129 triados, 15 duplicados/NV, 114 entradas únicas, 21 inacessíveis, 93 artigos finais aprovados e baixados.

2. Remover a expressão "demonstra de forma empírica" em `metodologia.tex`, pois o estudo é conceitual-comparativo, sem validação empírica em organização real. Trocar por "sustenta, em nível comparativo" ou equivalente.

3. Explicitar melhor a escala `Ausente/Parcial/Pleno`: unidade de análise, critério de classificação e ressalva de que a classificação avalia cobertura conceitual, não efetividade empírica.

### P1 - Coesão global

4. Reduzir repetição do gap dos "19 modelos". Declarar plenamente na Introdução; reapresentar operacionalmente na Metodologia/Análise; nas demais seções usar remissão curta.

5. Ajustar o fechamento do Referencial para não antecipar a solução completa do 3M 5.0. O referencial deve fechar com lacuna/requisitos teóricos; a operacionalização dos loops deve ficar no Retrofit.

6. Melhorar a transição Análise -> Discussão, deixando claro que os pontos mais disruptivos são Agência Ativa de IA e Governança Algorítmica.

7. Ajustar a Conclusão para sintetizar contribuições e limites, sem abrir revisão normativa nova. Manter AI Act, AI literacy e impactos psicossociais se já estiverem preparados na Discussão; caso contrário, reduzir.

### P2 - Método e pipeline

8. Manter a subseção de pipeline com a granularidade técnica atual. Não condensar, não mover para apêndice e não remover menções a `httpx`, `playwright`, `pydantic`, NFKD, `pgvector`, hashes, Zotero/Obsidian ou controles de implementação nesta rodada.

9. Corrigir apenas o que for factual ou epistemologicamente necessário dentro da metodologia: números da triagem, distinção entre validação conceitual-comparativa e empírica, e eventual frase de escopo sobre corpus da scoping review versus arcabouços fundacionais externos.

### P3 - Estilo e AI-isms

10. Reduzir o padrão `não apenas ... mas ...` para no máximo duas ocorrências.

11. Variar ou eliminar aberturas como "No cenário contemporâneo", "Nesse contexto sociotécnico complexo", "É importante notar", "Em síntese", "reside em".

12. Trocar adjetivação intensificadora por precisão conceitual: "profunda", "radicalmente", "acelerado", "holística", "vivo e emergente", "substancial", "sofisticada", "inegociáveis".

13. Evitar autoelogio do próprio modelo: trocar "supera", "preenche de maneira abrangente", "resolução mais sofisticada" por formulações como "amplia a cobertura", "sustenta", "pode ser tratado".

## Ancoragens Teóricas Recomendadas

As referências abaixo são oportunidades de reforço a partir do catálogo local. Elas não substituem arcabouços externos fundacionais; servem para robustecer pontos atualmente monoancorados ou subancorados.

### Alta prioridade

- `E0A01` - reforçar o argumento de tecnologia passiva em modelos contemporâneos de Universidade Corporativa.
- `E0A20` - reforçar a evolução SECI sob GenAI e dialogar com GRAI.
- `S7A04` - reforçar governança de IA em contexto de HRM/digital HR, especialmente accountability em decisões de requalificação.
- `S6A03` - reforçar aprendizagem no trabalho mediada por IA, resultados, oportunidades e desafios.
- `S8A07` - reforçar o eixo deskilling/reskilling/upskilling sob GenAI.

### Média prioridade

- `S2A04` - ancorar trajetória e estrutura intelectual do campo de Corporate University.
- `E0A08` - complementar Jarrahi na simbiose humano-IA por teoria de knowledge augmentation.
- `E0A17` - ancorar abertura de IA e criação de conhecimento com revisão sistemática.
- `S6A08` - reforçar a ambivalência IA no trabalho: ganho e risco.
- `S4A05`, `S4A07`, `S9A06`, `S10A03` - reforçar RAG/KG no `Model 5.0`.
- `S7A10` - reforçar governança algorítmica e inovação responsável.

### Opcional

- `S1A09`, `S2A01`, `E0A03` - reforçar evolução da UC, capital intelectual, ambidestria e cenários de evolução.
- `S8A01`, `S8A02`, `S8A03`, `S8A09` - reforçar upskilling/reskilling no `Motive 5.0`.

## Diffs Consolidados Prioritários

### 1. Corrigir números da triagem

```diff
--- a/artigo final/sections/metodologia.tex
+++ b/artigo final/sections/metodologia.tex
@@
-O processo inicial catalogou 114 entradas únicas e aprovadas no banco de dados (sendo 25 provenientes da Etapa 0 de mapeamento de base e 89 resultantes da execução direta das equações de busca).
-Após a triagem, 21 artigos foram excluídos por inacessibilidade física permanente (barreiras de paywall intransponíveis), resultando em um catálogo final consolidado de \textbf{93 artigos únicos e aprovados} indexados localmente com PDF completo.
+Após a deduplicação de 15 registros, o processo consolidou 114 entradas únicas (25 provenientes da Etapa 0 de mapeamento de base e 89 resultantes da execução direta das equações de busca). Destas, 21 foram excluídas por inacessibilidade física permanente, resultando em um catálogo final de \textbf{93 artigos aprovados} indexados localmente com PDF completo.
```

### 2. Corrigir status da validação

```diff
--- a/artigo final/sections/metodologia.tex
+++ b/artigo final/sections/metodologia.tex
@@
-Essa validação conceitual-construtiva demonstra de forma empírica e qualitativa como o framework 3M 5.0 preenche de maneira abrangente os gaps identificados, diferenciando-se dos 19 modelos históricos consolidados na literatura acadêmica.
+Essa validação conceitual-construtiva sustenta, em nível comparativo, que o Modelo 3M 5.0 cobre dimensões pouco desenvolvidas nos 19 modelos examinados, especialmente agência ativa de IA, simbiose humano-IA, ciclo dinâmico de GC, governança algorítmica e aprendizagem no fluxo de trabalho.
```

### 3. Manter a implementação técnica do pipeline nesta rodada

Não aplicar os diffs anteriores que condensavam a subseção do `SLR-RAG Agentic Pipeline`. A seção deve permanecer tecnicamente detalhada até decisão das orientadoras. O redator pode apenas ajustar frases pontuais se houver erro factual, imprecisão epistemológica ou problema de compilação.

### 4. Reduzir abertura genérica da Introdução

```diff
--- a/artigo final/sections/introducao.tex
+++ b/artigo final/sections/introducao.tex
@@
-No cenário contemporâneo da economia baseada no conhecimento, a vantagem competitiva sustentável das organizações reside na sua capacidade de criar, disseminar, aplicar e proteger seus ativos intelectuais.
+Em organizações intensivas em conhecimento, a vantagem competitiva depende da capacidade de criar, disseminar, aplicar e proteger ativos intelectuais.
```

### 5. Reduzir dramatização da ruptura tecnológica

```diff
--- a/artigo final/sections/introducao.tex
+++ b/artigo final/sections/introducao.tex
@@
-Embora o Modelo 3M mantenha sua vitalidade conceitual e lógica interna, a infraestrutura sociotécnica que sustenta a aprendizagem nas organizações mudou radicalmente nos últimos anos.
+Embora o Modelo 3M mantenha coerência interna, seus pressupostos tecnológicos foram formulados em um regime de tecnologia informacional passiva.
```

### 6. Não antecipar a solução no Referencial

```diff
--- a/artigo final/sections/referencial.tex
+++ b/artigo final/sections/referencial.tex
@@
-A governança de IA, portanto, se consolida como um processo dinâmico de Gestão do Conhecimento corporativo: as diretrizes éticas e técnicas do Moment 5.0 orientam a operação segura do Model 5.0, enquanto os aprendizados e desvios comportamentais detectados pelos loops de monitoramento em tempo real realimentam e reconfiguram as diretrizes de sensing de competências do Motive 5.0. Centralizar essa governança e capacitação na Universidade Corporativa assegura que a mitigação de riscos esteja intrinsecamente ligada à capacitação humana contínua e ao desenvolvimento organizacional sustentável.
+A governança de IA configura-se, assim, como um requisito teórico ainda pouco desenvolvido nos modelos de UC: uma função de aprendizagem organizacional, e não apenas de conformidade técnica. A operacionalização desse requisito nos pilares do Modelo 3M 5.0 é formulada na Seção \ref{sec:retrofit}.
```

### 7. Secar abertura do Retrofit

```diff
--- a/artigo final/sections/retrofit.tex
+++ b/artigo final/sections/retrofit.tex
@@
-Sob este novo paradigma, a UC deixa de ser vista como uma estrutura estática de alinhamento estratégico e operacional para se consolidar como um ecossistema sociotécnico vivo e emergente.
+Nesse arranjo, a UC deixa de operar apenas como estrutura de alinhamento estratégico e passa a coordenar interações recorrentes entre humanos, agentes de IA, processos de negócio e mecanismos de governança.
```

### 8. Explicitar cautela da escala comparativa

```diff
--- a/artigo final/sections/analise.tex
+++ b/artigo final/sections/analise.tex
@@
-A escala adotada qualifica a cobertura de cada dimensão como \textit{Ausente} (inexistência de modelagem), \textit{Parcial} (presença periférica ou reativa) ou \textit{Pleno} (elemento central e dinâmico de modelagem).
+A escala adotada qualifica a cobertura de cada dimensão como \textit{Ausente} (inexistência de modelagem), \textit{Parcial} (presença periférica ou reativa) ou \textit{Pleno} (elemento central de modelagem). A classificação avalia a presença explícita da dimensão na arquitetura conceitual dos modelos, não sua efetividade empírica em contextos organizacionais.
```

### 9. Ajustar transição Análise -> Discussão

```diff
--- a/artigo final/sections/analise.tex
+++ b/artigo final/sections/analise.tex
@@
-Os impactos teóricos e as implicações práticas dessa nova configuração sociotécnica são detalhados e discutidos na seção a seguir.
+Os pontos de cobertura plena exclusivos do 3M 5.0, especialmente Agência Ativa de IA e Governança Algorítmica, concentram as implicações teóricas e práticas discutidas na Seção \ref{sec:discussao}.
```

### 10. Remover autoelogio na Discussão

```diff
--- a/artigo final/sections/discussao.tex
+++ b/artigo final/sections/discussao.tex
@@
-O dilema sobre os limites da autonomia decisória da IA versus a supervisão humana estrita, enunciado em §\ref{subsec:tensoes_desafios}, encontra sua resolução mais sofisticada no plano pedagógico da governança algorítmica.
+O dilema sobre os limites da autonomia decisória da IA versus a supervisão humana estrita, enunciado em §\ref{subsec:tensoes_desafios}, pode ser tratado no plano pedagógico da governança algorítmica.
```

### 11. Ajustar a Conclusão

```diff
--- a/artigo final/sections/conclusao.tex
+++ b/artigo final/sections/conclusao.tex
@@
-práticas organizacionais inegociáveis como anonimização de dados informais, consentimento prévio e voluntário (\textit{opt-in}) e a estrita separação das análises pedagógicas de quaisquer avaliações punitivas
+práticas organizacionais recomendáveis, como anonimização de dados informais, consentimento voluntário (\textit{opt-in}) e separação entre análises pedagógicas e avaliações punitivas
```

## Resultado Esperado

Após a revisão, o artigo deve:

- preservar a arquitetura 3M 5.0 e a dupla perspectiva da IA;
- ficar menos repetitivo na apresentação do gap;
- preservar a descrição técnica do pipeline SLR-RAG até decisão autoral/orientadoras sobre corpo do texto, apêndice ou artigo separado;
- manter referências externas fundacionais sem constrangimento artificial ao SLR;
- reforçar pontos monoancorados com 4 a 8 novas referências do catálogo;
- soar mais acadêmico, seco e preciso.
