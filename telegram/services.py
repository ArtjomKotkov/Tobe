
def fix_built_ins(response):
    # Fix built in names like from, changing them to _from.
    built_ins = ['from', 'type']
    if response:
        for key in built_ins:
            if key in response:
                response[f'_{key}'] = response.pop(key)
    return response