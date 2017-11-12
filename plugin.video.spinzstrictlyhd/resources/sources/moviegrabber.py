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
base= 'http://moviegrabber.tv'
query_url = 'http://moviegrabber.tv/searchaskforapi/?id=%s'
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
    q = urllib.unquote_plus(query.lower())
    sess = requests.Session()
    try: moviegrabber = sess.get(query_url % query, verify=False, timeout=15).content
    except: return zip(titles, images, links)
    soup = BeautifulSoup(moviegrabber)
    try:
        results = soup.findAll('div',{'class':'thumbnail'})
        if results:
            for result in results:
                title = regulate.unescape(cleanHex(result.find('p',{'class':re.compile('text-center text-bold')}).text))
                if 'Server Error (500)' in title: continue
                try: year = re.compile('( \([0-9]{4}\))').findall(title)[0]
                except: 
                    try: year = re.compile('( [0-9]{4})').findall(title)[0]
                    except: year = ''
                title = title.replace(year,'')
                tcheck = title.lower()
                title += ' [COLOR green]%s[/COLOR] {moviegrabber}'
                image = result.find('img')['src']
                q = urllib2.unquote(query.replace('+',' ').lower())
                if q == tcheck:
                    ref = base+result.find('a')['href']
                    movie_id = re.compile('\/post\/(.+?)\/').findall(ref)[0]
                    list_page = base+'/api/media/getDetails?id=%s' % movie_id
                    try: 
                        results = sess.get(list_page, headers={'Referer':ref}, verify=False, timeout=15)
                        item_data = json.loads(results.text)
                    except: return zip(titles, images, links)
                    for post in item_data['show']['posts']:
                        if '1080' in post['title']: title = title % '1080P'
                        elif '720' in post['title']: title = title % '720P'
                        else: continue
                        post_id = post['id']
                        video_page_url = base+'/play/%s/%s/0' % (movie_id, post_id)
                        try: video_page = sess.get(video_page_url,headers={'Referer':'http://moviegrabber.tv/link/'}, verify=False, timeout=15).content
                        except: return zip(titles, images, links)
                        try: 
                            l = BeautifulSoup(video_page).find('source')['src']
                            l += '|Referer=%s&User-Agent=%s'%(video_page_url,'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36')
                            links.append(l)
                            titles.append(title)
                            images.append(image)
                        except: continue
                        
                        try:
                            video_page_url = base+'/play/%s/%s/1' % (movie_id, post_id)
                            try: video_page = sess.get(video_page_url,headers={'Referer':'http://moviegrabber.tv/link/'}, verify=False, timeout=15).content
                            except: return zip(titles, images, links)
                            l = BeautifulSoup(video_page).find('source')['src']
                            l += '|Referer=%s&User-Agent=%s'%(video_page_url,'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36')
                            links.append(l)
                            titles.append(title)
                            images.append(image)
                        except: continue
                        
                        try:
                            video_page_url = base+'/play/%s/%s/2' % (movie_id, post_id)
                            try: video_page = sess.get(video_page_url,headers={'Referer':'http://moviegrabber.tv/link/'}, verify=False, timeout=15).content
                            except: return zip(titles, images, links)
                            l = BeautifulSoup(video_page).find('source')['src']
                            l += '|Referer=%s&User-Agent=%s'%(video_page_url,'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36')
                            links.append(l)
                            titles.append(title)
                            images.append(image)
                        except: continue
    except:
        print '!!! >>> Error in Source 11 <<< !!!'
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
