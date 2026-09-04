# Parecer Consolidado V4 - Revisão Holística Final Camera-Ready

**Artigo:** Retrofit do Modelo 3M de Universidade Corporativa: Reinterpretação de seus Três Pilares à Luz da Inteligência Artificial  
**Pareceres consolidados:** GPT-5 Codex V4 + Claude Fable 5 V4  
**Versão auditada:** `artigo final/`  
**Data da consolidação:** 2026-06-11

## 1. Decisões Editoriais do Autor

As divergências entre os dois pareceres foram resolvidas da seguinte forma:

1. **Título:** manter exatamente o título atual. Nenhuma alteração deve ser proposta nesta rodada.
2. **Abstract:** substituir o texto atual por uma versão com **250 palavras exatas**.
3. **Meister:** manter a menção e adicionar a obra de Jeanne C. Meister ao `.bib` e ao texto.
4. **Hyperlinks:** utilizar `hidelinks` no PDF camera-ready.
5. **Ordem dos autores do Modelo 3M:** usar **Costa, Oliveira e Souza**, conforme a ordem registrada pelo Crossref para o DOI do capítulo original.
6. **Birkstedt et al. (2023):** corrigir a paginação, mas tratar o item como **não bloqueante**.

## 2. Status Go/No-Go

**Veredito consolidado: NO-GO técnico no estado atual; GO condicionado após as correções bloqueantes.**

O conteúdo acadêmico está maduro, sem overclaims relevantes, com metodologia defensável e adições sobre avaliação ordinal, GRAI, triagem por LLM e kappa de Cohen bem integradas. O manuscrito ainda não está camera-ready por quatro razões objetivas:

1. a Figura 1 permanece como `\framebox` placeholder;
2. 29 campos internos `ID do Catálogo` são impressos na bibliografia final;
3. o `IEEEtran.bst` rebaixa acrônimos e nomes próprios não protegidos nos títulos;
4. o abstract atual não atende à exigência autoral de 250 palavras.

A compilação explícita com `pdflatex` foi concluída sem erro fatal, sem citações indefinidas, sem referências indefinidas e sem `Overfull`. Permanecem avisos `Underfull`, especialmente em tabelas e na paginação final. O PDF possui 17 páginas.

## 3. Pendências Humanas Rigorosas

| Prioridade | Ação | Criticidade |
|---|---|---|
| H1 | Inserir o diagrama real da Figura 1, substituindo o `\framebox`. | Bloqueante |
| H2 | Confirmar direitos de reprodução/adaptação e manter crédito explícito a Costa, Oliveira e Souza. | Bloqueante |
| H3 | Confirmar o limite de páginas do veículo. O PDF atual possui 17 páginas. | Bloqueante se o limite for inferior |
| H4 | Inspecionar e equalizar visualmente as colunas da última página, conforme lembrete do `IEEEtran`. | Camera-ready |
| H5 | Revisar visualmente a bibliografia após recompilar, garantindo ausência de `ID do Catálogo` e preservação dos acrônimos. | Bloqueante |

## 4. Abstract Obrigatório com 250 Palavras

O abstract atual possui aproximadamente 172 palavras pelo critério de separação por espaços. A contagem de 177 encontrada no parecer GPT decorreu de tokenização que separava números e alguns termos compostos. Para eliminar a divergência, este consolidado adota a contagem editorial comum por unidades separadas por espaço.

O texto abaixo possui **250 palavras exatas por esse critério**:

```diff
diff --git a/artigo final/main.tex b/artigo final/main.tex
@@
 \begin{abstract}
-A difusão da Inteligência Artificial (IA) Generativa altera o papel das Universidades Corporativas (UCs) na Gestão do Conhecimento ao deslocar a tecnologia de suporte informacional para mediação ativa dos processos de aprendizagem. Este trabalho propõe um retrofit conceitual do Modelo 3M de Universidade Corporativa, formulado por Costa, Souza e Oliveira (2011), integrando tecnologias de IA como infraestrutura operacional e como agente organizacional no ecossistema de aprendizagem. A partir de uma scoping review assistida por pipeline SLR-RAG e de uma avaliação comparativa de cobertura conceitual, estruturam-se os pilares Motive 5.0 (sensoriamento semântico contínuo de competências), Model 5.0 (laboratório vivo apoiado por Geração Aumentada por Recuperação e grafos de conhecimento) e Moment 5.0 (governança de IA como processo adaptativo). A comparação frente aos modelos de UC catalogados na literatura indica que o 3M 5.0 explicita dimensões ausentes ou periféricas nos modelos existentes, especialmente agência ativa de IA, simbiose humano-IA e governança algorítmica. O modelo oferece, assim, uma resposta teórica à lacuna de integração da IA e da Indústria 5.0 à arquitetura interna da UC.
+A difusão da Inteligência Artificial Generativa transforma o papel das Universidades Corporativas na Gestão do Conhecimento ao deslocar a tecnologia de suporte informacional para a mediação ativa dos processos de aprendizagem. Este estudo propõe um retrofit conceitual do Modelo 3M de Universidade Corporativa, preservando suas visões de Motive, Model e Moment e integrando a Inteligência Artificial simultaneamente como infraestrutura operacional e agente organizacional. Adota-se uma abordagem conceitual-construtiva, apoiada por uma revisão de escopo assistida pelo pipeline SLR-RAG e por uma avaliação comparativa de cobertura conceitual frente a dezenove modelos de Universidades Corporativas catalogados na literatura. O retrofit estrutura três pilares: Motive 5.0, dedicado ao sensoriamento semântico contínuo de competências; Model 5.0, configurado como laboratório vivo apoiado por Geração Aumentada por Recuperação, grafos de conhecimento e aprendizagem no fluxo de trabalho; e Moment 5.0, orientado à governança algorítmica adaptativa, à integridade informacional e à contestabilidade humana. A análise indica que o Modelo 3M 5.0 explicita dimensões ausentes ou periféricas nos modelos existentes, especialmente agência ativa de Inteligência Artificial, simbiose humano-IA, ciclos dinâmicos de conhecimento e governança algorítmica. A contribuição é teórica e não constitui validação empírica de efetividade organizacional. O estudo também delimita riscos associados à vigilância de competências, à dependência cognitiva, às alucinações semânticas e aos vieses presentes em sistemas agênticos corporativos contemporâneos. Como resultado, o modelo oferece uma arquitetura conceitual para orientar a evolução responsável das Universidades Corporativas diante da Inteligência Artificial Generativa e da Indústria 5.0, preservando o julgamento humano, a segurança psicológica e a aprendizagem organizacional contínua.
 \end{abstract}
```

O novo abstract preserva a natureza teórica do estudo e evita apresentar a comparação conceitual como validação empírica.

## 5. Compliance IEEE e LaTeX

### 5.1 Estrutura conforme

- `\documentclass[conference,a4paper]{IEEEtran}`: conforme.
- Bloco único `\IEEEauthorblockN/A`: adequado para autores com a mesma afiliação.
- E-mails agrupados: sintaticamente válidos.
- `\bibliographystyle{IEEEtran}`: conforme.
- Cinco keywords: quantidade e escopo adequados.
- Título: preservado por decisão do autor.

### 5.2 Ocultar links coloridos

```diff
diff --git a/artigo final/main.tex b/artigo final/main.tex
@@
-\usepackage{hyperref}
+\usepackage[hidelinks]{hyperref}
@@
-\hypersetup{
-    colorlinks=true,
-    linkcolor=blue,
-    filecolor=magenta,
-    urlcolor=cyan,
-    citecolor=blue,
-}
+\hypersetup{hidelinks}
```

### 5.3 Figura 1

```diff
diff --git a/artigo final/sections/referencial.tex b/artigo final/sections/referencial.tex
@@
 \begin{figure}[h]
 \centering
-\framebox[0.45\textwidth]{\rule{0pt}{4cm} Representação do Modelo 3M Original}
-\caption{Representação Sistêmica do Modelo 3M Original (Adaptado de Costa, Souza e Oliveira, 2011)}
+\includegraphics[width=0.45\textwidth]{figures/modelo_3m_original}
+\caption{Representação sistêmica do Modelo 3M original (adaptado de \cite{costa20113m})}
 \label{fig:3m_original}
 \end{figure}
@@
-Para sistematizar essa interdependência entre a estratégia organizacional, a operação educacional e as flutuações do ambiente, Costa, Souza e Oliveira \cite{costa20113m} propuseram o Modelo 3M de Universidade Corporativa.
+Para sistematizar essa interdependência entre a estratégia organizacional, a operação educacional e as flutuações do ambiente, Costa, Oliveira e Souza \cite{costa20113m} propuseram o Modelo 3M de Universidade Corporativa, representado na Figura~\ref{fig:3m_original}.
```

## 6. Correções Textuais Obrigatórias

### 6.1 Ordem dos autores do Modelo 3M

O Crossref confirma a ordem: **Viviane Cunha Farias da Costa, Jonice Oliveira e Jano Moreira de Souza**. Corrigir as menções narrativas remanescentes:

```diff
diff --git a/artigo final/sections/introducao.tex b/artigo final/sections/introducao.tex
@@
-Em 2011, Costa, Souza e Oliveira \cite{costa20113m} propuseram o Modelo 3M
+Em 2011, Costa, Oliveira e Souza \cite{costa20113m} propuseram o Modelo 3M
```

O abstract proposto não contém a enumeração nominal, portanto não requer ajuste adicional.

### 6.2 Erros gramaticais e resíduo de edição

```diff
diff --git a/artigo final/sections/analise.tex b/artigo final/sections/analise.tex
@@
-mas ainda responde de forma puramente reativa ao entrada do colaborador.
+mas ainda responde de forma puramente reativa à entrada do colaborador.
```

```diff
diff --git a/artigo final/sections/retrofit.tex b/artigo final/sections/retrofit.tex
@@
-os processos de negócio e as estruturas de governança coevolvem a partir de
+os processos de negócio e as estruturas de governança coevoluem a partir de
```

```diff
diff --git a/artigo final/sections/metodologia.tex b/artigo final/sections/metodologia.tex
@@
-o framework proposto foi submetido a um procedimento de análise comparativa estruturada de cobertura teórica por meio de análise comparativa estruturada.
+o framework proposto foi submetido a um procedimento de análise comparativa estruturada de cobertura teórica.
@@
-\item \textbf{Simbiose Homem-IA}:
+\item \textbf{Simbiose Humano-IA}:
```

### 6.3 Citação de Meister

```diff
diff --git a/artigo final/sections/referencial.tex b/artigo final/sections/referencial.tex
@@
-A literatura clássica, liderada por Meister, descreve a UC como uma ferramenta estratégica centralizada para o desenvolvimento do capital intelectual corporativo.
+A literatura clássica, liderada por Meister \cite{meister1998corporate}, descreve a UC como uma ferramenta estratégica centralizada para o desenvolvimento do capital intelectual corporativo.
```

Entrada validada em catálogo bibliográfico:

```diff
diff --git a/artigo final/references.bib b/artigo final/references.bib
@@
+@book{meister1998corporate,
+  author    = {Meister, Jeanne C.},
+  title     = {Corporate Universities: Lessons in Building a World-Class Work Force},
+  edition   = {Rev. and updated ed.},
+  publisher = {McGraw-Hill},
+  address   = {New York},
+  year      = {1998},
+  isbn      = {978-0-7863-0787-6}
+}
```

Após essa inclusão, o cross-check esperado passa de **45/45 para 46/46**.

## 7. Higiene Obrigatória do BibTeX

### 7.1 Remover identificadores internos

Existem 29 campos `note` com `ID do Catálogo`. O `IEEEtran.bst` imprime esses campos no PDF final. Remover todos os identificadores internos. Em `S7A06`, preservar apenas `note = {Preprint}`.

Exemplo:

```diff
   doi = {10.1108/JKM-04-2018-0228},
-  url = {https://www.emerald.com/jkm/article/23/10/2086/264965},
-  note = {ID do Catálogo: S1A01}
+  url = {https://www.emerald.com/jkm/article/23/10/2086/264965}
```

Verificação obrigatória após a edição:

```bash
rg -n 'ID do Catálogo' references.bib
```

O comando não deve retornar ocorrências.

### 7.2 Proteger acrônimos e nomes próprios

O `.bbl` atual confirma rebaixamentos como `ai`, `genai`, `seci`, `grai`, `chinese`, `european`, `hrm` e `eu`. Proteger com chaves nos títulos das entradas afetadas:

- `jarrahi2023ai`: `{AI}`.
- `E0A06`, `E0A10`, `E0A20`, `E0A21`: `{AI}`.
- `E0A15`: `{GenAI}`.
- `E0A18`: `{SECI}` e `{GRAI}`.
- `birkstedt2023ai`, `S7A04`, `S7A05`, `S7A06`, `S7A08`: `{AI}`; em `S7A04`, também `{HRM}`.
- `S1A01`, `S1A06`, `S1A10`: `{Chinese}` ou `{China}`.
- `european2021industry`: `{Industry 5.0}` e `{European}`.
- `european2024aiact`: `{EU}`, `{European Parliament}`, `{Council}` e `{Artificial Intelligence Act}`.
- `S8A05`: `{Industry 4.0}`.

Exemplo crítico:

```diff
diff --git a/artigo final/references.bib b/artigo final/references.bib
@@
-  title = {Knowledge management in the age of generative artificial intelligence – from SECI to GRAI},
+  title = {Knowledge management in the age of generative artificial intelligence -- from {SECI} to {GRAI}},
```

### 7.3 DOI e caracteres problemáticos

```diff
diff --git a/artigo final/references.bib b/artigo final/references.bib
@@
 @article{E0A18,
-  author = {K Böhm and S Durst},
+  author = {K B{\"o}hm and S Durst},
@@
-  url = {https://doi.org/10.1108/VJIKMS-10-2024-0357},
+  doi = {10.1108/VJIKMS-10-2024-0357},
+  url = {https://doi.org/10.1108/VJIKMS-10-2024-0357},
@@
-  title = {The Impact of Artificial Intelligence on Workers’ Skills: Upskilling and Reskilling in Organisations},
+  title = {The Impact of Artificial Intelligence on Workers' Skills: Upskilling and Reskilling in Organisations},
```

### 7.4 Birkstedt et al. - não bloqueante

O Crossref informa páginas **133--167**. Corrigir quando aplicar o lote bibliográfico, mas manter a classificação não bloqueante definida pelo autor.

```diff
diff --git a/artigo final/references.bib b/artigo final/references.bib
@@
-  pages = {1--40},
+  pages = {133--167},
```

### 7.5 Melhorias bibliográficas opcionais

- `E0A10` e `E0A15` apontam para homepages dos periódicos; substituir pela URL específica ou remover a URL.
- Completar volume, número e páginas onde esses dados estiverem disponíveis.
- `E0A06` permanece uma entrada recente sem DOI ou URL e deve ser verificada antes da versão definitiva.
- Padronizar `scoping review` em itálico ou em redondo ao longo do texto.

## 8. Cross-Check de Citações e Referências

Estado atual:

| Verificação | Resultado |
|---|---:|
| Chaves únicas citadas | 45 |
| Entradas no `.bib` | 45 |
| Citações sem entrada | 0 |
| Entradas não citadas | 0 |
| Labels referenciados inexistentes | 0 |
| Erros do BibTeX | 0 |

Estado esperado após Meister:

| Verificação | Resultado esperado |
|---|---:|
| Chaves únicas citadas | 46 |
| Entradas no `.bib` | 46 |
| Citações sem entrada | 0 |
| Entradas não citadas | 0 |

## 9. Escaneamento Residual de IA e Fluidez

- Não foram encontrados `TODO`, `FIXME`, `XXX`, `\todo`, `\marginpar` ou blocos de comentário residuais.
- Não foram encontrados "Em suma", "Crucial", "É importante notar", "Navegar neste cenário" ou "Trama".
- Há duas ocorrências de "Em síntese". São aceitáveis e sua substituição é apenas cosmética.
- As limitações sobre escala ordinal, viés de confirmação, Delphi, GRAI, dupla triagem humana e kappa de Cohen estão integradas com fluidez.
- A repetição de "eminentemente" e a enumeração duplicada no início de `retrofit.tex` são ajustes opcionais.

## 10. Protocolo para a Versão em Inglês

1. Aplicar integralmente as correções na versão portuguesa.
2. Congelar a versão portuguesa como fonte única de verdade.
3. Sincronizar estrutura, labels, citações, tabelas e figuras com `artigo final en/`.
4. Usar glossário fixo: Corporate University, Knowledge Management, conceptual retrofit, continuous sensing, living lab, adaptive algorithmic governance, learning in the flow of work e AI literacy.
5. Remover itálico de estrangeirismos que se tornarem termos correntes em inglês.
6. Compartilhar o `.bib` já higienizado, adicionando `note = {In Portuguese}` apenas quando pertinente a obras em português.
7. Alterar `babel` para `english` e traduzir abstract e keywords após estabilizar o corpo.
8. Repetir cross-check 1:1 e compilação completa na versão inglesa.

## 11. Sequência de Liberação

1. Substituir a Figura 1 e citá-la no texto.
2. Aplicar o abstract de 250 palavras.
3. Adicionar Meister e corrigir a ordem Costa, Oliveira e Souza.
4. Remover os 29 IDs internos e proteger acrônimos no `.bib`.
5. Aplicar `hidelinks`.
6. Corrigir os três erros textuais obrigatórios.
7. Recompilar com `pdflatex`, `bibtex`, `pdflatex`, `pdflatex`.
8. Confirmar 46/46 no cross-check.
9. Inspecionar referências, Figura 1, tabelas e última página.
10. Confirmar o limite de 17 páginas e liberar para submissão.

## 12. Fontes de Verificação Externa

- [Crossref - capítulo original do Modelo 3M](https://api.crossref.org/works/10.4018/978-1-59904-931-1.ch012): confirma Costa, Oliveira e Souza.
- [Crossref - Birkstedt et al.](https://api.crossref.org/works/10.1108/INTR-01-2022-0042): confirma páginas 133--167.
- [Open Library - Corporate Universities](https://openlibrary.org/books/OL685942M): confirma autora, subtítulo, edição, editora, local, ano e ISBN da obra de Meister.

**Conclusão:** o artigo está academicamente pronto, mas somente deve receber GO após a substituição da Figura 1, a higienização da bibliografia, a aplicação do abstract de 250 palavras e a validação final do PDF.
