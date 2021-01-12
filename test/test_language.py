import unittest
from unittest.mock import patch
from language import *
from parameterized import parameterized

class LanguageTest(unittest.TestCase):
    def test_get_languages(self):
        languages = get_languages()
        self.assertIsInstance(languages, dict)
        self.assertTrue(len(languages) > 1)

    @parameterized.expand([
        ("en"),
        ("fr"),
    ])
    def test_get_commands_for_lang(self, lang):
        commands = get_command_for_lang(lang)
        self.assertIsInstance(commands, dict)
        self.assertTrue(len(commands) > 1)
