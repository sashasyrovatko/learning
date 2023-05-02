import turtle
import pandas

screen = turtle.Screen()
screen.title("pythonProject/Day 25")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)


# def get_mouse_click_coor(x, y):
#     print(x, y)


data = pandas.read_csv("50_states.csv")
states_list = data.state.to_list
# x_cor = data["x"].to_list
# y_cor = data["y"].to_list
print(states_list)
game_is_on = True
correct_answer = []

while len(correct_answer) < 50:
    answer_state = screen.textinput(title=f"len{correct_answer}/50 State Correct",
                                    prompt="What's another state's name?").title()
    if answer_state == "Exit":
        missing_states = []
        for state in states_list():
            if state not in correct_answer:
                missing_states.append(state)
        print(missing_states)
        sl = pandas.DataFrame(missing_states)
        sl.to_csv("states_to_learn.csv")
        break
    if answer_state in states_list():
        correct_answer.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer_state)




# for state in states_list():
#     if state == answer_state:
#         print(True)
#     else:
#         print(False)
# turtle.onscreenclick(get_mouse_click_coor)
turtle.mainloop()






