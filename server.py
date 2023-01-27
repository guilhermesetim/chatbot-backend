from flask import Flask, jsonify, request
import json
from flask_cors import CORS #
from chatterbot import ChatBot

global bot

app = Flask(__name__)

# configuração do bot
class ENGSM:
    ISO_639_1 = 'en_core_web_sm'

bot = ChatBot(
    'Bot-Generico', #nome do ChatBot
    tagger_language=ENGSM, # compatibilidade da biblioteca
    storage_adapter='chatterbot.storage.SQLStorageAdapter', #treinamento armazenado em um SQL Lite
    database_uri='sqlite:///bot-generico.sqlite3' # banco de dados SQL Lite
)





# recebimento método POST
@app.route('/todo/create', methods=['POST'])
def createTask():
    
    mensagemUsuario = request.form.get('usuario')

    mensagemBot = bot.get_response(mensagemUsuario)

    respostaBot = { 'texto': str(mensagemBot) }

    return jsonify(respostaBot)





# Main
if __name__ == "__main__":
    CORS(app)
    app.run(debug=True)
    