
answer_state = screen.textinput(title='Guess the State', prompt="What's another state's name?").title()

if answer_state in states.values:
    print('Good!')
else:
    print("Bad...")
