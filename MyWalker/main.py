import time
import math
import random

import Imp_boss
import Zomb_boss
import Ghost_boss

import Objects
import VisualEffects
import functions

import pygame
import pygame_menu
from pygame_menu import Theme

pygame.init()  # Инициализация pygame
pygame.font.init()

############################# Параметры экрана #############################
surface = pygame.display.set_mode((1400, 700))
display_width = 1400
display_height = 700
display = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption("Dungeon slider")
clock = pygame.time.Clock()

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
    all_zombs = pygame.sprite.Group()   # Группа зомби
    all_imp_fireballs = pygame.sprite.Group()   # Группа снарядов Импа
    all_items_ont_the_ground = pygame.sprite.Group()   # Группа предметов на земле
    all_bullets = pygame.sprite.Group()   # Группа снарядов
    all_enemy_bars = pygame.sprite.Group()   # Группа баров противников
    all_ghost_bars = pygame.sprite.Group()   # Группа баров призраков
    all_imp_bars = pygame.sprite.Group()  # Группа баров импов
    all_zomb_bars = pygame.sprite.Group()   # Группа баров зомби
    all_closing_walls = pygame.sprite.Group()   # Группа временных стен
    all_opening_walls = pygame.sprite.Group()   # Группа временных стен
    all_black_elements = pygame.sprite.Group()   # Группа чёрных фонов
    all_chests = pygame.sprite.Group()   # Группа сундуков
    all_messages = pygame.sprite.Group()   # Группа сообщений
    all_ghost_bosses = pygame.sprite.Group()   # Группа боссов
    all_ghost_boss_bars = pygame.sprite.Group()   # Группа баров боссов
    all_imp_bosses = pygame.sprite.Group()   # Группа боссов
    all_imp_boss_bars = pygame.sprite.Group()   # Группа баров боссов
    all_zomb_bosses = pygame.sprite.Group()  # Группа боссов
    all_zomb_boss_bars = pygame.sprite.Group()  # Группа баров боссов
    all_blue_boss_balls = pygame.sprite.Group()   # Группа синих файерболлов боссов
    all_pink_boss_balls = pygame.sprite.Group()   # Группа розовых файерболлов боссов
    right_top = pygame.sprite.Group()   ####### Стрельба розовыми файерболлами
    right_bottom = pygame.sprite.Group()
    left_top = pygame.sprite.Group()
    left_bottom = pygame.sprite.Group()   ####### Стрельба розовыми файерболлами
    creating_portals = pygame.sprite.Group()   # Создание порталов призраков
    all_portals = pygame.sprite.Group()   # Группа порталов босса-призрака
    all_sword_places = pygame.sprite.Group()   # Группа барьеров меча
    all_smashes = pygame.sprite.Group()   # Группа следов меча
    all_disappeared = pygame.sprite.Group()   # Группа исчезновения призраков
    all_blue_user_balls = pygame.sprite.Group()  # Группа розовых файерболлов игрока
    all_abilities_1 = pygame.sprite.Group()  # Группа абилки 1
    all_abilities_2 = pygame.sprite.Group()  # Группа абилки 2
    imp_boss_run_left = pygame.sprite.Group()   ####### Бег босса импов
    imp_boss_run_right = pygame.sprite.Group()
    imp_boss_run_top = pygame.sprite.Group()
    imp_boss_run_bottom = pygame.sprite.Group()   ####### Бег босса импов
    all_imp_boss_fireballs = pygame.sprite.Group()
    all_pentagramms = pygame.sprite.Group()
    imp_boss_attack_cooldown = pygame.sprite.Group()
    all_imps_portals = pygame.sprite.Group()
    creating_imp_portals = pygame.sprite.Group()
    deleting_imp_portals = pygame.sprite.Group()
    all_zombs_portals = pygame.sprite.Group()
    creating_imp_portals = pygame.sprite.Group()
    deleting_imp_portals = pygame.sprite.Group()
    all_slime_fireballs = pygame.sprite.Group()
    all_puddles = pygame.sprite.Group()
    creating_zomb_portals = pygame.sprite.Group()
    deleting_zomb_portals = pygame.sprite.Group()
    all_zomb_portals = pygame.sprite.Group()
    all_win_bars = pygame.sprite.Group()

    ############################# Задний фон ##############################
    background = Objects.Background()
    all_sprites.add(background)
    ############################# Создаём игрока ##############################
    user = Objects.Player()
    all_sprites.add(user)

    base_sword = Objects.Sword()
    user.items.append(base_sword)

    left_place_for_sword = Objects.Right_left_sword_barrier()
    left_place_for_sword.rect.center = user.rect.center
    left_place_for_sword.rect.right = user.rect.left
    left_place_for_sword.name = 'left'

    right_place_for_sword = Objects.Right_left_sword_barrier()
    right_place_for_sword.rect.center = user.rect.center
    right_place_for_sword.rect.left = user.rect.right
    right_place_for_sword.name = 'right'

    top_place_for_sword = Objects.Top_bottom_sword_barrier()
    top_place_for_sword.rect.center = user.rect.center
    top_place_for_sword.rect.bottom = user.rect.top
    top_place_for_sword.name = 'top'

    bottom_place_for_sword = Objects.Top_bottom_sword_barrier()
    bottom_place_for_sword.rect.center = user.rect.center
    bottom_place_for_sword.rect.top = user.rect.bottom
    bottom_place_for_sword.name = 'bottom'

    all_sprites.add(left_place_for_sword)
    all_sprites.add(right_place_for_sword)
    all_sprites.add(top_place_for_sword)
    all_sprites.add(bottom_place_for_sword)

    all_sword_places.add(left_place_for_sword)
    all_sword_places.add(right_place_for_sword)
    all_sword_places.add(top_place_for_sword)
    all_sword_places.add(bottom_place_for_sword)

    def open_walls(index_of_room):
        if index_of_room == 1:
            for i in all_closing_walls:
                if i.place != 'left':
                    all_closing_walls.remove(i)
                    all_opening_walls.add(i)
        elif index_of_room == 2:
            for i in all_closing_walls:
                if i.place != 'right':
                    all_closing_walls.remove(i)
                    all_opening_walls.add(i)
        elif index_of_room == 3:
            for i in all_closing_walls:
                if i.place != 'bottom':
                    all_closing_walls.remove(i)
                    all_opening_walls.add(i)
        elif index_of_room == 4:
            for i in all_closing_walls:
                if i.place != 'top':
                    all_closing_walls.remove(i)
                    all_opening_walls.add(i)
        else:
            for i in all_closing_walls:
                all_closing_walls.remove(i)
                all_opening_walls.add(i)


    def close_dors():
        sound = pygame.mixer.Sound('resources/sounds/mooving_wall_low.wav')
        sound.play()

        temporary_wall1 = Objects.Temporary_Wall_Vertical('left')
        walls.add(temporary_wall1)
        all_closing_walls.add(temporary_wall1)
        all_sprites.add(temporary_wall1)
        temporary_wall1.rect.bottom = 200

        temporary_wall2 = Objects.Temporary_Wall_Vertical('right')
        walls.add(temporary_wall2)
        all_closing_walls.add(temporary_wall2)
        all_sprites.add(temporary_wall2)
        temporary_wall2.rect.bottom = 200
        temporary_wall2.rect.x = display_width - 50

        temporary_wall3 = Objects.Temporary_Wall_Horizontal('bottom')
        walls.add(temporary_wall3)
        all_closing_walls.add(temporary_wall3)
        all_sprites.add(temporary_wall3)
        temporary_wall3.rect.right = 350
        temporary_wall3.rect.y = display_height - 50

        temporary_wall4 = Objects.Temporary_Wall_Horizontal('top')
        walls.add(temporary_wall4)
        all_closing_walls.add(temporary_wall4)
        all_sprites.add(temporary_wall4)
        temporary_wall4.rect.right = 700

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

        message = Objects.Message()
        all_sprites.add(message)
        all_messages.add(message)
        message.rect.center = (525, 500)
        if type_of_message == 'bow_is_broken':
            message.image = pygame.image.load('resources/messages/bow_is_broken.png')
            sound = pygame.mixer.Sound('resources/sounds/broke.wav')
            sound.play()
            delete()
        elif type_of_message == 'crossbow_is_broken':
            message.image = pygame.image.load('resources/messages/crossbow_is_broken.png')
            sound = pygame.mixer.Sound('resources/sounds/broke.wav')
            sound.play()
            delete()
        elif type_of_message == 'unlock_ability_1':
            message.image = pygame.image.load('resources/messages/unlock_ability_1.png')
            sound = pygame.mixer.Sound('resources/sounds/unlock_ability_1.wav')
            sound.play()
        elif type_of_message == 'unlock_ability_2':
            message.image = pygame.image.load('resources/messages/unlock_ability_2.png')
            sound = pygame.mixer.Sound('resources/sounds/unlock_ability_2.wav')
            sound.play()


    def use_first_item():
        if user.time_to_realise:
            if user.items[0].name == 'bow':
                if user.bow_time == 1:
                    sound = pygame.mixer.Sound('resources/sounds/user_shooting_from_bow.wav')
                    sound.play()
                    user.items[0].durability -= 1
                    arrow = Objects.Bullet()
                    all_sprites.add(arrow)
                    all_bullets.add(arrow)
                    arrow.rect.center = user.rect.center
                    if right:
                        arrow.direction = 'right'
                    elif left:
                        arrow.direction = 'left'
                    elif back:
                        arrow.direction = 'top'
                    elif front:
                        arrow.direction = 'bottom'
                    VisualEffects.animate_arrow(arrow)
                    bullet_move(arrow, arrow.direction)
                    if user.items[0].durability == 0:
                        user.time_to_realise = False
                        user.time_spended_to_realise = 0
                        print_the_message('bow_is_broken')
                    user.bow_time = 12

            elif user.items[0].name == 'crossbow':
                if user.crossbow_time == 1:
                    sound = pygame.mixer.Sound('resources/sounds/user_shooting_from_bow.wav')
                    sound.play()
                    user.items[0].durability -= 1
                    count = -80
                    if left or right:
                        for i in range(3):
                            count += 40
                            arrow = Objects.Bullet()
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

                            VisualEffects.animate_arrow(arrow)
                            bullet_move(arrow, arrow.direction)
                    elif front or back:
                        for i in range(3):
                            count += 40
                            arrow = Objects.Bullet()
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

                    if user.items[0].durability == 0:
                        user.time_to_realise = False
                        user.time_spended_to_realise = 0
                        print_the_message('crossbow_is_broken')

                    user.crossbow_time = 24

            elif user.items[0].name == 'heal_bottle':
                sound = pygame.mixer.Sound('resources/sounds/use_heal.wav')
                sound.play()
                user.hp += 1
                delete()

            elif user.items[0].name == 'paper_1':
                print_the_message('unlock_ability_1')
                delete()
                ability_cell_1.image = pygame.image.load('resources/Abilities/1_8.png')
                user.can_use_ability_1 = True

            elif user.items[0].name == 'paper_2':
                print_the_message('unlock_ability_2')
                delete()
                ability_cell_2.image = pygame.image.load('resources/Abilities/2_8.png')
                user.can_use_ability_2 = True

            elif user.items[0].name == 'sword':
                if user.sword_time == 1:
                    sound = pygame.mixer.Sound('resources/sounds/sword_sound.wav')
                    sound.play()
                    if left:
                        list = pygame.sprite.spritecollide(left_place_for_sword, all_enemy, False)
                        smash = Objects.Smash()
                        all_smashes.add(smash)
                        all_sprites.add(smash)
                        smash.name = 'left'
                        smash.rect.center = (user.rect.center[0] - 30, user.rect.center[1])
                    elif right:
                        list = pygame.sprite.spritecollide(right_place_for_sword, all_enemy, False)
                        smash = Objects.Smash()
                        all_smashes.add(smash)
                        all_sprites.add(smash)
                        smash.name = 'right'
                        smash.rect.center = (user.rect.center[0] + 5, user.rect.center[1])
                    elif back:
                        list = pygame.sprite.spritecollide(top_place_for_sword, all_enemy, False)
                        smash = Objects.Smash()
                        all_smashes.add(smash)
                        all_sprites.add(smash)
                        smash.name = 'top'
                        smash.rect.center = (user.rect.center[0] - 20, user.rect.center[1] - 20)
                    elif front:
                        list = pygame.sprite.spritecollide(bottom_place_for_sword, all_enemy, False)
                        smash = Objects.Smash()
                        all_smashes.add(smash)
                        all_sprites.add(smash)
                        smash.name = 'bottom'
                        smash.rect.center = (user.rect.center[0], user.rect.center[1] + 40)

                    for enemy in list:
                        enemy.hp -= 1
                    user.sword_time = 12
        else:
            pass

    ############################# Противники ##############################
    def generate_boss_of_imps():
        boss = Objects.Imp_Boss()
        boss.rect.center = (display_width/2, display_height/2)
        all_enemy.add(boss)
        all_imp_bosses.add(boss)
        all_sprites.add(boss)

        boss_bar = Objects.Boss_Bar_HP(boss)
        all_sprites.add(boss_bar)
        all_imp_boss_bars.add(boss_bar)
        boss.bar = boss_bar

    def generate_boss_of_ghost():
        boss = Objects.Ghost_Boss()
        boss.rect.center = (display_width/2, display_height/2)
        boss.image.set_alpha(1)
        all_enemy.add(boss)
        all_ghost_bosses.add(boss)
        all_sprites.add(boss)

        boss_bar = Objects.Boss_Bar_HP(boss)
        boss_bar.image.set_alpha(1)
        all_sprites.add(boss_bar)
        all_ghost_boss_bars.add(boss_bar)
        boss.bar = boss_bar

    def generate_boss_of_zombs():
        boss = Objects.Zomb_Boss()
        boss.rect.center = (display_width/2, display_height/2)
        all_enemy.add(boss)
        all_zomb_bosses.add(boss)
        all_sprites.add(boss)

        boss_bar = Objects.Boss_Bar_HP(boss)
        all_sprites.add(boss_bar)
        all_zomb_boss_bars.add(boss_bar)
        boss.bar = boss_bar


    def generate_ghosts():
        number_of_enemy = functions.chanse_to_spawn_the_ghosts(user.lvl)
        for i in range(number_of_enemy):
            ghost = Objects.Ghost()
            all_sprites.add(ghost)
            all_ghosts.add(ghost)
            all_enemy.add(ghost)
            ghost.rect.center = functions.random_position_of_spawn(display_width, display_height)

            ghost_bar = Objects.Enemy_Bar_HP(ghost)
            ghost.bar = ghost_bar
            all_sprites.add(ghost_bar)
            all_ghost_bars.add(ghost_bar)
            all_enemy_bars.add(ghost_bar)
            ghost_bar.rect.center = ghost_bar.follow.rect.center

    def generate_imps():
        number_of_enemy = functions.chanse_to_spawn_the_imps(user.lvl)
        for i in range(number_of_enemy):
            imp = Objects.Imp()
            all_sprites.add(imp)
            all_imps.add(imp)
            all_enemy.add(imp)
            imp.rect.center = functions.random_position_of_spawn(display_width, display_height)

            imp_bar = Objects.Enemy_Bar_HP(imp)
            imp.bar = imp_bar
            all_sprites.add(imp_bar)
            all_enemy_bars.add(imp_bar)
            all_imp_bars.add(imp_bar)
            imp_bar.rect.center = imp_bar.follow.rect.center

    def generate_zombies():
        number_of_enemy = functions.chanse_to_spawn_the_zombies(user.lvl)
        for i in range(number_of_enemy):
            zomb = Objects.Zombie()
            all_sprites.add(zomb)
            all_zombs.add(zomb)
            all_enemy.add(zomb)
            zomb.rect.center = functions.random_position_of_spawn(display_width, display_height)

            zomb_bar = Objects.Enemy_Bar_HP(zomb)
            zomb.bar = zomb_bar
            all_sprites.add(zomb_bar)
            all_enemy_bars.add(zomb_bar)
            all_zomb_bars.add(zomb_bar)
            zomb_bar.rect.center = zomb_bar.follow.rect.center


    ############################# ф-я генерации сундуков ##############################
    def generate_chests():
        for i in range(functions.chanse_to_spawn_the_chest(user)):
            chest = Objects.Chest()
            all_sprites.add(chest)
            all_chests.add(chest)
            chest.rect.center = functions.random_position_of_spawn_chest(display_width, display_height)

    def clean_the_display():
        display.fill((255, 255, 255))


    close_dors()
    ############################# Генерация сундуков ##############################
    generate_chests()
    ############################# Генерация противников ##############################
    generate_ghosts()
    ############################# Создаём стены ##############################
    wall_top_1 = Objects.Wall_Horizontal()
    all_sprites.add(wall_top_1)
    walls.add(wall_top_1)
    wall_top_1.rect.left = 0

    wall_top_2 = Objects.Wall_Horizontal()
    all_sprites.add(wall_top_2)
    walls.add(wall_top_2)
    wall_top_2.rect.left = 350

    wall_top_3 = Objects.Wall_Horizontal()
    all_sprites.add(wall_top_3)
    walls.add(wall_top_3)
    wall_top_3.rect.left = 1050

    wall_top_4 = Objects.Wall_Horizontal()
    all_sprites.add(wall_top_4)
    walls.add(wall_top_4)
    wall_top_4.rect.left = 0
    wall_top_4.rect.bottom = display_height

    wall_top_5 = Objects.Wall_Horizontal()
    all_sprites.add(wall_top_5)
    walls.add(wall_top_5)
    wall_top_5.rect.left = 750
    wall_top_5.rect.bottom = display_height

    wall_top_6 = Objects.Wall_Horizontal()
    all_sprites.add(wall_top_6)
    walls.add(wall_top_6)
    wall_top_6.rect.left = 1050
    wall_top_6.rect.bottom = display_height

    wall_top_7 = Objects.Wall_Vertical()
    all_sprites.add(wall_top_7)
    walls.add(wall_top_7)
    wall_top_7.rect.top = -150

    wall_top_8 = Objects.Wall_Vertical()
    all_sprites.add(wall_top_8)
    walls.add(wall_top_8)
    wall_top_8.rect.top = 500

    wall_top_9 = Objects.Wall_Vertical()
    all_sprites.add(wall_top_9)
    walls.add(wall_top_9)
    wall_top_9.rect.top = -150
    wall_top_9.rect.right = 1400

    wall_top_10 = Objects.Wall_Vertical()
    all_sprites.add(wall_top_10)
    walls.add(wall_top_10)
    wall_top_10.rect.right = 1400
    wall_top_10.rect.top = 500

    blocked_right = False
    blocked_left = False
    blocked_top = False
    blocked_bottom = False

    music_of_opening_walls = False

    ############################# Бар-хп ##############################
    bar = Objects.Bar_HP()   # бар
    all_sprites.add(bar)
    index_of_room = 0
    count_of_room = 1

    ############################# Бар-прочности ##############################
    bar_durability = Objects.Bar_DURABILITY()   # бар
    all_sprites.add(bar_durability)

    ############################# Ячейки абилок ##############################
    ability_cell_1 = Objects.Ability_cell_1()
    ability_cell_1.rect.top = display_height - 100
    ability_cell_2 = Objects.Ability_cell_2()
    ability_cell_2.rect.top = display_height - 150

    all_sprites.add(ability_cell_1)
    all_sprites.add(ability_cell_2)

    def drop(number, item):
        last_not_empty = len(user.items) - 1
        remember = user.items[number-1]
        user.items.pop(number-1)

        VisualEffects.upload_empty_slots(number, empty_1, empty_2, empty_3, empty_4, empty_5)
        print_items()

        if item == 'heal_bottle':
            dropted = Objects.Heal_bottle()
        elif item == 'bow':
            dropted = Objects.Bow()
            dropted.durability = remember.durability
        elif item == 'crossbow':
            dropted = Objects.Crossbow()
            dropted.durability = remember.durability
        elif item == 'sword':
            dropted = Objects.Sword()
        elif item == 'paper_1':
            dropted = Objects.Paper_1()
        elif item == 'paper_2':
            dropted = Objects.Paper_2()

        if right:
            dropted.rect.center = (user.rect.center[0] - 100, user.rect.center[1])
        elif left:
            dropted.rect.center = (user.rect.center[0] + 100, user.rect.center[1])
        elif front:
            dropted.rect.center = (user.rect.center[0], user.rect.center[1] - 100)
        elif back:
            dropted.rect.center = (user.rect.center[0], user.rect.center[1] + 100)

        all_sprites.add(dropted)
        all_items_ont_the_ground.add(dropted)

        VisualEffects.upload_last_empty_slots(last_not_empty, empty_1, empty_2, empty_3, empty_4, empty_5)


    def delete():
        last_not_empty = len(user.items) - 1
        user.items.pop(0)

        empty_1.image = pygame.image.load('resources\\inventory\\items\\empty_slot.png')

        print_items()
        VisualEffects.upload_last_empty_slots(last_not_empty, empty_1, empty_2, empty_3, empty_4, empty_5)

    def generate_red_chest():
        for i in all_chests:
            cur_chest = i
            break
        cur_chest.image = pygame.image.load('resources\\objects\\red_chest.png')
        cur_chest.special_drop = True


    inventory = Objects.Inventory()

    block_1 = Objects.Ceil_of_inventory()
    all_sprites.add(block_1)
    block_1.rect.center = (75,25)
    inventory.items.append(block_1)

    empty_1 = Objects.Place_for_item_in_ceil()
    all_sprites.add(empty_1)
    empty_1.rect.center = (75,25)
    empty_1.image = pygame.image.load('resources/inventory/items/sword.png')


    block_2 = Objects.Ceil_of_inventory()
    all_sprites.add(block_2)
    block_2.rect.center = (125,25)
    inventory.items.append(block_2)

    empty_2 = Objects.Place_for_item_in_ceil()
    all_sprites.add(empty_2)
    empty_2.rect.center = (125, 25)


    block_3 = Objects.Ceil_of_inventory()
    all_sprites.add(block_3)
    block_3.rect.center = (175,25)
    inventory.items.append(block_3)

    empty_3 = Objects.Place_for_item_in_ceil()
    all_sprites.add(empty_3)
    empty_3.rect.center = (175, 25)


    block_4 = Objects.Ceil_of_inventory()
    all_sprites.add(block_4)
    block_4.rect.center = (225,25)
    inventory.items.append(block_4)

    empty_4 = Objects.Place_for_item_in_ceil()
    all_sprites.add(empty_4)
    empty_4.rect.center = (225, 25)


    block_5 = Objects.Ceil_of_inventory()
    all_sprites.add(block_5)
    block_5.rect.center = (275,25)
    inventory.items.append(block_5)

    empty_5 = Objects.Place_for_item_in_ceil()
    all_sprites.add(empty_5)
    empty_5.rect.center = (275, 25)

    PAUSED = False
    while game:   # Пока сеанс игры запущен:
        if PAUSED:
            for event in pygame.event.get():   # Считываем все события
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        PAUSED = not PAUSED
        else:
            for event in pygame.event.get():   # Считываем все события
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        PAUSED = not PAUSED

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
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_1:
                        if user.can_use_ability_1:
                            use_ability_1(ability_cell_1)
                        else:
                            pass
                    if event.key == pygame.K_2:
                        if user.can_use_ability_2:
                            use_ability_2(ability_cell_2)
                        else:
                            pass

            keys = pygame.key.get_pressed()   # Инициализируем клавиатуру
            ############################# Движение игрока ##############################
            if first:
                back = False   # Направления, куда смотрит игрок
                front = True
                right = False
                left = False

                first = False

            if keys[pygame.K_w] and keys[pygame.K_a]:
                if user.rect.x < 50 and 200 <= user.rect.bottom <= 205:
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
                    user.rect.y -= user.speed / 2
                    user.rect.x -= user.speed / 2
            elif keys[pygame.K_w]:
                if user.rect.x < 50 and 200 <= user.rect.y <= 205:
                    pass
                elif user.rect.right > display_width - 50 and 200 <= user.rect.y <= 205:
                    pass
                elif user.rect.top <= -100 and 700 <= user.rect.x <= 975 and index_of_room == 4:
                    pass
                else:
                    user.rect.y -= user.speed
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
                    user.rect.x -= user.speed
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
                    user.rect.y -= user.speed / 2
                    user.rect.x += user.speed / 2
            elif keys[pygame.K_w]:
                if user.rect.x < 50 and 200 <= user.rect.y <= 205:
                    pass
                elif user.rect.right > display_width - 50 and 200 <= user.rect.y <= 205:
                    pass
                elif user.rect.top <= -100 and 700 <= user.rect.x <= 975 and index_of_room == 4:
                    pass
                else:
                    user.rect.y -= user.speed
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
                    user.rect.x += user.speed
                    back = False
                    front = False
                    right = True
                    left = False

            if keys[pygame.K_d] and keys[pygame.K_s]:
                if user.rect.x <= 50 and 495 <= user.rect.bottom <= 500:
                    pass
                elif user.rect.right > display_width - 50 and 200 <= user.rect.y <= 205:
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
                    user.rect.x += user.speed / 2
                    user.rect.y += user.speed / 2
            elif keys[pygame.K_d]:
                if 669 <= user.rect.x <= 675 and user.rect.bottom > 650:
                    pass
                elif 970 <= user.rect.x <= 975 and user.rect.top < 50:
                    pass
                elif user.rect.right > display_width + 100 and 200 <= user.rect.y <= 400 and index_of_room == 2:
                    pass
                else:
                    user.rect.x += user.speed
                    back = False
                    front = False
                    right = True
                    left = False
            elif keys[pygame.K_s]:
                if user.rect.x < 50 and 495 <= user.rect.bottom <= 500:
                    pass
                elif user.rect.right > display_width - 50 and 500 <= user.rect.bottom <= 505:
                    pass
                elif user.rect.bottom > display_height + 100 and 345 <= user.rect.x <= 675 and index_of_room == 3:
                    pass
                else:
                    user.rect.y += user.speed
                    back = False
                    front = True
                    right = False
                    left = False
            if keys[pygame.K_s] and keys[pygame.K_a]:
                if user.rect.x <= 50 and 200 <= user.rect.y <= 205:
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
                    user.rect.y += user.speed / 2
                    user.rect.x -= user.speed / 2
            elif keys[pygame.K_s]:
                if user.rect.x < 50 and 490 <= user.rect.bottom <= 500:
                    pass
                elif user.rect.right > display_width - 50 and 500 <= user.rect.bottom <= 505:
                    pass
                elif user.rect.bottom > display_height + 100 and 345 <= user.rect.x <= 675 and index_of_room == 3:
                    pass
                else:
                    user.rect.y += user.speed
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
                    user.rect.x -= user.speed
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
                black = Objects.Black()
                all_sprites.add(black)
                all_black_elements.add(black)

            if user.rect.right >= display_width + 150 or user.rect.left <= -150 or user.rect.top <= -150 or user.rect.bottom >= display_height + 150:
                count_of_room += 1
                count_of_room %= 4
                background.change_the_room(count_of_room)
                clean_the_display()
                for i in all_closing_walls:
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
                for sprite in all_blue_user_balls:
                    sprite.kill()
                remember = user
                user.kill()

                if user.rect.right >= display_width + 150:
                    user.lvl += 1
                    user.rect.left = -100
                    index_of_room = 1
                    close_dors()

                elif user.rect.left <= -150:
                    user.lvl += 1
                    user.rect.right = display_width + 100
                    index_of_room = 2
                    close_dors()

                elif user.rect.top <= -150:
                    user.lvl += 1
                    user.rect.bottom = display_height + 100
                    user.rect.x = 500
                    index_of_room = 3
                    close_dors()

                elif user.rect.bottom >= display_height + 150:
                    user.lvl += 1
                    user.rect.top = -100
                    user.rect.x = 835
                    index_of_room = 4
                    close_dors()

                if 1 <= user.lvl <= 9:
                    generate_ghosts()
                    generate_chests()
                if user.lvl == 10:
                    generate_boss_of_ghost()
                if 11 <= user.lvl < 19:
                    #generate_ghosts()
                    generate_imps()
                    generate_chests()
                if user.lvl == 19:
                    #generate_ghosts()
                    generate_imps()
                    generate_chests()
                    generate_red_chest()
                if user.lvl == 20:
                    generate_boss_of_imps()
                if 21 <= user.lvl <= 29:
                    #generate_ghosts()
                    #generate_imps()
                    generate_zombies()
                    generate_chests()
                if user.lvl == 30:
                    generate_boss_of_zombs()

                user = Objects.Player()
                user.can_use_ability_1 = remember.can_use_ability_1
                user.can_use_ability_2 = remember.can_use_ability_2
                user.items = remember.items
                user.hp = remember.hp
                user.rect.center = remember.rect.center
                user.scores = remember.scores
                user.lvl = remember.lvl
                all_sprites.add(user)

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
                    list[0].hp -= 1
                    bullet.kill()
                for wall in walls:
                    pygame.sprite.spritecollide(wall, all_bullets, True)
            ############################# Движение Призрака ##############################
            for ghost in all_ghosts:
                if not we_are_drawing:
                    if math.fabs(user.rect.center[0] - ghost.rect.center[0]) >= 50 or math.fabs(user.rect.center[1] - ghost.rect.center[1]) >= 50:
                        if user.rect.x > ghost.rect.x:
                            ghost.direction = 'right'
                            if user.rect.y > ghost.rect.y:
                                ghost.rect.y += ghost.speed / 2
                                ghost.rect.x += ghost.speed / 2
                            elif user.rect.y < ghost.rect.y:
                                ghost.rect.y -= ghost.speed / 2
                                ghost.rect.x += ghost.speed / 2
                            else:
                                ghost.rect.x += ghost.speed
                        elif user.rect.x < ghost.rect.x:
                            ghost.direction = 'left'
                            if user.rect.y > ghost.rect.y:
                                ghost.rect.y += ghost.speed / 2
                                ghost.rect.x -= ghost.speed / 2
                            elif user.rect.y < ghost.rect.y:
                                ghost.rect.y -= ghost.speed / 2
                                ghost.rect.x -= ghost.speed / 2
                            else:
                                ghost.rect.x -= ghost.speed
                        else:
                            if user.rect.y > ghost.rect.y :
                                ghost.rect.y += ghost.speed
                            elif user.rect.y < ghost.rect.y:
                                ghost.rect.y -= ghost.speed
                    else:
                        if pygame.sprite.spritecollide(user, all_ghosts, False):
                            sound = pygame.mixer.Sound('resources/sounds/ghost_dying.wav')
                            sound.play()
                            ghost.bar.kill()
                            all_enemy.remove(ghost)
                            all_ghosts.remove(ghost)
                            all_disappeared.add(ghost)
                            sound = pygame.mixer.Sound('resources/sounds/taking_damage_by_user.wav')
                            sound.play()
                            user.hp -= 1

                for bars in all_ghost_bars:
                    bars.rect.bottom = bars.follow.rect.top
                    bars.rect.x = bars.follow.rect.center[0] - 17

                    VisualEffects.update_ghost_bar(bars, all_enemy, all_ghosts, all_disappeared, user)

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

                VisualEffects.animate_ghost(ghost)

            ############################# Движение импа ##############################
            for imp in all_imps:
                if not we_are_drawing:
                    if math.fabs(user.rect.center[0] - imp.rect.center[0]) >= 50 or math.fabs(
                            user.rect.center[1] - imp.rect.center[1]) >= 50:
                        if user.rect.center[0] > imp.rect.center[0]:
                            imp.rect.x = imp.rect.x + imp.speed
                            imp.direction = 'right'
                        if user.rect.center[0] < imp.rect.center[0]:
                            imp.direction = 'left'
                            imp.rect.x = imp.rect.x - imp.speed

                        if user.rect.center[1] > imp.rect.center[1]:
                            imp.direction = 'bottom'
                            imp.rect.y = imp.rect.y + imp.speed
                        if user.rect.center[1] < imp.rect.center[1]:
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
                    VisualEffects.update_imp_bar(bars, user)

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
                VisualEffects.update_imp(imp)

            ############################# Отрисовка анимеции снарядов импа ##############################
            for ball in all_imp_fireballs:
                VisualEffects.update_imp_fireball(ball)

                if ball.rect.x < -100 or ball.rect.x > display_width + 100 or ball.rect.y < -100 or ball.rect.y > display_height + 100:
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
                imp_ball = Objects.Imp_Ball()
                imp_ball.direction = imp.direction
                all_sprites.add(imp_ball)
                all_imp_fireballs.add(imp_ball)
                imp_ball.rect.center = imp.rect.center

            for imp in all_imps:
                imp.shoot_timming += 1
                if imp.shoot_timming == 200:
                    imp_shoot(imp)
                    imp.shoot_timming = 1

            ############################# Движение зомби ##############################
            for zomb in all_zombs:
                if not we_are_drawing:
                    if math.fabs(user.rect.center[0] - zomb.rect.center[0]) >= 50 or math.fabs(
                            user.rect.center[1] - zomb.rect.center[1]) >= 50:
                        if user.rect.center[0] > zomb.rect.center[0]:
                            zomb.rect.x = zomb.rect.x + zomb.speed
                            zomb.direction = 'right'
                        if user.rect.center[0] < zomb.rect.center[0]:
                            zomb.direction = 'left'
                            zomb.rect.x = zomb.rect.x - zomb.speed

                        if user.rect.center[1] > zomb.rect.center[1]:
                            zomb.direction = 'bottom'
                            zomb.rect.y = zomb.rect.y + zomb.speed
                        if user.rect.center[1] < zomb.rect.center[1]:
                            zomb.direction = 'top'
                            zomb.rect.y = zomb.rect.y - zomb.speed
                    else:
                        if pygame.sprite.spritecollide(user, all_zombs, False):
                            zomb.kill()
                            zomb.bar.kill()
                            sound = pygame.mixer.Sound('resources/sounds/taking_damage_by_user.wav')
                            sound.play()
                            user.hp -= 3

                for bars in all_zomb_bars:
                    VisualEffects.update_zomb_bar(bars, user)

                if zomb.rect.top < 50:
                    if zomb.rect.left >= 700 and zomb.rect.right <= 1050:
                        pass
                    else:
                        zomb.rect.top = 50
                if zomb.rect.bottom > display_height - 50:
                    if zomb.rect.left >= 350 and zomb.rect.right <= 775:
                        pass
                    else:
                        zomb.rect.bottom = display_height - 50
                if zomb.rect.right > display_width - 50:
                    if zomb.rect.top >= 200 and zomb.rect.bottom <= 500:
                        pass
                    else:
                        zomb.rect.right = display_width - 50
                if zomb.rect.left < 50:
                    if zomb.rect.top >= 200 and zomb.rect.bottom <= 500:
                        pass
                    else:
                        zomb.rect.left = 50
                ############################# Отрисовка зомби ##############################
                VisualEffects.update_zomb(zomb)

            for zomb in all_zombs:
                zomb.run_timer += 1
                if zomb.run_timer == 200:
                    zomb.speed = 0
                if zomb.run_timer == 250:
                    zomb.speed = 2
                    zomb.running = True
                    zomb.condition = 1
                if zomb.run_timer == 400:
                    zomb.speed = 1
                    zomb.running = False
                    zomb.run_timer = 1


            def use_ability_1(ability_cell_1):
                all_abilities_1.add(ability_cell_1)
                user.can_use_ability_1 = False

                VisualEffects.upload_user_blue_balls_attack(user, all_sprites, all_blue_user_balls)

            def use_ability_2(ability_cell_2):
                all_abilities_2.add(ability_cell_2)
                user.can_use_ability_2 = False

                sound = pygame.mixer.Sound('resources/sounds/use_heal.wav')
                sound.play()

                user.hp += 1

            ############################# Предметы и взаимодействие с ними ##############################
            def pick_up():
                if len(user.items) < 5:
                    list = pygame.sprite.spritecollide(user, all_items_ont_the_ground, False)
                    sound = pygame.mixer.Sound('resources/sounds/pick_items_up.wav')
                    sound.play()
                    for i in range(len(list)):
                        if len(user.items) < 5:
                            user.items.append(list[i])
                            list[i].kill()
                    print_items()

            if pygame.sprite.spritecollide(user, all_items_ont_the_ground, False):
                pick_up()

            ############################# Сундуки и взаимодействие с ними ##############################
            def drop_items_from_chest(chest):
                if user.rect.center[0] >= chest.rect.center[0]:   # Если игрок стоит справа от сундука
                    if user.lvl < 20:
                        item = functions.choose_the_drop_10()
                    else:
                        item = functions.choose_the_drop_21()
                    distanse = -64
                    if item == 'bow':
                        item = Objects.Bow()
                    elif item == 'crossbow':
                        item = Objects.Crossbow()
                    elif item == 'heal_bottle':
                        item = Objects.Heal_bottle()
                elif user.rect.center[0] < chest.rect.center[0]:   # Если игрок стоит слева от сундука
                    if user.lvl < 20:
                        item = functions.choose_the_drop_10()
                    else:
                        item = functions.choose_the_drop_21()
                    distanse = 64
                    if item == 'bow':
                        item = Objects.Bow()
                    elif item == 'crossbow':
                        item = Objects.Crossbow()
                    elif item == 'heal_bottle':
                        item = Objects.Heal_bottle()

                all_sprites.add(item)
                all_items_ont_the_ground.add(item)
                item.rect.center = (chest.rect.center[0] + distanse, chest.rect.center[1])

            ############################# 'Красный' сундук и взаимодействие с ним ##############################
            def drop_items_from_red_chest(chest):
                if user.rect.center[0] >= chest.rect.center[0]:  # Если игрок стоит справа от сундука
                    item = functions.choose_the_drop_19()
                    distanse = -64
                    if item == 'paper_2':
                        item = Objects.Paper_2()
                elif user.rect.center[0] < chest.rect.center[0]:  # Если игрок стоит слева от сундука
                    item = functions.choose_the_drop_19()
                    distanse = 64
                    if item == 'paper_2':
                        item = Objects.Paper_2()

                all_sprites.add(item)
                all_items_ont_the_ground.add(item)
                item.rect.center = (chest.rect.center[0] + distanse, chest.rect.center[1])

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
                            if chest.special_drop:
                                drop_items_from_red_chest(chest)
                            else:
                                drop_items_from_chest(chest)
                        chest.dropted = True

            ############################# Выдвижение стен ##############################
            for block in all_closing_walls:
                if isinstance(block, Objects.Temporary_Wall_Vertical):
                    if block.place == 'left':
                        if user.rect.x > 125:
                            if block.rect.bottom < 500:
                                if block.rect.bottom == 250:
                                    sound = pygame.mixer.Sound('resources/sounds/mooving_wall_low.wav')
                                    sound.play()
                                block.rect.y += 5
                            else:
                                blocked_left = True
                    else:
                        if user.rect.x < display_width - 125:
                            if block.rect.bottom < 500:
                                if block.rect.bottom == 250:
                                    sound = pygame.mixer.Sound('resources/sounds/mooving_wall_low.wav')
                                    sound.play()
                                block.rect.y += 5
                            else:
                                blocked_right = True
                else:
                    if block.place == 'bottom':
                        if user.rect.y < display_height - 125:
                            if block.rect.right < 750:
                                if block.rect.right == 400:
                                    sound = pygame.mixer.Sound('resources/sounds/mooving_wall_low.wav')
                                    sound.play()
                                block.rect.x += 5
                            else:
                                blocked_bottom = True
                    else:
                        if user.rect.y > 125:
                            if block.rect.right < 1050:
                                if block.rect.right == 700:
                                    sound = pygame.mixer.Sound('resources/sounds/mooving_wall_low.wav')
                                    sound.play()
                                block.rect.x += 5
                            else:
                                blocked_top = True
            for block in all_opening_walls:
                if not music_of_opening_walls:
                    sound = pygame.mixer.Sound('resources/sounds/mooving_wall.wav')
                    sound.play()
                    music_of_opening_walls = True
                if isinstance(block, Objects.Temporary_Wall_Vertical):
                    if block.place == 'left':
                        if block.rect.bottom != 200:
                            block.rect.y -= 5
                        else:
                            block.kill()
                    else:
                        if block.rect.bottom != 200:
                            block.rect.y -= 5
                        else:
                            block.kill()
                else:
                    if block.place == 'bottom':
                        if block.rect.right != 350:
                            block.rect.x -= 5
                        else:
                            block.kill()
                    else:
                        if block.rect.right != 700:
                            block.rect.x -= 5
                        else:
                            block.kill()

            if not all_opening_walls:
                music_of_opening_walls = False

            ############################# Перестановка предметов из инвентаря ##############################
            def permutation():
                if len(user.items) > 1:
                    remember = user.items[0]
                    for i in range(len(user.items) - 1):
                        user.items[i] = user.items[i+1]
                    user.items[len(user.items) - 1] = remember
                    print_items()

                    if user.items[0].name == 'sword':
                        sound = pygame.mixer.Sound('resources/sounds/take_sword.wav')
                        sound.play()
                    elif user.items[0].name == 'bow':
                        sound = pygame.mixer.Sound('resources/sounds/take_bow.wav')
                        sound.play()
                    elif user.items[0].name == 'heal_bottle':
                        sound = pygame.mixer.Sound('resources/sounds/take_potion.wav')
                        sound.play()
                    elif user.items[0].name == 'paper_1':
                        sound = pygame.mixer.Sound('resources/sounds/take_paper_1.wav')
                        sound.play()
                    elif user.items[0].name == 'paper_2':
                        sound = pygame.mixer.Sound('resources/sounds/take_paper_1.wav')
                        sound.play()
                else:
                    pass
            ############################# Отрисовка предметов из инвентаря ##############################
            def print_items():
                for i in range(5):
                    inventory.items[i].is_empty = True

                for item in user.items:
                    VisualEffects.upload_current_item(item, inventory, empty_1, empty_2, empty_3, empty_4, empty_5)

            ############################# Отрисовка игрока и его хп ##############################
            VisualEffects.animate_player_and_his_bar(user, bar, front, back, right, left)

            ############################# Работа с баром прочности ##############################
            VisualEffects.upload_bar_of_duraility(user, bar_durability)

            ############################# Работа с боссом ##############################
            for boss in all_zomb_bosses:
                if math.fabs(user.rect.center[0] - boss.rect.center[0]) >= 50 or math.fabs(
                    user.rect.center[1] - boss.rect.center[1]) >= 50:
                    if user.rect.center[0] > boss.rect.center[0]:
                        boss.rect.x = boss.rect.x + boss.speed
                        boss.direction = 'right'
                    if user.rect.center[0] < boss.rect.center[0]:
                        boss.direction = 'left'
                        boss.rect.x = boss.rect.x - boss.speed

                    if user.rect.center[1] > boss.rect.center[1]:
                        boss.direction = 'bottom'
                        boss.rect.y = boss.rect.y + boss.speed
                    if user.rect.center[1] < boss.rect.center[1]:
                        boss.direction = 'top'
                        boss.rect.y = boss.rect.y - boss.speed

                if boss.rect.top < 50:
                    if boss.rect.left >= 700 and boss.rect.right <= 1050:
                        pass
                    else:
                        boss.rect.top = 50
                if boss.rect.bottom > display_height - 50:
                    if boss.rect.left >= 350 and boss.rect.right <= 775:
                        pass
                    else:
                        boss.rect.bottom = display_height - 50
                if boss.rect.right > display_width - 50:
                    if boss.rect.top >= 200 and boss.rect.bottom <= 500:
                        pass
                    else:
                        boss.rect.right = display_width - 50
                if boss.rect.left < 50:
                    if boss.rect.top >= 200 and boss.rect.bottom <= 500:
                        pass
                    else:
                        boss.rect.left = 50

                VisualEffects.update_zomb_boss_running(boss)

                if not boss.printed:
                    if boss.hp != 55:
                        boss.hp += 1
                    else:
                        boss.printed = True

            for bars in all_zomb_boss_bars:
                VisualEffects.upload_boss_of_zombs_bar(bars, all_disappeared, all_enemy, all_zombs, all_zomb_bosses, all_sprites)

            if pygame.sprite.spritecollide(user, all_zomb_bosses, False):
                for boss in all_zomb_bosses:
                    if not boss.attacked:
                        sound = pygame.mixer.Sound('resources/sounds/taking_damage_by_user.wav')
                        sound.play()
                        user.hp -= 1
                        boss.attacked = True
                        boss.attack_cooldown = 50

            for boss in all_zomb_bosses:
                if boss.attack_cooldown != 1:
                    boss.attack_cooldown -= 1
                else:
                    boss.attacked = False
            ############################# Выстрелы слизи ##############################
            for boss in all_zomb_bosses:
                boss.slime_fireball_timer += 1

                if boss.slime_fireball_timer == 500:
                    boss.slime_fireball_timer = 1
                    Zomb_boss.upload_slime_fireballs(all_slime_fireballs, all_sprites, boss)

            for ball in all_slime_fireballs:
                VisualEffects.update_slime_fireball(ball)
                Zomb_boss.check_to_target(all_slime_fireballs, walls, user, ball, all_sprites, all_puddles)



            for wall in walls:
                pygame.sprite.spritecollide(wall, all_slime_fireballs, True)

            for puddle in all_puddles:
                VisualEffects.update_puddle(puddle)
                puddle.timer_of_life += 1

                if not puddle.printed:
                    if puddle.image.get_alpha() != 251:
                        puddle.image.set_alpha(puddle.image.get_alpha() + 5)
                    else:
                        puddle.printed = True

                if puddle.timer_of_life == 200:
                    all_disappeared.add(puddle)
                    all_sprites.remove(puddle)
                    all_puddles.remove(puddle)

            list = pygame.sprite.spritecollide(user, all_puddles, False)
            for puddle in list:
                if not puddle.attacked:
                    user.hp -= 1

                    sound = pygame.mixer.Sound('resources/sounds/taking_damage_by_user.wav')
                    sound.play()

                    puddle.attacked = True
                    puddle.cooldown = 100

            for puddle in all_puddles:
                if puddle.cooldown != 1:
                    puddle.cooldown -= 1
                else:
                    puddle.attacked = False

            for boss in all_zomb_bosses:
                Zomb_boss.upload_zomb_portals(boss, all_sprites, display_width, display_height, creating_zomb_portals)

            for portal in creating_zomb_portals:
                if portal.image.get_alpha() != 251:
                    portal.image.set_alpha(portal.image.get_alpha() + 10)
                else:
                    creating_zomb_portals.remove(portal)
                    all_zomb_portals.add(portal)

            for portal in all_zomb_portals:
                VisualEffects.update_zomb_portals(portal)
                Zomb_boss.upload_zombs_in_portal(boss, portal, all_zomb_portals, all_sprites, all_zombs, all_enemy,
                                       all_enemy_bars, all_zomb_bars, deleting_zomb_portals)

            if all_zomb_portals or creating_zomb_portals:
                for boss in all_zomb_bosses:
                    boss.speed = 0
            else:
                for boss in all_zomb_bosses:
                    boss.speed = 1

            for portal in deleting_zomb_portals:
                if portal.image.get_alpha() != 1:
                    portal.image.set_alpha(portal.image.get_alpha() - 10)
                else:
                    portal.kill()
            ############################# Работа с боссом ##############################
            boss_printed = False

            for i in all_ghost_boss_bars:
                i.rect.center = (i.follow.rect.center[0], i.follow.rect.top - 20)

            for boss in all_ghost_bosses:   # Разворачивание босса в сторону игрока
                if user.rect.center[0] >= boss.rect.center[0]:
                    boss.direction = 'right'
                else:
                    boss.direction = 'left'
            ####### Проявление босса на карте #######
            for sprite in all_ghost_bosses:
                if sprite.image.get_alpha() != 255:
                    sprite.image.set_alpha(sprite.image.get_alpha() + 1)
                else:
                    boss_printed = True

            # Первое заполнение бара хп босса
            for sprite in all_ghost_boss_bars:
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
            for bars in all_ghost_boss_bars:
                VisualEffects.upload_boss_of_ghosts_bar(bars, all_disappeared, all_enemy, all_ghosts, all_ghost_bosses, all_sprites, all_items_ont_the_ground)

            # Атаки босса и анимация его самого
            if boss_printed:
                if not boss.angry:
                    for boss in all_ghost_bosses:
                        VisualEffects.upload_boss_of_ghosts(boss)

                ####### Атаки #######
                for boss in all_ghost_bosses:
                    Ghost_boss.upload_boss_teleportation(user, boss, display_width, display_height)

                    Ghost_boss.upload_boss_blue_balls_attack(boss, all_sprites, all_blue_boss_balls)

                    Ghost_boss.upload_boss_pink_balls_attack(boss, left_top, left_bottom, right_top, right_bottom, display_height, display_width)

                    Ghost_boss.upload_boss_portals(boss, creating_portals)

            for ball in all_pink_boss_balls:
                VisualEffects.update_boss_pink_fireballs(ball)
            for ball in all_blue_boss_balls:
                VisualEffects.update_boss_blue_fireballs(ball)

            # Создание порталов
            for boss in creating_portals:
                Ghost_boss.creating_boss_portals(user, boss, all_sprites, all_portals, creating_portals, display_width, display_height)

            # Анимация "злого" босса
            for boss in all_ghost_bosses:
                if not all_portals:
                    boss.angry = False

            # Спавн порталов- призраков
            for portal in all_portals:
                Ghost_boss.upload_ghosts_into_the_portals(boss, portal, all_sprites, all_ghosts, all_enemy, all_ghost_bars,
                                               all_enemy_bars)
                VisualEffects.update_boss_portals(portal)


            # Коллизия синих файерболлов и стен
            for wall in walls:
                pygame.sprite.spritecollide(wall, all_blue_boss_balls, True)

            # Коллизия синих файерболлов и игрока
            if pygame.sprite.spritecollide(user, all_blue_boss_balls, True):
                sound = pygame.mixer.Sound('resources/sounds/taking_damage_by_user.wav')
                sound.play()
                user.hp -= 1

            # Выстрелы розовых файерболлов
            for boss in left_top:
                Ghost_boss.shoot_boss_pink_balls_attack_left_top(boss, all_sprites, all_pink_boss_balls, left_top, display_width, display_height)

            for boss in left_bottom:
                Ghost_boss.shoot_boss_pink_balls_attack_left_bottom(boss, all_sprites, all_pink_boss_balls, left_bottom, display_width, display_height)

            for boss in right_top:
                Ghost_boss.shoot_boss_pink_balls_attack_right_top(boss, all_sprites, all_pink_boss_balls, right_top, display_width, display_height)

            for boss in right_bottom:
                Ghost_boss.shoot_boss_pink_balls_attack_right_bottom(boss, all_sprites, all_pink_boss_balls, right_bottom, display_width, display_height)

            # Коллизия розовых файерболлов и стен
            for wall in walls:
                pygame.sprite.spritecollide(wall, all_pink_boss_balls, True)

            # Коллизия розовых файерболлов и игрока
            if pygame.sprite.spritecollide(user, all_pink_boss_balls, True):
                sound = pygame.mixer.Sound('resources/sounds/taking_damage_by_user.wav')
                sound.play()
                user.hp -= 1

            # Коллизия игрока и босса
            for boss in all_ghost_bosses:
                if not boss.invisible:
                    if pygame.sprite.spritecollide(user, all_ghost_bosses, False):
                        sound = pygame.mixer.Sound('resources/sounds/taking_damage_by_user.wav')
                        sound.play()
                        for boss in all_ghost_bosses:
                            sound = pygame.mixer.Sound('resources/sounds/teleportation_of_ghost_boss.wav')
                            sound.play()
                            user.hp -= 1
                            boss.rect.center = functions.random_place_to_teleportation_of_boss_ghost(
                                display_width,
                                display_height,
                                user.rect.center[0],
                                user.rect.center[1]
                            )
                            boss.teleportation = 1

            ############################# Работа с боссом ##############################


            for boss in all_imp_bosses:
                if not boss.printed:
                    if boss.hp != 55:
                        boss.hp += 1
                    else:
                        boss.printed = True

            for bars in all_imp_boss_bars:
                bars.rect.bottom = bars.follow.rect.top
                bars.rect.x = bars.follow.rect.x - 65
                VisualEffects.upload_boss_of_imps_bar(bars, all_disappeared, all_imp_bosses, all_enemy)

            # Бег босса
            for boss in all_imp_bosses:
                Imp_boss.imp_boss_run(boss, user, imp_boss_run_left, imp_boss_run_right, imp_boss_run_top, imp_boss_run_bottom, display_width, display_height)

            for boss in imp_boss_run_left:
                if boss.need_to_run != 0:
                    boss.rect.x -= 5
                    boss.need_to_run -= 1
                    boss.direction = 'left'
                    VisualEffects.update_imp_boss_running(boss)
                    if boss.rect.left < 50:
                        boss.rect.left = 50
                        boss.image = pygame.image.load('resources/enemy/boss_imp_left_4.png')
                        imp_boss_run_left.remove(boss)
                        boss.need_to_run = 0
                else:
                    imp_boss_run_left.remove(boss)
                    boss.image = pygame.image.load('resources/enemy/boss_imp_left_4.png')

            for boss in imp_boss_run_right:
                if boss.need_to_run != 0:
                    boss.rect.x += 5
                    boss.need_to_run -= 1
                    boss.direction = 'right'
                    VisualEffects.update_imp_boss_running(boss)
                    if boss.rect.right > display_width - 50:
                        boss.rect.right = display_width - 50
                        boss.image = pygame.image.load('resources/enemy/boss_imp_right_4.png')
                        imp_boss_run_left.remove(boss)
                        boss.need_to_run = 0
                else:
                    imp_boss_run_right.remove(boss)
                    boss.image = pygame.image.load('resources/enemy/boss_imp_right_4.png')

            for boss in imp_boss_run_top:
                if boss.need_to_run != 0:
                    boss.rect.y -= 5
                    boss.need_to_run -= 1
                    boss.direction = 'top'
                    VisualEffects.update_imp_boss_running(boss)
                    if boss.rect.top < 50:
                        boss.rect.top = 50
                        boss.image = pygame.image.load('resources/enemy/boss_imp_top_3.png')
                        imp_boss_run_left.remove(boss)
                        boss.need_to_run = 0
                else:
                    imp_boss_run_top.remove(boss)
                    boss.image = pygame.image.load('resources/enemy/boss_imp_top_3.png')

            for boss in imp_boss_run_bottom:
                if boss.need_to_run != 0:
                    boss.rect.y += 5
                    boss.need_to_run -= 1
                    boss.direction = 'bottom'
                    VisualEffects.update_imp_boss_running(boss)
                    if boss.rect.bottom > display_height - 50:
                        boss.rect.bottom = display_height - 50
                        boss.image = pygame.image.load('resources/enemy/boss_imp_bottom_3.png')
                        imp_boss_run_left.remove(boss)
                        boss.need_to_run = 0
                else:
                    imp_boss_run_bottom.remove(boss)
                    boss.image = pygame.image.load('resources/enemy/boss_imp_bottom_3.png')

            #Выход босса за границы карты
            for boss in all_imp_bosses:
                if boss.rect.bottom > display_height - 50:
                    boss.rect.bottom = display_height - 50

            for boss in all_imp_bosses:
                Imp_boss.upload_imp_boss_fireballs(boss, user, all_sprites, all_imp_boss_fireballs, all_pentagramms)

                if boss.spawning_fireballs:
                    boss.count_of_spawned_fireballs += 1
                    if boss.count_of_spawned_fireballs <= 250:
                        if boss.count_of_spawned_fireballs%50 == 0:
                            sound = pygame.mixer.Sound('resources/sounds/imp_fireballs.wav')
                            sound.play()

                            ball = Objects.Boss_imp_fireball()
                            all_sprites.add(ball)
                            all_imp_boss_fireballs.add(ball)
                            ball.rect.center = (random.choice(range(boss.position_of_attacking[0]-100, boss.position_of_attacking[0]+100)), random.choice(range(boss.position_of_attacking[1]-100, boss.position_of_attacking[1]+100)) - 700)
                            ball.position_to_die = (ball.rect.center[0], ball.rect.center[1] + 700)
                    else:
                        boss.spawning_fireballs = False
                        boss.count_of_spawned_fireballs = 0

            for ball in all_imp_boss_fireballs:
                VisualEffects.update_imp_boss_fireball(ball)

            for penta in all_pentagramms:
                penta.condition += 1

                if not penta.spawned:
                    if penta.image.get_alpha() != 251:
                        penta.image.set_alpha(penta.image.get_alpha() + 10)
                    else:
                        penta.spawned = True
                if penta.condition == 350:
                    penta.killing = True

                if penta.killing:
                    if penta.image.get_alpha() != 1:
                        penta.image.set_alpha(penta.image.get_alpha() - 10)
                    else:
                        penta.kill()

            if pygame.sprite.spritecollide(user, all_imp_boss_fireballs, False):
                list = pygame.sprite.spritecollide(user, all_imp_boss_fireballs, False)
                if boss.position_of_attacking[0] - 115 <= list[0].rect.center[0] <= boss.position_of_attacking[0] + 115:
                    if boss.position_of_attacking[1] - 115 <= list[0].rect.center[1] <= boss.position_of_attacking[1] + 115:
                        if pygame.sprite.spritecollide(user, all_imp_boss_fireballs, True):
                            sound = pygame.mixer.Sound('resources/sounds/taking_damage_by_user.wav')
                            sound.play()
                            user.hp -= 1

            if pygame.sprite.spritecollide(user, all_imp_bosses, False):
                for boss in all_imp_bosses:
                    if not boss.attacked:
                        sound = pygame.mixer.Sound('resources/sounds/taking_damage_by_user.wav')
                        sound.play()
                        user.hp -= 1
                        boss.attacked = True
                        boss.attack_cooldown = 50

            for boss in all_imp_bosses:
                if boss.attack_cooldown != 1:
                    boss.attack_cooldown -= 1
                else:
                    boss.attacked = False

            for boss in all_imp_bosses:
                Imp_boss.upload_imp_portals(boss, all_sprites, display_width, display_height, creating_imp_portals)

            for portal in creating_imp_portals:
                if portal.image.get_alpha() != 251:
                    portal.image.set_alpha(portal.image.get_alpha() + 10)
                else:
                    creating_imp_portals.remove(portal)
                    all_imps_portals.add(portal)

            for portal in deleting_imp_portals:
                if portal.image.get_alpha() != 1:
                    portal.image.set_alpha(portal.image.get_alpha() - 10)
                else:
                    portal.kill()

            for portal in all_imps_portals:
                VisualEffects.update_imp_portals(portal)
                Imp_boss.upload_imps_in_portal(boss, portal, all_imps_portals, all_sprites, all_imps, all_enemy, all_enemy_bars, all_imp_bars, deleting_imp_portals)

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
                        i.image.set_alpha(i.image.get_alpha() - 8)
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

            for sword_place in all_sword_places:
                sword_place.rect.center = user.rect.center
                if sword_place.name == 'left':
                    sword_place.rect.right = user.rect.left
                elif sword_place.name == 'right':
                    sword_place.rect.left = user.rect.right
                elif sword_place.name == 'top':
                    sword_place.rect.bottom = user.rect.top
                elif sword_place.name == 'bottom':
                    sword_place.rect.top = user.rect.bottom

            for smash in all_smashes:
                VisualEffects.upload_user_sword_smashes(smash)

            for sprite in all_disappeared:
                if sprite.image.get_alpha() >= 1:
                    sprite.image.set_alpha(sprite.image.get_alpha() - 10)
                else:
                    sprite.kill()

            # Коллизия синих файерболлов и стен
            for wall in walls:
                pygame.sprite.spritecollide(wall, all_blue_user_balls, True)

            for abil in all_abilities_1:
                VisualEffects.update_ability_1(user, abil, all_abilities_1)

            for abil in all_abilities_2:
                VisualEffects.update_ability_2(user, abil, all_abilities_2)

            for ball in all_blue_user_balls:
                VisualEffects.update_boss_blue_fireballs(ball)
                if ball.rect.x <= -100 or ball.rect.x >= display_width + 100 or ball.rect.y <= -100 or ball.rect.y >= display_height + 100:
                    ball.kill()

            for win_bar in all_win_bars:
                if not win_bar.printed:
                    if win_bar.image.get_alpha() != 251:
                        win_bar.image.set_alpha(win_bar.image.get_alpha() + 5)
                    else:
                        win_bar.printed = True

                win_bar.rect.center = (user.rect.center[0] + 120, user.rect.center[1] - 45)

            # Коллизия синих файерболлов и противников
            for enemy in all_enemy:
                list = pygame.sprite.spritecollide(enemy, all_blue_user_balls, True)
                enemy.hp -= 2*len(list)

            if user.sword_time != 1:
                user.sword_time -= 1
            if user.bow_time != 1:
                user.bow_time -= 1
            if user.crossbow_time != 1:
                user.crossbow_time -= 1

            if not all_enemy and not user.lvl == 30:
                blocked_left = False
                blocked_right = False
                blocked_top = False
                blocked_bottom = False

                if index_of_room == 1:
                    blocked_left = True
                elif index_of_room == 2:
                    blocked_right = True
                elif index_of_room == 3:
                    blocked_bottom = True
                elif index_of_room == 4:
                    blocked_top = True

                open_walls(index_of_room)


            if user.lvl == 30:
                if not all_zomb_bosses:
                    for i in all_zombs:
                        i.bar.kill()
                        all_sprites.remove(i)
                        all_zombs.remove(i)
                        all_enemy.remove(i)
                        all_disappeared.add(i)

            if user.lvl == 20:
                if not all_imp_bosses:
                    for i in all_imps:
                        i.bar.kill()
                        all_sprites.remove(i)
                        all_imps.remove(i)
                        all_enemy.remove(i)
                        all_disappeared.add(i)

            if user.lvl == 10:
                if not all_ghost_bosses:
                    for i in all_ghosts:
                        i.bar.kill()
                        all_sprites.remove(i)
                        all_ghosts.remove(i)
                        all_enemy.remove(i)
                        all_disappeared.add(i)

            if user.lvl == 30 and (not all_enemy):
                user.soud_timer += 1
                if user.soud_timer == 50:
                    sound = pygame.mixer.Sound('resources/sounds/win.wav')
                    sound.play()
                    win_bar = Objects.Congrats()
                    all_sprites.add(win_bar)
                    all_win_bars.add(win_bar)


            pygame.display.update()
            all_sprites.update()   # Обновление спрайтов
            all_sprites.draw(display)  # Прорисовка всех спрайтов
            pygame.display.flip()   # Переворчиваем экран
            clock.tick(75)   # FPS

myimage = pygame_menu.baseimage.BaseImage(
    image_path='resources/menu_resources/background.png',
    drawing_mode=pygame_menu.baseimage.IMAGE_MODE_REPEAT_XY
)

mytheme = pygame_menu.themes.THEME_DARK
mytheme.widget_font = pygame_menu.font.FONT_MUNRO
mytheme.title_font = pygame_menu.font.FONT_MUNRO
mytheme.title_font_size = 100
mytheme.widget_font_size = 50
mytheme.background_color = myimage
mytheme.title_bar_style = pygame_menu.widgets.MENUBAR_STYLE_TITLE_ONLY_DIAGONAL

menu = pygame_menu.Menu('   Dungeon Slider   ', 1400, 700, theme=mytheme)
menu.add.button('Play', run_game)
menu.add.button('Quit', pygame_menu.events.EXIT)

menu.mainloop(surface)
