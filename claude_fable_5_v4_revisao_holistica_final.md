# Parecer de Liberação de Submissão — 4ª Revisão Holística (Camera-Ready)

**Artigo:** Retrofit do Modelo 3M de Universidade Corporativa: Reinterpretação de seus Três Pilares à Luz da Inteligência Artificial
**Revisor:** Claude Fable 5 (papel: Editor-Chefe / Copyeditor Sênior)
**Data:** 2026-06-09
**Escopo:** `artigo final/main.tex`, `sections/*.tex` (7 arquivos), `references.bib`, `main.log`, `main.blg`, `main.bbl`

---

## 1. Status Go/No-Go

### Veredito: **GO CONDICIONADO** 🟡

O texto está maduro, sem overclaims, com metodologia blindada e prosa fluida. A compilação está limpa (zero warnings LaTeX, zero erros BibTeX, zero overfull boxes). O cross-check de citações é **1:1 perfeito**. Porém, a auditoria do `.bbl` revelou **um bloqueador real que as revisões anteriores não pegaram**: os campos `note = {ID do Catálogo: ...}` do `.bib` estão sendo **impressos na bibliografia do PDF final** (ex.: *"...Journal of Knowledge Management, 2019, iD do Catálogo: S1A01"*), expondo artefatos internos de rastreabilidade do pipeline em ~29 referências. Além disso, o `IEEEtran.bst` está rebaixando acrônimos não protegidos nos títulos (*ai*, *genai*, *seci*, *grai*, *chinese*, *european*...). Esses dois itens são de correção mecânica rápida, mas **impedem a submissão no estado atual do PDF**.

Após aplicar os diffs da Seção 3 e resolver as 3 pendências humanas da Seção 2, o artigo está **liberado para submissão**.

---

## 2. Pendências Humanas Rigorosas (intransferíveis ao autor)

| # | Pendência | Local | Criticidade |
|---|-----------|-------|-------------|
| **H1** | **Inserir o diagrama real da Figura 1**, substituindo o `\framebox` placeholder por `\includegraphics`. Sem isso, o PDF camera-ready sai com uma caixa vazia rotulada "Representação do Modelo 3M Original". | `sections/referencial.tex`, linhas 16–21 | 🔴 Bloqueante |
| **H2** | **Verificar a ordem dos autores do Modelo 3M original.** O texto diz consistentemente "Costa, **Souza** e **Oliveira** (2011)" (abstract, introdução, referencial, caption da Fig. 1), mas o `.bib` registra a ordem **Costa, Oliveira, Souza**. Uma das duas está errada — conferir no capítulo original da *Encyclopedia of Knowledge Management* (2ª ed., IGI Global) e alinhar texto e `.bib`. Como a coautora Viviane Farias é autora do trabalho original, a confirmação é trivial. | Texto (4 ocorrências) vs. `references.bib:1-11` | 🔴 Bloqueante |
| **H3** | **Confirmar paginação de Birkstedt et al. (2023).** O `.bib` registra *Internet Research*, vol. 33, n. 7, **pp. 1–40** — paginação suspeita de ser a do preprint/PDF avulso, não a do fascículo (este artigo costuma ser citado com paginação na faixa de centenas). Conferir na página oficial da Emerald (DOI 10.1108/INTR-01-2022-0042). | `references.bib:57-66` | 🟡 Recomendado |

Pendência opcional (decisão editorial do autor, não bloqueia): o **título** não menciona "3M 5.0" nem o qualificador "Generativa". Para maximizar impacto e indexação, considerar: *"Retrofit do Modelo 3M de Universidade Corporativa (3M 5.0): Reinterpretação de seus Três Pilares à Luz da Inteligência Artificial Generativa"*. O artigo usa "IA Generativa" como conceito central em todo o corpo; o título atual é o único lugar onde só aparece "Inteligência Artificial".

---

## 3. Micro-ajustes Finais (Diffs cirúrgicos)

### 3.1 Texto — 4 correções obrigatórias

**(a) `sections/analise.tex` (linha 35) — erro gramatical ("ao entrada"):**

```diff
- mas ainda responde de forma puramente reativa ao entrada do colaborador.
+ mas ainda responde de forma puramente reativa à entrada do colaborador.
```

**(b) `sections/retrofit.tex` (linha 4) — conjugação inexistente ("coevolvem"):**

```diff
- os processos de negócio e as estruturas de governança coevolvem a partir de
+ os processos de negócio e as estruturas de governança coevoluem a partir de
```

**(c) `sections/metodologia.tex` (linha 100) — frase duplicada (resíduo de edição da rodada anterior):**

```diff
- o framework proposto foi submetido a um procedimento de análise comparativa estruturada de cobertura teórica por meio de análise comparativa estruturada.
+ o framework proposto foi submetido a um procedimento de análise comparativa estruturada de cobertura teórica.
```

**(d) `sections/referencial.tex` (linha 23) — a Figura 1 não é referenciada em nenhum ponto do texto** (violação de norma IEEE: toda figura deve ser citada). Ancorar na primeira menção formal ao modelo:

```diff
- Para sistematizar essa interdependência entre a estratégia organizacional, a operação educacional e as flutuações do ambiente, Costa, Souza e Oliveira \cite{costa20113m} propuseram o Modelo 3M de Universidade Corporativa. Estruturado em três visões estratégicas interdependentes, o Modelo 3M estabelece:
+ Para sistematizar essa interdependência entre a estratégia organizacional, a operação educacional e as flutuações do ambiente, Costa, Souza e Oliveira \cite{costa20113m} propuseram o Modelo 3M de Universidade Corporativa, representado na Figura~\ref{fig:3m_original}. Estruturado em três visões estratégicas interdependentes, o Modelo 3M estabelece:
```

### 3.2 `references.bib` — 2 correções sistemáticas obrigatórias

**(e) Remover TODOS os `note = {ID do Catálogo: ...}` (≈29 ocorrências).** Eles são impressos no PDF (o `.bbl` atual confirma: *"2019, iD do Catálogo: S1A01"*). Exemplo do padrão (repetir para S1A01, S1A03, S1A06, E0A01, E0A06, E0A07, E0A10, E0A13, E0A15, E0A18, E0A20, E0A21, S1A04, S1A09, S1A10, S2A04, S4A01, S5A02, S5A03, S6A01, S6A02, S6A03, S7A04, S7A05, S7A06, S7A08, S8A04, S8A05, S8A07):

```diff
   doi = {10.1108/JKM-04-2018-0228},
-  url = {https://www.emerald.com/jkm/article/23/10/2086/264965},
-  note = {ID do Catálogo: S1A01}
+  url = {https://www.emerald.com/jkm/article/23/10/2086/264965}
 }
```

No caso de `S7A06`, preservar a marcação de preprint: `note = {Preprint}`.

Comando de verificação pós-edição: `grep -c "Catálogo" references.bib` deve retornar **0**.

**(f) Proteger acrônimos e nomes próprios com chaves `{}` nos títulos** — o `IEEEtran.bst` rebaixa tudo para minúsculas. Rebaixamentos confirmados no `.bbl` atual: *ai, Ai, genai, seci, grai, chinese, china, european, hrm, (eu)*. Correções por entrada:

```diff
 @article{S1A01,
-  title = {The knowledge management functions of corporate university and their evolution: case studies of two Chinese corporate universities},
+  title = {The knowledge management functions of corporate university and their evolution: case studies of two {Chinese} corporate universities},

 @article{S1A06,
-  title = {Lifelong learning in the workplace: the knowledge management role of corporate universities in China},
+  title = {Lifelong learning in the workplace: the knowledge management role of corporate universities in {China}},

 @article{jarrahi2023ai,
-  title = {Artificial intelligence and knowledge management: A partnership between human and AI},
+  title = {Artificial intelligence and knowledge management: A partnership between human and {AI}},

 @article{E0A06,
-  title = {Agentic AI and the Co-Evolution of Organizational Knowledge},
+  title = {Agentic {AI} and the Co-Evolution of Organizational Knowledge},

 @article{E0A10,
-  title = {Generative AI Meets Knowledge Management: Insights From Software Development Practices},
+  title = {Generative {AI} Meets Knowledge Management: Insights From Software Development Practices},

 @article{E0A15,
-  title = {Knowledge Management Perspective of Generative Artificial Intelligence (GenAI)},
+  title = {Knowledge Management Perspective of Generative Artificial Intelligence ({GenAI})},

 @article{E0A18,
-  title = {Knowledge management in the age of generative artificial intelligence – from SECI to GRAI},
+  title = {Knowledge management in the age of generative artificial intelligence -- from {SECI} to {GRAI}},

 @article{E0A20,
-  title = {Tacit Knowledge Management with Generative AI: Proposal of the GenAI SECI Model},
+  title = {Tacit Knowledge Management with Generative {AI}: Proposal of the {GenAI} {SECI} Model},

 @article{E0A21,
-  title = {Knowledge Management in a World of Generative AI: Impact and Implications},
+  title = {Knowledge Management in a World of Generative {AI}: Impact and Implications},

 @article{birkstedt2023ai,
-  title = {AI governance: Themes, knowledge gaps and future agendas},
+  title = {{AI} governance: Themes, knowledge gaps and future agendas},

 @article{S7A04,
-  title = {Human-Centric AI Governance in Digital HRM: A Conceptual Framework for Responsible Digital Business},
+  title = {Human-Centric {AI} Governance in Digital {HRM}: A Conceptual Framework for Responsible Digital Business},

 @article{S7A05,
-  title = {The AI Integration Framework - An Original Blueprint for Responsible AI Adoption and Governance},
+  title = {The {AI} Integration Framework -- An Original Blueprint for Responsible {AI} Adoption and Governance},

 @misc{S7A06,
-  title = {AI Governance by Design for Agentic Systems: A Framework for Responsible Development and Deployment},
+  title = {{AI} Governance by Design for Agentic Systems: A Framework for Responsible Development and Deployment},

 @article{S7A08,
-  title = {A choices framework for the responsible use of AI},
+  title = {A choices framework for the responsible use of {AI}},

 @phdthesis{S1A10,
-  title = {Path of corporate university to enable enterprises: Based on the best corporate universities in China},
+  title = {Path of corporate university to enable enterprises: Based on the best corporate universities in {China}},

 @techreport{european2021industry,
-  title = {Industry 5.0: Towards a sustainable, human-centric and resilient European industry},
+  title = {{Industry 5.0}: Towards a sustainable, human-centric and resilient {European} industry},

 @misc{european2024aiact,
-  title = {Regulation (EU) 2024/1689 of the European Parliament and of the Council of 13 June 2024 laying down harmonised rules on artificial intelligence (Artificial Intelligence Act)},
+  title = {Regulation ({EU}) 2024/1689 of the {European} {Parliament} and of the {Council} of 13 {June} 2024 laying down harmonised rules on artificial intelligence ({Artificial} {Intelligence} {Act})},

 @article{S8A05,
-  title = {Reskilling and Upskilling the Future-ready Workforce for Industry 4.0 and Beyond},
+  title = {Reskilling and Upskilling the Future-ready Workforce for {Industry 4.0} and Beyond},
```

(`ng2021conceptualizing` e `dellacqua2023navigating` já estão protegidos — manter.)

**(g) `E0A18` — DOI no campo errado** (está em `url`, deixando o campo `doi` vazio):

```diff
 @article{E0A18,
   journal = {VINE Journal of Information and Knowledge Management Systems},
   year = {2025},
-  url = {https://doi.org/10.1108/VJIKMS-10-2024-0357},
+  doi = {10.1108/VJIKMS-10-2024-0357},
```

### 3.3 Ajustes opcionais (não bloqueiam)

1. **`E0A15` e `E0A10`** apontam para a homepage do periódico (`https://aisel.aisnet.org/jais/`, `https://onlinelibrary.wiley.com/journal/10991441`) em vez do artigo. Substituir pela URL/DOI do artigo específico ou remover o campo `url`.
2. **Volume/número/páginas ausentes** em ~18 entradas (S1A01, S1A03, S1A06, E0A07, E0A21, S4A01, S6A02, S8A04, S8A05, mora — esta completa — etc.). O estilo IEEE tolera, mas completar onde o dado existir eleva a qualidade percebida. Não é exigência de desk-reject.
3. **`hyperref` com links coloridos** (azul/ciano/magenta): muitos veículos IEEE pedem links pretos no camera-ready. Se for o caso do alvo: `\hypersetup{colorlinks=true, allcolors=black}` (mantém sem caixas). Decisão dependente do template do veículo.
4. **Itálico inconsistente:** "scoping review" aparece como `\textit{scoping review}` na metodologia e sem itálico na conclusão (linha 11). Padronizar.
5. **Repetição enumerativa** em `retrofit.tex` linha 4: duas frases consecutivas listam "humanos, agentes de IA, processos de negócio e governança". Fundir em uma única frase deixaria mais elegante — cosmético.
6. **"liderada por Meister"** (referencial, linha 8) menciona autora clássica sem `\cite`. Aceitável como menção histórica genérica; se preferir blindar, adicionar a referência de Meister (1998) ao `.bib`.

---

## 4. Relatório de Cross-check: Citações vs. Referências

**Resultado: ÍNTEGRO — match 1:1 perfeito.**

| Verificação | Resultado |
|---|---|
| Chaves únicas citadas via `\cite{}` no texto | **45** |
| Entradas no `references.bib` | **45** |
| Citações sem entrada no `.bib` (quebrariam compilação) | **0** |
| Entradas no `.bib` nunca citadas (a remover) | **0** |
| Erros/warnings BibTeX (`main.blg`) | **0** |
| Warnings LaTeX, referências indefinidas, overfull boxes (`main.log`) | **0** |

Citações mais mobilizadas (sanidade da ancoragem teórica): `costa20113m` (13×), `mora2025model` (12×), `prat2011hierarchical` (11×), `E0A13`/`jarrahi2023ai`/`E0A18`/`stollenwerk2001gestao`/`S7A06` (8× cada) — distribuição coerente com a tese central do retrofit.

Metadados: além dos itens H3, 3.2(g) e 3.3(1–2) acima, nada inconsistente entre ano/DOI/veículo foi detectado. Nota: `S8A05` tem `year = {2024}` com DOI de 2022 — correto (online-first 2022, fascículo *Information Systems Frontiers* 2024); não alterar.

---

## 5. Compliance de Formato (IEEE) e Metadados

- **Classe e blocos:** `IEEEtran` modo `conference,a4paper` correto; `\IEEEauthorblockN/A` bem formados; e-mails em padrão de grupo `\{...\}@cos.ufrj.br` compilando corretamente. Sem anomalias no log.
- **Abstract:** **172 palavras** — dentro do limite usual de 200–250. Densidade adequada: contexto → proposta → método → resultado → contribuição, sem promessa empírica indevida ("oferece uma resposta teórica").
- **Keywords:** 5 termos, escopo correto.
- **Título:** correto formalmente; ver sugestão de impacto na Seção 2 (opcional).
- **Tabelas:** as três `table*` (triagem, síntese do retrofit, comparativo) compilam sem overflow; `booktabs` + `tabularx` consistentes.
- **Babel brazilian + IEEEtran:** convivência limpa (cabeçalhos traduzidos automaticamente).

---

## 6. Escaneamento Residual de IA e Fluidez

**Varredura de clichês:** zero ocorrências de "Em suma", "crucial", "É importante notar", "navegar neste cenário", "trama", "tapeçaria", "desvendar", "game-changer", "sinergia", "alavancar", "fomentar" e variantes. O texto está limpo.

**Fluidez dos remendos da 3ª rodada:** as adições sobre escala ordinal/viés de confirmação/Delphi e sobre kappa de Cohen (conclusão, parágrafo de limitações) estão **bem integradas** — leem-se como argumentação contínua, com conectivos naturais ("Ressalta-se, ainda", "cabe registrar, contudo"). A blindagem do GRAI ("não depende ontologicamente do GRAI") está elegante. Único resíduo de edição encontrado foi a frase duplicada da metodologia (diff 3.1c) — exatamente o tipo de cicatriz que esta passada deveria capturar.

**Repetição menor:** "eminentemente" aparece 2× (discussão §4 e conclusão §1) — tolerável; trocar uma ocorrência por "essencialmente" se desejar polimento extra.

---

## 7. Protocolo de Transposição para a Versão em Inglês (`artigo final en/`)

O diretório `artigo final en/` já contém esqueleto (`main.tex`, `sections/`, `references.bib`). Estratégia recomendada, **somente após** aplicar os diffs deste parecer na versão PT (fonte única de verdade):

1. **Congelar a versão PT** (tag/cópia datada) para que a tradução parta de baseline imutável.
2. **Traduzir seção a seção** (1 arquivo `.tex` por vez), preservando 100% da estrutura LaTeX: labels, `\cite`, `\ref`, tabelas e ambientes idênticos — traduzir apenas o conteúdo textual. Isso permite diff estrutural PT↔EN automatizado ao final (`grep -o '\\cite{[^}]*}' | sort | diff`).
3. **Glossário terminológico fixo** antes de começar, para consistência: Universidade Corporativa→Corporate University; Gestão do Conhecimento→Knowledge Management; retrofit conceitual→conceptual retrofit; sensoriamento/sensing contínuo→continuous sensing; laboratório vivo→living lab; andaimes cognitivos→cognitive scaffolding; governança algorítmica adaptativa→adaptive algorithmic governance; aprendizagem no fluxo de trabalho→learning in the flow of work; letramento em IA→AI literacy; visões de motivo/modelo/momento→Motive/Model/Moment Visions (já em inglês — a tradução simplifica esses trechos).
4. **Atenção aos trechos que mudam de natureza na tradução:** citações diretas com aspas latinas ``...''; termos que estavam em `\textit{}` por serem estrangeirismos (prompt, upskilling, scaffolding) deixam de precisar de itálico em EN — remover caso a caso; o en-dash "–" da E0A18 e travessões "---".
5. **`references.bib` é compartilhável quase integralmente** — apenas `stollenwerk2001gestao` (obra em PT) ganha `note = {In Portuguese}`, prática padrão IEEE.
6. **Mudar `babel` para `english`** no `main.tex` EN e traduzir abstract/keywords por último, com o corpo já estabilizado.
7. **QA final EN:** rodar o mesmo checklist desta 4ª revisão (cross-check 1:1, log limpo, contagem do abstract, varredura de clichês — em inglês: "delve", "crucial", "landscape", "moreover", "it is important to note").

Recomendo registrar a tradução como 5ª rodada com parecer próprio (`*_v5_traducao_en.md`).

---

## 8. Síntese Executiva

| Categoria | Status |
|---|---|
| Compilação (log/blg) | ✅ Limpa |
| Cross-check citações ↔ `.bib` | ✅ 1:1 perfeito (45/45) |
| Abstract (172 palavras) e keywords | ✅ Conforme |
| Clichês de IA / remendos textuais | ✅ Limpo (1 frase duplicada → diff 3.1c) |
| Gramática residual | ⚠️ 2 typos (diffs 3.1a–b) |
| Figura 1 | 🔴 Placeholder + nunca referenciada (H1 + diff 3.1d) |
| `.bib`: notas internas impressas no PDF | 🔴 ~29 entradas (diff 3.2e) |
| `.bib`: acrônimos rebaixados pelo BST | 🔴 ~18 títulos (diff 3.2f) |
| Ordem de autores do 3M original | 🟡 Verificar (H2) |

**Sequência de liberação:** aplicar diffs 3.1–3.2 → resolver H1/H2/H3 → recompilar (2× pdflatex + bibtex) → conferir visualmente a seção de Referências no PDF (sem "iD do Catálogo", acrônimos corretos) → **submeter**.
