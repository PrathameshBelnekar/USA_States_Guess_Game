import turtle
import pandas as pd

data = pd.read_csv("50_states.csv")
states = data["state"].to_list()



screen = turtle.Screen()
screen.title("U.S States")
image = "blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)
guessed_states = []
while len(guessed_states) < 50:
    ans_state = screen.textinput(title=f"{len(guessed_states)}/50 states remaining", prompt="whats another states name").title()
    if ans_state == "Exit":
        states_to_learn = []
        for x in states:
            if x not in guessed_states:
                states_to_learn.append(x)
        new_data = pd.DataFrame(states_to_learn, columns=["state"])
        new_data.to_csv('states_to_learn.csv')
        break
    if ans_state in states:
        guessed_states.append(ans_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data["state"] == ans_state]
        t.goto(int(state_data["x"]),int(state_data["y"]))
        t.write(ans_state)
#test


