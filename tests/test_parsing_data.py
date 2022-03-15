import os
import pytest
from gendiff.data_parser import parsing
from gendiff.file import YML, JSON
from gendiff.file import read_file

FIXTURES_FOLDER = 'fixtures'
FILE_FLAT_FIRST_JSON = os.path.join(os.path.dirname(__file__), FIXTURES_FOLDER, 'file_flat_first.json')
FILE_FLAT_FIRST_YML = os.path.join(os.path.dirname(__file__), FIXTURES_FOLDER, 'file_flat_first.yml')

RESULT_DICT = {'host': 'hexlet.io', 'timeout': 50, 'proxy': '123.234.53.22', 'follow': False}

data_json_file = read_file(FILE_FLAT_FIRST_JSON)
data_yml_file = read_file(FILE_FLAT_FIRST_YML)


def test_parsing():
    assert parsing(data_json_file, JSON) == RESULT_DICT
    assert parsing(data_yml_file, YML) == RESULT_DICT
    with pytest.raises(Exception):
        parsing(data_yml_file, 'txt')
