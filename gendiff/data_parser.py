from json import load
from yaml import safe_load as load, parser


def parsing(data):
    try:
        parse = load(data)
        return parse
    except parser.ParserError as exc:
        return print("Error in configuration file:", exc)
