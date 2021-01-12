import sys
import time
from pygame import *
from settings import *
from Objects import *
from menu import dino_menu
from records import record_check
from retry import retry_menu




init()

if dino_menu():
    mixer.music.play(-1)
else:
    pass
generate_cactus_array(cactus_array)
pygame.display.set_caption('Играем')
while True:
    pace += 0.01
    score += 1
    for event_ in event.get():
        if event_.type == QUIT:  # exit game
            record_check(score // 10)
            retry_menu(score // 10)

    win_actions()
    time.Clock().tick(pace)



