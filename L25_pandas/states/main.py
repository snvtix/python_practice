import turtle
import pandas as pd
    
data = pd.read_csv("L25_pandas/states/50_states.csv")
states = data["state"].tolist()
guessed_states = []

screen = turtle.Screen()
screen.title("U.S. States Game")

image = "L25_pandas/states/blank_states_img.gif"
turtle.addshape(image)
turtle.shape(image)

while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"State guesser {len(guessed_states)}/50", 
                                    prompt="What's another state name?").title()

    if answer_state == "Exit":
        missing_states = []
        for state in states:
            if state not in guessed_states:
                missing_states.append(state)
        new_data = pd.DataFrame(missing_states)
        new_data.to_csv("L25_pandas/states/states_to_learn.csv")
        break

    if answer_state in states:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(state_data["x"].item(), state_data["y"].item())
        t.write(state_data.state.item())

screen.exitonclick()