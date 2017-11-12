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
query_url = 'http://www.mehlizmovies.com/?s=%s'
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
    query = query.replace('%3A','')
    try: mehlizmovies = requests.get(query_url % query, verify=False, timeout=15).content
    except: return zip(titles, images, links)
    soup = BeautifulSoup(mehlizmovies)
    try:
        results = soup.findAll('div',{'class':'result-item'})
        if results:
            for result in results:
                title = regulate.unescape(cleanHex(result.find('div',{'class':'title'}).a.text))
                if 'dubbed' in title.lower() or 'hindi' in title.lower(): continue
                title = title.replace(' 4K 2160P','').replace(' 2160P 4K','').replace(' 1080p','').replace(' [English]','')
                try: year = re.compile('( \([0-9]{4}\))').findall(title)[0]
                except: 
                    try: year = re.compile('( [0-9]{4})').findall(title)[0]
                    except: year = ''
                title = title.replace(year,'').replace(' Watch Full Movie Online','')
                qtitle = title.lower()
                q = urllib.unquote_plus(query.lower())
                if qtitle != q and qtitle.replace(':','') != q: continue
                title += ' [COLOR green]%s[/COLOR] {mehlizmovies}'
                link = result.find('div',{'class':'title'}).a['href']
                image = result.find('div',{'class':'image'}).div.a.img['src']
                
                resp = requests.get(link, verify=False).content
                soup2 = BeautifulSoup(resp)
                try: quality = soup2.find('div',{'id':'playex'}).find('span',{'class':'qualityx'}).text
                except: continue

                if 'Hindu' in quality or 'CAM' in quality: continue 
                iframe_src = soup2.find('div',{'class':'playex'}).findAll('iframe')
                for src in iframe_src:
                    if 'ok.ru' in src['src']:
                        okru = requests.get(src['src']).content
                        okru_soup = BeautifulSoup(okru)
                        OKVideo_jumbled = okru_soup.find('div',{'data-module':'OKVideo'})['data-options']
                        OKVideo_jumbled = urllib2.unquote(urllib2.unquote(OKVideo_jumbled))
                        OKVideo_jumbled = OKVideo_jumbled.decode('unicode_escape').decode('unicode_escape')
                        OKVideo_jumbled = urllib2.unquote(OKVideo_jumbled)
                        OKVideo_unjumbled = OKVideo_jumbled[:OKVideo_jumbled.find(',"metadataEmbedded":')].replace('"metadata":"{','')+'}}'
                        j_obj = json.loads(OKVideo_unjumbled)
                        for vid in j_obj['flashvars']['videos']:
                            if vid['name'] == 'hd':
                                titles.append(title % '720p')
                                links.append(vid['url'])
                                images.append(image)
                            elif vid['name'] == 'full': 
                                titles.append(title % '1080p')
                                links.append(vid['url'])
                                images.append(image)
                            elif vid['name'] == 'quad': 
                                titles.append(title % '2K')
                                links.append(vid['url'])
                                images.append(image)
                            elif vid['name'] == 'ultra': 
                                titles.append(title % '4K')
                                links.append(vid['url'])
                                images.append(image)
                                
                    elif 'player/embed.php' in src['src']:
                        embedded = requests.get(src['src'], verify=False).content
                        try: sources = re.compile("""sources: \[\{(.+?)\},\],""",re.DOTALL).findall(embedded)[0]
                        except: continue
                        srcs = sources.split('},{')
                        for s in srcs:
                            if '1080p' in s or '720p' in s:
                                l = re.compile("""file:\s*['"](.+?)['"]""").findall(s)[0]
                                links.append(l)
                                images.append(image)
                                if '1080p' in s: titles.append(title % '1080p')
                                else: titles.append(title % '720p')
                    else:
                        l = src['src']
                        if '1080' in l: 
                            links.append(l)
                            images.append(image)
                            titles.append(title % '1080p')
                        elif '720' in l: 
                            links.append(l)
                            images.append(image)
                            titles.append(title % '720p')
    except:
        print '!!! >>> Error in Source 8 <<< !!!'
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
