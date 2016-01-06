#!/usr/bin/env python

"""
flask-extensions.manage
~~~~~~~~~~~~~~~~~~~~~~~

Application setup-and-teardown.

:copyright: (c) 2016 Michael Hoyt. <@pr0xmeh>
:license: MIT
"""

import os
import sys

import requests
from bs4 import BeautifulSoup


def download(url, file_path):
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (compatible)'
        }

        r = requests.get(url, headers=headers)
        html = r.content

        with open(file_path, 'wb+') as f:
            f.write(html)

        return file_path
    except:
        print("Unexpected error: %s" % sys.exc_info()[0])
        return False


def scrape_github(url='mitsuhiko/flask'):
    github_url = 'http://github.com/{}'.format(url)

    f = download(github_url, 'cache.html')
    html = open(f).read()
    soup = BeautifulSoup(html, 'html5lib')

    stars = 0
    forks = 0

    try:
        social_soup = soup.find_all('a', {'class': 'social-count'})
    except:
        return (0,0)

    for social_obj in social_soup:
        href = social_obj['href']
        n = int(social_obj.text.strip().replace(' ', '').replace(',','')) or 0
        if href == '/{}/stargazers'.format(url):
            stars = n
        if href == '/{}/network'.format(url):
            forks = n

    return (stars, forks)


def main():
    scrape_github()


if __name__ == '__main__':
    main()
