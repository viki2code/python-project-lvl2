import json

MESSAGE = {'changed': "Property '{path}' was updated. "
                      "From {old_value} to {value}",
           'added': "Property '{path}' was added with value: {value}",
           'deleted': "Property '{path}' was removed"}


def get_name_value(value):
    if isinstance(value, dict):
        return '[complex value]'
    return json.dumps(value).replace('"', "'")


def plain_format(data):
    def walk(current_value, path):
        result_list = []
        for key, value in current_value.items():
            if isinstance(value, dict) \
                    and value.get('action') != 'unchanged':
                path.append(key)
                if value.get('action') == 'nested':
                    result_list.append(walk(value.get('value'), path))
                else:
                    old_value = get_name_value(value.get('old_value'))
                    new_value = get_name_value(value.get('value'))
                    result_list.append(MESSAGE[value.get('action')].format(
                        path='.'.join(path),
                        old_value=old_value,
                        value=new_value
                    ))
                path.pop(len(path) - 1)
        return '\n'.join(result_list)

    return walk(data, [])
