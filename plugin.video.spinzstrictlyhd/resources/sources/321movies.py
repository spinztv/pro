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
regulate = HTMLParser.HTMLParser()
query_url = 'http://321movies.cc/?s=%s'

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
    q = urllib.unquote_plus(query).lower()
    try: three21movies = requests.get(query_url % query, verify=False, timeout=15).content
    except: return zip(titles, images, links)
    soup = BeautifulSoup(three21movies)
    try:
        results = soup.findAll('div',{'class':'result-item'})
        if results:
            for result in results:
                title = result.find('div',{'class':'title'}).a.text.replace('Watch ','').replace(' For Free','')
                title = regulate.unescape(cleanHex(title))
                if title.lower() != q: continue
                title += ' [COLOR green]HD[/COLOR] {321movies}'
                image = result.find('img')['src']
                link = result.find('a')['href']
                vid_page = requests.get(link, verify=False).content
                vsoup = BeautifulSoup(vid_page)
                qualityx = vsoup.findAll('span',{'class':'qualityx'})[-1].text
                if not 'HD' in qualityx: continue
                frames = vsoup.findAll('iframe',{'class':'metaframe rptss'})[1:]
                for frame in frames:
                    links.append(frame['src'])
                    titles.append(title)
                    images.append(image)
    except:
        print '!!! >>> Error in Source 1 <<< !!!'
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
