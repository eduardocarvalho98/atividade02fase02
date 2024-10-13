# FIAP - Faculdade de Informática e Administração Paulista

## Nome do projeto
Sistema de Gerenciamento de Produtores Orgânicos

## Nome do grupo
Grupo Verde

👨‍🎓 Integrantes:
- Eduardo Carvalho
- Integrante 2
- Integrante 3
- Integrante 4
- Integrante 5

👩‍🏫 Professores:
**Tutor(a)**  
Nome do Tutor  
**Coordenador(a)**  
Nome do Coordenador  

📜 Descrição  
O projeto consiste no desenvolvimento de um sistema de gerenciamento para produtores orgânicos no Brasil. O objetivo principal é criar uma estrutura de banco de dados que permita o cadastro de produtores, produtos e comércios, facilitando a interação entre eles. O sistema possibilitará que produtores se associem a comércios e possam listar suas ofertas de produtos. A estrutura inclui tabelas associativas que ligam produtores a produtos e produtos a comércios, permitindo uma gestão eficiente das informações. 

Durante o desenvolvimento, foram implementadas funções para cadastrar produtores e comércios, além de associar produtos a ambos. As informações podem ser persistidas em formato JSON para facilitar o acesso e visualização dos dados. O sistema é desenvolvido em Python e utiliza um banco de dados Oracle para armazenamento das informações.

A solução atende à necessidade de promover a transparência e a acessibilidade aos produtos orgânicos, estimulando a comercialização direta entre produtores e consumidores.

📁 Estrutura de pastas  
Dentre os arquivos e pastas presentes na raiz do projeto, definem-se:

- **.github**: Nesta pasta ficarão os arquivos de configuração específicos do GitHub que ajudam a gerenciar e automatizar processos no repositório.
  
- **assets**: Aqui estão os arquivos relacionados a elementos não-estruturados deste repositório, como imagens.
  
- **config**: Posicione aqui arquivos de configuração que são usados para definir parâmetros e ajustes do projeto.
  
- **document**: Aqui estão todos os documentos do projeto que as atividades poderão pedir. Na subpasta "other", adicione documentos complementares e menos importantes.
  
- **scripts**: Posicione aqui scripts auxiliares para tarefas específicas do seu projeto, como deploy, migrações de banco de dados e backups.
  
- **src**: Todo o código fonte criado para o desenvolvimento do projeto ao longo das 7 fases.
  
- **README.md**: arquivo que serve como guia e explicação geral sobre o projeto (o mesmo que você está lendo agora).

🔧 Como executar o código  
Para executar o código, você precisará ter os seguintes pré-requisitos instalados em sua máquina:
- Python 3.x
- Biblioteca `oracledb` (para interação com o banco de dados Oracle)
  
### Passo a passo para execução:
1. Clone o repositório:
   ```bash
   git clone <URL do repositório>
   cd <pasta do repositório>
