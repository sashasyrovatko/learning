def turn_right():
    turn_left()
    turn_left()
    turn_left()


while not at_goal():
    if right_is_clear():
        if wall_in_front():
            turn_right()
            move()
        elif front_is_clear():
            move()
    elif front_is_clear():
        move()

    else:
        turn_left()