import pygame
from Helpers.FileReader import SettingsType
from typing import Union


SCREEN = WIDTH, HEIGHT = 1200, 800
FPS = 60


def import_settings(settings_dict: dict[SettingsType, dict[str, Union[int, float, str]]]) -> None:
    setting: dict[str, Union[int, float, str]] = settings_dict.get(SettingsType.DISPLAY)
    global SCREEN, WIDTH, HEIGHT, FPS
    if not setting is None:
        for key in setting:
            match key:
                case "FPS":
                    FPS = int(setting[key])
                case "WindowHeight":
                    HEIGHT = int(setting[key])
                case "WindowWidth":
                    WIDTH = int(setting[key])

    SCREEN = (WIDTH, HEIGHT)



#count = 0
#count = (count + 1) % 20
    #if count == 0:
        #color = pygame.Color(random.randrange(0, 255), random.randrange(0, 255), random.randrange(0, 255))