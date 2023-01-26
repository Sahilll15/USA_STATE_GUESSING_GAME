import turtle
import pandas

screen=turtle.Screen()
screen.title("U.S. States game")
image="blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)

# def get_mouse_click_color(x,y):
#     print(x,y)
#
# turtle.onscreenclick(get_mouse_click_color)
# turtle.mainloop()

data=pandas.read_csv("50_states.csv")
all_states=data["state"].to_list()
guessed_states=[]

while len(guessed_states)<50:
    answer_state=screen.textinput(title=f"{len(guessed_states)}/50 States Corect",prompt="What's another states name?").title()

    if answer_state=="Exit":
        # missing_state=[]
        # for state in all_states:
        #     if state not in guessed_states:
        #         missing_state.append(state)

        missing_state = [state for state in all_states if state not in guessed_states]
        new_data=pandas.DataFrame(missing_state)
        new_data.to_csv("states_learn")
        break
    #check if the state is proper
    if answer_state in all_states:
        guessed_states.append(answer_state)
        t=turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data=data[data.state ==answer_state]
        t.goto(int(state_data.x),int(state_data.y))
        t.write(answer_state)


#states to lears.csv


