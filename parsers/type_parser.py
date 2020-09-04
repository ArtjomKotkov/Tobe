import httplib2
import pprint

from bs4 import BeautifulSoup


def types_parser(url=None):
    url = 'https://core.telegram.org/bots/api#available-types'

    http = httplib2.Http()
    resp, content = http.request(uri=url)

    pprint.pprint(resp)

    if resp['status'] != '200':
        print(f'Response status {resp["status"]} try another url.')
        url = input()
        return types_parser(url=url)

    if resp['content-type'] != 'text/html; charset=utf-8':
        print(f'Response content-type {resp["content-type"]} try another url.')
        url = input()
        return types_parser(url=url)

    soup = BeautifulSoup(content, 'html.parser')



if __name__ == '__main__':
    types_parser()