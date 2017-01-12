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
def oOOOoO0O00o0 ( name ) :
 i1i1i11IIi = name
 II1III = iI1iI1I1i1I ( 'http://sptvserver.nl:8000/get.php?username=' + o0oOoO00o + '&password=' + i1 + '&type=m3u_plus&output=m3u8' )
 iIi11Ii1 = re . compile ( '#EXTINF:.+? tvg-name="([^"]*)" tvg-logo="([^"]*)" group-title="([^"]*)",.+?\n(.+?)\n' ) . findall ( II1III )
 for name , Ii11iII1 , iII , Oo0O0O0ooO0O in iIi11Ii1 :
  if i1i1i11IIi == 'Full List' :
   Oo0O0O0ooO0O = ( Oo0O0O0ooO0O ) . replace ( '.ts' , '.m3u8' )
   OO0o ( ( '' + name + '' ) . replace ( '_' , ' ' ) , ( Oo0O0O0ooO0O ) . strip ( ) , 15 , Ii11iII1 , Ii11iII1 , '' )
  else :
   i1i1i11IIi = ( i1i1i11IIi ) . replace ('World','القنوات العربية')
   if i1i1i11IIi in iII :
    Oo0O0O0ooO0O = ( Oo0O0O0ooO0O ) . replace ( '.ts' , '.m3u8' )
    print Oo0O0O0ooO0O + '>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>'
    OO0o ( ( '' + name + '' ) . replace ( '_' , ' ' ) , ( Oo0O0O0ooO0O ) . strip ( ) , 15 , Ii11iII1 , Ii11iII1 , '' )
   else :
    pass
def o0 ( ) :
 O0OOO0OOoO0O ( )
 try :
  ooOooo000oOO = gui . TVGuide ( )
  ooOooo000oOO . doModal ( )
  del ooOooo000oOO
  if 59 - 59: II111iiii + OoooooooOO * OoOoOO00 + i1IIi
 except :
  import sys
  import traceback as tb
  ( Oo0OoO00oOO0o , OOO00O , traceback ) = sys . exc_info ( )
  tb . print_exception ( Oo0OoO00oOO0o , OOO00O , traceback )
  if 84 - 84: oO0o * OoO0O00 / I11i - O0
def iI1iI1I1i1I ( url ) :
 IiI1 = urllib2 . Request ( url )
 IiI1 . add_header ( 'User-Agent' , 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3' )
 Oo0O00Oo0o0 = urllib2 . urlopen ( IiI1 )
 O00O0oOO00O00 = Oo0O00Oo0o0 . read ( )
 Oo0O00Oo0o0 . close ( )
 return O00O0oOO00O00
 if 11 - 11: i1I1i1Ii11 . I1ii11iIi11i
 if 92 - 92: ooOoo0O . IIIIII11i1I
 if 31 - 31: IIIIII11i1I . OoOoOO00 / O0
def O0OOO0OOoO0O ( ) :
 o000O0o = os . path . join ( oO0o0o0ooO0oO , 'addons.ini' )
 iI1iII1 = open ( o000O0o , "w+" )
 II1III = iI1iI1I1i1I ( 'http://sptvserver.nl:8000/get.php?username=' + o0oOoO00o + '&password=' + i1 + '&type=m3u_plus&output=m3u8' )
 iIi11Ii1 = re . compile ( '#EXTINF:.+? tvg-name="([^"]*)" tvg-logo="([^"]*)" group-title="([^"]*)",.+?\n(.+?).ts' ) . findall ( II1III )
 iI1iII1 . write ( r'[' + IiiIII111iI + ']' + '\n' )
 for oO0OOoo0OO , Ii11iII1 , iII , Oo0O0O0ooO0O in iIi11Ii1 :
  Oo0O0O0ooO0O = ( Oo0O0O0ooO0O + '.m3u8' ) . replace ( ':' , '%3A' ) . replace ( '/' , '%2F' )
  O0ii1ii1ii = ( oO0OOoo0OO + '=plugin://' + IiiIII111iI + '/?url=' + Oo0O0O0ooO0O + '&mode=15&name=' + ( oO0OOoo0OO ) . replace ( ' ' , '+' ) + '&amp;iconimage=' + ( Ii11iII1 ) . replace ( ' ' , '' ) + '+&amp;fanart=' + ( Ii11iII1 ) . replace ( ' ' , '' ) + '+&amp;description=' )
  iI1iII1 . write ( O0ii1ii1ii + '\n' )
  if 91 - 91: i1I1i1Ii11
  if 15 - 15: II111iiii
def Ii ( url ) :
 import urlresolver
 try :
  ooo0O = urlresolver . resolve ( url ) . strip ( )
  xbmc . Player ( ) . play ( ooo0O , xbmcgui . ListItem ( oO0OOoo0OO ) )
 except :
  try :
   xbmc . Player ( ) . play ( url , xbmcgui . ListItem ( oO0OOoo0OO ) )
  except :
   xbmcgui . Dialog ( ) . notification ( "SpinzTV" , "unplayable stream" )
   sys . exit ( )
   if 75 - 75: o0oOOo0O0Ooo % o0oOOo0O0Ooo . IIIIII11i1I
   if 5 - 5: o0oOOo0O0Ooo * o0o0OOO0o0 + OoOoOO00 . OOooOOo + OoOoOO00
def oOiIi1IIIi1 ( ) :
 try :
  O0oOoOOOoOO = getSet ( "core-player" )
  if ( O0oOoOOOoOO == 'DVDPLAYER' ) : ii1ii11IIIiiI = xbmc . PLAYER_CORE_DVDPLAYER
  elif ( O0oOoOOOoOO == 'MPLAYER' ) : ii1ii11IIIiiI = xbmc . PLAYER_CORE_MPLAYER
  elif ( O0oOoOOOoOO == 'PAPLAYER' ) : ii1ii11IIIiiI = xbmc . PLAYER_CORE_PAPLAYER
  else : ii1ii11IIIiiI = xbmc . PLAYER_CORE_AUTO
 except : ii1ii11IIIiiI = xbmc . PLAYER_CORE_AUTO
 return ii1ii11IIIiiI
 return True
 if 67 - 67: I11i * oO0o * I1ii11iIi11i + OOooOOo / i1IIi
 if 11 - 11: Ii1I + ooOoo0O - o0o0OOO0o0 * oO0o % i11iIiiIii - IIIIII11i1I
def Iii1i1I11I ( name , url , mode , iconimage , fanart , description ) :
 if 83 - 83: I11i / I1IiiI
 iIIiIi1iIII1 = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart ) + "&description=" + urllib . quote_plus ( description )
 Ooo = True
 OOOOo = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 OOOOo . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description } )
 OOOOo . setProperty ( "Fanart_Image" , fanart )
 Ooo = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = iIIiIi1iIII1 , listitem = OOOOo , isFolder = True )
 return Ooo
 if 76 - 76: OoO0O00
def OO0o ( name , url , mode , iconimage , fanart , description ) :
 if 29 - 29: OOooOOo + Oo0Ooo . i11iIiiIii - i1IIi / iIii1I11I1II1
 iIIiIi1iIII1 = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart ) + "&description=" + urllib . quote_plus ( description )
 Ooo = True
 OOOOo = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 OOOOo . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description } )
 OOOOo . setProperty ( "Fanart_Image" , fanart )
 Ooo = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = iIIiIi1iIII1 , listitem = OOOOo , isFolder = False )
 return Ooo
 if 26 - 26: I11i . OoooooooOO
def I11i1ii1 ( ) :
 O0Oooo0O = [ ]
 O0o = sys . argv [ 2 ]
 if len ( O0o ) >= 2 :
  OoOooO = sys . argv [ 2 ]
  II111iiiI1Ii = OoOooO . replace ( '?' , '' )
  if ( OoOooO [ len ( OoOooO ) - 1 ] == '/' ) :
   OoOooO = OoOooO [ 0 : len ( OoOooO ) - 2 ]
  o0O0OOO0Ooo = II111iiiI1Ii . split ( '&' )
  O0Oooo0O = { }
  for iiIiI in range ( len ( o0O0OOO0Ooo ) ) :
   I1 = { }
   I1 = o0O0OOO0Ooo [ iiIiI ] . split ( '=' )
   if ( len ( I1 ) ) == 2 :
    O0Oooo0O [ I1 [ 0 ] ] = I1 [ 1 ]
    if 86 - 86: OoOoOO00 - Ii1I - OoO0O00 * ooOoo0O
 return O0Oooo0O
 if 66 - 66: OoooooooOO + O0
 if 11 - 11: I11i + OoooooooOO - OoO0O00 / o0oOOo0O0Ooo + Oo0Ooo . II111iiii
OoOooO = I11i1ii1 ( )
Oo0O0O0ooO0O = None
oO0OOoo0OO = None
i1Iii1i1I = None
OOoO00 = None
IiI111111IIII = None
i1Ii = None
ii111iI1iIi1 = None
if 78 - 78: OoO0O00 . OOooOOo + OoO0O00 / I11i / OoO0O00
if 54 - 54: OoOoOO00 % ooOoo0O
try :
 ii111iI1iIi1 = int ( OoOooO [ "fav_mode" ] )
except :
 pass
 if 37 - 37: OoOoOO00 * Oo0Ooo / o0o0OOO0o0 - ooOoo0O % II111iiii . oO0o
try :
 Oo0O0O0ooO0O = urllib . unquote_plus ( OoOooO [ "url" ] )
except :
 pass
try :
 oO0OOoo0OO = urllib . unquote_plus ( OoOooO [ "name" ] )
except :
 pass
try :
 OOoO00 = urllib . unquote_plus ( OoOooO [ "iconimage" ] )
except :
 pass
try :
 i1Iii1i1I = int ( OoOooO [ "mode" ] )
except :
 pass
try :
 IiI111111IIII = urllib . unquote_plus ( OoOooO [ "fanart" ] )
except :
 pass
try :
 i1Ii = urllib . unquote_plus ( OoOooO [ "description" ] )
except :
 pass
 if 88 - 88: ooOoo0O . II111iiii * II111iiii % IIIIII11i1I
 if 15 - 15: i1IIi * I1IiiI + i11iIiiIii
print str ( i1iiIIiiI111 ) + ': ' + str ( oOo0oooo00o )
print "Mode: " + str ( i1Iii1i1I )
print "URL: " + str ( Oo0O0O0ooO0O )
print "Name: " + str ( oO0OOoo0OO )
print "IconImage: " + str ( OOoO00 )
if 6 - 6: o0o0OOO0o0 / i11iIiiIii + ooOoo0O * oO0o
if 80 - 80: II111iiii
def O0O ( content , viewType ) :
 if 1 - 1: II111iiii
 if content :
  xbmcplugin . setContent ( int ( sys . argv [ 1 ] ) , content )
 if O0oo0OO0 . getSetting ( 'auto-view' ) == 'true' :
  xbmc . executebuiltin ( "Container.SetViewMode(%s)" % O0oo0OO0 . getSetting ( viewType ) )
  if 84 - 84: o0oOOo0O0Ooo % II111iiii . i11iIiiIii / OoO0O00
  if 80 - 80: IIIIII11i1I . i11iIiiIii - o0oOOo0O0Ooo
if i1Iii1i1I == None : OooO0 ( )
elif i1Iii1i1I == 11 : o0 ( )
elif i1Iii1i1I == 12 : II11iiii1Ii ( )
elif i1Iii1i1I == 13 : oo000OO00Oo ( )
elif i1Iii1i1I == 14 : oOOOoO0O00o0 ( oO0OOoo0OO )
elif i1Iii1i1I == 15 : Ii ( Oo0O0O0ooO0O )
elif i1Iii1i1I == 16 : Iii111II ( )
elif i1Iii1i1I == 17 : O0oo0OO0oOOOo ( oO0OOoo0OO )
elif i1Iii1i1I == 60000 : O0oo0OO0 . openSettings ( sys . argv [ 0 ] )
xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
# dd678faae9ac167bc83abf78e5cb2f3f0688d3a3