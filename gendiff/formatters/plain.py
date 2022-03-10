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
        for key, value_ in current_value.items():
            if isinstance(value_, dict) \
                    and value_.get('action') != 'unchanged':
                path.append(key)
                if value_.get('action') == 'nested':
                    result_list.append(walk(value_.get('value'), path))
                else:
                    old_value = get_name_value(value_.get('old_value'))
                    value = get_name_value(value_.get('value'))
                    result_list.append(MESSAGE[value_.get('action')].format(
                        path='.'.join(path),
                        old_value=old_value,
                        value=value
                    ))
                path.pop(len(path) - 1)
        return '\n'.join(result_list)

    return walk(data, [])
