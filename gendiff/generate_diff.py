from gendiff.data_parser import parsing
from gendiff.file import get_data, get_extension
from gendiff.formatters.format import format_diff
from gendiff.compare_data import compare_data


def generate_diff(file_path1, file_path2, format_name):
    data1 = parsing(get_data(file_path1), get_extension(file_path1))
    data2 = parsing(get_data(file_path2), get_extension(file_path2))
    diff = compare_data(data1, data2)
    result = format_diff(diff, format_name)
    return result
