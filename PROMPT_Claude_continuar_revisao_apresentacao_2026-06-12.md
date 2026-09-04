# Prompt para o Claude

Continue a revisão da apresentação acadêmica deste projeto a partir do estado deixado pelo Codex. Não reinicie o trabalho e não redesenhe a apresentação do zero.

Leia primeiro:

`/Users/joaopedrobarbosa/Cowork/Msc_BMT/retrofit_3M_IA/artigos_materiais/HANDOFF_revisao_apresentacao_Claude_2026-06-12.md`

Em seguida, trabalhe diretamente com:

- Script principal:
  `/Users/joaopedrobarbosa/Cowork/Msc_BMT/retrofit_3M_IA/outputs/019ebbef-9e17-7ac2-ab0c-6c2b6b2b00d6/presentations/revisao-apresentacao-final/edit-deck.mjs`
- Starter validado:
  `/Users/joaopedrobarbosa/Cowork/Msc_BMT/retrofit_3M_IA/outputs/019ebbef-9e17-7ac2-ab0c-6c2b6b2b00d6/presentations/revisao-apresentacao-final/template-starter.pptx`
- PPTX revisado atual:
  `/Users/joaopedrobarbosa/Cowork/Msc_BMT/retrofit_3M_IA/artigos_materiais/ApresentacaoFinal_PESC_Retrofit_3M_5.0_revisada.pptx`
- Parecer acadêmico:
  `/Users/joaopedrobarbosa/Cowork/Msc_BMT/retrofit_3M_IA/artigos_materiais/parecer_revisao_apresentacao_final_2026-06-12.md`

Sua tarefa é concluir o último ciclo de QA e entregar o PPTX final.

Prioridades imediatas:

1. Corrija no `edit-deck.mjs` os erros restantes do `check_layout_quality.mjs`:
   - slide 10: padding dos blocos `Stat 93`, `Seta Resultado` e `Stat 20`;
   - slides 19–22: corpo das referências começa em `top=135` e sobrepõe a caixa do título; mova para cerca de `top=155` e ajuste a altura, preservando as 46 referências.
2. Execute novamente `edit-deck.mjs` usando o Node bundled indicado no handoff.
3. Regenere os previews e o contact sheet.
4. Inspecione visualmente todos os slides, com atenção especial aos slides 4, 10, 13, 14, 16, 17 e 19–23.
5. Reexecute `check_layout_quality.mjs` e `check_template_fidelity.mjs`.
6. Confirme que os slides 19–22 contêm exatamente as 46 referências efetivamente citadas no artigo, numeradas de `[1]` a `[46]`.
7. Preserve o título atual, o template PESC/COPPE, as cores, a proporção 4:3 e as decisões acadêmicas documentadas no handoff.

Regras:

- Não invente autores, dados, citações ou resultados.
- Não altere o PPTX original.
- Não use `python-pptx`, edição direta de OOXML ou LibreOffice para modificar o arquivo final.
- Use `@oai/artifact-tool`, importando o `template-starter.pptx` e exportando com `PresentationFile.exportPptx`.
- Não reverta mudanças preexistentes do usuário no repositório.
- Não declare concluído enquanto houver clipping, sobreposição, referência ausente ou falha de fidelidade.

Ao terminar, informe de forma concisa:

- caminho absoluto do PPTX final;
- quantidade de slides e referências;
- resultados dos dois checks de QA;
- qualquer risco residual que não tenha sido possível eliminar.
