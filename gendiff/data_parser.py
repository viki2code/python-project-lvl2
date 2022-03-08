from json import load
from yaml import safe_load, parser


def get_file_type(file_name):
    if file_name.endswith('.yaml') or file_name.endswith('.yml'):
        return 'YML'
    elif file_name.endswith('.json'):
        return 'JSON'


def parsing(data, file_type):
    try:
        if file_type.upper() == 'YML' or file_type.upper() == 'YML':
            return safe_load(data)
        elif file_type.upper() == 'JSON':
            return load(data)
    except parser.ParserError as exc:
        return print("Error in configuration file:", exc)
