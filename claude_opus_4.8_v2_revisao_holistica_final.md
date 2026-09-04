# Parecer de Revisão Final Holística — Segunda Passagem (Polimento Absoluto)
## "Retrofit do Modelo 3M de Universidade Corporativa (3M 5.0) com IA Generativa"

**Revisor:** Claude Opus 4.8 (Revisor Acadêmico Sênior — padrão periódico Q1, Sistemas de Informação / Gestão do Conhecimento)
**Data:** 09/06/2026
**Insumos:** versão atual de `main.tex` + 7 seções; `references.bib`; Catálogo da Scoping Review (`catalogo_artigos.csv`).
**Nota de continuidade:** Confirmei que a v1 foi absorvida — E0A01 entrou na Introdução, E0A20/S6A03/S8A07/S7A04 foram incorporados, a imprecisão numérica da triagem foi corrigida (Metodologia l. 55), o fechamento do Referencial foi reescrito (l. 91) e a redundância do gap foi atenuada. O texto subiu de patamar. Esta passagem é cirúrgica: aponta apenas o que ainda separa o manuscrito de um "submit-ready" Q1.

---

## 1. Diagnóstico do Teste de Estresse

**Veredito:** o artigo já se sustenta como um paper Q1 *forte em construção teórica*. O fio condutor resiste ao teste de estresse — a promessa da Introdução (RQ + 4 objetivos) é rastreável até a Conclusão, sem saltos: objetivo 1 (retrofit dos três pilares) → §IV; objetivo 2 (mapeamento Prat/Stollenwerk) → §IV e §V.3; objetivo 3 (governança no Moment 5.0) → §IV.3 e §VI.4; objetivo 4 (validação vs. 19 modelos) → §V. A cadeia lacuna → método → GRAI → governança → conclusão está logicamente fechada.

Há, contudo, **três elos residuais** que um parecerista Q1 atacará. Listo em ordem decrescente de risco de *desk reject* ou pedido de major revision.

### Elo mais fraco (risco real de revisão maior): a circularidade da "validação"
A Seção V apresenta-se como "validação", mas opera como **autoavaliação**: os autores comparam o 3M 5.0 contra uma coluna agregada "Modelos Tradicionais de UC" e atribuem a si próprios "Pleno" nas cinco dimensões, enquanto o agregado recebe "Ausente/Parcial". Nenhum dos 19 modelos é individualmente nomeado ou confrontado, e a escala ordinal (Ausente/Parcial/Pleno) é aplicada pelos próprios proponentes, sem segundo avaliador nem critério de codificação reproduzível. As salvaguardas já inseridas (Análise l. 6 — "avalia a presença explícita… não sua efetividade empírica"; Metodologia l. 113 — claim suavizado) **mitigam, mas não eliminam** a circularidade. Recomendação mínima para blindar o argumento: (i) rebatizar a Seção V de "Validação" para **"Análise Comparativa de Cobertura Conceitual"** (já é o título — então ajustar a *linguagem interna* que insiste em "validar/validação", ver §3); (ii) nomear explicitamente ao menos 2–3 dos 19 modelos de Mora-Mora et al. como exemplos concretos na coluna "Tradicionais", ancorando a nota "Ausente" em casos reais, não em um agregado abstrato. Isso converte uma autoavaliação em uma comparação defensável.

### Segundo elo: o descompasso entre o aparato metodológico e seu uso
A scoping review SLR-RAG produz **93 artigos**, mas a construção do modelo usa **20** ("curadoria fina… 20 referências", Metodologia l. 57), e o texto final ancora-se em ~6 teorias-núcleo. O leitor Q1 perguntará: *por que um pipeline com defesa contra prompt injection em três camadas e `pgvector` para sustentar um artigo conceitual de 20 fontes?* O elo 93 → 20 → modelo nunca é demonstrado (não há critério explícito de como as 20 emergiram das 93). Não é um defeito fatal, mas é o ponto onde método e contribuição se desalinham. Sugestão: uma frase em §III.2 explicitando o critério de curadoria das 20 (ex.: centralidade de citação + aderência às lentes teóricas) fecha a lacuna. O detalhamento de engenharia, ainda denso, segue desproporcional ao registro conceitual — reitero a recomendação v1 de remeter `httpx`/`playwright`/`magic bytes` a um apêndice.

### Terceiro elo: a ausência de uma figura do próprio 3M 5.0
O artigo propõe um *framework* e **não o desenha**. A única figura (Fig. 1) é um **placeholder** (`\framebox{...}`, Referencial l. 18) — bloqueador absoluto de submissão — e representa apenas o 3M *original*. Um paper de modelagem conceitual que apresenta seu artefato somente em prosa e tabelas perde força. Recomendo (a) substituir o placeholder por uma figura real do 3M original e (b) **adicionar um diagrama esquemático do 3M 5.0** (os três pilares × dupla perspectiva IA + loops de governança Moment→Model→Motive), que hoje só existe verbalmente em Retrofit l. 71. Este é o maior retorno visual/argumentativo disponível.

Resolvidos esses três pontos, o manuscrito passa de "forte em construção" para "competitivo para aceitação".

---

## 2. Achados de Precisão e Ancoragem (validação cruzada de referências)

### 2.1 Citação forçada / misattribuição — corrigir (prioridade alta)
> **Referencial, l. 40:** "…eles propõem a transição para o modelo GRAI \cite{E0A20}:"

O modelo **GRAI é de Böhm & Durst (E0A18)**. O artigo **E0A20** propõe o *GenAI-SECI Model* — um modelo **distinto**. Atrelar `\cite{E0A20}` diretamente ao nome "GRAI" cria uma **atribuição incorreta**: sugere que E0A20 é fonte do GRAI, quando é uma proposta paralela. A citação (sugerida na v1) é válida, mas está **mal ancorada**. Correção no diff §4.1: citar E0A20 como proposta *concorrente/corroborante* de revisão do SECI, não como origem do GRAI.

### 2.2 Citações "nuas" recém-inseridas (integração orgânica)
As inserções da v1 estão tematicamente corretas, mas três entraram como citação terminal solta, sem ancoragem autoral, o que destoa do padrão do texto (que tipicamente nomeia o autor):
- **Introdução l. 8** — `…infraestrutura de TI \cite{E0A01}.` → integrar: "…infraestrutura de TI, padrão também documentado por estudos sobre o uso de tecnologias em modelos contemporâneos de UC \cite{E0A01}."
- **Retrofit l. 15** — `…loops rápidos de adaptação \cite{S8A07}.` (aceitável; monitorar).
- **Retrofit l. 37** — `…a governança se torna pedagógica \cite{S7A04}.` → idealmente nomear o caráter human-centric/HRM da fonte.

Nenhuma é erro; são pontos de polimento de fluência da citação.

### 2.3 Lacunas residuais e cobertura do catálogo
A ancoragem está, no geral, saturada. Não há lacuna teórica que **exija** nova citação. Caso os autores queiram reforçar o **Elo 2** (validação comparativa concreta), o catálogo ainda oferece, **sem alucinação**, modelos individuais de UC não usados que poderiam ser nomeados como casos da coluna "Tradicionais": **S1A04** (*Proposed model of corporate university*, 2019), **S1A09** (*knowledge network-based intellectual capital in the corporate university*, 2023), **S1A10** (*Path of corporate university to enable enterprises*, 2023) e **S2A04** (*Mapping the themes and intellectual structure of corporate university*, 2019). São exemplares concretos da literatura de modelos de UC com tecnologia passiva — úteis exatamente para aterrar as notas "Ausente" da Tabela 2. Uso **opcional**, estritamente a serviço de quebrar a circularidade.

> Observação de integridade: **Meister** (Referencial l. 8) permanece sem citação e **não tem entrada no catálogo** — se citado diretamente, exige fonte externa. Mantido o aviso da v1.

---

## 3. Refinamentos Cirúrgicos de Tom

Resíduos de escrita robótica e oportunidades de elevação lexical. Densidade ainda alta de `de forma <adj>` (**31 ocorrências**) — é o tique dominante remanescente; recomenda-se varrer e substituir ~1/3 por advérbios sintéticos ("autonomamente", "continuamente", "dinamicamente") ou supressão.

| Local | Trecho atual | Substituição sugerida |
|---|---|---|
| Referencial l. 71 | "constitui o núcleo da **adição teórica sugerida pelo Prof. Jano Moreira de Souza** ao Modelo 3M 5.0." | **Remover a atribuição nominal.** Reescrever: "constitui o núcleo da reinterpretação ontológica proposta no Modelo 3M 5.0." Ver §4.2 — é também questão de anonimato. |
| Retrofit l. 71 | "**É importante notar a** interdependência entre essas tensões:" | "As tensões são interdependentes:" |
| Retrofit l. 4 | "**Longe de sugerir** uma ruptura ou abandono das bases consolidadas…" | "Sem romper as bases consolidadas de aprendizagem organizacional, a reconfiguração propõe…" |
| Introdução l. 26 | "preservando sua **vitalidade conceitual**" | "preservando sua consistência interna" (a expressão "vitalidade conceitual" reaparece; variar). |
| Referencial l. 81 | "riscos corporativos **de elevada gravidade**." | "riscos corporativos críticos." |
| Análise l. 35 | "permite que a UC **opere não apenas na distribuição, mas na cogeração** ativa de valor" | "permite que a UC migre da distribuição para a cogeração ativa de valor organizacional." |
| Análise l. 65 | "o framework proposto **não apenas preenche** o gap…, **mas define** uma nova base" | "o framework preenche o gap identificado e estabelece uma nova base para a evolução das capacidades dinâmicas." |
| Metodologia/Análise (passim) | "**validação** / **validar**" do próprio modelo | preferir "análise comparativa de cobertura" / "demonstração conceitual" — alinha a linguagem ao que o método de fato entrega (ver Elo 1). |
| Retrofit l. 4 | "interações recorrentes entre humanos, agentes de IA, processos de negócio e mecanismos de governança. **Nesse ecossistema, os seres humanos, os agentes de IA, os processos de negócio e as estruturas de governança** coevolvem…" | **Redundância literal** — a mesma enumeração quádrupla aparece em duas frases consecutivas. Fundir (ver diff §4.3). |

O tom geral já está denso e crítico; estas são afinações pontuais, não reescrita.

---

## 4. Micro-ajustes Estruturais e de Consistência LaTeX (Diffs)

### 4.1 Corrigir a atribuição do GRAI (precisão)
```diff
# sections/referencial.tex (l. 40)
- Com a IA Generativa, eles propõem a transição para o modelo GRAI \cite{E0A20}:
+ Com a IA Generativa, eles propõem a transição para o modelo GRAI:
```
E ao final do bloco GRAI (após a lista, l. 47), ancorar E0A20 corretamente como proposta paralela:
```diff
# sections/referencial.tex (l. 47)
- Essa evolução conceitual demonstra que a IA não atua apenas na periferia da GC,
- mas reconfigura os processos mais básicos de conversão de conhecimento.
+ Essa evolução conceitual demonstra que a IA reconfigura os processos mais básicos
+ de conversão de conhecimento. Proposta convergente é formulada por trabalhos que
+ readaptam diretamente o SECI ao contexto generativo, como o modelo GenAI-SECI
+ \cite{E0A20}, reforçando a insuficiência dos ciclos clássicos puramente humanos.
```

### 4.2 Anonimato / impessoalidade — remover atribuição nominal no corpo
Crítico para revisão (eventualmente cega) e para o registro impessoal Q1. O nome citado é, inclusive, coautor do 3M original e desta submissão.
```diff
# sections/referencial.tex (l. 71)
- A reinterpretação do status ontológico e operacional da Inteligência Artificial
- no ambiente de trabalho constitui o núcleo da adição teórica sugerida pelo
- Prof. Jano Moreira de Souza ao Modelo 3M 5.0.
+ A reinterpretação do status ontológico e operacional da Inteligência Artificial
+ no ambiente de trabalho constitui o núcleo da contribuição teórica do Modelo 3M 5.0.
```
*(Se houver intenção de creditar a origem da ideia, levar para a seção de Agradecimentos pós-aceitação.)*

### 4.3 Eliminar a enumeração quádrupla duplicada (Retrofit, abertura)
```diff
# sections/retrofit.tex (l. 4)
- Nesse arranjo, a UC deixa de operar apenas como estrutura de alinhamento
- estratégico e passa a coordenar interações recorrentes entre humanos, agentes de
- IA, processos de negócio e mecanismos de governança. Nesse ecossistema, os seres
- humanos, os agentes de IA, os processos de negócio e as estruturas de governança
- coevolvem a partir de uma simbiose cognitivo‑computacional contínua, nos termos de
- Jarrahi et al. \cite{jarrahi2023ai}.
+ Nesse arranjo, a UC deixa de operar apenas como estrutura de alinhamento
+ estratégico e passa a coordenar um ecossistema em que humanos, agentes de IA,
+ processos de negócio e mecanismos de governança coevoluem a partir de uma simbiose
+ cognitivo-computacional contínua, nos termos de Jarrahi et al. \cite{jarrahi2023ai}.
```

### 4.4 Padronizar aspas — `retrofit.tex` usa aspas retas (renderização incorreta em LaTeX)
Todo o restante do artigo usa `` ``…'' `` (aspas tipográficas). Em `retrofit.tex`, três termos usam aspas retas `"…"`, que em LaTeX renderizam como dois caracteres de fechamento (″…″).
```diff
# sections/retrofit.tex (l. 57)
- ela introduz o risco de uma "vigilância cognitiva" permanente.
+ ela introduz o risco de uma ``vigilância cognitiva'' permanente.

# sections/retrofit.tex (l. 61)
- Há um debate crescente sobre a ocorrência de "dependência de prompt" e atrofia cognitiva
+ Há um debate crescente sobre a ocorrência de ``dependência de prompt'' e atrofia cognitiva

# sections/retrofit.tex (l. 69)
- caracterizada como um "agente que aprende" ou que "cria conhecimento"?
+ caracterizada como um ``agente que aprende'' ou que ``cria conhecimento''?
```

### 4.5 Normalizar hífens Unicode em `retrofit.tex` (19 ocorrências de U+2011)
`retrofit.tex` contém **19 hifens não-quebráveis** (caractere U+2011, ex.: `aditiva‑reinterpretativa`, `não‑estruturados`, `pós‑LLMs`, `co‑evolui`), ausentes de todas as outras seções (que usam o hífen ASCII `-`). Risco de hifenização inconsistente e de falha de compilação conforme o encoding. Normalizar via substituição global no arquivo:
```bash
# executar uma vez sobre o arquivo
sed -i 's/\xe2\x80\x91/-/g' sections/retrofit.tex
```
*(Substitui U+2011 por hífen comum; revisar visualmente em seguida.)*

### 4.6 Consistência tipográfica de siglas e termos estrangeiros
Inconsistências detectadas na varredura:
- **RAG/GRAI**: `\texttt{RAG}` (5×) vs. `RAG` em fonte normal (13×); `\texttt{GRAI}` vs. `GRAI`. Decidir um padrão único. Recomendo **fonte normal** para ambas as siglas (`RAG`, `GRAI`, `KG`) — `\texttt{}` é convencionalmente reservado a código/identificadores, não a acrônimos conceituais; mantenha `\texttt{}` apenas para os identificadores reais de software na Metodologia (`httpx`, `pydantic`, `pgvector`).
- **framework**: `\textit{framework}` (2×) vs. `framework` romano (23×). Como o termo é central e já aportuguesado no uso, padronizar em **romano sem itálico** em todo o texto (e reservar itálico para estrangeirismos pontuais como *learning in the flow of work*, *scaffolding*, *deskilling*).
```diff
# sections/analise.tex (l. 63) — exemplo de unificação de siglas
- Através do acoplamento entre LLMs, Grafos de Conhecimento e arquiteturas de
- \texttt{RAG} \cite{pan2024unifying}, o \textit{Model 5.0} atua como um andaime
+ Através do acoplamento entre LLMs, Grafos de Conhecimento e arquiteturas de
+ RAG \cite{pan2024unifying}, o \textit{Model 5.0} atua como um andaime
```

### 4.7 Citação como substantivo (Metodologia l. 15)
`\cite` usado como nome de autor renderiza "…por [12]".
```diff
# sections/metodologia.tex (l. 15)
- análise comparativa do framework 3M 5.0 resultante em relação aos 19 modelos
- catalogados na literatura por \cite{mora2025model}, com o objetivo de demonstrar
+ análise comparativa do framework 3M 5.0 resultante em relação aos 19 modelos
+ catalogados por Mora-Mora et al. \cite{mora2025model}, com o objetivo de demonstrar
```

### 4.8 Consistência de nomeação do 3M original (refs vs. corpo)
A legenda da Fig. 1 e o corpo citam "**Costa, Souza e Oliveira, 2011**"; a entrada `costa20113m` lista os autores como **Farias da Costa, Oliveira e Moreira de Souza**. Como a primeira autora é coautora desta submissão, padronizar a forma de citação (sugiro "Costa, Oliveira e Souza" ou a forma exata do `.bib`) em legenda, corpo e abstract, evitando que o parecerista detecte divergência autor↔referência.

---

## 5. Síntese — Checklist de Submissão

**Bloqueadores (resolver antes de submeter):**
1. **Fig. 1 é placeholder** (`\framebox`) — substituir por figura real; idealmente **acrescentar diagrama do 3M 5.0** (§1, Elo 3).
2. **Atribuição nominal no corpo** ("Prof. Jano Moreira de Souza", Referencial l. 71) — remover (§4.2).
3. **Misattribuição do GRAI** a E0A20 (Referencial l. 40) — corrigir ancoragem (§4.1).

**Alto valor (robustez do argumento):**
4. Quebrar a circularidade da "validação" — nomear 2–3 modelos reais na coluna Tradicionais (catálogo: S1A04/S1A09/S1A10/S2A04) e calibrar a linguagem "validar→comparar cobertura" (§1 Elo 1; §3).
5. Explicitar o critério de curadoria 93→20 (§1 Elo 2).

**Polimento (cosmético, mas perceptível em Q1):**
6. Aspas retas → tipográficas em `retrofit.tex` (§4.4); normalizar U+2011 (§4.5).
7. Padronizar `RAG`/`GRAI`/`framework` (§4.6); corrigir `por \cite` (§4.7); unificar nome do 3M (§4.8).
8. Reduzir `de forma <adj>` (31→~20) e os resíduos de tom da tabela em §3.

**Avaliação final:** a construção teórica é original, bem ancorada e internamente coerente — material de Q1. O que ainda o segura não é o conteúdo, mas a **apresentação da evidência** (figura ausente, validação circular) e **higiene de submissão** (anonimato, tipografia). Nenhuma fonte foi inventada; todas as sugestões de citação (incluindo S1A04/S1A09/S1A10/S2A04) constam do catálogo local e foram verificadas como ainda não utilizadas. As fragilidades sem cobertura no acervo (Meister; figura) foram sinalizadas para ação dos autores.
