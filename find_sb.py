#!/usr/bin/python
# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup

index = 'http://www.uuhw.cn/'


def get_index(index):
    r = requests.get(index)
    with open('./index.html', 'w+') as f:
        f.write(r.content.decode('gbk').encode('utf-8'))
    return r.content


def get_url_first(something):
    soup = BeautifulSoup(get_index(index), 'lxml')
    for div in soup.find_all('div'):
        if div.get('id') == 'nv':
            for li in div.ul:
                if li.get('id') == 'mn_Ned10':
                    print li.a.get('href')
                    return li.a.get('href')
            break
    return None


def get_html_first():
    r = requests.get(get_url_first('...'))
    with open('./huodong.html', 'w+') as f:
        f.write(r.content.decode('gbk').encode('utf-8'))
    return r.status_code


if __name__ == '__main__':
    # get_url_first('说走就走')
    print get_html_first()
