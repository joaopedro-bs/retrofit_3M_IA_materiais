# Plano de Revisão e Download: PAYWALL & OA_INACESSÍVEL

Este documento serve como manual de instruções operacionais para o agente/modelo encarregado de revisar e baixar os artigos classificados como `PAYWALL` ou `OA_INACESSÍVEL` no projeto **GE — Gestão Aumentada do Conhecimento (CPS831)**.

---

## 🎯 Objetivo
Executar a revisão de **64 artigos** que estão catalogados com acesso restrito (`PAYWALL`) ou que falharam no download automático (`OA_INACESSÍVEL`), utilizando:
1. **Acesso Institucional Confederado (CAFE/CAPES/UFRJ)** via navegador interativo com login do usuário para artigos sob paywall.
2. **Download via Navegador Gerenciado** para contornar proteções anti-bot (Cloudflare, JS-rendering) em artigos de acesso aberto catalogados como `OA_INACESSÍVEL`.
3. **Atualização Geral:** Atualizar o catálogo, mover os PDFs e re-executar os scripts de consolidação e reestruturação.

---

## 📂 Diretórios e Arquivos Críticos

* **Workspace local:** `/Users/joaopedrobarbosa/Cowork/Msc_BMT/msc_GE_20261/`
* **Obsidian Vault:** `/Users/joaopedrobarbosa/Obsidian/Pessoal & Msc/02 - Mestrado/Disciplinas/GE — Gestão Aumentada do Conhecimento/trabalho final/artigos_materiais/`
* **Catálogo CSV:** `artigos_materiais/02_Catalogo/catalogo_artigos.csv`
* **Pasta de Destino dos PDFs:** `artigos_materiais/01_PDFs/<eixo_nome>/`
* **Pasta de Fichas:** `artigos_materiais/03_Fichas/fichas-individuais/<eixo_nome>/`
* **Scripts de Consolidação:**
  * `/Users/joaopedrobarbosa/.gemini/antigravity-ide/scratch/consolidate.py` (Gera `00_RANKING.md` e `biblioteca.ris`)
  * `/Users/joaopedrobarbosa/.gemini/antigravity-ide/scratch/restructure_and_ficha_mestre.py` (Reorganiza fichas e gera `ficha_mestre.md`)

---

## 🛠️ Instruções Passo a Passo para o Agente de Execução

### Passo 1: Autenticação Federada (Acesso CAFE/CAPES)
1. Abra o navegador gerenciado (use a ferramenta do navegador do seu ambiente, como devtools/chrome tools).
2. Navegue para o Portal de Periódicos CAPES: `http://www.periodicos.capes.gov.br/`
3. Localize e clique no link **"Acesso CAFE"** (Comunidade Acadêmica Federada).
4. No campo de busca de instituições, selecione **"UFRJ - Universidade Federal do Rio de Janeiro"** (ou a instituição que o usuário indicar) e clique em enviar.
5. **Ação do Usuário:** Pare a execução de ferramentas e instrua o usuário explicitamente a realizar o login informando seu usuário e senha institucionais na página de autenticação que se abriu.
6. Aguarde a confirmação do usuário de que o login foi efetuado e o Portal CAPES reconhece o acesso institucional (ex.: *"Acesso por: Universidade Federal do Rio de Janeiro"* no topo da tela).

### Passo 2: Processamento dos Artigos `PAYWALL` (Acesso via CAFE)
Para cada artigo com status `PAYWALL` no arquivo `catalogo_artigos.csv`:
1. Recupere o `DOI` ou a `URL` do artigo.
2. No mesmo navegador autenticado no Portal CAPES, acesse o link do artigo (ou busque o DOI/Título na barra de busca do Portal CAPES para ser redirecionado com o proxy institucional ativo).
3. O site do periódico (IEEE Xplore, ScienceDirect/Elsevier, Emerald Insight, SpringerLink, Wiley, etc.) deve reconhecer o acesso institucional.
4. Caso o acesso esteja liberado, clique para baixar o arquivo PDF.
5. Salve o PDF localmente na pasta de Downloads ou diretamente na pasta do eixo correto dentro de `artigos_materiais/01_PDFs/<eixo_nome>/`.
   * *Atenção:* Nomeie o arquivo seguindo o padrão já estabelecido (ex: `Autor_Ano_titulo-curto.pdf`).
6. Valide se o arquivo foi baixado por completo (tamanho $>0$ bytes e cabeçalho `%PDF`).
7. **Atualize o Catálogo:**
   * Altere a coluna `acesso` de `PAYWALL` para `BAIXADO`.
   * Preencha a coluna `arquivo_local` com o caminho relativo (ex: `01_PDFs/<eixo_nome>/<nome_arquivo>.pdf`).
   * Sincronize a linha alterada nos dois catálogos (Workspace e Obsidian).

### Passo 3: Processamento dos Artigos `OA_INACESSÍVEL` (Bypass do Navegador)
Para os artigos classificados como `OA_INACESSÍVEL`:
1. Abra a URL do artigo no navegador gerenciado.
2. Como o navegador simula um usuário real (com suporte a JavaScript e rendering completo), ele contorna proteções de Cloudflare/anti-scraping simples.
3. Se o PDF estiver visível na página ou houver um link direto de download, clique e salve-o na pasta do respectivo eixo.
4. **Atualize o Catálogo:**
   * Mude o status de `OA_INACESSÍVEL` para `BAIXADO`.
   * Insira o caminho relativo do arquivo em `arquivo_local`.
   * Sincronize nos catálogos do Workspace e do Obsidian.

### Passo 4: Re-Consolidação dos Dados
Após finalizar a rodada de downloads bem-sucedidos:
1. Execute o script de consolidação do ranking:
   ```bash
   python3 /Users/joaopedrobarbosa/.gemini/antigravity-ide/scratch/consolidate.py
   ```
   *(Isso atualizará os arquivos `00_RANKING.md` e `biblioteca.ris` tanto no Workspace quanto no Obsidian).*
2. Execute o script de reestruturação de fichas:
   ```bash
   python3 /Users/joaopedrobarbosa/.gemini/antigravity-ide/scratch/restructure_and_ficha_mestre.py
   ```
   *(Isso garantirá que as novas fichas sejam movidas e o arquivo `ficha_mestre.md` seja atualizado com as novas relevâncias e status).*
3. Atualize a tabela de progresso no arquivo `STATUS_PROJETO_GE.md` marcando a revisão e downloads como concluídos.
