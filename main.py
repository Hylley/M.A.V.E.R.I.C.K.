from AI import AI

bot = AI('MAVERICK', '~$', False)
last_statement = None

while True:
    text = input('>')

    if text == '~$q':
        bot.close_session()
        break

    response = bot.talk(text, last_statement)

    if not response == 110:
        print(response)
        last_statement = response