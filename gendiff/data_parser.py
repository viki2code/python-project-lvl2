from json import load
from yaml import safe_load, parser


def parsing(data, file_type):
    try:
        if file_type == 'yml':
            return safe_load(data)
        elif file_type == 'json':
            return load(data)
    except parser.ParserError as exc:
        return print("Error in configuration file:", exc)
