import telebot

key = "6489296743:AAHNHhQirARtbb7HIHE6WQAeF_Prp5gsUtk"

bot = telebot.TeleBot(key)
bot.remove_webhook()  # No es necesario, ya que no estamos configurando una webhook

@bot.message_handler(commands=["start", "codes", "love"])
def cmd(message):
    bot.reply_to(message, "hey, commands available")

@bot.message_handler(content_types=["text"])
def text(message):
    if message.text.startswith("/"):
        bot.send_message(message.chat.id, "sorry, this command does not exist")
    else:
        bot.send_message(message.chat.id, "hey, more details")

if __name__ == "__main__":
    print('start bot')
    try:
        bot.polling(none_stop=True)
    except Exception as e:
        print(f"Error: {str(e)}")
