import json

MESSAGE = {'changed': "Property '{path}' was updated. "
                      "From {old_value} to {value}",
           'added': "Property '{path}' was added with value: {value}",
           'deleted': "Property '{path}' was removed"}


def get_name_value(value):
    if isinstance(value, dict):
        return '[complex value]'
    return json.dumps(value).replace('"', "'")


def plain(data):
    def walk(current_value, path):
        result_list = []
        for key, value_dict in current_value.items():
            if isinstance(value_dict, dict) \
                    and value_dict.get('action') != 'unchanged':
                path.append(key)
                if value_dict.get('action') == 'nested':
                    result_list.append(walk(value_dict.get('value'), path))
                else:
                    old_value = get_name_value(value_dict.get('old_value'))
                    value = get_name_value(value_dict.get('value'))
                    result_list.append(MESSAGE[value_dict.get('action')].format(
                        path='.'.join(path),
                        old_value=old_value,
                        value=value
                    ))
                path.pop(len(path) - 1)
        return '\n'.join(result_list)

    return walk(data, [])
