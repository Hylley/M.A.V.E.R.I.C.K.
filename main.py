from AI import AI

bot = AI('MAVERICK', '~$')

while True:
    text = input('>')

    if text == '~$q':
        bot.close_session()
        break

    print(bot.talk(text))