import importlib
import re


def get_class_from_string(input_string):
    try:
        class_path = input_string.split('(')[0]
        module_path, class_name = class_path.rsplit('.', 1)
        module = importlib.import_module(module_path)
        return getattr(module, class_name)
    except AttributeError:
        raise ImportError


def get_arguments_from_string(input_string):
    def process_item(item):
        # TODO Add kwarg parsing here
        if item.strip('"') != item:
            return item.strip('"')
        if item.strip("'") != item:
            return item.strip("'")
        return int(item)
    all_args = input_string.split('(')
    if len(all_args) == 1:
        return None
    all_args = all_args[1].strip(')')
    if all_args == '':
        return []
    # TODO Get kwargs from `process_item` and add them to call
    items = [process_item(item.strip()) for item in all_args.split(',')]
    return items if len(items) > 0 else None


def load_object_from_string(input_str):
    # TODO Add validation that it is valid python syntax first
    class_type = get_class_from_string(input_str)
    args = get_arguments_from_string(input_str)
    if args is None:
        return class_type
    return class_type(*tuple(args))


def expand_item_type(input_item):
    def expand_dict_types(input_dict):
        return {key: expand_item_type(value) for key, value in input_dict.items()}

    def expand_list_types(input_list):
        return [expand_item_type(item) for item in input_list]

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


def is_address_string_expanded(input_str):
    return not re.match(r'.*\[\d+-\d+\].*', input_str)


def expand_address_string(input_str):
    if is_address_string_expanded(input_str):
        return input_str
    left_pieces = input_str.split('[')
    left_pieces = [left_pieces[0], "[".join(left_pieces[1:])]
    before = left_pieces[0]
    right_pieces = left_pieces[1].split(']')
    right_pieces = [right_pieces[0], "]".join(right_pieces[1:])]
    range_spec = right_pieces[0]
    after = right_pieces[1]
    start, end = range_spec.split('-')
    new_addresses = [
        before + str(i) + after for i in range(int(start), int(end) + 1)
    ]
    return [expand_address_string(addr) for addr in new_addresses]


def expand_address_glob(addr_glob):
    return flatten_multidimensional_arr(expand_address_string(addr_glob))


def flatten_multidimensional_arr(input_arr):
    return_list = []
    for item in input_arr:
        if type(item) == list:
            return_list += flatten_multidimensional_arr(item)
        else:
            return_list.append(item)
    return return_list
