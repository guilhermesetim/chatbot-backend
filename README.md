# Backend ChatBot


# Sobre o projeto
Trata-se de um projeto de ChatBot simples, em formato de aplicação *Web*, para testar o treinamento de um ChatBot.

Trata-se de um *backend* de ChatBot, com a biblioteca **ChatterBot** que funciona pelo método de *machine learning*, juntamente com a biblioteca **Spacy**. O projeto desse repositório propõe-se em receber uma mensagem do usuário por *request* do navegador, e retornar por uma API com o formato JSON ao navegador. O *framework* utilizado para desenvolver o servidor *web* foi o **Flask** com Python 3.6.13.

Além do servidor, desenvolvemos um treinamento para o ChaBot, que utiliza o arquivo 'conversas.json' para receber os diálogos de treinamento. O arquivo possui o atributo 'usuario' para receber as possibilidades de pergunta do usuário, e o atributo 'bot' com uma única resposta que o bot retornará conforme o processamento da mensagem recebida do usuario.

Esse repositório destina-se ao *back-end* da aplicação, a interface gráfica pode ser executado juntamente com nesse repositório: https://github.com/guilhermesetim/chatbot-frontend

## Tecnologias utilizadas para o Back-End
- Python 3.6.13;
- Flask;
- API
- SQL Lite;


### Biblioteca externa
- ChatterBot
A biblioteca de *ChatBot* por *Machine Learning*, pode ser encontrada em: https://github.com/gunthercox/ChatterBot/blob/181c69f2a44c2da88f9352d9c693773b09beb1f5/docs/index.rst


### Requisitos
- Anaconda Python;

Com o anaconda python instalado, necessário criar um *virtual environment* com Python na versão 3.6;

```
    conda create --name [nome do *virtual environment*] python=3.6
```

Em seguida, ativar o *virtual environment*:
``` 
    conda activate [nome do *virtual environment*]
```


### Instalação de pacotes via pip *virtual environment*
- Flask;
- Chatterbot;
- Spacy;

```
    pip install flask
    pip install chatterbot
    pip install spacy
```

## Como executar o projeto
Com o *virtual environment* ativo, primeiramente deve-se treinar o Bot e criar o banco de dados com o comando:
```
    python treinarBot.py
```

Para ativar o servidor, que localmente por padrão o Flask utiliza a porta 5000, execute o comando:
``` 
    python server.py
```

### Como adequar ao seu projeto de ChatBot
1. No arquivo conversas.json é destinado aos dialogos de treinamento do bot, o *software* já está preparado para receber o número de perguntas quiser ('usuario'), entretanto com apenas uma resposta ('bot'). Quanto maior a quantidade de perguntas, eleva o treinamento do Bot. Lembrando que o Bot funciona por *Machine Learning*, então ele continua aprendendo com as novas interações, que por sua vez, armazena no banco de dados SQL Lite.

2. API está configurada para receber e enviar por 'localhost:5000/todo/create', entretanto a url pode ser alterada para uma URL de produção. Lembrando que necessita alterar no Front-end

# Autor
Guilherme Setim
