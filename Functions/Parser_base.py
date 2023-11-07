import requests as rs
from bs4 import BeautifulSoup
from pprint import *


def get_info_html(url, soft):
    resp = rs.get(url).content
    html = BeautifulSoup(resp, 'html.parser')
    rest = html.find(class_=soft)
    pprint(rest.text)
    print(rest.attrs)


def get_info_json(url, info):
    result = []
    n=1
    link = rs.get(url).json()
    count = link['count']
    for j in range(count):
        try:
            link = rs.get(f'{url}?page={n}').json()
            n += 1
            for i in range(10):
                dmtr = link["results"][i][info]
                if dmtr == "unknown":
                    pass
                else:
                    result.append(int(dmtr))
        except ValueError:
            pass
        except KeyError:
            break
        except IndexError:
            break
    return max(result)

get_info_html('https://habr.com/ru/sandbox/149730/',
              'article-formatted-body article-formatted-body article-formatted-body_version-2')
