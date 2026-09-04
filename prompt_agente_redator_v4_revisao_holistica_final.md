# Prompt de Execução para o Agente Redator Existente - Parecer Consolidado V4

Antes de iniciar, carregue e assuma integralmente o agente já criado em:

`/Users/joaopedrobarbosa/Cowork/Msc_BMT/retrofit_3M_IA/artigos_materiais/agentes/redator_agent.md`

Atue como o **Agente Redator Acadêmico - Modelo 3M 5.0** definido nesse arquivo. Não crie um novo papel ou perfil de agente.

As instruções abaixo complementam o perfil do agente exclusivamente para a aplicação do parecer consolidado V4. Em caso de conflito com prompts de rodadas anteriores, estas instruções V4 prevalecem. As restrições de rigor acadêmico, escopo estrito e tolerância zero a alucinações do agente permanecem obrigatórias.

Nesta execução, a orientação original do agente para fornecer somente código LaTeX deve ser interpretada como: editar diretamente os arquivos autorizados e entregar ao final apenas o resumo técnico solicitado, sem reproduzir integralmente o artigo no chat.

Sua tarefa é aplicar, de forma cirúrgica e verificável, o parecer consolidado da quarta revisão holística ao artigo em português:

`/Users/joaopedrobarbosa/Cowork/Msc_BMT/retrofit_3M_IA/artigo final/`

O parecer que constitui a fonte normativa desta execução é:

`/Users/joaopedrobarbosa/Cowork/Msc_BMT/retrofit_3M_IA/artigos_materiais/parecer_consolidado_v4_revisao_holistica_final.md`

Leia integralmente esse parecer antes de editar qualquer arquivo.

## Objetivo

Converter a versão atual do artigo em uma versão camera-ready tecnicamente consistente, aplicando todas as correções textuais, bibliográficas e de LaTeX já aprovadas, sem reestruturar a narrativa e sem introduzir novas decisões editoriais.

## Decisões Já Tomadas - Não Reabrir

1. **Não alterar o título.** Manter exatamente:

   `Retrofit do Modelo 3M de Universidade Corporativa: Reinterpretação de seus Três Pilares à Luz da Inteligência Artificial`

2. O abstract deve possuir **exatamente 250 palavras**, usando como referência a versão aprovada no parecer consolidado.
3. Manter a menção a Jeanne C. Meister, adicionar a citação no texto e criar a entrada `meister1998corporate` no `.bib`.
4. Usar `hidelinks` no `hyperref`.
5. Padronizar a ordem dos autores do Modelo 3M original como **Costa, Oliveira e Souza**.
6. Corrigir Birkstedt et al. para páginas **133--167**, mas essa correção é classificada como não bloqueante.
7. Não editar a versão inglesa nesta tarefa.

## Arquivos de Trabalho

- `artigo final/main.tex`
- Todos os arquivos em `artigo final/sections/`
- `artigo final/references.bib`

Não edite arquivos fora desse escopo, salvo a criação de um relatório final de execução em `artigos_materiais/`.

## Procedimento Obrigatório

### 1. Inventário Inicial

Antes de editar:

1. Leia `main.tex`, todas as seções e `references.bib`.
2. Verifique o estado atual do Git para não sobrescrever alterações existentes do autor.
3. Confirme se já existe algum arquivo real para a Figura 1.
4. Não invente, desenhe ou gere a Figura 1 sem uma fonte fornecida pelo autor.

### 2. Abstract com 250 Palavras

Substitua o abstract atual pelo texto de 250 palavras aprovado no parecer consolidado.

Requisitos:

- manter exatamente 250 palavras pelo critério de unidades separadas por espaço;
- preservar a natureza teórica da contribuição;
- não afirmar validação empírica;
- não inserir citação autor-data no abstract;
- não alterar o título.

Após a edição, execute uma contagem automatizada e registre o resultado no relatório final.

### 3. Correções Textuais Obrigatórias

Aplicar todas as correções abaixo, adaptando o contexto apenas se o arquivo já tiver sido parcialmente modificado:

1. `ao entrada` -> `à entrada`.
2. `coevolvem` -> `coevoluem`.
3. Remover a repetição em:

   `análise comparativa estruturada de cobertura teórica por meio de análise comparativa estruturada`.

4. Padronizar `Simbiose Homem-IA` como `Simbiose Humano-IA`.
5. Corrigir todas as menções narrativas para `Costa, Oliveira e Souza`.
6. Manter Meister e adicionar `\cite{meister1998corporate}` na primeira atribuição histórica pertinente.
7. Referenciar explicitamente a Figura 1 no corpo do texto com `Figura~\ref{fig:3m_original}`.

Não faça reescritas estilísticas amplas. Os usos de `Em síntese`, a repetição de `eminentemente` e outros ajustes cosméticos não são obrigatórios.

### 4. Figura 1

Se existir um arquivo final válido da Figura 1:

1. Coloque-o em localização coerente, preferencialmente `artigo final/figures/`.
2. Substitua o `\framebox` por `\includegraphics`.
3. Use largura adequada à coluna IEEE.
4. Atualize a legenda para citar `\cite{costa20113m}` e usar a ordem Costa, Oliveira e Souza.
5. Confirme que a figura é mencionada antes ou imediatamente após sua apresentação.

Se não existir arquivo real:

- não crie imagem fictícia;
- preserve o placeholder para não quebrar a compilação;
- registre a Figura 1 como único bloqueio humano remanescente no relatório final.

### 5. Hyperref

Remova a configuração de links coloridos e aplique:

```latex
\usepackage[hidelinks]{hyperref}
```

Não deixe uma segunda configuração conflitante em `\hypersetup`.

### 6. Inclusão de Meister no BibTeX

Adicionar a entrada:

```bibtex
@book{meister1998corporate,
  author    = {Meister, Jeanne C.},
  title     = {Corporate Universities: Lessons in Building a World-Class Work Force},
  edition   = {Rev. and updated ed.},
  publisher = {McGraw-Hill},
  address   = {New York},
  year      = {1998},
  isbn      = {978-0-7863-0787-6}
}
```

Após a inclusão, o estado esperado é **46 chaves citadas e 46 entradas bibliográficas**, sem órfãs.

### 7. Higiene do References.bib

#### Remover rastreabilidade interna

Remova todos os trechos `ID do Catálogo: ...` dos campos `note`.

No caso de `S7A06`, preserve somente:

```bibtex
note = {Preprint}
```

Nenhum `ID do Catálogo` pode aparecer no `.bib` ou no `.bbl` final.

#### Proteger acrônimos e nomes próprios

Proteja com chaves BibTeX os termos que o `IEEEtran.bst` não pode converter para minúsculas, incluindo:

- `{AI}`
- `{GenAI}`
- `{SECI}`
- `{GRAI}`
- `{HRM}`
- `{EU}`
- `{China}` e `{Chinese}`
- `{European}`
- `{Industry 4.0}` e `{Industry 5.0}`
- `{Artificial Intelligence Act}`

Use a lista completa de entradas indicada no parecer consolidado. Depois da compilação, inspecione o `.bbl`, não apenas o `.bib`.

#### Corrigir metadados e caracteres

1. Em `E0A18`, adicionar:

   `doi = {10.1108/VJIKMS-10-2024-0357}`

2. Preservar também a URL DOI, se desejado.
3. Codificar Böhm de forma segura para BibTeX clássico: `B{\"o}hm`.
4. Substituir o apóstrofo tipográfico em `Workers’ Skills` por apóstrofo ASCII.
5. Alterar Birkstedt et al. de `pages = {1--40}` para `pages = {133--167}`.

Não invente DOI, volume, número, páginas ou URLs ausentes. `E0A06` deve permanecer sinalizada para verificação se não houver fonte confiável disponível.

### 8. Validação Automatizada

Execute, a partir de `artigo final/`:

```bash
pdflatex -interaction=nonstopmode -halt-on-error main.tex
bibtex main
pdflatex -interaction=nonstopmode -halt-on-error main.tex
pdflatex -interaction=nonstopmode -halt-on-error main.tex
```

Depois valide:

1. zero erros fatais;
2. zero citações indefinidas;
3. zero referências indefinidas;
4. zero `Overfull`;
5. ausência de `ID do Catálogo` em `references.bib` e `main.bbl`;
6. acrônimos preservados no `main.bbl`;
7. cross-check **46/46**;
8. abstract com exatamente 250 palavras;
9. título rigorosamente inalterado;
10. PDF gerado em A4 com `IEEEtran`.

Avisos `Underfull` devem ser relatados. Não distorça tabelas ou texto apenas para eliminá-los se não houver defeito visual relevante.

### 9. Inspeção Visual

Revise o PDF final, especialmente:

- primeira página: título, autores, afiliação, e-mails, abstract e keywords;
- Figura 1 ou placeholder remanescente;
- três tabelas largas;
- seção de referências;
- equilíbrio das colunas na última página;
- total de páginas.

Não declare o artigo liberado se a Figura 1 continuar como placeholder ou se o limite de páginas do veículo não tiver sido confirmado.

## Proibições

- Não alterar o título.
- Não editar `artigo final en/`.
- Não reestruturar seções.
- Não remover limitações metodológicas para reduzir páginas sem autorização.
- Não inventar fontes ou metadados.
- Não gerar uma Figura 1 fictícia.
- Não remover citações válidas para simplificar o cross-check.
- Não reverter alterações preexistentes do autor.

## Entrega Final

Ao concluir:

1. Salve as alterações nos arquivos LaTeX/BibTeX.
2. Gere o PDF recompilado.
3. Crie o relatório:

   `artigos_materiais/relatorio_aplicacao_parecer_consolidado_v4.md`

4. O relatório deve conter:

   - arquivos modificados;
   - alterações aplicadas;
   - contagem final do abstract;
   - resultado do cross-check de citações;
   - resultado da compilação;
   - warnings remanescentes;
   - confirmação de ausência de IDs internos no `.bbl`;
   - confirmação de preservação dos acrônimos;
   - pendências humanas restantes;
   - veredito final `GO`, `GO condicionado` ou `NO-GO`.

## Critério de Conclusão

A tarefa somente está concluída quando as correções automatizáveis tiverem sido aplicadas, o PDF tiver sido recompilado e o relatório de execução tiver sido salvo. Caso a Figura 1 real não esteja disponível, conclua todas as demais correções e classifique o resultado como **GO condicionado exclusivamente à inserção da figura e à confirmação do limite de páginas**.
