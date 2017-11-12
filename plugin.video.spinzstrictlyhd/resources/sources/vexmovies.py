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
query_url = 'http://vexmovies.org/?s=%s'
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
    try: vexmovies = requests.get(query_url % query, timeout=15).content
    except: return zip(titles, images, links)
    soup = BeautifulSoup(vexmovies)
    #try:
    results = soup.findAll('div',{'class':'item'})
    if results:
        for result in results:
            title = regulate.unescape(cleanHex(result.find('span',{'class':'tt'}).text))
            if not result.find('span',{'class':'calidad2'}): continue
            quality = result.find('span',{'class':'calidad2'}).text
            tcheck = title.lower()
            print 'tcheck : '+tcheck
            title += ' [COLOR green]%s[/COLOR] {vexmovies}'
            image = result.find('div',{'class':'image'}).img['src']
            q = urllib.unquote_plus(query).lower()
            if q == tcheck:
                content_page = result.a['href']
                link_page = requests.get(content_page).content
                soup = BeautifulSoup(link_page)
                try: iframe = soup.find('div',{'class':'entry-content'}).find('iframe')['src']
                except: continue
                print iframe
                if 'consistent.stream' in iframe:
                    cstream = requests.get(iframe, verify=False).content
                    if 'Whoops, looks like something went wrong.' in cstream: continue
                    scrambled_json = re.compile(""":title=["'](.+?)["']\>""").findall(cstream)[0]
                    decrypted = regulate.unescape(scrambled_json)
                    j_obj = json.loads(decrypted)
                    if '1080' in j_obj['name']: quality = '1080P'
                    elif '720' in j_obj['name']: quality = '720P'
                    for server in j_obj['servers']:
                        for source in server['sources']:
                            links.append(source['src'])
                            titles.append(title % quality)
                            images.append(image)
                else: 
                    links.append(iframe)
                    titles.append(title % quality)
                    images.append(image)
    #except:
    #    print '!!! >>> Error in Source 16 <<< !!!'
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
