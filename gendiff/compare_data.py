from operator import itemgetter
from gendiff.actions import CHANGED, ADDED, DELETED, NESTED, UNCHANGED


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
                    {'action': NESTED,
                     'value': walk(value1[key], value2[key])}
            elif value1[key] == value2[key]:
                result_dict[key] = \
                    {'action': UNCHANGED,
                     'value': value1[key]}
            else:
                result_dict[key] = \
                    {'action': CHANGED,
                     'old_value': value1[key],
                     'value': value2[key]}
        # add deleted element in compare dictionary
        result_dict.update(add_value(DELETED, diff_keys, value1))
        # add added element in compare dictionary
        result_dict.update(add_value(ADDED, add_keys, value2))
        sorted_result_dict = dict(sorted(result_dict.items(),
                                         key=itemgetter(0)))
        return sorted_result_dict

    return walk(data1, data2)
