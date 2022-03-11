from gendiff.formatters.plain_format import plain_format
from gendiff.formatters.stylish_format import stylish_format
from gendiff.formatters.json_format import json_format

PLAIN_FORMAT = 'PLAIN'
STYlISH_FORMAT = 'STYLISH'
JSON_FORMAT = 'JSON'


def format_diff(data, format_name):
    if format_name.upper() == STYlISH_FORMAT:
        return stylish_format(data, ' ', 2)
    elif format_name.upper() == PLAIN_FORMAT:
        return plain_format(data)
    elif format_name.upper() == JSON_FORMAT:
        return json_format(data)
    raise Exception('Invalid format')
