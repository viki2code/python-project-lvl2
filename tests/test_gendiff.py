from gendiff import generate_diff


def test_gendiff1():
    file1 = './tests/fixtures/first_file_test1.json'
    file2 = './tests/fixtures/second_file_test1.json'
    file_result = open('./tests/fixtures/result_test1.json')
    str_result = file_result.read()
    assert generate_diff(file1, file2) == str_result
    file_result.close()
