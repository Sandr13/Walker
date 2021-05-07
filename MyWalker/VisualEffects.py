import pygame
import functions
import Objects

############################# Игрок ##############################
def animate_player_and_his_bar(user, bar, front, back, right, left):
    if front:
        user.image = pygame.image.load('resources\knight\\front.png')  # Переменная-картинка игрока
    elif back:
        user.image = pygame.image.load('resources\knight\\back.png')  # Переменная-картинка игрока
    elif right:
        user.image = pygame.image.load('resources\knight\\right.png')  # Переменная-картинка игрока
    elif left:
        user.image = pygame.image.load('resources\knight\\left.png')  # Переменная-картинка игрока

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
        functions.endgame()

    elif user.hp > 5:
        user.hp = 5

############################# Прочность предметов ##############################
def upload_bar_of_duraility(user, bar_durability):
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

############################# Снаряды ##############################
def animate_arrow(arrow):
    if arrow.direction == 'right':
        arrow.image = pygame.image.load('resources\\attacking\\arrow-right.png')
    elif arrow.direction == 'left':
        arrow.image = pygame.image.load('resources\\attacking\\arrow-left.png')
    elif arrow.direction == 'top':
        arrow.image = pygame.image.load('resources\\attacking\\arrow-top.png')
    elif arrow.direction == 'bottom':
        arrow.image = pygame.image.load('resources\\attacking\\arrow-bottom.png')

############################# Инвентарь ##############################
def upload_empty_slots(number, empty_1, empty_2, empty_3, empty_4, empty_5):
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

def upload_last_empty_slots(last_not_empty, empty_1, empty_2, empty_3, empty_4, empty_5):
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

def upload_current_item(item, inventory, empty_1, empty_2, empty_3, empty_4, empty_5):
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

    elif item.name == 'sword':
        directory = 'resources\\inventory\\items\\sword.png'

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

    elif item.name == 'paper_1':
        directory = 'resources\\inventory\\items\\open_1.png'

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


############################# Призраки ##############################
def animate_ghost(ghost):
    if ghost.direction == 'right':
        ghost.image = pygame.image.load('resources\enemy\ghost_right.png')
    elif ghost.direction == 'left':
        ghost.image = pygame.image.load('resources\enemy\ghost_left.png')

def update_ghost_bar(bars, all_enemy, all_ghosts, all_disappeared, user):
    if 4 <= bars.follow.hp <= 5:
        bars.image = pygame.image.load('resources\\enemy health\\2.png')
    if 1 <= bars.follow.hp <= 3:
        bars.image = pygame.image.load('resources\\enemy health\\1.png')
    if bars.follow.hp <= 0:
        sound = pygame.mixer.Sound('resources/sounds/ghost_dying.wav')
        sound.play()
        all_enemy.remove(bars.follow)
        all_ghosts.remove(bars.follow)
        all_disappeared.add(bars.follow)
        bars.kill()
        user.scores += 1


############################# Босс призраков ##############################
def update_boss_portals(portal):
    portal.condition += 1
    if portal.direction == 'left':
        if portal.condition == 1:
            portal.image = pygame.image.load('resources/objects/portal_left_1.png')
        elif portal.condition == 8:
            portal.image = pygame.image.load('resources/objects/portal_left_2.png')
        elif portal.condition == 16:
            portal.image = pygame.image.load('resources/objects/portal_left_3.png')
        elif portal.condition == 24:
            portal.image = pygame.image.load('resources/objects/portal_left_4.png')
        elif portal.condition == 32:
            portal.image = pygame.image.load('resources/objects/portal_left_5.png')
        elif portal.condition == 40:
            portal.image = pygame.image.load('resources/objects/portal_left_6.png')
        elif portal.condition == 48:
            portal.image = pygame.image.load('resources/objects/portal_left_7.png')
        elif portal.condition == 56:
            portal.image = pygame.image.load('resources/objects/portal_left_8.png')
        elif portal.condition == 64:
            portal.image = pygame.image.load('resources/objects/portal_left_9.png')
            portal.condition = 1
    elif portal.direction == 'right':
        if portal.condition == 1:
            portal.image = pygame.image.load('resources/objects/portal_right_1.png')
        elif portal.condition == 8:
            portal.image = pygame.image.load('resources/objects/portal_right_2.png')
        elif portal.condition == 16:
            portal.image = pygame.image.load('resources/objects/portal_right_3.png')
        elif portal.condition == 24:
            portal.image = pygame.image.load('resources/objects/portal_right_4.png')
        elif portal.condition == 32:
            portal.image = pygame.image.load('resources/objects/portal_right_5.png')
        elif portal.condition == 40:
            portal.image = pygame.image.load('resources/objects/portal_right_6.png')
        elif portal.condition == 48:
            portal.image = pygame.image.load('resources/objects/portal_right_7.png')
        elif portal.condition == 56:
            portal.image = pygame.image.load('resources/objects/portal_right_8.png')
        elif portal.condition == 64:
            portal.image = pygame.image.load('resources/objects/portal_right_9.png')
            portal.condition = 1

def update_boss_pink_fireballs(ball):
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

def update_boss_blue_fireballs(ball):
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
            ball.condition = 1

def upload_boss_of_ghosts_bar(bars, all_disappeared, all_enemy, all_ghosts, all_bosses, all_sprites, all_items_ont_the_ground):
    bars.rect.center = (bars.follow.rect.center[0], bars.follow.rect.top - 20)
    if bars.follow.hp == 55:
        bars.image = pygame.image.load('resources/boss_bars/55.png')
    if bars.follow.hp == 54:
        bars.image = pygame.image.load('resources/boss_bars/54.png')
    elif bars.follow.hp == 53:
        bars.image = pygame.image.load('resources/boss_bars/53.png')
    elif bars.follow.hp == 52:
        bars.image = pygame.image.load('resources/boss_bars/52.png')
    elif bars.follow.hp == 51:
        bars.image = pygame.image.load('resources/boss_bars/51.png')
    elif bars.follow.hp == 50:
        bars.image = pygame.image.load('resources/boss_bars/50.png')
    elif bars.follow.hp == 49:
        bars.image = pygame.image.load('resources/boss_bars/49.png')
    elif bars.follow.hp == 48:
        bars.image = pygame.image.load('resources/boss_bars/48.png')
    elif bars.follow.hp == 47:
        bars.image = pygame.image.load('resources/boss_bars/47.png')
    elif bars.follow.hp == 46:
        bars.image = pygame.image.load('resources/boss_bars/46.png')
    elif bars.follow.hp == 45:
        bars.image = pygame.image.load('resources/boss_bars/45.png')
    elif bars.follow.hp == 44:
        bars.image = pygame.image.load('resources/boss_bars/44.png')
    elif bars.follow.hp == 43:
        bars.image = pygame.image.load('resources/boss_bars/43.png')
    elif bars.follow.hp == 42:
        bars.image = pygame.image.load('resources/boss_bars/42.png')
    elif bars.follow.hp == 41:
        bars.image = pygame.image.load('resources/boss_bars/41.png')
    elif bars.follow.hp == 40:
        bars.image = pygame.image.load('resources/boss_bars/40.png')
    elif bars.follow.hp == 39:
        bars.image = pygame.image.load('resources/boss_bars/39.png')
    elif bars.follow.hp == 38:
        bars.image = pygame.image.load('resources/boss_bars/38.png')
    elif bars.follow.hp == 37:
        bars.image = pygame.image.load('resources/boss_bars/37.png')
    elif bars.follow.hp == 36:
        bars.image = pygame.image.load('resources/boss_bars/36.png')
    elif bars.follow.hp == 35:
        bars.image = pygame.image.load('resources/boss_bars/35.png')
    elif bars.follow.hp == 34:
        bars.image = pygame.image.load('resources/boss_bars/34.png')
    elif bars.follow.hp == 33:
        bars.image = pygame.image.load('resources/boss_bars/33.png')
    elif bars.follow.hp == 32:
        bars.image = pygame.image.load('resources/boss_bars/32.png')
    elif bars.follow.hp == 31:
        bars.image = pygame.image.load('resources/boss_bars/31.png')
    elif bars.follow.hp == 30:
        bars.image = pygame.image.load('resources/boss_bars/30.png')
    elif bars.follow.hp == 29:
        bars.image = pygame.image.load('resources/boss_bars/29.png')
    elif bars.follow.hp == 28:
        bars.image = pygame.image.load('resources/boss_bars/28.png')
    elif bars.follow.hp == 27:
        bars.image = pygame.image.load('resources/boss_bars/27.png')
    elif bars.follow.hp == 26:
        bars.image = pygame.image.load('resources/boss_bars/26.png')
    elif bars.follow.hp == 25:
        bars.image = pygame.image.load('resources/boss_bars/25.png')
    elif bars.follow.hp == 24:
        bars.image = pygame.image.load('resources/boss_bars/24.png')
    elif bars.follow.hp == 23:
        bars.image = pygame.image.load('resources/boss_bars/23.png')
    elif bars.follow.hp == 22:
        bars.image = pygame.image.load('resources/boss_bars/22.png')
    elif bars.follow.hp == 21:
        bars.image = pygame.image.load('resources/boss_bars/21.png')
    elif bars.follow.hp == 20:
        bars.image = pygame.image.load('resources/boss_bars/20.png')
    elif bars.follow.hp == 19:
        bars.image = pygame.image.load('resources/boss_bars/19.png')
    elif bars.follow.hp == 18:
        bars.image = pygame.image.load('resources/boss_bars/18.png')
    elif bars.follow.hp == 17:
        bars.image = pygame.image.load('resources/boss_bars/17.png')
    elif bars.follow.hp == 16:
        bars.image = pygame.image.load('resources/boss_bars/16.png')
    elif bars.follow.hp == 15:
        bars.image = pygame.image.load('resources/boss_bars/15.png')
    elif bars.follow.hp == 14:
        bars.image = pygame.image.load('resources/boss_bars/14.png')
    elif bars.follow.hp == 13:
        bars.image = pygame.image.load('resources/boss_bars/13.png')
    elif bars.follow.hp == 12:
        bars.image = pygame.image.load('resources/boss_bars/12.png')
    elif bars.follow.hp == 11:
        bars.image = pygame.image.load('resources/boss_bars/11.png')
    elif bars.follow.hp == 10:
        bars.image = pygame.image.load('resources/boss_bars/10.png')
    elif bars.follow.hp == 9:
        bars.image = pygame.image.load('resources/boss_bars/9.png')
    elif bars.follow.hp == 8:
        bars.image = pygame.image.load('resources/boss_bars/8.png')
    elif bars.follow.hp == 7:
        bars.image = pygame.image.load('resources/boss_bars/7.png')
    elif bars.follow.hp == 6:
        bars.image = pygame.image.load('resources/boss_bars/6.png')
    elif bars.follow.hp == 5:
        bars.image = pygame.image.load('resources/boss_bars/5.png')
    elif bars.follow.hp == 4:
        bars.image = pygame.image.load('resources/boss_bars/4.png')
    elif bars.follow.hp == 3:
        bars.image = pygame.image.load('resources/boss_bars/3.png')
    elif bars.follow.hp == 2:
        bars.image = pygame.image.load('resources/boss_bars/2.png')
    elif bars.follow.hp == 1:
        bars.image = pygame.image.load('resources/boss_bars/1.png')
    elif bars.follow.hp <= 0:

        # Дроп разблокировки первого перка
        droppted_item = Objects.Paper_1()
        droppted_item.rect.center = bars.follow.rect.center
        all_sprites.add(droppted_item)
        all_items_ont_the_ground.add(droppted_item)

        all_enemy.remove(bars.follow)
        all_ghosts.remove(bars.follow)
        all_bosses.remove(bars.follow)
        all_disappeared.add(bars.follow)
        bars.kill()

def upload_boss_of_ghosts(boss):
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

def upload_user_sword_smashes(smash):
    smash.condition += 1
    if smash.name == 'left':
        if smash.condition == 1:
            smash.image = pygame.image.load('resources/attacking/smash_left_1.png')
        elif smash.condition == 2:
            smash.image = pygame.image.load('resources/attacking/smash_left_2.png')
        elif smash.condition == 3:
            smash.image = pygame.image.load('resources/attacking/smash_left_3.png')
        elif smash.condition == 4:
            smash.image = pygame.image.load('resources/attacking/smash_left_4.png')
        elif smash.condition == 5:
            smash.image = pygame.image.load('resources/attacking/smash_left_5.png')
        elif smash.condition == 6:
            smash.image = pygame.image.load('resources/attacking/smash_left_6.png')
        elif smash.condition == 7:
            smash.image = pygame.image.load('resources/attacking/smash_left_7.png')
        elif smash.condition == 8:
            smash.image = pygame.image.load('resources/attacking/smash_left_8.png')
        elif smash.condition == 9:
            smash.kill()
    elif smash.name == 'right':
        if smash.condition == 1:
            smash.image = pygame.image.load('resources/attacking/smash_right_1.png')
        elif smash.condition == 2:
            smash.image = pygame.image.load('resources/attacking/smash_right_2.png')
        elif smash.condition == 3:
            smash.image = pygame.image.load('resources/attacking/smash_right_3.png')
        elif smash.condition == 4:
            smash.image = pygame.image.load('resources/attacking/smash_right_4.png')
        elif smash.condition == 5:
            smash.image = pygame.image.load('resources/attacking/smash_right_5.png')
        elif smash.condition == 6:
            smash.image = pygame.image.load('resources/attacking/smash_right_6.png')
        elif smash.condition == 7:
            smash.image = pygame.image.load('resources/attacking/smash_right_7.png')
        elif smash.condition == 8:
            smash.image = pygame.image.load('resources/attacking/smash_right_8.png')
        elif smash.condition == 9:
            smash.kill()
    elif smash.name == 'top':
        if smash.condition == 1:
            smash.image = pygame.image.load('resources/attacking/smash_top_1.png')
        elif smash.condition == 2:
            smash.image = pygame.image.load('resources/attacking/smash_top_2.png')
        elif smash.condition == 3:
            smash.image = pygame.image.load('resources/attacking/smash_top_3.png')
        elif smash.condition == 4:
            smash.image = pygame.image.load('resources/attacking/smash_top_4.png')
        elif smash.condition == 5:
            smash.image = pygame.image.load('resources/attacking/smash_top_5.png')
        elif smash.condition == 6:
            smash.image = pygame.image.load('resources/attacking/smash_top_6.png')
        elif smash.condition == 7:
            smash.image = pygame.image.load('resources/attacking/smash_top_7.png')
        elif smash.condition == 8:
            smash.image = pygame.image.load('resources/attacking/smash_top_8.png')
        elif smash.condition == 9:
            smash.kill()
    elif smash.name == 'bottom':
        if smash.condition == 1:
            smash.image = pygame.image.load('resources/attacking/smash_bottom_1.png')
        elif smash.condition == 2:
            smash.image = pygame.image.load('resources/attacking/smash_bottom_2.png')
        elif smash.condition == 3:
            smash.image = pygame.image.load('resources/attacking/smash_bottom_3.png')
        elif smash.condition == 4:
            smash.image = pygame.image.load('resources/attacking/smash_bottom_4.png')
        elif smash.condition == 5:
            smash.image = pygame.image.load('resources/attacking/smash_bottom_5.png')
        elif smash.condition == 6:
            smash.image = pygame.image.load('resources/attacking/smash_bottom_6.png')
        elif smash.condition == 7:
            smash.image = pygame.image.load('resources/attacking/smash_bottom_7.png')
        elif smash.condition == 8:
            smash.image = pygame.image.load('resources/attacking/smash_bottom_8.png')
        elif smash.condition == 9:
            smash.kill()

def update_ability_1(user, abil, all_abilities_1):
    if abil.condition < 150:
        abil.image = pygame.image.load('resources/Abilities/1_1.png')
    elif abil.condition == 150:
        abil.image = pygame.image.load('resources/Abilities/1_2.png')
    elif abil.condition == 300:
        abil.image = pygame.image.load('resources/Abilities/1_3.png')
    elif abil.condition == 450:
        abil.image = pygame.image.load('resources/Abilities/1_4.png')
    elif abil.condition == 600:
        abil.image = pygame.image.load('resources/Abilities/1_5.png')
    elif abil.condition == 750:
        abil.image = pygame.image.load('resources/Abilities/1_6.png')
    elif abil.condition == 900:
        abil.image = pygame.image.load('resources/Abilities/1_7.png')
    elif abil.condition == 1150:
        abil.image = pygame.image.load('resources/Abilities/1_8.png')
        abil.condition = 1
        user.can_use_ability_1 = True
        all_abilities_1.remove(abil)

    abil.condition += 1

def upload_user_blue_balls_attack(user, all_sprites, all_blue_user_balls):
    sound = pygame.mixer.Sound('resources/sounds/blue_fireballs.wav')
    sound.play()

    ball1 = Objects.Ghost_boss_blue_ball()
    all_sprites.add(ball1)
    all_blue_user_balls.add(ball1)
    ball1.rect.center = user.rect.center
    ball1.direction = 'bottom'

    ball2 = Objects.Ghost_boss_blue_ball()
    all_sprites.add(ball2)
    all_blue_user_balls.add(ball2)
    ball2.rect.center = user.rect.center
    ball2.direction = 'bottom_left'

    ball3 = Objects.Ghost_boss_blue_ball()
    all_sprites.add(ball3)
    all_blue_user_balls.add(ball3)
    ball3.rect.center = user.rect.center
    ball3.direction = 'left'

    ball4 = Objects.Ghost_boss_blue_ball()
    all_sprites.add(ball4)
    all_blue_user_balls.add(ball4)
    ball4.rect.center = user.rect.center
    ball4.direction = 'top_left'

    ball5 = Objects.Ghost_boss_blue_ball()
    all_sprites.add(ball5)
    all_blue_user_balls.add(ball5)
    ball5.rect.center = user.rect.center
    ball5.direction = 'top'

    ball6 = Objects.Ghost_boss_blue_ball()
    all_sprites.add(ball6)
    all_blue_user_balls.add(ball6)
    ball6.rect.center = user.rect.center
    ball6.direction = 'top_right'

    ball7 = Objects.Ghost_boss_blue_ball()
    all_sprites.add(ball7)
    all_blue_user_balls.add(ball7)
    ball7.rect.center = user.rect.center
    ball7.direction = 'right'

    ball8 = Objects.Ghost_boss_blue_ball()
    all_sprites.add(ball8)
    all_blue_user_balls.add(ball8)
    ball8.rect.center = user.rect.center
    ball8.direction = 'bottom_right'

def update_imp_bar(bars, user):
    bars.rect.bottom = bars.follow.rect.top
    bars.rect.x = bars.follow.rect.center[0] - 10
    if bars.follow.hp <= 7:
        bars.image = pygame.image.load('resources\\enemy health\\2.png')
    if bars.follow.hp <= 4:
        bars.image = pygame.image.load('resources\\enemy health\\1.png')
    if bars.follow.hp <= 0:
        sound = pygame.mixer.Sound('resources/sounds/imp_dying.wav')
        sound.play()
        bars.follow.kill()
        bars.kill()
        user.scores += 3

def update_imp(imp):
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

def update_imp_fireball(ball):
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