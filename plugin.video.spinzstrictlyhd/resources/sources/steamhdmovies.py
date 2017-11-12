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
icon = addon.getAddonInfo('icon')
base = 'http://steamhdmovies.com%s'
token_url = 'http://steamhdmovies.com/generateToken'
embed_url = 'http://steamhdmovies.com/embed/%s/?key=MjIwMjAwMzUzMTY4&host=steamhdmovies.com&token=%s'
fullhd_query = 'http://steamhdmovies.com/search?q=%s&quality=3&genre=&type=movie&rated=&order=&result='
seventwenty_query = 'http://steamhdmovies.com/search?q=%s&quality=2&genre=&type=movie&rated=&order=&result='
o = 'https://openload.co/embed/%s'
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
    query = query.replace('%3A','+').replace('+-+','++')
    try: fullhd = requests.get(fullhd_query % query, timeout=15).content
    except: return zip(titles, images, links)
    soup = BeautifulSoup(fullhd)
    try:
        results = soup.findAll('a',{'class':'label'})
        q = urllib.unquote_plus(query.lower())
        if results:
            for result in results:
                title = regulate.unescape(cleanHex(result.find('div',{'class':'truncate'}).text))
                if title != q: continue
                title += ' [COLOR green]1080p[/COLOR] {steamhdmovies}'
                idItem = re.compile('/watch/(.+?)-').findall(result['href'])[0]
                tbody = {'host':'steamhdmovies.com','ref':'steamhdmovies.com','idItem':idItem}
                tcall = requests.post(token_url,data=tbody).text
                tj_obj = json.loads(tcall)
                token = tj_obj['data']['token']
                e_url = embed_url % (idItem, token)
                ecall = requests.get(e_url).text
                ej_obj = json.loads(ecall)
                i = base % result.find('img')['src']
                try:
                    for oload in ej_obj['data']['video']['openload']:
                        titles.append(title)
                        images.append(i)
                        links.append(o % oload['link'])
                except: pass
                try:
                    for p in ej_obj['data']['video']['picasa']:
                        if '1080' in p['label']:
                            titles.append(title)
                            images.append(i)
                            links.append(p['file'])
                except: pass
        seventwenty = requests.get(seventwenty_query % query).content
        soup = BeautifulSoup(seventwenty)
        results = soup.findAll('a',{'class':'label'})
        if results:
            for result in results:
                title = regulate.unescape(cleanHex(result.find('div',{'class':'truncate'}).text))
                if title.lower() != q: continue
                title += ' [COLOR green]720p[/COLOR] {steamhdmovies}'
                idItem = re.compile('/watch/(.+?)-').findall(result['href'])[0]
                tbody = {'host':'steamhdmovies.com','ref':'steamhdmovies.com','idItem':idItem}
                tcall = requests.post(token_url,data=tbody).text
                tj_obj = json.loads(tcall)
                token = tj_obj['data']['token']
                e_url = embed_url % (idItem, token)
                ecall = requests.get(e_url).text
                ej_obj = json.loads(ecall)
                i = base % result.find('img')['src']
                try:
                    for oload in ej_obj['data']['video']['openload']:
                        titles.append(title)
                        images.append(i)
                        links.append(o % oload['link'])
                except: pass
                try:
                    for p in ej_obj['data']['video']['picasa']:
                        if '720' in p['label']:
                            titles.append(title)
                            images.append(i)
                            links.append(p['file'])
                except: pass
    except:
        print '!!! >>> Error in Source 15 <<< !!!'
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
