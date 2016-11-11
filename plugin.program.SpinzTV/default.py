import xbmc , xbmcaddon , xbmcgui , xbmcplugin , os , sys , xbmcvfs , glob
import shutil
import urllib2 , urllib
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
try : from sqlite3 import dbapi2 as database
except : from pysqlite2 import dbapi2 as database
from datetime import date , datetime , timedelta
from resources . libs import extract , downloader , notify , debridit , traktit , loginit , skinSwitch , uploadLog , yt , wizard as wiz
if 64 - 64: i11iIiiIii
OO0o = xbmcaddon . Addon ( ) . getAddonInfo ( 'id' )
Oo0Ooo = 'SpinzTV'
O0O0OO0O0O0 = wiz . addonId ( OO0o )
iiiii = xbmcaddon . Addon ( OO0o )
ooo0OO = iiiii . getAddonInfo ( 'path' ) . decode ( "utf-8" )
II1 = xbmc . translatePath ( os . path . join ( ooo0OO , "resources" , "iiNT3LiiList.txt" ) )
O00ooooo00 = wiz . addonInfo ( OO0o , 'version' )
I1IiiI = wiz . addonInfo ( OO0o , 'path' )
IIi1IiiiI1Ii = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3'
I11i11Ii = xbmcgui . Dialog ( )
oO00oOo = xbmcgui . DialogProgress ( )
OOOo0 = xbmc . translatePath ( 'special://home/' )
Oooo000o = xbmc . translatePath ( os . path . join ( '//storage//emulated//0//Download' , '' ) )
IiIi11iIIi1Ii = xbmc . translatePath ( 'special://logpath/' )
Oo0O = xbmc . translatePath ( 'special://profile/' )
IiI = os . path . join ( OOOo0 , 'addons' )
zip = plugintools . get_setting ( "zip" )
ooOo = xbmc . translatePath ( os . path . join ( zip ) )
IiI = os . path . join ( OOOo0 , 'addons' )
Oo = os . path . join ( OOOo0 , 'userdata' )
o0O = os . path . join ( IiI , OO0o )
IiiIII111iI = os . path . join ( IiI , 'packages' )
IiII = os . path . join ( Oo , 'addon_data' )
iI1Ii11111iIi = os . path . join ( Oo , 'addon_data' , OO0o )
i1i1II = os . path . join ( Oo , 'advancedsettings.xml' )
O0oo0OO0 = os . path . join ( Oo , 'sources.xml' )
I1i1iiI1 = os . path . join ( Oo , 'favourites.xml' )
iiIIIII1i1iI = os . path . join ( Oo , 'profiles.xml' )
o0oO0 = os . path . join ( Oo , 'guisettings.xml' )
oo00 = os . path . join ( Oo , 'Thumbnails' )
o00 = os . path . join ( Oo , 'Database' )
Oo0oO0ooo = os . path . join ( o0O , 'fanart.jpg' )
o0oOoO00o = os . path . join ( o0O , 'icon.png' )
i1 = os . path . join ( o0O , 'resources' , 'art' )
oOOoo00O0O = os . path . join ( iI1Ii11111iIi , 'wizard.log' )
i1111 = xbmc . getSkinDir ( )
i11 = wiz . getS ( 'buildname' )
I11 = wiz . getS ( 'defaultskin' )
Oo0o0000o0o0 = wiz . getS ( 'defaultskinname' )
oOo0oooo00o = wiz . getS ( 'defaultskinignore' )
oO0o0o0ooO0oO = wiz . getS ( 'buildversion' )
oo0o0O00 = wiz . getS ( 'buildtheme' )
oO = wiz . getS ( 'latestversion' )
i1iiIIiiI111 = wiz . getS ( 'show15' )
oooOOOOO = wiz . getS ( 'show16' )
i1iiIII111ii = wiz . getS ( 'show17' )
i1iIIi1 = wiz . getS ( 'adult' )
ii11iIi1I = wiz . getS ( 'showmaint' )
iI111I11I1I1 = wiz . getS ( 'autoclean' )
OOooO0OOoo = wiz . getS ( 'clearcache' )
iIii1 = wiz . getS ( 'clearpackages' )
oOOoO0 = wiz . getS ( 'clearthumbs' )
O0OoO000O0OO = wiz . getS ( 'autocleanfeq' )
iiI1IiI = wiz . getS ( 'delayautoclean' )
II = wiz . getS ( 'nextautocleanup' )
ooOoOoo0O = wiz . getS ( 'includevideo' )
OooO0 = wiz . getS ( 'includeall' )
II11iiii1Ii = wiz . getS ( 'includebob' )
OO0oOoo = wiz . getS ( 'includephoenix' )
O0o0Oo = wiz . getS ( 'includespecto' )
Oo00OOOOO = wiz . getS ( 'includegenesis' )
O0O = wiz . getS ( 'includeexodus' )
O00o0OO = wiz . getS ( 'includeonechan' )
I11i1 = wiz . getS ( 'includesalts' )
iIi1ii1I1 = wiz . getS ( 'includesaltslite' )
o0 = wiz . getS ( 'seperate' )
I11II1i = wiz . getS ( 'notify' )
IIIII = wiz . getS ( 'noteid' )
ooooooO0oo = wiz . getS ( 'notedismiss' )
IIiiiiiiIi1I1 = wiz . getS ( 'traktlastsave' )
I1IIIii = wiz . getS ( 'debridlastsave' )
oOoOooOo0o0 = wiz . getS ( 'keepfavourites' )
OOOO = wiz . getS ( 'keepgui' )
OOO00 = wiz . getS ( 'keepsources' )
iiiiiIIii = wiz . getS ( 'keepprofiles' )
O000OO0 = wiz . getS ( 'keepadvanced' )
I11iii1Ii = wiz . getS ( 'keeptrakt' )
I1IIiiIiii = wiz . getS ( 'keepdebrid' )
O000oo0O = wiz . getS ( 'keeplogin' )
OOOOi11i1 = wiz . getS ( 'loginlastsave' )
IIIii1II1II = wiz . getS ( 'exodus' )
i1I1iI = wiz . getS ( 'salts' )
oo0OooOOo0 = wiz . getS ( 'saltshd' )
o0OO00oO = wiz . getS ( 'royalwe' )
I11i1I1I = wiz . getS ( 'velocity' )
oO0Oo = wiz . getS ( 'velocitykids' )
oOOoo0Oo = wiz . getS ( 'specto' )
o00OO00OoO = wiz . getS ( 'trakt' )
OOOO0OOoO0O0 = wiz . getS ( 'realexodus' )
O0Oo000ooO00 = wiz . getS ( 'realspecto' )
oO0 = wiz . getS ( 'urlresolver' )
Ii1iIiII1ii1 = wiz . getS ( 'developer' )
ooOooo000oOO = O0O0OO0O0O0 . getSetting ( 'path' ) if not O0O0OO0O0O0 . getSetting ( 'path' ) == '' else 'special://home/'
Oo0oOOo = os . path . join ( ooOooo000oOO , 'My_Builds' , '' )
O0OoO000O0OO = int ( float ( O0OoO000O0OO ) ) if O0OoO000O0OO . isdigit ( ) else 0
Oo0OoO00oOO0o = date . today ( )
OOO00O = Oo0OoO00oOO0o + timedelta ( days = 1 )
OOoOO0oo0ooO = Oo0OoO00oOO0o + timedelta ( days = 3 )
O0o0O00Oo0o0 = float ( xbmc . getInfoLabel ( "System.BuildVersion" ) [ : 4 ] )
O00O0oOO00O00 = "Kodi"
i1Oo00 = 'plugin.video.exodus'
i1i = 'plugin.video.velocity'
iiI111I1iIiI = 'plugin.video.velocitykids'
IIIi1I1IIii1II = 'plugin.video.salts'
O0 = 'plugin.video.saltshd.lite'
ii1ii1ii = 'plugin.video.theroyalwe'
oooooOoo0ooo = 'plugin.video.specto'
I1I1IiI1 = 'script.trakt'
III1iII1I1ii = 'script.module.urlresolver'
oOOo0 = os . path . join ( IiI , IIIi1I1IIii1II )
oo00O00oO = os . path . join ( IiI , O0 )
iIiIIIi = os . path . join ( IiI , i1Oo00 )
ooo00OOOooO = os . path . join ( IiI , i1i )
O00OOOoOoo0O = os . path . join ( IiI , iiI111I1iIiI )
O000OOo00oo = os . path . join ( IiI , ii1ii1ii )
oo0OOo = os . path . join ( IiI , oooooOoo0ooo )
ooOOO00Ooo = os . path . join ( IiI , I1I1IiI1 )
IiIIIi1iIi = os . path . join ( IiI , III1iII1I1ii )
ooOOoooooo = [ OO0o , 'repository.SpinzTV' , 'plugin.video.spinztvwiz' , 'plugin.video.spinz' , 'script.xtcodes.installer' ]
# 0 being every startup of kodi
II1I = 0
O0i1II1Iiii1I11 = Oo0OoO00oOO0o + timedelta ( days = II1I )
if 9 - 9: OoOooO / O000oo . Oo0O00O0O / OooOoooOo - I1 + OOO00O0O
iii = ''
if 90 - 90: oOOO % iII1Ii . I1I11
II1o0oO00000 = 'No'
OOOOoo0Oo = 'SpinzTV'
if 14 - 14: o00oO0oOo00
oO0oOo0 = 'No'
if 45 - 45: oO00OoOO000o / Oo00o0o0 / IIIi . I1Ii
O0oo00o0O = 'Thank you for choosing SpinzTV.\r\n\r\nContact us on facebook at http://facebook.com/groups/spinztv\r\n\r\nWebsite: www.spinztv.com'
if 1 - 1: I1IiiiiI
o0OIiII = 'No'
ii1iII1II = 'deepskyblue'
Iii1I1I11iiI1 = 'white'
I1I1i1I = '[COLOR ' + ii1iII1II + ']%s[/COLOR]'
ii1I = '[COLOR ' + Iii1I1I11iiI1 + ']%s[/COLOR]'
O0oO0 = '[COLOR ' + ii1iII1II + ']%s[/COLOR]'
oO0O0OO0O = '[COLOR ' + ii1iII1II + ']Current Build:[/COLOR] [COLOR ' + Iii1I1I11iiI1 + ']%s[/COLOR]'
OO = '[COLOR ' + ii1iII1II + ']Current Theme:[/COLOR] [COLOR ' + Iii1I1I11iiI1 + ']%s[/COLOR]'
OoOoO = 'No'
Ii1I1i = os . path . join ( i1 , 'mainticon.png' )
OOI1iI1ii1II = os . path . join ( i1 , 'buildsicon.png' )
O0O0OOOOoo = os . path . join ( i1 , 'contacticon.png' )
oOooO0 = os . path . join ( i1 , 'apkicon.png' )
Ii1I1Ii = os . path . join ( i1 , 'saveicon.png' )
OOoO0 = os . path . join ( i1 , 'trakticon.png' )
OO0Oooo0oOO0O = os . path . join ( i1 , 'realicon.png' )
o00O0 = os . path . join ( i1 , 'settingsicon.png' )
oOO0O00Oo0O0o = os . path . join ( i1 , 'spinzicon.png' )
ii1 = os . path . join ( i1 , 'kodiicon.png' )
I1iIIiiIIi1i = os . path . join ( i1 , 'kodiicon.png' )
O0O0ooOOO = os . path . join ( i1 , 'gamesicon.png' )
oOOo0O00o = os . path . join ( i1 , 'moviesicon.png' )
iIiIi11 = os . path . join ( i1 , 'droidicon.png' )
OOO = os . path . join ( i1 , 'speedicon.png' )
iiiiI = os . path . join ( i1 , 'spinzicon.png' )
oooOo0OOOoo0 = os . path . join ( i1 , 'spinzicon.png' )
OOoO = os . path . join ( i1 , 'spinzicon.png' )
OO0O000 = wiz . LOGFILES
iiIiI1i1 = traktit . TRAKTID
oO0O00oOOoooO = debridit . DEBRIDID
IiIi11iI = loginit . LOGINID
Oo0O00O000 = 'http://tribeca.tvaddons.ag/tools/maintenance/modules/'
if 3 - 3: O0OoOO0o * Iii % I1111i
if 14 - 14: Oo0OO / I1IiiiiI
if 73 - 73: Oo00o0o0 % OooOoooOo / OooOoooOo - Oo0OO
if 30 - 30: I1Ii / OOO00O0O
Iii1I1111ii = base64 . b64decode ( 'aHR0cDovL3NwZXoudHYvc3Bpbnovd2l6YXJkdHh0L3NwaW56d2l6YXJkMS50eHQ=' )
ooOoO00 = base64 . b64decode ( 'aHR0cDovL3NwZXoudHYvc3Bpbnovc3BlZWQvc3BlZWR0ZXN0LnR4dA==' )
Ii1IIiI1i = base64 . b64decode ( 'aHR0cDovL3NwZXoudHYvc3BpbnovYXBrdHh0cy9TcGluemFway50eHQ=' )
o0O00Oo0 = base64 . b64decode ( 'aHR0cDovL3NwZXoudHYvc3BpbnovdmlkZW90eHRzL2J1aWxkdmlkcy50eHQ=' )
if 33 - 33: OoOooO * o00oO0oOo00 - I1111i % I1111i
I11I = base64 . b64decode ( 'aHR0cDovL2FmdGVybWF0aHdpemFyZC5uZXQvcmVwby93aXphcmQvYWRkb25zLnR4dA==' )
if 50 - 50: I1111i * i11iIiiIii * O000oo - I1 * o00oO0oOo00 * I1I11
OoooOoo = 'http://'
O0o000Oo = base64 . b64decode ( 'aHR0cDovL3NwZXoudHYvc3BpbnovYXBrdHh0cy9TcGluelRWLWFway50eHQ=' )
ooo = base64 . b64decode ( 'aHR0cDovL3NwZXoudHYvc3BpbnovYXBrdHh0cy94eHhhcGtzLnR4dA==' )
i1i1iI1iiiI = base64 . b64decode ( 'aHR0cDovL3NwZXoudHYvc3BpbnovZW11bGF0b3Itcm9tdHh0L1JPTVNUWFQvU05FUy50eHQ=' )
Ooo0oOooo0 = base64 . b64decode ( 'aHR0cDovL3NwZXoudHYvc3BpbnovZW11bGF0b3Itcm9tdHh0L2VtdWxhdG9yLnR4dA==' )
oOOOoo00 = base64 . b64decode ( 'aHR0cDovL3NwZXoudHYvc3BpbnovZW11bGF0b3Itcm9tdHh0L1JPTVNUWFQvU05FU0EtQi50eHQ=' )
iiIiIIIiiI = base64 . b64decode ( 'aHR0cDovL3NwZXoudHYvc3BpbnovZW11bGF0b3Itcm9tdHh0L1JPTVNUWFQvU05FU0MtRS50eHQ=' )
iiI1IIIi = base64 . b64decode ( 'aHR0cDovL3NwZXoudHYvc3BpbnovZW11bGF0b3Itcm9tdHh0L1JPTVNUWFQvU05FU0YtSC50eHQ=' )
II11IiIi11 = base64 . b64decode ( 'aHR0cDovL3NwZXoudHYvc3BpbnovZW11bGF0b3Itcm9tdHh0L1JPTVNUWFQvU05FU0ktSy50eHQ=' )
IIOOO0O00O0OOOO = base64 . b64decode ( 'aHR0cDovL3NwZXoudHYvc3BpbnovZW11bGF0b3Itcm9tdHh0L1JPTVNUWFQvU05FU0wtTS50eHQ=' )
I1iiii1I = base64 . b64decode ( 'aHR0cDovL3NwZXoudHYvc3BpbnovZW11bGF0b3Itcm9tdHh0L1JPTVNUWFQvU05FU04tTy50eHQ=' )
OOo0 = base64 . b64decode ( 'aHR0cDovL3NwZXoudHYvc3BpbnovZW11bGF0b3Itcm9tdHh0L1JPTVNUWFQvU05FU1AtUi50eHQ=' )
oO00ooooO0o = base64 . b64decode ( 'aHR0cDovL3NwZXoudHYvc3BpbnovZW11bGF0b3Itcm9tdHh0L1JPTVNUWFQvU05FU1MudHh0' )
oo0o = base64 . b64decode ( 'aHR0cDovL3NwZXoudHYvc3BpbnovZW11bGF0b3Itcm9tdHh0L1JPTVNUWFQvU05FU1QtVi50eHQ=' )
o0oO0oooOoo = base64 . b64decode ( 'aHR0cDovL3NwZXoudHYvc3BpbnovZW11bGF0b3Itcm9tdHh0L1JPTVNUWFQvU05FU1ctWi50eHQ=' )
I1III1111iIi = base64 . b64decode ( 'aHR0cDovL3NwZXoudHYvc3BpbnovZW11bGF0b3Itcm9tdHh0L1JPTVNUWFQvTkVTQS1CLnR4dA==' )
I1i111I = base64 . b64decode ( 'aHR0cDovL3NwZXoudHYvc3BpbnovZW11bGF0b3Itcm9tdHh0L1JPTVNUWFQvTkVTQy50eHQ=' )
Ooo = base64 . b64decode ( 'aHR0cDovL3NwZXoudHYvc3BpbnovZW11bGF0b3Itcm9tdHh0L1JPTVNUWFQvTkVTRC1FLnR4dA==' )
Oo0oo0O0o00O = base64 . b64decode ( 'aHR0cDovL3NwZXoudHYvc3BpbnovZW11bGF0b3Itcm9tdHh0L1JPTVNUWFQvTkVTRi1HLnR4dA==' )
I1i11 = base64 . b64decode ( 'aHR0cDovL3NwZXoudHYvc3BpbnovZW11bGF0b3Itcm9tdHh0L1JPTVNUWFQvTkVTSC1LLnR4dA==' )
IiIi1I1 = base64 . b64decode ( 'aHR0cDovL3NwZXoudHYvc3BpbnovZW11bGF0b3Itcm9tdHh0L1JPTVNUWFQvTkVTTC1NLnR4dA==' )
IiIIi1 = base64 . b64decode ( 'aHR0cDovL3NwZXoudHYvc3BpbnovZW11bGF0b3Itcm9tdHh0L1JPTVNUWFQvTkVTTi1RLnR4dA==' )
IIIIiii1IIii = base64 . b64decode ( 'aHR0cDovL3NwZXoudHYvc3BpbnovZW11bGF0b3Itcm9tdHh0L1JPTVNUWFQvTkVTUi1TLnR4dA==' )
II1i11I = base64 . b64decode ( 'aHR0cDovL3NwZXoudHYvc3BpbnovZW11bGF0b3Itcm9tdHh0L1JPTVNUWFQvTkVTVC1WLnR4dA==' )
ii1I1IIii11 = base64 . b64decode ( 'aHR0cDovL3NwZXoudHYvc3BpbnovZW11bGF0b3Itcm9tdHh0L1JPTVNUWFQvTkVTVy1aLnR4dA==' )
O0o0oO = base64 . b64decode ( 'aHR0cDovL3NwZXoudHYvc3BpbnovZW11bGF0b3Itcm9tdHh0L1JPTVNUWFQvR0VOQS1CLnR4dA==' )
IIIIiIiIi1 = base64 . b64decode ( 'aHR0cDovL3NwZXoudHYvc3BpbnovZW11bGF0b3Itcm9tdHh0L1JPTVNUWFQvR0VOQy1ELnR4dA==' )
I11iiiiI1i = base64 . b64decode ( 'aHR0cDovL3NwZXoudHYvc3BpbnovZW11bGF0b3Itcm9tdHh0L1JPTVNUWFQvR0VORS1HLnR4dA==' )
iI1i11 = base64 . b64decode ( 'aHR0cDovL3NwZXoudHYvc3BpbnovZW11bGF0b3Itcm9tdHh0L1JPTVNUWFQvR0VOSC1MLnR4dA==' )
OoOOoooOO0O = base64 . b64decode ( 'aHR0cDovL3NwZXoudHYvc3BpbnovZW11bGF0b3Itcm9tdHh0L1JPTVNUWFQvR0VOTS1PLnR4dA==' )
ooo00Ooo = base64 . b64decode ( 'aHR0cDovL3NwZXoudHYvc3BpbnovZW11bGF0b3Itcm9tdHh0L1JPTVNUWFQvR0VOUC1SLnR4dA==' )
Oo0o0O00 = base64 . b64decode ( 'aHR0cDovL3NwZXoudHYvc3BpbnovZW11bGF0b3Itcm9tdHh0L1JPTVNUWFQvR0VOUy1ULnR4dA==' )
ii1I1i11 = base64 . b64decode ( 'aHR0cDovL3NwZXoudHYvc3BpbnovZW11bGF0b3Itcm9tdHh0L1JPTVNUWFQvR0VOVS1aLnR4dA==' )
OOo0O0oo0OO0O = base64 . b64decode ( 'aHR0cDovL3NwZXoudHYvc3BpbnovZW11bGF0b3Itcm9tdHh0L1JPTVNUWFQvQVRSQS1CLnR4dA==' )
OO0 = base64 . b64decode ( 'aHR0cDovL3NwZXoudHYvc3BpbnovZW11bGF0b3Itcm9tdHh0L1JPTVNUWFQvQVRSQy1ELnR4dA==' )
o0Oooo = base64 . b64decode ( 'aHR0cDovL3NwZXoudHYvc3BpbnovZW11bGF0b3Itcm9tdHh0L1JPTVNUWFQvQVRSRS1HLnR4dA==' )
iiI = base64 . b64decode ( 'aHR0cDovL3NwZXoudHYvc3BpbnovZW11bGF0b3Itcm9tdHh0L1JPTVNUWFQvQVRSSC1MLnR4dA==' )
oOIIiIi = base64 . b64decode ( 'aHR0cDovL3NwZXoudHYvc3BpbnovZW11bGF0b3Itcm9tdHh0L1JPTVNUWFQvQVRSTS1PLnR4dA==' )
OOoOooOoOOOoo = base64 . b64decode ( 'aHR0cDovL3NwZXoudHYvc3BpbnovZW11bGF0b3Itcm9tdHh0L1JPTVNUWFQvQVRSUC1SLnR4dA==' )
Iiii1iI1i = base64 . b64decode ( 'aHR0cDovL3NwZXoudHYvc3BpbnovZW11bGF0b3Itcm9tdHh0L1JPTVNUWFQvQVRSUy1VLnR4dA==' )
I1ii1ii11i1I = base64 . b64decode ( 'aHR0cDovL3NwZXoudHYvc3BpbnovZW11bGF0b3Itcm9tdHh0L1JPTVNUWFQvQVRSVi1aLnR4dA==' )
o0OoOO = base64 . b64decode ( 'aHR0cDovL3NwZXoudHYvc3BpbnovZW11bGF0b3Itcm9tdHh0L1JPTVNUWFQvTjY0LnR4dA==' )
O0O0Oo00 = base64 . b64decode ( 'aHR0cDovL3NwZXoudHYvc3BpbnovZW11bGF0b3Itcm9tdHh0L1JPTVNUWFQvTjY0QS1CLnR4dA==' )
oOoO00o = base64 . b64decode ( 'aHR0cDovL3NwZXoudHYvc3BpbnovZW11bGF0b3Itcm9tdHh0L1JPTVNUWFQvTjY0Qy1FLnR4dA==' )
oO00O0 = base64 . b64decode ( 'aHR0cDovL3NwZXoudHYvc3BpbnovZW11bGF0b3Itcm9tdHh0L1JPTVNUWFQvTjY0Ri1KLnR4dA==' )
IIi1IIIi = base64 . b64decode ( 'aHR0cDovL3NwZXoudHYvc3BpbnovZW11bGF0b3Itcm9tdHh0L1JPTVNUWFQvTjY0Sy1NLnR4dA==' )
O00Ooo = base64 . b64decode ( 'aHR0cDovL3NwZXoudHYvc3BpbnovZW11bGF0b3Itcm9tdHh0L1JPTVNUWFQvTjY0Ti1SLnR4dA==' )
OOOO0OOO = base64 . b64decode ( 'aHR0cDovL3NwZXoudHYvc3BpbnovZW11bGF0b3Itcm9tdHh0L1JPTVNUWFQvTjY0Uy1ULnR4dA==' )
i1i1ii = base64 . b64decode ( 'aHR0cDovL3NwZXoudHYvc3BpbnovZW11bGF0b3Itcm9tdHh0L1JPTVNUWFQvTjY0Vi1aLnR4dA==' )
iII1ii1 = base64 . b64decode ( 'aHR0cDovL3NwZXoudHYvc3BpbnovZW11bGF0b3Itcm9tdHh0L1JPTVNUWFQvVEdBLUIudHh0' )
I1i1iiiI1 = base64 . b64decode ( 'aHR0cDovL3NwZXoudHYvc3BpbnovZW11bGF0b3Itcm9tdHh0L1JPTVNUWFQvVEdDLUUudHh0' )
iIIi = base64 . b64decode ( 'aHR0cDovL3NwZXoudHYvc3BpbnovZW11bGF0b3Itcm9tdHh0L1JPTVNUWFQvVEdGLUkudHh0' )
oO0o00oo0 = base64 . b64decode ( 'aHR0cDovL3NwZXoudHYvc3BpbnovZW11bGF0b3Itcm9tdHh0L1JPTVNUWFQvVEdKLU0udHh0' )
ii1IIII = base64 . b64decode ( 'aHR0cDovL3NwZXoudHYvc3BpbnovZW11bGF0b3Itcm9tdHh0L1JPTVNUWFQvVEdOLVEudHh0' )
oO00oOooooo0 = base64 . b64decode ( 'aHR0cDovL3NwZXoudHYvc3BpbnovZW11bGF0b3Itcm9tdHh0L1JPTVNUWFQvVEdSLVUudHh0' )
oOo = base64 . b64decode ( 'aHR0cDovL3NwZXoudHYvc3BpbnovZW11bGF0b3Itcm9tdHh0L1JPTVNUWFQvVEdWLVoudHh0' )
O0OOooOoO = base64 . b64decode ( 'aHR0cDovL3NwZXoudHYvc3BpbnovZW11bGF0b3Itcm9tdHh0L1JPTVNUWFQvTkRTQS50eHQ=' )
i1II1I1Iii1 = base64 . b64decode ( 'aHR0cDovL3NwZXoudHYvc3BpbnovZW11bGF0b3Itcm9tdHh0L1JPTVNUWFQvTkRTQi50eHQ=' )
iiI11Iii = base64 . b64decode ( 'aHR0cDovL3NwZXoudHYvc3BpbnovZW11bGF0b3Itcm9tdHh0L1JPTVNUWFQvTkRTQy50eHQ=' )
O0o0O0 = base64 . b64decode ( 'aHR0cDovL3NwZXoudHYvc3BpbnovZW11bGF0b3Itcm9tdHh0L1JPTVNUWFQvTkRTRC50eHQ=' )
Ii1II1I11i1 = base64 . b64decode ( 'aHR0cDovL3NwZXoudHYvc3BpbnovZW11bGF0b3Itcm9tdHh0L1JPTVNUWFQvTkRTRS1GLnR4dA==' )
oOoooooOoO = base64 . b64decode ( 'aHR0cDovL3NwZXoudHYvc3BpbnovZW11bGF0b3Itcm9tdHh0L1JPTVNUWFQvTkRTRy1ILnR4dA==' )
Ii111 = base64 . b64decode ( 'aHR0cDovL3NwZXoudHYvc3BpbnovZW11bGF0b3Itcm9tdHh0L1JPTVNUWFQvTkRTSS1KLnR4dA==' )
I111i1i1111 = base64 . b64decode ( 'aHR0cDovL3NwZXoudHYvc3BpbnovZW11bGF0b3Itcm9tdHh0L1JPTVNUWFQvTkRTSy1MLnR4dA==' )
IIII1 = base64 . b64decode ( 'aHR0cDovL3NwZXoudHYvc3BpbnovZW11bGF0b3Itcm9tdHh0L1JPTVNUWFQvTkRTTS50eHQ=' )
I1I1i = base64 . b64decode ( 'aHR0cDovL3NwZXoudHYvc3BpbnovZW11bGF0b3Itcm9tdHh0L1JPTVNUWFQvTkRTTi1PLnR4dA==' )
I1IIIiIiIi = base64 . b64decode ( 'aHR0cDovL3NwZXoudHYvc3BpbnovZW11bGF0b3Itcm9tdHh0L1JPTVNUWFQvTkRTUC1RLnR4dA==' )
IIIII1 = base64 . b64decode ( 'aHR0cDovL3NwZXoudHYvc3BpbnovZW11bGF0b3Itcm9tdHh0L1JPTVNUWFQvTkRTUi50eHQ=' )
iIi1Ii1i1iI = base64 . b64decode ( 'aHR0cDovL3NwZXoudHYvc3BpbnovZW11bGF0b3Itcm9tdHh0L1JPTVNUWFQvTkRTUy50eHQ=' )
IIiI1 = base64 . b64decode ( 'aHR0cDovL3NwZXoudHYvc3BpbnovZW11bGF0b3Itcm9tdHh0L1JPTVNUWFQvTkRTVC1VLnR4dA==' )
i1iI1 = base64 . b64decode ( 'aHR0cDovL3NwZXoudHYvc3BpbnovZW11bGF0b3Itcm9tdHh0L1JPTVNUWFQvTkRTVi1aLnR4dA==' )
ii1I1IiiI1ii1i = base64 . b64decode ( 'aHR0cDovL3NwZXoudHYvc3BpbnovZW11bGF0b3Itcm9tdHh0L1JPTVNUWFQvUFNBLnR4dA==' )
O0o = base64 . b64decode ( 'aHR0cDovL3NwZXoudHYvc3BpbnovZW11bGF0b3Itcm9tdHh0L1JPTVNUWFQvUFNCLnR4dA==' )
oO0OoO00o = base64 . b64decode ( 'aHR0cDovL3NwZXoudHYvc3BpbnovZW11bGF0b3Itcm9tdHh0L1JPTVNUWFQvUFNDLUQudHh0' )
II1iiiiII = base64 . b64decode ( 'aHR0cDovL3NwZXoudHYvc3BpbnovZW11bGF0b3Itcm9tdHh0L1JPTVNUWFQvUFNFLUYudHh0' )
O0OoOO0oo0 = base64 . b64decode ( 'aHR0cDovL3NwZXoudHYvc3BpbnovZW11bGF0b3Itcm9tdHh0L1JPTVNUWFQvUFNHLUoudHh0' )
oOO = base64 . b64decode ( 'aHR0cDovL3NwZXoudHYvc3BpbnovZW11bGF0b3Itcm9tdHh0L1JPTVNUWFQvUFNLLU4udHh0' )
O0o0OO0000ooo = base64 . b64decode ( 'aHR0cDovL3NwZXoudHYvc3BpbnovZW11bGF0b3Itcm9tdHh0L1JPTVNUWFQvUFNPLVIudHh0' )
iIIII1iIIii = base64 . b64decode ( 'aHR0cDovL3NwZXoudHYvc3BpbnovZW11bGF0b3Itcm9tdHh0L1JPTVNUWFQvUFNTLVQudHh0' )
oOOO00o000o = base64 . b64decode ( 'aHR0cDovL3NwZXoudHYvc3BpbnovZW11bGF0b3Itcm9tdHh0L1JPTVNUWFQvUFNVLVoudHh0' )
if 9 - 9: Oo00o0o0 + I1Ii / I1Ii
if 12 - 12: Oo0O00O0O % o00oO0oOo00 * I1Ii % O000oo / I1IiiiiI
if 27 - 27: i11iIiiIii % I1 % I1Ii . OoOooO - oOOO + I1I11
ooO0o = wiz . workingURL ( Iii1I1111ii )
if 51 - 51: Iii
if 25 - 25: Oo0O00O0O + Iii * oO00OoOO000o
if 92 - 92: OOO00O0O + I1Ii + OoOooO / o00oO0oOo00 + I1111i
if 18 - 18: Oo0OO * I1I11 . O0OoOO0o / oO00OoOO000o / i11iIiiIii
if 21 - 21: Oo00o0o0 / oO00OoOO000o + I1IiiiiI + Oo0O00O0O
if 91 - 91: i11iIiiIii / OooOoooOo + O0OoOO0o + Oo0OO * i11iIiiIii
if 66 - 66: O000oo % OooOoooOo - OoOooO + I1Ii * I1111i . Iii
if 52 - 52: Oo0OO + OoOooO . O0OoOO0o . oO00OoOO000o . iII1Ii
if 97 - 97: OOO00O0O / O0OoOO0o
def Oooo0 ( ) :
 if OoOoO == 'Yes' :
  if wiz . workingURL ( WIZARDFILE ) == True :
   oOOOooo = wiz . checkWizard ( 'version' )
   if oOOOooo > O00ooooo00 : I1i1iiiII1i ( '%s [v%s] [COLOR red][B][UPDATE v%s][/B][/COLOR]' % ( Oo0Ooo , O00ooooo00 , oOOOooo ) , 'wizardupdate' , themeit = ii1I )
   else : I1i1iiiII1i ( '%s [v%s]' % ( Oo0Ooo , O00ooooo00 ) , '' , themeit = ii1I )
  else : I1i1iiiII1i ( '%s [v%s]' % ( Oo0Ooo , O00ooooo00 ) , '' , themeit = ii1I )
 else : I1i1iiiII1i ( '%s [v%s]' % ( Oo0Ooo , O00ooooo00 ) , '' , themeit = ii1I )
 if len ( i11 ) > 0 :
  oO0oO0 = wiz . checkBuild ( i11 , 'version' )
  i1i1IIIIi1i = '%s (v%s)' % ( i11 , oO0o0o0ooO0oO )
  if oO0oO0 > oO0o0o0ooO0oO : i1i1IIIIi1i = '%s [COLOR red][B][UPDATE v%s][/B][/COLOR]' % ( i1i1IIIIi1i , oO0oO0 )
  Ii11iiI ( i1i1IIIIi1i , 'viewbuild' , i11 , themeit = oO0O0OO0O )
  IIi1iiii1iI = wiz . checkBuild ( i11 , 'theme' )
  if not IIi1iiii1iI == 'http://' and wiz . workingURL ( IIi1iiii1iI ) == True :
   I1i1iiiII1i ( 'None' if oo0o0O00 == "" else oo0o0O00 , 'theme' , i11 , themeit = OO )
 else : Ii11iiI ( 'None' , 'builds' , themeit = oO0O0OO0O )
 if o0OIiII == 'No' : I1i1iiiII1i ( '============================================' , '' , themeit = O0oO0 )
 Ii11iiI ( 'SpinzTV Builds' , 'builds' , icon = OOI1iI1ii1II , themeit = I1I1i1I )
 Ii11iiI ( 'Maintenance' , 'maint' , icon = Ii1I1i , themeit = I1I1i1I )
 I1i1iiiII1i ( 'Speed Test' , 'speed' , icon = OOO , themeit = I1I1i1I )
 Ii11iiI ( 'Android Zone' , 'apk1' , icon = oOooO0 , themeit = I1I1i1I )
 if not I11I == 'http://' : iIiiii ( 'Addon Installer' , 'addons' , icon = iiiiI , themeit = I1I1i1I )
 Ii11iiI ( 'Save Data' , 'savedata' , icon = Ii1I1Ii , themeit = I1I1i1I )
 if oO0oOo0 == 'No' : I1i1iiiII1i ( 'Contact' , 'contact' , icon = O0O0OOOOoo , themeit = I1I1i1I )
 if o0OIiII == 'No' : I1i1iiiII1i ( '============================================' , '' , themeit = O0oO0 )
 I1i1iiiII1i ( 'Settings' , 'settings' , icon = o00O0 , themeit = I1I1i1I )
 if Ii1iIiII1ii1 == 'true' : Ii11iiI ( 'Developer Menu' , 'developer' , icon = o00O0 , themeit = I1I1i1I )
 O0000OOO0 ( 'movies' , 'MAIN' )
 if 51 - 51: OOO00O0O / Iii / I1IiiiiI
 if 6 - 6: I1IiiiiI - Oo0OO * IIIi . O0OoOO0o / OoOooO * Oo0OO
 if 22 - 22: oOOO % O0OoOO0o * oO00OoOO000o / IIIi % i11iIiiIii * I1Ii
 if 95 - 95: Oo0O00O0O - Iii * OOO00O0O + I1I11
def iIi1 ( ) :
 ooO0o = wiz . workingURL ( Iii1I1111ii )
 if not ooO0o == True :
  i11iiI1111 ( '%s Version: %s' % ( O00O0oOO00O00 , O0o0O00Oo0o0 ) , '' , icon = OOI1iI1ii1II , themeit = O0oO0 )
  if o0OIiII == 'No' : I1i1iiiII1i ( wiz . sep ( ) , '' , themeit = O0oO0 )
  i11iiI1111 ( 'Url for txt file not valid' , '' , icon = OOI1iI1ii1II , themeit = O0oO0 )
  i11iiI1111 ( '%s' % ooO0o , '' , icon = OOI1iI1ii1II , themeit = O0oO0 )
 else :
  oOoooo000Oo00 = wiz . openURL ( Iii1I1111ii ) . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' ) . replace ( 'gui=""' , 'gui="http://"' ) . replace ( 'theme=""' , 'theme="http://"' )
  OOoo = re . compile ( 'name="(.+?)".+?ersion="(.+?)".+?rl="(.+?)".+?ui="(.+?)".+?odi="(.+?)".+?heme="(.+?)".+?con="(.+?)".+?anart="(.+?)".+?dult="(.+?)".+?escription="(.+?)"' ) . findall ( oOoooo000Oo00 )
  if len ( OOoo ) == 1 :
   o00O00oO00 ( OOoo [ 0 ] [ 0 ] )
  elif len ( OOoo ) > 1 :
   i11iiI1111 ( '[B]%s Version: %s[/B]' % ( O00O0oOO00O00 , O0o0O00Oo0o0 ) , '' , icon = OOI1iI1ii1II , themeit = ii1I )
   Ii11iiI ( 'Video Preview Of Builds' , 'youtube' , url = o0O00Oo0 , icon = oOO0O00Oo0O0o , themeit = I1I1i1I )
   iIiiii ( 'Save Data Menu' , 'savedata' , icon = Ii1I1Ii , themeit = O0oO0 )
   if o0OIiII == 'No' : I1i1iiiII1i ( wiz . sep ( ) , '' , themeit = O0oO0 )
   if o0 == 'true' :
    for Ii1i1i1i1I1Ii , oO0oO0 , iiiI1 , OOOoO0O , o0iiiI1I1iIIIi1 , IiiI1iiiiI1iI , iIiiiii1i , iiIi1IIiI , i1oO0OO0 , o0O0Oo00 in OOoo :
     if not i1iIIi1 == 'true' and i1oO0OO0 . lower ( ) == 'yes' : continue
     O0Oo0o000oO = oO0o00oOOooO0 ( 'install' , '' , Ii1i1i1i1I1Ii )
     iIiiii ( '[%s] %s (v%s)' % ( float ( o0iiiI1I1iIIIi1 ) , Ii1i1i1i1I1Ii , oO0oO0 ) , 'viewbuild' , Ii1i1i1i1I1Ii , description = o0O0Oo00 , fanart = iiIi1IIiI , icon = iIiiiii1i , menu = O0Oo0o000oO , themeit = ii1I )
   else :
    OOOoO000 = wiz . buildCount ( '15' ) ; oOOOO = wiz . buildCount ( '16' ) ; Ii = wiz . buildCount ( '17' ) ;
    if Ii > 0 :
     Ii1ii111i1 = '+' if i1iiIII111ii == 'false' else '-'
     i11iiI1111 ( '[B]%s Krypton Builds(%s)[/B]' % ( Ii1ii111i1 , oOOOO ) , 'togglesetting' , 'show17' , themeit = O0oO0 )
     if i1iiIII111ii == 'true' :
      for Ii1i1i1i1I1Ii , oO0oO0 , iiiI1 , OOOoO0O , o0iiiI1I1iIIIi1 , IiiI1iiiiI1iI , iIiiiii1i , iiIi1IIiI , i1oO0OO0 , o0O0Oo00 in OOoo :
       if not i1iIIi1 == 'true' and i1oO0OO0 . lower ( ) == 'yes' : continue
       i1i1i1I = int ( float ( o0iiiI1I1iIIIi1 ) )
       if i1i1i1I == 17 :
        O0Oo0o000oO = oO0o00oOOooO0 ( 'install' , '' , Ii1i1i1i1I1Ii )
        iIiiii ( '[%s] %s (v%s)' % ( float ( o0iiiI1I1iIIIi1 ) , Ii1i1i1i1I1Ii , oO0oO0 ) , 'viewbuild' , Ii1i1i1i1I1Ii , description = o0O0Oo00 , fanart = iiIi1IIiI , icon = iIiiiii1i , menu = O0Oo0o000oO , themeit = ii1I )
    if oOOOO > 0 :
     Ii1ii111i1 = '+' if oooOOOOO == 'false' else '-'
     i11iiI1111 ( '[B]%s Jarvis Builds(%s)[/B]' % ( Ii1ii111i1 , oOOOO ) , 'togglesetting' , 'show16' , themeit = O0oO0 )
     if oooOOOOO == 'true' :
      for Ii1i1i1i1I1Ii , oO0oO0 , iiiI1 , OOOoO0O , o0iiiI1I1iIIIi1 , IiiI1iiiiI1iI , iIiiiii1i , iiIi1IIiI , i1oO0OO0 , o0O0Oo00 in OOoo :
       if not i1iIIi1 == 'true' and i1oO0OO0 . lower ( ) == 'yes' : continue
       i1i1i1I = int ( float ( o0iiiI1I1iIIIi1 ) )
       if i1i1i1I == 16 :
        O0Oo0o000oO = oO0o00oOOooO0 ( 'install' , '' , Ii1i1i1i1I1Ii )
        iIiiii ( '[%s] %s (v%s)' % ( float ( o0iiiI1I1iIIIi1 ) , Ii1i1i1i1I1Ii , oO0oO0 ) , 'viewbuild' , Ii1i1i1i1I1Ii , description = o0O0Oo00 , fanart = iiIi1IIiI , icon = iIiiiii1i , menu = O0Oo0o000oO , themeit = ii1I )
    if OOOoO000 > 0 :
     Ii1ii111i1 = '+' if i1iiIIiiI111 == 'false' else '-'
     I1i1iiiII1i ( '[B]%s Isengard and Below Builds(%s)[/B]' % ( Ii1ii111i1 , OOOoO000 ) , 'togglesetting' , 'show15' , themeit = O0oO0 )
     if i1iiIIiiI111 == 'true' :
      for Ii1i1i1i1I1Ii , oO0oO0 , iiiI1 , OOOoO0O , o0iiiI1I1iIIIi1 , IiiI1iiiiI1iI , iIiiiii1i , iiIi1IIiI , i1oO0OO0 , o0O0Oo00 in OOoo :
       if not i1iIIi1 == 'true' and i1oO0OO0 . lower ( ) == 'yes' : continue
       i1i1i1I = int ( float ( o0iiiI1I1iIIIi1 ) )
       if i1i1i1I <= 15 :
        O0Oo0o000oO = oO0o00oOOooO0 ( 'install' , '' , Ii1i1i1i1I1Ii )
        iIiiii ( '[%s] %s (v%s)' % ( float ( o0iiiI1I1iIIIi1 ) , Ii1i1i1i1I1Ii , oO0oO0 ) , 'viewbuild' , Ii1i1i1i1I1Ii , description = o0O0Oo00 , fanart = iiIi1IIiI , icon = iIiiiii1i , menu = O0Oo0o000oO , themeit = ii1I )
  else : I1i1iiiII1i ( 'Text file for builds not formated correctly.' , '' , icon = OOI1iI1ii1II , themeit = O0oO0 )
 O0000OOO0 ( 'files' , 'viewType' )
 if 83 - 83: Oo00o0o0 + Oo0O00O0O
def o00O00oO00 ( name ) :
 ooO0o = wiz . workingURL ( Iii1I1111ii )
 if not ooO0o == True :
  i11iiI1111 ( 'Url for txt file not valid' , '' , themeit = O0oO0 )
  i11iiI1111 ( '%s' % ooO0o , '' , themeit = O0oO0 )
  return
 if wiz . checkBuild ( name , 'version' ) == False :
  i11iiI1111 ( 'Error reading the txt file.' , '' , themeit = O0oO0 )
  i11iiI1111 ( '%s was not found in the builds list.' % name , '' , themeit = O0oO0 )
  return
 oOoooo000Oo00 = wiz . openURL ( Iii1I1111ii ) . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' ) . replace ( 'gui=""' , 'gui="http://"' ) . replace ( 'theme=""' , 'theme="http://"' )
 OOoo = re . compile ( 'name="%s".+?ersion="(.+?)".+?rl="(.+?)".+?ui="(.+?)".+?odi="(.+?)".+?heme="(.+?)".+?con="(.+?)".+?anart="(.+?)".+?dult="(.+?)".+?escription="(.+?)"' % name ) . findall ( oOoooo000Oo00 )
 for oO0oO0 , iiiI1 , OOOoO0O , o0iiiI1I1iIIIi1 , IIi1iiii1iI , iIiiiii1i , iiIi1IIiI , i1oO0OO0 , o0O0Oo00 in OOoo :
  iIiiiii1i = iIiiiii1i if wiz . workingURL ( iIiiiii1i ) else o0oOoO00o
  iiIi1IIiI = iiIi1IIiI if wiz . workingURL ( iiIi1IIiI ) else Oo0oO0ooo
  i1i1IIIIi1i = '%s (v%s)' % ( name , oO0oO0 )
  if i11 == name and oO0oO0 > oO0o0o0ooO0oO :
   i1i1IIIIi1i = '%s [COLOR red][CURRENT v%s][/COLOR]' % ( i1i1IIIIi1i , oO0o0o0ooO0oO )
  i11iiI1111 ( i1i1IIIIi1i , '' , description = o0O0Oo00 , fanart = iiIi1IIiI , icon = iIiiiii1i , themeit = oO0O0OO0O )
  if o0OIiII == 'No' : I1i1iiiII1i ( wiz . sep ( ) , '' , themeit = O0oO0 )
  i11iiI1111 ( 'Build Information' , 'buildinfo' , name , description = o0O0Oo00 , fanart = iiIi1IIiI , icon = iIiiiii1i , themeit = O0oO0 )
  iIiiii ( 'Save Data Menu' , 'savedata' , icon = Ii1I1Ii , themeit = O0oO0 )
  I111IiiIi1 = int ( float ( O0o0O00Oo0o0 ) ) ; o00o = int ( float ( o0iiiI1I1iIIIi1 ) )
  if not I111IiiIi1 == o00o :
   if I111IiiIi1 == 16 and o00o <= 15 : Ii1IIiiIIi = False
   else : Ii1IIiiIIi = True
  else : Ii1IIiiIIi = False
  if Ii1IIiiIIi == True :
   I1i1iiiII1i ( '[I]Build designed for kodi version %s(installed: %s)[/I]' % ( str ( o0iiiI1I1iIIIi1 ) , str ( O0o0O00Oo0o0 ) ) , '' , fanart = iiIi1IIiI , icon = iIiiiii1i , themeit = O0oO0 )
  i11iiI1111 ( wiz . sep ( 'INSTALL' ) , '' , fanart = iiIi1IIiI , icon = iIiiiii1i , themeit = O0oO0 )
  i11iiI1111 ( 'Fresh Install' , 'install' , name , 'fresh' , description = o0O0Oo00 , fanart = iiIi1IIiI , icon = iIiiiii1i , themeit = I1I1i1I )
  i11iiI1111 ( 'Standard Install' , 'install' , name , 'normal' , description = o0O0Oo00 , fanart = iiIi1IIiI , icon = iIiiiii1i , themeit = I1I1i1I )
  if not OOOoO0O == 'http://' : i11iiI1111 ( 'Apply guiFix' , 'install' , name , 'gui' , description = o0O0Oo00 , fanart = iiIi1IIiI , icon = iIiiiii1i , themeit = I1I1i1I )
  if not IIi1iiii1iI == 'http://' :
   if wiz . workingURL ( IIi1iiii1iI ) == True :
    i11iiI1111 ( wiz . sep ( 'THEMES' ) , '' , fanart = iiIi1IIiI , icon = iIiiiii1i , themeit = O0oO0 )
    oOoooo000Oo00 = wiz . openURL ( IIi1iiii1iI ) . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
    OOoo = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?con="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( oOoooo000Oo00 )
    for Oo000o , i11I1iIi , O0Oo , oOOOOoO00OoOO , o0O0Oo00 in OOoo :
     O0Oo = O0Oo if O0Oo == 'http://' else iIiiiii1i
     oOOOOoO00OoOO = oOOOOoO00OoOO if oOOOOoO00OoOO == 'http://' else iiIi1IIiI
     i11iiI1111 ( Oo000o if not Oo000o == oo0o0O00 else "[B]%s (Installed)[/B]" % Oo000o , 'theme' , name , Oo000o , description = o0O0Oo00 , fanart = oOOOOoO00OoOO , icon = O0Oo , themeit = O0oO0 )
 O0000OOO0 ( 'files' , 'viewType' )
 if 85 - 85: Oo00o0o0 - O000oo / OoOooO
 if 99 - 99: I1 * Iii % O000oo / I1IiiiiI
 if 90 - 90: Oo00o0o0 % IIIi - IIIi % I1 * iII1Ii
 if 39 - 39: I1Ii
 if 58 - 58: OooOoooOo % o00oO0oOo00
 if 79 - 79: o00oO0oOo00 % O0OoOO0o * Oo0O00O0O * O000oo . O0OoOO0o / I1IiiiiI
 if 19 - 19: OoOooO + I1Ii + I1IiiiiI / I1 / I1
 if 86 - 86: oO00OoOO000o * OoOooO * Iii
 if 51 - 51: I1 + Iii . OooOoooOo . oO00OoOO000o + I1I11 * OOO00O0O
 if 72 - 72: Oo00o0o0 + Oo00o0o0 / I1 . Oo0O00O0O % I1IiiiiI
 if 49 - 49: Oo00o0o0 . iII1Ii - oOOO * Oo0O00O0O . oOOO
 if 2 - 2: Oo0O00O0O % IIIi
 if 63 - 63: OOO00O0O % O000oo
 if 39 - 39: O0OoOO0o / I1 / oO00OoOO000o % OOO00O0O
 if 89 - 89: I1111i + Oo0O00O0O + I1111i * OooOoooOo + O000oo % I1Ii
 if 59 - 59: IIIi + i11iIiiIii
def oo0OOo0O ( ) :
 Ii11iiI ( 'Emulators And Roms' , 'emurom' , icon = O0O0ooOOO , themeit = I1I1i1I )
 Ii11iiI ( 'SpinzTV APKS' , 'apkshow' , url = Ii1IIiI1i , icon = oOO0O00Oo0O0o , themeit = I1I1i1I )
 Ii11iiI ( '[COLOR deepskyblue]APK Drawer[/COLOR]' , 'intellaunch' , )
 Ii11iiI ( 'Kodi and SPMC' , 'apkkodi' , icon = ii1 , themeit = I1I1i1I )
 Ii1IiII = I1i ( base64 . b64decode ( 'aHR0cHM6Ly93d3cuYXBrZmlsZXMuY29tLw==' ) )
 OOoo = re . compile ( 'href="([^"]*)">Applications(.+?)</a>' ) . findall ( Ii1IiII )
 oooii1iiIi1 = re . compile ( 'href="([^"]*)">Games(.+?)</a>' ) . findall ( Ii1IiII )
 for iiiI1 , i111iiI1ii in OOoo :
  IIiii ( '[COLOR deepskyblue]Android Apps[/COLOR]' + i111iiI1ii , 'https://www.apkfiles.com' + iiiI1 , 'apkgame' , i1 + 'apps.png' )
 for iiiI1 , i111iiI1ii in oooii1iiIi1 :
  IIiii ( '[COLOR deepskyblue]Android Games[/COLOR]' + i111iiI1ii , 'https://www.apkfiles.com' + iiiI1 , 'apkgame' , i1 + 'GAMES.png' )
 O0000OOO0 ( 'movies' , 'MAIN' )
 Ii11iiI ( 'Spinz Apk Picks' , 'apkshow' , url = O0o000Oo , icon = oOooO0 , themeit = I1I1i1I )
 if i1iIIi1 == 'true' : Ii11iiI ( 'XXX Apk' , 'apkshow' , url = ooo , icon = oOooO0 , themeit = I1I1i1I )
 if 30 - 30: I1Ii / I1IiiiiI . Iii . Oo0O00O0O - oOOO
def Ii1iI1iI11I1 ( url ) :
 if not I1i11iIIi11 ( url ) == True : return False
 oOoooo000Oo00 = I1i ( url ) . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
 OOoo = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?con="(.+?)".+?anart="(.+?)"' ) . findall ( oOoooo000Oo00 )
 if len ( OOoo ) > 0 :
  for Ii1i1i1i1I1Ii , url , iIiiiii1i , iiIi1IIiI in OOoo :
   I1i1iiiII1i ( Ii1i1i1i1I1Ii , 'apkinstall' , Ii1i1i1i1I1Ii , url , icon = iIiiiii1i , fanart = iiIi1IIiI , themeit = I1I1i1I )
  else : wiz . log ( "[APK Menu] ERROR: Invalid Format." )
 else : wiz . log ( "[APK Menu] ERROR: URL for emu list not working." )
 if 98 - 98: I1111i
def ii ( url ) :
 Ii1IiII = I1i ( url )
 OOoo = re . compile ( '<a href="([^"]*)" >(.+?)</a>' ) . findall ( Ii1IiII )
 for url , Ii1i1i1i1I1Ii in OOoo :
  if '/cat' in url :
   IIiii ( ( Ii1i1i1i1I1Ii ) . replace ( '&amp;' , ' - ' ) , 'https://www.apkfiles.com' + url , 'select' , i1 + 'APK.png' )
   if 32 - 32: I1IiiiiI % oO00OoOO000o - IIIi * o00oO0oOo00 + I1Ii
def II1IOoOo000oOo0oo ( url ) :
 Ii1IiII = I1i ( url )
 oO0O = url
 if "page=" in str ( url ) :
  oO0O = url . split ( '?' ) [ 0 ]
 OOoo = re . compile ( '<a href="([^"]*)".+?<img src="([^"]*)" class="file_list_icon".+?alt="([^"]*)"' , re . DOTALL ) . findall ( Ii1IiII )
 oooii1iiIi1 = re . compile ( 'class="[^"]*".+?ref="([^"]*)".+?yle=.+?</a>' ) . findall ( Ii1IiII )
 for url , oOOiiiIIiIi , Ii1i1i1i1I1Ii in OOoo :
  if 'apk' in url :
   IIiii ( ( Ii1i1i1i1I1Ii ) . replace ( '&#39;' , '' ) . replace ( '&amp;' , ' - ' ) . replace ( '&#174;:' , ': ' ) . replace ( '&#174;' , ' ' ) , 'https://www.apkfiles.com' + url , 'grab' , 'http:' + oOOiiiIIiIi )
 if len ( oooii1iiIi1 ) > 1 :
  oooii1iiIi1 = str ( oooii1iiIi1 [ len ( oooii1iiIi1 ) - 1 ] )
 IIiii ( 'Next Page' , oO0O + str ( oooii1iiIi1 ) , 'select' , i1 + 'Next.png' )
 if 68 - 68: OoOooO + I1I11 / Oo00o0o0 - IIIi + O000oo % I1IiiiiI
def i1iI1iii11i ( name , url ) :
 Ii1IiII = I1i ( url )
 name = name
 OOoo = re . compile ( 'href="([^"]*)".+?lass="yellow_button".+?itle=' ) . findall ( Ii1IiII )
 for url in OOoo :
  url = 'https://www.apkfiles.com' + url
  oOO00oO00O0OO ( name , url , 'Brackets' )
  if 96 - 96: I1I11
def o0OO0oO0oOO0O ( ) :
 I1i1iiiII1i ( 'Kodi (v%s)' % wiz . latestApk ( 'kodi' , 'version' ) , 'apkinstall' , 'kodi' , wiz . latestApk ( 'kodi' , 'url' ) , icon = ii1 , themeit = I1I1i1I )
 I1i1iiiII1i ( 'SPMC (v%s)' % wiz . latestApk ( 'spmc' , 'version' ) , 'apkinstall' , 'spmc' , wiz . latestApk ( 'spmc' , 'url' ) , icon = I1iIIiiIIi1i , themeit = I1I1i1I )
 if 39 - 39: I1IiiiiI * Oo0OO / I1I11 * iII1Ii . I1Ii % I1
 if 71 - 71: I1111i % OooOoooOo - I1 - IIIi + IIIi * Oo0OO
 if 51 - 51: O000oo / I1I11 + IIIi - I1Ii + O0OoOO0o
 if 29 - 29: o00oO0oOo00 % O000oo . Oo0O00O0O % Oo0O00O0O % I1 / O0OoOO0o
def oo0o0000Oo0 ( ) :
 if 80 - 80: I1111i - oOOO
 if os . path . isfile ( II1 ) :
  OOooO = True
  O00O0OO00oo = open ( II1 )
  oOOOooo0oooo0 = O00O0OO00oo . read ( )
  O00O0OO00oo . close ( )
 else :
  xbmcgui . Dialog ( ) . ok ( "[COLOR orange]SpinzTV[/COLOR]" , "[COLOR cyan][B]][[/B]NT3L[B]][[/B]G3NC[B]][[/B][/COLOR]" , "[COLOR ghostwhite]First Time Launching Will Take a Couple Minutes[/COLOR]" , "[COLOR ghostwhite]Please Be Patient![/COLOR]" )
  OOooO = False
  if 62 - 62: oO00OoOO000o + I1IiiiiI + OooOoooOo / Oo0O00O0O
  if 7 - 7: o00oO0oOo00 + OooOoooOo . OOO00O0O / oOOO
  if 22 - 22: Oo0OO - Oo0OO % IIIi . I1111i + Oo00o0o0
  if 63 - 63: OOO00O0O % I1111i * o00oO0oOo00 + I1111i / oOOO % O0OoOO0o
  if 45 - 45: Iii
  if 20 - 20: Oo0O00O0O * o00oO0oOo00 * OoOooO . IIIi
  if 78 - 78: O000oo + I1Ii - I1IiiiiI * I1111i - Oo0O00O0O % I1I11
  if 34 - 34: OoOooO
  if 80 - 80: OooOoooOo - oOOO / iII1Ii - i11iIiiIii
  if 68 - 68: Oo00o0o0 - oO00OoOO000o % OoOooO % I1111i
  if 11 - 11: OoOooO / iII1Ii % IIIi + o00oO0oOo00 + O000oo
 I1i1111I = ""
 OooOO0o0 = oOOoo0 ( )
 for i1111IIiii1 in OooOO0o0 :
  if OOooO == True :
   if i1111IIiii1 not in oOOOooo0oooo0 :
    if 49 - 49: IIIi . O000oo
    if 62 - 62: I1I11 / OOO00O0O - oO00OoOO000o - OOO00O0O + i11iIiiIii + OooOoooOo
    I1i11II = II11 ( I1i1111I , i1111IIiii1 )
    I1i1111I = I1i11II
    if 15 - 15: Iii / OoOooO . o00oO0oOo00 . i11iIiiIii
  else :
   I1i11II = II11 ( I1i1111I , i1111IIiii1 )
   I1i1111I = I1i11II
   if 59 - 59: I1111i - o00oO0oOo00 - Oo0OO
 if OOooO == True :
  O00O0OO00oo = open ( II1 , 'a' )
  if 48 - 48: OooOoooOo + I1Ii % I1I11 / oOOO - o00oO0oOo00
  if 67 - 67: Oo00o0o0 % o00oO0oOo00 . Oo0O00O0O + IIIi * I1Ii * I1I11
 else :
  O00O0OO00oo = open ( II1 , 'w' )
  if 36 - 36: OoOooO + oOOO
  if 5 - 5: oOOO * I1I11
 O00O0OO00oo . write ( I1i1111I )
 O00O0OO00oo . close ( )
 if 46 - 46: Oo0OO
 if 33 - 33: O0OoOO0o - I1 * Oo0O00O0O - oOOO - IIIi
 O00O0OO00oo = open ( II1 )
 oOOOooo0oooo0 = O00O0OO00oo . read ( )
 O00O0OO00oo . close ( )
 oOOOooo0oooo0 = oOOOooo0oooo0 . replace ( '\n' , '' ) . replace ( '\r' , '' )
 OOoo = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)".+?nstallRating="(.+?)"' ) . findall ( oOOOooo0oooo0 )
 if 84 - 84: I1111i + oOOO - I1I11 * I1I11
 if 61 - 61: Oo0O00O0O . Oo00o0o0 . Oo0O00O0O / oOOO
 for Ii1i1i1i1I1Ii , iiiI1 , o00O , iiIi1IIiI , o0O0Oo00 , i1iIIi in sorted ( OOoo , key = lambda OOoo : OOoo [ 0 ] ) :
  if iiiI1 in OooOO0o0 :
   oo0OO ( '[COLOR ghostwhite]' + str ( Ii1i1i1i1I1Ii ) + '[/COLOR]' , iiiI1 , 'intelselect' , o00O , iiIi1IIiI , o0O0Oo00 , i1iIIi )
   if 2 - 2: I1 - iII1Ii . Iii * O0OoOO0o / Oo00o0o0
def oOOoo0 ( ) :
 if xbmc . getCondVisibility ( 'system.platform.android' ) :
  try :
   OooOO0o0 = subprocess . Popen ( [ 'exec ' '/system/bin/pm list packages -3' '' ] , executable = '/system/bin/sh' , shell = True , stdout = subprocess . PIPE , stderr = subprocess . STDOUT ) . communicate ( ) [ 0 ] . rstrip ( '\n' ) . splitlines ( )
  except :
   OooOO0o0 = [ ]
   if 80 - 80: IIIi / I1Ii / I1I11 + OooOoooOo - oOOO
  for i1111IIiii1 in range ( len ( OooOO0o0 ) ) :
   OooOO0o0 [ i1111IIiii1 ] = OooOO0o0 [ i1111IIiii1 ] . partition ( ':' ) [ 2 ]
   if 11 - 11: o00oO0oOo00 * iII1Ii
 return OooOO0o0
 if 15 - 15: I1I11
def II11 ( theList , i ) :
 global theNotList
 oOoOoO000OO = "https://play.google.com/store/apps/details?id=" + i
 oOoooo000Oo00 = ii11II11 ( oOoOoO000OO )
 if 70 - 70: O000oo
 if oOoooo000Oo00 != False :
  oOoooo000Oo00 = oOoooo000Oo00 . replace ( '\n' , '' ) . replace ( '\r' , '' )
  if 48 - 48: I1 * Iii
  i1IiiI1iIi = r'<div class="id-app-title".tabindex=".">(.+?)</div>'
  OOoo = re . search ( i1IiiI1iIi , oOoooo000Oo00 )
  if OOoo != None : Ii1i1i1i1I1Ii = OOoo . group ( 1 )
  else : Ii1i1i1i1I1Ii = i
  if 66 - 66: iII1Ii * oOOO
  if 28 - 28: iII1Ii % I1I11 % oO00OoOO000o + OOO00O0O / OOO00O0O
  if 71 - 71: IIIi * iII1Ii % Oo0O00O0O % iII1Ii / OOO00O0O
  if 56 - 56: Oo0O00O0O % i11iIiiIii * O000oo . iII1Ii * OoOooO
  if 23 - 23: i11iIiiIii
  o00O = "androidapp://sources/apps/" + str ( i ) + ".png"
  if 39 - 39: o00oO0oOo00 - oO00OoOO000o % O0OoOO0o * iII1Ii - IIIi / O0OoOO0o
  if 29 - 29: oO00OoOO000o
  if 52 - 52: i11iIiiIii / OooOoooOo
  if 1 - 1: Oo0OO
  if 78 - 78: oO00OoOO000o + I1Ii - OoOooO
  if 10 - 10: I1111i % OOO00O0O
  oo0OoOooo = r'data-expand-to="full-screenshot-[0-9]{1,2}" src="(//\w+?.\w+?.\S+?=h900)"'
  OOoo = re . compile ( oo0OoOooo ) . findall ( oOoooo000Oo00 )
  if len ( OOoo ) != 0 : iiIi1IIiI = "https:" + OOoo [ len ( OOoo ) - 1 ]
  else : iiIi1IIiI = "None"
  if 95 - 95: Iii * oO00OoOO000o % Oo0OO % I1IiiiiI - I1IiiiiI
  oOoooO0 = r'data-video-url="https://www.youtube.com/embed/(\S.+?)\?ps=play.+?"'
  OOoo = re . search ( oOoooO0 , oOoooo000Oo00 )
  if OOoo != None : o0O0Oo00 = OOoo . group ( 1 )
  else : o0O0Oo00 = "None"
  if 68 - 68: Oo0OO / o00oO0oOo00
  Ii11 = r'<div class="content" itemprop="numDownloads">\s+?(\d.+?\s-\s\d.+?)\s+?</div>'
  OOoo = re . search ( Ii11 , oOoooo000Oo00 )
  if OOoo != None : II1i111 = 'Installed ' + OOoo . group ( 1 )
  else : II1i111 = "Installs: N/A"
  if 50 - 50: Iii % OooOoooOo
  iii11II1I = r'<div class="score" aria-label=" Rated .+? stars out of five stars ">(.+?)</div>'
  OOoo = re . search ( iii11II1I , oOoooo000Oo00 )
  if OOoo != None : iI111I11i = OOoo . group ( 1 ) + " Stars"
  else : iI111I11i = "Rating: N/A"
  i1iIIi = iI111I11i + " " + II1i111
  if 23 - 23: I1IiiiiI . o00oO0oOo00 + oOOO - IIIi
  if 18 - 18: I1I11 % i11iIiiIii % oO00OoOO000o / Oo00o0o0 / o00oO0oOo00 / OooOoooOo
  if 48 - 48: I1I11 + I1Ii / Iii + I1
  iiiI1 = i
  theList += 'name="' + Ii1i1i1i1I1Ii + '"url="' + iiiI1 + '"img="' + o00O + '"fanart="' + iiIi1IIiI + '"description="' + o0O0Oo00 + '"installRating="' + i1iIIi + '"'
  return theList
  if 18 - 18: oO00OoOO000o
  if 23 - 23: I1
  if 24 - 24: O000oo + O000oo * O0OoOO0o
  if 18 - 18: O0OoOO0o * I1Ii - I1IiiiiI
  if 31 - 31: oOOO - OoOooO % I1I11 % Oo00o0o0
  if 45 - 45: oO00OoOO000o + I1 * i11iIiiIii
  if 13 - 13: Oo0O00O0O * Oo00o0o0 - I1IiiiiI / IIIi + I1Ii + Iii
  if 39 - 39: O000oo - Oo0O00O0O
  if 81 - 81: oO00OoOO000o - OoOooO * Oo0O00O0O
 else :
  if 23 - 23: I1 / Oo00o0o0
  return theList
  if 28 - 28: oOOO * Oo0OO - iII1Ii
def iI11iiii1I ( name , url , iconimage , fanart , videolink ) :
 iiiiI1iiiIi = 0
 if 84 - 84: IIIi
 if videolink != "None" :
  iiiiI1iiiIi += 1
  if 87 - 87: Oo0OO + o00oO0oOo00
 if iiiiI1iiiIi == 1 : i1iIIIIIIiII1 = xbmcgui . Dialog ( ) . select ( '[COLOR deepskyblue]' + name + '[/COLOR]' , [ '[COLOR deepskyblue]Launch[/COLOR]' , '[COLOR ghostwhite]Preview Video[/COLOR]' , '[COLOR tomato]Uninstall[/COLOR]' ] )
 if iiiiI1iiiIi == 0 : i1iIIIIIIiII1 = xbmcgui . Dialog ( ) . select ( '[COLOR deepskyblue]' + name + '[/COLOR]' , [ '[COLOR deepskyblue]Launch[/COLOR]' , '[COLOR ghostwhite]No Preview Video[/COLOR]' , '[COLOR tomato]Uninstall[/COLOR]' ] )
 if 45 - 45: OOO00O0O / O0OoOO0o . O0OoOO0o
 if 35 - 35: I1111i . I1I11 * i11iIiiIii
 if 44 - 44: i11iIiiIii / oOOO
 if i1iIIIIIIiII1 == 1 :
  if videolink != 'None' :
   yt . PlayVideo ( videolink )
 if i1iIIIIIIiII1 == 0 :
  Ii1IIi = xbmcgui . Dialog ( ) . yesno ( "[COLOR orange]SpinzTV[/COLOR]" , "[COLOR cyan][B]][[/B]NT3L[B]][[/B]G3NC[B]][[/B][/COLOR]" , "" , "[COLOR ghostwhite]Would You Like To Launch:[/COLOR] [COLOR cyan]" + name + "[/COLOR]" , "[COLOR red]No Way[/COLOR]" , "[COLOR cyan]Heck Ya![/COLOR]" )
  if Ii1IIi == 1 :
   xbmc . executebuiltin ( 'StartAndroidActivity(%s)' % url )
 if i1iIIIIIIiII1 == 2 :
  i111i11I1ii = xbmcgui . Dialog ( ) . yesno ( "[COLOR orange]SpinzTV[/COLOR]" , "[COLOR cyan][B]][[/B]NT3L[B]][[/B]G3NC[B]][[/B][/COLOR]" , "" , "[COLOR ghostwhite]Would You Like To Remove:[/COLOR] [COLOR cyan]" + name + "[/COLOR]" , "[COLOR red]No Way[/COLOR]" , "[COLOR cyan]Heck Ya![/COLOR]" )
  if i111i11I1ii :
   xbmc . executebuiltin ( 'StartAndroidActivity("","android.intent.action.DELETE","","package:' + url + '")' )
   xbmc . sleep ( 2000 )
   try : shutil . rmtree ( "/sdcard/Android/data/" + url , ignore_errors = True , onerror = None )
   except : pass
   try : shutil . rmtree ( "/sdcard/Android/obb/" + url , ignore_errors = True , onerror = None )
   except : pass
   xbmc . executebuiltin ( 'Container.Refresh' )
   if 64 - 64: Oo00o0o0 / i11iIiiIii / o00oO0oOo00 . Oo0O00O0O
def ii11II11 ( url ) :
 try :
  i1iiIIi11I = urllib2 . Request ( url )
  i1iiIIi11I . add_header ( 'User-Agent' , 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3' )
  o0o0oOo000o0 = urllib2 . urlopen ( i1iiIIi11I )
  oOoooo000Oo00 = o0o0oOo000o0 . read ( )
  o0o0oOo000o0 . close ( )
  return oOoooo000Oo00
 except :
  return False
  if 25 - 25: I1Ii + I1I11 . o00oO0oOo00 % I1I11 * IIIi
  if 32 - 32: i11iIiiIii - I1111i
  if 53 - 53: Oo0O00O0O - Iii
def oOoi1i ( ) :
 Ii11iiI ( 'Emulators' , 'apkshow' , url = Ooo0oOooo0 , icon = O0O0ooOOO , themeit = I1I1i1I )
 Ii11iiI ( 'Roms' , 'roms' , icon = O0O0ooOOO , themeit = I1I1i1I )
 if 5 - 5: oO00OoOO000o + OoOooO + OoOooO . I1111i - Oo0OO
 if 63 - 63: Oo00o0o0
 if 71 - 71: OooOoooOo . I1IiiiiI * O0OoOO0o % Oo0O00O0O + IIIi
 if 36 - 36: Iii
def i1iiI ( ) :
 Ii11iiI ( 'NES' , 'nes' , icon = O0O0ooOOO , themeit = I1I1i1I )
 Ii11iiI ( 'SNES' , 'snes' , icon = O0O0ooOOO , themeit = I1I1i1I )
 Ii11iiI ( 'Nintendo 64' , 'n64' , icon = O0O0ooOOO , themeit = I1I1i1I )
 Ii11iiI ( 'Nintendo DS' , 'nds' , icon = O0O0ooOOO , themeit = I1I1i1I )
 Ii11iiI ( 'Genesis' , 'gen' , icon = O0O0ooOOO , themeit = I1I1i1I )
 Ii11iiI ( 'Playstation' , 'ps' , icon = O0O0ooOOO , themeit = I1I1i1I )
 Ii11iiI ( 'Atari' , 'atr' , icon = O0O0ooOOO , themeit = I1I1i1I )
 Ii11iiI ( 'PC Engine & Turbo Grafx' , 'tbg' , icon = O0O0ooOOO , themeit = I1I1i1I )
 if 74 - 74: I1111i % oO00OoOO000o
def iiIiI ( url ) :
 if not I1i11iIIi11 ( url ) == True : return False
 oOoooo000Oo00 = I1i ( url ) . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
 OOoo = re . compile ( '.+?ame="(.+?)".+?rl="(.+?)".+?con="(.+?)".+?anart="(.+?)"description="(.+?)"' ) . findall ( oOoooo000Oo00 )
 if len ( OOoo ) > 0 :
  for Ii1i1i1i1I1Ii , url , iIiiiii1i , iiIi1IIiI , o0O0Oo00 in OOoo :
   i1oOOOOOOOoO ( Ii1i1i1i1I1Ii , 'rominstall' , Ii1i1i1i1I1Ii , url , icon = iIiiiii1i , fanart = iiIi1IIiI , description = o0O0Oo00 , themeit = I1I1i1I )
  else : wiz . log ( "[ROM Menu] ERROR: Invalid Format." )
 else : wiz . log ( "[ROM Menu] ERROR: URL for apk list not working." )
 if 12 - 12: O0OoOO0o . Iii . I1I11 / OoOooO
 if 58 - 58: o00oO0oOo00 - I1 % Oo00o0o0 + I1111i . I1I11 / Iii
 if 8 - 8: oO00OoOO000o . iII1Ii * I1Ii + I1 % i11iIiiIii
 if 8 - 8: Oo0OO * OoOooO
def OOoOIiIIII ( ) :
 Ii11iiI ( 'SNES Titles A Thru B' , 'rom' , url = oOOOoo00 , icon = O0O0ooOOO , themeit = I1I1i1I )
 Ii11iiI ( 'SNES Titles C Thru E' , 'rom' , url = iiIiIIIiiI , icon = O0O0ooOOO , themeit = I1I1i1I )
 Ii11iiI ( 'SNES Titles F Thru H' , 'rom' , url = iiI1IIIi , icon = O0O0ooOOO , themeit = I1I1i1I )
 Ii11iiI ( 'SNES Titles I Thru K' , 'rom' , url = II11IiIi11 , icon = O0O0ooOOO , themeit = I1I1i1I )
 Ii11iiI ( 'SNES Titles L Thru M' , 'rom' , url = IIOOO0O00O0OOOO , icon = O0O0ooOOO , themeit = I1I1i1I )
 Ii11iiI ( 'SNES Titles N Thru O' , 'rom' , url = I1iiii1I , icon = O0O0ooOOO , themeit = I1I1i1I )
 Ii11iiI ( 'SNES Titles P Thru R' , 'rom' , url = OOo0 , icon = O0O0ooOOO , themeit = I1I1i1I )
 Ii11iiI ( 'SNES Titles S' , 'rom' , url = oO00ooooO0o , icon = O0O0ooOOO , themeit = I1I1i1I )
 Ii11iiI ( 'SNES Titles T Thru V' , 'rom' , url = oo0o , icon = O0O0ooOOO , themeit = I1I1i1I )
 Ii11iiI ( 'SNES Titles W Thru Z' , 'rom' , url = o0oO0oooOoo , icon = O0O0ooOOO , themeit = I1I1i1I )
 if 89 - 89: iII1Ii / OOO00O0O
 if 16 - 16: oOOO + Oo0OO / oOOO / iII1Ii % Oo00o0o0 % oO00OoOO000o
 if 22 - 22: I1 * iII1Ii * I1Ii + oO00OoOO000o * o00oO0oOo00
 if 100 - 100: OooOoooOo / Iii
def IiII1iiIiI ( ) :
 Ii11iiI ( 'NES Titles A Thru B' , 'rom' , url = I1III1111iIi , icon = O0O0ooOOO , themeit = I1I1i1I )
 Ii11iiI ( 'NES Titles C' , 'rom' , url = I1i111I , icon = oOooO0 , themeit = I1I1i1I )
 Ii11iiI ( 'NES Titles D Thru E' , 'rom' , url = Ooo , icon = O0O0ooOOO , themeit = I1I1i1I )
 Ii11iiI ( 'NES Titles F Thru G' , 'rom' , url = Oo0oo0O0o00O , icon = O0O0ooOOO , themeit = I1I1i1I )
 Ii11iiI ( 'NES Titles H Thru K' , 'rom' , url = I1i11 , icon = O0O0ooOOO , themeit = I1I1i1I )
 Ii11iiI ( 'NES Titles L Thru M' , 'rom' , url = IiIi1I1 , icon = O0O0ooOOO , themeit = I1I1i1I )
 Ii11iiI ( 'NES Titles N Thru Q' , 'rom' , url = IiIIi1 , icon = O0O0ooOOO , themeit = I1I1i1I )
 Ii11iiI ( 'NES Titles R Thru S' , 'rom' , url = IIIIiii1IIii , icon = O0O0ooOOO , themeit = I1I1i1I )
 Ii11iiI ( 'NES Titles T Thru V' , 'rom' , url = II1i11I , icon = O0O0ooOOO , themeit = I1I1i1I )
 Ii11iiI ( 'NES Titles W Thru Z' , 'rom' , url = ii1I1IIii11 , icon = O0O0ooOOO , themeit = I1I1i1I )
 if 59 - 59: OoOooO % oOOO
 if 92 - 92: I1IiiiiI % O0OoOO0o / oO00OoOO000o % oO00OoOO000o * OOO00O0O
 if 74 - 74: OoOooO . OOO00O0O % iII1Ii % Iii
 if 87 - 87: Oo00o0o0 - i11iIiiIii
 if 78 - 78: i11iIiiIii / O000oo - o00oO0oOo00
def iIIIIiiIii ( ) :
 Ii11iiI ( 'Genesis Titles A Thru B' , 'rom' , url = O0o0oO , icon = O0O0ooOOO , themeit = I1I1i1I )
 Ii11iiI ( 'Genesis Titles C Thru D' , 'rom' , url = IIIIiIiIi1 , icon = oOooO0 , themeit = I1I1i1I )
 Ii11iiI ( 'Genesis Titles E Thru G' , 'rom' , url = I11iiiiI1i , icon = O0O0ooOOO , themeit = I1I1i1I )
 Ii11iiI ( 'Genesis Titles H Thru L' , 'rom' , url = iI1i11 , icon = O0O0ooOOO , themeit = I1I1i1I )
 Ii11iiI ( 'Genesis Titles M Thru O' , 'rom' , url = OoOOoooOO0O , icon = O0O0ooOOO , themeit = I1I1i1I )
 Ii11iiI ( 'Genesis Titles P Thru R' , 'rom' , url = ooo00Ooo , icon = O0O0ooOOO , themeit = I1I1i1I )
 Ii11iiI ( 'Genesis Titles S Thru T' , 'rom' , url = Oo0o0O00 , icon = O0O0ooOOO , themeit = I1I1i1I )
 Ii11iiI ( 'Genesis Titles U Thru Z' , 'rom' , url = ii1I1i11 , icon = O0O0ooOOO , themeit = I1I1i1I )
 if 58 - 58: oOOO
 if 9 - 9: O000oo % oO00OoOO000o . IIIi + Oo0O00O0O
 if 62 - 62: OoOooO / OOO00O0O % OoOooO * iII1Ii % OOO00O0O
 if 33 - 33: OOO00O0O . Oo00o0o0 * iII1Ii * O000oo
 if 5 - 5: oOOO / Iii % OoOooO . I1111i * Iii
def ooOooOoOoO ( ) :
 Ii11iiI ( 'Atari Titles A Thru B' , 'rom' , url = OOo0O0oo0OO0O , icon = O0O0ooOOO , themeit = I1I1i1I )
 Ii11iiI ( 'Atari Titles C Thru D' , 'rom' , url = OO0 , icon = oOooO0 , themeit = I1I1i1I )
 Ii11iiI ( 'Atari Titles E Thru G' , 'rom' , url = o0Oooo , icon = O0O0ooOOO , themeit = I1I1i1I )
 Ii11iiI ( 'Atari Titles H Thru L' , 'rom' , url = iiI , icon = O0O0ooOOO , themeit = I1I1i1I )
 Ii11iiI ( 'Atari Titles M Thru O' , 'rom' , url = oOIIiIi , icon = O0O0ooOOO , themeit = I1I1i1I )
 Ii11iiI ( 'Atari Titles P Thru R' , 'rom' , url = OOoOooOoOOOoo , icon = O0O0ooOOO , themeit = I1I1i1I )
 Ii11iiI ( 'Atari Titles S Thru U' , 'rom' , url = Iiii1iI1i , icon = O0O0ooOOO , themeit = I1I1i1I )
 Ii11iiI ( 'Atari Titles V Thru Z' , 'rom' , url = I1ii1ii11i1I , icon = O0O0ooOOO , themeit = I1I1i1I )
 if 73 - 73: IIIi
 if 2 - 2: i11iIiiIii - I1 / Oo00o0o0 % OoOooO
 if 66 - 66: oOOO
 if 28 - 28: Iii - Iii . OooOoooOo - Oo0OO + OOO00O0O . Iii
 if 54 - 54: I1I11 - I1111i
def iIIiIIIi ( ) :
 Ii11iiI ( 'N64 Titles A Thru B' , 'rom' , url = O0O0Oo00 , icon = O0O0ooOOO , themeit = I1I1i1I )
 Ii11iiI ( 'N64 Titles C Thru E' , 'rom' , url = oOoO00o , icon = oOooO0 , themeit = I1I1i1I )
 Ii11iiI ( 'N64 Titles F Thru J' , 'rom' , url = oO00O0 , icon = O0O0ooOOO , themeit = I1I1i1I )
 Ii11iiI ( 'N64 Titles K Thru M' , 'rom' , url = IIi1IIIi , icon = O0O0ooOOO , themeit = I1I1i1I )
 Ii11iiI ( 'N64 Titles N Thru R' , 'rom' , url = O00Ooo , icon = O0O0ooOOO , themeit = I1I1i1I )
 Ii11iiI ( 'N64 Titles S Thru T' , 'rom' , url = OOOO0OOO , icon = O0O0ooOOO , themeit = I1I1i1I )
 Ii11iiI ( 'N64 Titles V Thru Z' , 'rom' , url = i1i1ii , icon = O0O0ooOOO , themeit = I1I1i1I )
 if 98 - 98: Oo00o0o0 % Iii * i11iIiiIii % oO00OoOO000o
 if 29 - 29: Iii
 if 66 - 66: oOOO
 if 97 - 97: OooOoooOo - Oo0O00O0O / I1111i * OOO00O0O
 if 55 - 55: o00oO0oOo00 . O0OoOO0o
def oOo00o00oO ( ) :
 Ii11iiI ( 'PC Engine And Turbo Grafx Titles A Thru B' , 'rom' , url = iII1ii1 , icon = O0O0ooOOO , themeit = I1I1i1I )
 Ii11iiI ( 'PC Engine And Turbo Grafx Titles C Thru E' , 'rom' , url = I1i1iiiI1 , icon = oOooO0 , themeit = I1I1i1I )
 Ii11iiI ( 'PC Engine And Turbo Grafx Titles F Thru I' , 'rom' , url = iIIi , icon = O0O0ooOOO , themeit = I1I1i1I )
 Ii11iiI ( 'PC Engine And Turbo Grafx Titles J Thru M' , 'rom' , url = oO0o00oo0 , icon = O0O0ooOOO , themeit = I1I1i1I )
 Ii11iiI ( 'PC Engine And Turbo Grafx Titles N Thru Q' , 'rom' , url = ii1IIII , icon = O0O0ooOOO , themeit = I1I1i1I )
 Ii11iiI ( 'PC Engine And Turbo Grafx Titles R Thru U' , 'rom' , url = oO00oOooooo0 , icon = O0O0ooOOO , themeit = I1I1i1I )
 Ii11iiI ( 'PC Engine And Turbo Grafx Titles V Thru Z' , 'rom' , url = oOo , icon = O0O0ooOOO , themeit = I1I1i1I )
 if 95 - 95: OOO00O0O
 if 88 - 88: Iii % iII1Ii + I1111i + I1111i * I1
 if 78 - 78: Oo0O00O0O
 if 77 - 77: oO00OoOO000o / OooOoooOo / oOOO % IIIi
 if 48 - 48: I1Ii - Iii + O000oo + Oo0O00O0O
def IiI1i111IiIiIi1 ( ) :
 Ii11iiI ( 'Nintendo DS Titles A' , 'rom' , url = O0OOooOoO , icon = O0O0ooOOO , themeit = I1I1i1I )
 Ii11iiI ( 'Nintendo DS Titles B' , 'rom' , url = i1II1I1Iii1 , icon = O0O0ooOOO , themeit = I1I1i1I )
 Ii11iiI ( 'Nintendo DS Titles C' , 'rom' , url = iiI11Iii , icon = O0O0ooOOO , themeit = I1I1i1I )
 Ii11iiI ( 'Nintendo DS Titles D' , 'rom' , url = O0o0O0 , icon = O0O0ooOOO , themeit = I1I1i1I )
 Ii11iiI ( 'Nintendo DS Titles E Thru F' , 'rom' , url = Ii1II1I11i1 , icon = O0O0ooOOO , themeit = I1I1i1I )
 Ii11iiI ( 'Nintendo DS Titles G Thru H' , 'rom' , url = oOoooooOoO , icon = O0O0ooOOO , themeit = I1I1i1I )
 Ii11iiI ( 'Nintendo DS Titles I Thru J' , 'rom' , url = Ii111 , icon = O0O0ooOOO , themeit = I1I1i1I )
 Ii11iiI ( 'Nintendo DS Titles K Thru L' , 'rom' , url = I111i1i1111 , icon = O0O0ooOOO , themeit = I1I1i1I )
 Ii11iiI ( 'Nintendo DS Titles M' , 'rom' , url = IIII1 , icon = O0O0ooOOO , themeit = I1I1i1I )
 Ii11iiI ( 'Nintendo DS Titles N Thru O' , 'rom' , url = I1I1i , icon = O0O0ooOOO , themeit = I1I1i1I )
 Ii11iiI ( 'Nintendo DS Titles P Thru Q' , 'rom' , url = I1IIIiIiIi , icon = O0O0ooOOO , themeit = I1I1i1I )
 Ii11iiI ( 'Nintendo DS Titles R' , 'rom' , url = IIIII1 , icon = O0O0ooOOO , themeit = I1I1i1I )
 Ii11iiI ( 'Nintendo DS Titles S' , 'rom' , url = iIi1Ii1i1iI , icon = O0O0ooOOO , themeit = I1I1i1I )
 Ii11iiI ( 'Nintendo DS Titles T Thru U' , 'rom' , url = IIiI1 , icon = O0O0ooOOO , themeit = I1I1i1I )
 Ii11iiI ( 'Nintendo DS Titles V Thru Z' , 'rom' , url = i1iI1 , icon = O0O0ooOOO , themeit = I1I1i1I )
 if 39 - 39: I1Ii - oO00OoOO000o
 if 53 - 53: o00oO0oOo00 % O0OoOO0o + Oo0OO . oOOO - oO00OoOO000o % o00oO0oOo00
 if 64 - 64: I1
 if 40 - 40: I1I11 % iII1Ii
def oo0O0o00 ( ) :
 Ii11iiI ( 'Playstation Titles A' , 'rom' , url = ii1I1IiiI1ii1i , icon = O0O0ooOOO , themeit = I1I1i1I )
 Ii11iiI ( 'Playstation Titles B' , 'rom' , url = O0o , icon = O0O0ooOOO , themeit = I1I1i1I )
 Ii11iiI ( 'Playstation Titles C Thru D' , 'rom' , url = oO0OoO00o , icon = O0O0ooOOO , themeit = I1I1i1I )
 Ii11iiI ( 'Playstation Titles E Thru F' , 'rom' , url = II1iiiiII , icon = O0O0ooOOO , themeit = I1I1i1I )
 Ii11iiI ( 'Playstation Titles G Thru J' , 'rom' , url = O0OoOO0oo0 , icon = O0O0ooOOO , themeit = I1I1i1I )
 Ii11iiI ( 'Playstation Titles K Thru N' , 'rom' , url = oOO , icon = O0O0ooOOO , themeit = I1I1i1I )
 Ii11iiI ( 'Playstation Titles O Thru R' , 'rom' , url = O0o0OO0000ooo , icon = O0O0ooOOO , themeit = I1I1i1I )
 Ii11iiI ( 'Playstation Titles S Thru T' , 'rom' , url = iIIII1iIIii , icon = O0O0ooOOO , themeit = I1I1i1I )
 Ii11iiI ( 'Playstation Titles U Thru Z' , 'rom' , url = oOOO00o000o , icon = O0O0ooOOO , themeit = I1I1i1I )
 if 70 - 70: iII1Ii
 if 46 - 46: I1Ii - OooOoooOo
 if 46 - 46: I1111i % I1IiiiiI
def oOOoO0OO00OOo0 ( ) :
 if not I11I == 'http://' :
  Ii1IIii = wiz . workingURL ( I11I )
  if Ii1IIii == True :
   oOoooo000Oo00 = wiz . openURL ( I11I ) . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' ) . replace ( 'repository=""' , 'repository="none"' ) . replace ( 'repositoryurl=""' , 'repositoryurl="http://"' ) . replace ( 'repositoryxml=""' , 'repositoryxml="http://"' )
   OOoo = re . compile ( 'name="(.+?)".+?lugin="(.+?)".+?rl="(.+?)".+?epository="(.+?)".+?epositoryxml="(.+?)".+?epositoryurl="(.+?)".+?con="(.+?)".+?anart="(.+?)".+?dult="(.+?)".+?escription="(.+?)"' ) . findall ( oOoooo000Oo00 )
   if len ( OOoo ) > 0 :
    for Ii1i1i1i1I1Ii , II1Ii , iiiI1 , oOOoOoOOO , oOoOo0oOo0O0O0o , IiiIIiIIii1iI , iIiiiii1i , iiIi1IIiI , i1oO0OO0 , o0O0Oo00 in OOoo :
     if not i1iIIi1 == 'true' and i1oO0OO0 . lower ( ) == 'yes' : continue
     try :
      Oo0O0O000 = xbmcaddon . Addon ( id = II1Ii )
      Ii1i1i1i1I1Ii = "[COLOR green][Installed][/COLOR] %s" % Ii1i1i1i1I1Ii
     except :
      pass
     i11iiI1111 ( Ii1i1i1i1I1Ii , 'addoninstall' , II1Ii , description = o0O0Oo00 , icon = iIiiiii1i , fanart = iiIi1IIiI , themeit = ii1I )
   else : wiz . log ( "[Addon Menu] ERROR: Invalid Format." )
  else :
   wiz . log ( "[Addon Menu] ERROR: URL for Addon list not working." )
   i11iiI1111 ( 'Url for txt file not valid' , '' , themeit = O0oO0 )
   i11iiI1111 ( '%s' % Ii1IIii , '' , themeit = O0oO0 )
 else : wiz . log ( "[Addon Menu] No Addon list added." )
 O0000OOO0 ( 'files' , 'viewType' )
 if 29 - 29: o00oO0oOo00 / oOOO * oO00OoOO000o . o00oO0oOo00
def oO00 ( plugin ) :
 if not I11I == 'http://' :
  Ii1IIii = wiz . workingURL ( I11I )
  if Ii1IIii == True :
   oOoooo000Oo00 = wiz . openURL ( I11I ) . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' ) . replace ( 'repository=""' , 'repository="none"' ) . replace ( 'repositoryurl=""' , 'repositoryurl="http://"' ) . replace ( 'repositoryxml=""' , 'repositoryxml="http://"' )
   OOoo = re . compile ( 'name="(.+?)".+?lugin="%s".+?rl="(.+?)".+?epository="(.+?)".+?epositoryxml="(.+?)".+?epositoryurl="(.+?)".+?con="(.+?)".+?anart="(.+?)".+?dult="(.+?)".+?escription="(.+?)"' % plugin ) . findall ( oOoooo000Oo00 )
   if len ( OOoo ) > 0 :
    for Ii1i1i1i1I1Ii , iiiI1 , oOOoOoOOO , oOoOo0oOo0O0O0o , IiiIIiIIii1iI , iIiiiii1i , iiIi1IIiI , i1oO0OO0 , o0O0Oo00 in OOoo :
     if os . path . exists ( os . path . join ( IiI , plugin ) ) :
      if I11i11Ii . yesno ( Oo0Ooo , "[COLOR %s]Would you like to remove and reinstall:" % Iii1I1I11iiI1 , "[COLOR %s]%s[/COLOR]?[/COLOR]" % ( ii1iII1II , plugin ) , yeslabel = "[B]Yes Remove[/B]" , nolabel = "[B]No Skip[/B]" ) :
       wiz . cleanHouse ( os . path . join ( IiI , plugin ) )
       if I11i11Ii . yesno ( Oo0Ooo , "[COLOR %s]Would you like to remove the addon_data for:" % Iii1I1I11iiI1 , "[COLOR %s]%s[/COLOR]?[/COLOR]" % ( ii1iII1II , plugin ) , yeslabel = "[B]Yes Remove[/B]" , nolabel = "[B]No Skip[/B]" ) :
        ii111IIII ( plugin )
      else : wiz . log ( "[Addon Installer] %s wasnt re-installed" % plugin ) ; return False
     i1iIi = os . path . join ( IiI , oOOoOoOOO )
     if not oOOoOoOOO . lower ( ) == 'none' and not os . path . exists ( i1iIi ) :
      wiz . log ( "Repository not installed, installing it" )
      if I11i11Ii . yesno ( Oo0Ooo , "[COLOR %s]Would you like to install the repository for [COLOR %s]%s[/COLOR]:" % ( Iii1I1I11iiI1 , ii1iII1II , plugin ) , "[COLOR %s]%s[/COLOR]?[/COLOR]" % ( ii1iII1II , oOOoOoOOO ) , yeslabel = "[B]Yes Install[/B]" , nolabel = "[B]No Skip[/B]" ) :
       I1Iiii = wiz . openURL ( oOoOo0oOo0O0O0o ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
       I1III1II1I11 = re . compile ( '<addon.+?d="%s".+?ersion="(.+?)".+?>' % oOOoOoOOO ) . findall ( I1Iiii )
       oooii1iiIi1 = re . compile ( '<addon.+?ersion="(.+?)".+?d="%s".+?>' % oOOoOoOOO ) . findall ( I1Iiii )
       wiz . log ( "Match 1: %s / Match 2: %s" % ( len ( I1III1II1I11 ) , len ( oooii1iiIi1 ) ) )
       if len ( I1III1II1I11 ) > 0 : oO0oO0 = I1III1II1I11 [ 0 ]
       elif len ( oooii1iiIi1 ) > 0 : oO0oO0 = oooii1iiIi1 [ 0 ]
       else : wiz . log ( "No Match" )
       IIi11 = '%s%s-%s.zip' % ( IiiIIiIIii1iI , oOOoOoOOO , oO0oO0 )
       wiz . log ( IIi11 )
       ooo0O0OOO000o ( oOOoOoOOO , IIi11 )
       wiz . ebi ( 'UpdateAddonRepos()' )
       wiz . log ( "Installing Addon from Kodi" )
       xbmc . sleep ( 1000 )
       iiI1iii = OOoOOo00O0o0 ( plugin )
       if iiI1iii :
        wiz . refresh ( )
        return True
      else : wiz . log ( "[Addon Installer] Repository for %s not installed: %s" % ( plugin , oOOoOoOOO ) )
     elif oOOoOoOOO . lower ( ) == 'none' :
      wiz . log ( "No repository, installing addon" )
      Oo0O0Oo00O = plugin
      iI = iiiI1
      ooo0O0OOO000o ( plugin , iiiI1 )
      wiz . refresh ( )
      return True
     else :
      wiz . log ( "Repository installed, installing addon" )
      iiI1iii = OOoOOo00O0o0 ( plugin )
      if iiI1iii :
       wiz . refresh ( )
       return True
     oo0ooooO = wiz . openURL ( oOoOo0oOo0O0O0o ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
     iiIIi = re . compile ( '<addon.+?id="%s".+?ersion="(.+?)".+?>' % plugin ) . findall ( oo0ooooO )
     i1iiIIiI1iiI = re . compile ( '<addon.+?ersion="(.+?)".+?id="%s".+?>' % plugin ) . findall ( oo0ooooO )
     if len ( iiIIi ) > 0 : oO0oO0 = iiIIi [ 0 ]
     elif len ( i1iiIIiI1iiI ) > 0 : oO0oO0 = i1iiIIiI1iiI [ 0 ]
     else : wiz . log ( "no match" )
     iiiI1 = "%s%s-%s.zip" % ( iiiI1 , plugin , oO0oO0 )
     wiz . log ( str ( iiiI1 ) )
     ooo0O0OOO000o ( plugin , iiiI1 )
     wiz . refresh ( )
   else : wiz . log ( "[Addon Installer] Invalid Format" )
  else : wiz . log ( "[Addon Installer] Text File: %s" % Ii1IIii )
 else : wiz . log ( "[Addon Installer] Not Enabled." )
 if 18 - 18: O0OoOO0o - Oo00o0o0 % O0OoOO0o / I1Ii
def OOoOOo00O0o0 ( plugin ) :
 wiz . log ( "Running Plugin" )
 wiz . ebi ( 'RunPlugin(plugin://%s)' % plugin )
 xbmc . sleep ( 500 )
 if not wiz . whileWindow ( 'yesnodialog' ) :
  return False
 xbmc . sleep ( 500 )
 if wiz . whileWindow ( 'okdialog' ) :
  return False
 O0Oo00OO00Ooo = wiz . whileWindow ( 'progressdialog' )
 xbmc . sleep ( 1000 )
 wiz . log ( "Download complete" )
 if os . path . exists ( os . path . join ( IiI , plugin ) ) : return True
 else : return False
 if 87 - 87: oOOO * IIIi % Iii % I1I11
def ooo0O0OOO000o ( name , url ) :
 if not wiz . workingURL ( url ) == True : wiz . LogNotify ( "Addon Installer" , '%s: [COLOR red]Invalid Zip Url![/COLOR]' % name ) ; return
 if not os . path . exists ( IiiIII111iI ) : os . makedirs ( IiiIII111iI )
 oO00oOo . create ( Oo0Ooo , '[COLOR %s][B]Downloading:[/B][/COLOR] [COLOR %s]%s[/COLOR]' % ( Iii1I1I11iiI1 , ii1iII1II , name ) , '' , 'Please Wait' )
 iIi1Ii = url . split ( '/' )
 IiI1IIIII1I = os . path . join ( IiiIII111iI , iIi1Ii [ - 1 ] )
 try : os . remove ( IiI1IIIII1I )
 except : pass
 downloader . download ( url , IiI1IIIII1I , oO00oOo )
 xbmc . sleep ( 500 )
 I1I1IiIi1 = '[COLOR %s][B]Installing:[/B][/COLOR] [COLOR %s]%s[/COLOR]' % ( Iii1I1I11iiI1 , ii1iII1II , name )
 oO00oOo . update ( 0 , I1I1IiIi1 , '' , 'Please Wait' )
 oOO0o0oo0 , oOo000O , iII = extract . all ( IiI1IIIII1I , IiI , oO00oOo , title = I1I1IiIi1 )
 oO00oOo . close ( )
 ooO0o0O0Oo ( name )
 IiiIIi ( name )
 xbmc . sleep ( 500 )
 wiz . ebi ( 'UpdateAddonRepos()' )
 wiz . ebi ( 'UpdateLocalAddons()' )
 xbmc . sleep ( 500 )
 wiz . refresh ( )
 if 71 - 71: Iii + OooOoooOo * oOOO % oOOO / oOOO
def IiiIIi ( name ) :
 OoO00o0 = os . path . join ( IiI , name , 'addon.xml' )
 if os . path . exists ( OoO00o0 ) :
  oo = open ( OoO00o0 , mode = 'r' ) ; oOoooo000Oo00 = oo . read ( ) ; oo . close ( ) ;
  OOoo = re . compile ( 'import addon="(.+?)"' ) . findall ( oOoooo000Oo00 )
  for o0oOOO0 in OOoo :
   if not 'xbmc.python' in o0oOOO0 :
    oOOOiI1iIIII1 = os . path . join ( IiI , o0oOOO0 )
    if not os . path . exists ( oOOOiI1iIIII1 ) :
     OO0I11Ii1iI11iI1 = '%s%s.zip' % ( Oo0O00O000 , o0oOOO0 )
     IiI1IIIII1I = os . path . join ( IiiIII111iI , '%s.zip' % o0oOOO0 )
     try : os . remove ( IiI1IIIII1I )
     except : pass
     oO00oOo . update ( 0 , '[COLOR %s][B]Downloading Dependency:[/B][/COLOR] [COLOR %s]%s[/COLOR]' % ( Iii1I1I11iiI1 , ii1iII1II , o0oOOO0 ) , '' , 'Please Wait' )
     downloader . download ( OO0I11Ii1iI11iI1 , IiI1IIIII1I , oO00oOo )
     xbmc . sleep ( 100 )
     I1I1IiIi1 = '[COLOR %s][B]Installing Dependency:[/B][/COLOR] [COLOR %s]%s[/COLOR]' % ( Iii1I1I11iiI1 , ii1iII1II , o0oOOO0 )
     oO00oOo . update ( 0 , I1I1IiIi1 , '' , 'Please Wait' )
     oOO0o0oo0 , oOo000O , iII = extract . all ( IiI1IIIII1I , IiI , oO00oOo , title = I1I1IiIi1 )
     ooO0o0O0Oo ( o0oOOO0 )
     IiiIIi ( o0oOOO0 )
     xbmc . sleep ( 100 )
     oO00oOo . close ( )
     if 32 - 32: OOO00O0O
def ooO0o0O0Oo ( addon ) :
 iiiI1 = os . path . join ( IiI , addon , 'addon.xml' )
 if os . path . exists ( iiiI1 ) :
  list = open ( iiiI1 , mode = 'r' ) ; oO0O00oo = list . read ( ) . replace ( '\n' , '' ) . replace ( '\r' , '' ) ; list . close ( )
  OOoo = re . compile ( '<addon.+?name="(.+?)".+?>' ) . findall ( oO0O00oo )
  iIiiiii1i = os . path . join ( IiI , addon , 'icon.png' )
  wiz . LogNotify ( OOoo [ 0 ] , 'Addon Enabled' , '2000' , iIiiiii1i )
  if 93 - 93: oO00OoOO000o % I1I11 . OoOooO / O0OoOO0o * Oo00o0o0
def i1iii1ii ( url ) :
 if not I1i11iIIi11 ( url ) == True : return False
 oOoooo000Oo00 = wiz . openURL ( url ) . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
 OOoo = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?con="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( oOoooo000Oo00 )
 if len ( OOoo ) > 0 :
  for Ii1i1i1i1I1Ii , url , iIiiiii1i , iiIi1IIiI , o0O0Oo00 in OOoo :
   i11iiI1111 ( Ii1i1i1i1I1Ii , 'viewVideo' , url = url , description = o0O0Oo00 , icon = iIiiiii1i , fanart = iiIi1IIiI , themeit = ii1I )
  else : wiz . log ( "[YouTube Menu] ERROR: Invalid Format." )
 else :
  wiz . log ( "[YouTube Menu] ERROR: URL for YouTube list not working." )
  i11iiI1111 ( 'Url for txt file not valid' , '' , themeit = O0oO0 )
 O0000OOO0 ( 'files' , 'viewType' )
 if 18 - 18: iII1Ii . I1 % I1I11 % I1IiiiiI
 if 87 - 87: O000oo . Oo0O00O0O * I1I11
 if 100 - 100: iII1Ii / OooOoooOo - OOO00O0O % I1IiiiiI - O000oo
def i11II ( view = None ) :
 o0o = '[B][COLOR green]ON[/COLOR][/B]' ; o00o0O0O00 = '[B][COLOR red]OFF[/COLOR][/B]'
 iIIOOoO0oO00o = 'true' if iI111I11I1I1 == 'true' else 'false'
 iiiiii1 = 'true' if OOooO0OOoo == 'true' else 'false'
 OO0o0oO0O000o = 'true' if iIii1 == 'true' else 'false'
 I1iI11iii = 'true' if oOOoO0 == 'true' else 'false'
 oo0oO = 'true' if iiI1IiI == 'true' else 'false'
 IiIi1iI11 = 'true' if ii11iIi1I == 'true' else 'false'
 iiI1iI1I = 'true' if ooOoOoo0O == 'true' else 'false'
 III1II111Ii1 = 'true' if OooO0 == 'true' else 'false'
 if wiz . Grab_Log ( True ) == False : o0O0OO0o = 0
 else : o0O0OO0o = OOOoOo ( wiz . Grab_Log ( True ) , True )
 if wiz . Grab_Log ( True , True ) == False : OOoO0oo0O = 0
 else : OOoO0oo0O = OOOoOo ( wiz . Grab_Log ( True , True ) , True )
 iiI1I1ii = int ( o0O0OO0o ) + int ( OOoO0oo0O )
 o00IiI1iiII1i1i = ': [COLOR red]Not Found[/COLOR]' if not os . path . exists ( oOOoo00O0O ) else ": [COLOR green]%s[/COLOR]" % wiz . convertSize ( os . path . getsize ( oOOoo00O0O ) )
 if III1II111Ii1 == 'true' :
  i1IiI = 'true'
  o0o0O00 = 'true'
  oOo000OOooO0O = 'true'
  IiOoOoooO0O00 = 'true'
  oOO0OooO0 = 'true'
  OoooOo = 'true'
  Ii1Iii11 = 'true'
  o0oO = 'true'
 else :
  i1IiI = 'true' if II11iiii1Ii == 'true' else 'false'
  o0o0O00 = 'true' if OO0oOoo == 'true' else 'false'
  oOo000OOooO0O = 'true' if O0o0Oo == 'true' else 'false'
  IiOoOoooO0O00 = 'true' if Oo00OOOOO == 'true' else 'false'
  oOO0OooO0 = 'true' if O0O == 'true' else 'false'
  OoooOo = 'true' if O00o0OO == 'true' else 'false'
  Ii1Iii11 = 'true' if I11i1 == 'true' else 'false'
  o0oO = 'true' if iIi1ii1I1 == 'true' else 'false'
 i11i11 = wiz . getSize ( IiiIII111iI )
 Ii11Iii = wiz . getSize ( oo00 )
 ooo00OoOO0o = wiz . getCacheSize ( )
 oo0O0o = i11i11 + Ii11Iii + ooo00OoOO0o
 IioO0O = [ 'Always' , 'Daily' , '3 Days' , 'Weekly' ]
 i11iiI1111 ( 'Show All Maintenance: %s' % IiIi1iI11 . replace ( 'true' , o0o ) . replace ( 'false' , o00o0O0O00 ) , 'togglesetting' , 'showmaint' , icon = Ii1I1i , themeit = ii1I )
 i11iiI1111 ( 'Auto Clean' , '' , fanart = Oo0oO0ooo , icon = Ii1I1i , themeit = I1I1i1I )
 i11iiI1111 ( 'Auto Clean Up On Startup: %s' % iIIOOoO0oO00o . replace ( 'true' , o0o ) . replace ( 'false' , o00o0O0O00 ) , 'togglesetting' , 'autoclean' , icon = Ii1I1i , themeit = O0oO0 )
 Ii11iiI ( '[B]Cleaning Tools[/B]' , 'maint' , 'clean' , icon = Ii1I1i , themeit = I1I1i1I )
 if iIIOOoO0oO00o == 'true' :
  i11iiI1111 ( '--- Auto Clean Fequency: [B][COLOR green]%s[/COLOR][/B]' % IioO0O [ O0OoO000O0OO ] , 'changefeq' , icon = Ii1I1i , themeit = O0oO0 )
  i11iiI1111 ( '--- Clear Cache on Startup: %s' % iiiiii1 . replace ( 'true' , o0o ) . replace ( 'false' , o00o0O0O00 ) , 'togglesetting' , 'clearcache' , icon = Ii1I1i , themeit = O0oO0 )
  i11iiI1111 ( '--- Clear Packages on Startup: %s' % OO0o0oO0O000o . replace ( 'true' , o0o ) . replace ( 'false' , o00o0O0O00 ) , 'togglesetting' , 'clearpackages' , icon = Ii1I1i , themeit = O0oO0 )
  i11iiI1111 ( '--- Clear Old Thumbs on Startup: %s' % I1iI11iii . replace ( 'true' , o0o ) . replace ( 'false' , o00o0O0O00 ) , 'togglesetting' , 'clearthumbs' , icon = Ii1I1i , themeit = O0oO0 )
  i11iiI1111 ( '--- Delay Clear Packages: %s' % oo0oO . replace ( 'true' , o0o ) . replace ( 'false' , o00o0O0O00 ) , 'togglesetting' , 'delayautoclean' , icon = Ii1I1i , themeit = O0oO0 )
 i11iiI1111 ( 'Clear Video Cache' , '' , fanart = Oo0oO0ooo , icon = Ii1I1i , themeit = I1I1i1I )
 i11iiI1111 ( 'Include Video Cache in Clear Cache: %s' % iiI1iI1I . replace ( 'true' , o0o ) . replace ( 'false' , o00o0O0O00 ) , 'togglecache' , 'includevideo' , icon = Ii1I1i , themeit = O0oO0 )
 if view == "clean" or ii11iIi1I == 'true' :
  i11iiI1111 ( 'Total Clean Up: [COLOR green][B]%s[/B][/COLOR]' % wiz . convertSize ( oo0O0o ) , 'fullclean' , icon = Ii1I1i , themeit = O0oO0 )
  i11iiI1111 ( 'Clear Cache: [COLOR green][B]%s[/B][/COLOR]' % wiz . convertSize ( ooo00OoOO0o ) , 'clearcache' , icon = Ii1I1i , themeit = O0oO0 )
  i11iiI1111 ( 'Clear Packages: [COLOR green][B]%s[/B][/COLOR]' % wiz . convertSize ( i11i11 ) , 'clearpackages' , icon = Ii1I1i , themeit = O0oO0 )
  i11iiI1111 ( 'Clear Thumbnails: [COLOR green][B]%s[/B][/COLOR]' % wiz . convertSize ( Ii11Iii ) , 'clearthumb' , icon = Ii1I1i , themeit = O0oO0 )
  i11iiI1111 ( 'Clear Crash Logs' , 'clearcrash' , icon = Ii1I1i , themeit = O0oO0 )
  i11iiI1111 ( 'Purge Databases' , 'purgedb' , icon = Ii1I1i , themeit = O0oO0 )
  i11iiI1111 ( 'Fresh Start' , 'freshstart' , icon = Ii1I1i , themeit = O0oO0 )
 iIiiii ( '[B]Addon Tools[/B]' , 'maint' , 'addon' , icon = Ii1I1i , themeit = I1I1i1I )
 if view == "addon" or ii11iIi1I == 'true' :
  iIiiii ( 'Remove Addons' , 'removeaddons' , icon = Ii1I1i , themeit = O0oO0 )
  iIiiii ( 'Remove Addon Data' , 'removeaddondata' , icon = Ii1I1i , themeit = O0oO0 )
  iIiiii ( 'Enable/Disable Addons' , 'enableaddons' , icon = Ii1I1i , themeit = O0oO0 )
  i11iiI1111 ( 'Enable/Disable Adult Addons' , 'toggleadult' , icon = Ii1I1i , themeit = O0oO0 )
  i11iiI1111 ( 'Force Update Addons' , 'forceupdate' , icon = Ii1I1i , themeit = O0oO0 )
  i11iiI1111 ( 'Hide Passwords On Keyboard Entry' , 'hidepassword' , icon = Ii1I1i , themeit = O0oO0 )
  i11iiI1111 ( 'Unhide Passwords On Keyboard Entry' , 'unhidepassword' , icon = Ii1I1i , themeit = O0oO0 )
 iIiiii ( '[B]Misc Maintenance[/B]' , 'maint' , 'misc' , icon = Ii1I1i , themeit = I1I1i1I )
 if view == "misc" or ii11iIi1I == 'true' :
  i11iiI1111 ( 'Reload Skin' , 'forceskin' , icon = Ii1I1i , themeit = O0oO0 )
  i11iiI1111 ( 'Force Close Kodi' , 'forceclose' , icon = Ii1I1i , themeit = O0oO0 )
  i11iiI1111 ( 'Upload Kodi.log' , 'uploadlog' , icon = Ii1I1i , themeit = O0oO0 )
  i11iiI1111 ( 'View Errors in Log: %s Error(s)' % ( iiI1I1ii ) , 'viewerrorlog' , icon = Ii1I1i , themeit = O0oO0 )
  i11iiI1111 ( 'View Log File' , 'viewlog' , icon = Ii1I1i , themeit = O0oO0 )
  i11iiI1111 ( 'View Wizard Log File' , 'viewwizlog' , icon = Ii1I1i , themeit = O0oO0 )
  i11iiI1111 ( 'Clear Wizard Log File %s' % o00IiI1iiII1i1i , 'clearwizlog' , icon = Ii1I1i , themeit = O0oO0 )
 iIiiii ( '[B]Back up/Restore[/B]' , 'maint' , 'backup' , icon = Ii1I1i , themeit = I1I1i1I )
 if view == "backup" or ii11iIi1I == 'true' :
  i11iiI1111 ( 'Clean Up Back Up Folder' , 'clearbackup' , icon = Ii1I1i , themeit = O0oO0 )
  i11iiI1111 ( 'Back Up Location: [COLOR %s]%s[/COLOR]' % ( Iii1I1I11iiI1 , Oo0oOOo ) , 'settings' , 'Maintenance' , icon = Ii1I1i , themeit = O0oO0 )
  i11iiI1111 ( '[Back Up]: Build' , 'backupbuild' , icon = Ii1I1i , themeit = O0oO0 )
  i11iiI1111 ( '[Back Up]: GuiFix' , 'backupgui' , icon = Ii1I1i , themeit = O0oO0 )
  i11iiI1111 ( '[Back Up]: Theme' , 'backuptheme' , icon = Ii1I1i , themeit = O0oO0 )
  i11iiI1111 ( '[Back Up]: Addon_data' , 'backupaddon' , icon = Ii1I1i , themeit = O0oO0 )
  i11iiI1111 ( '[Restore]: Local Build' , 'restorezip' , icon = Ii1I1i , themeit = O0oO0 )
  i11iiI1111 ( '[Restore]: Local GuiFix' , 'restoregui' , icon = Ii1I1i , themeit = O0oO0 )
  i11iiI1111 ( '[Restore]: Local Addon_data' , 'restoreaddon' , icon = Ii1I1i , themeit = O0oO0 )
  i11iiI1111 ( '[Restore]: External Build' , 'restoreextzip' , icon = Ii1I1i , themeit = O0oO0 )
  i11iiI1111 ( '[Restore]: External GuiFix' , 'restoreextgui' , icon = Ii1I1i , themeit = O0oO0 )
  i11iiI1111 ( '[Restore]: External Addon_data' , 'restoreextaddon' , icon = Ii1I1i , themeit = O0oO0 )
 iIiiii ( '[B]System Tweaks/Fixes[/B]' , 'maint' , 'tweaks' , icon = Ii1I1i , themeit = I1I1i1I )
 if view == "tweaks" or ii11iIi1I == 'true' :
  if not OoooOoo == 'http://' : Ii11iiI ( 'Advanced Settings' , 'advancedsetting' , icon = Ii1I1i , themeit = O0oO0 )
  else : I1i1iiiII1i ( 'Advanced Settings' , 'autoadvanced' , icon = Ii1I1i , themeit = O0oO0 )
  i11iiI1111 ( 'Scan Sources for broken links' , 'checksources' , icon = Ii1I1i , themeit = O0oO0 )
  i11iiI1111 ( 'Scan For Broken Repositories' , 'checkrepos' , icon = Ii1I1i , themeit = O0oO0 )
  i11iiI1111 ( 'Fix Addons Not Updating' , 'fixaddonupdate' , icon = Ii1I1i , themeit = O0oO0 )
  i11iiI1111 ( 'Remove special character filenames' , 'asciicheck' , icon = Ii1I1i , themeit = O0oO0 )
  i11iiI1111 ( 'Convert Paths to special' , 'convertpath' , icon = Ii1I1i , themeit = O0oO0 )
  iIiiii ( 'System Information' , 'systeminfo' , icon = Ii1I1i , themeit = O0oO0 )
 if iiI1iI1I == 'true' :
  i11iiI1111 ( '--- Include All Video Addons: %s' % III1II111Ii1 . replace ( 'true' , o0o ) . replace ( 'false' , o00o0O0O00 ) , 'togglecache' , 'includeall' , icon = Ii1I1i , themeit = O0oO0 )
  i11iiI1111 ( '--- Include Bob: %s' % i1IiI . replace ( 'true' , o0o ) . replace ( 'false' , o00o0O0O00 ) , 'togglecache' , 'includebob' , icon = Ii1I1i , themeit = O0oO0 )
  i11iiI1111 ( '--- Include Phoenix: %s' % o0o0O00 . replace ( 'true' , o0o ) . replace ( 'false' , o00o0O0O00 ) , 'togglecache' , 'includephoenix' , icon = Ii1I1i , themeit = O0oO0 )
  i11iiI1111 ( '--- Include Specto: %s' % oOo000OOooO0O . replace ( 'true' , o0o ) . replace ( 'false' , o00o0O0O00 ) , 'togglecache' , 'includespecto' , icon = Ii1I1i , themeit = O0oO0 )
  i11iiI1111 ( '--- Include Exodus: %s' % oOO0OooO0 . replace ( 'true' , o0o ) . replace ( 'false' , o00o0O0O00 ) , 'togglecache' , 'includeexodus' , icon = Ii1I1i , themeit = O0oO0 )
  i11iiI1111 ( '--- Include Salts: %s' % Ii1Iii11 . replace ( 'true' , o0o ) . replace ( 'false' , o00o0O0O00 ) , 'togglecache' , 'includesalts' , icon = Ii1I1i , themeit = O0oO0 )
  i11iiI1111 ( '--- Include Salts HD Lite: %s' % o0oO . replace ( 'true' , o0o ) . replace ( 'false' , o00o0O0O00 ) , 'togglecache' , 'includesaltslite' , icon = Ii1I1i , themeit = O0oO0 )
  i11iiI1111 ( '--- Include One Channel: %s' % OoooOo . replace ( 'true' , o0o ) . replace ( 'false' , o00o0O0O00 ) , 'togglecache' , 'includeonechan' , icon = Ii1I1i , themeit = O0oO0 )
  i11iiI1111 ( '--- Include Genesis: %s' % IiOoOoooO0O00 . replace ( 'true' , o0o ) . replace ( 'false' , o00o0O0O00 ) , 'togglecache' , 'includegenesis' , icon = Ii1I1i , themeit = O0oO0 )
  i11iiI1111 ( '--- Enable All Video Addons' , 'togglecache' , 'true' , icon = Ii1I1i , themeit = O0oO0 )
  i11iiI1111 ( '--- Disable All Video Addons' , 'togglecache' , 'false' , icon = Ii1I1i , themeit = O0oO0 )
 iIiiii ( '[I]<< Return to Main Menu[/I]' , icon = Ii1I1i , themeit = ii1I )
 O0000OOO0 ( 'files' , 'viewType' )
 if 79 - 79: Oo0O00O0O - Iii * Iii . I1I11
def Oo00ooO0OoOo ( ) :
 if not OoooOoo == 'http://' :
  i11iiI1111 ( 'Configure Wizard' , 'autoadvanced' , icon = Ii1I1i , themeit = O0oO0 )
  if os . path . exists ( i1i1II ) : I1i1iiiII1i ( 'View Currect AdvancedSettings.xml' , 'currentsettings' , icon = Ii1I1i , themeit = O0oO0 )
  o0oOO00 = wiz . workingURL ( OoooOoo )
  if o0oOO00 == True :
   if o0OIiII == 'No' : I1i1iiiII1i ( wiz . sep ( ) , '' , icon = Ii1I1i , themeit = O0oO0 )
   oOoooo000Oo00 = wiz . openURL ( OoooOoo ) . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
   OOoo = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?con="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( oOoooo000Oo00 )
   if len ( OOoo ) > 0 :
    for Ii1i1i1i1I1Ii , iiiI1 , iIiiiii1i , iiIi1IIiI , o0O0Oo00 in OOoo :
     i11iiI1111 ( Ii1i1i1i1I1Ii , 'writeadvanced' , Ii1i1i1i1I1Ii , description = o0O0Oo00 , icon = iIiiiii1i , fanart = iiIi1IIiI , themeit = ii1I )
   else : wiz . log ( "[Advanced Settings] ERROR: Invalid Format." )
  else : wiz . log ( "[Advanced Settings] URL not working: %s" % o0oOO00 )
 else : wiz . log ( "[Advanced Settings] not Enabled" )
 if 46 - 46: i11iIiiIii - I1Ii
def oOoOo ( name ) :
 if not OoooOoo == 'http://' :
  o0oOO00 = wiz . workingURL ( OoooOoo )
  if o0oOO00 == True :
   oOoooo000Oo00 = wiz . openURL ( OoooOoo ) . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
   OOoo = re . compile ( 'name="%s".+?rl="(.+?)"' % name ) . findall ( oOoooo000Oo00 )
   if len ( OOoo ) > 0 : OoO00O0OOO = OOoo [ 0 ]
   else : wiz . log ( "[Advanced Settings] ERROR: Invalid Format." ) ; wiz . LogNotify ( Oo0Ooo , "Invalid File Format" ) ; return
   if 87 - 87: Iii
   if os . path . exists ( i1i1II ) : ii1I11i = I11i11Ii . yesno ( Oo0Ooo , "[COLOR %s]Would you like to overwrite your current Advanced Settings with [COLOR %s]%s[/COLOR]?[/COLOR]" % ( ii1iII1II , Iii1I1I11iiI1 , name ) , yeslabel = "[B]Overwrite[/B]" , nolabel = "[B]Cancel[/B]" )
   else : ii1I11i = I11i11Ii . yesno ( Oo0Ooo , "[COLOR %s]Would you like to download and install [COLOR %s]%s[/COLOR]?[/COLOR]" % ( ii1iII1II , Iii1I1I11iiI1 , name ) , yeslabel = "[B]Install[/B]" , nolabel = "[B]Cancel[/B]" )
   if 89 - 89: I1111i . Iii % oOOO . oOOO - Oo0O00O0O
   if ii1I11i == 1 :
    file = wiz . openURL ( OoO00O0OOO )
    oo0ooO0O0o = open ( i1i1II , 'w' ) ;
    oo0ooO0O0o . write ( file )
    oo0ooO0O0o . close ( )
    I11i11Ii . ok ( Oo0Ooo , '[COLOR %s]AdvancedSettings.xml file has been successfully written.  Once you click okay it will force close kodi.[/COLOR]' % Iii1I1I11iiI1 )
    wiz . killxbmc ( True )
   else : wiz . log ( "[Advanced Settings] install canceled" ) ; wiz . LogNotify ( Oo0Ooo , "Write Cancelled!" ) ; return
  else : wiz . log ( "[Advanced Settings] URL not working: %s" % o0oOO00 ) ; wiz . LogNotify ( Oo0Ooo , "URL Not Working" )
 else : wiz . log ( "[Advanced Settings] not Enabled" ) ; wiz . LogNotify ( Oo0Ooo , "Not Enabled" )
 if 75 - 75: I1 + IIIi
def iIIi11 ( ) :
 oo0ooO0O0o = open ( i1i1II )
 o0000o0Oo = oo0ooO0O0o . read ( ) . replace ( '\t' , '    ' )
 wiz . TextBoxes ( Oo0Ooo , o0000o0Oo )
 oo0ooO0O0o . close ( )
 if 90 - 90: O000oo * I1
def oOOo0OoOOOoo ( ) :
 notify . autoConfig ( )
 if 88 - 88: Oo00o0o0 * iII1Ii
def II11I ( ) :
 iiiI11iIIi1 = 'http://whatismyipaddress.com/'
 if not wiz . workingURL ( iiiI11iIIi1 ) : return 'Unknown' , 'Unknown' , 'Unknown'
 o00OoooooooOo = wiz . openURL ( iiiI11iIIi1 ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 if not 'Access Denied' in o00OoooooooOo :
  iIii1I = re . compile ( 'whatismyipaddress.com/ip/(.+?)"' ) . findall ( o00OoooooooOo )
  iii11i1 = iIii1I [ 0 ] if ( len ( iIii1I ) > 0 ) else 'Unknown'
  i1IiI1I111iIi = re . compile ( '"font-size:14px;">(.+?)</td>' ) . findall ( o00OoooooooOo )
  IiiIIi1 = i1IiI1I111iIi [ 0 ] if ( len ( i1IiI1I111iIi ) > 0 ) else 'Unknown'
  iI1iIiiI = i1IiI1I111iIi [ 1 ] + ', ' + i1IiI1I111iIi [ 2 ] + ', ' + i1IiI1I111iIi [ 3 ] if ( len ( i1IiI1I111iIi ) > 2 ) else 'Unknown'
  return iii11i1 , IiiIIi1 , iI1iIiiI
 else : return 'Unknown' , 'Unknown' , 'Unknown'
 if 95 - 95: O000oo + oOOO * I1 + Oo0OO + OoOooO * I1Ii
def Ii11I1iIiiI ( ) :
 O0o0OO00 = [ 'System.FriendlyName' ,
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
 iIi11i = [ ] ; ooIII1II1iii1i = 0
 for O0OO0oOO in O0o0OO00 :
  ooooO = wiz . getInfo ( O0OO0oOO )
  oO0O0 = 0
  while ooooO == "Busy" and oO0O0 < 10 :
   ooooO = wiz . getInfo ( O0OO0oOO ) ; oO0O0 += 1 ; wiz . log ( "%s sleep %s" % ( O0OO0oOO , str ( oO0O0 ) ) ) ; xbmc . sleep ( 200 )
  iIi11i . append ( ooooO )
  ooIII1II1iii1i += 1
 iI111i11iI1 = iIi11i [ 8 ] if 'Una' in iIi11i [ 8 ] else wiz . convertSize ( int ( float ( iIi11i [ 8 ] [ : - 8 ] ) ) * 1024 * 1024 )
 III1ii = iIi11i [ 9 ] if 'Una' in iIi11i [ 9 ] else wiz . convertSize ( int ( float ( iIi11i [ 9 ] [ : - 8 ] ) ) * 1024 * 1024 )
 iI1III1iIi11 = iIi11i [ 10 ] if 'Una' in iIi11i [ 10 ] else wiz . convertSize ( int ( float ( iIi11i [ 10 ] [ : - 8 ] ) ) * 1024 * 1024 )
 i11I1I = wiz . convertSize ( int ( float ( iIi11i [ 11 ] [ : - 2 ] ) ) * 1024 * 1024 )
 oo0ooooo00o = wiz . convertSize ( int ( float ( iIi11i [ 12 ] [ : - 2 ] ) ) * 1024 * 1024 )
 OoOo = wiz . convertSize ( int ( float ( iIi11i [ 13 ] [ : - 2 ] ) ) * 1024 * 1024 )
 i111i1iIi1 , IiiIIi1 , iI1iIiiI = II11I ( )
 if 95 - 95: Oo0O00O0O + I1Ii - oO00OoOO000o / oO00OoOO000o . OooOoooOo . Oo0O00O0O
 i11iiI1111 ( '[B]Media Center Info:[/B]' , '' , icon = Ii1I1i , themeit = ii1I )
 i11iiI1111 ( '[COLOR %s]Name:[/COLOR] [COLOR %s]%s[/COLOR]' % ( ii1iII1II , Iii1I1I11iiI1 , iIi11i [ 0 ] ) , '' , icon = Ii1I1i , themeit = O0oO0 )
 i11iiI1111 ( '[COLOR %s]Version:[/COLOR] [COLOR %s]%s[/COLOR]' % ( ii1iII1II , Iii1I1I11iiI1 , iIi11i [ 1 ] ) , '' , icon = Ii1I1i , themeit = O0oO0 )
 i11iiI1111 ( '[COLOR %s]Platform:[/COLOR] [COLOR %s]%s[/COLOR]' % ( ii1iII1II , Iii1I1I11iiI1 , wiz . platform ( ) . title ( ) ) , '' , icon = Ii1I1i , themeit = O0oO0 )
 i11iiI1111 ( '[COLOR %s]CPU Usage:[/COLOR] [COLOR %s]%s[/COLOR]' % ( ii1iII1II , Iii1I1I11iiI1 , iIi11i [ 2 ] ) , '' , icon = Ii1I1i , themeit = O0oO0 )
 i11iiI1111 ( '[COLOR %s]Screen Mode:[/COLOR] [COLOR %s]%s[/COLOR]' % ( ii1iII1II , Iii1I1I11iiI1 , iIi11i [ 3 ] ) , '' , icon = Ii1I1i , themeit = O0oO0 )
 if 29 - 29: Oo0OO - OooOoooOo . I1Ii - oO00OoOO000o + Oo0OO + Oo0O00O0O
 i11iiI1111 ( '[B]Uptime:[/B]' , '' , icon = Ii1I1i , themeit = ii1I )
 i11iiI1111 ( '[COLOR %s]Current Uptime:[/COLOR] [COLOR %s]%s[/COLOR]' % ( ii1iII1II , Iii1I1I11iiI1 , iIi11i [ 6 ] ) , '' , icon = Ii1I1i , themeit = ii1I )
 i11iiI1111 ( '[COLOR %s]Total Uptime:[/COLOR] [COLOR %s]%s[/COLOR]' % ( ii1iII1II , Iii1I1I11iiI1 , iIi11i [ 7 ] ) , '' , icon = Ii1I1i , themeit = ii1I )
 if 36 - 36: OooOoooOo / Oo0OO . O000oo
 i11iiI1111 ( '[B]Local Storage:[/B]' , '' , icon = Ii1I1i , themeit = ii1I )
 i11iiI1111 ( '[COLOR %s]Used Storage:[/COLOR] [COLOR %s]%s[/COLOR]' % ( ii1iII1II , Iii1I1I11iiI1 , iI111i11iI1 ) , '' , icon = Ii1I1i , themeit = ii1I )
 i11iiI1111 ( '[COLOR %s]Free Storage:[/COLOR] [COLOR %s]%s[/COLOR]' % ( ii1iII1II , Iii1I1I11iiI1 , III1ii ) , '' , icon = Ii1I1i , themeit = ii1I )
 i11iiI1111 ( '[COLOR %s]Total Storage:[/COLOR] [COLOR %s]%s[/COLOR]' % ( ii1iII1II , Iii1I1I11iiI1 , iI1III1iIi11 ) , '' , icon = Ii1I1i , themeit = ii1I )
 if 12 - 12: I1IiiiiI
 i11iiI1111 ( '[B]Ram Usage:[/B]' , '' , icon = Ii1I1i , themeit = ii1I )
 i11iiI1111 ( '[COLOR %s]Used Memory:[/COLOR] [COLOR %s]%s[/COLOR]' % ( ii1iII1II , Iii1I1I11iiI1 , i11I1I ) , '' , icon = Ii1I1i , themeit = ii1I )
 i11iiI1111 ( '[COLOR %s]Free Memory:[/COLOR] [COLOR %s]%s[/COLOR]' % ( ii1iII1II , Iii1I1I11iiI1 , oo0ooooo00o ) , '' , icon = Ii1I1i , themeit = ii1I )
 i11iiI1111 ( '[COLOR %s]Total Memory:[/COLOR] [COLOR %s]%s[/COLOR]' % ( ii1iII1II , Iii1I1I11iiI1 , OoOo ) , '' , icon = Ii1I1i , themeit = ii1I )
 if 71 - 71: OOO00O0O . I1 . OOO00O0O - Oo0OO
 i11iiI1111 ( '[B]Network:[/B]' , '' , icon = Ii1I1i , themeit = ii1I )
 i11iiI1111 ( '[COLOR %s]Local IP:[/COLOR] [COLOR %s]%s[/COLOR]' % ( ii1iII1II , Iii1I1I11iiI1 , iIi11i [ 4 ] ) , '' , icon = Ii1I1i , themeit = ii1I )
 i11iiI1111 ( '[COLOR %s]External IP:[/COLOR] [COLOR %s]%s[/COLOR]' % ( ii1iII1II , Iii1I1I11iiI1 , i111i1iIi1 ) , '' , icon = Ii1I1i , themeit = ii1I )
 i11iiI1111 ( '[COLOR %s]Provider:[/COLOR] [COLOR %s]%s[/COLOR]' % ( ii1iII1II , Iii1I1I11iiI1 , IiiIIi1 ) , '' , icon = Ii1I1i , themeit = ii1I )
 i11iiI1111 ( '[COLOR %s]Location:[/COLOR] [COLOR %s]%s[/COLOR]' % ( ii1iII1II , Iii1I1I11iiI1 , iI1iIiiI ) , '' , icon = Ii1I1i , themeit = ii1I )
 I1i1iiiII1i ( '[COLOR %s]MacAddress:[/COLOR] [COLOR %s]%s[/COLOR]' % ( ii1iII1II , Iii1I1I11iiI1 , iIi11i [ 5 ] ) , '' , icon = Ii1I1i , themeit = ii1I )
 if 45 - 45: Iii / OoOooO / I1I11 * IIIi
 if 18 - 18: O000oo + IIIi + O000oo . oO00OoOO000o + I1111i . Oo0OO
 if 7 - 7: oO00OoOO000o + O000oo * I1Ii * I1Ii / I1 - I1IiiiiI
 if 65 - 65: Oo00o0o0 + I1I11 + I1
def oOOoo ( ) :
 xbmc . executebuiltin ( 'Runscript("special://home/addons/plugin.program.SpinzTV/ookla.py")' )
 if 6 - 6: IIIi
 if 98 - 98: Oo0O00O0O % OoOooO - OoOooO
 if 76 - 76: OooOoooOo % I1I11 - OOO00O0O / o00oO0oOo00 * Oo0OO
 if 4 - 4: oOOO * oOOO / I1I11
def Ii1Ii1Ii1I1I ( ) :
 o0o = '[COLOR green]ON[/COLOR]' ; o00o0O0O00 = '[COLOR red]OFF[/COLOR]'
 III1II1i = 'true' if I11iii1Ii == 'true' else 'false'
 iI1i1IiIIIIi = 'true' if I1IIiiIiii == 'true' else 'false'
 OooOooO0O0o0 = 'true' if O000oo0O == 'true' else 'false'
 OOO0o0 = 'true' if OOO00 == 'true' else 'false'
 IIIIII111Ii = 'true' if O000OO0 == 'true' else 'false'
 Ii1i1i = 'true' if iiiiiIIii == 'true' else 'false'
 iIi1Ii1IIiI = 'true' if oOoOooOo0o0 == 'true' else 'false'
 if 63 - 63: Oo0O00O0O % I1Ii . Iii
 iIiiii ( 'Keep Trakt Data' , 'trakt' , icon = OOoO0 , themeit = I1I1i1I )
 iIiiii ( 'Keep Real Debrid' , 'realdebrid' , icon = OO0Oooo0oOO0O , themeit = I1I1i1I )
 iIiiii ( 'Keep Login Info' , 'login' , icon = OOoO , themeit = I1I1i1I )
 i11iiI1111 ( '- Click to toggle settings -' , '' , themeit = O0oO0 )
 i11iiI1111 ( 'Save Trakt: %s' % III1II1i . replace ( 'true' , o0o ) . replace ( 'false' , o00o0O0O00 ) , 'togglesetting' , 'keeptrakt' , icon = OOoO0 , themeit = I1I1i1I )
 i11iiI1111 ( 'Save Real Debrid: %s' % iI1i1IiIIIIi . replace ( 'true' , o0o ) . replace ( 'false' , o00o0O0O00 ) , 'togglesetting' , 'keepdebrid' , icon = OO0Oooo0oOO0O , themeit = I1I1i1I )
 i11iiI1111 ( 'Save Login Info: %s' % OooOooO0O0o0 . replace ( 'true' , o0o ) . replace ( 'false' , o00o0O0O00 ) , 'togglesetting' , 'keeplogin' , icon = OOoO , themeit = I1I1i1I )
 i11iiI1111 ( 'Keep \'Sources.xml\': %s' % OOO0o0 . replace ( 'true' , o0o ) . replace ( 'false' , o00o0O0O00 ) , 'togglesetting' , 'keepsources' , icon = Ii1I1Ii , themeit = I1I1i1I )
 i11iiI1111 ( 'Keep \'Profiles.xml\': %s' % Ii1i1i . replace ( 'true' , o0o ) . replace ( 'false' , o00o0O0O00 ) , 'togglesetting' , 'keepprofiles' , icon = Ii1I1Ii , themeit = I1I1i1I )
 i11iiI1111 ( 'Keep \'Advancedsettings.xml\': %s' % IIIIII111Ii . replace ( 'true' , o0o ) . replace ( 'false' , o00o0O0O00 ) , 'togglesetting' , 'keepadvanced' , icon = Ii1I1Ii , themeit = I1I1i1I )
 i11iiI1111 ( 'Keep \'Favourites.xml\': %s' % iIi1Ii1IIiI . replace ( 'true' , o0o ) . replace ( 'false' , o00o0O0O00 ) , 'togglesetting' , 'keepfavourites' , icon = Ii1I1Ii , themeit = I1I1i1I )
 O0000OOO0 ( 'files' , 'viewType' )
 if 58 - 58: I1Ii * I1I11
 if 94 - 94: I1IiiiiI - oO00OoOO000o + o00oO0oOo00 - oOOO
def iiIi1iiI1I ( ) :
 III1II1i = '[COLOR green]ON[/COLOR]' if I11iii1Ii == 'true' else '[COLOR red]OFF[/COLOR]'
 Iiii1I = str ( IIiiiiiiIi1I1 ) if not IIiiiiiiIi1I1 == '' else 'Trakt hasnt been saved yet.'
 i11iiI1111 ( '[I]Register FREE Account at http://trakt.tv[/I]' , '' , icon = OOoO0 , themeit = O0oO0 )
 i11iiI1111 ( 'Save Trakt Data: %s' % III1II1i , 'togglesetting' , 'keeptrakt' , icon = OOoO0 , themeit = O0oO0 )
 if I11iii1Ii == 'true' : I1i1iiiII1i ( 'Last Save: %s' % str ( Iiii1I ) , '' , icon = OOoO0 , themeit = O0oO0 )
 if o0OIiII == 'No' : I1i1iiiII1i ( wiz . sep ( ) , '' , icon = OOoO0 , themeit = O0oO0 )
 if 56 - 56: i11iIiiIii - O000oo . I1
 for III1II1i in traktit . ORDER :
  Ii1i1i1i1I1Ii = iiIiI1i1 [ III1II1i ] [ 'name' ]
  O00O = iiIiI1i1 [ III1II1i ] [ 'path' ]
  II1oOo00o = iiIiI1i1 [ III1II1i ] [ 'saved' ]
  file = iiIiI1i1 [ III1II1i ] [ 'file' ]
  II111i1ii1iII = wiz . getS ( II1oOo00o )
  ooo0OoO = traktit . traktUser ( III1II1i )
  iIiiiii1i = iiIiI1i1 [ III1II1i ] [ 'icon' ] if os . path . exists ( O00O ) else OOoO0
  iiIi1IIiI = iiIiI1i1 [ III1II1i ] [ 'fanart' ] if os . path . exists ( O00O ) else Oo0oO0ooo
  O0Oo0o000oO = oO0o00oOOooO0 ( 'saveaddon' , 'Trakt' , III1II1i )
  iiI1111I11i1I = oO0o00oOOooO0 ( 'save' , 'Trakt' , III1II1i )
  O0Oo0o000oO . append ( ( ii1I % '%s Settings' % Ii1i1i1i1I1Ii , 'RunPlugin(plugin://%s/?mode=opensettings&name=%s&url=trakt)' % ( OO0o , III1II1i ) ) )
  if 85 - 85: IIIi * OooOoooOo % OOO00O0O - Oo0OO
  i11iiI1111 ( '[+]-> %s' % Ii1i1i1i1I1Ii , '' , icon = iIiiiii1i , fanart = iiIi1IIiI , themeit = O0oO0 )
  if not os . path . exists ( O00O ) : I1i1iiiII1i ( '[COLOR red]Addon Data: Not Installed[/COLOR]' , '' , icon = iIiiiii1i , fanart = iiIi1IIiI , menu = O0Oo0o000oO )
  elif not ooo0OoO : I1i1iiiII1i ( '[COLOR red]Addon Data: Not Registered[/COLOR]' , 'authtrakt' , III1II1i , icon = iIiiiii1i , fanart = iiIi1IIiI , menu = O0Oo0o000oO )
  else : I1i1iiiII1i ( '[COLOR green]Addon Data: %s[/COLOR]' % ooo0OoO , 'authtrakt' , III1II1i , icon = iIiiiii1i , fanart = iiIi1IIiI , menu = O0Oo0o000oO )
  if II111i1ii1iII == "" :
   if os . path . exists ( file ) : I1i1iiiII1i ( '[COLOR red]Saved Data: Save File Found(Import Data)[/COLOR]' , 'importtrakt' , III1II1i , icon = iIiiiii1i , fanart = iiIi1IIiI , menu = iiI1111I11i1I )
   else : I1i1iiiII1i ( '[COLOR red]Saved Data: Not Saved[/COLOR]' , 'savetrakt' , III1II1i , icon = iIiiiii1i , fanart = iiIi1IIiI , menu = iiI1111I11i1I )
  else : I1i1iiiII1i ( '[COLOR green]Saved Data: %s[/COLOR]' % II111i1ii1iII , '' , icon = iIiiiii1i , fanart = iiIi1IIiI , menu = iiI1111I11i1I )
  if 37 - 37: Iii . oOOO * oOOO * I1 * OoOooO
 if o0OIiII == 'No' : I1i1iiiII1i ( wiz . sep ( ) , '' , themeit = O0oO0 )
 i11iiI1111 ( 'Save All Trakt Data' , 'savetrakt' , 'all' , icon = OOoO0 , themeit = O0oO0 )
 i11iiI1111 ( 'Recover All Saved Trakt Data' , 'restoretrakt' , 'all' , icon = OOoO0 , themeit = O0oO0 )
 i11iiI1111 ( 'Import Trakt Data' , 'importtrakt' , 'all' , icon = OOoO0 , themeit = O0oO0 )
 i11iiI1111 ( 'Clear All Saved Trakt Data' , 'cleartrakt' , 'all' , icon = OOoO0 , themeit = O0oO0 )
 i11iiI1111 ( 'Clear All Addon Data' , 'addontrakt' , 'all' , icon = OOoO0 , themeit = O0oO0 )
 O0000OOO0 ( 'files' , 'viewType' )
 if 83 - 83: Iii / I1111i
def OOo000OO000 ( ) :
 iI1i1IiIIIIi = '[COLOR green]ON[/COLOR]' if I1IIiiIiii == 'true' else '[COLOR red]OFF[/COLOR]'
 Iiii1I = str ( I1IIIii ) if not I1IIIii == '' else 'Real Debrid hasnt been saved yet.'
 i11iiI1111 ( '[I]http://real-debrid.com is a PAID service.[/I]' , '' , icon = OO0Oooo0oOO0O , themeit = O0oO0 )
 i11iiI1111 ( 'Save Real Debrid Data: %s' % iI1i1IiIIIIi , 'togglesetting' , 'keepdebrid' , icon = OO0Oooo0oOO0O , themeit = O0oO0 )
 if I1IIiiIiii == 'true' : I1i1iiiII1i ( 'Last Save: %s' % str ( Iiii1I ) , '' , icon = OO0Oooo0oOO0O , themeit = O0oO0 )
 if o0OIiII == 'No' : I1i1iiiII1i ( wiz . sep ( ) , '' , icon = OO0Oooo0oOO0O , themeit = O0oO0 )
 if 83 - 83: o00oO0oOo00 % Oo00o0o0 + I1Ii % i11iIiiIii + OoOooO
 for OoOOoooO000 in debridit . ORDER :
  Ii1i1i1i1I1Ii = oO0O00oOOoooO [ OoOOoooO000 ] [ 'name' ]
  O00O = oO0O00oOOoooO [ OoOOoooO000 ] [ 'path' ]
  II1oOo00o = oO0O00oOOoooO [ OoOOoooO000 ] [ 'saved' ]
  file = oO0O00oOOoooO [ OoOOoooO000 ] [ 'file' ]
  II111i1ii1iII = wiz . getS ( II1oOo00o )
  ooo0OoO = debridit . debridUser ( OoOOoooO000 )
  iIiiiii1i = oO0O00oOOoooO [ OoOOoooO000 ] [ 'icon' ] if os . path . exists ( O00O ) else OO0Oooo0oOO0O
  iiIi1IIiI = oO0O00oOOoooO [ OoOOoooO000 ] [ 'fanart' ] if os . path . exists ( O00O ) else Oo0oO0ooo
  O0Oo0o000oO = oO0o00oOOooO0 ( 'saveaddon' , 'Debrid' , OoOOoooO000 )
  iiI1111I11i1I = oO0o00oOOooO0 ( 'save' , 'Debrid' , OoOOoooO000 )
  O0Oo0o000oO . append ( ( ii1I % '%s Settings' % Ii1i1i1i1I1Ii , 'RunPlugin(plugin://%s/?mode=opensettings&name=%s&url=debrid)' % ( OO0o , OoOOoooO000 ) ) )
  if 85 - 85: OOO00O0O % I1Ii + IIIi / I1IiiiiI % Oo0O00O0O
  i11iiI1111 ( '[+]-> %s' % Ii1i1i1i1I1Ii , '' , icon = iIiiiii1i , fanart = iiIi1IIiI , themeit = O0oO0 )
  if not os . path . exists ( O00O ) : i11iiI1111 ( '[COLOR red]Addon Data: Not Installed[/COLOR]' , '' , icon = iIiiiii1i , fanart = iiIi1IIiI , menu = O0Oo0o000oO )
  elif not ooo0OoO : i11iiI1111 ( '[COLOR red]Addon Data: Not Registered[/COLOR]' , 'authdebrid' , OoOOoooO000 , icon = iIiiiii1i , fanart = iiIi1IIiI , menu = O0Oo0o000oO )
  else : i11iiI1111 ( '[COLOR green]Addon Data: %s[/COLOR]' % ooo0OoO , 'authdebrid' , OoOOoooO000 , icon = iIiiiii1i , fanart = iiIi1IIiI , menu = O0Oo0o000oO )
  if II111i1ii1iII == "" :
   if os . path . exists ( file ) : i11iiI1111 ( '[COLOR red]Saved Data: Save File Found(Import Data)[/COLOR]' , 'importdebrid' , OoOOoooO000 , icon = iIiiiii1i , fanart = iiIi1IIiI , menu = iiI1111I11i1I )
   else : i11iiI1111 ( '[COLOR red]Saved Data: Not Saved[/COLOR]' , 'savedebrid' , OoOOoooO000 , icon = iIiiiii1i , fanart = iiIi1IIiI , menu = iiI1111I11i1I )
  else : i11iiI1111 ( '[COLOR green]Saved Data: %s[/COLOR]' % II111i1ii1iII , '' , icon = iIiiiii1i , fanart = iiIi1IIiI , menu = iiI1111I11i1I )
  if 42 - 42: I1111i * Iii
 if o0OIiII == 'No' : I1i1iiiII1i ( wiz . sep ( ) , '' , themeit = O0oO0 )
 i11iiI1111 ( 'Save All Real Debrid Data' , 'savedebrid' , 'all' , icon = OO0Oooo0oOO0O , themeit = O0oO0 )
 i11iiI1111 ( 'Recover All Saved Real Debrid Data' , 'restoredebrid' , 'all' , icon = OO0Oooo0oOO0O , themeit = O0oO0 )
 i11iiI1111 ( 'Import Real Debrid Data' , 'importdebrid' , 'all' , icon = OO0Oooo0oOO0O , themeit = O0oO0 )
 i11iiI1111 ( 'Clear All Saved Real Debrid Data' , 'cleardebrid' , 'all' , icon = OO0Oooo0oOO0O , themeit = O0oO0 )
 i11iiI1111 ( 'Clear All Addon Data' , 'addondebrid' , 'all' , icon = OO0Oooo0oOO0O , themeit = O0oO0 )
 setView1 ( 'files' , 'viewType' )
 if 23 - 23: Oo00o0o0 * I1111i - Oo0O00O0O * Oo0O00O0O % iII1Ii + I1
def ii1I1I1i1i11i ( ) :
 iI1i1IIiiiI1 = glob . glob ( os . path . join ( IiI , '*/' ) )
 for Iiii111 in sorted ( iI1i1IIiiiI1 , key = lambda ooIII1II1iii1i : ooIII1II1iii1i ) :
  Ooooo = Iiii111 . replace ( IiI , '' ) . replace ( '\\' , '' ) . replace ( '/' , '' )
  iIiiiii1i = os . path . join ( Iiii111 , 'icon.png' )
  iiIi1IIiI = os . path . join ( Iiii111 , 'fanart.png' )
  if Ooooo in ooOOoooooo : pass
  elif Ooooo == 'packages' : pass
  else :
   O0O0ooOoOO0OO = Ooooo
   I1iiIiiii1111 = { 'audio.' : '[COLOR orange][AUDIO] [/COLOR]' , 'metadata.' : '[COLOR cyan][METADATA] [/COLOR]' , 'module.' : '[COLOR orange][MODULE] [/COLOR]' , 'plugin.' : '[COLOR blue][PLUGIN] [/COLOR]' , 'program.' : '[COLOR orange][PROGRAM] [/COLOR]' , 'repository.' : '[COLOR gold][REPO] [/COLOR]' , 'script.' : '[COLOR green][SCRIPT] [/COLOR]' , 'service.' : '[COLOR green][SERVICE] [/COLOR]' , 'skin.' : '[COLOR dodgerblue][SKIN] [/COLOR]' , 'video.' : '[COLOR orange][VIDEO] [/COLOR]' , 'weather.' : '[COLOR yellow][WEATHER] [/COLOR]' }
   for I1ii1i11i in I1iiIiiii1111 :
    O0O0ooOoOO0OO = O0O0ooOoOO0OO . replace ( I1ii1i11i , I1iiIiiii1111 [ I1ii1i11i ] )
   i11iiI1111 ( '[COLOR red][B][REMOVE][/B][/COLOR] %s' % O0O0ooOoOO0OO , 'removeaddon' , Ooooo , icon = iIiiiii1i , fanart = iiIi1IIiI , themeit = ii1I )
 O0000OOO0 ( 'files' , 'viewType' )
 if 86 - 86: OoOooO % OooOoooOo . I1 . I1Ii
def IiI1II11ii1ii ( ) :
 if os . path . exists ( IiII ) :
  i11iiI1111 ( '[COLOR red][B][REMOVE][/B][/COLOR] All Addon_Data' , 'removedata' , 'all' , themeit = ii1I )
  i11iiI1111 ( '[COLOR red][B][REMOVE][/B][/COLOR] All Addon_Data for Uninstalled Addons' , 'removedata' , 'uninstalled' , themeit = ii1I )
  i11iiI1111 ( '[COLOR red][B][REMOVE][/B][/COLOR] All Empty Folders in Addon_Data' , 'removedata' , 'empty' , themeit = ii1I )
  i11iiI1111 ( '[COLOR red][B][REMOVE][/B][/COLOR] %s Addon_Data' % Oo0Ooo , 'resetaddon' , themeit = ii1I )
  if o0OIiII == 'No' : I1i1iiiII1i ( wiz . sep ( ) , '' , themeit = O0oO0 )
  iI1i1IIiiiI1 = glob . glob ( os . path . join ( IiII , '*/' ) )
  for Iiii111 in sorted ( iI1i1IIiiiI1 , key = lambda ooIII1II1iii1i : ooIII1II1iii1i ) :
   Ooooo = Iiii111 . replace ( IiII , '' ) . replace ( '\\' , '' ) . replace ( '/' , '' )
   iIiiiii1i = os . path . join ( Iiii111 . replace ( IiII , IiI ) , 'icon.png' )
   iiIi1IIiI = os . path . join ( Iiii111 . replace ( IiII , IiI ) , 'fanart.png' )
   O0O0ooOoOO0OO = Ooooo
   I1iiIiiii1111 = { 'audio.' : '[COLOR orange][AUDIO] [/COLOR]' , 'metadata.' : '[COLOR cyan][METADATA] [/COLOR]' , 'module.' : '[COLOR orange][MODULE] [/COLOR]' , 'plugin.' : '[COLOR blue][PLUGIN] [/COLOR]' , 'program.' : '[COLOR orange][PROGRAM] [/COLOR]' , 'repository.' : '[COLOR gold][REPO] [/COLOR]' , 'script.' : '[COLOR green][SCRIPT] [/COLOR]' , 'service.' : '[COLOR green][SERVICE] [/COLOR]' , 'skin.' : '[COLOR dodgerblue][SKIN] [/COLOR]' , 'video.' : '[COLOR orange][VIDEO] [/COLOR]' , 'weather.' : '[COLOR yellow][WEATHER] [/COLOR]' }
   for I1ii1i11i in I1iiIiiii1111 :
    O0O0ooOoOO0OO = O0O0ooOoOO0OO . replace ( I1ii1i11i , I1iiIiiii1111 [ I1ii1i11i ] )
   if Ooooo in ooOOoooooo : O0O0ooOoOO0OO = '[COLOR green][B][PROTECTED][/B][/COLOR] %s' % O0O0ooOoOO0OO
   else : O0O0ooOoOO0OO = '[COLOR red][B][REMOVE][/B][/COLOR] %s' % O0O0ooOoOO0OO
   I1i1iiiII1i ( ' %s' % O0O0ooOoOO0OO , 'removedata' , Ooooo , icon = iIiiiii1i , fanart = iiIi1IIiI , themeit = ii1I )
 else :
  i11iiI1111 ( 'No Addon data folder found.' , '' , themeit = O0oO0 )
 O0000OOO0 ( 'files' , 'viewType' )
 if 51 - 51: oO00OoOO000o * oO00OoOO000o
def OOo000o0 ( ) :
 i11iiI1111 ( "[I][B][COLOR red]!!Notice: Disabling Some Addons Can Cause Issues!![/COLOR][/B][/I]" , '' , icon = Ii1I1i )
 iI1i1IIiiiI1 = glob . glob ( os . path . join ( IiI , '*/' ) )
 for Iiii111 in sorted ( iI1i1IIiiiI1 , key = lambda ooIII1II1iii1i : ooIII1II1iii1i ) :
  if OO0o in Iiii111 : continue
  o00oo0OO0 = os . path . join ( Iiii111 , 'addon.xml' )
  if os . path . exists ( o00oo0OO0 ) :
   iI1i1IIiiiI1 = Iiii111 . replace ( IiI , '' ) [ 1 : - 1 ]
   oo0ooO0O0o = open ( o00oo0OO0 )
   o0000o0Oo = oo0ooO0O0o . read ( ) . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
   OOoo = re . compile ( '<addo.+?id="(.+?)".+?>' ) . findall ( o0000o0Oo )
   oooii1iiIi1 = re . compile ( '<addo.+? name="(.+?)".+?>' ) . findall ( o0000o0Oo )
   try :
    Oo0O0Oo00O = OOoo [ 0 ]
    Ii1i1i1i1I1Ii = oooii1iiIi1 [ 0 ]
   except :
    continue
   try :
    Oo0O0O000 = xbmcaddon . Addon ( id = Oo0O0Oo00O )
    Ii1ii111i1 = "[COLOR green][Enabled][/COLOR]"
    oO0o000OooOoo = "false"
   except :
    Ii1ii111i1 = "[COLOR red][Disabled][/COLOR]"
    oO0o000OooOoo = "true"
    pass
   iIiiiii1i = os . path . join ( Iiii111 , 'icon.png' ) if os . path . exists ( os . path . join ( Iiii111 , 'icon.png' ) ) else o0oOoO00o
   iiIi1IIiI = os . path . join ( Iiii111 , 'fanart.jpg' ) if os . path . exists ( os . path . join ( Iiii111 , 'fanart.jpg' ) ) else Oo0oO0ooo
   i11iiI1111 ( "%s %s" % ( Ii1ii111i1 , Ii1i1i1i1I1Ii ) , 'toggleaddon' , iI1i1IIiiiI1 , oO0o000OooOoo , icon = iIiiiii1i , fanart = iiIi1IIiI )
   oo0ooO0O0o . close ( )
 O0000OOO0 ( 'files' , 'viewType' )
 if 8 - 8: oOOO + Oo0OO / OoOooO * Oo0O00O0O * I1 % I1IiiiiI
def oO0o0oO ( ) :
 IioO0O = [ 'Every Startup' , 'Every Day' , 'Every Three Days' , 'Every Weekly' ]
 O0OOO00 = I11i11Ii . select ( "[COLOR %s]How often would you list to Auto Clean on Startup?[/COLOR]" % Iii1I1I11iiI1 , IioO0O )
 if not O0OOO00 == - 1 :
  wiz . setS ( 'autocleanfeq' , str ( O0OOO00 ) )
  wiz . LogNotify ( 'Auto Clean Up' , 'Fequency Now %s' % IioO0O [ O0OOO00 ] )
  if 62 - 62: i11iIiiIii + I1I11 + OooOoooOo
  if 69 - 69: I1I11
  if 63 - 63: iII1Ii / I1I11 * O000oo . I1111i
  if 85 - 85: i11iIiiIii / i11iIiiIii . iII1Ii . OoOooO
def OooOo ( ) :
 i11iiI1111 ( 'Test Update' , 'testupdate' , themeit = I1I1i1I )
 i11iiI1111 ( 'Test First Run' , 'testfirst' , themeit = I1I1i1I )
 O0000OOO0 ( 'files' , 'viewType' )
 I1i1iiiII1i ( 'Convert Paths to special' , 'convertpath' , icon = o0oOoO00o , themeit = I1I1i1I )
 i11iiI1111 ( 'Test Notifications' , 'testnotify' , icon = o0oOoO00o , themeit = I1I1i1I )
 if 67 - 67: oOOO / OoOooO
 if 88 - 88: I1I11 - IIIi
 if 63 - 63: Iii * Oo0O00O0O
 if 19 - 19: Iii - o00oO0oOo00 . O000oo . I1I11 / IIIi
 if 87 - 87: I1I11 - Oo0OO - IIIi + oOOO % O000oo / i11iIiiIii
def i1iIIII1iiIIi ( name , type , theme = None ) :
 i1I1IiI1ii = wiz . checkBuild ( name , 'url' )
 if i1I1IiI1ii == False :
  wiz . LogNotify ( Oo0Ooo , "Unabled to find build" )
  return
 if type == 'gui' :
  if name == i11 :
   O00OOoOOOO00O = I11i11Ii . yesno ( Oo0Ooo , '[COLOR %s]Would you like to apply the guifix for:' % Iii1I1I11iiI1 , '[COLOR %s]%s[/COLOR]?[/COLOR]' % ( ii1iII1II , name ) , nolabel = '[B]No, Cancel[/B]' , yeslabel = '[B]Apply Fix[/B]' )
  else :
   O00OOoOOOO00O = I11i11Ii . yesno ( "%s - [COLOR red]WARNING!![/COLOR]" % Oo0Ooo , "[COLOR %s][COLOR %s]%s[/COLOR] community build is not currently installed." % ( Iii1I1I11iiI1 , ii1iII1II , name ) , "Would you like to apply the guiFix anyways?.[/COLOR]" , nolabel = '[B]No, Cancel[/B]' , yeslabel = '[B]Apply Fix[/B]' )
  if O00OOoOOOO00O :
   Ooo0OOO = wiz . checkBuild ( name , 'gui' )
   ooooOoo0OO = name . replace ( '\\' , '' ) . replace ( '/' , '' ) . replace ( ':' , '' ) . replace ( '*' , '' ) . replace ( '?' , '' ) . replace ( '"' , '' ) . replace ( '<' , '' ) . replace ( '>' , '' ) . replace ( '|' , '' )
   if not wiz . workingURL ( Ooo0OOO ) == True : wiz . LogNotify ( Oo0Ooo , 'GuiFix: [COLOR red]Invalid Zip Url![/COLOR]' ) ; return
   if not os . path . exists ( IiiIII111iI ) : os . makedirs ( IiiIII111iI )
   oO00oOo . create ( Oo0Ooo , '[COLOR %s][B]Downloading GuiFix:[/B][/COLOR] [COLOR %s]%s[/COLOR]' % ( Iii1I1I11iiI1 , ii1iII1II , name ) , '' , 'Please Wait' )
   IiI1IIIII1I = os . path . join ( IiiIII111iI , '%s_guisettings.zip' % ooooOoo0OO )
   try : os . remove ( IiI1IIIII1I )
   except : pass
   downloader . download ( Ooo0OOO , IiI1IIIII1I , oO00oOo )
   xbmc . sleep ( 500 )
   I1I1IiIi1 = '[COLOR %s][B]Installing:[/B][/COLOR] [COLOR %s]%s[/COLOR]' % ( Iii1I1I11iiI1 , ii1iII1II , name )
   oO00oOo . update ( 0 , I1I1IiIi1 , '' , 'Please Wait' )
   extract . all ( IiI1IIIII1I , Oo , oO00oOo , title = I1I1IiIi1 )
   oO00oOo . close ( )
   wiz . defaultSkin ( )
   wiz . lookandFeelData ( 'save' )
   I11i11Ii . ok ( Oo0Ooo , "[COLOR %s]To save changes you now need to force close Kodi, Press OK to force close Kodi[/COLOR]" % Iii1I1I11iiI1 )
   wiz . killxbmc ( 'true' )
  else :
   wiz . LogNotify ( Oo0Ooo , 'GuiFix: [COLOR red]Cancelled![/COLOR]' )
 elif type == 'fresh' :
  Oo0 ( name )
 elif type == 'normal' :
  if iiiI1 == 'normal' :
   if I11iii1Ii == 'true' :
    traktit . autoUpdate ( 'all' )
    wiz . setS ( 'traktlastsave' , str ( OOoOO0oo0ooO ) )
   if I1IIiiIiii == 'true' :
    debridit . autoUpdate ( 'all' )
    wiz . setS ( 'debridlastsave' , str ( OOoOO0oo0ooO ) )
   if O000oo0O == 'true' :
    loginit . autoUpdate ( 'all' )
    wiz . setS ( 'loginlastsave' , str ( OOoOO0oo0ooO ) )
  O0000Oo00o = int ( O0o0O00Oo0o0 ) ; II1ii = int ( float ( wiz . checkBuild ( name , 'kodi' ) ) )
  if not O0000Oo00o == II1ii :
   if O0000Oo00o == 16 and II1ii <= 15 : Ii1IIiiIIi = False
   else : Ii1IIiiIIi = True
  else : Ii1IIiiIIi = False
  if Ii1IIiiIIi == True :
   o00iIiiiII = I11i11Ii . yesno ( "%s - [COLOR red]WARNING!![/COLOR]" % Oo0Ooo , '[COLOR %s]There is a chance that the skin will not appear correctly' % Iii1I1I11iiI1 , 'When installing a %s build on a Kodi %s install' % ( wiz . checkBuild ( name , 'kodi' ) , O0o0O00Oo0o0 ) , 'Would you still like to install: [COLOR %s]%s v%s[/COLOR]?[/COLOR]' % ( ii1iII1II , name , wiz . checkBuild ( name , 'version' ) ) , nolabel = '[B]No, Cancel[/B]' , yeslabel = '[B]Yes, Install[/B]' )
  else :
   o00iIiiiII = I11i11Ii . yesno ( Oo0Ooo , '[COLOR %s]Would you like to Download and Install:' % Iii1I1I11iiI1 , '[COLOR %s]%s v%s[/COLOR]?[/COLOR]' % ( ii1iII1II , name , wiz . checkBuild ( name , 'version' ) ) , nolabel = '[B]No, Cancel[/B]' , yeslabel = '[B]Yes, Install[/B]' )
  if o00iIiiiII :
   wiz . clearS ( 'build' )
   Ooo0OOO = wiz . checkBuild ( name , 'url' )
   ooooOoo0OO = name . replace ( '\\' , '' ) . replace ( '/' , '' ) . replace ( ':' , '' ) . replace ( '*' , '' ) . replace ( '?' , '' ) . replace ( '"' , '' ) . replace ( '<' , '' ) . replace ( '>' , '' ) . replace ( '|' , '' )
   if not wiz . workingURL ( Ooo0OOO ) == True : wiz . LogNotify ( Oo0Ooo , 'Build Install: [COLOR red]Invalid Zip Url![/COLOR]' ) ; return
   if not os . path . exists ( IiiIII111iI ) : os . makedirs ( IiiIII111iI )
   oO00oOo . create ( Oo0Ooo , '[COLOR %s][B]Downloading:[/B][/COLOR] [COLOR %s]%s v%s[/COLOR]' % ( Iii1I1I11iiI1 , ii1iII1II , name , wiz . checkBuild ( name , 'version' ) ) , '' , 'Please Wait' )
   IiI1IIIII1I = os . path . join ( IiiIII111iI , '%s.zip' % ooooOoo0OO )
   try : os . remove ( IiI1IIIII1I )
   except : pass
   downloader . download ( Ooo0OOO , IiI1IIIII1I , oO00oOo )
   xbmc . sleep ( 500 )
   I1I1IiIi1 = '[COLOR %s][B]Installing:[/B][/COLOR] [COLOR %s]%s v%s[/COLOR]' % ( Iii1I1I11iiI1 , ii1iII1II , name , wiz . checkBuild ( name , 'version' ) )
   oO00oOo . update ( 0 , I1I1IiIi1 , '' , 'Please Wait' )
   oOO0o0oo0 , oOo000O , iII = extract . all ( IiI1IIIII1I , OOOo0 , oO00oOo , title = I1I1IiIi1 )
   if int ( float ( oOO0o0oo0 ) ) > 0 :
    wiz . lookandFeelData ( 'save' )
    wiz . defaultSkin ( )
    wiz . setS ( 'buildname' , name )
    wiz . setS ( 'buildversion' , wiz . checkBuild ( name , 'version' ) )
    wiz . setS ( 'buildtheme' , '' )
    wiz . setS ( 'latestversion' , wiz . checkBuild ( name , 'version' ) )
    wiz . setS ( 'lastbuildcheck' , str ( O0i1II1Iiii1I11 ) )
    wiz . setS ( 'installed' , 'true' )
    wiz . setS ( 'extract' , str ( oOO0o0oo0 ) )
    wiz . setS ( 'errors' , str ( oOo000O ) )
    wiz . log ( 'INSTALLED %s: [ERRORS:%s]' % ( oOO0o0oo0 , oOo000O ) )
    if int ( float ( oOo000O ) ) > 0 :
     O00OOoOOOO00O = I11i11Ii . yesno ( Oo0Ooo , '[COLOR %s][COLOR %s]%s v%s[/COLOR]' % ( Iii1I1I11iiI1 , ii1iII1II , name , wiz . checkBuild ( name , 'version' ) ) , 'Completed: [COLOR %s]%s%s[/COLOR] [Errors:[COLOR %s]%s[/COLOR]]' % ( ii1iII1II , oOO0o0oo0 , '%' , ii1iII1II , oOo000O ) , 'Would you like to view the errors?[/COLOR]' , nolabel = '[B]No Thanks[/B]' , yeslabel = '[B]View Errors[/B]' )
     if O00OOoOOOO00O :
      if isinstance ( oOo000O , unicode ) :
       iII = iII . encode ( 'utf-8' )
      wiz . TextBoxes ( Oo0Ooo , iII )
    oO00oOo . close ( )
    IIi1iiii1iI = wiz . checkBuild ( name , 'theme' )
    if not IIi1iiii1iI == 'http://' :
     Ii1I1 = wiz . workingURL ( IIi1iiii1iI )
     if Ii1I1 == True : i1iIIII1iiIIi ( name , 'theme' )
     else : wiz . log ( "Theme File Not Working: %s" % Ii1I1 )
    I11i11Ii . ok ( Oo0Ooo , "[COLOR %s]To save changes you now need to force close Kodi, Press OK to force close Kodi[/COLOR]" % Iii1I1I11iiI1 )
    wiz . killxbmc ( 'true' )
   else :
    if isinstance ( oOo000O , unicode ) :
     iII = iII . encode ( 'utf-8' )
    wiz . TextBoxes ( "%s: Error Installing Build" % Oo0Ooo , iII )
  else :
   wiz . LogNotify ( Oo0Ooo , 'Build Install: [COLOR red]Cancelled![/COLOR]' )
 elif type == 'theme' :
  if theme == None :
   IIi1iiii1iI = wiz . checkBuild ( name , 'theme' )
   OO0ooO0 = [ ]
   if not IIi1iiii1iI == 'http://' and wiz . workingURL ( IIi1iiii1iI ) == True :
    oOoooo000Oo00 = wiz . openURL ( IIi1iiii1iI ) . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
    OOoo = re . compile ( 'name="(.+?)"' ) . findall ( oOoooo000Oo00 )
    if len ( OOoo ) > 0 :
     if I11i11Ii . yesno ( Oo0Ooo , "[COLOR %s]The Build [COLOR %s]%s[/COLOR] comes with [COLOR %s]%s[/COLOR] different themes" % ( Iii1I1I11iiI1 , ii1iII1II , name , ii1iII1II , len ( OOoo ) ) , "Would you like to install one now?[/COLOR]" , yeslabel = "[B]Install Theme[/B]" , nolabel = "[B]Cancel Themes[/B]" ) :
      for Oo000o in OOoo :
       OO0ooO0 . append ( Oo000o )
      wiz . log ( "Theme List: %s " % str ( OO0ooO0 ) )
      OoOooOO0oOOo0O = I11i11Ii . select ( Oo0Ooo , OO0ooO0 )
      wiz . log ( "Theme install selected: %s" % OoOooOO0oOOo0O )
      if not OoOooOO0oOOo0O == - 1 : theme = OO0ooO0 [ OoOooOO0oOOo0O ] ; I1II = True
      else : wiz . LogNotify ( Oo0Ooo , 'Theme Install: [COLOR red]Cancelled![/COLOR]' ) ; return
     else : wiz . LogNotify ( Oo0Ooo , 'Theme Install: [COLOR red]Cancelled![/COLOR]' ) ; return
   else : wiz . LogNotify ( Oo0Ooo , 'Theme Install: [COLOR red]None Found![/COLOR]' )
  else : I1II = I11i11Ii . yesno ( Oo0Ooo , '[COLOR %s]Would you like to install the theme:' % Iii1I1I11iiI1 , '[COLOR %s]%s[/COLOR]' % ( ii1iII1II , theme ) , 'for [COLOR %s]%s v%s[/COLOR]?[/COLOR]' % ( ii1iII1II , name , wiz . checkBuild ( name , 'version' ) ) , yeslabel = "[B]Install Theme[/B]" , nolabel = "[B]Cancel Themes[/B]" )
  if I1II :
   iIIi1Ii1III = wiz . checkTheme ( name , theme , 'url' )
   ooooOoo0OO = name . replace ( '\\' , '' ) . replace ( '/' , '' ) . replace ( ':' , '' ) . replace ( '*' , '' ) . replace ( '?' , '' ) . replace ( '"' , '' ) . replace ( '<' , '' ) . replace ( '>' , '' ) . replace ( '|' , '' )
   if not wiz . workingURL ( iIIi1Ii1III ) == True : wiz . LogNotify ( Oo0Ooo , 'Theme Install: [COLOR red]Invalid Zip Url![/COLOR]' ) ; return False
   if not os . path . exists ( IiiIII111iI ) : os . makedirs ( IiiIII111iI )
   oO00oOo . create ( Oo0Ooo , '[COLOR %s][B]Downloading:[/B][/COLOR] [COLOR %s]%s[/COLOR]' % ( Iii1I1I11iiI1 , ii1iII1II , name ) , '' , 'Please Wait' )
   IiI1IIIII1I = os . path . join ( IiiIII111iI , '%s.zip' % ooooOoo0OO )
   try : os . remove ( IiI1IIIII1I )
   except : pass
   downloader . download ( iIIi1Ii1III , IiI1IIIII1I , oO00oOo )
   xbmc . sleep ( 500 )
   oO00oOo . update ( 0 , "" , "Installing %s " % name )
   Oooo00 = False
   if iiiI1 not in [ "fresh" , "normal" ] :
    Oooo00 = iii1II1iI1IIi ( IiI1IIIII1I ) if not wiz . currSkin ( ) in [ 'skin.confluence' , 'skin.estuary' ] else False
    if Oooo00 == True :
     wiz . lookandFeelData ( 'save' )
     Ii11iiI1 = 'skin.confluence' if O0o0O00Oo0o0 < 17 else 'skin.estuary'
     oO0OOOoooO00o0o = xbmc . getSkinDir ( )
     if I11i11Ii . yesno ( Oo0Ooo , "[COLOR %s]Installing the theme [COLOR %s]%s[/COLOR] requires the skin to be swaped back to [COLOR %s]%s[/COLOR]" % ( Iii1I1I11iiI1 , ii1iII1II , theme , ii1iII1II , Ii11iiI1 [ 5 : ] ) , "Would you like to switch the skin?[/COLOR]" , yeslabel = "[B]Switch Skin[/B]" , nolabel = "[B]Don't Switch[/B]" ) :
      skinSwitch . swapSkins ( Ii11iiI1 )
      ooIII1II1iii1i = 0
      xbmc . sleep ( 1000 )
      while not xbmc . getCondVisibility ( "Window.isVisible(yesnodialog)" ) and ooIII1II1iii1i < 150 :
       ooIII1II1iii1i += 1
       xbmc . sleep ( 200 )
       if 10 - 10: I1IiiiiI - i11iIiiIii . oO00OoOO000o % OooOoooOo
      if xbmc . getCondVisibility ( "Window.isVisible(yesnodialog)" ) :
       wiz . ebi ( 'SendClick(11)' )
      else : wiz . LogNotify ( Oo0Ooo , 'Theme Install: [COLOR red]Skin Swap Timed Out![/COLOR]' ) ; return
      xbmc . sleep ( 500 )
     else : wiz . log ( "Theme Installer: %s skin swap ignored." % theme )
   I1I1IiIi1 = '[COLOR %s][B]Installing Theme:[/B][/COLOR] [COLOR %s]%s[/COLOR]' % ( Iii1I1I11iiI1 , ii1iII1II , name )
   oO00oOo . update ( 0 , I1I1IiIi1 , '' , 'Please Wait' )
   oOO0o0oo0 , oOo000O , iII = extract . all ( IiI1IIIII1I , OOOo0 , oO00oOo , title = I1I1IiIi1 )
   wiz . setS ( 'buildtheme' , theme )
   wiz . log ( 'INSTALLED %s: [ERRORS:%s]' % ( oOO0o0oo0 , oOo000O ) )
   oO00oOo . close ( )
   if iiiI1 not in [ "fresh" , "normal" ] :
    if Oooo00 == True :
     skinSwitch . swapSkins ( oO0OOOoooO00o0o )
     ooIII1II1iii1i = 0
     xbmc . sleep ( 1000 )
     while not xbmc . getCondVisibility ( "Window.isVisible(yesnodialog)" ) and ooIII1II1iii1i < 150 :
      ooIII1II1iii1i += 1
      xbmc . sleep ( 200 )
      if 78 - 78: O000oo * oOOO . oOOO - IIIi . O000oo
     if xbmc . getCondVisibility ( "Window.isVisible(yesnodialog)" ) :
      wiz . ebi ( 'SendClick(11)' )
     else : wiz . LogNotify ( Oo0Ooo , 'Theme Install: [COLOR red]Skin Swap Timed Out![/COLOR]' ) ; return
     wiz . lookandFeelData ( 'restore' )
    else :
     wiz . ebi ( "ReloadSkin()" )
     xbmc . sleep ( 1000 )
     wiz . ebi ( "Container.Refresh" )
  else :
   wiz . LogNotify ( Oo0Ooo , 'Theme Install: [COLOR red]Cancelled![/COLOR]' )
   if 30 - 30: Oo0OO + Oo0OO % Iii - o00oO0oOo00 - oO00OoOO000o
def iii1II1iI1IIi ( path ) :
 i111IiiI1Ii = zipfile . ZipFile ( path )
 for OooOOOOOo in i111IiiI1Ii . infolist ( ) :
  if '/settings.xml' in OooOOOOOo . filename :
   return True
 return False
 if 50 - 50: I1111i + Oo0OO + O0OoOO0o
def ii11iiI11I ( path ) :
 i111IiiI1Ii = zipfile . ZipFile ( path )
 for OooOOOOOo in i111IiiI1Ii . infolist ( ) :
  if '/guisettings.xml' in OooOOOOOo . filename :
   return True
 return False
 if 96 - 96: O000oo + i11iIiiIii - oOOO . Oo0OO
 if 31 - 31: O000oo % i11iIiiIii - Iii
 if 89 - 89: I1I11 % O000oo
 if 35 - 35: oO00OoOO000o + I1111i - I1I11 % Oo00o0o0 % o00oO0oOo00 % I1I11
def oOO00oO00O0OO ( apk , url , Brackets ) :
 if wiz . platform ( ) == 'android' :
  if apk in [ 'kodi' , 'spmc' ] :
   O00OOoOOOO00O = I11i11Ii . yesno ( Oo0Ooo , "Would you like to download and install:" , "%s (v%s)" % ( apk . upper ( ) , wiz . latestApk ( apk , 'version' ) ) )
   if not O00OOoOOOO00O : wiz . LogNotify ( Oo0Ooo , '[COLOR red]ERROR:[/COLOR] Install Cancelled' ) ; return
   ii1IIiII111I = "%s v%s" % ( apk . upper ( ) , wiz . latestApk ( apk , 'version' ) )
  else :
   O00OOoOOOO00O = I11i11Ii . yesno ( Oo0Ooo , "Would you like to download and install:" , "%s" % apk )
   if not O00OOoOOOO00O : wiz . LogNotify ( Oo0Ooo , '[COLOR red]ERROR:[/COLOR] Install Cancelled' ) ; return
   ii1IIiII111I = apk
  if O00OOoOOOO00O :
   if not os . path . exists ( IiiIII111iI ) : os . makedirs ( IiiIII111iI )
   if not wiz . workingURL ( url ) == True : wiz . LogNotify ( Oo0Ooo , 'APK Installer: [COLOR red]Invalid Apk Url![/COLOR]' ) ; return
   oO00oOo . create ( Oo0Ooo , 'Downloading %s' % ii1IIiII111I , '' , 'Please Wait' )
   IiI1IIIII1I = os . path . join ( IiiIII111iI , "%s.apk" % apk )
   try : os . remove ( IiI1IIIII1I )
   except : pass
   downloader . download ( url , IiI1IIIII1I , oO00oOo )
   xbmc . sleep ( 500 )
   oO00oOo . close ( )
   if "Brackets" in Brackets :
    O00OoOoO = zipfile . ZipFile ( IiI1IIIII1I )
    for file in O00OoOoO . namelist ( ) :
     if file . endswith ( '.apk' ) :
      with open ( os . path . join ( IiiIII111iI , os . path . basename ( file ) ) , 'wb' ) as oo0ooO0O0o :
       ooO0o0oo = file . split ( '/' ) [ 1 ]
       oo0ooO0O0o . write ( O00OoOoO . read ( file ) )
       xbmc . sleep ( 500 )
       oo0ooO0O0o . close ( )
       try :
        os . remove ( IiI1IIIII1I )
       except :
        pass
       IiI1IIIII1I = os . path . join ( IiiIII111iI , ooO0o0oo )
   I11i11Ii . ok ( Oo0Ooo , "Launching the APK to be installed" , "Follow the install process to complete." )
   xbmc . executebuiltin ( 'StartAndroidActivity("","android.intent.action.VIEW","application/vnd.android.package-archive","file:' + IiI1IIIII1I + '")' )
  else : wiz . LogNotify ( Oo0Ooo , '[COLOR red]ERROR:[/COLOR] Install Cancelled' )
 else : wiz . LogNotify ( Oo0Ooo , '[COLOR red]ERROR:[/COLOR] None Android Device' )
 if 79 - 79: Iii % iII1Ii
 if 81 - 81: i11iIiiIii + i11iIiiIii * iII1Ii + Iii
 if 32 - 32: OoOooO . Oo0O00O0O
 if 15 - 15: OOO00O0O . iII1Ii
def IiiIi ( name , url , ) :
 if "NULL" in url :
  I11i11Ii . ok ( Oo0Ooo , "[COLOR ghostwhite]Not a valid selection, please try again.[/COLOR]" )
  sys . exit ( 1 )
  if 42 - 42: O0OoOO0o + O000oo
 II1IiiIII = xbmcgui . DialogProgress ( )
 II1IiiIII . create ( Oo0Ooo , "" , "" , 'ROM: ' + name )
 ooooOoo0OO = name . replace ( '\\' , '' ) . replace ( '/' , '' ) . replace ( ':' , '' ) . replace ( '*' , '' ) . replace ( '?' , '' ) . replace ( '"' , '' ) . replace ( '<' , '' ) . replace ( '>' , '' ) . replace ( '|' , '' )
 IiI1IIIII1I = os . path . join ( IiiIII111iI , '%s.zip' % ooooOoo0OO )
 downloader . download ( url , IiI1IIIII1I , II1IiiIII )
 II1IiiIII . update ( 0 )
 extract . all ( IiI1IIIII1I , Oooo000o , II1IiiIII )
 I11i11Ii . ok ( Oo0Ooo , "[COLOR yellow]Download complete, ROM Location: [/COLOR][COLOR white]" + Oooo000o + "[/COLOR]" )
 if 41 - 41: I1 * Oo0OO
 if 68 - 68: I1IiiiiI - OOO00O0O
 if 41 - 41: Oo00o0o0
 if 21 - 21: Oo0OO + o00oO0oOo00 % I1111i + i11iIiiIii + O0OoOO0o + I1
 if 98 - 98: I1111i
def IIIIIIi1IiIi ( part , whole ) :
 return 100 * float ( part ) / float ( whole )
 if 14 - 14: iII1Ii / Oo0OO - IIIi / OOO00O0O
def oO0o00oOOooO0 ( type , add , name ) :
 if type == 'saveaddon' :
  Ii1IIIi = [ ]
  OOO000O0 = urllib . quote_plus ( add . lower ( ) . replace ( ' ' , '' ) )
  o0O00Oo0o0Oooo0 = add . replace ( 'Debrid' , 'Real Debrid' )
  ii1iIIi11 = urllib . quote_plus ( name . lower ( ) . replace ( ' ' , '' ) )
  name = name . replace ( 'url' , 'URL Resolver' )
  Ii1IIIi . append ( ( ii1I % name . title ( ) , ' ' ) )
  Ii1IIIi . append ( ( O0oO0 % 'Save %s Data' % o0O00Oo0o0Oooo0 , 'RunPlugin(plugin://%s/?mode=save%s&name=%s)' % ( OO0o , OOO000O0 , ii1iIIi11 ) ) )
  Ii1IIIi . append ( ( O0oO0 % 'Restore %s Data' % o0O00Oo0o0Oooo0 , 'RunPlugin(plugin://%s/?mode=restore%s&name=%s)' % ( OO0o , OOO000O0 , ii1iIIi11 ) ) )
  Ii1IIIi . append ( ( O0oO0 % 'Clear %s Data' % o0O00Oo0o0Oooo0 , 'RunPlugin(plugin://%s/?mode=clear%s&name=%s)' % ( OO0o , OOO000O0 , ii1iIIi11 ) ) )
 elif type == 'save' :
  Ii1IIIi = [ ]
  OOO000O0 = urllib . quote_plus ( add . lower ( ) . replace ( ' ' , '' ) )
  o0O00Oo0o0Oooo0 = add . replace ( 'Debrid' , 'Real Debrid' )
  ii1iIIi11 = urllib . quote_plus ( name . lower ( ) . replace ( ' ' , '' ) )
  name = name . replace ( 'url' , 'URL Resolver' )
  Ii1IIIi . append ( ( ii1I % name . title ( ) , ' ' ) )
  Ii1IIIi . append ( ( O0oO0 % 'Register %s' % o0O00Oo0o0Oooo0 , 'RunPlugin(plugin://%s/?mode=auth%s&name=%s)' % ( OO0o , OOO000O0 , ii1iIIi11 ) ) )
  Ii1IIIi . append ( ( O0oO0 % 'Save %s Data' % o0O00Oo0o0Oooo0 , 'RunPlugin(plugin://%s/?mode=save%s&name=%s)' % ( OO0o , OOO000O0 , ii1iIIi11 ) ) )
  Ii1IIIi . append ( ( O0oO0 % 'Restore %s Data' % o0O00Oo0o0Oooo0 , 'RunPlugin(plugin://%s/?mode=restore%s&name=%s)' % ( OO0o , OOO000O0 , ii1iIIi11 ) ) )
  Ii1IIIi . append ( ( O0oO0 % 'Import %s Data' % o0O00Oo0o0Oooo0 , 'RunPlugin(plugin://%s/?mode=import%s&name=%s)' % ( OO0o , OOO000O0 , ii1iIIi11 ) ) )
  Ii1IIIi . append ( ( O0oO0 % 'Clear Addon %s Data' % o0O00Oo0o0Oooo0 , 'RunPlugin(plugin://%s/?mode=addon%s&name=%s)' % ( OO0o , OOO000O0 , ii1iIIi11 ) ) )
 elif type == 'install' :
  Ii1IIIi = [ ]
  ii1iIIi11 = urllib . quote_plus ( name )
  Ii1IIIi . append ( ( ii1I % name , 'RunAddon(%s, ?mode=viewbuild&name=%s)' % ( OO0o , ii1iIIi11 ) ) )
  Ii1IIIi . append ( ( O0oO0 % 'Fresh Install' , 'RunPlugin(plugin://%s/?mode=install&name=%s&url=fresh)' % ( OO0o , ii1iIIi11 ) ) )
  Ii1IIIi . append ( ( O0oO0 % 'Normal Install' , 'RunPlugin(plugin://%s/?mode=install&name=%s&url=normal)' % ( OO0o , ii1iIIi11 ) ) )
  Ii1IIIi . append ( ( O0oO0 % 'Apply guiFix' , 'RunPlugin(plugin://%s/?mode=install&name=%s&url=gui)' % ( OO0o , ii1iIIi11 ) ) )
  Ii1IIIi . append ( ( O0oO0 % 'Build Information' , 'RunPlugin(plugin://%s/?mode=buildinfo&name=%s)' % ( OO0o , ii1iIIi11 ) ) )
 Ii1IIIi . append ( ( ii1I % '%s Settings' % Oo0Ooo , 'RunPlugin(plugin://%s/?mode=settings)' % OO0o ) )
 return Ii1IIIi
 if 21 - 21: oOOO % Iii
def oOO0Oooo ( state ) :
 II1i = [ 'includevideo' , 'includeall' , 'includebob' , 'includephoenix' , 'includespecto' , 'includegenesis' , 'includeexodus' , 'includeonechan' , 'includesalts' , 'includesaltslite' ]
 OOoOO0O0o0 = [ 'Include Video Addons' , 'Include All Addons' , 'Include Bob' , 'Include Phoenix' , 'Include Specto' , 'Include Genesis' , 'Include Exodus' , 'Include One Channel' , 'Include Salts' , 'Include Salts Lite HD' ]
 if state in [ 'true' , 'false' ] :
  for OooOOOOOo in II1i :
   wiz . setS ( OooOOOOOo , state )
 else :
  if not state in [ 'includevideo' , 'includeall' ] and wiz . getS ( 'includeall' ) == 'true' :
   try :
    OooOOOOOo = OOoOO0O0o0 [ II1i . index ( state ) ]
    I11i11Ii . ok ( Oo0Ooo , "[COLOR %s]You will need to turn off [COLOR %s]Include All Addons[/COLOR] to disable[/COLOR] [COLOR %s]%s[/COLOR]" % ( Iii1I1I11iiI1 , ii1iII1II , ii1iII1II , OooOOOOOo ) )
   except :
    wiz . LogNotify ( "Toggle Cache" , "Invalid id: %s" % state )
  else :
   I1II1 = 'true' if wiz . getS ( state ) == 'false' else 'false'
   wiz . setS ( state , I1II1 )
   if 89 - 89: iII1Ii / iII1Ii
def iIIIiiiiIiI1III ( url ) :
 if 'watch?v=' in url :
  o0000o0Oo , iIiI = url . split ( '?' )
  OO0OOoooo0o = iIiI . split ( '&' )
  for OooOOOOOo in OO0OOoooo0o :
   if OooOOOOOo . startswith ( 'v=' ) :
    url = OooOOOOOo [ 2 : ]
    break
   else : continue
 elif 'embed' in url or 'youtu.be' in url :
  o0000o0Oo = url . split ( '/' )
  if len ( o0000o0Oo [ - 1 ] ) > 5 :
   url = o0000o0Oo [ - 1 ]
  elif len ( o0000o0Oo [ - 2 ] ) > 5 :
   url = o0000o0Oo [ - 2 ]
 wiz . log ( "YouTube URL: %s" % url )
 yt . PlayVideo ( url )
 if 13 - 13: OOO00O0O + OoOooO - oO00OoOO000o % oOOO / I1IiiiiI . OooOoooOo
def OOOO00OoooO ( ) :
 IIIiIi1iiI1 = wiz . Grab_Log ( True )
 o0ooOOoO0oO0 = wiz . Grab_Log ( True , True )
 oo00I1IiI1IIiI = 0 ; oooo = IIIiIi1iiI1
 if not o0ooOOoO0oO0 == False and not IIIiIi1iiI1 == False :
  oo00I1IiI1IIiI = I11i11Ii . select ( Oo0Ooo , [ "View %s" % IIIiIi1iiI1 . replace ( IiIi11iIIi1Ii , "" ) , "View %s" % o0ooOOoO0oO0 . replace ( IiIi11iIIi1Ii , "" ) ] )
  if oo00I1IiI1IIiI == - 1 : wiz . LogNotify ( 'View Log' , 'View Log Cancelled!' ) ; return
 elif IIIiIi1iiI1 == False and o0ooOOoO0oO0 == False :
  wiz . LogNotify ( 'View Log' , 'No Log File Found!' )
  return
 elif not IIIiIi1iiI1 == False : oo00I1IiI1IIiI = 0
 elif not o0ooOOoO0oO0 == False : oo00I1IiI1IIiI = 1
 if 63 - 63: Oo0OO % OOO00O0O
 oooo = IIIiIi1iiI1 if oo00I1IiI1IIiI == 0 else o0ooOOoO0oO0
 o0Oo = wiz . Grab_Log ( False ) if oo00I1IiI1IIiI == 0 else wiz . Grab_Log ( False , True )
 if 4 - 4: I1
 wiz . TextBoxes ( "%s - %s" % ( Oo0Ooo , oooo ) , o0Oo )
 if 20 - 20: i11iIiiIii % Oo0O00O0O . Iii / I1Ii
def OOOoOo ( log = None , count = None , all = None ) :
 if log == None :
  IIIiIi1iiI1 = wiz . Grab_Log ( True )
  o0ooOOoO0oO0 = wiz . Grab_Log ( True , True )
  if not o0ooOOoO0oO0 == False and not IIIiIi1iiI1 == False :
   oo00I1IiI1IIiI = I11i11Ii . select ( Oo0Ooo , [ "View %s: %s error(s)" % ( IIIiIi1iiI1 . replace ( IiIi11iIIi1Ii , "" ) , OOOoOo ( IIIiIi1iiI1 , True ) ) , "View %s: %s error(s)" % ( o0ooOOoO0oO0 . replace ( IiIi11iIIi1Ii , "" ) , OOOoOo ( o0ooOOoO0oO0 , True ) ) ] )
   if oo00I1IiI1IIiI == - 1 : wiz . LogNotify ( 'View Log' , 'View Log Cancelled!' ) ; return
  elif IIIiIi1iiI1 == False and o0ooOOoO0oO0 == False :
   wiz . LogNotify ( 'View Log' , 'No Log File Found!' )
   return
  elif not IIIiIi1iiI1 == False : oo00I1IiI1IIiI = 0
  elif not o0ooOOoO0oO0 == False : oo00I1IiI1IIiI = 1
  log = IIIiIi1iiI1 if oo00I1IiI1IIiI == 0 else o0ooOOoO0oO0
 if log == False :
  if count == None :
   wiz . LogNotify ( Oo0Ooo , "Log File not Found" )
   return False
  else :
   return 0
 else :
  if os . path . exists ( log ) :
   oo0ooO0O0o = open ( log , mode = 'r' ) ; o0000o0Oo = oo0ooO0O0o . read ( ) . replace ( '\n' , '' ) . replace ( '\r' , '' ) ; oo0ooO0O0o . close ( )
   OOoo = re . compile ( "-->Python callback/script returned the following error<--(.+?)-->End of Python script error report<--" ) . findall ( o0000o0Oo )
   if not count == None :
    if all == None :
     ooIII1II1iii1i = 0
     for OooOOOOOo in OOoo :
      if OO0o in OooOOOOOo : ooIII1II1iii1i += 1
     return ooIII1II1iii1i
    else : return len ( OOoo )
   if len ( OOoo ) > 0 :
    ooIII1II1iii1i = 0 ; o0Oo = ""
    for OooOOOOOo in OOoo :
     if all == None and not OO0o in OooOOOOOo : continue
     else :
      ooIII1II1iii1i += 1
      o0Oo += "[COLOR red]Error Number %s[/COLOR]\n(PythonToCppException) : -->Python callback/script returned the following error<--%s-->End of Python script error report<--\n\n" % ( ooIII1II1iii1i , OooOOOOOo . replace ( '                                          ' , '\n' ) . replace ( '\\\\' , '\\' ) . replace ( OOOo0 , '' ) )
    if ooIII1II1iii1i > 0 :
     if O0o0O00Oo0o0 >= 16 : I11i11Ii . textviewer ( Oo0Ooo , o0Oo )
     else : wiz . TextBoxes ( Oo0Ooo , o0Oo )
    else : wiz . LogNotify ( Oo0Ooo , "No Errors Found in Log" )
   else : wiz . LogNotify ( Oo0Ooo , "No Errors Found in Log" )
  else : wiz . LogNotify ( Oo0Ooo , "Log File not Found" )
  if 34 - 34: i11iIiiIii / I1111i * IIIi . oOOO
def ooo0O00000oo0 ( ) :
 if os . path . exists ( oOOoo00O0O ) :
  oo0ooO0O0o = open ( oOOoo00O0O , mode = 'r' ) ; o0Oo = oo0ooO0O0o . read ( ) ; oo0ooO0O0o . close ( )
  wiz . TextBoxes ( "%s - Wizard.log" % Oo0Ooo , o0Oo )
 else :
  wiz . LogNotify ( 'View Log' , 'Wizard.log not found!' )
  if 80 - 80: oOOO + oO00OoOO000o
def oOIii11111iiI ( addon ) :
 if I11i11Ii . yesno ( Oo0Ooo , '[COLOR %s]Are you sure you want to delete the addon:' % ii1iII1II , '[COLOR %s]%s[/COLOR]?[/COLOR]' % ( ii1iII1II , addon ) , yeslabel = '[B]Remove Addon[/B]' , nolabel = '[B]Don\'t Remove[/B]' ) :
  wiz . cleanHouse ( os . path . join ( IiI , addon ) )
  ii111IIII ( addon )
  wiz . LogNotify ( 'Remove Addon' , 'Complete!' )
  I11i11Ii . ok ( Oo0Ooo , '[COLOR %s]The addon has been removed but will remain in the addons list until the next time you reload Kodi.[/COLOR]' )
 else : wiz . LogNotify ( 'Remove Addon' , 'Cancelled!' )
 wiz . refresh ( )
 if 67 - 67: o00oO0oOo00
def ii111IIII ( addon ) :
 if addon == 'all' :
  if I11i11Ii . yesno ( Oo0Ooo , '[COLOR %s]Would you like to remove [COLOR %s]ALL[/COLOR] addon data stored in you Userdata folder?[/COLOR]' % ( Iii1I1I11iiI1 , ii1iII1II ) , yeslabel = '[B]Remove Data[/B]' , nolabel = '[B]Don\'t Remove[/B]' ) :
   wiz . cleanHouse ( IiII )
  else : wiz . LogNotify ( 'Remove Addon Data' , 'Cancelled!' )
 elif addon == 'uninstalled' :
  if I11i11Ii . yesno ( Oo0Ooo , '[COLOR %s]Would you like to remove [COLOR %s]ALL[/COLOR] addon data stored in you Userdata folder for uninstalled addons?[/COLOR]' % ( Iii1I1I11iiI1 , ii1iII1II ) , yeslabel = '[B]Remove Data[/B]' , nolabel = '[B]Don\'t Remove[/B]' ) :
   OOOoO00O = 0
   for Iiii111 in glob . glob ( os . path . join ( IiII , '*' ) ) :
    Ooooo = Iiii111 . replace ( IiII , '' ) . replace ( '\\' , '' ) . replace ( '/' , '' )
    if Ooooo in ooOOoooooo : pass
    elif os . path . exists ( os . path . join ( IiI , Ooooo ) ) : pass
    else : wiz . cleanHouse ( Iiii111 ) ; OOOoO00O += 1 ; wiz . log ( Iiii111 ) ; shutil . rmtree ( Iiii111 )
   wiz . LogNotify ( 'Clean up Uninstalled' , '[COLOR yellow]%s[/COLOR] Folders(s) Removed' % OOOoO00O )
  else : wiz . LogNotify ( 'Remove Addon Data' , 'Cancelled!' )
 elif addon == 'empty' :
  if I11i11Ii . yesno ( Oo0Ooo , '[COLOR %s]Would you like to remove [COLOR %s]ALL[/COLOR] empty addon data folders in you Userdata folder?[/COLOR]' % ( Iii1I1I11iiI1 , ii1iII1II ) , yeslabel = '[B]Remove Data[/B]' , nolabel = '[B]Don\'t Remove[/B]' ) :
   OOOoO00O = wiz . emptyfolder ( IiII )
   wiz . LogNotify ( 'Remove Empty Folders' , '[COLOR yellow]%s[/COLOR] Folders(s) Removed' % OOOoO00O )
  else : wiz . LogNotify ( 'Remove Empty Folders' , 'Cancelled!' )
 else :
  iIiii1Ii1I1II = os . path . join ( Oo , 'addon_data' , addon )
  if addon in ooOOoooooo :
   wiz . LogNotify ( "Protected Plugin" , "Not allowed to remove Addon_Data" )
  elif os . path . exists ( iIiii1Ii1I1II ) :
   if I11i11Ii . yesno ( Oo0Ooo , '[COLOR %s]Would you also like to remove the addon data for:[/COLOR]' % Iii1I1I11iiI1 , '[COLOR %s]%s[/COLOR]' % ( ii1iII1II , addon ) , yeslabel = '[B]Remove Data[/B]' , nolabel = '[B]Don\'t Remove[/B]' ) :
    wiz . cleanHouse ( iIiii1Ii1I1II )
    try :
     shutil . rmtree ( iIiii1Ii1I1II )
    except :
     wiz . log ( "Error deleting: %s" % iIiii1Ii1I1II )
   else :
    wiz . log ( 'Addon data for %s was not removed' % addon )
 wiz . refresh ( )
 if 14 - 14: iII1Ii
def IIIII1i ( type ) :
 if type == 'build' :
  ooIII1II1iii1i = Oo0 ( 'restore' )
  if ooIII1II1iii1i == False : wiz . LogNotify ( Oo0Ooo , "Local Restore Cancelled" ) ; return
 wiz . restoreLocal ( type )
 if 39 - 39: Oo00o0o0 / oOOO
def II11iiii ( type ) :
 if type == 'build' :
  ooIII1II1iii1i = Oo0 ( 'restore' )
  if ooIII1II1iii1i == False : wiz . LogNotify ( Oo0Ooo , "External Restore Cancelled" ) ; return
 wiz . restoreExternal ( type )
 if 20 - 20: O0OoOO0o / IIIi
def I1111ii11IIII ( name ) :
 if wiz . workingURL ( Iii1I1111ii ) == True :
  if wiz . checkBuild ( name , 'url' ) :
   name , oO0oO0 , iiiI1 , OOOoO0O , o0iiiI1I1iIIIi1 , IiiI1iiiiI1iI , iIiiiii1i , iiIi1IIiI , i1oO0OO0 , o0O0Oo00 = wiz . checkBuild ( name , 'all' )
   i1oO0OO0 = 'Yes' if i1oO0OO0 . lower ( ) == 'yes' else 'No'
   o0Oo = "[COLOR %s]Build Name:[/COLOR] [COLOR %s]%s[/COLOR][CR]" % ( Iii1I1I11iiI1 , ii1iII1II , name )
   o0Oo += "[COLOR %s]Build Version:[/COLOR] [COLOR %s]%s[/COLOR][CR]" % ( Iii1I1I11iiI1 , ii1iII1II , oO0oO0 )
   if not IiiI1iiiiI1iI == "http://" :
    IiIi1II111I = wiz . themeCount ( name , False )
    o0Oo += "[COLOR %s]Build Theme(s):[/COLOR] [COLOR %s]%s[/COLOR][CR]" % ( Iii1I1I11iiI1 , ii1iII1II , ', ' . join ( IiIi1II111I ) )
   o0Oo += "[COLOR %s]Kodi Version:[/COLOR] [COLOR %s]%s[/COLOR][CR]" % ( Iii1I1I11iiI1 , ii1iII1II , o0iiiI1I1iIIIi1 )
   o0Oo += "[COLOR %s]Adult Content:[/COLOR] [COLOR %s]%s[/COLOR][CR]" % ( Iii1I1I11iiI1 , ii1iII1II , i1oO0OO0 )
   o0Oo += "[COLOR %s]Description:[/COLOR] [COLOR %s]%s[/COLOR][CR]" % ( Iii1I1I11iiI1 , ii1iII1II , o0O0Oo00 )
   wiz . TextBoxes ( Oo0Ooo , o0Oo )
  else : wiz . log ( "Invalid Build Name!" )
 else : wiz . log ( "Build text file not working: %s" % ooO0o )
 if 80 - 80: I1IiiiiI / IIIi
def I1i ( url ) :
 i1iiIIi11I = urllib2 . Request ( url )
 i1iiIIi11I . add_header ( 'User-Agent' , 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3' )
 o0o0oOo000o0 = urllib2 . urlopen ( i1iiIIi11I )
 oOoooo000Oo00 = o0o0oOo000o0 . read ( )
 o0o0oOo000o0 . close ( )
 return oOoooo000Oo00
 if 21 - 21: oOOO - O000oo - I1111i
def I1i11iIIi11 ( url ) :
 if url == 'http://' : return False
 try :
  i1iiIIi11I = urllib2 . Request ( url )
  i1iiIIi11I . add_header ( 'User-Agent' , IIi1IiiiI1Ii )
  o0o0oOo000o0 = urllib2 . urlopen ( i1iiIIi11I )
  o0o0oOo000o0 . close ( )
 except Exception , III1I1Iii11i :
  return III1I1Iii11i
 return True
 if 96 - 96: Oo00o0o0 - Oo00o0o0
 if 87 - 87: oOOO / Oo0O00O0O - oO00OoOO000o . Iii + O000oo . oO00OoOO000o
 if 4 - 4: Oo0O00O0O + Oo0OO . OooOoooOo / OoOooO - OoOooO
 if 52 - 52: iII1Ii * Oo0O00O0O
 if 12 - 12: OoOooO + Iii * OooOoooOo . iII1Ii
 if 71 - 71: I1111i - o00oO0oOo00 - IIIi
def Oo0 ( install = None , over = False ) :
 if I11iii1Ii == 'true' :
  traktit . autoUpdate ( 'all' )
  wiz . setS ( 'traktlastsave' , str ( OOoOO0oo0ooO ) )
 if I1IIiiIiii == 'true' :
  debridit . autoUpdate ( 'all' )
  wiz . setS ( 'debridlastsave' , str ( OOoOO0oo0ooO ) )
 if O000oo0O == 'true' :
  loginit . autoUpdate ( 'all' )
  wiz . setS ( 'loginlastsave' , str ( OOoOO0oo0ooO ) )
 if over == True : o00iIiiiII = 1
 elif install == 'restore' : o00iIiiiII = I11i11Ii . yesno ( Oo0Ooo , "[COLOR %s]Do you wish to restore your" % Iii1I1I11iiI1 , "Kodi configuration to default settings" , "Before installing the local backup?[/COLOR]" , nolabel = '[B]No, Cancel[/B]' , yeslabel = '[B]Continue[/B]' )
 elif install : o00iIiiiII = I11i11Ii . yesno ( Oo0Ooo , "[COLOR %s]Do you wish to restore your" % Iii1I1I11iiI1 , "Kodi configuration to default settings" , "Before installing [COLOR %s]%s[/COLOR]?" % ( ii1iII1II , install ) , nolabel = '[B]No, Cancel[/B]' , yeslabel = '[B]Continue[/B]' )
 else : o00iIiiiII = I11i11Ii . yesno ( Oo0Ooo , "[COLOR %s]Do you wish to restore your" % Iii1I1I11iiI1 , "Kodi configuration to default settings?[/COLOR]" , nolabel = '[B]No, Cancel[/B]' , yeslabel = '[B]Continue[/B]' )
 if o00iIiiiII :
  if not wiz . currSkin ( ) in [ 'skin.confluence' , 'skin.estuary' ] :
   Ii11iiI1 = 'skin.confluence' if O0o0O00Oo0o0 < 17 else 'skin.estuary'
   O00OOoOOOO00O = I11i11Ii . yesno ( Oo0Ooo , "[COLOR %s]The skin needs to be set back to [COLOR %s]%s[/COLOR]" % ( Iii1I1I11iiI1 , ii1iII1II , Ii11iiI1 [ 5 : ] ) , "Before doing a fresh install to clear all Texture files," , "Would you like us to do that for you?[/COLOR]" , yeslabel = "[B]Switch Skins[/B]" , nolabel = "[B]I'll Do It[/B]" ) ;
   if O00OOoOOOO00O :
    skinSwitch . swapSkins ( Ii11iiI1 )
    ooIII1II1iii1i = 0
    xbmc . sleep ( 1000 )
    while not xbmc . getCondVisibility ( "Window.isVisible(yesnodialog)" ) and ooIII1II1iii1i < 150 :
     ooIII1II1iii1i += 1
     xbmc . sleep ( 200 )
     wiz . ebi ( 'SendAction(Select)' )
    if xbmc . getCondVisibility ( "Window.isVisible(yesnodialog)" ) :
     wiz . ebi ( 'SendClick(11)' )
    else : wiz . LogNotify ( Oo0Ooo , 'Fresh Install: [COLOR red]Skin Swap Timed Out![/COLOR]' ) ; return False
    xbmc . sleep ( 1000 )
   else : wiz . LogNotify ( Oo0Ooo , 'Fresh Install: [COLOR red]Cancelled![/COLOR]' ) ; return False
  if not wiz . currSkin ( ) in [ 'skin.confluence' , 'skin.estuary' ] :
   wiz . LogNotify ( Oo0Ooo , 'Fresh Install: [COLOR red]Skin Swap Failed![/COLOR]' )
   return
  oO00oOo . create ( Oo0Ooo , "[COLOR %s]Clearing all files and folders:" % Iii1I1I11iiI1 , '' , 'Please Wait![/COLOR]' )
  iiIO0OO0o0O00oO = os . path . abspath ( OOOo0 )
  o00OoO0o0oOo = sum ( [ len ( OoO0O0oo0o ) for iIi11I11 , i1ioO , OoO0O0oo0o in os . walk ( iiIO0OO0o0O00oO ) ] ) ; I11iiI = 0
  for i1iIii1i111 , OOooo000OooO , OoO0O0oo0o in os . walk ( iiIO0OO0o0O00oO , topdown = True ) :
   ooOOoooooo . append ( 'My_Builds' )
   OOooo000OooO [ : ] = [ i1ioO for i1ioO in OOooo000OooO if i1ioO not in ooOOoooooo ]
   for Ii1i1i1i1I1Ii in OoO0O0oo0o :
    I11iiI += 1
    iI1i1IIiiiI1 = i1iIii1i111 . split ( '\\' )
    ooIII1II1iii1i = len ( iI1i1IIiiiI1 ) - 1
    if Ii1i1i1i1I1Ii == 'sources.xml' and iI1i1IIiiiI1 [ - 1 ] == 'userdata' and OOO00 == 'true' : wiz . log ( "Keep Sources: %s" % os . path . join ( i1iIii1i111 , Ii1i1i1i1I1Ii ) )
    elif Ii1i1i1i1I1Ii == 'favourites.xml' and iI1i1IIiiiI1 [ - 1 ] == 'userdata' and oOoOooOo0o0 == 'true' : wiz . log ( "Keep Favourites: %s" % os . path . join ( i1iIii1i111 , Ii1i1i1i1I1Ii ) )
    elif Ii1i1i1i1I1Ii == 'profiles.xml' and iI1i1IIiiiI1 [ - 1 ] == 'userdata' and iiiiiIIii == 'true' : wiz . log ( "Keep Profiles: %s" % os . path . join ( i1iIii1i111 , Ii1i1i1i1I1Ii ) )
    elif Ii1i1i1i1I1Ii == 'advancedsettings.xml' and iI1i1IIiiiI1 [ - 1 ] == 'userdata' and O000OO0 == 'true' : wiz . log ( "Keep Advanced Settings: %s" % os . path . join ( i1iIii1i111 , Ii1i1i1i1I1Ii ) )
    elif Ii1i1i1i1I1Ii in OO0O000 : wiz . log ( "Keep Log File: %s" % Ii1i1i1i1I1Ii )
    elif Ii1i1i1i1I1Ii . endswith ( '.db' ) :
     try :
      if Ii1i1i1i1I1Ii . endswith ( '.db' ) and Ii1i1i1i1I1Ii . startswith ( 'Addon' ) and O0o0O00Oo0o0 >= 17 : wiz . log ( "Ignoring %s on v%s" % ( Ii1i1i1i1I1Ii , O0o0O00Oo0o0 ) )
      else : os . remove ( os . path . join ( i1iIii1i111 , Ii1i1i1i1I1Ii ) )
     except Exception , III1I1Iii11i :
      wiz . log ( 'Failed to delete, Purging DB' )
      wiz . log ( "-> %s / %s" % ( Exception , str ( III1I1Iii11i ) ) )
      wiz . purgeDb ( os . path . join ( i1iIii1i111 , Ii1i1i1i1I1Ii ) )
    else :
     oO00oOo . update ( int ( IIIIIIi1IiIi ( I11iiI , o00OoO0o0oOo ) ) , '' , '[COLOR %s]File: [/COLOR][COLOR %s]%s[/COLOR]' % ( Iii1I1I11iiI1 , ii1iII1II , Ii1i1i1i1I1Ii ) , '' )
     try : os . remove ( os . path . join ( i1iIii1i111 , Ii1i1i1i1I1Ii ) )
     except Exception , III1I1Iii11i :
      wiz . log ( "Error removing %s" % os . path . join ( i1iIii1i111 , Ii1i1i1i1I1Ii ) )
      wiz . log ( "-> %s / %s" % ( Exception , str ( III1I1Iii11i ) ) )
   if oO00oOo . iscanceled ( ) :
    oO00oOo . close ( )
    wiz . LogNotify ( Oo0Ooo , "Fresh Start Cancelled" )
    return False
  for i1iIii1i111 , OOooo000OooO , OoO0O0oo0o in os . walk ( iiIO0OO0o0O00oO , topdown = True ) :
   OOooo000OooO [ : ] = [ i1ioO for i1ioO in OOooo000OooO if i1ioO not in ooOOoooooo ]
   for Ii1i1i1i1I1Ii in OOooo000OooO :
    oO00oOo . update ( 100 , '' , 'Cleaning Up Empty Folder: [COLOR %s]%s[/COLOR]' % ( ii1iII1II , Ii1i1i1i1I1Ii ) , '' )
    if Ii1i1i1i1I1Ii not in [ "Database" , "userdata" , "temp" , "addons" , "addon_data" ] :
     shutil . rmtree ( os . path . join ( i1iIii1i111 , Ii1i1i1i1I1Ii ) , ignore_errors = True , onerror = None )
   if oO00oOo . iscanceled ( ) :
    oO00oOo . close ( )
    wiz . LogNotify ( Oo0Ooo , "Fresh Start Cancelled" )
    return False
  oO00oOo . close ( )
  wiz . clearS ( 'build' )
  if install == 'restore' :
   I11i11Ii . ok ( Oo0Ooo , "[COLOR %s]Your current setup for kodi has been cleared!" % Iii1I1I11iiI1 , "Now we will install the local backup[/COLOR]" )
  elif install :
   I11i11Ii . ok ( Oo0Ooo , "[COLOR %s]Your current setup for kodi has been cleared!" % Iii1I1I11iiI1 , "Now we will install: [COLOR %s]%s v%s[/COLOR][/COLOR]" % ( ii1iII1II , install , wiz . checkBuild ( install , 'version' ) ) )
   i1iIIII1iiIIi ( install , 'normal' )
  else :
   I11i11Ii . ok ( Oo0Ooo , "[COLOR %s]The process is complete, you're now back to a fresh Kodi configuration with [COLOR %s]%s[/COLOR]" % ( Iii1I1I11iiI1 , ii1iII1II , Oo0Ooo ) , "Kodi will now force close, Please relaunch Kodi.[/COLOR]" )
   wiz . killxbmc ( )
 else :
  if not install == 'restore' : wiz . LogNotify ( Oo0Ooo , 'Fresh Install: [COLOR red]Cancelled![/COLOR]' ) ; wiz . refresh ( )
  if 99 - 99: IIIi / Iii / I1IiiiiI
  if 84 - 84: iII1Ii / O000oo
  if 33 - 33: OooOoooOo / I1111i - OooOoooOo . oOOO
  if 18 - 18: oOOO / OoOooO + O0OoOO0o
def ooIiI11i1I11111 ( ) :
 if I11i11Ii . yesno ( Oo0Ooo , '[COLOR %s]Would you like to clear cache?[/COLOR]' % Iii1I1I11iiI1 , nolabel = '[B]No, Cancel[/B]' , yeslabel = '[B]Clear Cache[/B]' ) :
  wiz . clearCache ( )
  Ii1IIIIIIiI1 ( )
  if 24 - 24: OOO00O0O * I1IiiiiI % OoOooO - oOOO
def ii1IOoO0O ( ) :
 if I11i11Ii . yesno ( Oo0Ooo , '[COLOR %s]Would you like to clear cache, packages and thumbnails?[/COLOR]' % Iii1I1I11iiI1 , nolabel = '[B]Cancel Process[/B]' , yeslabel = '[B]Clean All[/B]' ) :
  wiz . clearCache ( 'total' )
  wiz . clearPackages ( 'total' )
  Ii1IIIIIIiI1 ( 'total' )
  wiz . killxbmc ( )
  if 98 - 98: i11iIiiIii / OOO00O0O * o00oO0oOo00 / I1111i
def Ii1IIIIIIiI1 ( type = None ) :
 o0OOoOo0oo = wiz . latestDB ( 'Textures' )
 if not type == None : ii1I11i = 1
 else : ii1I11i = I11i11Ii . yesno ( Oo0Ooo , '[COLOR %s]Would you like to delete the %s and Thumbnails folder?' % ( Iii1I1I11iiI1 , o0OOoOo0oo ) , "They will repopulate on the next startup[/COLOR]" , nolabel = '[B]Don\'t Delete[/B]' , yeslabel = '[B]Delete Thumbs[/B]' )
 if ii1I11i == 1 :
  try : wiz . removeFile ( os . join ( o00 , o0OOoOo0oo ) )
  except : wiz . log ( 'Failed to delete, Purging DB.' ) ; wiz . purgeDb ( o0OOoOo0oo )
  wiz . removeFolder ( oo00 )
  if not type == 'total' : wiz . killxbmc ( )
 else : wiz . log ( 'Clear thumbnames cancelled' )
 if 64 - 64: OooOoooOo
def I1ii1i1iiii ( ) :
 I1i1I = [ ] ; ii1IIiII111I = [ ]
 for i1111iI1 , Oo0oOOOOo , OoO0O0oo0o in os . walk ( OOOo0 ) :
  for oo0ooO0O0o in fnmatch . filter ( OoO0O0oo0o , '*.db' ) :
   if oo0ooO0O0o != 'Thumbs.db' :
    iiiO000OOO = os . path . join ( i1111iI1 , oo0ooO0O0o )
    I1i1I . append ( iiiO000OOO )
    dir = iiiO000OOO . replace ( '\\' , '/' ) . split ( '/' )
    ii1IIiII111I . append ( '(%s) %s' % ( dir [ len ( dir ) - 2 ] , dir [ len ( dir ) - 1 ] ) )
 if O0o0O00Oo0o0 >= 16 :
  ii1I11i = I11i11Ii . multiselect ( "[COLOR %s]Select DB File to Purge[/COLOR]" % Iii1I1I11iiI1 , ii1IIiII111I )
  if ii1I11i == None : wiz . LogNotify ( "Purge Database" , "Cancelled" )
  elif len ( ii1I11i ) == 0 : wiz . LogNotify ( "Purge Database" , "Cancelled" )
  else :
   for o0IIi1 in ii1I11i : wiz . purgeDb ( I1i1I [ o0IIi1 ] )
 else :
  ii1I11i = I11i11Ii . select ( "[COLOR %s]Select DB File to Purge[/COLOR]" % Iii1I1I11iiI1 , ii1IIiII111I )
  if ii1I11i == - 1 : wiz . LogNotify ( "Purge Database" , "Cancelled" )
  else : wiz . purgeDb ( I1i1I [ o0IIi1 ] )
  if 73 - 73: IIIi + IIIi % I1Ii * OooOoooOo
  if 4 - 4: IIIi - Oo00o0o0 % I1I11 / I1 % Oo00o0o0
  if 96 - 96: I1IiiiiI . I1111i - oO00OoOO000o + o00oO0oOo00 * iII1Ii / O0OoOO0o
  if 26 - 26: IIIi * oOOO
def i1iI1Ii11Ii1 ( ) :
 iiiI1 = wiz . workingURL ( iii )
 if iiiI1 == True :
  oOoooo000Oo00 = wiz . openURL ( iii ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
  id , o0Oo = oOoooo000Oo00 . split ( '|||' )
  notify . testNotification ( o0Oo )
 else : wiz . LogNotify ( Oo0Ooo , "Invalid URL for Notification" )
 if 82 - 82: OoOooO
def O0oO0oo0O ( ) :
 notify . updateWindow ( )
 if 82 - 82: Oo0O00O0O . I1IiiiiI
def III1iiiII1ii ( ) :
 notify . firstRun ( )
 if 76 - 76: oO00OoOO000o
def ooO000OO ( ) :
 notify . apkInstaller ( 'SPMC' )
 if 43 - 43: Oo0OO * I1111i % IIIi
def iiiI11 ( ) :
 if o0OIiII == 'No' : I1i1iiiII1i ( '==============BackUp Options===============' , '' , themeit = O0oO0 )
 I1i1iiiII1i ( 'Full Backup' , 'full' , icon = o0oOoO00o , themeit = I1I1i1I )
 I1i1iiiII1i ( 'Backup for Builds (Exc: Thumbnails, Databases)' , 'backb' , icon = o0oOoO00o , themeit = I1I1i1I )
 I1i1iiiII1i ( 'Backup addon data' , 'backad' , icon = o0oOoO00o , themeit = I1I1i1I )
 if o0OIiII == 'No' : I1i1iiiII1i ( '==============Restore Options===============' , '' , themeit = O0oO0 )
 Ii11iiI ( 'Restore Full Backup' , 'refull' , icon = o0oOoO00o , themeit = I1I1i1I )
 Ii11iiI ( 'Restore Addon Data' , 'refull' , icon = o0oOoO00o , themeit = I1I1i1I )
 if o0OIiII == 'No' : I1i1iiiII1i ( '==============Other Options===============' , '' , themeit = O0oO0 )
 Ii11iiI ( 'Delete A Backup' , 'delbu' , icon = o0oOoO00o , themeit = I1I1i1I )
 I1i1iiiII1i ( 'Delete All Backups' , 'delall' , icon = o0oOoO00o , themeit = I1I1i1I )
 I1i1iiiII1i ( 'Select Backup Location' , 'settings' , icon = o0oOoO00o , themeit = I1I1i1I )
 if 89 - 89: Oo00o0o0
 if 87 - 87: O0OoOO0o % oOOO
 if 62 - 62: iII1Ii + Oo0OO / O0OoOO0o * i11iIiiIii
 if 37 - 37: O0OoOO0o
 if 33 - 33: iII1Ii - OoOooO - iII1Ii
 if 94 - 94: Iii * I1Ii * Oo0O00O0O / o00oO0oOo00 . Iii - o00oO0oOo00
def iIiiii ( display , mode = None , name = None , url = None , menu = None , description = Oo0Ooo , overwrite = True , fanart = Oo0oO0ooo , icon = o0oOoO00o , themeit = None ) :
 I1I1iiii1IiI1i = sys . argv [ 0 ]
 if not mode == None : I1I1iiii1IiI1i += "?mode=%s" % urllib . quote_plus ( mode )
 if not name == None : I1I1iiii1IiI1i += "&name=" + urllib . quote_plus ( name )
 if not url == None : I1I1iiii1IiI1i += "&url=" + urllib . quote_plus ( url )
 OooO0ooO0o0 = True
 if themeit : display = themeit % display
 OOOO00OOO00 = xbmcgui . ListItem ( display , iconImage = "DefaultFolder.png" , thumbnailImage = icon )
 OOOO00OOO00 . setInfo ( type = "Video" , infoLabels = { "Title" : display , "Plot" : description } )
 OOOO00OOO00 . setProperty ( "Fanart_Image" , fanart )
 if not menu == None : OOOO00OOO00 . addContextMenuItems ( menu , replaceItems = overwrite )
 OooO0ooO0o0 = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = I1I1iiii1IiI1i , listitem = OOOO00OOO00 , isFolder = True )
 return OooO0ooO0o0
 if 23 - 23: OoOooO
def Ii11iiI ( display , mode , name = None , url = None , menu = None , overwrite = True , fanart = Oo0oO0ooo , icon = o0oOoO00o , themeit = None ) :
 I1I1iiii1IiI1i = '%s?mode=%s' % ( sys . argv [ 0 ] , urllib . quote_plus ( mode ) )
 if not name == None : I1I1iiii1IiI1i += "&name=" + urllib . quote_plus ( name )
 if not url == None : I1I1iiii1IiI1i += "&url=" + urllib . quote_plus ( url )
 OooO0ooO0o0 = True
 if themeit : display = themeit % display
 OOOO00OOO00 = xbmcgui . ListItem ( display , iconImage = "DefaultFolder.png" , thumbnailImage = icon )
 OOOO00OOO00 . setInfo ( type = "Video" , infoLabels = { "Title" : display , "Plot" : Oo0Ooo } )
 OOOO00OOO00 . setProperty ( "Fanart_Image" , fanart )
 if not menu == None : OOOO00OOO00 . addContextMenuItems ( menu , replaceItems = overwrite )
 OooO0ooO0o0 = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = I1I1iiii1IiI1i , listitem = OOOO00OOO00 , isFolder = True )
 return OooO0ooO0o0
 if 9 - 9: I1Ii * oOOO . Oo0OO * i11iIiiIii - OoOooO
def IIiii ( name , url , mode , iconimage ) :
 I1I1iiii1IiI1i = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage )
 OooO0ooO0o0 = True
 OOOO00OOO00 = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 OOOO00OOO00 . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : name } )
 OooO0ooO0o0 = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = I1I1iiii1IiI1i , listitem = OOOO00OOO00 , isFolder = True )
 return OooO0ooO0o0
 if 54 - 54: OOO00O0O * IIIi + o00oO0oOo00 % OooOoooOo - o00oO0oOo00 + I1I11
def oo0OO ( name , url , mode , iconimage , fanart , description , installRating ) :
 I1I1iiii1IiI1i = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart ) + "&description=" + urllib . quote_plus ( description ) + "&installRating=" + urllib . quote_plus ( installRating )
 OooO0ooO0o0 = True
 OOOO00OOO00 = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 OOOO00OOO00 . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description , "Premiered" : installRating } )
 OOOO00OOO00 . setProperty ( "Fanart_Image" , fanart )
 OooO0ooO0o0 = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = I1I1iiii1IiI1i , listitem = OOOO00OOO00 , isFolder = False )
 return OooO0ooO0o0
 if 15 - 15: I1I11 * Oo00o0o0 + IIIi . I1Ii % OOO00O0O - Oo0OO
def i11iiI1111 ( display , mode = None , name = None , url = None , menu = None , description = Oo0Ooo , overwrite = True , fanart = Oo0oO0ooo , icon = o0oOoO00o , themeit = None ) :
 I1I1iiii1IiI1i = sys . argv [ 0 ]
 if not mode == None : I1I1iiii1IiI1i += "?mode=%s" % urllib . quote_plus ( mode )
 if not name == None : I1I1iiii1IiI1i += "&name=" + urllib . quote_plus ( name )
 if not url == None : I1I1iiii1IiI1i += "&url=" + urllib . quote_plus ( url )
 OooO0ooO0o0 = True
 if themeit : display = themeit % display
 OOOO00OOO00 = xbmcgui . ListItem ( display , iconImage = "DefaultFolder.png" , thumbnailImage = icon )
 OOOO00OOO00 . setInfo ( type = "Video" , infoLabels = { "Title" : display , "Plot" : description } )
 OOOO00OOO00 . setProperty ( "Fanart_Image" , fanart )
 if not menu == None : OOOO00OOO00 . addContextMenuItems ( menu , replaceItems = overwrite )
 OooO0ooO0o0 = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = I1I1iiii1IiI1i , listitem = OOOO00OOO00 , isFolder = False )
 return OooO0ooO0o0
 if 13 - 13: I1I11 % I1I11 % oOOO % OOO00O0O * OooOoooOo % I1Ii
def i1oOOOOOOOoO ( display , mode , name = None , url = None , menu = None , overwrite = True , fanart = Oo0oO0ooo , icon = o0oOoO00o , description = None , themeit = None ) :
 I1I1iiii1IiI1i = '%s?mode=%s' % ( sys . argv [ 0 ] , urllib . quote_plus ( mode ) )
 if not name == None : I1I1iiii1IiI1i += "&name=" + urllib . quote_plus ( name )
 if not url == None : I1I1iiii1IiI1i += "&url=" + urllib . quote_plus ( url )
 if not description == None : I1I1iiii1IiI1i += "&description=" + urllib . quote_plus ( description )
 OooO0ooO0o0 = True
 if themeit : display = themeit % display
 OOOO00OOO00 = xbmcgui . ListItem ( description , iconImage = "DefaultFolder.png" , thumbnailImage = icon )
 OOOO00OOO00 . setInfo ( type = "Video" , infoLabels = { "Title" : description , "Plot" : Oo0Ooo } )
 OOOO00OOO00 . setProperty ( "Fanart_Image" , fanart )
 if not menu == None : OOOO00OOO00 . addContextMenuItems ( menu , replaceItems = overwrite )
 OooO0ooO0o0 = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = I1I1iiii1IiI1i , listitem = OOOO00OOO00 , isFolder = False )
 return OooO0ooO0o0
 if 82 - 82: Iii . I1I11 / Oo0OO + O0OoOO0o - Oo0OO
def I1i1iiiII1i ( display , mode , name = None , url = None , menu = None , overwrite = True , fanart = Oo0oO0ooo , icon = o0oOoO00o , themeit = None ) :
 I1I1iiii1IiI1i = '%s?mode=%s' % ( sys . argv [ 0 ] , urllib . quote_plus ( mode ) )
 if not name == None : I1I1iiii1IiI1i += "&name=" + urllib . quote_plus ( name )
 if not url == None : I1I1iiii1IiI1i += "&url=" + urllib . quote_plus ( url )
 OooO0ooO0o0 = True
 if themeit : display = themeit % display
 OOOO00OOO00 = xbmcgui . ListItem ( display , iconImage = "DefaultFolder.png" , thumbnailImage = icon )
 OOOO00OOO00 . setInfo ( type = "Video" , infoLabels = { "Title" : display , "Plot" : Oo0Ooo } )
 OOOO00OOO00 . setProperty ( "Fanart_Image" , fanart )
 if not menu == None : OOOO00OOO00 . addContextMenuItems ( menu , replaceItems = overwrite )
 OooO0ooO0o0 = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = I1I1iiii1IiI1i , listitem = OOOO00OOO00 , isFolder = False )
 return OooO0ooO0o0
 if 55 - 55: Oo0OO % oOOO % o00oO0oOo00
def I1IiO00Ooo0ooo0 ( name , url , mode , iconimage , fanart , description ) :
 I1I1iiii1IiI1i = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&fanart=" + urllib . quote_plus ( fanart )
 OooO0ooO0o0 = True
 OOOO00OOO00 = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 OOOO00OOO00 . setInfo ( type = "Video" , infoLabels = { "Title" : name } )
 OOOO00OOO00 . setProperty ( "Fanart_Image" , fanart )
 OooO0ooO0o0 = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = I1I1iiii1IiI1i , listitem = OOOO00OOO00 , isFolder = False )
 return OooO0ooO0o0
 if 74 - 74: I1Ii
def Oo0O00o0oo0OO ( name , url , mode , iconimage , fanart , description ) :
 I1I1iiii1IiI1i = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart ) + "&description=" + urllib . quote_plus ( description )
 OooO0ooO0o0 = True
 OOOO00OOO00 = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 OOOO00OOO00 . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description } )
 OOOO00OOO00 . setProperty ( "Fanart_Image" , fanart )
 if mode == 90 :
  OooO0ooO0o0 = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = I1I1iiii1IiI1i , listitem = OOOO00OOO00 , isFolder = False )
 else :
  OooO0ooO0o0 = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = I1I1iiii1IiI1i , listitem = OOOO00OOO00 , isFolder = True )
 return OooO0ooO0o0
 if 97 - 97: i11iIiiIii + I1I11 / Oo0OO % IIIi
 if 38 - 38: IIIi % Iii % I1 - oOOO - O000oo
def iIiIIi11iI ( ) :
 ooo00o0o = [ ]
 OOOO00o000o = sys . argv [ 2 ]
 if len ( OOOO00o000o ) >= 2 :
  o0ooooO0 = sys . argv [ 2 ]
  IIII1ii1 = o0ooooO0 . replace ( '?' , '' )
  if ( o0ooooO0 [ len ( o0ooooO0 ) - 1 ] == '/' ) :
   o0ooooO0 = o0ooooO0 [ 0 : len ( o0ooooO0 ) - 2 ]
  OOO0O0OOo = IIII1ii1 . split ( '&' )
  ooo00o0o = { }
  for i1111IIiii1 in range ( len ( OOO0O0OOo ) ) :
   Iii1 = { }
   Iii1 = OOO0O0OOo [ i1111IIiii1 ] . split ( '=' )
   if ( len ( Iii1 ) ) == 2 :
    ooo00o0o [ Iii1 [ 0 ] ] = Iii1 [ 1 ]
    if 96 - 96: oOOO / Oo00o0o0 . I1 . oOOO
  return ooo00o0o
  if 91 - 91: I1 . IIIi + o00oO0oOo00
o0ooooO0 = iIiIIi11iI ( )
iiiI1 = None
Ii1i1i1i1I1Ii = None
I1iII1IIi1IiI = None
o00O = None
iiIi1IIiI = None
o0O0Oo00 = None
if 8 - 8: O000oo
try : I1iII1IIi1IiI = urllib . unquote_plus ( o0ooooO0 [ "mode" ] )
except : pass
try : Ii1i1i1i1I1Ii = urllib . unquote_plus ( o0ooooO0 [ "name" ] )
except : pass
try : iiiI1 = urllib . unquote_plus ( o0ooooO0 [ "url" ] )
except : pass
try : o00O = urllib . unquote_plus ( o0ooooO0 [ "iconimage" ] )
except : pass
try : iiIi1IIiI = urllib . unquote_plus ( o0ooooO0 [ "fanart" ] )
except : pass
try : o0O0Oo00 = urllib . unquote_plus ( o0ooooO0 [ "description" ] )
except : pass
if 55 - 55: Oo00o0o0
wiz . log ( '[ Version : \'%s\' ] [ Mode : \'%s\' ] [ Name : \'%s\' ] [ Url : \'%s\' ]' % ( O00ooooo00 , I1iII1IIi1IiI if not I1iII1IIi1IiI == '' else None , Ii1i1i1i1I1Ii , iiiI1 ) )
def i1iiIo0o ( ) :
 if 73 - 73: I1I11 % o00oO0oOo00
 for file in os . listdir ( ooOo ) :
  if file . endswith ( ".zip" ) :
   iiiI1 = xbmc . translatePath ( os . path . join ( ooOo , file ) )
   I1IiO00Ooo0ooo0 ( file , iiiI1 , 'read' , o0oOoO00o , o0oOoO00o , '' )
   if 71 - 71: Oo00o0o0 - Oo0O00O0O * oOOO * I1Ii + o00oO0oOo00 * oO00OoOO000o
def ooO ( ) :
 i1i111 = xbmc . translatePath ( os . path . join ( 'special://' , 'home' ) )
 for file in os . listdir ( ooOo ) :
  if file . endswith ( ".zip" ) :
   iiiI1 = xbmc . translatePath ( os . path . join ( ooOo , file ) )
   Oo0O00o0oo0OO ( file , iiiI1 , 'dell' , o0oOoO00o , o0oOoO00o , '' )
   if 25 - 25: Oo0O00O0O % I1IiiiiI * I1 - iII1Ii
def O0000OOO0 ( content , viewType ) :
 if 95 - 95: OOO00O0O % I1111i * OOO00O0O + OoOooO . I1111i % Oo0O00O0O
 if 6 - 6: I1I11 - Oo0OO * o00oO0oOo00 + I1I11 % o00oO0oOo00
 if wiz . getS ( 'auto-view' ) == 'true' :
  wiz . ebi ( "Container.SetViewMode(%s)" % wiz . getS ( viewType ) )
  if 100 - 100: iII1Ii % I1111i - I1Ii % I1Ii % I1Ii / Oo0OO
if I1iII1IIi1IiI == None : Oooo0 ( )
if 83 - 83: Oo00o0o0 - Oo0OO - Iii % OooOoooOo - O0OoOO0o . o00oO0oOo00
elif I1iII1IIi1IiI == 'wizardupdate' : wiz . wizardUpdate ( )
elif I1iII1IIi1IiI == 'builds' : iIi1 ( )
elif I1iII1IIi1IiI == 'viewbuild' : o00O00oO00 ( Ii1i1i1i1I1Ii )
elif I1iII1IIi1IiI == 'buildinfo' : I1111ii11IIII ( Ii1i1i1i1I1Ii )
elif I1iII1IIi1IiI == 'install' : i1iIIII1iiIIi ( Ii1i1i1i1I1Ii , iiiI1 )
elif I1iII1IIi1IiI == 'theme' : i1iIIII1iiIIi ( Ii1i1i1i1I1Ii , I1iII1IIi1IiI , iiiI1 )
if 96 - 96: oOOO + I1111i . OooOoooOo
elif I1iII1IIi1IiI == 'maint' : i11II ( Ii1i1i1i1I1Ii )
elif I1iII1IIi1IiI == 'speed' : oOOoo ( )
elif I1iII1IIi1IiI == 'advancedsetting' : Oo00ooO0OoOo ( )
elif I1iII1IIi1IiI == 'autoadvanced' : oOOo0OoOOOoo ( ) ; wiz . refresh ( )
elif I1iII1IIi1IiI == 'asciicheck' : wiz . asciiCheck ( )
elif I1iII1IIi1IiI == 'backupbuild' : wiz . backUpOptions ( 'build' )
elif I1iII1IIi1IiI == 'backupgui' : wiz . backUpOptions ( 'guifix' )
elif I1iII1IIi1IiI == 'backuptheme' : wiz . backUpOptions ( 'theme' )
elif I1iII1IIi1IiI == 'backupaddon' : wiz . backUpOptions ( 'addondata' )
elif I1iII1IIi1IiI == 'clearbackup' : wiz . cleanupBackup ( )
elif I1iII1IIi1IiI == 'convertpath' : wiz . convertSpecial ( OOOo0 )
elif I1iII1IIi1IiI == 'currentsettings' : iIIi11 ( )
elif I1iII1IIi1IiI == 'fullclean' : ii1IOoO0O ( ) ; wiz . refresh ( )
elif I1iII1IIi1IiI == 'clearcache' : ooIiI11i1I11111 ( ) ; wiz . refresh ( )
elif I1iII1IIi1IiI == 'clearpackages' : wiz . clearPackages ( ) ; wiz . refresh ( )
elif I1iII1IIi1IiI == 'clearcrash' : wiz . clearCrash ( ) ; wiz . refresh ( )
elif I1iII1IIi1IiI == 'clearthumb' : Ii1IIIIIIiI1 ( ) ; wiz . refresh ( )
elif I1iII1IIi1IiI == 'checksources' : wiz . checkSources ( ) ; wiz . refresh ( )
elif I1iII1IIi1IiI == 'checkrepos' : wiz . checkRepos ( ) ; wiz . refresh ( )
elif I1iII1IIi1IiI == 'freshstart' : Oo0 ( )
elif I1iII1IIi1IiI == 'forceupdate' : wiz . forceUpdate ( )
elif I1iII1IIi1IiI == 'forceclose' : wiz . killxbmc ( )
elif I1iII1IIi1IiI == 'forceskin' : wiz . ebi ( "ReloadSkin()" ) ; wiz . refresh ( )
elif I1iII1IIi1IiI == 'hidepassword' : wiz . hidePassword ( )
elif I1iII1IIi1IiI == 'unhidepassword' : wiz . unhidePassword ( )
elif I1iII1IIi1IiI == 'enableaddons' : OOo000o0 ( )
elif I1iII1IIi1IiI == 'toggleaddon' : wiz . toggleAddon ( Ii1i1i1i1I1Ii , iiiI1 ) ; wiz . refresh ( )
elif I1iII1IIi1IiI == 'togglecache' : oOO0Oooo ( Ii1i1i1i1I1Ii ) ; wiz . refresh ( )
elif I1iII1IIi1IiI == 'toggleadult' : wiz . toggleAdult ( ) ; wiz . refresh ( )
elif I1iII1IIi1IiI == 'changefeq' : oO0o0oO ( ) ; wiz . refresh ( )
elif I1iII1IIi1IiI == 'uploadlog' : uploadLog . Main ( )
elif I1iII1IIi1IiI == 'viewlog' : OOOO00OoooO ( )
elif I1iII1IIi1IiI == 'viewwizlog' : ooo0O00000oo0 ( )
elif I1iII1IIi1IiI == 'viewerrorlog' : OOOoOo ( )
elif I1iII1IIi1IiI == 'clearwizlog' : oo0ooO0O0o = open ( oOOoo00O0O , 'w' ) ; oo0ooO0O0o . close ( ) ; wiz . LogNotify ( Oo0Ooo , "Wizard Log Cleared!" )
elif I1iII1IIi1IiI == 'purgedb' : I1ii1i1iiii ( )
elif I1iII1IIi1IiI == 'fixaddonupdate' : wiz . purgeDb ( os . path . join ( o00 , wiz . latestDB ( 'Addons' ) ) )
elif I1iII1IIi1IiI == 'removeaddons' : ii1I1I1i1i11i ( )
elif I1iII1IIi1IiI == 'removeaddon' : oOIii11111iiI ( Ii1i1i1i1I1Ii )
elif I1iII1IIi1IiI == 'removeaddondata' : IiI1II11ii1ii ( )
elif I1iII1IIi1IiI == 'removedata' : ii111IIII ( Ii1i1i1i1I1Ii )
elif I1iII1IIi1IiI == 'resetaddon' : OOOoO00O = wiz . cleanHouse ( iI1Ii11111iIi , ignore = True ) ; wiz . LogNotify ( Oo0Ooo , "Addon_Data reset" )
elif I1iII1IIi1IiI == 'systeminfo' : Ii11I1iIiiI ( )
elif I1iII1IIi1IiI == 'restorezip' : IIIII1i ( 'build' )
elif I1iII1IIi1IiI == 'restoregui' : IIIII1i ( 'gui' )
elif I1iII1IIi1IiI == 'restoreaddon' : IIIII1i ( 'addondata' )
elif I1iII1IIi1IiI == 'restoreextzip' : II11iiii ( 'build' )
elif I1iII1IIi1IiI == 'restoreextgui' : II11iiii ( 'gui' )
elif I1iII1IIi1IiI == 'restoreextaddon' : II11iiii ( 'addondata' )
elif I1iII1IIi1IiI == 'writeadvanced' : oOoOo ( Ii1i1i1i1I1Ii )
if 54 - 54: I1 . OooOoooOo / oO00OoOO000o % OOO00O0O / I1111i
elif I1iII1IIi1IiI == 'apk1' : oo0OOo0O ( )
elif I1iII1IIi1IiI == 'apkgame' : ii ( iiiI1 )
elif I1iII1IIi1IiI == 'select' : II1IOoOo000oOo0oo ( iiiI1 )
elif I1iII1IIi1IiI == 'grab' : i1iI1iii11i ( Ii1i1i1i1I1Ii , iiiI1 )
elif I1iII1IIi1IiI == 'rom' : iiIiI ( iiiI1 )
elif I1iII1IIi1IiI == 'apkscrape' : APK ( )
elif I1iII1IIi1IiI == 'apkshow' : Ii1iI1iI11I1 ( iiiI1 )
elif I1iII1IIi1IiI == 'apkkodi' : o0OO0oO0oOO0O ( )
elif I1iII1IIi1IiI == 'intellaunch' : oo0o0000Oo0 ( )
elif I1iII1IIi1IiI == 'intelselect' : iI11iiii1I ( Ii1i1i1i1I1Ii , iiiI1 , o00O , iiIi1IIiI , o0O0Oo00 )
elif I1iII1IIi1IiI == 'emurom' : oOoi1i ( )
elif I1iII1IIi1IiI == 'roms' : i1iiI ( )
elif I1iII1IIi1IiI == 'snes' : OOoOIiIIII ( )
elif I1iII1IIi1IiI == 'nes' : IiII1iiIiI ( )
elif I1iII1IIi1IiI == 'gen' : iIIIIiiIii ( )
elif I1iII1IIi1IiI == 'atr' : ooOooOoOoO ( )
elif I1iII1IIi1IiI == 'n64' : iIIiIIIi ( )
elif I1iII1IIi1IiI == 'tbg' : oOo00o00oO ( )
elif I1iII1IIi1IiI == 'nds' : IiI1i111IiIiIi1 ( )
elif I1iII1IIi1IiI == 'ps' : oo0O0o00 ( )
elif I1iII1IIi1IiI == 'apkinstall' : oOO00oO00O0OO ( Ii1i1i1i1I1Ii , iiiI1 , "None" )
elif I1iII1IIi1IiI == 'rominstall' : IiiIi ( Ii1i1i1i1I1Ii , iiiI1 , )
if 65 - 65: I1I11 . I1I11 - Oo00o0o0 + oOOO / i11iIiiIii
elif I1iII1IIi1IiI == 'youtube' : i1iii1ii ( iiiI1 )
elif I1iII1IIi1IiI == 'viewVideo' : iIIIiiiiIiI1III ( iiiI1 )
if 90 - 90: O000oo + I1I11
elif I1iII1IIi1IiI == 'savedata' : Ii1Ii1Ii1I1I ( )
elif I1iII1IIi1IiI == 'togglesetting' : wiz . setS ( Ii1i1i1i1I1Ii , 'false' if wiz . getS ( Ii1i1i1i1I1Ii ) == 'true' else 'true' ) ; wiz . refresh ( )
if 9 - 9: O000oo . Oo0O00O0O + OooOoooOo - oOOO
elif I1iII1IIi1IiI == 'trakt' : iiIi1iiI1I ( )
elif I1iII1IIi1IiI == 'savetrakt' : traktit . traktIt ( 'update' , Ii1i1i1i1I1Ii )
elif I1iII1IIi1IiI == 'restoretrakt' : traktit . traktIt ( 'restore' , Ii1i1i1i1I1Ii )
elif I1iII1IIi1IiI == 'addontrakt' : traktit . traktIt ( 'clearaddon' , Ii1i1i1i1I1Ii )
elif I1iII1IIi1IiI == 'cleartrakt' : traktit . clearSaved ( Ii1i1i1i1I1Ii )
elif I1iII1IIi1IiI == 'authtrakt' : traktit . activateTrakt ( Ii1i1i1i1I1Ii ) ; wiz . refresh ( )
elif I1iII1IIi1IiI == 'updatetrakt' : traktit . autoUpdate ( 'all' )
elif I1iII1IIi1IiI == 'importtrakt' : traktit . importlist ( Ii1i1i1i1I1Ii ) ; wiz . refresh ( )
if 30 - 30: O0OoOO0o / iII1Ii . O0OoOO0o
elif I1iII1IIi1IiI == 'realdebrid' : OOo000OO000 ( )
elif I1iII1IIi1IiI == 'savedebrid' : debridit . debridIt ( 'update' , Ii1i1i1i1I1Ii )
elif I1iII1IIi1IiI == 'restoredebrid' : debridit . debridIt ( 'restore' , Ii1i1i1i1I1Ii )
elif I1iII1IIi1IiI == 'addondebrid' : debridit . debridIt ( 'clearaddon' , Ii1i1i1i1I1Ii )
elif I1iII1IIi1IiI == 'cleardebrid' : debridit . clearSaved ( Ii1i1i1i1I1Ii )
elif I1iII1IIi1IiI == 'authdebrid' : debridit . activateDebrid ( Ii1i1i1i1I1Ii ) ; wiz . refresh ( )
elif I1iII1IIi1IiI == 'updatedebrid' : debridit . autoUpdate ( 'all' )
elif I1iII1IIi1IiI == 'importdebrid' : debridit . importlist ( Ii1i1i1i1I1Ii ) ; wiz . refresh ( )
if 17 - 17: oOOO + Oo0O00O0O * Oo0O00O0O
elif I1iII1IIi1IiI == 'addons' : oOOoO0OO00OOo0 ( )
elif I1iII1IIi1IiI == 'addoninstall' : oO00 ( Ii1i1i1i1I1Ii )
if 5 - 5: I1111i % Oo0O00O0O . I1I11
elif I1iII1IIi1IiI == 'contact' : notify . contact ( O0oo00o0O )
elif I1iII1IIi1IiI == 'settings' : wiz . openS ( Ii1i1i1i1I1Ii ) ; wiz . refresh ( )
elif I1iII1IIi1IiI == 'opensettings' : id = eval ( iiiI1 . upper ( ) + 'ID' ) [ Ii1i1i1i1I1Ii ] [ 'plugin' ] ; oO00o00 = wiz . addonId ( id ) ; oO00o00 . openSettings ( ) ; wiz . refresh ( )
if 51 - 51: oOOO * O000oo . Oo0O00O0O . I1IiiiiI - IIIi / OOO00O0O
elif I1iII1IIi1IiI == 'developer' : OooOo ( )
elif I1iII1IIi1IiI == 'converttext' : wiz . convertText ( Ii1i1i1i1I1Ii )
elif I1iII1IIi1IiI == 'testnotify' : i1iI1Ii11Ii1 ( )
elif I1iII1IIi1IiI == 'bre' : iiiI11 ( )
elif I1iII1IIi1IiI == 'full' : backuprestore . FullBackup ( )
elif I1iII1IIi1IiI == 'backb' : backuprestore . Backup ( )
elif I1iII1IIi1IiI == 'backad' : backuprestore . ADDON_DATA_BACKUP ( )
elif I1iII1IIi1IiI == 'refull' : i1iiIo0o ( )
elif I1iII1IIi1IiI == 'delbu' : ooO ( )
elif I1iII1IIi1IiI == 'delall' : backuprestore . DeleteAllBackups ( )
elif I1iII1IIi1IiI == 'read' : backuprestore . READ_ZIP ( iiiI1 )
elif I1iII1IIi1IiI == 'dell' : backuprestore . DeleteBackup ( iiiI1 )
elif I1iII1IIi1IiI == 'testupdate' : O0oO0oo0O ( )
elif I1iII1IIi1IiI == 'testfirst' : III1iiiII1ii ( )
if I1iII1IIi1IiI not in [ '' , 'togglesettings' , 'settings' , 'contact' ] : xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
# dd678faae9ac167bc83abf78e5cb2f3f0688d3a3