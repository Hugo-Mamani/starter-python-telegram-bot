import telebot
from flask import Flask, request

# Clave de API de Telegram
key = "6489296743:AAHNHhQirARtbb7HIHE6WQAeF_Prp5gsUtk"

# Crear una instancia de tu bot
bot = telebot.TeleBot(key)

# Crear una aplicación Flask para gestionar la webhook
app = Flask(__name__)

# Ruta de la webhook
@app.route('/webhook', methods=['POST'])
def webhook():
    string = request.stream.read().decode("UTF-8")
    update = telebot.types.Update.de_json(request.stream.read().decode("UTF-8"))
    bot.process_new_updates([update])
    return "ok", 200

# Manejar comandos o mensajes de texto
@bot.message_handler(commands=["start", "codes", "love"])
def cmd(message):
    bot.reply_to(message, "Hey, commands available")

@bot.message_handler(content_types=["text"])
def text(message):
    if message.text.startswith("/"):
        bot.send_message(message.chat.id, "Sorry, this command does not exist")
    else:
        bot.send_message(message.chat.id, "Hey, more details")

if __name__ == "__main__":
    # Iniciar la aplicación Flask en modo debug
    app.run(debug=True)
