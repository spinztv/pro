# encoding: utf-8

from BeautifulSoup import BeautifulSoup
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

def RESOLVE(link):
    original = link
    content_page = requests.get(link).content
    soup = BeautifulSoup(content_page)
    php_url = soup.find('div',{'id':'player'}).iframe['src']
    link_page = requests.get(php_url).content
    soup = BeautifulSoup(link_page)
    link = soup.find('iframe')['src']
    
    try: play_link = urlresolver.HostedMediaFile(link).resolve()
    except: play_link = link
    if 'False' in str(play_link): play_link = original
    
    play_item = xbmcgui.ListItem(path=play_link)
    play_item.setProperty('IsPlayable','true')
    xbmcplugin.setResolvedUrl(_handle, True, listitem=play_item)

def cleanHex(s):
    cleaned = s.replace('&#8211;','-').replace(u'\xa0', u' ').replace(u'\xe9', u'e')
    cleaned = cleaned.replace('&#8217;',"'").replace('&#8216;',"'")
    cleaned = cleaned.replace('&#8230;','...').replace('[&hellip;]','...')
    return cleaned

def SEARCH(query):
    links, titles, images = [], [], []
    wpjson = 'http://1080pmovie.com/wp-json/wp/v2/posts?search=%s'
    try: j_obj = json.loads(requests.get(wpjson % query, verify=False, timeout=15).text)
    except: return zip(titles, images, links)
    try:
        titles = ['%s [COLOR green]1080p[/COLOR] {1080pmovies}' % regulate.unescape(post['title']['rendered'])[:-7] for post in j_obj if urllib.unquote_plus(query.lower()) == regulate.unescape(cleanHex(post['title']['rendered']).lower())[:-7]]
        images = [json.loads(requests.get('https://1080pmovie.com/wp-json/wp/v2/media/'+str(post['featured_media'])).text)['source_url'] for post in j_obj]
        links = [post['link'] for post in j_obj]
    except:
        print '!!! >>> Error in Source 2 <<< !!!'
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
