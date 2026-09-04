# Prompt para Terceira Revisão Holística do Artigo (Simulação de Peer Review e Proofreading Final)

**Instruções para o Usuário:** Copie o prompt abaixo e forneça ao modelo (Opus, GPT-4, etc.) junto com os arquivos `main.tex`, todas as `sections/*.tex` compiladas e o arquivo `references.bib`.

---

## Copie o texto abaixo:

**Contexto e Papel:**
Assuma o papel de um **Reviewer 2 (Revisor Cego e Crítico)** de um periódico Q1 (Qualis A1) em Sistemas de Informação e Gestão do Conhecimento. Sua missão agora é realizar a **Terceira e Última Revisão Holística (Simulação de Peer Review e Proofreading Final)** do artigo "Retrofit do Modelo 3M de Universidade Corporativa (3M 5.0) com IA Generativa". 

**Contexto do que já foi feito:** O artigo já passou por uma revisão estrutural profunda e uma segunda revisão de polimento (fio condutor e eliminação de AI-isms). A lógica central está sólida e a escrita está mais humana e densa. Agora, o foco é encontrar as "agulhas no palheiro": erros gramaticais, frases ambíguas, inconsistências finais de formatação e simular as críticas que um revisor real faria antes de aceitar o paper.

**Arquivos e Diretórios de Entrada:**
Você possui acesso integral ao sistema de arquivos local. Utilize suas ferramentas para ler:
1. Todos os arquivos LaTeX no diretório: `/Users/joaopedrobarbosa/Cowork/Msc_BMT/retrofit_3M_IA/artigo final/sections/` e o arquivo raiz `main.tex` (que pode estar um nível acima ou na mesma pasta, procure-o).
2. O nosso **Catálogo da Scoping Review**: `/Users/joaopedrobarbosa/Cowork/Msc_BMT/retrofit_3M_IA/artigos_materiais/artigos_materiais/02_Catalogo/catalogo_artigos.csv` (apenas para checagem de referências finais, se necessário).

**Diretrizes de Revisão de Terceira Passagem (Auditoria e Proofreading):**

1. **Proofreading Implacável e Micro-estilo:**
   - Cace erros de digitação, falhas de concordância (nominal e verbal), vírgulas mal colocadas e frases excessivamente longas (run-on sentences).
   - Identifique jargões que não foram devidamente explicados na primeira menção.
   - Verifique se a voz passiva está sendo usada em excesso, sugerindo voz ativa onde a clareza se beneficiar.

2. **Simulação de "Reviewer 2" (Crítica de Validade e Limitações):**
   - Ataque o artigo: quais seriam as duas maiores críticas de um revisor metodológico rigoroso quanto à aplicação do GRAI ou à generalização do modelo 3M 5.0?
   - Verifique se as **Limitações do Estudo** e os **Trabalhos Futuros** na Conclusão blindam o artigo contra essas críticas. Se não, sugira adições cirúrgicas à seção de Conclusão/Discussão.

3. **Auditoria de Resumo (Abstract) e Introdução:**
   - O Abstract contém de forma concisa: Contexto, Problema, Método, Resultados Principais e Contribuições? 
   - O Abstract está em perfeita sintonia com as promessas da Introdução e as entregas reais da Conclusão?
   - A Introdução "vende" o problema com urgência e clareza suficientes para um periódico de alto impacto?

4. **Sanidade do LaTeX (Pre-flight Check):**
   - Verifique o uso de aspas (no LaTeX padrão: \`\` e ''), espaçamentos duplos acidentais, citações e chamadas de tabelas/figuras que possam quebrar a compilação ou o layout.

5. **Formato da Entrega do Parecer:**
   Entregue um relatório de auditoria final ultra-focado contendo:
   - **Parecer do Reviewer 2:** (Um parágrafo com a crítica mais dura e plausível que o artigo poderia receber e como nos defendermos dela no texto).
   - **Auditoria do Abstract/Conclusão:** (Sugestões pontuais de melhoria para espelhamento perfeito).
   - **Lista de Proofreading e Typos:** (Lista indicando: "Arquivo X, Linha/Trecho: Substituir [erro] por [correção]").
   - **Micro-ajustes Estruturais/LaTeX (Diffs):** (Apenas blocos de código `diff` pontuais para correções definitivas no código LaTeX).

6. **Salvamento do Arquivo (Handoff):**
   - Ao invés de apenas imprimir a resposta no chat, você DEVE salvar o seu parecer estruturado fisicamente na pasta `/Users/joaopedrobarbosa/Cowork/Msc_BMT/retrofit_3M_IA/artigos_materiais/`.
   - O nome do arquivo deve seguir o formato: `[nome_do_seu_modelo]_v3_revisao_holistica_final.md` (por exemplo: `claude_3.5_sonnet_v3_revisao_holistica_final.md` ou `gpt4o_v3_revisao_holistica_final.md`).

---
**Inicie a varredura autônoma agora:** Leia os arquivos indicados, realize a terceira revisão de auditoria e proofreading e salve o parecer no caminho solicitado. Informe no chat quando concluir.
