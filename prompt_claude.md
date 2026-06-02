# Prompt para o Claude

Copie e cole o texto abaixo em uma nova sessão do Claude (que possui o MCP do PowerPoint habilitado) para que ele execute a geração da apresentação perfeitamente.

---

```text
Olá! Preciso que você crie/ajuste a minha apresentação de slides em PowerPoint (.pptx) de 10 minutos (média de 1 minuto de fala por slide de conteúdo) sobre os resultados parciais e evolução do meu trabalho final.


Você deve usar como base de conhecimento do projeto, histórico de decisões e status do desenvolvimento o seguinte arquivo (disponível tanto localmente quanto no Obsidian):

- Caminho local: `/Users/joaopedrobarbosa/Cowork/Msc_BMT/msc_GE_20261/artigo final/detalhes_status_apresentacao.md`
- Obsidian: `02 - Mestrado/Disciplinas/GE — Gestão Aumentada do Conhecimento/trabalho final/Guia de Apresentação Parcial - Retrofit 3M 5.0.md`
- Pode consultar todo o obsidian referente a disciplina, bem como nosso historico discutindo este projeto. E todo o conteudo do caminho Users/joaopedrobarbosa/Cowork/Msc_BMT/msc_GE_20261/artigo final/

Por favor, leia um dos arquivos acima por completo antes de começar. A partir das informações contidas nele (o feedback do prof. Jano sobre IA como agente, o scoping review de 93 artigos, o relatório da Gartner, a escrita das Seções I e II prontas e o cronograma), você deve raciocinar e projetar a estrutura ideal da apresentação (cerca de 10 slides de conteúdo mais capa e encerramento), definindo os títulos dos slides, os bullets e os speaker notes para guiar minha fala de 1 minuto por slide.

---

### Suas Diretrizes de Execução:

1. **Arquivo de Origem (Template)**:
   - Caminho: `/Users/joaopedrobarbosa/Cowork/Msc_BMT/msc_GE_20261/artigo final/Modelo de Apresentação do PESC.pptx`
   - Use este arquivo como template. Ele já possui os layouts oficiais do PESC com o design de fundo, cores e logos corretos.

2. **Arquivo de Saída**:
   - Salve o resultado final como: `/Users/joaopedrobarbosa/Cowork/Msc_BMT/msc_GE_20261/artigo final/Apresentacao_PESC_Retrofit_3M_5.0.pptx`

3. **Como Construir (Limpeza de Rascunhos)**:
   - Abra o template.
   - Delete TODOS os slides existentes nele primeiro, para que a apresentação final tenha exatamente e apenas os slides que vamos gerar agora.
   - Adicione os novos slides usando os layouts internos do próprio template:
     - **Layout Index 0 (TITLE)**: Use para a Capa (Slide 0) e Agradecimentos (Slide final).
     - **Layout Index 7 (Definição)**: Use para todos os slides de conteúdo (Slides intermediários).

4. **Tratamento de Textos e Bullets (Crucial para o Design)**:
   - Não faça cópia ou clonagem de XML bruto (`spTree`) de outros slides. Isso quebra relações e corrompe o arquivo.
   - Use a API limpa de placeholders do `python-pptx`.
   - Para títulos, defina a propriedade `.text` do placeholder correspondente (idx=0).
   - Para o corpo com bullets (idx=1), limpe o text frame e adicione cada parágrafo separadamente.
   - Defina o nível do parágrafo utilizando `.level = 0` para bullets principais e `.level = 1` para sub-bullets. Isso garantirá que o PowerPoint aplique as fontes (Calibri), tamanhos, cores (#222222) e estilos de marcador de forma 100% nativa do slide master.

5. **Notas do Apresentador**:
   - Defina o texto de speaker notes (`slide.notes_slide.notes_text_frame.text`) para cada slide com o roteiro que você mesmo projetar para garantir o tempo de fala de 1 minuto.
```
