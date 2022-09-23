from AI import AI

bot = AI('MAVERICK', '~$')
last_statement = None

while True:
    text = input('>')

    if text == '~$q':
        bot.close_session()
        break

    response = bot.talk(text, last_statement)
    print(response)
    last_statement = response