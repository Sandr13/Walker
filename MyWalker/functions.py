import random
import pygame

def choose_the_drop_10():
    list = ['bow', 'heal_bottle']
    return random.choice(list)

def choose_the_drop_19():
    list = ['paper_2']
    return random.choice(list)

def choose_the_drop_21():
    list = ['bow', 'crossbow', 'heal_bottle']
    return random.choice(list)

def choose_the_drop_29():
    list = ['paper_3']
    return random.choice(list)


def random_place_to_teleportation_of_boss_ghost(display_width, display_height, user_x, user_y):
    while True:
        x = random.choice(range(100, display_width - 100))
        y = random.choice(range(160, display_height - 160))

        if user_x-100 <= x <= user_x+100 and user_y-158 <= y <= user_y+158:
            pass
        else:
            break
    return (x, y)


def chanse_to_spawn_the_ghosts(lvl):   # Генерация рандомного числа противников
    if lvl <= 10:
        if lvl == 1:
            return 1
        elif 2 <= lvl <= 5:
            return 2
        elif 6 <= lvl <= 7:
            return 3
        elif lvl == 8:
            return 4
        elif lvl == 9:
            return 5
        elif lvl == 10:
            return 0
    elif lvl <= 20:
        if lvl == 11:
            return 1
        elif 12 <= lvl <= 15:
            return 2
        elif 16 <= lvl <= 19:
            return 3
        elif lvl == 20:
            return 0
    elif lvl <= 30:
        if lvl == 21:
            return 1
        elif 22 <= lvl <= 25:
            return 2
        elif 26 <= lvl <= 29:
            return 3
        elif lvl == 30:
            return 0

def chanse_to_spawn_the_imps(lvl):   # Генерация рандомного числа противников
    if lvl <= 20:
        if lvl == 11:
            return 1
        elif 12 <= lvl <= 15:
            return 2
        elif 16 <= lvl <= 19:
            return 3
        elif lvl == 20:
            return 0
    if lvl <= 30:
        if lvl == 21:
            return 1
        elif 22 <= lvl <= 25:
            return 2
        elif 26 <= lvl <= 29:
            return 3
        elif lvl == 30:
            return 0

def chanse_to_spawn_the_zombies(lvl):   # Генерация рандомного числа противников
    if lvl <= 30:
        if lvl == 21:
            return 1
        elif 22 <= lvl <= 25:
            return 2
        elif 26 <= lvl <= 29:
            return 3
        elif lvl == 30:
            return 0

def chanse_to_spawn_the_chest(user):   # Генерация рандомного числа сундуков
    choice = random.choice(range(100))

    if user.lvl == 19:
        if choice <= 10:
            return 3
        elif choice <= 20:
            return 2
        elif choice <= 85:
            return 1
        else:
            return 1
    else:
        if choice <= 10:
            return 3
        elif choice <= 20:
            return 2
        elif choice <= 85:
            return 1
        else:
            return 0

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

def chanse_to_broke_the_bow():
    return random.choice(range(100))

def endgame():
    while True:
        ### Задаём параметры экрана ###
        display_width = 1400
        display_height = 700

        display = pygame.display.set_mode((display_width, display_height))
        pygame.display.set_caption('Game Over')

        background_image = pygame.image.load('resources\\endgame\\background.png')

        clock = pygame.time.Clock()  # Переменная для подсчёта тиков
        while True:
            for event in pygame.event.get():  # Считываем все события
                if event.type == pygame.QUIT:  # Считываем нажатие на крестик
                    pygame.quit()  # Завершаем pygame
                    quit()

            display.blit(background_image, (700, 350))

            keys = pygame.key.get_pressed()  # Инициализируем клавиатуру
            if keys[pygame.K_SPACE]:
                exit()

            pygame.display.update()  # обновляем наш дисплей

        clock.tick(60)  # FPS