from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import json

# arquivo com os dialogos do treinamento do Bot
CONVERSAS_PROGRAMADAS = "conversas.json"


# Configuração inicial do Bot
class ENGSM:
    ISO_639_1 = 'en_core_web_sm'

def configBot():
    # Variavel para treinar o bot
    global trainer

    # ChatBot
    bot = ChatBot("Bot-Generico", 
    tagger_language=ENGSM,
    storage_adapter='chatterbot.storage.SQLStorageAdapter',
    database_uri='sqlite:///bot-generico.sqlite3'
    )
    trainer = ListTrainer(bot)




# Arquivo de dialogos
def extrairTreinamentoArquivo():
    
    with open(CONVERSAS_PROGRAMADAS, 'r',encoding="utf-8") as arquivo:
        mensagens_treinamento = json.load(arquivo)
        arquivo.close()

        return mensagens_treinamento
    

    

# Treinamento do Bot
def treinarBot(conteudo):
    
    for dialogo in conteudo["treinamento"]:
  
        perguntaUsuario = dialogo["usuario"]
        respostaBot = dialogo["bot"]

        for cadaPergunta in perguntaUsuario:
            trainer.train([cadaPergunta, respostaBot])



# Main
if __name__ == "__main__":
    configBot()
    conteudo = extrairTreinamentoArquivo()
    #if treinamento:
    treinarBot(conteudo)