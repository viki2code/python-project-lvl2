import os

YAML = 'YAML'
YML = 'YML'
JSON = 'JSON'


def read_file(file_path):
    with open(file_path) as f:
        data = f.read()
    return data


def get_extension(file_path):
    file_extension = os.path.splitext(file_path)[1]
    return file_extension.replace('.', '')
