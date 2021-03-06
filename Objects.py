from pygame import *
from settings import *
from random import *



class Enemies:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def cactus_spawn(self):
        if self.x >= -self.width:
            self.x -= 3.5
        else:
            self.x = 800
        win.blit(cactus_sprite, (self.x, self.y))


def win_actions():
    global win, run_status, pace
    win.blit(bg_image, (0, 0))
    update()
    if run_status:
        running_animation()
    show_cactus_array(cactus_array)
    display.flip()


def jump():
    global y, jump_status, jump_index, gravity, pace
    if not sneak_status:
        win.blit(jump_sprite, (x, y))
    else:
        win.blit(sneaking_sprite, (x, y))
    if jump_index >= -30:
        if jump_index == 30:
            mixer.Sound.play(jump_sound)
        y -= jump_index / gravity
        jump_index -= 1
    else:
        jump_index = 30
        jump_status = False
    
    
def update():
    global jump_status, sneak_status, run_status
    keys = key.get_pressed()
    if (keys[K_SPACE] or keys[K_UP]) and not sneak_status:
        jump_status = True
    if keys[K_DOWN] or keys[KMOD_CTRL]:
        run_status = False
        sneak_status = True
        sneak_animation()
    if not keys[K_DOWN] and not keys[KMOD_CTRL]:
        run_status = True
        sneak_status = False
    if jump_status:
        jump()


def running_animation():
    global run_index, run_status, win
    if run_index >= 16:
        run_index = 0
    if y == height - dino_height - 25:
        win.blit(run_sprite[run_index // 8], (x, y))
        run_index += 1


def sneak_animation():
    global sneak_status, sneak_index, run_status
    if sneak_index >= 16:
        sneak_index = 0
    if y == height - dino_height - 25:
        win.blit(sneak_sprite[sneak_index // 8], (x, y))
        sneak_index += 1


def generate_cactus_array(array):
    n = 0
    x = randint(70, 900)
    while n != 10:
        x1 = randint(70, 900)
        if x1 in range(x + 30, x - 30):
            if x > 415:
                x1 -= 50
            else:
                x1 += 50
        array.append(Enemies(x1, y, cactus_width, cactus_height))
        n += 1


def show_cactus_array(array):
    for cactus in array:
        cactus.cactus_spawn()
