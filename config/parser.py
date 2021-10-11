import importlib


def get_class_from_string(input_string):
    try:
        class_path = input_string.split('(')[0]
        module_path, class_name = class_path.rsplit('.', 1)
        module = importlib.import_module(module_path)
        return getattr(module, class_name)
    except AttributeError:
        raise ImportError


def process_item(item):
    if item.strip('"') != item:
        return item.strip('"')
    if item.strip("'") != item:
        return item.strip("'")
    return int(item)


def get_arguments_from_string(input_string):
    all_args = input_string.split('(')
    if len(all_args) == 1:
        return None
    all_args = all_args[1].strip(')')
    items = [process_item(item.strip()) for item in all_args.split(',')]
    return items if len(items) > 0 else None


def load_object_from_string(input_str):
    # TODO Add validation that it is valid python syntax first
    class_type = get_class_from_string(input_str)
    args = get_arguments_from_string(input_str)
    if args is None:
        return class_type
    return class_type(*tuple(args))


def expand_dict_types(input_dict):
    return {key: expand_item_type(value) for key, value in input_dict.items()}


def expand_list_types(input_list):
    return [expand_item_type(item) for item in input_list]


def expand_item_type(input_item):
    if type(input_item) == list:
        return expand_list_types(input_item)
    elif type(input_item) == dict:
        return expand_dict_types(input_item)
    try:
        item = load_object_from_string(input_item)
        return item
    except Exception:
        return input_item


def expand_config_types(input_obj):
    return expand_item_type(input_obj)