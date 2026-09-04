# Prompt para Agente Redator - Correções da Revisão Holística Final

Antes de iniciar, carregue e assuma explicitamente o agente já criado e disponível em:

`/Users/joaopedrobarbosa/Cowork/Msc_BMT/retrofit_3M_IA/artigos_materiais/agentes/redator_agent.md`

Você deve atuar como o **Agente Redator Acadêmico — Modelo 3M 5.0** definido nesse arquivo. As instruções abaixo complementam esse agente para a rodada específica de correções da revisão holística final.

Artigo alvo:

`/Users/joaopedrobarbosa/Cowork/Msc_BMT/retrofit_3M_IA/artigo final/`

## Objetivo

Aplicar uma rodada de revisão fina no artigo "Retrofit do Modelo 3M de Universidade Corporativa: Reinterpretação de seus Três Pilares à Luz da Inteligência Artificial", preservando a contribuição central e endereçando os pareceres holísticos consolidados.

Use como insumo principal:

`/Users/joaopedrobarbosa/Cowork/Msc_BMT/retrofit_3M_IA/artigos_materiais/parecer_consolidado_merge_revisao_holistica_final.md`

Use também, se precisar de detalhe:

- `/Users/joaopedrobarbosa/Cowork/Msc_BMT/retrofit_3M_IA/artigos_materiais/claude_opus_4.8_v1_revisao_holistica_final.md`
- `/Users/joaopedrobarbosa/Cowork/Msc_BMT/retrofit_3M_IA/artigos_materiais/gpt5_codex_v1_revisao_holistica_final.md`
- `/Users/joaopedrobarbosa/Cowork/Msc_BMT/retrofit_3M_IA/artigos_materiais/artigos_materiais/02_Catalogo/catalogo_artigos.csv`

## Decisão autoral importante

Referências que não estão no catálogo da scoping review NÃO são problema. Elas podem e devem ser mantidas quando funcionam como arcabouços fundacionais para a construção conceitual, por exemplo Costa, Prat, Stollenwerk, Jarrahi, Pan, Birkstedt, Orlikowski, Bender, Edmondson, Argyris, Foucault, AI Act, Ng e Dell'Acqua.

Portanto:

- não remova citações externas apenas por não estarem no SLR;
- não substitua arcabouços fundacionais por artigos do catálogo se isso empobrecer o argumento;
- use artigos ainda não citados do catálogo apenas para reforçar pontos subancorados ou monoancorados;
- se necessário, acrescente uma frase metodológica dizendo que a scoping review fornece o corpus temático de evidências, enquanto arcabouços fundacionais complementares são mobilizados para sustentação conceitual.

## Decisão autoral sobre a implementação do SLR

Mantenha, por enquanto, a descrição técnica da implementação do `SLR-RAG Agentic Pipeline` da forma como está. Não condense, não mova para apêndice e não remova detalhes como `httpx`, `playwright`, `pydantic`, NFKD, `pgvector`, hashes, Zotero/Obsidian ou mecanismos de defesa contra prompt injection.

Motivo: os autores ainda vão discutir com as orientadoras se essa seção permanece no corpo do artigo, vira apêndice, deriva para artigo separado ou recebe outro tratamento. Nesta rodada, edite essa parte apenas para corrigir erro factual, problema de compilação ou imprecisão metodológica objetiva.

## Regra dura de autoria e anonimato

Nunca atribua a perspectiva de IA como agente, a dupla perspectiva ferramenta/agente, ou qualquer parte do Modelo 3M 5.0 a uma sugestão, feedback ou provocação de professor específico. Não escrever formulações como "sugerida por professor", "feedback de professor", "adição de professor" ou equivalentes no artigo, resumo, notas, comentários ou texto de apoio ao manuscrito.

Formulação correta: tratar essa perspectiva como parte da proposta conceitual do próprio artigo/modelo. Exemplo aceitável: "A reinterpretação do status ontológico e operacional da Inteligência Artificial no ambiente de trabalho constitui o núcleo da perspectiva agêntica proposta no Modelo 3M 5.0."

## Arquivos a editar

Edite apenas o necessário:

- `artigo final/main.tex`
- `artigo final/sections/introducao.tex`
- `artigo final/sections/referencial.tex`
- `artigo final/sections/metodologia.tex`
- `artigo final/sections/retrofit.tex`
- `artigo final/sections/analise.tex`
- `artigo final/sections/discussao.tex`
- `artigo final/sections/conclusao.tex`
- `artigo final/references.bib` somente se inserir nova citação que ainda não exista no BibTeX.

Não altere PDFs, catálogo, arquivos de parecer ou materiais auxiliares.

## Prioridades obrigatórias

### P0 - Corrigir precisão metodológica

1. Corrija a ambiguidade numérica da triagem em `metodologia.tex`.

Formulação esperada:

```tex
Após a deduplicação de 15 registros, o processo consolidou 114 entradas únicas (25 provenientes da Etapa 0 de mapeamento de base e 89 resultantes da execução direta das equações de busca). Destas, 21 foram excluídas por inacessibilidade física permanente, resultando em um catálogo final de \textbf{93 artigos aprovados} indexados localmente com PDF completo.
```

2. Remova "demonstra de forma empírica" ou qualquer equivalente que sugira validação empírica organizacional.

Use algo como:

```tex
Essa validação conceitual-construtiva sustenta, em nível comparativo, que o Modelo 3M 5.0 cobre dimensões pouco desenvolvidas nos 19 modelos examinados...
```

3. Explicite que a escala `Ausente/Parcial/Pleno` mede cobertura conceitual, não efetividade empírica.

### P1 - Reequilibrar método e argumento

4. Não condense a descrição técnica do `SLR-RAG Agentic Pipeline` nesta rodada. Preserve a granularidade atual da implementação.

5. Corrija apenas elementos objetivos do método: números da triagem, distinção entre validação conceitual-comparativa e validação empírica, clareza da escala `Ausente/Parcial/Pleno` e eventual frase de escopo sobre corpus SLR versus arcabouços fundacionais externos.

6. Não crie Apêndice A, não remeta a implementação para apêndice e não proponha artigo separado no texto do manuscrito. Essa decisão ficará com os autores e orientadoras.

### P2 - Coesão global

7. Reduza repetição do gap dos "19 modelos". Declare plenamente na Introdução; na Metodologia e Análise, retome operacionalmente; nas demais seções use remissões curtas.

8. Ajuste o fechamento do Referencial para não antecipar o loop completo `Moment -> Model -> Motive`. O Referencial deve fechar com lacuna/requisitos teóricos; a solução deve aparecer no Retrofit.

9. Melhore a transição Análise -> Discussão, conectando Agência Ativa de IA e Governança Algorítmica às implicações discutidas depois.

10. Ajuste a Conclusão para sintetizar, não abrir novas frentes. Mantenha AI Act, AI literacy e impactos psicossociais se já estiverem adequadamente preparados na Discussão; caso contrário, reduza a densidade.

### P3 - Purificação de AI-isms

11. Reduza o padrão `não apenas ... mas ...` para no máximo duas ocorrências no artigo.

12. Elimine ou reescreva expressões como:

- "No cenário contemporâneo"
- "É importante notar"
- "Nesse contexto sociotécnico complexo"
- "reside em" quando usado repetidamente
- "Em síntese" em excesso
- "vivo e emergente"
- "resolução mais sofisticada"
- "práticas organizacionais inegociáveis"
- "mudou radicalmente"
- "profunda transformação"

13. Prefira formulações acadêmicas secas, diretas, impessoais e epistemologicamente precisas.

## Ancoragens teóricas recomendadas

Antes de inserir qualquer nova citação do catálogo:

1. Verifique se a chave já existe em `references.bib`.
2. Se não existir, adicione entrada BibTeX consistente.
3. Não invente DOI, periódico, título, autores ou achados.
4. Use apenas o que o catálogo e/ou PDF local sustentam.

Priorize inserir poucas referências de alto retorno, não uma enxurrada de citações.

### Inserções de maior retorno

- `E0A01`: reforçar tecnologia em modelos contemporâneos de Corporate University.
- `E0A20`: reforçar a evolução SECI sob GenAI, em diálogo com GRAI.
- `S7A04`: reforçar governança de IA em Digital HRM/accountability.
- `S6A03`: reforçar workplace education com IA.
- `S8A07`: reforçar deskilling/reskilling/upskilling sob GenAI.

### Inserções opcionais

- `S2A04`: trajetória e estrutura intelectual de Corporate University.
- `E0A08`: knowledge augmentation e simbiose humano-IA.
- `E0A17`: systematic review de AI e knowledge creation.
- `S6A08`: IA no trabalho como double-edged sword.
- `S4A05`, `S4A07`, `S9A06`, `S10A03`: RAG/KG/Enterprise KM.
- `S7A10`: governança algorítmica e inovação responsável.

## Diffs orientadores

Use os diffs em:

`artigos_materiais/parecer_consolidado_merge_revisao_holistica_final.md`

Eles são orientadores, não obrigatórios palavra por palavra. Preserve coerência com o texto final.

## Critérios de aceitação

Ao finalizar:

1. O artigo deve compilar em LaTeX sem erro.
2. Não deve haver citações sem entrada em `references.bib`.
3. O método deve declarar corretamente os números da triagem: 129 triados, 15 duplicados/NV, 114 únicos, 21 inacessíveis, 93 aprovados finais.
4. A validação deve ser descrita como conceitual-comparativa, não empírica.
5. O texto deve preservar a arquitetura 3M 5.0:
   - `Motive 5.0`: sensing contínuo de competências.
   - `Model 5.0`: laboratório vivo/RAG/KG/aprendizagem no fluxo.
   - `Moment 5.0`: governança algorítmica adaptativa.
   - IA como ferramenta e como agente organizacional.
6. As referências externas fundacionais devem ser mantidas quando úteis.
7. O texto deve ficar mais seco, menos repetitivo e menos marcado por AI-isms.

## Entrega esperada

Ao concluir, entregue:

1. lista objetiva dos arquivos alterados;
2. resumo das mudanças por seção;
3. novas citações adicionadas, se houver;
4. resultado da compilação LaTeX;
5. pendências ou decisões autorais que ainda exigem validação humana.
