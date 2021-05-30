import pygame
import functions
import Objects
import random

def upload_slime_fireballs(all_slime_fireballs, all_sprites, boss):
    list_of_directions = ['left', 'right', 'top', 'bottom']
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




    if pygame.sprite.spritecollide(user, all_slime_fireballs, False):
        puddle = Objects.Puddle()
        puddle.rect.center = user.rect.center
        user.hp -= 1

        sound = pygame.mixer.Sound('resources/sounds/taking_damage_by_user.wav')
        sound.play()

        all_sprites.add(puddle)
        all_puddles.add(puddle)
        ball.kill()

    if ball.target_point == ball.rect.center:
        puddle = Objects.Puddle()
        puddle.rect.center = ball.rect.center
        all_sprites.add(puddle)
        all_puddles.add(puddle)
        ball.kill()

