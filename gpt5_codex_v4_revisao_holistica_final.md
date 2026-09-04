# Parecer V4 - Revisao Holistica Final Camera-Ready

Artigo: "Retrofit do Modelo 3M de Universidade Corporativa (3M 5.0) com IA Generativa"  
Versao auditada: `artigo final/`  
Modelo revisor: GPT-5 Codex  
Data da validacao local: 2026-06-09

## 1. Status Go/No-Go

**Veredito do copyeditor: NO-GO tecnico para submissao imediata no estado atual; GO condicional apos correcoes finais de camera-ready.**

O texto esta substancialmente maduro, metodologicamente defensavel e sem problemas estruturais graves de citacao. A versao portuguesa pode ser considerada a versao-fonte definitiva para a traducao/adaptacao em ingles. No entanto, ainda ha bloqueios formais de submissao:

1. a Figura 1 ainda e um placeholder `\framebox`, portanto o PDF nao esta camera-ready;
2. o PDF gerado tem 17 paginas, exigindo verificacao do limite real de paginas do periodico/congresso alvo;
3. o aviso padrao do `IEEEtran` exige revisao visual/equalizacao manual da ultima pagina;
4. ha microajustes de LaTeX, estilo e BibTeX recomendados antes da geracao final do PDF.

Resultado objetivo da compilacao local:

- `pdflatex -interaction=nonstopmode -halt-on-error main.tex`: compilou com sucesso.
- Saida: `main.pdf`, 17 paginas.
- Sem `Overfull`, sem erro fatal, sem citacao indefinida, sem referencia indefinida.
- Avisos restantes: `Underfull \hbox` em tabelas/trechos estreitos e `Underfull \vbox` na paginacao final.
- Observacao IEEEtran: equalizar manualmente as duas colunas da ultima pagina antes do camera-ready.

## 2. Compliance IEEE, Metadados e Abstract

### Classe e estrutura

- `\documentclass[conference,a4paper]{IEEEtran}` esta correto para conferencia IEEE em A4.
- `\bibliographystyle{IEEEtran}` e `\bibliography{references}` estao corretos.
- O bloco de autores em um unico `\IEEEauthorblockN` + `\IEEEauthorblockA` e aceitavel porque os autores compartilham a mesma afiliacao.
- O bloco de e-mail com `\{joaopedro, vfarias, emlopes\}@cos.ufrj.br` e sintaticamente valido.

### Titulo

O titulo atual e formalmente correto, mas perde forca de indexacao porque usa "Inteligencia Artificial" de modo amplo e nao sinaliza explicitamente "IA Generativa" nem "3M 5.0" no titulo. Recomendo, sem obrigatoriedade, trocar para uma forma mais aderente ao conteudo:

```diff
diff --git a/artigo final/main.tex b/artigo final/main.tex
@@
-\title{Retrofit do Modelo 3M de Universidade Corporativa: Reinterpretação de seus Três Pilares à Luz da Inteligência Artificial}
+\title{Retrofit do Modelo 3M de Universidade Corporativa para IA Generativa: Proposta do 3M 5.0}
```

### Abstract

- Contagem aproximada: **177 palavras**.
- Esta abaixo dos limites usuais de 200-250 palavras.
- Densidade boa: problema, metodo, proposta tripartite e contribuicao aparecem no resumo.
- Ajuste opcional: remover a marcacao autor-data dentro do abstract para evitar hibridismo com o estilo numerico IEEE.

```diff
diff --git a/artigo final/main.tex b/artigo final/main.tex
@@
-Este trabalho propõe um retrofit conceitual do Modelo 3M de Universidade Corporativa, formulado por Costa, Souza e Oliveira (2011), integrando tecnologias de IA como infraestrutura operacional e como agente organizacional no ecossistema de aprendizagem.
+Este trabalho propõe um retrofit conceitual do Modelo 3M de Universidade Corporativa, originalmente formulado como uma estrutura tripartite, integrando tecnologias de IA como infraestrutura operacional e como agente organizacional no ecossistema de aprendizagem.
```

### Hyperlinks

Para camera-ready IEEE, evitar links/citacoes coloridos no PDF final. O atual `\hypersetup` gera links azuis/ciano. Recomendo ocultar cores.

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

## 3. Pendencias Humanas Rigorosas

1. **Substituir a Figura 1 real.**  
   Em `artigo final/sections/referencial.tex`, linhas 16-20, ainda existe:
   `\framebox[0.45\textwidth]{\rule{0pt}{4cm} Representação do Modelo 3M Original}`.  
   Inserir o diagrama final do Modelo 3M original e remover a caixa placeholder.

2. **Conferir direitos/credito da Figura 1.**  
   Se for adaptada de Costa, Souza e Oliveira (2011), manter citacao IEEE na legenda. Se for redesenhada pelo autor, explicitar "adaptado de \cite{costa20113m}".

3. **Verificar limite de paginas do venue.**  
   O PDF local gerado tem 17 paginas. Isso pode exceder limites comuns de conferencia IEEE. Para periodico, pode ser aceitavel; para congresso, precisa confirmacao antes de submeter.

4. **Equalizar visualmente a ultima pagina.**  
   O `IEEEtran` emitiu o lembrete padrao para equalizar manualmente as duas colunas da ultima pagina antes do camera-ready.

5. **Resolver metadados bibliograficos fracos.**  
   Especialmente `E0A06`, que aparece como artigo sem DOI nem URL. Livros/classicos sem DOI sao aceitaveis; artigo recente sem DOI/URL e fragil para auditoria.

## 4. Placeholders, Comentarios e Elementos Visuais

Resultado da varredura:

- `TODO`, `FIXME`, `XXX`, `\todo`, `\marginpar`, `\iffalse`, `comment`: nenhum encontrado.
- Comentarios `%` residuais nos arquivos auditados: nenhum encontrado.
- Placeholders visuais: **1 encontrado**, Figura 1 em `referencial.tex`.
- Arquivos de imagem em `artigo final/`: nenhum encontrado alem de `main.pdf`.

Diff recomendado para a Figura 1 e legenda:

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
```

Tambem recomendo referenciar a figura no corpo do texto:

```diff
diff --git a/artigo final/sections/referencial.tex b/artigo final/sections/referencial.tex
@@
-Para sistematizar essa interdependência entre a estratégia organizacional, a operação educacional e as flutuações do ambiente, Costa, Souza e Oliveira \cite{costa20113m} propuseram o Modelo 3M de Universidade Corporativa. Estruturado em três visões estratégicas interdependentes, o Modelo 3M estabelece:
+Para sistematizar essa interdependência entre a estratégia organizacional, a operação educacional e as flutuações do ambiente, Costa, Souza e Oliveira \cite{costa20113m} propuseram o Modelo 3M de Universidade Corporativa (Figura~\ref{fig:3m_original}). Estruturado em três visões estratégicas interdependentes, o Modelo 3M estabelece:
```

## 5. Auditoria Cega de Citacoes vs. BibTeX

Resultado automatizado:

- Chaves citadas unicas no texto: **45**.
- Entradas no `references.bib`: **45**.
- Citacoes no texto sem entrada `.bib`: **nenhuma**.
- Entradas `.bib` nao citadas: **nenhuma**.
- Labels referenciados inexistentes: **nenhum**.
- BibTeX compilou com `IEEEtran.bst` sem warnings.

Chaves citadas:

`E0A01`, `E0A06`, `E0A07`, `E0A10`, `E0A13`, `E0A15`, `E0A18`, `E0A20`, `E0A21`, `S1A01`, `S1A03`, `S1A04`, `S1A06`, `S1A09`, `S1A10`, `S2A04`, `S4A01`, `S5A02`, `S5A03`, `S6A01`, `S6A02`, `S6A03`, `S7A04`, `S7A05`, `S7A06`, `S7A08`, `S8A04`, `S8A05`, `S8A07`, `argyris1978organizational`, `bender2021stochastic`, `birkstedt2023ai`, `costa20113m`, `dellacqua2023navigating`, `edmondson1999psychological`, `european2021industry`, `european2024aiact`, `foucault1975surveiller`, `jarrahi2023ai`, `mora2025model`, `ng2021conceptualizing`, `orlikowski2007sociomaterial`, `pan2024unifying`, `prat2011hierarchical`, `stollenwerk2001gestao`.

Entradas sem DOI nem URL:

- `stollenwerk2001gestao` - aceitavel para capitulo/livro nacional antigo, se dados editoriais estiverem corretos.
- `argyris1978organizational` - aceitavel para livro.
- `foucault1975surveiller` - aceitavel para livro.
- `E0A06` - **fraco**: artigo recente sem DOI/URL. Recomendo enriquecer ou substituir por fonte com metadados verificaveis.

Entradas com DOI inferivel mas nao normalizado:

- `E0A18` tem URL `https://doi.org/10.1108/VJIKMS-10-2024-0357`, mas nao possui campo `doi`.

Diff BibTeX recomendado:

```diff
diff --git a/artigo final/references.bib b/artigo final/references.bib
@@
-  author = {K Böhm and S Durst},
-  title = {Knowledge management in the age of generative artificial intelligence – from SECI to GRAI},
+  author = {K B{\"o}hm and S Durst},
+  title = {Knowledge management in the age of generative artificial intelligence -- from SECI to GRAI},
   journal = {VINE Journal of Information and Knowledge Management Systems},
   year = {2025},
+  doi = {10.1108/VJIKMS-10-2024-0357},
   url = {https://doi.org/10.1108/VJIKMS-10-2024-0357},
@@
-  title = {The Impact of Artificial Intelligence on Workers’ Skills: Upskilling and Reskilling in Organisations},
+  title = {The Impact of Artificial Intelligence on Workers' Skills: Upskilling and Reskilling in Organisations},
```

## 6. Microajustes Textuais e LaTeX Recomendados

### Remover autor nomeado sem citacao direta

O trecho "liderada por Meister" em `referencial.tex` introduz um nome classico sem entrada no BibTeX. Para nao adicionar uma nova referencia nesta etapa, a solucao mais limpa e remover o nome.

```diff
diff --git a/artigo final/sections/referencial.tex b/artigo final/sections/referencial.tex
@@
-A literatura clássica, liderada por Meister, descreve a UC como uma ferramenta estratégica centralizada para o desenvolvimento do capital intelectual corporativo.
+A literatura clássica descreve a UC como uma ferramenta estratégica centralizada para o desenvolvimento do capital intelectual corporativo.
```

### Corrigir repeticao metodologica

```diff
diff --git a/artigo final/sections/metodologia.tex b/artigo final/sections/metodologia.tex
@@
-Para avaliar a contribuição conceitual do Modelo 3M 5.0 e justificar sua necessidade teórica frente aos modelos existentes, o framework proposto foi submetido a um procedimento de análise comparativa estruturada de cobertura teórica por meio de análise comparativa estruturada.
+Para avaliar a contribuição conceitual do Modelo 3M 5.0 e justificar sua necessidade teórica frente aos modelos existentes, o framework proposto foi submetido a um procedimento de análise comparativa estruturada de cobertura teórica.
```

### Padronizar "Humano-IA"

```diff
diff --git a/artigo final/sections/metodologia.tex b/artigo final/sections/metodologia.tex
@@
-\item \textbf{Simbiose Homem-IA}: Grau de integração colaborativa de tomadas de decisão e processos de aprendizagem mútua (simbiose cognitivo-computacional).
+\item \textbf{Simbiose Humano-IA}: Grau de integração colaborativa de tomadas de decisão e processos de aprendizagem mútua (simbiose cognitivo-computacional).
```

### Corrigir concordancia gramatical

```diff
diff --git a/artigo final/sections/analise.tex b/artigo final/sections/analise.tex
@@
-Sob a perspectiva de ferramenta, a cobertura é qualificada como parcial: a tecnologia funciona como um mecanismo avançado de processamento semântico e recuperação baseada em RAG, mas ainda responde de forma puramente reativa ao entrada do colaborador.
+Sob a perspectiva de ferramenta, a cobertura é qualificada como parcial: a tecnologia funciona como um mecanismo avançado de processamento semântico e recuperação baseada em RAG, mas ainda responde de forma puramente reativa à entrada do colaborador.
```

### Reduzir marcadores genericos de transicao

Foram encontrados dois usos de "Em síntese". Nao e erro, mas pode ser substituido por transicoes mais precisas.

```diff
diff --git a/artigo final/sections/analise.tex b/artigo final/sections/analise.tex
@@
-Em síntese, a análise comparativa demonstra que o Modelo 3M 5.0 supera a visão instrumentalista das tecnologias de informação que caracteriza os 19 modelos clássicos catalogados por Mora-Mora et al. \cite{mora2025model}.
+A análise comparativa, portanto, demonstra que o Modelo 3M 5.0 supera a visão instrumentalista das tecnologias de informação que caracteriza os 19 modelos clássicos catalogados por Mora-Mora et al. \cite{mora2025model}.
```

```diff
diff --git a/artigo final/sections/discussao.tex b/artigo final/sections/discussao.tex
@@
-Em síntese, as quatro dimensões discutidas evidenciam que a adoção do Modelo 3M 5.0 não constitui uma simples modernização tecnológica da Universidade Corporativa, mas uma reconfiguração epistemológica, trabalhista, ética e pedagógica de sua função institucional.
+As quatro dimensões discutidas evidenciam que a adoção do Modelo 3M 5.0 não constitui uma simples modernização tecnológica da Universidade Corporativa, mas uma reconfiguração epistemológica, trabalhista, ética e pedagógica de sua função institucional.
```

## 7. Escaneamento Residual de IA e Fluidez Metodologica

Termos problemáticos buscados:

- "Em suma": nao encontrado.
- "Crucial": nao encontrado.
- "Navegar neste/neste cenario": nao encontrado no texto autoral.
- "E importante notar": nao encontrado.
- "Trama": nao encontrado.

Termos marcados mas aceitaveis no contexto:

- "paradigma" aparece como termo tecnico de SI/GC, nao como floreio.
- "a luz de" aparece no titulo e em contexto metodologico; aceitavel, mas o titulo pode ser mais direto se a recomendacao acima for adotada.
- "Ressalta-se" aparece uma vez nas limitacoes. Nao bloqueia; o paragrafo esta fluido e defensivo.

As adicoes metodologicas da rodada anterior estao bem integradas. O trecho sobre classificacao ordinal, vies de confirmacao, ausencia de dupla triagem humana e kappa de Cohen em `conclusao.tex` e longo, mas funciona como blindagem metodologica. Nao parece remendo textual; parece uma secao de limitacoes deliberada. A unica ressalva e que, se houver limite rigido de paginas, esse paragrafo pode ser o primeiro candidato a compressao editorial.

## 8. Protocolo para Versao em Ingles (`artigo final en/`)

A versao portuguesa deve ser tratada como fonte congelada. Recomendo o seguinte protocolo:

1. Aplicar primeiro, na versao PT, os microajustes camera-ready acima.
2. Copiar a estrutura final validada para `artigo final en/`, mantendo os mesmos arquivos por secao e as mesmas chaves BibTeX.
3. Atualizar `main.tex` em ingles com `\usepackage[english]{babel}` e manter `IEEEtran`.
4. Traduzir por equivalencia tecnica, nao literalmente:
   - Universidade Corporativa -> Corporate University;
   - Gestao do Conhecimento -> Knowledge Management;
   - IA Generativa -> Generative AI;
   - Geração Aumentada por Recuperação -> Retrieval-Augmented Generation;
   - Grafos de Conhecimento -> Knowledge Graphs;
   - Motive, Model, Moment -> preservar em ingles.
5. Reusar `references.bib` apos a normalizacao BibTeX, sem traduzir titulos bibliograficos.
6. Rodar o mesmo cross-check de citacoes:
   - chaves citadas na versao EN devem ser identicas ou subset controlado da versao PT;
   - nenhuma entrada `.bib` nao citada;
   - nenhuma citacao sem entrada `.bib`.
7. Compilar `artigo final en/main.tex` com `pdflatex`/`bibtex`/`pdflatex`/`pdflatex` e revisar visualmente figuras, tabelas largas e ultima pagina.

## 9. Recomendacao Final

O artigo esta academicamente pronto, mas **nao esta camera-ready enquanto a Figura 1 for placeholder**. Apos inserir a imagem real, ocultar links coloridos, aplicar os microajustes listados e confirmar o limite de paginas do venue, o manuscrito pode ser liberado para submissao.

Prioridade de execucao:

1. Figura 1 real + legenda com citacao IEEE.
2. Confirmacao de limite de paginas.
3. `hidelinks` no `hyperref`.
4. Correcoes gramaticais/metodologicas pontuais.
5. Normalizacao BibTeX de `E0A18`, `S8A04` e verificacao de `E0A06`.
6. Recompilacao final e inspecao da ultima pagina.
