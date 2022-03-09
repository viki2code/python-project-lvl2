import itertools
import json

ACTION_SIGN = {'changed': ['-', '+'],
               'unchanged': ' ',
               'added': '+',
               'deleted': '-',
               'nested': ' '}


def get_str(value):
    if isinstance(value, str):
        return value
    else:
        return json.dumps(value)


def stylish(data, replacer=' ', spaces_count=1):
    def walk(current_value, depth):
        if not isinstance(current_value, dict):
            return get_str(current_value)
        deep_indent_size = depth * spaces_count
        deep_indent = replacer * deep_indent_size
        current_replacer = replacer * (deep_indent_size - spaces_count)
        lines = []
        for key, value_ in current_value.items():
            # if only copy dictionary
            is_value_dict = isinstance(value_, dict)
            if (is_value_dict and value_.get('action') is None) \
                    or not is_value_dict:
                sign = ACTION_SIGN['unchanged']
                value = value_
            else:
                sign = ACTION_SIGN[value_.get('action')]
                if isinstance(sign, list):
                    old_sign = sign[0]
                    old_value = value_['old_value']
                    lines.append(f'{deep_indent}{old_sign}{replacer}{key}: '
                                 f'{walk(old_value, depth + 2)}')
                    sign = sign[1]
                value = value_['value']
            lines.append(f'{deep_indent}{sign}{replacer}{key}: '
                         f'{walk(value, depth + 2)}')
        result = itertools.chain("{", lines, [current_replacer + "}"])
        return '\n'.join(result)

    return walk(data, 1)
