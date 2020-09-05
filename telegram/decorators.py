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

            if isinstance(result, Iterable):
                # If response are iterable push last found value.
                for key, value in values.items():
                    temp_value = None

                    for response in result:
                        try:
                            temp_value = response.__getattribute__(key)
                        except AttributeError:
                            pass
                    if temp_value:
                        self.propagated_values.update({
                            value: temp_value
                        })

            else:
                for key, value in values.items():
                    try:
                        self.propagated_values.update({
                            value: result.__getattribute__(key)
                        })
                    except AttributeError:
                        pass

            return result
        return second_wrapper
    return first_wrapper