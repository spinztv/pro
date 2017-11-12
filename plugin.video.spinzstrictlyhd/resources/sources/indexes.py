from BeautifulSoup import BeautifulSoup
from resources.modules import *
from urlparse import parse_qsl
from urllib import urlencode
import urlresolver
import xbmcplugin
import HTMLParser
import xbmcaddon
import urlparse
import requests
import xbmcgui
import urllib
import base64
import time
import json
import xbmc
import sys
import re

_handle = int(sys.argv[1])
addon_id = 'plugin.video.spinzstrictlyhd'
addon = xbmcaddon.Addon(id=addon_id)
query_url = 'http://cyberreel.com/search/%s'
regulate = HTMLParser.HTMLParser()

def RESOLVE(link):
    play_item = xbmcgui.ListItem(path=link)
    play_item.setProperty('IsPlayable','true')
    xbmcplugin.setResolvedUrl(_handle, True, listitem=play_item)

def SEARCH(query):
    links = []
    titles = []
    images = []
    query = urllib.unquote_plus(query)
    query = query.replace(':',' ').replace('-',' ').replace("'",'').replace('  ',' ').replace('  ',' ').lower()
    indicies = ['aHR0cHM6Ly9wYXN0ZWJpbi5jb20vcmF3L2VEclloMWt2',
                'aHR0cHM6Ly9wYXN0ZWJpbi5jb20vcmF3L2hndWN0QWR4',
                'aHR0cHM6Ly9wYXN0ZWJpbi5jb20vcmF3L2dMTlV4a01z']
    f = ''
    for i in indicies:
        try: f += requests.get(base64.b64decode(i), verify=False, timeout=15).text
        except: return zip(titles, images, links)
    f = base64.b64decode(f)
    items = re.compile('<item>(.+?)</item>', re.MULTILINE|re.DOTALL).findall(f)
    
    for item in items:
        try: 
            title = re.compile('<title>(.+?)\s\[').findall(item)[0]
            title = title.replace(':',' ').replace('-',' ').replace('  ',' ').replace(' V2 ',' ').lower().rstrip()
        except: 
            print 'Error parsing title : %s' % title
            continue
        if title != query: continue
        full_title = re.compile('<title>(.+?)</title>').findall(item)[0]
        full_title += ' {indexes}'
        link = re.compile('<link>(.+?)</link>').findall(item)[0]
        links.append(link)
        titles.append(full_title)
        images.append('')
    return zip(titles, images, links)

def router(paramstring):
    params = dict(parse_qsl(sys.argv[2][1:]))
    if params:
        link = params.get('endpoint')
        if link is not None: RESOLVE(link)
        else:
            raise ValueError('Invalid paramstring: {0}!'.format(paramstring))
    else:
        SEARCH(query)     
              
if __name__ == '__main__':
    router(sys.argv[2][1:])
