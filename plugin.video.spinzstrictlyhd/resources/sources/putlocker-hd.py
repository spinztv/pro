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
import urllib2
import urllib
import time
import json
import xbmc
import sys
import re

_handle = int(sys.argv[1])
addon_id = 'plugin.video.spinzstrictlyhd'
addon = xbmcaddon.Addon(id=addon_id)
regulate = HTMLParser.HTMLParser()

query_url = 'http://putlocker-hd.online/advanced-search?search_query={}&orderby=&order=&tax_quality%5B%5D=1080p&tax_quality%5B%5D=720p&wpas=1'

def RESOLVE(link):
    try: play_link = urlresolver.HostedMediaFile(link).resolve()
    except: play_link = link
    if 'False' in str(play_link): play_link = link
    
    play_item = xbmcgui.ListItem(path=play_link)
    play_item.setProperty('IsPlayable','true')
    xbmcplugin.setResolvedUrl(_handle, True, listitem=play_item)

def cleanHex(s):
    cleaned = s.replace('&#8211;','-').replace(u'\xa0', u' ').replace(u'\xe9', u'e')
    cleaned = cleaned.replace('&#8217;',"'").replace('&#8216;',"'")
    cleaned = cleaned.replace('&#8230;','...').replace('[&hellip;]','...')
    return cleaned

def SEARCH(query):
    links = []
    titles = []
    images = []
    query = urllib2.unquote(query.replace('&','and').replace('+',' ').replace('%3A','')).lower()
    try: putlockerhd = requests.get(query_url.format(urllib.quote_plus(query)), timeout=15).content
    except: return zip(titles, images, links)
    soup = BeautifulSoup(putlockerhd)
    try:
        results = soup.findAll('div',{'class':'resultado'})
        if results:
            for result in results:
                title = regulate.unescape(cleanHex(result.find('span',{'class':'titulo'}).a.text))[:-5]
                tcheck = title.lower()
                title += ' [COLOR green]HD[/COLOR] {putlocker-hd}'
                image = result.find('div',{'class':'imagen'}).a.img['src']
                if query == tcheck:
                    content_page = result.find('span',{'class':'titulo'}).a['href']
                    link_page = requests.get(content_page).content
                    soup = BeautifulSoup(link_page)
                    host_url = soup.find('div',{'class':'movieplay'}).iframe['src']
                    links.append(host_url)
                    titles.append(title)
                    images.append(image)
    except:
        print '!!! >>> Error in Source 13 <<< !!!'
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
