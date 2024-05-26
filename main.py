import pyautogui as pg
import keyboard

REGION_BATTLE = (1193, 391, 160, 69)
pg.useImageNotFoundException(False)

def check_battle():
  return pg.locateOnScreen('imgs/region_battle2.png', region=REGION_BATTLE)


def kill_monster():
  while True:
    keyboard.wait('h')
    is_battle = check_battle()
    if is_battle == None:
        print('Entrei aqui')
        pg.press('space')
        while pg.locateOnScreen('imgs/red_target.png', confidence=0.8,) != None:
           print('Esperando mostro morrer')
        print('procurando outro monstro')
    print(is_battle)

#while True:
 #  print(pg.locateOnScreen('imgs/region_loot.png'))

kill_monster()



