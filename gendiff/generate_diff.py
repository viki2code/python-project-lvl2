from gendiff.data_parser import parsing
from gendiff.file import get_data_format
from gendiff.formatters.format import format_diff
from gendiff.compare_data import compare_data


def generate_diff(file_path1, file_path2, format_name):
    data_file1, format_file1 = get_data_format(file_path1)
    data1 = parsing(data_file1, format_file1)
    data_file2, format_file2 = get_data_format(file_path2)
    data2 = parsing(data_file2, format_file2)
    diff = compare_data(data1, data2)
    return format_diff(diff, format_name)
