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
    def get_next_item(items):
        input_pos = 0
        seeking_quote = None
        token = ''
        ignore = False
        while input_pos < len(items):
            current_character = items[input_pos]
            if input_pos == 0:
                if current_character == '"' or current_character == "'":
                    seeking_quote = current_character
            if current_character == '\\':
                ignore = True
            if ignore:
                token += current_character
                input_pos += 1
                continue
            if current_character == ",":
                if not seeking_quote:
                    return token
            token += current_character
            input_pos += 1
        return token if token != "" else None

    match = re.match(r'.*\((\".*\")(,\w*(\".*\"))*\)', input_string)
    if match is not None:
        args = []
        args_string = match.group(1)
        while True:
            next_arg, length = get_next_item(args_string)
            if next_arg is not None:
                args.append(next_arg)
                args_string = args_string[length:]
            else:
                return args
        # TODO implement this- should pull both int and str args from string
        raise NotImplementedError
    return None


def load_object_from_string(input_str):
    # TODO Add validation that it is valid python syntax first
    class_type = get_class_from_string(input_str)
    args = get_arguments_from_string(input_str)
    if args is None:
        return class_type
    return class_type(*args)
