# Atividade Avaliativa Prática — Parte 1

**Disciplina:** Engenharia de Software  
**Aluno(a):** Felipe Dos Santos Rodrigues
**Data:** 12/05/2026  

---

## Tarefa 1.1 — Proposta de Tema

O sistema proposto resolve a dificuldade de transformar conteúdos técnicos já produzidos pela startup, como artigos do blog, changelogs e releases, em peças curtas e consistentes para redes sociais. A ferramenta acompanha o repositório e o blog da empresa, identifica novidades relevantes e sugere roteiros de carrosséis para Instagram com estilo técnico-educativo. Os principais usuários são alguém de marketing de conteúdo, uma pessoa de produto ou a própria fundadora da startup, que precisa divulgar novidades sem perder precisão técnica. O problema é relevante porque reduz retrabalho, acelera a comunicação entre times e ajuda a manter uma presença institucional frequente sem depender de produção manual a cada publicação.

Minha reflexão: Escolhi um tema que junta automação e revisão humana porque ele tem um escopo viável para prototipação e, ao mesmo tempo, exige decisões reais de produto. A proposta não é gerar conteúdo final automaticamente, mas apoiar a criação com rastreabilidade e padronização, o que deixa o problema mais específico e mais próximo de um caso de uso real de startup.

---

## Tarefa 1.2 — Planejamento de Entrevista

Objetivo da entrevista: entender como a pessoa responsável por conteúdo institucional descobre novidades da startup, transforma informações técnicas em posts para redes sociais e quais obstáculos enfrentam no processo atual. A entrevista busca mapear rotina, dores, critérios de qualidade e expectativas sobre um sistema que detecta conteúdos novos e sugere roteiros de carrosséis, sem assumir que a automação substitui a validação humana. O foco é identificar como o trabalho acontece na prática, quais informações são indispensáveis e quais partes do fluxo têm mais custo, risco ou retrabalho.

1. Como você descobre quais novidades da empresa merecem virar conteúdo para redes sociais?
2. Quando sai um artigo novo, um changelog ou um release, qual é o seu fluxo atual para transformar isso em um post?
3. Que tipo de informação você considera indispensável para conseguir escrever um carrossel com segurança técnica?
4. Em quais momentos do seu trabalho você sente mais dificuldade para adaptar um conteúdo técnico para uma linguagem acessível?
5. Quantas pessoas normalmente participam da aprovação de um conteúdo antes da publicação?
6. O que costuma atrasar mais o processo hoje: encontrar a informação, escrever o texto, revisar tecnicamente ou ajustar o formato visual?
7. Quais problemas você já teve com soluções atuais, como planilhas, e-mails, documentos soltos ou ferramentas genéricas de IA?
8. Se uma ferramenta sugerisse roteiros automaticamente, o que faria você confiar ou desconfiar da sugestão?
9. O que seria um sinal claro de que essa ferramenta realmente economiza tempo e melhora a consistência do conteúdo?
10. Para encerrar, existe algum detalhe do seu fluxo de trabalho ou alguma restrição da empresa que eu não tenha perguntado e que seria importante considerar?

Minha reflexão: A entrevista precisa explorar tanto o processo editorial quanto os limites da automação, porque o risco aqui não é só técnico, mas também de comunicação e de confiança. Eu priorizei perguntas que revelam rotina, pontos de atrito e critérios de aprovação, já que isso orienta melhor o escopo do protótipo do que perguntas genéricas sobre redes sociais.

---

## Tarefa 1.3 — Histórias de Usuário

1. Como pessoa de marketing de conteúdo, quero que o sistema detecte automaticamente novos artigos, changelogs e releases do repositório e do blog para que eu não precise monitorar essas fontes manualmente.

Critérios de aceitação:
- O sistema deve permitir configurar quais fontes serão monitoradas.
- O sistema deve identificar novos itens publicados e registrar data, título e link de origem.
- O sistema deve evitar duplicar sugestões para o mesmo conteúdo já processado.

Prioridade: Alta. Essa história é a base do produto, porque sem detecção automática não existe ganho de produtividade nem fluxo contínuo de sugestões. Ela também sustenta as demais histórias, que dependem da identificação correta das novidades.

2. Como pessoa de marketing de conteúdo, quero que o sistema gere um roteiro de carrossel com tom técnico-educativo a partir de um conteúdo detectado para que eu tenha uma primeira versão pronta para revisão.

Critérios de aceitação:
- O sistema deve produzir uma estrutura com abertura, desenvolvimento e encerramento.
- O roteiro deve manter relação clara com o conteúdo de origem.
- O sistema deve sugerir texto por slide em linguagem adequada ao público da startup.

Prioridade: Alta. Essa é a principal entrega de valor percebida pelo usuário, pois reduz o esforço de transformar conteúdo técnico em formato de rede social. Também define o diferencial do sistema em relação a uma simples lista de links.

3. Como pessoa revisora, quero que o sistema destaque trechos técnicos, termos sensíveis e pontos que exigem validação humana para que eu consiga revisar o roteiro com mais rapidez e menos risco.

Critérios de aceitação:
- O sistema deve marcar partes do roteiro que dependem de confirmação técnica.
- O sistema deve indicar quando uma informação parece inferida e não explicitamente presente na fonte.
- O sistema deve permitir que o usuário aceite, ajuste ou rejeite cada sugestão destacada.

Prioridade: Alta. A revisão humana é um requisito central do tema e evita que a automação gere conteúdo incorreto ou arriscado. Essa funcionalidade aumenta a confiança no sistema e reduz retrabalho na etapa final.

4. Como pessoa de marketing de conteúdo, quero que o sistema sugira variações de roteiro para o mesmo conteúdo para que eu possa adaptar a publicação ao contexto da campanha ou ao tom da marca.

Critérios de aceitação:
- O sistema deve apresentar pelo menos duas variações do roteiro gerado.
- As variações devem alterar ângulo, ordem ou foco narrativo sem fugir do conteúdo original.
- O usuário deve conseguir comparar as versões antes de escolher uma.

Prioridade: Média. A função amplia flexibilidade editorial, mas não é indispensável para validar o conceito inicial do produto. Ela agrega valor quando a operação já estiver mais madura e houver necessidade de reaproveitar um mesmo conteúdo em campanhas diferentes.

5. Como pessoa gestora de conteúdo, quero que o sistema registre histórico das sugestões geradas e das edições feitas manualmente para que eu acompanhe decisões editoriais e reutilize padrões bem-sucedidos.

Critérios de aceitação:
- O sistema deve salvar a versão original sugerida e a versão final revisada.
- O histórico deve mostrar quem aprovou ou alterou o conteúdo.
- O usuário deve conseguir consultar versões anteriores de um mesmo roteiro.

Prioridade: Média. O histórico ajuda na governança do conteúdo e na aprendizagem do time, mas não é o primeiro requisito a ser entregue. Ele se torna mais útil depois que o fluxo básico de detecção e geração já estiver funcionando.

Minha reflexão: As histórias foram escritas para manter o foco em um fluxo enxuto: detectar, sugerir, revisar e registrar. Eu evitei ampliar demais o escopo para não transformar o projeto em uma plataforma completa de marketing, porque isso enfraqueceria a prototipação dentro do tempo da atividade.

---

## Tarefa 1.4 — Validação de Requisitos

### História escolhida 1

Como pessoa de marketing de conteúdo, quero que o sistema gere um roteiro de carrossel com tom técnico-educativo a partir de um conteúdo detectado para que eu tenha uma primeira versão pronta para revisão.

Verificação de completude e consistência:
- Ambiguidades nos critérios de aceitação: os termos “tom técnico-educativo” e “linguagem adequada” ainda são subjetivos e podem variar conforme a empresa. Também não está definido quantos slides o roteiro deve ter nem o nível de detalhe esperado em cada slide.
- Conflitos potenciais com outras histórias: esta história depende da história de detecção automática e pode conflitar com a história de variações de roteiro se não houver uma definição clara do que é a versão principal e do que é apenas alternativa.
- Informações que precisam ser elucidadas novamente junto ao usuário: é preciso entender se o roteiro deve seguir um padrão fixo de carrossel, se deve haver limite de caracteres por slide e se o sistema pode usar apenas o conteúdo de origem ou também combinar fontes adicionais.

### História escolhida 2

Como pessoa revisora, quero que o sistema destaque trechos técnicos, termos sensíveis e pontos que exigem validação humana para que eu consiga revisar o roteiro com mais rapidez e menos risco.

Verificação de completude e consistência:
- Ambiguidades nos critérios de aceitação: expressões como “termos sensíveis” e “informação inferida” precisam de definição operacional, caso contrário a ferramenta pode marcar coisas diferentes do que o usuário espera.
- Conflitos potenciais com outras histórias: essa história pode entrar em conflito com a geração automática se o sistema sugerir afirmações excessivamente prontas sem sinalizar o grau de confiança. Ela também precisa estar alinhada ao histórico de edições, para não duplicar registros de revisão sem necessidade.
- Informações que precisam ser elucidadas novamente junto ao usuário: é importante perguntar quais tipos de alerta são realmente úteis, quais podem ser ignorados e se o destaque deve ser feito por slide, por frase ou por trecho do texto.

### Revisão crítica

Se o escopo do projeto precisasse ser reduzido pela metade, eu removeria a história de variações de roteiro para o mesmo conteúdo. Essa remoção tem impacto menor sobre o fluxo principal, porque o sistema ainda continuaria entregando detecção, geração, revisão e histórico, que são os elementos mais importantes para validar a proposta. Para o usuário, a perda seria a flexibilidade editorial; para o restante do conjunto, quase nada seria comprometido.

Minha reflexão: A validação mostrou que o risco maior do projeto não está em gerar conteúdo, mas em definir com precisão o que o sistema pode afirmar e o que precisa ser revisado. Isso me ajuda a separar o que é indispensável no protótipo do que pode virar melhoria futura sem prejudicar a proposta principal.
