# Playwright Python Test Project

Este projeto utiliza o [Playwright](https://playwright.dev/) para automação de testes em aplicações web, juntamente com a biblioteca [Faker](https://faker.readthedocs.io/en/master/) para gerar dados fictícios.

## Pré-requisitos

Antes de começar, você precisa ter o Python instalado em sua máquina. Você pode baixá-lo em [python.org](https://www.python.org/downloads/).

### Instalação do Ambiente Virtual

Recomenda-se criar um ambiente virtual para isolar as dependências do projeto. Para fazer isso, execute:

#### Crie o ambiente virtual
python -m venv venv

##### Ative o ambiente virtual
Windows
venv\Scripts\activate

Mac/Linux
source venv/bin/activate

###### Instalação das Dependências
pip install -r requirements.txt

####### Instalação dos Navegadores
playwright install

######## Executando os Testes
python tests/form_test.py
