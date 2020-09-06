from collections.abc import Iterable


def propagate_value(**values):
    """Parse values from response and push to class instance witch method was decorated.

    Parameters
    ----------
        All values must be provided as key=value, where key - method value, value - bot attr.

    """

    def first_wrapper(func):
        def second_wrapper(*args, **kwargs):

            # Get self argument.
            self = args[0]
            result = func(*args, **kwargs)

            # Add additional fields in values which need to pass in bot [from execute].
            if 'propagate_fields' in kwargs and isinstance(kwargs['propagate_fields'], dict):
                for from_method, to_bot in kwargs['propagate_fields'].items():
                    values.update({from_method: to_bot})

            if isinstance(result, list):
                # If response are iterable push last found value.
                for response in result:
                    propogate_block(values, response, self)
            else:
                propogate_block(values, result, self)

            return [item[0] for item in result] if isinstance(result, list) else result[0]

        return second_wrapper

    return first_wrapper

def propogate_block(values, response, self):
    response, propagate_field_from_method = response[0], response[1]

    # Support for propagating field from method.
    if propagate_field_from_method:
        values.update(propagate_field_from_method)

    propagate_values(values=values, response=response, self_instance=self)

def propagate_values(values, response, self_instance):
    """Shortcut function."""
    for key, value in values.items():

        temp_value = response
        error = False

        if isinstance(temp_value, Iterable):
            for inner_response in temp_value:
                temp_value, error = get_inner_values(inner_response, key)
        else:
            temp_value, error = get_inner_values(temp_value, key)

        if error:
            continue

        self_instance.propagated_values.update({
            value: temp_value
        })


def get_inner_values(response, key_str):
    keys = key_str.split('.')
    answer = response
    try:
        for key in keys:
            answer = answer.__getattribute__(key)
    except AttributeError:
        return None, True
    return answer, False