def turn_left():
    pass


def turn_right():
    turn_left()
    turn_left()
    turn_left()


def move():
    pass


def jump():
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()


# jump()
# jump()
# jump()
# jump()
# jump()
# jump()
for step in range(6):
    jump()
