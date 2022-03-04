import os
from gendiff.generate_diff import generate_diff
from gendiff.stylish import stylish


FIXTURES_FOLDER = 'fixtures'


def test_gendiff_json():
    file1 = os.path.join(os.path.dirname(__file__), FIXTURES_FOLDER, 'first_file_test1.json')
    file2 = os.path.join(os.path.dirname(__file__), FIXTURES_FOLDER, 'second_file_test1.json')
    file_result = open(os.path.join(os.path.dirname(__file__), FIXTURES_FOLDER, 'result_test1.json'))
    str_result = file_result.read()
    assert stylish(generate_diff(file1, file2), ' ', 2) == str_result
    file_result.close()


'''def test_gendiff_yaml():
    file1 = os.path.join(os.path.dirname(__file__), FIXTURES_FOLDER, 'first_file_test1.json')
    file2 = os.path.join(os.path.dirname(__file__), FIXTURES_FOLDER, 'second_file_test2.yml')
    file_result = open(os.path.join(os.path.dirname(__file__), FIXTURES_FOLDER, 'result_test2.json'))
    str_result = file_result.read()
    assert stylish(generate_diff(file1, file2), ' ', 2) == str_result
    file_result.close()
'''

def test_nesteed_gendiff_yaml():
    file1 = os.path.join(os.path.dirname(__file__), FIXTURES_FOLDER, 'file_nesteed1.json')
    file2 = os.path.join(os.path.dirname(__file__), FIXTURES_FOLDER, 'file_nesteed2.json')
    file_result = open(os.path.join(os.path.dirname(__file__), FIXTURES_FOLDER, 'result_nesteed.json'))
    str_result = file_result.read()
    assert stylish(generate_diff(file1, file2), ' ', 2) == str_result
    file_result.close()
