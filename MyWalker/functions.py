import random


def chanse_to_spawn_the_enemy():
    choice = random.choice(range(100))

    if choice <= 25:
        return 3
    elif choice <= 50:
        return 2
    else:
        return 1

def random_position_of_spawn(display_width, display_height):
    x = random.choice(range(display_width))
    y = random.choice(range(display_height))

    return (x, y)