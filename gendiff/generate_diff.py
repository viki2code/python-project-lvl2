from gendiff.data_parser import parsing
from operator import itemgetter


def add_value(sign, keys, value):
    result = {}
    for key in keys:
        result.update({(sign, key): value[key]})
    return result


def get_file_type(file_name):
    if file_name.endswith('.yaml') or file_name.endswith('.yml'):
        return 'yml'
    elif file_name.endswith('.json'):
        return 'json'


def generate_diff(file_path1, file_path2):
    data1 = parsing(open(file_path1), get_file_type(file_path1))
    data2 = parsing(open(file_path2), get_file_type(file_path2))

    def walk(value1, value2):
        common_keys = value1.keys() & value2.keys()
        diff_keys = value1.keys() - value2.keys()
        add_keys = value2.keys() - value1.keys()
        result_dict = {}
        for key in common_keys:
            if isinstance(value1[key], dict) and isinstance(value2[key], dict):
                result_dict[(' ', key)] = walk(value1[key], value2[key])
            elif value1[key] == value2[key]:
                result_dict.update({(' ', key): value1[key]})
            else:
                result_dict.update({('-', key): value1[key]})
                result_dict.update({('+', key): value2[key]})
        diff_dict = add_value('-', diff_keys, value1)
        add_dict = add_value('+', add_keys, value2)
        result_dict.update(diff_dict)
        result_dict.update(add_dict)
        sorted_key = sorted(result_dict.keys(), key=itemgetter(1))
        sorted_result_dict = {}
        for i in sorted_key:
            sorted_result_dict[i] = result_dict[i]
        return sorted_result_dict
    return walk(data1, data2)
