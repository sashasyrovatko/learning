def my_function():
    print("Hello")
    print("Bye")

def turn_right():
    turn_left()
    turn_left()
    turn_left()
def jump():
    turn_left()
    move()
    while not right_is_clear():
       move()
    turn_right()
    move()
    turn_right()
    move()
    while not wall_in_front():
        move()
    else:
       turn_left()
while not at_goal():
   if wall_in_front():
       jump()
   else:
        move()