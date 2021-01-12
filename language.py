import yaml
from enum import Enum

__LANGUAGE_FILE = './language/language.yml'
__COMMAND_FILE_PREFIX = './language/command_'

def get_languages():
    return __read_yaml(__LANGUAGE_FILE)

def get_command_for_lang(language):
    commands_file = f'{__COMMAND_FILE_PREFIX}{language[:2].lower()}.yml'
    return __read_yaml(commands_file)

def __read_yaml(file_path):
    with open(file_path, 'r') as file:
        content = yaml.load(file, Loader=yaml.FullLoader)

    return content

class Language(Enum):
    FR = 'fr-FR'
    EN = 'en-US'