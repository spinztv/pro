# -*- coding: cp1252 -*-
import xbmc , xbmcaddon , xbmcgui , xbmcplugin , os , base64 , sys , xbmcvfs , unicodedata
import urlresolver
import httplib
import requests
import urlparse
import shutil
import binascii
import subprocess
import urllib2 , urllib , glob , traceback
import re
import plugintools
import zipfile
import time
import ntpath
import cookielib
import buggalo
from urllib2 import urlopen
from bs4 import BeautifulSoup
from BeautifulSoup import BeautifulStoneSoup , BeautifulSOAP
from cookielib import CookieJar
from addon . common . addon import Addon
from addon . common . net import Net
from imports . tvGuide import gui
if 64 - 64: i11iIiiIii
if 65 - 65: O0 / iIii1I11I1II1 % OoooooooOO - i1IIi
if 73 - 73: II111iiii
if 22 - 22: I1IiiI * Oo0Ooo / OoO0O00 . OoOoOO00 . o0oOOo0O0Ooo / I1ii11iIi11i
if 48 - 48: oO0o / OOooOOo / I11i / Ii1I
IiiIII111iI = 'plugin.video.spinz'
IiII = 'plugin.video.spinz'
iI1Ii11111iIi = xbmc . translatePath ( 'special://home/addons/' )
i1i1II = xbmc . translatePath ( 'special://home/addonsbroke/' )
O0oo0OO0 = xbmcaddon . Addon ( id = IiII )
I1i1iiI1 = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3'
IiII = 'plugin.video.spinz'
iiIIIII1i1iI = 'plugin.video.spinz'
o0oO0 = xbmcgui . DialogProgress ( )
oo00 = "Spinz Tv Pro"
o00 = Net ( )
Oo0oO0ooo = base64 . decodestring
o0oOoO00o = O0oo0OO0 . getSetting ( 'User' )
i1 = O0oo0OO0 . getSetting ( 'Pass' )
oOOoo00O0O = O0oo0OO0 . getSetting ( 'AdultPass' )
i1111 = xbmc . translatePath ( 'special://home/' )
i11 = ( Oo0oO0ooo ( 'aHR0cDovL2dlbmlldHYuY28udWsvc3Bpbnov' ) )
I11 = xbmc . translatePath ( os . path . join ( 'special://home/addons/' + IiII , 'icon.png' ) )
Oo0o0000o0o0 = i11 + ( Oo0oO0ooo ( 'YXJ0Lw==' ) )
oOo0oooo00o = "0.0.1"
oO0o0o0ooO0oO = xbmc . translatePath ( 'special://home/userdata/addon_data/plugin.video.spinz' )
oo0o0O00 = xbmc . translatePath ( os . path . join ( 'special://home/addons/plugin.video.spinz/imports/tvGuide/ResetDatabase.py' ) )
oO = xbmc . translatePath ( 'special://thumbnails' ) ;
i1iiIIiiI111 = "Xhoans"
oooOOOOO = xbmc . translatePath ( os . path . join ( 'special://home/addons/' + IiII , 'fanart.jpg' ) )
i1iiIII111ii = base64 . decodestring ( 'LnBocA==' )
i1iIIi1 = O0oo0OO0 . getLocalizedString
ii11iIi1I = CookieJar ( )
iI111I11I1I1 = urllib2 . build_opener ( urllib2 . HTTPCookieProcessor ( ii11iIi1I ) )
iI111I11I1I1 . addheaders = [ ( 'User-Agent' , 'Mozilla/5.0' ) ]
OOooO0OOoo = int ( sys . argv [ 1 ] )
iIii1 = xbmc . translatePath ( O0oo0OO0 . getAddonInfo ( 'profile' ) . decode ( 'utf-8' ) )
oOOoO0 = xbmc . translatePath ( 'special://home/userdata/' )
O0OoO000O0OO = xbmc . translatePath ( os . path . join ( 'special://home/userdata' , 'favourites.xml' ) )
iiI1IiI = oO0o0o0ooO0oO + '/addons.ini'
II = xbmcgui . Dialog ( )
if 57 - 57: ooOoo0O
def OooO0 ( ) :
 II11iiii1Ii ( )
 OO0o ( '[COLORsteelblue]LOGIN[/COLOR]' , '' , 60000 , I11 , oooOOOOO , '' )
 if 82 - 82: i1I1i1Ii11 . IIIIII11i1I - o0o0OOO0o0 % O0 % i1IIi * OoOoOO00
 if 62 - 62: i1I1i1Ii11 . i1IIi / Ii1I
 Iii1i1I11I ( '[COLORsteelblue]Stream Lists[/COLOR]' , '' , 16 , I11 , oooOOOOO , '' )
 if 50 - 50: i1IIi . I1IiiI % OoOoOO00 - OoO0O00 - I11i
 if 34 - 34: II111iiii / OoooooooOO . o0oOOo0O0Ooo . OoooooooOO % i1IIi
def II11iiii1Ii ( ) :
 if i1 == 'insert_password' :
  II . ok ( '[COLORsteelblue]Spinz Tv Pro Login[/COLOR]' , 'You need to set username and password to access this' , 'These are unique and provided upon purchase ' , ' @ [COLORsteelblue]https://www.facebook.com/groups/614286415341465/[/COLOR]' )
  O0oo0OO0 . openSettings ( sys . argv [ 0 ] )
  if 49 - 49: o0oOOo0O0Ooo * iIii1I11I1II1 / i1IIi / i11iIiiIii / o0oOOo0O0Ooo
  if 28 - 28: OOooOOo - i1I1i1Ii11 . i1I1i1Ii11 + OoOoOO00 - OoooooooOO + O0
  if 95 - 95: OoO0O00 % oO0o . O0
  if 15 - 15: o0o0OOO0o0 / Ii1I . Ii1I - i1IIi
  if 53 - 53: i1I1i1Ii11 + I1IiiI * oO0o
  if 61 - 61: i1IIi * OOooOOo / OoooooooOO . i11iIiiIii . OoOoOO00
  if 60 - 60: I11i / I11i
  if 46 - 46: Ii1I * OOooOOo - OoO0O00 * oO0o - IIIIII11i1I
  if 83 - 83: OoooooooOO
def Iii111II ( ) :
 Iii1i1I11I ( 'Full List' , '' , 14 , I11 , oooOOOOO , '' )
 Iii1i1I11I ( 'Entertainment - USA/CA' , '' , 14 , I11 , oooOOOOO , '' )
 Iii1i1I11I ( 'Entertainment - UK' , '' , 14 , I11 , oooOOOOO , '' )
 Iii1i1I11I ( 'Sports - US/CA' , '' , 14 , I11 , oooOOOOO , '' )
 Iii1i1I11I ( 'UK Sports' , '' , 14 , I11 , oooOOOOO , '' )
 Iii1i1I11I ( 'NBA / NFL / NHL' , '' , 14 , I11 , oooOOOOO , '' )
 Iii1i1I11I ( 'Football' , '' , 14 , I11 , oooOOOOO , '' )
 Iii1i1I11I ( 'Boxing / UFC / WWE' , '' , 14 , I11 , oooOOOOO , '' )
 Iii1i1I11I ( 'World Sports' , '' , 14 , I11 , oooOOOOO , '' )
 Iii1i1I11I ( 'Cinema' , '' , 14 , I11 , oooOOOOO , '' )
 Iii1i1I11I ( 'Kids' , '' , 14 , I11 , oooOOOOO , '' )
 Iii1i1I11I ( 'News Networks' , '' , 14 , I11 , oooOOOOO , '' )
 Iii1i1I11I ( 'Music' , '' , 14 , I11 , oooOOOOO , '' )
 Iii1i1I11I ( 'Education / Lifestyle' , '' , 14 , I11 , oooOOOOO , '' )
 Iii1i1I11I ( 'Sci-Fi Movies' , '' , 14 , I11 , oooOOOOO , '' )
 if 9 - 9: OoO0O00
 if 33 - 33: o0o0OOO0o0 . ooOoo0O
def O0oo0OO0oOOOo ( name ) :
 i1i1i11IIi = name
 II1III = iI1iI1I1i1I ( Oo0oO0ooo ( '' ) )
 iIi11Ii1 = re . compile ( '#EXTINF:.+? tvg-name="(.+?)" tvg-logo="(.+?)" group-title="Live Events"",.+?\n(.+?)\n' ) . findall ( II1III )
 for name , Ii11iII1 , Oo0O0O0ooO0O in iIi11Ii1 :
  Oo0O0O0ooO0O = ( Oo0O0O0ooO0O ) . replace ( 'replace_user' , o0oOoO00o ) . replace ( 'replace_pass' , i1 )
  OO0o ( ( '' + name + '' ) . replace ( '_' , ' ' ) , ( Oo0O0O0ooO0O ) . strip ( ) , 15 , Ii11iII1 , Ii11iII1 , '' )
 else :
  OO0o ( '[COLORred]Streams will appear here for live events when available[/COLOR]' , '' , 15 , '' , '' , '' )
  if 15 - 15: I1ii11iIi11i + OoOoOO00 - OoooooooOO / OOooOOo
def oo000OO00Oo ( ) :
 xbmc . executebuiltin ( "XBMC.RunScript(" + oo0o0O00 + ")" )
 O0OOO0OOoO0O ( )
 if 70 - 70: i1I1i1Ii11 * Oo0Ooo * I11i / Ii1I
 if 88 - 88: O0
def O0OoO0O00o0oO ( name ) :
 i1i1i11IIi = name
 II1III = iI1iI1I1i1I ( 'http://spinztvpro.tk:8000/get.php?username=' + o0oOoO00o + '&password=' + i1 + '&type=m3u_plus&output=m3u8' )
 iIi11Ii1 = re . compile ( '#EXTINF:.+? tvg-name="([^"]*)" tvg-logo="([^"]*)" group-title="([^"]*)",.+?\n(.+?)\n' ) . findall ( II1III )
 for name , Ii11iII1 , I1ii1Ii1 , Oo0O0O0ooO0O in iIi11Ii1 :
  if i1i1i11IIi == 'Full List' :
   Oo0O0O0ooO0O = ( Oo0O0O0ooO0O ) . replace ( '.ts' , '.m3u8' )
   OO0o ( ( '' + name + '' ) . replace ( '_' , ' ' ) , ( Oo0O0O0ooO0O ) . strip ( ) , 15 , Ii11iII1 , Ii11iII1 , '' )
  else :
   i1i1i11IIi = ( i1i1i11IIi ) . replace ('World','القنوات العربية')
   if i1i1i11IIi in I1ii1Ii1 :
    Oo0O0O0ooO0O = ( Oo0O0O0ooO0O ) . replace ( '.ts' , '.m3u8' )
    print Oo0O0O0ooO0O + '>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>'
    OO0o ( ( '' + name + '' ) . replace ( '_' , ' ' ) , ( Oo0O0O0ooO0O ) . strip ( ) , 15 , Ii11iII1 , Ii11iII1 , '' )
   else :
    pass
def iii11 ( ) :
 O0OOO0OOoO0O ( )
 try :
  oOOOOo0 = gui . TVGuide ( )
  oOOOOo0 . doModal ( )
  del oOOOOo0
  if 20 - 20: i1IIi + I1ii11iIi11i - o0o0OOO0o0
 except :
  import sys
  import traceback as tb
  ( IiI11iII1 , IIII11I1I , traceback ) = sys . exc_info ( )
  tb . print_exception ( IiI11iII1 , IIII11I1I , traceback )
  if 91 - 91: OoO0O00 / I11i - II111iiii . I11i
def iI1iI1I1i1I ( url ) :
 i1I11i1I = urllib2 . Request ( url )
 i1I11i1I . add_header ( 'User-Agent' , 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3' )
 Oo0o00 = urllib2 . urlopen ( i1I11i1I )
 O0O0oOO00O00o = Oo0o00 . read ( )
 Oo0o00 . close ( )
 return O0O0oOO00O00o
 if 24 - 24: i1I1i1Ii11
 if 57 - 57: O0 / IIIIII11i1I % OoO0O00 / IIIIII11i1I . OoOoOO00 / O0
 if 89 - 89: OoOoOO00
def O0OOO0OOoO0O ( ) :
 OO0oOoOO0oOO0 = os . path . join ( oO0o0o0ooO0oO , 'addons.ini' )
 oO0OOoo0OO = open ( OO0oOoOO0oOO0 , "w+" )
 II1III = iI1iI1I1i1I ( 'http://spinztvpro.tk:8000/get.php?username=' + o0oOoO00o + '&password=' + i1 + '&type=m3u_plus&output=m3u8' )
 iIi11Ii1 = re . compile ( '#EXTINF:.+? tvg-name="([^"]*)" tvg-logo="([^"]*)" group-title="([^"]*)",.+?\n(.+?).ts' ) . findall ( II1III )
 oO0OOoo0OO . write ( r'[' + IiiIII111iI + ']' + '\n' )
 for O0ii1ii1ii , Ii11iII1 , I1ii1Ii1 , Oo0O0O0ooO0O in iIi11Ii1 :
  Oo0O0O0ooO0O = ( Oo0O0O0ooO0O + '.m3u8' ) . replace ( ':' , '%3A' ) . replace ( '/' , '%2F' )
  oooooOoo0ooo = ( O0ii1ii1ii + '=plugin://' + IiiIII111iI + '/?url=' + Oo0O0O0ooO0O + '&mode=15&name=' + ( O0ii1ii1ii ) . replace ( ' ' , '+' ) + '&amp;iconimage=' + ( Ii11iII1 ) . replace ( ' ' , '' ) + '+&amp;fanart=' + ( Ii11iII1 ) . replace ( ' ' , '' ) + '+&amp;description=' )
  oO0OOoo0OO . write ( oooooOoo0ooo + '\n' )
  if 6 - 6: I11i - Ii1I + iIii1I11I1II1 - IIIIII11i1I - i11iIiiIii
  if 79 - 79: OoOoOO00 - O0 * OoO0O00 + OoOoOO00 % O0 * O0
def oOOo0 ( url ) :
 oo00O00oO = xbmc . Player ( iIiIIIi ( ) )
 import urlresolver
 try : oo00O00oO . play ( url ) . strip ( )
 except : pass
 if 93 - 93: ooOoo0O
 if 10 - 10: I11i
def iIiIIIi ( ) :
 try :
  OOooOO000 = getSet ( "core-player" )
  if ( OOooOO000 == 'DVDPLAYER' ) : OOoOoo = xbmc . PLAYER_CORE_DVDPLAYER
  elif ( OOooOO000 == 'MPLAYER' ) : OOoOoo = xbmc . PLAYER_CORE_MPLAYER
  elif ( OOooOO000 == 'PAPLAYER' ) : OOoOoo = xbmc . PLAYER_CORE_PAPLAYER
  else : OOoOoo = xbmc . PLAYER_CORE_AUTO
 except : OOoOoo = xbmc . PLAYER_CORE_AUTO
 return OOoOoo
 return True
 if 85 - 85: I1ii11iIi11i % ooOoo0O % o0o0OOO0o0
 if 82 - 82: i11iIiiIii - ooOoo0O * OoooooooOO / I11i
def Iii1i1I11I ( name , url , mode , iconimage , fanart , description ) :
 if 31 - 31: i1I1i1Ii11 . OoO0O00 - iIii1I11I1II1
 ooOOO00Ooo = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart ) + "&description=" + urllib . quote_plus ( description )
 IiIIIi1iIi = True
 ooOOoooooo = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 ooOOoooooo . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description } )
 ooOOoooooo . setProperty ( "Fanart_Image" , fanart )
 IiIIIi1iIi = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = ooOOO00Ooo , listitem = ooOOoooooo , isFolder = True )
 return IiIIIi1iIi
 if 1 - 1: Oo0Ooo / o0oOOo0O0Ooo % ooOoo0O * i1I1i1Ii11 . i11iIiiIii
def OO0o ( name , url , mode , iconimage , fanart , description ) :
 if 2 - 2: I1ii11iIi11i * I11i - iIii1I11I1II1 + I1IiiI . oO0o % ooOoo0O
 ooOOO00Ooo = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart ) + "&description=" + urllib . quote_plus ( description )
 IiIIIi1iIi = True
 ooOOoooooo = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 ooOOoooooo . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description } )
 ooOOoooooo . setProperty ( "Fanart_Image" , fanart )
 IiIIIi1iIi = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = ooOOO00Ooo , listitem = ooOOoooooo , isFolder = False )
 return IiIIIi1iIi
 if 92 - 92: ooOoo0O
def IIiIiiIi ( ) :
 O000oo = [ ]
 IIi1I11I1II = sys . argv [ 2 ]
 if len ( IIi1I11I1II ) >= 2 :
  OooOoooOo = sys . argv [ 2 ]
  ii11IIII11I = OooOoooOo . replace ( '?' , '' )
  if ( OooOoooOo [ len ( OooOoooOo ) - 1 ] == '/' ) :
   OooOoooOo = OooOoooOo [ 0 : len ( OooOoooOo ) - 2 ]
  OOooo = ii11IIII11I . split ( '&' )
  O000oo = { }
  for oOooOOOoOo in range ( len ( OOooo ) ) :
   i1Iii1i1I = { }
   i1Iii1i1I = OOooo [ oOooOOOoOo ] . split ( '=' )
   if ( len ( i1Iii1i1I ) ) == 2 :
    O000oo [ i1Iii1i1I [ 0 ] ] = i1Iii1i1I [ 1 ]
    if 91 - 91: I1ii11iIi11i + I1IiiI . OOooOOo * I1ii11iIi11i + I1IiiI * Oo0Ooo
 return O000oo
 if 80 - 80: ooOoo0O % OOooOOo % oO0o - Oo0Ooo + Oo0Ooo
 if 19 - 19: OoOoOO00 * i1IIi
OooOoooOo = IIiIiiIi ( )
Oo0O0O0ooO0O = None
O0ii1ii1ii = None
ii111iI1iIi1 = None
OOO = None
oo0OOo0 = None
I11IiI = None
O0ooO0Oo00o = None
if 77 - 77: iIii1I11I1II1 * OoO0O00
if 95 - 95: I1IiiI + i11iIiiIii
try :
 O0ooO0Oo00o = int ( OooOoooOo [ "fav_mode" ] )
except :
 pass
 if 6 - 6: o0o0OOO0o0 / i11iIiiIii + ooOoo0O * oO0o
try :
 Oo0O0O0ooO0O = urllib . unquote_plus ( OooOoooOo [ "url" ] )
except :
 pass
try :
 O0ii1ii1ii = urllib . unquote_plus ( OooOoooOo [ "name" ] )
except :
 pass
try :
 OOO = urllib . unquote_plus ( OooOoooOo [ "iconimage" ] )
except :
 pass
try :
 ii111iI1iIi1 = int ( OooOoooOo [ "mode" ] )
except :
 pass
try :
 oo0OOo0 = urllib . unquote_plus ( OooOoooOo [ "fanart" ] )
except :
 pass
try :
 I11IiI = urllib . unquote_plus ( OooOoooOo [ "description" ] )
except :
 pass
 if 80 - 80: II111iiii
 if 83 - 83: I11i . i11iIiiIii + II111iiii . o0oOOo0O0Ooo * I11i
print str ( i1iiIIiiI111 ) + ': ' + str ( oOo0oooo00o )
print "Mode: " + str ( ii111iI1iIi1 )
print "URL: " + str ( Oo0O0O0ooO0O )
print "Name: " + str ( O0ii1ii1ii )
print "IconImage: " + str ( OOO )
if 53 - 53: II111iiii
if 31 - 31: OoO0O00
def o0O ( content , viewType ) :
 if 2 - 2: iIii1I11I1II1 / oO0o + OoO0O00 / OOooOOo
 if content :
  xbmcplugin . setContent ( int ( sys . argv [ 1 ] ) , content )
 if O0oo0OO0 . getSetting ( 'auto-view' ) == 'true' :
  xbmc . executebuiltin ( "Container.SetViewMode(%s)" % O0oo0OO0 . getSetting ( viewType ) )
  if 9 - 9: o0oOOo0O0Ooo . o0o0OOO0o0 - Oo0Ooo - oO0o + II111iiii * i11iIiiIii
  if 79 - 79: oO0o % I11i % I1IiiI
if ii111iI1iIi1 == None : OooO0 ( )
elif ii111iI1iIi1 == 11 : iii11 ( )
elif ii111iI1iIi1 == 12 : II11iiii1Ii ( )
elif ii111iI1iIi1 == 13 : oo000OO00Oo ( )
elif ii111iI1iIi1 == 14 : O0OoO0O00o0oO ( O0ii1ii1ii )
elif ii111iI1iIi1 == 15 : oOOo0 ( Oo0O0O0ooO0O )
elif ii111iI1iIi1 == 16 : Iii111II ( )
elif ii111iI1iIi1 == 17 : O0oo0OO0oOOOo ( O0ii1ii1ii )
elif ii111iI1iIi1 == 60000 : O0oo0OO0 . openSettings ( sys . argv [ 0 ] )
xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
# dd678faae9ac167bc83abf78e5cb2f3f0688d3a3