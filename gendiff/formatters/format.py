from gendiff.formatters.plain import plain
from gendiff.formatters.stylish import stylish

PLAIN_FORMAT = 'PLAIN'
STYlISH_FORMAT = 'STYLISH'


def format_diff(data, format_name):
    if format_name.upper() == STYlISH_FORMAT:
        return stylish(data, ' ', 2)
    elif format_name.upper() == PLAIN_FORMAT:
        return plain(data)
    raise Exception('Invalid format')
