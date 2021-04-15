import time
import pygame
import math
import functions

pygame.init()  # Инициализация pygame

############################# Параметры экрана #############################
display_width = 1400
display_height = 700
display = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption("My Walker")
clock = pygame.time.Clock()  # Переменная для подсчёта тиков

############################# Класс объекта-игрока ##############################
class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('resources\\knight\\front.png')
        self.rect = self.image.get_rect()
        self.rect.center = (display_width / 2, display_height / 2)
        self.hp = 5
        self.items = []
        self.scores = 0
        self.lvl = 1
        self.time_to_realise = True
        self.time_spended_to_realise = 0

############################# Класс инвентаря ##############################
class Inventory:
    def __init__(self):
        self.items = []

############################# Класс объекта-бара хп ##############################
class Bar_HP(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('resources\\health\\5.png')
        self.rect = self.image.get_rect()
        self.rect.center = (1215,675)

############################# Класс объекта-бара хп противника ##############################
class Enemy_Bar_HP(pygame.sprite.Sprite):
    def __init__(self, object):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('resources\\enemy health\\3.png')
        self.rect = self.image.get_rect()
        self.follow = object

################################ Класс призрака ##################################
class Ghost(pygame.sprite.Sprite):
    def __init__(self, object=0):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('resources\\enemy\\ghost_left.png')
        self.rect = self.image.get_rect()
        self.speed = 2
        self.hp = 6
        self.bar = object

################################ Класс призрака-босса ##################################
class Ghost_Boss(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('resources\\enemy\\ghost_boss_left_1.png')
        self.rect = self.image.get_rect()

################################ Класс импа ##################################
class Imp(pygame.sprite.Sprite):
    def __init__(self, object=0):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('resources\\enemy\\imp_front_1.png')
        self.rect = self.image.get_rect()
        self.speed = 1
        self.hp = 10
        self.bar = object
        self.shoot_timming = 1
        self.condition = 1
        self.direction = ''

############################# Класс объекта-снаряда Импа ##############################
class Imp_Ball(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('resources/inventory/items/empty_slot.png')
        self.rect = self.image.get_rect()
        self.condition = 1
        self.direction = ''

################################ Класс ячейки инвентаря ##################################
class Ceil_of_inventory(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('resources\\inventory\\ceil_of_inventory.png')
        self.rect = self.image.get_rect()
        self.is_empty = True


################################ Класс места для предмета в ячейке инвентаря ##################################
class Place_for_item_in_ceil(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('resources\\inventory\\items\\empty_slot.png')
        self.rect = self.image.get_rect()

################################ Класс сундука ##################################
class Chest(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('resources\\objects\\chest.png')
        self.rect = self.image.get_rect()
        self.opened = False
        self.dropted = False

############################# Класс гозизонтальной стены ##############################
class Wall_Horizontal(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('resources\\level elements\\wall-horizontal.png')
        self.rect = self.image.get_rect()

############################# Класс вертикальной стены ##############################
class Wall_Vertical(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('resources\\level elements\\wall-vertical.png')
        self.rect = self.image.get_rect()

############################# Класс временной вертикальной стены ##############################
class Temporary_Wall_Vertical(pygame.sprite.Sprite):
    def __init__(self, place):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('resources\\level elements\\temporary_vertical_wall.png')
        self.rect = self.image.get_rect()
        self.place = place

############################# Класс временной горизонтальной стены ##############################
class Temporary_Wall_Horizontal(pygame.sprite.Sprite):
    def __init__(self, place):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('resources\\level elements\\temporary_horizontal_wall.png')
        self.rect = self.image.get_rect()
        self.place = place

############################# Класс хилки ##############################
class Heal_bottle(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('resources/inventory/items/heal_bottle.png')
        self.rect = self.image.get_rect()
        self.name = 'heal_bottle'

############################# Класс чёрного фона ##############################
class Black(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('resources/level elements/black.png')
        self.rect = self.image.get_rect()
        self.image.set_alpha(1)

############################# Класс арбалета ##############################
class Crossbow(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('resources/inventory/items/crossbow.png')
        self.rect = self.image.get_rect()
        self.name = 'crossbow'

############################# Класс лука ##############################
class Bow(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('resources/inventory/items/bow.png')
        self.rect = self.image.get_rect()
        self.name = 'bow'

############################# Класс сообщения ##############################
class Message(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('resources/inventory/items/empty_slot.png')
        self.rect = self.image.get_rect()

############################# Класс снаряда ##############################
class Bullet(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('resources\\attacking\\arrow.png')
        self.rect = self.image.get_rect()
        self.direction = 0
        self.speed = 11

################################ Класс заднего фона ##################################
class Background(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('resources\\level elements\\background-1.png')
        self.rect = self.image.get_rect()
        self.index_of_room = 1

    def change_the_room(self, count_of_room):
        directory = 'resources\\level elements\\background-' + str(count_of_room + 1) + '.png'
        self.image = pygame.image.load(directory)


def run_game():   # Основная функция игры
    game = True
    first = True
    stop = True
    we_are_drawing = False

    ############################# Создаём группы объектов на карте ##############################
    all_sprites = pygame.sprite.Group()  # Группа спрайтов
    walls = pygame.sprite.Group()   # Группа стен
    all_enemy = pygame.sprite.Group()  # Группа монстров
    all_ghosts = pygame.sprite.Group()   # Группа призраков
    all_imps = pygame.sprite.Group()   # Группа импов
    all_imp_fireballs = pygame.sprite.Group()   # Группа снарядов Импа
    all_items_ont_the_ground = pygame.sprite.Group()   # Группа предметов на земле
    all_bullets = pygame.sprite.Group()   # Группа снарядов
    all_enemy_bars = pygame.sprite.Group()   # Группа баров противников
    all_ghost_bars = pygame.sprite.Group()   # Группа баров призраков
    all_imp_bars = pygame.sprite.Group()  # Группа баров импов
    all_temporary_walls = pygame.sprite.Group()   # Группа временных стен
    all_black_elements = pygame.sprite.Group()   # Группа чёрных фонов
    all_chests = pygame.sprite.Group()   # Группа сундуков
    all_messages = pygame.sprite.Group()   # Группа сообщений

    ############################# Задний фон ##############################
    background = Background()
    all_sprites.add(background)
    ############################# Создаём игрока ##############################
    user = Player()
    all_sprites.add(user)

    ############################# Стрельба ##############################
    def bullet_move(arrow, direction):
        if direction == 'right':
            if arrow.rect.right <= display_width - 50:
                arrow.rect.right += 1
        elif direction == 'left':
            if arrow.rect.left >= 50:
                arrow.rect.right += 1
        elif direction == 'top':
            if arrow.rect.top >= 50:
                arrow.rect.right += 1
        elif direction == 'bottom':
            if arrow.rect.bottom <= display_height - 50:
                arrow.rect.right += 1

    def print_the_message(type_of_message):
        sound = pygame.mixer.Sound('resources/sounds/broke.wav')
        sound.play()
        message = Message()
        all_sprites.add(message)
        all_messages.add(message)
        message.rect.center = (525, 500)
        if type_of_message == 'bow_is_broken':
            message.image = pygame.image.load('resources/messages/bow_is_broken.png')
            delete()

    def use_first_item():
        if user.time_to_realise:
            if user.items[0] == 'bow':
                if functions.chanse_to_broke_the_bow() <= 2:
                    user.time_to_realise = False
                    user.time_spended_to_realise = 0
                    print_the_message('bow_is_broken')
                sound = pygame.mixer.Sound('resources/sounds/user_shooting_from_bow.wav')
                sound.play()
                arrow = Bullet()
                all_sprites.add(arrow)
                all_bullets.add(arrow)
                arrow.rect.center = user.rect.center
                if right:
                    arrow.direction = 'right'
                    arrow.image = pygame.image.load('resources\\attacking\\arrow-right.png')
                elif left:
                    arrow.direction = 'left'
                    arrow.image = pygame.image.load('resources\\attacking\\arrow-left.png')
                elif back:
                    arrow.direction = 'top'
                    arrow.image = pygame.image.load('resources\\attacking\\arrow-top.png')
                elif front:
                    arrow.direction = 'bottom'
                    arrow.image = pygame.image.load('resources\\attacking\\arrow-bottom.png')

                bullet_move(arrow, arrow.direction)
            elif user.items[0] == 'crossbow':
                sound = pygame.mixer.Sound('resources/sounds/user_shooting_from_bow.wav')
                sound.play()
                count = -80
                if left or right:
                    for i in range(3):
                        count += 40
                        arrow = Bullet()
                        all_sprites.add(arrow)
                        all_bullets.add(arrow)
                        arrow.rect.center = (user.rect.center[0], user.rect.center[1] + count)
                        if right:
                            arrow.direction = 'right'
                            arrow.image = pygame.image.load('resources\\attacking\\arrow-right.png')
                        elif left:
                            arrow.direction = 'left'
                            arrow.image = pygame.image.load('resources\\attacking\\arrow-left.png')
                        elif back:
                            arrow.direction = 'top'
                            arrow.image = pygame.image.load('resources\\attacking\\arrow-top.png')
                        elif front:
                            arrow.direction = 'bottom'
                            arrow.image = pygame.image.load('resources\\attacking\\arrow-bottom.png')

                        bullet_move(arrow, arrow.direction)
                elif front  or back:
                    for i in range(3):
                        count += 40
                        arrow = Bullet()
                        all_sprites.add(arrow)
                        all_bullets.add(arrow)
                        arrow.rect.center = (user.rect.center[0] + count, user.rect.center[1])
                        if right:
                            arrow.direction = 'right'
                            arrow.image = pygame.image.load('resources\\attacking\\arrow-right.png')
                        elif left:
                            arrow.direction = 'left'
                            arrow.image = pygame.image.load('resources\\attacking\\arrow-left.png')
                        elif back:
                            arrow.direction = 'top'
                            arrow.image = pygame.image.load('resources\\attacking\\arrow-top.png')
                        elif front:
                            arrow.direction = 'bottom'
                            arrow.image = pygame.image.load('resources\\attacking\\arrow-bottom.png')

                        bullet_move(arrow, arrow.direction)
            elif user.items[0] == 'heal_bottle':
                use_heal()
        else:
            pass
    ############################# Противники ##############################
    def generate_ghosts():
        number_of_enemy = functions.chanse_to_spawn_the_enemy(user.lvl)
        for i in range(number_of_enemy):
            ghost = Ghost()
            all_sprites.add(ghost)
            all_ghosts.add(ghost)
            all_enemy.add(ghost)
            ghost.rect.center = functions.random_position_of_spawn(display_width, display_height)

            ghost_bar = Enemy_Bar_HP(ghost)
            ghost.bar = ghost_bar
            all_sprites.add(ghost_bar)
            all_ghost_bars.add(ghost_bar)
            all_enemy_bars.add(ghost_bar)
            ghost_bar.rect.center = ghost_bar.follow.rect.center

    def generate_boss_of_ghost():
        pass


    def generate_imps():
        number_of_enemy = functions.chanse_to_spawn_the_enemy()
        for i in range(number_of_enemy):
            imp = Imp()
            all_sprites.add(imp)
            all_imps.add(imp)
            all_enemy.add(imp)
            imp.rect.center = functions.random_position_of_spawn(display_width, display_height)

            imp_bar = Enemy_Bar_HP(imp)
            imp.bar = imp_bar
            all_sprites.add(imp_bar)
            all_enemy_bars.add(imp_bar)
            all_imp_bars.add(imp_bar)
            imp_bar.rect.center = imp_bar.follow.rect.center

    ############################# ф-я генерации сундуков ##############################
    def generate_chests():
        for i in range(functions.chanse_to_spawn_the_chest()):
            chest = Chest()
            all_sprites.add(chest)
            all_chests.add(chest)
            chest.rect.center = functions.random_position_of_spawn_chest(display_width, display_height)

    ############################# Генерация сундуков ##############################
    generate_chests()
    ############################# Генерация противников ##############################
    generate_ghosts()
    ############################# Создаём стены ##############################
    wall_top_1 = Wall_Horizontal()
    all_sprites.add(wall_top_1)
    walls.add(wall_top_1)
    wall_top_1.rect.left = 0

    wall_top_2 = Wall_Horizontal()
    all_sprites.add(wall_top_2)
    walls.add(wall_top_2)
    wall_top_2.rect.left = 350

    wall_top_3 = Wall_Horizontal()
    all_sprites.add(wall_top_3)
    walls.add(wall_top_3)
    wall_top_3.rect.left = 1050

    wall_top_4 = Wall_Horizontal()
    all_sprites.add(wall_top_4)
    walls.add(wall_top_4)
    wall_top_4.rect.left = 0
    wall_top_4.rect.bottom = display_height

    wall_top_5 = Wall_Horizontal()
    all_sprites.add(wall_top_5)
    walls.add(wall_top_5)
    wall_top_5.rect.left = 750
    wall_top_5.rect.bottom = display_height

    wall_top_6 = Wall_Horizontal()
    all_sprites.add(wall_top_6)
    walls.add(wall_top_6)
    wall_top_6.rect.left = 1050
    wall_top_6.rect.bottom = display_height

    wall_top_7 = Wall_Vertical()
    all_sprites.add(wall_top_7)
    walls.add(wall_top_7)
    wall_top_7.rect.top = -150

    wall_top_8 = Wall_Vertical()
    all_sprites.add(wall_top_8)
    walls.add(wall_top_8)
    wall_top_8.rect.top = 500

    wall_top_9 = Wall_Vertical()
    all_sprites.add(wall_top_9)
    walls.add(wall_top_9)
    wall_top_9.rect.top = -150
    wall_top_9.rect.right = 1400

    wall_top_10 = Wall_Vertical()
    all_sprites.add(wall_top_10)
    walls.add(wall_top_10)
    wall_top_10.rect.right = 1400
    wall_top_10.rect.top = 500

    blocked_right = False
    blocked_left = False
    blocked_top = False
    blocked_bottom = False

    ############################# Бар-хп ##############################
    bar = Bar_HP()   # бар
    all_sprites.add(bar)
    index_of_room = 0
    count_of_room = 1

    ######################### Отрисовка очков ############################
    def draw_scores():
        font = pygame.font.Font(None, 72)
        text_scores = font.render(str(user.scores), True, (192, 192, 192))
        display.blit(text_scores, (display_width-70, 7))

    ############################# Инвентарь ##############################
    def use_heal():
        have_heal = False
        last_not_empty = len(user.items) - 1

        sound = pygame.mixer.Sound('resources/sounds/use_heal.wav')

        for item in user.items:
            if item == 'heal_bottle':
                have_heal = True
        if have_heal:
            sound.play()
            user.hp += 1
            index = user.items.index('heal_bottle')
            user.items.pop(index)

            if index == 0:
                empty_1.image = pygame.image.load('resources\\inventory\\items\\empty_slot.png')
            elif index == 1:
                empty_2.image = pygame.image.load('resources\\inventory\\items\\empty_slot.png')
            elif index == 2:
                empty_3.image = pygame.image.load('resources\\inventory\\items\\empty_slot.png')
            elif index == 3:
                empty_4.image = pygame.image.load('resources\\inventory\\items\\empty_slot.png')
            elif index == 4:
                empty_5.image = pygame.image.load('resources\\inventory\\items\\empty_slot.png')
            print_items()
            if last_not_empty == 0:
                empty_1.image = pygame.image.load('resources\\inventory\\items\\empty_slot.png')
            elif last_not_empty == 1:
                empty_2.image = pygame.image.load('resources\\inventory\\items\\empty_slot.png')
            elif last_not_empty == 2:
                empty_3.image = pygame.image.load('resources\\inventory\\items\\empty_slot.png')
            elif last_not_empty == 3:
                empty_4.image = pygame.image.load('resources\\inventory\\items\\empty_slot.png')
            elif last_not_empty == 4:
                empty_5.image = pygame.image.load('resources\\inventory\\items\\empty_slot.png')
        else:
            pass

    def drop(number, item):
        last_not_empty = len(user.items) - 1
        user.items.pop(number-1)

        if number == 1:
            empty_1.image = pygame.image.load('resources\\inventory\\items\\empty_slot.png')
        elif number == 2:
            empty_2.image = pygame.image.load('resources\\inventory\\items\\empty_slot.png')
        elif number == 3:
            empty_3.image = pygame.image.load('resources\\inventory\\items\\empty_slot.png')
        elif number == 4:
            empty_4.image = pygame.image.load('resources\\inventory\\items\\empty_slot.png')
        elif number == 5:
            empty_5.image = pygame.image.load('resources\\inventory\\items\\empty_slot.png')

        print_items()

        if item == 'heal_bottle':
            dropted = Heal_bottle()
        elif item == 'bow':
            dropted = Bow()
        elif item == 'crossbow':
            dropted = Crossbow()

        all_sprites.add(dropted)
        all_items_ont_the_ground.add(dropted)
        if right:
            dropted.rect.center = (user.rect.center[0] - 100, user.rect.center[1])
        elif left:
            dropted.rect.center = (user.rect.center[0] + 100, user.rect.center[1])
        elif front:
            dropted.rect.center = (user.rect.center[0], user.rect.center[1] - 100)
        elif back:
            dropted.rect.center = (user.rect.center[0], user.rect.center[1] + 100)

        if last_not_empty == 0:
            empty_1.image = pygame.image.load('resources\\inventory\\items\\empty_slot.png')
        elif last_not_empty == 1:
            empty_2.image = pygame.image.load('resources\\inventory\\items\\empty_slot.png')
        elif last_not_empty == 2:
            empty_3.image = pygame.image.load('resources\\inventory\\items\\empty_slot.png')
        elif last_not_empty == 3:
            empty_4.image = pygame.image.load('resources\\inventory\\items\\empty_slot.png')
        elif last_not_empty == 4:
            empty_5.image = pygame.image.load('resources\\inventory\\items\\empty_slot.png')

    def delete():
        last_not_empty = len(user.items) - 1
        user.items.pop(0)

        empty_1.image = pygame.image.load('resources\\inventory\\items\\empty_slot.png')

        print_items()

        if last_not_empty == 0:
            empty_1.image = pygame.image.load('resources\\inventory\\items\\empty_slot.png')
        elif last_not_empty == 1:
            empty_2.image = pygame.image.load('resources\\inventory\\items\\empty_slot.png')
        elif last_not_empty == 2:
            empty_3.image = pygame.image.load('resources\\inventory\\items\\empty_slot.png')
        elif last_not_empty == 3:
            empty_4.image = pygame.image.load('resources\\inventory\\items\\empty_slot.png')
        elif last_not_empty == 4:
            empty_5.image = pygame.image.load('resources\\inventory\\items\\empty_slot.png')

    inventory = Inventory()

    block_1 = Ceil_of_inventory()
    all_sprites.add(block_1)
    block_1.rect.center = (75,25)
    inventory.items.append(block_1)

    empty_1 = Place_for_item_in_ceil()
    all_sprites.add(empty_1)
    empty_1.rect.center = (75,25)


    block_2 = Ceil_of_inventory()
    all_sprites.add(block_2)
    block_2.rect.center = (125,25)
    inventory.items.append(block_2)

    empty_2 = Place_for_item_in_ceil()
    all_sprites.add(empty_2)
    empty_2.rect.center = (125, 25)


    block_3 = Ceil_of_inventory()
    all_sprites.add(block_3)
    block_3.rect.center = (175,25)
    inventory.items.append(block_3)

    empty_3 = Place_for_item_in_ceil()
    all_sprites.add(empty_3)
    empty_3.rect.center = (175, 25)


    block_4 = Ceil_of_inventory()
    all_sprites.add(block_4)
    block_4.rect.center = (225,25)
    inventory.items.append(block_4)

    empty_4 = Place_for_item_in_ceil()
    all_sprites.add(empty_4)
    empty_4.rect.center = (225, 25)


    block_5 = Ceil_of_inventory()
    all_sprites.add(block_5)
    block_5.rect.center = (275,25)
    inventory.items.append(block_5)

    empty_5 = Place_for_item_in_ceil()
    all_sprites.add(empty_5)
    empty_5.rect.center = (275, 25)

    while game:   # Пока сеанс игры запущен:
        if not we_are_drawing:
            for event in pygame.event.get():   # Считываем все события
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        try:
                            use_first_item()
                        except:
                            pass
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        permutation()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_KP1:
                        try:
                            drop(1, user.items[0])
                        except:
                            pass
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_KP2:
                        try:
                            drop(2, user.items[1])
                        except:
                            pass
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_KP3:
                        try:
                            drop(3, user.items[2])
                        except:
                            pass
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_KP4:
                        try:
                            drop(4, user.items[3])
                        except:
                            pass
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_KP5:
                        try:
                            drop(5, user.items[4])
                        except:
                            pass
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_c:
                        try:
                            open_chest()
                        except:
                            pass

            keys = pygame.key.get_pressed()   # Инициализируем клавиатуру
            ############################# Стрельба ##############################


            ############################# Движение игрока ##############################

            ghost_right = True   # Направления, куда смотрит призрак
            ghost_left = False

            imp_right = True   # Направление, куда смотрит имп
            imp_left = False
            imp_top = False
            imp_bottom = False

            if first:
                back = False   # Направления, куда смотрит игрок
                front = True
                right = False
                left = False

                first = False

            if keys[pygame.K_w] and keys[pygame.K_a]:
                if user.rect.x <= 50 and 200 <= user.rect.y <= 205:
                    pass
                elif user.rect.right >= display_width - 50 and 300 <= user.rect.bottom <= 500:
                    pass
                elif 339 <= user.rect.left <= 350 and user.rect.bottom > 650:
                    pass
                elif 700 <= user.rect.x <= 705 and user.rect.top < 50:
                    pass
                elif user.rect.left <= -100 and 200 <= user.rect.y <= 400 and index_of_room == 1:
                    pass
                elif user.rect.top <= -100 and 700 <= user.rect.x <= 975 and index_of_room == 4:
                    pass
                else:
                    user.rect.y -= 2
                    user.rect.x -= 2
            elif keys[pygame.K_w]:
                if user.rect.x <= 50 and 200 <= user.rect.y <= 205:
                    pass
                elif user.rect.right > display_width - 50 and 200 <= user.rect.y <= 205:
                    pass
                elif user.rect.top <= -100 and 700 <= user.rect.x <= 975 and index_of_room == 4:
                    pass
                else:
                    user.rect.y -= 4
                    back = True
                    front = False
                    right = False
                    left = False
            elif keys[pygame.K_a]:
                if 339 <= user.rect.left <= 350 and user.rect.bottom > 650:
                    pass
                elif 700 <= user.rect.x <= 705 and user.rect.top < 50:
                    pass
                elif user.rect.left <= -100 and 200 <= user.rect.y <= 400 and index_of_room == 1:
                    pass
                else:
                    user.rect.x -= 4
                    back = False
                    front = False
                    right = False
                    left = True

            if keys[pygame.K_w] and keys[pygame.K_d]:
                if user.rect.x <= 50 and 200 <= user.rect.y <= 205:
                    pass
                elif user.rect.right >= display_width - 50 and 200 <= user.rect.y <= 205:
                    pass
                elif 669 <= user.rect.x <= 675 and user.rect.bottom > 650:
                    pass
                elif 970 <= user.rect.x <= 975 and user.rect.top < 50:
                    pass
                elif user.rect.right > display_width + 100 and 200 <= user.rect.y <= 400 and index_of_room == 2:
                    pass
                elif user.rect.top <= -100 and 700 <= user.rect.x <= 975 and index_of_room == 4:
                    pass
                else:
                    user.rect.y -= 2
                    user.rect.x += 2
            elif keys[pygame.K_w]:
                if user.rect.x <= 50 and 200 <= user.rect.y <= 205:
                    pass
                elif user.rect.right > display_width - 50 and 200 <= user.rect.y <= 205:
                    pass
                elif user.rect.top <= -100 and 700 <= user.rect.x <= 975 and index_of_room == 4:
                    pass
                else:
                    user.rect.y -= 4
                    back = True
                    front = False
                    right = False
                    left = False
            elif keys[pygame.K_d]:
                if 669 <= user.rect.x <= 675 and user.rect.bottom > 650:
                    pass
                elif 970 <= user.rect.x <= 975 and user.rect.top < 50:
                    pass
                elif user.rect.right > display_width + 100 and 200 <= user.rect.y <= 400 and index_of_room == 2:
                    pass
                else:
                    user.rect.x += 4
                    back = False
                    front = False
                    right = True
                    left = False

            if keys[pygame.K_d] and keys[pygame.K_s]:
                if user.rect.x <= 50 and 495 <= user.rect.bottom <= 500:
                    pass
                elif user.rect.right > display_width - 50 and 500 <= user.rect.bottom <= 505:
                    pass
                elif 669 <= user.rect.x <= 675 and user.rect.bottom > 650:
                    pass
                elif 970 <= user.rect.x <= 975 and user.rect.top < 50:
                    pass
                elif user.rect.right > display_width + 100 and 200 <= user.rect.y <= 400 and index_of_room == 2:
                    pass
                elif user.rect.bottom > display_height + 100 and 345 <= user.rect.x <= 675 and index_of_room == 3:
                    pass
                else:
                    user.rect.x += 2
                    user.rect.y += 2
            elif keys[pygame.K_d]:
                if 669 <= user.rect.x <= 675 and user.rect.bottom > 650:
                    pass
                elif 970 <= user.rect.x <= 975 and user.rect.top < 50:
                    pass
                elif user.rect.right > display_width + 100 and 200 <= user.rect.y <= 400 and index_of_room == 2:
                    pass
                else:
                    user.rect.x += 4
                    back = False
                    front = False
                    right = True
                    left = False
            elif keys[pygame.K_s]:
                if user.rect.x <= 50 and 495 <= user.rect.bottom <= 500:
                    pass
                elif user.rect.right > display_width - 50 and 500 <= user.rect.bottom <= 505:
                    pass
                elif user.rect.bottom > display_height + 100 and 345 <= user.rect.x <= 675 and index_of_room == 3:
                    pass
                else:
                    user.rect.y += 4
                    back = False
                    front = True
                    right = False
                    left = False
            if keys[pygame.K_s] and keys[pygame.K_a]:
                if user.rect.x <= 50 and 495 <= user.rect.bottom <= 500:
                    pass
                elif user.rect.right >= display_width - 50 and 495 <= user.rect.bottom <= 501:
                    pass
                elif 339 <= user.rect.left <= 350 and user.rect.bottom > 650:
                    pass
                elif 700 <= user.rect.x <= 705 and user.rect.top < 50:
                    pass
                elif user.rect.left <= -100 and 200 <= user.rect.y <= 400 and index_of_room == 1:
                    pass
                elif user.rect.bottom > display_height + 100 and 345 <= user.rect.x <= 675 and index_of_room == 3:
                    pass
                else:
                    user.rect.y += 2
                    user.rect.x -= 2
            elif keys[pygame.K_s]:
                if user.rect.x <= 50 and 490 <= user.rect.bottom <= 500:
                    pass
                elif user.rect.right > display_width - 50 and 500 <= user.rect.bottom <= 505:
                    pass
                elif user.rect.bottom > display_height + 100 and 345 <= user.rect.x <= 675 and index_of_room == 3:
                    pass
                else:
                    user.rect.y += 4
                    back = False
                    front = True
                    right = False
                    left = False
            elif keys[pygame.K_a]:
                if 339 <= user.rect.left <= 350 and user.rect.bottom > 650:
                    pass
                elif 700 <= user.rect.x <= 705 and user.rect.top < 50:
                    pass
                elif user.rect.left <= -100 and 200 <= user.rect.y <= 400 and index_of_room == 1:
                    pass
                else:
                    user.rect.x -= 4
                    back = False
                    front = False
                    right = False
                    left = True

            ############################# Границы карты ##############################
            if user.rect.right > display_width - 50:
                if 200 <= user.rect.y <= 400:
                    pass
                else:
                    user.rect.right = display_width - 50
            if user.rect.left < 50:
                if 200 <= user.rect.y <= 400:
                    pass
                else:
                    user.rect.left = 50
            if user.rect.top < 50:
                if 700 <= user.rect.x <= 975:
                    pass
                else:
                    user.rect.top = 50
            if user.rect.bottom > display_height - 50:
                if 345 <= user.rect.x <= 675:
                    pass
                else:
                    user.rect.bottom = display_height - 50

            if blocked_right:
                if user.rect.right > display_width - 50:
                    user.rect.right = display_width - 50
            if blocked_left:
                if user.rect. left < 50:
                    user.rect.left = 50
            if blocked_top:
                if user.rect.top < 50:
                    user.rect.top = 50
            if blocked_bottom:
                if user.rect.bottom > display_height - 50:
                    user.rect.bottom = display_height - 50
            ############################# Смена уровня ##############################
            def pause():
                black = Black()
                all_sprites.add(black)
                all_black_elements.add(black)

            if user.rect.right >= display_width + 150 or user.rect.left <= -150 or user.rect.top <= -150 or user.rect.bottom >= display_height + 150:

                if user.rect.right >= display_width + 150:
                    user.lvl += 1
                    user.rect.left = -100
                    index_of_room = 1

                    blocked_left = False
                    blocked_right = False
                    blocked_top = False
                    blocked_bottom = False

                    temporary_wall = Temporary_Wall_Vertical('left')
                    walls.add(temporary_wall)
                    all_temporary_walls.add(temporary_wall)
                    all_sprites.add(temporary_wall)
                    temporary_wall.rect.bottom = 200

                elif user.rect.left <= -150:
                    user.lvl += 1
                    user.rect.right = display_width + 100
                    index_of_room = 2

                    blocked_left = False
                    blocked_right = False
                    blocked_top = False
                    blocked_bottom = False

                    temporary_wall = Temporary_Wall_Vertical('right')
                    walls.add(temporary_wall)
                    all_temporary_walls.add(temporary_wall)
                    all_sprites.add(temporary_wall)
                    temporary_wall.rect.bottom = 200
                    temporary_wall.rect.x = display_width - 50

                elif user.rect.top <= -150:
                    user.lvl += 1
                    user.rect.bottom = display_height + 100
                    user.rect.x = 500
                    index_of_room = 3

                    blocked_left = False
                    blocked_right = False
                    blocked_top = False
                    blocked_bottom = False

                    temporary_wall = Temporary_Wall_Horizontal('bottom')
                    walls.add(temporary_wall)
                    all_temporary_walls.add(temporary_wall)
                    all_sprites.add(temporary_wall)
                    temporary_wall.rect.right = 350
                    temporary_wall.rect.y = display_height - 50

                elif user.rect.bottom >= display_height + 150:
                    user.lvl += 1
                    user.rect.top = -100
                    user.rect.x = 835
                    index_of_room = 4

                    blocked_left = False
                    blocked_right = False
                    blocked_top = False
                    blocked_bottom = False

                    temporary_wall = Temporary_Wall_Horizontal('top')
                    walls.add(temporary_wall)
                    all_temporary_walls.add(temporary_wall)
                    all_sprites.add(temporary_wall)
                    temporary_wall.rect.right = 700

                count_of_room += 1
                count_of_room %= 4
                background.change_the_room(count_of_room)
                for i in all_temporary_walls:
                    if i in walls:
                        walls.remove(i)
                    i.kill()
                for sprite in all_enemy:
                    sprite.kill()
                for sprite in all_items_ont_the_ground:
                    sprite.kill()
                for sprite in all_bullets:
                    sprite.kill()
                for sprite in all_imp_fireballs:
                    sprite.kill()
                for sprite in all_enemy_bars:
                    sprite.kill()
                for sprite in all_chests:
                    sprite.kill()
                remember = user
                user.kill()

                user = Player()
                user.items = remember.items
                user.hp = remember.hp
                user.rect.center = remember.rect.center
                user.scores = remember.scores
                user.lvl = remember.lvl
                all_sprites.add(user)

                if user.lvl < 10:
                    generate_ghosts()
                    generate_chests()

                pause()


            for bullet in all_bullets:
                ### Направление движения ###
                if bullet.direction == 'right':
                    bullet.rect.right += bullet.speed
                elif bullet.direction == 'left':
                    bullet.rect.left -= bullet.speed
                elif bullet.direction == 'top':
                    bullet.rect.top -= bullet.speed
                elif bullet.direction == 'bottom':
                    bullet.rect.bottom += bullet.speed

                if bullet.rect.y >= display_height + 100:
                    bullet.kill()
                if bullet.rect.y <= -100:
                    bullet.kill()
                if bullet.rect.x <= -100:
                    bullet.kill()
                if bullet.rect.x >= display_width + 100:
                    bullet.kill()

                list = pygame.sprite.spritecollide(bullet, all_enemy, False)
                if list:
                    for i in range(len(list)):
                        list[i].hp -= len(list)
                    bullet.kill()

                for wall in walls:
                    pygame.sprite.spritecollide(wall, all_bullets, True)
            ############################# Движение Призрака ##############################
            for ghost in all_ghosts:
                if math.fabs(user.rect.center[0] - ghost.rect.center[0]) >= 50 or math.fabs(user.rect.center[1] - ghost.rect.center[1]) >= 50:
                    if user.rect.x - ghost.rect.x > 0:
                        ghost.rect.x = ghost.rect.x + ghost.speed
                        ghost_right = True
                        ghost_left = False
                    if user.rect.x - ghost.rect.x < 0:
                        ghost_right = False
                        ghost_left = True
                        ghost.rect.x = ghost.rect.x - ghost.speed

                    if user.rect.y - ghost.rect.y > 0:
                        ghost.rect.y = ghost.rect.y + ghost.speed
                    if user.rect.y - ghost.rect.y < 0:
                        ghost.rect.y = ghost.rect.y - ghost.speed
                else:
                    if pygame.sprite.spritecollide(user, all_ghosts, False):
                        sound = pygame.mixer.Sound('resources/sounds/ghost_dying.wav')
                        sound.play()
                        ghost.bar.kill()
                        ghost.kill()
                        sound = pygame.mixer.Sound('resources/sounds/taking_damage_by_user.wav')
                        sound.play()
                        user.hp -= 1

                for bars in all_ghost_bars:
                    bars.rect.bottom = bars.follow.rect.top
                    bars.rect.x = bars.follow.rect.center[0] - 17
                    if 4 <= bars.follow.hp <= 5:
                        bars.image = pygame.image.load('resources\\enemy health\\2.png')
                    if 1 <= bars.follow.hp <= 3:
                        bars.image = pygame.image.load('resources\\enemy health\\1.png')
                    if bars.follow.hp <= 0:
                        sound = pygame.mixer.Sound('resources/sounds/ghost_dying.wav')
                        sound.play()
                        bars.follow.kill()
                        bars.kill()
                        user.scores+=1

                if ghost.rect.top < 50:
                    if ghost.rect.left >= 700 and ghost.rect.right <= 1050:
                        pass
                    else:
                        ghost.rect.top = 50
                if ghost.rect.bottom > display_height - 50:
                    if ghost.rect.left >= 350 and ghost.rect.right <= 775:
                        pass
                    else:
                        ghost.rect.bottom = display_height - 50
                if ghost.rect.right > display_width - 50:
                    if ghost.rect.top >= 200 and ghost.rect.bottom <= 500:
                        pass
                    else:
                        ghost.rect.right = display_width - 50
                if ghost.rect.left < 50:
                    if ghost.rect.top >= 200 and ghost.rect.bottom <= 500:
                        pass
                    else:
                        ghost.rect.left = 50

                ############################# Отрисовка призрака ##############################
                if ghost_right:
                    ghost.image = pygame.image.load('resources\enemy\ghost_right.png')
                elif ghost_left:
                    ghost.image = pygame.image.load('resources\enemy\ghost_left.png')

            ############################# Движение импа ##############################
            for imp in all_imps:
                if math.fabs(user.rect.center[0] - imp.rect.center[0]) >= 50 or math.fabs(
                        user.rect.center[1] - imp.rect.center[1]) >= 50:
                    if user.rect.center[0] > imp.rect.center[0]:
                        imp.rect.x = imp.rect.x + imp.speed
                        imp_right = True
                        imp_left = False
                        imp_top = False
                        imp_bottom = False
                        imp.direction = 'right'
                    if user.rect.center[0] < imp.rect.center[0]:
                        imp_right = False
                        imp_left = True
                        imp_top = False
                        imp_bottom = False
                        imp.direction = 'left'
                        imp.rect.x = imp.rect.x - imp.speed

                    if user.rect.center[1] > imp.rect.center[1]:
                        imp_right = False
                        imp_left = False
                        imp_top = False
                        imp_bottom = True
                        imp.direction = 'bottom'
                        imp.rect.y = imp.rect.y + imp.speed
                    if user.rect.center[1] < imp.rect.center[1]:
                        imp_right = False
                        imp_left = False
                        imp_top = True
                        imp_bottom = False
                        imp.direction = 'top'
                        imp.rect.y = imp.rect.y - imp.speed
                else:
                    if pygame.sprite.spritecollide(user, all_imps, False):
                        imp.kill()
                        imp.bar.kill()
                        sound = pygame.mixer.Sound('resources/sounds/taking_damage_by_user.wav')
                        sound.play()
                        user.hp -= 2

                for bars in all_imp_bars:
                    bars.rect.bottom = bars.follow.rect.top
                    bars.rect.x = bars.follow.rect.center[0] -10
                    if bars.follow.hp <= 7:
                        bars.image = pygame.image.load('resources\\enemy health\\2.png')
                    if bars.follow.hp <= 4:
                        bars.image = pygame.image.load('resources\\enemy health\\1.png')
                    if bars.follow.hp <= 0:
                        sound = pygame.mixer.Sound('resources/sounds/imp_dying.wav')
                        sound.play()
                        bars.follow.kill()
                        bars.kill()
                        user.scores+=3

                if imp.rect.top < 50:
                    if imp.rect.left >= 700 and imp.rect.right <= 1050:
                        pass
                    else:
                        imp.rect.top = 50
                if imp.rect.bottom > display_height - 50:
                    if imp.rect.left >= 350 and imp.rect.right <= 775:
                        pass
                    else:
                        imp.rect.bottom = display_height - 50
                if imp.rect.right > display_width - 50:
                    if imp.rect.top >= 200 and imp.rect.bottom <= 500:
                        pass
                    else:
                        imp.rect.right = display_width - 50
                if imp.rect.left < 50:
                    if imp.rect.top >= 200 and imp.rect.bottom <= 500:
                        pass
                    else:
                        imp.rect.left = 50
                ############################# Отрисовка импа ##############################
                imp.condition += 1
                if imp.direction == 'right':
                    if imp.condition == 1:
                        imp.image = pygame.image.load('resources/enemy/imp_right_1.png')
                    if imp.condition == 20:
                        imp.image = pygame.image.load('resources/enemy/imp_right_2.png')
                    if imp.condition == 40:
                        imp.image = pygame.image.load('resources/enemy/imp_right_3.png')
                        imp.condition = 1
                if imp.direction == 'left':
                    if imp.condition == 1:
                        imp.image = pygame.image.load('resources/enemy/imp_left_1.png')
                    if imp.condition == 20:
                        imp.image = pygame.image.load('resources/enemy/imp_left_2.png')
                    if imp.condition == 40:
                        imp.image = pygame.image.load('resources/enemy/imp_left_3.png')
                        imp.condition = 1
                if imp.direction == 'top':
                    if imp.condition == 1:
                        imp.image = pygame.image.load('resources/enemy/imp_back_1.png')
                    if imp.condition == 20:
                        imp.image = pygame.image.load('resources/enemy/imp_back_2.png')
                    if imp.condition == 40:
                        imp.image = pygame.image.load('resources/enemy/imp_back_3.png')
                        imp.condition = 1
                if imp.direction == 'bottom':
                    if imp.condition == 1:
                        imp.image = pygame.image.load('resources/enemy/imp_front_1.png')
                    if imp.condition == 20:
                        imp.image = pygame.image.load('resources/enemy/imp_front_2.png')
                    if imp.condition == 40:
                        imp.image = pygame.image.load('resources/enemy/imp_front_3.png')
                        imp.condition = 1

            ############################# Предметы и взаимодействие с ними ##############################
            def pick_up():
                if len(user.items) < 5:
                    list = pygame.sprite.spritecollide(user, all_items_ont_the_ground, True)
                    for i in range(len(list)):
                        if len(user.items) < 5:
                            user.items.append(list[i].name)
                    print_items()

            if pygame.sprite.spritecollide(user, all_items_ont_the_ground, False):
                pick_up()

            ############################# Сундуки и взаимодействие с ними ##############################
            def drop_items_from_chest(chest):
                if user.rect.center[0] >= chest.rect.center[0]:   # Если игрок стоит справа от сундука
                    item = functions.choose_the_drop_10()
                    if item == 'bow':
                        item = Bow()
                        all_sprites.add(item)
                        all_items_ont_the_ground.add(item)
                        item.rect.center = (chest.rect.center[0] - 64, chest.rect.center[1])
                    elif item == 'heal_bottle':
                        item = Heal_bottle()
                        all_sprites.add(item)
                        all_items_ont_the_ground.add(item)
                        item.rect.center = (chest.rect.center[0] - 64, chest.rect.center[1])
                    elif item == 'crossbow':
                        item = Crossbow()
                        all_sprites.add(item)
                        all_items_ont_the_ground.add(item)
                        item.rect.center = (chest.rect.center[0] - 83, chest.rect.center[1])
                elif user.rect.center[0] <= chest.rect.center[0]:   # Если игрок стоит слева от сундука
                    item = functions.choose_the_drop_10()
                    if item == 'bow':
                        item = Bow()
                        all_sprites.add(item)
                        all_items_ont_the_ground.add(item)
                        item.rect.center = (chest.rect.center[0] + 64, chest.rect.center[1])
                    elif item == 'heal_bottle':
                        item = Heal_bottle()
                        all_sprites.add(item)
                        all_items_ont_the_ground.add(item)
                        item.rect.center = (chest.rect.center[0] + 64, chest.rect.center[1])
                    elif item == 'crossbow':
                        item = Crossbow()
                        all_sprites.add(item)
                        all_items_ont_the_ground.add(item)
                        item.rect.center = (chest.rect.center[0] + 83, chest.rect.center[1])

            def open_chest():
                list = pygame.sprite.spritecollide(user, all_chests, False)
                for chest in list:
                    sound = pygame.mixer.Sound('resources/sounds/chest_sound.wav')
                    sound.play()
                    if chest.opened:
                        chest.image = pygame.image.load('resources/objects/chest.png')
                        chest.opened = False
                    else:
                        chest.image = pygame.image.load('resources/objects/chest_opened.png')
                        chest.opened = True
                        if not chest.dropted:
                            drop_items_from_chest(chest)
                        chest.dropted = True




            ############################# Выдвижение стен ##############################
            for block in all_temporary_walls:
                if isinstance(block, Temporary_Wall_Vertical):
                    if block.place == 'left':
                        if user.rect.x > 125:
                            if block.rect.bottom < 500:
                                block.rect.y += 5
                            else:
                                blocked_left = True
                                blocked_right = False
                                blocked_top = False
                                blocked_bottom = False
                    else:
                        if user.rect.x < display_width - 125:
                            if block.rect.bottom < 500:
                                block.rect.y += 5
                            else:
                                blocked_left = False
                                blocked_right = True
                                blocked_top = False
                                blocked_bottom = False
                else:
                    if block.place == 'bottom':
                        if user.rect.y < display_height - 125:
                            if block.rect.right < 750:
                                block.rect.x += 5
                            else:
                                blocked_left = False
                                blocked_right = False
                                blocked_top = False
                                blocked_bottom = True
                    else:
                        if user.rect.y > 125:
                            if block.rect.right < 1050:
                                block.rect.x += 5
                            else:
                                blocked_left = False
                                blocked_right = False
                                blocked_top = True
                                blocked_bottom = False

            ############################# Перестановка предметов из инвентаря ##############################
            def permutation():
                if len(user.items) != 0:
                    remember = user.items[0]
                    for i in range(len(user.items) - 1):
                        user.items[i] = user.items[i+1]
                    user.items[len(user.items) - 1] = remember
                    print_items()
                else:
                    pass
            ############################# Отрисовка предметов из инвентаря ##############################
            def print_items():
                for i in range(5):
                    inventory.items[i].is_empty = True

                for item in user.items:
                    if item == 'heal_bottle':

                        directory = 'resources\\inventory\\items\\heal_bottle.png'

                        if inventory.items[0].is_empty:
                            empty_1.image = pygame.image.load(directory)
                            inventory.items[0].is_empty = False
                        elif inventory.items[1].is_empty:
                            empty_2.image = pygame.image.load(directory)
                            inventory.items[1].is_empty = False
                        elif inventory.items[2].is_empty:
                            empty_3.image = pygame.image.load(directory)
                            inventory.items[2].is_empty = False
                        elif inventory.items[3].is_empty:
                            empty_4.image = pygame.image.load(directory)
                            inventory.items[3].is_empty = False
                        elif inventory.items[4].is_empty:
                            empty_5.image = pygame.image.load(directory)
                            inventory.items[4].is_empty = False

                    elif item == 'bow':
                        directory = 'resources\\inventory\\items\\bow.png'

                        if inventory.items[0].is_empty:
                            empty_1.image = pygame.image.load(directory)
                            inventory.items[0].is_empty = False
                        elif inventory.items[1].is_empty:
                            empty_2.image = pygame.image.load(directory)
                            inventory.items[1].is_empty = False
                        elif inventory.items[2].is_empty:
                            empty_3.image = pygame.image.load(directory)
                            inventory.items[2].is_empty = False
                        elif inventory.items[3].is_empty:
                            empty_4.image = pygame.image.load(directory)
                            inventory.items[3].is_empty = False
                        elif inventory.items[4].is_empty:
                            empty_5.image = pygame.image.load(directory)
                            inventory.items[4].is_empty = False

                    elif item == 'crossbow':
                        directory = 'resources\\inventory\\items\\crossbow.png'

                        if inventory.items[0].is_empty:
                            empty_1.image = pygame.image.load(directory)
                            inventory.items[0].is_empty = False
                        elif inventory.items[1].is_empty:
                            empty_2.image = pygame.image.load(directory)
                            inventory.items[1].is_empty = False
                        elif inventory.items[2].is_empty:
                            empty_3.image = pygame.image.load(directory)
                            inventory.items[2].is_empty = False
                        elif inventory.items[3].is_empty:
                            empty_4.image = pygame.image.load(directory)
                            inventory.items[3].is_empty = False
                        elif inventory.items[4].is_empty:
                            empty_5.image = pygame.image.load(directory)
                            inventory.items[4].is_empty = False
            ############################# Отрисовка анимеции снарядов импа ##############################
            for ball in all_imp_fireballs:
                ball.condition += 1

                if ball.direction == 'left':
                    if ball.condition == 1:
                        ball.image = pygame.image.load('resources/attacking/fireball_1_left.png')
                    if ball.condition == 10:
                        ball.image = pygame.image.load('resources/attacking/fireball_2_left.png')
                    if ball.condition == 20:
                        ball.image = pygame.image.load('resources/attacking/fireball_3_left.png')
                    if ball.condition == 30:
                        ball.image = pygame.image.load('resources/attacking/fireball_4_left.png')
                    if ball.condition == 40:
                        ball.image = pygame.image.load('resources/attacking/fireball_5_left.png')
                        ball.condition = 1
                    ball.rect.x -= 5
                if ball.direction == 'right':
                    if ball.condition == 1:
                        ball.image = pygame.image.load('resources/attacking/fireball_1_right.png')
                    if ball.condition == 10:
                        ball.image = pygame.image.load('resources/attacking/fireball_2_right.png')
                    if ball.condition == 20:
                        ball.image = pygame.image.load('resources/attacking/fireball_3_right.png')
                    if ball.condition == 30:
                        ball.image = pygame.image.load('resources/attacking/fireball_4_right.png')
                    if ball.condition == 40:
                        ball.image = pygame.image.load('resources/attacking/fireball_5_right.png')
                        ball.condition = 1
                    ball.rect.x += 5
                if ball.direction == 'top':
                    if ball.condition == 1:
                        ball.image = pygame.image.load('resources/attacking/fireball_1_top.png')
                    if ball.condition == 10:
                        ball.image = pygame.image.load('resources/attacking/fireball_2_top.png')
                    if ball.condition == 20:
                        ball.image = pygame.image.load('resources/attacking/fireball_3_top.png')
                    if ball.condition == 30:
                        ball.image = pygame.image.load('resources/attacking/fireball_4_top.png')
                    if ball.condition == 40:
                        ball.image = pygame.image.load('resources/attacking/fireball_5_top.png')
                        ball.condition = 1
                    ball.rect.y -= 5
                if ball.direction == 'bottom':
                    if ball.condition == 1:
                        ball.image = pygame.image.load('resources/attacking/fireball_1_bottom.png')
                    if ball.condition == 10:
                        ball.image = pygame.image.load('resources/attacking/fireball_2_bottom.png')
                    if ball.condition == 20:
                        ball.image = pygame.image.load('resources/attacking/fireball_3_bottom.png')
                    if ball.condition == 30:
                        ball.image = pygame.image.load('resources/attacking/fireball_4_bottom.png')
                    if ball.condition == 40:
                        ball.image = pygame.image.load('resources/attacking/fireball_5_bottom.png')
                        ball.condition = 1
                    ball.rect.y += 5

                if ball.rect.y >= display_height + 100:
                    ball.kill()
                if ball.rect.y <= -100:
                    ball.kill()
                if ball.rect.x <= -100:
                    ball.kill()
                if ball.rect.x >= display_width + 100:
                    ball.kill()

                if pygame.sprite.spritecollide(user, all_imp_fireballs, True):
                    sound = pygame.mixer.Sound('resources/sounds/taking_damage_by_user.wav')
                    sound.play()
                    user.hp -= 1

                for wall in walls:
                    pygame.sprite.spritecollide(wall, all_imp_fireballs, True)

            def imp_shoot(imp):
                sound = pygame.mixer.Sound('resources/sounds/imp_shooting.wav')
                sound.play()
                imp_ball = Imp_Ball()
                imp_ball.direction = imp.direction
                all_sprites.add(imp_ball)
                all_imp_fireballs.add(imp_ball)
                imp_ball.rect.center = imp.rect.center


            for imp in all_imps:
                imp.shoot_timming += 1
                if imp.shoot_timming == 100:
                    imp_shoot(imp)
                    imp.shoot_timming = 1

            ############################# Отрисовка игрока ##############################
            if front:
                user.image = pygame.image.load('resources\knight\\front.png')  # Переменная-картинка игрока
            elif back:
                user.image = pygame.image.load('resources\knight\\back.png')  # Переменная-картинка игрока
            elif right:
                user.image = pygame.image.load('resources\knight\\right.png')  # Переменная-картинка игрока
            elif left:
                user.image = pygame.image.load('resources\knight\\left.png')  # Переменная-картинка игрока

            ############################# Отрисовка hp игрока ##############################
            if user.hp == 5:
                bar.image = pygame.image.load('resources\\health\\5.png')
            elif user.hp == 4:
                bar.image = pygame.image.load('resources\\health\\4.png')
            elif user.hp == 3:
                bar.image = pygame.image.load('resources\\health\\3.png')
            elif user.hp == 2:
                bar.image = pygame.image.load('resources\\health\\2.png')
            elif user.hp == 1:
                bar.image = pygame.image.load('resources\\health\\1.png')
            elif user.hp <= 0:
                bar.image = pygame.image.load('resources\\health\\0.png')
                exit()

            elif user.hp > 5:
                user.hp = 5

        ############################# Работа с паузой ##############################
        for block in all_messages:
            if block.image.get_alpha() != 0:
                block.image.set_alpha(block.image.get_alpha() - 1)
            else:
                block.kill()
        ############################# Работа с паузой ##############################

        for i in all_black_elements:
            we_are_drawing = True
            if stop:
                if i.image.get_alpha() != 241:
                    i.image.set_alpha(i.image.get_alpha() + 16)
                else:
                    stop = False
                    i.image.set_alpha(i.image.get_alpha() - 1)
            else:
                if i.image.get_alpha() != 0:
                    i.image.set_alpha(i.image.get_alpha() - 4)
                else:
                    stop = True
                    all_black_elements.remove(i)
                    all_sprites.remove(i)
                    i.kill()
                    we_are_drawing = False

        user.time_spended_to_realise += 1
        if user.time_spended_to_realise == 100:
            user.time_to_realise = True
            user.time_spended_to_realise = 0

        print(user.time_spended_to_realise, user.time_to_realise)

        draw_scores()
        pygame.display.update()
        all_sprites.update()   # Обновление спрайтов
        all_sprites.draw(display)  # Прорисовка всех спрайтов
        pygame.display.flip()   # Переворчиваем экран
        clock.tick(60)   # FPS

run_game()
