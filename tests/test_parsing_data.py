import os
from gendiff.data_parser import parsing

FIXTURES_FOLDER = 'fixtures'
FILE_FLAT_FIRST_JSON = os.path.join(os.path.dirname(__file__), FIXTURES_FOLDER, 'file_flat_first.json')
FILE_FLAT_FIRST_YML = os.path.join(os.path.dirname(__file__), FIXTURES_FOLDER, 'file_flat_first.yml')

RESULT_DICT = {'host': 'hexlet.io', 'timeout': 50, 'proxy': '123.234.53.22', 'follow': False}


def test_parsing():
    assert parsing(open(FILE_FLAT_FIRST_JSON), 'json') == RESULT_DICT
    assert parsing(open(FILE_FLAT_FIRST_YML), 'yml') == RESULT_DICT
    assert parsing(open(FILE_FLAT_FIRST_YML), 'txt') is None
