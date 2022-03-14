import os
import pytest
from gendiff.gendiff import generate_diff
from gendiff.formatters.format import STYlISH_FORMAT, PLAIN_FORMAT, JSON_FORMAT
import typing

FIXTURES_FOLDER = 'fixtures'


def get_path(file_name):
    return os.path.join(os.path.dirname(__file__), FIXTURES_FOLDER, file_name)


FILE_FLAT_FIRST_JSON = get_path('file_flat_first.json')
FILE_FLAT_SECOND_JSON = get_path('file_flat_second.json')
FILE_FLAT_FIRST_YML = get_path('file_flat_first.yml')
FILE_FLAT_SECOND_YML = get_path('file_flat_second.yml')
FILE_NESTED_FIRST_JSON = get_path('file_nested_first.json')
FILE_NESTED_SECOND_JSON = get_path('file_nested_second.json')
FILE_NESTED_FIRST_YML = get_path('file_nested_first.yml')
FILE_NESTED_SECOND_YML = get_path('file_nested_second.yml')

RESULT_FLAT_STYLISH = get_path('result_flat_stylish.txt')
RESULT_FLAT_PLAIN = get_path('result_flat_plain.txt')
RESULT_FLAT_JSON = get_path('result_flat_json.txt')
RESULT_NESTED_STYLISH = get_path('result_nested_stylish.txt')
RESULT_NESTED_PLAIN = get_path('result_nested_plain.txt')
RESULT_NESTED_JSON = get_path('result_nested_json.json')


def get_correct_result(path_file):
    with open(path_file, 'r') as file:
        result = file.read()
    return result


@pytest.mark.parametrize("first_file, second_file, result_file,format_name", [
    (FILE_FLAT_FIRST_JSON, FILE_FLAT_SECOND_JSON, RESULT_FLAT_STYLISH, STYlISH_FORMAT),
    (FILE_FLAT_FIRST_YML, FILE_FLAT_SECOND_YML, RESULT_FLAT_STYLISH, STYlISH_FORMAT),
    (FILE_FLAT_FIRST_JSON, FILE_FLAT_SECOND_JSON, RESULT_FLAT_PLAIN, PLAIN_FORMAT),
    (FILE_FLAT_FIRST_YML, FILE_FLAT_SECOND_YML, RESULT_FLAT_PLAIN, PLAIN_FORMAT),
    (FILE_FLAT_FIRST_JSON, FILE_FLAT_SECOND_JSON, RESULT_FLAT_JSON, JSON_FORMAT),
    (FILE_FLAT_FIRST_YML, FILE_FLAT_SECOND_YML, RESULT_FLAT_JSON, JSON_FORMAT),
    (FILE_NESTED_FIRST_JSON, FILE_NESTED_SECOND_JSON, RESULT_NESTED_STYLISH, STYlISH_FORMAT),
    (FILE_NESTED_FIRST_YML, FILE_NESTED_SECOND_YML, RESULT_NESTED_STYLISH, STYlISH_FORMAT),
    (FILE_NESTED_FIRST_JSON, FILE_NESTED_SECOND_JSON, RESULT_NESTED_PLAIN, PLAIN_FORMAT),
    (FILE_NESTED_FIRST_YML, FILE_NESTED_SECOND_YML, RESULT_NESTED_PLAIN, PLAIN_FORMAT),
    (FILE_NESTED_FIRST_JSON, FILE_NESTED_SECOND_JSON, RESULT_NESTED_JSON, JSON_FORMAT),
    (FILE_NESTED_FIRST_YML, FILE_NESTED_SECOND_YML, RESULT_NESTED_JSON, JSON_FORMAT)])
def test_gendiff(first_file, second_file, result_file, format_name):
    assert isinstance(generate_diff, typing.Callable)
    assert generate_diff(first_file, second_file, format_name) == get_correct_result(result_file)


