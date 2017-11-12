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
query_url = 'http://m4ufree.com/?keyword=%s&search_section=1'
regulate = HTMLParser.HTMLParser()

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
    try: m4ufree = requests.get(query_url % query, timeout=15).content
    except: return zip(titles, images, links)
    soup = BeautifulSoup(m4ufree)
    try:
        results = soup.findAll('div',{'class':'item'})
        if results:
            for result in results:
                title = regulate.unescape(result.a['title'])
                image = result.a.img['src']
                q = query.replace('+',' ').lower()
                if q in title.lower():
                    quality = result.find('span',{'class':'quality'}).text
                    if not 'HD' in quality: continue
                    content_page = 'http://m4ufree.com'+result.a['href'][1:]
                    
                    
                    ajax = 'http://m4ufree.com/ajax_new.php'
                    mfouru = requests.session()
                    sess = mfouru.get(content_page).content
                    soup = BeautifulSoup(sess)
                    servers = soup.findAll('span',{'class':re.compile('^singlemv ')})
                    datas = [server['data'] for server in servers]
                    
                    for d in datas:
                        ajax_resp = mfouru.post(ajax, data = {'m4u':d}).content
                        videos = re.compile("""{"label":"(.+?)","type":"video/mp4","file":"(.+?)"}""").findall(ajax_resp)
                        if len(videos)> 0:
                            for quality, url in videos:
                                if '720' in quality or '1080' in quality:
                                    titles.append(title+' [COLOR green]%s[/COLOR] {m4ufree}' % quality)
                                    images.append(image)
                                    if url.startswith('http'):
                                        links.append(url)
                                    else:
                                        links.append('http://m4ufree.com/'+url)
                        videos = re.compile("""{file: "(.+?)",type: 'mp4', label: '(.+?)'}""").findall(ajax_resp)
                        if len(videos)> 0:
                            for url, quality in videos:
                                if '720' in quality or '1080' in quality:
                                    titles.append(title+' [COLOR green]%s[/COLOR] {m4ufree}' % quality)
                                    images.append(image)
                                    if url.startswith('http'):
                                        links.append(url)
                                    else:
                                        links.append('http://m4ufree.com/'+url)
    except:
        print '!!! >>> Error in Source 7 <<< !!!'
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
