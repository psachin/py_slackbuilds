#!/usr/bin/env python

import urllib
import BeautifulSoup
import requests

from platform import machine


def download_tarball(url):
    url_data = requests.get(url)
    soup = BeautifulSoup.BeautifulSoup(url_data.text)
    tarballs = []
    for link in soup.findAll('a'):
        if link.get('href').endswith('tar.gz') or link.get('href').endswith('tar.bz2'):
            print link.get('href')
            tarballs.append(link.get('href'))
            user_reply = raw_input("Do you want to download this tarball? (y/n): ")
            if user_reply == 'y':
                urllib.urlretrieve(link.get('href'),
                                   link.get('href').split('/')[-1])
    return tarballs


if __name__ == '__main__':
    url = raw_input("Please enter the url of library: ")
    download_tarball(url)
