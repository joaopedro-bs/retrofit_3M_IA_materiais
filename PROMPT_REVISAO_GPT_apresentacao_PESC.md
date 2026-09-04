# Prompt para Revisão Cruzada — Apresentação PESC (CPS831)

> **Como usar:** abra uma nova conversa com o GPT **com acesso à pasta do projeto** e cole o texto abaixo (da linha `---` em diante). O GPT lê o arquivo direto da pasta — não precisa anexar. Depois traga as recomendações de volta para implementação.

---

## Arquivos para acessar na pasta

- **Apresentação (revisar este):** `/Users/joaopedrobarbosa/Cowork/Msc_BMT/retrofit_3M_IA/artigos_materiais/ApresentacaoFinal_PESC_Retrofit_3M_5.0.pptx`
- **Extração de texto (caso não abra o .pptx diretamente):** rode `python -m markitdown` sobre o arquivo acima, ou abra o PDF parcial de referência em `/Users/joaopedrobarbosa/Cowork/Msc_BMT/retrofit_3M_IA/artigos_materiais/ApresentacaoParcial_PESC_Retrofit_3M_5.0.pdf`.
- **Pasta do projeto (material de apoio: artigos-fonte, pareceres, revisões anteriores):** `/Users/joaopedrobarbosa/Cowork/Msc_BMT/retrofit_3M_IA/`

> Se o caminho acima não resolver no seu ambiente, o arquivo está na pasta conectada do projeto, em `artigos_materiais/ApresentacaoFinal_PESC_Retrofit_3M_5.0.pptx`.

## Papel e objetivo

Você é um **revisor sênior de apresentações acadêmicas** (mestrado/doutorado em Engenharia de Sistemas e Computação). Vou te entregar uma apresentação de qualificação/defesa e quero uma **revisão crítica e acionável**, focada em *melhorias*, não em elogios. Assuma que há problemas e seu trabalho é encontrá-los. Para cada ponto, diga **onde** (slide nº), **qual o problema** e **a correção concreta sugerida** (texto reescrito quando for o caso).

## Contexto do trabalho

- **Disciplina:** CPS831 — Gestão Aumentada do Conhecimento 5.0 (PESC/COPPE-UFRJ, 2026).
- **Tema do artigo/apresentação:** *Retrofit conceitual do Modelo 3M de Universidade Corporativa (Motive / Model / Moment), reinterpretando seus três pilares à luz da IA Generativa*, sob dupla perspectiva da IA (ferramenta e agente organizacional), alinhado aos processos de Gestão do Conhecimento (GC) e incorporando governança algorítmica.
- **Autores:** Martins, J.P.B.; Costa, V.C.F.; Lopes, E.
- **Formato:** 18 slides, proporção 4:3, template institucional PESC (logo Engenharia de Sistemas e Computação / PESC-COPPE).
- **Estrutura aproximada:** título → agenda → contexto (UCs e Modelo 3M) → problema e questão de pesquisa → referencial teórico (5 partes: fundamentos de GC; IA Generativa e GC; aprendizagem no fluxo de trabalho; IA como agente organizacional; governança de IA) → metodologia (pipeline agêntico SLR-RAG; estratégia de retrofit e dimensões de validação) → modelo 3M 5.0 proposto → resultados/discussão → limitações → conclusão → referências.

## Padrão visual já adotado (mantenha a consistência)

A apresentação já passou por dois ciclos de redesenho. O padrão visual validado é:
- **Cor de acento:** laranja `#EB976D` (negrito) para termos-chave / nomes de autores no início de cada bullet.
- **Cor de corpo:** navy `#38415C` para as explicações.
- **Cinza itálico** `#8C8C96` para notas/limitações de fechamento.
- **Hierarquia:** bullet de 1º nível em 14pt (`•`); sub-bullets indentados em 12pt (`–`); título de slide em 28pt.
- **Estrutura de bullet:** `Termo/Autor (laranja, negrito): explicação (navy)`. Enumerações densas viram sub-bullets em vez de listas embutidas com (1)(2)(3).
- Sem linhas decorativas sob títulos; uso de espaço em branco para respirar.

## O que já foi feito (não preciso que repita, mas pode criticar)

- Reestruturação de densidade nos slides de referencial teórico e metodologia (normalização de fonte, lead-ins coloridos, conversão de enumerações em sub-bullets nos pilares de Birkstedt, nas 5 dimensões analíticas e nas 3 camadas de defesa anti-prompt-injection).

## Foco da sua revisão (em ordem de prioridade)

1. **Conteúdo e rigor acadêmico:** clareza da questão de pesquisa, encadeamento lógico, coerência entre objetivos → método → resultados → conclusão. Há afirmações fortes sem suporte? Há contradições entre slides? A contribuição original está nítida?
2. **Adequação à banca:** o que uma banca de PESC provavelmente questionaria? Liste **5–8 perguntas difíceis prováveis** e sugira onde/como a apresentação poderia se antecipar a elas.
3. **Densidade e legibilidade:** slides ainda sobrecarregados de texto; sugestões de corte (o que mover para a fala do apresentador vs. o que fica no slide).
4. **Narrativa/storytelling:** o "fio condutor" está claro? A transição entre seções é fluida? Há um gancho inicial e um fechamento memorável?
5. **Precisão terminológica:** uso correto de termos (SECI→GRAI, RAG, grafos de conhecimento, human-in/on/out-of-the-loop, deskilling, scaffolding, etc.) e consistência de nomenclatura ao longo dos slides.
6. **Sugestões de elementos visuais:** onde um diagrama, fluxo ou tabela comparativa substituiria texto com ganho (ex.: mapeamento 3M→3M 5.0; pipeline SLR-RAG; matriz de 5 dimensões × 3 níveis Ausente/Parcial/Pleno).

## Regras importantes

- **Não invente fatos, números, datas, citações ou autores.** Se sugerir incluir um dado, marque explicitamente como "[a confirmar pelo autor]".
- Preserve o português acadêmico (PT-BR).
- Não reescreva tudo: priorize o que tem maior impacto. Seja específico e cirúrgico.

## Formato de saída desejado

1. **Diagnóstico geral** (5–8 linhas): impressão global e os 3 problemas mais críticos.
2. **Revisão slide a slide** (apenas slides com sugestões): `Slide N — [problema] → [correção concreta]`.
3. **Perguntas prováveis da banca** (lista) com mini-estratégia de resposta.
4. **Top 10 melhorias priorizadas** (tabela: melhoria | impacto Alto/Médio/Baixo | esforço).
5. **Sugestões de novos elementos visuais** (diagramas/tabelas) com descrição do conteúdo.

Ao final, devolva tudo em um único bloco organizado que eu possa copiar para outro agente implementar.
