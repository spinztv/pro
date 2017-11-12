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

host = 'http://api.themoviedb.org/3/'
api_key = 'c1935caceb7875775ddc15fd3ce21b43'
lang = 'en-US'
tmdb_thumb = 'http://image.tmdb.org/t/p/w342%s'
tmdb_fanart = 'http://image.tmdb.org/t/p/w1280%s'
trending_endpoint = ('%ssearch/trending'
                    '?api_key=%s'
                    '&page=%s')
popular_endpoint = ('%smovie/popular'
                    '?api_key=%s'
                    '&language=%s'
                    '&page=%s')
genres_endpoint = ('%sgenre/movie/list'
                   '?api_key=%s'
                   '&language=%s')
genre_endpoint = ('%sdiscover/movie'
                  '?api_key=%s'
                  '&language=%s'
                  '&sort_by=popularity.desc'
                  '&include_adult=false'
                  '&include_video=false'
                  '&page=%s'
                  '&with_genres=%s')
search_endpoint = ('%ssearch/movie'
                   '?api_key=%s'
                   '&language=%s'
                   '&query=%s'
                   '&page=%s'
                   '&include_adult=false')

_url = sys.argv[0]
_handle = int(sys.argv[1])
addon_id = 'plugin.video.spinzstrictlyhd'
addon = xbmcaddon.Addon(id=addon_id)
path = 'special://home/addons/%s/' % addon_id
genres_icon = xbmc.translatePath(path+'genres.png')
trending_icon = xbmc.translatePath(path+'trending.png')
popular_icon = xbmc.translatePath(path+'popular.png')
search_icon = xbmc.translatePath(path+'search.png')
fanart = addon.getAddonInfo('fanart')

def get_url(**kwargs):
    kwargs = {k: unicode(v).encode('ascii', 'ignore') for k,v in kwargs.iteritems()}
    return '{0}?{1}'.format(_url, urlencode(kwargs))

def genre_list():
    endpoint = genres_endpoint % (host, api_key, lang)
    print endpoint
    resp = requests.get(endpoint).text
    j_obj = json.loads(resp)
    print str(j_obj)
    for g in j_obj['genres']:
        list_item = xbmcgui.ListItem(label=g['name'])
        list_item.setArt({'fanart':fanart,'thumb':genres_icon,'poster':genres_icon})
        url = get_url(module='tmdb',genre=g['id'])
        xbmcplugin.addDirectoryItem(_handle, url, list_item, True)
    xbmcplugin.addSortMethod(_handle, xbmcplugin.SORT_METHOD_NONE)
    xbmcplugin.endOfDirectory(_handle)

def get_genre(genre, page='1'):
    endpoint = genre_endpoint % (host, api_key, lang, page, str(genre))
    resp = requests.get(endpoint).text
    j_obj = json.loads(resp)
    for r in j_obj['results']:
        list_item = xbmcgui.ListItem(label=r['title'])
        list_item.setArt({'fanart':tmdb_fanart % r['backdrop_path'],'thumb':tmdb_thumb % r['poster_path'],'poster':tmdb_thumb % r['poster_path']})
        list_item.setInfo('video',{'plot':r['overview'],'premiered':r['release_date'],'title':r['title']})
        url = get_url(source='search',title=r['title'])
        xbmcplugin.addDirectoryItem(_handle, url, list_item, True)
    if j_obj['page'] < j_obj['total_pages']:
        list_item = xbmcgui.ListItem(label='[COLOR yellow]NEXT PAGE >>>[/COLOR]')
        list_item.setArt({'fanart':fanart,'thumb':genres_icon,'poster':genres_icon})
        url = get_url(module='tmdb',genre=genre, page=j_obj['page']+1)
        xbmcplugin.addDirectoryItem(_handle, url, list_item, True)
    xbmcplugin.addSortMethod(_handle, xbmcplugin.SORT_METHOD_NONE)
    xbmcplugin.endOfDirectory(_handle)

def get_popular(page='1'):
    endpoint = popular_endpoint % (host, api_key, lang, page)
    resp = requests.get(endpoint, verify=False).text
    j_obj = json.loads(resp)
    for r in j_obj['results']:
        list_item = xbmcgui.ListItem(label=r['title'])
        list_item.setArt({'fanart':tmdb_fanart % r['backdrop_path'],'thumb':tmdb_thumb % r['poster_path'],'poster':tmdb_thumb % r['poster_path']})
        list_item.setInfo('video',{'plot':r['overview'],'premiered':r['release_date'],'title':r['title']})
        url = get_url(source='search',title=r['title'])
        xbmcplugin.addDirectoryItem(_handle, url, list_item, True)
    if j_obj['page'] < j_obj['total_pages']:
        list_item = xbmcgui.ListItem(label='[COLOR yellow]NEXT PAGE >>>[/COLOR]')
        list_item.setArt({'fanart':fanart,'thumb':popular_icon,'poster':popular_icon})
        url = get_url(module='tmdb', endpoint='popular', page=j_obj['page']+1)
        xbmcplugin.addDirectoryItem(_handle, url, list_item, True)
    xbmcplugin.addSortMethod(_handle, xbmcplugin.SORT_METHOD_NONE)
    xbmcplugin.endOfDirectory(_handle)

def get_trending(page='1'):
    endpoint = trending_endpoint % (host, api_key, page)
    resp = requests.get(endpoint, verify=False).text
    j_obj = json.loads(resp)
    print str(j_obj).decode('utf-8').encode('ascii','ignore')
    for r in j_obj['results']:
        if not r['media_type'] == 'movie': continue
        list_item = xbmcgui.ListItem(label=r['title'])
        list_item.setArt({'fanart':tmdb_fanart % r['backdrop_path'],'thumb':tmdb_thumb % r['poster_path'],'poster':tmdb_thumb % r['poster_path']})
        list_item.setInfo('video',{'plot':r['overview'],'premiered':r['release_date'],'title':r['title']})
        url = get_url(source='search',title=r['title'])
        xbmcplugin.addDirectoryItem(_handle, url, list_item, True)
    if j_obj['page'] < j_obj['total_pages']:
        list_item = xbmcgui.ListItem(label='[COLOR yellow]NEXT PAGE >>>[/COLOR]')
        list_item.setArt({'fanart':fanart,'thumb':trending_icon,'poster':trending_icon})
        url = get_url(module='tmdb', endpoint='trending', page=j_obj['page']+1)
        xbmcplugin.addDirectoryItem(_handle, url, list_item, True)
    xbmcplugin.addSortMethod(_handle, xbmcplugin.SORT_METHOD_NONE)
    xbmcplugin.endOfDirectory(_handle)

def get_search(query, page='1'):
    endpoint = search_endpoint % (host, api_key, lang, query, page)
    resp = requests.get(endpoint).text
    j_obj = json.loads(resp)
    for r in j_obj['results']:
        list_item = xbmcgui.ListItem(label=r['title'])
        list_item.setArt({'fanart':tmdb_fanart % r['backdrop_path'],'thumb':tmdb_thumb % r['poster_path'],'poster':tmdb_thumb % r['poster_path']})
        list_item.setInfo('video',{'plot':r['overview'],'premiered':r['release_date'],'title':r['title']})
        url = get_url(source='search',title=r['title'])
        xbmcplugin.addDirectoryItem(_handle, url, list_item, True)
    if j_obj['page'] < j_obj['total_pages']:
        list_item = xbmcgui.ListItem(label='[COLOR yellow]NEXT PAGE >>>[/COLOR]')
        list_item.setArt({'fanart':fanart,'thumb':search_icon,'poster':search_icon})
        url = get_url(module='tmdb',endpoint='search', title=query, page=j_obj['page']+1)
        xbmcplugin.addDirectoryItem(_handle, url, list_item, True)
    xbmcplugin.addSortMethod(_handle, xbmcplugin.SORT_METHOD_NONE)
    xbmcplugin.endOfDirectory(_handle)
