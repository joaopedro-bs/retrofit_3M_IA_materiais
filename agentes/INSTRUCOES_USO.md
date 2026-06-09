# Guia de Uso — Multi-Agentes para Escrita Científica

Este diretório contém os perfis de sistema e diretrizes para estruturar o fluxo de trabalho de escrita científica da monografia/artigo **Modelo 3M 5.0** utilizando Inteligência Artificial em papéis especializados.

---

## 🛠️ Como Funciona o Workflow

O processo de escrita é colaborativo e adota o modelo de **Revisão por Pares (Peer Review)**, onde dois papéis distintos operam de forma sequencial para garantir rigor conceitual e qualidade de escrita:

1. **Agente Redator**: Recebe as diretrizes da seção, os artigos de base e escreve o código LaTeX correspondente.
2. **Agente Revisor**: Avalia criticamente o rascunho sob critérios de consistência teórica, validade bibliográfica (contra a base de fichas reais) e compilação LaTeX, gerando um relatório estruturado.
3. **Loop de Refinamento**: O Redator corrige o rascunho com base nas recomendações do Revisor.
4. **Humano-no-Loop**: Você (João Pedro) avalia e aprova a versão final para compilação.

---

## 🚀 Como Invocar e Usar os Agentes no Chat

Você pode delegar as tarefas a modelos de IA (via Antigravity, ChatGPT, Claude) a qualquer momento fornecendo os links e conteúdos destes manuais:

### Passo 1: Invocar o Redator para Escrever
Cole um comando semelhante a este no chat do modelo de redação:

> **Comando**:
> "Assuma o papel do [Agente Redator](file:///Users/joaopedrobarbosa/Cowork/Msc_BMT/retrofit_3M_IA/artigos_materiais/agentes/redator_agent.md) e redija a **Seção X: Título**. 
> Utilize as seguintes evidências e literatura como base: [inserir fontes/dados].
> Escreva o arquivo correspondente em LaTeX de forma impessoal e densa."

### Passo 2: Invocar o Revisor para Validar
Após a geração do rascunho, utilize um modelo diferente (ou uma nova sessão) para realizar a revisão independente:

> **Comando**:
> "Assuma o papel do [Agente Revisor](file:///Users/joaopedrobarbosa/Cowork/Msc_BMT/retrofit_3M_IA/artigos_materiais/agentes/revisor_agent.md) e faça um peer-review Q1 crítico da seção X no arquivo [caminho.tex].
> Avalie rigorosamente a estrutura metodológica, as citações, a transição entre as teorias (ex: modelo GRAI) e emita o Parecer de Severidade (Alta, Média, Baixa) com os Diffs de correção sugeridos."
