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
query_url = 'http://movie4u.cc/?s=%s'
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
    query = urllib.unquote_plus(query.lower())
    try: movie4u = requests.get(query_url % query, verify=False, timeout=15).content
    except: return zip(titles, images, links)
    soup = BeautifulSoup(movie4u)
    try:
        results = soup.findAll('div',{'class':'result-item'})
        if results:
            for result in results:
                title = regulate.unescape(cleanHex(result.find('div',{'class':'title'}).a.text))
                try: year = re.compile('( \([0-9]{4}\))').findall(title)[0]
                except: 
                    try: year = re.compile('( [0-9]{4})').findall(title)[0]
                    except: year = ''
                title = title.replace(year,'')
                if query == title.lower():
                    content_page = result.find('div',{'class':'title'}).a['href']
                    link_page = requests.get(content_page, verify=False).content
                    soup = BeautifulSoup(link_page)
                    if not soup.find('span',{'class':'qualityx'}): continue
                    quality = soup.find('span',{'class':'qualityx'}).text
                    if 'HD' in quality:
                        title += ' [COLOR green]%s[/COLOR] {movie4u}' % quality.replace('HD ','')
                        image = result.find('div',{'class':'image'}).img['src']
                        movie_tags = soup.findAll('iframe',{'class':'metaframe rptss'})
                        for tag in movie_tags:
                            links.append(tag['src'])
                            titles.append(title)
                            images.append(image)
    except:
        print '!!! >>> Error in Source 10 <<< !!!'
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
