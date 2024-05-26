import pyautogui as pg


def check_battle():
    return pg.locateOnScreen('imgs/region_battle.PNG')

while True:
  is_battle = check_battle()
  print(is_battle)