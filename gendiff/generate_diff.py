from gendiff.data_parser import parsing


def get_str(value):
    if isinstance(value, bool):
        return str(value).lower()
    else:
        return str(value)


def generate_diff(file_path1, file_path2):
    data1 = parsing(open(file_path1))
    data2 = parsing(open(file_path2))
    keys = sorted(data1.keys() | data2.keys())
    result = '{\n'
    for key in keys:
        if key not in data1:
            result += f'  + {key}: {get_str(data2[key])}\n'
        elif key not in data2:
            result += f'  - {key}: {get_str(data1[key])}\n'
        elif data1[key] != data2[key]:
            result += f'  - {key}: {get_str(data1[key])}\n'
            result += f'  + {key}: {get_str(data2[key])}\n'
        else:
            result += f'    {key}: {get_str(data1[key])}\n'
    result += '}'
    return result
