import pygame
import random

import Objects


def imp_boss_run(boss, user, imp_boss_run_left, imp_boss_run_right, imp_boss_run_top, imp_boss_run_bottom, display_width, display_height):
    boss.run_timer += 1

    if boss.run_timer == 200:
        boss.run_timer = 1
        boss.condition = 1

        way = random.choice(['horizontal', 'vertical'])

        length_to_run = random.choice(range(300, 600, 5))
        boss.need_to_run = length_to_run/5

        if way == 'horizontal':
            if boss.rect.x == 50 or boss.rect.x == display_width-50:
                if boss.rect.x == 50:
                    imp_boss_run_right.add(boss)
                elif boss.rect.x == display_width-50:
                    imp_boss_run_left.add(boss)
            else:
                if user.rect.x < boss.rect.x:
                    imp_boss_run_left.add(boss)
                elif user.rect.x >= boss.rect.x:
                    imp_boss_run_right.add(boss)
        elif way == 'vertical':
            if boss.rect.y == 50 or boss.rect.y == display_height-50:
                if boss.rect.y == 50:
                    imp_boss_run_bottom.add(boss)
                elif boss.rect.y == display_height-50:
                    imp_boss_run_top.add(boss)
            else:
                if user.rect.y < boss.rect.y:
                    imp_boss_run_top.add(boss)
                elif user.rect.y >= boss.rect.y:
                    imp_boss_run_bottom.add(boss)

def upload_imp_boss_fireballs(boss, user, all_sprites, all_imp_boss_fireballs, all_pentagramms):
    boss.fireballs_timer += 1

    if boss.fireballs_timer == 400:
        boss.spawning_fireballs = True
        boss.fireballs_timer = -200
        boss.position_of_attacking = (random.choice(range(user.rect.center[0]-100, user.rect.center[0]+100)), random.choice(range(user.rect.center[1]-100, user.rect.center[1]+100)))

        pentagramm = Objects.Pentagramm()
        all_sprites.add(pentagramm)
        all_pentagramms.add(pentagramm)
        pentagramm.rect.center = boss.position_of_attacking

def upload_imp_portals(boss, all_sprites, display_width, display_height, creating_imp_portals):
    boss.portal_timer += 1

    if boss.portal_timer == 600:
        boss.portal_timer = 1
        boss.fireballs_timer = 1
        for i in range(random.choice([1, 2])):
            portal = Objects.Imp_portal()
            creating_imp_portals.add(portal)
            all_sprites.add(portal)
            portal.rect.center = (random.choice(range(150, display_width - 150)), random.choice(range(150, display_height - 150)))
            if portal.rect.center[0] <= display_width/2:
                portal.direction = 'left'
                portal.image = pygame.image.load('resources/objects/imp_portal_left_1.png')
                portal.image.set_alpha(1)
            elif portal.rect.center[0] > display_width/2:
                portal.direction = 'right'
                portal.image = pygame.image.load('resources/objects/imp_portal_right_1.png')
                portal.image.set_alpha(1)

def upload_imps_in_portal(boss, portal, all_imps_portals, all_sprites, all_imps, all_enemy, all_enemy_bars, all_imp_bars, deleting_imp_portals):
    portal.spawn_timer += 1

    if portal.spawn_timer <= 200:
        boss.portal_timer = 1
        if portal.spawn_timer%200 == 0:
            imp = Objects.Imp()
            all_sprites.add(imp)
            all_imps.add(imp)
            all_enemy.add(imp)
            imp.rect.x = portal.rect.center[0]
            imp.rect.y = portal.rect.center[1]

            imp_bar = Objects.Enemy_Bar_HP(imp)
            imp.bar = imp_bar
            all_sprites.add(imp_bar)
            all_enemy_bars.add(imp_bar)
            all_imp_bars.add(imp_bar)
            imp_bar.rect.center = imp_bar.follow.rect.center
    else:
        all_imps_portals.remove(portal)
        deleting_imp_portals.add(portal)
