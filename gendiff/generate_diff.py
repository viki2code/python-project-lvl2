import json


def generate_diff(file_path1, file_path2):
    data1 = json.load(open(file_path1))
    data2 = json.load(open(file_path2))
    keys = sorted(data1.keys() | data2.keys())
    result = '{\n  '
    for key in keys:
        if key not in data1:
            result += f'+ {key}: {json.dumps(data2[key])}\n  '
        elif key not in data2:
            result += f'- {key}:{json.dumps(data1[key])}\n  '
        elif data1[key] != data2[key]:
            result += f'- {key}:{json.dumps(data1[key])}\n  '
            result += f'+ {key}:{json.dumps(data2[key])}\n  '
        else:
            result += f'  {key}:{json.dumps(data1[key])}\n  '
    result += '\r}'
    return result
