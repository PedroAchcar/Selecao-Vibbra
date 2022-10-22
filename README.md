# Selecao Vibbra
API para Teste de Backend do portal Vibbra

## Autor
Nome: Pedro Francisco Ignácio Achcar

Email: pedroachcar@gmail.com

## Avaliação do Escopo
O projeto começa fazendo a avaliação do escopo das demandas passadas pelo Sr. Vibbraneo, foi enviado um email pedindo auxílio para identificar os maiores problemas e se estava tudo certo com a demanda passada para mim inicialmente.

## Ambiente e Tecnologias
Para a linguagem foi usada a linguagem de programação Python, utilizada juntamente do framework Django para criação do backend e do Django Rest Framework para facilitar a criação de uma API RESTful. Como banco de dados foi utilado o SQLite que é criado automaticamente pelo Django ao iniciarmos a aplicação. Para teste dos endpoints foi utilizado a plataforma de testes de API Postman.

## Atividades do projeto
As atividades foram divididas em um Trello (que pode ser acessado neste [link](https://trello.com/invite/b/3caMzDNP/ATTId76f10b47b8410c8ddc50b12948a4512E9EF4DFB/selecao-vibbra)) para que pudesse organizar o trabalho. Primeira atividade foi o contato com o cliente por email e a configuração do ambiente Python que foi utilizado. Após isso, já com as informações passadas pelo cliente e com o ambiente propriamente instalado, comecei a fazer a criação dos modelos para o banco de dados, temos três modelos nesta demanda, um para os dados do usuário, um para os projetos e um para ser adicionado o tempo gasto de cada usuário em seu respectivo projeto. Assim que terminado os modelos, foi feito o início da criação dos endpoints MUST HAVE, primeiramente com os endpoints referentes ao User, em seguida os referentes ao Project e, por fim, os referentes ao modelo Time. Próxima atividade foi fazer os endpoints NICE TO HAVE que foram feitos na mesma ordem. Para finalizar, os testes e correções de erros foram feitos para identificar os possíveis erros e resolvê-los.

## Estimativa do tempo em horas
Foi feita uma estimativa inicial de utilizar para a criação completa da API de 70 horas

## Tempo gasto em horas
- **Contato com o cliente**: 20h
- **Preparação do ambiente**: 2h
- **Criação dos modelos User, Project, Time**: 7h30m
- **Criação dos endpoints MUST HAVE**: 12h
- **Criação dos endpoints NICE TO HAVE**: 12h
- **Testes e correções**: 7h
- **Documentação e entrega**: 5h30m
- **Total Gasto**: 62h

## Estimativa do tempo em dias
Foi feita uma estimativa inicial de utilizar os 6 dos 7 dias disponíveis para entrega do projeto e foram utilizados os 6 dias para completar o projeto da API (considerando uma folga no domingo)

## Instalação do ambiente
Após clonar o repositório para a sua máquina e ter o Python instalado, abra o terminal do Windows (outros sistemas operacionais o comando é outro) e digite o seguinte comando para criar um ambiente virtual e o segundo para ativação do ambiente virtual:
```
python -m venv .venv
.\.venv\Scripts\activate
```
Seguinte, para instalar as bibliotecas e framework utilizado, utilizamos o comando a seguir na pasta raiz do projeto onde está o arquivo requirements.txt:
```
pip install -r requirements.txt
```
Com tudo instalado e configurado, para iniciar o servidor de testes da API, utilizamos a seguinte sequência de comandos:
```
python manage.py migrate
python manage.py makemigrations
python manage.p migrate
python manage.py runserver
```
Com isso, já temos nosso servidor funcionando. O Django utiliza por padrão a porta 8000 para testes (```http://127.0.0.1:8000/```). Estamos aptos a consumir a API, porém precisamos de um super usuário para iniciar os testes, esse usuário pode ser iniciado com o comando ```python manage.py createsuperuser``` e seguindo as instruções que irão aparecer na tela.

## Testes na API
Os testes da API foram gravados e postados no Youtube com o seguinte [link](https://youtu.be/HO9xwoKk4zU) para demonstração.
