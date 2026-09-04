# Prompt de retorno ao Codex — fechar QA e entregar PPTX final

> **Contexto:** o deck passou por uma verificação cruzada no Claude. O QA visual e a conferência das 46 referências já foram feitos e estão confirmados (ver abaixo). O Claude **não consegue** rodar o pipeline `@oai/artifact-tool` nem os checkers (o runtime do Codex e os scripts em `~/.codex/...` / `~/.cache/codex-runtimes/...` não estão acessíveis ao sandbox dele). Por isso, os ajustes geométricos finais voltam para você concluir no pipeline original.

---

Continue a revisão da apresentação acadêmica **a partir do estado atual**, sem reiniciar e sem redesenhar do zero. Use o workspace e o fluxo já existentes:

- Workspace: `/Users/joaopedrobarbosa/Cowork/Msc_BMT/retrofit_3M_IA/outputs/019ebbef-9e17-7ac2-ab0c-6c2b6b2b00d6/presentations/revisao-apresentacao-final`
- Script principal: `edit-deck.mjs` (importa `template-starter.pptx`, edita com `@oai/artifact-tool`, exporta o PPTX revisado)
- Saída: `/Users/joaopedrobarbosa/Cowork/Msc_BMT/retrofit_3M_IA/artigos_materiais/ApresentacaoFinal_PESC_Retrofit_3M_5.0_revisada.pptx`
- Handoff de referência: `artigos_materiais/HANDOFF_revisao_apresentacao_Claude_2026-06-12.md`

## Já verificado no Claude (não precisa refazer, mas confirme ao final)

- **QA visual** (render via LibreOffice, 100 dpi) dos 23 slides — **sem clipping, sobreposição visível ou cabeçalho invisível**. Inspecionados com atenção: 4, 10, 13, 14, 16, 17, 19, 22, 23. Tabelas dos slides 13/19/22 com cabeçalhos legíveis (texto branco sobre azul).
- **Referências:** `used-references.json` tem **exatamente 46** entradas; o deck contém os marcadores **`[1]` a `[46]` sem lacunas**, distribuídos nos slides 19–22 (19=[1–12], 20≈[13–24], 21≈[25–35], 22=[36–46]).
- **Rodapé/autoria/total:** `Martins · Costa · Lopes`, `/23` — corretos.
- Observação: os avisos do `check_layout_quality.mjs` são **geométricos/sub-pixel** e **não aparecem no render**; precisam ser fechados no checker do próprio pipeline.

## Punch-list a aplicar no `edit-deck.mjs`

1. **Slide 10 — padding inferior de ~11 px** nos blocos `Stat 93`, `Seta Resultado` e `Stat 20`: subir/reduzir esses elementos alguns pixels para zerar o aviso de padding.
2. **Slide 10 — aviso `split-inline`** entre a seta e o bloco da direita: aumentar levemente o espaço horizontal entre a `Seta Resultado` e o bloco `Stat 20`.
3. **Slides 19–22 — sobreposição título×corpo:** o título herdado vai até `top≈147` e o corpo das referências começa em `top=135`. Mover o corpo para **`top≈155`** e reduzir a altura para **≈465**, **preservando as 46 referências visíveis** (sem cortar a última linha do slide 22).

## Passos

1. Editar `edit-deck.mjs` com os ajustes acima.
2. Reexecutar:
   ```bash
   cd /Users/joaopedrobarbosa/Cowork/Msc_BMT/retrofit_3M_IA/outputs/019ebbef-9e17-7ac2-ab0c-6c2b6b2b00d6/presentations/revisao-apresentacao-final
   /Users/joaopedrobarbosa/.cache/codex-runtimes/codex-primary-runtime/dependencies/node/bin/node edit-deck.mjs
   ```
3. Regenerar previews e o `final-contact-sheet.png` (`make_contact_sheet.py`, `--cols 4`).
4. Reexecutar **`check_layout_quality.mjs`** (meta: sem erros) e **`check_template_fidelity.mjs`** (deve continuar `pass`, `issueCount: 0`).
5. Inspeção visual final, com foco em 4, 10, 13, 14, 16, 17 e 19–23.
6. Confirmar `[1]`–`[46]` sem lacunas após o reflow das caixas de referência.

## Pedido extra (para permitir nova revisão cruzada no Claude)

Ao concluir, **disponibilize numa pasta acessível** (dentro de `…/revisao-apresentacao-final/` ou em `artigos_materiais/`):

- o **PPTX final** já corrigido;
- o **`final-contact-sheet.png`** atualizado e os PNGs de `preview/final/`;
- os **relatórios dos dois checkers** (saída de `check_layout_quality.mjs` e `check_template_fidelity.mjs`) em arquivos `.txt`/`.json`;
- o **`used-references.json`** (já presente).

Esses artefatos são PNG/PPTX/TXT/JSON "puros" — o Claude consegue lê-los no sandbox para a próxima rodada de QA, mesmo sem o `@oai/artifact-tool`.

## Regras (inalteradas)

- Não inventar autores, dados, citações ou resultados.
- Não alterar o PPTX original (`…_5.0.pptx`).
- Continuar com `@oai/artifact-tool` + template-following; **não** usar `python-pptx`, OOXML direto ou LibreOffice no arquivo final.
- Não reverter mudanças preexistentes do usuário no repositório.
- Não declarar concluído enquanto houver clipping, sobreposição, referência ausente ou falha de fidelidade.

## Ao terminar, reporte (conciso)

- caminho absoluto do PPTX final;
- nº de slides e de referências;
- resultado dos dois checkers (idealmente `check_layout_quality` sem erros e `check_template_fidelity` = pass);
- qualquer risco residual não eliminado.
