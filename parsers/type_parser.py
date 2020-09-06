import httplib2

from bs4 import BeautifulSoup


def types_parser(url=None):
    if not url:
        url = 'https://core.telegram.org/bots/api#available-types'

    http = httplib2.Http()
    resp, content = http.request(uri=url)

    if resp['status'] != '200':
        print(f'Response status {resp["status"]} try another url.')
        url = input()
        return types_parser(url=url)

    if resp['content-type'] != 'text/html; charset=utf-8':
        print(f'Response content-type {resp["content-type"]} try another url.')
        url = input()
        return types_parser(url=url)

    soup = BeautifulSoup(content, 'html.parser')

    #
    def top_el(tag):
        #return 'Available types' in tag.descendants and tag.name == 'h3'
        return 'Stickers' in tag.descendants and tag.name == 'h3'

    def bottom_el(tag):
        #return 'Available methods' in tag.descendants and tag.name == 'h3'
        return 'Inline mode' in tag.descendants and tag.name == 'h3'


    top_element = soup.find(top_el)
    bottom_element = soup.find(bottom_el)

    c = top_element.next_sibling

    classes_list = []

    while c != bottom_element:
        if c.name == 'h4':
            classes_list.append(parse_block(c))
        c = c.next_sibling

    print(', '.join(classes_list))

def parse_block(tag):
    """Read block of type."""
    first = True # Indicate that it's first iteration.
    block_info = {
        'name': None,
        'description': None,
        'table_info': None, # tag instance.
        'blockquote': None
    }
    while tag.name not in ['h3', 'h4'] or first == True:
        first = False
        if tag.name == 'h4':
            block_info['name'] = get_raw_string(tag)
        elif tag.name == 'p':
            block_info['description'] = get_raw_string(tag)
        elif tag.name == 'blockquote':
            block_info['blockquote'] = get_raw_string(tag.p)
        elif tag.name == 'table':
            block_info['table_info'] = tag
        tag = tag.next_sibling
    create_type(block_info)
    return block_info['name']

def create_type(block):
    """

    :param block:
    :return:
    """
    try:
        block['table_info'] = parse_table(block['table_info'])
    except AttributeError:
        return

    with open(f'parsed_data/types.py', 'a') as file:
        class_name = block["name"]
        docstring = f'{block["description"]}\n'+create_doc_string_args(block["table_info"])
        pattern = f'class {class_name}(ResponseBaseType):\n' \
                  f'\t"""{docstring}\n\t"""\n' \
                  f'\tdef __init__(self, {create_string_args(block["table_info"])}):\n' \
                  f'\t\tsuper().__init__()\n' \
                  f'{create_init_args(block["table_info"])}\n\n\n'
        file.write(pattern)


def create_doc_string_args(args:list):
    args_strings = ['\t', 'Parameters', '----------']
    for arg in args:
        args_strings.append(f'{arg[0]} : {arg[1]}{", optional" if arg[2] and "Optional. " in arg[2] else ""}')
        if arg[2]:
            args_strings.append(f'\t {arg[2].replace("Optional. ", "")}')
    return '\n\t'.join(args_strings)

def create_string_args(args:list):
    args_strings = []
    for num, arg in enumerate(args):
        arg = arg[0] if arg[2] and not "Optional. " in arg[2] else f'{arg[0]}=None'
        args_strings.append(arg if num == 0 else '\t\t\t'+arg)
    return ',\n'.join(args_strings)

def create_init_args(args:list):
    args_strings = []
    for num, arg in enumerate(args):
        args_strings.append(f'self.{arg[0]}={arg[0]}' if num != 0 else f'\t\tself.{arg[0]}={arg[0]}')
    return '\n\t\t'.join(args_strings)

def parse_table(table):
    """Parse table, return list of parsed rows."""
    hash_list = []
    for tr in table.tbody.contents:

        if tr == '\n':
            continue
        tr = BeautifulSoup(tr.encode('utf-8'), 'html.parser')
        row = []
        for td in tr.find_all('td'):
            if len(td.contents) == 1:
                row.append(td.string)
            else:
                row.append(get_raw_string(td))

        hash_list.append(row)
    return hash_list

def get_raw_string(tag):
    temp_string = ''
    for elem in tag.descendants:
        if not elem.name:
            temp_string += elem.string
    return temp_string

if __name__ == '__main__':
    types_parser()

# python parsers\type_parser.py


