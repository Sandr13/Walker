import random

def choose_the_drop():
    list = ['bow', 'heal_bottle']
    return random.choice(list)

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

def random_position_of_spawn_chest(display_width, display_height):   # Генерация рандомного места для сундука генерации на карте
    x = random.choice(range(165, display_width - 165))
    y = random.choice(range(165, display_height - 165))

    return (x, y)

def check_for_item(list):
    return random.choice(list)
