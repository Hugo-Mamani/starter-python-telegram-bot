import telebot, multiprocessing

key = "6489296743:AAHNHhQirARtbb7HIHE6WQAeF_Prp5gsUtk"

bot = telebot.TeleBot(key)
bot.remove_webhook()  # Asegúrate de eliminar la webhook

def subprocess(chat, name, url):
    import requests
    source = url
    saved = name
    legth_frag = 1024 * 1024  # 1MB
    response = requests.get(source, stream=True)
    if response.status_code == 200:
        with open(saved, 'wb') as file:
            for frag in response.iter_content(chunk_size=legth_frag):
                if frag:
                    file.write(frag)
            file.close()
        bot.send_message(chat.id, f"saved {saved}")
    else:
        print(f'Error download: {response.status_code}')

@bot.message_handler(commands=["start", "download", "alive"])
def cmd(message):
    if message.text[:9] == "/download":
        mss = message.text.split()
        if len(mss) > 1:
            args = mss[1:]
            parser = dict(map((lambda e: e.split('=')), args))
            if not '' in parser.values() and len(parser.values()) == 2:
                global process
                process = multiprocessing.Process(target=subprocess,args=(message.chat,parser['file'],parser['source']))
                process.start()
                bot.send_message(message.chat.id, "downloading")
        else:
            bot.send_message(message.chat.id, "required arguments for download")
    elif message.text == '/alive':
        if process.is_alive():
            bot.send_message(message.chat.id, "process downloading")
        else:
            bot.send_message(message.chat.id, "finish")
    #bot.reply_to(message, "hey, commands available")

@bot.message_handler(content_types=["text"])
def text(message):
    if message.text.startswith("/"):
        bot.send_message(message.chat.id, "sorry, this command does not exist")

    else:
        bot.send_message(message.chat.id, "hey, more details")

if __name__ == "__main__":
    print('start bot')
    bot.polling(none_stop=True)
