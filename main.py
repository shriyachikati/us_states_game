import turtle
import pandas

screen = turtle.Screen()
image = 'blank_states_img.gif'

screen.addshape(image)
turtle.shape(image)

new_turtle = turtle.Turtle()
new_turtle.hideturtle()

correct = 0

# To get the coordinates of the states
# def get_coor_click(x, y):
#     print(x, y)
#
#
# screen.listen()
# screen.onscreenclick(get_coor_click)
# turtle.mainloop()

guessed_states = []

game_is_on = True

while game_is_on:
    data = pandas.read_csv('50_states.csv')

    user_answer = screen.textinput(title=f"Number of states named: {correct}/50", prompt="Name a state (enter 'exit' to end the game)").title().strip()
    # if user_answer == data.state:
    states = data.state

    missed_states = []
    if user_answer.title() == "Exit":
        for state_name in states.values:
            if state_name not in guessed_states:
                missed_states.append(state_name)
        new_data = pandas.DataFrame(missed_states)
        new_data.to_csv('states_to_learn.csv')

        break

    elif user_answer in states.values:
        guessed_states.append(user_answer)
        state_data = data[data.state == user_answer]
        new_turtle.penup()
        new_turtle.goto(int(state_data.x), int(state_data.y))
        new_turtle.write(f"{user_answer}", font=("Courier", 10, "normal"), align="center")

        correct += 1
    else:
        continue

    if correct == 50:
        game_is_on = False


turtle.mainloop()

screen.exitonclick()