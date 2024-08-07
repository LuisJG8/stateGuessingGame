import turtle
import pandas
from turtle import Turtle

screen = turtle.Screen()
screen.title("U.S. State Games")
image = "blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)
tim = Turtle()

def get_mouse_click_coor(x, y):
    print(x, y)

turtle.onscreenclick(get_mouse_click_coor)

my_file = pandas.read_csv("50_states.csv")
all_states = my_file.state

game_on = True
while game_on:

    answer = screen.textinput(title="Guess the state", prompt="Name a state in the map").title()
    if answer == "Exit":
        game_on = False
    for state in all_states:
        if answer == state:
            print(answer)
            find_state_info = my_file[my_file.state == answer]
            the_index = my_file[my_file.state == answer].index

            state_to_dictionary = find_state_info.to_dict()
            print(state_to_dictionary)
            print("\n")

            new_index = the_index[0]
            print(new_index)

            new_x = state_to_dictionary["x"][new_index]
            new_y = state_to_dictionary["y"][new_index]
            my_tupil = new_x, new_y
            print(my_tupil)

            tim.penup()
            tim.goto(x=new_x, y=new_y)
            tim.color("red")
            tim.write(arg=f"{answer}")


turtle.mainloop()

#Improved version#

# import turtle
# import pandas

# screen = turtle.Screen()
# screen.title("U.S. States Game")
# image = "blank_states_img.gif"
# screen.addshape(image)
# turtle.shape(image)

# data = pandas.read_csv("50_states.csv")
# all_states = data.state.to_list()
# guessed_states = []

# while len(guessed_states) < 50:
#     answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct",
#                                     prompt="What's another state's name?").title()
#     if answer_state == "Exit":
#         missing_states = []
#         for state in all_states:
#             if state not in guessed_states:
#                 missing_states.append(state)
#         new_data = pandas.DataFrame(missing_states)
#         new_data.to_csv("states_to_learn.csv")
#         break
#     if answer_state in all_states:
#         guessed_states.append(answer_state)
#         t = turtle.Turtle()
#         t.hideturtle()
#         t.penup()
#         state_data = data[data.state == answer_state]
#         t.goto(state_data.x.item(), state_data.y.item())
#         t.write(answer_state)
