import itertools
import json


def get_str(value):
    if isinstance(value, str):
        return value
    else:
        return json.dumps(value)


def stylish(value, replacer=' ', spaces_count=1):

    def walk(current_value, depth):
        if not isinstance(current_value, dict):
            return get_str(current_value)
        deep_indent_size = depth * spaces_count
        deep_indent = replacer * deep_indent_size
        current_replacer = replacer * (deep_indent_size - spaces_count)
        lines = []
        for key, val in current_value.items():
            if isinstance(key, tuple):
                key_str = replacer.join(key)
            else:
                key_str = f' {replacer}{key}'

            lines.append(f'{deep_indent}{key_str}: {walk(val, depth + 2)}')
        result = itertools.chain("{", lines, [current_replacer + "}"])
        return '\n'.join(result)
    return walk(value, 1)
