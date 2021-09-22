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
