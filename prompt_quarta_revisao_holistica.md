# Prompt para Quarta Revisão Holística do Artigo (Camera-Ready e Validação de Submissão)

**Instruções para o Usuário:** Copie o prompt abaixo e forneça ao modelo (Opus, GPT-4, Gemini, etc.) junto com os arquivos finais `main.tex`, todas as `sections/*.tex` compiladas e o arquivo `references.bib`.

---

## Copie o texto abaixo:

**Contexto e Papel:**
Assuma o papel de um **Editor-Chefe / Preparador de Textos (Copyeditor) Sênior** de um periódico (ou congresso Qualis A1) de prestígio em Sistemas de Informação e Gestão do Conhecimento. Sua missão agora é realizar a **Quarta e Última Revisão Holística (Camera-Ready, Compliance e Validação de Submissão)** do artigo "Retrofit do Modelo 3M de Universidade Corporativa (3M 5.0) com IA Generativa".

**Contexto do que já foi feito:** O artigo passou recentemente pela aplicação de um terceiro parecer consolidado profundo, que corrigiu overclaims, blindou a metodologia (antecipando críticas ao método GRAI e triagem por LLMs), refinou citações indefinidas e limpou artefatos gramaticais. O texto atual é considerado a versão "quase final". O objetivo agora NÃO é reestruturar ou reescrever a narrativa, mas garantir que o artigo esteja impecável técnica e formalmente para submissão imediata (Camera-Ready).

**Arquivos e Diretórios de Entrada:**
Você possui acesso integral ao sistema de arquivos local. Utilize suas ferramentas para ler rigorosamente:
1. O arquivo raiz `main.tex` e todos os arquivos no diretório: `/Users/joaopedrobarbosa/Cowork/Msc_BMT/retrofit_3M_IA/artigo final/sections/`.
2. O arquivo de bibliografia: `/Users/joaopedrobarbosa/Cowork/Msc_BMT/retrofit_3M_IA/artigo final/references.bib`.

**Diretrizes de Revisão de Quarta Passagem (Camera-Ready e Compliance):**

1. **Compliance de Formato (IEEE) e Metadados:**
   - Verifique o padrão de blocos de autores, afiliações e e-mails no formato `IEEEtran` no `main.tex` (se há alguma anomalia de compilação ou formatação).
   - Analise o Título e o Resumo (Abstract): O título tem o impacto necessário? O abstract cumpre a densidade exigida e excede algum limite crítico de contagem de palavras comum a periódicos (geralmente 200-250 palavras)?

2. **Auditoria Cega de Referências e Citações (Cross-check Final):**
   - Execute um match 1:1 entre o texto e o `.bib`: existem citações no texto (`\cite{}`) que não constam no `.bib`?
   - Existem entradas no `.bib` que não foram citadas em nenhum lugar no texto? (Se sim, liste-as para remoção, dado que bibliografias IEEE devem conter apenas itens citados).
   - Os metadados do `.bib` estão completos (DOI, ano, volume, URL consistentes)?

3. **Check de Placeholders e Elementos Visuais:**
   - Procure por anotações residuais (TODOs, FIXMEs), comentários ocultos `%` que não deveriam estar lá, caixas vazias (como o `\framebox` da Figura 1 que sabemos estar pendente) ou marcações do LaTeX que possam causar problemas de renderização.
   - Formalize exatamente o que precisa de intervenção manual humana *antes* de gerar o PDF final (ex: "Inserir o diagrama real da Figura 1 sobrepondo a caixa de placeholder").

4. **Escaneamento Residual de IA e Transições Abruptas:**
   - Faça uma varredura final implacável buscando palavras-clichês de IA (ex: "Em suma", "Crucial", "Navegar neste cenário", "É importante notar", "Trama") que possam ter sobrevivido.
   - Verifique se as adições metodológicas feitas na rodada anterior (limitações sobre a avaliação ordinal e kappa de Cohen) estão fluidas e não parecem "remendos textuais".

5. **Sincronização e Planejamento da Versão em Inglês:**
   - Reconheça que a versão em português está concluída e elabore, de forma resumida, a melhor estratégia/protocolo para transpor (traduzir e adaptar) essa versão definitiva para o diretório `artigo final en/` de forma consistente.

6. **Formato da Entrega do Parecer:**
   Entregue um relatório de liberação de submissão ultra-direto e estruturado contendo:
   - **Status de "Go/No-Go":** O artigo está pronto para submissão? Qual é o veredito do copyeditor?
   - **Lista de Pendências Humanas Rigorosas:** (Ações intransferíveis para o autor, como substituir a imagem).
   - **Micro-ajustes Finais de LaTeX e `.bib` (Diffs):** (Apenas blocos de código `diff` pontuais para as correções cirúrgicas finais encontradas).
   - **Recomendações de Cross-check:** Relatório final sobre a integridade das citações vs referências.

7. **Salvamento do Arquivo (Handoff Obrigatório):**
   - Ao invés de apenas imprimir a resposta no chat, você **DEVE salvar o seu parecer estruturado fisicamente na pasta** `/Users/joaopedrobarbosa/Cowork/Msc_BMT/retrofit_3M_IA/artigos_materiais/`.
   - O nome do arquivo deve seguir o formato: `[nome_do_seu_modelo]_v4_revisao_holistica_final.md` (por exemplo: `claude_3.5_sonnet_v4_revisao_holistica_final.md` ou `gpt4o_v4_revisao_holistica_final.md`).

---
**Inicie a validação de submissão agora:** Leia todos os arquivos indicados para a versão em português, realize a quarta revisão (Camera-Ready) e salve o parecer final estruturado no caminho solicitado. Informe no chat assim que a análise e o salvamento forem concluídos.
