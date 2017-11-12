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
query_url = 'http://cyberreel.com/search/%s'
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
    try: cyberreel = requests.get(query_url % query, timeout=15).content
    except: return zip(titles, images, links)
    soup = BeautifulSoup(cyberreel)
    try:
        results = soup.findAll('div',{'class':'item'})
        if results:
            for result in results:
                title = regulate.unescape(cleanHex(result.find('span',{'class':'tt'}).text))
                if 'trailer' in title.lower(): continue
                if not result.find('span',{'class':'calidad2'}): continue
                quality = result.find('span',{'class':'calidad2'}).text
                if not '720' in quality and not '1080' in quality: continue
                try: year = re.compile('( \([0-9]{4}\))').findall(title)[0]
                except: 
                    try: year = re.compile('( [0-9]{4})').findall(title)[0]
                    except: year = ''
                title = title.replace(year,'')
                qtitle = title.lower()
                title += ' [COLOR green]%s[/COLOR] {cyberreel}'
                image = result.find('div',{'class':'image'}).img['src']
                q = urllib.unquote_plus(query.lower())
                if q == qtitle:
                    content_page = result.a['href']
                    link_page = requests.get(content_page).content
                    soup = BeautifulSoup(link_page)
                    movie_tags = soup.findAll('div',{'class':'movieplay'})
                    if len(movie_tags) == 0: movie_tags = soup.findAll('iframe')[1:]
                    for tag in movie_tags:
                        try: source = tag.iframe['src']
                        except: 
                            try:source = tag['src']
                            except: continue
                        if 'cyberreel' in source:
                            videojsphp = requests.get(source).content
                            moresoup = BeautifulSoup(videojsphp)
                            sources = moresoup.findAll('source')
                            if sources:
                                for s in sources:
                                    try:
                                        if '720' in s['label'] or '1080' in s['label']:
                                            links.append(s['src'])
                                            titles.append(title % s['label'].replace(' HD',''))
                                            images.append(image)
                                    except:
                                        if '720' in s['data-res'] or '1080' in s['data-res']:
                                            links.append(s['src'])
                                            titles.append(title % s['data-res'].replace(' HD',''))
                                            images.append(image)
                        else:
                            links.append(source)
                            titles.append(title % quality.replace(' HD',''))
                            images.append(image)
    except: 
        print '!!! >>> Error in Source 3 <<< !!!'
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
