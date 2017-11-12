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

query_url = 'http://www.filmxy.cc/category/720p-1080p/?s=%s'
query_url2 = 'http://www.filmxy.cc/tag/720p-1080p-movies/?s=%s'

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
    try: filmxy = requests.get(query_url % query, timeout=15).content
    except: return zip(titles, images, links)
    soup = BeautifulSoup(filmxy)
    try:
        results = soup.findAll('div',{'class':'single-post'})
        if results:
            for result in results:
                title = result.find('div',{'class':'post-title'}).text
                title = title[:title.find('(')]
                image = result.find('img')['src']
                q = query.replace('+',' ').lower()
                if q in title.lower():
                    content_page = result.div.a['href']
                    link_page = requests.get(content_page).content
                    soup = BeautifulSoup(link_page)
                    try:
                        link = soup.find('div',{'class':'video-section'}).iframe['src']
                    except: continue
                    if 'vidme.cc' in link:
                        vidme = requests.get(link).content
                        soup = BeautifulSoup(vidme)
                        server_tags = soup.findAll('a',{'class':'player-button'})
                        servers = [BeautifulSoup(urllib.unquote(server['data-server']).replace('+',' ')).iframe['src'] for server in server_tags]
                        for server in servers:
                            links.append(server)
                            if '720' in server: quality = '[COLOR green]720p[/COLOR]'
                            if '1080' in server: quality = '[COLOR green]1080p[/COLOR]'
                            titles.append('%s %s {filmxy}' % (title, quality))
                            images.append(image)
                    else:
                        links.append(link)
                        if '720' in server: quality = '[COLOR green]720p[/COLOR]'
                        if '1080' in server: quality = '[COLOR green]1080p[/COLOR]'
                        titles.append('%s %s {filmxy}' % (title, quality))
                        images.append(image)
    except:
        print '!!! >>> Error in Source 4 <<< !!!'
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
