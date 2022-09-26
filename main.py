from AI import AI

MAVERICK = AI('MAVERICK', '~$')
last_statement = None

while True:
    text = input('>')

    if text == '~$q':
        MAVERICK.close_session()
        break

    response = MAVERICK.talk(text, last_statement)

    if not response == 110:
        print(response)
        last_statement = response