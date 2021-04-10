import random


def chanse_to_spawn_the_enemy():   # Генерация рандомного числа противников
    choice = random.choice(range(100))

    if choice <= 25:
        return 3
    elif choice <= 50:
        return 2
    else:
        return 1

def random_position_of_spawn(display_width, display_height):   # Генерация рандомного места генерации на карте
    x = random.choice(range(65, display_width - 65))
    y = random.choice(range(65, display_height - 65))

    return (x, y)

def check_for_item(list):
    return random.choice(list)
