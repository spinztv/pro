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
import time
import json
import xbmc
import sys
import re

_handle = int(sys.argv[1])
addon_id = 'plugin.video.spinzstrictlyhd'
addon = xbmcaddon.Addon(id=addon_id)

query_url = 'http://movie4k.is/?s=%s'

def RESOLVE(link):
    try: play_link = urlresolver.HostedMediaFile(link).resolve()
    except: play_link = link
    if 'False' in str(play_link): play_link = link
    
    play_item = xbmcgui.ListItem(path=play_link)
    play_item.setProperty('IsPlayable','true')
    xbmcplugin.setResolvedUrl(_handle, True, listitem=play_item)

def SEARCH(query):
    links = []
    titles = []
    images = []
    try: movie4k = requests.get(query_url % query, timeout=15).content
    except: return zip(titles, images, links)
    soup = BeautifulSoup(movie4k)
    try:
        results = soup.findAll('div',{'class':'item'})
        if results:
            for result in results:
                title = result.find('span',{'class':'tt'}).text
                if not result.find('span',{'class':'calidad2'}): continue
                title += ' [COLOR green]%s[/COLOR] {movie4k}' % result.find('span',{'class':'calidad2'}).text
                image = result.find('div',{'class':'image'}).img['src']
                q = query.replace('+',' ').lower()
                if q in title.lower():
                    content_page = result.a['href']
                    link_page = requests.get(content_page).content
                    soup = BeautifulSoup(link_page)
                    movie_tags = soup.findAll('div',{'class':'movieplay'})
                    for tag in movie_tags:
                        links.append(tag.iframe['data-lazy-src'])
                        titles.append(title)
                        images.append(image)
    except:
        print '!!! >>> Error in Source 9 <<< !!!'
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
