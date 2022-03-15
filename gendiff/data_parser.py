from json import loads
from yaml import safe_load
from gendiff.file import YAML, YML, JSON


def parsing(data, data_format):
    if data_format.upper() == YML or data_format.upper() == YAML:
        return safe_load(data)
    elif data_format.upper() == JSON:
        return loads(data)
    else:
        raise Exception("Format error")
