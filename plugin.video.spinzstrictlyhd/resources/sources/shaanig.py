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
query_url = 'http://www.shaanig.se/?s=%s'

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
    try: shaanig = requests.get(query_url % query, verify=False, timeout=15).content
    except: return zip(titles, images, links)
    soup = BeautifulSoup(shaanig)
    try:
        results = soup.findAll('div',{'class':'ml-item'})
        if results:
            for result in results:
                title = regulate.unescape(cleanHex(result.find('span',{'class':'mli-info'}).text))
                try: 
                    year = re.compile('( \([0-9]{4}\))').findall(title)[0]
                    title = title.replace(year,'')
                except: pass
                if title.lower() != q: continue
                quality = result.find('span',{'class':'mli-quality'}).text
                if quality != 'Bluray': continue
                title += ' [COLOR green]%s[/COLOR] {shaanig}'
                try: image = result.find('img')['src']
                except: image = result.find('img')['data-original']
                link = result.find('a')['href']
                vid_page = requests.get(link, verify=False).content
                vsoup = BeautifulSoup(vid_page)
                prelinks = vsoup.findAll('a',{'class':re.compile('^lnk-lnk')})
                for prelink in prelinks:
                    if '1080' in prelink.text: quality = '1080p'
                    elif '720' in prelink.text: quality = '720p'
                    else: continue
                    link = prelink['href'].replace('https://linkshrink.net/zCqB=','').strip()
                    links.append(link)
                    images.append(image)
                    titles.append(title % quality)
    except:
        print '!!! >>> Error in Source 14 <<< !!!'
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
