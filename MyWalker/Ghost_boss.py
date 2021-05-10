import pygame
import functions
import Objects
import random


def upload_ghosts_into_the_portals(boss, portal, all_sprites, all_ghosts, all_enemy, all_ghost_bars, all_enemy_bars):
    boss.pink_ball_timer = 1
    boss.blue_ball_timer = 1
    boss.teleportation = 1
    boss.portal_timer = 1
    if portal.spawned_ghosts != 2:
        portal.spawn_timer += 1
        if portal.spawn_timer == 200:
            portal.spawned_ghosts += 1
            portal.spawn_timer = 1

            ghost = Objects.Ghost()
            all_sprites.add(ghost)
            all_ghosts.add(ghost)
            all_enemy.add(ghost)
            ghost.rect.center = portal.rect.center

            ghost_bar = Objects.Enemy_Bar_HP(ghost)
            ghost.bar = ghost_bar
            all_sprites.add(ghost_bar)
            all_ghost_bars.add(ghost_bar)
            all_enemy_bars.add(ghost_bar)
            ghost_bar.rect.center = ghost_bar.follow.rect.center

    else:
        portal.kill()


def upload_boss_portals(boss, creating_portals):
    if boss.portal_timer == 700:
        creating_portals.add(boss)
        boss.portal_timer = 1
    else:
        boss.portal_timer += 1

def creating_boss_portals(user, boss, all_sprites, all_portals, creating_portals, display_width, display_height):
    boss.pink_ball_timer = 1
    boss.blue_ball_timer = 1
    boss.teleportation = 1
    boss.portal_timer = 1

    sound = pygame.mixer.Sound('resources/sounds/creating_a_portal.wav')
    sound.play()

    boss.angry = True
    if boss.direction == 'left':
        boss.image = pygame.image.load('resources/enemy/ghost_boss_angry_left.png')
    elif boss.direction == 'right':
        boss.image = pygame.image.load('resources/enemy/ghost_boss_angry_right.png')

    for i in range(random.choice([1, 2])):
        portal = Objects.Ghost_portal()
        all_sprites.add(portal)
        all_portals.add(portal)
        portal.rect.center = functions.random_position_of_spawn(display_width, display_height)
        if portal.rect.center[0] >= user.rect.center[0]:
            portal.direction = 'right'
        else:
            portal.direction = 'left'
    creating_portals.remove(boss)

def upload_boss_teleportation(user, boss, display_width, display_height):
    if boss.teleportation == 150:
        sound = pygame.mixer.Sound('resources/sounds/teleportation_of_ghost_boss.wav')
        sound.play()
        boss.rect.center = functions.random_place_to_teleportation_of_boss_ghost(
            display_width,
            display_height,
            user.rect.center[0],
            user.rect.center[1]
        )
        boss.teleportation = 1
    else:
        boss.teleportation += 1

def shoot_boss_pink_balls_attack_left_top(boss, all_sprites, all_pink_boss_balls, left_top, display_width, display_height):
    boss.pink_ball_timer = 1
    boss.blue_ball_timer = 1
    boss.teleportation = 1
    boss.invisible = True

    if boss.rect.bottom < display_height - 50:
        boss.rect.y += 2
        boss.count_of_pink_balls += 1
        if boss.count_of_pink_balls % 40 == 0:

            sound = pygame.mixer.Sound('resources/sounds/pink_fireballs.wav')
            sound.play()

            ball = Objects.Ghost_boss_pink_ball()
            all_sprites.add(ball)
            all_pink_boss_balls.add(ball)
            ball.rect.center = boss.rect.center
            ball.direction = 'right'
        else:
            pass
    else:
        left_top.remove(boss)
        boss.count_of_pink_balls = 0
        boss.invisible = False

def shoot_boss_pink_balls_attack_left_bottom(boss, all_sprites, all_pink_boss_balls, left_bottom, display_width, display_height):
    boss.pink_ball_timer = 1
    boss.blue_ball_timer = 1
    boss.teleportation = 1
    boss.invisible = True

    if boss.rect.top > 50:
        boss.rect.y -= 2
        boss.count_of_pink_balls += 1
        if boss.count_of_pink_balls % 40 == 0:

            sound = pygame.mixer.Sound('resources/sounds/pink_fireballs.wav')
            sound.play()

            ball = Objects.Ghost_boss_pink_ball()
            all_sprites.add(ball)
            all_pink_boss_balls.add(ball)
            ball.rect.center = boss.rect.center
            ball.direction = 'right'
        else:
            pass
    else:
        left_bottom.remove(boss)
        boss.count_of_pink_balls = 0
        boss.invisible = False

def shoot_boss_pink_balls_attack_right_top(boss, all_sprites, all_pink_boss_balls, right_top, display_width, display_height):
    boss.pink_ball_timer = 1
    boss.blue_ball_timer = 1
    boss.teleportation = 1
    boss.invisible = True

    if boss.rect.bottom < display_height - 50:
        boss.rect.y += 2
        boss.count_of_pink_balls += 1
        if boss.count_of_pink_balls % 40 == 0:

            sound = pygame.mixer.Sound('resources/sounds/pink_fireballs.wav')
            sound.play()

            ball = Objects.Ghost_boss_pink_ball()
            all_sprites.add(ball)
            all_pink_boss_balls.add(ball)
            ball.rect.center = boss.rect.center
            ball.direction = 'left'
        else:
            pass
    else:
        right_top.remove(boss)
        boss.count_of_pink_balls = 0
        boss.invisible = False

def shoot_boss_pink_balls_attack_right_bottom(boss, all_sprites, all_pink_boss_balls, right_bottom, display_width, display_height):
    boss.pink_ball_timer = 1
    boss.blue_ball_timer = 1
    boss.teleportation = 1
    boss.invisible = True

    if boss.rect.top > 50:
        boss.rect.y -= 2
        boss.count_of_pink_balls += 1
        if boss.count_of_pink_balls % 40 == 0:

            sound = pygame.mixer.Sound('resources/sounds/pink_fireballs.wav')
            sound.play()

            ball = Objects.Ghost_boss_pink_ball()
            all_sprites.add(ball)
            all_pink_boss_balls.add(ball)
            ball.rect.center = boss.rect.center
            ball.direction = 'left'
        else:
            pass
    else:
        right_bottom.remove(boss)
        boss.count_of_pink_balls = 0
        boss.invisible = False


def upload_boss_pink_balls_attack(boss, left_top, left_bottom, right_top, right_bottom, display_height, display_width):
    if boss.pink_ball_timer == 500:
        boss.portal_timer -= 200
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

def upload_boss_blue_balls_attack(boss, all_sprites, all_blue_boss_balls):
    if boss.blue_ball_timer == 200:
        boss.blue_ball_timer = 1

        sound = pygame.mixer.Sound('resources/sounds/blue_fireballs.wav')
        sound.play()

        ball1 = Objects.Ghost_boss_blue_ball()
        all_sprites.add(ball1)
        all_blue_boss_balls.add(ball1)
        ball1.rect.center = boss.rect.center
        ball1.direction = 'bottom'

        ball2 = Objects.Ghost_boss_blue_ball()
        all_sprites.add(ball2)
        all_blue_boss_balls.add(ball2)
        ball2.rect.center = boss.rect.center
        ball2.direction = 'bottom_left'

        ball3 = Objects.Ghost_boss_blue_ball()
        all_sprites.add(ball3)
        all_blue_boss_balls.add(ball3)
        ball3.rect.center = boss.rect.center
        ball3.direction = 'left'

        ball4 = Objects.Ghost_boss_blue_ball()
        all_sprites.add(ball4)
        all_blue_boss_balls.add(ball4)
        ball4.rect.center = boss.rect.center
        ball4.direction = 'top_left'

        ball5 = Objects.Ghost_boss_blue_ball()
        all_sprites.add(ball5)
        all_blue_boss_balls.add(ball5)
        ball5.rect.center = boss.rect.center
        ball5.direction = 'top'

        ball6 = Objects.Ghost_boss_blue_ball()
        all_sprites.add(ball6)
        all_blue_boss_balls.add(ball6)
        ball6.rect.center = boss.rect.center
        ball6.direction = 'top_right'

        ball7 = Objects.Ghost_boss_blue_ball()
        all_sprites.add(ball7)
        all_blue_boss_balls.add(ball7)
        ball7.rect.center = boss.rect.center
        ball7.direction = 'right'

        ball8 = Objects.Ghost_boss_blue_ball()
        all_sprites.add(ball8)
        all_blue_boss_balls.add(ball8)
        ball8.rect.center = boss.rect.center
        ball8.direction = 'bottom_right'
    else:
        boss.blue_ball_timer += 1