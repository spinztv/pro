# -*- coding: cp1252 -*-
import xbmc , xbmcaddon , xbmcgui , xbmcplugin , os , sys , xbmcvfs , glob
import shutil
import urllib2 , urllib , glob , traceback
import re
import fnmatch
import backuprestore
import plugintools
import base64
import time
import platform , subprocess
import zipfile
import yt
import ookla
import unicodedata
import urlresolver
import httplib
import requests
import urlparse
import binascii
import subprocess
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
try : from sqlite3 import dbapi2 as database
except : from pysqlite2 import dbapi2 as database
from datetime import date , datetime , timedelta
from resources . libs import extract , downloader , notify , debridit , traktit , loginit , skinSwitch , uploadLog , yt , wizard as wiz
if 64 - 64: i11iIiiIii
OO0o = xbmcaddon . Addon ( ) . getAddonInfo ( 'id' )
Oo0Ooo = 'plugin.program.SpinzTV'
O0O0OO0O0O0 = 'plugin.program.SpinzTV'
iiiii = 'SpinzTV'
ooo0OO = wiz . addonId ( OO0o )
Addon = xbmcaddon . Addon ( OO0o )
II1 = xbmc . translatePath ( 'special://home/addons/' )
O00ooooo00 = xbmc . translatePath ( 'special://home/addonsbroke/' )
I1IiiI = xbmcgui . DialogProgress ( )
IIi1IiiiI1Ii = "SpinzTv"
I11i11Ii = Net ( )
oO00oOo = base64 . decodestring
OOOo0 = ooo0OO . getSetting ( 'User' )
Oooo000o = ooo0OO . getSetting ( 'Pass' )
IiIi11iIIi1Ii = ooo0OO . getSetting ( 'AdultPass' )
Oo0O = Addon . getAddonInfo ( 'path' ) . decode ( "utf-8" )
IiI = xbmc . translatePath ( os . path . join ( Oo0O , "resources" , "iiNT3LiiList.txt" ) )
ooOo = wiz . addonInfo ( OO0o , 'version' )
Oo = wiz . addonInfo ( OO0o , 'path' )
o0O = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3'
IiiIII111iI = xbmcgui . Dialog ( )
IiII = xbmcgui . Dialog ( )
iI1Ii11111iIi = xbmcgui . DialogProgress ( )
i1i1II = xbmc . translatePath ( 'special://home/' )
O0oo0OO0 = ( oO00oOo ( 'aHR0cDovL2dlbmlldHYuY28udWsvc3Bpbnov' ) )
I1i1iiI1 = xbmc . translatePath ( 'special://home/userdata/addon_data/plugin.program.SpinzTV' )
iiIIIII1i1iI = xbmc . translatePath ( os . path . join ( 'special://home/addons/plugin.program.SpinzTV/imports/tvGuide/ResetDatabase.py' ) )
o0oO0 = xbmc . translatePath ( 'special://thumbnails' ) ;
oo00 = "Xhoans"
o00 = base64 . decodestring ( 'LnBocA==' )
Oo0oO0ooo = ooo0OO . getLocalizedString
o0oOoO00o = CookieJar ( )
i1 = urllib2 . build_opener ( urllib2 . HTTPCookieProcessor ( o0oOoO00o ) )
i1 . addheaders = [ ( 'User-Agent' , 'Mozilla/5.0' ) ]
oOOoo00O0O = int ( sys . argv [ 1 ] )
i1111 = xbmc . translatePath ( ooo0OO . getAddonInfo ( 'profile' ) . decode ( 'utf-8' ) )
i11 = xbmc . translatePath ( os . path . join ( 'special://home/userdata' , 'favourites.xml' ) )
I11 = I1i1iiI1 + '/addons.ini'
Oo0o0000o0o0 = xbmc . translatePath ( os . path . join ( '//storage//emulated//0//Download' , '' ) )
oOo0oooo00o = xbmc . translatePath ( 'special://logpath/' )
oO0o0o0ooO0oO = xbmc . translatePath ( 'special://profile/' )
II1 = os . path . join ( i1i1II , 'addons' )
zip = plugintools . get_setting ( "zip" )
oo0o0O00 = xbmc . translatePath ( os . path . join ( zip ) )
II1 = os . path . join ( i1i1II , 'addons' )
oO = os . path . join ( i1i1II , 'userdata' )
i1iiIIiiI111 = os . path . join ( II1 , OO0o )
oooOOOOO = os . path . join ( II1 , 'packages' )
i1iiIII111ii = os . path . join ( oO , 'addon_data' )
i1iIIi1 = os . path . join ( oO , 'addon_data' , OO0o )
ii11iIi1I = os . path . join ( oO , 'advancedsettings.xml' )
iI111I11I1I1 = os . path . join ( oO , 'sources.xml' )
OOooO0OOoo = os . path . join ( oO , 'favourites.xml' )
iIii1 = os . path . join ( oO , 'profiles.xml' )
oOOoO0 = os . path . join ( oO , 'guisettings.xml' )
O0OoO000O0OO = os . path . join ( oO , 'Thumbnails' )
iiI1IiI = os . path . join ( oO , 'Database' )
II = os . path . join ( i1iiIIiiI111 , 'fanart.jpg' )
ooOoOoo0O = os . path . join ( i1iiIIiiI111 , 'icon.png' )
OooO0 = os . path . join ( i1iiIIiiI111 , 'resources' , 'art' )
II11iiii1Ii = os . path . join ( i1iIIi1 , 'wizard.log' )
OO0oOoo = xbmc . getSkinDir ( )
O0o0Oo = wiz . getS ( 'buildname' )
Oo00OOOOO = wiz . getS ( 'defaultskin' )
O0O = wiz . getS ( 'defaultskinname' )
O00o0OO = wiz . getS ( 'defaultskinignore' )
I11i1 = wiz . getS ( 'buildversion' )
iIi1ii1I1 = wiz . getS ( 'buildtheme' )
o0 = wiz . getS ( 'latestversion' )
I11II1i = wiz . getS ( 'show15' )
IIIII = wiz . getS ( 'show16' )
ooooooO0oo = wiz . getS ( 'show17' )
IIiiiiiiIi1I1 = wiz . getS ( 'adult' )
I1IIIii = wiz . getS ( 'showmaint' )
oOoOooOo0o0 = wiz . getS ( 'autoclean' )
OOOO = wiz . getS ( 'clearcache' )
OOO00 = wiz . getS ( 'clearpackages' )
iiiiiIIii = wiz . getS ( 'clearthumbs' )
O000OO0 = wiz . getS ( 'autocleanfeq' )
I11iii1Ii = wiz . getS ( 'delayautoclean' )
I1IIiiIiii = wiz . getS ( 'nextautocleanup' )
O000oo0O = wiz . getS ( 'includevideo' )
OOOOi11i1 = wiz . getS ( 'includeall' )
IIIii1II1II = wiz . getS ( 'includebob' )
i1I1iI = wiz . getS ( 'includephoenix' )
oo0OooOOo0 = wiz . getS ( 'includespecto' )
o0OO00oO = wiz . getS ( 'includegenesis' )
I11i1I1I = wiz . getS ( 'includeexodus' )
oO0Oo = wiz . getS ( 'includeonechan' )
oOOoo0Oo = wiz . getS ( 'includesalts' )
o00OO00OoO = wiz . getS ( 'includesaltslite' )
OOOO0OOoO0O0 = wiz . getS ( 'seperate' )
O0Oo000ooO00 = wiz . getS ( 'notify' )
oO0 = wiz . getS ( 'noteid' )
Ii1iIiII1ii1 = wiz . getS ( 'notedismiss' )
ooOooo000oOO = wiz . getS ( 'traktlastsave' )
Oo0oOOo = wiz . getS ( 'debridlastsave' )
Oo0OoO00oOO0o = wiz . getS ( 'keepfavourites' )
OOO00O = wiz . getS ( 'keepgui' )
OOoOO0oo0ooO = wiz . getS ( 'keepsources' )
O0o0O00Oo0o0 = wiz . getS ( 'keepprofiles' )
O00O0oOO00O00 = wiz . getS ( 'keepadvanced' )
i1Oo00 = wiz . getS ( 'keeptrakt' )
i1i = wiz . getS ( 'keepdebrid' )
iiI111I1iIiI = wiz . getS ( 'keeplogin' )
IIIi1I1IIii1II = wiz . getS ( 'loginlastsave' )
O0 = wiz . getS ( 'exodus' )
ii1ii1ii = wiz . getS ( 'salts' )
oooooOoo0ooo = wiz . getS ( 'saltshd' )
I1I1IiI1 = wiz . getS ( 'royalwe' )
III1iII1I1ii = wiz . getS ( 'velocity' )
oOOo0 = wiz . getS ( 'velocitykids' )
oo00O00oO = wiz . getS ( 'specto' )
iIiIIIi = wiz . getS ( 'trakt' )
ooo00OOOooO = wiz . getS ( 'realexodus' )
O00OOOoOoo0O = wiz . getS ( 'realspecto' )
O000OOo00oo = wiz . getS ( 'urlresolver' )
oo0OOo = wiz . getS ( 'developer' )
ooOOO00Ooo = ooo0OO . getSetting ( 'path' ) if not ooo0OO . getSetting ( 'path' ) == '' else 'special://home/'
IiIIIi1iIi = os . path . join ( ooOOO00Ooo , 'My_Builds' , '' )
O000OO0 = int ( float ( O000OO0 ) ) if O000OO0 . isdigit ( ) else 0
ooOOoooooo = date . today ( )
II1I = ooOOoooooo + timedelta ( days = 1 )
O0i1II1Iiii1I11 = ooOOoooooo + timedelta ( days = 3 )
IIII = float ( xbmc . getInfoLabel ( "System.BuildVersion" ) [ : 4 ] )
iiIiI = "Kodi"
o00oooO0Oo = 'plugin.video.exodus'
o0O0OOO0Ooo = 'plugin.video.velocity'
iiIiII1 = 'plugin.video.velocitykids'
OOO00O0O = 'plugin.video.salts'
iii = 'plugin.video.saltshd.lite'
oOooOOOoOo = 'plugin.video.theroyalwe'
i1Iii1i1I = 'plugin.video.specto'
OOoO00 = 'script.trakt'
IiI111111IIII = 'script.module.urlresolver'
i1Ii = os . path . join ( II1 , OOO00O0O )
ii111iI1iIi1 = os . path . join ( II1 , iii )
OOO = os . path . join ( II1 , o00oooO0Oo )
oo0OOo0 = os . path . join ( II1 , o0O0OOO0Ooo )
I11IiI = os . path . join ( II1 , iiIiII1 )
O0ooO0Oo00o = os . path . join ( II1 , oOooOOOoOo )
ooO0oOOooOo0 = os . path . join ( II1 , i1Iii1i1I )
i1I1ii11i1Iii = os . path . join ( II1 , OOoO00 )
I1IiiiiI = os . path . join ( II1 , IiI111111IIII )
o0OIiII = [ OO0o , 'repository.SpinzTV' , 'plugin.program.SpinzTV' , 'script.module.beautifulsoup' , 'script.module.beautifulsoup4' , 'script.module.urlresolver' , 'script.module.requests' , 'script.module.addon.common' , 'script.module.simplejson' , 'script.module.buggalo' , 'script.module.t0mm0.common' ]
if 25 - 25: IIOOOO0oo0 - O0ooO0o0O0O + oOoooo0O0Oo
o00ooO = 0
OO0OO0O00oO0 = ooOOoooooo + timedelta ( days = o00ooO )
if 55 - 55: oO0Oo0O0o . OO
I1iI1ii1II = 'http://spez.tv/spinz/wizardtxt/notify.txt'
if 57 - 57: oOOOOoo0OOO % ii1Ii1I1Ii11i / I111I1Iiii1i + oOOoo00O00o
O0O00Oo = 'Yes'
oooooo0O000o = 'SpinzTV'
if 64 - 64: Ii1iI1I1 . oOOOOOOo0O00o - iiIi111 . oOoOoo
iIi1ii = 'No'
if 58 - 58: Iii1I1i % i1III1I
OOOOoOoO0o0 = 'Thank you for choosing SpinzTV.\r\n\r\nContact us on facebook at http://facebook.com/groups/spinztv\r\n\r\nWebsite: www.spinztv.com'
if 69 - 69: oO00oOOoooO
IiIi11iI = 'No'
Oo0O00O000 = 'deepskyblue'
i11I1IiII1i1i = 'white'
oo = '[COLOR ' + Oo0O00O000 + ']%s[/COLOR]'
I1111i = '[COLOR ' + i11I1IiII1i1i + ']%s[/COLOR]'
iIIii = '[COLOR ' + Oo0O00O000 + ']%s[/COLOR]'
o00O0O = '[COLOR ' + Oo0O00O000 + ']Current Build:[/COLOR] [COLOR ' + i11I1IiII1i1i + ']%s[/COLOR]'
ii1iii1i = '[COLOR ' + Oo0O00O000 + ']Current Theme:[/COLOR] [COLOR ' + i11I1IiII1i1i + ']%s[/COLOR]'
Iii1I1111ii = 'No'
ooOoO00 = os . path . join ( OooO0 , 'mainticon.png' )
Ii1IIiI1i = os . path . join ( OooO0 , 'buildsicon.png' )
o0O00Oo0 = os . path . join ( OooO0 , 'contacticon.png' )
IiII111i1i11 = os . path . join ( OooO0 , 'apkicon.png' )
i111iIi1i1II1 = os . path . join ( OooO0 , 'saveicon.png' )
oooO = os . path . join ( OooO0 , 'trakticon.png' )
i1I1i111Ii = os . path . join ( OooO0 , 'realicon.png' )
ooo = os . path . join ( OooO0 , 'settingsicon.png' )
i1i1iI1iiiI = os . path . join ( OooO0 , 'spinzicon.png' )
Ooo0oOooo0 = os . path . join ( OooO0 , 'kodiicon.png' )
oOOOoo00 = os . path . join ( OooO0 , 'kodiicon.png' )
iiIiIIIiiI = os . path . join ( OooO0 , 'gamesicon.png' )
iiI1IIIi = os . path . join ( OooO0 , 'moviesicon.png' )
II11IiIi11 = os . path . join ( OooO0 , 'droidicon.png' )
IIOOO0O00O0OOOO = os . path . join ( OooO0 , 'speedicon.png' )
I1iiii1I = os . path . join ( OooO0 , 'proicon.png' )
OOo0 = os . path . join ( OooO0 , 'spinzicon.png' )
oO00ooooO0o = os . path . join ( OooO0 , 'spinzicon.png' )
oo0o = os . path . join ( OooO0 , 'spinzicon.png' )
o0oO0oooOoo = wiz . LOGFILES
I1III1111iIi = traktit . TRAKTID
I1i111I = debridit . DEBRIDID
Ooo = loginit . LOGINID
Oo0oo0O0o00O = 'http://tribeca.tvaddons.ag/tools/maintenance/modules/'
if 48 - 48: o0o0OoOo0O0OO / Ii1I11I + oo0 + I111I1Iiii1i - oOOOOoo0OOO . ii1Ii1I1Ii11i
if 84 - 84: oOoOoo - oO00oOOoooO / oo0
if 65 - 65: i1III1I / Iii1I1i / oOOoo00O00o
if 92 - 92: IIOOOO0oo0 - oO00oOOoooO . oOoOoo * i1III1I
I1iI = base64 . b64decode ( 'aHR0cDovL3NwZXoudHYvc3Bpbnovd2l6YXJkdHh0L3NwaW56d2l6YXJkMS50eHQ=' )
IIIIiIiIi1 = base64 . b64decode ( 'aHR0cDovL3NwZXoudHYvc3Bpbnovc3BlZWQvc3BlZWR0ZXN0LnR4dA==' )
I11iiiiI1i = base64 . b64decode ( 'aHR0cDovL3NwZXoudHYvc3BpbnovYXBrdHh0cy9TcGluemFway50eHQ=' )
iI1i11 = base64 . b64decode ( 'aHR0cDovL3NwZXoudHYvc3BpbnovdmlkZW90eHRzL2J1aWxkdmlkcy50eHQ=' )
if 66 - 66: IIOOOO0oo0 % oOOOOOOo0O00o + i11iIiiIii . oOOoo00O00o / i1III1I + oOOOOOOo0O00o
ooo00Ooo = base64 . b64decode ( 'aHR0cDovL2FmdGVybWF0aHdpemFyZC5uZXQvcmVwby93aXphcmQvYWRkb25zLnR4dA==' )
if 93 - 93: i11iIiiIii - oOOOOoo0OOO * oOOOOOOo0O00o * Iii1I1i % IIOOOO0oo0 + oOoooo0O0Oo
I1i1i1 = 'http://'
OoO0O00O0oo0O = base64 . b64decode ( 'aHR0cDovL3NwZXoudHYvc3BpbnovYXBrdHh0cy9TcGluelRWLWFway50eHQ=' )
I1IiI11 = base64 . b64decode ( 'aHR0cDovL3NwZXoudHYvc3BpbnovYXBrdHh0cy94eHhhcGtzLnR4dA==' )
iI1iiiiIii = base64 . b64decode ( 'aHR0cDovL3NwZXoudHYvc3BpbnovZW11bGF0b3Itcm9tdHh0L2VtdWxhdG9yLnR4dA==' )
iIiIiIiI = base64 . b64decode ( "aHR0cDovL3AuYnJvc2dpdC5wcm8vc3BpbnovZW11bGF0b3Itcm9tdHh0L1JPTVNUWFQvU05FU0EtQi50eHQ=" )
i11OOoo = base64 . b64decode ( "aHR0cDovL3AuYnJvc2dpdC5wcm8vc3BpbnovZW11bGF0b3Itcm9tdHh0L1JPTVNUWFQvU05FU0MtRS50eHQ=" )
iIIiiiI = base64 . b64decode ( "aHR0cDovL3AuYnJvc2dpdC5wcm8vc3BpbnovZW11bGF0b3Itcm9tdHh0L1JPTVNUWFQvU05FU0YtSC50eHQ=" )
oo0IiI111ii1ii = base64 . b64decode ( "aHR0cDovL3AuYnJvc2dpdC5wcm8vc3BpbnovZW11bGF0b3Itcm9tdHh0L1JPTVNUWFQvU05FU0ktSy50eHQ=" )
O0OOo = base64 . b64decode ( "aHR0cDovL3AuYnJvc2dpdC5wcm8vc3BpbnovZW11bGF0b3Itcm9tdHh0L1JPTVNUWFQvU05FU0wtTS50eHQ=" )
IiIII1 = base64 . b64decode ( "aHR0cDovL3AuYnJvc2dpdC5wcm8vc3BpbnovZW11bGF0b3Itcm9tdHh0L1JPTVNUWFQvU05FU04tTy50eHQ=" )
O0Oo000 = base64 . b64decode ( "aHR0cDovL3AuYnJvc2dpdC5wcm8vc3BpbnovZW11bGF0b3Itcm9tdHh0L1JPTVNUWFQvU05FU1AtUi50eHQ=" )
iiI11i1II = base64 . b64decode ( "aHR0cDovL3AuYnJvc2dpdC5wcm8vc3BpbnovZW11bGF0b3Itcm9tdHh0L1JPTVNUWFQvU05FU1MudHh0" )
OO0O0OOo0O = base64 . b64decode ( "aHR0cDovL3AuYnJvc2dpdC5wcm8vc3BpbnovZW11bGF0b3Itcm9tdHh0L1JPTVNUWFQvU05FU1QtVi50eHQ=" )
I1 = base64 . b64decode ( "aHR0cDovL3AuYnJvc2dpdC5wcm8vc3BpbnovZW11bGF0b3Itcm9tdHh0L1JPTVNUWFQvU05FU1ctWi50eHQ=" )
o0OooOOOOOO = base64 . b64decode ( "aHR0cDovL3AuYnJvc2dpdC5wcm8vc3BpbnovZW11bGF0b3Itcm9tdHh0L1JPTVNUWFQvTkVTQS1CLnR4dA==" )
OOooO0o0 = base64 . b64decode ( "aHR0cDovL3AuYnJvc2dpdC5wcm8vc3BpbnovZW11bGF0b3Itcm9tdHh0L1JPTVNUWFQvTkVTQy50eHQ=" )
iiIII1i = base64 . b64decode ( "aHR0cDovL3AuYnJvc2dpdC5wcm8vc3BpbnovZW11bGF0b3Itcm9tdHh0L1JPTVNUWFQvTkVTRC1FLnR4dA==" )
I1I = base64 . b64decode ( "aHR0cDovL3AuYnJvc2dpdC5wcm8vc3BpbnovZW11bGF0b3Itcm9tdHh0L1JPTVNUWFQvTkVTRi1HLnR4dA==" )
ooooO0oOoOOoO = base64 . b64decode ( "aHR0cDovL3AuYnJvc2dpdC5wcm8vc3BpbnovZW11bGF0b3Itcm9tdHh0L1JPTVNUWFQvTkVTSC1LLnR4dA==" )
I1i11i = base64 . b64decode ( "aHR0cDovL3AuYnJvc2dpdC5wcm8vc3BpbnovZW11bGF0b3Itcm9tdHh0L1JPTVNUWFQvTkVTTC1NLnR4dA==" )
IiIi = base64 . b64decode ( "aHR0cDovL3AuYnJvc2dpdC5wcm8vc3BpbnovZW11bGF0b3Itcm9tdHh0L1JPTVNUWFQvTkVTTi1RLnR4dA==" )
OOOOO0O00 = base64 . b64decode ( "aHR0cDovL3AuYnJvc2dpdC5wcm8vc3BpbnovZW11bGF0b3Itcm9tdHh0L1JPTVNUWFQvTkVTUi1TLnR4dA==" )
Iii = base64 . b64decode ( "aHR0cDovL3AuYnJvc2dpdC5wcm8vc3BpbnovZW11bGF0b3Itcm9tdHh0L1JPTVNUWFQvTkVTVC1WLnR4dA==" )
iIIiIiI1I1 = base64 . b64decode ( "aHR0cDovL3AuYnJvc2dpdC5wcm8vc3BpbnovZW11bGF0b3Itcm9tdHh0L1JPTVNUWFQvTkVTVy1aLnR4dA==" )
ooO = base64 . b64decode ( "aHR0cDovL3AuYnJvc2dpdC5wcm8vc3BpbnovZW11bGF0b3Itcm9tdHh0L1JPTVNUWFQvR0VOQS1CLnR4dA==" )
ii = base64 . b64decode ( "aHR0cDovL3AuYnJvc2dpdC5wcm8vc3BpbnovZW11bGF0b3Itcm9tdHh0L1JPTVNUWFQvR0VOQy1ELnR4dA==" )
OO0O0Ooo = base64 . b64decode ( "aHR0cDovL3AuYnJvc2dpdC5wcm8vc3BpbnovZW11bGF0b3Itcm9tdHh0L1JPTVNUWFQvR0VORS1HLnR4dA==" )
oOoO0 = base64 . b64decode ( "aHR0cDovL3AuYnJvc2dpdC5wcm8vc3BpbnovZW11bGF0b3Itcm9tdHh0L1JPTVNUWFQvR0VOSC1MLnR4dA==" )
Oo0 = base64 . b64decode ( "aHR0cDovL3AuYnJvc2dpdC5wcm8vc3BpbnovZW11bGF0b3Itcm9tdHh0L1JPTVNUWFQvR0VOTS1PLnR4dA==" )
oo0O0o00o0O = base64 . b64decode ( "aHR0cDovL3AuYnJvc2dpdC5wcm8vc3BpbnovZW11bGF0b3Itcm9tdHh0L1JPTVNUWFQvR0VOUC1SLnR4dA==" )
I11i1II = base64 . b64decode ( "aHR0cDovL3AuYnJvc2dpdC5wcm8vc3BpbnovZW11bGF0b3Itcm9tdHh0L1JPTVNUWFQvR0VOUy1ULnR4dA==" )
OooiiIi1i = base64 . b64decode ( "aHR0cDovL3AuYnJvc2dpdC5wcm8vc3BpbnovZW11bGF0b3Itcm9tdHh0L1JPTVNUWFQvR0VOVS1aLnR4dA==" )
I1i11111i1i11 = base64 . b64decode ( "aHR0cDovL3AuYnJvc2dpdC5wcm8vc3BpbnovZW11bGF0b3Itcm9tdHh0L1JPTVNUWFQvQVRSQS1CLnR4dA==" )
OOoOOO0 = base64 . b64decode ( "aHR0cDovL3AuYnJvc2dpdC5wcm8vc3BpbnovZW11bGF0b3Itcm9tdHh0L1JPTVNUWFQvQVRSQy1ELnR4dA==" )
I1I1i = base64 . b64decode ( "aHR0cDovL3AuYnJvc2dpdC5wcm8vc3BpbnovZW11bGF0b3Itcm9tdHh0L1JPTVNUWFQvQVRSRS1HLnR4dA==" )
I1IIIiIiIi = base64 . b64decode ( "aHR0cDovL3AuYnJvc2dpdC5wcm8vc3BpbnovZW11bGF0b3Itcm9tdHh0L1JPTVNUWFQvQVRSSC1MLnR4dA==" )
IIIII1 = base64 . b64decode ( "aHR0cDovL3AuYnJvc2dpdC5wcm8vc3BpbnovZW11bGF0b3Itcm9tdHh0L1JPTVNUWFQvQVRSTS1PLnR4dA==" )
iIi1Ii1i1iI = base64 . b64decode ( "aHR0cDovL3AuYnJvc2dpdC5wcm8vc3BpbnovZW11bGF0b3Itcm9tdHh0L1JPTVNUWFQvQVRSUC1SLnR4dA==" )
IIiI1 = base64 . b64decode ( "aHR0cDovL3AuYnJvc2dpdC5wcm8vc3BpbnovZW11bGF0b3Itcm9tdHh0L1JPTVNUWFQvQVRSUy1VLnR4dA==" )
i1iI1 = base64 . b64decode ( "aHR0cDovL3AuYnJvc2dpdC5wcm8vc3BpbnovZW11bGF0b3Itcm9tdHh0L1JPTVNUWFQvQVRSVi1aLnR4dA==" )
ii1 = base64 . b64decode ( "aHR0cDovL3AuYnJvc2dpdC5wcm8vc3BpbnovZW11bGF0b3Itcm9tdHh0L1JPTVNUWFQvTjY0QS1CLnR4dA==" )
I1IiiI1ii1i = base64 . b64decode ( "aHR0cDovL3AuYnJvc2dpdC5wcm8vc3BpbnovZW11bGF0b3Itcm9tdHh0L1JPTVNUWFQvTjY0Qy1FLnR4dA==" )
O0o = base64 . b64decode ( "aHR0cDovL3AuYnJvc2dpdC5wcm8vc3BpbnovZW11bGF0b3Itcm9tdHh0L1JPTVNUWFQvTjY0Ri1KLnR4dA==" )
oO0OoO00o = base64 . b64decode ( "aHR0cDovL3AuYnJvc2dpdC5wcm8vc3BpbnovZW11bGF0b3Itcm9tdHh0L1JPTVNUWFQvTjY0Sy1NLnR4dA==" )
II1iiiiII = base64 . b64decode ( "aHR0cDovL3AuYnJvc2dpdC5wcm8vc3BpbnovZW11bGF0b3Itcm9tdHh0L1JPTVNUWFQvTjY0Ti1SLnR4dA==" )
O0OoOO0oo0 = base64 . b64decode ( "aHR0cDovL3AuYnJvc2dpdC5wcm8vc3BpbnovZW11bGF0b3Itcm9tdHh0L1JPTVNUWFQvTjY0Uy1ULnR4dA==" )
oOO = base64 . b64decode ( "aHR0cDovL3AuYnJvc2dpdC5wcm8vc3BpbnovZW11bGF0b3Itcm9tdHh0L1JPTVNUWFQvTjY0Vi1aLnR4dA==" )
O0o0OO0000ooo = base64 . b64decode ( "aHR0cDovL3AuYnJvc2dpdC5wcm8vc3BpbnovZW11bGF0b3Itcm9tdHh0L1JPTVNUWFQvVEdBLUIudHh0" )
iIIII1iIIii = base64 . b64decode ( "aHR0cDovL3AuYnJvc2dpdC5wcm8vc3BpbnovZW11bGF0b3Itcm9tdHh0L1JPTVNUWFQvVEdDLUUudHh0" )
oOOO00o000o = base64 . b64decode ( "aHR0cDovL3AuYnJvc2dpdC5wcm8vc3BpbnovZW11bGF0b3Itcm9tdHh0L1JPTVNUWFQvVEdGLUkudHh0" )
iIi11i1 = base64 . b64decode ( "aHR0cDovL3AuYnJvc2dpdC5wcm8vc3BpbnovZW11bGF0b3Itcm9tdHh0L1JPTVNUWFQvVEdKLU0udHh0" )
oO00oo0o00o0o = base64 . b64decode ( "aHR0cDovL3AuYnJvc2dpdC5wcm8vc3BpbnovZW11bGF0b3Itcm9tdHh0L1JPTVNUWFQvVEdOLVEudHh0" )
IiIIIIIi = base64 . b64decode ( "aHR0cDovL3AuYnJvc2dpdC5wcm8vc3BpbnovZW11bGF0b3Itcm9tdHh0L1JPTVNUWFQvVEdSLVUudHh0" )
IiIi1iIIi1 = base64 . b64decode ( "aHR0cDovL3AuYnJvc2dpdC5wcm8vc3BpbnovZW11bGF0b3Itcm9tdHh0L1JPTVNUWFQvVEdWLVoudHh0" )
O0OoO0ooOO0o = base64 . b64decode ( "aHR0cDovL3AuYnJvc2dpdC5wcm8vc3BpbnovZW11bGF0b3Itcm9tdHh0L1JPTVNUWFQvTkRTQS50eHQ=" )
OoOo0oOooOoOO = base64 . b64decode ( "aHR0cDovL3AuYnJvc2dpdC5wcm8vc3BpbnovZW11bGF0b3Itcm9tdHh0L1JPTVNUWFQvTkRTQi50eHQ=" )
oo00ooOoO00 = base64 . b64decode ( "aHR0cDovL3AuYnJvc2dpdC5wcm8vc3BpbnovZW11bGF0b3Itcm9tdHh0L1JPTVNUWFQvTkRTQy50eHQ=" )
o00oOoOo0 = base64 . b64decode ( "aHR0cDovL3AuYnJvc2dpdC5wcm8vc3BpbnovZW11bGF0b3Itcm9tdHh0L1JPTVNUWFQvTkRTRC50eHQ=" )
o0O0O0ooo0oOO = base64 . b64decode ( "aHR0cDovL3AuYnJvc2dpdC5wcm8vc3BpbnovZW11bGF0b3Itcm9tdHh0L1JPTVNUWFQvTkRTRS1GLnR4dA==" )
oo000 = base64 . b64decode ( "aHR0cDovL3AuYnJvc2dpdC5wcm8vc3BpbnovZW11bGF0b3Itcm9tdHh0L1JPTVNUWFQvTkRTRy1ILnR4dA==" )
iiOoO = base64 . b64decode ( "aHR0cDovL3AuYnJvc2dpdC5wcm8vc3BpbnovZW11bGF0b3Itcm9tdHh0L1JPTVNUWFQvTkRTSS1KLnR4dA==" )
Iiiiii111i1ii = base64 . b64decode ( "aHR0cDovL3AuYnJvc2dpdC5wcm8vc3BpbnovZW11bGF0b3Itcm9tdHh0L1JPTVNUWFQvTkRTSy1MLnR4dA==" )
i1i1iII1 = base64 . b64decode ( "aHR0cDovL3AuYnJvc2dpdC5wcm8vc3BpbnovZW11bGF0b3Itcm9tdHh0L1JPTVNUWFQvTkRTTS50eHQ=" )
iii11i1IIII = base64 . b64decode ( "aHR0cDovL3AuYnJvc2dpdC5wcm8vc3BpbnovZW11bGF0b3Itcm9tdHh0L1JPTVNUWFQvTkRTTi1PLnR4dA==" )
Ii = base64 . b64decode ( "aHR0cDovL3AuYnJvc2dpdC5wcm8vc3BpbnovZW11bGF0b3Itcm9tdHh0L1JPTVNUWFQvTkRTUC1RLnR4dA==" )
o00iiI1Ii1 = base64 . b64decode ( "aHR0cDovL3AuYnJvc2dpdC5wcm8vc3BpbnovZW11bGF0b3Itcm9tdHh0L1JPTVNUWFQvTkRTUi50eHQ=" )
ii1i = base64 . b64decode ( "aHR0cDovL3AuYnJvc2dpdC5wcm8vc3BpbnovZW11bGF0b3Itcm9tdHh0L1JPTVNUWFQvTkRTUy50eHQ=" )
oOOoo = base64 . b64decode ( "aHR0cDovL3AuYnJvc2dpdC5wcm8vc3BpbnovZW11bGF0b3Itcm9tdHh0L1JPTVNUWFQvTkRTVC1VLnR4dA==" )
iII1111III1I = base64 . b64decode ( "aHR0cDovL3AuYnJvc2dpdC5wcm8vc3BpbnovZW11bGF0b3Itcm9tdHh0L1JPTVNUWFQvTkRTVi1aLnR4dA==" )
ii11i = base64 . b64decode ( "aHR0cDovL3AuYnJvc2dpdC5wcm8vc3BpbnovZW11bGF0b3Itcm9tdHh0L1JPTVNUWFQvUFNBLnR4dA==" )
O00oOo00o0o = base64 . b64decode ( "aHR0cDovL3AuYnJvc2dpdC5wcm8vc3BpbnovZW11bGF0b3Itcm9tdHh0L1JPTVNUWFQvUFNCLnR4dA==" )
O00oO0 = base64 . b64decode ( "aHR0cDovL3AuYnJvc2dpdC5wcm8vc3BpbnovZW11bGF0b3Itcm9tdHh0L1JPTVNUWFQvUFNDLUQudHh0" )
O0Oo00OoOo = base64 . b64decode ( "aHR0cDovL3AuYnJvc2dpdC5wcm8vc3BpbnovZW11bGF0b3Itcm9tdHh0L1JPTVNUWFQvUFNFLUYudHh0" )
ii1ii111 = base64 . b64decode ( "aHR0cDovL3AuYnJvc2dpdC5wcm8vc3BpbnovZW11bGF0b3Itcm9tdHh0L1JPTVNUWFQvUFNHLUoudHh0" )
i11111I1I = base64 . b64decode ( "aHR0cDovL3AuYnJvc2dpdC5wcm8vc3BpbnovZW11bGF0b3Itcm9tdHh0L1JPTVNUWFQvUFNLLU4udHh0" )
ii1Oo0000oOo = base64 . b64decode ( "aHR0cDovL3AuYnJvc2dpdC5wcm8vc3BpbnovZW11bGF0b3Itcm9tdHh0L1JPTVNUWFQvUFNPLVIudHh0" )
I11o0oO00oO0o0o0 = base64 . b64decode ( "aHR0cDovL3AuYnJvc2dpdC5wcm8vc3BpbnovZW11bGF0b3Itcm9tdHh0L1JPTVNUWFQvUFNTLVQudHh0" )
I1Iooooo = base64 . b64decode ( "aHR0cDovL3AuYnJvc2dpdC5wcm8vc3BpbnovZW11bGF0b3Itcm9tdHh0L1JPTVNUWFQvUFNVLVoudHh0" )
if 1 - 1: oo0 % oOOoo00O00o * ii1Ii1I1Ii11i
if 55 - 55: oOOoo00O00o
if 87 - 87: oOoooo0O0Oo % oO00oOOoooO . oOOOOoo0OOO / oo0
i1I1iIo0 = wiz . workingURL ( I1iI )
if 17 - 17: O0ooO0o0O0O . oOoooo0O0Oo / Iii1I1i % OO % oO0Oo0O0o / i11iIiiIii
if 58 - 58: ii1Ii1I1Ii11i . OO + iiIi111 - i11iIiiIii / OO / IIOOOO0oo0
if 85 - 85: oOOoo00O00o + oOoOoo
if 10 - 10: o0o0OoOo0O0OO / I111I1Iiii1i + oOOoo00O00o / oO0Oo0O0o
if 27 - 27: i1III1I
if 67 - 67: oOOOOoo0OOO
if 55 - 55: oOOOOOOo0O00o - oO00oOOoooO * Ii1iI1I1 + oOOoo00O00o * oOOoo00O00o * IIOOOO0oo0
if 91 - 91: Ii1I11I - oOoOoo % O0ooO0o0O0O - oOoooo0O0Oo % oo0
if 98 - 98: I111I1Iiii1i . I111I1Iiii1i * iiIi111 * OO * Ii1I11I
def oOooO0 ( ) :
 if Iii1I1111ii == 'Yes' :
  if wiz . workingURL ( WIZARDFILE ) == True :
   OOOoO000 = wiz . checkWizard ( 'version' )
   if OOOoO000 > ooOo : oOOOO ( '%s [v%s] [COLOR red][B][UPDATE v%s][/B][/COLOR]' % ( iiiii , ooOo , OOOoO000 ) , 'wizardupdate' , themeit = I1111i )
   else : oOOOO ( '%s [v%s]' % ( iiiii , ooOo ) , '' , themeit = I1111i )
  else : oOOOO ( '%s [v%s]' % ( iiiii , ooOo ) , '' , themeit = I1111i )
 else : oOOOO ( '%s [v%s]' % ( iiiii , ooOo ) , '' , themeit = I1111i )
 if len ( O0o0Oo ) > 0 :
  IiIi1ii111i1 = wiz . checkBuild ( O0o0Oo , 'version' )
  i1i1i1I = '%s (v%s)' % ( O0o0Oo , I11i1 )
  if IiIi1ii111i1 > I11i1 : i1i1i1I = '%s [COLOR red][B][UPDATE v%s][/B][/COLOR]' % ( i1i1i1I , IiIi1ii111i1 )
  oOoo000 ( i1i1i1I , 'viewbuild' , O0o0Oo , themeit = o00O0O )
  OooOo00o = wiz . checkBuild ( O0o0Oo , 'theme' )
  if not OooOo00o == 'http://' and wiz . workingURL ( OooOo00o ) == True :
   oOOOO ( 'None' if iIi1ii1I1 == "" else iIi1ii1I1 , 'theme' , O0o0Oo , themeit = ii1iii1i )
 else : oOoo000 ( 'None' , 'builds' , themeit = o00O0O )
 if IiIi11iI == 'No' : oOOOO ( '============================================' , '' , themeit = iIIii )
 oOoo000 ( 'SpinzTV Builds' , 'builds' , icon = Ii1IIiI1i , themeit = oo )
 oOoo000 ( '[COLOR deepskyblue]SpinzTV[/COLOR] [COLOR red]PRO[/COLOR]' , 'pro' , icon = I1iiii1I , themeit = None )
 oOoo000 ( 'Maintenance' , 'maint' , icon = ooOoO00 , themeit = oo )
 oOOOO ( 'Speed Test' , 'speed' , icon = IIOOO0O00O0OOOO , themeit = oo )
 oOoo000 ( 'Android Zone' , 'apk1' , icon = IiII111i1i11 , themeit = oo )
 if not ooo00Ooo == 'http://' : IiI11i1IIiiI ( 'Addon Installer' , 'addons' , icon = OOo0 , themeit = oo )
 oOoo000 ( 'Save Data' , 'savedata' , icon = i111iIi1i1II1 , themeit = oo )
 if iIi1ii == 'No' : oOOOO ( 'Contact' , 'contact' , icon = o0O00Oo0 , themeit = oo )
 if IiIi11iI == 'No' : oOOOO ( '============================================' , '' , themeit = iIIii )
 oOOOO ( 'Settings' , 'settings' , icon = ooo , themeit = oo )
 if oo0OOo == 'true' : oOoo000 ( 'Developer Menu' , 'developer' , icon = ooo , themeit = oo )
 oOOo000oOoO0 ( 'movies' , 'MAIN' )
 if 86 - 86: OO % i11iIiiIii + i1III1I % i11iIiiIii
 if 92 - 92: i11iIiiIii - oO00oOOoooO / oo0 / iiIi111
 if 43 - 43: OO + oOoOoo + oO00oOOoooO
 if 40 - 40: Ii1iI1I1
def OOOooo ( ) :
 i1I1iIo0 = wiz . workingURL ( I1iI )
 if not i1I1iIo0 == True :
  Oo00oo0000OO ( '%s Version: %s' % ( iiIiI , IIII ) , '' , icon = Ii1IIiI1i , themeit = iIIii )
  if IiIi11iI == 'No' : oOOOO ( wiz . sep ( ) , '' , themeit = iIIii )
  Oo00oo0000OO ( 'Url for txt file not valid' , '' , icon = Ii1IIiI1i , themeit = iIIii )
  Oo00oo0000OO ( '%s' % i1I1iIo0 , '' , icon = Ii1IIiI1i , themeit = iIIii )
 else :
  O0oOOo0Oo = wiz . openURL ( I1iI ) . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' ) . replace ( 'gui=""' , 'gui="http://"' ) . replace ( 'theme=""' , 'theme="http://"' )
  o000O000 = re . compile ( 'name="(.+?)".+?ersion="(.+?)".+?rl="(.+?)".+?ui="(.+?)".+?odi="(.+?)".+?heme="(.+?)".+?con="(.+?)".+?anart="(.+?)".+?dult="(.+?)".+?escription="(.+?)"' ) . findall ( O0oOOo0Oo )
  if len ( o000O000 ) == 1 :
   ii1oOoO0o0ooo ( o000O000 [ 0 ] [ 0 ] )
  elif len ( o000O000 ) > 1 :
   Oo00oo0000OO ( '[B]%s Version: %s[/B]' % ( iiIiI , IIII ) , '' , icon = Ii1IIiI1i , themeit = I1111i )
   oOoo000 ( 'Video Preview Of Builds' , 'youtube' , url = iI1i11 , icon = i1i1iI1iiiI , themeit = oo )
   IiI11i1IIiiI ( 'Save Data Menu' , 'savedata' , icon = i111iIi1i1II1 , themeit = iIIii )
   if IiIi11iI == 'No' : oOOOO ( wiz . sep ( ) , '' , themeit = iIIii )
   if OOOO0OOoO0O0 == 'true' :
    for oO0o0O0Ooo0o , IiIi1ii111i1 , i1Ii11II , IioO0oOOO0Ooo , i1i1I , IiIIi1 , iII11I1Ii1 , o0o0 , oOo0oO , IIi1IIIIi in o000O000 :
     if not IIiiiiiiIi1I1 == 'true' and oOo0oO . lower ( ) == 'yes' : continue
     OOOoO = I1i ( 'install' , '' , oO0o0O0Ooo0o )
     IiI11i1IIiiI ( '[%s] %s (v%s)' % ( float ( i1i1I ) , oO0o0O0Ooo0o , IiIi1ii111i1 ) , 'viewbuild' , oO0o0O0Ooo0o , description = IIi1IIIIi , fanart = o0o0 , icon = iII11I1Ii1 , menu = OOOoO , themeit = I1111i )
   else :
    iiiI = wiz . buildCount ( '15' ) ; IiIi1 = wiz . buildCount ( '16' ) ; i111iiI1ii = wiz . buildCount ( '17' ) ;
    if i111iiI1ii > 0 :
     IIiii = '+' if ooooooO0oo == 'false' else '-'
     Oo00oo0000OO ( '[B]%s Krypton Builds(%s)[/B]' % ( IIiii , IiIi1 ) , 'togglesetting' , 'show17' , themeit = iIIii )
     if ooooooO0oo == 'true' :
      for oO0o0O0Ooo0o , IiIi1ii111i1 , i1Ii11II , IioO0oOOO0Ooo , i1i1I , IiIIi1 , iII11I1Ii1 , o0o0 , oOo0oO , IIi1IIIIi in o000O000 :
       if not IIiiiiiiIi1I1 == 'true' and oOo0oO . lower ( ) == 'yes' : continue
       I1i1i = int ( float ( i1i1I ) )
       if I1i1i == 17 :
        OOOoO = I1i ( 'install' , '' , oO0o0O0Ooo0o )
        IiI11i1IIiiI ( '[%s] %s (v%s)' % ( float ( i1i1I ) , oO0o0O0Ooo0o , IiIi1ii111i1 ) , 'viewbuild' , oO0o0O0Ooo0o , description = IIi1IIIIi , fanart = o0o0 , icon = iII11I1Ii1 , menu = OOOoO , themeit = I1111i )
    if IiIi1 > 0 :
     IIiii = '+' if IIIII == 'false' else '-'
     Oo00oo0000OO ( '[B]%s Jarvis Builds(%s)[/B]' % ( IIiii , IiIi1 ) , 'togglesetting' , 'show16' , themeit = iIIii )
     if IIIII == 'true' :
      for oO0o0O0Ooo0o , IiIi1ii111i1 , i1Ii11II , IioO0oOOO0Ooo , i1i1I , IiIIi1 , iII11I1Ii1 , o0o0 , oOo0oO , IIi1IIIIi in o000O000 :
       if not IIiiiiiiIi1I1 == 'true' and oOo0oO . lower ( ) == 'yes' : continue
       I1i1i = int ( float ( i1i1I ) )
       if I1i1i == 16 :
        OOOoO = I1i ( 'install' , '' , oO0o0O0Ooo0o )
        IiI11i1IIiiI ( '[%s] %s (v%s)' % ( float ( i1i1I ) , oO0o0O0Ooo0o , IiIi1ii111i1 ) , 'viewbuild' , oO0o0O0Ooo0o , description = IIi1IIIIi , fanart = o0o0 , icon = iII11I1Ii1 , menu = OOOoO , themeit = I1111i )
    if iiiI > 0 :
     IIiii = '+' if I11II1i == 'false' else '-'
     oOOOO ( '[B]%s Isengard and Below Builds(%s)[/B]' % ( IIiii , iiiI ) , 'togglesetting' , 'show15' , themeit = iIIii )
     if I11II1i == 'true' :
      for oO0o0O0Ooo0o , IiIi1ii111i1 , i1Ii11II , IioO0oOOO0Ooo , i1i1I , IiIIi1 , iII11I1Ii1 , o0o0 , oOo0oO , IIi1IIIIi in o000O000 :
       if not IIiiiiiiIi1I1 == 'true' and oOo0oO . lower ( ) == 'yes' : continue
       I1i1i = int ( float ( i1i1I ) )
       if I1i1i <= 15 :
        OOOoO = I1i ( 'install' , '' , oO0o0O0Ooo0o )
        IiI11i1IIiiI ( '[%s] %s (v%s)' % ( float ( i1i1I ) , oO0o0O0Ooo0o , IiIi1ii111i1 ) , 'viewbuild' , oO0o0O0Ooo0o , description = IIi1IIIIi , fanart = o0o0 , icon = iII11I1Ii1 , menu = OOOoO , themeit = I1111i )
  else : oOOOO ( 'Text file for builds not formated correctly.' , '' , icon = Ii1IIiI1i , themeit = iIIii )
 oOOo000oOoO0 ( 'files' , 'viewType' )
 if 86 - 86: ii1Ii1I1Ii11i / iiIi111 + IIOOOO0oo0 * oO00oOOoooO
def ii1oOoO0o0ooo ( name ) :
 i1I1iIo0 = wiz . workingURL ( I1iI )
 if not i1I1iIo0 == True :
  Oo00oo0000OO ( 'Url for txt file not valid' , '' , themeit = iIIii )
  Oo00oo0000OO ( '%s' % i1I1iIo0 , '' , themeit = iIIii )
  return
 if wiz . checkBuild ( name , 'version' ) == False :
  Oo00oo0000OO ( 'Error reading the txt file.' , '' , themeit = iIIii )
  Oo00oo0000OO ( '%s was not found in the builds list.' % name , '' , themeit = iIIii )
  return
 O0oOOo0Oo = wiz . openURL ( I1iI ) . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' ) . replace ( 'gui=""' , 'gui="http://"' ) . replace ( 'theme=""' , 'theme="http://"' )
 o000O000 = re . compile ( 'name="%s".+?ersion="(.+?)".+?rl="(.+?)".+?ui="(.+?)".+?odi="(.+?)".+?heme="(.+?)".+?con="(.+?)".+?anart="(.+?)".+?dult="(.+?)".+?escription="(.+?)"' % name ) . findall ( O0oOOo0Oo )
 for IiIi1ii111i1 , i1Ii11II , IioO0oOOO0Ooo , i1i1I , OooOo00o , iII11I1Ii1 , o0o0 , oOo0oO , IIi1IIIIi in o000O000 :
  iII11I1Ii1 = iII11I1Ii1 if wiz . workingURL ( iII11I1Ii1 ) else ooOoOoo0O
  o0o0 = o0o0 if wiz . workingURL ( o0o0 ) else II
  i1i1i1I = '%s (v%s)' % ( name , IiIi1ii111i1 )
  if O0o0Oo == name and IiIi1ii111i1 > I11i1 :
   i1i1i1I = '%s [COLOR red][CURRENT v%s][/COLOR]' % ( i1i1i1I , I11i1 )
  Oo00oo0000OO ( i1i1i1I , '' , description = IIi1IIIIi , fanart = o0o0 , icon = iII11I1Ii1 , themeit = o00O0O )
  if IiIi11iI == 'No' : oOOOO ( wiz . sep ( ) , '' , themeit = iIIii )
  Oo00oo0000OO ( 'Build Information' , 'buildinfo' , name , description = IIi1IIIIi , fanart = o0o0 , icon = iII11I1Ii1 , themeit = iIIii )
  IiI11i1IIiiI ( 'Save Data Menu' , 'savedata' , icon = i111iIi1i1II1 , themeit = iIIii )
  iiI11I1i1i1iI = int ( float ( IIII ) ) ; OoOOo000o0 = int ( float ( i1i1I ) )
  if not iiI11I1i1i1iI == OoOOo000o0 :
   if iiI11I1i1i1iI == 16 and OoOOo000o0 <= 15 : iiI1II11II1i = False
   else : iiI1II11II1i = True
  else : iiI1II11II1i = False
  if iiI1II11II1i == True :
   oOOOO ( '[I]Build designed for kodi version %s(installed: %s)[/I]' % ( str ( i1i1I ) , str ( IIII ) ) , '' , fanart = o0o0 , icon = iII11I1Ii1 , themeit = iIIii )
  Oo00oo0000OO ( wiz . sep ( 'INSTALL' ) , '' , fanart = o0o0 , icon = iII11I1Ii1 , themeit = iIIii )
  Oo00oo0000OO ( 'Fresh Install' , 'install' , name , 'fresh' , description = IIi1IIIIi , fanart = o0o0 , icon = iII11I1Ii1 , themeit = oo )
  Oo00oo0000OO ( 'Standard Install' , 'install' , name , 'normal' , description = IIi1IIIIi , fanart = o0o0 , icon = iII11I1Ii1 , themeit = oo )
  if not IioO0oOOO0Ooo == 'http://' : Oo00oo0000OO ( 'Apply guiFix' , 'install' , name , 'gui' , description = IIi1IIIIi , fanart = o0o0 , icon = iII11I1Ii1 , themeit = oo )
  if not OooOo00o == 'http://' :
   if wiz . workingURL ( OooOo00o ) == True :
    Oo00oo0000OO ( wiz . sep ( 'THEMES' ) , '' , fanart = o0o0 , icon = iII11I1Ii1 , themeit = iIIii )
    O0oOOo0Oo = wiz . openURL ( OooOo00o ) . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
    o000O000 = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?con="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( O0oOOo0Oo )
    for o0O0O0 , I11oo0ooOO , iI1IiIIiIIi , IiIi11Iii , IIi1IIIIi in o000O000 :
     iI1IiIIiIIi = iI1IiIIiIIi if iI1IiIIiIIi == 'http://' else iII11I1Ii1
     IiIi11Iii = IiIi11Iii if IiIi11Iii == 'http://' else o0o0
     Oo00oo0000OO ( o0O0O0 if not o0O0O0 == iIi1ii1I1 else "[B]%s (Installed)[/B]" % o0O0O0 , 'theme' , name , o0O0O0 , description = IIi1IIIIi , fanart = IiIi11Iii , icon = iI1IiIIiIIi , themeit = iIIii )
 oOOo000oOoO0 ( 'files' , 'viewType' )
 if 46 - 46: oOOoo00O00o - Iii1I1i - i1III1I . oO0Oo0O0o
 if 35 - 35: OO * Iii1I1i - oOoooo0O0Oo . Iii1I1i . Iii1I1i
 if 11 - 11: Ii1I11I / oOOoo00O00o + Iii1I1i % O0ooO0o0O0O
 if 42 - 42: oOOOOOOo0O00o * oOOoo00O00o % oo0 - oOOoo00O00o . i11iIiiIii - Ii1I11I
 if 84 - 84: Ii1I11I - oOOOOOOo0O00o / Iii1I1i
 if 13 - 13: o0o0OoOo0O0OO - ii1Ii1I1Ii11i - oo0
 if 92 - 92: oo0 / oOOoo00O00o * I111I1Iiii1i . Iii1I1i % OO
 if 71 - 71: Ii1I11I % oO0Oo0O0o - OO - oOoOoo + oOoOoo * oo0
 if 51 - 51: O0ooO0o0O0O / oOOoo00O00o + oOoOoo - Iii1I1i + oO00oOOoooO
 if 29 - 29: Ii1iI1I1 % O0ooO0o0O0O . oOoooo0O0Oo % oOoooo0O0Oo % OO / oO00oOOoooO
 if 70 - 70: i11iIiiIii % oO00oOOoooO
 if 11 - 11: o0o0OoOo0O0OO % oOOOOOOo0O00o % i1III1I / OO % Ii1I11I - ii1Ii1I1Ii11i
 if 96 - 96: oOOOOOOo0O00o / OO . i1III1I - oO00oOOoooO * Iii1I1i * iiIi111
 if 76 - 76: i1III1I - OO * oOoOoo / oOoooo0O0Oo
 if 18 - 18: I111I1Iiii1i + O0ooO0o0O0O - OO - oOOOOoo0OOO
 if 71 - 71: oOoooo0O0Oo
def iIIIII1iiiiII ( ) :
 oOoo000 ( 'Emulators And Roms' , 'emurom' , icon = iiIiIIIiiI , themeit = oo )
 oOoo000 ( 'SpinzTV APKS' , 'apkshow' , url = I11iiiiI1i , icon = i1i1iI1iiiI , themeit = oo )
 oOoo000 ( '[COLOR deepskyblue]APK Drawer[/COLOR]' , 'intellaunch' , )
 oOoo000 ( 'Kodi and SPMC' , 'apkkodi' , icon = Ooo0oOooo0 , themeit = oo )
 oooOI111i1I1 = O0o00OOo00O0O ( base64 . b64decode ( 'aHR0cHM6Ly93d3cuYXBrZmlsZXMuY29tLw==' ) )
 o000O000 = re . compile ( 'href="([^"]*)">Applications(.+?)</a>' ) . findall ( oooOI111i1I1 )
 II1i = re . compile ( 'href="([^"]*)">Games(.+?)</a>' ) . findall ( oooOI111i1I1 )
 for i1Ii11II , OoOOoO000O00oO in o000O000 :
  i1OoOO ( '[COLOR deepskyblue]Android Apps[/COLOR]' + OoOOoO000O00oO , 'https://www.apkfiles.com' + i1Ii11II , 'apkgame' , II11IiIi11 )
 for i1Ii11II , OoOOoO000O00oO in II1i :
  i1OoOO ( '[COLOR deepskyblue]Android Games[/COLOR]' + OoOOoO000O00oO , 'https://www.apkfiles.com' + i1Ii11II , 'apkgame' , iiIiIIIiiI )
 oOOo000oOoO0 ( 'movies' , 'MAIN' )
 oOoo000 ( 'Spinz Apk Picks' , 'apkshow' , url = OoO0O00O0oo0O , icon = IiII111i1i11 , themeit = oo )
 if IIiiiiiiIi1I1 == 'true' : oOoo000 ( 'XXX Apk' , 'apkshow' , url = I1IiI11 , icon = IiII111i1i11 , themeit = oo )
 if 44 - 44: oOoOoo
def O0O0o0o0o ( url ) :
 if not IIIIIiI ( url ) == True : return False
 O0oOOo0Oo = O0o00OOo00O0O ( url ) . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
 o000O000 = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?con="(.+?)".+?anart="(.+?)"' ) . findall ( O0oOOo0Oo )
 if len ( o000O000 ) > 0 :
  for oO0o0O0Ooo0o , url , iII11I1Ii1 , o0o0 in o000O000 :
   oOOOO ( oO0o0O0Ooo0o , 'apkinstall' , oO0o0O0Ooo0o , url , icon = iII11I1Ii1 , fanart = o0o0 , themeit = oo )
  else : wiz . log ( "[APK Menu] ERROR: Invalid Format." )
 else : wiz . log ( "[APK Menu] ERROR: URL for emu list not working." )
 if 80 - 80: O0ooO0o0O0O * Ii1I11I % Iii1I1i % ii1Ii1I1Ii11i
def OooOO0o0 ( url ) :
 oooOI111i1I1 = O0o00OOo00O0O ( url )
 o000O000 = re . compile ( '<a href="([^"]*)" >(.+?)</a>' ) . findall ( oooOI111i1I1 )
 for url , oO0o0O0Ooo0o in o000O000 :
  if '/cat' in url :
   i1OoOO ( ( oO0o0O0Ooo0o ) . replace ( '&amp;' , ' - ' ) , 'https://www.apkfiles.com' + url , 'select' , OooO0 + 'APK.png' )
   if 91 - 91: iiIi111 + oOoooo0O0Oo - oO0Oo0O0o
def o000 ( url ) :
 oooOI111i1I1 = O0o00OOo00O0O ( url )
 OOooo0O = url
 if "page=" in str ( url ) :
  OOooo0O = url . split ( '?' ) [ 0 ]
 o000O000 = re . compile ( '<a href="([^"]*)".+?<img src="([^"]*)" class="file_list_icon".+?alt="([^"]*)"' , re . DOTALL ) . findall ( oooOI111i1I1 )
 II1i = re . compile ( 'class="[^"]*".+?ref="([^"]*)".+?yle=.+?</a>' ) . findall ( oooOI111i1I1 )
 for url , iiI1iIIiI , oO0o0O0Ooo0o in o000O000 :
  if 'apk' in url :
   i1OoOO ( ( oO0o0O0Ooo0o ) . replace ( '&#39;' , '' ) . replace ( '&amp;' , ' - ' ) . replace ( '&#174;:' , ': ' ) . replace ( '&#174;' , ' ' ) , 'https://www.apkfiles.com' + url , 'grab' , 'http:' + iiI1iIIiI )
 if len ( II1i ) > 1 :
  II1i = str ( II1i [ len ( II1i ) - 1 ] )
 i1OoOO ( 'Next Page' , OOooo0O + str ( II1i ) , 'select' , OooO0 + 'Next.png' )
 if 57 - 57: I111I1Iiii1i / oO0Oo0O0o . oO0Oo0O0o
def oo00OOoOoO00 ( name , url ) :
 oooOI111i1I1 = O0o00OOo00O0O ( url )
 name = name
 o000O000 = re . compile ( 'href="([^"]*)".+?lass="yellow_button".+?itle=' ) . findall ( oooOI111i1I1 )
 for url in o000O000 :
  url = 'https://www.apkfiles.com' + url
  I1iii ( name , url , 'Brackets' )
  if 51 - 51: oOOOOOOo0O00o
def III1I1Ii11iI ( ) :
 oOOOO ( 'Kodi (v%s)' % wiz . latestApk ( 'kodi' , 'version' ) , 'apkinstall' , 'kodi' , wiz . latestApk ( 'kodi' , 'url' ) , icon = Ooo0oOooo0 , themeit = oo )
 oOOOO ( 'SPMC (v%s)' % wiz . latestApk ( 'spmc' , 'version' ) , 'apkinstall' , 'spmc' , wiz . latestApk ( 'spmc' , 'url' ) , icon = oOOOoo00 , themeit = oo )
 if 52 - 52: oOoOoo - oO00oOOoooO * iiIi111
 if 17 - 17: oOoooo0O0Oo + oOoOoo * Iii1I1i * oOOoo00O00o
 if 36 - 36: IIOOOO0oo0 + ii1Ii1I1Ii11i
 if 5 - 5: ii1Ii1I1Ii11i * oOOoo00O00o
def ii1I11iIiIII1 ( ) :
 if 52 - 52: Ii1iI1I1 * o0o0OoOo0O0OO + oOOoo00O00o
 if os . path . isfile ( IiI ) :
  IiiiIiiI = True
  o00O = open ( IiI )
  i1iIIi = o00O . read ( )
  o00O . close ( )
 else :
  xbmcgui . Dialog ( ) . ok ( "[COLOR orange]SpinzTV[/COLOR]" , "[COLOR cyan][B]][[/B]NT3L[B]][[/B]G3NC[B]][[/B][/COLOR]" , "[COLOR ghostwhite]First Time Launching Will Take a Couple Minutes[/COLOR]" , "[COLOR ghostwhite]Please Be Patient![/COLOR]" )
  IiiiIiiI = False
  if 58 - 58: OO
  if 19 - 19: oOOOOOOo0O00o - Iii1I1i . OO - I111I1Iiii1i . o0o0OoOo0O0OO * oOoooo0O0Oo
  if 84 - 84: oO00oOOoooO % oOoOoo / Iii1I1i / oOOOOoo0OOO
  if 46 - 46: ii1Ii1I1Ii11i / oO0Oo0O0o . Ii1iI1I1 * I111I1Iiii1i
  if 15 - 15: oOOoo00O00o
  if 62 - 62: i1III1I
  if 51 - 51: oOOoo00O00o
  if 14 - 14: o0o0OoOo0O0OO % iiIi111 % ii1Ii1I1Ii11i - i11iIiiIii
  if 53 - 53: i1III1I % ii1Ii1I1Ii11i
  if 59 - 59: oOoOoo % O0ooO0o0O0O . oO0Oo0O0o + OO * o0o0OoOo0O0OO
  if 41 - 41: i1III1I % oOOOOOOo0O00o
 i1iIiIi1I = ""
 i1I1IIIiiI = OO0O0ooOOO00 ( )
 for IiIiiiiI1 in i1I1IIIiiI :
  if IiiiIiiI == True :
   if IiIiiiiI1 not in i1iIIi :
    if 62 - 62: oOOOOOOo0O00o % oO00oOOoooO * I111I1Iiii1i - oO0Oo0O0o
    if 66 - 66: i11iIiiIii / Ii1iI1I1 - oOoooo0O0Oo / oO0Oo0O0o . i11iIiiIii
    IIIII1iii11 = IIi1I ( i1iIiIi1I , IiIiiiiI1 )
    i1iIiIi1I = IIIII1iii11
    if 27 - 27: IIOOOO0oo0 . Ii1I11I / oO00oOOoooO
  else :
   IIIII1iii11 = IIi1I ( i1iIiIi1I , IiIiiiiI1 )
   i1iIiIi1I = IIIII1iii11
   if 96 - 96: oOOOOOOo0O00o % oo0 % i1III1I - oo0 % oOOoo00O00o + oOOOOOOo0O00o
 if IiiiIiiI == True :
  o00O = open ( IiI , 'a' )
  if 3 - 3: IIOOOO0oo0
  if 64 - 64: oO0Oo0O0o % oo0 / i11iIiiIii - oO0Oo0O0o % oOoOoo . oO00oOOoooO
 else :
  o00O = open ( IiI , 'w' )
  if 8 - 8: ii1Ii1I1Ii11i + OO * oOoOoo * oOOoo00O00o * Iii1I1i / o0o0OoOo0O0OO
  if 21 - 21: iiIi111 / oOoooo0O0Oo
 o00O . write ( i1iIiIi1I )
 o00O . close ( )
 if 11 - 11: oOoOoo % i1III1I - i11iIiiIii - iiIi111 + oo0 + o0o0OoOo0O0OO
 if 87 - 87: Ii1I11I * oO0Oo0O0o / oOOOOOOo0O00o
 o00O = open ( IiI )
 i1iIIi = o00O . read ( )
 o00O . close ( )
 i1iIIi = i1iIIi . replace ( '\n' , '' ) . replace ( '\r' , '' )
 o000O000 = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)".+?nstallRating="(.+?)"' ) . findall ( i1iIIi )
 if 6 - 6: Ii1iI1I1 + ii1Ii1I1Ii11i - oOoooo0O0Oo % oOoOoo * oOOoo00O00o
 if 69 - 69: oO0Oo0O0o
 for oO0o0O0Ooo0o , i1Ii11II , ooOoOOOOo , o0o0 , IIi1IIIIi , ooooOooooOOo in sorted ( o000O000 , key = lambda o000O000 : o000O000 [ 0 ] ) :
  if i1Ii11II in i1I1IIIiiI :
   ooO00O00oOO ( '[COLOR ghostwhite]' + str ( oO0o0O0Ooo0o ) + '[/COLOR]' , i1Ii11II , 'intelselect' , ooOoOOOOo , o0o0 , IIi1IIIIi , ooooOooooOOo )
   if 40 - 40: oO00oOOoooO . iiIi111 + oOOOOoo0OOO + oOOOOOOo0O00o + Ii1I11I
def OO0O0ooOOO00 ( ) :
 if xbmc . getCondVisibility ( 'system.platform.android' ) :
  try :
   i1I1IIIiiI = subprocess . Popen ( [ 'exec ' '/system/bin/pm list packages -3' '' ] , executable = '/system/bin/sh' , shell = True , stdout = subprocess . PIPE , stderr = subprocess . STDOUT ) . communicate ( ) [ 0 ] . rstrip ( '\n' ) . splitlines ( )
  except :
   i1I1IIIiiI = [ ]
   if 26 - 26: O0ooO0o0O0O
  for IiIiiiiI1 in range ( len ( i1I1IIIiiI ) ) :
   i1I1IIIiiI [ IiIiiiiI1 ] = i1I1IIIiiI [ IiIiiiiI1 ] . partition ( ':' ) [ 2 ]
   if 87 - 87: oOOOOOOo0O00o / oOoooo0O0Oo - ii1Ii1I1Ii11i % oOOoo00O00o % o0o0OoOo0O0OO % ii1Ii1I1Ii11i
 return i1I1IIIiiI
 if 29 - 29: oOoooo0O0Oo . oOOOOoo0OOO % oOOOOOOo0O00o - oO00oOOoooO
def IIi1I ( theList , i ) :
 global theNotList
 iiii = "https://play.google.com/store/apps/details?id=" + i
 O0oOOo0Oo = o0OO0Oo ( iiii )
 if 3 - 3: Ii1I11I - IIOOOO0oo0 % O0ooO0o0O0O / o0o0OoOo0O0OO . Ii1iI1I1
 if O0oOOo0Oo != False :
  O0oOOo0Oo = O0oOOo0Oo . replace ( '\n' , '' ) . replace ( '\r' , '' )
  if 3 - 3: IIOOOO0oo0 % oOoooo0O0Oo / oOoOoo
  ooOoo0oO0OoO0 = r'<div class="id-app-title".tabindex=".">(.+?)</div>'
  o000O000 = re . search ( ooOoo0oO0OoO0 , O0oOOo0Oo )
  if o000O000 != None : oO0o0O0Ooo0o = o000O000 . group ( 1 )
  else : oO0o0O0Ooo0o = i
  if 70 - 70: iiIi111 - iiIi111
  if 57 - 57: oOOOOoo0OOO - Ii1iI1I1 + I111I1Iiii1i % ii1Ii1I1Ii11i
  if 26 - 26: oO00oOOoooO . oO00oOOoooO
  if 35 - 35: Ii1I11I . oOOoo00O00o * i11iIiiIii
  if 44 - 44: i11iIiiIii / ii1Ii1I1Ii11i
  ooOoOOOOo = "androidapp://sources/apps/" + str ( i ) + ".png"
  if 42 - 42: oOoooo0O0Oo + ii1Ii1I1Ii11i % OO + I111I1Iiii1i
  if 24 - 24: oO00oOOoooO * OO % oO00oOOoooO % o0o0OoOo0O0OO + oOoooo0O0Oo
  if 29 - 29: OO - oOoooo0O0Oo - i11iIiiIii . Ii1iI1I1
  if 19 - 19: OO
  if 72 - 72: oOoooo0O0Oo / oOOOOoo0OOO + i1III1I / oOOoo00O00o * i1III1I
  if 34 - 34: IIOOOO0oo0 * IIOOOO0oo0 % oOoooo0O0Oo + oO00oOOoooO * O0ooO0o0O0O % i1III1I
  I1iI1I1 = r'data-expand-to="full-screenshot-[0-9]{1,2}" src="(//\w+?.\w+?.\S+?=h900)"'
  o000O000 = re . compile ( I1iI1I1 ) . findall ( O0oOOo0Oo )
  if len ( o000O000 ) != 0 : o0o0 = "https:" + o000O000 [ len ( o000O000 ) - 1 ]
  else : o0o0 = "None"
  if 48 - 48: oOOOOoo0OOO / i11iIiiIii - Ii1iI1I1 * iiIi111 / oOoooo0O0Oo
  OoOo = r'data-video-url="https://www.youtube.com/embed/(\S.+?)\?ps=play.+?"'
  o000O000 = re . search ( OoOo , O0oOOo0Oo )
  if o000O000 != None : IIi1IIIIi = o000O000 . group ( 1 )
  else : IIi1IIIIi = "None"
  if 17 - 17: i1III1I . i11iIiiIii
  IIIiiiI = r'<div class="content" itemprop="numDownloads">\s+?(\d.+?\s-\s\d.+?)\s+?</div>'
  o000O000 = re . search ( IIIiiiI , O0oOOo0Oo )
  if o000O000 != None : OoO00oo00 = 'Installed ' + o000O000 . group ( 1 )
  else : OoO00oo00 = "Installs: N/A"
  if 76 - 76: oOoooo0O0Oo + ii1Ii1I1Ii11i % o0o0OoOo0O0OO . I111I1Iiii1i + OO
  oO0o = r'<div class="score" aria-label=" Rated .+? stars out of five stars ">(.+?)</div>'
  o000O000 = re . search ( oO0o , O0oOOo0Oo )
  if o000O000 != None : OooooOoO = o000O000 . group ( 1 ) + " Stars"
  else : OooooOoO = "Rating: N/A"
  ooooOooooOOo = OooooOoO + " " + OoO00oo00
  if 38 - 38: o0o0OoOo0O0OO . i1III1I
  if 24 - 24: Ii1iI1I1 - Ii1iI1I1 + oOOOOOOo0O00o + oOOOOoo0OOO - iiIi111
  if 12 - 12: oO00oOOoooO . o0o0OoOo0O0OO . oOOoo00O00o / IIOOOO0oo0
  i1Ii11II = i
  theList += 'name="' + oO0o0O0Ooo0o + '"url="' + i1Ii11II + '"img="' + ooOoOOOOo + '"fanart="' + o0o0 + '"description="' + IIi1IIIIi + '"installRating="' + ooooOooooOOo + '"'
  return theList
  if 58 - 58: Ii1iI1I1 - OO % iiIi111 + Ii1I11I . oOOoo00O00o / o0o0OoOo0O0OO
  if 8 - 8: oOOOOOOo0O00o . I111I1Iiii1i * Iii1I1i + OO % i11iIiiIii
  if 8 - 8: oo0 * IIOOOO0oo0
  if 73 - 73: Ii1iI1I1 / iiIi111 / Iii1I1i / I111I1Iiii1i
  if 11 - 11: oOOoo00O00o + o0o0OoOo0O0OO - oOoooo0O0Oo / I111I1Iiii1i
  if 34 - 34: oo0
  if 45 - 45: oo0 / ii1Ii1I1Ii11i / i1III1I
  if 44 - 44: oOOOOOOo0O00o - i1III1I / OO * I111I1Iiii1i * ii1Ii1I1Ii11i
  if 73 - 73: Ii1iI1I1 - oOOOOoo0OOO * oO0Oo0O0o / i11iIiiIii * oOoOoo % OO
 else :
  if 56 - 56: oOoooo0O0Oo * ii1Ii1I1Ii11i . ii1Ii1I1Ii11i . oOOOOOOo0O00o
  return theList
  if 24 - 24: ii1Ii1I1Ii11i . Iii1I1i * i1III1I % oO00oOOoooO / oOoOoo
def Oo0Ooo0O0 ( name , url , iconimage , fanart , videolink ) :
 IiIIi1IiiIiI = 0
 if 23 - 23: Iii1I1i
 if videolink != "None" :
  IiIIi1IiiIiI += 1
  if 40 - 40: Ii1iI1I1 - OO / ii1Ii1I1Ii11i
 if IiIIi1IiiIiI == 1 : iiIiI1ii = xbmcgui . Dialog ( ) . select ( '[COLOR deepskyblue]' + name + '[/COLOR]' , [ '[COLOR deepskyblue]Launch[/COLOR]' , '[COLOR ghostwhite]Preview Video[/COLOR]' , '[COLOR tomato]Uninstall[/COLOR]' ] )
 if IiIIi1IiiIiI == 0 : iiIiI1ii = xbmcgui . Dialog ( ) . select ( '[COLOR deepskyblue]' + name + '[/COLOR]' , [ '[COLOR deepskyblue]Launch[/COLOR]' , '[COLOR ghostwhite]No Preview Video[/COLOR]' , '[COLOR tomato]Uninstall[/COLOR]' ] )
 if 56 - 56: oOoooo0O0Oo - Iii1I1i - oO0Oo0O0o
 if 8 - 8: Ii1I11I / oOoOoo . oOOOOoo0OOO + oOOOOOOo0O00o / i11iIiiIii
 if 31 - 31: oo0 - O0ooO0o0O0O + oO00oOOoooO . ii1Ii1I1Ii11i / o0o0OoOo0O0OO % O0ooO0o0O0O
 if iiIiI1ii == 1 :
  if videolink != 'None' :
   yt . PlayVideo ( videolink )
 if iiIiI1ii == 0 :
  I11i1iIiiIiIi = xbmcgui . Dialog ( ) . yesno ( "[COLOR orange]SpinzTV[/COLOR]" , "[COLOR cyan][B]][[/B]NT3L[B]][[/B]G3NC[B]][[/B][/COLOR]" , "" , "[COLOR ghostwhite]Would You Like To Launch:[/COLOR] [COLOR cyan]" + name + "[/COLOR]" , "[COLOR red]No Way[/COLOR]" , "[COLOR cyan]Heck Ya![/COLOR]" )
  if I11i1iIiiIiIi == 1 :
   xbmc . executebuiltin ( 'StartAndroidActivity(%s)' % url )
 if iiIiI1ii == 2 :
  I1iOo = xbmcgui . Dialog ( ) . yesno ( "[COLOR orange]SpinzTV[/COLOR]" , "[COLOR cyan][B]][[/B]NT3L[B]][[/B]G3NC[B]][[/B][/COLOR]" , "" , "[COLOR ghostwhite]Would You Like To Remove:[/COLOR] [COLOR cyan]" + name + "[/COLOR]" , "[COLOR red]No Way[/COLOR]" , "[COLOR cyan]Heck Ya![/COLOR]" )
  if I1iOo :
   xbmc . executebuiltin ( 'StartAndroidActivity("","android.intent.action.DELETE","","package:' + url + '")' )
   xbmc . sleep ( 2000 )
   try : shutil . rmtree ( "/sdcard/Android/data/" + url , ignore_errors = True , onerror = None )
   except : pass
   try : shutil . rmtree ( "/sdcard/Android/obb/" + url , ignore_errors = True , onerror = None )
   except : pass
   xbmc . executebuiltin ( 'Container.Refresh' )
   if 29 - 29: IIOOOO0oo0 - i11iIiiIii - OO + oOoOoo * o0o0OoOo0O0OO
def o0OO0Oo ( url ) :
 try :
  IiI1ii1Ii = urllib2 . Request ( url )
  IiI1ii1Ii . add_header ( 'User-Agent' , 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3' )
  oooOOOoOOOo0O = urllib2 . urlopen ( IiI1ii1Ii )
  O0oOOo0Oo = oooOOOoOOOo0O . read ( )
  oooOOOoOOOo0O . close ( )
  return O0oOOo0Oo
 except :
  return False
  if 82 - 82: o0o0OoOo0O0OO * i11iIiiIii % OO - oOoooo0O0Oo
  if 90 - 90: ii1Ii1I1Ii11i . iiIi111 * oO0Oo0O0o - oO0Oo0O0o
  if 16 - 16: oOOOOoo0OOO * oO0Oo0O0o - Ii1iI1I1 . o0o0OoOo0O0OO % Iii1I1i / Ii1iI1I1
def Ii11iI1ii1111 ( ) :
 oOoo000 ( 'Emulators' , 'apkshow' , url = iI1iiiiIii , icon = iiIiIIIiiI , themeit = oo )
 oOoo000 ( 'Roms' , 'roms' , icon = iiIiIIIiiI , themeit = oo )
 if 42 - 42: Ii1I11I + Ii1I11I * OO
 if 78 - 78: oOoooo0O0Oo
 if 77 - 77: oOOOOOOo0O00o / oO0Oo0O0o / ii1Ii1I1Ii11i % oOoOoo
 if 48 - 48: Iii1I1i - o0o0OoOo0O0OO + O0ooO0o0O0O + oOoooo0O0Oo
def IiI1i111IiIiIi1 ( ) :
 oOoo000 ( 'NES' , 'nes' , icon = iiIiIIIiiI , themeit = oo )
 oOoo000 ( 'SNES' , 'snes' , icon = iiIiIIIiiI , themeit = oo )
 oOoo000 ( 'Nintendo 64' , 'n64' , icon = iiIiIIIiiI , themeit = oo )
 oOoo000 ( 'Nintendo DS' , 'nds' , icon = iiIiIIIiiI , themeit = oo )
 oOoo000 ( 'Genesis' , 'gen' , icon = iiIiIIIiiI , themeit = oo )
 oOoo000 ( 'Playstation' , 'ps' , icon = iiIiIIIiiI , themeit = oo )
 oOoo000 ( 'Atari' , 'atr' , icon = iiIiIIIiiI , themeit = oo )
 oOoo000 ( 'PC Engine & Turbo Grafx' , 'tbg' , icon = iiIiIIIiiI , themeit = oo )
 if 39 - 39: Iii1I1i - oOOOOOOo0O00o
def OOO0o0OO0OO ( url ) :
 if not IIIIIiI ( url ) == True : return False
 O0oOOo0Oo = O0o00OOo00O0O ( url ) . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
 o000O000 = re . compile ( '.+?ame="(.+?)".+?rl="(.+?)".+?con="(.+?)".+?anart="(.+?)"description="(.+?)"' ) . findall ( O0oOOo0Oo )
 if len ( o000O000 ) > 0 :
  for oO0o0O0Ooo0o , url , iII11I1Ii1 , o0o0 , IIi1IIIIi in o000O000 :
   oOo0O ( oO0o0O0Ooo0o , 'rominstall' , oO0o0O0Ooo0o , url , icon = iII11I1Ii1 , fanart = o0o0 , description = IIi1IIIIi , themeit = oo )
  else : wiz . log ( "[ROM Menu] ERROR: Invalid Format." )
 else : wiz . log ( "[ROM Menu] ERROR: URL for apk list not working." )
 if 43 - 43: Ii1iI1I1 . oO00oOOoooO . Iii1I1i + O0ooO0o0O0O
 if 78 - 78: O0ooO0o0O0O % oOOoo00O00o + oOOOOOOo0O00o / oO0Oo0O0o % OO + oOoOoo
 if 91 - 91: O0ooO0o0O0O % I111I1Iiii1i . Ii1iI1I1 + i1III1I + Ii1iI1I1
 if 95 - 95: i1III1I + oOOOOOOo0O00o * oOoOoo
def I1Ii ( ) :
 oOoo000 ( 'SNES Titles A Thru B' , 'rom' , url = iIiIiIiI , icon = iiIiIIIiiI , themeit = oo )
 oOoo000 ( 'SNES Titles C Thru E' , 'rom' , url = i11OOoo , icon = iiIiIIIiiI , themeit = oo )
 oOoo000 ( 'SNES Titles F Thru H' , 'rom' , url = iIIiiiI , icon = iiIiIIIiiI , themeit = oo )
 oOoo000 ( 'SNES Titles I Thru K' , 'rom' , url = oo0IiI111ii1ii , icon = iiIiIIIiiI , themeit = oo )
 oOoo000 ( 'SNES Titles L Thru M' , 'rom' , url = O0OOo , icon = iiIiIIIiiI , themeit = oo )
 oOoo000 ( 'SNES Titles N Thru O' , 'rom' , url = IiIII1 , icon = iiIiIIIiiI , themeit = oo )
 oOoo000 ( 'SNES Titles P Thru R' , 'rom' , url = O0Oo000 , icon = iiIiIIIiiI , themeit = oo )
 oOoo000 ( 'SNES Titles S' , 'rom' , url = iiI11i1II , icon = iiIiIIIiiI , themeit = oo )
 oOoo000 ( 'SNES Titles T Thru V' , 'rom' , url = OO0O0OOo0O , icon = iiIiIIIiiI , themeit = oo )
 oOoo000 ( 'SNES Titles W Thru Z' , 'rom' , url = I1 , icon = iiIiIIIiiI , themeit = oo )
 if 77 - 77: O0ooO0o0O0O - oO0Oo0O0o . iiIi111
 if 26 - 26: Ii1iI1I1 * o0o0OoOo0O0OO . oO0Oo0O0o
 if 59 - 59: IIOOOO0oo0 + oO0Oo0O0o - Ii1iI1I1
 if 62 - 62: i11iIiiIii % oOoOoo . o0o0OoOo0O0OO . oOoOoo
def ooOo0O0O0oOO0 ( ) :
 oOoo000 ( 'NES Titles A Thru B' , 'rom' , url = o0OooOOOOOO , icon = iiIiIIIiiI , themeit = oo )
 oOoo000 ( 'NES Titles C' , 'rom' , url = OOooO0o0 , icon = IiII111i1i11 , themeit = oo )
 oOoo000 ( 'NES Titles D Thru E' , 'rom' , url = iiIII1i , icon = iiIiIIIiiI , themeit = oo )
 oOoo000 ( 'NES Titles F Thru G' , 'rom' , url = I1I , icon = iiIiIIIiiI , themeit = oo )
 oOoo000 ( 'NES Titles H Thru K' , 'rom' , url = ooooO0oOoOOoO , icon = iiIiIIIiiI , themeit = oo )
 oOoo000 ( 'NES Titles L Thru M' , 'rom' , url = I1i11i , icon = iiIiIIIiiI , themeit = oo )
 oOoo000 ( 'NES Titles N Thru Q' , 'rom' , url = IiIi , icon = iiIiIIIiiI , themeit = oo )
 oOoo000 ( 'NES Titles R Thru S' , 'rom' , url = OOOOO0O00 , icon = iiIiIIIiiI , themeit = oo )
 oOoo000 ( 'NES Titles T Thru V' , 'rom' , url = Iii , icon = iiIiIIIiiI , themeit = oo )
 oOoo000 ( 'NES Titles W Thru Z' , 'rom' , url = iIIiIiI1I1 , icon = iiIiIIIiiI , themeit = oo )
 if 10 - 10: ii1Ii1I1Ii11i + IIOOOO0oo0
 if 43 - 43: O0ooO0o0O0O / OO % Ii1iI1I1 - oOoOoo
 if 62 - 62: Iii1I1i
 if 63 - 63: oOoOoo + oo0 * iiIi111 / Ii1iI1I1 / ii1Ii1I1Ii11i * O0ooO0o0O0O
 if 57 - 57: oOOoo00O00o - iiIi111 / oo0 % i11iIiiIii
def I11oOOooo ( ) :
 oOoo000 ( 'Genesis Titles A Thru B' , 'rom' , url = ooO , icon = iiIiIIIiiI , themeit = oo )
 oOoo000 ( 'Genesis Titles C Thru D' , 'rom' , url = ii , icon = IiII111i1i11 , themeit = oo )
 oOoo000 ( 'Genesis Titles E Thru G' , 'rom' , url = OO0O0Ooo , icon = iiIiIIIiiI , themeit = oo )
 oOoo000 ( 'Genesis Titles H Thru L' , 'rom' , url = oOoO0 , icon = iiIiIIIiiI , themeit = oo )
 oOoo000 ( 'Genesis Titles M Thru O' , 'rom' , url = Oo0 , icon = iiIiIIIiiI , themeit = oo )
 oOoo000 ( 'Genesis Titles P Thru R' , 'rom' , url = oo0O0o00o0O , icon = iiIiIIIiiI , themeit = oo )
 oOoo000 ( 'Genesis Titles S Thru T' , 'rom' , url = I11i1II , icon = iiIiIIIiiI , themeit = oo )
 oOoo000 ( 'Genesis Titles U Thru Z' , 'rom' , url = OooiiIi1i , icon = iiIiIIIiiI , themeit = oo )
 if 80 - 80: oOOOOoo0OOO - i11iIiiIii
 if 69 - 69: iiIi111 % oOoooo0O0Oo . oOOOOoo0OOO
 if 34 - 34: i1III1I * oOOoo00O00o - o0o0OoOo0O0OO - oOOOOoo0OOO - i1III1I
 if 42 - 42: OO * oOOOOoo0OOO % oO0Oo0O0o - i1III1I % o0o0OoOo0O0OO
 if 36 - 36: i11iIiiIii / iiIi111 * oOOOOOOo0O00o * oOOOOOOo0O00o + i1III1I * Iii1I1i
def iIiI1i ( ) :
 oOoo000 ( 'Atari Titles A Thru B' , 'rom' , url = I1i11111i1i11 , icon = iiIiIIIiiI , themeit = oo )
 oOoo000 ( 'Atari Titles C Thru D' , 'rom' , url = OOoOOO0 , icon = IiII111i1i11 , themeit = oo )
 oOoo000 ( 'Atari Titles E Thru G' , 'rom' , url = I1I1i , icon = iiIiIIIiiI , themeit = oo )
 oOoo000 ( 'Atari Titles H Thru L' , 'rom' , url = I1IIIiIiIi , icon = iiIiIIIiiI , themeit = oo )
 oOoo000 ( 'Atari Titles M Thru O' , 'rom' , url = IIIII1 , icon = iiIiIIIiiI , themeit = oo )
 oOoo000 ( 'Atari Titles P Thru R' , 'rom' , url = iIi1Ii1i1iI , icon = iiIiIIIiiI , themeit = oo )
 oOoo000 ( 'Atari Titles S Thru U' , 'rom' , url = IIiI1 , icon = iiIiIIIiiI , themeit = oo )
 oOoo000 ( 'Atari Titles V Thru Z' , 'rom' , url = i1iI1 , icon = iiIiIIIiiI , themeit = oo )
 if 31 - 31: i1III1I
 if 78 - 78: i11iIiiIii + Ii1iI1I1 + Ii1I11I / Ii1iI1I1 % O0ooO0o0O0O % o0o0OoOo0O0OO
 if 83 - 83: O0ooO0o0O0O % oOOoo00O00o % Ii1iI1I1 % Ii1I11I . oOOOOOOo0O00o % IIOOOO0oo0
 if 47 - 47: Ii1iI1I1
 if 66 - 66: oOOOOoo0OOO - o0o0OoOo0O0OO
def iiIii ( ) :
 oOoo000 ( 'N64 Titles A Thru B' , 'rom' , url = ii1 , icon = iiIiIIIiiI , themeit = oo )
 oOoo000 ( 'N64 Titles C Thru E' , 'rom' , url = I1IiiI1ii1i , icon = IiII111i1i11 , themeit = oo )
 oOoo000 ( 'N64 Titles F Thru J' , 'rom' , url = O0o , icon = iiIiIIIiiI , themeit = oo )
 oOoo000 ( 'N64 Titles K Thru M' , 'rom' , url = oO0OoO00o , icon = iiIiIIIiiI , themeit = oo )
 oOoo000 ( 'N64 Titles N Thru R' , 'rom' , url = II1iiiiII , icon = iiIiIIIiiI , themeit = oo )
 oOoo000 ( 'N64 Titles S Thru T' , 'rom' , url = O0OoOO0oo0 , icon = iiIiIIIiiI , themeit = oo )
 oOoo000 ( 'N64 Titles V Thru Z' , 'rom' , url = oOO , icon = iiIiIIIiiI , themeit = oo )
 if 28 - 28: iiIi111
 if 52 - 52: oOOOOoo0OOO + O0ooO0o0O0O
 if 71 - 71: IIOOOO0oo0 / iiIi111
 if 34 - 34: oOOoo00O00o . O0ooO0o0O0O % IIOOOO0oo0
 if 43 - 43: oOOOOOOo0O00o - oO00oOOoooO
def O000O ( ) :
 oOoo000 ( 'PC Engine And Turbo Grafx Titles A Thru B' , 'rom' , url = O0o0OO0000ooo , icon = iiIiIIIiiI , themeit = oo )
 oOoo000 ( 'PC Engine And Turbo Grafx Titles C Thru E' , 'rom' , url = iIIII1iIIii , icon = IiII111i1i11 , themeit = oo )
 oOoo000 ( 'PC Engine And Turbo Grafx Titles F Thru I' , 'rom' , url = oOOO00o000o , icon = iiIiIIIiiI , themeit = oo )
 oOoo000 ( 'PC Engine And Turbo Grafx Titles J Thru M' , 'rom' , url = iIi11i1 , icon = iiIiIIIiiI , themeit = oo )
 oOoo000 ( 'PC Engine And Turbo Grafx Titles N Thru Q' , 'rom' , url = oO00oo0o00o0o , icon = iiIiIIIiiI , themeit = oo )
 oOoo000 ( 'PC Engine And Turbo Grafx Titles R Thru U' , 'rom' , url = IiIIIIIi , icon = iiIiIIIiiI , themeit = oo )
 oOoo000 ( 'PC Engine And Turbo Grafx Titles V Thru Z' , 'rom' , url = IiIi1iIIi1 , icon = iiIiIIIiiI , themeit = oo )
 if 98 - 98: O0ooO0o0O0O + Ii1I11I % oOOoo00O00o + Iii1I1i % oOOoo00O00o
 if 24 - 24: iiIi111 * Ii1I11I
 if 40 - 40: i1III1I - oOOoo00O00o * oOOoo00O00o . oOOoo00O00o + oOoooo0O0Oo
 if 77 - 77: O0ooO0o0O0O . i1III1I % iiIi111 / i1III1I
 if 54 - 54: iiIi111 + oo0 - ii1Ii1I1Ii11i
def I1I1IiIi1 ( ) :
 oOoo000 ( 'Nintendo DS Titles A' , 'rom' , url = O0OoO0ooOO0o , icon = iiIiIIIiiI , themeit = oo )
 oOoo000 ( 'Nintendo DS Titles B' , 'rom' , url = OoOo0oOooOoOO , icon = iiIiIIIiiI , themeit = oo )
 oOoo000 ( 'Nintendo DS Titles C' , 'rom' , url = oo00ooOoO00 , icon = iiIiIIIiiI , themeit = oo )
 oOoo000 ( 'Nintendo DS Titles D' , 'rom' , url = o00oOoOo0 , icon = iiIiIIIiiI , themeit = oo )
 oOoo000 ( 'Nintendo DS Titles E Thru F' , 'rom' , url = o0O0O0ooo0oOO , icon = iiIiIIIiiI , themeit = oo )
 oOoo000 ( 'Nintendo DS Titles G Thru H' , 'rom' , url = oo000 , icon = iiIiIIIiiI , themeit = oo )
 oOoo000 ( 'Nintendo DS Titles I Thru J' , 'rom' , url = iiOoO , icon = iiIiIIIiiI , themeit = oo )
 oOoo000 ( 'Nintendo DS Titles K Thru L' , 'rom' , url = Iiiiii111i1ii , icon = iiIiIIIiiI , themeit = oo )
 oOoo000 ( 'Nintendo DS Titles M' , 'rom' , url = i1i1iII1 , icon = iiIiIIIiiI , themeit = oo )
 oOoo000 ( 'Nintendo DS Titles N Thru O' , 'rom' , url = iii11i1IIII , icon = iiIiIIIiiI , themeit = oo )
 oOoo000 ( 'Nintendo DS Titles P Thru Q' , 'rom' , url = Ii , icon = iiIiIIIiiI , themeit = oo )
 oOoo000 ( 'Nintendo DS Titles R' , 'rom' , url = o00iiI1Ii1 , icon = iiIiIIIiiI , themeit = oo )
 oOoo000 ( 'Nintendo DS Titles S' , 'rom' , url = ii1i , icon = iiIiIIIiiI , themeit = oo )
 oOoo000 ( 'Nintendo DS Titles T Thru U' , 'rom' , url = oOOoo , icon = iiIiIIIiiI , themeit = oo )
 oOoo000 ( 'Nintendo DS Titles V Thru Z' , 'rom' , url = iII1111III1I , icon = iiIiIIIiiI , themeit = oo )
 if 58 - 58: oOOoo00O00o - oO00oOOoooO - oOoooo0O0Oo
 if 96 - 96: O0ooO0o0O0O
 if 82 - 82: oOOoo00O00o + IIOOOO0oo0 - o0o0OoOo0O0OO % iiIi111 * i11iIiiIii
 if 15 - 15: Ii1iI1I1
def I1iIoO0Ooo0OooOOo ( ) :
 oOoo000 ( 'Playstation Titles A' , 'rom' , url = ii11i , icon = iiIiIIIiiI , themeit = oo )
 oOoo000 ( 'Playstation Titles B' , 'rom' , url = O00oOo00o0o , icon = iiIiIIIiiI , themeit = oo )
 oOoo000 ( 'Playstation Titles C Thru D' , 'rom' , url = O00oO0 , icon = iiIiIIIiiI , themeit = oo )
 oOoo000 ( 'Playstation Titles E Thru F' , 'rom' , url = O0Oo00OoOo , icon = iiIiIIIiiI , themeit = oo )
 oOoo000 ( 'Playstation Titles G Thru J' , 'rom' , url = ii1ii111 , icon = iiIiIIIiiI , themeit = oo )
 oOoo000 ( 'Playstation Titles K Thru N' , 'rom' , url = i11111I1I , icon = iiIiIIIiiI , themeit = oo )
 oOoo000 ( 'Playstation Titles O Thru R' , 'rom' , url = ii1Oo0000oOo , icon = iiIiIIIiiI , themeit = oo )
 oOoo000 ( 'Playstation Titles S Thru T' , 'rom' , url = I11o0oO00oO0o0o0 , icon = iiIiIIIiiI , themeit = oo )
 oOoo000 ( 'Playstation Titles U Thru Z' , 'rom' , url = I1Iooooo , icon = iiIiIIIiiI , themeit = oo )
 if 71 - 71: o0o0OoOo0O0OO + oO0Oo0O0o * ii1Ii1I1Ii11i % ii1Ii1I1Ii11i / ii1Ii1I1Ii11i
 if 55 - 55: oOoooo0O0Oo + Ii1I11I + oOoooo0O0Oo * oo0
 if 68 - 68: IIOOOO0oo0
def II1iIII ( ) :
 if not ooo00Ooo == 'http://' :
  OoOOOOo = wiz . workingURL ( ooo00Ooo )
  if OoOOOOo == True :
   O0oOOo0Oo = wiz . openURL ( ooo00Ooo ) . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' ) . replace ( 'repository=""' , 'repository="none"' ) . replace ( 'repositoryurl=""' , 'repositoryurl="http://"' ) . replace ( 'repositoryxml=""' , 'repositoryxml="http://"' )
   o000O000 = re . compile ( 'name="(.+?)".+?lugin="(.+?)".+?rl="(.+?)".+?epository="(.+?)".+?epositoryxml="(.+?)".+?epositoryurl="(.+?)".+?con="(.+?)".+?anart="(.+?)".+?dult="(.+?)".+?escription="(.+?)"' ) . findall ( O0oOOo0Oo )
   if len ( o000O000 ) > 0 :
    for oO0o0O0Ooo0o , OoOOOO0O0oO0 , i1Ii11II , I11Ii1iI11iI1 , i1III1 , Iii111IiIii , iII11I1Ii1 , o0o0 , oOo0oO , IIi1IIIIi in o000O000 :
     if not IIiiiiiiIi1I1 == 'true' and oOo0oO . lower ( ) == 'yes' : continue
     try :
      OooO0ooo0 = xbmcaddon . Addon ( id = OoOOOO0O0oO0 )
      oO0o0O0Ooo0o = "[COLOR green][Installed][/COLOR] %s" % oO0o0O0Ooo0o
     except :
      pass
     Oo00oo0000OO ( oO0o0O0Ooo0o , 'addoninstall' , OoOOOO0O0oO0 , description = IIi1IIIIi , icon = iII11I1Ii1 , fanart = o0o0 , themeit = I1111i )
   else : wiz . log ( "[Addon Menu] ERROR: Invalid Format." )
  else :
   wiz . log ( "[Addon Menu] ERROR: URL for Addon list not working." )
   Oo00oo0000OO ( 'Url for txt file not valid' , '' , themeit = iIIii )
   Oo00oo0000OO ( '%s' % OoOOOOo , '' , themeit = iIIii )
 else : wiz . log ( "[Addon Menu] No Addon list added." )
 oOOo000oOoO0 ( 'files' , 'viewType' )
 if 2 - 2: oOoooo0O0Oo
def o0o0O00 ( plugin ) :
 if not ooo00Ooo == 'http://' :
  OoOOOOo = wiz . workingURL ( ooo00Ooo )
  if OoOOOOo == True :
   O0oOOo0Oo = wiz . openURL ( ooo00Ooo ) . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' ) . replace ( 'repository=""' , 'repository="none"' ) . replace ( 'repositoryurl=""' , 'repositoryurl="http://"' ) . replace ( 'repositoryxml=""' , 'repositoryxml="http://"' )
   o000O000 = re . compile ( 'name="(.+?)".+?lugin="%s".+?rl="(.+?)".+?epository="(.+?)".+?epositoryxml="(.+?)".+?epositoryurl="(.+?)".+?con="(.+?)".+?anart="(.+?)".+?dult="(.+?)".+?escription="(.+?)"' % plugin ) . findall ( O0oOOo0Oo )
   if len ( o000O000 ) > 0 :
    for oO0o0O0Ooo0o , i1Ii11II , I11Ii1iI11iI1 , i1III1 , Iii111IiIii , iII11I1Ii1 , o0o0 , oOo0oO , IIi1IIIIi in o000O000 :
     if os . path . exists ( os . path . join ( II1 , plugin ) ) :
      if IiiIII111iI . yesno ( iiiii , "[COLOR %s]Would you like to remove and reinstall:" % i11I1IiII1i1i , "[COLOR %s]%s[/COLOR]?[/COLOR]" % ( Oo0O00O000 , plugin ) , yeslabel = "[B]Yes Remove[/B]" , nolabel = "[B]No Skip[/B]" ) :
       wiz . cleanHouse ( os . path . join ( II1 , plugin ) )
       if IiiIII111iI . yesno ( iiiii , "[COLOR %s]Would you like to remove the addon_data for:" % i11I1IiII1i1i , "[COLOR %s]%s[/COLOR]?[/COLOR]" % ( Oo0O00O000 , plugin ) , yeslabel = "[B]Yes Remove[/B]" , nolabel = "[B]No Skip[/B]" ) :
        i1iIiIIi1II1ii ( plugin )
      else : wiz . log ( "[Addon Installer] %s wasnt re-installed" % plugin ) ; return False
     i1II1Ii1i1 = os . path . join ( II1 , I11Ii1iI11iI1 )
     if not I11Ii1iI11iI1 . lower ( ) == 'none' and not os . path . exists ( i1II1Ii1i1 ) :
      wiz . log ( "Repository not installed, installing it" )
      if IiiIII111iI . yesno ( iiiii , "[COLOR %s]Would you like to install the repository for [COLOR %s]%s[/COLOR]:" % ( i11I1IiII1i1i , Oo0O00O000 , plugin ) , "[COLOR %s]%s[/COLOR]?[/COLOR]" % ( Oo0O00O000 , I11Ii1iI11iI1 ) , yeslabel = "[B]Yes Install[/B]" , nolabel = "[B]No Skip[/B]" ) :
       I1i1I1I11IiiI = wiz . openURL ( i1III1 ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
       I1IiI1iI11 = re . compile ( '<addon.+?d="%s".+?ersion="(.+?)".+?>' % I11Ii1iI11iI1 ) . findall ( I1i1I1I11IiiI )
       II1i = re . compile ( '<addon.+?ersion="(.+?)".+?d="%s".+?>' % I11Ii1iI11iI1 ) . findall ( I1i1I1I11IiiI )
       wiz . log ( "Match 1: %s / Match 2: %s" % ( len ( I1IiI1iI11 ) , len ( II1i ) ) )
       if len ( I1IiI1iI11 ) > 0 : IiIi1ii111i1 = I1IiI1iI11 [ 0 ]
       elif len ( II1i ) > 0 : IiIi1ii111i1 = II1i [ 0 ]
       else : wiz . log ( "No Match" )
       iIi = '%s%s-%s.zip' % ( Iii111IiIii , I11Ii1iI11iI1 , IiIi1ii111i1 )
       wiz . log ( iIi )
       iiO0O0o0oO0O00 ( I11Ii1iI11iI1 , iIi )
       wiz . ebi ( 'UpdateAddonRepos()' )
       wiz . log ( "Installing Addon from Kodi" )
       xbmc . sleep ( 1000 )
       o0O0oO0 = oo0i1 ( plugin )
       if o0O0oO0 :
        wiz . refresh ( )
        return True
      else : wiz . log ( "[Addon Installer] Repository for %s not installed: %s" % ( plugin , I11Ii1iI11iI1 ) )
     elif I11Ii1iI11iI1 . lower ( ) == 'none' :
      wiz . log ( "No repository, installing addon" )
      i1IiIi1 = plugin
      I1iiIiI1iI1I = i1Ii11II
      iiO0O0o0oO0O00 ( plugin , i1Ii11II )
      wiz . refresh ( )
      return True
     else :
      wiz . log ( "Repository installed, installing addon" )
      o0O0oO0 = oo0i1 ( plugin )
      if o0O0oO0 :
       wiz . refresh ( )
       return True
     III1II111Ii1 = wiz . openURL ( i1III1 ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
     o0O0OO0o = re . compile ( '<addon.+?id="%s".+?ersion="(.+?)".+?>' % plugin ) . findall ( III1II111Ii1 )
     OOOoOo = re . compile ( '<addon.+?ersion="(.+?)".+?id="%s".+?>' % plugin ) . findall ( III1II111Ii1 )
     if len ( o0O0OO0o ) > 0 : IiIi1ii111i1 = o0O0OO0o [ 0 ]
     elif len ( OOOoOo ) > 0 : IiIi1ii111i1 = OOOoOo [ 0 ]
     else : wiz . log ( "no match" )
     i1Ii11II = "%s%s-%s.zip" % ( i1Ii11II , plugin , IiIi1ii111i1 )
     wiz . log ( str ( i1Ii11II ) )
     iiO0O0o0oO0O00 ( plugin , i1Ii11II )
     wiz . refresh ( )
   else : wiz . log ( "[Addon Installer] Invalid Format" )
  else : wiz . log ( "[Addon Installer] Text File: %s" % OoOOOOo )
 else : wiz . log ( "[Addon Installer] Not Enabled." )
 if 70 - 70: ii1Ii1I1Ii11i - iiIi111 . O0ooO0o0O0O % Iii1I1i / oOOoo00O00o - IIOOOO0oo0
def oo0i1 ( plugin ) :
 wiz . log ( "Running Plugin" )
 wiz . ebi ( 'RunPlugin(plugin://%s)' % plugin )
 xbmc . sleep ( 500 )
 if not wiz . whileWindow ( 'yesnodialog' ) :
  return False
 xbmc . sleep ( 500 )
 if wiz . whileWindow ( 'okdialog' ) :
  return False
 o0O0oo0o = wiz . whileWindow ( 'progressdialog' )
 xbmc . sleep ( 1000 )
 wiz . log ( "Download complete" )
 if os . path . exists ( os . path . join ( II1 , plugin ) ) : return True
 else : return False
 if 12 - 12: oOOoo00O00o % o0o0OoOo0O0OO % oOOOOOOo0O00o . i11iIiiIii * O0ooO0o0O0O
def iiO0O0o0oO0O00 ( name , url ) :
 if not wiz . workingURL ( url ) == True : wiz . LogNotify ( "Addon Installer" , '%s: [COLOR red]Invalid Zip Url![/COLOR]' % name ) ; return
 if not os . path . exists ( oooOOOOO ) : os . makedirs ( oooOOOOO )
 iI1Ii11111iIi . create ( iiiii , '[COLOR %s][B]Downloading:[/B][/COLOR] [COLOR %s]%s[/COLOR]' % ( i11I1IiII1i1i , Oo0O00O000 , name ) , '' , 'Please Wait' )
 oo0oooo0OoO0o = url . split ( '/' )
 I1I1 = os . path . join ( oooOOOOO , oo0oooo0OoO0o [ - 1 ] )
 try : os . remove ( I1I1 )
 except : pass
 downloader . download ( url , I1I1 , iI1Ii11111iIi )
 xbmc . sleep ( 500 )
 O0Oo0 = '[COLOR %s][B]Installing:[/B][/COLOR] [COLOR %s]%s[/COLOR]' % ( i11I1IiII1i1i , Oo0O00O000 , name )
 iI1Ii11111iIi . update ( 0 , O0Oo0 , '' , 'Please Wait' )
 OOooO0OO0 , iI1iIiiiI1I1 , OOOOOo = extract . all ( I1I1 , II1 , iI1Ii11111iIi , title = O0Oo0 )
 iI1Ii11111iIi . close ( )
 I1IiiiIiI ( name )
 O0Oo ( name )
 xbmc . sleep ( 500 )
 wiz . ebi ( 'UpdateAddonRepos()' )
 wiz . ebi ( 'UpdateLocalAddons()' )
 xbmc . sleep ( 500 )
 wiz . refresh ( )
 if 20 - 20: oo0 % oOoooo0O0Oo + i11iIiiIii % OO - I111I1Iiii1i
def O0Oo ( name ) :
 Ii11i1Ii11I = os . path . join ( II1 , name , 'addon.xml' )
 if os . path . exists ( Ii11i1Ii11I ) :
  ii1ii11IiI = open ( Ii11i1Ii11I , mode = 'r' ) ; O0oOOo0Oo = ii1ii11IiI . read ( ) ; ii1ii11IiI . close ( ) ;
  o000O000 = re . compile ( 'import addon="(.+?)"' ) . findall ( O0oOOo0Oo )
  for I1IiI1ii1ii1I in o000O000 :
   if not 'xbmc.python' in I1IiI1ii1ii1I :
    iI1IIi11i1I1 = os . path . join ( II1 , I1IiI1ii1ii1I )
    if not os . path . exists ( iI1IIi11i1I1 ) :
     O00oo = '%s%s.zip' % ( Oo0oo0O0o00O , I1IiI1ii1ii1I )
     I1I1 = os . path . join ( oooOOOOO , '%s.zip' % I1IiI1ii1ii1I )
     try : os . remove ( I1I1 )
     except : pass
     iI1Ii11111iIi . update ( 0 , '[COLOR %s][B]Downloading Dependency:[/B][/COLOR] [COLOR %s]%s[/COLOR]' % ( i11I1IiII1i1i , Oo0O00O000 , I1IiI1ii1ii1I ) , '' , 'Please Wait' )
     downloader . download ( O00oo , I1I1 , iI1Ii11111iIi )
     xbmc . sleep ( 100 )
     O0Oo0 = '[COLOR %s][B]Installing Dependency:[/B][/COLOR] [COLOR %s]%s[/COLOR]' % ( i11I1IiII1i1i , Oo0O00O000 , I1IiI1ii1ii1I )
     iI1Ii11111iIi . update ( 0 , O0Oo0 , '' , 'Please Wait' )
     OOooO0OO0 , iI1iIiiiI1I1 , OOOOOo = extract . all ( I1I1 , II1 , iI1Ii11111iIi , title = O0Oo0 )
     I1IiiiIiI ( I1IiI1ii1ii1I )
     O0Oo ( I1IiI1ii1ii1I )
     xbmc . sleep ( 100 )
     iI1Ii11111iIi . close ( )
     if 58 - 58: O0ooO0o0O0O - i11iIiiIii - i11iIiiIii * i1III1I + Ii1iI1I1 . oOOoo00O00o
def I1IiiiIiI ( addon ) :
 i1Ii11II = os . path . join ( II1 , addon , 'addon.xml' )
 if os . path . exists ( i1Ii11II ) :
  list = open ( i1Ii11II , mode = 'r' ) ; OoOo00o = list . read ( ) . replace ( '\n' , '' ) . replace ( '\r' , '' ) ; list . close ( )
  o000O000 = re . compile ( '<addon.+?name="(.+?)".+?>' ) . findall ( OoOo00o )
  iII11I1Ii1 = os . path . join ( II1 , addon , 'icon.png' )
  wiz . LogNotify ( o000O000 [ 0 ] , 'Addon Enabled' , '2000' , iII11I1Ii1 )
  if 30 - 30: oOOoo00O00o . Iii1I1i / Iii1I1i * i11iIiiIii
def II1III1i1iiI ( url ) :
 if not IIIIIiI ( url ) == True : return False
 O0oOOo0Oo = wiz . openURL ( url ) . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
 o000O000 = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?con="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( O0oOOo0Oo )
 if len ( o000O000 ) > 0 :
  for oO0o0O0Ooo0o , url , iII11I1Ii1 , o0o0 , IIi1IIIIi in o000O000 :
   Oo00oo0000OO ( oO0o0O0Ooo0o , 'viewVideo' , url = url , description = IIi1IIIIi , icon = iII11I1Ii1 , fanart = o0o0 , themeit = I1111i )
  else : wiz . log ( "[YouTube Menu] ERROR: Invalid Format." )
 else :
  wiz . log ( "[YouTube Menu] ERROR: URL for YouTube list not working." )
  Oo00oo0000OO ( 'Url for txt file not valid' , '' , themeit = iIIii )
 oOOo000oOoO0 ( 'files' , 'viewType' )
 if 27 - 27: i1III1I - IIOOOO0oo0 % Iii1I1i * Ii1I11I . o0o0OoOo0O0OO % O0ooO0o0O0O
 if 37 - 37: oOoooo0O0Oo + IIOOOO0oo0 - oO0Oo0O0o % oo0
 if 24 - 24: oOOoo00O00o
def Oo0oOo0ooOOOo ( view = None ) :
 OoO0000o = '[B][COLOR green]ON[/COLOR][/B]' ; o0Ii1 = '[B][COLOR red]OFF[/COLOR][/B]'
 IIi1IiII = 'true' if oOoOooOo0o0 == 'true' else 'false'
 o0IIIIiI11I = 'true' if OOOO == 'true' else 'false'
 iiiI11iIIi1 = 'true' if OOO00 == 'true' else 'false'
 o00OoooooooOo = 'true' if iiiiiIIii == 'true' else 'false'
 iIii1I = 'true' if I11iii1Ii == 'true' else 'false'
 iii11i1 = 'true' if I1IIIii == 'true' else 'false'
 i1IiI1I111iIi = 'true' if O000oo0O == 'true' else 'false'
 IiiIIi1 = 'true' if OOOOi11i1 == 'true' else 'false'
 if wiz . Grab_Log ( True ) == False : iI1iIiiI = 0
 else : iI1iIiiI = Oo0OOo ( wiz . Grab_Log ( True ) , True )
 if wiz . Grab_Log ( True , True ) == False : Ii1I11i11I1i = 0
 else : Ii1I11i11I1i = Oo0OOo ( wiz . Grab_Log ( True , True ) , True )
 oO00 = int ( iI1iIiiI ) + int ( Ii1I11i11I1i )
 IiI1II11iiI = ': [COLOR red]Not Found[/COLOR]' if not os . path . exists ( II11iiii1Ii ) else ": [COLOR green]%s[/COLOR]" % wiz . convertSize ( os . path . getsize ( II11iiii1Ii ) )
 if IiiIIi1 == 'true' :
  o0oOOooo00O = 'true'
  OO0ooo0 = 'true'
  II1II1iI = 'true'
  OooooO = 'true'
  oO0O0 = 'true'
  iI111i11iI1 = 'true'
  III1ii = 'true'
  iI1III1iIi11 = 'true'
 else :
  o0oOOooo00O = 'true' if IIIii1II1II == 'true' else 'false'
  OO0ooo0 = 'true' if i1I1iI == 'true' else 'false'
  II1II1iI = 'true' if oo0OooOOo0 == 'true' else 'false'
  OooooO = 'true' if o0OO00oO == 'true' else 'false'
  oO0O0 = 'true' if I11i1I1I == 'true' else 'false'
  iI111i11iI1 = 'true' if oO0Oo == 'true' else 'false'
  III1ii = 'true' if oOOoo0Oo == 'true' else 'false'
  iI1III1iIi11 = 'true' if o00OO00OoO == 'true' else 'false'
 i11I1I = wiz . getSize ( oooOOOOO )
 oo0ooooo00o = wiz . getSize ( O0OoO000O0OO )
 OoOoi111i1iIi1 = wiz . getCacheSize ( )
 OoO0oO = i11I1I + oo0ooooo00o + OoOoi111i1iIi1
 IiiI1iiI1III1i = [ 'Always' , 'Daily' , '3 Days' , 'Weekly' ]
 Oo00oo0000OO ( 'Show All Maintenance: %s' % iii11i1 . replace ( 'true' , OoO0000o ) . replace ( 'false' , o0Ii1 ) , 'togglesetting' , 'showmaint' , icon = ooOoO00 , themeit = I1111i )
 Oo00oo0000OO ( 'Auto Clean' , '' , fanart = II , icon = ooOoO00 , themeit = oo )
 Oo00oo0000OO ( 'Auto Clean Up On Startup: %s' % IIi1IiII . replace ( 'true' , OoO0000o ) . replace ( 'false' , o0Ii1 ) , 'togglesetting' , 'autoclean' , icon = ooOoO00 , themeit = iIIii )
 oOoo000 ( '[B]Cleaning Tools[/B]' , 'maint' , 'clean' , icon = ooOoO00 , themeit = oo )
 if IIi1IiII == 'true' :
  Oo00oo0000OO ( '--- Auto Clean Fequency: [B][COLOR green]%s[/COLOR][/B]' % IiiI1iiI1III1i [ O000OO0 ] , 'changefeq' , icon = ooOoO00 , themeit = iIIii )
  Oo00oo0000OO ( '--- Clear Cache on Startup: %s' % o0IIIIiI11I . replace ( 'true' , OoO0000o ) . replace ( 'false' , o0Ii1 ) , 'togglesetting' , 'clearcache' , icon = ooOoO00 , themeit = iIIii )
  Oo00oo0000OO ( '--- Clear Packages on Startup: %s' % iiiI11iIIi1 . replace ( 'true' , OoO0000o ) . replace ( 'false' , o0Ii1 ) , 'togglesetting' , 'clearpackages' , icon = ooOoO00 , themeit = iIIii )
  Oo00oo0000OO ( '--- Clear Old Thumbs on Startup: %s' % o00OoooooooOo . replace ( 'true' , OoO0000o ) . replace ( 'false' , o0Ii1 ) , 'togglesetting' , 'clearthumbs' , icon = ooOoO00 , themeit = iIIii )
  Oo00oo0000OO ( '--- Delay Clear Packages: %s' % iIii1I . replace ( 'true' , OoO0000o ) . replace ( 'false' , o0Ii1 ) , 'togglesetting' , 'delayautoclean' , icon = ooOoO00 , themeit = iIIii )
 Oo00oo0000OO ( 'Clear Video Cache' , '' , fanart = II , icon = ooOoO00 , themeit = oo )
 Oo00oo0000OO ( 'Include Video Cache in Clear Cache: %s' % i1IiI1I111iIi . replace ( 'true' , OoO0000o ) . replace ( 'false' , o0Ii1 ) , 'togglecache' , 'includevideo' , icon = ooOoO00 , themeit = iIIii )
 if view == "clean" or I1IIIii == 'true' :
  Oo00oo0000OO ( 'Total Clean Up: [COLOR green][B]%s[/B][/COLOR]' % wiz . convertSize ( OoO0oO ) , 'fullclean' , icon = ooOoO00 , themeit = iIIii )
  Oo00oo0000OO ( 'Clear Cache: [COLOR green][B]%s[/B][/COLOR]' % wiz . convertSize ( OoOoi111i1iIi1 ) , 'clearcache' , icon = ooOoO00 , themeit = iIIii )
  Oo00oo0000OO ( 'Clear Packages: [COLOR green][B]%s[/B][/COLOR]' % wiz . convertSize ( i11I1I ) , 'clearpackages' , icon = ooOoO00 , themeit = iIIii )
  Oo00oo0000OO ( 'Clear Thumbnails: [COLOR green][B]%s[/B][/COLOR]' % wiz . convertSize ( oo0ooooo00o ) , 'clearthumb' , icon = ooOoO00 , themeit = iIIii )
  Oo00oo0000OO ( 'Clear Crash Logs' , 'clearcrash' , icon = ooOoO00 , themeit = iIIii )
  Oo00oo0000OO ( 'Purge Databases' , 'purgedb' , icon = ooOoO00 , themeit = iIIii )
  Oo00oo0000OO ( 'Fresh Start' , 'freshstart' , icon = ooOoO00 , themeit = iIIii )
 IiI11i1IIiiI ( '[B]Addon Tools[/B]' , 'maint' , 'addon' , icon = ooOoO00 , themeit = oo )
 if view == "addon" or I1IIIii == 'true' :
  IiI11i1IIiiI ( 'Remove Addons' , 'removeaddons' , icon = ooOoO00 , themeit = iIIii )
  IiI11i1IIiiI ( 'Remove Addon Data' , 'removeaddondata' , icon = ooOoO00 , themeit = iIIii )
  IiI11i1IIiiI ( 'Enable/Disable Addons' , 'enableaddons' , icon = ooOoO00 , themeit = iIIii )
  Oo00oo0000OO ( 'Enable/Disable Adult Addons' , 'toggleadult' , icon = ooOoO00 , themeit = iIIii )
  Oo00oo0000OO ( 'Force Update Addons' , 'forceupdate' , icon = ooOoO00 , themeit = iIIii )
  Oo00oo0000OO ( 'Hide Passwords On Keyboard Entry' , 'hidepassword' , icon = ooOoO00 , themeit = iIIii )
  Oo00oo0000OO ( 'Unhide Passwords On Keyboard Entry' , 'unhidepassword' , icon = ooOoO00 , themeit = iIIii )
 IiI11i1IIiiI ( '[B]Misc Maintenance[/B]' , 'maint' , 'misc' , icon = ooOoO00 , themeit = oo )
 if view == "misc" or I1IIIii == 'true' :
  Oo00oo0000OO ( 'Reload Skin' , 'forceskin' , icon = ooOoO00 , themeit = iIIii )
  Oo00oo0000OO ( 'Force Close Kodi' , 'forceclose' , icon = ooOoO00 , themeit = iIIii )
  Oo00oo0000OO ( 'Upload Kodi.log' , 'uploadlog' , icon = ooOoO00 , themeit = iIIii )
  Oo00oo0000OO ( 'View Errors in Log: %s Error(s)' % ( oO00 ) , 'viewerrorlog' , icon = ooOoO00 , themeit = iIIii )
  Oo00oo0000OO ( 'View Log File' , 'viewlog' , icon = ooOoO00 , themeit = iIIii )
  Oo00oo0000OO ( 'View Wizard Log File' , 'viewwizlog' , icon = ooOoO00 , themeit = iIIii )
  Oo00oo0000OO ( 'Clear Wizard Log File %s' % IiI1II11iiI , 'clearwizlog' , icon = ooOoO00 , themeit = iIIii )
 IiI11i1IIiiI ( '[B]Back up/Restore[/B]' , 'maint' , 'backup' , icon = ooOoO00 , themeit = oo )
 if view == "backup" or I1IIIii == 'true' :
  Oo00oo0000OO ( 'Clean Up Back Up Folder' , 'clearbackup' , icon = ooOoO00 , themeit = iIIii )
  Oo00oo0000OO ( 'Back Up Location: [COLOR %s]%s[/COLOR]' % ( i11I1IiII1i1i , IiIIIi1iIi ) , 'settings' , 'Maintenance' , icon = ooOoO00 , themeit = iIIii )
  Oo00oo0000OO ( '[Back Up]: Build' , 'backupbuild' , icon = ooOoO00 , themeit = iIIii )
  Oo00oo0000OO ( '[Back Up]: GuiFix' , 'backupgui' , icon = ooOoO00 , themeit = iIIii )
  Oo00oo0000OO ( '[Back Up]: Theme' , 'backuptheme' , icon = ooOoO00 , themeit = iIIii )
  Oo00oo0000OO ( '[Back Up]: Addon_data' , 'backupaddon' , icon = ooOoO00 , themeit = iIIii )
  Oo00oo0000OO ( '[Restore]: Local Build' , 'restorezip' , icon = ooOoO00 , themeit = iIIii )
  Oo00oo0000OO ( '[Restore]: Local GuiFix' , 'restoregui' , icon = ooOoO00 , themeit = iIIii )
  Oo00oo0000OO ( '[Restore]: Local Addon_data' , 'restoreaddon' , icon = ooOoO00 , themeit = iIIii )
  Oo00oo0000OO ( '[Restore]: External Build' , 'restoreextzip' , icon = ooOoO00 , themeit = iIIii )
  Oo00oo0000OO ( '[Restore]: External GuiFix' , 'restoreextgui' , icon = ooOoO00 , themeit = iIIii )
  Oo00oo0000OO ( '[Restore]: External Addon_data' , 'restoreextaddon' , icon = ooOoO00 , themeit = iIIii )
 IiI11i1IIiiI ( '[B]System Tweaks/Fixes[/B]' , 'maint' , 'tweaks' , icon = ooOoO00 , themeit = oo )
 if view == "tweaks" or I1IIIii == 'true' :
  if not I1i1i1 == 'http://' : oOoo000 ( 'Advanced Settings' , 'advancedsetting' , icon = ooOoO00 , themeit = iIIii )
  else : oOOOO ( 'Advanced Settings' , 'autoadvanced' , icon = ooOoO00 , themeit = iIIii )
  Oo00oo0000OO ( 'Scan Sources for broken links' , 'checksources' , icon = ooOoO00 , themeit = iIIii )
  Oo00oo0000OO ( 'Scan For Broken Repositories' , 'checkrepos' , icon = ooOoO00 , themeit = iIIii )
  Oo00oo0000OO ( 'Fix Addons Not Updating' , 'fixaddonupdate' , icon = ooOoO00 , themeit = iIIii )
  Oo00oo0000OO ( 'Remove special character filenames' , 'asciicheck' , icon = ooOoO00 , themeit = iIIii )
  Oo00oo0000OO ( 'Convert Paths to special' , 'convertpath' , icon = ooOoO00 , themeit = iIIii )
  IiI11i1IIiiI ( 'System Information' , 'systeminfo' , icon = ooOoO00 , themeit = iIIii )
 if i1IiI1I111iIi == 'true' :
  Oo00oo0000OO ( '--- Include All Video Addons: %s' % IiiIIi1 . replace ( 'true' , OoO0000o ) . replace ( 'false' , o0Ii1 ) , 'togglecache' , 'includeall' , icon = ooOoO00 , themeit = iIIii )
  Oo00oo0000OO ( '--- Include Bob: %s' % o0oOOooo00O . replace ( 'true' , OoO0000o ) . replace ( 'false' , o0Ii1 ) , 'togglecache' , 'includebob' , icon = ooOoO00 , themeit = iIIii )
  Oo00oo0000OO ( '--- Include Phoenix: %s' % OO0ooo0 . replace ( 'true' , OoO0000o ) . replace ( 'false' , o0Ii1 ) , 'togglecache' , 'includephoenix' , icon = ooOoO00 , themeit = iIIii )
  Oo00oo0000OO ( '--- Include Specto: %s' % II1II1iI . replace ( 'true' , OoO0000o ) . replace ( 'false' , o0Ii1 ) , 'togglecache' , 'includespecto' , icon = ooOoO00 , themeit = iIIii )
  Oo00oo0000OO ( '--- Include Exodus: %s' % oO0O0 . replace ( 'true' , OoO0000o ) . replace ( 'false' , o0Ii1 ) , 'togglecache' , 'includeexodus' , icon = ooOoO00 , themeit = iIIii )
  Oo00oo0000OO ( '--- Include Salts: %s' % III1ii . replace ( 'true' , OoO0000o ) . replace ( 'false' , o0Ii1 ) , 'togglecache' , 'includesalts' , icon = ooOoO00 , themeit = iIIii )
  Oo00oo0000OO ( '--- Include Salts HD Lite: %s' % iI1III1iIi11 . replace ( 'true' , OoO0000o ) . replace ( 'false' , o0Ii1 ) , 'togglecache' , 'includesaltslite' , icon = ooOoO00 , themeit = iIIii )
  Oo00oo0000OO ( '--- Include One Channel: %s' % iI111i11iI1 . replace ( 'true' , OoO0000o ) . replace ( 'false' , o0Ii1 ) , 'togglecache' , 'includeonechan' , icon = ooOoO00 , themeit = iIIii )
  Oo00oo0000OO ( '--- Include Genesis: %s' % OooooO . replace ( 'true' , OoO0000o ) . replace ( 'false' , o0Ii1 ) , 'togglecache' , 'includegenesis' , icon = ooOoO00 , themeit = iIIii )
  Oo00oo0000OO ( '--- Enable All Video Addons' , 'togglecache' , 'true' , icon = ooOoO00 , themeit = iIIii )
  Oo00oo0000OO ( '--- Disable All Video Addons' , 'togglecache' , 'false' , icon = ooOoO00 , themeit = iIIii )
 IiI11i1IIiiI ( '[I]<< Return to Main Menu[/I]' , icon = ooOoO00 , themeit = I1111i )
 oOOo000oOoO0 ( 'files' , 'viewType' )
 if 36 - 36: oO0Oo0O0o / oo0 . O0ooO0o0O0O
def i1IiiiiIi1I ( ) :
 if not I1i1i1 == 'http://' :
  Oo00oo0000OO ( 'Configure Wizard' , 'autoadvanced' , icon = ooOoO00 , themeit = iIIii )
  if os . path . exists ( ii11iIi1I ) : oOOOO ( 'View Currect AdvancedSettings.xml' , 'currentsettings' , icon = ooOoO00 , themeit = iIIii )
  ooo0O0o0OoOO = wiz . workingURL ( I1i1i1 )
  if ooo0O0o0OoOO == True :
   if IiIi11iI == 'No' : oOOOO ( wiz . sep ( ) , '' , icon = ooOoO00 , themeit = iIIii )
   O0oOOo0Oo = wiz . openURL ( I1i1i1 ) . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
   o000O000 = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?con="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( O0oOOo0Oo )
   if len ( o000O000 ) > 0 :
    for oO0o0O0Ooo0o , i1Ii11II , iII11I1Ii1 , o0o0 , IIi1IIIIi in o000O000 :
     Oo00oo0000OO ( oO0o0O0Ooo0o , 'writeadvanced' , oO0o0O0Ooo0o , description = IIi1IIIIi , icon = iII11I1Ii1 , fanart = o0o0 , themeit = I1111i )
   else : wiz . log ( "[Advanced Settings] ERROR: Invalid Format." )
  else : wiz . log ( "[Advanced Settings] URL not working: %s" % ooo0O0o0OoOO )
 else : wiz . log ( "[Advanced Settings] not Enabled" )
 if 9 - 9: I111I1Iiii1i
def o0o0OO0o00o0O ( name ) :
 if not I1i1i1 == 'http://' :
  ooo0O0o0OoOO = wiz . workingURL ( I1i1i1 )
  if ooo0O0o0OoOO == True :
   O0oOOo0Oo = wiz . openURL ( I1i1i1 ) . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
   o000O000 = re . compile ( 'name="%s".+?rl="(.+?)"' % name ) . findall ( O0oOOo0Oo )
   if len ( o000O000 ) > 0 : IIIIIIi1i = o000O000 [ 0 ]
   else : wiz . log ( "[Advanced Settings] ERROR: Invalid Format." ) ; wiz . LogNotify ( iiiii , "Invalid File Format" ) ; return
   if 26 - 26: O0ooO0o0O0O - IIOOOO0oo0 . IIOOOO0oo0
   if os . path . exists ( ii11iIi1I ) : O0oOoo = IiiIII111iI . yesno ( iiiii , "[COLOR %s]Would you like to overwrite your current Advanced Settings with [COLOR %s]%s[/COLOR]?[/COLOR]" % ( Oo0O00O000 , i11I1IiII1i1i , name ) , yeslabel = "[B]Overwrite[/B]" , nolabel = "[B]Cancel[/B]" )
   else : O0oOoo = IiiIII111iI . yesno ( iiiii , "[COLOR %s]Would you like to download and install [COLOR %s]%s[/COLOR]?[/COLOR]" % ( Oo0O00O000 , i11I1IiII1i1i , name ) , yeslabel = "[B]Install[/B]" , nolabel = "[B]Cancel[/B]" )
   if 76 - 76: oO0Oo0O0o % oOOoo00O00o - oOOOOoo0OOO / Ii1iI1I1 * oo0
   if O0oOoo == 1 :
    file = wiz . openURL ( IIIIIIi1i )
    iIiIIiI1i1Ii = open ( ii11iIi1I , 'w' ) ;
    iIiIIiI1i1Ii . write ( file )
    iIiIIiI1i1Ii . close ( )
    IiiIII111iI . ok ( iiiii , '[COLOR %s]AdvancedSettings.xml file has been successfully written.  Once you click okay it will force close kodi.[/COLOR]' % i11I1IiII1i1i )
    wiz . killxbmc ( True )
   else : wiz . log ( "[Advanced Settings] install canceled" ) ; wiz . LogNotify ( iiiii , "Write Cancelled!" ) ; return
  else : wiz . log ( "[Advanced Settings] URL not working: %s" % ooo0O0o0OoOO ) ; wiz . LogNotify ( iiiii , "URL Not Working" )
 else : wiz . log ( "[Advanced Settings] not Enabled" ) ; wiz . LogNotify ( iiiii , "Not Enabled" )
 if 72 - 72: oOoOoo . oOoOoo - oOOOOOOo0O00o
def III1II1i ( ) :
 iIiIIiI1i1Ii = open ( ii11iIi1I )
 iI1i1IiIIIIi = iIiIIiI1i1Ii . read ( ) . replace ( '\t' , '    ' )
 wiz . TextBoxes ( iiiii , iI1i1IiIIIIi )
 iIiIIiI1i1Ii . close ( )
 if 65 - 65: IIOOOO0oo0 * oOOOOoo0OOO / oOOOOoo0OOO . oOOoo00O00o
def Oo0O0OOO0o0O ( ) :
 notify . autoConfig ( )
 if 51 - 51: iiIi111 + I111I1Iiii1i + oO00oOOoooO + oO00oOOoooO % Ii1iI1I1
def iIi1i1iIi1Ii1 ( ) :
 oOOoOOO0oo0 = 'http://whatismyipaddress.com/'
 if not wiz . workingURL ( oOOoOOO0oo0 ) : return 'Unknown' , 'Unknown' , 'Unknown'
 O00O = wiz . openURL ( oOOoOOO0oo0 ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 if not 'Access Denied' in O00O :
  O0OOOOOoo = re . compile ( 'whatismyipaddress.com/ip/(.+?)"' ) . findall ( O00O )
  oo0ooO0 = O0OOOOOoo [ 0 ] if ( len ( O0OOOOOoo ) > 0 ) else 'Unknown'
  oOooo0OOO = re . compile ( '"font-size:14px;">(.+?)</td>' ) . findall ( O00O )
  oooO00O = oOooo0OOO [ 0 ] if ( len ( oOooo0OOO ) > 0 ) else 'Unknown'
  II1oOo00o = oOooo0OOO [ 1 ] + ', ' + oOooo0OOO [ 2 ] + ', ' + oOooo0OOO [ 3 ] if ( len ( oOooo0OOO ) > 2 ) else 'Unknown'
  return oo0ooO0 , oooO00O , II1oOo00o
 else : return 'Unknown' , 'Unknown' , 'Unknown'
 if 12 - 12: Ii1iI1I1 * Ii1I11I % OO * oO0Oo0O0o * O0ooO0o0O0O
def oO0oOoo0O ( ) :
 II1iI11 = [ 'System.FriendlyName' ,
 'System.BuildVersion' ,
 'System.CpuUsage' ,
 'System.ScreenMode' ,
 'Network.IPAddress' ,
 'Network.MacAddress' ,
 'System.Uptime' ,
 'System.TotalUptime' ,
 'System.FreeSpace' ,
 'System.UsedSpace' ,
 'System.TotalSpace' ,
 'System.Memory(free)' ,
 'System.Memory(used)' ,
 'System.Memory(total)' ]
 O00o0O = [ ] ; O00oOo0O0o00O = 0
 for ooo0oo00O00Oo in II1iI11 :
  OOO000000OOO0 = wiz . getInfo ( ooo0oo00O00Oo )
  ooOoOOoooO000 = 0
  while OOO000000OOO0 == "Busy" and ooOoOOoooO000 < 10 :
   OOO000000OOO0 = wiz . getInfo ( ooo0oo00O00Oo ) ; ooOoOOoooO000 += 1 ; wiz . log ( "%s sleep %s" % ( ooo0oo00O00Oo , str ( ooOoOOoooO000 ) ) ) ; xbmc . sleep ( 200 )
  O00o0O . append ( OOO000000OOO0 )
  O00oOo0O0o00O += 1
 OoO0o000oOo = O00o0O [ 8 ] if 'Una' in O00o0O [ 8 ] else wiz . convertSize ( int ( float ( O00o0O [ 8 ] [ : - 8 ] ) ) * 1024 * 1024 )
 Oo00OO00o0oO = O00o0O [ 9 ] if 'Una' in O00o0O [ 9 ] else wiz . convertSize ( int ( float ( O00o0O [ 9 ] [ : - 8 ] ) ) * 1024 * 1024 )
 iI1 = O00o0O [ 10 ] if 'Una' in O00o0O [ 10 ] else wiz . convertSize ( int ( float ( O00o0O [ 10 ] [ : - 8 ] ) ) * 1024 * 1024 )
 I1I1i1i = wiz . convertSize ( int ( float ( O00o0O [ 11 ] [ : - 2 ] ) ) * 1024 * 1024 )
 OOo0O = wiz . convertSize ( int ( float ( O00o0O [ 12 ] [ : - 2 ] ) ) * 1024 * 1024 )
 oOOoooO0O0 = wiz . convertSize ( int ( float ( O00o0O [ 13 ] [ : - 2 ] ) ) * 1024 * 1024 )
 ii1O0ooooo000 , oooO00O , II1oOo00o = iIi1i1iIi1Ii1 ( )
 if 97 - 97: i11iIiiIii % iiIi111 / ii1Ii1I1Ii11i / ii1Ii1I1Ii11i
 Oo00oo0000OO ( '[B]Media Center Info:[/B]' , '' , icon = ooOoO00 , themeit = I1111i )
 Oo00oo0000OO ( '[COLOR %s]Name:[/COLOR] [COLOR %s]%s[/COLOR]' % ( Oo0O00O000 , i11I1IiII1i1i , O00o0O [ 0 ] ) , '' , icon = ooOoO00 , themeit = iIIii )
 Oo00oo0000OO ( '[COLOR %s]Version:[/COLOR] [COLOR %s]%s[/COLOR]' % ( Oo0O00O000 , i11I1IiII1i1i , O00o0O [ 1 ] ) , '' , icon = ooOoO00 , themeit = iIIii )
 Oo00oo0000OO ( '[COLOR %s]Platform:[/COLOR] [COLOR %s]%s[/COLOR]' % ( Oo0O00O000 , i11I1IiII1i1i , wiz . platform ( ) . title ( ) ) , '' , icon = ooOoO00 , themeit = iIIii )
 Oo00oo0000OO ( '[COLOR %s]CPU Usage:[/COLOR] [COLOR %s]%s[/COLOR]' % ( Oo0O00O000 , i11I1IiII1i1i , O00o0O [ 2 ] ) , '' , icon = ooOoO00 , themeit = iIIii )
 Oo00oo0000OO ( '[COLOR %s]Screen Mode:[/COLOR] [COLOR %s]%s[/COLOR]' % ( Oo0O00O000 , i11I1IiII1i1i , O00o0O [ 3 ] ) , '' , icon = ooOoO00 , themeit = iIIii )
 if 97 - 97: OO - Ii1I11I - O0ooO0o0O0O * oOOOOoo0OOO
 Oo00oo0000OO ( '[B]Uptime:[/B]' , '' , icon = ooOoO00 , themeit = I1111i )
 Oo00oo0000OO ( '[COLOR %s]Current Uptime:[/COLOR] [COLOR %s]%s[/COLOR]' % ( Oo0O00O000 , i11I1IiII1i1i , O00o0O [ 6 ] ) , '' , icon = ooOoO00 , themeit = I1111i )
 Oo00oo0000OO ( '[COLOR %s]Total Uptime:[/COLOR] [COLOR %s]%s[/COLOR]' % ( Oo0O00O000 , i11I1IiII1i1i , O00o0O [ 7 ] ) , '' , icon = ooOoO00 , themeit = I1111i )
 if 54 - 54: O0ooO0o0O0O
 Oo00oo0000OO ( '[B]Local Storage:[/B]' , '' , icon = ooOoO00 , themeit = I1111i )
 Oo00oo0000OO ( '[COLOR %s]Used Storage:[/COLOR] [COLOR %s]%s[/COLOR]' % ( Oo0O00O000 , i11I1IiII1i1i , OoO0o000oOo ) , '' , icon = ooOoO00 , themeit = I1111i )
 Oo00oo0000OO ( '[COLOR %s]Free Storage:[/COLOR] [COLOR %s]%s[/COLOR]' % ( Oo0O00O000 , i11I1IiII1i1i , Oo00OO00o0oO ) , '' , icon = ooOoO00 , themeit = I1111i )
 Oo00oo0000OO ( '[COLOR %s]Total Storage:[/COLOR] [COLOR %s]%s[/COLOR]' % ( Oo0O00O000 , i11I1IiII1i1i , iI1 ) , '' , icon = ooOoO00 , themeit = I1111i )
 if 5 - 5: o0o0OoOo0O0OO
 Oo00oo0000OO ( '[B]Ram Usage:[/B]' , '' , icon = ooOoO00 , themeit = I1111i )
 Oo00oo0000OO ( '[COLOR %s]Used Memory:[/COLOR] [COLOR %s]%s[/COLOR]' % ( Oo0O00O000 , i11I1IiII1i1i , I1I1i1i ) , '' , icon = ooOoO00 , themeit = I1111i )
 Oo00oo0000OO ( '[COLOR %s]Free Memory:[/COLOR] [COLOR %s]%s[/COLOR]' % ( Oo0O00O000 , i11I1IiII1i1i , OOo0O ) , '' , icon = ooOoO00 , themeit = I1111i )
 Oo00oo0000OO ( '[COLOR %s]Total Memory:[/COLOR] [COLOR %s]%s[/COLOR]' % ( Oo0O00O000 , i11I1IiII1i1i , oOOoooO0O0 ) , '' , icon = ooOoO00 , themeit = I1111i )
 if 84 - 84: OO * iiIi111 * OO % o0o0OoOo0O0OO / oOOOOoo0OOO
 Oo00oo0000OO ( '[B]Network:[/B]' , '' , icon = ooOoO00 , themeit = I1111i )
 Oo00oo0000OO ( '[COLOR %s]Local IP:[/COLOR] [COLOR %s]%s[/COLOR]' % ( Oo0O00O000 , i11I1IiII1i1i , O00o0O [ 4 ] ) , '' , icon = ooOoO00 , themeit = I1111i )
 Oo00oo0000OO ( '[COLOR %s]External IP:[/COLOR] [COLOR %s]%s[/COLOR]' % ( Oo0O00O000 , i11I1IiII1i1i , ii1O0ooooo000 ) , '' , icon = ooOoO00 , themeit = I1111i )
 Oo00oo0000OO ( '[COLOR %s]Provider:[/COLOR] [COLOR %s]%s[/COLOR]' % ( Oo0O00O000 , i11I1IiII1i1i , oooO00O ) , '' , icon = ooOoO00 , themeit = I1111i )
 Oo00oo0000OO ( '[COLOR %s]Location:[/COLOR] [COLOR %s]%s[/COLOR]' % ( Oo0O00O000 , i11I1IiII1i1i , II1oOo00o ) , '' , icon = ooOoO00 , themeit = I1111i )
 oOOOO ( '[COLOR %s]MacAddress:[/COLOR] [COLOR %s]%s[/COLOR]' % ( Oo0O00O000 , i11I1IiII1i1i , O00o0O [ 5 ] ) , '' , icon = ooOoO00 , themeit = I1111i )
 if 100 - 100: o0o0OoOo0O0OO . i1III1I - O0ooO0o0O0O . i11iIiiIii / OO
 if 71 - 71: Ii1I11I * ii1Ii1I1Ii11i . Iii1I1i
 if 49 - 49: o0o0OoOo0O0OO * IIOOOO0oo0 . o0o0OoOo0O0OO
 if 19 - 19: OO - o0o0OoOo0O0OO
def OOOOo000o00OO ( ) :
 xbmc . executebuiltin ( 'Runscript("special://home/addons/plugin.program.SpinzTV/ookla.py")' )
 if 96 - 96: IIOOOO0oo0 . oOoOoo % oo0 + i11iIiiIii - oOoOoo * oo0
 if 33 - 33: oo0 % oO0Oo0O0o - iiIi111 . IIOOOO0oo0 / IIOOOO0oo0
 if 96 - 96: oOoooo0O0Oo + o0o0OoOo0O0OO * IIOOOO0oo0
 if 86 - 86: i1III1I
def IiII1i1iI ( ) :
 O0OOO00 ( )
 ooOOo0o ( '[COLORsteelblue]LOGIN[/COLOR]' , '' , 'addonopen' , ooOoOoo0O , II , '' )
 if 50 - 50: OO - Ii1I11I + O0ooO0o0O0O + O0ooO0o0O0O
 if 91 - 91: OO - IIOOOO0oo0 . O0ooO0o0O0O . IIOOOO0oo0 + oOOOOOOo0O00o - OO
 iiIiiIi1 ( '[COLORsteelblue]Stream Lists[/COLOR]' , '' , 'streams' , ooOoOoo0O , II , '' )
 if 30 - 30: oOoOoo + OO - o0o0OoOo0O0OO * oOoooo0O0Oo
 if 19 - 19: o0o0OoOo0O0OO - Ii1iI1I1 . O0ooO0o0O0O . oOOoo00O00o / oOoOoo
def O0OOO00 ( ) :
 if Oooo000o == 'insert_password' :
  IiII . ok ( '[COLORsteelblue]Spinz Tv Pro Login[/COLOR]' , 'You need to set username and password to access this' , 'These are unique and provided upon purchase ' , ' @ [COLORsteelblue]https://www.facebook.com/groups/614286415341465/[/COLOR]' )
  ooo0OO . openSettings ( sys . argv [ 0 ] )
  if 87 - 87: oOOoo00O00o - oo0 - oOoOoo + ii1Ii1I1Ii11i % O0ooO0o0O0O / i11iIiiIii
  if 12 - 12: oo0
  if 86 - 86: iiIi111 - I111I1Iiii1i
  if 63 - 63: oOOOOoo0OOO / oOOoo00O00o + oOoooo0O0Oo . Iii1I1i . oo0
  if 48 - 48: oO0Oo0O0o - oO00oOOoooO - i11iIiiIii . Iii1I1i - oO00oOOoooO * Iii1I1i
  if 60 - 60: oOOoo00O00o / oOOOOOOo0O00o + oOoOoo - oO00oOOoooO
  if 49 - 49: I111I1Iiii1i - IIOOOO0oo0 / I111I1Iiii1i * oOOoo00O00o + Ii1I11I
  if 35 - 35: OO . oOOOOoo0OOO / oO0Oo0O0o / oOOOOoo0OOO * iiIi111
  if 85 - 85: OO . oo0 % oOoOoo % Iii1I1i
def OOo00ooOoO0o ( ) :
 iiIiiIi1 ( 'Full List' , '' , 'getlistplay' , ooOoOoo0O , II , '' )
 iiIiiIi1 ( 'Entertainment - USA/CA' , '' , 'getlistplay' , ooOoOoo0O , II , '' )
 iiIiiIi1 ( 'Entertainment - UK' , '' , 'getlistplay' , ooOoOoo0O , II , '' )
 iiIiiIi1 ( 'Sports - US/CA' , '' , 'getlistplay' , ooOoOoo0O , II , '' )
 iiIiiIi1 ( 'UK Sports' , '' , 'getlistplay' , ooOoOoo0O , II , '' )
 iiIiiIi1 ( 'NBA / NFL / NHL' , '' , 'getlistplay' , ooOoOoo0O , II , '' )
 iiIiiIi1 ( 'Football' , '' , 'getlistplay' , ooOoOoo0O , II , '' )
 iiIiiIi1 ( 'Boxing / UFC / WWE' , '' , 'getlistplay' , ooOoOoo0O , II , '' )
 iiIiiIi1 ( 'World Sports' , '' , 'getlistplay' , ooOoOoo0O , II , '' )
 iiIiiIi1 ( 'Cinema' , '' , 'getlistplay' , ooOoOoo0O , II , '' )
 iiIiiIi1 ( 'Kids' , '' , 'getlistplay' , ooOoOoo0O , II , '' )
 iiIiiIi1 ( 'News Networks' , '' , 'getlistplay' , ooOoOoo0O , II , '' )
 iiIiiIi1 ( 'Music' , '' , 'getlistplay' , ooOoOoo0O , II , '' )
 iiIiiIi1 ( 'Education / Lifestyle' , '' , 'getlistplay' , ooOoOoo0O , II , '' )
 iiIiiIi1 ( 'Sci-Fi Movies' , '' , 'getlistplay' , ooOoOoo0O , II , '' )
 if 21 - 21: i11iIiiIii
def o00iIiiiII ( name ) :
 Ii1I1 = name
 OO0ooO0 = O0o00OOo00O0O ( oO00oOo ( '' ) )
 o000O000 = re . compile ( '#EXTINF:.+? tvg-name="(.+?)" tvg-logo="(.+?)" group-title="Live Events"",.+?\n(.+?)\n' ) . findall ( OO0ooO0 )
 for name , iiI1iIIiI , i1Ii11II in o000O000 :
  i1Ii11II = ( i1Ii11II ) . replace ( 'replace_user' , OOOo0 ) . replace ( 'replace_pass' , Oooo000o )
  ooOOo0o ( ( '' + name + '' ) . replace ( '_' , ' ' ) , ( i1Ii11II ) . strip ( ) , 'resolve' , iiI1iIIiI , iiI1iIIiI , '' )
 else :
  ooOOo0o ( '[COLORred]Streams will appear here for live events when available[/COLOR]' , '' , 'resolve' , '' , '' , '' )
  if 95 - 95: O0ooO0o0O0O . o0o0OoOo0O0OO - oOoooo0O0Oo * I111I1Iiii1i / Ii1iI1I1
def oOo0OO0o0 ( ) :
 xbmc . executebuiltin ( "XBMC.RunScript(" + iiIIIII1i1iI + ")" )
 II1I1I ( )
 if 23 - 23: I111I1Iiii1i + o0o0OoOo0O0OO + ii1Ii1I1Ii11i % O0ooO0o0O0O . i11iIiiIii
 if 81 - 81: oOOOOoo0OOO . oOoooo0O0Oo * i1III1I . iiIi111 - IIOOOO0oo0 * iiIi111
def OoO0Oo00 ( name ) :
 Ii1I1 = name
 OO0ooO0 = O0o00OOo00O0O ( 'http://spinztvpro.tk:8000/get.php?username=' + OOOo0 + '&password=' + Oooo000o + '&type=m3u_plus&output=m3u8' )
 o000O000 = re . compile ( '#EXTINF:.+? tvg-name="([^"]*)" tvg-logo="([^"]*)" group-title="([^"]*)",.+?\n(.+?)\n' ) . findall ( OO0ooO0 )
 for name , iiI1iIIiI , i11IiI1I , i1Ii11II in o000O000 :
  if Ii1I1 == 'Full List' :
   i1Ii11II = ( i1Ii11II ) . replace ( '.ts' , '.m3u8' )
   ooOOo0o ( ( '' + name + '' ) . replace ( '_' , ' ' ) , ( i1Ii11II ) . strip ( ) , 'resolve' , iiI1iIIiI , iiI1iIIiI , '' )
  else :
   Ii1I1 = ( Ii1I1 ) . replace ('World','القنوات العربية')
   if Ii1I1 in i11IiI1I :
    i1Ii11II = ( i1Ii11II ) . replace ( '.ts' , '.m3u8' )
    print i1Ii11II + '>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>'
    ooOOo0o ( ( '' + name + '' ) . replace ( '_' , ' ' ) , ( i1Ii11II ) . strip ( ) , 'resolve' , iiI1iIIiI , iiI1iIIiI , '' )
   else :
    pass
def OOoooO00o0o ( ) :
 II1I1I ( )
 try :
  I1ii1Ii1 = gui . TVGuide ( )
  I1ii1Ii1 . doModal ( )
  del I1ii1Ii1
  if 73 - 73: IIOOOO0oo0 . iiIi111 + i11iIiiIii + O0ooO0o0O0O - Iii1I1i / oOOoo00O00o
 except :
  import sys
  import traceback as tb
  ( OO0OOOOo0000O , i1Ii11ii , traceback ) = sys . exc_info ( )
  tb . print_exception ( OO0OOOOo0000O , i1Ii11ii , traceback )
  if 89 - 89: ii1Ii1I1Ii11i + oOOOOOOo0O00o - Ii1iI1I1
def O0o00OOo00O0O ( url ) :
 IiI1ii1Ii = urllib2 . Request ( url )
 IiI1ii1Ii . add_header ( 'User-Agent' , 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3' )
 oooOOOoOOOo0O = urllib2 . urlopen ( IiI1ii1Ii )
 O0oOOo0Oo = oooOOOoOOOo0O . read ( )
 oooOOOoOOOo0O . close ( )
 return O0oOOo0Oo
 if 40 - 40: I111I1Iiii1i + I111I1Iiii1i
 if 94 - 94: oO00oOOoooO * O0ooO0o0O0O . Iii1I1i
 if 13 - 13: O0ooO0o0O0O * oOOoo00O00o / Ii1I11I % oo0 + iiIi111
def II1I1I ( ) :
 iiiI1iI1 = os . path . join ( I1i1iiI1 , 'addons.ini' )
 I1oOoO0OOO00O = open ( iiiI1iI1 , "w+" )
 OO0ooO0 = O0o00OOo00O0O ( 'http://spinztvpro.tk:8000/get.php?username=' + OOOo0 + '&password=' + Oooo000o + '&type=m3u_plus&output=m3u8' )
 o000O000 = re . compile ( '#EXTINF:.+? tvg-name="([^"]*)" tvg-logo="([^"]*)" group-title="([^"]*)",.+?\n(.+?).ts' ) . findall ( OO0ooO0 )
 I1oOoO0OOO00O . write ( r'[' + OO0o + ']' + '\n' )
 for oO0o0O0Ooo0o , iiI1iIIiI , i11IiI1I , i1Ii11II in o000O000 :
  i1Ii11II = ( i1Ii11II + '.m3u8' ) . replace ( ':' , '%3A' ) . replace ( '/' , '%2F' )
  OOOOO0o0OOo = ( oO0o0O0Ooo0o + '=plugin://' + OO0o + '/?url=' + i1Ii11II + '&mode=resolve&name=' + ( oO0o0O0Ooo0o ) . replace ( ' ' , '+' ) + '&amp;iconimage=' + ( iiI1iIIiI ) . replace ( ' ' , '' ) + '+&amp;fanart=' + ( iiI1iIIiI ) . replace ( ' ' , '' ) + '+&amp;description=' )
  I1oOoO0OOO00O . write ( OOOOO0o0OOo + '\n' )
  if 40 - 40: o0o0OoOo0O0OO * iiIi111 % Iii1I1i * oOOOOOOo0O00o
  if 80 - 80: O0ooO0o0O0O - oOoooo0O0Oo - oOOOOOOo0O00o - oOOOOOOo0O00o . oOoooo0O0Oo
def I1iI11I ( url ) :
 Oo0oOO = xbmc . Player ( ooooo ( ) )
 import urlresolver
 try : Oo0oOO . play ( url ) . strip ( )
 except : pass
 if 26 - 26: oOOOOoo0OOO
 if 41 - 41: oOOOOoo0OOO - i11iIiiIii
def ooooo ( ) :
 try :
  iIiI1 = getSet ( "core-player" )
  if ( iIiI1 == 'DVDPLAYER' ) : iII1IiiIIII = xbmc . PLAYER_CORE_DVDPLAYER
  elif ( iIiI1 == 'MPLAYER' ) : iII1IiiIIII = xbmc . PLAYER_CORE_MPLAYER
  elif ( iIiI1 == 'PAPLAYER' ) : iII1IiiIIII = xbmc . PLAYER_CORE_PAPLAYER
  else : iII1IiiIIII = xbmc . PLAYER_CORE_AUTO
 except : iII1IiiIIII = xbmc . PLAYER_CORE_AUTO
 return iII1IiiIIII
 return True
 if 24 - 24: oo0 / oO0Oo0O0o % i1III1I - I111I1Iiii1i / iiIi111 . oO0Oo0O0o
 if 97 - 97: i1III1I * I111I1Iiii1i - Ii1I11I
 if 46 - 46: oOOoo00O00o
 if 83 - 83: i11iIiiIii * Ii1I11I
 if 49 - 49: ii1Ii1I1Ii11i * iiIi111 + Ii1iI1I1 - i11iIiiIii
def OOooO ( ) :
 OoO0000o = '[COLOR green]ON[/COLOR]' ; o0Ii1 = '[COLOR red]OFF[/COLOR]'
 i1i1Ii1Ii = 'true' if i1Oo00 == 'true' else 'false'
 oOo0OoO = 'true' if i1i == 'true' else 'false'
 O000O0 = 'true' if iiI111I1iIiI == 'true' else 'false'
 o0O00Oo0o0Oooo0 = 'true' if OOoOO0oo0ooO == 'true' else 'false'
 ii1iIIi11 = 'true' if O00O0oOO00O00 == 'true' else 'false'
 iI1IIIII1Ii = 'true' if O0o0O00Oo0o0 == 'true' else 'false'
 iIiI1I1IiII1I1i1I1 = 'true' if Oo0OoO00oOO0o == 'true' else 'false'
 if 28 - 28: ii1Ii1I1Ii11i + o0o0OoOo0O0OO % OO / I111I1Iiii1i + i11iIiiIii
 IiI11i1IIiiI ( 'Keep Trakt Data' , 'trakt' , icon = oooO , themeit = oo )
 IiI11i1IIiiI ( 'Keep Real Debrid' , 'realdebrid' , icon = i1I1i111Ii , themeit = oo )
 IiI11i1IIiiI ( 'Keep Login Info' , 'login' , icon = oo0o , themeit = oo )
 Oo00oo0000OO ( '- Click to toggle settings -' , '' , themeit = iIIii )
 Oo00oo0000OO ( 'Save Trakt: %s' % i1i1Ii1Ii . replace ( 'true' , OoO0000o ) . replace ( 'false' , o0Ii1 ) , 'togglesetting' , 'keeptrakt' , icon = oooO , themeit = oo )
 Oo00oo0000OO ( 'Save Real Debrid: %s' % oOo0OoO . replace ( 'true' , OoO0000o ) . replace ( 'false' , o0Ii1 ) , 'togglesetting' , 'keepdebrid' , icon = i1I1i111Ii , themeit = oo )
 Oo00oo0000OO ( 'Save Login Info: %s' % O000O0 . replace ( 'true' , OoO0000o ) . replace ( 'false' , o0Ii1 ) , 'togglesetting' , 'keeplogin' , icon = oo0o , themeit = oo )
 Oo00oo0000OO ( 'Keep \'Sources.xml\': %s' % o0O00Oo0o0Oooo0 . replace ( 'true' , OoO0000o ) . replace ( 'false' , o0Ii1 ) , 'togglesetting' , 'keepsources' , icon = i111iIi1i1II1 , themeit = oo )
 Oo00oo0000OO ( 'Keep \'Profiles.xml\': %s' % iI1IIIII1Ii . replace ( 'true' , OoO0000o ) . replace ( 'false' , o0Ii1 ) , 'togglesetting' , 'keepprofiles' , icon = i111iIi1i1II1 , themeit = oo )
 Oo00oo0000OO ( 'Keep \'Advancedsettings.xml\': %s' % ii1iIIi11 . replace ( 'true' , OoO0000o ) . replace ( 'false' , o0Ii1 ) , 'togglesetting' , 'keepadvanced' , icon = i111iIi1i1II1 , themeit = oo )
 Oo00oo0000OO ( 'Keep \'Favourites.xml\': %s' % iIiI1I1IiII1I1i1I1 . replace ( 'true' , OoO0000o ) . replace ( 'false' , o0Ii1 ) , 'togglesetting' , 'keepfavourites' , icon = i111iIi1i1II1 , themeit = oo )
 oOOo000oOoO0 ( 'files' , 'viewType' )
 if 20 - 20: oOOOOOOo0O00o
 if 3 - 3: I111I1Iiii1i * oO0Oo0O0o . oOOOOoo0OOO . IIOOOO0oo0 - oOOoo00O00o
def OOoooOoO0 ( ) :
 i1i1Ii1Ii = '[COLOR green]ON[/COLOR]' if i1Oo00 == 'true' else '[COLOR red]OFF[/COLOR]'
 O0OOoooo0 = str ( ooOooo000oOO ) if not ooOooo000oOO == '' else 'Trakt hasnt been saved yet.'
 Oo00oo0000OO ( '[I]Register FREE Account at http://trakt.tv[/I]' , '' , icon = oooO , themeit = iIIii )
 Oo00oo0000OO ( 'Save Trakt Data: %s' % i1i1Ii1Ii , 'togglesetting' , 'keeptrakt' , icon = oooO , themeit = iIIii )
 if i1Oo00 == 'true' : oOOOO ( 'Last Save: %s' % str ( O0OOoooo0 ) , '' , icon = oooO , themeit = iIIii )
 if IiIi11iI == 'No' : oOOOO ( wiz . sep ( ) , '' , icon = oooO , themeit = iIIii )
 if 7 - 7: Ii1I11I
 for i1i1Ii1Ii in traktit . ORDER :
  oO0o0O0Ooo0o = I1III1111iIi [ i1i1Ii1Ii ] [ 'name' ]
  ii1IiIi1i = I1III1111iIi [ i1i1Ii1Ii ] [ 'path' ]
  OOOO00OoooO = I1III1111iIi [ i1i1Ii1Ii ] [ 'saved' ]
  file = I1III1111iIi [ i1i1Ii1Ii ] [ 'file' ]
  IIIi = wiz . getS ( OOOO00OoooO )
  Ii1iiI1 = traktit . traktUser ( i1i1Ii1Ii )
  iII11I1Ii1 = I1III1111iIi [ i1i1Ii1Ii ] [ 'icon' ] if os . path . exists ( ii1IiIi1i ) else oooO
  o0o0 = I1III1111iIi [ i1i1Ii1Ii ] [ 'fanart' ] if os . path . exists ( ii1IiIi1i ) else II
  OOOoO = I1i ( 'saveaddon' , 'Trakt' , i1i1Ii1Ii )
  o0ooOOoO0oO0 = I1i ( 'save' , 'Trakt' , i1i1Ii1Ii )
  OOOoO . append ( ( I1111i % '%s Settings' % oO0o0O0Ooo0o , 'RunPlugin(plugin://%s/?mode=opensettings&name=%s&url=trakt)' % ( OO0o , i1i1Ii1Ii ) ) )
  if 86 - 86: oO0Oo0O0o / i1III1I * oOOOOoo0OOO
  Oo00oo0000OO ( '[+]-> %s' % oO0o0O0Ooo0o , '' , icon = iII11I1Ii1 , fanart = o0o0 , themeit = iIIii )
  if not os . path . exists ( ii1IiIi1i ) : oOOOO ( '[COLOR red]Addon Data: Not Installed[/COLOR]' , '' , icon = iII11I1Ii1 , fanart = o0o0 , menu = OOOoO )
  elif not Ii1iiI1 : oOOOO ( '[COLOR red]Addon Data: Not Registered[/COLOR]' , 'authtrakt' , i1i1Ii1Ii , icon = iII11I1Ii1 , fanart = o0o0 , menu = OOOoO )
  else : oOOOO ( '[COLOR green]Addon Data: %s[/COLOR]' % Ii1iiI1 , 'authtrakt' , i1i1Ii1Ii , icon = iII11I1Ii1 , fanart = o0o0 , menu = OOOoO )
  if IIIi == "" :
   if os . path . exists ( file ) : oOOOO ( '[COLOR red]Saved Data: Save File Found(Import Data)[/COLOR]' , 'importtrakt' , i1i1Ii1Ii , icon = iII11I1Ii1 , fanart = o0o0 , menu = o0ooOOoO0oO0 )
   else : oOOOO ( '[COLOR red]Saved Data: Not Saved[/COLOR]' , 'savetrakt' , i1i1Ii1Ii , icon = iII11I1Ii1 , fanart = o0o0 , menu = o0ooOOoO0oO0 )
  else : oOOOO ( '[COLOR green]Saved Data: %s[/COLOR]' % IIIi , '' , icon = iII11I1Ii1 , fanart = o0o0 , menu = o0ooOOoO0oO0 )
  if 67 - 67: oOOOOOOo0O00o * oOOOOOOo0O00o / iiIi111 * oOoooo0O0Oo + oOOoo00O00o
 if IiIi11iI == 'No' : oOOOO ( wiz . sep ( ) , '' , themeit = iIIii )
 Oo00oo0000OO ( 'Save All Trakt Data' , 'savetrakt' , 'all' , icon = oooO , themeit = iIIii )
 Oo00oo0000OO ( 'Recover All Saved Trakt Data' , 'restoretrakt' , 'all' , icon = oooO , themeit = iIIii )
 Oo00oo0000OO ( 'Import Trakt Data' , 'importtrakt' , 'all' , icon = oooO , themeit = iIIii )
 Oo00oo0000OO ( 'Clear All Saved Trakt Data' , 'cleartrakt' , 'all' , icon = oooO , themeit = iIIii )
 Oo00oo0000OO ( 'Clear All Addon Data' , 'addontrakt' , 'all' , icon = oooO , themeit = iIIii )
 oOOo000oOoO0 ( 'files' , 'viewType' )
 if 79 - 79: oO0Oo0O0o
def iIi1 ( ) :
 oOo0OoO = '[COLOR green]ON[/COLOR]' if i1i == 'true' else '[COLOR red]OFF[/COLOR]'
 O0OOoooo0 = str ( Oo0oOOo ) if not Oo0oOOo == '' else 'Real Debrid hasnt been saved yet.'
 Oo00oo0000OO ( '[I]http://real-debrid.com is a PAID service.[/I]' , '' , icon = i1I1i111Ii , themeit = iIIii )
 Oo00oo0000OO ( 'Save Real Debrid Data: %s' % oOo0OoO , 'togglesetting' , 'keepdebrid' , icon = i1I1i111Ii , themeit = iIIii )
 if i1i == 'true' : oOOOO ( 'Last Save: %s' % str ( O0OOoooo0 ) , '' , icon = i1I1i111Ii , themeit = iIIii )
 if IiIi11iI == 'No' : oOOOO ( wiz . sep ( ) , '' , icon = i1I1i111Ii , themeit = iIIii )
 if 96 - 96: oO0Oo0O0o % oOoooo0O0Oo
 for ooiI1i in debridit . ORDER :
  oO0o0O0Ooo0o = I1i111I [ ooiI1i ] [ 'name' ]
  ii1IiIi1i = I1i111I [ ooiI1i ] [ 'path' ]
  OOOO00OoooO = I1i111I [ ooiI1i ] [ 'saved' ]
  file = I1i111I [ ooiI1i ] [ 'file' ]
  IIIi = wiz . getS ( OOOO00OoooO )
  Ii1iiI1 = debridit . debridUser ( ooiI1i )
  iII11I1Ii1 = I1i111I [ ooiI1i ] [ 'icon' ] if os . path . exists ( ii1IiIi1i ) else i1I1i111Ii
  o0o0 = I1i111I [ ooiI1i ] [ 'fanart' ] if os . path . exists ( ii1IiIi1i ) else II
  OOOoO = I1i ( 'saveaddon' , 'Debrid' , ooiI1i )
  o0ooOOoO0oO0 = I1i ( 'save' , 'Debrid' , ooiI1i )
  OOOoO . append ( ( I1111i % '%s Settings' % oO0o0O0Ooo0o , 'RunPlugin(plugin://%s/?mode=opensettings&name=%s&url=debrid)' % ( OO0o , ooiI1i ) ) )
  if 3 - 3: o0o0OoOo0O0OO / Iii1I1i
  Oo00oo0000OO ( '[+]-> %s' % oO0o0O0Ooo0o , '' , icon = iII11I1Ii1 , fanart = o0o0 , themeit = iIIii )
  if not os . path . exists ( ii1IiIi1i ) : Oo00oo0000OO ( '[COLOR red]Addon Data: Not Installed[/COLOR]' , '' , icon = iII11I1Ii1 , fanart = o0o0 , menu = OOOoO )
  elif not Ii1iiI1 : Oo00oo0000OO ( '[COLOR red]Addon Data: Not Registered[/COLOR]' , 'authdebrid' , ooiI1i , icon = iII11I1Ii1 , fanart = o0o0 , menu = OOOoO )
  else : Oo00oo0000OO ( '[COLOR green]Addon Data: %s[/COLOR]' % Ii1iiI1 , 'authdebrid' , ooiI1i , icon = iII11I1Ii1 , fanart = o0o0 , menu = OOOoO )
  if IIIi == "" :
   if os . path . exists ( file ) : Oo00oo0000OO ( '[COLOR red]Saved Data: Save File Found(Import Data)[/COLOR]' , 'importdebrid' , ooiI1i , icon = iII11I1Ii1 , fanart = o0o0 , menu = o0ooOOoO0oO0 )
   else : Oo00oo0000OO ( '[COLOR red]Saved Data: Not Saved[/COLOR]' , 'savedebrid' , ooiI1i , icon = iII11I1Ii1 , fanart = o0o0 , menu = o0ooOOoO0oO0 )
  else : Oo00oo0000OO ( '[COLOR green]Saved Data: %s[/COLOR]' % IIIi , '' , icon = iII11I1Ii1 , fanart = o0o0 , menu = o0ooOOoO0oO0 )
  if 34 - 34: i11iIiiIii / Ii1I11I * oOoOoo . ii1Ii1I1Ii11i
 if IiIi11iI == 'No' : oOOOO ( wiz . sep ( ) , '' , themeit = iIIii )
 Oo00oo0000OO ( 'Save All Real Debrid Data' , 'savedebrid' , 'all' , icon = i1I1i111Ii , themeit = iIIii )
 Oo00oo0000OO ( 'Recover All Saved Real Debrid Data' , 'restoredebrid' , 'all' , icon = i1I1i111Ii , themeit = iIIii )
 Oo00oo0000OO ( 'Import Real Debrid Data' , 'importdebrid' , 'all' , icon = i1I1i111Ii , themeit = iIIii )
 Oo00oo0000OO ( 'Clear All Saved Real Debrid Data' , 'cleardebrid' , 'all' , icon = i1I1i111Ii , themeit = iIIii )
 Oo00oo0000OO ( 'Clear All Addon Data' , 'addondebrid' , 'all' , icon = i1I1i111Ii , themeit = iIIii )
 oOOo000oOoO0 ( 'files' , 'viewType' )
 if 79 - 79: Ii1I11I
def iI11111ii11 ( ) :
 iI1iiI = glob . glob ( os . path . join ( II1 , '*/' ) )
 for Iii11111iiI in sorted ( iI1iiI , key = lambda O00oOo0O0o00O : O00oOo0O0o00O ) :
  o0OOOOoO = Iii11111iiI . replace ( II1 , '' ) . replace ( '\\' , '' ) . replace ( '/' , '' )
  iII11I1Ii1 = os . path . join ( Iii11111iiI , 'icon.png' )
  o0o0 = os . path . join ( Iii11111iiI , 'fanart.png' )
  if o0OOOOoO in o0OIiII : pass
  elif o0OOOOoO == 'packages' : pass
  else :
   OoO0Ooo = o0OOOOoO
   Ii1I1I = { 'audio.' : '[COLOR orange][AUDIO] [/COLOR]' , 'metadata.' : '[COLOR cyan][METADATA] [/COLOR]' , 'module.' : '[COLOR orange][MODULE] [/COLOR]' , 'plugin.' : '[COLOR blue][PLUGIN] [/COLOR]' , 'program.' : '[COLOR orange][PROGRAM] [/COLOR]' , 'repository.' : '[COLOR gold][REPO] [/COLOR]' , 'script.' : '[COLOR green][SCRIPT] [/COLOR]' , 'service.' : '[COLOR green][SERVICE] [/COLOR]' , 'skin.' : '[COLOR dodgerblue][SKIN] [/COLOR]' , 'video.' : '[COLOR orange][VIDEO] [/COLOR]' , 'weather.' : '[COLOR yellow][WEATHER] [/COLOR]' }
   for oOOoOOO0oOoo in Ii1I1I :
    OoO0Ooo = OoO0Ooo . replace ( oOOoOOO0oOoo , Ii1I1I [ oOOoOOO0oOoo ] )
   Oo00oo0000OO ( '[COLOR red][B][REMOVE][/B][/COLOR] %s' % OoO0Ooo , 'removeaddon' , o0OOOOoO , icon = iII11I1Ii1 , fanart = o0o0 , themeit = I1111i )
 oOOo000oOoO0 ( 'files' , 'viewType' )
 if 65 - 65: oO00oOOoooO . iiIi111 - i1III1I
def ooii11i ( ) :
 if os . path . exists ( i1iiIII111ii ) :
  Oo00oo0000OO ( '[COLOR red][B][REMOVE][/B][/COLOR] All Addon_Data' , 'removedata' , 'all' , themeit = I1111i )
  Oo00oo0000OO ( '[COLOR red][B][REMOVE][/B][/COLOR] All Addon_Data for Uninstalled Addons' , 'removedata' , 'uninstalled' , themeit = I1111i )
  Oo00oo0000OO ( '[COLOR red][B][REMOVE][/B][/COLOR] All Empty Folders in Addon_Data' , 'removedata' , 'empty' , themeit = I1111i )
  Oo00oo0000OO ( '[COLOR red][B][REMOVE][/B][/COLOR] %s Addon_Data' % iiiii , 'resetaddon' , themeit = I1111i )
  if IiIi11iI == 'No' : oOOOO ( wiz . sep ( ) , '' , themeit = iIIii )
  iI1iiI = glob . glob ( os . path . join ( i1iiIII111ii , '*/' ) )
  for Iii11111iiI in sorted ( iI1iiI , key = lambda O00oOo0O0o00O : O00oOo0O0o00O ) :
   o0OOOOoO = Iii11111iiI . replace ( i1iiIII111ii , '' ) . replace ( '\\' , '' ) . replace ( '/' , '' )
   iII11I1Ii1 = os . path . join ( Iii11111iiI . replace ( i1iiIII111ii , II1 ) , 'icon.png' )
   o0o0 = os . path . join ( Iii11111iiI . replace ( i1iiIII111ii , II1 ) , 'fanart.png' )
   OoO0Ooo = o0OOOOoO
   Ii1I1I = { 'audio.' : '[COLOR orange][AUDIO] [/COLOR]' , 'metadata.' : '[COLOR cyan][METADATA] [/COLOR]' , 'module.' : '[COLOR orange][MODULE] [/COLOR]' , 'plugin.' : '[COLOR blue][PLUGIN] [/COLOR]' , 'program.' : '[COLOR orange][PROGRAM] [/COLOR]' , 'repository.' : '[COLOR gold][REPO] [/COLOR]' , 'script.' : '[COLOR green][SCRIPT] [/COLOR]' , 'service.' : '[COLOR green][SERVICE] [/COLOR]' , 'skin.' : '[COLOR dodgerblue][SKIN] [/COLOR]' , 'video.' : '[COLOR orange][VIDEO] [/COLOR]' , 'weather.' : '[COLOR yellow][WEATHER] [/COLOR]' }
   for oOOoOOO0oOoo in Ii1I1I :
    OoO0Ooo = OoO0Ooo . replace ( oOOoOOO0oOoo , Ii1I1I [ oOOoOOO0oOoo ] )
   if o0OOOOoO in o0OIiII : OoO0Ooo = '[COLOR green][B][PROTECTED][/B][/COLOR] %s' % OoO0Ooo
   else : OoO0Ooo = '[COLOR red][B][REMOVE][/B][/COLOR] %s' % OoO0Ooo
   oOOOO ( ' %s' % OoO0Ooo , 'removedata' , o0OOOOoO , icon = iII11I1Ii1 , fanart = o0o0 , themeit = I1111i )
 else :
  Oo00oo0000OO ( 'No Addon data folder found.' , '' , themeit = iIIii )
 oOOo000oOoO0 ( 'files' , 'viewType' )
 if 71 - 71: i1III1I * Ii1I11I % OO . i1III1I % I111I1Iiii1i + oOOOOOOo0O00o
def o0oOo0OO ( ) :
 Oo00oo0000OO ( "[I][B][COLOR red]!!Notice: Disabling Some Addons Can Cause Issues!![/COLOR][/B][/I]" , '' , icon = ooOoO00 )
 iI1iiI = glob . glob ( os . path . join ( II1 , '*/' ) )
 for Iii11111iiI in sorted ( iI1iiI , key = lambda O00oOo0O0o00O : O00oOo0O0o00O ) :
  if OO0o in Iii11111iiI : continue
  OO0oo00oOO = os . path . join ( Iii11111iiI , 'addon.xml' )
  if os . path . exists ( OO0oo00oOO ) :
   iI1iiI = Iii11111iiI . replace ( II1 , '' ) [ 1 : - 1 ]
   iIiIIiI1i1Ii = open ( OO0oo00oOO )
   iI1i1IiIIIIi = iIiIIiI1i1Ii . read ( ) . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
   o000O000 = re . compile ( '<addo.+?id="(.+?)".+?>' ) . findall ( iI1i1IiIIIIi )
   II1i = re . compile ( '<addo.+? name="(.+?)".+?>' ) . findall ( iI1i1IiIIIIi )
   try :
    i1IiIi1 = o000O000 [ 0 ]
    oO0o0O0Ooo0o = II1i [ 0 ]
   except :
    continue
   try :
    OooO0ooo0 = xbmcaddon . Addon ( id = i1IiIi1 )
    IIiii = "[COLOR green][Enabled][/COLOR]"
    I1iOO0O0O = "false"
   except :
    IIiii = "[COLOR red][Disabled][/COLOR]"
    I1iOO0O0O = "true"
    pass
   iII11I1Ii1 = os . path . join ( Iii11111iiI , 'icon.png' ) if os . path . exists ( os . path . join ( Iii11111iiI , 'icon.png' ) ) else ooOoOoo0O
   o0o0 = os . path . join ( Iii11111iiI , 'fanart.jpg' ) if os . path . exists ( os . path . join ( Iii11111iiI , 'fanart.jpg' ) ) else II
   Oo00oo0000OO ( "%s %s" % ( IIiii , oO0o0O0Ooo0o ) , 'toggleaddon' , iI1iiI , I1iOO0O0O , icon = iII11I1Ii1 , fanart = o0o0 )
   iIiIIiI1i1Ii . close ( )
 oOOo000oOoO0 ( 'files' , 'viewType' )
 if 33 - 33: i1III1I
def ooOOO00oOOooO ( ) :
 IiiI1iiI1III1i = [ 'Every Startup' , 'Every Day' , 'Every Three Days' , 'Every Weekly' ]
 IiIIii1iiI = IiiIII111iI . select ( "[COLOR %s]How often would you list to Auto Clean on Startup?[/COLOR]" % i11I1IiII1i1i , IiiI1iiI1III1i )
 if not IiIIii1iiI == - 1 :
  wiz . setS ( 'autocleanfeq' , str ( IiIIii1iiI ) )
  wiz . LogNotify ( 'Auto Clean Up' , 'Fequency Now %s' % IiiI1iiI1III1i [ IiIIii1iiI ] )
  if 7 - 7: Ii1iI1I1
  if 18 - 18: oOoooo0O0Oo + Ii1iI1I1 . IIOOOO0oo0 + o0o0OoOo0O0OO * oO0Oo0O0o . I111I1Iiii1i
  if 71 - 71: Ii1I11I - Ii1iI1I1 - oOoOoo
  if 28 - 28: O0ooO0o0O0O
def iI11II1i1I1 ( ) :
 Oo00oo0000OO ( 'Test Update' , 'testupdate' , themeit = oo )
 Oo00oo0000OO ( 'Test First Run' , 'testfirst' , themeit = oo )
 oOOo000oOoO0 ( 'files' , 'viewType' )
 oOOOO ( 'Convert Paths to special' , 'convertpath' , icon = ooOoOoo0O , themeit = oo )
 Oo00oo0000OO ( 'Test Notifications' , 'testnotify' , icon = ooOoOoo0O , themeit = oo )
 if 72 - 72: oO00oOOoooO - oOoooo0O0Oo
 if 25 - 25: oOOoo00O00o % oOoooo0O0Oo * ii1Ii1I1Ii11i - oO0Oo0O0o * OO * iiIi111
 if 30 - 30: Iii1I1i % oOOoo00O00o / oOOOOOOo0O00o * IIOOOO0oo0 * i1III1I . oOOOOoo0OOO
 if 46 - 46: oOOoo00O00o - IIOOOO0oo0
 if 70 - 70: Iii1I1i + ii1Ii1I1Ii11i * O0ooO0o0O0O . oOOOOoo0OOO * Iii1I1i
def ii1i11ii ( name , type , theme = None ) :
 iIi11iIi = wiz . checkBuild ( name , 'url' )
 if iIi11iIi == False :
  wiz . LogNotify ( iiiii , "Unabled to find build" )
  return
 if type == 'gui' :
  if name == O0o0Oo :
   I111 = IiiIII111iI . yesno ( iiiii , '[COLOR %s]Would you like to apply the guifix for:' % i11I1IiII1i1i , '[COLOR %s]%s[/COLOR]?[/COLOR]' % ( Oo0O00O000 , name ) , nolabel = '[B]No, Cancel[/B]' , yeslabel = '[B]Apply Fix[/B]' )
  else :
   I111 = IiiIII111iI . yesno ( "%s - [COLOR red]WARNING!![/COLOR]" % iiiii , "[COLOR %s][COLOR %s]%s[/COLOR] community build is not currently installed." % ( i11I1IiII1i1i , Oo0O00O000 , name ) , "Would you like to apply the guiFix anyways?.[/COLOR]" , nolabel = '[B]No, Cancel[/B]' , yeslabel = '[B]Apply Fix[/B]' )
  if I111 :
   OOooo000OooO = wiz . checkBuild ( name , 'gui' )
   o0o0OoOo = name . replace ( '\\' , '' ) . replace ( '/' , '' ) . replace ( ':' , '' ) . replace ( '*' , '' ) . replace ( '?' , '' ) . replace ( '"' , '' ) . replace ( '<' , '' ) . replace ( '>' , '' ) . replace ( '|' , '' )
   if not wiz . workingURL ( OOooo000OooO ) == True : wiz . LogNotify ( iiiii , 'GuiFix: [COLOR red]Invalid Zip Url![/COLOR]' ) ; return
   if not os . path . exists ( oooOOOOO ) : os . makedirs ( oooOOOOO )
   iI1Ii11111iIi . create ( iiiii , '[COLOR %s][B]Downloading GuiFix:[/B][/COLOR] [COLOR %s]%s[/COLOR]' % ( i11I1IiII1i1i , Oo0O00O000 , name ) , '' , 'Please Wait' )
   I1I1 = os . path . join ( oooOOOOO , '%s_guisettings.zip' % o0o0OoOo )
   try : os . remove ( I1I1 )
   except : pass
   downloader . download ( OOooo000OooO , I1I1 , iI1Ii11111iIi )
   xbmc . sleep ( 500 )
   O0Oo0 = '[COLOR %s][B]Installing:[/B][/COLOR] [COLOR %s]%s[/COLOR]' % ( i11I1IiII1i1i , Oo0O00O000 , name )
   iI1Ii11111iIi . update ( 0 , O0Oo0 , '' , 'Please Wait' )
   extract . all ( I1I1 , oO , iI1Ii11111iIi , title = O0Oo0 )
   iI1Ii11111iIi . close ( )
   wiz . defaultSkin ( )
   wiz . lookandFeelData ( 'save' )
   IiiIII111iI . ok ( iiiii , "[COLOR %s]To save changes you now need to force close Kodi, Press OK to force close Kodi[/COLOR]" % i11I1IiII1i1i )
   wiz . killxbmc ( 'true' )
  else :
   wiz . LogNotify ( iiiii , 'GuiFix: [COLOR red]Cancelled![/COLOR]' )
 elif type == 'fresh' :
  IiI1 ( name )
 elif type == 'normal' :
  if i1Ii11II == 'normal' :
   if i1Oo00 == 'true' :
    traktit . autoUpdate ( 'all' )
    wiz . setS ( 'traktlastsave' , str ( O0i1II1Iiii1I11 ) )
   if i1i == 'true' :
    debridit . autoUpdate ( 'all' )
    wiz . setS ( 'debridlastsave' , str ( O0i1II1Iiii1I11 ) )
   if iiI111I1iIiI == 'true' :
    loginit . autoUpdate ( 'all' )
    wiz . setS ( 'loginlastsave' , str ( O0i1II1Iiii1I11 ) )
  iiIiII = int ( IIII ) ; IIiiiI1iI = int ( float ( wiz . checkBuild ( name , 'kodi' ) ) )
  if not iiIiII == IIiiiI1iI :
   if iiIiII == 16 and IIiiiI1iI <= 15 : iiI1II11II1i = False
   else : iiI1II11II1i = True
  else : iiI1II11II1i = False
  if iiI1II11II1i == True :
   O0O0 = IiiIII111iI . yesno ( "%s - [COLOR red]WARNING!![/COLOR]" % iiiii , '[COLOR %s]There is a chance that the skin will not appear correctly' % i11I1IiII1i1i , 'When installing a %s build on a Kodi %s install' % ( wiz . checkBuild ( name , 'kodi' ) , IIII ) , 'Would you still like to install: [COLOR %s]%s v%s[/COLOR]?[/COLOR]' % ( Oo0O00O000 , name , wiz . checkBuild ( name , 'version' ) ) , nolabel = '[B]No, Cancel[/B]' , yeslabel = '[B]Yes, Install[/B]' )
  else :
   O0O0 = IiiIII111iI . yesno ( iiiii , '[COLOR %s]Would you like to Download and Install:' % i11I1IiII1i1i , '[COLOR %s]%s v%s[/COLOR]?[/COLOR]' % ( Oo0O00O000 , name , wiz . checkBuild ( name , 'version' ) ) , nolabel = '[B]No, Cancel[/B]' , yeslabel = '[B]Yes, Install[/B]' )
  if O0O0 :
   wiz . clearS ( 'build' )
   OOooo000OooO = wiz . checkBuild ( name , 'url' )
   o0o0OoOo = name . replace ( '\\' , '' ) . replace ( '/' , '' ) . replace ( ':' , '' ) . replace ( '*' , '' ) . replace ( '?' , '' ) . replace ( '"' , '' ) . replace ( '<' , '' ) . replace ( '>' , '' ) . replace ( '|' , '' )
   if not wiz . workingURL ( OOooo000OooO ) == True : wiz . LogNotify ( iiiii , 'Build Install: [COLOR red]Invalid Zip Url![/COLOR]' ) ; return
   if not os . path . exists ( oooOOOOO ) : os . makedirs ( oooOOOOO )
   iI1Ii11111iIi . create ( iiiii , '[COLOR %s][B]Downloading:[/B][/COLOR] [COLOR %s]%s v%s[/COLOR]' % ( i11I1IiII1i1i , Oo0O00O000 , name , wiz . checkBuild ( name , 'version' ) ) , '' , 'Please Wait' )
   I1I1 = os . path . join ( oooOOOOO , '%s.zip' % o0o0OoOo )
   try : os . remove ( I1I1 )
   except : pass
   downloader . download ( OOooo000OooO , I1I1 , iI1Ii11111iIi )
   xbmc . sleep ( 500 )
   O0Oo0 = '[COLOR %s][B]Installing:[/B][/COLOR] [COLOR %s]%s v%s[/COLOR]' % ( i11I1IiII1i1i , Oo0O00O000 , name , wiz . checkBuild ( name , 'version' ) )
   iI1Ii11111iIi . update ( 0 , O0Oo0 , '' , 'Please Wait' )
   OOooO0OO0 , iI1iIiiiI1I1 , OOOOOo = extract . all ( I1I1 , i1i1II , iI1Ii11111iIi , title = O0Oo0 )
   if int ( float ( OOooO0OO0 ) ) > 0 :
    wiz . lookandFeelData ( 'save' )
    wiz . defaultSkin ( )
    wiz . setS ( 'buildname' , name )
    wiz . setS ( 'buildversion' , wiz . checkBuild ( name , 'version' ) )
    wiz . setS ( 'buildtheme' , '' )
    wiz . setS ( 'latestversion' , wiz . checkBuild ( name , 'version' ) )
    wiz . setS ( 'lastbuildcheck' , str ( OO0OO0O00oO0 ) )
    wiz . setS ( 'installed' , 'true' )
    wiz . setS ( 'extract' , str ( OOooO0OO0 ) )
    wiz . setS ( 'errors' , str ( iI1iIiiiI1I1 ) )
    wiz . log ( 'INSTALLED %s: [ERRORS:%s]' % ( OOooO0OO0 , iI1iIiiiI1I1 ) )
    if int ( float ( iI1iIiiiI1I1 ) ) > 0 :
     I111 = IiiIII111iI . yesno ( iiiii , '[COLOR %s][COLOR %s]%s v%s[/COLOR]' % ( i11I1IiII1i1i , Oo0O00O000 , name , wiz . checkBuild ( name , 'version' ) ) , 'Completed: [COLOR %s]%s%s[/COLOR] [Errors:[COLOR %s]%s[/COLOR]]' % ( Oo0O00O000 , OOooO0OO0 , '%' , Oo0O00O000 , iI1iIiiiI1I1 ) , 'Would you like to view the errors?[/COLOR]' , nolabel = '[B]No Thanks[/B]' , yeslabel = '[B]View Errors[/B]' )
     if I111 :
      if isinstance ( iI1iIiiiI1I1 , unicode ) :
       OOOOOo = OOOOOo . encode ( 'utf-8' )
      wiz . TextBoxes ( iiiii , OOOOOo )
    iI1Ii11111iIi . close ( )
    OooOo00o = wiz . checkBuild ( name , 'theme' )
    if not OooOo00o == 'http://' :
     O0oO0o0OOOOOO = wiz . workingURL ( OooOo00o )
     if O0oO0o0OOOOOO == True : ii1i11ii ( name , 'theme' )
     else : wiz . log ( "Theme File Not Working: %s" % O0oO0o0OOOOOO )
    IiiIII111iI . ok ( iiiii , "[COLOR %s]To save changes you now need to force close Kodi, Press OK to force close Kodi[/COLOR]" % i11I1IiII1i1i )
    wiz . killxbmc ( 'true' )
   else :
    if isinstance ( iI1iIiiiI1I1 , unicode ) :
     OOOOOo = OOOOOo . encode ( 'utf-8' )
    wiz . TextBoxes ( "%s: Error Installing Build" % iiiii , OOOOOo )
  else :
   wiz . LogNotify ( iiiii , 'Build Install: [COLOR red]Cancelled![/COLOR]' )
 elif type == 'theme' :
  if theme == None :
   OooOo00o = wiz . checkBuild ( name , 'theme' )
   IiI1i11IiIiii = [ ]
   if not OooOo00o == 'http://' and wiz . workingURL ( OooOo00o ) == True :
    O0oOOo0Oo = wiz . openURL ( OooOo00o ) . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
    o000O000 = re . compile ( 'name="(.+?)"' ) . findall ( O0oOOo0Oo )
    if len ( o000O000 ) > 0 :
     if IiiIII111iI . yesno ( iiiii , "[COLOR %s]The Build [COLOR %s]%s[/COLOR] comes with [COLOR %s]%s[/COLOR] different themes" % ( i11I1IiII1i1i , Oo0O00O000 , name , Oo0O00O000 , len ( o000O000 ) ) , "Would you like to install one now?[/COLOR]" , yeslabel = "[B]Install Theme[/B]" , nolabel = "[B]Cancel Themes[/B]" ) :
      for o0O0O0 in o000O000 :
       IiI1i11IiIiii . append ( o0O0O0 )
      wiz . log ( "Theme List: %s " % str ( IiI1i11IiIiii ) )
      I11iiI1I1 = IiiIII111iI . select ( iiiii , IiI1i11IiIiii )
      wiz . log ( "Theme install selected: %s" % I11iiI1I1 )
      if not I11iiI1I1 == - 1 : theme = IiI1i11IiIiii [ I11iiI1I1 ] ; o0i1Ii11II = True
      else : wiz . LogNotify ( iiiii , 'Theme Install: [COLOR red]Cancelled![/COLOR]' ) ; return
     else : wiz . LogNotify ( iiiii , 'Theme Install: [COLOR red]Cancelled![/COLOR]' ) ; return
   else : wiz . LogNotify ( iiiii , 'Theme Install: [COLOR red]None Found![/COLOR]' )
  else : o0i1Ii11II = IiiIII111iI . yesno ( iiiii , '[COLOR %s]Would you like to install the theme:' % i11I1IiII1i1i , '[COLOR %s]%s[/COLOR]' % ( Oo0O00O000 , theme ) , 'for [COLOR %s]%s v%s[/COLOR]?[/COLOR]' % ( Oo0O00O000 , name , wiz . checkBuild ( name , 'version' ) ) , yeslabel = "[B]Install Theme[/B]" , nolabel = "[B]Cancel Themes[/B]" )
  if o0i1Ii11II :
   i1iiiiI11ii = wiz . checkTheme ( name , theme , 'url' )
   o0o0OoOo = name . replace ( '\\' , '' ) . replace ( '/' , '' ) . replace ( ':' , '' ) . replace ( '*' , '' ) . replace ( '?' , '' ) . replace ( '"' , '' ) . replace ( '<' , '' ) . replace ( '>' , '' ) . replace ( '|' , '' )
   if not wiz . workingURL ( i1iiiiI11ii ) == True : wiz . LogNotify ( iiiii , 'Theme Install: [COLOR red]Invalid Zip Url![/COLOR]' ) ; return False
   if not os . path . exists ( oooOOOOO ) : os . makedirs ( oooOOOOO )
   iI1Ii11111iIi . create ( iiiii , '[COLOR %s][B]Downloading:[/B][/COLOR] [COLOR %s]%s[/COLOR]' % ( i11I1IiII1i1i , Oo0O00O000 , name ) , '' , 'Please Wait' )
   I1I1 = os . path . join ( oooOOOOO , '%s.zip' % o0o0OoOo )
   try : os . remove ( I1I1 )
   except : pass
   downloader . download ( i1iiiiI11ii , I1I1 , iI1Ii11111iIi )
   xbmc . sleep ( 500 )
   iI1Ii11111iIi . update ( 0 , "" , "Installing %s " % name )
   oooooOOo0o = False
   if i1Ii11II not in [ "fresh" , "normal" ] :
    oooooOOo0o = oOO0 ( I1I1 ) if not wiz . currSkin ( ) in [ 'skin.confluence' , 'skin.estuary' ] else False
    if oooooOOo0o == True :
     wiz . lookandFeelData ( 'save' )
     OoO000Oo0oO = 'skin.confluence' if IIII < 17 else 'skin.estuary'
     iiiIiiiI1 = xbmc . getSkinDir ( )
     if IiiIII111iI . yesno ( iiiii , "[COLOR %s]Installing the theme [COLOR %s]%s[/COLOR] requires the skin to be swaped back to [COLOR %s]%s[/COLOR]" % ( i11I1IiII1i1i , Oo0O00O000 , theme , Oo0O00O000 , OoO000Oo0oO [ 5 : ] ) , "Would you like to switch the skin?[/COLOR]" , yeslabel = "[B]Switch Skin[/B]" , nolabel = "[B]Don't Switch[/B]" ) :
      skinSwitch . swapSkins ( OoO000Oo0oO )
      O00oOo0O0o00O = 0
      xbmc . sleep ( 1000 )
      while not xbmc . getCondVisibility ( "Window.isVisible(yesnodialog)" ) and O00oOo0O0o00O < 150 :
       O00oOo0O0o00O += 1
       xbmc . sleep ( 200 )
       if 50 - 50: oo0 * oOOoo00O00o + oOOOOOOo0O00o - i11iIiiIii + ii1Ii1I1Ii11i * oOOOOOOo0O00o
      if xbmc . getCondVisibility ( "Window.isVisible(yesnodialog)" ) :
       wiz . ebi ( 'SendClick(11)' )
      else : wiz . LogNotify ( iiiii , 'Theme Install: [COLOR red]Skin Swap Timed Out![/COLOR]' ) ; return
      xbmc . sleep ( 500 )
     else : wiz . log ( "Theme Installer: %s skin swap ignored." % theme )
   O0Oo0 = '[COLOR %s][B]Installing Theme:[/B][/COLOR] [COLOR %s]%s[/COLOR]' % ( i11I1IiII1i1i , Oo0O00O000 , name )
   iI1Ii11111iIi . update ( 0 , O0Oo0 , '' , 'Please Wait' )
   OOooO0OO0 , iI1iIiiiI1I1 , OOOOOo = extract . all ( I1I1 , i1i1II , iI1Ii11111iIi , title = O0Oo0 )
   wiz . setS ( 'buildtheme' , theme )
   wiz . log ( 'INSTALLED %s: [ERRORS:%s]' % ( OOooO0OO0 , iI1iIiiiI1I1 ) )
   iI1Ii11111iIi . close ( )
   if i1Ii11II not in [ "fresh" , "normal" ] :
    if oooooOOo0o == True :
     skinSwitch . swapSkins ( iiiIiiiI1 )
     O00oOo0O0o00O = 0
     xbmc . sleep ( 1000 )
     while not xbmc . getCondVisibility ( "Window.isVisible(yesnodialog)" ) and O00oOo0O0o00O < 150 :
      O00oOo0O0o00O += 1
      xbmc . sleep ( 200 )
      if 20 - 20: Ii1I11I / Ii1iI1I1 % oOOoo00O00o
     if xbmc . getCondVisibility ( "Window.isVisible(yesnodialog)" ) :
      wiz . ebi ( 'SendClick(11)' )
     else : wiz . LogNotify ( iiiii , 'Theme Install: [COLOR red]Skin Swap Timed Out![/COLOR]' ) ; return
     wiz . lookandFeelData ( 'restore' )
    else :
     wiz . ebi ( "ReloadSkin()" )
     xbmc . sleep ( 1000 )
     wiz . ebi ( "Container.Refresh" )
  else :
   wiz . LogNotify ( iiiii , 'Theme Install: [COLOR red]Cancelled![/COLOR]' )
   if 69 - 69: Ii1I11I - oO0Oo0O0o % oO00oOOoooO . oOoOoo - oOoOoo
def oOO0 ( path ) :
 o0oO00o = zipfile . ZipFile ( path )
 for OOO0OoO0oo0OO in o0oO00o . infolist ( ) :
  if '/settings.xml' in OOO0OoO0oo0OO . filename :
   return True
 return False
 if 31 - 31: Iii1I1i * iiIi111 . i1III1I
def i1Ii11ii1I ( path ) :
 o0oO00o = zipfile . ZipFile ( path )
 for OOO0OoO0oo0OO in o0oO00o . infolist ( ) :
  if '/guisettings.xml' in OOO0OoO0oo0OO . filename :
   return True
 return False
 if 66 - 66: ii1Ii1I1Ii11i / oOoooo0O0Oo % Ii1I11I / oO00oOOoooO + oOoooo0O0Oo
 if 6 - 6: OO % Ii1I11I
 if 41 - 41: o0o0OoOo0O0OO - OO . OO + oOOOOoo0OOO
 if 59 - 59: O0ooO0o0O0O % i1III1I . i11iIiiIii
def I1iii ( apk , url , Brackets ) :
 if wiz . platform ( ) == 'android' :
  if apk in [ 'kodi' , 'spmc' ] :
   I111 = IiiIII111iI . yesno ( iiiii , "Would you like to download and install:" , "%s (v%s)" % ( apk . upper ( ) , wiz . latestApk ( apk , 'version' ) ) )
   if not I111 : wiz . LogNotify ( iiiii , '[COLOR red]ERROR:[/COLOR] Install Cancelled' ) ; return
   OOo = "%s v%s" % ( apk . upper ( ) , wiz . latestApk ( apk , 'version' ) )
  else :
   I111 = IiiIII111iI . yesno ( iiiii , "Would you like to download and install:" , "%s" % apk )
   if not I111 : wiz . LogNotify ( iiiii , '[COLOR red]ERROR:[/COLOR] Install Cancelled' ) ; return
   OOo = apk
  if I111 :
   if not os . path . exists ( oooOOOOO ) : os . makedirs ( oooOOOOO )
   if not wiz . workingURL ( url ) == True : wiz . LogNotify ( iiiii , 'APK Installer: [COLOR red]Invalid Apk Url![/COLOR]' ) ; return
   iI1Ii11111iIi . create ( iiiii , 'Downloading %s' % OOo , '' , 'Please Wait' )
   I1I1 = os . path . join ( oooOOOOO , "%s.apk" % apk )
   try : os . remove ( I1I1 )
   except : pass
   downloader . download ( url , I1I1 , iI1Ii11111iIi )
   xbmc . sleep ( 500 )
   iI1Ii11111iIi . close ( )
   if "Brackets" in Brackets :
    O0OOOO0000O = zipfile . ZipFile ( I1I1 )
    for file in O0OOOO0000O . namelist ( ) :
     if file . endswith ( '.apk' ) :
      with open ( os . path . join ( oooOOOOO , os . path . basename ( file ) ) , 'wb' ) as iIiIIiI1i1Ii :
       iiiI11 = file . split ( '/' ) [ 1 ]
       iIiIIiI1i1Ii . write ( O0OOOO0000O . read ( file ) )
       xbmc . sleep ( 500 )
       iIiIIiI1i1Ii . close ( )
       try :
        os . remove ( I1I1 )
       except :
        pass
       I1I1 = os . path . join ( oooOOOOO , iiiI11 )
   IiiIII111iI . ok ( iiiii , "Launching the APK to be installed" , "Follow the install process to complete." )
   xbmc . executebuiltin ( 'StartAndroidActivity("","android.intent.action.VIEW","application/vnd.android.package-archive","file:' + I1I1 + '")' )
  else : wiz . LogNotify ( iiiii , '[COLOR red]ERROR:[/COLOR] Install Cancelled' )
 else : wiz . LogNotify ( iiiii , '[COLOR red]ERROR:[/COLOR] None Android Device' )
 if 89 - 89: iiIi111
 if 87 - 87: oO00oOOoooO % ii1Ii1I1Ii11i
 if 62 - 62: I111I1Iiii1i + oo0 / oO00oOOoooO * i11iIiiIii
 if 37 - 37: oO00oOOoooO
def iIIiI1111 ( name , url , ) :
 if "NULL" in url :
  IiiIII111iI . ok ( iiiii , "[COLOR ghostwhite]Not a valid selection, please try again.[/COLOR]" )
  sys . exit ( 1 )
  if 91 - 91: oOoooo0O0Oo / Ii1iI1I1 . o0o0OoOo0O0OO - O0ooO0o0O0O - i1III1I
 I1IiiI = xbmcgui . DialogProgress ( )
 I1IiiI . create ( iiiii , "" , "" , 'ROM: ' + name )
 o0o0OoOo = name . replace ( '\\' , '' ) . replace ( '/' , '' ) . replace ( ':' , '' ) . replace ( '*' , '' ) . replace ( '?' , '' ) . replace ( '"' , '' ) . replace ( '<' , '' ) . replace ( '>' , '' ) . replace ( '|' , '' )
 I1I1 = os . path . join ( oooOOOOO , '%s.zip' % o0o0OoOo )
 downloader . download ( url , I1I1 , I1IiiI )
 I1IiiI . update ( 0 )
 extract . all ( I1I1 , Oo0o0000o0o0 , I1IiiI )
 IiiIII111iI . ok ( iiiii , "[COLOR yellow]Download complete, ROM Location: [/COLOR][COLOR white]" + Oo0o0000o0o0 + "[/COLOR]" )
 if 31 - 31: o0o0OoOo0O0OO - I111I1Iiii1i / oOoOoo . oO0Oo0O0o / i1III1I
 if 66 - 66: I111I1Iiii1i
 if 72 - 72: Ii1I11I
 if 91 - 91: OO / o0o0OoOo0O0OO + O0ooO0o0O0O . Iii1I1i - IIOOOO0oo0
 if 70 - 70: i1III1I * iiIi111 - Iii1I1i + ii1Ii1I1Ii11i % oOOOOOOo0O00o - o0o0OoOo0O0OO
def oooOoO00OooO0 ( part , whole ) :
 return 100 * float ( part ) / float ( whole )
 if 98 - 98: oOoOoo + i1III1I
def I1i ( type , add , name ) :
 if type == 'saveaddon' :
  OOOOIIIIiI11Ii1i = [ ]
  O0O0O0o = urllib . quote_plus ( add . lower ( ) . replace ( ' ' , '' ) )
  o00o0oOO0O = add . replace ( 'Debrid' , 'Real Debrid' )
  OO000OOo = urllib . quote_plus ( name . lower ( ) . replace ( ' ' , '' ) )
  name = name . replace ( 'url' , 'URL Resolver' )
  OOOOIIIIiI11Ii1i . append ( ( I1111i % name . title ( ) , ' ' ) )
  OOOOIIIIiI11Ii1i . append ( ( iIIii % 'Save %s Data' % o00o0oOO0O , 'RunPlugin(plugin://%s/?mode=save%s&name=%s)' % ( OO0o , O0O0O0o , OO000OOo ) ) )
  OOOOIIIIiI11Ii1i . append ( ( iIIii % 'Restore %s Data' % o00o0oOO0O , 'RunPlugin(plugin://%s/?mode=restore%s&name=%s)' % ( OO0o , O0O0O0o , OO000OOo ) ) )
  OOOOIIIIiI11Ii1i . append ( ( iIIii % 'Clear %s Data' % o00o0oOO0O , 'RunPlugin(plugin://%s/?mode=clear%s&name=%s)' % ( OO0o , O0O0O0o , OO000OOo ) ) )
 elif type == 'save' :
  OOOOIIIIiI11Ii1i = [ ]
  O0O0O0o = urllib . quote_plus ( add . lower ( ) . replace ( ' ' , '' ) )
  o00o0oOO0O = add . replace ( 'Debrid' , 'Real Debrid' )
  OO000OOo = urllib . quote_plus ( name . lower ( ) . replace ( ' ' , '' ) )
  name = name . replace ( 'url' , 'URL Resolver' )
  OOOOIIIIiI11Ii1i . append ( ( I1111i % name . title ( ) , ' ' ) )
  OOOOIIIIiI11Ii1i . append ( ( iIIii % 'Register %s' % o00o0oOO0O , 'RunPlugin(plugin://%s/?mode=auth%s&name=%s)' % ( OO0o , O0O0O0o , OO000OOo ) ) )
  OOOOIIIIiI11Ii1i . append ( ( iIIii % 'Save %s Data' % o00o0oOO0O , 'RunPlugin(plugin://%s/?mode=save%s&name=%s)' % ( OO0o , O0O0O0o , OO000OOo ) ) )
  OOOOIIIIiI11Ii1i . append ( ( iIIii % 'Restore %s Data' % o00o0oOO0O , 'RunPlugin(plugin://%s/?mode=restore%s&name=%s)' % ( OO0o , O0O0O0o , OO000OOo ) ) )
  OOOOIIIIiI11Ii1i . append ( ( iIIii % 'Import %s Data' % o00o0oOO0O , 'RunPlugin(plugin://%s/?mode=import%s&name=%s)' % ( OO0o , O0O0O0o , OO000OOo ) ) )
  OOOOIIIIiI11Ii1i . append ( ( iIIii % 'Clear Addon %s Data' % o00o0oOO0O , 'RunPlugin(plugin://%s/?mode=addon%s&name=%s)' % ( OO0o , O0O0O0o , OO000OOo ) ) )
 elif type == 'install' :
  OOOOIIIIiI11Ii1i = [ ]
  OO000OOo = urllib . quote_plus ( name )
  OOOOIIIIiI11Ii1i . append ( ( I1111i % name , 'RunAddon(%s, ?mode=viewbuild&name=%s)' % ( OO0o , OO000OOo ) ) )
  OOOOIIIIiI11Ii1i . append ( ( iIIii % 'Fresh Install' , 'RunPlugin(plugin://%s/?mode=install&name=%s&url=fresh)' % ( OO0o , OO000OOo ) ) )
  OOOOIIIIiI11Ii1i . append ( ( iIIii % 'Normal Install' , 'RunPlugin(plugin://%s/?mode=install&name=%s&url=normal)' % ( OO0o , OO000OOo ) ) )
  OOOOIIIIiI11Ii1i . append ( ( iIIii % 'Apply guiFix' , 'RunPlugin(plugin://%s/?mode=install&name=%s&url=gui)' % ( OO0o , OO000OOo ) ) )
  OOOOIIIIiI11Ii1i . append ( ( iIIii % 'Build Information' , 'RunPlugin(plugin://%s/?mode=buildinfo&name=%s)' % ( OO0o , OO000OOo ) ) )
 OOOOIIIIiI11Ii1i . append ( ( I1111i % '%s Settings' % iiiii , 'RunPlugin(plugin://%s/?mode=settings)' % OO0o ) )
 return OOOOIIIIiI11Ii1i
 if 70 - 70: ii1Ii1I1Ii11i * O0ooO0o0O0O
def O00Ooo0ooo0 ( state ) :
 oO00o0O00o = [ 'includevideo' , 'includeall' , 'includebob' , 'includephoenix' , 'includespecto' , 'includegenesis' , 'includeexodus' , 'includeonechan' , 'includesalts' , 'includesaltslite' ]
 o0OOOooO00OO00O = [ 'Include Video Addons' , 'Include All Addons' , 'Include Bob' , 'Include Phoenix' , 'Include Specto' , 'Include Genesis' , 'Include Exodus' , 'Include One Channel' , 'Include Salts' , 'Include Salts Lite HD' ]
 if state in [ 'true' , 'false' ] :
  for OOO0OoO0oo0OO in oO00o0O00o :
   wiz . setS ( OOO0OoO0oo0OO , state )
 else :
  if not state in [ 'includevideo' , 'includeall' ] and wiz . getS ( 'includeall' ) == 'true' :
   try :
    OOO0OoO0oo0OO = o0OOOooO00OO00O [ oO00o0O00o . index ( state ) ]
    IiiIII111iI . ok ( iiiii , "[COLOR %s]You will need to turn off [COLOR %s]Include All Addons[/COLOR] to disable[/COLOR] [COLOR %s]%s[/COLOR]" % ( i11I1IiII1i1i , Oo0O00O000 , Oo0O00O000 , OOO0OoO0oo0OO ) )
   except :
    wiz . LogNotify ( "Toggle Cache" , "Invalid id: %s" % state )
  else :
   OoOOooO0O = 'true' if wiz . getS ( state ) == 'false' else 'false'
   wiz . setS ( state , OoOOooO0O )
   if 3 - 3: OO - i1III1I % oOOoo00O00o / iiIi111
def Ii1 ( url ) :
 if 'watch?v=' in url :
  iI1i1IiIIIIi , ooOO0OOO00o = url . split ( '?' )
  OoOoO0ooooO0 = ooOO0OOO00o . split ( '&' )
  for OOO0OoO0oo0OO in OoOoO0ooooO0 :
   if OOO0OoO0oo0OO . startswith ( 'v=' ) :
    url = OOO0OoO0oo0OO [ 2 : ]
    break
   else : continue
 elif 'embed' in url or 'youtu.be' in url :
  iI1i1IiIIIIi = url . split ( '/' )
  if len ( iI1i1IiIIIIi [ - 1 ] ) > 5 :
   url = iI1i1IiIIIIi [ - 1 ]
  elif len ( iI1i1IiIIIIi [ - 2 ] ) > 5 :
   url = iI1i1IiIIIIi [ - 2 ]
 wiz . log ( "YouTube URL: %s" % url )
 yt . PlayVideo ( url )
 if 4 - 4: ii1Ii1I1Ii11i - I111I1Iiii1i - i11iIiiIii * Ii1I11I / i1III1I - oOoOoo
def II1IIii1ii ( ) :
 IIiIiIiiI1Iii = wiz . Grab_Log ( True )
 Ii111iII = wiz . Grab_Log ( True , True )
 Oo0OoOo = 0 ; iiIIIi1i = IIiIiIiiI1Iii
 if not Ii111iII == False and not IIiIiIiiI1Iii == False :
  Oo0OoOo = IiiIII111iI . select ( iiiii , [ "View %s" % IIiIiIiiI1Iii . replace ( oOo0oooo00o , "" ) , "View %s" % Ii111iII . replace ( oOo0oooo00o , "" ) ] )
  if Oo0OoOo == - 1 : wiz . LogNotify ( 'View Log' , 'View Log Cancelled!' ) ; return
 elif IIiIiIiiI1Iii == False and Ii111iII == False :
  wiz . LogNotify ( 'View Log' , 'No Log File Found!' )
  return
 elif not IIiIiIiiI1Iii == False : Oo0OoOo = 0
 elif not Ii111iII == False : Oo0OoOo = 1
 if 1 - 1: ii1Ii1I1Ii11i * Ii1I11I . oOoooo0O0Oo
 iiIIIi1i = IIiIiIiiI1Iii if Oo0OoOo == 0 else Ii111iII
 oOO00OO0o0O = wiz . Grab_Log ( False ) if Oo0OoOo == 0 else wiz . Grab_Log ( False , True )
 if 35 - 35: Ii1iI1I1 * oO00oOOoooO - O0ooO0o0O0O + Ii1iI1I1 . oOoooo0O0Oo
 wiz . TextBoxes ( "%s - %s" % ( iiiii , iiIIIi1i ) , oOO00OO0o0O )
 if 13 - 13: IIOOOO0oo0 % oo0 % Iii1I1i
def Oo0OOo ( log = None , count = None , all = None ) :
 if log == None :
  IIiIiIiiI1Iii = wiz . Grab_Log ( True )
  Ii111iII = wiz . Grab_Log ( True , True )
  if not Ii111iII == False and not IIiIiIiiI1Iii == False :
   Oo0OoOo = IiiIII111iI . select ( iiiii , [ "View %s: %s error(s)" % ( IIiIiIiiI1Iii . replace ( oOo0oooo00o , "" ) , Oo0OOo ( IIiIiIiiI1Iii , True ) ) , "View %s: %s error(s)" % ( Ii111iII . replace ( oOo0oooo00o , "" ) , Oo0OOo ( Ii111iII , True ) ) ] )
   if Oo0OoOo == - 1 : wiz . LogNotify ( 'View Log' , 'View Log Cancelled!' ) ; return
  elif IIiIiIiiI1Iii == False and Ii111iII == False :
   wiz . LogNotify ( 'View Log' , 'No Log File Found!' )
   return
  elif not IIiIiIiiI1Iii == False : Oo0OoOo = 0
  elif not Ii111iII == False : Oo0OoOo = 1
  log = IIiIiIiiI1Iii if Oo0OoOo == 0 else Ii111iII
 if log == False :
  if count == None :
   wiz . LogNotify ( iiiii , "Log File not Found" )
   return False
  else :
   return 0
 else :
  if os . path . exists ( log ) :
   iIiIIiI1i1Ii = open ( log , mode = 'r' ) ; iI1i1IiIIIIi = iIiIIiI1i1Ii . read ( ) . replace ( '\n' , '' ) . replace ( '\r' , '' ) ; iIiIIiI1i1Ii . close ( )
   o000O000 = re . compile ( "-->Python callback/script returned the following error<--(.+?)-->End of Python script error report<--" ) . findall ( iI1i1IiIIIIi )
   if not count == None :
    if all == None :
     O00oOo0O0o00O = 0
     for OOO0OoO0oo0OO in o000O000 :
      if OO0o in OOO0OoO0oo0OO : O00oOo0O0o00O += 1
     return O00oOo0O0o00O
    else : return len ( o000O000 )
   if len ( o000O000 ) > 0 :
    O00oOo0O0o00O = 0 ; oOO00OO0o0O = ""
    for OOO0OoO0oo0OO in o000O000 :
     if all == None and not OO0o in OOO0OoO0oo0OO : continue
     else :
      O00oOo0O0o00O += 1
      oOO00OO0o0O += "[COLOR red]Error Number %s[/COLOR]\n(PythonToCppException) : -->Python callback/script returned the following error<--%s-->End of Python script error report<--\n\n" % ( O00oOo0O0o00O , OOO0OoO0oo0OO . replace ( '                                          ' , '\n' ) . replace ( '\\\\' , '\\' ) . replace ( i1i1II , '' ) )
    if O00oOo0O0o00O > 0 :
     if IIII >= 16 : IiiIII111iI . textviewer ( iiiii , oOO00OO0o0O )
     else : wiz . TextBoxes ( iiiii , oOO00OO0o0O )
    else : wiz . LogNotify ( iiiii , "No Errors Found in Log" )
   else : wiz . LogNotify ( iiiii , "No Errors Found in Log" )
  else : wiz . LogNotify ( iiiii , "Log File not Found" )
  if 25 - 25: oOoooo0O0Oo % i1III1I * OO - I111I1Iiii1i
def Oo00Oooo00o ( ) :
 if os . path . exists ( II11iiii1Ii ) :
  iIiIIiI1i1Ii = open ( II11iiii1Ii , mode = 'r' ) ; oOO00OO0o0O = iIiIIiI1i1Ii . read ( ) ; iIiIIiI1i1Ii . close ( )
  wiz . TextBoxes ( "%s - Wizard.log" % iiiii , oOO00OO0o0O )
 else :
  wiz . LogNotify ( 'View Log' , 'Wizard.log not found!' )
  if 6 - 6: oOOoo00O00o - oo0 * Ii1iI1I1 + oOOoo00O00o % Ii1iI1I1
def OOO00000o0 ( addon ) :
 if IiiIII111iI . yesno ( iiiii , '[COLOR %s]Are you sure you want to delete the addon:' % Oo0O00O000 , '[COLOR %s]%s[/COLOR]?[/COLOR]' % ( Oo0O00O000 , addon ) , yeslabel = '[B]Remove Addon[/B]' , nolabel = '[B]Don\'t Remove[/B]' ) :
  wiz . cleanHouse ( os . path . join ( II1 , addon ) )
  i1iIiIIi1II1ii ( addon )
  wiz . LogNotify ( 'Remove Addon' , 'Complete!' )
  IiiIII111iI . ok ( iiiii , '[COLOR %s]The addon has been removed but will remain in the addons list until the next time you reload Kodi.[/COLOR]' )
 else : wiz . LogNotify ( 'Remove Addon' , 'Cancelled!' )
 wiz . refresh ( )
 if 96 - 96: Ii1iI1I1 * iiIi111 - oOoOoo * Ii1iI1I1 * oO0Oo0O0o
def i1iIiIIi1II1ii ( addon ) :
 if addon == 'all' :
  if IiiIII111iI . yesno ( iiiii , '[COLOR %s]Would you like to remove [COLOR %s]ALL[/COLOR] addon data stored in you Userdata folder?[/COLOR]' % ( i11I1IiII1i1i , Oo0O00O000 ) , yeslabel = '[B]Remove Data[/B]' , nolabel = '[B]Don\'t Remove[/B]' ) :
   wiz . cleanHouse ( i1iiIII111ii )
  else : wiz . LogNotify ( 'Remove Addon Data' , 'Cancelled!' )
 elif addon == 'uninstalled' :
  if IiiIII111iI . yesno ( iiiii , '[COLOR %s]Would you like to remove [COLOR %s]ALL[/COLOR] addon data stored in you Userdata folder for uninstalled addons?[/COLOR]' % ( i11I1IiII1i1i , Oo0O00O000 ) , yeslabel = '[B]Remove Data[/B]' , nolabel = '[B]Don\'t Remove[/B]' ) :
   I1IIIi1i = 0
   for Iii11111iiI in glob . glob ( os . path . join ( i1iiIII111ii , '*' ) ) :
    o0OOOOoO = Iii11111iiI . replace ( i1iiIII111ii , '' ) . replace ( '\\' , '' ) . replace ( '/' , '' )
    if o0OOOOoO in o0OIiII : pass
    elif os . path . exists ( os . path . join ( II1 , o0OOOOoO ) ) : pass
    else : wiz . cleanHouse ( Iii11111iiI ) ; I1IIIi1i += 1 ; wiz . log ( Iii11111iiI ) ; shutil . rmtree ( Iii11111iiI )
   wiz . LogNotify ( 'Clean up Uninstalled' , '[COLOR yellow]%s[/COLOR] Folders(s) Removed' % I1IIIi1i )
  else : wiz . LogNotify ( 'Remove Addon Data' , 'Cancelled!' )
 elif addon == 'empty' :
  if IiiIII111iI . yesno ( iiiii , '[COLOR %s]Would you like to remove [COLOR %s]ALL[/COLOR] empty addon data folders in you Userdata folder?[/COLOR]' % ( i11I1IiII1i1i , Oo0O00O000 ) , yeslabel = '[B]Remove Data[/B]' , nolabel = '[B]Don\'t Remove[/B]' ) :
   I1IIIi1i = wiz . emptyfolder ( i1iiIII111ii )
   wiz . LogNotify ( 'Remove Empty Folders' , '[COLOR yellow]%s[/COLOR] Folders(s) Removed' % I1IIIi1i )
  else : wiz . LogNotify ( 'Remove Empty Folders' , 'Cancelled!' )
 else :
  OooIii1I1iI = os . path . join ( oO , 'addon_data' , addon )
  if addon in o0OIiII :
   wiz . LogNotify ( "Protected Plugin" , "Not allowed to remove Addon_Data" )
  elif os . path . exists ( OooIii1I1iI ) :
   if IiiIII111iI . yesno ( iiiii , '[COLOR %s]Would you also like to remove the addon data for:[/COLOR]' % i11I1IiII1i1i , '[COLOR %s]%s[/COLOR]' % ( Oo0O00O000 , addon ) , yeslabel = '[B]Remove Data[/B]' , nolabel = '[B]Don\'t Remove[/B]' ) :
    wiz . cleanHouse ( OooIii1I1iI )
    try :
     shutil . rmtree ( OooIii1I1iI )
    except :
     wiz . log ( "Error deleting: %s" % OooIii1I1iI )
   else :
    wiz . log ( 'Addon data for %s was not removed' % addon )
 wiz . refresh ( )
 if 62 - 62: iiIi111 + ii1Ii1I1Ii11i / i11iIiiIii
def ooOoOo ( type ) :
 if type == 'build' :
  O00oOo0O0o00O = IiI1 ( 'restore' )
  if O00oOo0O0o00O == False : wiz . LogNotify ( iiiii , "Local Restore Cancelled" ) ; return
 wiz . restoreLocal ( type )
 if 13 - 13: oOoOoo . ii1Ii1I1Ii11i / OO
def iiI1iIII1ii ( type ) :
 if type == 'build' :
  O00oOo0O0o00O = IiI1 ( 'restore' )
  if O00oOo0O0o00O == False : wiz . LogNotify ( iiiii , "External Restore Cancelled" ) ; return
 wiz . restoreExternal ( type )
 if 5 - 5: Ii1I11I % oOoooo0O0Oo . oOOoo00O00o
def oO00o00 ( name ) :
 if wiz . workingURL ( I1iI ) == True :
  if wiz . checkBuild ( name , 'url' ) :
   name , IiIi1ii111i1 , i1Ii11II , IioO0oOOO0Ooo , i1i1I , IiIIi1 , iII11I1Ii1 , o0o0 , oOo0oO , IIi1IIIIi = wiz . checkBuild ( name , 'all' )
   oOo0oO = 'Yes' if oOo0oO . lower ( ) == 'yes' else 'No'
   oOO00OO0o0O = "[COLOR %s]Build Name:[/COLOR] [COLOR %s]%s[/COLOR][CR]" % ( i11I1IiII1i1i , Oo0O00O000 , name )
   oOO00OO0o0O += "[COLOR %s]Build Version:[/COLOR] [COLOR %s]%s[/COLOR][CR]" % ( i11I1IiII1i1i , Oo0O00O000 , IiIi1ii111i1 )
   if not IiIIi1 == "http://" :
    OOooooO0o0O0 = wiz . themeCount ( name , False )
    oOO00OO0o0O += "[COLOR %s]Build Theme(s):[/COLOR] [COLOR %s]%s[/COLOR][CR]" % ( i11I1IiII1i1i , Oo0O00O000 , ', ' . join ( OOooooO0o0O0 ) )
   oOO00OO0o0O += "[COLOR %s]Kodi Version:[/COLOR] [COLOR %s]%s[/COLOR][CR]" % ( i11I1IiII1i1i , Oo0O00O000 , i1i1I )
   oOO00OO0o0O += "[COLOR %s]Adult Content:[/COLOR] [COLOR %s]%s[/COLOR][CR]" % ( i11I1IiII1i1i , Oo0O00O000 , oOo0oO )
   oOO00OO0o0O += "[COLOR %s]Description:[/COLOR] [COLOR %s]%s[/COLOR][CR]" % ( i11I1IiII1i1i , Oo0O00O000 , IIi1IIIIi )
   wiz . TextBoxes ( iiiii , oOO00OO0o0O )
  else : wiz . log ( "Invalid Build Name!" )
 else : wiz . log ( "Build text file not working: %s" % i1I1iIo0 )
 if 74 - 74: oOOoo00O00o / oO0Oo0O0o % oOoooo0O0Oo
def O0o00OOo00O0O ( url ) :
 IiI1ii1Ii = urllib2 . Request ( url )
 IiI1ii1Ii . add_header ( 'User-Agent' , 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3' )
 oooOOOoOOOo0O = urllib2 . urlopen ( IiI1ii1Ii )
 O0oOOo0Oo = oooOOOoOOOo0O . read ( )
 oooOOOoOOOo0O . close ( )
 return O0oOOo0Oo
 if 52 - 52: o0o0OoOo0O0OO % oo0
def IIIIIiI ( url ) :
 if url == 'http://' : return False
 try :
  IiI1ii1Ii = urllib2 . Request ( url )
  IiI1ii1Ii . add_header ( 'User-Agent' , o0O )
  oooOOOoOOOo0O = urllib2 . urlopen ( IiI1ii1Ii )
  oooOOOoOOOo0O . close ( )
 except Exception , I111oOOooo00OOooO :
  return I111oOOooo00OOooO
 return True
 if 31 - 31: oOOOOoo0OOO / Ii1iI1I1 + oOOOOoo0OOO - OO
 if 29 - 29: oOOOOoo0OOO + i11iIiiIii . IIOOOO0oo0
 if 75 - 75: Ii1I11I + O0ooO0o0O0O
 if 19 - 19: oOOOOoo0OOO + i11iIiiIii . o0o0OoOo0O0OO - Iii1I1i / i1III1I + Ii1iI1I1
 if 38 - 38: ii1Ii1I1Ii11i / O0ooO0o0O0O * O0ooO0o0O0O % oOOOOOOo0O00o
 if 92 - 92: Iii1I1i / IIOOOO0oo0 * oOOOOoo0OOO - Iii1I1i
def IiI1 ( install = None , over = False ) :
 if i1Oo00 == 'true' :
  traktit . autoUpdate ( 'all' )
  wiz . setS ( 'traktlastsave' , str ( O0i1II1Iiii1I11 ) )
 if i1i == 'true' :
  debridit . autoUpdate ( 'all' )
  wiz . setS ( 'debridlastsave' , str ( O0i1II1Iiii1I11 ) )
 if iiI111I1iIiI == 'true' :
  loginit . autoUpdate ( 'all' )
  wiz . setS ( 'loginlastsave' , str ( O0i1II1Iiii1I11 ) )
 if over == True : O0O0 = 1
 elif install == 'restore' : O0O0 = IiiIII111iI . yesno ( iiiii , "[COLOR %s]Do you wish to restore your" % i11I1IiII1i1i , "Kodi configuration to default settings" , "Before installing the local backup?[/COLOR]" , nolabel = '[B]No, Cancel[/B]' , yeslabel = '[B]Continue[/B]' )
 elif install : O0O0 = IiiIII111iI . yesno ( iiiii , "[COLOR %s]Do you wish to restore your" % i11I1IiII1i1i , "Kodi configuration to default settings" , "Before installing [COLOR %s]%s[/COLOR]?" % ( Oo0O00O000 , install ) , nolabel = '[B]No, Cancel[/B]' , yeslabel = '[B]Continue[/B]' )
 else : O0O0 = IiiIII111iI . yesno ( iiiii , "[COLOR %s]Do you wish to restore your" % i11I1IiII1i1i , "Kodi configuration to default settings?[/COLOR]" , nolabel = '[B]No, Cancel[/B]' , yeslabel = '[B]Continue[/B]' )
 if O0O0 :
  if not wiz . currSkin ( ) in [ 'skin.confluence' , 'skin.estuary' ] :
   OoO000Oo0oO = 'skin.confluence' if IIII < 17 else 'skin.estuary'
   I111 = IiiIII111iI . yesno ( iiiii , "[COLOR %s]The skin needs to be set back to [COLOR %s]%s[/COLOR]" % ( i11I1IiII1i1i , Oo0O00O000 , OoO000Oo0oO [ 5 : ] ) , "Before doing a fresh install to clear all Texture files," , "Would you like us to do that for you?[/COLOR]" , yeslabel = "[B]Switch Skins[/B]" , nolabel = "[B]I'll Do It[/B]" ) ;
   if I111 :
    skinSwitch . swapSkins ( OoO000Oo0oO )
    O00oOo0O0o00O = 0
    xbmc . sleep ( 1000 )
    while not xbmc . getCondVisibility ( "Window.isVisible(yesnodialog)" ) and O00oOo0O0o00O < 150 :
     O00oOo0O0o00O += 1
     xbmc . sleep ( 200 )
     wiz . ebi ( 'SendAction(Select)' )
    if xbmc . getCondVisibility ( "Window.isVisible(yesnodialog)" ) :
     wiz . ebi ( 'SendClick(11)' )
    else : wiz . LogNotify ( iiiii , 'Fresh Install: [COLOR red]Skin Swap Timed Out![/COLOR]' ) ; return False
    xbmc . sleep ( 1000 )
   else : wiz . LogNotify ( iiiii , 'Fresh Install: [COLOR red]Cancelled![/COLOR]' ) ; return False
  if not wiz . currSkin ( ) in [ 'skin.confluence' , 'skin.estuary' ] :
   wiz . LogNotify ( iiiii , 'Fresh Install: [COLOR red]Skin Swap Failed![/COLOR]' )
   return
  iI1Ii11111iIi . create ( iiiii , "[COLOR %s]Clearing all files and folders:" % i11I1IiII1i1i , '' , 'Please Wait![/COLOR]' )
  oooOo00000 = os . path . abspath ( i1i1II )
  IiI1IiI1iiI1 = sum ( [ len ( O000o0 ) for Iiiii1 , O0Ooo0O , O000o0 in os . walk ( oooOo00000 ) ] ) ; iii1 = 0
  for oOo0OoOOOo0 , OOoo00 , O000o0 in os . walk ( oooOo00000 , topdown = True ) :
   o0OIiII . append ( 'My_Builds' )
   OOoo00 [ : ] = [ O0Ooo0O for O0Ooo0O in OOoo00 if O0Ooo0O not in o0OIiII ]
   for oO0o0O0Ooo0o in O000o0 :
    iii1 += 1
    iI1iiI = oOo0OoOOOo0 . split ( '\\' )
    O00oOo0O0o00O = len ( iI1iiI ) - 1
    if oO0o0O0Ooo0o == 'sources.xml' and iI1iiI [ - 1 ] == 'userdata' and OOoOO0oo0ooO == 'true' : wiz . log ( "Keep Sources: %s" % os . path . join ( oOo0OoOOOo0 , oO0o0O0Ooo0o ) )
    elif oO0o0O0Ooo0o == 'favourites.xml' and iI1iiI [ - 1 ] == 'userdata' and Oo0OoO00oOO0o == 'true' : wiz . log ( "Keep Favourites: %s" % os . path . join ( oOo0OoOOOo0 , oO0o0O0Ooo0o ) )
    elif oO0o0O0Ooo0o == 'profiles.xml' and iI1iiI [ - 1 ] == 'userdata' and O0o0O00Oo0o0 == 'true' : wiz . log ( "Keep Profiles: %s" % os . path . join ( oOo0OoOOOo0 , oO0o0O0Ooo0o ) )
    elif oO0o0O0Ooo0o == 'advancedsettings.xml' and iI1iiI [ - 1 ] == 'userdata' and O00O0oOO00O00 == 'true' : wiz . log ( "Keep Advanced Settings: %s" % os . path . join ( oOo0OoOOOo0 , oO0o0O0Ooo0o ) )
    elif oO0o0O0Ooo0o in o0oO0oooOoo : wiz . log ( "Keep Log File: %s" % oO0o0O0Ooo0o )
    elif oO0o0O0Ooo0o . endswith ( '.db' ) :
     try :
      if oO0o0O0Ooo0o . endswith ( '.db' ) and oO0o0O0Ooo0o . startswith ( 'Addon' ) and IIII >= 17 : wiz . log ( "Ignoring %s on v%s" % ( oO0o0O0Ooo0o , IIII ) )
      else : os . remove ( os . path . join ( oOo0OoOOOo0 , oO0o0O0Ooo0o ) )
     except Exception , I111oOOooo00OOooO :
      wiz . log ( 'Failed to delete, Purging DB' )
      wiz . log ( "-> %s / %s" % ( Exception , str ( I111oOOooo00OOooO ) ) )
      wiz . purgeDb ( os . path . join ( oOo0OoOOOo0 , oO0o0O0Ooo0o ) )
    else :
     iI1Ii11111iIi . update ( int ( oooOoO00OooO0 ( iii1 , IiI1IiI1iiI1 ) ) , '' , '[COLOR %s]File: [/COLOR][COLOR %s]%s[/COLOR]' % ( i11I1IiII1i1i , Oo0O00O000 , oO0o0O0Ooo0o ) , '' )
     try : os . remove ( os . path . join ( oOo0OoOOOo0 , oO0o0O0Ooo0o ) )
     except Exception , I111oOOooo00OOooO :
      wiz . log ( "Error removing %s" % os . path . join ( oOo0OoOOOo0 , oO0o0O0Ooo0o ) )
      wiz . log ( "-> %s / %s" % ( Exception , str ( I111oOOooo00OOooO ) ) )
   if iI1Ii11111iIi . iscanceled ( ) :
    iI1Ii11111iIi . close ( )
    wiz . LogNotify ( iiiii , "Fresh Start Cancelled" )
    return False
  for oOo0OoOOOo0 , OOoo00 , O000o0 in os . walk ( oooOo00000 , topdown = True ) :
   OOoo00 [ : ] = [ O0Ooo0O for O0Ooo0O in OOoo00 if O0Ooo0O not in o0OIiII ]
   for oO0o0O0Ooo0o in OOoo00 :
    iI1Ii11111iIi . update ( 100 , '' , 'Cleaning Up Empty Folder: [COLOR %s]%s[/COLOR]' % ( Oo0O00O000 , oO0o0O0Ooo0o ) , '' )
    if oO0o0O0Ooo0o not in [ "Database" , "userdata" , "temp" , "addons" , "addon_data" ] :
     shutil . rmtree ( os . path . join ( oOo0OoOOOo0 , oO0o0O0Ooo0o ) , ignore_errors = True , onerror = None )
   if iI1Ii11111iIi . iscanceled ( ) :
    iI1Ii11111iIi . close ( )
    wiz . LogNotify ( iiiii , "Fresh Start Cancelled" )
    return False
  iI1Ii11111iIi . close ( )
  wiz . clearS ( 'build' )
  if install == 'restore' :
   IiiIII111iI . ok ( iiiii , "[COLOR %s]Your current setup for kodi has been cleared!" % i11I1IiII1i1i , "Now we will install the local backup[/COLOR]" )
  elif install :
   IiiIII111iI . ok ( iiiii , "[COLOR %s]Your current setup for kodi has been cleared!" % i11I1IiII1i1i , "Now we will install: [COLOR %s]%s v%s[/COLOR][/COLOR]" % ( Oo0O00O000 , install , wiz . checkBuild ( install , 'version' ) ) )
   ii1i11ii ( install , 'normal' )
  else :
   IiiIII111iI . ok ( iiiii , "[COLOR %s]The process is complete, you're now back to a fresh Kodi configuration with [COLOR %s]%s[/COLOR]" % ( i11I1IiII1i1i , Oo0O00O000 , iiiii ) , "Kodi will now force close, Please relaunch Kodi.[/COLOR]" )
   wiz . killxbmc ( )
 else :
  if not install == 'restore' : wiz . LogNotify ( iiiii , 'Fresh Install: [COLOR red]Cancelled![/COLOR]' ) ; wiz . refresh ( )
  if 22 - 22: oo0 / oo0 - i1III1I % Iii1I1i . oOoOoo + o0o0OoOo0O0OO
  if 64 - 64: oO0Oo0O0o % oOOOOOOo0O00o / i1III1I % oOoooo0O0Oo
  if 24 - 24: Ii1I11I + oOoooo0O0Oo . o0o0OoOo0O0OO / oOOoo00O00o / Iii1I1i
  if 65 - 65: oOoooo0O0Oo
def iiii11iI1 ( ) :
 if IiiIII111iI . yesno ( iiiii , '[COLOR %s]Would you like to clear cache?[/COLOR]' % i11I1IiII1i1i , nolabel = '[B]No, Cancel[/B]' , yeslabel = '[B]Clear Cache[/B]' ) :
  wiz . clearCache ( )
  Oo00Oo ( )
  if 25 - 25: O0ooO0o0O0O
def o0o0O0oOOOooo ( ) :
 if IiiIII111iI . yesno ( iiiii , '[COLOR %s]Would you like to clear cache, packages and thumbnails?[/COLOR]' % i11I1IiII1i1i , nolabel = '[B]Cancel Process[/B]' , yeslabel = '[B]Clean All[/B]' ) :
  wiz . clearCache ( 'total' )
  wiz . clearPackages ( 'total' )
  Oo00Oo ( 'total' )
  wiz . killxbmc ( )
  if 6 - 6: O0ooO0o0O0O - O0ooO0o0O0O % Ii1iI1I1 / O0ooO0o0O0O * Ii1I11I
def Oo00Oo ( type = None ) :
 iIio0oooo0OOo00 = wiz . latestDB ( 'Textures' )
 if not type == None : O0oOoo = 1
 else : O0oOoo = IiiIII111iI . yesno ( iiiii , '[COLOR %s]Would you like to delete the %s and Thumbnails folder?' % ( i11I1IiII1i1i , iIio0oooo0OOo00 ) , "They will repopulate on the next startup[/COLOR]" , nolabel = '[B]Don\'t Delete[/B]' , yeslabel = '[B]Delete Thumbs[/B]' )
 if O0oOoo == 1 :
  try : wiz . removeFile ( os . join ( iiI1IiI , iIio0oooo0OOo00 ) )
  except : wiz . log ( 'Failed to delete, Purging DB.' ) ; wiz . purgeDb ( iIio0oooo0OOo00 )
  wiz . removeFolder ( O0OoO000O0OO )
  if not type == 'total' : wiz . killxbmc ( )
 else : wiz . log ( 'Clear thumbnames cancelled' )
 if 90 - 90: Ii1iI1I1 / oOoOoo - oOoOoo . oOOOOoo0OOO
def o0OOoo0oOoO00 ( ) :
 i1ii1iIi = [ ] ; OOo = [ ]
 for I1I1Ii , iI1IIII1 , O000o0 in os . walk ( i1i1II ) :
  for iIiIIiI1i1Ii in fnmatch . filter ( O000o0 , '*.db' ) :
   if iIiIIiI1i1Ii != 'Thumbs.db' :
    Oo0o = os . path . join ( I1I1Ii , iIiIIiI1i1Ii )
    i1ii1iIi . append ( Oo0o )
    dir = Oo0o . replace ( '\\' , '/' ) . split ( '/' )
    OOo . append ( '(%s) %s' % ( dir [ len ( dir ) - 2 ] , dir [ len ( dir ) - 1 ] ) )
 if IIII >= 16 :
  O0oOoo = IiiIII111iI . multiselect ( "[COLOR %s]Select DB File to Purge[/COLOR]" % i11I1IiII1i1i , OOo )
  if O0oOoo == None : wiz . LogNotify ( "Purge Database" , "Cancelled" )
  elif len ( O0oOoo ) == 0 : wiz . LogNotify ( "Purge Database" , "Cancelled" )
  else :
   for OoO000oo000o0 in O0oOoo : wiz . purgeDb ( i1ii1iIi [ OoO000oo000o0 ] )
 else :
  O0oOoo = IiiIII111iI . select ( "[COLOR %s]Select DB File to Purge[/COLOR]" % i11I1IiII1i1i , OOo )
  if O0oOoo == - 1 : wiz . LogNotify ( "Purge Database" , "Cancelled" )
  else : wiz . purgeDb ( i1ii1iIi [ OoO000oo000o0 ] )
  if 6 - 6: oo0
  if 71 - 71: oo0 . Iii1I1i + oOoOoo
  if 8 - 8: i11iIiiIii * IIOOOO0oo0 + oOOOOOOo0O00o . O0ooO0o0O0O % Iii1I1i / Iii1I1i
  if 70 - 70: oOOOOoo0OOO + i1III1I
def o0o ( ) :
 i1Ii11II = wiz . workingURL ( I1iI1ii1II )
 if i1Ii11II == True :
  O0oOOo0Oo = wiz . openURL ( I1iI1ii1II ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
  id , oOO00OO0o0O = O0oOOo0Oo . split ( '|||' )
  notify . testNotification ( oOO00OO0o0O )
 else : wiz . LogNotify ( iiiii , "Invalid URL for Notification" )
 if 76 - 76: oO00oOOoooO . o0o0OoOo0O0OO % oO00oOOoooO - Ii1I11I
def Oo0O0oo ( ) :
 notify . updateWindow ( )
 if 62 - 62: Iii1I1i / oOOOOOOo0O00o
def OoO0o0O ( ) :
 notify . firstRun ( )
 if 20 - 20: IIOOOO0oo0
def Ooo0oOOoo0O ( ) :
 notify . apkInstaller ( 'SPMC' )
 if 57 - 57: oOOOOoo0OOO . i11iIiiIii * OO + oOoooo0O0Oo + i1III1I
def OoO0o0oOOO ( ) :
 if IiIi11iI == 'No' : oOOOO ( '==============BackUp Options===============' , '' , themeit = iIIii )
 oOOOO ( 'Full Backup' , 'full' , icon = ooOoOoo0O , themeit = oo )
 oOOOO ( 'Backup for Builds (Exc: Thumbnails, Databases)' , 'backb' , icon = ooOoOoo0O , themeit = oo )
 oOOOO ( 'Backup addon data' , 'backad' , icon = ooOoOoo0O , themeit = oo )
 if IiIi11iI == 'No' : oOOOO ( '==============Restore Options===============' , '' , themeit = iIIii )
 oOoo000 ( 'Restore Full Backup' , 'refull' , icon = ooOoOoo0O , themeit = oo )
 oOoo000 ( 'Restore Addon Data' , 'refull' , icon = ooOoOoo0O , themeit = oo )
 if IiIi11iI == 'No' : oOOOO ( '==============Other Options===============' , '' , themeit = iIIii )
 oOoo000 ( 'Delete A Backup' , 'delbu' , icon = ooOoOoo0O , themeit = oo )
 oOOOO ( 'Delete All Backups' , 'delall' , icon = ooOoOoo0O , themeit = oo )
 oOOOO ( 'Select Backup Location' , 'settings' , icon = ooOoOoo0O , themeit = oo )
 if 86 - 86: oOOoo00O00o . o0o0OoOo0O0OO
 if 10 - 10: oO00oOOoooO * i1III1I - oo0 . Iii1I1i - oOoOoo
 if 94 - 94: oOOOOoo0OOO % o0o0OoOo0O0OO + I111I1Iiii1i
 if 90 - 90: oO0Oo0O0o + IIOOOO0oo0 - iiIi111 . oO00oOOoooO + O0ooO0o0O0O
 if 88 - 88: i1III1I * IIOOOO0oo0 . Ii1I11I / oOoooo0O0Oo
 if 29 - 29: oOoooo0O0Oo . OO % oOOoo00O00o
def IiI11i1IIiiI ( display , mode = None , name = None , url = None , menu = None , description = iiiii , overwrite = True , fanart = II , icon = ooOoOoo0O , themeit = None ) :
 IiiIi1I11 = sys . argv [ 0 ]
 if not mode == None : IiiIi1I11 += "?mode=%s" % urllib . quote_plus ( mode )
 if not name == None : IiiIi1I11 += "&name=" + urllib . quote_plus ( name )
 if not url == None : IiiIi1I11 += "&url=" + urllib . quote_plus ( url )
 i1I1Ii11II1i = True
 if themeit : display = themeit % display
 oooOoOOoOO0O = xbmcgui . ListItem ( display , iconImage = "DefaultFolder.png" , thumbnailImage = icon )
 oooOoOOoOO0O . setInfo ( type = "Video" , infoLabels = { "Title" : display , "Plot" : description } )
 oooOoOOoOO0O . setProperty ( "Fanart_Image" , fanart )
 if not menu == None : oooOoOOoOO0O . addContextMenuItems ( menu , replaceItems = overwrite )
 i1I1Ii11II1i = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = IiiIi1I11 , listitem = oooOoOOoOO0O , isFolder = True )
 return i1I1Ii11II1i
 if 9 - 9: Ii1I11I * oOoooo0O0Oo % oOOOOoo0OOO / oOOoo00O00o * Iii1I1i
def ooOOo0o ( name , url , mode , iconimage , fanart , description ) :
 if 48 - 48: oOoooo0O0Oo . oOOoo00O00o
 IiiIi1I11 = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart ) + "&description=" + urllib . quote_plus ( description )
 i1I1Ii11II1i = True
 oooOoOOoOO0O = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 oooOoOOoOO0O . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description } )
 oooOoOOoOO0O . setProperty ( "Fanart_Image" , fanart )
 i1I1Ii11II1i = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = IiiIi1I11 , listitem = oooOoOOoOO0O , isFolder = False )
 if 65 - 65: iiIi111 . ii1Ii1I1Ii11i
def oOoo000 ( display , mode , name = None , url = None , menu = None , overwrite = True , fanart = II , icon = ooOoOoo0O , themeit = None ) :
 IiiIi1I11 = '%s?mode=%s' % ( sys . argv [ 0 ] , urllib . quote_plus ( mode ) )
 if not name == None : IiiIi1I11 += "&name=" + urllib . quote_plus ( name )
 if not url == None : IiiIi1I11 += "&url=" + urllib . quote_plus ( url )
 i1I1Ii11II1i = True
 if themeit : display = themeit % display
 oooOoOOoOO0O = xbmcgui . ListItem ( display , iconImage = "DefaultFolder.png" , thumbnailImage = icon )
 oooOoOOoOO0O . setInfo ( type = "Video" , infoLabels = { "Title" : display , "Plot" : iiiii } )
 oooOoOOoOO0O . setProperty ( "Fanart_Image" , fanart )
 if not menu == None : oooOoOOoOO0O . addContextMenuItems ( menu , replaceItems = overwrite )
 i1I1Ii11II1i = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = IiiIi1I11 , listitem = oooOoOOoOO0O , isFolder = True )
 return i1I1Ii11II1i
 if 94 - 94: oOOoo00O00o + o0o0OoOo0O0OO . oo0
def i1OoOO ( name , url , mode , iconimage ) :
 IiiIi1I11 = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage )
 i1I1Ii11II1i = True
 oooOoOOoOO0O = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 oooOoOOoOO0O . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : name } )
 i1I1Ii11II1i = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = IiiIi1I11 , listitem = oooOoOOoOO0O , isFolder = True )
 return i1I1Ii11II1i
 if 69 - 69: IIOOOO0oo0 - IIOOOO0oo0
def ooO00O00oOO ( name , url , mode , iconimage , fanart , description , installRating ) :
 IiiIi1I11 = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart ) + "&description=" + urllib . quote_plus ( description ) + "&installRating=" + urllib . quote_plus ( installRating )
 i1I1Ii11II1i = True
 oooOoOOoOO0O = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 oooOoOOoOO0O . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description , "Premiered" : installRating } )
 oooOoOOoOO0O . setProperty ( "Fanart_Image" , fanart )
 i1I1Ii11II1i = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = IiiIi1I11 , listitem = oooOoOOoOO0O , isFolder = False )
 return i1I1Ii11II1i
 if 41 - 41: o0o0OoOo0O0OO % Ii1iI1I1
def Oo00oo0000OO ( display , mode = None , name = None , url = None , menu = None , description = iiiii , overwrite = True , fanart = II , icon = ooOoOoo0O , themeit = None ) :
 IiiIi1I11 = sys . argv [ 0 ]
 if not mode == None : IiiIi1I11 += "?mode=%s" % urllib . quote_plus ( mode )
 if not name == None : IiiIi1I11 += "&name=" + urllib . quote_plus ( name )
 if not url == None : IiiIi1I11 += "&url=" + urllib . quote_plus ( url )
 i1I1Ii11II1i = True
 if themeit : display = themeit % display
 oooOoOOoOO0O = xbmcgui . ListItem ( display , iconImage = "DefaultFolder.png" , thumbnailImage = icon )
 oooOoOOoOO0O . setInfo ( type = "Video" , infoLabels = { "Title" : display , "Plot" : description } )
 oooOoOOoOO0O . setProperty ( "Fanart_Image" , fanart )
 if not menu == None : oooOoOOoOO0O . addContextMenuItems ( menu , replaceItems = overwrite )
 i1I1Ii11II1i = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = IiiIi1I11 , listitem = oooOoOOoOO0O , isFolder = False )
 return i1I1Ii11II1i
 if 67 - 67: IIOOOO0oo0 % Ii1I11I
def oOo0O ( display , mode , name = None , url = None , menu = None , overwrite = True , fanart = II , icon = ooOoOoo0O , description = None , themeit = None ) :
 IiiIi1I11 = '%s?mode=%s' % ( sys . argv [ 0 ] , urllib . quote_plus ( mode ) )
 if not name == None : IiiIi1I11 += "&name=" + urllib . quote_plus ( name )
 if not url == None : IiiIi1I11 += "&url=" + urllib . quote_plus ( url )
 if not description == None : IiiIi1I11 += "&description=" + urllib . quote_plus ( description )
 i1I1Ii11II1i = True
 if themeit : display = themeit % display
 oooOoOOoOO0O = xbmcgui . ListItem ( description , iconImage = "DefaultFolder.png" , thumbnailImage = icon )
 oooOoOOoOO0O . setInfo ( type = "Video" , infoLabels = { "Title" : description , "Plot" : iiiii } )
 oooOoOOoOO0O . setProperty ( "Fanart_Image" , fanart )
 if not menu == None : oooOoOOoOO0O . addContextMenuItems ( menu , replaceItems = overwrite )
 i1I1Ii11II1i = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = IiiIi1I11 , listitem = oooOoOOoOO0O , isFolder = False )
 return i1I1Ii11II1i
 if 35 - 35: oOOOOoo0OOO . oOOoo00O00o + oOoooo0O0Oo % ii1Ii1I1Ii11i % oOoOoo
def oOOOO ( display , mode , name = None , url = None , menu = None , overwrite = True , fanart = II , icon = ooOoOoo0O , themeit = None ) :
 IiiIi1I11 = '%s?mode=%s' % ( sys . argv [ 0 ] , urllib . quote_plus ( mode ) )
 if not name == None : IiiIi1I11 += "&name=" + urllib . quote_plus ( name )
 if not url == None : IiiIi1I11 += "&url=" + urllib . quote_plus ( url )
 i1I1Ii11II1i = True
 if themeit : display = themeit % display
 oooOoOOoOO0O = xbmcgui . ListItem ( display , iconImage = "DefaultFolder.png" , thumbnailImage = icon )
 oooOoOOoOO0O . setInfo ( type = "Video" , infoLabels = { "Title" : display , "Plot" : iiiii } )
 oooOoOOoOO0O . setProperty ( "Fanart_Image" , fanart )
 if not menu == None : oooOoOOoOO0O . addContextMenuItems ( menu , replaceItems = overwrite )
 i1I1Ii11II1i = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = IiiIi1I11 , listitem = oooOoOOoOO0O , isFolder = False )
 return i1I1Ii11II1i
 if 39 - 39: i1III1I
def oOo0000ooO ( name , url , mode , iconimage , fanart , description ) :
 IiiIi1I11 = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&fanart=" + urllib . quote_plus ( fanart )
 i1I1Ii11II1i = True
 oooOoOOoOO0O = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 oooOoOOoOO0O . setInfo ( type = "Video" , infoLabels = { "Title" : name } )
 oooOoOOoOO0O . setProperty ( "Fanart_Image" , fanart )
 i1I1Ii11II1i = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = IiiIi1I11 , listitem = oooOoOOoOO0O , isFolder = False )
 return i1I1Ii11II1i
 if 15 - 15: oo0 . Ii1iI1I1 + oOOoo00O00o . O0ooO0o0O0O % oo0 + IIOOOO0oo0
def iiIiiIi1 ( name , url , mode , iconimage , fanart , description ) :
 if 22 - 22: Ii1iI1I1 + ii1Ii1I1Ii11i . oo0 + oOOOOOOo0O00o * oO00oOOoooO . i11iIiiIii
 IiiIi1I11 = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart ) + "&description=" + urllib . quote_plus ( description )
 i1I1Ii11II1i = True
 oooOoOOoOO0O = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 oooOoOOoOO0O . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description } )
 oooOoOOoOO0O . setProperty ( "Fanart_Image" , fanart )
 i1I1Ii11II1i = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = IiiIi1I11 , listitem = oooOoOOoOO0O , isFolder = True )
 return i1I1Ii11II1i
 if 90 - 90: oOoOoo * oOOoo00O00o - ii1Ii1I1Ii11i + Ii1iI1I1
 if 53 - 53: oOoooo0O0Oo . oOoooo0O0Oo + Ii1iI1I1 - oO00oOOoooO + oOoOoo
 if 44 - 44: Ii1I11I - o0o0OoOo0O0OO
def OOOi1iIIiiIiII ( name , url , mode , iconimage , fanart , description ) :
 IiiIi1I11 = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart ) + "&description=" + urllib . quote_plus ( description )
 i1I1Ii11II1i = True
 oooOoOOoOO0O = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 oooOoOOoOO0O . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description } )
 oooOoOOoOO0O . setProperty ( "Fanart_Image" , fanart )
 if mode == 90 :
  i1I1Ii11II1i = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = IiiIi1I11 , listitem = oooOoOOoOO0O , isFolder = False )
 else :
  i1I1Ii11II1i = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = IiiIi1I11 , listitem = oooOoOOoOO0O , isFolder = True )
 return i1I1Ii11II1i
 if 20 - 20: oo0 . I111I1Iiii1i * oO00oOOoooO
 if 71 - 71: ii1Ii1I1Ii11i . OO / OO * i1III1I * I111I1Iiii1i
def IiiI11 ( ) :
 o0o0oO00OoO0o = [ ]
 Oo0OO00 = sys . argv [ 2 ]
 if len ( Oo0OO00 ) >= 2 :
  o0ooOOOo = sys . argv [ 2 ]
  OOoOOo0oO = o0ooOOOo . replace ( '?' , '' )
  if ( o0ooOOOo [ len ( o0ooOOOo ) - 1 ] == '/' ) :
   o0ooOOOo = o0ooOOOo [ 0 : len ( o0ooOOOo ) - 2 ]
  I1Ii1IIIiII = OOoOOo0oO . split ( '&' )
  o0o0oO00OoO0o = { }
  for IiIiiiiI1 in range ( len ( I1Ii1IIIiII ) ) :
   iiII1IIii1i1 = { }
   iiII1IIii1i1 = I1Ii1IIIiII [ IiIiiiiI1 ] . split ( '=' )
   if ( len ( iiII1IIii1i1 ) ) == 2 :
    o0o0oO00OoO0o [ iiII1IIii1i1 [ 0 ] ] = iiII1IIii1i1 [ 1 ]
    if 38 - 38: oO00oOOoooO * oOoooo0O0Oo
  return o0o0oO00OoO0o
  if 2 - 2: iiIi111 - i11iIiiIii
o0ooOOOo = IiiI11 ( )
i1Ii11II = None
oO0o0O0Ooo0o = None
OOOo00o = None
ooOoOOOOo = None
o0o0 = None
IIi1IIIIi = None
ii1iiii1 = None
if 94 - 94: oo0 + oOOOOoo0OOO
try :
 ii1iiii1 = int ( o0ooOOOo [ "fav_mode" ] )
except :
 pass
try : OOOo00o = urllib . unquote_plus ( o0ooOOOo [ "mode" ] )
except : pass
try : oO0o0O0Ooo0o = urllib . unquote_plus ( o0ooOOOo [ "name" ] )
except : pass
try : i1Ii11II = urllib . unquote_plus ( o0ooOOOo [ "url" ] )
except : pass
try : ooOoOOOOo = urllib . unquote_plus ( o0ooOOOo [ "iconimage" ] )
except : pass
try : o0o0 = urllib . unquote_plus ( o0ooOOOo [ "fanart" ] )
except : pass
try : IIi1IIIIi = urllib . unquote_plus ( o0ooOOOo [ "description" ] )
except : pass
if 56 - 56: oOOoo00O00o % Ii1iI1I1
print str ( oo00 ) + ': ' + str ( ooOo )
print "Mode: " + str ( OOOo00o )
print "URL: " + str ( i1Ii11II )
print "Name: " + str ( oO0o0O0Ooo0o )
print "IconImage: " + str ( ooOoOOOOo )
if 40 - 40: oOoOoo / o0o0OoOo0O0OO
wiz . log ( '[ Version : \'%s\' ] [ Mode : \'%s\' ] [ Name : \'%s\' ] [ Url : \'%s\' ]' % ( ooOo , OOOo00o if not OOOo00o == '' else None , oO0o0O0Ooo0o , i1Ii11II ) )
def i1i11I1I1 ( ) :
 if 82 - 82: I111I1Iiii1i - ii1Ii1I1Ii11i - IIOOOO0oo0 - oOoooo0O0Oo
 for file in os . listdir ( oo0o0O00 ) :
  if file . endswith ( ".zip" ) :
   i1Ii11II = xbmc . translatePath ( os . path . join ( oo0o0O00 , file ) )
   oOo0000ooO ( file , i1Ii11II , 'read' , ooOoOoo0O , ooOoOoo0O , '' )
   if 4 - 4: OO - iiIi111 % ii1Ii1I1Ii11i * i11iIiiIii
def iIiII1iiiiI ( ) :
 OOOOooO0 = xbmc . translatePath ( os . path . join ( 'special://' , 'home' ) )
 for file in os . listdir ( oo0o0O00 ) :
  if file . endswith ( ".zip" ) :
   i1Ii11II = xbmc . translatePath ( os . path . join ( oo0o0O00 , file ) )
   OOOi1iIIiiIiII ( file , i1Ii11II , 'dell' , ooOoOoo0O , ooOoOoo0O , '' )
   if 86 - 86: o0o0OoOo0O0OO
def oOOo000oOoO0 ( content , viewType ) :
 if 43 - 43: oOOOOoo0OOO / oO00oOOoooO / oo0 + O0ooO0o0O0O + oOoooo0O0Oo
 if content :
  xbmcplugin . setContent ( int ( sys . argv [ 1 ] ) , content )
 if ooo0OO . getSetting ( 'auto-view' ) == 'true' :
  xbmc . executebuiltin ( "Container.SetViewMode(%s)" % ooo0OO . getSetting ( viewType ) )
  if 33 - 33: OO - o0o0OoOo0O0OO - oo0
  if 92 - 92: I111I1Iiii1i * o0o0OoOo0O0OO
  if 92 - 92: iiIi111
  if 7 - 7: oO00oOOoooO
  if 73 - 73: I111I1Iiii1i % oOOOOOOo0O00o
  if 32 - 32: oOoOoo + oO00oOOoooO + O0ooO0o0O0O * ii1Ii1I1Ii11i
  if 62 - 62: i11iIiiIii
if OOOo00o == None : oOooO0 ( )
if 2 - 2: oOOOOoo0OOO
elif OOOo00o == 'wizardupdate' : wiz . wizardUpdate ( )
elif OOOo00o == 'builds' : OOOooo ( )
elif OOOo00o == 'viewbuild' : ii1oOoO0o0ooo ( oO0o0O0Ooo0o )
elif OOOo00o == 'buildinfo' : oO00o00 ( oO0o0O0Ooo0o )
elif OOOo00o == 'install' : ii1i11ii ( oO0o0O0Ooo0o , i1Ii11II )
elif OOOo00o == 'theme' : ii1i11ii ( oO0o0O0Ooo0o , OOOo00o , i1Ii11II )
if 69 - 69: oOoooo0O0Oo / ii1Ii1I1Ii11i * Ii1I11I
elif OOOo00o == 'pro' : IiII1i1iI ( )
if 99 - 99: OO * O0ooO0o0O0O % IIOOOO0oo0 * iiIi111 / OO % oOoooo0O0Oo
elif OOOo00o == 'maint' : Oo0oOo0ooOOOo ( oO0o0O0Ooo0o )
elif OOOo00o == 'speed' : OOOOo000o00OO ( )
elif OOOo00o == 'advancedsetting' : i1IiiiiIi1I ( )
elif OOOo00o == 'autoadvanced' : Oo0O0OOO0o0O ( ) ; wiz . refresh ( )
elif OOOo00o == 'asciicheck' : wiz . asciiCheck ( )
elif OOOo00o == 'backupbuild' : wiz . backUpOptions ( 'build' )
elif OOOo00o == 'backupgui' : wiz . backUpOptions ( 'guifix' )
elif OOOo00o == 'backuptheme' : wiz . backUpOptions ( 'theme' )
elif OOOo00o == 'backupaddon' : wiz . backUpOptions ( 'addondata' )
elif OOOo00o == 'clearbackup' : wiz . cleanupBackup ( )
elif OOOo00o == 'convertpath' : wiz . convertSpecial ( i1i1II )
elif OOOo00o == 'currentsettings' : III1II1i ( )
elif OOOo00o == 'fullclean' : o0o0O0oOOOooo ( ) ; wiz . refresh ( )
elif OOOo00o == 'clearcache' : iiii11iI1 ( ) ; wiz . refresh ( )
elif OOOo00o == 'clearpackages' : wiz . clearPackages ( ) ; wiz . refresh ( )
elif OOOo00o == 'clearcrash' : wiz . clearCrash ( ) ; wiz . refresh ( )
elif OOOo00o == 'clearthumb' : Oo00Oo ( ) ; wiz . refresh ( )
elif OOOo00o == 'checksources' : wiz . checkSources ( ) ; wiz . refresh ( )
elif OOOo00o == 'checkrepos' : wiz . checkRepos ( ) ; wiz . refresh ( )
elif OOOo00o == 'freshstart' : IiI1 ( )
elif OOOo00o == 'forceupdate' : wiz . forceUpdate ( )
elif OOOo00o == 'forceclose' : wiz . killxbmc ( )
elif OOOo00o == 'forceskin' : wiz . ebi ( "ReloadSkin()" ) ; wiz . refresh ( )
elif OOOo00o == 'hidepassword' : wiz . hidePassword ( )
elif OOOo00o == 'unhidepassword' : wiz . unhidePassword ( )
elif OOOo00o == 'enableaddons' : o0oOo0OO ( )
elif OOOo00o == 'toggleaddon' : wiz . toggleAddon ( oO0o0O0Ooo0o , i1Ii11II ) ; wiz . refresh ( )
elif OOOo00o == 'togglecache' : O00Ooo0ooo0 ( oO0o0O0Ooo0o ) ; wiz . refresh ( )
elif OOOo00o == 'toggleadult' : wiz . toggleAdult ( ) ; wiz . refresh ( )
elif OOOo00o == 'changefeq' : ooOOO00oOOooO ( ) ; wiz . refresh ( )
elif OOOo00o == 'uploadlog' : uploadLog . Main ( )
elif OOOo00o == 'viewlog' : II1IIii1ii ( )
elif OOOo00o == 'viewwizlog' : Oo00Oooo00o ( )
elif OOOo00o == 'viewerrorlog' : Oo0OOo ( )
elif OOOo00o == 'clearwizlog' : iIiIIiI1i1Ii = open ( II11iiii1Ii , 'w' ) ; iIiIIiI1i1Ii . close ( ) ; wiz . LogNotify ( iiiii , "Wizard Log Cleared!" )
elif OOOo00o == 'purgedb' : o0OOoo0oOoO00 ( )
elif OOOo00o == 'fixaddonupdate' : wiz . purgeDb ( os . path . join ( iiI1IiI , wiz . latestDB ( 'Addons' ) ) )
elif OOOo00o == 'removeaddons' : iI11111ii11 ( )
elif OOOo00o == 'removeaddon' : OOO00000o0 ( oO0o0O0Ooo0o )
elif OOOo00o == 'removeaddondata' : ooii11i ( )
elif OOOo00o == 'removedata' : i1iIiIIi1II1ii ( oO0o0O0Ooo0o )
elif OOOo00o == 'resetaddon' : I1IIIi1i = wiz . cleanHouse ( i1iIIi1 , ignore = True ) ; wiz . LogNotify ( iiiii , "Addon_Data reset" )
elif OOOo00o == 'systeminfo' : oO0oOoo0O ( )
elif OOOo00o == 'restorezip' : ooOoOo ( 'build' )
elif OOOo00o == 'restoregui' : ooOoOo ( 'gui' )
elif OOOo00o == 'restoreaddon' : ooOoOo ( 'addondata' )
elif OOOo00o == 'restoreextzip' : iiI1iIII1ii ( 'build' )
elif OOOo00o == 'restoreextgui' : iiI1iIII1ii ( 'gui' )
elif OOOo00o == 'restoreextaddon' : iiI1iIII1ii ( 'addondata' )
elif OOOo00o == 'writeadvanced' : o0o0OO0o00o0O ( oO0o0O0Ooo0o )
if 14 - 14: o0o0OoOo0O0OO . o0o0OoOo0O0OO % oo0
elif OOOo00o == 'apk1' : iIIIII1iiiiII ( )
elif OOOo00o == 'apkgame' : OooOO0o0 ( i1Ii11II )
elif OOOo00o == 'select' : o000 ( i1Ii11II )
elif OOOo00o == 'grab' : oo00OOoOoO00 ( oO0o0O0Ooo0o , i1Ii11II )
elif OOOo00o == 'rom' : OOO0o0OO0OO ( i1Ii11II )
elif OOOo00o == 'apkscrape' : APK ( )
elif OOOo00o == 'apkshow' : O0O0o0o0o ( i1Ii11II )
elif OOOo00o == 'apkkodi' : III1I1Ii11iI ( )
elif OOOo00o == 'intellaunch' : ii1I11iIiIII1 ( )
elif OOOo00o == 'intelselect' : Oo0Ooo0O0 ( oO0o0O0Ooo0o , i1Ii11II , ooOoOOOOo , o0o0 , IIi1IIIIi )
elif OOOo00o == 'emurom' : Ii11iI1ii1111 ( )
elif OOOo00o == 'roms' : IiI1i111IiIiIi1 ( )
elif OOOo00o == 'snes' : I1Ii ( )
elif OOOo00o == 'nes' : ooOo0O0O0oOO0 ( )
elif OOOo00o == 'gen' : I11oOOooo ( )
elif OOOo00o == 'atr' : iIiI1i ( )
elif OOOo00o == 'n64' : iiIii ( )
elif OOOo00o == 'tbg' : O000O ( )
elif OOOo00o == 'nds' : I1I1IiIi1 ( )
elif OOOo00o == 'ps' : I1iIoO0Ooo0OooOOo ( )
elif OOOo00o == 'apkinstall' : I1iii ( oO0o0O0Ooo0o , i1Ii11II , "None" )
elif OOOo00o == 'rominstall' : iIIiI1111 ( oO0o0O0Ooo0o , i1Ii11II , )
if 42 - 42: Ii1iI1I1 . oOoOoo - oo0
elif OOOo00o == 'youtube' : II1III1i1iiI ( i1Ii11II )
elif OOOo00o == 'viewVideo' : Ii1 ( i1Ii11II )
if 33 - 33: OO / IIOOOO0oo0 / o0o0OoOo0O0OO - Iii1I1i - oO0Oo0O0o
elif OOOo00o == 'savedata' : OOooO ( )
elif OOOo00o == 'togglesetting' : wiz . setS ( oO0o0O0Ooo0o , 'false' if wiz . getS ( oO0o0O0Ooo0o ) == 'true' else 'true' ) ; wiz . refresh ( )
if 8 - 8: i11iIiiIii . oO00oOOoooO / O0ooO0o0O0O / oOOOOOOo0O00o / o0o0OoOo0O0OO - i1III1I
elif OOOo00o == 'trakt' : OOoooOoO0 ( )
elif OOOo00o == 'savetrakt' : traktit . traktIt ( 'update' , oO0o0O0Ooo0o )
elif OOOo00o == 'restoretrakt' : traktit . traktIt ( 'restore' , oO0o0O0Ooo0o )
elif OOOo00o == 'addontrakt' : traktit . traktIt ( 'clearaddon' , oO0o0O0Ooo0o )
elif OOOo00o == 'cleartrakt' : traktit . clearSaved ( oO0o0O0Ooo0o )
elif OOOo00o == 'authtrakt' : traktit . activateTrakt ( oO0o0O0Ooo0o ) ; wiz . refresh ( )
elif OOOo00o == 'updatetrakt' : traktit . autoUpdate ( 'all' )
elif OOOo00o == 'importtrakt' : traktit . importlist ( oO0o0O0Ooo0o ) ; wiz . refresh ( )
if 32 - 32: Ii1iI1I1 . oO0Oo0O0o * ii1Ii1I1Ii11i
elif OOOo00o == 'realdebrid' : iIi1 ( )
elif OOOo00o == 'savedebrid' : debridit . debridIt ( 'update' , oO0o0O0Ooo0o )
elif OOOo00o == 'restoredebrid' : debridit . debridIt ( 'restore' , oO0o0O0Ooo0o )
elif OOOo00o == 'addondebrid' : debridit . debridIt ( 'clearaddon' , oO0o0O0Ooo0o )
elif OOOo00o == 'cleardebrid' : debridit . clearSaved ( oO0o0O0Ooo0o )
elif OOOo00o == 'authdebrid' : debridit . activateDebrid ( oO0o0O0Ooo0o ) ; wiz . refresh ( )
elif OOOo00o == 'updatedebrid' : debridit . autoUpdate ( 'all' )
elif OOOo00o == 'importdebrid' : debridit . importlist ( oO0o0O0Ooo0o ) ; wiz . refresh ( )
if 98 - 98: i1III1I - OO / oOOOOoo0OOO . iiIi111 * o0o0OoOo0O0OO . Iii1I1i
elif OOOo00o == 'addons' : II1iIII ( )
elif OOOo00o == 'addoninstall' : o0o0O00 ( oO0o0O0Ooo0o )
if 25 - 25: i11iIiiIii / oOOoo00O00o - Ii1I11I / I111I1Iiii1i . Ii1iI1I1 . Ii1iI1I1
elif OOOo00o == 'contact' : notify . contact ( OOOOoOoO0o0 )
elif OOOo00o == 'settings' : wiz . openS ( oO0o0O0Ooo0o ) ; wiz . refresh ( )
elif OOOo00o == 'opensettings' : id = eval ( i1Ii11II . upper ( ) + 'ID' ) [ oO0o0O0Ooo0o ] [ 'plugin' ] ; iI1iIIII1 = wiz . addonId ( id ) ; iI1iIIII1 . openSettings ( ) ; wiz . refresh ( )
if 65 - 65: IIOOOO0oo0 / OO . O0ooO0o0O0O . iiIi111 / ii1Ii1I1Ii11i % O0ooO0o0O0O
elif OOOo00o == 'developer' : iI11II1i1I1 ( )
elif OOOo00o == 'converttext' : wiz . convertText ( oO0o0O0Ooo0o )
elif OOOo00o == 'testnotify' : o0o ( )
elif OOOo00o == 'bre' : OoO0o0oOOO ( )
elif OOOo00o == 'full' : backuprestore . FullBackup ( )
elif OOOo00o == 'backb' : backuprestore . Backup ( )
elif OOOo00o == 'backad' : backuprestore . ADDON_DATA_BACKUP ( )
elif OOOo00o == 'refull' : i1i11I1I1 ( )
elif OOOo00o == 'delbu' : iIiII1iiiiI ( )
elif OOOo00o == 'delall' : backuprestore . DeleteAllBackups ( )
elif OOOo00o == 'read' : backuprestore . READ_ZIP ( i1Ii11II )
elif OOOo00o == 'dell' : backuprestore . DeleteBackup ( i1Ii11II )
elif OOOo00o == 'testupdate' : Oo0O0oo ( )
elif OOOo00o == 'testfirst' : OoO0o0O ( )
if 74 - 74: oO0Oo0O0o / oOOOOoo0OOO % oOOOOOOo0O00o / IIOOOO0oo0 % Iii1I1i - oOOoo00O00o
elif OOOo00o == 'guide' : OOoooO00o0o ( )
if 31 - 31: oOOOOoo0OOO / oOoooo0O0Oo . O0ooO0o0O0O * oOOoo00O00o . oOoooo0O0Oo + OO
elif OOOo00o == 'recreateaddon' : oOo0OO0o0 ( )
elif OOOo00o == 'getlistplay' : OoO0Oo00 ( oO0o0O0Ooo0o )
elif OOOo00o == 'resolve' : I1iI11I ( i1Ii11II )
elif OOOo00o == 'streams' : OOo00ooOoO0o ( )
elif OOOo00o == 'liveevent' : o00iIiiiII ( oO0o0O0Ooo0o )
elif OOOo00o == 'addonopen' : ooo0OO . openSettings ( sys . argv [ 0 ] )
if OOOo00o not in [ '' , 'togglesettings' , 'settings' , 'contact' ] : xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
# dd678faae9ac167bc83abf78e5cb2f3f0688d3a3