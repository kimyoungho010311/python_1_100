import turtle
import pandas as pd

FONT = ("Arial", 12, "normal")

screen = turtle.Screen()
screen.title("U.S. States Game")
image = 'blank_states_img.gif'
screen.addshape(image)
turtle.shape(image)
t = turtle.Turtle()
t.penup()


data = pd.read_csv("50_states.csv")
states = data.state
all_states = data.state.to_list()

def write_text(text, x, y):
    t.hideturtle()
    t.goto(x,y)
    t.write(text, align='center', font=FONT )

keep_going = True
score = 0
correct_answer = []
while keep_going:

    answer_state = screen.textinput(title=f'{score}/50 Guess the State', prompt="What's another state's name?").title()
    if answer_state == 'Exit':
        # missing_state = []
        # for state in all_states:
        #     if state not in correct_answer:
        #         missing_state.append(state)
        missing_state = [ state for state in all_states if state not in correct_answer]
        new_data = pd.DataFrame(missing_state)
        new_data.to_csv('states_to_learn.csv')
        break

    if answer_state in states.values:
        x = data.loc[data["state"] == answer_state, 'x'].values[0]
        y = data.loc[data["state"] == answer_state, 'y'].values[0]
        write_text(answer_state,x,y)
        if answer_state not in correct_answer:
            correct_answer.append(answer_state)
            score += 1
        else:
            print("You already answered!!")
        
    else:
        print("Bad...")

# states_to_learn.csv
