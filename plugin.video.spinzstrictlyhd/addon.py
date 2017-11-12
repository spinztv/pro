from BeautifulSoup import BeautifulSoup
from resources.modules import *
from urlparse import parse_qsl
from urllib import urlencode
import urlresolver
import xbmcplugin
import HTMLParser
import xbmcaddon
import importlib
import urlparse
import requests
import xbmcgui
import urllib
import time
import json
import xbmc
import sys
import re

_url = sys.argv[0]
_handle = int(sys.argv[1])
addon_id = 'plugin.video.spinzstrictlyhd'
addon = xbmcaddon.Addon(id=addon_id)
path = 'special://home/addons/%s/' % addon_id
icon = addon.getAddonInfo('icon')
fanart = addon.getAddonInfo('fanart')
cookie_file = xbmc.translatePath(path+'cookies.lwp')

def get_url(**kwargs):
    kwargs = {k: unicode(v).encode('ascii', 'ignore') for k,v in kwargs.iteritems()}
    return '{0}?{1}'.format(_url, urlencode(kwargs))

params = dict(parse_qsl(sys.argv[2][1:]))
if not params:
    trending = xbmc.translatePath(path+'trending.png')
    list_item = xbmcgui.ListItem(label='Trending')
    list_item.setArt({'thumb':trending,'fanart':fanart,'poster':trending})
    url = get_url(module='tmdb', endpoint='trending')
    xbmcplugin.addDirectoryItem(_handle, url, list_item, True)
    popular = xbmc.translatePath(path+'popular.png')
    list_item = xbmcgui.ListItem(label='Popular')
    list_item.setArt({'thumb':popular,'fanart':fanart,'poster':popular})
    url = get_url(module='tmdb', endpoint='popular')
    xbmcplugin.addDirectoryItem(_handle, url, list_item, True)
    genres = xbmc.translatePath(path+'genres.png')
    list_item = xbmcgui.ListItem(label='Genres')
    list_item.setArt({'thumb':genres,'fanart':fanart,'poster':genres})
    url = get_url(module='tmdb', endpoint='genres')
    xbmcplugin.addDirectoryItem(_handle, url, list_item, True)
    search = xbmc.translatePath(path+'search.png')
    list_item = xbmcgui.ListItem(label='Search')
    list_item.setArt({'thumb':search,'fanart':fanart,'poster':search})
    url = get_url(source='search')
    xbmcplugin.addDirectoryItem(_handle, url, list_item, True)
    xbmcplugin.addSortMethod(_handle, xbmcplugin.SORT_METHOD_NONE)
    xbmcplugin.endOfDirectory(_handle)
else:
    source = params.get('source')
    tmdb = params.get('module')
    settings = params.get('action')
    if settings:
        import xbmcvfs
        dialog = xbmcgui.Dialog()
        if xbmcvfs.exists(cookie_file):
            xbmcvfs.delete(cookie_file)
            status = xbmcvfs.exists(cookie_file)
            if not status:
                d = dialog.ok('Cookie File Deleted','Existing cookie file successfully deleted. Image issues should now be resolved.')
            else:
                d = dialog.ok('Deletion Unsuccessful','Existing cookie file was not deleted.')
        else:
            d = dialog.ok('No File', 'No cookie file currently exists. The add-on will automatically create it when needed.')
    elif source:
        Site = importlib.import_module('.'+source.lower(), package='resources.sources')
        Site.router(sys.argv[2][1:])
    elif tmdb:
        genre = params.get('genre')
        title = params.get('title')
        page = params.get('page')
        endpoint = params.get('endpoint')
        from resources.modules import tmdb as api
        
        if genre:
            if page: api.get_genre(genre, page)
            else: api.get_genre(genre)
        elif endpoint == 'genres': api.genre_list()
        elif endpoint == 'search': api.get_search(title, page)
        elif endpoint == 'popular':
            if page: api.get_popular(page)
            else: api.get_popular()
        elif endpoint == 'trending':
            if page: api.get_trending(page)
            else: api.get_trending()
