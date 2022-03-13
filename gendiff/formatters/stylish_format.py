import itertools
import json
from gendiff.actions import CHANGED, ADDED, DELETED, NESTED, UNCHANGED


ACTION_SIGN = {CHANGED: ['-', '+'],
               UNCHANGED: ' ',
               ADDED: '+',
               DELETED: '-',
               NESTED: ' '}


def get_str(value):
    if isinstance(value, str):
        return value
    else:
        return json.dumps(value)


def stylish_format(data, replacer=' ', spaces_count=1):
    def walk(current_value, depth):
        if not isinstance(current_value, dict):
            return get_str(current_value)
        deep_indent_size = depth * spaces_count
        deep_indent = replacer * deep_indent_size
        current_replacer = replacer * (deep_indent_size - spaces_count)
        lines = []
        for key, value in current_value.items():
            # if only copy dictionary
            is_value_dict = isinstance(value, dict)
            if (is_value_dict and value.get('action') is None) \
                    or not is_value_dict:
                sign = ACTION_SIGN['unchanged']
                new_value = value
            else:
                sign = ACTION_SIGN[value.get('action')]
                if isinstance(sign, list):
                    old_sign = sign[0]
                    old_value = value['old_value']
                    lines.append(f'{deep_indent}{old_sign}{replacer}{key}: '
                                 f'{walk(old_value, depth + 2)}')
                    sign = sign[1]
                new_value = value['value']
            lines.append(f'{deep_indent}{sign}{replacer}{key}: '
                         f'{walk(new_value, depth + 2)}')
        result = itertools.chain("{", lines, [current_replacer + "}"])
        return '\n'.join(result)

    return walk(data, 1)
