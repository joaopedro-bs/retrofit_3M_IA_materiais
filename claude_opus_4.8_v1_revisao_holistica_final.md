# Parecer de Revisão Final Holística
## "Retrofit do Modelo 3M de Universidade Corporativa: Reinterpretação de seus Três Pilares à Luz da Inteligência Artificial"

**Revisor:** Claude Opus 4.8 (Revisor Acadêmico Sênior — padrão periódico Q1, Sistemas de Informação / Gestão do Conhecimento)
**Data:** 09/06/2026
**Insumos analisados:** `main.tex` + 7 seções (`introducao`, `referencial`, `metodologia`, `retrofit`, `analise`, `discussao`, `conclusao`); `references.bib`; Catálogo da Scoping Review (`catalogo_artigos.csv`, 108 registros, 93 aprovados).
**Restrição observada:** todas as sugestões de citação abaixo referem-se **exclusivamente** a artigos já presentes no catálogo local e **ainda não utilizados** no LaTeX. Nenhuma referência externa foi inventada. Onde o catálogo não cobre a fragilidade, isso é declarado explicitamente.

---

## 1. Visão Geral e Fio Condutor

O artigo apresenta um *Golden Thread* sólido e, em sua arquitetura macro, coeso. A cadeia argumentativa — (i) economia do conhecimento → UC como locus de GC → (ii) Modelo 3M clássico ancorado em Prat → (iii) ruptura sociotécnica da IA Generativa/agêntica → (iv) gap empírico de Mora-Mora et al. (19 modelos, tecnologia passiva) → (v) retrofit 3M 5.0 (Motive/Model/Moment + GRAI) → (vi) validação comparativa em 5 dimensões → (vii) discussão e limites — é logicamente encadeada e raramente quebra. A decisão de manter um vocabulário recorrente de *âncoras* (Prat/Stollenwerk para os processos de GC; Jarrahi para a simbiose; Böhm & Durst/GRAI para a evolução do SECI; Faraj et al. para a agência material) dá liga ao texto e permite ao leitor rastrear cada afirmação até sua origem teórica. Esse é o maior acerto estrutural do manuscrito.

Três observações sobre a integridade do fio condutor merecem atenção:

**(a) O gap é introduzido em regime de quase-redundância.** A afirmação central de Mora-Mora et al. — "19 modelos, nenhum integra IA/Indústria 5.0 de forma ativa" — aparece na Introdução (l. 8), no Referencial (§4.1, l. 32), na Metodologia (Fase 1 e §Validação, l. 12 e l. 102), no Retrofit (l. 6), na Análise (l. 4, l. 33, l. 65) e na Discussão (l. 4). A repetição literal do mesmo enunciado quantitativo ("19 modelos... nenhum deles integra...") em seis seções enfraquece a densidade. A recomendação é **declarar o gap uma vez de forma plena (Introdução), reapresentá-lo operacionalmente na Metodologia/Análise, e nas demais ocorrências referenciá-lo por remissão** (ex.: "o gap estrutural identificado na Seção II") em vez de reescrever a estatística. Ver diffs na Seção 4.

**(b) A transição Referencial → Metodologia é o elo mais frágil.** O Referencial encerra (§4.5, l. 91) com uma síntese conceitual já operacional do loop Moment→Model→Motive — isto é, antecipa a *solução* (a arquitetura 3M 5.0) antes de a Metodologia justificar *como* tal arquitetura foi construída. O leitor chega à Metodologia já convencido do desenho, o que esvazia a função de justificação metodológica. Sugere-se que o parágrafo de fechamento do Referencial se restrinja a consolidar a **lacuna e os requisitos teóricos** (não a solução), deixando a formulação do loop para o Retrofit (onde, de fato, ela é reapresentada em l. 71).

**(c) A Metodologia carrega peso de engenharia que destoa do registro conceitual.** A subseção 5.2 (pipeline SLR-RAG: `httpx`, `playwright`, `pydantic`, `pgvector`, defesa contra *prompt injection* em três camadas) é tecnicamente impressionante, porém sua granularidade de implementação ofusca o argumento metodológico central — que é *conceitual-construtivo*. Para um periódico Q1 de SI, o detalhamento de *exponential backoff* e *magic bytes* SHA-256 é periférico à contribuição. Recomenda-se condensar 5.2.1–5.2.3 em um parágrafo denso e remeter o detalhe de implementação a um apêndice ou nota, preservando apenas o que sustenta a **validade da triagem** (defesa contra injeção, determinismo a temperatura 0.0, validação Pydantic). Isso reequilibra o fio condutor entre método e construção.

No conjunto, o manuscrito está maduro. As intervenções recomendadas são de **calibragem** (redundância, equilíbrio de registro, amarração de transições), não de reestruturação.

---

## 2. Caça aos "AI-isms"

A varredura identificou padrões de escrita assistida por LLM em três níveis: (i) construções sintáticas repetitivas, (ii) transições contrastivas robóticas e (iii) adjetivação avaliativa. Métricas da varredura automática (7 seções):

- `não apenas … mas …`: **7 ocorrências** (padrão sintático mais característico de LLM no texto).
- `de forma <adjetivo>`: **~32 ocorrências** (autônoma, contínua, dinâmica, holística, integrada, sistemática, transparente, segura, acrítica…).
- Transições contrastivas em início de frase (`Contudo`/`Entretanto`/`Todavia`/`Diante disso`/`Em síntese`/`Nesse contexto`/`Sob essa ótica`): **20 ocorrências**.
- `reside na/no/em` como abertura enfática: **5 ocorrências**.

Nenhuma dessas marcas é isoladamente fatal, mas sua densidade agregada produz a "assinatura" de redação por IA. Abaixo, os trechos prioritários e a respectiva reescrita seca.

### 2.1 Construção `não apenas X, mas Y` (sobreuso)

> **Introdução, l. 12** — "o retrofit 3M 5.0 não apenas atualiza a tecnologia subjacente à UC, mas reposiciona-a como um ecossistema sociotécnico de aprendizagem contínua e governada."
> **Reescrita:** "o retrofit 3M 5.0 reposiciona a UC como um ecossistema sociotécnico de aprendizagem contínua e governada, para além da mera atualização tecnológica."

> **Análise, l. 35** — "permite que a UC opere não apenas na distribuição, mas na cogeração ativa de valor organizacional."
> **Reescrita:** "permite que a UC migre da distribuição para a cogeração ativa de valor organizacional."

> **Análise, l. 65** — "o framework proposto não apenas preenche o gap identificado na literatura, mas define uma nova base para a evolução das capacidades dinâmicas."
> **Reescrita:** "o framework proposto preenche o gap identificado e estabelece uma base para a evolução das capacidades dinâmicas de aprendizagem organizacional."

*Recomendação geral:* reduzir as 7 ocorrências a no máximo 2. O recurso, quando raro, é retórico; quando recorrente, é tique.

### 2.2 Adjetivação avaliativa e "vitalidade"

> **Retrofit, l. 4** — "para se consolidar como um ecossistema sociotécnico **vivo e emergente**."
> **Reescrita:** "para se consolidar como um ecossistema sociotécnico coevolutivo." (a metáfora "vivo" já é carregada por "Laboratório Vivo"; "emergente" é redundante com "coevolutivo").

> **Introdução, l. 26 / Conclusão** — "preservando sua **vitalidade conceitual**" / "mantenha sua **vitalidade conceitual**".
> **Observação:** a expressão "vitalidade conceitual" aparece duas vezes com função idêntica. Substituir uma por "consistência interna" ou "validade estrutural".

> **Referencial, l. 81** — "riscos corporativos **de elevada gravidade**."
> **Reescrita:** "riscos corporativos críticos." (a adjetivação intensificadora "de elevada gravidade" é vazia de informação).

### 2.3 Transições robóticas / balanceadas

> **Referencial, l. 53** — "**Nesse contexto sociotécnico complexo**, a simbiose humano-IA proposta por Jarrahi et al. consolida-se como o referencial analítico adequado."
> **Reescrita:** "A simbiose humano-IA de Jarrahi et al. fornece o referencial analítico para esse arranjo." (elimina o conector-clichê e a auto-qualificação "adequado").

> **Retrofit, l. 71** — "**É importante notar a** interdependência entre essas tensões…"
> **Reescrita:** "As tensões são interdependentes:" (o metacomentário "é importante notar" é descartável; vá direto ao conteúdo).

> **Retrofit, l. 50/52** — "A proposição do Modelo 3M 5.0 **não se pretende acrítica**."
> **Reescrita:** "A proposição do Modelo 3M 5.0 reconhece suas próprias tensões." (afirmar o que o texto *é*, não o que não pretende ser).

> **Discussão, l. 32 / Análise, l. 65** — duplo uso de "**Em síntese**" para abrir parágrafos de fechamento.
> **Recomendação:** manter no máximo um. No segundo, abrir diretamente pela tese.

### 2.4 Aberturas enfáticas `reside em`

Ocorre 5×, sempre na mesma função ("o problema reside em…", "a resolução reside em…", "o aspecto inovador reside em…"). Recomenda-se variar pelo menos 3 delas com formulações diretas (ex.: "O problema central é…"; "A tensão resolve-se no pilar Moment 5.0…"; "A inovação do Modelo 3M está em…").

### 2.5 Aspas de distanciamento (uso aceitável, monitorar)

O texto usa aspas para cunhar conceitos ("vigilância cognitiva", "muletas cognitivas", "monstros de Haraway", "dependência de prompt", "andaimes", "agente que aprende"). Aqui o uso é **legítimo** — são termos técnicos ou citações. Não alterar; apenas evitar acrescentar novos casos, pois o acúmulo de aspas também sinaliza redação por IA.

---

## 3. Oportunidades de Ancoragem Teórica (apenas Catálogo Local)

A tabela abaixo lista pontos onde o argumento está **subancorado** e indica o artigo do catálogo **sobrando** (não citado no LaTeX) que pode cobri-lo. Confidência = força do encaixe temático. Todos os IDs foram verificados como ausentes do conjunto de 20 códigos atualmente citados.

| # | Local no texto (fragilidade) | Artigo do catálogo NÃO usado | Conf. |
|---|---|---|---|
| A1 | **Referencial §4.1, l. 8** — a evolução histórica da UC ("liderada por Meister") não tem citação de suporte; afirmação de campo sem lastro bibliométrico. | **S2A04** (2019) — *Mapping the themes and intellectual structure of corporate university: co-citation and cluster analyses*. Ancora empiricamente a trajetória/estrutura intelectual do campo. | Alta |
| A2 | **Referencial §4.1, l. 32 / Introdução l. 8** — o argumento de que os modelos de UC tratam a tecnologia como infraestrutura passiva apoia-se apenas em Mora-Mora et al. | **E0A01** (2018) — *Purpose of the use of technologies in the contemporary models of Corporate University*. Evidência direta e independente sobre o papel (passivo) da tecnologia nos modelos de UC; reforça o gap sem circular em Mora-Mora. | **Muito alta** |
| A3 | **Referencial §4.2, l. 53 / Retrofit §Motive, l. 15** — a simbiose humano-IA repousa monoliticamente em Jarrahi et al. | **E0A08** (2022) — *The Recursive Theory of Knowledge Augmentation: integrating human intuition and knowledge in AI to augment organizational knowledge*. Segundo pilar teórico para a complementaridade cognitiva humano-IA. | Alta |
| A4 | **Referencial §4.2, l. 40 / Retrofit §Model, l. 26 / Discussão l. 10** — a transição SECI→GRAI sustenta-se só em Böhm & Durst (E0A18). | **E0A20** (2026) — *Tacit Knowledge Management with Generative AI: Proposal of the GenAI SECI Model*. Uma segunda proposta independente de revisão do SECI sob GenAI fortalece a tese de que o modelo clássico precisa evoluir (corrobora, não substitui, o GRAI). | **Muito alta** |
| A5 | **Referencial §4.2, l. 34–36** — abertura do bloco "IA Generativa e GC" carece de um respaldo de revisão sistemática sobre criação de conhecimento mediada por IA. | **E0A17** (2025) — *Transforming organizational knowledge creation through artificial intelligence: a systematic review*. Âncora de SLR para a afirmação de disrupção na criação de conhecimento. | Média-alta |
| A6 | **Retrofit §Model 5.0, l. 24 / Análise §LFW, l. 63** — afirmações empíricas sobre IA como andaime e ganho de aprendizagem no fluxo de trabalho. | **S6A03** (2025) — *AI-Supported Workplace Education: A Systematic Review of Learning Outcomes, Opportunities, and Challenges*. Lastro empírico (resultados de aprendizagem) para o "Laboratório Vivo". | Alta |
| A7 | **Retrofit §Tensões "Dependência Cognitiva", l. 59–61 / Discussão l. 14** — o risco de atrofia/"muletas cognitivas" apoia-se em Callari & Puppione e Dell'Acqua. | **S6A08** (2020) — *Artificial intelligence in the workplace – A double-edged sword*. Reforça a ambivalência (ganho × dependência) com fonte dedicada ao tema. | Alta |
| A8 | **Discussão §Reconfiguração do Trabalho, l. 14** — o argumento de *deskilling* repousa em Dell'Acqua (working paper externo). | **S8A07** (2026) — *Deskilling, reskilling, or upskilling? Unpacking the pathways of student adaptation to generative AI*. Fonte do catálogo dedicada justamente ao eixo deskilling/upskilling sob GenAI. | Alta |
| A9 | **Discussão §Caráter Pedagógico/Accountability, l. 30** — a discussão de *accountability* algorítmica em RH (encaminhamento à requalificação) usa Joshi + Birkstedt. | **S7A04** (2026) — *Human-Centric AI Governance in Digital HRM: A Conceptual Framework for Responsible Digital Business*. Encaixe quase exato: governança de IA centrada no humano aplicada a RH digital. | **Muito alta** |
| A10 | **Retrofit §Model 5.0, l. 24 / Análise l. 63** — o acoplamento RAG + Grafos de Conhecimento apoia-se apenas em Pan et al. (roadmap genérico). | **S9A09** (2026) — *A Hybrid RAG System Integrating Knowledge Graph and Vector Retrieval* (alternativa: **S4A05**, 2025 — *RAG and LLMs for Enterprise KM: a Systematic Literature Review*). Sustenta tecnicamente a alegação de que o acoplamento RAG+KG resolve a acurácia factual. | Média-alta |

**Fragilidades sem cobertura no catálogo (apontar para busca externa, NÃO inventar):**

- **Referencial §4.1, l. 8** — a atribuição a **Meister** como fundadora do conceito de UC não tem entrada própria no catálogo (S2A04 cobre a *estrutura do campo*, não a obra seminal de Meister). Se os autores quiserem citar Meister diretamente, é necessária busca externa.
- **Discussão** — `bender2021stochastic`, `orlikowski2007sociomaterial`, `edmondson1999psychological`, `argyris1978organizational`, `foucault1975surveiller`, `dellacqua2023navigating`, `ng2021conceptualizing`, `european2024aiact` são âncoras externas (corretas e bem empregadas), porém **fora do catálogo**. Estão devidamente no `.bib`; apenas registre que não derivam da scoping review, caso o método exija rastreabilidade total das fontes ao catálogo.

---

## 4. Micro-ajustes Estruturais (Diffs)

Blocos `diff` pontuais. Linhas precedidas de `-` são o texto atual; `+` é a substituição sugerida.

### 4.1 Eliminar redundância do gap (Referencial → fechamento §4.1)
Foco: tirar a reapresentação da estatística e amarrar à Metodologia.

```diff
# sections/referencial.tex (l. 32, final do parágrafo)
- Nenhum dos modelos existentes integra tecnologias agênticas ou os pressupostos
- da Indústria 5.0 à sua arquitetura interna de processos de aprendizagem, criando
- um vácuo teórico que este trabalho busca preencher.
+ Nenhum dos modelos existentes integra tecnologias agênticas ou os pressupostos
+ da Indústria 5.0 à arquitetura interna de processos de aprendizagem. Esse vácuo
+ teórico — e o protocolo de scoping review que o evidencia — é detalhado na
+ Seção \ref{sec:metodologia}.
```

### 4.2 Reduzir antecipação da solução no fechamento do Referencial
```diff
# sections/referencial.tex (§4.5, l. 91)
- A governança de IA, portanto, se consolida como um processo dinâmico de Gestão
- do Conhecimento corporativo: as diretrizes éticas e técnicas do Moment 5.0
- orientam a operação segura do Model 5.0, enquanto os aprendizados e desvios
- comportamentais detectados pelos loops de monitoramento em tempo real
- realimentam e reconfiguram as diretrizes de sensing de competências do Motive 5.0.
- Centralizar essa governança e capacitação na Universidade Corporativa assegura
- que a mitigação de riscos esteja intrinsecamente ligada à capacitação humana
- contínua e ao desenvolvimento organizacional sustentável.
+ A governança de IA configura-se, assim, como um requisito teórico ainda não
+ atendido pelos modelos de UC: uma função de aprendizagem organizacional, e não
+ de mera conformidade técnica. A operacionalização desse requisito nos pilares do
+ Modelo 3M 5.0 é formulada na Seção \ref{sec:retrofit}.
```

### 4.3 Condensar registro de engenharia na Metodologia (amostra)
```diff
# sections/metodologia.tex (§5.2.1, l. 24–27)
- O sistema faz uso de clientes assíncronos (\texttt{CrossrefClient},
- \texttt{SemanticScholarClient} e \texttt{UnpaywallClient}) implementados em Python
- por meio da biblioteca \texttt{httpx}. Para garantir a estabilidade das
- requisições simultâneas em bases acadêmicas lentas, o ciclo de vida do cliente
- HTTP foi gerenciado sob políticas de controle de concorrência restritas, limites
- de conexões simultâneas e mecanismos de \textit{exponential backoff} para
- contornar bloqueios de \textit{rate limiting}.
+ A ingestão usou clientes assíncronos (Crossref, Semantic Scholar e Unpaywall) em
+ Python, com controle de concorrência e \textit{backoff} para estabilidade frente
+ a \textit{rate limiting}. Detalhes de implementação constam no Apêndice~A.
```

### 4.4 Corrigir imprecisão numérica na triagem (precisão epistemológica)
A redação atual conflita "114 entradas únicas **e aprovadas**" com o total final de "93 aprovados", e o parêntese "(25 da Etapa 0 e 89 da execução das equações)" soma 114 — número de registros **únicos**, não de **aprovados**. Os totais da Tabela 1 (Triados 129 − Duplicados 15 − Inacessíveis 21 = 93) estão corretos; o texto corrido é que ambiguiza.

```diff
# sections/metodologia.tex (l. 55–56)
- O processo inicial catalogou 114 entradas únicas e aprovadas no banco de dados
- (sendo 25 provenientes da Etapa 0 de mapeamento de base e 89 resultantes da
- execução direta das equações de busca).
- Após a triagem, 21 artigos foram excluídos por inacessibilidade física permanente
- (barreiras de paywall intransponíveis), resultando em um catálogo final
- consolidado de \textbf{93 artigos únicos e aprovados} indexados localmente com PDF completo.
+ Após a deduplicação (15 registros redundantes), o processo consolidou 114 entradas
+ únicas (25 da Etapa 0 de mapeamento de base e 89 da execução direta das equações de
+ busca). Destas, 21 foram excluídas por inacessibilidade física permanente (paywall
+ intransponível), resultando em um catálogo final de \textbf{93 artigos aprovados}
+ indexados localmente com PDF completo.
```

### 4.5 Amarração explícita Análise → Discussão (transição entre seções)
A última frase da Análise já antecipa a Discussão, mas de forma genérica. Reforçar o vínculo causal:
```diff
# sections/analise.tex (l. 65, final)
- Os impactos teóricos e as implicações práticas dessa nova configuração
- sociotécnica são detalhados e discutidos na seção a seguir.
+ Os dois pontos de cobertura plena exclusivos do 3M 5.0 — Agência Ativa de IA e
+ Governança Algorítmica — concentram as implicações teóricas e práticas mais
+ disruptivas, e estruturam a discussão conduzida na Seção \ref{sec:discussao}.
```

### 4.6 Desinflar abertura `não apenas … mas` (Introdução)
```diff
# sections/introducao.tex (l. 12)
- Nesse sentido, o retrofit 3M 5.0 não apenas atualiza a tecnologia subjacente à
- UC, mas reposiciona-a como um ecossistema sociotécnico de aprendizagem contínua e governada.
+ O retrofit 3M 5.0 reposiciona a UC como um ecossistema sociotécnico de
+ aprendizagem contínua e governada, para além da atualização da tecnologia subjacente.
```

---

## 5. Síntese do Parecer

O manuscrito está em estágio de **revisão fina**, não de reescrita. O fio condutor é robusto e as âncoras teóricas são coerentes e bem aplicadas. As prioridades, em ordem:

1. **Precisão (alta prioridade):** corrigir a ambiguidade numérica da triagem (§4.4) — é o único ponto que toca a integridade factual do método.
2. **Redundância (alta):** desinflar a repetição literal do gap "19 modelos" (§4.1, §4.2) e reequilibrar método vs. construção (§4.3).
3. **AI-isms (média):** reduzir `não apenas…mas` (7→2), variar transições contrastivas e aberturas `reside em`, podar adjetivação avaliativa (Seção 2).
4. **Ancoragem (oportunidade, não obrigatória):** os encaixes A2 (E0A01), A4 (E0A20) e A9 (S7A04) são os de maior retorno — todos cobrem pontos hoje mono-ancorados, com artigos do próprio catálogo. Demais encaixes (A1, A3, A5–A8, A10) são reforços opcionais.

Nenhuma alucinação foi introduzida; todas as sugestões de citação são rastreáveis ao catálogo local e verificadas como ainda não utilizadas no LaTeX. Fragilidades sem cobertura no acervo (Meister; âncoras externas da Discussão) foram sinalizadas para decisão dos autores, sem fabricação de fontes.
