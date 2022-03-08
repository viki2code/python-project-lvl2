from gendiff.data_parser import parsing, get_file_type
from gendiff.formatters.format import format_diff
from operator import itemgetter


def add_value(action, keys, value):
    result = {}
    for key in keys:
        result[key] = {'action': action, 'value': value[key]}
    return result


def compare_data(data1, data2):
    def walk(value1, value2):
        common_keys = value1.keys() & value2.keys()
        diff_keys = value1.keys() - value2.keys()
        add_keys = value2.keys() - value1.keys()
        result_dict = {}
        for key in common_keys:
            if isinstance(value1[key], dict) and isinstance(value2[key], dict):
                result_dict[key] = \
                    {'action': 'nested',
                     'value': walk(value1[key], value2[key])}
            elif value1[key] == value2[key]:
                result_dict[key] = \
                    {'action': 'unchanged',
                     'value': value1[key]}
            else:
                result_dict[key] = \
                    {'action': 'changed',
                     'old_value': value1[key],
                     'value': value2[key]}
        # add deleted element in compare dictionary
        result_dict.update(add_value('deleted', diff_keys, value1))
        # add added element in compare dictionary
        result_dict.update(add_value('added', add_keys, value2))
        sorted_result_dict = dict(sorted(result_dict.items(),
                                         key=itemgetter(0)))
        return sorted_result_dict

    return walk(data1, data2)


def generate_diff(file_path1, file_path2, format_name):
    data1 = parsing(open(file_path1), get_file_type(file_path1))
    data2 = parsing(open(file_path2), get_file_type(file_path2))
    diff = compare_data(data1, data2)
    return format_diff(diff, format_name)
