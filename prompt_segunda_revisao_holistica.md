# Prompt para Segunda Revisão Holística do Artigo (Polimento Final Absoluto)

**Instruções para o Usuário:** Copie o prompt abaixo e forneça ao modelo (Opus, GPT-4, etc.) junto com os arquivos `main.tex`, todas as `sections/*.tex` compiladas e o arquivo `references.bib`.

---

## Copie o texto abaixo:

**Contexto e Papel:**
Assuma novamente o papel do **Revisor Acadêmico Sênior** (Padrão Periódico Q1 em Sistemas de Informação e Gestão do Conhecimento). Sua missão agora é realizar a **Segunda Revisão Holística (Polimento Final Absoluto)** do artigo "Retrofit do Modelo 3M de Universidade Corporativa (3M 5.0) com IA Generativa". 

**Contexto do que já foi feito:** O artigo já passou por uma primeira revisão holística rigorosa. Já enxugamos redundâncias, lapidamos transições entre as seções e fizemos um expurgo agressivo de "AI-isms" (clichês de LLM). Agora, estamos na etapa de lapidação final, buscando a perfeição cirúrgica do texto para submissão.

**Arquivos e Diretórios de Entrada:**
Você possui acesso integral ao sistema de arquivos local. Utilize suas ferramentas para ler:
1. Todos os arquivos LaTeX no diretório: `/Users/joaopedrobarbosa/Cowork/Msc_BMT/retrofit_3M_IA/artigo final/sections/` e o arquivo raiz `main.tex`.
2. O nosso **Catálogo da Scoping Review**: `/Users/joaopedrobarbosa/Cowork/Msc_BMT/retrofit_3M_IA/artigos_materiais/artigos_materiais/02_Catalogo/catalogo_artigos.csv`.

**Diretrizes de Revisão de Segunda Passagem (Polimento Fino):**

1. **Teste de Estresse do "Fio Condutor" (Golden Thread):**
   - Na primeira revisão, ajustamos as transições lógicas. Sua tarefa agora é fazer o **teste de estresse**: há alguma ruptura lógica residual entre a formulação da lacuna, a justificativa do método, a aplicação do GRAI e a conclusão?
   - Avalie se a promessa feita na Introdução é plenamente e inequivocamente respondida na Conclusão, sem saltos argumentativos.

2. **Varredura Fina "Zero AI-isms" e Consistência de Tom:**
   - Faça uma segunda varredura implacável em busca de qualquer resquício de escrita robótica, transições excessivamente mecânicas ou adjetivação desnecessária.
   - O tom está suficientemente denso, crítico e acadêmico? Sugira apenas trocas pontuais de vocabulário que elevem o nível da prosa acadêmica.

3. **Validação Cruzada de Referências e Ancoragem Teórica:**
   - Verifique se as citações mais recentes incorporadas estão organicamente inseridas no texto ou se parecem "forçadas".
   - **Regra Restrita:** Se ainda houver alguma lacuna teórica mínima, você só pode sugerir citações do **Catálogo da Scoping Review** (fornecido acima) que ainda não foram usadas. Zero tolerância a alucinação bibliográfica.

4. **Verificação de Consistência LaTeX (Micro-ajustes):**
   - Identifique problemas de consistência na formatação (ex: uso de aspas, itálico em termos estrangeiros, espaçamentos, chamadas de figuras/tabelas que possam estar quebradas ou confusas na narrativa).

5. **Formato da Entrega do Parecer:**
   Entregue um relatório ultra-focado contendo:
   - **Diagnóstico do Teste de Estresse:** O artigo se sustenta como um paper Q1 forte? Onde está o elo mais fraco atual?
   - **Refinamentos Cirúrgicos de Tom:** (Lista pontual de frases ou palavras que ainda soam artificiais, com a sugestão direta de substituição).
   - **Micro-ajustes Estruturais (Diffs):** (Apenas blocos de código `diff` pontuais sugerindo pequenas correções de texto, formatação ou amarrações finais).

6. **Salvamento do Arquivo (Handoff):**
   - Ao invés de apenas imprimir a resposta no chat, você DEVE salvar o seu parecer estruturado fisicamente na pasta `/Users/joaopedrobarbosa/Cowork/Msc_BMT/retrofit_3M_IA/artigos_materiais/`.
   - O nome do arquivo deve seguir o formato: `[nome_do_seu_modelo]_v2_revisao_holistica_final.md` (por exemplo: `claude_3.5_sonnet_v2_revisao_holistica_final.md` ou `gpt4o_v2_revisao_holistica_final.md`).

---
**Inicie a varredura autônoma agora:** Leia os arquivos indicados, realize a segunda revisão de polimento e salve o parecer no caminho solicitado. Informe no chat quando concluir.
