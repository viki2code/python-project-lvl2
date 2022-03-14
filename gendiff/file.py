import os

YAML = 'YAML'
YML = 'YML'
JSON = 'JSON'


def get_data(file_path):
    return open(file_path)


def get_extension(file_path):
    file_extension = os.path.splitext(file_path)[1]
    return file_extension.replace('.', '')
