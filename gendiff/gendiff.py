from gendiff.data_parser import parsing
from gendiff.file import read_file, get_extension
from gendiff.formatters.format import format_diff
from gendiff.compare_data import compare_data
from gendiff.formatters.format import STYlISH_FORMAT


def generate_diff(file_path1, file_path2, format_name=STYlISH_FORMAT):
    data1 = parsing(read_file(file_path1), get_extension(file_path1))
    data2 = parsing(read_file(file_path2), get_extension(file_path2))
    diff = compare_data(data1, data2)
    return format_diff(diff, format_name)
