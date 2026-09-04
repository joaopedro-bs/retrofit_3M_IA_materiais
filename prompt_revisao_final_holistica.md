# Prompt para Revisão Final Holística do Artigo (Padrão Q1)

**Instruções para o Usuário:** Copie o prompt abaixo e forneça ao modelo (Opus, GPT-4, etc.) junto com os arquivos `main.tex`, todas as `sections/*.tex` compiladas e o arquivo `references.bib`.

---

## Copie o texto abaixo:

**Contexto e Papel:**
Assuma o papel do **Revisor Acadêmico Sênior** (Padrão Periódico Q1 em Sistemas de Informação e Gestão do Conhecimento). Sua missão agora é realizar a **Revisão Final Holística** do artigo completo "Retrofit do Modelo 3M de Universidade Corporativa (3M 5.0) com IA Generativa". O artigo já passou por rodadas iterativas de construção e validação por seções.

**Arquivos e Diretórios de Entrada:**
Você possui acesso integral ao sistema de arquivos. Por favor, utilize suas ferramentas de leitura para analisar:
1. Todos os arquivos LaTeX compilados no diretório: `/Users/joaopedrobarbosa/Cowork/Msc_BMT/retrofit_3M_IA/artigo final/sections/` e o `main.tex`.
2. O nosso **Catálogo da Scoping Review** que contém todos os metadados dos 93 artigos aprovados. Leia o arquivo CSV em: `/Users/joaopedrobarbosa/Cowork/Msc_BMT/retrofit_3M_IA/artigos_materiais/artigos_materiais/02_Catalogo/catalogo_artigos.csv`.

**Diretrizes de Revisão Profunda:**

1. **Revisão Estrutural e Coesão Global:**
   - Analise o "fio condutor" (*Golden Thread*) do artigo, desde a Introdução até a Conclusão. A transição entre o referencial teórico clássico (SECI, 3M original), a lacuna de pesquisa e a formulação do retrofit 3M 5.0 (com o modelo GRAI) flui de maneira lógica e inquebrável?
   - Identifique quebras de coesão entre as seções ou redundâncias argumentativas que possam ser enxugadas.

2. **Purificação de "AI-isms" (Marcas de Escrita por IA):**
   - Rastreie e sugira a remoção ou substituição de clichês típicos de redação por LLMs (ex: "Em suma", "É crucial notar que", "Uma tapeçaria de", "Mergulha profundamente", "Um testemunho de", "Neste cenário em rápida evolução", adjetivações excessivas, transições robóticas ou frases excessivamente balanceadas).
   - O tom deve ser densamente acadêmico, seco, direto, impessoal e focado na precisão epistemológica.

3. **Ampliação do Referencial Teórico (Com Restrição Estrita):**
   - Identifique oportunidades onde o argumento metodológico ou conceitual está frágil e precisa de mais lastro de evidências.
   - **REGRA DE OURO:** Você **SÓ PODE** sugerir a inserção de novas citações se essas referências **JÁ EXISTIREM** no **Catálogo da Scoping Review** que eu fornecerei e que **AINDA NÃO TENHAM SIDO UTILIZADAS** no texto atual do LaTeX.
   - **Tolerância Zero a Alucinações:** É terminantemente proibido inventar autores, artigos empíricos, resultados ou buscar literatura fora do escopo fornecido. Se faltar evidência e não houver um artigo não-utilizado no nosso catálogo para cobrir a lacuna, apenas aponte a fragilidade para que os autores busquem externamente.

4. **Formato da Entrega do Parecer:**
   Entregue um relatório estruturado contendo:
   - **Visão Geral e Fio Condutor:** (Avaliação holística da narrativa e transição entre as seções I a VII).
   - **Caça aos "AI-isms":** (Lista de trechos com escrita viciada e a respectiva sugestão de reescrita).
   - **Oportunidades de Ancoragem Teórica (Apenas Catálogo Local):** (Sugestão de trechos que precisam de citação, indicando EXATAMENTE qual artigo do nosso Catálogo Scoping Review está sobrando e pode ser encaixado).
   - **Micro-ajustes Estruturais (Diffs):** (Blocos de código `diff` pontuais sugerindo cortes de redundância ou amarrações entre as seções).

5. **Salvamento do Arquivo (Handoff):**
   - Ao invés de apenas imprimir a resposta no chat, você DEVE criar e salvar o seu parecer estruturado fisicamente na pasta `/Users/joaopedrobarbosa/Cowork/Msc_BMT/retrofit_3M_IA/artigos_materiais/`.
   - O nome do arquivo deve seguir estritamente o formato: `[nome_do_seu_modelo]_v1_revisao_holistica_final.md` (por exemplo: `claude_3.5_sonnet_v1_revisao_holistica_final.md` ou `gpt4o_v1_revisao_holistica_final.md`).

---
**Inicie a varredura autônoma agora:** Leia todos os arquivos nos caminhos indicados acima, analise a integridade do artigo e salve o Parecer Estruturado final no arquivo conforme orientado. Informe no chat quando concluir.
