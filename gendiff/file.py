YAML = 'YAML'
YML = 'YML'
JSON = 'JSON'


def get_data_format(file):
    try:
        data = open(file)
    except OSError:
        raise Exception(f'Could not open file: {file}')
    if file.upper().endswith(YML) or file.upper().endswith(YAML):
        data_format = YML
    elif file.upper().endswith(JSON):
        data_format = JSON
    else:
        raise Exception("This format is not supported")
    return data, data_format
