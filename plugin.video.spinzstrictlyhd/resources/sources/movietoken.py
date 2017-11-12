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
query_url = 'https://movietoken.net/?s=%s'
purl = 'https://putstream.com/decode-link'
regulate = HTMLParser.HTMLParser()
mozhdr = {'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3'}

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
    query = urllib.unquote_plus(query.lower())
    movietoken = requests.get(query_url % query).content
    soup = BeautifulSoup(movietoken)
    results = soup.findAll('div',{'class':'ml-item'})
    if results:
        for result in results:
            title = regulate.unescape(cleanHex(result.find('h2').text))
            if query != title.lower(): continue
            quality = result.find('span',{'class':'mli-quality'}).text
            if not 'hd' in quality.lower(): continue
            qtitle = '%s [COLOR green]%s[/COLOR] {movietoken}'
            image = result.find('img')['data-original']
            content_page = requests.get(result.a['href']).content
            soup = BeautifulSoup(content_page)
            movie_tags = soup.findAll('div',{'class':'movieplay'})[1:]
            for tag in movie_tags:
                iframesrc = tag.iframe['src']
                if 'putstream' in iframesrc:
                    html = requests.get(iframesrc, headers=mozhdr)
                    try: tc = re.findall("tc\s*=\s*'([^']+)",html.text)[0]
                    except: continue
                    s = re.search('function\s_t_t.+?\((\d*),(\d*).+?"([^"]+)".+?"([^"]+)',html.text)
                    s1 = int(s.group(1))
                    s2 = int(s.group(2))
                    xt = tc[s1:s2]
                    xt = xt[::-1]
                    xt = xt + s.group(3) + s.group(4)
                    token = re.findall('_token":\s*"([^"]+)',html.text)[0]
                    data = {'tokenCode': tc,
                            '_token': token}
                    headers = mozhdr
                    headers['x-token'] = xt
                    headers['X-Requested-With'] = 'XMLHttpRequest'
                    h2 = requests.post(purl, data=data, headers=headers, cookies=html.cookies)
                    q_count = 1
                    try:
                        for u in h2.json():
                            if u != '':
                                if '/?' in u:
                                    stream_url = requests.get(surl, headers=mozhdr, allow_redirects=False).headers['location']
                                    print 'stream_url for movietoken is: '+stream_url
                                    links.append(stream_url)
                                else: links.append(u)
                                if q_count == 1: titles.append(qtitle % (title,'720P'))
                                elif q_count == 2: titles.append(qtitle % (title,'1080P'))
                                else: titles.append(qtitle % (title,'HD'))
                                images.append(image)
                            q_count += 1
                    except: pass
                    try:
                        oloadtest = re.compile("var locationPath = '(.+?src=openload)';",re.DOTALL).findall(html.text)[0]
                        opage = requests.get(oloadtest).content
                        osoup = BeautifulSoup(opage)
                        links.append(osoup.find('iframe',{'id':'openloadIframe'})['src'])
                        titles.append(title)
                        images.append(image)
                    except: pass
                else: 
                    links.append(iframesrc)
                    titles.append(title)
                    images.append(image)

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
