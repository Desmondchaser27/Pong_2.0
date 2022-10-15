import io
import typing
from typing import Union
from enum import Enum


class SettingsType(Enum):
    NULL = 0
    SKIP = 1
    DISPLAY = 2

# -> Define return type

def read_settings_file(filepath: str) -> dict[SettingsType, dict[str, Union[int, float, str]]]:
    #the file variable is of the type typing.TEXTIO
    file: typing.TextIO = open(filepath, 'r')
    line: str = "_"  # Filler to get in while loop
    settings_type: SettingsType = SettingsType.SKIP
    dictionary: dict[SettingsType, dict[str, Union[int, float, str]]] = dict()
    while line != '':
        line = file.readline().strip()

        # TODO: as we add more setting options expand this match/case
        match line:
            case "[Display]":
                settings_type = SettingsType.DISPLAY

        while "[" not in line and "]" not in line and not line == '':
            words: list[str] = line.split('=')
            for i in range(len(words)):
                words[i] = words[i].strip()
            if len(words) == 2:
                entry = dictionary.get(settings_type)
                if entry is None:
                    dictionary[settings_type] = {words[0]: words[1]}
                else:
                    entry[words[0]] = words[1]
            line = file.readline().strip()
    file.close()
    return dictionary