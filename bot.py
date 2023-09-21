import telebot

key = "6489296743:AAHNHhQirARtbb7HIHE6WQAeF_Prp5gsUtk"

bot = telebot.TeleBot(key)

@bot.message_handler(commands=["start","codes","love"])
def cmd(message):
    bot.reply_to(message, "hey, commands available")

@bot.message_handler(content_types=["text"])
def text(message):
    if message.text.startswith("/"):
        bot.send_message(message.chat.id ,"sorry not exist this command")
    else:
        bot.send_message(message.chat.id, "hey, but details")

if __name__ == "__main__":
    print('start bot')
    bot.infinity_polling()
