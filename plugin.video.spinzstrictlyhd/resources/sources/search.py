from urlparse import parse_qsl
from urllib import urlencode
import urlresolver
import xbmcplugin
import HTMLParser
import xbmcaddon
import requests
import xbmcgui
import urllib
import base64
import xbmc
import json
import sys
import os

addon_id = 'plugin.video.spinzstrictlyhd'
addon = xbmcaddon.Addon(id=addon_id)
path = 'special://home/addons/%s/' % addon_id
addonname = addon.getAddonInfo('name')
icon = addon.getAddonInfo('icon')
fanart = addon.getAddonInfo('fanart')
_url = sys.argv[0]
_handle = int(sys.argv[1])
time = 8000

def get_url(**kwargs):
    kwargs = {k: unicode(v).encode('ascii', 'ignore') for k,v in kwargs.iteritems()}
    return '{0}?{1}'.format(_url, urlencode(kwargs))

def SEARCH(title=None):
    if not title:
        dialog = xbmcgui.Dialog()
        title = dialog.input('Enter search term', type=xbmcgui.INPUT_ALPHANUM)
        if title == '': quit()
        from resources.modules import tmdb
        tmdb.get_search(title)
    else:
        print 'search term is '+title
        srcs = []
            
        pl=xbmc.PlayList(1)
        pl.clear()
        
        from resources.modules import workers
        results = workers.Sites().search(title)
        
        q_sort = [(title, image, link) for (title, image, link) in results if '[COLOR green]4' in title]
        q_sort.extend([(title, image, link) for (title, image, link) in results if '[COLOR green]2' in title])
        q_sort.extend([(title, image, link) for (title, image, link) in results if '[COLOR green]1080' in title])
        q_sort.extend([(title, image, link) for (title, image, link) in results if '[COLOR green]720' in title])
        q_sort.extend([(title, image, link) for (title, image, link) in results if '[COLOR green]HD' in title])
        
        for i, (title, image, link) in enumerate(q_sort):
            s = title[title.find('{')+1:title.rfind('}')].lower()
            if s not in srcs: srcs.append(s)
            title = title[:title.find('{')]
            list_item = xbmcgui.ListItem(label=title)
            list_item.setArt({'fanart':fanart,'thumb':image})
            
            url = get_url(source=s,endpoint=link)
            pl.add(url, list_item)
            xbmcplugin.addDirectoryItem(_handle, url, list_item, False)
            
        print 'Total Source relevant to this search '+str(len(srcs))
        xbmcplugin.addSortMethod(_handle, xbmcplugin.SORT_METHOD_NONE)
        xbmcplugin.endOfDirectory(_handle)

def router(paramstring):
    params = dict(parse_qsl(sys.argv[2][1:]))
    params.pop('source')
    title = params.get('title')
    link = params.get('link')
    if params:
        if title is not None: SEARCH(title)
        elif link is not None: RESOLVE(link)
        else:
            raise ValueError('Invalid paramstring: {0}!'.format(paramstring))
    else:
        SEARCH(title)     
              
if __name__ == '__main__':
    router(sys.argv[2][1:])
