def turn_left():
    pass


def turn_right():
    turn_left()
    turn_left()
    turn_left()


def move():
    pass


##################
# def jump():
# turn_left()
# move()
# turn_right()
# move()
# turn_right()
# move()
# turn_left()
##################


def wall_on_right():
    pass


def front_is_clear():
    pass


def jump():
    turn_left()
    while wall_on_right():
        move()
    turn_right()
    move()
    turn_right()

    while front_is_clear():
        move()

    turn_left()

###################################
# # jump()
# # jump()
# # jump()
# # jump()
# # jump()
# # jump()
# for step in range(6):
# jump()

# number_of_hurdles = 6
# while number_of_hurdles > 0:
# jump()
# number_of_hurdles -= 1
# print(number_of_hurdles)
####################################


def at_goal():
    pass


# jump()
def wall_in_front():
    pass


while not at_goal():
    if wall_in_front():
        jump()
    else:
        move()
