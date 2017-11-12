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
query_url = 'http://hevcbluray.info/?s=%s'
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
    try: hevcbluray = requests.get(query_url % query, timeout=15).content
    except: return zip(titles, images, links)
    soup = BeautifulSoup(hevcbluray)
    try:
        results = soup.findAll('div',{'class':'img-div'})
        if results:
            for result in results:
                title = regulate.unescape(cleanHex(result.a['title']))
                try: year = re.compile('( [0-9]{4})').findall(title)[0]
                except: continue
                if '720' in title:
                    title = title[:title.find(' 720')]
                    qtitle = title.replace(year,'') + ' [COLOR green]720p[/COLOR] {hevcbluray}'
                elif '1080' in title:
                    title = title[:title.find(' 1080')]
                    qtitle = title.replace(year,'') + ' [COLOR green]1080p[/COLOR] {hevcbluray}'
                else: continue
                title = title.replace(year,'')
                image = result.a.img['src']
                q = urllib.unquote_plus(query).lower()
                nodash = q.replace('-',' ').replace('   ',' ')
                nocolon = q.replace(':','').replace('  ',' ')
                nosymbols = nodash.replace(':','').replace('  ',' ')
                if q == title.lower() or nodash == title.lower() or nocolon == title.lower() or nosymbols == title.lower():
                    content_page = result.a['href']
                    link_page = requests.get(content_page).content
                    vid_links = re.compile('<h3 style="text-align: center;"><a href="(.+?)">').findall(link_page)
                    for l in vid_links:
                        links.append(l)
                        titles.append(qtitle)
                        images.append(image)
    except:
        print '!!! >>> Error in Source 5 <<< !!!'
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
