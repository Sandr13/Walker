import time
import pygame
import math
import random
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
        self.lvl = 9
        self.time_to_realise = True
        self.time_spended_to_realise = 0
        self.knockbacked = 0

############################# Класс инвентаря ##############################
class Inventory:
    def __init__(self):
        self.items = []

############################# Класс объекта-бара прочности ##############################
class Bar_DURABILITY(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('resources\\inventory\\items\\empty_slot.png')
        self.rect = self.image.get_rect()
        self.rect.left = 350
        self.rect.top = 5

############################# Класс объекта-бара хп ##############################
class Bar_HP(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('resources\\health\\5.png')
        self.rect = self.image.get_rect()
        self.rect.center = (1215,675)

############################# Класс объекта-бара хп босса ##############################
class Boss_Bar_HP(pygame.sprite.Sprite):
    def __init__(self, object=0):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('resources\\boss_bars\\1.png')
        self.rect = self.image.get_rect()
        self.rect.center = (500,500)
        self.follow = object
        self.condition = 1

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
    def __init__(self, object=0):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('resources\\enemy\\ghost_boss_left_1.png')
        self.rect = self.image.get_rect()
        self.bar = object
        self.hp = 1
        self.condition = 1
        self.direction = 'left'
        self.teleportation = 1
        self.blue_ball_timer = 1
        self.pink_ball_timer = 1
        self.count_of_pink_balls = 0

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

############################# Класс объекта-снаряда Импа ##############################
class Ghost_boss_blue_ball(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('resources/attacking/blue_ball_left_1.png')
        self.rect = self.image.get_rect()
        self.condition = 1
        self.direction = ''

############################# Класс объекта-снаряда Импа ##############################
class Ghost_boss_pink_ball(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('resources/attacking/pink_ball_left_1.png')
        self.rect = self.image.get_rect()
        self.condition = 1
        self.direction =''
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
        self.durability = 30

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
    blocked = True
    bar_printed = False

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
    all_bosses = pygame.sprite.Group()   # Группа боссов
    all_boss_bars = pygame.sprite.Group()   # Группа баров боссов
    all_blue_boss_balls = pygame.sprite.Group()   # Группа синих файерболлов боссов
    all_pink_boss_balls = pygame.sprite.Group()   # Группа розовых файерболлов боссов
    right_top = pygame.sprite.Group()
    right_bottom = pygame.sprite.Group()
    left_top = pygame.sprite.Group()
    left_bottom = pygame.sprite.Group()

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
            if user.items[0].name == 'bow':
                if user.items[0].durability == 0:
                    user.time_to_realise = False
                    user.time_spended_to_realise = 0
                    print_the_message('bow_is_broken')
                sound = pygame.mixer.Sound('resources/sounds/user_shooting_from_bow.wav')
                sound.play()
                user.items[0].durability -= 1
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
            elif user.items[0].name == 'crossbow':
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
            elif user.items[0].name == 'heal_bottle':
                sound = pygame.mixer.Sound('resources/sounds/use_heal.wav')
                sound.play()
                user.hp += 1
                delete()
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
        temporary_wall1 = Temporary_Wall_Vertical('left')
        walls.add(temporary_wall1)
        all_temporary_walls.add(temporary_wall1)
        all_sprites.add(temporary_wall1)
        temporary_wall1.rect.bottom = 200

        temporary_wall2 = Temporary_Wall_Vertical('right')
        walls.add(temporary_wall2)
        all_temporary_walls.add(temporary_wall2)
        all_sprites.add(temporary_wall2)
        temporary_wall2.rect.bottom = 200
        temporary_wall2.rect.x = display_width - 50

        temporary_wall3 = Temporary_Wall_Horizontal('bottom')
        walls.add(temporary_wall3)
        all_temporary_walls.add(temporary_wall3)
        all_sprites.add(temporary_wall3)
        temporary_wall3.rect.right = 350
        temporary_wall3.rect.y = display_height - 50

        temporary_wall4 = Temporary_Wall_Horizontal('top')
        walls.add(temporary_wall4)
        all_temporary_walls.add(temporary_wall4)
        all_sprites.add(temporary_wall4)
        temporary_wall4.rect.right = 700

        boss = Ghost_Boss()
        boss.rect.center = (display_width/2, display_height/2)
        boss.image.set_alpha(1)
        all_enemy.add(boss)
        all_bosses.add(boss)
        all_sprites.add(boss)

        boss_bar = Boss_Bar_HP(boss)
        boss_bar.image.set_alpha(1)
        all_sprites.add(boss_bar)
        all_boss_bars.add(boss_bar)
        boss.bar = boss_bar


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

    ############################# Бар-прочности ##############################
    bar_durability = Bar_DURABILITY()   # бар
    all_sprites.add(bar_durability)

    ######################### Отрисовка очков ############################
    def draw_scores():
        font = pygame.font.Font(None, 72)
        text_scores = font.render(str(user.scores), True, (192, 192, 192))
        display.blit(text_scores, (display_width-70, 7))


    def drop(number, item):
        last_not_empty = len(user.items) - 1

        remember = user.items[number-1]

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
            dropted.durability = remember.durability
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
                            drop(1, user.items[0].name)
                        except:
                            pass
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_KP2:
                        try:
                            drop(2, user.items[1].name)
                        except:
                            pass
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_KP3:
                        try:
                            drop(3, user.items[2].name)
                        except:
                            pass
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_KP4:
                        try:
                            drop(4, user.items[3].name)
                        except:
                            pass
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_KP5:
                        try:
                            drop(5, user.items[4].name)
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



                if user.lvl < 10:
                    generate_ghosts()
                    generate_chests()
                elif user.lvl == 10:
                    ################################# Битва с босом призраков #################################
                    generate_boss_of_ghost()

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
                            user.items.append(list[i])
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
                            elif user.lvl != 10:
                                blocked_left = True
                                blocked_right = False
                                blocked_top = False
                                blocked_bottom = False
                            else:
                                blocked_left = True
                                blocked_right = True
                                blocked_top = True
                                blocked_bottom = True
                    else:
                        if user.rect.x < display_width - 125:
                            if block.rect.bottom < 500:
                                block.rect.y += 5
                            elif user.lvl != 10:
                                blocked_left = False
                                blocked_right = True
                                blocked_top = False
                                blocked_bottom = False
                            else:
                                blocked_left = True
                                blocked_right = True
                                blocked_top = True
                                blocked_bottom = True
                else:
                    if block.place == 'bottom':
                        if user.rect.y < display_height - 125:
                            if block.rect.right < 750:
                                block.rect.x += 5
                            elif user.lvl != 10:
                                blocked_left = False
                                blocked_right = False
                                blocked_top = False
                                blocked_bottom = True
                            else:
                                blocked_left = True
                                blocked_right = True
                                blocked_top = True
                                blocked_bottom = True
                    else:
                        if user.rect.y > 125:
                            if block.rect.right < 1050:
                                block.rect.x += 5
                            elif user.lvl != 10:
                                blocked_left = False
                                blocked_right = False
                                blocked_top = True
                                blocked_bottom = False
                            else:
                                blocked_left = True
                                blocked_right = True
                                blocked_top = True
                                blocked_bottom = True

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
                    if item.name == 'heal_bottle':

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

                    elif item.name == 'bow':
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

                    elif item.name == 'crossbow':
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

        ############################# Работа с баром прочности ##############################
        if len(user.items) != 0:
            item = user.items[0]
            if item.name == 'bow':
                if 28 <= item.durability <= 30:
                    bar_durability.image = pygame.image.load('resources/durability/10.png')
                elif 25 <= item.durability <= 27:
                    bar_durability.image = pygame.image.load('resources/durability/9.png')
                elif 22 <= item.durability <= 24:
                    bar_durability.image = pygame.image.load('resources/durability/8.png')
                elif 19 <= item.durability <= 21:
                    bar_durability.image = pygame.image.load('resources/durability/7.png')
                elif 16 <= item.durability <= 18:
                    bar_durability.image = pygame.image.load('resources/durability/6.png')
                elif 13 <= item.durability <= 15:
                    bar_durability.image = pygame.image.load('resources/durability/5.png')
                elif 10 <= item.durability <= 12:
                    bar_durability.image = pygame.image.load('resources/durability/4.png')
                elif 7 <= item.durability <= 9:
                    bar_durability.image = pygame.image.load('resources/durability/3.png')
                elif 4 <= item.durability <= 6:
                    bar_durability.image = pygame.image.load('resources/durability/2.png')
                elif 1 <= item.durability <= 3:
                    bar_durability.image = pygame.image.load('resources/durability/1.png')
            else:
                bar_durability.image = pygame.image.load('resources/inventory/items/empty_slot.png')
        else:
            bar_durability.image = pygame.image.load('resources/inventory/items/empty_slot.png')

        ############################# Работа с боссом ##############################
        boss_printed = False

        for i in all_boss_bars:
            i.rect.center = (i.follow.rect.center[0], i.follow.rect.top - 20)

        for boss in all_bosses:   # Разворачивание босса в сторону игрока
            if user.rect.center[0] >= boss.rect.center[0]:
                boss.direction = 'right'
            else:
                boss.direction = 'left'
        ####### Проявление босса на карте #######
        for sprite in all_bosses:
            if sprite.image.get_alpha() != 255:
                sprite.image.set_alpha(sprite.image.get_alpha() + 1)
            else:
                boss_printed = True

        for sprite in all_boss_bars:   # Первое заполнение бара хп босса
            if not bar_printed:
                if sprite.follow.hp != 55:
                    if sprite.condition == 4:
                        sprite.follow.hp += 1
                        sprite.condition = 1
                    else:
                        sprite.condition += 1
                else:
                    bar_printed = True

        # Изменение состояния бара босса
        for i in all_boss_bars:
            i.rect.center = (i.follow.rect.center[0], i.follow.rect.top - 20)
            if i.follow.hp == 55:
                i.image = pygame.image.load('resources/boss_bars/55.png')
            if i.follow.hp == 54:
                i.image = pygame.image.load('resources/boss_bars/54.png')
            elif i.follow.hp == 53:
                i.image = pygame.image.load('resources/boss_bars/53.png')
            elif i.follow.hp == 52:
                i.image = pygame.image.load('resources/boss_bars/52.png')
            elif i.follow.hp == 51:
                i.image = pygame.image.load('resources/boss_bars/51.png')
            elif i.follow.hp == 50:
                i.image = pygame.image.load('resources/boss_bars/50.png')
            elif i.follow.hp == 49:
                i.image = pygame.image.load('resources/boss_bars/49.png')
            elif i.follow.hp == 48:
                i.image = pygame.image.load('resources/boss_bars/48.png')
            elif i.follow.hp == 47:
                i.image = pygame.image.load('resources/boss_bars/47.png')
            elif i.follow.hp == 46:
                i.image = pygame.image.load('resources/boss_bars/46.png')
            elif i.follow.hp == 45:
                i.image = pygame.image.load('resources/boss_bars/45.png')
            elif i.follow.hp == 44:
                i.image = pygame.image.load('resources/boss_bars/44.png')
            elif i.follow.hp == 43:
                i.image = pygame.image.load('resources/boss_bars/43.png')
            elif i.follow.hp == 42:
                i.image = pygame.image.load('resources/boss_bars/42.png')
            elif i.follow.hp == 41:
                i.image = pygame.image.load('resources/boss_bars/41.png')
            elif i.follow.hp == 40:
                i.image = pygame.image.load('resources/boss_bars/40.png')
            elif i.follow.hp == 39:
                i.image = pygame.image.load('resources/boss_bars/39.png')
            elif i.follow.hp == 38:
                i.image = pygame.image.load('resources/boss_bars/38.png')
            elif i.follow.hp == 37:
                i.image = pygame.image.load('resources/boss_bars/37.png')
            elif i.follow.hp == 36:
                i.image = pygame.image.load('resources/boss_bars/36.png')
            elif i.follow.hp == 35:
                i.image = pygame.image.load('resources/boss_bars/35.png')
            elif i.follow.hp == 34:
                i.image = pygame.image.load('resources/boss_bars/34.png')
            elif i.follow.hp == 33:
                i.image = pygame.image.load('resources/boss_bars/33.png')
            elif i.follow.hp == 32:
                i.image = pygame.image.load('resources/boss_bars/32.png')
            elif i.follow.hp == 31:
                i.image = pygame.image.load('resources/boss_bars/31.png')
            elif i.follow.hp == 30:
                i.image = pygame.image.load('resources/boss_bars/30.png')
            elif i.follow.hp == 29:
                i.image = pygame.image.load('resources/boss_bars/29.png')
            elif i.follow.hp == 28:
                i.image = pygame.image.load('resources/boss_bars/28.png')
            elif i.follow.hp == 27:
                i.image = pygame.image.load('resources/boss_bars/27.png')
            elif i.follow.hp == 26:
                i.image = pygame.image.load('resources/boss_bars/26.png')
            elif i.follow.hp == 25:
                i.image = pygame.image.load('resources/boss_bars/25.png')
            elif i.follow.hp == 24:
                i.image = pygame.image.load('resources/boss_bars/24.png')
            elif i.follow.hp == 23:
                i.image = pygame.image.load('resources/boss_bars/23.png')
            elif i.follow.hp == 22:
                i.image = pygame.image.load('resources/boss_bars/22.png')
            elif i.follow.hp == 21:
                i.image = pygame.image.load('resources/boss_bars/21.png')
            elif i.follow.hp == 20:
                i.image = pygame.image.load('resources/boss_bars/20.png')
            elif i.follow.hp == 19:
                i.image = pygame.image.load('resources/boss_bars/19.png')
            elif i.follow.hp == 18:
                i.image = pygame.image.load('resources/boss_bars/18.png')
            elif i.follow.hp == 17:
                i.image = pygame.image.load('resources/boss_bars/17.png')
            elif i.follow.hp == 16:
                i.image = pygame.image.load('resources/boss_bars/16.png')
            elif i.follow.hp == 15:
                i.image = pygame.image.load('resources/boss_bars/15.png')
            elif i.follow.hp == 14:
                i.image = pygame.image.load('resources/boss_bars/14.png')
            elif i.follow.hp == 13:
                i.image = pygame.image.load('resources/boss_bars/13.png')
            elif i.follow.hp == 12:
                i.image = pygame.image.load('resources/boss_bars/12.png')
            elif i.follow.hp == 11:
                i.image = pygame.image.load('resources/boss_bars/11.png')
            elif i.follow.hp == 10:
                i.image = pygame.image.load('resources/boss_bars/10.png')
            elif i.follow.hp == 9:
                i.image = pygame.image.load('resources/boss_bars/9.png')
            elif i.follow.hp == 8:
                i.image = pygame.image.load('resources/boss_bars/8.png')
            elif i.follow.hp == 7:
                i.image = pygame.image.load('resources/boss_bars/7.png')
            elif i.follow.hp == 6:
                i.image = pygame.image.load('resources/boss_bars/6.png')
            elif i.follow.hp == 5:
                i.image = pygame.image.load('resources/boss_bars/5.png')
            elif i.follow.hp == 4:
                i.image = pygame.image.load('resources/boss_bars/4.png')
            elif i.follow.hp == 3:
                i.image = pygame.image.load('resources/boss_bars/3.png')
            elif i.follow.hp == 2:
                i.image = pygame.image.load('resources/boss_bars/2.png')
            elif i.follow.hp == 1:
                i.image = pygame.image.load('resources/boss_bars/1.png')
            elif i.follow.hp <= 0:
                i.folow.kill()
                i.kill()

        if boss_printed:   # Анимация плаща босса
            for boss in all_bosses:
                if boss.direction == 'left':
                    if boss.condition == 1:
                        boss.image = pygame.image.load('resources/enemy/ghost_boss_left_1.png')
                    elif boss.condition == 12:
                        boss.image = pygame.image.load('resources/enemy/ghost_boss_left_2.png')
                    elif boss.condition == 24:
                        boss.image = pygame.image.load('resources/enemy/ghost_boss_left_3.png')
                    elif boss.condition == 36:
                        boss.image = pygame.image.load('resources/enemy/ghost_boss_left_4.png')
                    elif boss.condition == 48:
                        boss.image = pygame.image.load('resources/enemy/ghost_boss_left_5.png')
                    elif boss.condition == 60:
                        boss.image = pygame.image.load('resources/enemy/ghost_boss_left_6.png')
                    elif boss.condition == 72:
                        boss.image = pygame.image.load('resources/enemy/ghost_boss_left_7.png')
                    elif boss.condition == 84:
                        boss.image = pygame.image.load('resources/enemy/ghost_boss_left_8.png')
                        boss.condition = 1
                elif boss.direction == 'right':
                    if boss.condition == 1:
                        boss.image = pygame.image.load('resources/enemy/ghost_boss_right_1.png')
                    elif boss.condition == 12:
                        boss.image = pygame.image.load('resources/enemy/ghost_boss_right_2.png')
                    elif boss.condition == 24:
                        boss.image = pygame.image.load('resources/enemy/ghost_boss_right_3.png')
                    elif boss.condition == 36:
                        boss.image = pygame.image.load('resources/enemy/ghost_boss_right_4.png')
                    elif boss.condition == 48:
                        boss.image = pygame.image.load('resources/enemy/ghost_boss_right_5.png')
                    elif boss.condition == 60:
                        boss.image = pygame.image.load('resources/enemy/ghost_boss_right_6.png')
                    elif boss.condition == 72:
                        boss.image = pygame.image.load('resources/enemy/ghost_boss_right_7.png')
                    elif boss.condition == 84:
                        boss.image = pygame.image.load('resources/enemy/ghost_boss_right_8.png')
                        boss.condition = 1
                boss.condition += 1

            for boss in all_bosses:
                if boss.teleportation == 150:   # Телепортация
                    boss.rect.center = functions.random_place_to_teleportation_of_boss_ghost(
                        display_width,
                        display_height,
                        user.rect.center[0],
                        user.rect.center[1]
                    )
                    boss.teleportation = 1
                else:
                    boss.teleportation += 1

                # Стрельба синими файерболлами
                if boss.blue_ball_timer == 200:
                    boss.blue_ball_timer = 1

                    ball1 = Ghost_boss_blue_ball()
                    all_sprites.add(ball1)
                    all_blue_boss_balls.add(ball1)
                    ball1.rect.center = boss.rect.center
                    ball1.direction = 'bottom'

                    ball2 = Ghost_boss_blue_ball()
                    all_sprites.add(ball2)
                    all_blue_boss_balls.add(ball2)
                    ball2.rect.center = boss.rect.center
                    ball2.direction = 'bottom_left'

                    ball3 = Ghost_boss_blue_ball()
                    all_sprites.add(ball3)
                    all_blue_boss_balls.add(ball3)
                    ball3.rect.center = boss.rect.center
                    ball3.direction = 'left'

                    ball4 = Ghost_boss_blue_ball()
                    all_sprites.add(ball4)
                    all_blue_boss_balls.add(ball4)
                    ball4.rect.center = boss.rect.center
                    ball4.direction = 'top_left'

                    ball5 = Ghost_boss_blue_ball()
                    all_sprites.add(ball5)
                    all_blue_boss_balls.add(ball5)
                    ball5.rect.center = boss.rect.center
                    ball5.direction = 'top'

                    ball6 = Ghost_boss_blue_ball()
                    all_sprites.add(ball6)
                    all_blue_boss_balls.add(ball6)
                    ball6.rect.center = boss.rect.center
                    ball6.direction = 'top_right'

                    ball7 = Ghost_boss_blue_ball()
                    all_sprites.add(ball7)
                    all_blue_boss_balls.add(ball7)
                    ball7.rect.center = boss.rect.center
                    ball7.direction = 'right'

                    ball8 = Ghost_boss_blue_ball()
                    all_sprites.add(ball8)
                    all_blue_boss_balls.add(ball8)
                    ball8.rect.center = boss.rect.center
                    ball8.direction = 'bottom_right'

                else:
                    boss.blue_ball_timer += 1

                # Стрельба розовыми файерболлами
                if boss.pink_ball_timer == 500:
                    place = random.choice(['left_top', 'left_bottom', 'right_top', 'right_bottom'])
                    if place == 'left_top':
                        boss.rect.top = 50
                        boss.rect.left = 50
                        left_top.add(boss)
                    elif place == 'left_bottom':
                        boss.rect.bottom = display_height - 50
                        boss.rect.left = 50
                        left_bottom.add(boss)
                    elif place == 'right_top':
                        boss.rect.top = 50
                        boss.rect.right = display_width - 50
                        right_top.add(boss)
                    elif place == 'right_bottom':
                        boss.rect.bottom = display_height - 50
                        boss.rect.right = display_width - 50
                        right_bottom.add(boss)
                    boss.pink_ball_timer = 1
                else:
                    boss.pink_ball_timer += 1



        # Анимация синих файерболлов
        for ball in all_blue_boss_balls:
            ball.condition += 1
            if ball.direction == 'bottom':
                ball.rect.y += 4
                if ball.condition == 8:
                    ball.image = pygame.image.load('resources/attacking/blue_ball_bottom_1.png')
                elif ball.condition == 16:
                    ball.image = pygame.image.load('resources/attacking/blue_ball_bottom_2.png')
                elif ball.condition == 24:
                    ball.image = pygame.image.load('resources/attacking/blue_ball_bottom_3.png')
                elif ball.condition == 32:
                    ball.image = pygame.image.load('resources/attacking/blue_ball_bottom_4.png')
                elif ball.condition == 40:
                    ball.image = pygame.image.load('resources/attacking/blue_ball_bottom_5.png')
                elif ball.condition == 48:
                    ball.image = pygame.image.load('resources/attacking/blue_ball_bottom_6.png')
                elif ball.condition == 56:
                    ball.image = pygame.image.load('resources/attacking/blue_ball_bottom_7.png')
                elif ball.condition == 64:
                    ball.image = pygame.image.load('resources/attacking/blue_ball_bottom_8.png')
                    ball.condition = 1
            elif ball.direction == 'bottom_left':
                ball.rect.y += 2
                ball.rect.x -= 2
                if ball.condition == 8:
                    ball.image = pygame.image.load('resources/attacking/blue_ball_bottom_left_1.png')
                elif ball.condition == 16:
                    ball.image = pygame.image.load('resources/attacking/blue_ball_bottom_left_2.png')
                elif ball.condition == 24:
                    ball.image = pygame.image.load('resources/attacking/blue_ball_bottom_left_3.png')
                elif ball.condition == 32:
                    ball.image = pygame.image.load('resources/attacking/blue_ball_bottom_left_4.png')
                elif ball.condition == 40:
                    ball.image = pygame.image.load('resources/attacking/blue_ball_bottom_left_5.png')
                elif ball.condition == 48:
                    ball.image = pygame.image.load('resources/attacking/blue_ball_bottom_left_6.png')
                elif ball.condition == 56:
                    ball.image = pygame.image.load('resources/attacking/blue_ball_bottom_left_7.png')
                elif ball.condition == 64:
                    ball.image = pygame.image.load('resources/attacking/blue_ball_bottom_left_8.png')
                    ball.condition = 1
            elif ball.direction == 'left':
                ball.rect.x -= 4
                if ball.condition == 8:
                    ball.image = pygame.image.load('resources/attacking/blue_ball_left_1.png')
                elif ball.condition == 16:
                    ball.image = pygame.image.load('resources/attacking/blue_ball_left_2.png')
                elif ball.condition == 24:
                    ball.image = pygame.image.load('resources/attacking/blue_ball_left_3.png')
                elif ball.condition == 32:
                    ball.image = pygame.image.load('resources/attacking/blue_ball_left_4.png')
                elif ball.condition == 40:
                    ball.image = pygame.image.load('resources/attacking/blue_ball_left_5.png')
                elif ball.condition == 48:
                    ball.image = pygame.image.load('resources/attacking/blue_ball_left_6.png')
                elif ball.condition == 56:
                    ball.image = pygame.image.load('resources/attacking/blue_ball_left_7.png')
                elif ball.condition == 64:
                    ball.image = pygame.image.load('resources/attacking/blue_ball_left_8.png')
                    ball.condition = 1
            elif ball.direction == 'top_left':
                ball.rect.x -= 2
                ball.rect.y -= 2
                if ball.condition == 8:
                    ball.image = pygame.image.load('resources/attacking/blue_ball_top_left_1.png')
                elif ball.condition == 16:
                    ball.image = pygame.image.load('resources/attacking/blue_ball_top_left_2.png')
                elif ball.condition == 24:
                    ball.image = pygame.image.load('resources/attacking/blue_ball_top_left_3.png')
                elif ball.condition == 32:
                    ball.image = pygame.image.load('resources/attacking/blue_ball_top_left_4.png')
                elif ball.condition == 40:
                    ball.image = pygame.image.load('resources/attacking/blue_ball_top_left_5.png')
                elif ball.condition == 48:
                    ball.image = pygame.image.load('resources/attacking/blue_ball_top_left_6.png')
                elif ball.condition == 56:
                    ball.image = pygame.image.load('resources/attacking/blue_ball_top_left_7.png')
                elif ball.condition == 64:
                    ball.image = pygame.image.load('resources/attacking/blue_ball_top_left_8.png')
                    ball.condition = 1
            elif ball.direction == 'top':
                ball.rect.y -= 4
                if ball.condition == 8:
                    ball.image = pygame.image.load('resources/attacking/blue_ball_top_1.png')
                elif ball.condition == 16:
                    ball.image = pygame.image.load('resources/attacking/blue_ball_top_2.png')
                elif ball.condition == 24:
                    ball.image = pygame.image.load('resources/attacking/blue_ball_top_3.png')
                elif ball.condition == 32:
                    ball.image = pygame.image.load('resources/attacking/blue_ball_top_4.png')
                elif ball.condition == 40:
                    ball.image = pygame.image.load('resources/attacking/blue_ball_top_5.png')
                elif ball.condition == 48:
                    ball.image = pygame.image.load('resources/attacking/blue_ball_top_6.png')
                elif ball.condition == 56:
                    ball.image = pygame.image.load('resources/attacking/blue_ball_top_7.png')
                elif ball.condition == 64:
                    ball.image = pygame.image.load('resources/attacking/blue_ball_top_8.png')
                    ball.condition = 1
            elif ball.direction == 'top_right':
                ball.rect.x += 2
                ball.rect.y -= 2
                if ball.condition == 8:
                    ball.image = pygame.image.load('resources/attacking/blue_ball_top_right_1.png')
                elif ball.condition == 16:
                    ball.image = pygame.image.load('resources/attacking/blue_ball_top_right_2.png')
                elif ball.condition == 24:
                    ball.image = pygame.image.load('resources/attacking/blue_ball_top_right_3.png')
                elif ball.condition == 32:
                    ball.image = pygame.image.load('resources/attacking/blue_ball_top_right_4.png')
                elif ball.condition == 40:
                    ball.image = pygame.image.load('resources/attacking/blue_ball_top_right_5.png')
                elif ball.condition == 48:
                    ball.image = pygame.image.load('resources/attacking/blue_ball_top_right_6.png')
                elif ball.condition == 56:
                    ball.image = pygame.image.load('resources/attacking/blue_ball_top_right_7.png')
                elif ball.condition == 64:
                    ball.image = pygame.image.load('resources/attacking/blue_ball_top_right_8.png')
                    ball.condition = 1
            elif ball.direction == 'right':
                ball.rect.x += 4
                if ball.condition == 8:
                    ball.image = pygame.image.load('resources/attacking/blue_ball_right_1.png')
                elif ball.condition == 16:
                    ball.image = pygame.image.load('resources/attacking/blue_ball_right_2.png')
                elif ball.condition == 24:
                    ball.image = pygame.image.load('resources/attacking/blue_ball_right_3.png')
                elif ball.condition == 32:
                    ball.image = pygame.image.load('resources/attacking/blue_ball_right_4.png')
                elif ball.condition == 40:
                    ball.image = pygame.image.load('resources/attacking/blue_ball_right_5.png')
                elif ball.condition == 48:
                    ball.image = pygame.image.load('resources/attacking/blue_ball_right_6.png')
                elif ball.condition == 56:
                    ball.image = pygame.image.load('resources/attacking/blue_ball_right_7.png')
                elif ball.condition == 64:
                    ball.image = pygame.image.load('resources/attacking/blue_ball_right_8.png')
                    ball.condition = 1
            elif ball.direction == 'bottom_right':
                ball.rect.x += 2
                ball.rect.y += 2
                if ball.condition == 8:
                    ball.image = pygame.image.load('resources/attacking/blue_ball_bottom_right_1.png')
                elif ball.condition == 16:
                    ball.image = pygame.image.load('resources/attacking/blue_ball_bottom_right_2.png')
                elif ball.condition == 24:
                    ball.image = pygame.image.load('resources/attacking/blue_ball_bottom_right_3.png')
                elif ball.condition == 32:
                    ball.image = pygame.image.load('resources/attacking/blue_ball_bottom_right_4.png')
                elif ball.condition == 40:
                    ball.image = pygame.image.load('resources/attacking/blue_ball_bottom_right_5.png')
                elif ball.condition == 48:
                    ball.image = pygame.image.load('resources/attacking/blue_ball_bottom_right_6.png')
                elif ball.condition == 56:
                    ball.image = pygame.image.load('resources/attacking/blue_ball_bottom_right_7.png')
                elif ball.condition == 64:
                    ball.image = pygame.image.load('resources/attacking/blue_ball_bottom_right_8.png')
                    ball.condition = 1   # Анимация синих

        for wall in walls:
            pygame.sprite.spritecollide(wall, all_blue_boss_balls, True)

        if pygame.sprite.spritecollide(user, all_blue_boss_balls, True):
            sound = pygame.mixer.Sound('resources/sounds/taking_damage_by_user.wav')
            sound.play()
            user.hp -= 1


        for boss in left_top:
            boss.pink_ball_timer = 1
            boss.blue_ball_timer = 1
            boss.teleportation = 1
            if boss.rect.bottom < display_height - 50:
                boss.rect.y += 2
                boss.count_of_pink_balls += 1
                if boss.count_of_pink_balls % 40 == 0:
                    ball = Ghost_boss_pink_ball()
                    all_sprites.add(ball)
                    all_pink_boss_balls.add(ball)
                    ball.rect.center = boss.rect.center
                    ball.direction = 'right'
                else:
                    pass
            else:
                left_top.remove(boss)
                boss.count_of_pink_balls = 0
        for boss in left_bottom:
            boss.pink_ball_timer = 1
            boss.blue_ball_timer = 1
            boss.teleportation = 1
            if boss.rect.top > 50:
                boss.rect.y -= 2
                boss.count_of_pink_balls += 1
                if boss.count_of_pink_balls % 40 == 0:
                    ball = Ghost_boss_pink_ball()
                    all_sprites.add(ball)
                    all_pink_boss_balls.add(ball)
                    ball.rect.center = boss.rect.center
                    ball.direction = 'right'
                else:
                    pass
            else:
                left_bottom.remove(boss)
                boss.count_of_pink_balls = 0
        for boss in right_top:
            boss.pink_ball_timer = 1
            boss.blue_ball_timer = 1
            boss.teleportation = 1
            if boss.rect.bottom < display_height - 50:
                boss.rect.y += 2
                boss.count_of_pink_balls += 1
                if boss.count_of_pink_balls % 40 == 0:
                    ball = Ghost_boss_pink_ball()
                    all_sprites.add(ball)
                    all_pink_boss_balls.add(ball)
                    ball.rect.center = boss.rect.center
                    ball.direction = 'left'
                else:
                    pass
            else:
                right_top.remove(boss)
                boss.count_of_pink_balls = 0
        for boss in right_bottom:
            boss.pink_ball_timer = 1
            boss.blue_ball_timer = 1
            boss.teleportation = 1
            if boss.rect.top > 50:
                boss.rect.y -= 2
                boss.count_of_pink_balls += 1
                if boss.count_of_pink_balls % 40 == 0:
                    ball = Ghost_boss_pink_ball()
                    all_sprites.add(ball)
                    all_pink_boss_balls.add(ball)
                    ball.rect.center = boss.rect.center
                    ball.direction = 'left'
                else:
                    pass
            else:
                right_bottom.remove(boss)
                boss.count_of_pink_balls = 0

        # Анимация розовых файерболлов
        for ball in all_pink_boss_balls:
            if ball.direction == 'left':
                ball.rect.x -= 10
                ball.condition += 1
                if ball.condition == 8:
                    ball.image = pygame.image.load('resources/attacking/pink_ball_left_1.png')
                elif ball.condition == 16:
                    ball.image = pygame.image.load('resources/attacking/pink_ball_left_2.png')
                elif ball.condition == 24:
                    ball.image = pygame.image.load('resources/attacking/pink_ball_left_3.png')
                elif ball.condition == 32:
                    ball.image = pygame.image.load('resources/attacking/pink_ball_left_4.png')
                elif ball.condition == 40:
                    ball.image = pygame.image.load('resources/attacking/pink_ball_left_5.png')
                elif ball.condition == 48:
                    ball.image = pygame.image.load('resources/attacking/pink_ball_left_6.png')
                elif ball.condition == 56:
                    ball.image = pygame.image.load('resources/attacking/pink_ball_left_7.png')
                elif ball.condition == 64:
                    ball.image = pygame.image.load('resources/attacking/pink_ball_left_8.png')
                    ball.condition = 1
            elif ball.direction == 'right':
                ball.rect.x += 10
                ball.condition += 1
                if ball.condition == 8:
                    ball.image = pygame.image.load('resources/attacking/pink_ball_right_1.png')
                elif ball.condition == 16:
                    ball.image = pygame.image.load('resources/attacking/pink_ball_right_2.png')
                elif ball.condition == 24:
                    ball.image = pygame.image.load('resources/attacking/pink_ball_right_3.png')
                elif ball.condition == 32:
                    ball.image = pygame.image.load('resources/attacking/pink_ball_right_4.png')
                elif ball.condition == 40:
                    ball.image = pygame.image.load('resources/attacking/pink_ball_right_5.png')
                elif ball.condition == 48:
                    ball.image = pygame.image.load('resources/attacking/pink_ball_right_6.png')
                elif ball.condition == 56:
                    ball.image = pygame.image.load('resources/attacking/pink_ball_right_7.png')
                elif ball.condition == 64:
                    ball.image = pygame.image.load('resources/attacking/pink_ball_right_8.png')
                    ball.condition = 1

        for wall in walls:
            pygame.sprite.spritecollide(wall, all_pink_boss_balls, True)

        if pygame.sprite.spritecollide(user, all_pink_boss_balls, True):
            sound = pygame.mixer.Sound('resources/sounds/taking_damage_by_user.wav')
            sound.play()
            user.hp -= 1

        if pygame.sprite.spritecollide(user, all_bosses, False):   # Игрок касается босса
            sound = pygame.mixer.Sound('resources/sounds/taking_damage_by_user.wav')
            sound.play()
            for boss in all_bosses:
                user.hp -= 1
                boss.rect.center = functions.random_place_to_teleportation_of_boss_ghost(
                    display_width,
                    display_height,
                    user.rect.center[0],
                    user.rect.center[1]
                )
                boss.teleportation = 1


        ############################# Работа с сообщениями ##############################
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

        draw_scores()
        pygame.display.update()
        all_sprites.update()   # Обновление спрайтов
        all_sprites.draw(display)  # Прорисовка всех спрайтов
        pygame.display.flip()   # Переворчиваем экран
        clock.tick(60)   # FPS

run_game()
