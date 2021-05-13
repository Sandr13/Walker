import pygame
display_width = 1400
display_height = 700

############################# Класс объекта-игрока ##############################
class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('resources\\knight\\front.png')
        self.rect = self.image.get_rect()
        self.rect.center = (display_width / 2, display_height / 2)
        self.hp = 5
        self.speed = 2
        self.items = []
        self.scores = 0
        self.lvl = 21
        self.time_to_realise = True
        self.time_spended_to_realise = 0
        self.sword_time = 1
        self.bow_time = 1
        self.can_use_ability_1 = False
        self.can_use_ability_2 = False


############################# Класс инвентаря ##############################
class Inventory:
    def __init__(self):
        self.items = []

############################# Класс объекта-ячейки абилки ##############################
class Ability_cell_1(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('resources/Abilities/1_blocked.png')
        self.rect = self.image.get_rect()
        self.condition = 1

############################# Класс объекта-ячейки абилки ##############################
class Ability_cell_2(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('resources/Abilities/2_blocked.png')
        self.rect = self.image.get_rect()
        self.condition = 1


############################# Класс объекта-бара прочности ##############################
class Bar_DURABILITY(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('resources\\inventory\\items\\empty_slot.png')
        self.rect = self.image.get_rect()
        self.rect.left = 350
        self.rect.top = 5

############################# Класс эффекта следа меча ##############################
class Smash(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('resources/inventory/items/empty_slot.png')
        self.rect = self.image.get_rect()
        self.name = ''
        self.condition = 1

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

############################# Класс объекта-портала призраков ##############################
class Ghost_portal(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('resources/objects/portal_right_1.png')
        self.rect = self.image.get_rect()
        self.condition = 1
        self.direction = ''
        self.spawned_ghosts = 0
        self.spawn_timer = 1

############################# Класс объекта-портала импов ##############################
class Imp_portal(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('resources/inventory/items/empty_slot.png')
        self.image.set_alpha(1)
        self.rect = self.image.get_rect()
        self.condition = 1
        self.direction = ''
        self.created = False
        self.destroyings = False
        self.spawn_timer = 1


################################ Класс призрака ##################################
class Ghost(pygame.sprite.Sprite):
    def __init__(self, object=0):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('resources\\enemy\\ghost_left.png')
        self.rect = self.image.get_rect()
        self.speed = 2
        self.hp = 6
        self.bar = object
        self.direction = ''

################################ Класс импа-босса ##################################
class Imp_Boss(pygame.sprite.Sprite):
    def __init__(self, object=0):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('resources/enemy/boss_imp_bottom_1.png')
        self.rect = self.image.get_rect()
        self.bar = object
        self.hp = 1
        self.printed = False
        self.run_timer = 1
        self.fireballs_timer = 1
        self.need_to_run = 0
        self.direction = ''
        self.condition = 1
        self.count_of_spawned_fireballs = 0
        self.spawning_fireballs = False
        self.position_of_attacking = (0, 0)
        self.attacked = False
        self.attack_cooldown = 1
        self.portal_timer = 1

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
        self.portal_timer = 1
        self.angry = False
        self.created_portals = False
        self.invisible = False

############################# Класс объекта-верхнего файерболла босса импов ##############################
class Boss_imp_fireball(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('resources/inventory/items/empty_slot.png')
        self.rect = self.image.get_rect()
        self.condition = 1
        self.position_to_die = 0

############################# Класс пентаграммы ##############################
class Pentagramm(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('resources/objects/pentagramm.png')
        self.image.set_alpha(1)
        self.rect = self.image.get_rect()
        self.spawned = False
        self.condition = 1
        self.killing = False

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

################################ Класс зомби ##################################
class Zombie(pygame.sprite.Sprite):
    def __init__(self, object=0):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('resources\\enemy\\zombie_bottom_2.png')
        self.rect = self.image.get_rect()
        self.speed = 1
        self.hp = 15
        self.bar = object
        self.condition = 1
        self.running = False
        self.run_timer = 1
        self.direction = ''


############################# Класс объекта-снаряда Импа ##############################
class Imp_Ball(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('resources/inventory/items/empty_slot.png')
        self.rect = self.image.get_rect()
        self.condition = 1
        self.direction = ''

############################# Класс объекта-синего файерболла ##############################
class Ghost_boss_blue_ball(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('resources/attacking/blue_ball_left_1.png')
        self.rect = self.image.get_rect()
        self.condition = 1
        self.direction = ''

############################# Класс объекта-розового файерболла ##############################
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
        self.special_drop = False


############################# Класс right_left места для меча ##############################
class Right_left_sword_barrier(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('resources/attacking/left_and_right_sword_place.png')
        self.rect = self.image.get_rect()
        self.name = ''

############################# Класс top_bottom места для меча ##############################
class Top_bottom_sword_barrier(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('resources/attacking/top_and_bottom_sword_place.png')
        self.rect = self.image.get_rect()
        self.name = ''

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
        self.index = ''
        self.sound = False

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

############################# Класс пергамента абилки_1 ##############################
class Paper_1(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('resources/Abilities/open_ability_1.png')
        self.rect = self.image.get_rect()
        self.name = 'paper_1'

############################# Класс пергамента абилки_2 ##############################
class Paper_2(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('resources/Abilities/open_ability_2.png')
        self.rect = self.image.get_rect()
        self.name = 'paper_2'

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

############################# Класс меча ##############################
class Sword(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('resources/inventory/items/sword.png')
        self.rect = self.image.get_rect()
        self.name = 'sword'

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