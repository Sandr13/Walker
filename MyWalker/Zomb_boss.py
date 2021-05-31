import pygame
import functions
import Objects
import random

def upload_slime_fireballs(all_slime_fireballs, all_sprites, boss):
    list_of_directions = ['left', 'right', 'top', 'bottom']

    sound = pygame.mixer.Sound('resources/sounds/dropping_axid.wav')
    sound.play()

    for i in range(random.choice([1, 2])):
        ball = Objects.Slime_fireBall()
        ball.rect.center = boss.rect.center
        all_slime_fireballs.add(ball)
        all_sprites.add(ball)
        ball.direction = random.choice(list_of_directions)

        if ball.direction == 'left':
            ball.target_point = (boss.rect.center[0] - 300, boss.rect.center[1])
            list_of_directions.remove('left')
        elif ball.direction == 'right':
            ball.target_point = (boss.rect.center[0] + 300, boss.rect.center[1])
            list_of_directions.remove('right')
        elif ball.direction == 'top':
            ball.target_point = (boss.rect.center[0], boss.rect.center[1] - 300)
            list_of_directions.remove('top')
        elif ball.direction == 'bottom':
            ball.target_point = (boss.rect.center[0], boss.rect.center[1] + 300)
            list_of_directions.remove('bottom')

def check_to_target(all_slime_fireballs, walls, user, ball, all_sprites, all_puddles):
    for wall in walls:
        if pygame.sprite.spritecollide(wall, all_slime_fireballs, False):
            puddle = Objects.Puddle()

            if ball.direction == 'left':
                puddle.rect.center = (ball.rect.center[0] + 60, ball.rect.center[1])
            elif ball.direction == 'right':
                puddle.rect.center = (ball.rect.center[0] - 60, ball.rect.center[1])
            elif ball.direction == 'top':
                puddle.rect.center = (ball.rect.center[0], ball.rect.center[1] + 25)
            elif ball.direction == 'bottom':
                puddle.rect.center = (ball.rect.center[0], ball.rect.center[1] - 25)

            all_sprites.add(puddle)
            all_puddles.add(puddle)
            ball.kill()

            sound = pygame.mixer.Sound('resources/sounds/axid.wav')
            sound.play()




    if pygame.sprite.spritecollide(user, all_slime_fireballs, False):
        puddle = Objects.Puddle()
        puddle.rect.center = user.rect.center
        user.hp -= 1

        sound = pygame.mixer.Sound('resources/sounds/taking_damage_by_user.wav')
        sound.play()
        sound = pygame.mixer.Sound('resources/sounds/axid.wav')
        sound.play()

        all_sprites.add(puddle)
        all_puddles.add(puddle)
        ball.kill()
        sound = pygame.mixer.Sound('resources/sounds/axid.wav')
        sound.play()

    if ball.target_point == ball.rect.center:
        puddle = Objects.Puddle()
        puddle.rect.center = ball.rect.center
        all_sprites.add(puddle)
        all_puddles.add(puddle)
        ball.kill()
        sound = pygame.mixer.Sound('resources/sounds/axid.wav')
        sound.play()


def upload_zomb_portals(boss, all_sprites, display_width, display_height, creating_zomb_portals):
    boss.portal_timer += 1

    if boss.portal_timer == 800:
        sound = pygame.mixer.Sound('resources/sounds/creating_a_portal_imp.wav')
        sound.play()

        boss.portal_timer = 1
        boss.slime_fireball_timer = 1

        portal = Objects.Zomb_portal()
        creating_zomb_portals.add(portal)
        all_sprites.add(portal)
        portal.rect.center = (
        random.choice(range(150, display_width - 150)), random.choice(range(150, display_height - 150)))
        if portal.rect.center[0] <= display_width / 2:
            portal.direction = 'left'
            portal.image.set_alpha(1)
        elif portal.rect.center[0] > display_width / 2:
            portal.direction = 'right'
            portal.image.set_alpha(1)

def upload_zombs_in_portal(boss, portal, all_zomb_portals, all_sprites, all_zombs, all_enemy, all_enemy_bars, all_zomb_bars, deleting_zomb_portals):
    portal.spawn_timer += 1

    if portal.spawn_timer <= 200:
        boss.portal_timer = 1
        if portal.spawn_timer%200 == 0:
            zomb = Objects.Zombie()
            all_sprites.add(zomb)
            all_zombs.add(zomb)
            all_enemy.add(zomb)
            zomb.rect.x = portal.rect.center[0]
            zomb.rect.y = portal.rect.center[1]

            zomb_bar = Objects.Enemy_Bar_HP(zomb)
            zomb.bar = zomb_bar
            all_sprites.add(zomb_bar)
            all_enemy_bars.add(zomb_bar)
            all_zomb_bars.add(zomb_bar)
            zomb_bar.rect.center = zomb_bar.follow.rect.center
    else:
        all_zomb_portals.remove(portal)
        deleting_zomb_portals.add(portal)
