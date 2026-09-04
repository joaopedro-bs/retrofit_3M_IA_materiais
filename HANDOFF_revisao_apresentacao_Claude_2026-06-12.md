# Handoff — revisão da apresentação acadêmica

Data: 2026-06-12

## Objetivo

Concluir a revisão crítica e visual da apresentação do artigo sobre o retrofit conceitual do Modelo 3M de Universidade Corporativa, preservando o template institucional PESC/COPPE e incluindo todas as referências efetivamente citadas no artigo.

## Arquivos principais

- PPTX original, que deve permanecer intacto:
  `/Users/joaopedrobarbosa/Cowork/Msc_BMT/retrofit_3M_IA/artigos_materiais/ApresentacaoFinal_PESC_Retrofit_3M_5.0.pptx`
- Cópia revisada já gerada, ainda sujeita ao último QA:
  `/Users/joaopedrobarbosa/Cowork/Msc_BMT/retrofit_3M_IA/artigos_materiais/ApresentacaoFinal_PESC_Retrofit_3M_5.0_revisada.pptx`
- Parecer crítico detalhado:
  `/Users/joaopedrobarbosa/Cowork/Msc_BMT/retrofit_3M_IA/artigos_materiais/parecer_revisao_apresentacao_final_2026-06-12.md`
- Artigo e bibliografia:
  `/Users/joaopedrobarbosa/Cowork/Msc_BMT/retrofit_3M_IA/artigo final/main.tex`
  `/Users/joaopedrobarbosa/Cowork/Msc_BMT/retrofit_3M_IA/artigo final/sections/`
  `/Users/joaopedrobarbosa/Cowork/Msc_BMT/retrofit_3M_IA/artigo final/references.bib`

## Workspace de edição

`/Users/joaopedrobarbosa/Cowork/Msc_BMT/retrofit_3M_IA/outputs/019ebbef-9e17-7ac2-ab0c-6c2b6b2b00d6/presentations/revisao-apresentacao-final`

Arquivos relevantes:

- `edit-deck.mjs`: script autoral principal. Importa `template-starter.pptx`, edita com `@oai/artifact-tool` e exporta o PPTX revisado.
- `template-frame-map.json`: mapeamento dos 23 slides para os slides-fonte.
- `template-audit.txt`, `deviation-log.txt`, `source-notes.txt`, `reference-audit.txt`.
- `used-references.json`: 46 referências citadas, na ordem de primeira ocorrência no artigo.
- `preview/final/`: PNGs dos 23 slides.
- `layout/final/`: arquivos de layout para QA.
- `final-contact-sheet.png`: contato anterior; deve ser regenerado após a última execução.

## Estado atual

- O deck revisado possui 23 slides.
- Slides 1–18: narrativa principal revisada.
- Slides 19–22: todas as 46 referências efetivamente citadas no artigo.
- Slide 23: apêndice técnico do pipeline SLR-RAG.
- Título do trabalho foi preservado.
- Autoria corrigida para João Pedro Barbosa Martins, Viviane Cunha Farias da Costa e Emily Lopes.
- Rodapé passou a mostrar `Martins · Costa · Lopes` e total `/23`.
- O `check_template_fidelity.mjs` passou sem problemas (`status: pass`, `issueCount: 0`).
- A inspeção visual mostrou conteúdo legível e o problema de cabeçalhos invisíveis das tabelas foi corrigido.

## Decisões acadêmicas já incorporadas

- O trabalho é apresentado como contribuição teórico-conceitual, não validação empírica.
- A comparação de cobertura é explicitamente denominada classificação autoral exploratória.
- Mora-Mora et al. são descritos com cuidado: 19 modelos anteriores catalogados; o artigo de 2025 também propõe um novo modelo com I4/I5.
- GRAI é tratado como extensão recente, ainda dependente de validação independente, e não como substituto consensual do SECI.
- Agência de IA significa agência operacional/material delimitada; não implica consciência, intenção própria ou aprendizagem contínua garantida.
- RAG, grafos de conhecimento, scaffolding, deskilling e human-in/on/out-of-the-loop foram definidos de forma mais precisa.
- AI Act aparece como referência de governança, não como validação do modelo.

## Pendências conhecidas antes da entrega final

1. Corrigir os avisos do QA de layout.

O comando executado foi:

```bash
/Users/joaopedrobarbosa/.cache/codex-runtimes/codex-primary-runtime/dependencies/node/bin/node \
  /Users/joaopedrobarbosa/.codex/plugins/cache/openai-primary-runtime/presentations/26.601.10930/skills/presentations/scripts/check_layout_quality.mjs \
  --layout /Users/joaopedrobarbosa/Cowork/Msc_BMT/retrofit_3M_IA/outputs/019ebbef-9e17-7ac2-ab0c-6c2b6b2b00d6/presentations/revisao-apresentacao-final/layout/final \
  --warn-only
```

Resultados restantes:

- Slide 10: três avisos de padding inferior de 11 px nos elementos `Stat 93`, `Seta Resultado` e `Stat 20`; mover/reduzir esses elementos alguns pixels resolve.
- Slide 10: aviso `split-inline` entre seta e bloco da direita; é provavelmente tolerável, mas pode ser eliminado aumentando o espaço entre ambos.
- Slides 19–22: o verificador detecta sobreposição entre título e corpo porque o título herdado tem caixa alta até `top=147` e o corpo começa em `top=135`. Mudar o corpo das referências para `top=155`, reduzindo a altura para aproximadamente `465`, elimina o alerta. Confirmar que todas as referências continuam visíveis.

2. Executar novamente o script após os ajustes:

```bash
cd /Users/joaopedrobarbosa/Cowork/Msc_BMT/retrofit_3M_IA/outputs/019ebbef-9e17-7ac2-ab0c-6c2b6b2b00d6/presentations/revisao-apresentacao-final
/Users/joaopedrobarbosa/.cache/codex-runtimes/codex-primary-runtime/dependencies/node/bin/node edit-deck.mjs
```

3. Regenerar o contact sheet:

```bash
/Users/joaopedrobarbosa/.cache/codex-runtimes/codex-primary-runtime/dependencies/python/bin/python3 \
  /Users/joaopedrobarbosa/.codex/plugins/cache/openai-primary-runtime/presentations/26.601.10930/skills/presentations/scripts/make_contact_sheet.py \
  --output /Users/joaopedrobarbosa/Cowork/Msc_BMT/retrofit_3M_IA/outputs/019ebbef-9e17-7ac2-ab0c-6c2b6b2b00d6/presentations/revisao-apresentacao-final/final-contact-sheet.png \
  --cols 4 \
  /Users/joaopedrobarbosa/Cowork/Msc_BMT/retrofit_3M_IA/outputs/019ebbef-9e17-7ac2-ab0c-6c2b6b2b00d6/presentations/revisao-apresentacao-final/preview/final/*.png
```

4. Reexecutar:

- `check_layout_quality.mjs`, idealmente sem erros.
- `check_template_fidelity.mjs`, que já passou, para confirmar que continua passando.

5. Fazer inspeção visual final, principalmente nos slides 4, 10, 13, 14, 16, 17 e 19–23.

6. Validar que existem 46 itens em `used-references.json` e que os slides 19–22 cobrem `[1]` a `[46]` sem lacunas.

7. Não alterar o PPTX original nem reverter mudanças preexistentes no repositório.

## Restrição técnica importante

Continuar usando `@oai/artifact-tool` e o fluxo de template-following. Não usar `python-pptx`, edição direta de OOXML ou LibreOffice para modificar o arquivo final.

## Critério de conclusão

Entregar o PPTX revisado somente após:

- QA visual dos 23 slides;
- 46 referências confirmadas;
- fidelidade do template aprovada;
- nenhum erro material de clipping, sobreposição ou cabeçalho invisível.
