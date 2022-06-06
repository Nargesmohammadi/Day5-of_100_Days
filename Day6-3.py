def turn_left():
    pass


def turn_right():
    turn_left()
    turn_left()
    turn_left()


def at_goal():
    pass


def right_is_clear():
    pass


def move():
    pass


def front_is_clear():
    pass


while front_is_clear():
    move()
turn_left()

while not at_goal():
    if right_is_clear():
        turn_right()
        move()
    elif front_is_clear():
        move()
    else:
        turn_left()
