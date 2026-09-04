# Prompt para Agente Redator - Revisao Holistica v2

Antes de iniciar, carregue e assuma explicitamente o agente ja criado e disponivel em:

`/Users/joaopedrobarbosa/Cowork/Msc_BMT/retrofit_3M_IA/artigos_materiais/agentes/redator_agent.md`

Voce deve atuar como o **Agente Redator Academico - Modelo 3M 5.0** definido nesse arquivo. As instrucoes abaixo complementam esse agente para a rodada final de polimento e correcao.

## Objetivo

Aplicar as correcoes consolidadas da segunda revisao holistica final no artigo:

`/Users/joaopedrobarbosa/Cowork/Msc_BMT/retrofit_3M_IA/artigo final/`

Insumo principal obrigatorio:

`/Users/joaopedrobarbosa/Cowork/Msc_BMT/retrofit_3M_IA/artigos_materiais/parecer_consolidado_v2_revisao_holistica_final.md`

Insumos auxiliares, se precisar de detalhe:

- `/Users/joaopedrobarbosa/Cowork/Msc_BMT/retrofit_3M_IA/artigos_materiais/claude_opus_4.8_v2_revisao_holistica_final.md`
- `/Users/joaopedrobarbosa/Cowork/Msc_BMT/retrofit_3M_IA/artigos_materiais/gpt5_codex_v2_revisao_holistica_final.md`
- `/Users/joaopedrobarbosa/Cowork/Msc_BMT/retrofit_3M_IA/artigos_materiais/artigos_materiais/02_Catalogo/catalogo_artigos.csv`

## Regras Autorais Bloqueantes

1. Nunca atribua a perspectiva de IA como agente, a dupla perspectiva ferramenta/agente ou qualquer parte do Modelo 3M 5.0 a sugestao, feedback, provocacao ou adicao de professor especifico.

2. Trate essa perspectiva como contribuicao conceitual do proprio artigo/modelo.

3. Nao remova referencias fundacionais externas ao catalogo apenas por nao estarem no SLR. Elas podem sustentar arcaboucos teoricos necessarios.

4. Nao condense a implementacao tecnica do `SLR-RAG Agentic Pipeline` nesta rodada. Manter a granularidade tecnica atual ate decisao dos autores/orientadoras. Edite essa parte apenas para corrigir erro factual, problema de compilacao ou imprecisao metodologica objetiva.

5. Nao invente referencias, autores, DOI, periodicos, resultados empiricos ou achados. Se inserir nova citacao do catalogo, confirme que ela existe no CSV e adicione BibTeX consistente se necessario.

## Arquivos que Podem Ser Editados

Edite apenas se necessario:

- `artigo final/main.tex`
- `artigo final/sections/introducao.tex`
- `artigo final/sections/referencial.tex`
- `artigo final/sections/metodologia.tex`
- `artigo final/sections/retrofit.tex`
- `artigo final/sections/analise.tex`
- `artigo final/sections/discussao.tex`
- `artigo final/sections/conclusao.tex`
- `artigo final/references.bib`, somente se inserir nova citacao.

Nao altere PDFs, catalogo, pareceres ou materiais auxiliares.

Se tambem for solicitado revisar a versao em ingles, aplique a mesma regra de autoria em:

- `artigo final en/sections/literature_review.tex`

## Ordem de Execucao

### P0 - Bloqueadores de submissao

1. Revarrer o artigo para garantir que nao ha atribuicao da perspectiva agêntica a professor especifico. Substituir qualquer ocorrencia por formulacao impessoal vinculada ao Modelo 3M 5.0.

Formula aceitavel:

```tex
A reinterpretação do status ontológico e operacional da Inteligência Artificial no ambiente de trabalho constitui o núcleo da perspectiva agêntica proposta no Modelo 3M 5.0.
```

2. Corrigir a ancoragem de `E0A20`: nao apresentar `E0A20` como fonte do GRAI. O GRAI deve permanecer atribuido a `E0A18`; `E0A20` deve aparecer apenas como proposta convergente de atualizacao do SECI sob GenAI.

3. Eliminar linguagem empirica indevida:

- `gap empírico` -> `lacuna teórica` ou `lacuna conceitual`;
- `validação empírico-qualitativa` -> `validação conceitual-comparativa` ou `análise comparativa de cobertura conceitual`;
- evitar qualquer promessa de validacao empirica organizacional ja realizada.

4. Manter o placeholder da Figura 1 (`\framebox`) exatamente como esta. Nao substituir, remover, redesenhar ou criar figura/diagrama; o autor adicionara a figura posteriormente.

5. Nao tratar a ausencia da figura final como pendencia bloqueante do agente redator. Apenas preservar caption, label e chamada textual para facilitar a substituicao futura pelo autor.

### P1 - Robustez argumentativa

6. Reduzir a circularidade da "validacao": sempre que possivel, trocar linguagem de "validacao" por "analise comparativa de cobertura conceitual".

7. Se couber sem alongar excessivamente, nomear 2 ou 3 modelos concretos do catalogo como exemplos da coluna "modelos tradicionais" na analise comparativa.

Candidatos possiveis:

- `S1A04`
- `S1A09`
- `S1A10`
- `S2A04`

Use apenas se o catalogo/ficha/PDF sustentar a frase. Nao invente caracteristicas dos modelos.

8. Explicitar o criterio de curadoria das 20 referencias selecionadas a partir dos 93 artigos.

Sugestao de frase:

```tex
A seleção das 20 referências mobilizadas diretamente na formulação do modelo priorizou aderência às lentes teóricas do estudo, centralidade para os processos de GC analisados e capacidade de sustentar as cinco dimensões comparativas definidas na validação conceitual.
```

### P2 - Polimento textual

9. Atualizar o resumo para o mesmo padrao do corpo revisado. Remover "cenario de profunda transformacao", "Atraves", "gap empirico", "falham" e "de forma integrada".

10. Remover antropomorfismo residual:

- `funcionário digital` -> `agente algorítmico organizacional`.

11. Secar marcadores de AI-ism:

- `É importante notar` -> iniciar diretamente pela tese;
- `Longe de sugerir` -> `Em vez de` ou `Sem`;
- `não apenas ... mas ...` -> reduzir ao minimo;
- `reside em` repetido -> reformular diretamente;
- `riscos corporativos de elevada gravidade` -> `riscos corporativos críticos`;
- `vitalidade conceitual` -> `consistência interna` ou `validade estrutural`.

12. Tornar citacoes recem-inseridas organicas:

- `S6A03`: mover para frase propria sobre workplace education apoiada por IA.
- `E0A01`: se soar terminal, integrar como evidencia do uso passivo de tecnologia em modelos de UC.
- `S7A04`: se mantida, conectar ao carater human-centric/digital HRM da governanca.

### P3 - Microconsistencia LaTeX

13. Trocar aspas retas em termos conceituais por aspas LaTeX:

```tex
``vigilância cognitiva''
``dependência de prompt''
``agente que aprende''
``cria conhecimento''
```

14. Padronizar hifens Unicode em `retrofit.tex` se nao prejudicar o texto.

15. Padronizar `RAG`, `GRAI`, `KG` em fonte normal, salvo decisao editorial contraria. Usar `\texttt{}` apenas para codigo/identificadores reais.

16. Padronizar `framework` em romano, salvo quando houver razao especifica para italico.

17. Evitar `\cite{...}` como sujeito:

```tex
Costa, Souza e Oliveira \cite{costa20113m}
Mora-Mora et al. \cite{mora2025model}
```

18. Padronizar a forma de citacao do Modelo 3M original entre resumo, corpo, legenda e `references.bib`.

## Citacoes Novas

Nao ampliar o referencial substancialmente nesta etapa.

Inserir nova citacao apenas se atender a um destes objetivos:

1. reduzir circularidade da analise comparativa;
2. reforcar RAG/KG com catalogo local;
3. tornar uma citacao ja sugerida organicamente necessaria.

Possiveis referencias para RAG/KG, se necessario:

- `S4A05`
- `S4A07`
- `S9A06`
- `S10A03`

## Validacao Final

Antes de entregar:

1. Rodar busca por termos de autoria indevida: `Prof.`, `sugerida`, `feedback`, `adição`, `provocação`.
2. Rodar busca por `gap empírico`, `empírico-qualitativa`, `funcionário digital`, `É importante notar`.
3. Verificar se todas as chaves citadas existem em `references.bib`.
4. Compilar LaTeX.
5. Reportar warnings relevantes: undefined refs/citations, overfull/underfull críticos, figuras quebradas.
6. Reportar apenas que a Figura 1 permanece como placeholder por decisao autoral, sem classificar isso como bloqueio do redator.

## Entrega Esperada

Ao concluir, entregue:

1. arquivos alterados;
2. resumo das mudancas por secao;
3. novas citacoes adicionadas, se houver;
4. resultado da compilacao;
5. pendencias humanas restantes; a Figura 1 deve constar apenas como placeholder mantido por decisao autoral, e a decisao sobre implementacao tecnica do SLR permanece em aberto.
