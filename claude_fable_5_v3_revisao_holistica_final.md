# Parecer V3 — Revisão Holística Final (Simulação de Peer Review + Proofreading)

**Artigo:** Retrofit do Modelo 3M de Universidade Corporativa (3M 5.0) com IA Generativa
**Revisor simulado:** Reviewer 2 (cego, metodológico, Q1/A1 em SI & GC)
**Modelo revisor:** Claude Fable 5 (Anthropic)
**Data:** 2026-06-09
**Arquivos auditados:** `main.tex`, `sections/{introducao, referencial, metodologia, retrofit, analise, discussao, conclusao}.tex`, `references.bib`, `main.log`, `main.blg`

---

## 1. Parecer do Reviewer 2

> *"O artigo propõe um modelo conceitual e declara tê-lo 'validado' por meio de uma análise comparativa cujas cinco dimensões foram definidas pelos próprios autores — e que coincidem, uma a uma, com as forças anunciadas do modelo proposto. A pontuação (Ausente/Parcial/Pleno) foi atribuída pelos próprios proponentes, sem juízes independentes, sem medida de concordância inter-avaliadores e sem acesso do leitor à matriz de codificação dos 19 modelos individuais (a Tabela 2 agrega os 19 modelos em uma única coluna). Trata-se de um baralho embaralhado pelos autores e cortado por eles mesmos. Adicionalmente, o backbone processual do modelo apoia-se no GRAI (Böhm & Durst, 2025), um framework recém-publicado e ainda sem validação empírica independente — o retrofit, portanto, troca um alicerce testado por duas décadas (SECI) por um alicerce de meses. Por fim, a triagem da scoping review foi delegada a um LLM avaliador único (temperatura 0.0), sem amostra de dupla triagem humana, sem métricas de recall/precisão da triagem automatizada e sem aderência declarada ao PRISMA-ScR."*

**Como nos defendemos no texto (3 inserções cirúrgicas):**

1. **Rebaixar a palavra "validação" e blindar a circularidade.** Onde o texto diz "validação conceitual", qualificar explicitamente como *avaliação comparativa de cobertura conceitual conduzida pelos autores* e admitir na Conclusão (limitações) que: (a) as dimensões e a pontuação são autoatribuídas; (b) a robustez exige painel de especialistas independentes (Delphi/julgamento por pares) — já proposto como trabalho futuro. Ver diff D1.
2. **Blindar a dependência do GRAI.** Acrescentar uma frase na Discussão ou Conclusão reconhecendo que o GRAI é recente e não validado empiricamente, e que o 3M 5.0 não depende ontologicamente dele: o mapeamento Prat/Stollenwerk permanece válido caso o GRAI seja refinado pela literatura. Ver diff D2.
3. **Blindar a triagem automatizada.** Acrescentar nas limitações que a triagem assistida por LLM, embora mitigue subjetividade humana, introduz viés próprio do modelo avaliador, e que não houve dupla triagem humana por amostragem — recomendação futura: calibração com kappa humano-máquina. Ver diff D3.

**Segunda maior crítica plausível (generalização):** o Modelo 3M original é um capítulo de enciclopédia (2011) com difusão limitada fora do contexto brasileiro; um revisor internacional perguntará por que fazer retrofit *deste* modelo e não de um framework de maior circulação. A defesa já existe no texto (ancoragem única do 3M nos processos de GC de Prat — argumento bom), mas está implícita. Sugiro torná-la explícita em uma frase na Introdução: o 3M é o único dos modelos catalogados com mapeamento formal visão-a-processo de GC, o que o torna o candidato natural a um retrofit orientado a processos.

---

## 2. Auditoria do Abstract / Introdução / Conclusão (espelhamento)

### 2.1 Abstract — checklist

| Elemento | Presente? | Observação |
|---|---|---|
| Contexto | Sim | OK (1ª frase) |
| Problema/lacuna | Sim | OK (última frase) |
| **Método** | **Parcial** | Não menciona a scoping review (93 artigos) nem a análise comparativa estruturada |
| **Resultados principais** | **Ausente** | O abstract termina na lacuna; não reporta o resultado da comparação (cobertura plena nas 5 dimensões vs. 19 modelos) |
| Contribuições | Parcial | Implícitas nos pilares; não explícitas |

O abstract "vende" o modelo mas não entrega o desfecho. Sugestão de acréscimo (após "...processo adaptativo)."):

> *"A análise comparativa frente aos 19 modelos de UC catalogados na literatura, conduzida sobre cinco dimensões analíticas a partir de uma scoping review de 93 artigos, indica que o 3M 5.0 alcança cobertura plena em dimensões ausentes ou periféricas nos modelos existentes — notadamente agência ativa de IA e governança algorítmica."*

E reposicionar a frase da lacuna antes dessa, para fechar com a contribuição (e não com o problema).

### 2.2 Espelhamento Introdução ↔ Conclusão

- **Promessa não ecoada:** a Introdução promete três dimensões de contribuição (teórica, prática, **metodológica** — "formaliza o uso do retrofit conceitual como estratégia de evolução de teorias"). A Conclusão cobre teórica e gerencial, mas **omite a contribuição metodológica** (retrofit como método + pipeline SLR-RAG). Ver diff D4.
- Os 4 objetivos específicos da Introdução têm correspondência nas Seções 4 e 5 — OK.
- Glosa dos pilares na Conclusão diverge do restante do artigo: "pilares de **motivação**, **entrega instrucional** e **governança ética**" vs. "visão de motivo / modelo / momento" usados em todo o texto. Harmonizar (diff D5).

### 2.3 Introdução — urgência

A Introdução vende bem o problema (lacuna quantificada: 19 modelos, nenhum integra IA). Único reparo: a frase final do §3 é redundante ("fator **passivo** de infraestrutura... evidenciando o uso **passivo** de tecnologia") — diff P4.

---

## 3. Achados CRÍTICOS de pré-voo (bloqueiam submissão)

### C1. Quatro citações quebradas — renderizam `[?]` no PDF
`main.log`/`main.blg` confirmam: **S1A04, S1A09, S1A10, S2A04** são citadas em `analise.tex` (linhas 33 e 40) e **não existem em `references.bib`**. O PDF atual exibe `[?]` na página 11. Ação: adicionar as 4 entradas ao `.bib` (verificar no `catalogo_artigos.csv`) **ou** remover as chamadas, citando apenas `\cite{mora2025model}` como fonte agregadora dos exemplos.

### C2. Figura 1 é um placeholder
`referencial.tex` (linhas 16–21): a Figura `fig:3m_original` é um `\framebox` com o texto "Representação do Modelo 3M Original". Além disso, **a figura nunca é referenciada** no corpo do texto (nenhum `\ref{fig:3m_original}`). Ação dupla: inserir a figura real e adicionar uma chamada no parágrafo que descreve o Modelo 3M (ex.: "...o Modelo 3M estabelece (Figura~\ref{fig:3m_original}):").

### C3. Inconsistência numérica entre o texto e a Tabela 1 (metodologia)
A lista por eixos (`metodologia.tex`, linhas 46–53) reporta **14 + 27 + 24 + 10 + 18 + 15 = 108** artigos. A Tabela `tab:triagem` reporta **129 triados** (29 da Etapa 0 + 100 das buscas) e consolidados por eixo de **13 / 11 / 11 / 10 / 8 / 15** (+25 da Etapa 0 = 93). Os números da lista **não fecham com a tabela sob nenhuma leitura** (não são "triados", nem "consolidados", nem "consolidados + etapa 0"). Um revisor metodológico refaz essa soma em 30 segundos. **Não proponho correção inventada: é preciso reconciliar com os dados reais do pipeline** e alinhar lista e tabela (ou declarar explicitamente o que cada número representa).

### C4. Dois conjuntos de processos atribuídos a Prat
- `referencial.tex` L30: Prat = "identificação, avaliação, atualização e proteção" (estratégicos) + "aquisição, transferência, armazenamento e utilização" (operacionais).
- `metodologia.tex` L91 e `retrofit.tex` L6: Prat = "geração, codificação, armazenamento, distribuição e aplicação".

As duas listas não podem ser ambas "os processos de Prat". Verificar a fonte primária e harmonizar — ou explicitar que a primeira lista é o mapeamento de Costa et al. (2011) sobre Prat, e a segunda é a síntese de macroprocessos adotada no retrofit. Conexo: `retrofit.tex` L17 atribui "identificação" a `\cite{prat2011hierarchical, stollenwerk2001gestao}` — se identificação vem de Stollenwerk, a ordem das citações deveria refletir isso.

### C5. Citação com atribuição errada (Alavi & Leidner)
`referencial.tex` L36: "Na perspectiva **fundacional** da GC formulada por Alavi e Leidner `\cite{E0A15}`" — mas E0A15 é **Alavi, Leidner & Mousavi (2024)**, o paper de GenAI. A perspectiva fundacional é Alavi & Leidner (2001, MISQ), que não está no `.bib`. Adicionar a referência de 2001 ou reformular a frase (diff P7).

### C6. Ordem de autores do Modelo 3M
O texto usa consistentemente "Costa, Souza e Oliveira", mas `references.bib` registra `Farias da Costa ... and Oliveira, Jonice and Moreira de Souza, Jano` (Costa, **Oliveira**, Souza). Verificar a ordem na fonte original e alinhar texto ↔ bib.

---

## 4. Lista de Proofreading e Typos

| # | Arquivo / Local | Substituir | Por |
|---|---|---|---|
| P1 | `retrofit.tex`, L4 | "as estruturas de governança **coevolvem**" | "**coevoluem**" (verbo coevoluir) |
| P2 | `referencial.tex`, L38 | "as **cinco** fases clássicas do ciclo de conhecimento ... criação, armazenamento/recuperação, transferência e aplicação" | "as **quatro** fases" (a lista tem 4 itens; o framework de Alavi-Leidner tem 4 processos) |
| P3 | `conclusao.tex`, L9 | "**Recuperação Aumentada por Geração** (RAG)" | "**Geração Aumentada por Recuperação** (RAG)" — tradução invertida; inconsistente com a Introdução |
| P4 | `introducao.tex`, L8 | "tratando a tecnologia quase sempre como um fator passivo de infraestrutura de TI, **evidenciando o uso passivo de tecnologia em modelos de UC** \cite{E0A01}" | "tratando a tecnologia quase sempre como um fator passivo de infraestrutura de TI \cite{E0A01}" — elimina redundância "passivo...passivo" |
| P5 | `introducao.tex`, L10 | "**co-evolui** com a inteligência humana" | "**coevolui**" — padronizar grafia sem hífen ("coevolução" é a forma dominante no texto; também corrigir "co-evolução" em `referencial.tex` L73 e "co-definindo" em `retrofit.tex` L13, se optar por uniformidade total) |
| P6 | `metodologia.tex`, L12 | "nenhum deles **integra** tecnologias de IA ou conceitos de Indústria 5.0 à sua arquitetura interna de processos **de forma integrada**" | "...à sua arquitetura interna de processos **de forma abrangente**" — cacofonia integra/integrada |
| P7 | `referencial.tex`, L36 | "Na perspectiva fundacional da Gestão do Conhecimento formulada por Alavi e Leidner \cite{E0A15}" | "Na perspectiva fundacional da GC formulada por Alavi e Leidner — retomada e atualizada para o contexto de GenAI por Alavi, Leidner e Mousavi \cite{E0A15} —" (ou citar o paper de 2001) |
| P8 | `referencial.tex`, L32 | "e 15 incorporem variáveis de TI, **a totalidade deles** posiciona a tecnologia apenas como infraestrutura passiva" | "**todos os 19** posicionam a tecnologia apenas como infraestrutura passiva" — desfaz ambiguidade (totalidade de quê: dos 19 ou dos 15?) |
| P9 | `discussao.tex`, L14 | "identificado como tensão intrínseca do ecossistema 3M 5.0 (§...). [...] essa simbiose cognitivo-computacional **carrega a tensão intrínseca do** risco de dependência" | 2ª ocorrência: "carrega **o** risco de dependência" — elimina repetição de "tensão intrínseca" no mesmo parágrafo |
| P10 | `discussao.tex`, L20 | "materializa-se de forma mais aguda quando se examina que a introdução do sensing contínuo [...] **introduz** um dilema" (frase de ~70 palavras) | Dividir: "materializa-se de forma aguda no *sensing* contínuo do pilar *Motive 5.0*. Embora solucione a lentidão histórica do diagnóstico de defasagens, o *sensing* introduz um dilema sociotécnico de alta sensibilidade: ..." |
| P11 | `conclusao.tex`, L3 | "pilares de motivação (*Motive 5.0*), entrega instrucional (*Model 5.0*) e governança ética (*Moment 5.0*)" | "as visões de motivo (*Motive 5.0*), de modelo (*Model 5.0*) e de momento (*Moment 5.0*)" — consistência terminológica com todo o artigo |
| P12 | `metodologia.tex`, L4 | Frase de abertura com ~60 palavras (run-on) | Dividir após "(revisão de escopo)": ". A triagem foi suportada por um pipeline agêntico de automação..." |
| P13 | `metodologia.tex`, L4 | Citação `\cite{jarrahi2023ai}` como suporte de que "o método conceitual-construtivo é amplamente empregado na área de SI" | Jarrahi et al. não é referência metodológica. Citar uma fonte de método (ex.: Meredith, 1993; Jaakkola, 2020 — *conceptual papers*) ou remover a citação |
| P14 | Vários | Espaços em branco no fim de linha (`introducao.tex` L14/26, `referencial.tex` L65/85, `metodologia.tex` L89, `analise.tex` L49, `main.tex` L15/34) | Remover (cosmético, sem efeito no PDF) |
| P15 | `conclusao.tex` L9 vs. restante | "**dezenove** modelos" vs. "19 modelos" em todo o resto | Padronizar "19" |

**Voz passiva:** o uso é alto na Metodologia ("estruturou-se", "implementou-se", "realizou-se" em sequência), mas é convencional em PT-BR acadêmico e não compromete a clareza — sem ação obrigatória. Nas demais seções o equilíbrio ativa/passiva está bom.

**Jargões na primeira menção:** RAG, LLM, KG, GC, UC, SECI, GRAI — todos definidos na primeira ocorrência ✓. Exceções menores: *pgvector*, *MCP (Model Context Protocol)* e *magic bytes* aparecem na metodologia sem glosa — aceitável para o público-alvo, mas "MCP" merece meia-frase explicativa.

---

## 5. Sanidade LaTeX (pre-flight)

- **Compilação atual:** pdfLaTeX (TeX Live 2025) compila sem erros; únicos warnings relevantes são as 4 citações indefinidas (item C1).
- **Aspas:** uso correto de `` `` ''`` em todo o prosa-texto ✓. Aspas retas `"` aparecem **apenas** dentro de `\texttt{}` na Tabela 1 (strings de busca) — correto e intencional ✓.
- **Caracteres Unicode:** `retrofit.tex` usa 15 hífens não separáveis U+2011 ("aditiva‑reinterpretativa", "centrava‑se" etc.) e em-dashes U+2014 diretos; `analise/discussao/conclusao` usam U+2014; `introducao/metodologia/referencial` usam `---` ASCII. Compila no TeX Live 2025, mas **sistemas de submissão de editoras (e versões antigas de pdfLaTeX) podem falhar com U+2011**. Recomendo normalizar: U+2011 → `-`, U+2014 → `---` (diff D6, comando incluído).
- **Faltam pacotes recomendados:** sem `\usepackage[T1]{fontenc}` a hifenização de palavras acentuadas em português é degradada e o PDF não tem texto copiável correto. Adicionar (diff D7).
- **Bloco de autores:** três `\IEEEauthorblockN` empilhados geram três linhas separadas sem espaçamento padrão IEEE; e-mail renderiza como `[joaopedro, vfarias, emlopes]@cos.ufrj.br` com colchetes literais — o padrão IEEE usa chaves: `\{joaopedro, vfarias, emlopes\}@cos.ufrj.br` (diff D8).
- **Labels/refs:** todos os `\ref` resolvem ✓. Labels órfãos (definidos e nunca referenciados): `fig:3m_original` (ver C2), `subsec:abordagem`, `subsec:retrofit_metodo`, `subsec:validacao_conceitual`, `subsec:motive50`, `subsec:model50`, `subsec:sintese_comparativa`, `subsec:analise_*` — inofensivos, manter.
- **Estilo de referência cruzada misto:** "Seção~\ref{}" convive com "§\ref{}" (retrofit L69, discussao L8/14/20/26). Escolher um padrão (sugiro "Seção/Subseção" por extenso, mais comum em IEEE em português).
- **`\bibliographystyle{IEEEtran}` + chaves tipo `S1A03`:** funciona, mas atenção: as entradas com autores abreviados sem ponto ("M Alavi") renderizam como "M. Alavi" apenas se o BibTeX entender as iniciais — conferir saída no PDF final (formato `{M Alavi}` trata "M" como primeiro nome, OK).

---

## 6. Micro-ajustes Estruturais (Diffs)

### D1 — Conclusão: blindagem contra circularidade da validação (`conclusao.tex`, L9)

```diff
-Primeiramente, o escopo da pesquisa reveste-se de caráter teórico-conceitual, sendo a formulação do Modelo 3M 5.0 fundamentada em uma análise comparativa qualitativa frente aos dezenove modelos clássicos organizados por Mora-Mora et al. \cite{mora2025model}, sem ainda configurar validação empírica em contexto organizacional real.
+Primeiramente, o escopo da pesquisa reveste-se de caráter teórico-conceitual, sendo a formulação do Modelo 3M 5.0 fundamentada em uma análise comparativa qualitativa frente aos 19 modelos clássicos organizados por Mora-Mora et al. \cite{mora2025model}, sem ainda configurar validação empírica em contexto organizacional real. Ressalta-se, ainda, que tanto as cinco dimensões analíticas quanto a classificação ordinal de cobertura foram definidas e atribuídas pelos próprios autores, o que introduz risco de viés de confirmação; a corroboração da análise por painel independente de especialistas (por exemplo, via método Delphi) constitui etapa necessária de robustecimento.
```

### D2 — Discussão ou Conclusão: blindagem da dependência do GRAI (`conclusao.tex`, L9, após o trecho acima)

```diff
 Em segundo lugar, a operacionalidade do modelo esbarra em limitações técnicas inerentes aos próprios LLMs contemporâneos, [...]
+Em terceiro lugar, o backbone processual adotado apoia-se no modelo GRAI \cite{E0A18}, proposta recente e ainda carente de validação empírica independente; cabe registrar, contudo, que a arquitetura do 3M 5.0 não depende ontologicamente do GRAI, uma vez que o mapeamento das visões aos processos de GC de Prat \cite{prat2011hierarchical} e Stollenwerk \cite{stollenwerk2001gestao} permanece válido caso aquele framework venha a ser refinado pela literatura.
```

### D3 — Conclusão: blindagem da triagem automatizada (`conclusao.tex`, L9, no mesmo parágrafo de limitações)

```diff
+Por fim, embora a triagem automatizada por LLM no protocolo de scoping review mitigue a subjetividade humana, ela introduz vieses próprios do modelo avaliador; a ausência de dupla triagem humana por amostragem e de métricas de concordância humano-máquina (e.g., kappa de Cohen) limita a auditabilidade do processo de seleção.
```

### D4 — Conclusão: ecoar a contribuição metodológica prometida na Introdução (`conclusao.tex`, fim do L5 ou novo parágrafo curto antes das limitações)

```diff
+Na dimensão metodológica, o estudo formaliza o retrofit conceitual como estratégia replicável de evolução de teorias organizacionais frente a rupturas tecnológicas e documenta um pipeline agêntico de revisão de literatura (SLR-RAG) reutilizável em estudos secundários na área de Sistemas de Informação.
```

### D5 — Conclusão: harmonizar a glosa dos pilares (`conclusao.tex`, L3)

```diff
-Ao integrar de forma sistêmica os pilares de motivação (\textit{Motive 5.0}), entrega instrucional (\textit{Model 5.0}) e governança ética (\textit{Moment 5.0}),
+Ao integrar de forma sistêmica as visões de motivo (\textit{Motive 5.0}), de modelo (\textit{Model 5.0}) e de momento (\textit{Moment 5.0}),
```

### D6 — Normalização de Unicode arriscado (comando, executar na pasta `sections/`)

```bash
# U+2011 (non-breaking hyphen) -> hífen ASCII; U+2014 (em dash) -> ---
sed -i '' $'s/‑/-/g; s/—/---/g' sections/*.tex
```

### D7 — Preâmbulo (`main.tex`, L2)

```diff
 \usepackage[utf8]{inputenc}
+\usepackage[T1]{fontenc}
 \usepackage[brazilian]{babel}
```

### D8 — Bloco de autores (`main.tex`, L26–33)

```diff
 \author{
-    \IEEEauthorblockN{João Pedro Barbosa Martins}
-    \IEEEauthorblockN{Viviane Cunha Farias da Costa}
-    \IEEEauthorblockN{Emily Lopes}
+    \IEEEauthorblockN{João Pedro Barbosa Martins, Viviane Cunha Farias da Costa e Emily Lopes}
     \IEEEauthorblockA{\textit{Programa de Engenharia de Sistemas e Computação (PESC)} \\
     \textit{COPPE/UFRJ -- Universidade Federal do Rio de Janeiro} \\
     Rio de Janeiro, Brasil \\
-   {[joaopedro, vfarias, emlopes]}@cos.ufrj.br}}
+   \{joaopedro, vfarias, emlopes\}@cos.ufrj.br}}
```

### D9 — Citações quebradas (`analise.tex`, L33 e L40) — alternativa rápida caso não adicione as entradas ao .bib

```diff
-os 19 modelos catalogados (exemplificados por frameworks como \cite{S1A04, S1A09}) tratam a infraestrutura tecnológica
+os 19 modelos catalogados por Mora-Mora et al. \cite{mora2025model} tratam a infraestrutura tecnológica
```
```diff
-Nos modelos tradicionais de UC (como \cite{S1A10, S2A04}), as dinâmicas de aprendizagem
+Nos modelos tradicionais de UC \cite{mora2025model}, as dinâmicas de aprendizagem
```
*(Preferível, porém, adicionar as 4 entradas reais ao `references.bib` a partir do catálogo — os exemplos concretos enriquecem a análise.)*

### D10 — Chamada da Figura 1 (`referencial.tex`, L23)

```diff
-Para sistematizar essa interdependência [...] propuseram o Modelo 3M de Universidade Corporativa. Estruturado em três visões estratégicas interdependentes, o Modelo 3M estabelece:
+Para sistematizar essa interdependência [...] propuseram o Modelo 3M de Universidade Corporativa (Figura~\ref{fig:3m_original}). Estruturado em três visões estratégicas interdependentes, o Modelo 3M estabelece:
```

---

## 7. Síntese de prioridades

| Prioridade | Itens |
|---|---|
| **Bloqueante** | C1 (citações `[?]`), C2 (figura placeholder), C3 (números texto ≠ tabela) |
| **Alta** | C4 (listas de Prat), C5 (Alavi & Leidner), D1–D3 (blindagem de limitações), Abstract sem resultados |
| **Média** | P1–P3, P7, P8, P11 (typos com erro factual/terminológico), D4, D7, D8 |
| **Baixa** | P4–P6, P9, P10, P12–P15, D6, estilo §/Seção |

O artigo está conceitualmente maduro e bem amarrado — o fio condutor lacuna → retrofit → comparação → tensões → governança funciona. Os itens bloqueantes são todos mecânicos e resolvíveis em uma sessão de trabalho; as blindagens D1–D3 são o que separa um *major revision* de um *minor revision* no parecer real.
