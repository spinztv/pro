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
query_url = 'http://www.wannahd.com/?s=%s'
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
    try: wannahd = requests.get(query_url % query, timeout=15).content
    except: return zip(titles, images, links)
    soup = BeautifulSoup(wannahd)
    try:
        results = soup.findAll('div',{'class':'result-item'})
        if results:
            for result in results:
                title = regulate.unescape(cleanHex(result.find('div',{'class':'title'}).a.text))
                image = result.find('img')['src']
                q = urllib.unquote_plus(query).lower()
                if q == title.lower():
                    content_page = result.article.div.div.a['href']
                    link_page = requests.get(content_page).content
                    try: 
                        json_regex = re.compile("""sources:\s\[(.+?)\]""",re.DOTALL).findall(link_page)[0]
                        if len(json_regex.rstrip().strip()) == 0:
                            json_regex = re.compile("""sources:\s\[(.+?)\]""",re.DOTALL).findall(link_page)[1]
                    except: 
                        jumbled = re.compile('document\.write\(unescape\("(.+?)"\)\)',re.DOTALL).findall(link_page)[0]
                        unjumbled = urllib2.unquote(jumbled)
                        json_regex = re.compile("""sources:\s\[(.+?)\]""",re.DOTALL).findall(unjumbled)[0]
                    sets = json_regex.split('}, {')
                    for source in sets:
                        try: quality = re.compile("""label:\s['"](.+?)['"]""").findall(source)[0]
                        except: quality = re.compile("""['"]label['"]:\s['"](.+?)['"]""").findall(source)[0]
                        try: link = re.compile("""file:['"](.+?)['"]""").findall(source)[0]
                        except: link = re.compile("""['"]file['"]:\s*['"](.+?)['"]""").findall(source)[0]
                        if '720' in quality or '1080' in quality or '720' in link or '1080' in link:
                            if '720' in link: quality = '720p'
                            elif '1080' in link: quality = '1080p'
                            links.append(link+'|Referer=%s' % content_page)
                            titles.append('%s [COLOR green]%s[/COLOR] {wannahd}' % (title, quality))
                            images.append(image)
    except:
        print '!!! >>> Error in Source 17 <<< !!!'
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
