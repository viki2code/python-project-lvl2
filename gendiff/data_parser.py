from json import load
from yaml import safe_load


def get_file_type(file_name):
    if file_name.endswith('.yaml') or file_name.endswith('.yml'):
        return 'YML'
    elif file_name.endswith('.json'):
        return 'JSON'


def parsing(data, file_type):
    if file_type.upper() == 'YML' or file_type.upper() == 'YAML':
        return safe_load(data)
    elif file_type.upper() == 'JSON':
        return load(data)
    else:
        raise Exception("Error in configuration file")
