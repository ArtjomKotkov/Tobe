import httplib2
import pprint

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

    def top_el(tag):
        return 'Available types' in tag.descendants and tag.name == 'h3'

    def bottom_el(tag):
        return 'Available methods' in tag.descendants and tag.name == 'h3'

    top_element = soup.find(top_el)
    bottom_element = soup.find(bottom_el)


    c = top_element.next_sibling
    print(c.name)

    while c.name not in ('h4', 'p', 'table'):
        c = c.next_sibling

    pprint.pprint(c)

if __name__ == '__main__':
    types_parser()

# python parsers\type_parser.py


