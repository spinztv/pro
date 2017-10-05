################################################################################
#      Copyright (C) 2015 Surfacingx                                           #
#                                                                              #
#  This Program is free software; you can redistribute it and/or modify        #
#  it under the terms of the GNU General Public License as published by        #
#  the Free Software Foundation; either version 2, or (at your option)         #
#  any later version.                                                          #
#                                                                              #
#  This Program is distributed in the hope that it will be useful,             #
#  but WITHOUT ANY WARRANTY; without even the implied warranty of              #
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the                #
#  GNU General Public License for more details.                                #
#                                                                              #
#  You should have received a copy of the GNU General Public License           #
#  along with XBMC; see the file COPYING.  If not, write to                    #
#  the Free Software Foundation, 675 Mass Ave, Cambridge, MA 02139, USA.       #
#  http://www.gnu.org/copyleft/gpl.html                                        #
################################################################################
if 64 - 64: i11iIiiIii
import xbmc , xbmcaddon , xbmcgui , xbmcplugin , os , sys , xbmcvfs , glob
import shutil
import urllib2 , urllib
import re
import zipfile
import uservar
import fnmatch
import plugintools
import base64
import time
import platform , subprocess
import zipfile
import yt
import ookla
import requests
if 65 - 65: O0 / iIii1I11I1II1 % OoooooooOO - i1IIi
try : from sqlite3 import dbapi2 as database
except : from pysqlite2 import dbapi2 as database
from datetime import date , datetime , timedelta
from urlparse import urljoin
from resources . libs import extract , downloader , notify , debridit , traktit , loginit , skinSwitch , uploadLog , yt , wizard as wiz
if 73 - 73: II111iiii
IiII1IiiIiI1 = uservar . ADDON_ID
iIiiiI1IiI1I1 = uservar . ADDON_ID
o0OoOoOO00 = uservar . ADDON_ID
I11i = xbmcaddon . Addon ( IiII1IiiIiI1 )
O0O = xbmc . translatePath ( 'special://home/addons/' )
Oo = xbmc . translatePath ( 'special://home/addonsbroke/' )
I1ii11iIi11i = wiz . addonId ( IiII1IiiIiI1 )
I1IiI = xbmcgui . DialogProgress ( )
o0OOO = uservar . ADDONTITLE
if 13 - 13: ooOo + Ooo0O
IiiIII111iI = base64 . decodestring
IiII = I1ii11iIi11i . getSetting ( 'User' )
iI1Ii11111iIi = I11i . getAddonInfo ( 'path' ) . decode ( "utf-8" )
i1i1II = xbmc . translatePath ( os . path . join ( iI1Ii11111iIi , "resources" , "iiNT3LiiList.txt" ) )
O0oo0OO0 = wiz . addonInfo ( IiII1IiiIiI1 , 'version' )
I1i1iiI1 = wiz . addonInfo ( IiII1IiiIiI1 , 'path' )
iiIIIII1i1iI = xbmcgui . Dialog ( )
o0oO0 = xbmcgui . Dialog ( )
oo00 = xbmcgui . DialogProgress ( )
o00 = xbmc . translatePath ( 'special://home/' )
Oo0oO0ooo = ( IiiIII111iI ( 'aHR0cDovL2dlbmlldHYuY28udWsvc3Bpbnov' ) )
o0oOoO00o = xbmc . translatePath ( 'special://home/userdata/addon_data/plugin.program.SpinzTV' )
i1 = xbmc . translatePath ( os . path . join ( 'special://home/addons/plugin.program.SpinzTV/imports/tvGuide/ResetDatabase.py' ) )
oOOoo00O0O = xbmc . translatePath ( 'special://thumbnails' ) ;
i1111 = "Xhoans"
i11 = base64 . decodestring ( 'LnBocA==' )
I11 = I1ii11iIi11i . getLocalizedString
if 98 - 98: I1111 * o0o0Oo0oooo0 / I1I1i1 * oO0 / IIIi1i1I
if 72 - 72: iii11iiII % i11IiIiiIIIII / IiiIII111ii / iiIIi1IiIi11 . i1Ii
if 25 - 25: OO00O0O0O00Oo + OOoooooO / i1IIi . i11IiIiiIIIII % I1111 . I1I1i1
i1I111I = int ( sys . argv [ 1 ] )
i11I1IIiiIi = xbmc . translatePath ( I1ii11iIi11i . getAddonInfo ( 'profile' ) . decode ( 'utf-8' ) )
IiIiIi = xbmc . translatePath ( os . path . join ( 'special://home/userdata' , 'favourites.xml' ) )
II = o0oOoO00o + '/addons.ini'
iI = xbmc . translatePath ( os . path . join ( '//storage//emulated//0//Download' , '' ) )
iI11iiiI1II = xbmc . translatePath ( 'special://logpath/' )
O0oooo0Oo00 = xbmc . translatePath ( 'special://profile/' )
O0O = os . path . join ( o00 , 'addons' )
zip = plugintools . get_setting ( "zip" )
Ii11iii11I = xbmc . translatePath ( os . path . join ( zip ) )
oOo00Oo00O = os . path . join ( o00 , 'userdata' )
iI11i1I1 = os . path . join ( O0O , IiII1IiiIiI1 )
o0o0OOO0o0 = os . path . join ( O0O , 'packages' )
ooOOOo0oo0O0 = os . path . join ( oOo00Oo00O , 'addon_data' )
o0 = os . path . join ( oOo00Oo00O , 'addon_data' , IiII1IiiIiI1 )
I11II1i = os . path . join ( oOo00Oo00O , 'advancedsettings.xml' )
IIIII = os . path . join ( oOo00Oo00O , 'sources.xml' )
ooooooO0oo = os . path . join ( oOo00Oo00O , 'favourites.xml' )
IIiiiiiiIi1I1 = os . path . join ( oOo00Oo00O , 'profiles.xml' )
I1IIIii = os . path . join ( oOo00Oo00O , 'guisettings.xml' )
oOoOooOo0o0 = os . path . join ( oOo00Oo00O , 'Thumbnails' )
OOOO = os . path . join ( oOo00Oo00O , 'Database' )
OOO00 = os . path . join ( I1i1iiI1 , 'fanart.jpg' )
iiiiiIIii = os . path . join ( I1i1iiI1 , 'icon.png' )
O000OO0 = os . path . join ( I1i1iiI1 , 'resources' , 'art' )
I11iii1Ii = os . path . join ( o0 , 'wizard.log' )
I1IIiiIiii = xbmc . getSkinDir ( )
O000oo0O = wiz . getS ( 'buildname' )
OOOOi11i1 = wiz . getS ( 'defaultskin' )
IIIii1II1II = wiz . getS ( 'defaultskinname' )
i1I1iI = wiz . getS ( 'defaultskinignore' )
oo0OooOOo0 = wiz . getS ( 'buildversion' )
o0O = wiz . getS ( 'buildtheme' )
O00oO = wiz . getS ( 'latestversion' )
I11i1I1I = wiz . getS ( 'installmethod' )
oO0Oo = wiz . getS ( 'show15' )
oOOoo0Oo = wiz . getS ( 'show16' )
o00OO00OoO = wiz . getS ( 'show17' )
OOOO0OOoO0O0 = wiz . getS ( 'show18' )
O0Oo000ooO00 = wiz . getS ( 'adult' )
oO0Ii1iIiII1ii1 = wiz . getS ( 'showmaint' )
ooOooo000oOO = wiz . getS ( 'autoclean' )
Oo0oOOo = wiz . getS ( 'clearcache' )
Oo0OoO00oOO0o = wiz . getS ( 'clearpackages' )
OOO00O = wiz . getS ( 'clearthumbs' )
OOoOO0oo0ooO = wiz . getS ( 'autocleanfeq' )
O0o0O00Oo0o0 = wiz . getS ( 'nextautocleanup' )
O00O0oOO00O00 = wiz . getS ( 'includevideo' )
i1Oo00 = wiz . getS ( 'includeall' )
i1i = wiz . getS ( 'includebob' )
iiI111I1iIiI = wiz . getS ( 'includephoenix' )
IIIi1I1IIii1II = wiz . getS ( 'includespecto' )
O0ii1ii1ii = wiz . getS ( 'includegenesis' )
oooooOoo0ooo = wiz . getS ( 'includeexodus' )
I1I1IiI1 = wiz . getS ( 'includeonechan' )
III1iII1I1ii = wiz . getS ( 'includesalts' )
oOOo0 = wiz . getS ( 'includesaltslite' )
oo00O00oO = wiz . getS ( 'seperate' )
iIiIIIi = wiz . getS ( 'notify' )
ooo00OOOooO = wiz . getS ( 'noteid' )
O00OOOoOoo0O = wiz . getS ( 'notedismiss' )
O000OOo00oo = wiz . getS ( 'traktlastsave' )
oo0OOo = wiz . getS ( 'debridlastsave' )
ooOOO00Ooo = wiz . getS ( 'loginlastsave' )
IiIIIi1iIi = wiz . getS ( 'keepfavourites' )
ooOOoooooo = wiz . getS ( 'keepsources' )
II1I = wiz . getS ( 'keepprofiles' )
O0i1II1Iiii1I11 = wiz . getS ( 'keepadvanced' )
IIII = wiz . getS ( 'keeprepos' )
iiIiI = wiz . getS ( 'keepsuper' )
o00oooO0Oo = wiz . getS ( 'keepwhitelist' )
o0O0OOO0Ooo = wiz . getS ( 'keeptrakt' )
iiIiII1 = wiz . getS ( 'keepdebrid' )
OOO00O0O = wiz . getS ( 'keeplogin' )
ooOOO00Ooo = wiz . getS ( 'loginlastsave' )
iii = wiz . getS ( 'developer' )
oOooOOOoOo = wiz . getS ( 'enable3rd' )
i1Iii1i1I = wiz . getS ( 'wizard1name' )
OOoO00 = wiz . getS ( 'wizard1url' )
IiI111111IIII = wiz . getS ( 'wizard2name' )
i1Iiii111iI1iIi1 = wiz . getS ( 'wizard2url' )
OOO = wiz . getS ( 'wizard3name' )
oo0OOo0 = wiz . getS ( 'wizard3url' )
I11IiI = I1ii11iIi11i . getSetting ( 'path' ) if not I1ii11iIi11i . getSetting ( 'path' ) == '' else 'special://home/'
O0ooO0Oo00o = os . path . join ( I11IiI , 'My_Builds' , '' )
OOoOO0oo0ooO = int ( float ( OOoOO0oo0ooO ) ) if OOoOO0oo0ooO . isdigit ( ) else 0
ooO0oOOooOo0 = date . today ( )
i1I1ii11i1Iii = ooO0oOOooOo0 + timedelta ( days = 1 )
I1IiiiiI = ooO0oOOooOo0 + timedelta ( days = 3 )
o0OIiII = float ( xbmc . getInfoLabel ( "System.BuildVersion" ) [ : 4 ] )
ii1iII1II = wiz . mediaCenter ( )
Iii1I1I11iiI1 = uservar . EXCLUDES
I1I1i1I = uservar . BUILDFILE
ii1I = uservar . APKFILE
O0oO0 = uservar . YOUTUBETITLE
oO0O0OO0O = uservar . YOUTUBEFILE
OO = uservar . ADDONFILE
OoOoO = uservar . ADVANCEDFILE
Ii1I1i = uservar . UPDATECHECK if str ( uservar . UPDATECHECK ) . isdigit ( ) else 1
OOI1iI1ii1II = ooO0oOOooOo0 + timedelta ( days = Ii1I1i )
O0O0OOOOoo = uservar . NOTIFICATION
oOooO0 = uservar . ENABLE
Ii1I1Ii = uservar . HEADERMESSAGE
OOoO0 = uservar . AUTOUPDATE
OO0Oooo0oOO0O = uservar . WIZARDFILE
o00O0 = uservar . HIDECONTACT
oOO0O00Oo0O0o = uservar . CONTACT
ii1 = uservar . CONTACTICON if not uservar . CONTACTICON == 'http://' else iiiiiIIii
I1iIIiiIIi1i = uservar . CONTACTFANART if not uservar . CONTACTFANART == 'http://' else OOO00
O0O0ooOOO = uservar . HIDESPACERS
oOOo0O00o = uservar . COLOR1
iIiIi11 = uservar . COLOR2
OOOiiiiI = uservar . THEME1
oooOo0OOOoo0 = uservar . THEME2
OOoO = uservar . THEME3
OO0O000 = uservar . THEME4
iiIiI1i1 = uservar . THEME5
oO0O00oOOoooO = uservar . ICONBUILDS if not uservar . ICONBUILDS == 'http://' else iiiiiIIii
IiIi11iI = uservar . ICONMAINT if not uservar . ICONMAINT == 'http://' else iiiiiIIii
Oo0O00O000 = uservar . ICONAPK if not uservar . ICONAPK == 'http://' else iiiiiIIii
i11I1IiII1i1i = uservar . ICONADDONS if not uservar . ICONADDONS == 'http://' else iiiiiIIii
oo = uservar . ICONYOUTUBE if not uservar . ICONYOUTUBE == 'http://' else iiiiiIIii
I1111i = uservar . ICONSAVE if not uservar . ICONSAVE == 'http://' else iiiiiIIii
iIIii = uservar . ICONTRAKT if not uservar . ICONTRAKT == 'http://' else iiiiiIIii
o00O0O = uservar . ICONREAL if not uservar . ICONREAL == 'http://' else iiiiiIIii
ii1iii1i = uservar . ICONLOGIN if not uservar . ICONLOGIN == 'http://' else iiiiiIIii
Iii1I1111ii = uservar . ICONCONTACT if not uservar . ICONCONTACT == 'http://' else iiiiiIIii
ooOoO00 = uservar . ICONSETTINGS if not uservar . ICONSETTINGS == 'http://' else iiiiiIIii
Ii1IIiI1i = uservar . ICONSPINZ if not uservar . ICONSPINZ == 'http://' else iiiiiIIii
o0O00Oo0 = uservar . ICONKODI if not uservar . ICONKODI == 'http://' else iiiiiIIii
IiII111i1i11 = uservar . ICONSPMC if not uservar . ICONSPMC == 'http://' else iiiiiIIii
i111iIi1i1II1 = uservar . ICONGAMES if not uservar . ICONGAMES == 'http://' else iiiiiIIii
oooO = uservar . ICONMOVIES if not uservar . ICONMOVIES == 'http://' else iiiiiIIii
i1I1i111Ii = uservar . ICONANDROID if not uservar . ICONANDROID == 'http://' else iiiiiIIii
ooo = uservar . ICONSPEED if not uservar . ICONSPEED == 'http://' else iiiiiIIii
i1i1iI1iiiI = uservar . ICONPRO if not uservar . ICONPRO == 'http://' else iiiiiIIii
i11I1IiII1i1i = os . path . join ( O000OO0 , 'spinzicon.png' )
oo = os . path . join ( O000OO0 , 'spinzicon.png' )
ii1iii1i = os . path . join ( O000OO0 , 'spinzicon.png' )
Ooo0oOooo0 = wiz . LOGFILES
oOOOoo00 = traktit . TRAKTID
iiIiIIIiiI = debridit . DEBRIDID
iiI1IIIi = loginit . LOGINID
II11IiIi11 = 'http://tribeca.tvaddons.ag/tools/maintenance/modules/'
IIOOO0O00O0OOOO = 'http://mirrors.kodi.tv/addons/jarvis/'
I1iiii1I = [ 'Always Ask' , 'Reload Profile' , 'Force Close' ]
OOo0 = [ 'metadata.album.universal' , 'metadata.artists.universal' , 'metadata.common.fanart.tv' , 'metadata.common.imdb.com' , 'metadata.common.musicbrainz.org' , 'metadata.themoviedb.org' , 'metadata.tvdb.com' , 'service.xbmc.versioncheck' ]
if 73 - 73: iiIIi1IiIi11
if 42 - 42: i11iIiiIii * iIii1I11I1II1 / oO0 . i11iIiiIii % i11IiIiiIIIII
if 41 - 41: i1Ii / O0
if 51 - 51: i11IiIiiIIIII % ooOo
OooOo = 'http://stvmc.net/APK/apktxts/Spinzapk.txt'
i11III1111iIi = 'http://stvmc.net/APK/apktxts/xxxapks.txt'
I1i111I = 'http://stvmc.net/APK/apktxts/emulator.txt'
Ooo = base64 . b64decode ( "aHR0cDovL3AuYnJvc2dpdC5wcm8vc3BpbnovZW11bGF0b3Itcm9tdHh0L1JPTVNUWFQvU05FU0EtQi50eHQ=" )
Oo0oo0O0o00O = base64 . b64decode ( "aHR0cDovL3AuYnJvc2dpdC5wcm8vc3BpbnovZW11bGF0b3Itcm9tdHh0L1JPTVNUWFQvU05FU0MtRS50eHQ=" )
I1i11 = base64 . b64decode ( "aHR0cDovL3AuYnJvc2dpdC5wcm8vc3BpbnovZW11bGF0b3Itcm9tdHh0L1JPTVNUWFQvU05FU0YtSC50eHQ=" )
IiIi1I1 = base64 . b64decode ( "aHR0cDovL3AuYnJvc2dpdC5wcm8vc3BpbnovZW11bGF0b3Itcm9tdHh0L1JPTVNUWFQvU05FU0ktSy50eHQ=" )
IiIIi1 = base64 . b64decode ( "aHR0cDovL3AuYnJvc2dpdC5wcm8vc3BpbnovZW11bGF0b3Itcm9tdHh0L1JPTVNUWFQvU05FU0wtTS50eHQ=" )
IIIIiii1IIii = base64 . b64decode ( "aHR0cDovL3AuYnJvc2dpdC5wcm8vc3BpbnovZW11bGF0b3Itcm9tdHh0L1JPTVNUWFQvU05FU04tTy50eHQ=" )
II1i11I = base64 . b64decode ( "aHR0cDovL3AuYnJvc2dpdC5wcm8vc3BpbnovZW11bGF0b3Itcm9tdHh0L1JPTVNUWFQvU05FU1AtUi50eHQ=" )
ii1I1IIii11 = base64 . b64decode ( "aHR0cDovL3AuYnJvc2dpdC5wcm8vc3BpbnovZW11bGF0b3Itcm9tdHh0L1JPTVNUWFQvU05FU1MudHh0" )
O0o0oO = base64 . b64decode ( "aHR0cDovL3AuYnJvc2dpdC5wcm8vc3BpbnovZW11bGF0b3Itcm9tdHh0L1JPTVNUWFQvU05FU1QtVi50eHQ=" )
IIIIiIiIi1 = base64 . b64decode ( "aHR0cDovL3AuYnJvc2dpdC5wcm8vc3BpbnovZW11bGF0b3Itcm9tdHh0L1JPTVNUWFQvU05FU1ctWi50eHQ=" )
I11iiiiI1i = base64 . b64decode ( "aHR0cDovL3AuYnJvc2dpdC5wcm8vc3BpbnovZW11bGF0b3Itcm9tdHh0L1JPTVNUWFQvTkVTQS1CLnR4dA==" )
iI1i11 = base64 . b64decode ( "aHR0cDovL3AuYnJvc2dpdC5wcm8vc3BpbnovZW11bGF0b3Itcm9tdHh0L1JPTVNUWFQvTkVTQy50eHQ=" )
OoOOoooOO0O = base64 . b64decode ( "aHR0cDovL3AuYnJvc2dpdC5wcm8vc3BpbnovZW11bGF0b3Itcm9tdHh0L1JPTVNUWFQvTkVTRC1FLnR4dA==" )
ooo00Ooo = base64 . b64decode ( "aHR0cDovL3AuYnJvc2dpdC5wcm8vc3BpbnovZW11bGF0b3Itcm9tdHh0L1JPTVNUWFQvTkVTRi1HLnR4dA==" )
Oo0o0O00 = base64 . b64decode ( "aHR0cDovL3AuYnJvc2dpdC5wcm8vc3BpbnovZW11bGF0b3Itcm9tdHh0L1JPTVNUWFQvTkVTSC1LLnR4dA==" )
ii1I1i11 = base64 . b64decode ( "aHR0cDovL3AuYnJvc2dpdC5wcm8vc3BpbnovZW11bGF0b3Itcm9tdHh0L1JPTVNUWFQvTkVTTC1NLnR4dA==" )
OOo0O0oo0OO0O = base64 . b64decode ( "aHR0cDovL3AuYnJvc2dpdC5wcm8vc3BpbnovZW11bGF0b3Itcm9tdHh0L1JPTVNUWFQvTkVTTi1RLnR4dA==" )
OO0 = base64 . b64decode ( "aHR0cDovL3AuYnJvc2dpdC5wcm8vc3BpbnovZW11bGF0b3Itcm9tdHh0L1JPTVNUWFQvTkVTUi1TLnR4dA==" )
o0Oooo = base64 . b64decode ( "aHR0cDovL3AuYnJvc2dpdC5wcm8vc3BpbnovZW11bGF0b3Itcm9tdHh0L1JPTVNUWFQvTkVTVC1WLnR4dA==" )
iiI = base64 . b64decode ( "aHR0cDovL3AuYnJvc2dpdC5wcm8vc3BpbnovZW11bGF0b3Itcm9tdHh0L1JPTVNUWFQvTkVTVy1aLnR4dA==" )
oO = base64 . b64decode ( "aHR0cDovL3AuYnJvc2dpdC5wcm8vc3BpbnovZW11bGF0b3Itcm9tdHh0L1JPTVNUWFQvR0VOQS1CLnR4dA==" )
IIiIi = base64 . b64decode ( "aHR0cDovL3AuYnJvc2dpdC5wcm8vc3BpbnovZW11bGF0b3Itcm9tdHh0L1JPTVNUWFQvR0VOQy1ELnR4dA==" )
OOoOooOoOOOoo = base64 . b64decode ( "aHR0cDovL3AuYnJvc2dpdC5wcm8vc3BpbnovZW11bGF0b3Itcm9tdHh0L1JPTVNUWFQvR0VORS1HLnR4dA==" )
Iiii1iI1i = base64 . b64decode ( "aHR0cDovL3AuYnJvc2dpdC5wcm8vc3BpbnovZW11bGF0b3Itcm9tdHh0L1JPTVNUWFQvR0VOSC1MLnR4dA==" )
I1ii1ii11i1I = base64 . b64decode ( "aHR0cDovL3AuYnJvc2dpdC5wcm8vc3BpbnovZW11bGF0b3Itcm9tdHh0L1JPTVNUWFQvR0VOTS1PLnR4dA==" )
o0OoOO = base64 . b64decode ( "aHR0cDovL3AuYnJvc2dpdC5wcm8vc3BpbnovZW11bGF0b3Itcm9tdHh0L1JPTVNUWFQvR0VOUC1SLnR4dA==" )
O0O0Oo00 = base64 . b64decode ( "aHR0cDovL3AuYnJvc2dpdC5wcm8vc3BpbnovZW11bGF0b3Itcm9tdHh0L1JPTVNUWFQvR0VOUy1ULnR4dA==" )
oOoO00o = base64 . b64decode ( "aHR0cDovL3AuYnJvc2dpdC5wcm8vc3BpbnovZW11bGF0b3Itcm9tdHh0L1JPTVNUWFQvR0VOVS1aLnR4dA==" )
oO00O0 = base64 . b64decode ( "aHR0cDovL3AuYnJvc2dpdC5wcm8vc3BpbnovZW11bGF0b3Itcm9tdHh0L1JPTVNUWFQvQVRSQS1CLnR4dA==" )
IIi1IIIi = base64 . b64decode ( "aHR0cDovL3AuYnJvc2dpdC5wcm8vc3BpbnovZW11bGF0b3Itcm9tdHh0L1JPTVNUWFQvQVRSQy1ELnR4dA==" )
O00Ooo = base64 . b64decode ( "aHR0cDovL3AuYnJvc2dpdC5wcm8vc3BpbnovZW11bGF0b3Itcm9tdHh0L1JPTVNUWFQvQVRSRS1HLnR4dA==" )
OOOO0OOO = base64 . b64decode ( "aHR0cDovL3AuYnJvc2dpdC5wcm8vc3BpbnovZW11bGF0b3Itcm9tdHh0L1JPTVNUWFQvQVRSSC1MLnR4dA==" )
i1i1ii = base64 . b64decode ( "aHR0cDovL3AuYnJvc2dpdC5wcm8vc3BpbnovZW11bGF0b3Itcm9tdHh0L1JPTVNUWFQvQVRSTS1PLnR4dA==" )
iII1ii1 = base64 . b64decode ( "aHR0cDovL3AuYnJvc2dpdC5wcm8vc3BpbnovZW11bGF0b3Itcm9tdHh0L1JPTVNUWFQvQVRSUC1SLnR4dA==" )
I1i1iiiI1 = base64 . b64decode ( "aHR0cDovL3AuYnJvc2dpdC5wcm8vc3BpbnovZW11bGF0b3Itcm9tdHh0L1JPTVNUWFQvQVRSUy1VLnR4dA==" )
iIIi = base64 . b64decode ( "aHR0cDovL3AuYnJvc2dpdC5wcm8vc3BpbnovZW11bGF0b3Itcm9tdHh0L1JPTVNUWFQvQVRSVi1aLnR4dA==" )
oO0o00oo0 = base64 . b64decode ( "aHR0cDovL3AuYnJvc2dpdC5wcm8vc3BpbnovZW11bGF0b3Itcm9tdHh0L1JPTVNUWFQvTjY0QS1CLnR4dA==" )
ii1IIII = base64 . b64decode ( "aHR0cDovL3AuYnJvc2dpdC5wcm8vc3BpbnovZW11bGF0b3Itcm9tdHh0L1JPTVNUWFQvTjY0Qy1FLnR4dA==" )
oO00oOooooo0 = base64 . b64decode ( "aHR0cDovL3AuYnJvc2dpdC5wcm8vc3BpbnovZW11bGF0b3Itcm9tdHh0L1JPTVNUWFQvTjY0Ri1KLnR4dA==" )
oOo = base64 . b64decode ( "aHR0cDovL3AuYnJvc2dpdC5wcm8vc3BpbnovZW11bGF0b3Itcm9tdHh0L1JPTVNUWFQvTjY0Sy1NLnR4dA==" )
O0OOooOoO = base64 . b64decode ( "aHR0cDovL3AuYnJvc2dpdC5wcm8vc3BpbnovZW11bGF0b3Itcm9tdHh0L1JPTVNUWFQvTjY0Ti1SLnR4dA==" )
i1II1I1Iii1 = base64 . b64decode ( "aHR0cDovL3AuYnJvc2dpdC5wcm8vc3BpbnovZW11bGF0b3Itcm9tdHh0L1JPTVNUWFQvTjY0Uy1ULnR4dA==" )
iiI11Iii = base64 . b64decode ( "aHR0cDovL3AuYnJvc2dpdC5wcm8vc3BpbnovZW11bGF0b3Itcm9tdHh0L1JPTVNUWFQvTjY0Vi1aLnR4dA==" )
O0o0O0 = base64 . b64decode ( "aHR0cDovL3AuYnJvc2dpdC5wcm8vc3BpbnovZW11bGF0b3Itcm9tdHh0L1JPTVNUWFQvVEdBLUIudHh0" )
Ii1II1I11i1 = base64 . b64decode ( "aHR0cDovL3AuYnJvc2dpdC5wcm8vc3BpbnovZW11bGF0b3Itcm9tdHh0L1JPTVNUWFQvVEdDLUUudHh0" )
oOoooooOoO = base64 . b64decode ( "aHR0cDovL3AuYnJvc2dpdC5wcm8vc3BpbnovZW11bGF0b3Itcm9tdHh0L1JPTVNUWFQvVEdGLUkudHh0" )
Ii111 = base64 . b64decode ( "aHR0cDovL3AuYnJvc2dpdC5wcm8vc3BpbnovZW11bGF0b3Itcm9tdHh0L1JPTVNUWFQvVEdKLU0udHh0" )
I111i1i1111 = base64 . b64decode ( "aHR0cDovL3AuYnJvc2dpdC5wcm8vc3BpbnovZW11bGF0b3Itcm9tdHh0L1JPTVNUWFQvVEdOLVEudHh0" )
IIII1 = base64 . b64decode ( "aHR0cDovL3AuYnJvc2dpdC5wcm8vc3BpbnovZW11bGF0b3Itcm9tdHh0L1JPTVNUWFQvVEdSLVUudHh0" )
I1I1i = base64 . b64decode ( "aHR0cDovL3AuYnJvc2dpdC5wcm8vc3BpbnovZW11bGF0b3Itcm9tdHh0L1JPTVNUWFQvVEdWLVoudHh0" )
I1IIIiIiIi = base64 . b64decode ( "aHR0cDovL3AuYnJvc2dpdC5wcm8vc3BpbnovZW11bGF0b3Itcm9tdHh0L1JPTVNUWFQvTkRTQS50eHQ=" )
IIIII1 = base64 . b64decode ( "aHR0cDovL3AuYnJvc2dpdC5wcm8vc3BpbnovZW11bGF0b3Itcm9tdHh0L1JPTVNUWFQvTkRTQi50eHQ=" )
iIi1Ii1i1iI = base64 . b64decode ( "aHR0cDovL3AuYnJvc2dpdC5wcm8vc3BpbnovZW11bGF0b3Itcm9tdHh0L1JPTVNUWFQvTkRTQy50eHQ=" )
IIiI1 = base64 . b64decode ( "aHR0cDovL3AuYnJvc2dpdC5wcm8vc3BpbnovZW11bGF0b3Itcm9tdHh0L1JPTVNUWFQvTkRTRC50eHQ=" )
i1iI1 = base64 . b64decode ( "aHR0cDovL3AuYnJvc2dpdC5wcm8vc3BpbnovZW11bGF0b3Itcm9tdHh0L1JPTVNUWFQvTkRTRS1GLnR4dA==" )
ii1I1IiiI1ii1i = base64 . b64decode ( "aHR0cDovL3AuYnJvc2dpdC5wcm8vc3BpbnovZW11bGF0b3Itcm9tdHh0L1JPTVNUWFQvTkRTRy1ILnR4dA==" )
O0o = base64 . b64decode ( "aHR0cDovL3AuYnJvc2dpdC5wcm8vc3BpbnovZW11bGF0b3Itcm9tdHh0L1JPTVNUWFQvTkRTSS1KLnR4dA==" )
oO0OoO00o = base64 . b64decode ( "aHR0cDovL3AuYnJvc2dpdC5wcm8vc3BpbnovZW11bGF0b3Itcm9tdHh0L1JPTVNUWFQvTkRTSy1MLnR4dA==" )
II1iiiiII = base64 . b64decode ( "aHR0cDovL3AuYnJvc2dpdC5wcm8vc3BpbnovZW11bGF0b3Itcm9tdHh0L1JPTVNUWFQvTkRTTS50eHQ=" )
O0OoOO0oo0 = base64 . b64decode ( "aHR0cDovL3AuYnJvc2dpdC5wcm8vc3BpbnovZW11bGF0b3Itcm9tdHh0L1JPTVNUWFQvTkRTTi1PLnR4dA==" )
oOO = base64 . b64decode ( "aHR0cDovL3AuYnJvc2dpdC5wcm8vc3BpbnovZW11bGF0b3Itcm9tdHh0L1JPTVNUWFQvTkRTUC1RLnR4dA==" )
O0o0OO0000ooo = base64 . b64decode ( "aHR0cDovL3AuYnJvc2dpdC5wcm8vc3BpbnovZW11bGF0b3Itcm9tdHh0L1JPTVNUWFQvTkRTUi50eHQ=" )
iIIII1iIIii = base64 . b64decode ( "aHR0cDovL3AuYnJvc2dpdC5wcm8vc3BpbnovZW11bGF0b3Itcm9tdHh0L1JPTVNUWFQvTkRTUy50eHQ=" )
oOOO00o000o = base64 . b64decode ( "aHR0cDovL3AuYnJvc2dpdC5wcm8vc3BpbnovZW11bGF0b3Itcm9tdHh0L1JPTVNUWFQvTkRTVC1VLnR4dA==" )
iIi11i1 = base64 . b64decode ( "aHR0cDovL3AuYnJvc2dpdC5wcm8vc3BpbnovZW11bGF0b3Itcm9tdHh0L1JPTVNUWFQvTkRTVi1aLnR4dA==" )
oO00oo0o00o0o = base64 . b64decode ( "aHR0cDovL3AuYnJvc2dpdC5wcm8vc3BpbnovZW11bGF0b3Itcm9tdHh0L1JPTVNUWFQvUFNBLnR4dA==" )
IiIIIIIi = base64 . b64decode ( "aHR0cDovL3AuYnJvc2dpdC5wcm8vc3BpbnovZW11bGF0b3Itcm9tdHh0L1JPTVNUWFQvUFNCLnR4dA==" )
IiIi1iIIi1 = base64 . b64decode ( "aHR0cDovL3AuYnJvc2dpdC5wcm8vc3BpbnovZW11bGF0b3Itcm9tdHh0L1JPTVNUWFQvUFNDLUQudHh0" )
O0OoO0ooOO0o = base64 . b64decode ( "aHR0cDovL3AuYnJvc2dpdC5wcm8vc3BpbnovZW11bGF0b3Itcm9tdHh0L1JPTVNUWFQvUFNFLUYudHh0" )
OoOo0oOooOoOO = base64 . b64decode ( "aHR0cDovL3AuYnJvc2dpdC5wcm8vc3BpbnovZW11bGF0b3Itcm9tdHh0L1JPTVNUWFQvUFNHLUoudHh0" )
oo00ooOoO00 = base64 . b64decode ( "aHR0cDovL3AuYnJvc2dpdC5wcm8vc3BpbnovZW11bGF0b3Itcm9tdHh0L1JPTVNUWFQvUFNLLU4udHh0" )
o00oOoOo0 = base64 . b64decode ( "aHR0cDovL3AuYnJvc2dpdC5wcm8vc3BpbnovZW11bGF0b3Itcm9tdHh0L1JPTVNUWFQvUFNPLVIudHh0" )
o0O0O0ooo0oOO = base64 . b64decode ( "aHR0cDovL3AuYnJvc2dpdC5wcm8vc3BpbnovZW11bGF0b3Itcm9tdHh0L1JPTVNUWFQvUFNTLVQudHh0" )
oo000 = base64 . b64decode ( "aHR0cDovL3AuYnJvc2dpdC5wcm8vc3BpbnovZW11bGF0b3Itcm9tdHh0L1JPTVNUWFQvUFNVLVoudHh0" )
if 32 - 32: i1IIi . IiiIII111ii
if 59 - 59: OoooooooOO
if 47 - 47: OOoooooO - ooOo / II111iiii
if 12 - 12: iii11iiII
if 83 - 83: iiIIi1IiIi11 . O0 / Ooo0O / iii11iiII - II111iiii
if 100 - 100: I1111
if 46 - 46: o0o0Oo0oooo0 / iIii1I11I1II1 % iiIIi1IiIi11 . iIii1I11I1II1 * iiIIi1IiIi11
if 38 - 38: oO0 - iiIIi1IiIi11 / O0 . OO00O0O0O00Oo
def i1iiIiI1Ii1i ( ) :
 if OOoO0 == 'Yes' :
  if wiz . workingURL ( OO0Oooo0oOO0O ) == True :
   i1iIi = wiz . checkWizard ( 'version' )
   if i1iIi > O0oo0OO0 : iiiii1II ( '%s [v%s] [COLOR red][B][UPDATE v%s][/B][/COLOR]' % ( o0OOO , O0oo0OO0 , i1iIi ) , 'wizardupdate' , themeit = oooOo0OOOoo0 )
   else : iiiii1II ( '%s [v%s]' % ( o0OOO , O0oo0OO0 ) , '' , themeit = oooOo0OOOoo0 )
  else : iiiii1II ( '%s [v%s]' % ( o0OOO , O0oo0OO0 ) , '' , themeit = oooOo0OOOoo0 )
 else : iiiii1II ( '%s [v%s]' % ( o0OOO , O0oo0OO0 ) , '' , themeit = oooOo0OOOoo0 )
 if len ( O000oo0O ) > 0 :
  O0OOO0OOooo00 = wiz . checkBuild ( O000oo0O , 'version' )
  I111iIi1 = '%s (v%s)' % ( O000oo0O , oo0OooOOo0 )
  if O0OOO0OOooo00 > oo0OooOOo0 : I111iIi1 = '%s [COLOR red][B][UPDATE v%s][/B][/COLOR]' % ( I111iIi1 , O0OOO0OOooo00 )
  oo00O00oO000o ( I111iIi1 , 'viewbuild' , O000oo0O , themeit = OO0O000 )
  OOo00OoO = wiz . themeCount ( O000oo0O )
  if not OOo00OoO == False :
   iiiii1II ( 'None' if o0O == "" else o0O , 'theme' , O000oo0O , themeit = iiIiI1i1 )
 else : oo00O00oO000o ( 'None' , 'builds' , themeit = OO0O000 )
 if O0O0ooOOO == 'No' : iiiii1II ( wiz . sep ( ) , '' , themeit = OOoO )
 oo00O00oO000o ( 'Builds' , 'builds' , icon = oO0O00oOOoooO , themeit = OOOiiiiI )
 oo00O00oO000o ( 'Maintenance' , 'maint' , icon = IiIi11iI , themeit = OOOiiiiI )
 oo00O00oO000o ( 'Android Zone' , 'apk1' , icon = Oo0O00O000 , themeit = OOOiiiiI )
 iiiii1II ( 'Speed Test' , 'speed' , icon = ooo , themeit = OOOiiiiI )
 if not OO == 'http://' : oo00O00oO000o ( 'Addon Installer' , 'addons' , icon = i11I1IiII1i1i , themeit = OOOiiiiI )
 if not oO0O0OO0O == 'http://' and not O0oO0 == '' : oo00O00oO000o ( O0oO0 , 'youtube' , icon = oo , themeit = OOOiiiiI )
 oo00O00oO000o ( 'Save Data' , 'savedata' , icon = I1111i , themeit = OOOiiiiI )
 if o00O0 == 'No' : iiiii1II ( 'Contact' , 'contact' , icon = Iii1I1111ii , themeit = OOOiiiiI )
 if O0O0ooOOO == 'No' : iiiii1II ( wiz . sep ( ) , '' , themeit = OOoO )
 iiiii1II ( 'Settings' , 'settings' , icon = ooOoO00 , themeit = OOOiiiiI )
 if iii == 'true' : oo00O00oO000o ( 'Developer Menu' , 'developer' , icon = ooOoO00 , themeit = OOOiiiiI )
 iIi1 ( 'files' , 'viewType' )
 if 21 - 21: i11IiIiiIIIII
def OoO00 ( ) :
 OO0Ooooo000Oo ( )
 O0oOoo0o000O0 = wiz . workingURL ( I1I1i1I )
 if not O0oOoo0o000O0 == True :
  iiiii1II ( '%s Version: %s' % ( ii1iII1II , o0OIiII ) , '' , icon = oO0O00oOOoooO , themeit = OOoO )
  oo00O00oO000o ( 'Save Data Menu' , 'savedata' , icon = I1111i , themeit = OOoO )
  if O0O0ooOOO == 'No' : iiiii1II ( wiz . sep ( ) , '' , themeit = OOoO )
  iiiii1II ( 'Url for txt file not valid' , '' , icon = oO0O00oOOoooO , themeit = OOoO )
  iiiii1II ( '%s' % O0oOoo0o000O0 , '' , icon = oO0O00oOOoooO , themeit = OOoO )
 else :
  o00oO0o0o , oo0O0Ooooooo , I1IIIiI1I1ii1 , iiiI1I1iIIIi1 , Iii , I1iiiiI1iI , iIiiiii1i = wiz . buildCount ( )
  iiIi1IIiI = False ; i1oO0OO0 = [ ]
  if oOooOOOoOo == 'true' :
   if not i1Iii1i1I == '' and not OOoO00 == '' : iiIi1IIiI = True ; i1oO0OO0 . append ( '1' )
   if not IiI111111IIII == '' and not i1Iiii111iI1iIi1 == '' : iiIi1IIiI = True ; i1oO0OO0 . append ( '2' )
   if not OOO == '' and not oo0OOo0 == '' : iiIi1IIiI = True ; i1oO0OO0 . append ( '3' )
  o0O0Oo00 = wiz . openURL ( I1I1i1I ) . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' ) . replace ( 'gui=""' , 'gui="http://"' ) . replace ( 'theme=""' , 'theme="http://"' ) . replace ( 'adult=""' , 'adult="no"' )
  O0Oo0o000oO = re . compile ( 'name="(.+?)".+?ersion="(.+?)".+?rl="(.+?)".+?ui="(.+?)".+?odi="(.+?)".+?heme="(.+?)".+?con="(.+?)".+?anart="(.+?)".+?dult="(.+?)".+?escription="(.+?)".+?ounter="(.+?)"' ) . findall ( o0O0Oo00 )
  if o00oO0o0o == 1 and iiIi1IIiI == False :
   for oO0o00oOOooO0 , O0OOO0OOooo00 , OOOoO000 , oOOOO , Ii , Ii1ii111i1 , i1i1i1I , oOoo000 , OooOo00o , IiI11i1IIiiI , oOOo000oOoO0 in O0Oo0o000oO :
    if not O0Oo000ooO00 == 'true' and OooOo00o . lower ( ) == 'yes' : continue
    if not iii == 'true' and wiz . strTest ( oO0o00oOOooO0 ) : continue
    OoOo00o0OO ( O0Oo0o000oO [ 0 ] [ 0 ] )
    return
  iiiii1II ( '%s Version: %s' % ( ii1iII1II , o0OIiII ) , '' , icon = oO0O00oOOoooO , themeit = OOoO )
  oo00O00oO000o ( 'Save Data Menu' , 'savedata' , icon = I1111i , themeit = OOoO )
  if O0O0ooOOO == 'No' : iiiii1II ( wiz . sep ( ) , '' , themeit = OOoO )
  if iiIi1IIiI == True :
   for ii1IIIIiI11 in i1oO0OO0 :
    oO0o00oOOooO0 = eval ( 'THIRD%sNAME' % ii1IIIIiI11 )
    oo00O00oO000o ( "[B]%s[/B]" % oO0o00oOOooO0 , 'viewthirdparty' , ii1IIIIiI11 , icon = oO0O00oOOoooO , themeit = OOoO )
  if len ( O0Oo0o000oO ) >= 1 :
   if oo00O00oO == 'true' :
    for oO0o00oOOooO0 , O0OOO0OOooo00 , OOOoO000 , oOOOO , Ii , Ii1ii111i1 , i1i1i1I , oOoo000 , OooOo00o , IiI11i1IIiiI , oOOo000oOoO0 in O0Oo0o000oO :
     if not O0Oo000ooO00 == 'true' and OooOo00o . lower ( ) == 'yes' : continue
     if not iii == 'true' and wiz . strTest ( oO0o00oOOooO0 ) : continue
     iI1IIIii = I1i11ii11 ( 'install' , '' , oO0o00oOOooO0 )
     OO00O0oOO = " | [COLOR powderblue] Downloads:[/COLOR][COLOR white] Total:[/COLOR] [COLOR yellow]" + str ( wiz . count_total ( oOOo000oOoO0 ) ) + "[/COLOR]"
     oo00O00oO000o ( '[%s] %s (v%s) %s' % ( float ( Ii ) , oO0o00oOOooO0 , O0OOO0OOooo00 , OO00O0oOO ) , 'viewbuild' , oO0o00oOOooO0 , description = IiI11i1IIiiI , fanart = oOoo000 , icon = i1i1i1I , menu = iI1IIIii , themeit = oooOo0OOOoo0 )
   else :
    if Iii > 0 :
     Ii1iI111 = '+' if OOOO0OOoO0O0 == 'false' else '-'
     iiiii1II ( '[B]%s Leia Builds(%s)[/B]' % ( Ii1iI111 , Iii ) , 'togglesetting' , 'show17' , themeit = OOoO )
     if OOOO0OOoO0O0 == 'true' :
      for oO0o00oOOooO0 , O0OOO0OOooo00 , OOOoO000 , oOOOO , Ii , Ii1ii111i1 , i1i1i1I , oOoo000 , OooOo00o , IiI11i1IIiiI , oOOo000oOoO0 in O0Oo0o000oO :
       if not O0Oo000ooO00 == 'true' and OooOo00o . lower ( ) == 'yes' : continue
       if not iii == 'true' and wiz . strTest ( oO0o00oOOooO0 ) : continue
       O0oooo00o0Oo = int ( float ( Ii ) )
       if O0oooo00o0Oo == 18 :
        iI1IIIii = I1i11ii11 ( 'install' , '' , oO0o00oOOooO0 )
        OO00O0oOO = " | [COLOR powderblue] Downloads:[/COLOR][COLOR white] Total:[/COLOR] [COLOR yellow]" + str ( wiz . count_total ( oOOo000oOoO0 ) ) + "[/COLOR]"
        oo00O00oO000o ( '[%s] %s (v%s) %s' % ( float ( Ii ) , oO0o00oOOooO0 , O0OOO0OOooo00 , OO00O0oOO ) , 'viewbuild' , oO0o00oOOooO0 , description = IiI11i1IIiiI , fanart = oOoo000 , icon = i1i1i1I , menu = iI1IIIii , themeit = oooOo0OOOoo0 )
    if iiiI1I1iIIIi1 > 0 :
     Ii1iI111 = '+' if o00OO00OoO == 'false' else '-'
     iiiii1II ( '[B]%s Krypton Builds(%s)[/B]' % ( Ii1iI111 , iiiI1I1iIIIi1 ) , 'togglesetting' , 'show17' , themeit = OOoO )
     if o00OO00OoO == 'true' :
      for oO0o00oOOooO0 , O0OOO0OOooo00 , OOOoO000 , oOOOO , Ii , Ii1ii111i1 , i1i1i1I , oOoo000 , OooOo00o , IiI11i1IIiiI , oOOo000oOoO0 in O0Oo0o000oO :
       if not O0Oo000ooO00 == 'true' and OooOo00o . lower ( ) == 'yes' : continue
       if not iii == 'true' and wiz . strTest ( oO0o00oOOooO0 ) : continue
       O0oooo00o0Oo = int ( float ( Ii ) )
       if O0oooo00o0Oo == 17 :
        iI1IIIii = I1i11ii11 ( 'install' , '' , oO0o00oOOooO0 )
        OO00O0oOO = " | [COLOR powderblue] Downloads:[/COLOR][COLOR white] Total:[/COLOR] [COLOR yellow]" + str ( wiz . count_total ( oOOo000oOoO0 ) ) + "[/COLOR]"
        oo00O00oO000o ( '[%s] %s (v%s) %s' % ( float ( Ii ) , oO0o00oOOooO0 , O0OOO0OOooo00 , OO00O0oOO ) , 'viewbuild' , oO0o00oOOooO0 , description = IiI11i1IIiiI , fanart = oOoo000 , icon = i1i1i1I , menu = iI1IIIii , themeit = oooOo0OOOoo0 )
    if I1IIIiI1I1ii1 > 0 :
     Ii1iI111 = '+' if oOOoo0Oo == 'false' else '-'
     iiiii1II ( '[B]%s Jarvis Builds(%s)[/B]' % ( Ii1iI111 , I1IIIiI1I1ii1 ) , 'togglesetting' , 'show16' , themeit = OOoO )
     if oOOoo0Oo == 'true' :
      for oO0o00oOOooO0 , O0OOO0OOooo00 , OOOoO000 , oOOOO , Ii , Ii1ii111i1 , i1i1i1I , oOoo000 , OooOo00o , IiI11i1IIiiI , oOOo000oOoO0 in O0Oo0o000oO :
       if not O0Oo000ooO00 == 'true' and OooOo00o . lower ( ) == 'yes' : continue
       if not iii == 'true' and wiz . strTest ( oO0o00oOOooO0 ) : continue
       O0oooo00o0Oo = int ( float ( Ii ) )
       if O0oooo00o0Oo == 16 :
        iI1IIIii = I1i11ii11 ( 'install' , '' , oO0o00oOOooO0 )
        OO00O0oOO = " | [COLOR powderblue] Downloads:[/COLOR][COLOR white] Total:[/COLOR] [COLOR yellow]" + str ( wiz . count_total ( oOOo000oOoO0 ) ) + "[/COLOR]"
        oo00O00oO000o ( '[%s] %s (v%s) %s' % ( float ( Ii ) , oO0o00oOOooO0 , O0OOO0OOooo00 , OO00O0oOO ) , 'viewbuild' , oO0o00oOOooO0 , description = IiI11i1IIiiI , fanart = oOoo000 , icon = i1i1i1I , menu = iI1IIIii , themeit = oooOo0OOOoo0 )
    if oo0O0Ooooooo > 0 :
     Ii1iI111 = '+' if oO0Oo == 'false' else '-'
     iiiii1II ( '[B]%s Isengard and Below Builds(%s)[/B]' % ( Ii1iI111 , oo0O0Ooooooo ) , 'togglesetting' , 'show15' , themeit = OOoO )
     if oO0Oo == 'true' :
      for oO0o00oOOooO0 , O0OOO0OOooo00 , OOOoO000 , oOOOO , Ii , Ii1ii111i1 , i1i1i1I , oOoo000 , OooOo00o , IiI11i1IIiiI , oOOo000oOoO0 in O0Oo0o000oO :
       if not O0Oo000ooO00 == 'true' and OooOo00o . lower ( ) == 'yes' : continue
       if not iii == 'true' and wiz . strTest ( oO0o00oOOooO0 ) : continue
       O0oooo00o0Oo = int ( float ( Ii ) )
       if O0oooo00o0Oo <= 15 :
        iI1IIIii = I1i11ii11 ( 'install' , '' , oO0o00oOOooO0 )
        OO00O0oOO = " | [COLOR powderblue] Downloads:[/COLOR][COLOR white] Total:[/COLOR] [COLOR yellow]" + str ( wiz . count_total ( oOOo000oOoO0 ) ) + "[/COLOR]"
        oo00O00oO000o ( '[%s] %s (v%s) %s' % ( float ( Ii ) , oO0o00oOOooO0 , O0OOO0OOooo00 , OO00O0oOO ) , 'viewbuild' , oO0o00oOOooO0 , description = IiI11i1IIiiI , fanart = oOoo000 , icon = i1i1i1I , menu = iI1IIIii , themeit = oooOo0OOOoo0 )
  elif iIiiiii1i > 0 :
   if I1iiiiI1iI > 0 :
    iiiii1II ( 'There is currently only Adult builds' , '' , icon = oO0O00oOOoooO , themeit = OOoO )
    iiiii1II ( 'Enable Show Adults in Addon Settings > Misc' , '' , icon = oO0O00oOOoooO , themeit = OOoO )
   else :
    iiiii1II ( 'Currently No Builds Offered from %s' % o0OOO , '' , icon = oO0O00oOOoooO , themeit = OOoO )
  else : iiiii1II ( 'Text file for builds not formated correctly.' , '' , icon = oO0O00oOOoooO , themeit = OOoO )
 iIi1 ( 'files' , 'viewType' )
 if 36 - 36: IiiIII111ii / II111iiii / i1Ii / i1Ii + oO0
def OO0Ooooo000Oo ( ) :
 if 95 - 95: i1Ii
 if 51 - 51: II111iiii + i1Ii . i1IIi . oO0 + o0o0Oo0oooo0 * ooOo
 import sys
 if 72 - 72: IIIi1i1I + IIIi1i1I / II111iiii . OoooooooOO % IiiIII111ii
 III = 'aHR0cDovL3N0dm1jLm5ldC9waW4='
 IiiIii = 'MGZlYTY4MGY5NmVjY2E0'
 oOo0OoOOo0 = base64 . b64decode ( 'aHR0cDovL29mZnNob3JlcGx1Z2lucy5jb20vcG9ydGFsL2FwaS5waHA/cGluPSVzJmtleT0=' ) + base64 . b64decode ( IiiIii )
 iII11I1Ii1 = 'W0NPTE9SIGJsdWVdSW4gb3JkZXIgdG8gY29udGludWUgcGxlYXNlWy9DT0xPUl0gW0NPTE9SIHdoaXRlXVtCXVZFUklGWVsvQl1bL0NPTE9SXSBbQ09MT1IgYmx1ZV15b3VyIGRldmljZSBieSBnZXR0aW5nIGEgcGluIGZyb20gb3VyIHdlYnNpdGUgYW5kIGVudGVyaW5nIHRoZSBwaW4gb24gdGhlIG5leHQgcHJvbXQuWy9DT0xPUl1bQ09MT1Igd2hpdGVdW0Jdc3R2bWMubmV0L3BpblsvQl1bL0NPTE9SXQ=='
 if 92 - 92: i11IiIiiIIIII / i11IiIiiIIIII . oO0
 ii1iIi1II = base64 . b64decode ( iII11I1Ii1 )
 IIIIi1I = xbmcaddon . Addon ( ) . getAddonInfo
 IiIi1i1ii = xbmcaddon . Addon ( ) . getSetting ( 'pin' )
 IiiIII111iI = lambda iiIi : base64 . b64decode ( str ( iiIi ) )
 oOIi111 = lambda iiIi : requests . get ( oOo0OoOOo0 % ( iiIi ) ) . text . strip ( )
 oO0i1iI = lambda iiIi : xbmcaddon . Addon ( ) . setSetting ( base64 . b64decode ( 'cGlu' ) , iiIi )
 ii = lambda iiIi : xbmcgui . Dialog ( ) . yesno ( IIIIi1I ( 'name' ) , iiIi , yeslabel = "Get A Pin" , nolabel = 'Cancel' )
 oo0o0OoOOO = bool ( oOIi111 ( IiIi1i1ii ) == base64 . b64decode ( 'UGluIFZlcmlmaWVk' ) )
 if 88 - 88: iiIIi1IiIi11
 if oo0o0OoOOO : return
 else :
  if 19 - 19: II111iiii * i1Ii + IiiIII111ii
  if ii ( ii1iIi1II ) :
   O0ooO00oO ( III )
   i11i1iIiii = OOO00OO0oOo ( 'Type Your Pin Here' )
   oO0i1iI ( i11i1iIiii )
   OO0Ooooo000Oo ( )
  else : sys . exit ( )
  if 35 - 35: iiIIi1IiIi11 + OOoooooO - IIIi1i1I . iiIIi1IiIi11 . i1Ii
  if 87 - 87: o0o0Oo0oooo0
  if 25 - 25: i1IIi . I1111 - o0o0Oo0oooo0 / I1111 % I1111 * iIii1I11I1II1
def IIIiIiIi11Ii ( st ) :
 import re
 st = re . sub ( '\[.+\]' , '' , st )
 import string
 iIII1i1i = 0
 for IiI1iii11iIi1 in st :
  if IiI1iii11iIi1 in 'lij|\' ' : iIII1i1i += 37
  elif IiI1iii11iIi1 in '![]fI.,:;/\\t' : iIII1i1i += 50
  elif IiI1iii11iIi1 in '`-(){}r"' : iIII1i1i += 60
  elif IiI1iii11iIi1 in '*^zcsJkvxy' : iIII1i1i += 85
  elif IiI1iii11iIi1 in 'aebdhnopqug#$L+<>=?_~FZT' + string . digits : iIII1i1i += 95
  elif IiI1iii11iIi1 in 'BSPEAKVXY&UwNRCHD' : iIII1i1i += 112
  elif IiI1iii11iIi1 in 'QGOMm%W@' : iIII1i1i += 135
  else : iIII1i1i += 50
 return int ( iIII1i1i * 6.5 / 100 )
 if 40 - 40: i11IiIiiIIIII % I1111 . OO00O0O0O00Oo
def OOO00OO0oOo ( Heading = xbmcaddon . Addon ( ) . getAddonInfo ( 'name' ) ) :
 OOO0oOOo00O = xbmc . Keyboard ( '' , Heading )
 OOO0oOOo00O . doModal ( )
 if ( OOO0oOOo00O . isConfirmed ( ) ) :
  return OOO0oOOo00O . getText ( )
  if 51 - 51: oO0 / iIii1I11I1II1 % IIIi1i1I + I1I1i1 * OOoooooO + OO00O0O0O00Oo
def O0ooO00oO ( url ) :
 if 77 - 77: OOoooooO * o0o0Oo0oooo0
 import webbrowser
 if 14 - 14: i11IiIiiIIIII % i11IiIiiIIIII / i1Ii
 OoOoO00O0 = webbrowser . open
 OoOOO = xbmc . executebuiltin
 o0o00Ooo0o = lambda iiIi : xbmc . getCondVisibility ( str ( iiIi ) )
 oo00o = lambda iiIi : OoOOO ( 'StartAndroidActivity(,android.intent.action.VIEW,,%s)' % ( iiIi ) )
 if 76 - 76: iiIIi1IiIi11
 I11Ii11iI1 = 'System.Platform.Android'
 if 39 - 39: ooOo * i11iIiiIii - IIIi1i1I / i1Ii % OO00O0O0O00Oo % i11IiIiiIIIII
 if o0o00Ooo0o ( I11Ii11iI1 ) : oo00o ( base64 . b64decode ( url ) )
 else : OoOoO00O0 ( base64 . b64decode ( url ) )
 if 65 - 65: IIIi1i1I - OOoooooO % OoooooooOO / OoooooooOO % OoooooooOO
 if 52 - 52: oO0 + oO0 . II111iiii
def OoOo00o0OO ( name , counter ) :
 O0oOoo0o000O0 = wiz . workingURL ( I1I1i1I )
 if not O0oOoo0o000O0 == True :
  iiiii1II ( 'Url for txt file not valid' , '' , themeit = OOoO )
  iiiii1II ( '%s' % O0oOoo0o000O0 , '' , themeit = OOoO )
  return
 if wiz . checkBuild ( name , 'version' ) == False :
  iiiii1II ( 'Error reading the txt file.' , '' , themeit = OOoO )
  iiiii1II ( '%s was not found in the builds list.' % name , '' , themeit = OOoO )
  return
 o0O0Oo00 = wiz . openURL ( I1I1i1I ) . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' ) . replace ( 'gui=""' , 'gui="http://"' ) . replace ( 'theme=""' , 'theme="http://"' )
 O0Oo0o000oO = re . compile ( 'name="%s".+?ersion="(.+?)".+?rl="(.+?)".+?ui="(.+?)".+?odi="(.+?)".+?heme="(.+?)".+?con="(.+?)".+?anart="(.+?)".+?review="(.+?)".+?dult="(.+?)".+?escription="(.+?)".+?ounter="(.+?)"' % name ) . findall ( o0O0Oo00 )
 for O0OOO0OOooo00 , OOOoO000 , oOOOO , Ii , OOo00OoO , i1i1i1I , oOoo000 , IiiIIIII1iii , OooOo00o , IiI11i1IIiiI , counter in O0Oo0o000oO :
  i1i1i1I = i1i1i1I if wiz . workingURL ( i1i1i1I ) else iiiiiIIii
  oOoo000 = oOoo000 if wiz . workingURL ( oOoo000 ) else OOO00
  I111iIi1 = '%s (v%s)' % ( name , O0OOO0OOooo00 )
  if O000oo0O == name and O0OOO0OOooo00 > oo0OooOOo0 :
   I111iIi1 = '%s [COLOR red][CURRENT v%s][/COLOR]' % ( I111iIi1 , oo0OooOOo0 )
  iiiii1II ( I111iIi1 , '' , description = IiI11i1IIiiI , fanart = oOoo000 , icon = i1i1i1I , themeit = OO0O000 )
  if O0O0ooOOO == 'No' : iiiii1II ( wiz . sep ( ) , '' , themeit = OOoO )
  oo00O00oO000o ( 'Save Data Menu' , 'savedata' , icon = I1111i , themeit = OOoO )
  iiiii1II ( 'Build Information' , 'buildinfo' , name , description = IiI11i1IIiiI , fanart = oOoo000 , icon = i1i1i1I , themeit = OOoO )
  if not IiiIIIII1iii == "http://" : iiiii1II ( 'View Video Preview' , 'buildpreview' , name , description = IiI11i1IIiiI , fanart = oOoo000 , icon = i1i1i1I , themeit = OOoO )
  IIiiii = int ( float ( o0OIiII ) ) ; iI111i1I1II = int ( float ( Ii ) )
  if not IIiiii == iI111i1I1II :
   if IIiiii == 16 and iI111i1I1II <= 15 : O00OO = False
   else : O00OO = True
  else : O00OO = False
  if O00OO == True :
   iiiii1II ( '[I]Build designed for kodi version %s(installed: %s)[/I]' % ( str ( Ii ) , str ( o0OIiII ) ) , '' , fanart = oOoo000 , icon = i1i1i1I , themeit = OOoO )
  iiiii1II ( wiz . sep ( 'INSTALL' ) , '' , fanart = oOoo000 , icon = i1i1i1I , themeit = OOoO )
  iiiii1II ( 'Fresh Install' , 'install' , name , 'fresh' , description = IiI11i1IIiiI , fanart = oOoo000 , icon = i1i1i1I , themeit = OOOiiiiI )
  iiiii1II ( 'Standard Install' , 'install' , name , 'normal' , description = IiI11i1IIiiI , fanart = oOoo000 , icon = i1i1i1I , themeit = OOOiiiiI )
  if not oOOOO == 'http://' : iiiii1II ( 'Apply guiFix' , 'install' , name , 'gui' , description = IiI11i1IIiiI , fanart = oOoo000 , icon = i1i1i1I , themeit = OOOiiiiI )
  if not OOo00OoO == 'http://' :
   if wiz . workingURL ( OOo00OoO ) == True :
    iiiii1II ( wiz . sep ( 'THEMES' ) , '' , fanart = oOoo000 , icon = i1i1i1I , themeit = OOoO )
    o0O0Oo00 = wiz . openURL ( OOo00OoO ) . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
    O0Oo0o000oO = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?con="(.+?)".+?anart="(.+?)".+?dult="(.+?)".+?escription="(.+?)".+?ounter"(.+?)"' ) . findall ( o0O0Oo00 )
    for II1Ii1iI1i1 , o0OoO000O , OOo , iIIiiIIIi1I , OO0o0o0oo0O , IiI11i1IIiiI , counter in O0Oo0o000oO :
     if not O0Oo000ooO00 == 'true' and OO0o0o0oo0O . lower ( ) == 'yes' : continue
     OOo = OOo if OOo == 'http://' else i1i1i1I
     iIIiiIIIi1I = iIIiiIIIi1I if iIIiiIIIi1I == 'http://' else oOoo000
     iiiii1II ( II1Ii1iI1i1 if not II1Ii1iI1i1 == o0O else "[B]%s (Installed)[/B]" % II1Ii1iI1i1 , 'theme' , name , II1Ii1iI1i1 , description = IiI11i1IIiiI , fanart = iIIiiIIIi1I , icon = OOo , themeit = OOoO )
 iIi1 ( 'files' , 'viewType' )
 if 40 - 40: I1I1i1 + Ooo0O . I1I1i1 % OOoooooO
def I11I1IIiiII1 ( number ) :
 oO0o00oOOooO0 = eval ( 'THIRD%sNAME' % number )
 OOOoO000 = eval ( 'THIRD%sURL' % number )
 IIIIIii1ii11 = wiz . workingURL ( OOOoO000 )
 if not IIIIIii1ii11 == True :
  iiiii1II ( 'Url for txt file not valid' , '' , icon = oO0O00oOOoooO , themeit = OOoO )
  iiiii1II ( '%s' % WORKINGURL , '' , icon = oO0O00oOOoooO , themeit = OOoO )
 else :
  type , OOOooo0OooOoO = wiz . thirdParty ( OOOoO000 )
  iiiii1II ( "[B]%s[/B]" % oO0o00oOOooO0 , '' , themeit = OOoO )
  if O0O0ooOOO == 'No' : iiiii1II ( wiz . sep ( ) , '' , themeit = OOoO )
  if type :
   for oO0o00oOOooO0 , O0OOO0OOooo00 , OOOoO000 , Ii , i1i1i1I , oOoo000 , OooOo00o , IiI11i1IIiiI in OOOooo0OooOoO :
    if not O0Oo000ooO00 == 'true' and OooOo00o . lower ( ) == 'yes' : continue
    iiiii1II ( "[%s] %s v%s" % ( Ii , oO0o00oOOooO0 , O0OOO0OOooo00 ) , 'installthird' , oO0o00oOOooO0 , OOOoO000 , icon = i1i1i1I , fanart = oOoo000 , description = IiI11i1IIiiI , themeit = oooOo0OOOoo0 )
  else :
   for oO0o00oOOooO0 , OOOoO000 , i1i1i1I , oOoo000 , IiI11i1IIiiI in OOOooo0OooOoO :
    iiiii1II ( oO0o00oOOooO0 , 'installthird' , oO0o00oOOooO0 , OOOoO000 , icon = i1i1i1I , fanart = oOoo000 , description = IiI11i1IIiiI , themeit = oooOo0OOOoo0 )
    if 91 - 91: IIIi1i1I + ooOo
def OoOooo ( number ) :
 oO0o00oOOooO0 = eval ( 'THIRD%sNAME' % number )
 OOOoO000 = eval ( 'THIRD%sURL' % number )
 oo00OOoOoO00 = wiz . getKeyboard ( oO0o00oOOooO0 , 'Enter the Name of the Wizard' )
 I1iii = wiz . getKeyboard ( OOOoO000 , 'Enter the URL of the Wizard Text' )
 if 51 - 51: oO0
 wiz . setS ( 'wizard%sname' % number , oo00OOoOoO00 )
 wiz . setS ( 'wizard%surl' % number , I1iii )
 if 41 - 41: oO0 * OOoooooO - IiiIII111ii + Ooo0O
def IiIIIII11I ( name = "" ) :
 if name == 'kodi' :
  Ii1I11I = 'http://mirrors.kodi.tv/releases/android/arm/'
  iiIii1I = 'http://mirrors.kodi.tv/releases/android/arm/old/'
  i1I11iIiII = wiz . openURL ( Ii1I11I ) . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
  I1iii = wiz . openURL ( iiIii1I ) . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
  iiIi = 0
  OO0OO0OO = re . compile ( '<tr><td><a href="(.+?)".+?>(.+?)</a></td><td>(.+?)</td><td>(.+?)</td></tr>' ) . findall ( i1I11iIiII )
  OoooO0o = re . compile ( '<tr><td><a href="(.+?)".+?>(.+?)</a></td><td>(.+?)</td><td>(.+?)</td></tr>' ) . findall ( I1iii )
  if 24 - 24: o0o0Oo0oooo0 % i1IIi + iiIIi1IiIi11 . i11iIiiIii . oO0
  iiiii1II ( "Official Kodi Apk\'s" , themeit = OOOiiiiI )
  IIi1II = False
  for OOOoO000 , name , iIII1i1i , IiiI11i1I in OO0OO0OO :
   if OOOoO000 in [ '../' , 'old/' ] : continue
   if not OOOoO000 . endswith ( '.apk' ) : continue
   if not OOOoO000 . find ( '_' ) == - 1 and IIi1II == True : continue
   try :
    OOo0iiIii1IIi = name . split ( '-' )
    if not OOOoO000 . find ( '_' ) == - 1 :
     IIi1II = True
     oo00OOoOoO00 , ii1IiIiI1 = OOo0iiIii1IIi [ 2 ] . split ( '_' )
    else :
     oo00OOoOoO00 = OOo0iiIii1IIi [ 2 ]
     ii1IiIiI1 = ''
    OOOoOo00O = "[COLOR %s]%s v%s%s %s[/COLOR] [COLOR %s]%s[/COLOR] [COLOR %s]%s[/COLOR]" % ( oOOo0O00o , OOo0iiIii1IIi [ 0 ] . title ( ) , OOo0iiIii1IIi [ 1 ] , ii1IiIiI1 . upper ( ) , oo00OOoOoO00 , iIiIi11 , iIII1i1i . replace ( ' ' , '' ) , oOOo0O00o , IiiI11i1I )
    O0ooOo0o0Oo = urljoin ( Ii1I11I , OOOoO000 )
    iiiii1II ( OOOoOo00O , 'apkinstall' , "%s v%s%s %s" % ( OOo0iiIii1IIi [ 0 ] . title ( ) , OOo0iiIii1IIi [ 1 ] , ii1IiIiI1 . upper ( ) , oo00OOoOoO00 ) , O0ooOo0o0Oo )
    iiIi += 1
   except :
    wiz . log ( "Error on: %s" % name )
    if 71 - 71: iIii1I11I1II1 - iii11iiII . ooOo % OoooooooOO + iii11iiII
  for OOOoO000 , name , iIII1i1i , IiiI11i1I in OoooO0o :
   if OOOoO000 in [ '../' , 'old/' ] : continue
   if not OOOoO000 . endswith ( '.apk' ) : continue
   if not OOOoO000 . find ( '_' ) == - 1 : continue
   try :
    OOo0iiIii1IIi = name . split ( '-' )
    OOOoOo00O = "[COLOR %s]%s v%s %s[/COLOR] [COLOR %s]%s[/COLOR] [COLOR %s]%s[/COLOR]" % ( oOOo0O00o , OOo0iiIii1IIi [ 0 ] . title ( ) , OOo0iiIii1IIi [ 1 ] , OOo0iiIii1IIi [ 2 ] , iIiIi11 , iIII1i1i . replace ( ' ' , '' ) , oOOo0O00o , IiiI11i1I )
    O0ooOo0o0Oo = urljoin ( iiIii1I , OOOoO000 )
    iiiii1II ( OOOoOo00O , 'apkinstall' , "%s v%s %s" % ( OOo0iiIii1IIi [ 0 ] . title ( ) , OOo0iiIii1IIi [ 1 ] , OOo0iiIii1IIi [ 2 ] ) , O0ooOo0o0Oo )
    iiIi += 1
   except :
    wiz . log ( "Error on: %s" % name )
  if iiIi == 0 : iiiii1II ( "Error Kodi Scraper Is Currently Down." )
 elif name == 'spmc' :
  IIi11I1 = 'https://github.com/koying/SPMC/releases'
  i1I11iIiII = wiz . openURL ( IIi11I1 ) . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
  iiIi = 0
  OO0OO0OO = re . compile ( '<div.+?lass="release-body.+?div class="release-header".+?a href=.+?>(.+?)</a>.+?ul class="release-downloads">(.+?)</ul>.+?/div>' ) . findall ( i1I11iIiII )
  if 49 - 49: II111iiii - ooOo / i11IiIiiIIIII
  iiiii1II ( "Official SPMC Apk\'s" , themeit = OOOiiiiI )
  if 74 - 74: i11IiIiiIIIII - iii11iiII + i1IIi . ooOo + iii11iiII - i11IiIiiIIIII
  for name , IiIiiiiI1 in OO0OO0OO :
   OO00OOoO0o = ''
   OoooO0o = re . compile ( '<li>.+?<a href="(.+?)" rel="nofollow">.+?<small class="text-gray float-right">(.+?)</small>.+?strong>(.+?)</strong>.+?</a>.+?</li>' ) . findall ( IiIiiiiI1 )
   for Iiiiiii1 , oOO0oo , II1iIi1IiIii in OoooO0o :
    if II1iIi1IiIii . find ( 'armeabi' ) == - 1 : continue
    if II1iIi1IiIii . find ( 'launcher' ) > - 1 : continue
    OO00OOoO0o = urljoin ( 'https://github.com' , Iiiiiii1 )
    break
   if OO00OOoO0o == '' : continue
   try :
    name = "SPMC %s" % name
    OOOoOo00O = "[COLOR %s]%s[/COLOR] [COLOR %s]%s[/COLOR]" % ( oOOo0O00o , name , iIiIi11 , oOO0oo . replace ( ' ' , '' ) )
    O0ooOo0o0Oo = OO00OOoO0o
    iiiii1II ( OOOoOo00O , 'apkinstall' , name , O0ooOo0o0Oo )
    iiIi += 1
   except Exception , I111I11I111 :
    wiz . log ( "Error on: %s / %s" % ( name , str ( I111I11I111 ) ) )
  if iiIi == 0 : iiiii1II ( "Error SPMC Scraper Is Currently Down." )
  if 46 - 46: i11iIiiIii - O0 . IIIi1i1I
def Oo0O ( ) :
 oo00O00oO000o ( 'Emulators And Roms' , 'emurom' , icon = i111iIi1i1II1 , themeit = OOOiiiiI )
 oo00O00oO000o ( 'SpinzTV APKS' , 'apkshow' , url = OooOo , icon = Ii1IIiI1i , themeit = OOOiiiiI )
 oo00O00oO000o ( '[COLOR deepskyblue]APK Drawer[/COLOR]' , 'intellaunch' , )
 oo00O00oO000o ( 'Official Kodi Apk\'s' , 'apkscrape' , 'kodi' , icon = Oo0O00O000 , themeit = OOOiiiiI )
 oo00O00oO000o ( 'Official SPMC Apk\'s' , 'apkscrape' , 'spmc' , icon = Oo0O00O000 , themeit = OOOiiiiI )
 Ii11 = II1i111 ( base64 . b64decode ( 'aHR0cHM6Ly93d3cuYXBrZmlsZXMuY29tLw==' ) )
 O0Oo0o000oO = re . compile ( 'href="([^"]*)">Applications(.+?)</a>' ) . findall ( Ii11 )
 OoooO0o = re . compile ( 'href="([^"]*)">Games(.+?)</a>' ) . findall ( Ii11 )
 for OOOoO000 , i1iiiIii11 in O0Oo0o000oO :
  OOoOOO000O0 ( '[COLOR deepskyblue]Android Apps[/COLOR]' + i1iiiIii11 , 'https://www.apkfiles.com' + OOOoO000 , 'apkgame' , i1I1i111Ii )
 for OOOoO000 , i1iiiIii11 in OoooO0o :
  OOoOOO000O0 ( '[COLOR deepskyblue]Android Games[/COLOR]' + i1iiiIii11 , 'https://www.apkfiles.com' + OOOoO000 , 'apkgame' , i111iIi1i1II1 )
 iIi1 ( 'movies' , 'MAIN' )
 oo00O00oO000o ( 'Spinz Apk Picks' , 'apkshow' , url = ii1I , icon = Oo0O00O000 , themeit = OOOiiiiI )
 if O0Oo000ooO00 == 'true' : oo00O00oO000o ( 'XXX Apk' , 'apkshow' , url = i11III1111iIi , icon = Oo0O00O000 , themeit = OOOiiiiI )
 iIi1 ( 'files' , 'viewType' )
 if 92 - 92: oO0 / O0
def oOO0o00O ( url ) :
 o0O0Oo00 = II1i111 ( url ) . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
 O0Oo0o000oO = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?con="(.+?)".+?anart="(.+?)"' ) . findall ( o0O0Oo00 )
 if len ( O0Oo0o000oO ) > 0 :
  for oO0o00oOOooO0 , url , i1i1i1I , oOoo000 in O0Oo0o000oO :
   iiiii1II ( oO0o00oOOooO0 , 'apkinstall' , oO0o00oOOooO0 , url , icon = i1i1i1I , fanart = oOoo000 , themeit = OOOiiiiI )
  else : wiz . log ( "[APK Menu] ERROR: Invalid Format." )
 else : wiz . log ( "[APK Menu] ERROR: URL for emu list not working." )
 if 69 - 69: i1IIi
def ooOoOOOOo ( url ) :
 Ii11 = II1i111 ( url )
 O0Oo0o000oO = re . compile ( '<a href="([^"]*)" >(.+?)</a>' ) . findall ( Ii11 )
 for url , oO0o00oOOooO0 in O0Oo0o000oO :
  if '/cat' in url :
   OOoOOO000O0 ( ( oO0o00oOOooO0 ) . replace ( '&amp;' , ' - ' ) , 'https://www.apkfiles.com' + url , 'select' , O000OO0 + 'APK.png' )
   if 71 - 71: II111iiii * iIii1I11I1II1 / oO0
def iiIIi ( url ) :
 Ii11 = II1i111 ( url )
 i1I11iIiII = url
 if "page=" in str ( url ) :
  i1I11iIiII = url . split ( '?' ) [ 0 ]
 O0Oo0o000oO = re . compile ( '<a href="([^"]*)".+?<img src="([^"]*)" class="file_list_icon".+?alt="([^"]*)"' , re . DOTALL ) . findall ( Ii11 )
 OoooO0o = re . compile ( 'class="[^"]*".+?ref="([^"]*)".+?yle=.+?</a>' ) . findall ( Ii11 )
 for url , ooO00O00oOO , oO0o00oOOooO0 in O0Oo0o000oO :
  if 'apk' in url :
   OOoOOO000O0 ( ( oO0o00oOOooO0 ) . replace ( '&#39;' , '' ) . replace ( '&amp;' , ' - ' ) . replace ( '&#174;:' , ': ' ) . replace ( '&#174;' , ' ' ) , 'https://www.apkfiles.com' + url , 'grab' , 'http:' + ooO00O00oOO )
 if len ( OoooO0o ) > 1 :
  OoooO0o = str ( OoooO0o [ len ( OoooO0o ) - 1 ] )
 OOoOOO000O0 ( 'Next Page' , i1I11iIiII + str ( OoooO0o ) , 'select' , O000OO0 + 'Next.png' )
 if 40 - 40: iiIIi1IiIi11 . IIIi1i1I + ooOo + oO0 + OO00O0O0O00Oo
def i11Ii1I1I11I ( name , url ) :
 Ii11 = II1i111 ( url )
 name = name
 O0Oo0o000oO = re . compile ( 'href="([^"]*)".+?lass="yellow_button".+?itle=' ) . findall ( Ii11 )
 for url in O0Oo0o000oO :
  url = 'https://www.apkfiles.com' + url
  Ii1 ( name , url , 'Brackets' )
  if 34 - 34: iiIIi1IiIi11 - OoooooooOO . ooOo / II111iiii
  if 27 - 27: I1111 / Ooo0O * OOoooooO - I1111
  if 19 - 19: i11IiIiiIIIII
  if 67 - 67: O0 % iIii1I11I1II1 / i1Ii . i11iIiiIii - IiiIII111ii + O0
def i1iiiIi1i ( ) :
 xbmc . executebuiltin ( 'Runscript("special://home/addons/plugin.program.SpinzTV/ookla.py")' )
 if 67 - 67: o0o0Oo0oooo0 / I1I1i1 * I1111 / iii11iiII * oO0 / IIIi1i1I
 if 64 - 64: IIIi1i1I - ooOo / iiIIi1IiIi11 - I1111
 if 37 - 37: i11iIiiIii / iiIIi1IiIi11
 if 85 - 85: i11iIiiIii + OO00O0O0O00Oo * o0o0Oo0oooo0
def iiiII ( ) :
 if 57 - 57: i11IiIiiIIIII . Ooo0O + II111iiii
 if os . path . isfile ( i1i1II ) :
  i111i11I1ii = True
  OOooo = open ( i1i1II )
  oo0 = OOooo . read ( )
  OOooo . close ( )
 else :
  xbmcgui . Dialog ( ) . ok ( "[COLOR orange]SpinzTV[/COLOR]" , "[COLOR cyan][B]][[/B]NT3L[B]][[/B]G3NC[B]][[/B][/COLOR]" , "[COLOR ghostwhite]First Time Launching Will Take a Couple Minutes[/COLOR]" , "[COLOR ghostwhite]Please Be Patient![/COLOR]" )
  i111i11I1ii = False
  if 73 - 73: o0o0Oo0oooo0 . ooOo
  if 32 - 32: o0o0Oo0oooo0 * ooOo % OOoooooO * IiiIII111ii . O0
  if 48 - 48: iiIIi1IiIi11 * iiIIi1IiIi11
  if 13 - 13: IiiIII111ii / i11IiIiiIIIII + o0o0Oo0oooo0 . I1I1i1 % OOoooooO
  if 48 - 48: ooOo / i11iIiiIii - I1I1i1 * IIIi1i1I / OoooooooOO
  if 89 - 89: iIii1I11I1II1 / ooOo - II111iiii / IiiIII111ii . i11iIiiIii . IiiIII111ii
  if 48 - 48: O0 + O0 . OO00O0O0O00Oo - OOoooooO
  if 63 - 63: IIIi1i1I
  if 71 - 71: i1IIi . IiiIII111ii * iiIIi1IiIi11 % OoooooooOO + iii11iiII
  if 36 - 36: i1Ii
  if 49 - 49: iii11iiII / OoooooooOO / ooOo
 o0OooooOoOO = ""
 i1i1IIIIIIIi = oo0o0oOo ( )
 for OO0oOOo0o in i1i1IIIIIIIi :
  if i111i11I1ii == True :
   if OO0oOOo0o not in oo0 :
    if 50 - 50: iiIIi1IiIi11 . oO0 . I1111 * i11IiIiiIIIII + II111iiii % i11iIiiIii
    if 8 - 8: OOoooooO * O0
    OOoOIiIIII = oOOo ( o0OooooOoOO , OO0oOOo0o )
    o0OooooOoOO = OOoOIiIIII
    if 100 - 100: ooOo + ooOo * Ooo0O
  else :
   OOoOIiIIII = oOOo ( o0OooooOoOO , OO0oOOo0o )
   o0OooooOoOO = OOoOIiIIII
   if 77 - 77: IIIi1i1I % i1IIi - IiiIII111ii
 if i111i11I1ii == True :
  OOooo = open ( i1i1II , 'a' )
  if 93 - 93: I1111 * Ooo0O
  if 73 - 73: I1I1i1 - ooOo * i1IIi / i11iIiiIii * iii11iiII % II111iiii
 else :
  OOooo = open ( i1i1II , 'w' )
  if 56 - 56: OoooooooOO * Ooo0O . Ooo0O . oO0
  if 24 - 24: Ooo0O . i11IiIiiIIIII * IiiIII111ii % iiIIi1IiIi11 / iii11iiII
 OOooo . write ( o0OooooOoOO )
 OOooo . close ( )
 if 58 - 58: ooOo - oO0 % O0 . ooOo % I1111 % i1Ii
 if 87 - 87: IIIi1i1I - i11iIiiIii
 OOooo = open ( i1i1II )
 oo0 = OOooo . read ( )
 OOooo . close ( )
 oo0 = oo0 . replace ( '\n' , '' ) . replace ( '\r' , '' )
 O0Oo0o000oO = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)".+?nstallRating="(.+?)"' ) . findall ( oo0 )
 if 78 - 78: i11iIiiIii / iIii1I11I1II1 - I1I1i1
 if 23 - 23: i11IiIiiIIIII
 for oO0o00oOOooO0 , OOOoO000 , iIiiIiiIi , oOoo000 , IiI11i1IIiiI , i1iiIIIi in sorted ( O0Oo0o000oO , key = lambda O0Oo0o000oO : O0Oo0o000oO [ 0 ] ) :
  if OOOoO000 in i1i1IIIIIIIi :
   Oo0o ( '[COLOR ghostwhite]' + str ( oO0o00oOOooO0 ) + '[/COLOR]' , OOOoO000 , 'intelselect' , iIiiIiiIi , oOoo000 , IiI11i1IIiiI , i1iiIIIi )
   if 93 - 93: iii11iiII
def oo0o0oOo ( ) :
 if xbmc . getCondVisibility ( 'system.platform.android' ) :
  try :
   i1i1IIIIIIIi = subprocess . Popen ( [ 'exec ' '/system/bin/pm list packages -3' '' ] , executable = '/system/bin/sh' , shell = True , stdout = subprocess . PIPE , stderr = subprocess . STDOUT ) . communicate ( ) [ 0 ] . rstrip ( '\n' ) . splitlines ( )
  except :
   i1i1IIIIIIIi = [ ]
   if 43 - 43: oO0 / ooOo . OOoooooO
  for OO0oOOo0o in range ( len ( i1i1IIIIIIIi ) ) :
   i1i1IIIIIIIi [ OO0oOOo0o ] = i1i1IIIIIIIi [ OO0oOOo0o ] . partition ( ':' ) [ 2 ]
   if 62 - 62: iIii1I11I1II1 + iiIIi1IiIi11 . Ooo0O / i1Ii % O0 . OO00O0O0O00Oo
 return i1i1IIIIIIIi
 if 93 - 93: i11iIiiIii % iIii1I11I1II1 % i11iIiiIii + I1I1i1 / I1I1i1 / II111iiii
def oOOo ( theList , i ) :
 global theNotList
 I1i = "https://play.google.com/store/apps/details?id=" + i
 o0O0Oo00 = OoIiIiIi1I1 ( I1i )
 if 2 - 2: i1IIi - OOoooooO + ooOo . I1I1i1 * I1I1i1 / o0o0Oo0oooo0
 if o0O0Oo00 != False :
  o0O0Oo00 = o0O0Oo00 . replace ( '\n' , '' ) . replace ( '\r' , '' )
  if 93 - 93: i1IIi
  ooOOOo = r'<div class="id-app-title".tabindex=".">(.+?)</div>'
  O0Oo0o000oO = re . search ( ooOOOo , o0O0Oo00 )
  if O0Oo0o000oO != None : oO0o00oOOooO0 = O0Oo0o000oO . group ( 1 )
  else : oO0o00oOOooO0 = i
  if 98 - 98: IIIi1i1I % i1Ii * i11iIiiIii % oO0
  if 29 - 29: i1Ii
  if 66 - 66: Ooo0O
  if 97 - 97: i1IIi - OoooooooOO / OO00O0O0O00Oo * ooOo
  if 55 - 55: I1I1i1 . iiIIi1IiIi11
  iIiiIiiIi = "androidapp://sources/apps/" + str ( i ) + ".png"
  if 87 - 87: I1I1i1 % iIii1I11I1II1
  if 100 - 100: OO00O0O0O00Oo . ooOo * OO00O0O0O00Oo - ooOo . i11IiIiiIIIII * IiiIII111ii
  if 89 - 89: I1111 + i1Ii * OO00O0O0O00Oo
  if 28 - 28: OoooooooOO . IIIi1i1I % oO0 / i1IIi / iii11iiII
  if 36 - 36: I1I1i1 + i11IiIiiIIIII - i1Ii + iIii1I11I1II1 + OoooooooOO
  if 4 - 4: II111iiii . i11IiIiiIIIII + IiiIII111ii * OO00O0O0O00Oo . OOoooooO
  oOoOo = r'data-expand-to="full-screenshot-[0-9]{1,2}" src="(//\w+?.\w+?.\S+?=h900)"'
  O0Oo0o000oO = re . compile ( oOoOo ) . findall ( o0O0Oo00 )
  if len ( O0Oo0o000oO ) != 0 : oOoo000 = "https:" + O0Oo0o000oO [ len ( O0Oo0o000oO ) - 1 ]
  else : oOoo000 = "None"
  if 74 - 74: IIIi1i1I / oO0 % I1I1i1
  OO0o0OO0 = r'data-video-url="https://www.youtube.com/embed/(\S.+?)\?ps=play.+?"'
  O0Oo0o000oO = re . search ( OO0o0OO0 , o0O0Oo00 )
  if O0Oo0o000oO != None : IiI11i1IIiiI = O0Oo0o000oO . group ( 1 )
  else : IiI11i1IIiiI = "None"
  if 56 - 56: i11iIiiIii - Ooo0O / iiIIi1IiIi11 / o0o0Oo0oooo0
  III1i111i = r'<div class="content" itemprop="numDownloads">\s+?(\d.+?\s-\s\d.+?)\s+?</div>'
  O0Oo0o000oO = re . search ( III1i111i , o0O0Oo00 )
  if O0Oo0o000oO != None : iI1i = 'Installed ' + O0Oo0o000oO . group ( 1 )
  else : iI1i = "Installs: N/A"
  if 46 - 46: OO00O0O0O00Oo % IiiIII111ii
  oOOoO0OO00OOo0 = r'<div class="score" aria-label=" Rated .+? stars out of five stars ">(.+?)</div>'
  O0Oo0o000oO = re . search ( oOOoO0OO00OOo0 , o0O0Oo00 )
  if O0Oo0o000oO != None : Ii1IIii = O0Oo0o000oO . group ( 1 ) + " Stars"
  else : Ii1IIii = "Rating: N/A"
  i1iiIIIi = Ii1IIii + " " + iI1i
  if 21 - 21: o0o0Oo0oooo0 / I1I1i1 * i1Ii . i1IIi
  if 59 - 59: O0 + i1IIi - I1I1i1
  if 62 - 62: i11iIiiIii % iii11iiII . i1Ii . iii11iiII
  OOOoO000 = i
  theList += 'name="' + oO0o00oOOooO0 + '"url="' + OOOoO000 + '"img="' + iIiiIiiIi + '"fanart="' + oOoo000 + '"description="' + IiI11i1IIiiI + '"installRating="' + i1iiIIIi + '"'
  return theList
  if 84 - 84: i11iIiiIii * I1111
  if 18 - 18: iii11iiII - IiiIII111ii - o0o0Oo0oooo0 / OO00O0O0O00Oo - O0
  if 30 - 30: O0 + oO0 + II111iiii
  if 14 - 14: I1I1i1 / iii11iiII - iIii1I11I1II1 - IIIi1i1I % OOoooooO
  if 49 - 49: OOoooooO * IIIi1i1I / I1I1i1 / Ooo0O * iIii1I11I1II1
  if 57 - 57: o0o0Oo0oooo0 - IIIi1i1I / OOoooooO % i11iIiiIii
  if 3 - 3: iiIIi1IiIi11 . OOoooooO % ooOo + oO0
  if 64 - 64: i1IIi
  if 29 - 29: I1I1i1 / i11iIiiIii / ooOo % IIIi1i1I % i11iIiiIii
 else :
  if 18 - 18: iii11iiII + OO00O0O0O00Oo
  return theList
  if 80 - 80: IIIi1i1I + I1I1i1 * IiiIII111ii + I1111
def O0oOo ( name , url , iconimage , fanart , videolink ) :
 OO0oo0O0OOO0 = 0
 if 76 - 76: i11iIiiIii / o0o0Oo0oooo0 + o0o0Oo0oooo0 / i1IIi * ooOo
 if videolink != "None" :
  OO0oo0O0OOO0 += 1
  if 12 - 12: OO00O0O0O00Oo % i11iIiiIii + I1I1i1 + OO00O0O0O00Oo / i11IiIiiIIIII
 if OO0oo0O0OOO0 == 1 : O00 = xbmcgui . Dialog ( ) . select ( '[COLOR deepskyblue]' + name + '[/COLOR]' , [ '[COLOR deepskyblue]Launch[/COLOR]' , '[COLOR ghostwhite]Preview Video[/COLOR]' , '[COLOR tomato]Uninstall[/COLOR]' ] )
 if OO0oo0O0OOO0 == 0 : O00 = xbmcgui . Dialog ( ) . select ( '[COLOR deepskyblue]' + name + '[/COLOR]' , [ '[COLOR deepskyblue]Launch[/COLOR]' , '[COLOR ghostwhite]No Preview Video[/COLOR]' , '[COLOR tomato]Uninstall[/COLOR]' ] )
 if 94 - 94: i11IiIiiIIIII . i11IiIiiIIIII + i11iIiiIii - iii11iiII * oO0
 if 9 - 9: I1I1i1 . ooOo - oO0
 if 32 - 32: OoooooooOO / ooOo / iIii1I11I1II1 + II111iiii . IIIi1i1I . I1I1i1
 if O00 == 1 :
  if videolink != 'None' :
   yt . PlayVideo ( videolink )
 if O00 == 0 :
  ii1ii = xbmcgui . Dialog ( ) . yesno ( "[COLOR orange]SpinzTV[/COLOR]" , "[COLOR cyan][B]][[/B]NT3L[B]][[/B]G3NC[B]][[/B][/COLOR]" , "" , "[COLOR ghostwhite]Would You Like To Launch:[/COLOR] [COLOR cyan]" + name + "[/COLOR]" , "[COLOR red]No Way[/COLOR]" , "[COLOR cyan]Heck Ya![/COLOR]" )
  if ii1ii == 1 :
   xbmc . executebuiltin ( 'StartAndroidActivity(%s)' % url )
 if O00 == 2 :
  IIiI1i = xbmcgui . Dialog ( ) . yesno ( "[COLOR orange]SpinzTV[/COLOR]" , "[COLOR cyan][B]][[/B]NT3L[B]][[/B]G3NC[B]][[/B][/COLOR]" , "" , "[COLOR ghostwhite]Would You Like To Remove:[/COLOR] [COLOR cyan]" + name + "[/COLOR]" , "[COLOR red]No Way[/COLOR]" , "[COLOR cyan]Heck Ya![/COLOR]" )
  if IIiI1i :
   xbmc . executebuiltin ( 'StartAndroidActivity("","android.intent.action.DELETE","","package:' + url + '")' )
   xbmc . sleep ( 2000 )
   try : shutil . rmtree ( "/sdcard/Android/data/" + url , ignore_errors = True , onerror = None )
   except : pass
   try : shutil . rmtree ( "/sdcard/Android/obb/" + url , ignore_errors = True , onerror = None )
   except : pass
   xbmc . executebuiltin ( 'Container.Refresh' )
   if 6 - 6: oO0 / iiIIi1IiIi11 - iii11iiII
def OoIiIiIi1I1 ( url ) :
 try :
  o00O00Oo00O = urllib2 . Request ( url )
  o00O00Oo00O . add_header ( 'User-Agent' , 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3' )
  IIii1I1I1I = urllib2 . urlopen ( o00O00Oo00O )
  o0O0Oo00 = IIii1I1I1I . read ( )
  IIii1I1I1I . close ( )
  return o0O0Oo00
 except :
  return False
  if 79 - 79: i11iIiiIii + Ooo0O + OoooooooOO + IIIi1i1I % iIii1I11I1II1 . iiIIi1IiIi11
  if 80 - 80: IiiIII111ii - I1I1i1
  if 41 - 41: I1I1i1 - Ooo0O * ooOo
def OO0OoOo0OOO ( ) :
 oo00O00oO000o ( 'Emulators' , 'apkshow' , url = I1i111I , icon = i111iIi1i1II1 , themeit = OOOiiiiI )
 oo00O00oO000o ( 'Roms' , 'roms' , icon = i111iIi1i1II1 , themeit = OOOiiiiI )
 if 47 - 47: OoooooooOO % O0 * iiIIi1IiIi11 . IiiIII111ii
 if 38 - 38: O0 - i1Ii % OO00O0O0O00Oo
 if 64 - 64: iIii1I11I1II1
 if 15 - 15: oO0 + iii11iiII / oO0 / OO00O0O0O00Oo
def I1Iii1I ( ) :
 oo00O00oO000o ( 'NES' , 'nes' , icon = i111iIi1i1II1 , themeit = OOOiiiiI )
 oo00O00oO000o ( 'SNES' , 'snes' , icon = i111iIi1i1II1 , themeit = OOOiiiiI )
 oo00O00oO000o ( 'Nintendo 64' , 'n64' , icon = i111iIi1i1II1 , themeit = OOOiiiiI )
 oo00O00oO000o ( 'Nintendo DS' , 'nds' , icon = i111iIi1i1II1 , themeit = OOOiiiiI )
 oo00O00oO000o ( 'Genesis' , 'gen' , icon = i111iIi1i1II1 , themeit = OOOiiiiI )
 oo00O00oO000o ( 'Playstation' , 'ps' , icon = i111iIi1i1II1 , themeit = OOOiiiiI )
 oo00O00oO000o ( 'Atari' , 'atr' , icon = i111iIi1i1II1 , themeit = OOOiiiiI )
 oo00O00oO000o ( 'PC Engine & Turbo Grafx' , 'tbg' , icon = i111iIi1i1II1 , themeit = OOOiiiiI )
 if 13 - 13: I1I1i1 + O0
def O00o0O ( url ) :
 o0O0Oo00 = II1i111 ( url ) . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
 O0Oo0o000oO = re . compile ( '.+?ame="(.+?)".+?rl="(.+?)".+?con="(.+?)".+?anart="(.+?)"description="(.+?)"' ) . findall ( o0O0Oo00 )
 if len ( O0Oo0o000oO ) > 0 :
  for oO0o00oOOooO0 , url , i1i1i1I , oOoo000 , IiI11i1IIiiI in O0Oo0o000oO :
   iIIIiI ( oO0o00oOOooO0 , 'rominstall' , oO0o00oOOooO0 , url , icon = i1i1i1I , fanart = oOoo000 , description = IiI11i1IIiiI , themeit = OOOiiiiI )
  else : wiz . log ( "[ROM Menu] ERROR: Invalid Format." )
 else : wiz . log ( "[ROM Menu] ERROR: URL for apk list not working." )
 if 93 - 93: OOoooooO . iIii1I11I1II1 % i11iIiiIii . o0o0Oo0oooo0 % OOoooooO + O0
 if 65 - 65: IiiIII111ii + I1111 - OoooooooOO
 if 51 - 51: Ooo0O + IIIi1i1I / iiIIi1IiIi11 - i1IIi
 if 51 - 51: Ooo0O - oO0 * i11IiIiiIIIII
def ii1111Ii1i ( ) :
 oo00O00oO000o ( 'SNES Titles A Thru B' , 'rom' , url = Ooo , icon = i111iIi1i1II1 , themeit = OOOiiiiI )
 oo00O00oO000o ( 'SNES Titles C Thru E' , 'rom' , url = Oo0oo0O0o00O , icon = i111iIi1i1II1 , themeit = OOOiiiiI )
 oo00O00oO000o ( 'SNES Titles F Thru H' , 'rom' , url = I1i11 , icon = i111iIi1i1II1 , themeit = OOOiiiiI )
 oo00O00oO000o ( 'SNES Titles I Thru K' , 'rom' , url = IiIi1I1 , icon = i111iIi1i1II1 , themeit = OOOiiiiI )
 oo00O00oO000o ( 'SNES Titles L Thru M' , 'rom' , url = IiIIi1 , icon = i111iIi1i1II1 , themeit = OOOiiiiI )
 oo00O00oO000o ( 'SNES Titles N Thru O' , 'rom' , url = IIIIiii1IIii , icon = i111iIi1i1II1 , themeit = OOOiiiiI )
 oo00O00oO000o ( 'SNES Titles P Thru R' , 'rom' , url = II1i11I , icon = i111iIi1i1II1 , themeit = OOOiiiiI )
 oo00O00oO000o ( 'SNES Titles S' , 'rom' , url = ii1I1IIii11 , icon = i111iIi1i1II1 , themeit = OOOiiiiI )
 oo00O00oO000o ( 'SNES Titles T Thru V' , 'rom' , url = O0o0oO , icon = i111iIi1i1II1 , themeit = OOOiiiiI )
 oo00O00oO000o ( 'SNES Titles W Thru Z' , 'rom' , url = IIIIiIiIi1 , icon = i111iIi1i1II1 , themeit = OOOiiiiI )
 if 48 - 48: O0 * IiiIII111ii - O0 / IiiIII111ii + o0o0Oo0oooo0
 if 52 - 52: I1111 % IiiIII111ii * II111iiii
 if 4 - 4: i11IiIiiIIIII % O0 - OoooooooOO + OOoooooO . IIIi1i1I % II111iiii
 if 9 - 9: II111iiii * II111iiii . i11iIiiIii * iIii1I11I1II1
def II1 ( ) :
 oo00O00oO000o ( 'NES Titles A Thru B' , 'rom' , url = I11iiiiI1i , icon = i111iIi1i1II1 , themeit = OOOiiiiI )
 oo00O00oO000o ( 'NES Titles C' , 'rom' , url = iI1i11 , icon = Oo0O00O000 , themeit = OOOiiiiI )
 oo00O00oO000o ( 'NES Titles D Thru E' , 'rom' , url = OoOOoooOO0O , icon = i111iIi1i1II1 , themeit = OOOiiiiI )
 oo00O00oO000o ( 'NES Titles F Thru G' , 'rom' , url = ooo00Ooo , icon = i111iIi1i1II1 , themeit = OOOiiiiI )
 oo00O00oO000o ( 'NES Titles H Thru K' , 'rom' , url = Oo0o0O00 , icon = i111iIi1i1II1 , themeit = OOOiiiiI )
 oo00O00oO000o ( 'NES Titles L Thru M' , 'rom' , url = ii1I1i11 , icon = i111iIi1i1II1 , themeit = OOOiiiiI )
 oo00O00oO000o ( 'NES Titles N Thru Q' , 'rom' , url = OOo0O0oo0OO0O , icon = i111iIi1i1II1 , themeit = OOOiiiiI )
 oo00O00oO000o ( 'NES Titles R Thru S' , 'rom' , url = OO0 , icon = i111iIi1i1II1 , themeit = OOOiiiiI )
 oo00O00oO000o ( 'NES Titles T Thru V' , 'rom' , url = o0Oooo , icon = i111iIi1i1II1 , themeit = OOOiiiiI )
 oo00O00oO000o ( 'NES Titles W Thru Z' , 'rom' , url = iiI , icon = i111iIi1i1II1 , themeit = OOOiiiiI )
 if 27 - 27: IiiIII111ii + ooOo * iIii1I11I1II1 . OoooooooOO * o0o0Oo0oooo0
 if 100 - 100: I1111 / i1IIi - ooOo % IiiIII111ii - iIii1I11I1II1
 if 17 - 17: i11IiIiiIIIII / I1I1i1 % Ooo0O
 if 71 - 71: i1Ii . OO00O0O0O00Oo . I1111
 if 68 - 68: i11iIiiIii % IIIi1i1I * I1111 * i1Ii * II111iiii + O0
def o00OoO0oO00 ( ) :
 oo00O00oO000o ( 'Genesis Titles A Thru B' , 'rom' , url = oO , icon = i111iIi1i1II1 , themeit = OOOiiiiI )
 oo00O00oO000o ( 'Genesis Titles C Thru D' , 'rom' , url = IIiIi , icon = Oo0O00O000 , themeit = OOOiiiiI )
 oo00O00oO000o ( 'Genesis Titles E Thru G' , 'rom' , url = OOoOooOoOOOoo , icon = i111iIi1i1II1 , themeit = OOOiiiiI )
 oo00O00oO000o ( 'Genesis Titles H Thru L' , 'rom' , url = Iiii1iI1i , icon = i111iIi1i1II1 , themeit = OOOiiiiI )
 oo00O00oO000o ( 'Genesis Titles M Thru O' , 'rom' , url = I1ii1ii11i1I , icon = i111iIi1i1II1 , themeit = OOOiiiiI )
 oo00O00oO000o ( 'Genesis Titles P Thru R' , 'rom' , url = o0OoOO , icon = i111iIi1i1II1 , themeit = OOOiiiiI )
 oo00O00oO000o ( 'Genesis Titles S Thru T' , 'rom' , url = O0O0Oo00 , icon = i111iIi1i1II1 , themeit = OOOiiiiI )
 oo00O00oO000o ( 'Genesis Titles U Thru Z' , 'rom' , url = oOoO00o , icon = i111iIi1i1II1 , themeit = OOOiiiiI )
 if 2 - 2: iIii1I11I1II1
 if 45 - 45: OoooooooOO / i11iIiiIii
 if 10 - 10: iiIIi1IiIi11 - IIIi1i1I * iIii1I11I1II1 % iIii1I11I1II1 * i1Ii - oO0
 if 97 - 97: II111iiii % OO00O0O0O00Oo + OO00O0O0O00Oo - I1111 / IiiIII111ii * ooOo
 if 17 - 17: IiiIII111ii
def i1i1IiIi1 ( ) :
 oo00O00oO000o ( 'Atari Titles A Thru B' , 'rom' , url = oO00O0 , icon = i111iIi1i1II1 , themeit = OOOiiiiI )
 oo00O00oO000o ( 'Atari Titles C Thru D' , 'rom' , url = IIi1IIIi , icon = Oo0O00O000 , themeit = OOOiiiiI )
 oo00O00oO000o ( 'Atari Titles E Thru G' , 'rom' , url = O00Ooo , icon = i111iIi1i1II1 , themeit = OOOiiiiI )
 oo00O00oO000o ( 'Atari Titles H Thru L' , 'rom' , url = OOOO0OOO , icon = i111iIi1i1II1 , themeit = OOOiiiiI )
 oo00O00oO000o ( 'Atari Titles M Thru O' , 'rom' , url = i1i1ii , icon = i111iIi1i1II1 , themeit = OOOiiiiI )
 oo00O00oO000o ( 'Atari Titles P Thru R' , 'rom' , url = iII1ii1 , icon = i111iIi1i1II1 , themeit = OOOiiiiI )
 oo00O00oO000o ( 'Atari Titles S Thru U' , 'rom' , url = I1i1iiiI1 , icon = i111iIi1i1II1 , themeit = OOOiiiiI )
 oo00O00oO000o ( 'Atari Titles V Thru Z' , 'rom' , url = iIIi , icon = i111iIi1i1II1 , themeit = OOOiiiiI )
 if 22 - 22: i11IiIiiIIIII * O0 . II111iiii - I1111
 if 90 - 90: IIIi1i1I
 if 94 - 94: i11IiIiiIIIII / oO0 * OO00O0O0O00Oo - o0o0Oo0oooo0
 if 44 - 44: IiiIII111ii % i11iIiiIii - iiIIi1IiIi11 * oO0 + Ooo0O * iii11iiII
 if 41 - 41: O0 * OOoooooO - o0o0Oo0oooo0 . IiiIII111ii
def oOIIIiI1ii1IIi ( ) :
 oo00O00oO000o ( 'N64 Titles A Thru B' , 'rom' , url = oO0o00oo0 , icon = i111iIi1i1II1 , themeit = OOOiiiiI )
 oo00O00oO000o ( 'N64 Titles C Thru E' , 'rom' , url = ii1IIII , icon = Oo0O00O000 , themeit = OOOiiiiI )
 oo00O00oO000o ( 'N64 Titles F Thru J' , 'rom' , url = oO00oOooooo0 , icon = i111iIi1i1II1 , themeit = OOOiiiiI )
 oo00O00oO000o ( 'N64 Titles K Thru M' , 'rom' , url = oOo , icon = i111iIi1i1II1 , themeit = OOOiiiiI )
 oo00O00oO000o ( 'N64 Titles N Thru R' , 'rom' , url = O0OOooOoO , icon = i111iIi1i1II1 , themeit = OOOiiiiI )
 oo00O00oO000o ( 'N64 Titles S Thru T' , 'rom' , url = i1II1I1Iii1 , icon = i111iIi1i1II1 , themeit = OOOiiiiI )
 oo00O00oO000o ( 'N64 Titles V Thru Z' , 'rom' , url = iiI11Iii , icon = i111iIi1i1II1 , themeit = OOOiiiiI )
 if 55 - 55: iiIIi1IiIi11 - I1111
 if 100 - 100: O0
 if 79 - 79: iIii1I11I1II1
 if 81 - 81: iii11iiII + iIii1I11I1II1 * OO00O0O0O00Oo - iIii1I11I1II1 . iii11iiII
 if 48 - 48: i11IiIiiIIIII . OoooooooOO . ooOo . o0o0Oo0oooo0 % oO0 / iiIIi1IiIi11
def ii1I111i1Ii ( ) :
 oo00O00oO000o ( 'PC Engine And Turbo Grafx Titles A Thru B' , 'rom' , url = O0o0O0 , icon = i111iIi1i1II1 , themeit = OOOiiiiI )
 oo00O00oO000o ( 'PC Engine And Turbo Grafx Titles C Thru E' , 'rom' , url = Ii1II1I11i1 , icon = Oo0O00O000 , themeit = OOOiiiiI )
 oo00O00oO000o ( 'PC Engine And Turbo Grafx Titles F Thru I' , 'rom' , url = oOoooooOoO , icon = i111iIi1i1II1 , themeit = OOOiiiiI )
 oo00O00oO000o ( 'PC Engine And Turbo Grafx Titles J Thru M' , 'rom' , url = Ii111 , icon = i111iIi1i1II1 , themeit = OOOiiiiI )
 oo00O00oO000o ( 'PC Engine And Turbo Grafx Titles N Thru Q' , 'rom' , url = I111i1i1111 , icon = i111iIi1i1II1 , themeit = OOOiiiiI )
 oo00O00oO000o ( 'PC Engine And Turbo Grafx Titles R Thru U' , 'rom' , url = IIII1 , icon = i111iIi1i1II1 , themeit = OOOiiiiI )
 oo00O00oO000o ( 'PC Engine And Turbo Grafx Titles V Thru Z' , 'rom' , url = I1I1i , icon = i111iIi1i1II1 , themeit = OOOiiiiI )
 if 84 - 84: oO0 % iIii1I11I1II1 + I1111 . oO0 % I1111
 if 93 - 93: O0
 if 85 - 85: i11iIiiIii % i11iIiiIii + O0 / iii11iiII
 if 89 - 89: IiiIII111ii % i1IIi % IIIi1i1I
 if 53 - 53: IIIi1i1I * OoooooooOO . o0o0Oo0oooo0
def OOoooOoO0Oo ( ) :
 oo00O00oO000o ( 'Nintendo DS Titles A' , 'rom' , url = I1IIIiIiIi , icon = i111iIi1i1II1 , themeit = OOOiiiiI )
 oo00O00oO000o ( 'Nintendo DS Titles B' , 'rom' , url = IIIII1 , icon = i111iIi1i1II1 , themeit = OOOiiiiI )
 oo00O00oO000o ( 'Nintendo DS Titles C' , 'rom' , url = iIi1Ii1i1iI , icon = i111iIi1i1II1 , themeit = OOOiiiiI )
 oo00O00oO000o ( 'Nintendo DS Titles D' , 'rom' , url = IIiI1 , icon = i111iIi1i1II1 , themeit = OOOiiiiI )
 oo00O00oO000o ( 'Nintendo DS Titles E Thru F' , 'rom' , url = i1iI1 , icon = i111iIi1i1II1 , themeit = OOOiiiiI )
 oo00O00oO000o ( 'Nintendo DS Titles G Thru H' , 'rom' , url = ii1I1IiiI1ii1i , icon = i111iIi1i1II1 , themeit = OOOiiiiI )
 oo00O00oO000o ( 'Nintendo DS Titles I Thru J' , 'rom' , url = O0o , icon = i111iIi1i1II1 , themeit = OOOiiiiI )
 oo00O00oO000o ( 'Nintendo DS Titles K Thru L' , 'rom' , url = oO0OoO00o , icon = i111iIi1i1II1 , themeit = OOOiiiiI )
 oo00O00oO000o ( 'Nintendo DS Titles M' , 'rom' , url = II1iiiiII , icon = i111iIi1i1II1 , themeit = OOOiiiiI )
 oo00O00oO000o ( 'Nintendo DS Titles N Thru O' , 'rom' , url = O0OoOO0oo0 , icon = i111iIi1i1II1 , themeit = OOOiiiiI )
 oo00O00oO000o ( 'Nintendo DS Titles P Thru Q' , 'rom' , url = oOO , icon = i111iIi1i1II1 , themeit = OOOiiiiI )
 oo00O00oO000o ( 'Nintendo DS Titles R' , 'rom' , url = O0o0OO0000ooo , icon = i111iIi1i1II1 , themeit = OOOiiiiI )
 oo00O00oO000o ( 'Nintendo DS Titles S' , 'rom' , url = iIIII1iIIii , icon = i111iIi1i1II1 , themeit = OOOiiiiI )
 oo00O00oO000o ( 'Nintendo DS Titles T Thru U' , 'rom' , url = oOOO00o000o , icon = i111iIi1i1II1 , themeit = OOOiiiiI )
 oo00O00oO000o ( 'Nintendo DS Titles V Thru Z' , 'rom' , url = iIi11i1 , icon = i111iIi1i1II1 , themeit = OOOiiiiI )
 if 78 - 78: OoooooooOO / iii11iiII % o0o0Oo0oooo0 * OoooooooOO
 if 68 - 68: IIIi1i1I
 if 29 - 29: iiIIi1IiIi11 + i11iIiiIii % i11IiIiiIIIII
 if 93 - 93: o0o0Oo0oooo0 % iIii1I11I1II1
def Ooo0o0oo0 ( ) :
 oo00O00oO000o ( 'Playstation Titles A' , 'rom' , url = oO00oo0o00o0o , icon = i111iIi1i1II1 , themeit = OOOiiiiI )
 oo00O00oO000o ( 'Playstation Titles B' , 'rom' , url = IiIIIIIi , icon = i111iIi1i1II1 , themeit = OOOiiiiI )
 oo00O00oO000o ( 'Playstation Titles C Thru D' , 'rom' , url = IiIi1iIIi1 , icon = i111iIi1i1II1 , themeit = OOOiiiiI )
 oo00O00oO000o ( 'Playstation Titles E Thru F' , 'rom' , url = O0OoO0ooOO0o , icon = i111iIi1i1II1 , themeit = OOOiiiiI )
 oo00O00oO000o ( 'Playstation Titles G Thru J' , 'rom' , url = OoOo0oOooOoOO , icon = i111iIi1i1II1 , themeit = OOOiiiiI )
 oo00O00oO000o ( 'Playstation Titles K Thru N' , 'rom' , url = oo00ooOoO00 , icon = i111iIi1i1II1 , themeit = OOOiiiiI )
 oo00O00oO000o ( 'Playstation Titles O Thru R' , 'rom' , url = o00oOoOo0 , icon = i111iIi1i1II1 , themeit = OOOiiiiI )
 oo00O00oO000o ( 'Playstation Titles S Thru T' , 'rom' , url = o0O0O0ooo0oOO , icon = i111iIi1i1II1 , themeit = OOOiiiiI )
 oo00O00oO000o ( 'Playstation Titles U Thru Z' , 'rom' , url = oo000 , icon = i111iIi1i1II1 , themeit = OOOiiiiI )
 if 87 - 87: o0o0Oo0oooo0 / i1Ii + iIii1I11I1II1
def oo0O0o ( url = None ) :
 if not OO == 'http://' :
  if url == None :
   IioO0O = wiz . workingURL ( OO )
   Oo00o0O0O = uservar . ADDONFILE
  else :
   IioO0O = wiz . workingURL ( url )
   Oo00o0O0O = url
  if IioO0O == True :
   o0O0Oo00 = wiz . openURL ( Oo00o0O0O ) . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' ) . replace ( 'repository=""' , 'repository="none"' ) . replace ( 'repositoryurl=""' , 'repositoryurl="http://"' ) . replace ( 'repositoryxml=""' , 'repositoryxml="http://"' )
   O0Oo0o000oO = re . compile ( 'name="(.+?)".+?lugin="(.+?)".+?rl="(.+?)".+?epository="(.+?)".+?epositoryxml="(.+?)".+?epositoryurl="(.+?)".+?con="(.+?)".+?anart="(.+?)".+?dult="(.+?)".+?escription="(.+?)"' ) . findall ( o0O0Oo00 )
   if len ( O0Oo0o000oO ) > 0 :
    iiIi = 0
    for oO0o00oOOooO0 , o0ooO0OoOo , url , o0oOO00 , ii11iiIi , i11iI11I1I , i1i1i1I , oOoo000 , OooOo00o , IiI11i1IIiiI in O0Oo0o000oO :
     if o0ooO0OoOo . lower ( ) == 'section' :
      iiIi += 1
      oo00O00oO000o ( "[B]%s[/B]" % oO0o00oOOooO0 , 'addons' , url , description = IiI11i1IIiiI , icon = i1i1i1I , fanart = oOoo000 , themeit = OOoO )
     else :
      if not O0Oo000ooO00 == 'true' and OooOo00o . lower ( ) == 'yes' : continue
      try :
       Ii1iiIi1I11i = xbmcaddon . Addon ( id = o0ooO0OoOo ) . getAddonInfo ( 'path' )
       if os . path . exists ( Ii1iiIi1I11i ) :
        oO0o00oOOooO0 = "[COLOR green][Installed][/COLOR] %s" % oO0o00oOOooO0
      except :
       pass
      iiIi += 1
      iiiii1II ( oO0o00oOOooO0 , 'addoninstall' , o0ooO0OoOo , Oo00o0O0O , description = IiI11i1IIiiI , icon = i1i1i1I , fanart = oOoo000 , themeit = oooOo0OOOoo0 )
     if iiIi < 1 :
      iiiii1II ( "No addons added to this menu yet!" , '' , themeit = oooOo0OOOoo0 )
   else :
    iiiii1II ( 'Text File not formated correctly!' , '' , themeit = OOoO )
    wiz . log ( "[Addon Menu] ERROR: Invalid Format." )
  else :
   wiz . log ( "[Addon Menu] ERROR: URL for Addon list not working." )
   iiiii1II ( 'Url for txt file not valid' , '' , themeit = OOoO )
   iiiii1II ( '%s' % IioO0O , '' , themeit = OOoO )
 else : wiz . log ( "[Addon Menu] No Addon list added." )
 iIi1 ( 'files' , 'viewType' )
 if 89 - 89: OO00O0O0O00Oo . i1Ii % Ooo0O . Ooo0O - OoooooooOO
def oo0ooO0O0o ( plugin , url ) :
 if not OO == 'http://' :
  IioO0O = wiz . workingURL ( url )
  if IioO0O == True :
   o0O0Oo00 = wiz . openURL ( url ) . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' ) . replace ( 'repository=""' , 'repository="none"' ) . replace ( 'repositoryurl=""' , 'repositoryurl="http://"' ) . replace ( 'repositoryxml=""' , 'repositoryxml="http://"' )
   O0Oo0o000oO = re . compile ( 'name="(.+?)".+?lugin="%s".+?rl="(.+?)".+?epository="(.+?)".+?epositoryxml="(.+?)".+?epositoryurl="(.+?)".+?con="(.+?)".+?anart="(.+?)".+?dult="(.+?)".+?escription="(.+?)"' % plugin ) . findall ( o0O0Oo00 )
   if len ( O0Oo0o000oO ) > 0 :
    for oO0o00oOOooO0 , url , o0oOO00 , ii11iiIi , i11iI11I1I , i1i1i1I , oOoo000 , OooOo00o , IiI11i1IIiiI in O0Oo0o000oO :
     if os . path . exists ( os . path . join ( O0O , plugin ) ) :
      oo0ooO = [ 'Launch Addon' , 'Remove Addon' ]
      I11o0000o0Oo = iiIIIII1i1iI . select ( "[COLOR %s]Addon already installed what would you like to do?[/COLOR]" % iIiIi11 , oo0ooO )
      if I11o0000o0Oo == 0 :
       wiz . ebi ( 'RunAddon(%s)' % plugin )
       xbmc . sleep ( 500 )
       return True
      elif I11o0000o0Oo == 1 :
       wiz . cleanHouse ( os . path . join ( O0O , plugin ) )
       try : wiz . removeFolder ( os . path . join ( O0O , plugin ) )
       except : pass
       if iiIIIII1i1iI . yesno ( o0OOO , "[COLOR %s]Would you like to remove the addon_data for:" % iIiIi11 , "[COLOR %s]%s[/COLOR]?[/COLOR]" % ( oOOo0O00o , plugin ) , yeslabel = "[B][COLOR green]Yes Remove[/COLOR][/B]" , nolabel = "[B][COLOR red]No Skip[/COLOR][/B]" ) :
        ooo0O0OOo0OoO ( plugin )
       wiz . refresh ( )
       return True
      else :
       return False
     Ii1i1 = os . path . join ( O0O , o0oOO00 )
     if not o0oOO00 . lower ( ) == 'none' and not os . path . exists ( Ii1i1 ) :
      wiz . log ( "Repository not installed, installing it" )
      if iiIIIII1i1iI . yesno ( o0OOO , "[COLOR %s]Would you like to install the repository for [COLOR %s]%s[/COLOR]:" % ( iIiIi11 , oOOo0O00o , plugin ) , "[COLOR %s]%s[/COLOR]?[/COLOR]" % ( oOOo0O00o , o0oOO00 ) , yeslabel = "[B][COLOR green]Yes Install[/COLOR][/B]" , nolabel = "[B][COLOR red]No Skip[/COLOR][/B]" ) :
       i1iIi = wiz . parseDOM ( wiz . openURL ( ii11iiIi ) , 'addon' , ret = 'version' , attrs = { 'id' : o0oOO00 } )
       if len ( i1iIi ) > 0 :
        oOoO00 = '%s%s-%s.zip' % ( i11iI11I1I , o0oOO00 , i1iIi [ 0 ] )
        wiz . log ( oOoO00 )
        if o0OIiII >= 17 : wiz . addonDatabase ( o0oOO00 , 1 )
        i1ii1iIIi11i111I ( o0oOO00 , oOoO00 )
        wiz . ebi ( 'UpdateAddonRepos()' )
        if 16 - 16: ooOo . iIii1I11I1II1
        wiz . log ( "Installing Addon from Kodi" )
        iiiIIIii = ooOoo00 ( plugin )
        wiz . log ( "Install from Kodi: %s" % iiiIIIii )
        if iiiIIIii :
         wiz . refresh ( )
         return True
       else :
        wiz . log ( "[Addon Installer] Repository not installed: Unable to grab url! (%s)" % o0oOO00 )
      else : wiz . log ( "[Addon Installer] Repository for %s not installed: %s" % ( plugin , o0oOO00 ) )
     elif o0oOO00 . lower ( ) == 'none' :
      wiz . log ( "No repository, installing addon" )
      Ii11IiI = plugin
      o00oOoO0Oo = url
      i1ii1iIIi11i111I ( plugin , url )
      wiz . refresh ( )
      return True
     else :
      wiz . log ( "Repository installed, installing addon" )
      iiiIIIii = ooOoo00 ( plugin , False )
      if iiiIIIii :
       wiz . refresh ( )
       return True
     if os . path . exists ( os . path . join ( O0O , plugin ) ) : return True
     Ii1iiII1i = wiz . parseDOM ( wiz . openURL ( ii11iiIi ) , 'addon' , ret = 'version' , attrs = { 'id' : plugin } )
     if len ( Ii1iiII1i ) > 0 :
      url = "%s%s-%s.zip" % ( url , plugin , Ii1iiII1i [ 0 ] )
      wiz . log ( str ( url ) )
      if o0OIiII >= 17 : wiz . addonDatabase ( plugin , 1 )
      i1ii1iIIi11i111I ( plugin , url )
      wiz . refresh ( )
     else :
      wiz . log ( "no match" ) ; return False
   else : wiz . log ( "[Addon Installer] Invalid Format" )
  else : wiz . log ( "[Addon Installer] Text File: %s" % IioO0O )
 else : wiz . log ( "[Addon Installer] Not Enabled." )
 if 52 - 52: IIIi1i1I / OO00O0O0O00Oo
def ooOoo00 ( plugin , over = True ) :
 if over == True :
  xbmc . sleep ( 2000 )
  if 91 - 91: i1Ii . Ooo0O + II111iiii
 wiz . ebi ( 'RunPlugin(plugin://%s)' % plugin )
 if not wiz . whileWindow ( 'yesnodialog' ) :
  return False
 xbmc . sleep ( 500 )
 if wiz . whileWindow ( 'okdialog' ) :
  return False
 wiz . whileWindow ( 'progressdialog' )
 if os . path . exists ( os . path . join ( O0O , plugin ) ) : return True
 else : return False
 if 36 - 36: O0 * I1111 % iiIIi1IiIi11 * iiIIi1IiIi11 / I1111 * i1Ii
def i1ii1iIIi11i111I ( name , url ) :
 if not wiz . workingURL ( url ) == True : wiz . LogNotify ( "[COLOR %s]Addon Installer[/COLOR]" % oOOo0O00o , '[COLOR %s]%s:[/COLOR] [COLOR %s]Invalid Zip Url![/COLOR]' % ( oOOo0O00o , name , iIiIi11 ) ) ; return
 if not os . path . exists ( o0o0OOO0o0 ) : os . makedirs ( o0o0OOO0o0 )
 oo00 . create ( o0OOO , '[COLOR %s][B]Downloading:[/B][/COLOR] [COLOR %s]%s[/COLOR]' % ( iIiIi11 , oOOo0O00o , name ) , '' , '[COLOR %s]Please Wait[/COLOR]' % iIiIi11 )
 IiI = url . split ( '/' )
 O0o0OO00 = os . path . join ( o0o0OOO0o0 , IiI [ - 1 ] )
 try : os . remove ( O0o0OO00 )
 except : pass
 downloader . download ( url , O0o0OO00 , oo00 )
 OOOoOo00O = '[COLOR %s][B]Installing:[/B][/COLOR] [COLOR %s]%s[/COLOR]' % ( iIiIi11 , oOOo0O00o , name )
 oo00 . update ( 0 , OOOoOo00O , '' , '[COLOR %s]Please Wait[/COLOR]' % iIiIi11 )
 iIi11i , ooIII1II1iii1i , O0OO0oOO = extract . all ( O0o0OO00 , O0O , oo00 , title = OOOoOo00O )
 oo00 . update ( 0 , OOOoOo00O , '' , '[COLOR %s]Installing Dependencies[/COLOR]' % iIiIi11 )
 ooooO ( name )
 oO0O0 ( name , oo00 )
 oo00 . close ( )
 wiz . ebi ( 'UpdateAddonRepos()' )
 wiz . ebi ( 'UpdateLocalAddons()' )
 wiz . refresh ( )
 if 19 - 19: IiiIII111ii
def oO0O0 ( name , DP = None ) :
 O0o00oO0oOO = os . path . join ( O0O , name , 'addon.xml' )
 if os . path . exists ( O0o00oO0oOO ) :
  iiiii1I1III1 = open ( O0o00oO0oOO , mode = 'r' ) ; o0O0Oo00 = iiiii1I1III1 . read ( ) ; iiiii1I1III1 . close ( ) ;
  O0Oo0o000oO = wiz . parseDOM ( o0O0Oo00 , 'import' , ret = 'addon' )
  for i1oO00O in O0Oo0o000oO :
   if not 'xbmc.python' in i1oO00O :
    if not DP == None :
     DP . update ( 0 , '' , '[COLOR %s]%s[/COLOR]' % ( oOOo0O00o , i1oO00O ) )
    wiz . createTemp ( i1oO00O )
    if 77 - 77: i11iIiiIii % i1IIi % i1Ii
    if 15 - 15: iIii1I11I1II1 . O0
    if 70 - 70: IiiIII111ii . i11iIiiIii % IiiIII111ii . O0 - iIii1I11I1II1
    if 26 - 26: iii11iiII
    if 76 - 76: i1IIi * OoooooooOO * O0 + OO00O0O0O00Oo * OO00O0O0O00Oo
    if 35 - 35: I1I1i1
    if 73 - 73: O0 - oO0
    if 2 - 2: II111iiii / OO00O0O0O00Oo
    if 54 - 54: i1IIi . i11IiIiiIIIII - oO0 + OOoooooO + Ooo0O / Ooo0O
    if 22 - 22: OOoooooO . iIii1I11I1II1
    if 12 - 12: IiiIII111ii
    if 71 - 71: ooOo . II111iiii . ooOo - OOoooooO
    if 45 - 45: i1Ii / O0 / o0o0Oo0oooo0 * iii11iiII
    if 18 - 18: iIii1I11I1II1 + iii11iiII + iIii1I11I1II1 . oO0 + OO00O0O0O00Oo . OOoooooO
    if 7 - 7: oO0 + iIii1I11I1II1 * i11IiIiiIIIII * i11IiIiiIIIII / II111iiii - IiiIII111ii
    if 65 - 65: IIIi1i1I + o0o0Oo0oooo0 + II111iiii
    if 77 - 77: II111iiii
    if 50 - 50: O0 . O0 . OOoooooO % Ooo0O
    if 68 - 68: IIIi1i1I
    if 10 - 10: IiiIII111ii
    if 77 - 77: iii11iiII / II111iiii + i1Ii + OOoooooO - i11iIiiIii
    if 44 - 44: ooOo + o0o0Oo0oooo0 + oO0 . ooOo * o0o0Oo0oooo0 % iIii1I11I1II1
    if 72 - 72: iii11iiII . iii11iiII - oO0
    if 48 - 48: Ooo0O - OOoooooO + Ooo0O - ooOo * i11iIiiIii . iiIIi1IiIi11
    if 35 - 35: i1Ii . O0 + Ooo0O + iii11iiII + i1IIi
    if 65 - 65: O0 * ooOo / ooOo . o0o0Oo0oooo0
def ooooO ( addon ) :
 OOOoO000 = os . path . join ( O0O , addon , 'addon.xml' )
 if os . path . exists ( OOOoO000 ) :
  try :
   list = open ( OOOoO000 , mode = 'r' ) ; Oo0O0OOO0o0O = list . read ( ) ; list . close ( )
   oO0o00oOOooO0 = wiz . parseDOM ( Oo0O0OOO0o0O , 'addon' , ret = 'name' , attrs = { 'id' : addon } )
   i1i1i1I = os . path . join ( O0O , addon , 'icon.png' )
   wiz . LogNotify ( '[COLOR %s]%s[/COLOR]' % ( oOOo0O00o , oO0o00oOOooO0 [ 0 ] ) , '[COLOR %s]Addon Enabled[/COLOR]' % iIiIi11 , '2000' , i1i1i1I )
  except : pass
  if 51 - 51: IIIi1i1I + I1111 + iiIIi1IiIi11 + iiIIi1IiIi11 % I1I1i1
def iIi1i1iIi1Ii1 ( url = None ) :
 if not oO0O0OO0O == 'http://' :
  if url == None :
   oOOoOOO0oo0 = wiz . workingURL ( oO0O0OO0O )
   O00O = uservar . YOUTUBEFILE
  else :
   oOOoOOO0oo0 = wiz . workingURL ( url )
   O00O = url
  if oOOoOOO0oo0 == True :
   o0O0Oo00 = wiz . openURL ( O00O ) . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
   O0Oo0o000oO = re . compile ( 'name="(.+?)".+?ection="(.+?)".+?rl="(.+?)".+?con="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( o0O0Oo00 )
   if len ( O0Oo0o000oO ) > 0 :
    for oO0o00oOOooO0 , O0OOOOOoo , url , i1i1i1I , oOoo000 , IiI11i1IIiiI in O0Oo0o000oO :
     if O0OOOOOoo . lower ( ) == "yes" :
      oo00O00oO000o ( "[B]%s[/B]" % oO0o00oOOooO0 , 'youtube' , url , description = IiI11i1IIiiI , icon = i1i1i1I , fanart = oOoo000 , themeit = OOoO )
     else :
      iiiii1II ( oO0o00oOOooO0 , 'viewVideo' , url = url , description = IiI11i1IIiiI , icon = i1i1i1I , fanart = oOoo000 , themeit = oooOo0OOOoo0 )
   else : wiz . log ( "[YouTube Menu] ERROR: Invalid Format." )
  else :
   wiz . log ( "[YouTube Menu] ERROR: URL for YouTube list not working." )
   iiiii1II ( 'Url for txt file not valid' , '' , themeit = OOoO )
   iiiii1II ( '%s' % oOOoOOO0oo0 , '' , themeit = OOoO )
 else : wiz . log ( "[YouTube Menu] No YouTube list added." )
 iIi1 ( 'files' , 'viewType' )
 if 69 - 69: ooOo + iiIIi1IiIi11
def i1IiII ( view = None ) :
 i1II = '[B][COLOR green]ON[/COLOR][/B]' ; IiiIi11Ii1iI1 = '[B][COLOR red]OFF[/COLOR][/B]'
 oOo00o = 'true' if ooOooo000oOO == 'true' else 'false'
 II111i1ii1iII = 'true' if Oo0oOOo == 'true' else 'false'
 ooo0OoO = 'true' if Oo0OoO00oOO0o == 'true' else 'false'
 iiI1111I11i1I = 'true' if OOO00O == 'true' else 'false'
 O00oOo0O0o00O = 'true' if oO0Ii1iIiII1ii1 == 'true' else 'false'
 ooo0oo00O00Oo = 'true' if O00O0oOO00O00 == 'true' else 'false'
 OOO000000OOO0 = 'true' if i1Oo00 == 'true' else 'false'
 ooOoOOoooO000 = 'true' if oOooOOOoOo == 'true' else 'false'
 if wiz . Grab_Log ( True ) == False : OoO0o000oOo = 0
 else : OoO0o000oOo = Oo00OO00o0oO ( wiz . Grab_Log ( True ) , True , True )
 if wiz . Grab_Log ( True , True ) == False : iI1 = 0
 else : iI1 = Oo00OO00o0oO ( wiz . Grab_Log ( True , True ) , True , True )
 I1I1i1i = int ( OoO0o000oOo ) + int ( iI1 )
 OOo0O = str ( I1I1i1i ) + ' Error(s) Found' if I1I1i1i > 0 else 'None Found'
 oOOoooO0O0 = ': [COLOR red]Not Found[/COLOR]' if not os . path . exists ( I11iii1Ii ) else ": [COLOR green]%s[/COLOR]" % wiz . convertSize ( os . path . getsize ( I11iii1Ii ) )
 if OOO000000OOO0 == 'true' :
  ii1O0ooooo000 = 'true'
  OooOoOO0OO = 'true'
  I1iiIiiii1111 = 'true'
  I1ii1i11i = 'true'
  Oooooo0O00o = 'true'
  II11ii1 = 'true'
  ii1II1II = 'true'
  i11i11II11i = 'true'
 else :
  ii1O0ooooo000 = 'true' if i1i == 'true' else 'false'
  OooOoOO0OO = 'true' if iiI111I1iIiI == 'true' else 'false'
  I1iiIiiii1111 = 'true' if IIIi1I1IIii1II == 'true' else 'false'
  I1ii1i11i = 'true' if O0ii1ii1ii == 'true' else 'false'
  Oooooo0O00o = 'true' if oooooOoo0ooo == 'true' else 'false'
  II11ii1 = 'true' if I1I1IiI1 == 'true' else 'false'
  ii1II1II = 'true' if III1iII1I1ii == 'true' else 'false'
  i11i11II11i = 'true' if oOOo0 == 'true' else 'false'
 II1Ii1I1i = wiz . getSize ( o0o0OOO0o0 )
 OOooOooo0OOo0 = wiz . getSize ( oOoOooOo0o0 )
 oo0o0OoOO0o0 = wiz . getCacheSize ( )
 III1III11II = II1Ii1I1i + OOooOooo0OOo0 + oo0o0OoOO0o0
 iIi1iI = [ 'Always' , 'Daily' , '3 Days' , 'Weekly' ]
 oo00O00oO000o ( '[B]Cleaning Tools[/B]' , 'maint' , 'clean' , icon = IiIi11iI , themeit = OOOiiiiI )
 if view == "clean" or oO0Ii1iIiII1ii1 == 'true' :
  iiiii1II ( 'Total Clean Up: [COLOR green][B]%s[/B][/COLOR]' % wiz . convertSize ( III1III11II ) , 'fullclean' , icon = IiIi11iI , themeit = OOoO )
  iiiii1II ( 'Clear Cache: [COLOR green][B]%s[/B][/COLOR]' % wiz . convertSize ( oo0o0OoOO0o0 ) , 'clearcache' , icon = IiIi11iI , themeit = OOoO )
  iiiii1II ( 'Clear Packages: [COLOR green][B]%s[/B][/COLOR]' % wiz . convertSize ( II1Ii1I1i ) , 'clearpackages' , icon = IiIi11iI , themeit = OOoO )
  iiiii1II ( 'Clear Thumbnails: [COLOR green][B]%s[/B][/COLOR]' % wiz . convertSize ( OOooOooo0OOo0 ) , 'clearthumb' , icon = IiIi11iI , themeit = OOoO )
  iiiii1II ( 'Clear Old Thumbnails' , 'oldThumbs' , icon = IiIi11iI , themeit = OOoO )
  iiiii1II ( 'Clear Crash Logs' , 'clearcrash' , icon = IiIi11iI , themeit = OOoO )
  iiiii1II ( 'Purge Databases' , 'purgedb' , icon = IiIi11iI , themeit = OOoO )
  iiiii1II ( 'Fresh Start' , 'freshstart' , icon = IiIi11iI , themeit = OOoO )
 oo00O00oO000o ( '[B]Addon Tools[/B]' , 'maint' , 'addon' , icon = IiIi11iI , themeit = OOOiiiiI )
 if view == "addon" or oO0Ii1iIiII1ii1 == 'true' :
  iiiii1II ( 'Remove Addons' , 'removeaddons' , icon = IiIi11iI , themeit = OOoO )
  oo00O00oO000o ( 'Remove Addon Data' , 'removeaddondata' , icon = IiIi11iI , themeit = OOoO )
  oo00O00oO000o ( 'Enable/Disable Addons' , 'enableaddons' , icon = IiIi11iI , themeit = OOoO )
  iiiii1II ( 'Enable/Disable Adult Addons' , 'toggleadult' , icon = IiIi11iI , themeit = OOoO )
  iiiii1II ( 'Force Update Addons' , 'forceupdate' , icon = IiIi11iI , themeit = OOoO )
  iiiii1II ( 'Hide Passwords On Keyboard Entry' , 'hidepassword' , icon = IiIi11iI , themeit = OOoO )
  iiiii1II ( 'Unhide Passwords On Keyboard Entry' , 'unhidepassword' , icon = IiIi11iI , themeit = OOoO )
 oo00O00oO000o ( '[B]Misc Maintenance[/B]' , 'maint' , 'misc' , icon = IiIi11iI , themeit = OOOiiiiI )
 if view == "misc" or oO0Ii1iIiII1ii1 == 'true' :
  iiiii1II ( 'Kodi 17 Fix' , 'kodi17fix' , icon = IiIi11iI , themeit = OOoO )
  iiiii1II ( 'Reload Skin' , 'forceskin' , icon = IiIi11iI , themeit = OOoO )
  iiiii1II ( 'Reload Profile' , 'forceprofile' , icon = IiIi11iI , themeit = OOoO )
  iiiii1II ( 'Force Close Kodi' , 'forceclose' , icon = IiIi11iI , themeit = OOoO )
  iiiii1II ( 'Upload Kodi.log' , 'uploadlog' , icon = IiIi11iI , themeit = OOoO )
  iiiii1II ( 'View Errors in Log: %s' % ( OOo0O ) , 'viewerrorlog' , icon = IiIi11iI , themeit = OOoO )
  iiiii1II ( 'View Log File' , 'viewlog' , icon = IiIi11iI , themeit = OOoO )
  iiiii1II ( 'View Wizard Log File' , 'viewwizlog' , icon = IiIi11iI , themeit = OOoO )
  iiiii1II ( 'Clear Wizard Log File%s' % oOOoooO0O0 , 'clearwizlog' , icon = IiIi11iI , themeit = OOoO )
 oo00O00oO000o ( '[B]Back up/Restore[/B]' , 'maint' , 'backup' , icon = IiIi11iI , themeit = OOOiiiiI )
 if view == "backup" or oO0Ii1iIiII1ii1 == 'true' :
  iiiii1II ( 'Clean Up Back Up Folder' , 'clearbackup' , icon = IiIi11iI , themeit = OOoO )
  iiiii1II ( 'Back Up Location: [COLOR %s]%s[/COLOR]' % ( iIiIi11 , O0ooO0Oo00o ) , 'settings' , 'Maintenance' , icon = IiIi11iI , themeit = OOoO )
  iiiii1II ( '[Back Up]: Build' , 'backupbuild' , icon = IiIi11iI , themeit = OOoO )
  iiiii1II ( '[Back Up]: GuiFix' , 'backupgui' , icon = IiIi11iI , themeit = OOoO )
  iiiii1II ( '[Back Up]: Theme' , 'backuptheme' , icon = IiIi11iI , themeit = OOoO )
  iiiii1II ( '[Back Up]: Addon_data' , 'backupaddon' , icon = IiIi11iI , themeit = OOoO )
  iiiii1II ( '[Restore]: Local Build' , 'restorezip' , icon = IiIi11iI , themeit = OOoO )
  iiiii1II ( '[Restore]: Local GuiFix' , 'restoregui' , icon = IiIi11iI , themeit = OOoO )
  iiiii1II ( '[Restore]: Local Addon_data' , 'restoreaddon' , icon = IiIi11iI , themeit = OOoO )
  iiiii1II ( '[Restore]: External Build' , 'restoreextzip' , icon = IiIi11iI , themeit = OOoO )
  iiiii1II ( '[Restore]: External GuiFix' , 'restoreextgui' , icon = IiIi11iI , themeit = OOoO )
  iiiii1II ( '[Restore]: External Addon_data' , 'restoreextaddon' , icon = IiIi11iI , themeit = OOoO )
 oo00O00oO000o ( '[B]System Tweaks/Fixes[/B]' , 'maint' , 'tweaks' , icon = IiIi11iI , themeit = OOOiiiiI )
 if view == "tweaks" or oO0Ii1iIiII1ii1 == 'true' :
  if not OoOoO == 'http://' and not OoOoO == '' :
   oo00O00oO000o ( 'Advanced Settings' , 'advancedsetting' , icon = IiIi11iI , themeit = OOoO )
  else :
   if os . path . exists ( I11II1i ) :
    iiiii1II ( 'View Currect AdvancedSettings.xml' , 'currentsettings' , icon = IiIi11iI , themeit = OOoO )
    iiiii1II ( 'Remove Currect AdvancedSettings.xml' , 'removeadvanced' , icon = IiIi11iI , themeit = OOoO )
   iiiii1II ( 'Quick Configure AdvancedSettings.xml' , 'autoadvanced' , icon = IiIi11iI , themeit = OOoO )
  iiiii1II ( 'Scan Sources for broken links' , 'checksources' , icon = IiIi11iI , themeit = OOoO )
  iiiii1II ( 'Scan For Broken Repositories' , 'checkrepos' , icon = IiIi11iI , themeit = OOoO )
  iiiii1II ( 'Fix Addons Not Updating' , 'fixaddonupdate' , icon = IiIi11iI , themeit = OOoO )
  iiiii1II ( 'Remove Non-Ascii filenames' , 'asciicheck' , icon = IiIi11iI , themeit = OOoO )
  iiiii1II ( 'Convert Paths to special' , 'convertpath' , icon = IiIi11iI , themeit = OOoO )
  oo00O00oO000o ( 'System Information' , 'systeminfo' , icon = IiIi11iI , themeit = OOoO )
 iiiii1II ( 'Show All Maintenance: %s' % O00oOo0O0o00O . replace ( 'true' , i1II ) . replace ( 'false' , IiiIi11Ii1iI1 ) , 'togglesetting' , 'showmaint' , icon = IiIi11iI , themeit = oooOo0OOOoo0 )
 oo00O00oO000o ( '[I]<< Return to Main Menu[/I]' , icon = IiIi11iI , themeit = oooOo0OOOoo0 )
 iiiii1II ( 'Third Party Wizards: %s' % ooOoOOoooO000 . replace ( 'true' , i1II ) . replace ( 'false' , IiiIi11Ii1iI1 ) , 'togglesetting' , 'enable3rd' , fanart = OOO00 , icon = IiIi11iI , themeit = OOOiiiiI )
 if ooOoOOoooO000 == 'true' :
  OO0Oo = i1Iii1i1I if not i1Iii1i1I == '' else 'Not Set'
  IIiiiiiIiIIi = IiI111111IIII if not IiI111111IIII == '' else 'Not Set'
  iiIi1IIiI = OOO if not OOO == '' else 'Not Set'
  iiiii1II ( 'Edit Third Party Wizard 1: [COLOR %s]%s[/COLOR]' % ( iIiIi11 , OO0Oo ) , 'editthird' , '1' , icon = IiIi11iI , themeit = OOoO )
  iiiii1II ( 'Edit Third Party Wizard 2: [COLOR %s]%s[/COLOR]' % ( iIiIi11 , IIiiiiiIiIIi ) , 'editthird' , '2' , icon = IiIi11iI , themeit = OOoO )
  iiiii1II ( 'Edit Third Party Wizard 3: [COLOR %s]%s[/COLOR]' % ( iIiIi11 , iiIi1IIiI ) , 'editthird' , '3' , icon = IiIi11iI , themeit = OOoO )
 iiiii1II ( 'Auto Clean' , '' , fanart = OOO00 , icon = IiIi11iI , themeit = OOOiiiiI )
 iiiii1II ( 'Auto Clean Up On Startup: %s' % oOo00o . replace ( 'true' , i1II ) . replace ( 'false' , IiiIi11Ii1iI1 ) , 'togglesetting' , 'autoclean' , icon = IiIi11iI , themeit = OOoO )
 if oOo00o == 'true' :
  iiiii1II ( '--- Auto Clean Fequency: [B][COLOR green]%s[/COLOR][/B]' % iIi1iI [ OOoOO0oo0ooO ] , 'changefeq' , icon = IiIi11iI , themeit = OOoO )
  iiiii1II ( '--- Clear Cache on Startup: %s' % II111i1ii1iII . replace ( 'true' , i1II ) . replace ( 'false' , IiiIi11Ii1iI1 ) , 'togglesetting' , 'clearcache' , icon = IiIi11iI , themeit = OOoO )
  iiiii1II ( '--- Clear Packages on Startup: %s' % ooo0OoO . replace ( 'true' , i1II ) . replace ( 'false' , IiiIi11Ii1iI1 ) , 'togglesetting' , 'clearpackages' , icon = IiIi11iI , themeit = OOoO )
  iiiii1II ( '--- Clear Old Thumbs on Startup: %s' % iiI1111I11i1I . replace ( 'true' , i1II ) . replace ( 'false' , IiiIi11Ii1iI1 ) , 'togglesetting' , 'clearthumbs' , icon = IiIi11iI , themeit = OOoO )
 iiiii1II ( 'Clear Video Cache' , '' , fanart = OOO00 , icon = IiIi11iI , themeit = OOOiiiiI )
 iiiii1II ( 'Include Video Cache in Clear Cache: %s' % ooo0oo00O00Oo . replace ( 'true' , i1II ) . replace ( 'false' , IiiIi11Ii1iI1 ) , 'togglecache' , 'includevideo' , icon = IiIi11iI , themeit = OOoO )
 if ooo0oo00O00Oo == 'true' :
  iiiii1II ( '--- Include All Video Addons: %s' % OOO000000OOO0 . replace ( 'true' , i1II ) . replace ( 'false' , IiiIi11Ii1iI1 ) , 'togglecache' , 'includeall' , icon = IiIi11iI , themeit = OOoO )
  iiiii1II ( '--- Include Bob: %s' % ii1O0ooooo000 . replace ( 'true' , i1II ) . replace ( 'false' , IiiIi11Ii1iI1 ) , 'togglecache' , 'includebob' , icon = IiIi11iI , themeit = OOoO )
  iiiii1II ( '--- Include Phoenix: %s' % OooOoOO0OO . replace ( 'true' , i1II ) . replace ( 'false' , IiiIi11Ii1iI1 ) , 'togglecache' , 'includephoenix' , icon = IiIi11iI , themeit = OOoO )
  iiiii1II ( '--- Include Specto: %s' % I1iiIiiii1111 . replace ( 'true' , i1II ) . replace ( 'false' , IiiIi11Ii1iI1 ) , 'togglecache' , 'includespecto' , icon = IiIi11iI , themeit = OOoO )
  iiiii1II ( '--- Include Exodus: %s' % Oooooo0O00o . replace ( 'true' , i1II ) . replace ( 'false' , IiiIi11Ii1iI1 ) , 'togglecache' , 'includeexodus' , icon = IiIi11iI , themeit = OOoO )
  iiiii1II ( '--- Include Salts: %s' % ii1II1II . replace ( 'true' , i1II ) . replace ( 'false' , IiiIi11Ii1iI1 ) , 'togglecache' , 'includesalts' , icon = IiIi11iI , themeit = OOoO )
  iiiii1II ( '--- Include Salts HD Lite: %s' % i11i11II11i . replace ( 'true' , i1II ) . replace ( 'false' , IiiIi11Ii1iI1 ) , 'togglecache' , 'includesaltslite' , icon = IiIi11iI , themeit = OOoO )
  iiiii1II ( '--- Include One Channel: %s' % II11ii1 . replace ( 'true' , i1II ) . replace ( 'false' , IiiIi11Ii1iI1 ) , 'togglecache' , 'includeonechan' , icon = IiIi11iI , themeit = OOoO )
  iiiii1II ( '--- Include Genesis: %s' % I1ii1i11i . replace ( 'true' , i1II ) . replace ( 'false' , IiiIi11Ii1iI1 ) , 'togglecache' , 'includegenesis' , icon = IiIi11iI , themeit = OOoO )
  iiiii1II ( '--- Enable All Video Addons' , 'togglecache' , 'true' , icon = IiIi11iI , themeit = OOoO )
  iiiii1II ( '--- Disable All Video Addons' , 'togglecache' , 'false' , icon = IiIi11iI , themeit = OOoO )
 iIi1 ( 'files' , 'viewType' )
 if 26 - 26: I1I1i1
def IiIi ( url = None ) :
 if not OoOoO == 'http://' :
  if url == None :
   oO0Oo00oo = wiz . workingURL ( OoOoO )
   OoOoooO000OO = uservar . ADVANCEDFILE
  else :
   oO0Oo00oo = wiz . workingURL ( url )
   OoOoooO000OO = url
  iiiii1II ( 'Quick Configure AdvancedSettings.xml' , 'autoadvanced' , icon = IiIi11iI , themeit = OOoO )
  if os . path . exists ( I11II1i ) :
   iiiii1II ( 'View Currect AdvancedSettings.xml' , 'currentsettings' , icon = IiIi11iI , themeit = OOoO )
   iiiii1II ( 'Remove Currect AdvancedSettings.xml' , 'removeadvanced' , icon = IiIi11iI , themeit = OOoO )
  if oO0Oo00oo == True :
   if O0O0ooOOO == 'No' : iiiii1II ( wiz . sep ( ) , '' , icon = IiIi11iI , themeit = OOoO )
   o0O0Oo00 = wiz . openURL ( OoOoooO000OO ) . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
   O0Oo0o000oO = re . compile ( 'name="(.+?)".+?ection="(.+?)".+?rl="(.+?)".+?con="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( o0O0Oo00 )
   if len ( O0Oo0o000oO ) > 0 :
    for oO0o00oOOooO0 , O0OOOOOoo , url , i1i1i1I , oOoo000 , IiI11i1IIiiI in O0Oo0o000oO :
     if O0OOOOOoo . lower ( ) == "yes" :
      oo00O00oO000o ( "[B]%s[/B]" % oO0o00oOOooO0 , 'advancedsetting' , url , description = IiI11i1IIiiI , icon = i1i1i1I , fanart = oOoo000 , themeit = OOoO )
     else :
      iiiii1II ( oO0o00oOOooO0 , 'writeadvanced' , oO0o00oOOooO0 , url , description = IiI11i1IIiiI , icon = i1i1i1I , fanart = oOoo000 , themeit = oooOo0OOOoo0 )
   else : wiz . log ( "[Advanced Settings] ERROR: Invalid Format." )
  else : wiz . log ( "[Advanced Settings] URL not working: %s" % oO0Oo00oo )
 else : wiz . log ( "[Advanced Settings] not Enabled" )
 if 62 - 62: iii11iiII + Ooo0O % iIii1I11I1II1 / iIii1I11I1II1 . OOoooooO . i1Ii
def III1iiIIi ( name , url ) :
 oO0Oo00oo = wiz . workingURL ( url )
 if oO0Oo00oo == True :
  if os . path . exists ( I11II1i ) : i1I1IiI1ii = iiIIIII1i1iI . yesno ( o0OOO , "[COLOR %s]Would you like to overwrite your current Advanced Settings with [COLOR %s]%s[/COLOR]?[/COLOR]" % ( iIiIi11 , oOOo0O00o , name ) , yeslabel = "[B][COLOR green]Overwrite[/COLOR][/B]" , nolabel = "[B][COLOR red]Cancel[/COLOR][/B]" )
  else : i1I1IiI1ii = iiIIIII1i1iI . yesno ( o0OOO , "[COLOR %s]Would you like to download and install [COLOR %s]%s[/COLOR]?[/COLOR]" % ( iIiIi11 , oOOo0O00o , name ) , yeslabel = "[B][COLOR green]Install[/COLOR][/B]" , nolabel = "[B][COLOR red]Cancel[/COLOR][/B]" )
  if 64 - 64: iiIIi1IiIi11 * oO0 % II111iiii - o0o0Oo0oooo0 + oO0
  if i1I1IiI1ii == 1 :
   file = wiz . openURL ( url )
   OO0OOoo0OOO = open ( I11II1i , 'w' ) ;
   OO0OOoo0OOO . write ( file )
   OO0OOoo0OOO . close ( )
   iiIIIII1i1iI . ok ( o0OOO , '[COLOR %s]AdvancedSettings.xml file has been successfully written.  Once you click okay it will force close kodi.[/COLOR]' % iIiIi11 )
   wiz . killxbmc ( True )
  else : wiz . log ( "[Advanced Settings] install canceled" ) ; wiz . LogNotify ( '[COLOR %s]%s[/COLOR]' % ( oOOo0O00o , o0OOO ) , "[COLOR %s]Write Cancelled![/COLOR]" % iIiIi11 ) ; return
 else : wiz . log ( "[Advanced Settings] URL not working: %s" % oO0Oo00oo ) ; wiz . LogNotify ( '[COLOR %s]%s[/COLOR]' % ( oOOo0O00o , o0OOO ) , "[COLOR %s]URL Not Working[/COLOR]" % iIiIi11 )
 if 94 - 94: i11iIiiIii % OoooooooOO / ooOo
def iII1Iii11111 ( ) :
 OO0OOoo0OOO = open ( I11II1i )
 OOo00ooOoO0o = OO0OOoo0OOO . read ( ) . replace ( '\t' , '    ' )
 wiz . TextBox ( o0OOO , OOo00ooOoO0o )
 OO0OOoo0OOO . close ( )
 if 21 - 21: i11iIiiIii
def o00iIiiiII ( ) :
 if os . path . exists ( I11II1i ) :
  wiz . removeFile ( I11II1i )
 else : LogNotify ( "[COLOR %s]%s[/COLOR]" % ( oOOo0O00o , o0OOO ) , "[COLOR %s]AdvancedSettings.xml not found[/COLOR]" )
 if 5 - 5: OoooooooOO / I1I1i1 % i11IiIiiIIIII % I1111 * iiIIi1IiIi11 + iIii1I11I1II1
def I11iiI11iiI ( ) :
 notify . autoConfig ( )
 if 51 - 51: IIIi1i1I . iIii1I11I1II1 + I1111 * IiiIII111ii + i1IIi
def ooO0OOo0 ( ) :
 iIII11Iiii1 = 'http://whatismyipaddress.com/'
 if not wiz . workingURL ( iIII11Iiii1 ) : return 'Unknown' , 'Unknown' , 'Unknown'
 o0oo0 = wiz . openURL ( iIII11Iiii1 ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 if not 'Access Denied' in o0oo0 :
  OoO0OOoO0Oo0 = re . compile ( 'whatismyipaddress.com/ip/(.+?)"' ) . findall ( o0oo0 )
  oO00O = OoO0OOoO0Oo0 [ 0 ] if ( len ( OoO0OOoO0Oo0 ) > 0 ) else 'Unknown'
  II111IiiiI1 = re . compile ( '"font-size:14px;">(.+?)</td>' ) . findall ( o0oo0 )
  oooOO0oo0Oo00 = II111IiiiI1 [ 0 ] if ( len ( II111IiiiI1 ) > 0 ) else 'Unknown'
  oOoO = II111IiiiI1 [ 1 ] + ', ' + II111IiiiI1 [ 2 ] + ', ' + II111IiiiI1 [ 3 ] if ( len ( II111IiiiI1 ) > 2 ) else 'Unknown'
  return oO00O , oooOO0oo0Oo00 , oOoO
 else : return 'Unknown' , 'Unknown' , 'Unknown'
 if 13 - 13: o0o0Oo0oooo0 % OOoooooO
def O0OOOOo0 ( ) :
 OOooO0Oo00 = [ 'System.FriendlyName' ,
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
 iIIIIIIIiIII = [ ] ; iiIi = 0
 for o0oo0o00ooO00 in OOooO0Oo00 :
  IIiIiiI1i = wiz . getInfo ( o0oo0o00ooO00 )
  IIi = 0
  while IIiIiiI1i == "Busy" and IIi < 10 :
   IIiIiiI1i = wiz . getInfo ( o0oo0o00ooO00 ) ; IIi += 1 ; wiz . log ( "%s sleep %s" % ( o0oo0o00ooO00 , str ( IIi ) ) ) ; xbmc . sleep ( 200 )
  iIIIIIIIiIII . append ( IIiIiiI1i )
  iiIi += 1
 O0Oo = iIIIIIIIiIII [ 8 ] if 'Una' in iIIIIIIIiIII [ 8 ] else wiz . convertSize ( int ( float ( iIIIIIIIiIII [ 8 ] [ : - 8 ] ) ) * 1024 * 1024 )
 III11I1 = iIIIIIIIiIII [ 9 ] if 'Una' in iIIIIIIIiIII [ 9 ] else wiz . convertSize ( int ( float ( iIIIIIIIiIII [ 9 ] [ : - 8 ] ) ) * 1024 * 1024 )
 OOOO0o0O = iIIIIIIIiIII [ 10 ] if 'Una' in iIIIIIIIiIII [ 10 ] else wiz . convertSize ( int ( float ( iIIIIIIIiIII [ 10 ] [ : - 8 ] ) ) * 1024 * 1024 )
 iI111I = wiz . convertSize ( int ( float ( iIIIIIIIiIII [ 11 ] [ : - 2 ] ) ) * 1024 * 1024 )
 O00OoOoO = wiz . convertSize ( int ( float ( iIIIIIIIiIII [ 12 ] [ : - 2 ] ) ) * 1024 * 1024 )
 ooO0o0oo = wiz . convertSize ( int ( float ( iIIIIIIIiIII [ 13 ] [ : - 2 ] ) ) * 1024 * 1024 )
 o0O0OOo0oO , oooOO0oo0Oo00 , oOoO = ooO0OOo0 ( )
 if 42 - 42: II111iiii / O0 . iIii1I11I1II1 / O0 / I1111 / OoooooooOO
 ooiiI1ii = [ ] ; O0OooOO = [ ] ; i1i1 = [ ] ; o0oOoOo0 = [ ] ; III1IiI1i1i = [ ] ; o0OOOOOo0 = [ ] ; oooOoO = [ ]
 if 62 - 62: iii11iiII / II111iiii + o0o0Oo0oooo0 % OOoooooO / o0o0Oo0oooo0 + oO0
 IiI11I111 = glob . glob ( os . path . join ( O0O , '*/' ) )
 for Ooo000O00 in sorted ( IiI11I111 , key = lambda iiIi : iiIi ) :
  i1iI1Iiii1I = os . path . split ( Ooo000O00 [ : - 1 ] ) [ 1 ]
  if i1iI1Iiii1I == 'packages' : continue
  I1iII = os . path . join ( Ooo000O00 , 'addon.xml' )
  if os . path . exists ( I1iII ) :
   OO0OOoo0OOO = open ( I1iII )
   OOo00ooOoO0o = OO0OOoo0OOO . read ( )
   Iii1I1IIII = re . compile ( "<provides>(.+?)</provides>" ) . findall ( OOo00ooOoO0o )
   if len ( Iii1I1IIII ) == 0 :
    if i1iI1Iiii1I . startswith ( 'skin' ) : oooOoO . append ( i1iI1Iiii1I )
    if i1iI1Iiii1I . startswith ( 'repo' ) : III1IiI1i1i . append ( i1iI1Iiii1I )
    else : o0OOOOOo0 . append ( i1iI1Iiii1I )
   elif not ( Iii1I1IIII [ 0 ] ) . find ( 'executable' ) == - 1 : o0oOoOo0 . append ( i1iI1Iiii1I )
   elif not ( Iii1I1IIII [ 0 ] ) . find ( 'video' ) == - 1 : i1i1 . append ( i1iI1Iiii1I )
   elif not ( Iii1I1IIII [ 0 ] ) . find ( 'audio' ) == - 1 : O0OooOO . append ( i1iI1Iiii1I )
   elif not ( Iii1I1IIII [ 0 ] ) . find ( 'image' ) == - 1 : ooiiI1ii . append ( i1iI1Iiii1I )
   if 57 - 57: O0 - O0 . oO0 / I1I1i1 / IiiIII111ii
 iiiii1II ( '[B]Media Center Info:[/B]' , '' , icon = IiIi11iI , themeit = oooOo0OOOoo0 )
 iiiii1II ( '[COLOR %s]Name:[/COLOR] [COLOR %s]%s[/COLOR]' % ( oOOo0O00o , iIiIi11 , iIIIIIIIiIII [ 0 ] ) , '' , icon = IiIi11iI , themeit = OOoO )
 iiiii1II ( '[COLOR %s]Version:[/COLOR] [COLOR %s]%s[/COLOR]' % ( oOOo0O00o , iIiIi11 , iIIIIIIIiIII [ 1 ] ) , '' , icon = IiIi11iI , themeit = OOoO )
 iiiii1II ( '[COLOR %s]Platform:[/COLOR] [COLOR %s]%s[/COLOR]' % ( oOOo0O00o , iIiIi11 , wiz . platform ( ) . title ( ) ) , '' , icon = IiIi11iI , themeit = OOoO )
 iiiii1II ( '[COLOR %s]CPU Usage:[/COLOR] [COLOR %s]%s[/COLOR]' % ( oOOo0O00o , iIiIi11 , iIIIIIIIiIII [ 2 ] ) , '' , icon = IiIi11iI , themeit = OOoO )
 iiiii1II ( '[COLOR %s]Screen Mode:[/COLOR] [COLOR %s]%s[/COLOR]' % ( oOOo0O00o , iIiIi11 , iIIIIIIIiIII [ 3 ] ) , '' , icon = IiIi11iI , themeit = OOoO )
 if 20 - 20: iii11iiII * II111iiii - o0o0Oo0oooo0 - IIIi1i1I * OO00O0O0O00Oo
 iiiii1II ( '[B]Uptime:[/B]' , '' , icon = IiIi11iI , themeit = oooOo0OOOoo0 )
 iiiii1II ( '[COLOR %s]Current Uptime:[/COLOR] [COLOR %s]%s[/COLOR]' % ( oOOo0O00o , iIiIi11 , iIIIIIIIiIII [ 6 ] ) , '' , icon = IiIi11iI , themeit = oooOo0OOOoo0 )
 iiiii1II ( '[COLOR %s]Total Uptime:[/COLOR] [COLOR %s]%s[/COLOR]' % ( oOOo0O00o , iIiIi11 , iIIIIIIIiIII [ 7 ] ) , '' , icon = IiIi11iI , themeit = oooOo0OOOoo0 )
 if 6 - 6: OOoooooO + iii11iiII / Ooo0O + i1Ii % II111iiii / I1111
 iiiii1II ( '[B]Local Storage:[/B]' , '' , icon = IiIi11iI , themeit = oooOo0OOOoo0 )
 iiiii1II ( '[COLOR %s]Used Storage:[/COLOR] [COLOR %s]%s[/COLOR]' % ( oOOo0O00o , iIiIi11 , O0Oo ) , '' , icon = IiIi11iI , themeit = oooOo0OOOoo0 )
 iiiii1II ( '[COLOR %s]Free Storage:[/COLOR] [COLOR %s]%s[/COLOR]' % ( oOOo0O00o , iIiIi11 , III11I1 ) , '' , icon = IiIi11iI , themeit = oooOo0OOOoo0 )
 iiiii1II ( '[COLOR %s]Total Storage:[/COLOR] [COLOR %s]%s[/COLOR]' % ( oOOo0O00o , iIiIi11 , OOOO0o0O ) , '' , icon = IiIi11iI , themeit = oooOo0OOOoo0 )
 if 45 - 45: OoooooooOO
 iiiii1II ( '[B]Ram Usage:[/B]' , '' , icon = IiIi11iI , themeit = oooOo0OOOoo0 )
 iiiii1II ( '[COLOR %s]Used Memory:[/COLOR] [COLOR %s]%s[/COLOR]' % ( oOOo0O00o , iIiIi11 , iI111I ) , '' , icon = IiIi11iI , themeit = oooOo0OOOoo0 )
 iiiii1II ( '[COLOR %s]Free Memory:[/COLOR] [COLOR %s]%s[/COLOR]' % ( oOOo0O00o , iIiIi11 , O00OoOoO ) , '' , icon = IiIi11iI , themeit = oooOo0OOOoo0 )
 iiiii1II ( '[COLOR %s]Total Memory:[/COLOR] [COLOR %s]%s[/COLOR]' % ( oOOo0O00o , iIiIi11 , ooO0o0oo ) , '' , icon = IiIi11iI , themeit = oooOo0OOOoo0 )
 if 9 - 9: i11IiIiiIIIII . I1111 * i1IIi . OoooooooOO
 iiiii1II ( '[B]Network:[/B]' , '' , icon = IiIi11iI , themeit = oooOo0OOOoo0 )
 iiiii1II ( '[COLOR %s]Local IP:[/COLOR] [COLOR %s]%s[/COLOR]' % ( oOOo0O00o , iIiIi11 , iIIIIIIIiIII [ 4 ] ) , '' , icon = IiIi11iI , themeit = oooOo0OOOoo0 )
 iiiii1II ( '[COLOR %s]External IP:[/COLOR] [COLOR %s]%s[/COLOR]' % ( oOOo0O00o , iIiIi11 , o0O0OOo0oO ) , '' , icon = IiIi11iI , themeit = oooOo0OOOoo0 )
 iiiii1II ( '[COLOR %s]Provider:[/COLOR] [COLOR %s]%s[/COLOR]' % ( oOOo0O00o , iIiIi11 , oooOO0oo0Oo00 ) , '' , icon = IiIi11iI , themeit = oooOo0OOOoo0 )
 iiiii1II ( '[COLOR %s]Location:[/COLOR] [COLOR %s]%s[/COLOR]' % ( oOOo0O00o , iIiIi11 , oOoO ) , '' , icon = IiIi11iI , themeit = oooOo0OOOoo0 )
 iiiii1II ( '[COLOR %s]MacAddress:[/COLOR] [COLOR %s]%s[/COLOR]' % ( oOOo0O00o , iIiIi11 , iIIIIIIIiIII [ 5 ] ) , '' , icon = IiIi11iI , themeit = oooOo0OOOoo0 )
 if 32 - 32: o0o0Oo0oooo0 . oO0 % ooOo - II111iiii
 iiI111 = len ( ooiiI1ii ) + len ( O0OooOO ) + len ( i1i1 ) + len ( o0oOoOo0 ) + len ( o0OOOOOo0 ) + len ( oooOoO ) + len ( III1IiI1i1i )
 iiiii1II ( '[B]Addons([COLOR %s]%s[/COLOR]):[/B]' % ( oOOo0O00o , iiI111 ) , '' , icon = IiIi11iI , themeit = oooOo0OOOoo0 )
 iiiii1II ( '[COLOR %s]Video Addons:[/COLOR] [COLOR %s]%s[/COLOR]' % ( oOOo0O00o , iIiIi11 , str ( len ( i1i1 ) ) ) , '' , icon = IiIi11iI , themeit = oooOo0OOOoo0 )
 iiiii1II ( '[COLOR %s]Program Addons:[/COLOR] [COLOR %s]%s[/COLOR]' % ( oOOo0O00o , iIiIi11 , str ( len ( o0oOoOo0 ) ) ) , '' , icon = IiIi11iI , themeit = oooOo0OOOoo0 )
 iiiii1II ( '[COLOR %s]Music Addons:[/COLOR] [COLOR %s]%s[/COLOR]' % ( oOOo0O00o , iIiIi11 , str ( len ( O0OooOO ) ) ) , '' , icon = IiIi11iI , themeit = oooOo0OOOoo0 )
 iiiii1II ( '[COLOR %s]Picture Addons:[/COLOR] [COLOR %s]%s[/COLOR]' % ( oOOo0O00o , iIiIi11 , str ( len ( ooiiI1ii ) ) ) , '' , icon = IiIi11iI , themeit = oooOo0OOOoo0 )
 iiiii1II ( '[COLOR %s]Repositories:[/COLOR] [COLOR %s]%s[/COLOR]' % ( oOOo0O00o , iIiIi11 , str ( len ( III1IiI1i1i ) ) ) , '' , icon = IiIi11iI , themeit = oooOo0OOOoo0 )
 iiiii1II ( '[COLOR %s]Skins:[/COLOR] [COLOR %s]%s[/COLOR]' % ( oOOo0O00o , iIiIi11 , str ( len ( oooOoO ) ) ) , '' , icon = IiIi11iI , themeit = oooOo0OOOoo0 )
 iiiii1II ( '[COLOR %s]Scripts/Modules:[/COLOR] [COLOR %s]%s[/COLOR]' % ( oOOo0O00o , iIiIi11 , str ( len ( o0OOOOOo0 ) ) ) , '' , icon = IiIi11iI , themeit = oooOo0OOOoo0 )
 if 62 - 62: oO0 - O0 . ooOo . O0 * iIii1I11I1II1
def oOo0O ( ) :
 i1II = '[COLOR green]ON[/COLOR]' ; IiiIi11Ii1iI1 = '[COLOR red]OFF[/COLOR]'
 i1iOO = 'true' if o0O0OOO0Ooo == 'true' else 'false'
 OO00OoooO = 'true' if iiIiII1 == 'true' else 'false'
 IIIi = 'true' if OOO00O0O == 'true' else 'false'
 Ii1iiI1 = 'true' if ooOOoooooo == 'true' else 'false'
 o0ooOOoO0oO0 = 'true' if O0i1II1Iiii1I11 == 'true' else 'false'
 oo00I1IiI1IIiI = 'true' if II1I == 'true' else 'false'
 oooo = 'true' if IiIIIi1iIi == 'true' else 'false'
 III1IiI1i1i = 'true' if IIII == 'true' else 'false'
 super = 'true' if iiIiI == 'true' else 'false'
 o0o0oo0Ooo = 'true' if o00oooO0Oo == 'true' else 'false'
 if 12 - 12: oO0 / IiiIII111ii
 oo00O00oO000o ( 'Keep Trakt Data' , 'trakt' , icon = iIIii , themeit = OOOiiiiI )
 oo00O00oO000o ( 'Keep Real Debrid' , 'realdebrid' , icon = o00O0O , themeit = OOOiiiiI )
 oo00O00oO000o ( 'Keep Login Info' , 'login' , icon = ii1iii1i , themeit = OOOiiiiI )
 iiiii1II ( 'Import Save Data' , 'managedata' , 'import' , icon = I1111i , themeit = OOOiiiiI )
 iiiii1II ( 'Export Save Data' , 'managedata' , 'export' , icon = I1111i , themeit = OOOiiiiI )
 iiiii1II ( '- Click to toggle settings -' , '' , themeit = OOoO )
 iiiii1II ( 'Save Trakt: %s' % i1iOO . replace ( 'true' , i1II ) . replace ( 'false' , IiiIi11Ii1iI1 ) , 'togglesetting' , 'keeptrakt' , icon = iIIii , themeit = OOOiiiiI )
 iiiii1II ( 'Save Real Debrid: %s' % OO00OoooO . replace ( 'true' , i1II ) . replace ( 'false' , IiiIi11Ii1iI1 ) , 'togglesetting' , 'keepdebrid' , icon = o00O0O , themeit = OOOiiiiI )
 iiiii1II ( 'Save Login Info: %s' % IIIi . replace ( 'true' , i1II ) . replace ( 'false' , IiiIi11Ii1iI1 ) , 'togglesetting' , 'keeplogin' , icon = ii1iii1i , themeit = OOOiiiiI )
 iiiii1II ( 'Keep \'Sources.xml\': %s' % Ii1iiI1 . replace ( 'true' , i1II ) . replace ( 'false' , IiiIi11Ii1iI1 ) , 'togglesetting' , 'keepsources' , icon = I1111i , themeit = OOOiiiiI )
 iiiii1II ( 'Keep \'Profiles.xml\': %s' % oo00I1IiI1IIiI . replace ( 'true' , i1II ) . replace ( 'false' , IiiIi11Ii1iI1 ) , 'togglesetting' , 'keepprofiles' , icon = I1111i , themeit = OOOiiiiI )
 iiiii1II ( 'Keep \'Advancedsettings.xml\': %s' % o0ooOOoO0oO0 . replace ( 'true' , i1II ) . replace ( 'false' , IiiIi11Ii1iI1 ) , 'togglesetting' , 'keepadvanced' , icon = I1111i , themeit = OOOiiiiI )
 iiiii1II ( 'Keep \'Favourites.xml\': %s' % oooo . replace ( 'true' , i1II ) . replace ( 'false' , IiiIi11Ii1iI1 ) , 'togglesetting' , 'keepfavourites' , icon = I1111i , themeit = OOOiiiiI )
 iiiii1II ( 'Keep Super Favourites: %s' % super . replace ( 'true' , i1II ) . replace ( 'false' , IiiIi11Ii1iI1 ) , 'togglesetting' , 'keepsuper' , icon = I1111i , themeit = OOOiiiiI )
 iiiii1II ( 'Keep Installed Repo\'s: %s' % III1IiI1i1i . replace ( 'true' , i1II ) . replace ( 'false' , IiiIi11Ii1iI1 ) , 'togglesetting' , 'keeprepos' , icon = I1111i , themeit = OOOiiiiI )
 iiiii1II ( 'Keep My \'WhiteList\': %s' % o0o0oo0Ooo . replace ( 'true' , i1II ) . replace ( 'false' , IiiIi11Ii1iI1 ) , 'togglesetting' , 'keepwhitelist' , icon = I1111i , themeit = OOOiiiiI )
 if o0o0oo0Ooo == 'true' :
  iiiii1II ( 'Edit My Whitelist' , 'whitelist' , 'edit' , icon = I1111i , themeit = OOOiiiiI )
  iiiii1II ( 'View My Whitelist' , 'whitelist' , 'view' , icon = I1111i , themeit = OOOiiiiI )
  iiiii1II ( 'Clear My Whitelist' , 'whitelist' , 'clear' , icon = I1111i , themeit = OOOiiiiI )
  iiiii1II ( 'Import My Whitelist' , 'whitelist' , 'import' , icon = I1111i , themeit = OOOiiiiI )
  iiiii1II ( 'Export My Whitelist' , 'whitelist' , 'export' , icon = I1111i , themeit = OOOiiiiI )
 iIi1 ( 'files' , 'viewType' )
 if 5 - 5: OoooooooOO
def IIIii11i1I ( ) :
 i1iOO = '[COLOR green]ON[/COLOR]' if o0O0OOO0Ooo == 'true' else '[COLOR red]OFF[/COLOR]'
 ooo0O00000oo0 = str ( O000OOo00oo ) if not O000OOo00oo == '' else 'Trakt hasnt been saved yet.'
 iiiii1II ( '[I]Register FREE Account at http://trakt.tv[/I]' , '' , icon = iIIii , themeit = OOoO )
 iiiii1II ( 'Save Trakt Data: %s' % i1iOO , 'togglesetting' , 'keeptrakt' , icon = iIIii , themeit = OOoO )
 if o0O0OOO0Ooo == 'true' : iiiii1II ( 'Last Save: %s' % str ( ooo0O00000oo0 ) , '' , icon = iIIii , themeit = OOoO )
 if O0O0ooOOO == 'No' : iiiii1II ( wiz . sep ( ) , '' , icon = iIIii , themeit = OOoO )
 if 80 - 80: Ooo0O + oO0
 for i1iOO in traktit . ORDER :
  oO0o00oOOooO0 = oOOOoo00 [ i1iOO ] [ 'name' ]
  oOIii11111iiI = oOOOoo00 [ i1iOO ] [ 'path' ]
  o0OOOOoO = oOOOoo00 [ i1iOO ] [ 'saved' ]
  file = oOOOoo00 [ i1iOO ] [ 'file' ]
  OoO0Ooo = wiz . getS ( o0OOOOoO )
  Ii1I1I = traktit . traktUser ( i1iOO )
  i1i1i1I = oOOOoo00 [ i1iOO ] [ 'icon' ] if os . path . exists ( oOIii11111iiI ) else iIIii
  oOoo000 = oOOOoo00 [ i1iOO ] [ 'fanart' ] if os . path . exists ( oOIii11111iiI ) else OOO00
  iI1IIIii = I1i11ii11 ( 'saveaddon' , 'Trakt' , i1iOO )
  oOOoOOO0oOoo = I1i11ii11 ( 'save' , 'Trakt' , i1iOO )
  iI1IIIii . append ( ( oooOo0OOOoo0 % '%s Settings' % oO0o00oOOooO0 , 'RunPlugin(plugin://%s/?mode=opensettings&name=%s&url=trakt)' % ( IiII1IiiIiI1 , i1iOO ) ) )
  if 65 - 65: iiIIi1IiIi11 . IIIi1i1I - IiiIII111ii
  iiiii1II ( '[+]-> %s' % oO0o00oOOooO0 , '' , icon = i1i1i1I , fanart = oOoo000 , themeit = OOoO )
  if not os . path . exists ( oOIii11111iiI ) : iiiii1II ( '[COLOR red]Addon Data: Not Installed[/COLOR]' , '' , icon = i1i1i1I , fanart = oOoo000 , menu = iI1IIIii )
  elif not Ii1I1I : iiiii1II ( '[COLOR red]Addon Data: Not Registered[/COLOR]' , 'authtrakt' , i1iOO , icon = i1i1i1I , fanart = oOoo000 , menu = iI1IIIii )
  else : iiiii1II ( '[COLOR green]Addon Data: %s[/COLOR]' % Ii1I1I , 'authtrakt' , i1iOO , icon = i1i1i1I , fanart = oOoo000 , menu = iI1IIIii )
  if OoO0Ooo == "" :
   if os . path . exists ( file ) : iiiii1II ( '[COLOR red]Saved Data: Save File Found(Import Data)[/COLOR]' , 'importtrakt' , i1iOO , icon = i1i1i1I , fanart = oOoo000 , menu = oOOoOOO0oOoo )
   else : iiiii1II ( '[COLOR red]Saved Data: Not Saved[/COLOR]' , 'savetrakt' , i1iOO , icon = i1i1i1I , fanart = oOoo000 , menu = oOOoOOO0oOoo )
  else : iiiii1II ( '[COLOR green]Saved Data: %s[/COLOR]' % OoO0Ooo , '' , icon = i1i1i1I , fanart = oOoo000 , menu = oOOoOOO0oOoo )
  if 93 - 93: O0
 if O0O0ooOOO == 'No' : iiiii1II ( wiz . sep ( ) , '' , themeit = OOoO )
 iiiii1II ( 'Save All Trakt Data' , 'savetrakt' , 'all' , icon = iIIii , themeit = OOoO )
 iiiii1II ( 'Recover All Saved Trakt Data' , 'restoretrakt' , 'all' , icon = iIIii , themeit = OOoO )
 iiiii1II ( 'Import Trakt Data' , 'importtrakt' , 'all' , icon = iIIii , themeit = OOoO )
 iiiii1II ( 'Clear All Saved Trakt Data' , 'cleartrakt' , 'all' , icon = iIIii , themeit = OOoO )
 iiiii1II ( 'Clear All Addon Data' , 'addontrakt' , 'all' , icon = iIIii , themeit = OOoO )
 iIi1 ( 'files' , 'viewType' )
 if 4 - 4: ooOo / ooOo
def O0000 ( ) :
 OO00OoooO = '[COLOR green]ON[/COLOR]' if iiIiII1 == 'true' else '[COLOR red]OFF[/COLOR]'
 ooo0O00000oo0 = str ( oo0OOo ) if not oo0OOo == '' else 'Real Debrid hasnt been saved yet.'
 iiiii1II ( '[I]http://real-debrid.com is a PAID service.[/I]' , '' , icon = o00O0O , themeit = OOoO )
 iiiii1II ( 'Save Real Debrid Data: %s' % OO00OoooO , 'togglesetting' , 'keepdebrid' , icon = o00O0O , themeit = OOoO )
 if iiIiII1 == 'true' : iiiii1II ( 'Last Save: %s' % str ( ooo0O00000oo0 ) , '' , icon = o00O0O , themeit = OOoO )
 if O0O0ooOOO == 'No' : iiiii1II ( wiz . sep ( ) , '' , icon = o00O0O , themeit = OOoO )
 if 74 - 74: II111iiii . IiiIII111ii % I1111 + iii11iiII - I1I1i1 + IiiIII111ii
 for i1IIOO0oo00oOO in debridit . ORDER :
  oO0o00oOOooO0 = iiIiIIIiiI [ i1IIOO0oo00oOO ] [ 'name' ]
  oOIii11111iiI = iiIiIIIiiI [ i1IIOO0oo00oOO ] [ 'path' ]
  o0OOOOoO = iiIiIIIiiI [ i1IIOO0oo00oOO ] [ 'saved' ]
  file = iiIiIIIiiI [ i1IIOO0oo00oOO ] [ 'file' ]
  OoO0Ooo = wiz . getS ( o0OOOOoO )
  Ii1I1I = debridit . debridUser ( i1IIOO0oo00oOO )
  i1i1i1I = iiIiIIIiiI [ i1IIOO0oo00oOO ] [ 'icon' ] if os . path . exists ( oOIii11111iiI ) else o00O0O
  oOoo000 = iiIiIIIiiI [ i1IIOO0oo00oOO ] [ 'fanart' ] if os . path . exists ( oOIii11111iiI ) else OOO00
  iI1IIIii = I1i11ii11 ( 'saveaddon' , 'Debrid' , i1IIOO0oo00oOO )
  oOOoOOO0oOoo = I1i11ii11 ( 'save' , 'Debrid' , i1IIOO0oo00oOO )
  iI1IIIii . append ( ( oooOo0OOOoo0 % '%s Settings' % oO0o00oOOooO0 , 'RunPlugin(plugin://%s/?mode=opensettings&name=%s&url=debrid)' % ( IiII1IiiIiI1 , i1IIOO0oo00oOO ) ) )
  if 38 - 38: OO00O0O0O00Oo . iiIIi1IiIi11 . ooOo * I1111
  iiiii1II ( '[+]-> %s' % oO0o00oOOooO0 , '' , icon = i1i1i1I , fanart = oOoo000 , themeit = OOoO )
  if not os . path . exists ( oOIii11111iiI ) : iiiii1II ( '[COLOR red]Addon Data: Not Installed[/COLOR]' , '' , icon = i1i1i1I , fanart = oOoo000 , menu = iI1IIIii )
  elif not Ii1I1I : iiiii1II ( '[COLOR red]Addon Data: Not Registered[/COLOR]' , 'authdebrid' , i1IIOO0oo00oOO , icon = i1i1i1I , fanart = oOoo000 , menu = iI1IIIii )
  else : iiiii1II ( '[COLOR green]Addon Data: %s[/COLOR]' % Ii1I1I , 'authdebrid' , i1IIOO0oo00oOO , icon = i1i1i1I , fanart = oOoo000 , menu = iI1IIIii )
  if OoO0Ooo == "" :
   if os . path . exists ( file ) : iiiii1II ( '[COLOR red]Saved Data: Save File Found(Import Data)[/COLOR]' , 'importdebrid' , i1IIOO0oo00oOO , icon = i1i1i1I , fanart = oOoo000 , menu = oOOoOOO0oOoo )
   else : iiiii1II ( '[COLOR red]Saved Data: Not Saved[/COLOR]' , 'savedebrid' , i1IIOO0oo00oOO , icon = i1i1i1I , fanart = oOoo000 , menu = oOOoOOO0oOoo )
  else : iiiii1II ( '[COLOR green]Saved Data: %s[/COLOR]' % OoO0Ooo , '' , icon = i1i1i1I , fanart = oOoo000 , menu = oOOoOOO0oOoo )
  if 69 - 69: I1I1i1 % i11iIiiIii / IiiIII111ii
 if O0O0ooOOO == 'No' : iiiii1II ( wiz . sep ( ) , '' , themeit = OOoO )
 iiiii1II ( 'Save All Real Debrid Data' , 'savedebrid' , 'all' , icon = o00O0O , themeit = OOoO )
 iiiii1II ( 'Recover All Saved Real Debrid Data' , 'restoredebrid' , 'all' , icon = o00O0O , themeit = OOoO )
 iiiii1II ( 'Import Real Debrid Data' , 'importdebrid' , 'all' , icon = o00O0O , themeit = OOoO )
 iiiii1II ( 'Clear All Saved Real Debrid Data' , 'cleardebrid' , 'all' , icon = o00O0O , themeit = OOoO )
 iiiii1II ( 'Clear All Addon Data' , 'addondebrid' , 'all' , icon = o00O0O , themeit = OOoO )
 iIi1 ( 'files' , 'viewType' )
 if 93 - 93: OOoooooO
def II11iIIii ( ) :
 IIIi = '[COLOR green]ON[/COLOR]' if OOO00O0O == 'true' else '[COLOR red]OFF[/COLOR]'
 ooo0O00000oo0 = str ( ooOOO00Ooo ) if not ooOOO00Ooo == '' else 'Login data hasnt been saved yet.'
 iiiii1II ( '[I]Several of these addons are PAID services.[/I]' , '' , icon = ii1iii1i , themeit = OOoO )
 iiiii1II ( 'Save Login Data: %s' % IIIi , 'togglesetting' , 'keeplogin' , icon = ii1iii1i , themeit = OOoO )
 if OOO00O0O == 'true' : iiiii1II ( 'Last Save: %s' % str ( ooo0O00000oo0 ) , '' , icon = ii1iii1i , themeit = OOoO )
 if O0O0ooOOO == 'No' : iiiii1II ( wiz . sep ( ) , '' , icon = ii1iii1i , themeit = OOoO )
 if 57 - 57: O0 * oO0 . i11iIiiIii
 for IIIi in loginit . ORDER :
  oO0o00oOOooO0 = iiI1IIIi [ IIIi ] [ 'name' ]
  oOIii11111iiI = iiI1IIIi [ IIIi ] [ 'path' ]
  o0OOOOoO = iiI1IIIi [ IIIi ] [ 'saved' ]
  file = iiI1IIIi [ IIIi ] [ 'file' ]
  OoO0Ooo = wiz . getS ( o0OOOOoO )
  Ii1I1I = loginit . loginUser ( IIIi )
  i1i1i1I = iiI1IIIi [ IIIi ] [ 'icon' ] if os . path . exists ( oOIii11111iiI ) else ii1iii1i
  oOoo000 = iiI1IIIi [ IIIi ] [ 'fanart' ] if os . path . exists ( oOIii11111iiI ) else OOO00
  iI1IIIii = I1i11ii11 ( 'saveaddon' , 'Login' , IIIi )
  oOOoOOO0oOoo = I1i11ii11 ( 'save' , 'Login' , IIIi )
  iI1IIIii . append ( ( oooOo0OOOoo0 % '%s Settings' % oO0o00oOOooO0 , 'RunPlugin(plugin://%s/?mode=opensettings&name=%s&url=login)' % ( IiII1IiiIiI1 , IIIi ) ) )
  if 69 - 69: O0 / II111iiii * i1IIi
  iiiii1II ( '[+]-> %s' % oO0o00oOOooO0 , '' , icon = i1i1i1I , fanart = oOoo000 , themeit = OOoO )
  if not os . path . exists ( oOIii11111iiI ) : iiiii1II ( '[COLOR red]Addon Data: Not Installed[/COLOR]' , '' , icon = i1i1i1I , fanart = oOoo000 , menu = iI1IIIii )
  elif not Ii1I1I : iiiii1II ( '[COLOR red]Addon Data: Not Registered[/COLOR]' , 'authlogin' , IIIi , icon = i1i1i1I , fanart = oOoo000 , menu = iI1IIIii )
  else : iiiii1II ( '[COLOR green]Addon Data: %s[/COLOR]' % Ii1I1I , 'authlogin' , IIIi , icon = i1i1i1I , fanart = oOoo000 , menu = iI1IIIii )
  if OoO0Ooo == "" :
   if os . path . exists ( file ) : iiiii1II ( '[COLOR red]Saved Data: Save File Found(Import Data)[/COLOR]' , 'importlogin' , IIIi , icon = i1i1i1I , fanart = oOoo000 , menu = oOOoOOO0oOoo )
   else : iiiii1II ( '[COLOR red]Saved Data: Not Saved[/COLOR]' , 'savelogin' , IIIi , icon = i1i1i1I , fanart = oOoo000 , menu = oOOoOOO0oOoo )
  else : iiiii1II ( '[COLOR green]Saved Data: %s[/COLOR]' % OoO0Ooo , '' , icon = i1i1i1I , fanart = oOoo000 , menu = oOOoOOO0oOoo )
  if 66 - 66: O0
 if O0O0ooOOO == 'No' : iiiii1II ( wiz . sep ( ) , '' , themeit = OOoO )
 iiiii1II ( 'Save All Login Data' , 'savelogin' , 'all' , icon = ii1iii1i , themeit = OOoO )
 iiiii1II ( 'Recover All Saved Login Data' , 'restorelogin' , 'all' , icon = ii1iii1i , themeit = OOoO )
 iiiii1II ( 'Import Login Data' , 'importlogin' , 'all' , icon = ii1iii1i , themeit = OOoO )
 iiiii1II ( 'Clear All Saved Login Data' , 'clearlogin' , 'all' , icon = ii1iii1i , themeit = OOoO )
 iiiii1II ( 'Clear All Addon Data' , 'addonlogin' , 'all' , icon = ii1iii1i , themeit = OOoO )
 iIi1 ( 'files' , 'viewType' )
 if 52 - 52: I1111 * OoooooooOO
def Ii11iiI ( ) :
 if o0OIiII < 17 :
  o0OO0oooo = os . path . join ( OOOO , wiz . latestDB ( 'Addons' ) )
  try :
   os . remove ( o0OO0oooo )
  except Exception , I111I11I111 :
   wiz . log ( "Unable to remove %s, Purging DB" % o0OO0oooo )
   wiz . purgeDb ( o0OO0oooo )
 else :
  xbmc . log ( "Requested Addons.db be removed but doesnt work in Kod17" )
  if 40 - 40: OO00O0O0O00Oo - o0o0Oo0oooo0 * i11IiIiiIIIII - i1Ii / o0o0Oo0oooo0
def OO0oo ( ) :
 IiI11I111 = glob . glob ( os . path . join ( O0O , '*/' ) )
 O0oOO0o = [ ] ; oo000oO0O = [ ]
 for Ooo000O00 in sorted ( IiI11I111 , key = lambda iiIi : iiIi ) :
  i1iI1Iiii1I = os . path . split ( Ooo000O00 [ : - 1 ] ) [ 1 ]
  if i1iI1Iiii1I in Iii1I1I11iiI1 : continue
  elif i1iI1Iiii1I in OOo0 : continue
  elif i1iI1Iiii1I == 'packages' : continue
  I1iII = os . path . join ( Ooo000O00 , 'addon.xml' )
  if os . path . exists ( I1iII ) :
   OO0OOoo0OOO = open ( I1iII )
   OOo00ooOoO0o = OO0OOoo0OOO . read ( )
   O0Oo0o000oO = wiz . parseDOM ( OOo00ooOoO0o , 'addon' , ret = 'id' )
   if 100 - 100: iIii1I11I1II1
   ooOOo00 = i1iI1Iiii1I if len ( O0Oo0o000oO ) == 0 else O0Oo0o000oO [ 0 ]
   try :
    Ii1iiIi1I11i = xbmcaddon . Addon ( id = ooOOo00 )
    O0oOO0o . append ( Ii1iiIi1I11i . getAddonInfo ( 'name' ) )
    oo000oO0O . append ( ooOOo00 )
   except :
    pass
 if len ( O0oOO0o ) == 0 :
  wiz . LogNotify ( "[COLOR %s]%s[/COLOR]" % ( oOOo0O00o , o0OOO ) , "[COLOR %s]No Addons To Remove[/COLOR]" % iIiIi11 )
  return
 if o0OIiII > 16 :
  I11o0000o0Oo = iiIIIII1i1iI . multiselect ( "%s: Select the addons you wish to remove." % o0OOO , O0oOO0o )
 else :
  I11o0000o0Oo = [ ] ; i1I1IiI1ii = 0
  IIii1i1IiIi1 = [ "-- Click here to Continue --" ] + O0oOO0o
  while not i1I1IiI1ii == - 1 :
   i1I1IiI1ii = iiIIIII1i1iI . select ( "%s: Select the addons you wish to remove." % o0OOO , IIii1i1IiIi1 )
   if i1I1IiI1ii == - 1 : break
   elif i1I1IiI1ii == 0 : break
   else :
    IiiiiIIi11iI = ( i1I1IiI1ii - 1 )
    if IiiiiIIi11iI in I11o0000o0Oo :
     I11o0000o0Oo . remove ( IiiiiIIi11iI )
     IIii1i1IiIi1 [ i1I1IiI1ii ] = O0oOO0o [ IiiiiIIi11iI ]
    else :
     I11o0000o0Oo . append ( IiiiiIIi11iI )
     IIii1i1IiIi1 [ i1I1IiI1ii ] = "[B][COLOR %s]%s[/COLOR][/B]" % ( oOOo0O00o , O0oOO0o [ IiiiiIIi11iI ] )
 if I11o0000o0Oo == None : return
 if len ( I11o0000o0Oo ) > 0 :
  wiz . addonUpdates ( 'set' )
  for ii111I11Ii in I11o0000o0Oo :
   i11IiiI1Ii1 ( oo000oO0O [ ii111I11Ii ] , O0oOO0o [ ii111I11Ii ] , True )
   if 23 - 23: iiIIi1IiIi11 % OoooooooOO / iIii1I11I1II1 + oO0 / i1IIi / I1I1i1
  xbmc . sleep ( 500 )
  if 94 - 94: i1IIi
  if I11i1I1I == 1 : iiIIi1 = 1
  elif I11i1I1I == 2 : iiIIi1 = 0
  else : iiIIi1 = iiIIIII1i1iI . yesno ( o0OOO , "[COLOR %s]Would you like to [COLOR %s]Force close[/COLOR] kodi or [COLOR %s]Reload Profile[/COLOR]?[/COLOR]" % ( iIiIi11 , oOOo0O00o , oOOo0O00o ) , yeslabel = "[B][COLOR green]Reload Profile[/COLOR][/B]" , nolabel = "[B][COLOR red]Force Close[/COLOR][/B]" )
  if iiIIi1 == 1 : wiz . reloadFix ( 'remove addon' )
  else : wiz . addonUpdates ( 'reset' ) ; wiz . killxbmc ( True )
  if 65 - 65: i1IIi . oO0 / OOoooooO
def I1i1I11111iI1 ( ) :
 if os . path . exists ( ooOOOo0oo0O0 ) :
  iiiii1II ( '[COLOR red][B][REMOVE][/B][/COLOR] All Addon_Data' , 'removedata' , 'all' , themeit = oooOo0OOOoo0 )
  iiiii1II ( '[COLOR red][B][REMOVE][/B][/COLOR] All Addon_Data for Uninstalled Addons' , 'removedata' , 'uninstalled' , themeit = oooOo0OOOoo0 )
  iiiii1II ( '[COLOR red][B][REMOVE][/B][/COLOR] All Empty Folders in Addon_Data' , 'removedata' , 'empty' , themeit = oooOo0OOOoo0 )
  iiiii1II ( '[COLOR red][B][REMOVE][/B][/COLOR] %s Addon_Data' % o0OOO , 'resetaddon' , themeit = oooOo0OOOoo0 )
  if O0O0ooOOO == 'No' : iiiii1II ( wiz . sep ( ) , '' , themeit = OOoO )
  IiI11I111 = glob . glob ( os . path . join ( ooOOOo0oo0O0 , '*/' ) )
  for Ooo000O00 in sorted ( IiI11I111 , key = lambda iiIi : iiIi ) :
   i1iI1Iiii1I = Ooo000O00 . replace ( ooOOOo0oo0O0 , '' ) . replace ( '\\' , '' ) . replace ( '/' , '' )
   i1i1i1I = os . path . join ( Ooo000O00 . replace ( ooOOOo0oo0O0 , O0O ) , 'icon.png' )
   oOoo000 = os . path . join ( Ooo000O00 . replace ( ooOOOo0oo0O0 , O0O ) , 'fanart.png' )
   IIIIIIi = i1iI1Iiii1I
   OO0o = { 'audio.' : '[COLOR orange][AUDIO] [/COLOR]' , 'metadata.' : '[COLOR cyan][METADATA] [/COLOR]' , 'module.' : '[COLOR orange][MODULE] [/COLOR]' , 'plugin.' : '[COLOR blue][PLUGIN] [/COLOR]' , 'program.' : '[COLOR orange][PROGRAM] [/COLOR]' , 'repository.' : '[COLOR gold][REPO] [/COLOR]' , 'script.' : '[COLOR green][SCRIPT] [/COLOR]' , 'service.' : '[COLOR green][SERVICE] [/COLOR]' , 'skin.' : '[COLOR dodgerblue][SKIN] [/COLOR]' , 'video.' : '[COLOR orange][VIDEO] [/COLOR]' , 'weather.' : '[COLOR yellow][WEATHER] [/COLOR]' }
   for OoOoooo0O in OO0o :
    IIIIIIi = IIIIIIi . replace ( OoOoooo0O , OO0o [ OoOoooo0O ] )
   if i1iI1Iiii1I in Iii1I1I11iiI1 : IIIIIIi = '[COLOR green][B][PROTECTED][/B][/COLOR] %s' % IIIIIIi
   else : IIIIIIi = '[COLOR red][B][REMOVE][/B][/COLOR] %s' % IIIIIIi
   iiiii1II ( ' %s' % IIIIIIi , 'removedata' , i1iI1Iiii1I , icon = i1i1i1I , fanart = oOoo000 , themeit = oooOo0OOOoo0 )
 else :
  iiiii1II ( 'No Addon data folder found.' , '' , themeit = OOoO )
 iIi1 ( 'files' , 'viewType' )
 if 95 - 95: II111iiii / IiiIII111ii - OOoooooO - II111iiii - i11iIiiIii
def oO0O ( ) :
 iiiii1II ( "[I][B][COLOR red]!!Notice: Disabling Some Addons Can Cause Issues!![/COLOR][/B][/I]" , '' , icon = IiIi11iI )
 IiI11I111 = glob . glob ( os . path . join ( O0O , '*/' ) )
 iiIi = 0
 for Ooo000O00 in sorted ( IiI11I111 , key = lambda iiIi : iiIi ) :
  i1iI1Iiii1I = os . path . split ( Ooo000O00 [ : - 1 ] ) [ 1 ]
  if i1iI1Iiii1I in Iii1I1I11iiI1 : continue
  if i1iI1Iiii1I in OOo0 : continue
  IIIiIi1iiI = os . path . join ( Ooo000O00 , 'addon.xml' )
  if os . path . exists ( IIIiIi1iiI ) :
   iiIi += 1
   IiI11I111 = Ooo000O00 . replace ( O0O , '' ) [ 1 : - 1 ]
   OO0OOoo0OOO = open ( IIIiIi1iiI )
   OOo00ooOoO0o = OO0OOoo0OOO . read ( ) . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
   O0Oo0o000oO = wiz . parseDOM ( OOo00ooOoO0o , 'addon' , ret = 'id' )
   OoooO0o = wiz . parseDOM ( OOo00ooOoO0o , 'addon' , ret = 'name' )
   try :
    Ii11IiI = O0Oo0o000oO [ 0 ]
    oO0o00oOOooO0 = OoooO0o [ 0 ]
   except :
    continue
   try :
    Ii1iiIi1I11i = xbmcaddon . Addon ( id = Ii11IiI )
    Ii1iI111 = "[COLOR green][Enabled][/COLOR]"
    iI1o0 = "false"
   except :
    Ii1iI111 = "[COLOR red][Disabled][/COLOR]"
    iI1o0 = "true"
    pass
   i1i1i1I = os . path . join ( Ooo000O00 , 'icon.png' ) if os . path . exists ( os . path . join ( Ooo000O00 , 'icon.png' ) ) else iiiiiIIii
   oOoo000 = os . path . join ( Ooo000O00 , 'fanart.jpg' ) if os . path . exists ( os . path . join ( Ooo000O00 , 'fanart.jpg' ) ) else OOO00
   iiiii1II ( "%s %s" % ( Ii1iI111 , oO0o00oOOooO0 ) , 'toggleaddon' , IiI11I111 , iI1o0 , icon = i1i1i1I , fanart = oOoo000 )
   OO0OOoo0OOO . close ( )
 if iiIi == 0 :
  iiiii1II ( "No Addons Found to Enable or Disable." , '' , icon = IiIi11iI )
 iIi1 ( 'files' , 'viewType' )
 if 32 - 32: OoooooooOO / II111iiii / IIIi1i1I + IiiIII111ii / O0
def oOO0 ( ) :
 iIi1iI = [ 'Every Startup' , 'Every Day' , 'Every Three Days' , 'Every Weekly' ]
 OoO000Oo0oO = iiIIIII1i1iI . select ( "[COLOR %s]How often would you list to Auto Clean on Startup?[/COLOR]" % iIiIi11 , iIi1iI )
 if not OoO000Oo0oO == - 1 :
  wiz . setS ( 'autocleanfeq' , str ( OoO000Oo0oO ) )
  wiz . LogNotify ( '[COLOR %s]Auto Clean Up[/COLOR]' % oOOo0O00o , '[COLOR %s]Fequency Now %s[/COLOR]' % ( iIiIi11 , iIi1iI [ OoO000Oo0oO ] ) )
  if 46 - 46: O0 - o0o0Oo0oooo0 . OoooooooOO
def i1I111II ( ) :
 iiiii1II ( 'Convert Text Files to 0.1.7' , 'converttext' , themeit = OOOiiiiI )
 iiiii1II ( 'Create QR Code' , 'createqr' , themeit = OOOiiiiI )
 iiiii1II ( 'Test Notifications' , 'testnotify' , themeit = OOOiiiiI )
 iiiii1II ( 'Test Update' , 'testupdate' , themeit = OOOiiiiI )
 iiiii1II ( 'Test First Run' , 'testfirst' , themeit = OOOiiiiI )
 iiiii1II ( 'Test First Run Settings' , 'testfirstrun' , themeit = OOOiiiiI )
 iiiii1II ( 'Test APk' , 'testapk' , themeit = OOOiiiiI )
 if 65 - 65: i11iIiiIii + Ooo0O * OoooooooOO - I1111
 iIi1 ( 'files' , 'viewType' )
 if 26 - 26: I1I1i1 % iii11iiII + iii11iiII % i11IiIiiIIIII * i11iIiiIii / iiIIi1IiIi11
 if 64 - 64: IIIi1i1I % o0o0Oo0oooo0 / II111iiii % OOoooooO - iiIIi1IiIi11
 if 2 - 2: OO00O0O0O00Oo - oO0 + I1I1i1 * I1111 / iiIIi1IiIi11
 if 26 - 26: iii11iiII * Ooo0O
def i1iI1Ii11Ii1 ( name , type , theme = None , over = False ) :
 if over == False :
  o0OoO0oo0O0o = wiz . checkBuild ( name , 'url' )
  if o0OoO0oo0O0o == False :
   wiz . LogNotify ( "[COLOR %s]%s[/COLOR]" % ( oOOo0O00o , o0OOO ) , "[COLOR %s]Unabled to find build[/COLOR]" % iIiIi11 )
   return
  ii1III1iiIi = wiz . workingURL ( o0OoO0oo0O0o )
  if ii1III1iiIi == False :
   wiz . LogNotify ( "[COLOR %s]%s[/COLOR]" % ( oOOo0O00o , o0OOO ) , "[COLOR %s]Build Zip Error: %s[/COLOR]" % ( iIiIi11 , ii1III1iiIi ) )
   return
 if type == 'gui' :
  if name == O000oo0O :
   if over == True : I1ii1iI = 1
   else : I1ii1iI = iiIIIII1i1iI . yesno ( o0OOO , '[COLOR %s]Would you like to apply the guifix for:' % iIiIi11 , '[COLOR %s]%s[/COLOR]?[/COLOR]' % ( oOOo0O00o , name ) , nolabel = '[B][COLOR red]No, Cancel[/COLOR][/B]' , yeslabel = '[B][COLOR green]Apply Fix[/COLOR][/B]' )
  else :
   I1ii1iI = iiIIIII1i1iI . yesno ( "%s - [COLOR red]WARNING!![/COLOR]" % o0OOO , "[COLOR %s][COLOR %s]%s[/COLOR] community build is not currently installed." % ( iIiIi11 , oOOo0O00o , name ) , "Would you like to apply the guiFix anyways?.[/COLOR]" , nolabel = '[B][COLOR red]No, Cancel[/COLOR][/B]' , yeslabel = '[B][COLOR green]Apply Fix[/COLOR][/B]' )
  if I1ii1iI :
   ooO000OO = wiz . checkBuild ( name , 'gui' )
   i111IIiIiiI1 = name . replace ( '\\' , '' ) . replace ( '/' , '' ) . replace ( ':' , '' ) . replace ( '*' , '' ) . replace ( '?' , '' ) . replace ( '"' , '' ) . replace ( '<' , '' ) . replace ( '>' , '' ) . replace ( '|' , '' )
   if not wiz . workingURL ( ooO000OO ) == True : wiz . LogNotify ( "[COLOR %s]%s[/COLOR]" % ( oOOo0O00o , o0OOO ) , '[COLOR %s]GuiFix: Invalid Zip Url![/COLOR]' % iIiIi11 ) ; return
   if not os . path . exists ( o0o0OOO0o0 ) : os . makedirs ( o0o0OOO0o0 )
   oo00 . create ( o0OOO , '[COLOR %s][B]Downloading GuiFix:[/B][/COLOR] [COLOR %s]%s[/COLOR]' % ( iIiIi11 , oOOo0O00o , name ) , '' , 'Please Wait' )
   O0o0OO00 = os . path . join ( o0o0OOO0o0 , '%s_guisettings.zip' % i111IIiIiiI1 )
   try : os . remove ( O0o0OO00 )
   except : pass
   downloader . download ( ooO000OO , O0o0OO00 , oo00 )
   xbmc . sleep ( 500 )
   OOOoOo00O = '[COLOR %s][B]Installing:[/B][/COLOR] [COLOR %s]%s[/COLOR]' % ( iIiIi11 , oOOo0O00o , name )
   oo00 . update ( 0 , OOOoOo00O , '' , 'Please Wait' )
   extract . all ( O0o0OO00 , oOo00Oo00O , oo00 , title = OOOoOo00O )
   oo00 . close ( )
   wiz . defaultSkin ( )
   wiz . lookandFeelData ( 'save' )
   if I11i1I1I == 1 : iiIIi1 = 1
   elif I11i1I1I == 2 : iiIIi1 = 0
   else : iiIIi1 = iiIIIII1i1iI . yesno ( o0OOO , "[COLOR %s]The Gui fix has been installed.  Would you like to Reload the profile or Force Close Kodi?[/COLOR]" % iIiIi11 , yeslabel = "[B][COLOR red]Reload Profile[/COLOR][/B]" , nolabel = "[B][COLOR green]Force Close[/COLOR][/B]" )
   if iiIIi1 == 1 : wiz . reloadFix ( )
   else : iiIIIII1i1iI . ok ( o0OOO , "[COLOR %s]To save changes you now need to force close Kodi, Press OK to force close Kodi[/COLOR]" % iIiIi11 ) ; wiz . killxbmc ( 'true' )
  else :
   wiz . LogNotify ( "[COLOR %s]%s[/COLOR]" % ( oOOo0O00o , o0OOO ) , '[COLOR %s]GuiFix: Cancelled![/COLOR]' % iIiIi11 )
 elif type == 'fresh' :
  OO0IIIIIIi111i ( name )
 elif type == 'normal' :
  if OOOoO000 == 'normal' :
   if o0O0OOO0Ooo == 'true' :
    traktit . autoUpdate ( 'all' )
    wiz . setS ( 'traktlastsave' , str ( I1IiiiiI ) )
   if iiIiII1 == 'true' :
    debridit . autoUpdate ( 'all' )
    wiz . setS ( 'debridlastsave' , str ( I1IiiiiI ) )
   if OOO00O0O == 'true' :
    loginit . autoUpdate ( 'all' )
    wiz . setS ( 'loginlastsave' , str ( I1IiiiiI ) )
  iiIIIIiI111 = int ( o0OIiII ) ; OoooOO0Oo0 = int ( float ( wiz . checkBuild ( name , 'kodi' ) ) )
  if not iiIIIIiI111 == OoooOO0Oo0 :
   if iiIIIIiI111 == 16 and OoooOO0Oo0 <= 15 : O00OO = False
   else : O00OO = True
  else : O00OO = False
  if O00OO == True :
   I1iIiIii = iiIIIII1i1iI . yesno ( "%s - [COLOR red]WARNING!![/COLOR]" % o0OOO , '[COLOR %s]There is a chance that the skin will not appear correctly' % iIiIi11 , 'When installing a %s build on a Kodi %s install' % ( wiz . checkBuild ( name , 'kodi' ) , o0OIiII ) , 'Would you still like to install: [COLOR %s]%s v%s[/COLOR]?[/COLOR]' % ( oOOo0O00o , name , wiz . checkBuild ( name , 'version' ) ) , nolabel = '[B][COLOR red]No, Cancel[/COLOR][/B]' , yeslabel = '[B][COLOR green]Yes, Install[/COLOR][/B]' )
  else :
   if not over == False : I1iIiIii = 1
   else : I1iIiIii = iiIIIII1i1iI . yesno ( o0OOO , '[COLOR %s]Would you like to Download and Install:' % iIiIi11 , '[COLOR %s]%s v%s[/COLOR]?[/COLOR]' % ( oOOo0O00o , name , wiz . checkBuild ( name , 'version' ) ) , nolabel = '[B][COLOR red]No, Cancel[/COLOR][/B]' , yeslabel = '[B][COLOR green]Yes, Install[/COLOR][/B]' )
  if I1iIiIii :
   wiz . clearS ( 'build' )
   ooO000OO = wiz . checkBuild ( name , 'url' )
   i111IIiIiiI1 = name . replace ( '\\' , '' ) . replace ( '/' , '' ) . replace ( ':' , '' ) . replace ( '*' , '' ) . replace ( '?' , '' ) . replace ( '"' , '' ) . replace ( '<' , '' ) . replace ( '>' , '' ) . replace ( '|' , '' )
   if not wiz . workingURL ( ooO000OO ) == True : wiz . LogNotify ( "[COLOR %s]%s[/COLOR]" % ( oOOo0O00o , o0OOO ) , '[COLOR %s]Build Install: Invalid Zip Url![/COLOR]' % iIiIi11 ) ; return
   if not os . path . exists ( o0o0OOO0o0 ) : os . makedirs ( o0o0OOO0o0 )
   oo00 . create ( o0OOO , '[COLOR %s][B]Downloading:[/B][/COLOR] [COLOR %s]%s v%s[/COLOR]' % ( iIiIi11 , oOOo0O00o , name , wiz . checkBuild ( name , 'version' ) ) , '' , 'Please Wait' )
   O0o0OO00 = os . path . join ( o0o0OOO0o0 , '%s.zip' % i111IIiIiiI1 )
   try : os . remove ( O0o0OO00 )
   except : pass
   wiz . add_one ( name )
   downloader . download ( ooO000OO , O0o0OO00 , oo00 )
   xbmc . sleep ( 500 )
   OOOoOo00O = '[COLOR %s][B]Installing:[/B][/COLOR] [COLOR %s]%s v%s[/COLOR]' % ( iIiIi11 , oOOo0O00o , name , wiz . checkBuild ( name , 'version' ) )
   oo00 . update ( 0 , OOOoOo00O , '' , 'Please Wait' )
   iIi11i , ooIII1II1iii1i , O0OO0oOO = extract . all ( O0o0OO00 , o00 , oo00 , title = OOOoOo00O )
   if int ( float ( iIi11i ) ) > 0 :
    wiz . fixmetas ( )
    wiz . lookandFeelData ( 'save' )
    wiz . defaultSkin ( )
    if 76 - 76: I1111 . OoooooooOO % OO00O0O0O00Oo * IiiIII111ii
    wiz . setS ( 'buildname' , name )
    wiz . setS ( 'buildversion' , wiz . checkBuild ( name , 'version' ) )
    wiz . setS ( 'buildtheme' , '' )
    wiz . setS ( 'latestversion' , wiz . checkBuild ( name , 'version' ) )
    wiz . setS ( 'lastbuildcheck' , str ( OOI1iI1ii1II ) )
    wiz . setS ( 'installed' , 'true' )
    wiz . setS ( 'extract' , str ( iIi11i ) )
    wiz . setS ( 'errors' , str ( ooIII1II1iii1i ) )
    wiz . log ( 'INSTALLED %s: [ERRORS:%s]' % ( iIi11i , ooIII1II1iii1i ) )
    try : os . remove ( O0o0OO00 )
    except : pass
    if int ( float ( ooIII1II1iii1i ) ) > 0 :
     I1ii1iI = iiIIIII1i1iI . yesno ( o0OOO , '[COLOR %s][COLOR %s]%s v%s[/COLOR]' % ( iIiIi11 , oOOo0O00o , name , wiz . checkBuild ( name , 'version' ) ) , 'Completed: [COLOR %s]%s%s[/COLOR] [Errors:[COLOR %s]%s[/COLOR]]' % ( oOOo0O00o , iIi11i , '%' , oOOo0O00o , ooIII1II1iii1i ) , 'Would you like to view the errors?[/COLOR]' , nolabel = '[B][COLOR red]No Thanks[/COLOR][/B]' , yeslabel = '[B][COLOR green]View Errors[/COLOR][/B]' )
     if I1ii1iI :
      if isinstance ( ooIII1II1iii1i , unicode ) :
       O0OO0oOO = O0OO0oOO . encode ( 'utf-8' )
      wiz . TextBox ( o0OOO , O0OO0oOO )
    oo00 . close ( )
    OOo00OoO = wiz . themeCount ( name )
    if not OOo00OoO == False :
     i1iI1Ii11Ii1 ( name , 'theme' )
    if o0OIiII >= 17 : wiz . addonDatabase ( IiII1IiiIiI1 , 1 )
    if I11i1I1I == 1 : iiIIi1 = 1
    elif I11i1I1I == 2 : iiIIi1 = 0
    else : iiIIi1 = iiIIIII1i1iI . yesno ( o0OOO , "[COLOR %s]Would you like to [COLOR %s]Force close[/COLOR] kodi or [COLOR %s]Reload Profile[/COLOR]?[/COLOR]" % ( iIiIi11 , oOOo0O00o , oOOo0O00o ) , yeslabel = "[B][COLOR red]Reload Profile[/COLOR][/B]" , nolabel = "[B][COLOR green]Force Close[/COLOR][/B]" )
    if iiIIi1 == 1 : wiz . reloadFix ( )
    else : wiz . killxbmc ( True )
   else :
    if isinstance ( ooIII1II1iii1i , unicode ) :
     O0OO0oOO = O0OO0oOO . encode ( 'utf-8' )
    wiz . TextBox ( "%s: Error Installing Build" % o0OOO , O0OO0oOO )
  else :
   wiz . LogNotify ( "[COLOR %s]%s[/COLOR]" % ( oOOo0O00o , o0OOO ) , '[COLOR %s]Build Install: Cancelled![/COLOR]' % iIiIi11 )
 elif type == 'theme' :
  if theme == None :
   OOo00OoO = wiz . checkBuild ( name , 'theme' )
   i1iiI1i = [ ]
   if not OOo00OoO == 'http://' and wiz . workingURL ( OOo00OoO ) == True :
    i1iiI1i = wiz . themeCount ( name , False )
    if len ( i1iiI1i ) > 0 :
     if iiIIIII1i1iI . yesno ( o0OOO , "[COLOR %s]The Build [COLOR %s]%s[/COLOR] comes with [COLOR %s]%s[/COLOR] different themes" % ( iIiIi11 , oOOo0O00o , name , oOOo0O00o , len ( i1iiI1i ) ) , "Would you like to install one now?[/COLOR]" , yeslabel = "[B][COLOR green]Install Theme[/COLOR][/B]" , nolabel = "[B][COLOR red]Cancel Themes[/COLOR][/B]" ) :
      wiz . log ( "Theme List: %s " % str ( i1iiI1i ) )
      O0OOO00OOO00o = iiIIIII1i1iI . select ( o0OOO , i1iiI1i )
      wiz . log ( "Theme install selected: %s" % O0OOO00OOO00o )
      if not O0OOO00OOO00o == - 1 : theme = i1iiI1i [ O0OOO00OOO00o ] ; i11o00Ooo = True
      else : wiz . LogNotify ( "[COLOR %s]%s[/COLOR]" % ( oOOo0O00o , o0OOO ) , '[COLOR %s]Theme Install: Cancelled![/COLOR]' % iIiIi11 ) ; return
     else : wiz . LogNotify ( "[COLOR %s]%s[/COLOR]" % ( oOOo0O00o , o0OOO ) , '[COLOR %s]Theme Install: Cancelled![/COLOR]' % iIiIi11 ) ; return
   else : wiz . LogNotify ( "[COLOR %s]%s[/COLOR]" % ( oOOo0O00o , o0OOO ) , '[COLOR %s]Theme Install: None Found![/COLOR]' % iIiIi11 )
  else : i11o00Ooo = iiIIIII1i1iI . yesno ( o0OOO , '[COLOR %s]Would you like to install the theme:' % iIiIi11 , '[COLOR %s]%s[/COLOR]' % ( oOOo0O00o , theme ) , 'for [COLOR %s]%s v%s[/COLOR]?[/COLOR]' % ( oOOo0O00o , name , wiz . checkBuild ( name , 'version' ) ) , yeslabel = "[B][COLOR green]Install Theme[/COLOR][/B]" , nolabel = "[B][COLOR red]Cancel Themes[/COLOR][/B]" )
  if i11o00Ooo :
   OoO00OOoOOOo0 = wiz . checkTheme ( name , theme , 'url' )
   i111IIiIiiI1 = name . replace ( '\\' , '' ) . replace ( '/' , '' ) . replace ( ':' , '' ) . replace ( '*' , '' ) . replace ( '?' , '' ) . replace ( '"' , '' ) . replace ( '<' , '' ) . replace ( '>' , '' ) . replace ( '|' , '' )
   if not wiz . workingURL ( OoO00OOoOOOo0 ) == True : wiz . LogNotify ( "[COLOR %s]%s[/COLOR]" % ( oOOo0O00o , o0OOO ) , '[COLOR %s]Theme Install: Invalid Zip Url![/COLOR]' % iIiIi11 ) ; return False
   if not os . path . exists ( o0o0OOO0o0 ) : os . makedirs ( o0o0OOO0o0 )
   oo00 . create ( o0OOO , '[COLOR %s][B]Downloading:[/B][/COLOR] [COLOR %s]%s[/COLOR]' % ( iIiIi11 , oOOo0O00o , theme ) , '' , 'Please Wait' )
   O0o0OO00 = os . path . join ( o0o0OOO0o0 , '%s.zip' % i111IIiIiiI1 )
   try : os . remove ( O0o0OO00 )
   except : pass
   downloader . download ( OoO00OOoOOOo0 , O0o0OO00 , oo00 )
   xbmc . sleep ( 500 )
   oo00 . update ( 0 , "" , "Installing %s " % name )
   oOoO00O = False
   if OOOoO000 not in [ "fresh" , "normal" ] :
    oOoO00O = I11I1I1i1i ( O0o0OO00 ) if not wiz . currSkin ( ) in [ 'skin.confluence' , 'skin.estuary' ] else False
    Oo0oOO0O00 = o00OOo0o0O ( O0o0OO00 ) if not wiz . currSkin ( ) in [ 'skin.confluence' , 'skin.estuary' ] else False
    if oOoO00O == True :
     wiz . lookandFeelData ( 'save' )
     I111Iii1 = 'skin.confluence' if o0OIiII < 17 else 'skin.estuary'
     i11i = xbmc . getSkinDir ( )
     if 73 - 73: OOoooooO % OOoooooO . iiIIi1IiIi11 + OO00O0O0O00Oo
     skinSwitch . swapSkins ( I111Iii1 )
     iiIi = 0
     xbmc . sleep ( 1000 )
     while not xbmc . getCondVisibility ( "Window.isVisible(yesnodialog)" ) and iiIi < 150 :
      iiIi += 1
      xbmc . sleep ( 200 )
     if xbmc . getCondVisibility ( "Window.isVisible(yesnodialog)" ) :
      wiz . ebi ( 'SendClick(11)' )
     else : wiz . LogNotify ( "[COLOR %s]%s[/COLOR]" % ( oOOo0O00o , o0OOO ) , '[COLOR %s]Theme Install: Skin Swap Timed Out![/COLOR]' % iIiIi11 ) ; return
     xbmc . sleep ( 500 )
   OOOoOo00O = '[COLOR %s][B]Installing Theme:[/B][/COLOR] [COLOR %s]%s[/COLOR]' % ( iIiIi11 , oOOo0O00o , theme )
   oo00 . update ( 0 , OOOoOo00O , '' , 'Please Wait' )
   iIi11i , ooIII1II1iii1i , O0OO0oOO = extract . all ( O0o0OO00 , o00 , oo00 , title = OOOoOo00O )
   wiz . setS ( 'buildtheme' , theme )
   wiz . log ( 'INSTALLED %s: [ERRORS:%s]' % ( iIi11i , ooIII1II1iii1i ) )
   oo00 . close ( )
   if OOOoO000 not in [ "fresh" , "normal" ] :
    wiz . forceUpdate ( )
    if o0OIiII >= 17 : wiz . kodi17Fix ( )
    if Oo0oOO0O00 == True :
     wiz . lookandFeelData ( 'save' )
     wiz . defaultSkin ( )
     i11i = wiz . getS ( 'defaultskin' )
     skinSwitch . swapSkins ( i11i )
     iiIi = 0
     xbmc . sleep ( 1000 )
     while not xbmc . getCondVisibility ( "Window.isVisible(yesnodialog)" ) and iiIi < 150 :
      iiIi += 1
      xbmc . sleep ( 200 )
      if 10 - 10: O0 / iii11iiII * OOoooooO - I1111 - i1IIi . o0o0Oo0oooo0
     if xbmc . getCondVisibility ( "Window.isVisible(yesnodialog)" ) :
      wiz . ebi ( 'SendClick(11)' )
     wiz . lookandFeelData ( 'restore' )
    elif oOoO00O == True :
     skinSwitch . swapSkins ( i11i )
     iiIi = 0
     xbmc . sleep ( 1000 )
     while not xbmc . getCondVisibility ( "Window.isVisible(yesnodialog)" ) and iiIi < 150 :
      iiIi += 1
      xbmc . sleep ( 200 )
      if 69 - 69: Ooo0O - IiiIII111ii % IiiIII111ii - iii11iiII * iii11iiII / Ooo0O
     if xbmc . getCondVisibility ( "Window.isVisible(yesnodialog)" ) :
      wiz . ebi ( 'SendClick(11)' )
     else : wiz . LogNotify ( "[COLOR %s]%s[/COLOR]" % ( oOOo0O00o , o0OOO ) , '[COLOR %s]Theme Install: Skin Swap Timed Out![/COLOR]' % iIiIi11 ) ; return
     wiz . lookandFeelData ( 'restore' )
    else :
     wiz . ebi ( "ReloadSkin()" )
     xbmc . sleep ( 1000 )
     wiz . ebi ( "Container.Refresh" )
  else :
   wiz . LogNotify ( "[COLOR %s]%s[/COLOR]" % ( oOOo0O00o , o0OOO ) , '[COLOR %s]Theme Install: Cancelled![/COLOR]' % iIiIi11 )
   if 13 - 13: o0o0Oo0oooo0
def OOo0oOOOOoo0 ( name , url ) :
 if not wiz . workingURL ( url ) :
  LogNotify ( "[COLOR %s]%s[/COLOR]" % ( oOOo0O00o , o0OOO ) , '[COLOR %s]Invalid URL for Build[/COLOR]' % iIiIi11 ) ; return
 type = iiIIIII1i1iI . yesno ( o0OOO , "[COLOR %s]Would you like to preform a [COLOR %s]Fresh Install[/COLOR] or [COLOR %s]Normal Install[/COLOR] for:[/COLOR]" % ( iIiIi11 , oOOo0O00o , oOOo0O00o ) , "[COLOR %s]%s[/COLOR]" % ( oOOo0O00o , name ) , yeslabel = "[B][COLOR green]Fresh Install[/COLOR][/B]" , nolabel = "[B][COLOR red]Normal Install[/COLOR][/B]" )
 if type == 1 :
  OO0IIIIIIi111i ( 'third' , True )
 wiz . clearS ( 'build' )
 i111IIiIiiI1 = name . replace ( '\\' , '' ) . replace ( '/' , '' ) . replace ( ':' , '' ) . replace ( '*' , '' ) . replace ( '?' , '' ) . replace ( '"' , '' ) . replace ( '<' , '' ) . replace ( '>' , '' ) . replace ( '|' , '' )
 if not os . path . exists ( o0o0OOO0o0 ) : os . makedirs ( o0o0OOO0o0 )
 oo00 . create ( o0OOO , '[COLOR %s][B]Downloading:[/B][/COLOR] [COLOR %s]%s[/COLOR]' % ( iIiIi11 , oOOo0O00o , name ) , '' , 'Please Wait' )
 O0o0OO00 = os . path . join ( o0o0OOO0o0 , '%s.zip' % i111IIiIiiI1 )
 try : os . remove ( O0o0OO00 )
 except : pass
 downloader . download ( url , O0o0OO00 , oo00 )
 xbmc . sleep ( 500 )
 OOOoOo00O = '[COLOR %s][B]Installing:[/B][/COLOR] [COLOR %s]%s[/COLOR]' % ( iIiIi11 , oOOo0O00o , name )
 oo00 . update ( 0 , OOOoOo00O , '' , 'Please Wait' )
 iIi11i , ooIII1II1iii1i , O0OO0oOO = extract . all ( O0o0OO00 , o00 , oo00 , title = OOOoOo00O )
 if int ( float ( iIi11i ) ) > 0 :
  wiz . fixmetas ( )
  wiz . lookandFeelData ( 'save' )
  wiz . defaultSkin ( )
  if 80 - 80: i11iIiiIii % oO0
  wiz . setS ( 'installed' , 'true' )
  wiz . setS ( 'extract' , str ( iIi11i ) )
  wiz . setS ( 'errors' , str ( ooIII1II1iii1i ) )
  wiz . log ( 'INSTALLED %s: [ERRORS:%s]' % ( iIi11i , ooIII1II1iii1i ) )
  try : os . remove ( O0o0OO00 )
  except : pass
  if int ( float ( ooIII1II1iii1i ) ) > 0 :
   I1ii1iI = iiIIIII1i1iI . yesno ( o0OOO , '[COLOR %s][COLOR %s]%s[/COLOR]' % ( iIiIi11 , oOOo0O00o , name ) , 'Completed: [COLOR %s]%s%s[/COLOR] [Errors:[COLOR %s]%s[/COLOR]]' % ( oOOo0O00o , iIi11i , '%' , oOOo0O00o , ooIII1II1iii1i ) , 'Would you like to view the errors?[/COLOR]' , nolabel = '[B][COLOR red]No Thanks[/COLOR][/B]' , yeslabel = '[B][COLOR green]View Errors[/COLOR][/B]' )
   if I1ii1iI :
    if isinstance ( ooIII1II1iii1i , unicode ) :
     O0OO0oOO = O0OO0oOO . encode ( 'utf-8' )
    wiz . TextBox ( o0OOO , O0OO0oOO )
 oo00 . close ( )
 if o0OIiII >= 17 : wiz . addonDatabase ( IiII1IiiIiI1 , 1 )
 if I11i1I1I == 1 : iiIIi1 = 1
 elif I11i1I1I == 2 : iiIIi1 = 0
 else : iiIIi1 = iiIIIII1i1iI . yesno ( o0OOO , "[COLOR %s]Would you like to [COLOR %s]Force close[/COLOR] kodi or [COLOR %s]Reload Profile[/COLOR]?[/COLOR]" % ( iIiIi11 , oOOo0O00o , oOOo0O00o ) , yeslabel = "[B][COLOR green]Reload Profile[/COLOR][/B]" , nolabel = "[B][COLOR red]Force Close[/COLOR][/B]" )
 if iiIIi1 == 1 : wiz . reloadFix ( )
 else : wiz . killxbmc ( True )
 if 54 - 54: I1I1i1 + i11IiIiiIIIII - iIii1I11I1II1 % OOoooooO % i1Ii
def I11I1I1i1i ( path ) :
 II1i = zipfile . ZipFile ( path )
 for ii1IIIIiI11 in II1i . infolist ( ) :
  if '/settings.xml' in ii1IIIIiI11 . filename :
   return True
 return False
 if 13 - 13: oO0 . i1Ii
def o00OOo0o0O ( path ) :
 II1i = zipfile . ZipFile ( path )
 for ii1IIIIiI11 in II1i . infolist ( ) :
  if '/guisettings.xml' in ii1IIIIiI11 . filename :
   return True
 return False
 if 4 - 4: Ooo0O - I1111 - i11iIiiIii * OO00O0O0O00Oo / IiiIII111ii - iii11iiII
def Ii1 ( apk , url , Brackets ) :
 wiz . log ( apk )
 wiz . log ( url )
 if wiz . platform ( ) == 'android' :
  I1ii1iI = iiIIIII1i1iI . yesno ( o0OOO , "[COLOR %s]Would you like to download and install:" % iIiIi11 , "[COLOR %s]%s[/COLOR]" % ( oOOo0O00o , apk ) , yeslabel = "[B][COLOR green]Download[/COLOR][/B]" , nolabel = "[B][COLOR red]Cancel[/COLOR][/B]" )
  if not I1ii1iI : wiz . LogNotify ( "[COLOR %s]%s[/COLOR]" % ( oOOo0O00o , o0OOO ) , '[COLOR %s]ERROR: Install Cancelled[/COLOR]' % iIiIi11 ) ; return
  II1IIii1ii = apk
  if not os . path . exists ( o0o0OOO0o0 ) : os . makedirs ( o0o0OOO0o0 )
  if not wiz . workingURL ( url ) == True : wiz . LogNotify ( "[COLOR %s]%s[/COLOR]" % ( oOOo0O00o , o0OOO ) , '[COLOR %s]APK Installer: Invalid Apk Url![/COLOR]' % iIiIi11 ) ; return
  oo00 . create ( o0OOO , '[COLOR %s][B]Downloading:[/B][/COLOR] [COLOR %s]%s[/COLOR]' % ( iIiIi11 , oOOo0O00o , II1IIii1ii ) , '' , 'Please Wait' )
  O0o0OO00 = os . path . join ( o0o0OOO0o0 , "%s.apk" % apk . replace ( '\\' , '' ) . replace ( '/' , '' ) . replace ( ':' , '' ) . replace ( '*' , '' ) . replace ( '?' , '' ) . replace ( '"' , '' ) . replace ( '<' , '' ) . replace ( '>' , '' ) . replace ( '|' , '' ) )
  try : os . remove ( O0o0OO00 )
  except : pass
  downloader . download ( url , O0o0OO00 , oo00 )
  xbmc . sleep ( 100 )
  oo00 . close ( )
  if "Brackets" in Brackets :
   IIiIiIiiI1Iii = zipfile . ZipFile ( O0o0OO00 )
   for file in IIiIiIiiI1Iii . namelist ( ) :
    if file . endswith ( '.apk' ) :
     with open ( os . path . join ( o0o0OOO0o0 , os . path . basename ( file ) ) , 'wb' ) as OO0OOoo0OOO :
      Ii111iII = file . split ( '/' ) [ 1 ]
      OO0OOoo0OOO . write ( IIiIiIiiI1Iii . read ( file ) )
      xbmc . sleep ( 500 )
      OO0OOoo0OOO . close ( )
      try :
       os . remove ( O0o0OO00 )
      except :
       pass
      O0o0OO00 = os . path . join ( o0o0OOO0o0 , Ii111iII )
  iiIIIII1i1iI . ok ( o0OOO , "Launching the APK to be installed" , "Follow the install process to complete." )
  notify . apkInstaller ( apk )
  wiz . ebi ( 'StartAndroidActivity("","android.intent.action.VIEW","application/vnd.android.package-archive","file:' + O0o0OO00 + '")' )
 else : wiz . LogNotify ( "[COLOR %s]%s[/COLOR]" % ( oOOo0O00o , o0OOO ) , '[COLOR %s]ERROR: None Android Device[/COLOR]' % iIiIi11 )
 if 83 - 83: OoooooooOO + I1111 * IIIi1i1I . O0
 if 13 - 13: I1I1i1
 if 7 - 7: ooOo + i1Ii / i11iIiiIii / Ooo0O
 if 97 - 97: OO00O0O0O00Oo . i11IiIiiIIIII / ooOo
def o00OO0o0 ( name , url , ) :
 if "NULL" in url :
  iiIIIII1i1iI . ok ( o0OOO , "[COLOR ghostwhite]Not a valid selection, please try again.[/COLOR]" )
  sys . exit ( 1 )
  if 39 - 39: OOoooooO % oO0 - iiIIi1IiIi11
 I1IiI = xbmcgui . DialogProgress ( )
 I1IiI . create ( o0OOO , "" , "" , 'ROM: ' + name )
 i111IIiIiiI1 = name . replace ( '\\' , '' ) . replace ( '/' , '' ) . replace ( ':' , '' ) . replace ( '*' , '' ) . replace ( '?' , '' ) . replace ( '"' , '' ) . replace ( '<' , '' ) . replace ( '>' , '' ) . replace ( '|' , '' )
 O0o0OO00 = os . path . join ( o0o0OOO0o0 , '%s.zip' % i111IIiIiiI1 )
 downloader . download ( url , O0o0OO00 , I1IiI )
 I1IiI . update ( 0 )
 extract . all ( O0o0OO00 , iI , I1IiI )
 iiIIIII1i1iI . ok ( o0OOO , "[COLOR yellow]Download complete, ROM Location: [/COLOR][COLOR white]" + iI + "[/COLOR]" )
 if 48 - 48: i11iIiiIii
 if 52 - 52: iIii1I11I1II1
 if 38 - 38: i11IiIiiIIIII . i11IiIiiIIIII * IIIi1i1I / OoooooooOO % OOoooooO
 if 80 - 80: I1111 / i1Ii * ooOo % i1Ii
 if 95 - 95: O0 / i11IiIiiIIIII . OO00O0O0O00Oo
def iII11II1II ( part , whole ) :
 return 100 * float ( part ) / float ( whole )
 if 100 - 100: I1111 % OO00O0O0O00Oo - i11IiIiiIIIII % i11IiIiiIIIII % i11IiIiiIIIII / OOoooooO
def I1i11ii11 ( type , add , name ) :
 if type == 'saveaddon' :
  OOO000Oo = [ ]
  I1IIIi1i = urllib . quote_plus ( add . lower ( ) . replace ( ' ' , '' ) )
  OooIii1I1iI = add . replace ( 'Debrid' , 'Real Debrid' )
  oo00OOoOoO00 = urllib . quote_plus ( name . lower ( ) . replace ( ' ' , '' ) )
  name = name . replace ( 'url' , 'URL Resolver' )
  OOO000Oo . append ( ( oooOo0OOOoo0 % name . title ( ) , ' ' ) )
  OOO000Oo . append ( ( OOoO % 'Save %s Data' % OooIii1I1iI , 'RunPlugin(plugin://%s/?mode=save%s&name=%s)' % ( IiII1IiiIiI1 , I1IIIi1i , oo00OOoOoO00 ) ) )
  OOO000Oo . append ( ( OOoO % 'Restore %s Data' % OooIii1I1iI , 'RunPlugin(plugin://%s/?mode=restore%s&name=%s)' % ( IiII1IiiIiI1 , I1IIIi1i , oo00OOoOoO00 ) ) )
  OOO000Oo . append ( ( OOoO % 'Clear %s Data' % OooIii1I1iI , 'RunPlugin(plugin://%s/?mode=clear%s&name=%s)' % ( IiII1IiiIiI1 , I1IIIi1i , oo00OOoOoO00 ) ) )
 elif type == 'save' :
  OOO000Oo = [ ]
  I1IIIi1i = urllib . quote_plus ( add . lower ( ) . replace ( ' ' , '' ) )
  OooIii1I1iI = add . replace ( 'Debrid' , 'Real Debrid' )
  oo00OOoOoO00 = urllib . quote_plus ( name . lower ( ) . replace ( ' ' , '' ) )
  name = name . replace ( 'url' , 'URL Resolver' )
  OOO000Oo . append ( ( oooOo0OOOoo0 % name . title ( ) , ' ' ) )
  OOO000Oo . append ( ( OOoO % 'Register %s' % OooIii1I1iI , 'RunPlugin(plugin://%s/?mode=auth%s&name=%s)' % ( IiII1IiiIiI1 , I1IIIi1i , oo00OOoOoO00 ) ) )
  OOO000Oo . append ( ( OOoO % 'Save %s Data' % OooIii1I1iI , 'RunPlugin(plugin://%s/?mode=save%s&name=%s)' % ( IiII1IiiIiI1 , I1IIIi1i , oo00OOoOoO00 ) ) )
  OOO000Oo . append ( ( OOoO % 'Restore %s Data' % OooIii1I1iI , 'RunPlugin(plugin://%s/?mode=restore%s&name=%s)' % ( IiII1IiiIiI1 , I1IIIi1i , oo00OOoOoO00 ) ) )
  OOO000Oo . append ( ( OOoO % 'Import %s Data' % OooIii1I1iI , 'RunPlugin(plugin://%s/?mode=import%s&name=%s)' % ( IiII1IiiIiI1 , I1IIIi1i , oo00OOoOoO00 ) ) )
  OOO000Oo . append ( ( OOoO % 'Clear Addon %s Data' % OooIii1I1iI , 'RunPlugin(plugin://%s/?mode=addon%s&name=%s)' % ( IiII1IiiIiI1 , I1IIIi1i , oo00OOoOoO00 ) ) )
 elif type == 'install' :
  OOO000Oo = [ ]
  oo00OOoOoO00 = urllib . quote_plus ( name )
  OOO000Oo . append ( ( oooOo0OOOoo0 % name , 'RunAddon(%s, ?mode=viewbuild&name=%s)' % ( IiII1IiiIiI1 , oo00OOoOoO00 ) ) )
  OOO000Oo . append ( ( OOoO % 'Fresh Install' , 'RunPlugin(plugin://%s/?mode=install&name=%s&url=fresh)' % ( IiII1IiiIiI1 , oo00OOoOoO00 ) ) )
  OOO000Oo . append ( ( OOoO % 'Normal Install' , 'RunPlugin(plugin://%s/?mode=install&name=%s&url=normal)' % ( IiII1IiiIiI1 , oo00OOoOoO00 ) ) )
  OOO000Oo . append ( ( OOoO % 'Apply guiFix' , 'RunPlugin(plugin://%s/?mode=install&name=%s&url=gui)' % ( IiII1IiiIiI1 , oo00OOoOoO00 ) ) )
  OOO000Oo . append ( ( OOoO % 'Build Information' , 'RunPlugin(plugin://%s/?mode=buildinfo&name=%s)' % ( IiII1IiiIiI1 , oo00OOoOoO00 ) ) )
 OOO000Oo . append ( ( oooOo0OOOoo0 % '%s Settings' % o0OOO , 'RunPlugin(plugin://%s/?mode=settings)' % IiII1IiiIiI1 ) )
 return OOO000Oo
 if 62 - 62: IIIi1i1I + Ooo0O / i11iIiiIii
def ooOoOo ( state ) :
 iIi = [ 'includevideo' , 'includeall' , 'includebob' , 'includephoenix' , 'includespecto' , 'includegenesis' , 'includeexodus' , 'includeonechan' , 'includesalts' , 'includesaltslite' ]
 ii1iI1i = [ 'Include Video Addons' , 'Include All Addons' , 'Include Bob' , 'Include Phoenix' , 'Include Specto' , 'Include Genesis' , 'Include Exodus' , 'Include One Channel' , 'Include Salts' , 'Include Salts Lite HD' ]
 if state in [ 'true' , 'false' ] :
  for ii1IIIIiI11 in iIi :
   wiz . setS ( ii1IIIIiI11 , state )
 else :
  if not state in [ 'includevideo' , 'includeall' ] and wiz . getS ( 'includeall' ) == 'true' :
   try :
    ii1IIIIiI11 = ii1iI1i [ iIi . index ( state ) ]
    iiIIIII1i1iI . ok ( o0OOO , "[COLOR %s]You will need to turn off [COLOR %s]Include All Addons[/COLOR] to disable[/COLOR] [COLOR %s]%s[/COLOR]" % ( iIiIi11 , oOOo0O00o , oOOo0O00o , ii1IIIIiI11 ) )
   except :
    wiz . LogNotify ( "[COLOR %s]Toggle Cache[/COLOR]" % oOOo0O00o , "[COLOR %s]Invalid id: %s[/COLOR]" % ( iIiIi11 , state ) )
  else :
   i1iiiI = 'true' if wiz . getS ( state ) == 'false' else 'false'
   wiz . setS ( state , i1iiiI )
   if 75 - 75: OoooooooOO . iii11iiII + I1111 / IiiIII111ii - ooOo % IiiIII111ii
def O0OooooO0o0O0 ( url ) :
 if 'watch?v=' in url :
  OOo00ooOoO0o , oO0oo = url . split ( '?' )
  o00o0o000Oo = oO0oo . split ( '&' )
  for ii1IIIIiI11 in o00o0o000Oo :
   if ii1IIIIiI11 . startswith ( 'v=' ) :
    url = ii1IIIIiI11 [ 2 : ]
    break
   else : continue
 elif 'embed' in url or 'youtu.be' in url :
  OOo00ooOoO0o = url . split ( '/' )
  if len ( OOo00ooOoO0o [ - 1 ] ) > 5 :
   url = OOo00ooOoO0o [ - 1 ]
  elif len ( OOo00ooOoO0o [ - 2 ] ) > 5 :
   url = OOo00ooOoO0o [ - 2 ]
 wiz . log ( "YouTube URL: %s" % url )
 yt . PlayVideo ( url )
 if 100 - 100: i1IIi - i11iIiiIii . OO00O0O0O00Oo * I1111
def oOIIII ( ) :
 ooOOo = wiz . Grab_Log ( True )
 i1iii1IiiiI1i1 = wiz . Grab_Log ( True , True )
 IIIiI1i1 = 0 ; IIi11iII11i1 = ooOOo
 if not i1iii1IiiiI1i1 == False and not ooOOo == False :
  IIIiI1i1 = iiIIIII1i1iI . select ( o0OOO , [ "View %s" % ooOOo . replace ( iI11iiiI1II , "" ) , "View %s" % i1iii1IiiiI1i1 . replace ( iI11iiiI1II , "" ) ] )
  if IIIiI1i1 == - 1 : wiz . LogNotify ( '[COLOR %s]View Log[/COLOR]' % oOOo0O00o , '[COLOR %s]View Log Cancelled![/COLOR]' % iIiIi11 ) ; return
 elif ooOOo == False and i1iii1IiiiI1i1 == False :
  wiz . LogNotify ( '[COLOR %s]View Log[/COLOR]' % oOOo0O00o , '[COLOR %s]No Log File Found![/COLOR]' % iIiIi11 )
  return
 elif not ooOOo == False : IIIiI1i1 = 0
 elif not i1iii1IiiiI1i1 == False : IIIiI1i1 = 1
 if 5 - 5: II111iiii - i1Ii
 IIi11iII11i1 = ooOOo if IIIiI1i1 == 0 else i1iii1IiiiI1i1
 O0O00oO0OoO0o = wiz . Grab_Log ( False ) if IIIiI1i1 == 0 else wiz . Grab_Log ( False , True )
 if 5 - 5: iii11iiII % Ooo0O % i1Ii % OOoooooO
 wiz . TextBox ( "%s - %s" % ( o0OOO , IIi11iII11i1 ) , O0O00oO0OoO0o )
 if 17 - 17: IiiIII111ii + II111iiii + OoooooooOO / iii11iiII / i1Ii
def Oo00OO00o0oO ( log = None , count = None , all = None ) :
 if log == None :
  ooOOo = wiz . Grab_Log ( True )
  i1iii1IiiiI1i1 = wiz . Grab_Log ( True , True )
  if not i1iii1IiiiI1i1 == False and not ooOOo == False :
   IIIiI1i1 = iiIIIII1i1iI . select ( o0OOO , [ "View %s: %s error(s)" % ( ooOOo . replace ( iI11iiiI1II , "" ) , Oo00OO00o0oO ( ooOOo , True , True ) ) , "View %s: %s error(s)" % ( i1iii1IiiiI1i1 . replace ( iI11iiiI1II , "" ) , Oo00OO00o0oO ( i1iii1IiiiI1i1 , True , True ) ) ] )
   if IIIiI1i1 == - 1 : wiz . LogNotify ( '[COLOR %s]View Log[/COLOR]' % oOOo0O00o , '[COLOR %s]View Log Cancelled![/COLOR]' % iIiIi11 ) ; return
  elif ooOOo == False and i1iii1IiiiI1i1 == False :
   wiz . LogNotify ( '[COLOR %s]View Log[/COLOR]' % oOOo0O00o , '[COLOR %s]No Log File Found![/COLOR]' % iIiIi11 )
   return
  elif not ooOOo == False : IIIiI1i1 = 0
  elif not i1iii1IiiiI1i1 == False : IIIiI1i1 = 1
  log = ooOOo if IIIiI1i1 == 0 else i1iii1IiiiI1i1
 if log == False :
  if count == None :
   wiz . LogNotify ( "[COLOR %s]%s[/COLOR]" % ( oOOo0O00o , o0OOO ) , "[COLOR %s]Log File not Found[/COLOR]" % iIiIi11 )
   return False
  else :
   return 0
 else :
  if os . path . exists ( log ) :
   OO0OOoo0OOO = open ( log , mode = 'r' ) ; OOo00ooOoO0o = OO0OOoo0OOO . read ( ) . replace ( '\n' , '' ) . replace ( '\r' , '' ) ; OO0OOoo0OOO . close ( )
   O0Oo0o000oO = re . compile ( "-->Python callback/script returned the following error<--(.+?)-->End of Python script error report<--" ) . findall ( OOo00ooOoO0o )
   if not count == None :
    if all == None :
     iiIi = 0
     for ii1IIIIiI11 in O0Oo0o000oO :
      if IiII1IiiIiI1 in ii1IIIIiI11 : iiIi += 1
     return iiIi
    else : return len ( O0Oo0o000oO )
   if len ( O0Oo0o000oO ) > 0 :
    iiIi = 0 ; O0O00oO0OoO0o = ""
    for ii1IIIIiI11 in O0Oo0o000oO :
     if all == None and not IiII1IiiIiI1 in ii1IIIIiI11 : continue
     else :
      iiIi += 1
      O0O00oO0OoO0o += "[COLOR red]Error Number %s[/COLOR]\n(PythonToCppException) : -->Python callback/script returned the following error<--%s-->End of Python script error report<--\n\n" % ( iiIi , ii1IIIIiI11 . replace ( '                                          ' , '\n' ) . replace ( '\\\\' , '\\' ) . replace ( o00 , '' ) )
    if iiIi > 0 :
     wiz . TextBox ( o0OOO , O0O00oO0OoO0o )
    else : wiz . LogNotify ( o0OOO , "No Errors Found in Log" )
   else : wiz . LogNotify ( o0OOO , "No Errors Found in Log" )
  else : wiz . LogNotify ( o0OOO , "Log File not Found" )
  if 80 - 80: I1I1i1 % i1IIi / i11IiIiiIIIII
ooi1i1Ii1IiIII = 10
I1IIii11 = 92
I1I1 = 1
O0OOO0ooO00o = 2
I1iii1 = 3
iIiiiIIiii = 4
OO0Oo00Oo = 104
iIiO0O = 105
oOOoooo = 107
O0oIi1iIiIi1I11 = 7
ii1I11 = 110
OOO0 = 100
I1Ii1 = 108
if 67 - 67: i11IiIiiIIIII % i11iIiiIii . iIii1I11I1II1 * ooOo - i11IiIiiIIIII + IiiIII111ii
def i1ii1iIi ( default = None ) :
 class i1ii1iIi ( xbmcgui . WindowXMLDialog ) :
  def __init__ ( self , * args , ** kwargs ) :
   self . default = kwargs [ 'default' ]
   if 43 - 43: IiiIII111ii + iiIIi1IiIi11 + i1IIi - o0o0Oo0oooo0 + I1I1i1
  def onInit ( self ) :
   self . title = 101
   self . msg = 102
   self . scrollbar = 103
   self . upload = 201
   self . kodi = 202
   self . kodiold = 203
   self . wizard = 204
   self . okbutton = 205
   OO0OOoo0OOO = open ( self . default , 'r' )
   self . logmsg = OO0OOoo0OOO . read ( )
   OO0OOoo0OOO . close ( )
   self . titlemsg = "%s: %s" % ( o0OOO , self . default . replace ( iI11iiiI1II , '' ) . replace ( o0 , '' ) )
   self . showdialog ( )
   if 54 - 54: oO0 + oO0 + i11IiIiiIIIII % i1IIi % i11iIiiIii
  def showdialog ( self ) :
   self . getControl ( self . title ) . setLabel ( self . titlemsg )
   self . getControl ( self . msg ) . setText ( wiz . highlightText ( self . logmsg ) )
   self . setFocusId ( self . scrollbar )
   if 100 - 100: oO0
  def onClick ( self , controlId ) :
   if controlId == self . okbutton : self . close ( )
   elif controlId == self . upload : self . close ( ) ; uploadLog . Main ( )
   elif controlId == self . kodi :
    OOOoo000o0oo0 = wiz . Grab_Log ( False )
    o0Ii11iIiiI = wiz . Grab_Log ( True )
    if OOOoo000o0oo0 == False :
     self . titlemsg = "%s: View Log Error" % o0OOO
     self . getControl ( self . msg ) . setText ( "Log File Does Not Exists!" )
    else :
     self . titlemsg = "%s: %s" % ( o0OOO , o0Ii11iIiiI . replace ( iI11iiiI1II , '' ) )
     self . getControl ( self . title ) . setLabel ( self . titlemsg )
     self . getControl ( self . msg ) . setText ( wiz . highlightText ( OOOoo000o0oo0 ) )
     self . setFocusId ( self . scrollbar )
   elif controlId == self . kodiold :
    OOOoo000o0oo0 = wiz . Grab_Log ( False , True )
    o0Ii11iIiiI = wiz . Grab_Log ( True , True )
    if OOOoo000o0oo0 == False :
     self . titlemsg = "%s: View Log Error" % o0OOO
     self . getControl ( self . msg ) . setText ( "Log File Does Not Exists!" )
    else :
     self . titlemsg = "%s: %s" % ( o0OOO , o0Ii11iIiiI . replace ( iI11iiiI1II , '' ) )
     self . getControl ( self . title ) . setLabel ( self . titlemsg )
     self . getControl ( self . msg ) . setText ( wiz . highlightText ( OOOoo000o0oo0 ) )
     self . setFocusId ( self . scrollbar )
   elif controlId == self . wizard :
    OOOoo000o0oo0 = wiz . Grab_Log ( False , False , True )
    o0Ii11iIiiI = wiz . Grab_Log ( True , False , True )
    if OOOoo000o0oo0 == False :
     self . titlemsg = "%s: View Log Error" % o0OOO
     self . getControl ( self . msg ) . setText ( "Log File Does Not Exists!" )
    else :
     self . titlemsg = "%s: %s" % ( o0OOO , o0Ii11iIiiI . replace ( o0 , '' ) )
     self . getControl ( self . title ) . setLabel ( self . titlemsg )
     self . getControl ( self . msg ) . setText ( wiz . highlightText ( OOOoo000o0oo0 ) )
     self . setFocusId ( self . scrollbar )
     if 82 - 82: OoooooooOO
  def onAction ( self , action ) :
   if action == ooi1i1Ii1IiIII : self . close ( )
   elif action == I1IIii11 : self . close ( )
 if default == None : default = wiz . Grab_Log ( True )
 OoOO00oo0o = i1ii1iIi ( "LogViewer.xml" , I1ii11iIi11i . getAddonInfo ( 'path' ) , 'DefaultSkin' , default = default )
 OoOO00oo0o . doModal ( )
 del OoOO00oo0o
 if 76 - 76: iiIIi1IiIi11 . i1Ii % iiIIi1IiIi11 - OO00O0O0O00Oo
def i11IiiI1Ii1 ( addon , name , over = False ) :
 if not over == False :
  I1ii1iI = 1
 else :
  I1ii1iI = iiIIIII1i1iI . yesno ( o0OOO , '[COLOR %s]Are you sure you want to delete the addon:' % iIiIi11 , 'Name: [COLOR %s]%s[/COLOR]' % ( oOOo0O00o , name ) , 'ID: [COLOR %s]%s[/COLOR][/COLOR]' % ( oOOo0O00o , addon ) , yeslabel = '[B][COLOR green]Remove Addon[/COLOR][/B]' , nolabel = '[B][COLOR red]Don\'t Remove[/COLOR][/B]' )
 if I1ii1iI == 1 :
  Ooo000O00 = os . path . join ( O0O , addon )
  wiz . log ( "Removing Addon %s" % addon )
  wiz . cleanHouse ( Ooo000O00 )
  xbmc . sleep ( 200 )
  try : shutil . rmtree ( Ooo000O00 )
  except Exception , I111I11I111 : wiz . log ( "Error removing %s" % addon , xbmc . LOGNOTICE )
  ooo0O0OOo0OoO ( addon , name , over )
 if over == False :
  wiz . LogNotify ( "[COLOR %s]%s[/COLOR]" % ( oOOo0O00o , o0OOO ) , "[COLOR %s]%s Removed[/COLOR]" % ( iIiIi11 , name ) )
  if 51 - 51: OoooooooOO + I1I1i1 * iIii1I11I1II1 * IIIi1i1I / i1IIi
def ooo0O0OOo0OoO ( addon , name = None , over = False ) :
 if addon == 'all' :
  if iiIIIII1i1iI . yesno ( o0OOO , '[COLOR %s]Would you like to remove [COLOR %s]ALL[/COLOR] addon data stored in you Userdata folder?[/COLOR]' % ( iIiIi11 , oOOo0O00o ) , yeslabel = '[B][COLOR green]Remove Data[/COLOR][/B]' , nolabel = '[B][COLOR red]Don\'t Remove[/COLOR][/B]' ) :
   wiz . cleanHouse ( ooOOOo0oo0O0 )
  else : wiz . LogNotify ( '[COLOR %s]Remove Addon Data[/COLOR]' % oOOo0O00o , '[COLOR %s]Cancelled![/COLOR]' % iIiIi11 )
 elif addon == 'uninstalled' :
  if iiIIIII1i1iI . yesno ( o0OOO , '[COLOR %s]Would you like to remove [COLOR %s]ALL[/COLOR] addon data stored in you Userdata folder for uninstalled addons?[/COLOR]' % ( iIiIi11 , oOOo0O00o ) , yeslabel = '[B][COLOR green]Remove Data[/COLOR][/B]' , nolabel = '[B][COLOR red]Don\'t Remove[/COLOR][/B]' ) :
   o00oO0o0o = 0
   for Ooo000O00 in glob . glob ( os . path . join ( ooOOOo0oo0O0 , '*' ) ) :
    i1iI1Iiii1I = Ooo000O00 . replace ( ooOOOo0oo0O0 , '' ) . replace ( '\\' , '' ) . replace ( '/' , '' )
    if i1iI1Iiii1I in Iii1I1I11iiI1 : pass
    elif os . path . exists ( os . path . join ( O0O , i1iI1Iiii1I ) ) : pass
    else : wiz . cleanHouse ( Ooo000O00 ) ; o00oO0o0o += 1 ; wiz . log ( Ooo000O00 ) ; shutil . rmtree ( Ooo000O00 )
   wiz . LogNotify ( '[COLOR %s]Clean up Uninstalled[/COLOR]' % oOOo0O00o , '[COLOR %s]%s Folders(s) Removed[/COLOR]' % ( iIiIi11 , o00oO0o0o ) )
  else : wiz . LogNotify ( '[COLOR %s]Remove Addon Data[/COLOR]' % oOOo0O00o , '[COLOR %s]Cancelled![/COLOR]' % iIiIi11 )
 elif addon == 'empty' :
  if iiIIIII1i1iI . yesno ( o0OOO , '[COLOR %s]Would you like to remove [COLOR %s]ALL[/COLOR] empty addon data folders in you Userdata folder?[/COLOR]' % ( iIiIi11 , oOOo0O00o ) , yeslabel = '[B][COLOR green]Remove Data[/COLOR][/B]' , nolabel = '[B][COLOR red]Don\'t Remove[/COLOR][/B]' ) :
   o00oO0o0o = wiz . emptyfolder ( ooOOOo0oo0O0 )
   wiz . LogNotify ( '[COLOR %s]Remove Empty Folders[/COLOR]' % oOOo0O00o , '[COLOR %s]%s Folders(s) Removed[/COLOR]' % ( iIiIi11 , o00oO0o0o ) )
  else : wiz . LogNotify ( '[COLOR %s]Remove Empty Folders[/COLOR]' % oOOo0O00o , '[COLOR %s]Cancelled![/COLOR]' % iIiIi11 )
 else :
  I11IiI1i = os . path . join ( oOo00Oo00O , 'addon_data' , addon )
  if addon in Iii1I1I11iiI1 :
   wiz . LogNotify ( "[COLOR %s]Protected Plugin[/COLOR]" % oOOo0O00o , "[COLOR %s]Not allowed to remove Addon_Data[/COLOR]" % iIiIi11 )
  elif os . path . exists ( I11IiI1i ) :
   if iiIIIII1i1iI . yesno ( o0OOO , '[COLOR %s]Would you also like to remove the addon data for:[/COLOR]' % iIiIi11 , '[COLOR %s]%s[/COLOR]' % ( oOOo0O00o , addon ) , yeslabel = '[B][COLOR green]Remove Data[/COLOR][/B]' , nolabel = '[B][COLOR red]Don\'t Remove[/COLOR][/B]' ) :
    wiz . cleanHouse ( I11IiI1i )
    try :
     shutil . rmtree ( I11IiI1i )
    except :
     wiz . log ( "Error deleting: %s" % I11IiI1i )
   else :
    wiz . log ( 'Addon data for %s was not removed' % addon )
 wiz . refresh ( )
 if 81 - 81: iIii1I11I1II1 / IIIi1i1I . i11iIiiIii * II111iiii
def o0oOOoo0O ( type ) :
 if type == 'build' :
  iiIi = OO0IIIIIIi111i ( 'restore' )
  if iiIi == False : wiz . LogNotify ( "[COLOR %s]%s[/COLOR]" % ( oOOo0O00o , o0OOO ) , "[COLOR %s]Local Restore Cancelled[/COLOR]" % iIiIi11 ) ; return
 if not wiz . currSkin ( ) in [ 'skin.confluence' , 'skin.estuary' ] :
  wiz . skinToDefault ( )
 wiz . restoreLocal ( type )
 if 57 - 57: ooOo . i11iIiiIii * II111iiii + OoooooooOO + IiiIII111ii
def OoO0o0oOOO ( type ) :
 if type == 'build' :
  iiIi = OO0IIIIIIi111i ( 'restore' )
  if iiIi == False : wiz . LogNotify ( "[COLOR %s]%s[/COLOR]" % ( oOOo0O00o , o0OOO ) , "[COLOR %s]External Restore Cancelled[/COLOR]" % iIiIi11 ) ; return
 wiz . restoreExternal ( type )
 if 86 - 86: o0o0Oo0oooo0 . i1Ii
def I1I1i1I1I1I1 ( name ) :
 if wiz . workingURL ( I1I1i1I ) == True :
  if wiz . checkBuild ( name , 'url' ) :
   name , O0OOO0OOooo00 , OOOoO000 , oOOOO , Ii , Ii1ii111i1 , i1i1i1I , oOoo000 , IiiIIIII1iii , OooOo00o , IiI11i1IIiiI , oOOo000oOoO0 = wiz . checkBuild ( name , 'all' )
   OooOo00o = 'Yes' if OooOo00o . lower ( ) == 'yes' else 'No'
   O0O00oO0OoO0o = "[COLOR %s]Build Name:[/COLOR] [COLOR %s]%s[/COLOR][CR]" % ( iIiIi11 , oOOo0O00o , name )
   O0O00oO0OoO0o += "[COLOR %s]Build Version:[/COLOR] [COLOR %s]%s[/COLOR][CR]" % ( iIiIi11 , oOOo0O00o , O0OOO0OOooo00 )
   if not Ii1ii111i1 == "http://" :
    iI11IiIiiII1 = wiz . themeCount ( name , False )
    O0O00oO0OoO0o += "[COLOR %s]Build Theme(s):[/COLOR] [COLOR %s]%s[/COLOR][CR]" % ( iIiIi11 , oOOo0O00o , ', ' . join ( iI11IiIiiII1 ) )
   O0O00oO0OoO0o += "[COLOR %s]Kodi Version:[/COLOR] [COLOR %s]%s[/COLOR][CR]" % ( iIiIi11 , oOOo0O00o , Ii )
   O0O00oO0OoO0o += "[COLOR %s]Adult Content:[/COLOR] [COLOR %s]%s[/COLOR][CR]" % ( iIiIi11 , oOOo0O00o , OooOo00o )
   O0O00oO0OoO0o += "[COLOR %s]Description:[/COLOR] [COLOR %s]%s[/COLOR][CR]" % ( iIiIi11 , oOOo0O00o , IiI11i1IIiiI )
   wiz . TextBox ( o0OOO , O0O00oO0OoO0o )
  else : wiz . log ( "Invalid Build Name!" )
 else : wiz . log ( "Build text file not working: %s" % WORKINGURL )
 if 15 - 15: OOoooooO - O0 % ooOo . OoooooooOO * Ooo0O / O0
def IIi1I ( name ) :
 if wiz . workingURL ( I1I1i1I ) == True :
  ii1I11iI = wiz . checkBuild ( name , 'preview' )
  if ii1I11iI and not ii1I11iI == 'http://' : O0OooooO0o0O0 ( ii1I11iI )
  else : wiz . log ( "[%s]Unable to find url for video preview" % name )
 else : wiz . log ( "Build text file not working: %s" % WORKINGURL )
 if 85 - 85: iii11iiII + II111iiii - iii11iiII * IIIi1i1I - i1IIi % iiIIi1IiIi11
def IiIiI ( plugin ) :
 IIIiIi1iiI = os . path . join ( O0O , plugin , 'addon.xml' )
 if os . path . exists ( IIIiIi1iiI ) :
  iiiii1I1III1 = open ( IIIiIi1iiI , mode = 'r' ) ; o0O0Oo00 = iiiii1I1III1 . read ( ) ; iiiii1I1III1 . close ( ) ;
  O0Oo0o000oO = wiz . parseDOM ( o0O0Oo00 , 'import' , ret = 'addon' )
  iI1Ii11 = [ ]
  for i1oO00O in O0Oo0o000oO :
   if not 'xbmc.python' in i1oO00O :
    iI1Ii11 . append ( i1oO00O )
  return iI1Ii11
 return [ ]
 if 93 - 93: ooOo / OOoooooO / i11IiIiiIIIII + II111iiii + i11iIiiIii
def iiiII1III ( do ) :
 if do == 'import' :
  I1iIiiIi11I1i = os . path . join ( o0 , 'temp' )
  if not os . path . exists ( I1iIiiIi11I1i ) : os . makedirs ( I1iIiiIi11I1i )
  iiiii1I1III1 = iiIIIII1i1iI . browse ( 1 , '[COLOR %s]Select the location of the SaveData.zip[/COLOR]' % iIiIi11 , 'files' , '.zip' , False , False , o00 )
  if not iiiii1I1III1 . endswith ( '.zip' ) :
   wiz . LogNotify ( "[COLOR %s]%s[/COLOR]" % ( oOOo0O00o , o0OOO ) , "[COLOR %s]Import Data Error![/COLOR]" % ( iIiIi11 ) )
   return
  oO0oOOO0o0O0 = os . path . join ( O0ooO0Oo00o , 'SaveData.zip' )
  iI1o0 = xbmcvfs . copy ( iiiii1I1III1 , oO0oOOO0o0O0 )
  wiz . log ( "%s" % str ( iI1o0 ) )
  extract . all ( xbmc . translatePath ( oO0oOOO0o0O0 ) , I1iIiiIi11I1i )
  i1iOO = os . path . join ( I1iIiiIi11I1i , 'trakt' )
  IIIi = os . path . join ( I1iIiiIi11I1i , 'login' )
  i1IIOO0oo00oOO = os . path . join ( I1iIiiIi11I1i , 'debrid' )
  iiIi = 0
  if os . path . exists ( i1iOO ) :
   iiIi += 1
   iIi1Ii1111i = os . listdir ( i1iOO )
   if not os . path . exists ( traktit . TRAKTFOLD ) : os . makedirs ( traktit . TRAKTFOLD )
   for ii1IIIIiI11 in iIi1Ii1111i :
    i1iooO0oO0o = os . path . join ( traktit . TRAKTFOLD , ii1IIIIiI11 )
    IIiIiiI1i = os . path . join ( i1iOO , ii1IIIIiI11 )
    if os . path . exists ( i1iooO0oO0o ) :
     if not iiIIIII1i1iI . yesno ( o0OOO , "[COLOR %s]Would you like replace the current [COLOR %s]%s[/COLOR] file?" % ( iIiIi11 , oOOo0O00o , ii1IIIIiI11 ) , yeslabel = "[B][COLOR green]Yes Replace[/COLOR][/B]" , nolabel = "[B][COLOR red]No Skip[/COLOR][/B]" ) : continue
     else : os . remove ( i1iooO0oO0o )
    shutil . copy ( IIiIiiI1i , i1iooO0oO0o )
   traktit . importlist ( 'all' )
   traktit . traktIt ( 'restore' , 'all' )
  if os . path . exists ( IIIi ) :
   iiIi += 1
   iIi1Ii1111i = os . listdir ( IIIi )
   if not os . path . exists ( loginit . LOGINFOLD ) : os . makedirs ( loginit . LOGINFOLD )
   for ii1IIIIiI11 in iIi1Ii1111i :
    i1iooO0oO0o = os . path . join ( loginit . LOGINFOLD , ii1IIIIiI11 )
    IIiIiiI1i = os . path . join ( IIIi , ii1IIIIiI11 )
    if os . path . exists ( i1iooO0oO0o ) :
     if not iiIIIII1i1iI . yesno ( o0OOO , "[COLOR %s]Would you like replace the current [COLOR %s]%s[/COLOR] file?" % ( iIiIi11 , oOOo0O00o , ii1IIIIiI11 ) , yeslabel = "[B][COLOR green]Yes Replace[/COLOR][/B]" , nolabel = "[B][COLOR red]No Skip[/COLOR][/B]" ) : continue
     else : os . remove ( i1iooO0oO0o )
    shutil . copy ( IIiIiiI1i , i1iooO0oO0o )
   loginit . importlist ( 'all' )
   loginit . loginIt ( 'restore' , 'all' )
  if os . path . exists ( i1IIOO0oo00oOO ) :
   iiIi += 1
   iIi1Ii1111i = os . listdir ( i1IIOO0oo00oOO )
   if not os . path . exists ( debridit . REALFOLD ) : os . makedirs ( debridit . REALFOLD )
   for ii1IIIIiI11 in iIi1Ii1111i :
    i1iooO0oO0o = os . path . join ( debridit . REALFOLD , ii1IIIIiI11 )
    IIiIiiI1i = os . path . join ( i1IIOO0oo00oOO , ii1IIIIiI11 )
    if os . path . exists ( i1iooO0oO0o ) :
     if not iiIIIII1i1iI . yesno ( o0OOO , "[COLOR %s]Would you like replace the current [COLOR %s]%s[/COLOR] file?" % ( iIiIi11 , oOOo0O00o , ii1IIIIiI11 ) , yeslabel = "[B][COLOR green]Yes Replace[/COLOR][/B]" , nolabel = "[B][COLOR red]No Skip[/COLOR][/B]" ) : continue
     else : os . remove ( i1iooO0oO0o )
    shutil . copy ( IIiIiiI1i , i1iooO0oO0o )
   debridit . importlist ( 'all' )
   debridit . debridIt ( 'restore' , 'all' )
  wiz . cleanHouse ( I1iIiiIi11I1i )
  wiz . removeFolder ( I1iIiiIi11I1i )
  os . remove ( oO0oOOO0o0O0 )
  if iiIi == 0 : wiz . LogNotify ( "[COLOR %s]%s[/COLOR]" % ( oOOo0O00o , o0OOO ) , "[COLOR %s]Save Data Import Failed[/COLOR]" % iIiIi11 )
  else : wiz . LogNotify ( "[COLOR %s]%s[/COLOR]" % ( oOOo0O00o , o0OOO ) , "[COLOR %s]Save Data Import Complete[/COLOR]" % iIiIi11 )
 elif do == 'export' :
  IIiII11 = xbmc . translatePath ( O0ooO0Oo00o )
  dir = [ traktit . TRAKTFOLD , debridit . REALFOLD , loginit . LOGINFOLD ]
  traktit . traktIt ( 'update' , 'all' )
  loginit . loginIt ( 'update' , 'all' )
  debridit . debridIt ( 'update' , 'all' )
  iiiii1I1III1 = iiIIIII1i1iI . browse ( 3 , '[COLOR %s]Select where you wish to export the savedata zip?[/COLOR]' % iIiIi11 , 'files' , '' , False , True , o00 )
  iiiii1I1III1 = xbmc . translatePath ( iiiii1I1III1 )
  oo0O00OOOOO = os . path . join ( IIiII11 , 'SaveData.zip' )
  OoO = zipfile . ZipFile ( oo0O00OOOOO , mode = 'w' )
  for IiI11I111 in dir :
   if os . path . exists ( IiI11I111 ) :
    iIi1Ii1111i = os . listdir ( IiI11I111 )
    for file in iIi1Ii1111i :
     OoO . write ( os . path . join ( IiI11I111 , file ) , os . path . join ( IiI11I111 , file ) . replace ( o0 , '' ) , zipfile . ZIP_DEFLATED )
  OoO . close ( )
  if iiiii1I1III1 == IIiII11 :
   iiIIIII1i1iI . ok ( o0OOO , "[COLOR %s]Save data has been backed up to:[/COLOR]" % ( iIiIi11 ) , "[COLOR %s]%s[/COLOR]" % ( oOOo0O00o , oo0O00OOOOO ) )
  else :
   try :
    xbmcvfs . copy ( oo0O00OOOOO , os . path . join ( iiiii1I1III1 , 'SaveData.zip' ) )
    iiIIIII1i1iI . ok ( o0OOO , "[COLOR %s]Save data has been backed up to:[/COLOR]" % ( iIiIi11 ) , "[COLOR %s]%s[/COLOR]" % ( oOOo0O00o , os . path . join ( iiiii1I1III1 , 'SaveData.zip' ) ) )
   except :
    iiIIIII1i1iI . ok ( o0OOO , "[COLOR %s]Save data has been backed up to:[/COLOR]" % ( iIiIi11 ) , "[COLOR %s]%s[/COLOR]" % ( oOOo0O00o , oo0O00OOOOO ) )
    if 18 - 18: Ooo0O - iii11iiII * II111iiii + IIIi1i1I
def II1i111 ( url ) :
 o00O00Oo00O = urllib2 . Request ( url )
 o00O00Oo00O . add_header ( 'User-Agent' , 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3' )
 IIii1I1I1I = urllib2 . urlopen ( o00O00Oo00O )
 o0O0Oo00 = IIii1I1I1I . read ( )
 IIii1I1I1I . close ( )
 return o0O0Oo00
 if 93 - 93: iiIIi1IiIi11 * IIIi1i1I . I1111 - IiiIII111ii + O0 * I1111
def oOoOO ( url ) :
 if url == 'http://' : return False
 try :
  o00O00Oo00O = urllib2 . Request ( url )
  o00O00Oo00O . add_header ( 'User-Agent' , USER_AGENT )
  IIii1I1I1I = urllib2 . urlopen ( o00O00Oo00O )
  IIii1I1I1I . close ( )
 except Exception , I111I11I111 :
  return I111I11I111
 return True
 if 20 - 20: OOoooooO . I1111 * iiIIi1IiIi11
 if 71 - 71: Ooo0O . II111iiii / II111iiii * IiiIII111ii * I1111
 if 25 - 25: i11iIiiIii + Ooo0O . iiIIi1IiIi11 % ooOo - OOoooooO * i1IIi
 if 98 - 98: iiIIi1IiIi11 - iiIIi1IiIi11
def OO0IIIIIIi111i ( install = None , over = False ) :
 if o0O0OOO0Ooo == 'true' :
  traktit . autoUpdate ( 'all' )
  wiz . setS ( 'traktlastsave' , str ( I1IiiiiI ) )
 if iiIiII1 == 'true' :
  debridit . autoUpdate ( 'all' )
  wiz . setS ( 'debridlastsave' , str ( I1IiiiiI ) )
 if OOO00O0O == 'true' :
  loginit . autoUpdate ( 'all' )
  wiz . setS ( 'loginlastsave' , str ( I1IiiiiI ) )
 if over == True : I1iIiIii = 1
 elif install == 'restore' : I1iIiIii = iiIIIII1i1iI . yesno ( o0OOO , "[COLOR %s]Do you wish to restore your" % iIiIi11 , "Kodi configuration to default settings" , "Before installing the local backup?[/COLOR]" , nolabel = '[B][COLOR red]No, Cancel[/COLOR][/B]' , yeslabel = '[B][COLOR green]Continue[/COLOR][/B]' )
 elif install : I1iIiIii = iiIIIII1i1iI . yesno ( o0OOO , "[COLOR %s]Do you wish to restore your" % iIiIi11 , "Kodi configuration to default settings" , "Before installing [COLOR %s]%s[/COLOR]?" % ( oOOo0O00o , install ) , nolabel = '[B][COLOR red]No, Cancel[/COLOR][/B]' , yeslabel = '[B][COLOR green]Continue[/COLOR][/B]' )
 else : I1iIiIii = iiIIIII1i1iI . yesno ( o0OOO , "[COLOR %s]Do you wish to restore your" % iIiIi11 , "Kodi configuration to default settings?[/COLOR]" , nolabel = '[B][COLOR red]No, Cancel[/COLOR][/B]' , yeslabel = '[B][COLOR green]Continue[/COLOR][/B]' )
 if I1iIiIii :
  if not wiz . currSkin ( ) in [ 'skin.confluence' , 'skin.estuary' ] :
   I111Iii1 = 'skin.confluence' if o0OIiII < 17 else 'skin.estuary'
   if 58 - 58: IIIi1i1I
   if 98 - 98: I1I1i1 * I1111
   skinSwitch . swapSkins ( I111Iii1 )
   iiIi = 0
   xbmc . sleep ( 1000 )
   while not xbmc . getCondVisibility ( "Window.isVisible(yesnodialog)" ) and iiIi < 150 :
    iiIi += 1
    xbmc . sleep ( 200 )
    wiz . ebi ( 'SendAction(Select)' )
   if xbmc . getCondVisibility ( "Window.isVisible(yesnodialog)" ) :
    wiz . ebi ( 'SendClick(11)' )
   else : wiz . LogNotify ( "[COLOR %s]%s[/COLOR]" % ( oOOo0O00o , o0OOO ) , '[COLOR %s]Fresh Install: Skin Swap Timed Out![/COLOR]' % iIiIi11 ) ; return False
   xbmc . sleep ( 1000 )
  if not wiz . currSkin ( ) in [ 'skin.confluence' , 'skin.estuary' ] :
   wiz . LogNotify ( "[COLOR %s]%s[/COLOR]" % ( oOOo0O00o , o0OOO ) , '[COLOR %s]Fresh Install: Skin Swap Failed![/COLOR]' % iIiIi11 )
   return
  wiz . addonUpdates ( 'set' )
  II11IiI1 = os . path . abspath ( o00 )
  oo00 . create ( o0OOO , "[COLOR %s]Calculating files and folders" % iIiIi11 , '' , 'Please Wait![/COLOR]' )
  iIIi11i = sum ( [ len ( iIi1Ii1111i ) for IIIiiIi111Ii1II , oOoo0oO , iIi1Ii1111i in os . walk ( II11IiI1 ) ] ) ; IIii1i = 0
  oo00 . update ( 0 , "[COLOR %s]Gathering Excludes list." % iIiIi11 )
  Iii1I1I11iiI1 . append ( 'My_Builds' )
  Iii1I1I11iiI1 . append ( 'archive_cache' )
  if IIII == 'true' :
   III1IiI1i1i = glob . glob ( os . path . join ( O0O , 'repo*/' ) )
   for ii1IIIIiI11 in III1IiI1i1i :
    o00oo = os . path . split ( ii1IIIIiI11 [ : - 1 ] ) [ 1 ]
    if not o00oo == Iii1I1I11iiI1 :
     Iii1I1I11iiI1 . append ( o00oo )
  if iiIiI == 'true' :
   Iii1I1I11iiI1 . append ( 'plugin.program.super.favourites' )
  if o00oooO0Oo == 'true' :
   Ii11IIIi1 = ''
   o0o0oo0Ooo = wiz . whiteList ( 'read' )
   if len ( o0o0oo0Ooo ) > 0 :
    for ii1IIIIiI11 in o0o0oo0Ooo :
     try : oO0o00oOOooO0 , id , IiI11I111 = ii1IIIIiI11
     except : pass
     if IiI11I111 . startswith ( 'pvr' ) : Ii11IIIi1 = id
     i1oO00O = IiIiI ( IiI11I111 )
     for ooooooo00oO0OO in i1oO00O :
      if not ooooooo00oO0OO in Iii1I1I11iiI1 :
       Iii1I1I11iiI1 . append ( ooooooo00oO0OO )
      IIIii11 = IiIiI ( ooooooo00oO0OO )
      for i1i11I1I1 in IIIii11 :
       if not i1i11I1I1 in Iii1I1I11iiI1 :
        Iii1I1I11iiI1 . append ( i1i11I1I1 )
     if not IiI11I111 in Iii1I1I11iiI1 :
      Iii1I1I11iiI1 . append ( IiI11I111 )
    if not Ii11IIIi1 == '' : wiz . setS ( 'pvrclient' , IiI11I111 )
  if wiz . getS ( 'pvrclient' ) == '' :
   for ii1IIIIiI11 in Iii1I1I11iiI1 :
    if ii1IIIIiI11 . startswith ( 'pvr' ) :
     wiz . setS ( 'pvrclient' , ii1IIIIiI11 )
  oo00 . update ( 0 , "[COLOR %s]Clearing out files and folders:" % iIiIi11 )
  OOOOOoooO = wiz . latestDB ( 'Addons' )
  for oO0Oooo0OoO , Iiii1IIIIiiI11 , iIi1Ii1111i in os . walk ( II11IiI1 , topdown = True ) :
   Iiii1IIIIiiI11 [ : ] = [ oOoo0oO for oOoo0oO in Iiii1IIIIiiI11 if oOoo0oO not in Iii1I1I11iiI1 ]
   for oO0o00oOOooO0 in iIi1Ii1111i :
    IIii1i += 1
    IiI11I111 = oO0Oooo0OoO . replace ( '/' , '\\' ) . split ( '\\' )
    iiIi = len ( IiI11I111 ) - 1
    if oO0o00oOOooO0 == 'sources.xml' and IiI11I111 [ - 1 ] == 'userdata' and ooOOoooooo == 'true' : wiz . log ( "Keep Sources: %s" % os . path . join ( oO0Oooo0OoO , oO0o00oOOooO0 ) , xbmc . LOGNOTICE )
    elif oO0o00oOOooO0 == 'favourites.xml' and IiI11I111 [ - 1 ] == 'userdata' and IiIIIi1iIi == 'true' : wiz . log ( "Keep Favourites: %s" % os . path . join ( oO0Oooo0OoO , oO0o00oOOooO0 ) , xbmc . LOGNOTICE )
    elif oO0o00oOOooO0 == 'profiles.xml' and IiI11I111 [ - 1 ] == 'userdata' and II1I == 'true' : wiz . log ( "Keep Profiles: %s" % os . path . join ( oO0Oooo0OoO , oO0o00oOOooO0 ) , xbmc . LOGNOTICE )
    elif oO0o00oOOooO0 == 'advancedsettings.xml' and IiI11I111 [ - 1 ] == 'userdata' and O0i1II1Iiii1I11 == 'true' : wiz . log ( "Keep Advanced Settings: %s" % os . path . join ( oO0Oooo0OoO , oO0o00oOOooO0 ) , xbmc . LOGNOTICE )
    elif oO0o00oOOooO0 in Ooo0oOooo0 : wiz . log ( "Keep Log File: %s" % oO0o00oOOooO0 , xbmc . LOGNOTICE )
    elif oO0o00oOOooO0 . endswith ( '.db' ) :
     try :
      if oO0o00oOOooO0 == OOOOOoooO and o0OIiII >= 17 : wiz . log ( "Ignoring %s on v%s" % ( oO0o00oOOooO0 , o0OIiII ) , xbmc . LOGNOTICE )
      else : os . remove ( os . path . join ( oO0Oooo0OoO , oO0o00oOOooO0 ) )
     except Exception , I111I11I111 :
      if not oO0o00oOOooO0 . startswith ( 'Textures13' ) :
       wiz . log ( 'Failed to delete, Purging DB' , xbmc . LOGNOTICE )
       wiz . log ( "-> %s" % ( str ( I111I11I111 ) ) , xbmc . LOGNOTICE )
       wiz . purgeDb ( os . path . join ( oO0Oooo0OoO , oO0o00oOOooO0 ) )
    else :
     oo00 . update ( int ( wiz . percentage ( IIii1i , iIIi11i ) ) , '' , '[COLOR %s]File: [/COLOR][COLOR %s]%s[/COLOR]' % ( iIiIi11 , oOOo0O00o , oO0o00oOOooO0 ) , '' )
     try : os . remove ( os . path . join ( oO0Oooo0OoO , oO0o00oOOooO0 ) )
     except Exception , I111I11I111 :
      wiz . log ( "Error removing %s" % os . path . join ( oO0Oooo0OoO , oO0o00oOOooO0 ) , xbmc . LOGNOTICE )
      wiz . log ( "-> / %s" % ( str ( I111I11I111 ) ) , xbmc . LOGNOTICE )
   if oo00 . iscanceled ( ) :
    oo00 . close ( )
    wiz . LogNotify ( "[COLOR %s]%s[/COLOR]" % ( oOOo0O00o , o0OOO ) , "[COLOR %s]Fresh Start Cancelled[/COLOR]" % iIiIi11 )
    return False
  for oO0Oooo0OoO , Iiii1IIIIiiI11 , iIi1Ii1111i in os . walk ( II11IiI1 , topdown = True ) :
   Iiii1IIIIiiI11 [ : ] = [ oOoo0oO for oOoo0oO in Iiii1IIIIiiI11 if oOoo0oO not in Iii1I1I11iiI1 ]
   for oO0o00oOOooO0 in Iiii1IIIIiiI11 :
    oo00 . update ( 100 , '' , 'Cleaning Up Empty Folder: [COLOR %s]%s[/COLOR]' % ( oOOo0O00o , oO0o00oOOooO0 ) , '' )
    if oO0o00oOOooO0 not in [ "Database" , "userdata" , "temp" , "addons" , "addon_data" ] :
     shutil . rmtree ( os . path . join ( oO0Oooo0OoO , oO0o00oOOooO0 ) , ignore_errors = True , onerror = None )
   if oo00 . iscanceled ( ) :
    oo00 . close ( )
    wiz . LogNotify ( "[COLOR %s]%s[/COLOR]" % ( oOOo0O00o , o0OOO ) , "[COLOR %s]Fresh Start Cancelled[/COLOR]" % iIiIi11 )
    return False
  oo00 . close ( )
  wiz . clearS ( 'build' )
  if over == True :
   return True
  elif install == 'restore' :
   return True
  elif install :
   i1iI1Ii11Ii1 ( install , 'normal' , over = True )
  else :
   if I11i1I1I == 1 : iiIIi1 = 1
   elif I11i1I1I == 2 : iiIIi1 = 0
   else : iiIIi1 = iiIIIII1i1iI . yesno ( o0OOO , "[COLOR %s]Would you like to [COLOR %s]Force close[/COLOR] kodi or [COLOR %s]Reload Profile[/COLOR]?[/COLOR]" % ( iIiIi11 , oOOo0O00o , oOOo0O00o ) , yeslabel = "[B][COLOR red]Reload Profile[/COLOR][/B]" , nolabel = "[B][COLOR green]Force Close[/COLOR][/B]" )
   if iiIIi1 == 1 : wiz . reloadFix ( 'fresh' )
   else : wiz . addonUpdates ( 'reset' ) ; wiz . killxbmc ( True )
 else :
  if not install == 'restore' :
   wiz . LogNotify ( "[COLOR %s]%s[/COLOR]" % ( oOOo0O00o , o0OOO ) , '[COLOR %s]Fresh Install: Cancelled![/COLOR]' % iIiIi11 )
   wiz . refresh ( )
   if 8 - 8: IiiIII111ii + ooOo / iiIIi1IiIi11 / OOoooooO + iIii1I11I1II1 + OoooooooOO
   if 33 - 33: II111iiii - i1Ii - OOoooooO
   if 92 - 92: I1111 * i1Ii
   if 92 - 92: IIIi1i1I
def i1i1IIiII1I ( ) :
 if iiIIIII1i1iI . yesno ( o0OOO , '[COLOR %s]Would you like to clear cache?[/COLOR]' % iIiIi11 , nolabel = '[B][COLOR red]No, Cancel[/COLOR][/B]' , yeslabel = '[B][COLOR green]Clear Cache[/COLOR][/B]' ) :
  wiz . clearCache ( )
  if 85 - 85: Ooo0O . i11iIiiIii - i11iIiiIii . ooOo . I1111 % OoooooooOO
  if 20 - 20: OO00O0O0O00Oo + OO00O0O0O00Oo * II111iiii * iIii1I11I1II1 % O0 * ooOo
def OooOoO0OOoOOO0o0o ( ) :
 if iiIIIII1i1iI . yesno ( o0OOO , '[COLOR %s]Would you like to clear cache, packages and thumbnails?[/COLOR]' % iIiIi11 , nolabel = '[B][COLOR red]Cancel Process[/COLOR][/B]' , yeslabel = '[B][COLOR green]Clean All[/COLOR][/B]' ) :
  wiz . clearCache ( )
  wiz . clearPackages ( 'total' )
  iIOoo0ooo0oo ( 'total' )
  if 21 - 21: i1Ii - ooOo % OoooooooOO + I1I1i1
def iIOoo0ooo0oo ( type = None ) :
 o00O0o = wiz . latestDB ( 'Textures' )
 if not type == None : i1I1IiI1ii = 1
 else : i1I1IiI1ii = iiIIIII1i1iI . yesno ( o0OOO , '[COLOR %s]Would you like to delete the %s and Thumbnails folder?' % ( iIiIi11 , o00O0o ) , "They will repopulate on the next startup[/COLOR]" , nolabel = '[B][COLOR red]Don\'t Delete[/COLOR][/B]' , yeslabel = '[B][COLOR green]Delete Thumbs[/COLOR][/B]' )
 if i1I1IiI1ii == 1 :
  try : wiz . removeFile ( os . join ( OOOO , o00O0o ) )
  except : wiz . log ( 'Failed to delete, Purging DB.' ) ; wiz . purgeDb ( o00O0o )
  wiz . removeFolder ( oOoOooOo0o0 )
  if 28 - 28: ooOo
 else : wiz . log ( 'Clear thumbnames cancelled' )
 wiz . redoThumbs ( )
 if 87 - 87: i1Ii . i1IIi % OoooooooOO * i11iIiiIii
def o0oOo ( ) :
 OoIIiIIIII1I = [ ] ; II1IIii1ii = [ ]
 for ooiiI , o00iIiI1iI1Ii1 , iIi1Ii1111i in os . walk ( o00 ) :
  for OO0OOoo0OOO in fnmatch . filter ( iIi1Ii1111i , '*.db' ) :
   if OO0OOoo0OOO != 'Thumbs.db' :
    iioO = os . path . join ( ooiiI , OO0OOoo0OOO )
    OoIIiIIIII1I . append ( iioO )
    dir = iioO . replace ( '\\' , '/' ) . split ( '/' )
    II1IIii1ii . append ( '(%s) %s' % ( dir [ len ( dir ) - 2 ] , dir [ len ( dir ) - 1 ] ) )
 if o0OIiII >= 16 :
  i1I1IiI1ii = iiIIIII1i1iI . multiselect ( "[COLOR %s]Select DB File to Purge[/COLOR]" % iIiIi11 , II1IIii1ii )
  if i1I1IiI1ii == None : wiz . LogNotify ( "[COLOR %s]Purge Database[/COLOR]" % oOOo0O00o , "[COLOR %s]Cancelled[/COLOR]" % iIiIi11 )
  elif len ( i1I1IiI1ii ) == 0 : wiz . LogNotify ( "[COLOR %s]Purge Database[/COLOR]" % oOOo0O00o , "[COLOR %s]Cancelled[/COLOR]" % iIiIi11 )
  else :
   for ii11I in i1I1IiI1ii : wiz . purgeDb ( OoIIiIIIII1I [ ii11I ] )
 else :
  i1I1IiI1ii = iiIIIII1i1iI . select ( "[COLOR %s]Select DB File to Purge[/COLOR]" % iIiIi11 , II1IIii1ii )
  if i1I1IiI1ii == - 1 : wiz . LogNotify ( "[COLOR %s]Purge Database[/COLOR]" % oOOo0O00o , "[COLOR %s]Cancelled[/COLOR]" % iIiIi11 )
  else : wiz . purgeDb ( OoIIiIIIII1I [ ii11I ] )
  if 97 - 97: i1IIi + iiIIi1IiIi11 . OOoooooO - iiIIi1IiIi11
  if 53 - 53: O0 . ooOo
  if 74 - 74: OOoooooO % o0o0Oo0oooo0 / Ooo0O
  if 2 - 2: i1Ii % i1Ii % OO00O0O0O00Oo
def o0o00OoOo0 ( ) :
 OOOoO000 = wiz . workingURL ( O0O0OOOOoo )
 if OOOoO000 == True :
  try :
   id , O0O00oO0OoO0o = wiz . splitNotify ( O0O0OOOOoo )
   if id == False : wiz . LogNotify ( "[COLOR %s]%s[/COLOR]" % ( oOOo0O00o , o0OOO ) , "[COLOR %s]Notification: Not Formated Correctly[/COLOR]" % iIiIi11 ) ; return
   notify . notification ( O0O00oO0OoO0o , True )
  except Exception , I111I11I111 :
   wiz . log ( "Error on Notifications Window: %s" % str ( I111I11I111 ) , xbmc . LOGERROR )
 else : wiz . LogNotify ( "[COLOR %s]%s[/COLOR]" % ( oOOo0O00o , o0OOO ) , "[COLOR %s]Invalid URL for Notification[/COLOR]" % iIiIi11 )
 if 98 - 98: OoooooooOO % IIIi1i1I * OOoooooO
def OO0Oo00OO0oo ( ) :
 if O000oo0O == "" :
  notify . updateWindow ( )
 else :
  notify . updateWindow ( O000oo0O , oo0OooOOo0 , O00oO , wiz . checkBuild ( O000oo0O , 'icon' ) , wiz . checkBuild ( O000oo0O , 'fanart' ) )
  if 53 - 53: I1111 - OOoooooO + IiiIII111ii
def I1Ii1II ( ) :
 notify . firstRun ( )
 if 31 - 31: i11iIiiIii % i11iIiiIii
def IiIiiI1iii1iIiiI ( ) :
 notify . firstRunSettings ( )
 if 36 - 36: I1111 - O0 * ooOo / oO0 / iii11iiII
 if 33 - 33: OoooooooOO % oO0 . O0 / oO0
 if 63 - 63: i1Ii + iIii1I11I1II1 + ooOo + OO00O0O0O00Oo
 if 72 - 72: I1111 + i11iIiiIii + oO0
 if 96 - 96: IIIi1i1I % i1IIi / I1I1i1
def Ii1IIi11 ( display , mode = None , name = None , url = None , menu = None , description = o0OOO , overwrite = True , fanart = OOO00 , icon = iiiiiIIii , themeit = None ) :
 i1ooO = sys . argv [ 0 ]
 if not mode == None : i1ooO += "?mode=%s" % urllib . quote_plus ( mode )
 if not name == None : i1ooO += "&name=" + urllib . quote_plus ( name )
 if not url == None : i1ooO += "&url=" + urllib . quote_plus ( url )
 i11iii1Ii1 = True
 if themeit : display = themeit % display
 o0oO0iiiiI1Iii = xbmcgui . ListItem ( display , iconImage = "DefaultFolder.png" , thumbnailImage = icon )
 o0oO0iiiiI1Iii . setInfo ( type = "Video" , infoLabels = { "Title" : display , "Plot" : description } )
 o0oO0iiiiI1Iii . setProperty ( "Fanart_Image" , fanart )
 if not menu == None : o0oO0iiiiI1Iii . addContextMenuItems ( menu , replaceItems = overwrite )
 i11iii1Ii1 = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = i1ooO , listitem = o0oO0iiiiI1Iii , isFolder = True )
 return i11iii1Ii1
 if 41 - 41: iiIIi1IiIi11 % iiIIi1IiIi11 - i1Ii % I1111 - OoooooooOO - iiIIi1IiIi11
def oOOo00O0O0 ( name , url , mode , iconimage , fanart , description ) :
 if 11 - 11: i11iIiiIii + oO0 + i11iIiiIii
 i1ooO = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart ) + "&description=" + urllib . quote_plus ( description )
 i11iii1Ii1 = True
 o0oO0iiiiI1Iii = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 o0oO0iiiiI1Iii . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description } )
 o0oO0iiiiI1Iii . setProperty ( "Fanart_Image" , fanart )
 i11iii1Ii1 = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = i1ooO , listitem = o0oO0iiiiI1Iii , isFolder = False )
 if 31 - 31: IIIi1i1I * OO00O0O0O00Oo . o0o0Oo0oooo0 * i11IiIiiIIIII
def oo00O00oO000o ( display , mode = None , name = None , url = None , menu = None , description = o0OOO , overwrite = True , fanart = OOO00 , icon = iiiiiIIii , themeit = None ) :
 i1ooO = sys . argv [ 0 ]
 if not mode == None : i1ooO += "?mode=%s" % urllib . quote_plus ( mode )
 if not name == None : i1ooO += "&name=" + urllib . quote_plus ( name )
 if not url == None : i1ooO += "&url=" + urllib . quote_plus ( url )
 i11iii1Ii1 = True
 if themeit : display = themeit % display
 o0oO0iiiiI1Iii = xbmcgui . ListItem ( display , iconImage = "DefaultFolder.png" , thumbnailImage = icon )
 o0oO0iiiiI1Iii . setInfo ( type = "Video" , infoLabels = { "Title" : display , "Plot" : description } )
 o0oO0iiiiI1Iii . setProperty ( "Fanart_Image" , fanart )
 if not menu == None : o0oO0iiiiI1Iii . addContextMenuItems ( menu , replaceItems = overwrite )
 i11iii1Ii1 = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = i1ooO , listitem = o0oO0iiiiI1Iii , isFolder = True )
 return i11iii1Ii1
 if 28 - 28: i1Ii + ooOo - Ooo0O % iii11iiII . i11IiIiiIIIII + ooOo
def iiiii1II ( display , mode = None , name = None , url = None , menu = None , description = o0OOO , overwrite = True , fanart = OOO00 , icon = iiiiiIIii , themeit = None ) :
 i1ooO = sys . argv [ 0 ]
 if not mode == None : i1ooO += "?mode=%s" % urllib . quote_plus ( mode )
 if not name == None : i1ooO += "&name=" + urllib . quote_plus ( name )
 if not url == None : i1ooO += "&url=" + urllib . quote_plus ( url )
 i11iii1Ii1 = True
 if themeit : display = themeit % display
 o0oO0iiiiI1Iii = xbmcgui . ListItem ( display , iconImage = "DefaultFolder.png" , thumbnailImage = icon )
 o0oO0iiiiI1Iii . setInfo ( type = "Video" , infoLabels = { "Title" : display , "Plot" : description } )
 o0oO0iiiiI1Iii . setProperty ( "Fanart_Image" , fanart )
 if not menu == None : o0oO0iiiiI1Iii . addContextMenuItems ( menu , replaceItems = overwrite )
 i11iii1Ii1 = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = i1ooO , listitem = o0oO0iiiiI1Iii , isFolder = False )
 return i11iii1Ii1
 if 72 - 72: IiiIII111ii / Ooo0O / IIIi1i1I * o0o0Oo0oooo0 + iii11iiII
def OOoOOO000O0 ( name , url , mode , iconimage ) :
 i1ooO = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage )
 i11iii1Ii1 = True
 o0oO0iiiiI1Iii = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 o0oO0iiiiI1Iii . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : name } )
 i11iii1Ii1 = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = i1ooO , listitem = o0oO0iiiiI1Iii , isFolder = True )
 return i11iii1Ii1
 if 58 - 58: I1I1i1 % ooOo . ooOo * I1111 - i1Ii . OoooooooOO
def Oo0o ( name , url , mode , iconimage , fanart , description , installRating ) :
 i1ooO = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart ) + "&description=" + urllib . quote_plus ( description ) + "&installRating=" + urllib . quote_plus ( installRating )
 i11iii1Ii1 = True
 o0oO0iiiiI1Iii = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 o0oO0iiiiI1Iii . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description , "Premiered" : installRating } )
 o0oO0iiiiI1Iii . setProperty ( "Fanart_Image" , fanart )
 i11iii1Ii1 = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = i1ooO , listitem = o0oO0iiiiI1Iii , isFolder = False )
 return i11iii1Ii1
 if 10 - 10: OO00O0O0O00Oo
def I11i1i11IiIi1 ( display , mode = None , name = None , url = None , menu = None , description = o0OOO , overwrite = True , fanart = OOO00 , icon = iiiiiIIii , themeit = None ) :
 i1ooO = sys . argv [ 0 ]
 if not mode == None : i1ooO += "?mode=%s" % urllib . quote_plus ( mode )
 if not name == None : i1ooO += "&name=" + urllib . quote_plus ( name )
 if not url == None : i1ooO += "&url=" + urllib . quote_plus ( url )
 i11iii1Ii1 = True
 if themeit : display = themeit % display
 o0oO0iiiiI1Iii = xbmcgui . ListItem ( display , iconImage = "DefaultFolder.png" , thumbnailImage = icon )
 o0oO0iiiiI1Iii . setInfo ( type = "Video" , infoLabels = { "Title" : display , "Plot" : description } )
 o0oO0iiiiI1Iii . setProperty ( "Fanart_Image" , fanart )
 if not menu == None : o0oO0iiiiI1Iii . addContextMenuItems ( menu , replaceItems = overwrite )
 i11iii1Ii1 = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = i1ooO , listitem = o0oO0iiiiI1Iii , isFolder = False )
 return i11iii1Ii1
 if 8 - 8: iiIIi1IiIi11 - ooOo * Ooo0O % oO0 * OoooooooOO
def iIIIiI ( display , mode , name = None , url = None , menu = None , overwrite = True , fanart = OOO00 , icon = iiiiiIIii , description = None , themeit = None ) :
 i1ooO = '%s?mode=%s' % ( sys . argv [ 0 ] , urllib . quote_plus ( mode ) )
 if not name == None : i1ooO += "&name=" + urllib . quote_plus ( name )
 if not url == None : i1ooO += "&url=" + urllib . quote_plus ( url )
 if not description == None : i1ooO += "&description=" + urllib . quote_plus ( description )
 i11iii1Ii1 = True
 if themeit : display = themeit % display
 o0oO0iiiiI1Iii = xbmcgui . ListItem ( description , iconImage = "DefaultFolder.png" , thumbnailImage = icon )
 o0oO0iiiiI1Iii . setInfo ( type = "Video" , infoLabels = { "Title" : description , "Plot" : o0OOO } )
 o0oO0iiiiI1Iii . setProperty ( "Fanart_Image" , fanart )
 if not menu == None : o0oO0iiiiI1Iii . addContextMenuItems ( menu , replaceItems = overwrite )
 i11iii1Ii1 = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = i1ooO , listitem = o0oO0iiiiI1Iii , isFolder = False )
 return i11iii1Ii1
 if 26 - 26: i1IIi / iiIIi1IiIi11 . iiIIi1IiIi11
def I1i11IIIi ( name , url , mode , iconimage , fanart , description ) :
 i1ooO = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&fanart=" + urllib . quote_plus ( fanart )
 i11iii1Ii1 = True
 o0oO0iiiiI1Iii = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 o0oO0iiiiI1Iii . setInfo ( type = "Video" , infoLabels = { "Title" : name } )
 o0oO0iiiiI1Iii . setProperty ( "Fanart_Image" , fanart )
 i11iii1Ii1 = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = i1ooO , listitem = o0oO0iiiiI1Iii , isFolder = False )
 return i11iii1Ii1
 if 19 - 19: IIIi1i1I * iiIIi1IiIi11 + o0o0Oo0oooo0 - IIIi1i1I + oO0
def iIii1ii ( name , url , mode , iconimage , fanart , description ) :
 if 24 - 24: i1IIi / OO00O0O0O00Oo * i11IiIiiIIIII / O0
 i1ooO = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart ) + "&description=" + urllib . quote_plus ( description )
 i11iii1Ii1 = True
 o0oO0iiiiI1Iii = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 o0oO0iiiiI1Iii . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description } )
 o0oO0iiiiI1Iii . setProperty ( "Fanart_Image" , fanart )
 i11iii1Ii1 = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = i1ooO , listitem = o0oO0iiiiI1Iii , isFolder = True )
 return i11iii1Ii1
 if 88 - 88: oO0 . OO00O0O0O00Oo * Ooo0O - iii11iiII . o0o0Oo0oooo0 . OO00O0O0O00Oo
 if 27 - 27: ooOo
 if 27 - 27: iIii1I11I1II1 % i11IiIiiIIIII - OO00O0O0O00Oo
def Oo00 ( name , url , mode , iconimage , fanart , description ) :
 i1ooO = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart ) + "&description=" + urllib . quote_plus ( description )
 i11iii1Ii1 = True
 o0oO0iiiiI1Iii = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 o0oO0iiiiI1Iii . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description } )
 o0oO0iiiiI1Iii . setProperty ( "Fanart_Image" , fanart )
 if mode == 90 :
  i11iii1Ii1 = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = i1ooO , listitem = o0oO0iiiiI1Iii , isFolder = False )
 else :
  i11iii1Ii1 = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = i1ooO , listitem = o0oO0iiiiI1Iii , isFolder = True )
 return i11iii1Ii1
 if 71 - 71: OOoooooO . oO0 * O0 - OO00O0O0O00Oo - II111iiii
def iIIi11ii ( ) :
 O000Oo00 = [ ]
 iI1oOoo = sys . argv [ 2 ]
 if len ( iI1oOoo ) >= 2 :
  o00O0o00oo = sys . argv [ 2 ]
  iIiiII = o00O0o00oo . replace ( '?' , '' )
  if ( o00O0o00oo [ len ( o00O0o00oo ) - 1 ] == '/' ) :
   o00O0o00oo = o00O0o00oo [ 0 : len ( o00O0o00oo ) - 2 ]
  iII1I = iIiiII . split ( '&' )
  O000Oo00 = { }
  for OO0oOOo0o in range ( len ( iII1I ) ) :
   o00oOOo0Oo = { }
   o00oOOo0Oo = iII1I [ OO0oOOo0o ] . split ( '=' )
   if ( len ( o00oOOo0Oo ) ) == 2 :
    O000Oo00 [ o00oOOo0Oo [ 0 ] ] = o00oOOo0Oo [ 1 ]
    if 91 - 91: II111iiii - iIii1I11I1II1 / i1IIi * i1IIi % Ooo0O
  return O000Oo00
  if 82 - 82: OOoooooO
o00O0o00oo = iIIi11ii ( )
OOOoO000 = None
oO0o00oOOooO0 = None
OoOooO0 = None
iIiiIiiIi = None
oOoo000 = None
IiI11i1IIiiI = None
iI1IiiiIi = None
oOOo000oOoO0 = None
try :
 iI1IiiiIi = int ( o00O0o00oo [ "fav_mode" ] )
except :
 pass
try : OoOooO0 = urllib . unquote_plus ( o00O0o00oo [ "mode" ] )
except : pass
try : oO0o00oOOooO0 = urllib . unquote_plus ( o00O0o00oo [ "name" ] )
except : pass
try : OOOoO000 = urllib . unquote_plus ( o00O0o00oo [ "url" ] )
except : pass
try : iIiiIiiIi = urllib . unquote_plus ( o00O0o00oo [ "iconimage" ] )
except : pass
try : oOoo000 = urllib . unquote_plus ( o00O0o00oo [ "fanart" ] )
except : pass
try : IiI11i1IIiiI = urllib . unquote_plus ( o00O0o00oo [ "description" ] )
except : pass
if 31 - 31: i11iIiiIii + i1Ii - OO00O0O0O00Oo * iiIIi1IiIi11
print "Mode: " + str ( OoOooO0 )
print "URL: " + str ( OOOoO000 )
print "Name: " + str ( oO0o00oOOooO0 )
print "IconImage: " + str ( iIiiIiiIi )
if 60 - 60: iiIIi1IiIi11 + I1111 + i11IiIiiIIIII % iIii1I11I1II1 . Ooo0O
wiz . log ( '[ Version : \'%s\' ] [ Mode : \'%s\' ] [ Name : \'%s\' ] [ Url : \'%s\' ]' % ( O0oo0OO0 , OoOooO0 if not OoOooO0 == '' else None , oO0o00oOOooO0 , OOOoO000 ) )
if 73 - 73: OO00O0O0O00Oo * oO0 + I1I1i1 - Ooo0O . i11IiIiiIIIII
def o0oOOO ( ) :
 if 62 - 62: IiiIII111ii - IIIi1i1I % iIii1I11I1II1
 for file in os . listdir ( Ii11iii11I ) :
  if file . endswith ( ".zip" ) :
   OOOoO000 = xbmc . translatePath ( os . path . join ( Ii11iii11I , file ) )
   I1i11IIIi ( file , OOOoO000 , 'read' , iiiiiIIii , iiiiiIIii , '' )
   if 57 - 57: OoooooooOO / o0o0Oo0oooo0
def iI1ii1iIiii1i ( ) :
 ooOooo00O = xbmc . translatePath ( os . path . join ( 'special://' , 'home' ) )
 for file in os . listdir ( Ii11iii11I ) :
  if file . endswith ( ".zip" ) :
   OOOoO000 = xbmc . translatePath ( os . path . join ( Ii11iii11I , file ) )
   Oo00 ( file , OOOoO000 , 'dell' , iiiiiIIii , iiiiiIIii , '' )
   if 5 - 5: i11IiIiiIIIII . II111iiii / i1Ii % i11IiIiiIIIII + IIIi1i1I
def iIi1 ( content , viewType ) :
 if 35 - 35: I1111
 if content :
  xbmcplugin . setContent ( int ( sys . argv [ 1 ] ) , content )
 if ADDON . getSetting ( 'auto-view' ) == 'true' :
  xbmc . executebuiltin ( "Container.SetViewMode(%s)" % ADDON . getSetting ( viewType ) )
  if 52 - 52: Ooo0O / iiIIi1IiIi11
  if 42 - 42: iIii1I11I1II1 * IiiIII111ii / I1111 + iii11iiII
  if 48 - 48: OoooooooOO - OO00O0O0O00Oo . i11iIiiIii * iiIIi1IiIi11 - IiiIII111ii - I1I1i1
  if 59 - 59: iiIIi1IiIi11 / i11IiIiiIIIII . Ooo0O
  if 100 - 100: O0
  if 94 - 94: oO0 - I1I1i1
  if 42 - 42: I1I1i1 * o0o0Oo0oooo0 . I1111 - iiIIi1IiIi11 / II111iiii
def iIi1 ( content , viewType ) :
 if wiz . getS ( 'auto-view' ) == 'true' :
  iII1ii11III = wiz . getS ( viewType )
  if iII1ii11III == '50' and o0OIiII >= 17 and I1IIiiIiii == 'skin.estuary' : iII1ii11III = '55'
  if iII1ii11III == '500' and o0OIiII >= 17 and I1IIiiIiii == 'skin.estuary' : iII1ii11III = '50'
  wiz . ebi ( "Container.SetViewMode(%s)" % iII1ii11III )
  if 92 - 92: I1111 - oO0 + iIii1I11I1II1 % I1I1i1
if OoOooO0 == None : i1iiIiI1Ii1i ( )
if 78 - 78: iIii1I11I1II1 - II111iiii / ooOo
elif OoOooO0 == 'wizardupdate' : wiz . wizardUpdate ( )
elif OoOooO0 == 'builds' : OoO00 ( )
elif OoOooO0 == 'pin' : check ( )
elif OoOooO0 == 'viewbuild' : OoOo00o0OO ( oO0o00oOOooO0 , oOOo000oOoO0 )
elif OoOooO0 == 'buildinfo' : I1I1i1I1I1I1 ( oO0o00oOOooO0 )
elif OoOooO0 == 'buildpreview' : IIi1I ( oO0o00oOOooO0 )
elif OoOooO0 == 'install' : i1iI1Ii11Ii1 ( oO0o00oOOooO0 , OOOoO000 )
elif OoOooO0 == 'theme' : i1iI1Ii11Ii1 ( oO0o00oOOooO0 , oOOo000oOoO0 , OoOooO0 , OOOoO000 )
elif OoOooO0 == 'viewthirdparty' : I11I1IIiiII1 ( oO0o00oOOooO0 )
elif OoOooO0 == 'installthird' : OOo0oOOOOoo0 ( oO0o00oOOooO0 , OOOoO000 )
elif OoOooO0 == 'editthird' : OoOooo ( oO0o00oOOooO0 ) ; wiz . refresh ( )
if 9 - 9: oO0 * IiiIII111ii - i1Ii
elif OoOooO0 == 'pro' : Main_Menu ( )
if 88 - 88: iIii1I11I1II1
elif OoOooO0 == 'maint' : i1IiII ( oO0o00oOOooO0 )
elif OoOooO0 == 'speed' : i1iiiIi1i ( )
elif OoOooO0 == 'kodi17fix' : wiz . kodi17Fix ( )
elif OoOooO0 == 'advancedsetting' : IiIi ( oO0o00oOOooO0 )
elif OoOooO0 == 'autoadvanced' : I11iiI11iiI ( ) ; wiz . refresh ( )
elif OoOooO0 == 'removeadvanced' : o00iIiiiII ( ) ; wiz . refresh ( )
elif OoOooO0 == 'asciicheck' : wiz . asciiCheck ( )
elif OoOooO0 == 'backupbuild' : wiz . backUpOptions ( 'build' )
elif OoOooO0 == 'backupgui' : wiz . backUpOptions ( 'guifix' )
elif OoOooO0 == 'backuptheme' : wiz . backUpOptions ( 'theme' )
elif OoOooO0 == 'backupaddon' : wiz . backUpOptions ( 'addondata' )
elif OoOooO0 == 'oldThumbs' : wiz . oldThumbs ( )
elif OoOooO0 == 'clearbackup' : wiz . cleanupBackup ( )
elif OoOooO0 == 'convertpath' : wiz . convertSpecial ( o00 )
elif OoOooO0 == 'currentsettings' : iII1Iii11111 ( )
elif OoOooO0 == 'fullclean' : OooOoO0OOoOOO0o0o ( ) ; wiz . refresh ( )
elif OoOooO0 == 'clearcache' : i1i1IIiII1I ( ) ; wiz . refresh ( )
elif OoOooO0 == 'clearpackages' : wiz . clearPackages ( ) ; wiz . refresh ( )
elif OoOooO0 == 'clearcrash' : wiz . clearCrash ( ) ; wiz . refresh ( )
elif OoOooO0 == 'clearthumb' : iIOoo0ooo0oo ( ) ; wiz . refresh ( )
elif OoOooO0 == 'checksources' : wiz . checkSources ( ) ; wiz . refresh ( )
elif OoOooO0 == 'checkrepos' : wiz . checkRepos ( ) ; wiz . refresh ( )
elif OoOooO0 == 'freshstart' : OO0IIIIIIi111i ( )
elif OoOooO0 == 'forceupdate' : wiz . forceUpdate ( )
elif OoOooO0 == 'forceprofile' : wiz . reloadProfile ( wiz . getInfo ( 'System.ProfileName' ) )
elif OoOooO0 == 'forceclose' : wiz . killxbmc ( )
elif OoOooO0 == 'forceskin' : wiz . ebi ( "ReloadSkin()" ) ; wiz . refresh ( )
elif OoOooO0 == 'hidepassword' : wiz . hidePassword ( )
elif OoOooO0 == 'unhidepassword' : wiz . unhidePassword ( )
elif OoOooO0 == 'enableaddons' : oO0O ( )
elif OoOooO0 == 'toggleaddon' : wiz . toggleAddon ( oO0o00oOOooO0 , OOOoO000 ) ; wiz . refresh ( )
elif OoOooO0 == 'togglecache' : ooOoOo ( oO0o00oOOooO0 ) ; wiz . refresh ( )
elif OoOooO0 == 'toggleadult' : wiz . toggleAdult ( ) ; wiz . refresh ( )
elif OoOooO0 == 'changefeq' : oOO0 ( ) ; wiz . refresh ( )
elif OoOooO0 == 'uploadlog' : uploadLog . Main ( )
elif OoOooO0 == 'viewlog' : i1ii1iIi ( )
elif OoOooO0 == 'viewwizlog' : i1ii1iIi ( I11iii1Ii )
elif OoOooO0 == 'viewerrorlog' : Oo00OO00o0oO ( all = True )
elif OoOooO0 == 'clearwizlog' : OO0OOoo0OOO = open ( I11iii1Ii , 'w' ) ; OO0OOoo0OOO . close ( ) ; wiz . LogNotify ( "[COLOR %s]%s[/COLOR]" % ( oOOo0O00o , o0OOO ) , "[COLOR %s]Wizard Log Cleared![/COLOR]" % iIiIi11 )
elif OoOooO0 == 'purgedb' : o0oOo ( )
elif OoOooO0 == 'fixaddonupdate' : Ii11iiI ( )
elif OoOooO0 == 'removeaddons' : OO0oo ( )
elif OoOooO0 == 'removeaddon' : i11IiiI1Ii1 ( oO0o00oOOooO0 )
elif OoOooO0 == 'removeaddondata' : I1i1I11111iI1 ( )
elif OoOooO0 == 'removedata' : ooo0O0OOo0OoO ( oO0o00oOOooO0 )
elif OoOooO0 == 'resetaddon' : o00oO0o0o = wiz . cleanHouse ( o0 , ignore = True ) ; wiz . LogNotify ( "[COLOR %s]%s[/COLOR]" % ( oOOo0O00o , o0OOO ) , "[COLOR %s]Addon_Data reset[/COLOR]" % iIiIi11 )
elif OoOooO0 == 'systeminfo' : O0OOOOo0 ( )
elif OoOooO0 == 'restorezip' : o0oOOoo0O ( 'build' )
elif OoOooO0 == 'restoregui' : o0oOOoo0O ( 'gui' )
elif OoOooO0 == 'restoreaddon' : o0oOOoo0O ( 'addondata' )
elif OoOooO0 == 'restoreextzip' : OoO0o0oOOO ( 'build' )
elif OoOooO0 == 'restoreextgui' : OoO0o0oOOO ( 'gui' )
elif OoOooO0 == 'restoreextaddon' : OoO0o0oOOO ( 'addondata' )
elif OoOooO0 == 'writeadvanced' : III1iiIIi ( oO0o00oOOooO0 , OOOoO000 )
if 27 - 27: i11IiIiiIIIII * i11iIiiIii . iii11iiII + OOoooooO
elif OoOooO0 == 'apk1' : Oo0O ( )
elif OoOooO0 == 'apkgame' : ooOoOOOOo ( OOOoO000 )
elif OoOooO0 == 'select' : iiIIi ( OOOoO000 )
elif OoOooO0 == 'grab' : i11Ii1I1I11I ( oO0o00oOOooO0 , OOOoO000 )
elif OoOooO0 == 'rom' : O00o0O ( OOOoO000 )
elif OoOooO0 == 'apkscrape1' : APK ( )
elif OoOooO0 == 'apkscrape' : IiIIIII11I ( oO0o00oOOooO0 )
elif OoOooO0 == 'apkshow' : oOO0o00O ( OOOoO000 )
elif OoOooO0 == 'intellaunch' : iiiII ( )
elif OoOooO0 == 'intelselect' : O0oOo ( oO0o00oOOooO0 , OOOoO000 , iIiiIiiIi , oOoo000 , IiI11i1IIiiI )
elif OoOooO0 == 'emurom' : OO0OoOo0OOO ( )
elif OoOooO0 == 'roms' : I1Iii1I ( )
elif OoOooO0 == 'snes' : ii1111Ii1i ( )
elif OoOooO0 == 'nes' : II1 ( )
elif OoOooO0 == 'gen' : o00OoO0oO00 ( )
elif OoOooO0 == 'atr' : i1i1IiIi1 ( )
elif OoOooO0 == 'n64' : oOIIIiI1ii1IIi ( )
elif OoOooO0 == 'tbg' : ii1I111i1Ii ( )
elif OoOooO0 == 'nds' : OOoooOoO0Oo ( )
elif OoOooO0 == 'ps' : Ooo0o0oo0 ( )
elif OoOooO0 == 'apkinstall' : Ii1 ( oO0o00oOOooO0 , OOOoO000 , "None" )
elif OoOooO0 == 'rominstall' : o00OO0o0 ( oO0o00oOOooO0 , OOOoO000 , )
if 14 - 14: OO00O0O0O00Oo * I1111 + i11IiIiiIIIII - i1Ii . oO0 * IIIi1i1I
elif OoOooO0 == 'youtube' : iIi1i1iIi1Ii1 ( oO0o00oOOooO0 )
elif OoOooO0 == 'viewVideo' : O0OooooO0o0O0 ( OOOoO000 )
if 100 - 100: i11IiIiiIIIII
elif OoOooO0 == 'addons' : oo0O0o ( oO0o00oOOooO0 )
elif OoOooO0 == 'addoninstall' : oo0ooO0O0o ( oO0o00oOOooO0 , OOOoO000 )
if 36 - 36: I1111 + II111iiii * o0o0Oo0oooo0
elif OoOooO0 == 'savedata' : oOo0O ( )
elif OoOooO0 == 'togglesetting' : wiz . setS ( oO0o00oOOooO0 , 'false' if wiz . getS ( oO0o00oOOooO0 ) == 'true' else 'true' ) ; wiz . refresh ( )
elif OoOooO0 == 'managedata' : iiiII1III ( oO0o00oOOooO0 )
elif OoOooO0 == 'whitelist' : wiz . whiteList ( oO0o00oOOooO0 )
if 14 - 14: OO00O0O0O00Oo % OO00O0O0O00Oo
elif OoOooO0 == 'trakt' : IIIii11i1I ( )
elif OoOooO0 == 'savetrakt' : traktit . traktIt ( 'update' , oO0o00oOOooO0 )
elif OoOooO0 == 'restoretrakt' : traktit . traktIt ( 'restore' , oO0o00oOOooO0 )
elif OoOooO0 == 'addontrakt' : traktit . traktIt ( 'clearaddon' , oO0o00oOOooO0 )
elif OoOooO0 == 'cleartrakt' : traktit . clearSaved ( oO0o00oOOooO0 )
elif OoOooO0 == 'authtrakt' : traktit . activateTrakt ( oO0o00oOOooO0 ) ; wiz . refresh ( )
elif OoOooO0 == 'updatetrakt' : traktit . autoUpdate ( 'all' )
elif OoOooO0 == 'importtrakt' : traktit . importlist ( oO0o00oOOooO0 ) ; wiz . refresh ( )
if 9 - 9: Ooo0O - Ooo0O - I1I1i1 + OO00O0O0O00Oo - II111iiii . ooOo
elif OoOooO0 == 'realdebrid' : O0000 ( )
elif OoOooO0 == 'savedebrid' : debridit . debridIt ( 'update' , oO0o00oOOooO0 )
elif OoOooO0 == 'restoredebrid' : debridit . debridIt ( 'restore' , oO0o00oOOooO0 )
elif OoOooO0 == 'addondebrid' : debridit . debridIt ( 'clearaddon' , oO0o00oOOooO0 )
elif OoOooO0 == 'cleardebrid' : debridit . clearSaved ( oO0o00oOOooO0 )
elif OoOooO0 == 'authdebrid' : debridit . activateDebrid ( oO0o00oOOooO0 ) ; wiz . refresh ( )
elif OoOooO0 == 'updatedebrid' : debridit . autoUpdate ( 'all' )
elif OoOooO0 == 'importdebrid' : debridit . importlist ( oO0o00oOOooO0 ) ; wiz . refresh ( )
if 57 - 57: iiIIi1IiIi11 - ooOo + OoooooooOO / iiIIi1IiIi11 . OOoooooO % i1IIi
elif OoOooO0 == 'login' : II11iIIii ( )
elif OoOooO0 == 'savelogin' : loginit . loginIt ( 'update' , oO0o00oOOooO0 )
elif OoOooO0 == 'restorelogin' : loginit . loginIt ( 'restore' , oO0o00oOOooO0 )
elif OoOooO0 == 'addonlogin' : loginit . loginIt ( 'clearaddon' , oO0o00oOOooO0 )
elif OoOooO0 == 'clearlogin' : loginit . clearSaved ( oO0o00oOOooO0 )
elif OoOooO0 == 'authlogin' : loginit . activateLogin ( oO0o00oOOooO0 ) ; wiz . refresh ( )
elif OoOooO0 == 'updatelogin' : loginit . autoUpdate ( 'all' )
elif OoOooO0 == 'importlogin' : loginit . importlist ( oO0o00oOOooO0 ) ; wiz . refresh ( )
if 52 - 52: O0 - iIii1I11I1II1 / I1111 / i1Ii
elif OoOooO0 == 'contact' : notify . contact ( oOO0O00Oo0O0o )
elif OoOooO0 == 'settings' : wiz . openS ( oO0o00oOOooO0 ) ; wiz . refresh ( )
elif OoOooO0 == 'opensettings' : id = eval ( OOOoO000 . upper ( ) + 'ID' ) [ oO0o00oOOooO0 ] [ 'plugin' ] ; I11Iii11i11I1 = wiz . addonId ( id ) ; I11Iii11i11I1 . openSettings ( ) ; wiz . refresh ( )
if 1 - 1: i1IIi . oO0 * I1I1i1 % II111iiii % iIii1I11I1II1
elif OoOooO0 == 'developer' : i1I111II ( )
elif OoOooO0 == 'converttext' : wiz . convertText ( )
elif OoOooO0 == 'createqr' : wiz . createQR ( )
elif OoOooO0 == 'testnotify' : o0o00OoOo0 ( )
elif OoOooO0 == 'testupdate' : OO0Oo00OO0oo ( )
elif OoOooO0 == 'testfirst' : I1Ii1II ( )
elif OoOooO0 == 'testfirstrun' : IiIiiI1iii1iIiiI ( )
elif OoOooO0 == 'testapk' : notify . apkInstaller ( 'SPMC' )
if 71 - 71: I1111 + i1Ii / i11IiIiiIIIII * Ooo0O . IiiIII111ii . i11IiIiiIIIII
elif OoOooO0 == 'guide' : TvGuide ( )
if 33 - 33: IIIi1i1I / IiiIII111ii - ooOo % OO00O0O0O00Oo
elif OoOooO0 == 'recreateaddon' : ReCreate_Addon_ini ( )
elif OoOooO0 == 'getlistplay' : Get_List_playlinks ( oO0o00oOOooO0 )
elif OoOooO0 == 'resolve' : RESOLVER ( OOOoO000 )
elif OoOooO0 == 'streams' : Streams_Menu ( )
elif OoOooO0 == 'liveevent' : Live_Events ( oO0o00oOOooO0 )
elif OoOooO0 == 'addonopen' : I1ii11iIi11i . openSettings ( sys . argv [ 0 ] )
xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
# dd678faae9ac167bc83abf78e5cb2f3f0688d3a3
