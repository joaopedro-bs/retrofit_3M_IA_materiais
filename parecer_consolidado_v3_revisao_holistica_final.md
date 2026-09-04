# Parecer Consolidado v3 - Revisao Holistica Final

Base mergeada:
- `claude_fable_5_v3_revisao_holistica_final.md`
- `gpt5_codex_v3_revisao_holistica_final.md`
- Decisao autoral preservada de `parecer_consolidado_v2_revisao_holistica_final.md`

Data: 2026-06-09

## Decisao de Conflito

### Figura 1 do Modelo 3M original

Conflito identificado: os pareceres v3 tratam o placeholder da Figura 1 como problema relevante para submissao, enquanto o consolidado v2 registrava uma decisao autoral explicita de manter o placeholder ate substituicao posterior pelo autor.

Decisao do autor: **manter a decisao autoral anterior**.

Regra para o redator:
- manter o `\framebox` da Figura 1 como esta;
- nao remover, redesenhar ou substituir a figura nesta rodada;
- nao classificar a Figura 1 como bloqueante operacional para o agente redator;
- registrar apenas como pendencia futura de camera-ready/submissao final: inserir figura real antes da versao definitiva.

Nao encontrei outros conflitos substantivos entre os pareceres v3. As demais recomendacoes sao compatíveis e foram consolidadas abaixo.

## Diagnostico Consolidado

O artigo esta conceitualmente maduro e defensavel para Sistemas de Informacao e Gestao do Conhecimento. A contribuicao central esta clara: atualizar o Modelo 3M de Universidade Corporativa por meio de um retrofit conceitual que reposiciona IA Generativa como infraestrutura sociotecnica e como agente organizacional nos processos de GC.

O maior risco editorial remanescente nao e de originalidade, mas de **calibragem metodologica**: o texto ainda usa linguagem de "validacao" em pontos nos quais a evidencia apresentada corresponde a uma **avaliacao comparativa de cobertura conceitual conduzida pelos autores**. Essa calibragem deve ser feita para evitar uma critica forte de circularidade, autoavaliacao e generalizacao indevida.

O segundo risco e de higiene de submissao: ha citacoes quebradas, possiveis inconsistencias numericas na metodologia, atribuicoes conceituais a revisar e pequenos problemas de LaTeX/estilo.

## Prioridades Consolidadas

| Prioridade | Itens |
|---|---|
| **P0 - Bloqueante** | Corrigir citacoes indefinidas; reconciliar numeros da triagem; harmonizar processos atribuidos a Prat/Stollenwerk; corrigir traducao de RAG na conclusao; revisar atribuicao Alavi & Leidner |
| **P1 - Alto valor metodologico** | Trocar "validacao" por "avaliacao de cobertura conceitual" quando adequado; explicitar viés de autoavaliacao; reconhecer limites do GRAI; reconhecer limites da triagem por LLM |
| **P2 - Espelhamento textual** | Atualizar abstract; ecoar contribuicao metodologica na conclusao; harmonizar terminologia Motive/Model/Moment |
| **P3 - Polimento e LaTeX** | Normalizar Unicode arriscado; adicionar `fontenc`; ajustar bloco de autores; remover redundancias e anglicismos desnecessarios |
| **Pendencia autoral futura** | Substituir Figura 1 placeholder por figura real antes da versao definitiva |

## Pontos P0 - Bloqueantes

### P0.1 - Quatro citacoes indefinidas

Problema confirmado por pre-flight LaTeX: `S1A04`, `S1A09`, `S1A10` e `S2A04` sao citadas em `analise.tex`, mas nao existem em `references.bib`. O PDF pode renderizar `[?]`.

Decisao recomendada: **adicionar as quatro entradas ao `.bib`**, pois os exemplos concretos fortalecem a analise comparativa. O catalogo confirma:
- `S1A04`: Garzon Castrillon, 2019, *Proposed model of corporate university*.
- `S1A09`: Chen, Zhou e Wang, 2023, *The role and evolution of knowledge network-based intellectual capital in the corporate university*.
- `S1A10`: Zhou, 2023, tese/dissertacao, *Path of corporate university to enable enterprises*.
- `S2A04`: Singh, Verma e Chaurasia, 2019, *Mapping the themes and intellectual structure of corporate university*.

Diff orientador:

```diff
diff --git a/artigo final/references.bib b/artigo final/references.bib
@@
+@article{S1A04,
+  author = {Garzón Castrillón, M. A.},
+  title = {Proposed model of corporate university},
+  journal = {Visión de Futuro},
+  year = {2019},
+  doi = {10.36995/j.visiondefuturo.2019.23.01.006.en},
+  url = {https://rid.unam.edu.ar/handle/20.500.12219/2488},
+  note = {ID do Catálogo: S1A04}
+}
+
+@article{S1A09,
+  author = {Chen, Y. and Zhou, L. and Wang, Y.},
+  title = {The role and evolution of knowledge network-based intellectual capital in the corporate university},
+  journal = {Journal of Intellectual Capital},
+  year = {2023},
+  doi = {10.1108/JIC-12-2022-0238},
+  url = {https://www.emerald.com/jic/article/24/6/1604/226655},
+  note = {ID do Catálogo: S1A09}
+}
+
+@phdthesis{S1A10,
+  author = {Zhou, Y.},
+  title = {Path of corporate university to enable enterprises: Based on the best corporate universities in China},
+  school = {University of Otago},
+  year = {2023},
+  url = {https://ourarchive.otago.ac.nz/esploro/outputs/graduate/Path-of-corporate-university-to-enable/9926501875701891},
+  note = {ID do Catálogo: S1A10}
+}
+
+@article{S2A04,
+  author = {Singh, V. and Verma, S. and Chaurasia, S. S.},
+  title = {Mapping the themes and intellectual structure of corporate university: co-citation and cluster analyses},
+  journal = {Scientometrics},
+  year = {2019},
+  doi = {10.1007/s11192-019-03328-0},
+  url = {https://doi.org/10.1007/s11192-019-03328-0},
+  note = {ID do Catálogo: S2A04}
+}
```

### P0.2 - Inconsistencia numerica na metodologia

Problema: a lista por eixos em `metodologia.tex` soma 108 artigos, enquanto a tabela reporta 129 triados, 15 duplicados/NV, 21 inacessiveis e 93 consolidados. A relacao entre os numeros da lista e da tabela nao fica clara.

Acao obrigatoria:
- reconciliar com os dados reais do pipeline;
- explicitar se os numeros por eixo sao triados, consolidados, aprovados, baixados ou mobilizados;
- nao inventar correcao textual sem conferir a fonte de dados.

Orientacao editorial: se nao houver tempo para reabrir os logs do pipeline, simplificar o texto e fazer a tabela ser a fonte unica dos numeros.

### P0.3 - Harmonizar processos atribuidos a Prat/Stollenwerk

Problema:
- `referencial.tex` descreve Prat por processos estrategicos e operacionais: identificacao, avaliacao, atualizacao, protecao; aquisicao, transferencia, armazenamento e utilizacao.
- `metodologia.tex` e `retrofit.tex` apresentam Prat como geracao, codificacao, armazenamento, distribuicao e aplicacao.

Acao:
- verificar a fonte primaria;
- se ambas as listas forem usadas, explicitar que a primeira e o mapeamento do Modelo 3M original/Costa et al. sobre Prat, e a segunda e a sintese de macroprocessos adotada no retrofit;
- evitar escrever que as duas listas sao, indistintamente, "os processos de Prat".

### P0.4 - Corrigir traducao de RAG

Em `conclusao.tex`, trocar:

```diff
-Recuperação Aumentada por Geração (RAG)
+Geração Aumentada por Recuperação (RAG)
```

### P0.5 - Revisar atribuicao Alavi & Leidner

Problema: `referencial.tex` chama `E0A15` de perspectiva fundacional de Alavi e Leidner, mas a entrada atual e Alavi, Leidner e Mousavi (2024), sobre GenAI.

Escolher uma rota:
- adicionar a referencia fundacional Alavi & Leidner (2001); ou
- reformular para deixar claro que o paper de 2024 retoma a perspectiva fundacional.

Diff seguro:

```diff
-Na perspectiva fundacional da Gestão do Conhecimento formulada por Alavi e Leidner \cite{E0A15},
+Na perspectiva de Gestão do Conhecimento retomada e atualizada para o contexto de GenAI por Alavi, Leidner e Mousavi \cite{E0A15},
```

## Pontos P1 - Blindagem Metodologica

### P1.1 - Rebaixar "validacao" para "avaliacao de cobertura conceitual"

Problema: "validacao conceitual" pode soar como prova de efetividade ou como autoavaliacao circular.

Aplicar principalmente em:
- `introducao.tex`, objetivo 4;
- `metodologia.tex`, fase 4 e subtitulo/trechos de validacao;
- `analise.tex`, quando falar da escala Ausente/Parcial/Pleno;
- `discussao.tex`, primeira frase;
- `conclusao.tex`, limitacoes.

Diff orientador:

```diff
diff --git a/artigo final/sections/metodologia.tex b/artigo final/sections/metodologia.tex
@@
-    \item \textbf{Validação Conceitual}: Realizou-se uma análise comparativa do framework 3M 5.0 resultante em relação aos 19 modelos catalogados por Mora-Mora et al. \cite{mora2025model}, com o objetivo de demonstrar as contribuições conceituais e o preenchimento do gap de pesquisa.
+    \item \textbf{Avaliação de Cobertura Conceitual}: Realizou-se uma análise comparativa do framework 3M 5.0 resultante em relação aos 19 modelos catalogados por Mora-Mora et al. \cite{mora2025model}, com o objetivo de demonstrar suas contribuições conceituais e seu potencial de preenchimento do gap de pesquisa, sem caracterizar validação empírica de efetividade organizacional.
@@
-Para validar a contribuição conceitual do Modelo 3M 5.0 e justificar sua necessidade teórica frente aos modelos existentes, o framework proposto foi submetido a um procedimento de validação conceitual por meio de análise comparativa estruturada.
+Para avaliar a contribuição conceitual do Modelo 3M 5.0 e justificar sua necessidade teórica frente aos modelos existentes, o framework proposto foi submetido a um procedimento de análise comparativa estruturada de cobertura teórica.
```

### P1.2 - Blindar a circularidade da matriz ordinal

Adicionar na conclusao/limitacoes:

```diff
+Ressalta-se, ainda, que tanto as cinco dimensões analíticas quanto a classificação ordinal de cobertura foram definidas e atribuídas pelos próprios autores, o que introduz risco de viés de confirmação; a corroboração da análise por painel independente de especialistas, por exemplo via método Delphi, constitui etapa necessária de robustecimento.
```

### P1.3 - Blindar a dependencia do GRAI

Adicionar nas limitacoes:

```diff
+O backbone processual adotado apoia-se no modelo GRAI \cite{E0A18}, proposta recente e ainda carente de validação empírica independente; cabe registrar, contudo, que a arquitetura do 3M 5.0 não depende ontologicamente do GRAI, uma vez que o mapeamento das visões aos processos de GC de Prat \cite{prat2011hierarchical} e Stollenwerk \cite{stollenwerk2001gestao} permanece válido caso aquele framework venha a ser refinado pela literatura.
```

### P1.4 - Blindar a triagem automatizada por LLM

Adicionar nas limitacoes:

```diff
+Embora a triagem automatizada por LLM no protocolo de scoping review reduza parte da carga operacional e padronize critérios de seleção, ela também introduz vieses próprios do modelo avaliador; a ausência de dupla triagem humana por amostragem e de métricas de concordância humano-máquina, como kappa de Cohen, limita a auditabilidade do processo de seleção.
```

### P1.5 - Explicitar criterio 93 -> 20

O metodo ja informa 93 artigos aprovados e 20 referencias usadas diretamente na formulacao. Falta explicitar o criterio de curadoria.

Sugestao:

```tex
A seleção das 20 referências mobilizadas diretamente na formulação do modelo priorizou aderência às lentes teóricas do estudo, centralidade para os processos de GC analisados e capacidade de sustentar as cinco dimensões comparativas definidas na avaliação de cobertura conceitual.
```

## Pontos P2 - Abstract, Introducao e Conclusao

### P2.1 - Atualizar abstract

Objetivo: incluir metodo e resultado, sem overclaim.

Diff recomendado:

```diff
diff --git a/artigo final/main.tex b/artigo final/main.tex
@@
-A difusão da Inteligência Artificial (IA) Generativa altera o papel das Universidades Corporativas (UCs) na Gestão do Conhecimento ao deslocar a tecnologia de suporte informacional para mediação ativa dos processos de aprendizagem. Este trabalho propõe um retrofit conceitual do Modelo 3M de Universidade Corporativa, formulado por Costa, Souza e Oliveira (2011), integrando tecnologias de IA como infraestrutura operacional e como agente organizacional no ecossistema de aprendizagem. Por meio de um mapeamento comparativo ancorado nos processos de Gestão do Conhecimento (GC), estruturam-se os pilares Motive 5.0 (sensing contínuo de competências), Model 5.0 (laboratório vivo de redesenho e RAG/grafos de conhecimento) e Moment 5.0 (governança de IA como processo adaptativo). O modelo proposto, 3M 5.0, responde a uma lacuna teórica mapeada na literatura: modelos existentes tratam tecnologias de IA e Indústria 5.0 como infraestrutura periférica, sem integrá-las à arquitetura interna da UC.
+A difusão da Inteligência Artificial (IA) Generativa altera o papel das Universidades Corporativas (UCs) na Gestão do Conhecimento ao deslocar a tecnologia de suporte informacional para mediação ativa dos processos de aprendizagem. Este trabalho propõe um retrofit conceitual do Modelo 3M de Universidade Corporativa, formulado por Costa, Souza e Oliveira (2011), integrando tecnologias de IA como infraestrutura operacional e como agente organizacional no ecossistema de aprendizagem. A partir de uma scoping review assistida por pipeline SLR-RAG e de uma avaliação comparativa de cobertura conceitual, estruturam-se os pilares Motive 5.0 (sensoriamento semântico contínuo de competências), Model 5.0 (laboratório vivo apoiado por Geração Aumentada por Recuperação e grafos de conhecimento) e Moment 5.0 (governança de IA como processo adaptativo). A comparação frente aos modelos de UC catalogados na literatura indica que o 3M 5.0 explicita dimensões ausentes ou periféricas nos modelos existentes, especialmente agência ativa de IA, simbiose humano-IA e governança algorítmica. O modelo oferece, assim, uma resposta teórica à lacuna de integração da IA e da Indústria 5.0 à arquitetura interna da UC.
```

### P2.2 - Suavizar overclaim da introducao

Em `introducao.tex`, linha sobre IA agentica:

```diff
-Com a IA agêntica, a máquina assume um papel ativo de criação e tomada de decisão autônoma.
+Com a IA agêntica, a máquina passa a participar ativamente de fluxos de síntese, recomendação e apoio à decisão.
```

### P2.3 - Ecoar contribuicao metodologica na conclusao

A Introducao promete contribuicao metodologica, mas a Conclusao privilegia teoria e gestao. Inserir antes das limitacoes:

```diff
+Na dimensão metodológica, o estudo formaliza o retrofit conceitual como estratégia replicável de evolução de teorias organizacionais frente a rupturas tecnológicas e documenta um pipeline agêntico de revisão de literatura (SLR-RAG) reutilizável em estudos secundários na área de Sistemas de Informação.
```

### P2.4 - Harmonizar Motive/Model/Moment na conclusao

```diff
-Ao integrar de forma sistêmica os pilares de motivação (\textit{Motive 5.0}), entrega instrucional (\textit{Model 5.0}) e governança ética (\textit{Moment 5.0}),
+Ao integrar de forma sistêmica as visões de motivo (\textit{Motive 5.0}), de modelo (\textit{Model 5.0}) e de momento (\textit{Moment 5.0}),
```

### P2.5 - Limites e trabalhos futuros mais precisos

Trecho consolidado para `conclusao.tex`:

```diff
-Apesar de suas contribuições, as limitações metodológicas e tecnológicas deste estudo devem ser mapeadas de forma transparente.
+Apesar de suas contribuições, as limitações metodológicas e tecnológicas deste estudo devem ser reconhecidas de forma transparente.
```

```diff
-validação empírica quantitativa e longitudinal
+validação empírica, preferencialmente quantitativa e longitudinal
```

## Pontos P3 - Proofreading e Microestilo

Aplicar ajustes pontuais:

- `main.tex`, abstract: trocar `sensing contínuo de competências` por `sensoriamento semântico contínuo de competências`.
- `main.tex`, linha de `\hypersetup`: remover espacos finais em `filecolor=magenta,`.
- `introducao.tex`: remover redundancia `passivo ... uso passivo`.
- `introducao.tex`: trocar `Validar conceitualmente` por `Avaliar conceitualmente` ou `Examinar comparativamente`.
- `referencial.tex`: trocar `focando em obter` por `com foco em obter`.
- `referencial.tex`: trocar `pesquisas manuais de manuais e políticas internas` por `buscas manuais em manuais e políticas internas`.
- `referencial.tex`: corrigir `cinco fases` para `quatro fases`, se a lista permanecer com quatro itens.
- `metodologia.tex`: trocar `A fundamentação deste gap foi validada` por `A fundamentação desta lacuna foi sustentada`.
- `metodologia.tex`: trocar `Para mitigar a subjetividade humana` por `Para padronizar a triagem e reduzir parte da carga operacional`.
- `metodologia.tex`: trocar `\texttt{<ARTICLE\_\{DATA\}>}` por `\texttt{<ARTICLE\_DATA>}`.
- `retrofit.tex`: trocar `Ao invés de` por `Em vez de`.
- `retrofit.tex`: trocar `resolve o problema de falta de acurácia factual` por `mitiga o problema de falta de acurácia factual`.
- `retrofit.tex`: trocar `O \textit{Moment 5.0} resolve isso` por `O \textit{Moment 5.0} enfrenta essa lacuna`.
- `retrofit.tex`: trocar `loops onde` por `loops nos quais`.
- `retrofit.tex`: trocar `output algorítmico` por `saída algorítmica`.
- `retrofit.tex`: padronizar `coevolui`, `coevolução`, `coproduz`, salvo decisão editorial por manter hifenização.
- `analise.tex`: trocar `input do colaborador` por `entrada do colaborador`.
- `analise.tex`: trocar `garante que` por `propõe mecanismos para que`.
- `discussao.tex`: trocar `constructo` por `construto`.
- `discussao.tex`: trocar `pode mitigar o esforço crítico humano` por `pode reduzir o exercício do esforço crítico humano`.
- `discussao.tex`: trocar `total desvinculação de processos punitivos` por `desvinculação explícita de processos punitivos`.
- `conclusao.tex`: padronizar `19 modelos` em vez de alternar com `dezenove modelos`.

## Pontos P3 - LaTeX e Portabilidade

### Unicode tipografico

Ha `—`, `‑`, `–` e apostrofos tipograficos no `.tex`/`.bib`. O TeX Live local compila, mas para submissao IEEE e portabilidade recomenda-se normalizar.

Comando orientador, se o redator for aplicar mecanicamente apos revisar impacto:

```bash
sed -i '' $'s/‑/-/g; s/—/---/g' sections/*.tex
```

### `fontenc`

Adicionar ao preambulo:

```diff
 \usepackage[utf8]{inputenc}
+\usepackage[T1]{fontenc}
 \usepackage[brazilian]{babel}
```

### Bloco de autores

Avaliar ajuste ao padrao IEEE:

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

### Referencias cruzadas

Padronizar `§\ref{...}` para `Subseção~\ref{...}` ou `Seção~\ref{...}`, de acordo com o nivel da referencia.

## Decisoes Autorais Mantidas

1. Nao atribuir a perspectiva de IA como agente, a dupla perspectiva ferramenta/agente ou qualquer componente do Modelo 3M 5.0 a sugestao, feedback ou provocacao de professor especifico.
2. Manter a granularidade tecnica do `SLR-RAG Agentic Pipeline` nesta rodada, corrigindo apenas erros factuais, de compilacao ou imprecisoes metodologicas objetivas.
3. Permitir referencias fundacionais externas ao catalogo quando sustentarem arcaboucos teoricos necessarios.
4. Manter o placeholder da Figura 1 ate substituicao posterior pelo autor.

## Checklist para o Redator

1. Corrigir as quatro citacoes indefinidas no `.bib`.
2. Reconciliar os numeros da triagem antes de mexer na tabela.
3. Harmonizar os processos atribuidos a Prat/Stollenwerk.
4. Corrigir RAG e Alavi/Leidner.
5. Reduzir "validacao" para "avaliacao de cobertura conceitual" onde aplicavel.
6. Inserir limitacoes sobre autoavaliacao, GRAI e triagem LLM.
7. Atualizar o abstract com metodo e resultado.
8. Ecoar a contribuicao metodologica na conclusao.
9. Aplicar typos e ajustes de overclaim.
10. Preservar a Figura 1 placeholder nesta rodada.
11. Recompilar com `latexmk` e verificar citacoes, referencias, overfull/underfull relevantes.

## Veredito Consolidado

Recomendacao simulada: **aceitavel apos revisoes menores, com ajustes metodologicos pontuais obrigatorios e saneamento LaTeX/bibliografico**.

O artigo nao precisa de nova reestruturacao profunda. O foco deve ser: remover overclaims de validacao, tornar as limitacoes metodologicas mais honestas, corrigir problemas objetivos de compilacao e fechar o espelhamento entre abstract, introducao e conclusao. Com esses ajustes, a versao fica mais resistente a um Reviewer 2 metodologico sem sacrificar a tese central do 3M 5.0.
