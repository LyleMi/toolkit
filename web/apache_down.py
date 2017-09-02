# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup
import os
import urllib

url = '' # init

def download(url, uri):

    r = requests.get(url+uri)
    soup = BeautifulSoup(r.text, "html.parser")
    links = soup.find_all('a')
    for i in links:
        if i.text == '../':
            continue

        name = i['href']
        print name

        if name == '/':
            continue

        if name[-1] == '/':
            download(url, name)
            if not os.path.exists(name):
                os.makedirs(name)
        else:
            # file
            try:
                filename = name.split('/')[-1]
                # print 'filename  ',filename
                if not os.path.exists('./' + uri + filename):
                    urllib.urlretrieve(url + name, './' + uri + filename)
                    print 'download->', url + name
                else:
                    print 'exists', url + name
            except:
                print url + name, 'failed!'

# def download
if __name__ == '__main__':
    download(url, '')
