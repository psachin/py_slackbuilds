#!/usr/bin/env python

import re
import urllib
import BeautifulSoup
import requests

from platform import machine
tarballs = []

def prepare_tarball_list(url):
    url_data = requests.get(url)
    soup = BeautifulSoup.BeautifulSoup(url_data.text)
    global tarballs
    # Flush any previous values
    tarballs = []
    for link in soup.findAll('a'):
        if link.get('href').endswith('tar.gz') or link.get('href').endswith('tar.bz2'):
            tarballs.append(link.get('href'))
    return tarballs

def download_slackbuild_src():
    print "Downloading SlackBuild: {}".format(tarballs[-1])
    # Source comes last in the list
    urllib.urlretrieve(tarballs[-1], tarballs[-1].split('/')[-1])
    # remove Slackbuild source from the list
    tarballs.pop()

def download_package_src_64bit():
    regex = re.compile(".*(" + machine() + ").*")
    for package in [m.group(0) for l in tarballs for m in [regex.search(l)] if m]:
        print "Downloading {}".format(package)
        urllib.urlretrieve(package, package.split('/')[-1])

def download_package_src():
    for package in tarballs:
        print "Downloading {}".format(package)
        urllib.urlretrieve(package, package[-1].split('/')[-1])

def download_src(url):
    prepare_tarball_list(url)
    download_slackbuild_src()
    if machine() == 'x86_64':
        download_package_src_64bit()
    else:
        download_package_src()

if __name__ == '__main__':
    url = raw_input("Enter url: ")
    download_src(url)
