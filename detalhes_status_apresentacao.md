# Base de Conhecimento e Status de Desenvolvimento — Modelo 3M 5.0

Este documento reúne todas as informações de progresso do trabalho, embasamento teórico, decisões de design conceituais e restrições técnicas da apresentação. O objetivo é servir como fonte de contexto para que a Inteligência Artificial planeje, estruture e crie a apresentação de slides de forma inteligente e autônoma.

---

## 1. Metadados do Projeto
- **Mestrando**: João Pedro Barbosa
- **Programa**: PESC / COPPE-UFRJ (Engenharia de Sistemas e Computação)
- **Disciplina**: CPS831 — Gestão Aumentada do Conhecimento 5.0
- **Orientadoras**: Viviane Cunha Farias da Costa & Emilly
- **Título do Trabalho**: Retrofit do Modelo 3M de Universidade Corporativa à Luz da Inteligência Artificial

---

## 2. Status Atual de Desenvolvimento da Monografia (Artigo Final)

### A. Estrutura Textual do Artigo (IEEEtran de Duas Colunas)
O artigo está estruturado em 7 seções principais:
1. **Seção I: Introdução** — Contextualização da Gestão do Conhecimento (GC), o papel da Universidade Corporativa (UC), o gap empírico, a pergunta de pesquisa e os objetivos específicos do retrofit.
2. **Seção II: Referencial Teórico** — Mapeamento denso da literatura em 5 subseções temáticas (UC & Modelo 3M, GenAI & GC, Aprendizagem no Fluxo de Trabalho, IA como Agente Organizacional, Governança de IA).
3. **Seção III: Metodologia** — Formalização da abordagem conceitual-construtiva (retrofit teórico) e do protocolo de busca e curadoria sistemática de artigos.
4. **Seção IV: O Modelo 3M 5.0** — Reinterpretação dos três pilares clássicos (*Motive*, *Model* e *Moment*).
5. **Seção V: Análise Comparativa** — Validação conceitual do retrofit contra os 19 modelos de UC catalogados na literatura internacional recente.
6. **Seção VI: Discussão** — Contribuições teóricas e implicações práticas para a governança.
7. **Seção VII: Conclusão** — Limitações do estudo e rumos de trabalhos futuros.

### B. O que já está Escrito e Concluído
- **Redação Concluída**: Seção I (Introdução) e Seção II (Referencial Teórico) em português estão completamente redigidas, totalizando **4.345 palavras**. O texto é denso, formal e faz uso direto de citações integradas.
- **Estruturação do Rascunho LaTeX**: Toda a estrutura das Seções I a VII e o banco de referências (`references.bib`) estão configurados. Os capítulos III a VII estão atualmente vazios (apenas com `\section` e `\label`), para compilação sem erros.
- **Rascunho em Inglês (EN)**: Uma versão preliminar de 7 páginas em inglês, traduzindo fielmente a Introdução e a Revisão de Literatura, foi compilada com sucesso.

---

## 3. A Evolução do Modelo: O que Mudou desde a Proposta

### A. Feedback da Proposta (Prof. Jano Moreira de Souza)
O principal ponto de evolução do trabalho originou-se do feedback crítico da banca na defesa da proposta de pesquisa:
- **A Provocação**: A IA Generativa e os Large Language Models (LLMs) não devem ser vistos como meras tecnologias passivas ou ferramentas de busca de suporte.
- **A Resposta (A IA como Agente)**: No retrofit do modelo, a IA Generativa é incorporada sob uma **dupla perspectiva**:
  1. **IA como Ferramenta**: O papel clássico e utilitário (ex: automação de buscas, RAG corporativo de suporte, curadoria passiva de conteúdo).
  2. **IA como Agente Organizacional Ativo**: A IA agêntica atua de forma proativa no ecossistema da UC. Ela assume papéis de tomada de decisão (como um "colaborador digital"), negociando premissas, gerando conhecimento autônomo no fluxo de trabalho e gerando dados para auditar a própria governança.

### B. Reconfiguração dos Pilares (3M 5.0)
Essa dupla perspectiva foi integrada de forma transversal nas três visões do Modelo 3M:
- **Motive 5.0 (Sensing & Estratégia)**: Além do mapeamento de competências (ferramenta), a IA co-define trilhas de aprendizagem e estratégias com base no que infere da dinâmica interna.
- **Model 5.0 (Laboratório Vivo & Criação)**: Além de repositórios dinâmicos e RAGs de apoio (ferramenta), a IA participa como agente ativo na coprodução de soluções e geração de conhecimento tácito-explícito.
- **Moment 5.0 (Governança & Avaliação)**: Além do monitoramento de conformidade ética (ferramenta), a IA é sujeita a regras de governança e, ao mesmo tempo, gera dados ativos para auditar as regras e calibrar o aprendizado da UC.

### C. Aprofundamento do Referencial de GC Revisitado
A inclusão da IA-agente exigiu a busca e incorporação de novas teorias de GC e sociotécnicas:
- **Modelo GRAI (Böhm & Durst, 2025)**: Em substituição ao SECI de Nonaka, para explicar a integração e aplicação de conhecimento mediados por IA.
- **Co-evolução Híbrida (Islam & Ajmal, 2025)**: Coprodução de saberes corporativos por redes sociotécnicas heterogêneas (humanos + não-humanos).
- **Knowing Organizacional (Faraj et al., 2026)**: LLMs corporativos desafiando a exclusividade humana no ato de "saber" e negociar legitimidade técnica.

### D. Protocolo Metodológico de Scoping Review
Para dar robustez científica à revisão de literatura, foi conduzido um protocolo rigoroso de Scoping Review:
- **Busca**: Formulação de 10 equações de busca booleanas direcionadas a 6 eixos temáticos.
- **Varredura**: Inicialmente mapeados **93 artigos científicos indexados** em grandes bases (Scopus, Web of Science, etc.).
- **Filtro e Expansão**: O teto inicial do catálogo (20 artigos) foi removido na revisão para garantir profundidade teórica total, mantendo a curadoria de artigos de alta relevância (Q1/Q2).
- **Relatório Gartner**: Inserção de um relatório técnico recente da Gartner (sugestão da orientadora Viviane Costa) para complementar a visão científica acadêmica com dados e projeções contemporâneas do mercado corporativo.

---

## 4. Planejamento da Apresentação

### A. Restrições de Tempo e Foco
- **Tempo Limite**: Até 10 minutos (média de 1 minuto por slide de conteúdo).
- **Meta**: Apresentar os resultados parciais e a evolução do trabalho.
- **Foco da Banca (O que apresentar)**:
  - Focar na evolução conceitual: o feedback sobre "IA como agente organizacional", como isso reconfigurou o 3M 5.0 e as teorias de GC que sustentam essa agência.
  - Explicitar o protocolo metodológico de scoping de referências (as buscas, os 93 artigos e a ampliação da base bibliográfica com o relatório da Gartner).
  - Mostrar os resultados concretos de redação (Seções I e II prontas, volume de texto de 4.345 palavras) e o cronograma dos próximos passos.
- **O que Omitir**:
  - Evitar detalhar bugs de compilação, problemas com LaTeX, infraestrutura de diretórios, tradução para inglês ou detalhes operacionais de escrita do PDF. Focar estritamente no conteúdo científico e no progresso.

### B. Especificações Técnicas do Template do PESC (`Modelo de Apresentação do PESC.pptx`)
- **Layout 0: `TITLE`**
  - Placeholder `idx=0`: Título principal da capa/fim.
  - Placeholder `idx=1`: Subtítulo da capa/fim.
- **Layout 7: `Definição`**
  - Placeholder `idx=0`: Título do slide.
  - Placeholder `idx=1`: Caixa de texto para bullets (hierarquia de parágrafos `level=0` para bullet principal e `level=1` para sub-bullet).
  - Placeholder `idx=12`: Número do slide.
- **Layout 1: `Title and Content`**
  - Placeholder `idx=0`: Título do slide (ex: Referências).
  - Placeholder `idx=1`: Caixa de texto de conteúdo.

---

## 5. Instruções de Geração para a IA (Como Programar / Criar)

1. **Procedimento de Limpeza**: Carregar o arquivo `Modelo de Apresentação do PESC.pptx`. Remover todos os slides existentes do rascunho do template antes de adicionar os novos slides, para que a apresentação final tenha exatamente e apenas os slides gerados.
2. **Uso dos Layouts**:
   - Slide de Capa e Slide de Encerramento: Devem usar o **Layout 0 (TITLE)**.
   - Slides de conteúdo: Devem usar o **Layout 7 (Definição)**.
   - Slide de referências bibliográficas: Deve usar o **Layout 1 (Title and Content)**.
3. **Uso Nativo do Slide Master**:
   - Não tente duplicar ou clonar elementos XML de shapes (`spTree`) de slides de exemplo, pois isso quebra relações (`rId`) internas do arquivo pptx.
   - Adicione novos slides utilizando `prs.slides.add_slide(prs.slide_layouts[layout_idx])`.
   - Limpe o placeholder de conteúdo (`idx=1`) e use `tf.add_paragraph()` configurando o atributo `.level` para controlar as indentações. O próprio Slide Master aplicará automaticamente a fonte (Calibri), tamanhos, cores (#222222) e bullets corretos.
4. **Speaker Notes**: Preencher a área de notas de apresentador (`slide.notes_slide.notes_text_frame.text`) com o roteiro de fala sugerido para cada slide.
