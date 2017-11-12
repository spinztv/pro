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
query_url = 'http://www.onlinehdwatch.com/?s=%s'
regulate = HTMLParser.HTMLParser()

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
    try: onlinehdwatch = requests.get(query_url % query.replace('%3A',''), timeout=15).content
    except: return zip(titles, images, links)
    soup = BeautifulSoup(onlinehdwatch)
    try:
        results = soup.findAll('div',{'class':'item'})
        if results:
            for result in results:
                title = regulate.unescape(cleanHex(result.find('span',{'class':'tt'}).text))
                if 'trailer' in title.lower(): continue
                quality = result.find('span',{'class':'calidad2'})
                if quality is None: continue
                
                title = title.replace(' Full HD Movies Watch','').replace(' Full Movies Online','').replace(' Full Movie Online','')
                title = title.replace(' Online HD Movies','').replace(' Full HD Movie DVD','').replace(' Full HD Movies','')
                try: year = re.compile('( \([0-9]{4}\))').findall(title)[0]
                except: year = re.compile('( [0-9]{4})').findall(title)[0]
                title = title.replace(year,'')
                tcheck = title.replace(':','').lower()
                title += ' [COLOR green]%s[/COLOR] {onlinehdwatch}' % quality.text
                image = result.find('div',{'class':'image'}).img['src']
                q = urllib.unquote_plus(query.replace('%3A','')).lower()
                if q == tcheck:
                    content_page = result.a['href']
                    link_page = requests.get(content_page).content
                    soup = BeautifulSoup(link_page)
                    movie_tags = soup.findAll('div',{'class':'movieplay'})
                    for tag in movie_tags:
                        links.append(tag.iframe['src'])
                        titles.append(title)
                        images.append(image)
    except:
        print '!!! >>> Error in Source 12 <<< !!!'
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
