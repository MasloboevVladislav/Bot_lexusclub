import dp
import telebot
from telebot import types



bot = telebot.TeleBot('7415847840:AAFtWghoUOgREQC9ANwWTvljsJkdl4R57-0')
#бот выводи сообщение при команде старт
@bot.message_handler(commands=['start'])
def main(message):

    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton('Техничка', url='https://t.me/lexusgsl10'))
    markup.add(types.InlineKeyboardButton('Наш Инстаграм', url='https://www.instagram.com/p/Bvf6gusgBS6/?utm_source=ig_share_sheet&igshid=wk1771mssa4n'))
    markup.add(types.InlineKeyboardButton('Барахолка', url='https://t.me/lexusGSL100'))
    markup.add(types.InlineKeyboardButton('Галерея красивых фото GSIV', url='https://t.me/lexusgsfoto'))
    markup.add(types.InlineKeyboardButton('Продажа запчастей', url='https://www.doctorlexus.ru'))
    bot.send_message(message.chat.id, 'Пару правил и рекомендаций для участников и новичков:' 
                                      "\n 1. Представьтесь пожалуйста, Имя, Город и Фото машины " 
                                      "\n 2. Сразу отключаем уведомление на группу, т.к. много спама!" 
                                      "\n 3. Форма общения свободная. 🤷‍♂" 
                                      "️\n 4. Рекомендуем не пересылать откровенное порно и «мясо», здесь этого не любят, никто не удалит, но лучше воздержаться." 
                                      "\n 5. В описании группы, есть ссылка на два чата «Барахолка» и «Техничка», собрана информация по обслуживанию GS4, там есть много интересного! Не  ленитесь☝️" 
                                      "\n 6. Если по каким то причинам, чат не понравился или захотели выйти, как в «реале» рекомендуем попрощаться или сказать до свидание, считаем это правило хорошего тона. Не сделавшие это по умолчанию становятся «ну ОЧЕНЬ не хорошими людьми» 🤝" 
                                      "\n 7. Мат в чате не приветствуется ☝️ за неоднократные нарушения, участник будет удалён." "\n 8. ‼️‼️‼️ просим не поднимать в чате политические или межнациональные вопросы ☝️ у нас большая группа, много национальностей и народов! Поверьте есть каждому, что сказать! Во избежание бардака и ругани, пложалуйста воздержитесь высказывания на данные темы.", reply_markup=markup)
#\n - новая строка



#бот выводит данные группы  (Надо вырезать эту функцию что бы пользователи не могли ею воспользоваться и засрать чат)
@bot.message_handler()
def main(message):
    if message.text.lower() == 'id':
        bot.send_message(message.chat.id, message)

    # \n - новая строка

#бот отправляет сообщение когда кто-то входит в группу

@bot.message_handler(content_types=["new_chat_members"])
def main(message):

    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton('Техничка', url='https://t.me/lexusgsl10'))
    markup.add(types.InlineKeyboardButton('Наш Инстаграм', url='https://www.instagram.com/p/Bvf6gusgBS6/?utm_source=ig_share_sheet&igshid=wk1771mssa4n'))
    markup.add(types.InlineKeyboardButton('Барахолка', url='https://t.me/lexusGSL100'))
    markup.add(types.InlineKeyboardButton('Галерея красивых фото GSIV', url='https://t.me/lexusgsfoto'))
    markup.add(types.InlineKeyboardButton('Продажа запчастей', url='https://www.doctorlexus.ru'))
    bot.send_message(message.chat.id, 'Пару правил и рекомендаций для участников и новичков:' 
                                      "\n 1. Представьтесь пожалуйста, Имя, Город и Фото машины " 
                                      "\n 2. Сразу отключаем уведомление на группу, т.к. много спама!" 
                                      "\n 3. Форма общения свободная. 🤷‍♂" 
                                      "️\n 4. Рекомендуем не пересылать откровенное порно и «мясо», здесь этого не любят, никто не удалит, но лучше воздержаться." 
                                      "\n 5. В описании группы, есть ссылка на два чата «Барахолка» и «Техничка», собрана информация по обслуживанию GS4, там есть много интересного! Не  ленитесь☝️" 
                                      "\n 6. Если по каким то причинам, чат не понравился или захотели выйти, как в «реале» рекомендуем попрощаться или сказать до свидание, считаем это правило хорошего тона. Не сделавшие это по умолчанию становятся «ну ОЧЕНЬ не хорошими людьми» 🤝" 
                                      "\n 7. Мат в чате не приветствуется ☝️ за неоднократные нарушения, участник будет удалён." "\n 8. ‼️‼️‼️ просим не поднимать в чате политические или межнациональные вопросы ☝️ у нас большая группа, много национальностей и народов! Поверьте есть каждому, что сказать! Во избежание бардака и ругани, пложалуйста воздержитесь высказывания на данные темы.", reply_markup=markup)
#\n - новая строка



bot.polling(non_stop=True)
