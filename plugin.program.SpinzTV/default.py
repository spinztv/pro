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
 import webbrowser
 import time
 if 72 - 72: IIIi1i1I + IIIi1i1I / II111iiii . OoooooooOO % IiiIII111ii
 III = 'System.Platform.Android'
 IiiIii = 'system.platform.ios'
 oOo0OoOOo0 = 'system.platform.osx'
 iII11I1Ii1 = 'system.platform.atv2'
 o0o0 = 'aHR0cDovL3d3dy5zdHZtYy5uZXQvcGlu'
 oOo0oO = 'MGZlYTY4MGY5NmVjY2E0'
 IIi1IIIIi = base64 . b64decode ( 'aHR0cDovL29mZnNob3JlcGx1Z2lucy5jb20vcG9ydGFsL2FwaS5waHA/cGluPSVzJmtleT0=' ) + base64 . b64decode ( oOo0oO )
 OOOoO = 'W0NPTE9SIGJsdWVdSW4gb3JkZXIgdG8gY29udGludWUgcGxlYXNlWy9DT0xPUl0gW0NPTE9SIHdoaXRlXVtCXVZFUklGWVsvQl1bL0NPTE9SXSBbQ09MT1IgYmx1ZV15b3VyIGRldmljZSBieSBnZXR0aW5nIGFbL0NPTE9SXVtDT0xPUiB3aGl0ZV1bQl0gRlJFRSBQSU5bL0JdWy9DT0xPUl1bQ09MT1IgYmx1ZV0gZnJvbSBvdXIgd2Vic2l0ZSBhbmQgZW50ZXJpbmcgdGhlIHBpbiBvbiB0aGUgbmV4dCBwcm9tcHQuICBbL0NPTE9SXVtDT0xPUiB3aGl0ZV1bQl18ICAgd3d3LnN0dm1jLm5ldC9waW5bL0JdWy9DT0xPUl0NCltDT0xPUiByZWRdW0JdRklSRSBERVZJQ0VTIERPIE5PVCBISVQgR0VUIFBJTi4gVVNFIEEgUEhPTkUgT1IgQ09NUFVURVIgVE8gR0VUIFlPVVIgUElOIE5VTUJFUlsvQl1bL0NPTE9SXQ0K'
 if 14 - 14: i11IiIiiIIIII . iIii1I11I1II1 . OoooooooOO . II111iiii / I1I1i1
 o0oO0 = xbmcgui . Dialog ( )
 IiIi1 = webbrowser . open
 i111iiI1ii = xbmc . executebuiltin
 IIiii = base64 . b64decode ( OOOoO )
 I1i1i = xbmcaddon . Addon ( ) . getAddonInfo
 OOOOooO0oO00O0o = xbmcaddon . Addon ( ) . getSetting ( 'pin' )
 IiiIII111iI = lambda ooOO00oOOo000 : base64 . b64decode ( str ( ooOO00oOOo000 ) )
 IIi = lambda ooOO00oOOo000 : requests . get ( IIi1IIIIi % ( ooOO00oOOo000 ) ) . text . strip ( )
 i11II11II1 = lambda ooOO00oOOo000 : xbmcaddon . Addon ( ) . setSetting ( base64 . b64decode ( 'cGlu' ) , ooOO00oOOo000 )
 II1IOoOo000oOo0oo = lambda ooOO00oOOo000 : xbmc . getCondVisibility ( str ( ooOO00oOOo000 ) )
 oO0O = lambda ooOO00oOOo000 : i111iiI1ii ( 'StartAndroidActivity(,android.intent.action.VIEW,,%s)' % ( ooOO00oOOo000 ) )
 oOOiiiIIiIi = bool ( IIi ( OOOOooO0oO00O0o ) == base64 . b64decode ( 'UGluIFZlcmlmaWVk' ) )
 if 68 - 68: O0 + o0o0Oo0oooo0 / IIIi1i1I - iii11iiII + iIii1I11I1II1 % IiiIII111ii
 if 23 - 23: OOoooooO % I1I1i1 / i11IiIiiIIIII
 if not oOOiiiIIiIi == True :
  xbmcgui . Dialog ( ) . ok ( I1i1i ( 'name' ) , '' , IIiii , '' )
  i11I1II = xbmcgui . Dialog ( ) . contextmenu ( [ 'Enter Your Pin' , 'Get A New Pin' , 'Cancel' ] )
  if 79 - 79: I1111 . iiIIi1IiIi11 * IiiIII111ii - iii11iiII + OOoooooO
  if i11I1II == 0 :
   ii11II1i = OOOO000o0 ( 'Type Your Pin Here' )
   i11II11II1 ( ii11II1i )
   time . sleep ( 5 )
   OO0Ooooo000Oo ( )
   if 98 - 98: I1111 . i11IiIiiIIIII % II111iiii
   if 71 - 71: OO00O0O0O00Oo % i1IIi - II111iiii - iii11iiII + iii11iiII * OOoooooO
   if 51 - 51: iIii1I11I1II1 / o0o0Oo0oooo0 + iii11iiII - i11IiIiiIIIII + iiIIi1IiIi11
  if i11I1II == 1 :
   if 29 - 29: I1I1i1 % iIii1I11I1II1 . OoooooooOO % OoooooooOO % II111iiii / iiIIi1IiIi11
   if II1IOoOo000oOo0oo ( III ) :
    oO0O ( base64 . b64decode ( o0o0 ) )
    ii11II1i = OOOO000o0 ( 'Type Your Pin Here' )
    i11II11II1 ( ii11II1i )
    time . sleep ( 7 )
    OO0Ooooo000Oo ( )
    if 70 - 70: i11iIiiIii % iiIIi1IiIi11
   else :
    IiIi1 ( base64 . b64decode ( o0o0 ) )
    ii11II1i = OOOO000o0 ( 'Type Your Pin Here' )
    i11II11II1 ( ii11II1i )
    time . sleep ( 7 )
    OO0Ooooo000Oo ( )
    if 11 - 11: i1Ii % oO0 % IiiIII111ii / II111iiii % OO00O0O0O00Oo - Ooo0O
    if 96 - 96: oO0 / II111iiii . IiiIII111ii - iiIIi1IiIi11 * i11IiIiiIIIII * IIIi1i1I
  if i11I1II == 2 :
   sys . exit ( )
   if 76 - 76: IiiIII111ii - II111iiii * iii11iiII / OoooooooOO
  else :
   if not i11I1II == 0 :
    OO0Ooooo000Oo ( )
    if 18 - 18: I1111 + iIii1I11I1II1 - II111iiii - ooOo
   if not i11I1II == 1 :
    OO0Ooooo000Oo ( )
    if 71 - 71: OoooooooOO
   if not i11I1II == 2 :
    OO0Ooooo000Oo ( )
    if 33 - 33: OO00O0O0O00Oo
    if 62 - 62: oO0 + IiiIII111ii + i1IIi / OoooooooOO
    if 7 - 7: I1I1i1 + i1IIi . ooOo / Ooo0O
def I111i1I1 ( st ) :
 import re
 st = re . sub ( '\[.+\]' , '' , st )
 import string
 O0o00OOo00O0O = 0
 for II1i in st :
  if II1i in 'lij|\' ' : O0o00OOo00O0O += 37
  elif II1i in '![]fI.,:;/\\t' : O0o00OOo00O0O += 50
  elif II1i in '`-(){}r"' : O0o00OOo00O0O += 60
  elif II1i in '*^zcsJkvxy' : O0o00OOo00O0O += 85
  elif II1i in 'aebdhnopqug#$L+<>=?_~FZT' + string . digits : O0o00OOo00O0O += 95
  elif II1i in 'BSPEAKVXY&UwNRCHD' : O0o00OOo00O0O += 112
  elif II1i in 'QGOMm%W@' : O0o00OOo00O0O += 135
  else : O0o00OOo00O0O += 50
 return int ( O0o00OOo00O0O * 6.5 / 100 )
 if 96 - 96: O0 . IiiIII111ii % I1111 * iIii1I11I1II1
def OOOO000o0 ( Heading = xbmcaddon . Addon ( ) . getAddonInfo ( 'name' ) ) :
 O0O00oOooo0OO = xbmc . Keyboard ( '' , Heading )
 O0O00oOooo0OO . doModal ( )
 if ( O0O00oOooo0OO . isConfirmed ( ) ) :
  return O0O00oOooo0OO . getText ( )
  if 23 - 23: IIIi1i1I + I1111
def III1I1i1 ( url ) :
 if 11 - 11: O0 / I1111 % iii11iiII + I1I1i1 + iIii1I11I1II1
 import webbrowser
 if 40 - 40: OOoooooO - iii11iiII . IiiIII111ii * Ooo0O % OO00O0O0O00Oo
 IiIi1 = webbrowser . open
 i111iiI1ii = xbmc . executebuiltin
 II1IOoOo000oOo0oo = lambda ooOO00oOOo000 : xbmc . getCondVisibility ( str ( ooOO00oOOo000 ) )
 oO0O = lambda ooOO00oOOo000 : i111iiI1ii ( 'StartAndroidActivity(,android.intent.action.VIEW,,%s)' % ( ooOO00oOOo000 ) )
 if 56 - 56: i11iIiiIii . I1I1i1 - ooOo * i11IiIiiIIIII
 III = 'System.Platform.Android'
 if 91 - 91: IIIi1i1I + OoooooooOO - i1IIi
 if II1IOoOo000oOo0oo ( III ) : oO0O ( base64 . b64decode ( url ) )
 else : IiIi1 ( base64 . b64decode ( url ) )
 if 84 - 84: IiiIII111ii / i1Ii
 if 86 - 86: o0o0Oo0oooo0 * II111iiii - O0 . o0o0Oo0oooo0 % iIii1I11I1II1 / iii11iiII
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
 for O0OOO0OOooo00 , OOOoO000 , oOOOO , Ii , OOo00OoO , i1i1i1I , oOoo000 , IiIIiIIIiIii , OooOo00o , IiI11i1IIiiI , counter in O0Oo0o000oO :
  i1i1i1I = i1i1i1I if wiz . workingURL ( i1i1i1I ) else iiiiiIIii
  oOoo000 = oOoo000 if wiz . workingURL ( oOoo000 ) else OOO00
  I111iIi1 = '%s (v%s)' % ( name , O0OOO0OOooo00 )
  if O000oo0O == name and O0OOO0OOooo00 > oo0OooOOo0 :
   I111iIi1 = '%s [COLOR red][CURRENT v%s][/COLOR]' % ( I111iIi1 , oo0OooOOo0 )
  iiiii1II ( I111iIi1 , '' , description = IiI11i1IIiiI , fanart = oOoo000 , icon = i1i1i1I , themeit = OO0O000 )
  if O0O0ooOOO == 'No' : iiiii1II ( wiz . sep ( ) , '' , themeit = OOoO )
  oo00O00oO000o ( 'Save Data Menu' , 'savedata' , icon = I1111i , themeit = OOoO )
  iiiii1II ( 'Build Information' , 'buildinfo' , name , description = IiI11i1IIiiI , fanart = oOoo000 , icon = i1i1i1I , themeit = OOoO )
  if not IiIIiIIIiIii == "http://" : iiiii1II ( 'View Video Preview' , 'buildpreview' , name , description = IiI11i1IIiiI , fanart = oOoo000 , icon = i1i1i1I , themeit = OOoO )
  I1i11II = int ( float ( o0OIiII ) ) ; II11 = int ( float ( Ii ) )
  if not I1i11II == II11 :
   if I1i11II == 16 and II11 <= 15 : I1iii = False
   else : I1iii = True
  else : I1iii = False
  if I1iii == True :
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
    for oOO0OO0O , o00o , III11I , Ii1I11I , iiIii1I , IiI11i1IIiiI , counter in O0Oo0o000oO :
     if not O0Oo000ooO00 == 'true' and iiIii1I . lower ( ) == 'yes' : continue
     III11I = III11I if III11I == 'http://' else i1i1i1I
     Ii1I11I = Ii1I11I if Ii1I11I == 'http://' else oOoo000
     iiiii1II ( oOO0OO0O if not oOO0OO0O == o0O else "[B]%s (Installed)[/B]" % oOO0OO0O , 'theme' , name , oOO0OO0O , description = IiI11i1IIiiI , fanart = Ii1I11I , icon = III11I , themeit = OOoO )
 iIi1 ( 'files' , 'viewType' )
 if 47 - 47: OOoooooO . i11IiIiiIIIII / I1I1i1
def OOoOO ( number ) :
 oO0o00oOOooO0 = eval ( 'THIRD%sNAME' % number )
 OOOoO000 = eval ( 'THIRD%sURL' % number )
 OO0OO0OO = wiz . workingURL ( OOOoO000 )
 if not OO0OO0OO == True :
  iiiii1II ( 'Url for txt file not valid' , '' , icon = oO0O00oOOoooO , themeit = OOoO )
  iiiii1II ( '%s' % WORKINGURL , '' , icon = oO0O00oOOoooO , themeit = OOoO )
 else :
  type , OoooO0o = wiz . thirdParty ( OOOoO000 )
  iiiii1II ( "[B]%s[/B]" % oO0o00oOOooO0 , '' , themeit = OOoO )
  if O0O0ooOOO == 'No' : iiiii1II ( wiz . sep ( ) , '' , themeit = OOoO )
  if type :
   for oO0o00oOOooO0 , O0OOO0OOooo00 , OOOoO000 , Ii , i1i1i1I , oOoo000 , OooOo00o , IiI11i1IIiiI in OoooO0o :
    if not O0Oo000ooO00 == 'true' and OooOo00o . lower ( ) == 'yes' : continue
    iiiii1II ( "[%s] %s v%s" % ( Ii , oO0o00oOOooO0 , O0OOO0OOooo00 ) , 'installthird' , oO0o00oOOooO0 , OOOoO000 , icon = i1i1i1I , fanart = oOoo000 , description = IiI11i1IIiiI , themeit = oooOo0OOOoo0 )
  else :
   for oO0o00oOOooO0 , OOOoO000 , i1i1i1I , oOoo000 , IiI11i1IIiiI in OoooO0o :
    iiiii1II ( oO0o00oOOooO0 , 'installthird' , oO0o00oOOooO0 , OOOoO000 , icon = i1i1i1I , fanart = oOoo000 , description = IiI11i1IIiiI , themeit = oooOo0OOOoo0 )
    if 24 - 24: o0o0Oo0oooo0 % i1IIi + iiIIi1IiIi11 . i11iIiiIii . oO0
def IIi1II ( number ) :
 oO0o00oOOooO0 = eval ( 'THIRD%sNAME' % number )
 OOOoO000 = eval ( 'THIRD%sURL' % number )
 IiiI11i1I = wiz . getKeyboard ( oO0o00oOOooO0 , 'Enter the Name of the Wizard' )
 OOo0iiIii1IIi = wiz . getKeyboard ( OOOoO000 , 'Enter the URL of the Wizard Text' )
 if 10 - 10: i11iIiiIii - I1I1i1 % iIii1I11I1II1
 wiz . setS ( 'wizard%sname' % number , IiiI11i1I )
 wiz . setS ( 'wizard%surl' % number , OOo0iiIii1IIi )
 if 49 - 49: IIIi1i1I
def OOOOoOo00OO ( name = "" ) :
 if name == 'kodi' :
  OooOo0o0Oo = 'http://mirrors.kodi.tv/releases/android/arm/'
  OooO0oOo = 'http://mirrors.kodi.tv/releases/android/arm/old/'
  oOOo00O0OOOo = wiz . openURL ( OooOo0o0Oo ) . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
  OOo0iiIii1IIi = wiz . openURL ( OooO0oOo ) . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
  ooOO00oOOo000 = 0
  i11I1I1iiI = re . compile ( '<tr><td><a href="(.+?)".+?>(.+?)</a></td><td>(.+?)</td><td>(.+?)</td></tr>' ) . findall ( oOOo00O0OOOo )
  I1i1iii1Ii = re . compile ( '<tr><td><a href="(.+?)".+?>(.+?)</a></td><td>(.+?)</td><td>(.+?)</td></tr>' ) . findall ( OOo0iiIii1IIi )
  if 23 - 23: i11iIiiIii
  iiiii1II ( "Official Kodi Apk\'s" , themeit = OOOiiiiI )
  II1I11IIi = False
  for OOOoO000 , name , O0o00OOo00O0O , OoOOo in i11I1I1iiI :
   if OOOoO000 in [ '../' , 'old/' ] : continue
   if not OOOoO000 . endswith ( '.apk' ) : continue
   if not OOOoO000 . find ( '_' ) == - 1 and II1I11IIi == True : continue
   try :
    iii1 = name . split ( '-' )
    if not OOOoO000 . find ( '_' ) == - 1 :
     II1I11IIi = True
     IiiI11i1I , oOO0oo = iii1 [ 2 ] . split ( '_' )
    else :
     IiiI11i1I = iii1 [ 2 ]
     oOO0oo = ''
    II1iIi1IiIii = "[COLOR %s]%s v%s%s %s[/COLOR] [COLOR %s]%s[/COLOR] [COLOR %s]%s[/COLOR]" % ( oOOo0O00o , iii1 [ 0 ] . title ( ) , iii1 [ 1 ] , oOO0oo . upper ( ) , IiiI11i1I , iIiIi11 , O0o00OOo00O0O . replace ( ' ' , '' ) , oOOo0O00o , OoOOo )
    I111I11I111 = urljoin ( OooOo0o0Oo , OOOoO000 )
    iiiii1II ( II1iIi1IiIii , 'apkinstall' , "%s v%s%s %s" % ( iii1 [ 0 ] . title ( ) , iii1 [ 1 ] , oOO0oo . upper ( ) , IiiI11i1I ) , I111I11I111 )
    ooOO00oOOo000 += 1
   except :
    wiz . log ( "Error on: %s" % name )
    if 46 - 46: i11iIiiIii - O0 . IIIi1i1I
  for OOOoO000 , name , O0o00OOo00O0O , OoOOo in I1i1iii1Ii :
   if OOOoO000 in [ '../' , 'old/' ] : continue
   if not OOOoO000 . endswith ( '.apk' ) : continue
   if not OOOoO000 . find ( '_' ) == - 1 : continue
   try :
    iii1 = name . split ( '-' )
    II1iIi1IiIii = "[COLOR %s]%s v%s %s[/COLOR] [COLOR %s]%s[/COLOR] [COLOR %s]%s[/COLOR]" % ( oOOo0O00o , iii1 [ 0 ] . title ( ) , iii1 [ 1 ] , iii1 [ 2 ] , iIiIi11 , O0o00OOo00O0O . replace ( ' ' , '' ) , oOOo0O00o , OoOOo )
    I111I11I111 = urljoin ( OooO0oOo , OOOoO000 )
    iiiii1II ( II1iIi1IiIii , 'apkinstall' , "%s v%s %s" % ( iii1 [ 0 ] . title ( ) , iii1 [ 1 ] , iii1 [ 2 ] ) , I111I11I111 )
    ooOO00oOOo000 += 1
   except :
    wiz . log ( "Error on: %s" % name )
  if ooOO00oOOo000 == 0 : iiiii1II ( "Error Kodi Scraper Is Currently Down." )
 elif name == 'spmc' :
  Oo0O = 'https://github.com/koying/SPMC/releases'
  oOOo00O0OOOo = wiz . openURL ( Oo0O ) . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
  ooOO00oOOo000 = 0
  i11I1I1iiI = re . compile ( '<div.+?lass="release-body.+?div class="release-header".+?a href=.+?>(.+?)</a>.+?ul class="release-downloads">(.+?)</ul>.+?/div>' ) . findall ( oOOo00O0OOOo )
  if 1 - 1: O0 / iiIIi1IiIi11 % OO00O0O0O00Oo . Ooo0O + i1Ii
  iiiii1II ( "Official SPMC Apk\'s" , themeit = OOOiiiiI )
  if 27 - 27: OO00O0O0O00Oo % OoooooooOO + i1Ii % i1IIi / IIIi1i1I / OoooooooOO
  for name , III1IiIII1 in i11I1I1iiI :
   O00ooOo = ''
   I1i1iii1Ii = re . compile ( '<li>.+?<a href="(.+?)" rel="nofollow">.+?<small class="text-gray float-right">(.+?)</small>.+?strong>(.+?)</strong>.+?</a>.+?</li>' ) . findall ( III1IiIII1 )
   for oOO0o00O , oOoO , IIIIiI1iiiIiii in I1i1iii1Ii :
    if IIIIiI1iiiIiii . find ( 'armeabi' ) == - 1 : continue
    if IIIIiI1iiiIiii . find ( 'launcher' ) > - 1 : continue
    O00ooOo = urljoin ( 'https://github.com' , oOO0o00O )
    break
   if O00ooOo == '' : continue
   try :
    name = "SPMC %s" % name
    II1iIi1IiIii = "[COLOR %s]%s[/COLOR] [COLOR %s]%s[/COLOR]" % ( oOOo0O00o , name , iIiIi11 , oOoO . replace ( ' ' , '' ) )
    I111I11I111 = O00ooOo
    iiiii1II ( II1iIi1IiIii , 'apkinstall' , name , I111I11I111 )
    ooOO00oOOo000 += 1
   except Exception , ii1i1i :
    wiz . log ( "Error on: %s / %s" % ( name , str ( ii1i1i ) ) )
  if ooOO00oOOo000 == 0 : iiiii1II ( "Error SPMC Scraper Is Currently Down." )
  if 50 - 50: I1I1i1 * IiiIII111ii % oO0 / Ooo0O - O0 % iiIIi1IiIi11
def IIII1ii ( ) :
 oo00O00oO000o ( 'Emulators And Roms' , 'emurom' , icon = i111iIi1i1II1 , themeit = OOOiiiiI )
 oo00O00oO000o ( 'SpinzTV APKS' , 'apkshow' , url = OooOo , icon = Ii1IIiI1i , themeit = OOOiiiiI )
 oo00O00oO000o ( '[COLOR deepskyblue]APK Drawer[/COLOR]' , 'intellaunch' , )
 oo00O00oO000o ( 'Official Kodi Apk\'s' , 'apkscrape' , 'kodi' , icon = Oo0O00O000 , themeit = OOOiiiiI )
 oo00O00oO000o ( 'Official SPMC Apk\'s' , 'apkscrape' , 'spmc' , icon = Oo0O00O000 , themeit = OOOiiiiI )
 IiIIi1I1I11Ii = o0OO ( base64 . b64decode ( 'aHR0cHM6Ly93d3cuYXBrZmlsZXMuY29tLw==' ) )
 O0Oo0o000oO = re . compile ( 'href="([^"]*)">Applications(.+?)</a>' ) . findall ( IiIIi1I1I11Ii )
 I1i1iii1Ii = re . compile ( 'href="([^"]*)">Games(.+?)</a>' ) . findall ( IiIIi1I1I11Ii )
 for OOOoO000 , OoiiIiI in O0Oo0o000oO :
  o0Ooo0O00 ( '[COLOR deepskyblue]Android Apps[/COLOR]' + OoiiIiI , 'https://www.apkfiles.com' + OOOoO000 , 'apkgame' , i1I1i111Ii )
 for OOOoO000 , OoiiIiI in I1i1iii1Ii :
  o0Ooo0O00 ( '[COLOR deepskyblue]Android Games[/COLOR]' + OoiiIiI , 'https://www.apkfiles.com' + OOOoO000 , 'apkgame' , i111iIi1i1II1 )
 iIi1 ( 'movies' , 'MAIN' )
 oo00O00oO000o ( 'Spinz Apk Picks' , 'apkshow' , url = ii1I , icon = Oo0O00O000 , themeit = OOOiiiiI )
 if O0Oo000ooO00 == 'true' : oo00O00oO000o ( 'XXX Apk' , 'apkshow' , url = i11III1111iIi , icon = Oo0O00O000 , themeit = OOOiiiiI )
 iIi1 ( 'files' , 'viewType' )
 if 9 - 9: O0 . i1Ii
def o0oooO ( url ) :
 o0O0Oo00 = o0OO ( url ) . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
 O0Oo0o000oO = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?con="(.+?)".+?anart="(.+?)"' ) . findall ( o0O0Oo00 )
 if len ( O0Oo0o000oO ) > 0 :
  for oO0o00oOOooO0 , url , i1i1i1I , oOoo000 in O0Oo0o000oO :
   iiiii1II ( oO0o00oOOooO0 , 'apkinstall' , oO0o00oOOooO0 , url , icon = i1i1i1I , fanart = oOoo000 , themeit = OOOiiiiI )
  else : wiz . log ( "[APK Menu] ERROR: Invalid Format." )
 else : wiz . log ( "[APK Menu] ERROR: URL for emu list not working." )
 if 89 - 89: II111iiii / IIIi1i1I
def IIo0OoO00 ( url ) :
 IiIIi1I1I11Ii = o0OO ( url )
 O0Oo0o000oO = re . compile ( '<a href="([^"]*)" >(.+?)</a>' ) . findall ( IiIIi1I1I11Ii )
 for url , oO0o00oOOooO0 in O0Oo0o000oO :
  if '/cat' in url :
   o0Ooo0O00 ( ( oO0o00oOOooO0 ) . replace ( '&amp;' , ' - ' ) , 'https://www.apkfiles.com' + url , 'select' , O000OO0 + 'APK.png' )
   if 18 - 18: IIIi1i1I - I1I1i1 - ooOo - ooOo
def OOooo00 ( url ) :
 IiIIi1I1I11Ii = o0OO ( url )
 oOOo00O0OOOo = url
 if "page=" in str ( url ) :
  oOOo00O0OOOo = url . split ( '?' ) [ 0 ]
 O0Oo0o000oO = re . compile ( '<a href="([^"]*)".+?<img src="([^"]*)" class="file_list_icon".+?alt="([^"]*)"' , re . DOTALL ) . findall ( IiIIi1I1I11Ii )
 I1i1iii1Ii = re . compile ( 'class="[^"]*".+?ref="([^"]*)".+?yle=.+?</a>' ) . findall ( IiIIi1I1I11Ii )
 for url , i1oO , oO0o00oOOooO0 in O0Oo0o000oO :
  if 'apk' in url :
   o0Ooo0O00 ( ( oO0o00oOOooO0 ) . replace ( '&#39;' , '' ) . replace ( '&amp;' , ' - ' ) . replace ( '&#174;:' , ': ' ) . replace ( '&#174;' , ' ' ) , 'https://www.apkfiles.com' + url , 'grab' , 'http:' + i1oO )
 if len ( I1i1iii1Ii ) > 1 :
  I1i1iii1Ii = str ( I1i1iii1Ii [ len ( I1i1iii1Ii ) - 1 ] )
 o0Ooo0O00 ( 'Next Page' , oOOo00O0OOOo + str ( I1i1iii1Ii ) , 'select' , O000OO0 + 'Next.png' )
 if 30 - 30: Ooo0O . I1111
def o0Oii1111i ( name , url ) :
 IiIIi1I1I11Ii = o0OO ( url )
 name = name
 O0Oo0o000oO = re . compile ( 'href="([^"]*)".+?lass="yellow_button".+?itle=' ) . findall ( IiIIi1I1I11Ii )
 for url in O0Oo0o000oO :
  url = 'https://www.apkfiles.com' + url
  O0ooOO ( name , url , 'Brackets' )
  if 28 - 28: i11iIiiIii / I1I1i1 . iIii1I11I1II1 / II111iiii
  if 72 - 72: OoooooooOO / ooOo + IiiIII111ii / o0o0Oo0oooo0 * IiiIII111ii
  if 34 - 34: O0 * O0 % OoooooooOO + iiIIi1IiIi11 * iIii1I11I1II1 % IiiIII111ii
  if 25 - 25: i11IiIiiIIIII + o0o0Oo0oooo0 . I1I1i1 % o0o0Oo0oooo0 * iii11iiII
def ii1IiIi11 ( ) :
 xbmc . executebuiltin ( 'Runscript("special://home/addons/plugin.program.SpinzTV/ookla.py")' )
 if 22 - 22: IIIi1i1I
 if 33 - 33: iIii1I11I1II1 / IiiIII111ii
 if 1 - 1: IiiIII111ii
 if 48 - 48: O0 + O0 . OO00O0O0O00Oo - OOoooooO
def o00oo0000 ( ) :
 if 44 - 44: Ooo0O % iIii1I11I1II1
 if os . path . isfile ( i1i1II ) :
  oo0ooO0 = True
  IIiiiiIiIIii = open ( i1i1II )
  O0OO = IIiiiiIiIIii . read ( )
  IIiiiiIiIIii . close ( )
 else :
  xbmcgui . Dialog ( ) . ok ( "[COLOR orange]SpinzTV[/COLOR]" , "[COLOR cyan][B]][[/B]NT3L[B]][[/B]G3NC[B]][[/B][/COLOR]" , "[COLOR ghostwhite]First Time Launching Will Take a Couple Minutes[/COLOR]" , "[COLOR ghostwhite]Please Be Patient![/COLOR]" )
  oo0ooO0 = False
  if 39 - 39: oO0 + ooOo - iIii1I11I1II1 - I1I1i1
  if 7 - 7: i1Ii . o0o0Oo0oooo0 / oO0 . iii11iiII * i11IiIiiIIIII - II111iiii
  if 37 - 37: OO00O0O0O00Oo . o0o0Oo0oooo0 / O0 * iiIIi1IiIi11
  if 7 - 7: I1111 * i11IiIiiIIIII + II111iiii % i11iIiiIii
  if 8 - 8: OOoooooO * O0
  if 73 - 73: I1I1i1 / IIIi1i1I / i11IiIiiIIIII / I1111
  if 11 - 11: o0o0Oo0oooo0 + i1Ii - OoooooooOO / I1111
  if 34 - 34: OOoooooO
  if 45 - 45: OOoooooO / Ooo0O / IiiIII111ii
  if 44 - 44: oO0 - IiiIII111ii / II111iiii * I1111 * Ooo0O
  if 73 - 73: I1I1i1 - ooOo * i1IIi / i11iIiiIii * iii11iiII % II111iiii
 OooOoOOo0oO00 = ""
 O00O = O0Ooo ( )
 for oO00oOOo0Oo in O00O :
  if oo0ooO0 == True :
   if oO00oOOo0Oo not in O0OO :
    if 5 - 5: I1I1i1 . O0 / Ooo0O % I1111
    if 60 - 60: II111iiii / iIii1I11I1II1 + oO0 . i11iIiiIii
    i1iiIIIi = Oo0o ( OooOoOOo0oO00 , oO00oOOo0Oo )
    OooOoOOo0oO00 = i1iiIIIi
    if 93 - 93: iii11iiII
  else :
   i1iiIIIi = Oo0o ( OooOoOOo0oO00 , oO00oOOo0Oo )
   OooOoOOo0oO00 = i1iiIIIi
   if 43 - 43: oO0 / ooOo . OOoooooO
 if oo0ooO0 == True :
  IIiiiiIiIIii = open ( i1i1II , 'a' )
  if 62 - 62: iIii1I11I1II1 + iiIIi1IiIi11 . Ooo0O / i1Ii % O0 . OO00O0O0O00Oo
  if 93 - 93: i11iIiiIii % iIii1I11I1II1 % i11iIiiIii + I1I1i1 / I1I1i1 / II111iiii
 else :
  IIiiiiIiIIii = open ( i1i1II , 'w' )
  if 49 - 49: iii11iiII . oO0 . i11iIiiIii - II111iiii / IiiIII111ii
  if 62 - 62: iii11iiII
 IIiiiiIiIIii . write ( OooOoOOo0oO00 )
 IIiiiiIiIIii . close ( )
 if 1 - 1: i1Ii / i1Ii - i11iIiiIii
 if 87 - 87: Ooo0O / O0 * i1Ii / I1I1i1
 IIiiiiIiIIii = open ( i1i1II )
 O0OO = IIiiiiIiIIii . read ( )
 IIiiiiIiIIii . close ( )
 O0OO = O0OO . replace ( '\n' , '' ) . replace ( '\r' , '' )
 O0Oo0o000oO = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)".+?nstallRating="(.+?)"' ) . findall ( O0OO )
 if 19 - 19: OO00O0O0O00Oo + i1IIi . ooOo - Ooo0O
 if 16 - 16: IIIi1i1I + OOoooooO / I1I1i1
 for oO0o00oOOooO0 , OOOoO000 , O00oOoo0OoO0 , oOoo000 , IiI11i1IIiiI , Ooo0 in sorted ( O0Oo0o000oO , key = lambda O0Oo0o000oO : O0Oo0o000oO [ 0 ] ) :
  if OOOoO000 in O00O :
   oooO00o0 ( '[COLOR ghostwhite]' + str ( oO0o00oOOooO0 ) + '[/COLOR]' , OOOoO000 , 'intelselect' , O00oOoo0OoO0 , oOoo000 , IiI11i1IIiiI , Ooo0 )
   if 53 - 53: OOoooooO
def O0Ooo ( ) :
 if xbmc . getCondVisibility ( 'system.platform.android' ) :
  try :
   O00O = subprocess . Popen ( [ 'exec ' '/system/bin/pm list packages -3' '' ] , executable = '/system/bin/sh' , shell = True , stdout = subprocess . PIPE , stderr = subprocess . STDOUT ) . communicate ( ) [ 0 ] . rstrip ( '\n' ) . splitlines ( )
  except :
   O00O = [ ]
   if 98 - 98: OO00O0O0O00Oo
  for oO00oOOo0Oo in range ( len ( O00O ) ) :
   O00O [ oO00oOOo0Oo ] = O00O [ oO00oOOo0Oo ] . partition ( ':' ) [ 2 ]
   if 92 - 92: OO00O0O0O00Oo - iIii1I11I1II1
 return O00O
 if 32 - 32: IiiIII111ii % I1111 * I1111 + i1Ii * II111iiii * IiiIII111ii
def Oo0o ( theList , i ) :
 global theNotList
 iIiIii1I1II = "https://play.google.com/store/apps/details?id=" + i
 o0O0Oo00 = O0Oooo ( iIiIii1I1II )
 if 77 - 77: II111iiii
 if o0O0Oo00 != False :
  o0O0Oo00 = o0O0Oo00 . replace ( '\n' , '' ) . replace ( '\r' , '' )
  if 42 - 42: IiiIII111ii * OO00O0O0O00Oo . i1Ii * ooOo + o0o0Oo0oooo0
  i1i1II11II1 = r'<div class="id-app-title".tabindex=".">(.+?)</div>'
  O0Oo0o000oO = re . search ( i1i1II11II1 , o0O0Oo00 )
  if O0Oo0o000oO != None : oO0o00oOOooO0 = O0Oo0o000oO . group ( 1 )
  else : oO0o00oOOooO0 = i
  if 5 - 5: Ooo0O - oO0 % IIIi1i1I - II111iiii . ooOo + iiIIi1IiIi11
  if 47 - 47: O0 - iIii1I11I1II1 - iiIIi1IiIi11
  if 46 - 46: IiiIII111ii . iii11iiII * I1111 . OoooooooOO + oO0
  if 72 - 72: II111iiii + iii11iiII
  if 91 - 91: iIii1I11I1II1 % I1111 . I1I1i1 + IiiIII111ii + I1I1i1
  O00oOoo0OoO0 = "androidapp://sources/apps/" + str ( i ) + ".png"
  if 95 - 95: IiiIII111ii + oO0 * iii11iiII
  if 16 - 16: i11IiIiiIIIII / ooOo + I1111 % iIii1I11I1II1 - i1IIi . IIIi1i1I
  if 26 - 26: I1I1i1 * i1Ii . i1IIi
  if 59 - 59: O0 + i1IIi - I1I1i1
  if 62 - 62: i11iIiiIii % iii11iiII . i1Ii . iii11iiII
  if 84 - 84: i11iIiiIii * I1111
  I1I1iII1i = r'data-expand-to="full-screenshot-[0-9]{1,2}" src="(//\w+?.\w+?.\S+?=h900)"'
  O0Oo0o000oO = re . compile ( I1I1iII1i ) . findall ( o0O0Oo00 )
  if len ( O0Oo0o000oO ) != 0 : oOoo000 = "https:" + O0Oo0o000oO [ len ( O0Oo0o000oO ) - 1 ]
  else : oOoo000 = "None"
  if 30 - 30: O0 + oO0 + II111iiii
  III1I = r'data-video-url="https://www.youtube.com/embed/(\S.+?)\?ps=play.+?"'
  O0Oo0o000oO = re . search ( III1I , o0O0Oo00 )
  if O0Oo0o000oO != None : IiI11i1IIiiI = O0Oo0o000oO . group ( 1 )
  else : IiI11i1IIiiI = "None"
  if 11 - 11: OOoooooO - iii11iiII + OOoooooO * IIIi1i1I / ooOo
  OoOOOO = r'<div class="content" itemprop="numDownloads">\s+?(\d.+?\s-\s\d.+?)\s+?</div>'
  O0Oo0o000oO = re . search ( OoOOOO , o0O0Oo00 )
  if O0Oo0o000oO != None : I1iiIi111I = 'Installed ' + O0Oo0o000oO . group ( 1 )
  else : I1iiIi111I = "Installs: N/A"
  if 34 - 34: i11iIiiIii - II111iiii / ooOo % I1I1i1
  iI1IiiiI11 = r'<div class="score" aria-label=" Rated .+? stars out of five stars ">(.+?)</div>'
  O0Oo0o000oO = re . search ( iI1IiiiI11 , o0O0Oo00 )
  if O0Oo0o000oO != None : OO0OO0O = O0Oo0o000oO . group ( 1 ) + " Stars"
  else : OO0OO0O = "Rating: N/A"
  Ooo0 = OO0OO0O + " " + I1iiIi111I
  if 75 - 75: i11IiIiiIIIII / I1I1i1 / iii11iiII / i1Ii % OOoooooO + II111iiii
  if 4 - 4: iiIIi1IiIi11 - Ooo0O - i1Ii - i11IiIiiIIIII % i11iIiiIii / I1111
  if 50 - 50: OOoooooO + i1IIi
  OOOoO000 = i
  theList += 'name="' + oO0o00oOOooO0 + '"url="' + OOOoO000 + '"img="' + O00oOoo0OoO0 + '"fanart="' + oOoo000 + '"description="' + IiI11i1IIiiI + '"installRating="' + Ooo0 + '"'
  return theList
  if 31 - 31: IiiIII111ii
  if 78 - 78: i11iIiiIii + I1I1i1 + OO00O0O0O00Oo / I1I1i1 % iIii1I11I1II1 % i1Ii
  if 83 - 83: iIii1I11I1II1 % o0o0Oo0oooo0 % I1I1i1 % OO00O0O0O00Oo . oO0 % O0
  if 47 - 47: I1I1i1
  if 66 - 66: ooOo - i1Ii
  if 33 - 33: ooOo / I1111
  if 12 - 12: II111iiii
  if 2 - 2: i1IIi - ooOo + i11IiIiiIIIII . II111iiii
  if 25 - 25: IIIi1i1I
 else :
  if 34 - 34: o0o0Oo0oooo0 . iIii1I11I1II1 % O0
  return theList
  if 43 - 43: oO0 - iiIIi1IiIi11
def O000O ( name , url , iconimage , fanart , videolink ) :
 Oo00OO0 = 0
 if 72 - 72: i1IIi / IIIi1i1I * OO00O0O0O00Oo
 if videolink != "None" :
  Oo00OO0 += 1
  if 40 - 40: IiiIII111ii - o0o0Oo0oooo0 * o0o0Oo0oooo0 . o0o0Oo0oooo0 + OoooooooOO
 if Oo00OO0 == 1 : Oo0 = xbmcgui . Dialog ( ) . select ( '[COLOR deepskyblue]' + name + '[/COLOR]' , [ '[COLOR deepskyblue]Launch[/COLOR]' , '[COLOR ghostwhite]Preview Video[/COLOR]' , '[COLOR tomato]Uninstall[/COLOR]' ] )
 if Oo00OO0 == 0 : Oo0 = xbmcgui . Dialog ( ) . select ( '[COLOR deepskyblue]' + name + '[/COLOR]' , [ '[COLOR deepskyblue]Launch[/COLOR]' , '[COLOR ghostwhite]No Preview Video[/COLOR]' , '[COLOR tomato]Uninstall[/COLOR]' ] )
 if 80 - 80: IiiIII111ii - I1I1i1
 if 41 - 41: I1I1i1 - Ooo0O * ooOo
 if 82 - 82: I1111 % I1I1i1 % iii11iiII / O0
 if Oo0 == 1 :
  if videolink != 'None' :
   yt . PlayVideo ( videolink )
 if Oo0 == 0 :
  OOOO0o0 = xbmcgui . Dialog ( ) . yesno ( "[COLOR orange]SpinzTV[/COLOR]" , "[COLOR cyan][B]][[/B]NT3L[B]][[/B]G3NC[B]][[/B][/COLOR]" , "" , "[COLOR ghostwhite]Would You Like To Launch:[/COLOR] [COLOR cyan]" + name + "[/COLOR]" , "[COLOR red]No Way[/COLOR]" , "[COLOR cyan]Heck Ya![/COLOR]" )
  if OOOO0o0 == 1 :
   xbmc . executebuiltin ( 'StartAndroidActivity(%s)' % url )
 if Oo0 == 2 :
  i1IIIi111Ii = xbmcgui . Dialog ( ) . yesno ( "[COLOR orange]SpinzTV[/COLOR]" , "[COLOR cyan][B]][[/B]NT3L[B]][[/B]G3NC[B]][[/B][/COLOR]" , "" , "[COLOR ghostwhite]Would You Like To Remove:[/COLOR] [COLOR cyan]" + name + "[/COLOR]" , "[COLOR red]No Way[/COLOR]" , "[COLOR cyan]Heck Ya![/COLOR]" )
  if i1IIIi111Ii :
   xbmc . executebuiltin ( 'StartAndroidActivity("","android.intent.action.DELETE","","package:' + url + '")' )
   xbmc . sleep ( 2000 )
   try : shutil . rmtree ( "/sdcard/Android/data/" + url , ignore_errors = True , onerror = None )
   except : pass
   try : shutil . rmtree ( "/sdcard/Android/obb/" + url , ignore_errors = True , onerror = None )
   except : pass
   xbmc . executebuiltin ( 'Container.Refresh' )
   if 15 - 15: I1I1i1
def O0Oooo ( url ) :
 try :
  I1iI = urllib2 . Request ( url )
  I1iI . add_header ( 'User-Agent' , 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3' )
  oO0Ooo0OooOOo = urllib2 . urlopen ( I1iI )
  o0O0Oo00 = oO0Ooo0OooOOo . read ( )
  oO0Ooo0OooOOo . close ( )
  return o0O0Oo00
 except :
  return False
  if 71 - 71: i1Ii + i1IIi * Ooo0O % Ooo0O / Ooo0O
  if 55 - 55: OoooooooOO + OO00O0O0O00Oo + OoooooooOO * OOoooooO
  if 68 - 68: O0
def II1iIII ( ) :
 oo00O00oO000o ( 'Emulators' , 'apkshow' , url = I1i111I , icon = i111iIi1i1II1 , themeit = OOOiiiiI )
 oo00O00oO000o ( 'Roms' , 'roms' , icon = i111iIi1i1II1 , themeit = OOOiiiiI )
 if 79 - 79: OoooooooOO + oO0 - Ooo0O + OoooooooOO
 if 61 - 61: i1IIi * I1111 - Ooo0O - OOoooooO
 if 57 - 57: o0o0Oo0oooo0 . iIii1I11I1II1 % OOoooooO % IiiIII111ii * o0o0Oo0oooo0
 if 8 - 8: o0o0Oo0oooo0 . OOoooooO % IIIi1i1I . ooOo % ooOo . IiiIII111ii
def I1I11ii ( ) :
 oo00O00oO000o ( 'NES' , 'nes' , icon = i111iIi1i1II1 , themeit = OOOiiiiI )
 oo00O00oO000o ( 'SNES' , 'snes' , icon = i111iIi1i1II1 , themeit = OOOiiiiI )
 oo00O00oO000o ( 'Nintendo 64' , 'n64' , icon = i111iIi1i1II1 , themeit = OOOiiiiI )
 oo00O00oO000o ( 'Nintendo DS' , 'nds' , icon = i111iIi1i1II1 , themeit = OOOiiiiI )
 oo00O00oO000o ( 'Genesis' , 'gen' , icon = i111iIi1i1II1 , themeit = OOOiiiiI )
 oo00O00oO000o ( 'Playstation' , 'ps' , icon = i111iIi1i1II1 , themeit = OOOiiiiI )
 oo00O00oO000o ( 'Atari' , 'atr' , icon = i111iIi1i1II1 , themeit = OOOiiiiI )
 oo00O00oO000o ( 'PC Engine & Turbo Grafx' , 'tbg' , icon = i111iIi1i1II1 , themeit = OOOiiiiI )
 if 93 - 93: oO0 % o0o0Oo0oooo0 . O0 / iiIIi1IiIi11 * IIIi1i1I
def i1iii1ii ( url ) :
 o0O0Oo00 = o0OO ( url ) . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
 O0Oo0o000oO = re . compile ( '.+?ame="(.+?)".+?rl="(.+?)".+?con="(.+?)".+?anart="(.+?)"description="(.+?)"' ) . findall ( o0O0Oo00 )
 if len ( O0Oo0o000oO ) > 0 :
  for oO0o00oOOooO0 , url , i1i1i1I , oOoo000 , IiI11i1IIiiI in O0Oo0o000oO :
   II1 ( oO0o00oOOooO0 , 'rominstall' , oO0o00oOOooO0 , url , icon = i1i1i1I , fanart = oOoo000 , description = IiI11i1IIiiI , themeit = OOOiiiiI )
  else : wiz . log ( "[ROM Menu] ERROR: Invalid Format." )
 else : wiz . log ( "[ROM Menu] ERROR: URL for apk list not working." )
 if 27 - 27: IiiIII111ii + ooOo * iIii1I11I1II1 . OoooooooOO * o0o0Oo0oooo0
 if 100 - 100: I1111 / i1IIi - ooOo % IiiIII111ii - iIii1I11I1II1
 if 17 - 17: i11IiIiiIIIII / I1I1i1 % Ooo0O
 if 71 - 71: i1Ii . OO00O0O0O00Oo . I1111
def Oo0O0O00Oo ( ) :
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
 if 10 - 10: IiiIII111ii + i11IiIiiIIIII % OoooooooOO - ooOo
 if 70 - 70: iii11iiII - iiIIi1IiIi11
 if 2 - 2: iIii1I11I1II1
 if 45 - 45: OoooooooOO / i11iIiiIii
def I11I1i1iI ( ) :
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
 if 90 - 90: i1Ii * II111iiii % OO00O0O0O00Oo + IIIi1i1I
 if 93 - 93: OO00O0O0O00Oo + IiiIII111ii
 if 33 - 33: O0
 if 78 - 78: O0 / II111iiii * I1111
 if 50 - 50: OoooooooOO - iIii1I11I1II1 + i1IIi % OO00O0O0O00Oo - iIii1I11I1II1 % O0
def o0oO0Oo ( ) :
 oo00O00oO000o ( 'Genesis Titles A Thru B' , 'rom' , url = oO , icon = i111iIi1i1II1 , themeit = OOOiiiiI )
 oo00O00oO000o ( 'Genesis Titles C Thru D' , 'rom' , url = IIiIi , icon = Oo0O00O000 , themeit = OOOiiiiI )
 oo00O00oO000o ( 'Genesis Titles E Thru G' , 'rom' , url = OOoOooOoOOOoo , icon = i111iIi1i1II1 , themeit = OOOiiiiI )
 oo00O00oO000o ( 'Genesis Titles H Thru L' , 'rom' , url = Iiii1iI1i , icon = i111iIi1i1II1 , themeit = OOOiiiiI )
 oo00O00oO000o ( 'Genesis Titles M Thru O' , 'rom' , url = I1ii1ii11i1I , icon = i111iIi1i1II1 , themeit = OOOiiiiI )
 oo00O00oO000o ( 'Genesis Titles P Thru R' , 'rom' , url = o0OoOO , icon = i111iIi1i1II1 , themeit = OOOiiiiI )
 oo00O00oO000o ( 'Genesis Titles S Thru T' , 'rom' , url = O0O0Oo00 , icon = i111iIi1i1II1 , themeit = OOOiiiiI )
 oo00O00oO000o ( 'Genesis Titles U Thru Z' , 'rom' , url = oOoO00o , icon = i111iIi1i1II1 , themeit = OOOiiiiI )
 if 71 - 71: I1I1i1 - o0o0Oo0oooo0 * iiIIi1IiIi11 + IiiIII111ii % i11iIiiIii - OOoooooO
 if 82 - 82: OO00O0O0O00Oo - iii11iiII + I1111
 if 64 - 64: I1I1i1 . O0 * IiiIII111ii + OoooooooOO - Ooo0O . OoooooooOO
 if 70 - 70: Ooo0O - IIIi1i1I . iIii1I11I1II1 % i11IiIiiIIIII / o0o0Oo0oooo0 - O0
 if 55 - 55: iiIIi1IiIi11 - I1111
def o0i1I11iI1iiI ( ) :
 oo00O00oO000o ( 'Atari Titles A Thru B' , 'rom' , url = oO00O0 , icon = i111iIi1i1II1 , themeit = OOOiiiiI )
 oo00O00oO000o ( 'Atari Titles C Thru D' , 'rom' , url = IIi1IIIi , icon = Oo0O00O000 , themeit = OOOiiiiI )
 oo00O00oO000o ( 'Atari Titles E Thru G' , 'rom' , url = O00Ooo , icon = i111iIi1i1II1 , themeit = OOOiiiiI )
 oo00O00oO000o ( 'Atari Titles H Thru L' , 'rom' , url = OOOO0OOO , icon = i111iIi1i1II1 , themeit = OOOiiiiI )
 oo00O00oO000o ( 'Atari Titles M Thru O' , 'rom' , url = i1i1ii , icon = i111iIi1i1II1 , themeit = OOOiiiiI )
 oo00O00oO000o ( 'Atari Titles P Thru R' , 'rom' , url = iII1ii1 , icon = i111iIi1i1II1 , themeit = OOOiiiiI )
 oo00O00oO000o ( 'Atari Titles S Thru U' , 'rom' , url = I1i1iiiI1 , icon = i111iIi1i1II1 , themeit = OOOiiiiI )
 oo00O00oO000o ( 'Atari Titles V Thru Z' , 'rom' , url = iIIi , icon = i111iIi1i1II1 , themeit = OOOiiiiI )
 if 48 - 48: i11IiIiiIIIII . OoooooooOO . ooOo . o0o0Oo0oooo0 % oO0 / iiIIi1IiIi11
 if 11 - 11: i1IIi % I1111 % iiIIi1IiIi11
 if 99 - 99: OOoooooO / iIii1I11I1II1 - IiiIII111ii * oO0 % ooOo
 if 13 - 13: I1111
 if 70 - 70: OO00O0O0O00Oo + O0 . IIIi1i1I * IiiIII111ii
def ii ( ) :
 oo00O00oO000o ( 'N64 Titles A Thru B' , 'rom' , url = oO0o00oo0 , icon = i111iIi1i1II1 , themeit = OOOiiiiI )
 oo00O00oO000o ( 'N64 Titles C Thru E' , 'rom' , url = ii1IIII , icon = Oo0O00O000 , themeit = OOOiiiiI )
 oo00O00oO000o ( 'N64 Titles F Thru J' , 'rom' , url = oO00oOooooo0 , icon = i111iIi1i1II1 , themeit = OOOiiiiI )
 oo00O00oO000o ( 'N64 Titles K Thru M' , 'rom' , url = oOo , icon = i111iIi1i1II1 , themeit = OOOiiiiI )
 oo00O00oO000o ( 'N64 Titles N Thru R' , 'rom' , url = O0OOooOoO , icon = i111iIi1i1II1 , themeit = OOOiiiiI )
 oo00O00oO000o ( 'N64 Titles S Thru T' , 'rom' , url = i1II1I1Iii1 , icon = i111iIi1i1II1 , themeit = OOOiiiiI )
 oo00O00oO000o ( 'N64 Titles V Thru Z' , 'rom' , url = iiI11Iii , icon = i111iIi1i1II1 , themeit = OOOiiiiI )
 if 9 - 9: I1111 * IiiIII111ii % i1IIi % IIIi1i1I
 if 53 - 53: IIIi1i1I * OoooooooOO . o0o0Oo0oooo0
 if 96 - 96: ooOo % i1IIi . I1I1i1 . O0
 if 37 - 37: i1IIi - iii11iiII % OoooooooOO / iii11iiII % OOoooooO
 if 48 - 48: i11iIiiIii % IIIi1i1I
def i11i11 ( ) :
 oo00O00oO000o ( 'PC Engine And Turbo Grafx Titles A Thru B' , 'rom' , url = O0o0O0 , icon = i111iIi1i1II1 , themeit = OOOiiiiI )
 oo00O00oO000o ( 'PC Engine And Turbo Grafx Titles C Thru E' , 'rom' , url = Ii1II1I11i1 , icon = Oo0O00O000 , themeit = OOOiiiiI )
 oo00O00oO000o ( 'PC Engine And Turbo Grafx Titles F Thru I' , 'rom' , url = oOoooooOoO , icon = i111iIi1i1II1 , themeit = OOOiiiiI )
 oo00O00oO000o ( 'PC Engine And Turbo Grafx Titles J Thru M' , 'rom' , url = Ii111 , icon = i111iIi1i1II1 , themeit = OOOiiiiI )
 oo00O00oO000o ( 'PC Engine And Turbo Grafx Titles N Thru Q' , 'rom' , url = I111i1i1111 , icon = i111iIi1i1II1 , themeit = OOOiiiiI )
 oo00O00oO000o ( 'PC Engine And Turbo Grafx Titles R Thru U' , 'rom' , url = IIII1 , icon = i111iIi1i1II1 , themeit = OOOiiiiI )
 oo00O00oO000o ( 'PC Engine And Turbo Grafx Titles V Thru Z' , 'rom' , url = I1I1i , icon = i111iIi1i1II1 , themeit = OOOiiiiI )
 if 18 - 18: iIii1I11I1II1 + i11IiIiiIIIII * ooOo - iii11iiII / ooOo
 if 78 - 78: i11IiIiiIIIII . i1Ii
 if 38 - 38: o0o0Oo0oooo0 + i1Ii
 if 15 - 15: Ooo0O + i11IiIiiIIIII . OOoooooO - iIii1I11I1II1 / O0 % iIii1I11I1II1
 if 86 - 86: ooOo / IIIi1i1I * IiiIII111ii
def O00o ( ) :
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
 if 86 - 86: oO0 * II111iiii * i11IiIiiIIIII
 if 74 - 74: oO0 / i1Ii
 if 60 - 60: oO0
 if 1 - 1: o0o0Oo0oooo0 . i11iIiiIii % o0o0Oo0oooo0 - iiIIi1IiIi11 % i1IIi + oO0
def IiiIiIi111iI1 ( ) :
 oo00O00oO000o ( 'Playstation Titles A' , 'rom' , url = oO00oo0o00o0o , icon = i111iIi1i1II1 , themeit = OOOiiiiI )
 oo00O00oO000o ( 'Playstation Titles B' , 'rom' , url = IiIIIIIi , icon = i111iIi1i1II1 , themeit = OOOiiiiI )
 oo00O00oO000o ( 'Playstation Titles C Thru D' , 'rom' , url = IiIi1iIIi1 , icon = i111iIi1i1II1 , themeit = OOOiiiiI )
 oo00O00oO000o ( 'Playstation Titles E Thru F' , 'rom' , url = O0OoO0ooOO0o , icon = i111iIi1i1II1 , themeit = OOOiiiiI )
 oo00O00oO000o ( 'Playstation Titles G Thru J' , 'rom' , url = OoOo0oOooOoOO , icon = i111iIi1i1II1 , themeit = OOOiiiiI )
 oo00O00oO000o ( 'Playstation Titles K Thru N' , 'rom' , url = oo00ooOoO00 , icon = i111iIi1i1II1 , themeit = OOOiiiiI )
 oo00O00oO000o ( 'Playstation Titles O Thru R' , 'rom' , url = o00oOoOo0 , icon = i111iIi1i1II1 , themeit = OOOiiiiI )
 oo00O00oO000o ( 'Playstation Titles S Thru T' , 'rom' , url = o0O0O0ooo0oOO , icon = i111iIi1i1II1 , themeit = OOOiiiiI )
 oo00O00oO000o ( 'Playstation Titles U Thru Z' , 'rom' , url = oo000 , icon = i111iIi1i1II1 , themeit = OOOiiiiI )
 if 88 - 88: Ooo0O % IIIi1i1I + i1Ii
def IiIi1Oo00o000oOO ( url = None ) :
 if not OO == 'http://' :
  if url == None :
   ii1i1iiI = wiz . workingURL ( OO )
   Oo0oOo0ooOOOo = uservar . ADDONFILE
  else :
   ii1i1iiI = wiz . workingURL ( url )
   Oo0oOo0ooOOOo = url
  if ii1i1iiI == True :
   o0O0Oo00 = wiz . openURL ( Oo0oOo0ooOOOo ) . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' ) . replace ( 'repository=""' , 'repository="none"' ) . replace ( 'repositoryurl=""' , 'repositoryurl="http://"' ) . replace ( 'repositoryxml=""' , 'repositoryxml="http://"' )
   O0Oo0o000oO = re . compile ( 'name="(.+?)".+?lugin="(.+?)".+?rl="(.+?)".+?epository="(.+?)".+?epositoryxml="(.+?)".+?epositoryurl="(.+?)".+?con="(.+?)".+?anart="(.+?)".+?dult="(.+?)".+?escription="(.+?)"' ) . findall ( o0O0Oo00 )
   if len ( O0Oo0o000oO ) > 0 :
    ooOO00oOOo000 = 0
    for oO0o00oOOooO0 , OoO0000o , url , o0Ii1 , IIi1IiII , o0IIIIiI11I , i1i1i1I , oOoo000 , OooOo00o , IiI11i1IIiiI in O0Oo0o000oO :
     if OoO0000o . lower ( ) == 'section' :
      ooOO00oOOo000 += 1
      oo00O00oO000o ( "[B]%s[/B]" % oO0o00oOOooO0 , 'addons' , url , description = IiI11i1IIiiI , icon = i1i1i1I , fanart = oOoo000 , themeit = OOoO )
     else :
      if not O0Oo000ooO00 == 'true' and OooOo00o . lower ( ) == 'yes' : continue
      try :
       iiiI11iIIi1 = xbmcaddon . Addon ( id = OoO0000o ) . getAddonInfo ( 'path' )
       if os . path . exists ( iiiI11iIIi1 ) :
        oO0o00oOOooO0 = "[COLOR green][Installed][/COLOR] %s" % oO0o00oOOooO0
      except :
       pass
      ooOO00oOOo000 += 1
      iiiii1II ( oO0o00oOOooO0 , 'addoninstall' , OoO0000o , Oo0oOo0ooOOOo , description = IiI11i1IIiiI , icon = i1i1i1I , fanart = oOoo000 , themeit = oooOo0OOOoo0 )
     if ooOO00oOOo000 < 1 :
      iiiii1II ( "No addons added to this menu yet!" , '' , themeit = oooOo0OOOoo0 )
   else :
    iiiii1II ( 'Text File not formated correctly!' , '' , themeit = OOoO )
    wiz . log ( "[Addon Menu] ERROR: Invalid Format." )
  else :
   wiz . log ( "[Addon Menu] ERROR: URL for Addon list not working." )
   iiiii1II ( 'Url for txt file not valid' , '' , themeit = OOoO )
   iiiii1II ( '%s' % ii1i1iiI , '' , themeit = OOoO )
 else : wiz . log ( "[Addon Menu] No Addon list added." )
 iIi1 ( 'files' , 'viewType' )
 if 72 - 72: iiIIi1IiIi11 * iii11iiII
def oooo ( plugin , url ) :
 if not OO == 'http://' :
  ii1i1iiI = wiz . workingURL ( url )
  if ii1i1iiI == True :
   o0O0Oo00 = wiz . openURL ( url ) . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' ) . replace ( 'repository=""' , 'repository="none"' ) . replace ( 'repositoryurl=""' , 'repositoryurl="http://"' ) . replace ( 'repositoryxml=""' , 'repositoryxml="http://"' )
   O0Oo0o000oO = re . compile ( 'name="(.+?)".+?lugin="%s".+?rl="(.+?)".+?epository="(.+?)".+?epositoryxml="(.+?)".+?epositoryurl="(.+?)".+?con="(.+?)".+?anart="(.+?)".+?dult="(.+?)".+?escription="(.+?)"' % plugin ) . findall ( o0O0Oo00 )
   if len ( O0Oo0o000oO ) > 0 :
    for oO0o00oOOooO0 , url , o0Ii1 , IIi1IiII , o0IIIIiI11I , i1i1i1I , oOoo000 , OooOo00o , IiI11i1IIiiI in O0Oo0o000oO :
     if os . path . exists ( os . path . join ( O0O , plugin ) ) :
      iiiIIIii = [ 'Launch Addon' , 'Remove Addon' ]
      ooOoo00 = iiIIIII1i1iI . select ( "[COLOR %s]Addon already installed what would you like to do?[/COLOR]" % iIiIi11 , iiiIIIii )
      if ooOoo00 == 0 :
       wiz . ebi ( 'RunAddon(%s)' % plugin )
       xbmc . sleep ( 500 )
       return True
      elif ooOoo00 == 1 :
       wiz . cleanHouse ( os . path . join ( O0O , plugin ) )
       try : wiz . removeFolder ( os . path . join ( O0O , plugin ) )
       except : pass
       if iiIIIII1i1iI . yesno ( o0OOO , "[COLOR %s]Would you like to remove the addon_data for:" % iIiIi11 , "[COLOR %s]%s[/COLOR]?[/COLOR]" % ( oOOo0O00o , plugin ) , yeslabel = "[B][COLOR green]Yes Remove[/COLOR][/B]" , nolabel = "[B][COLOR red]No Skip[/COLOR][/B]" ) :
        Ii11IiI ( plugin )
       wiz . refresh ( )
       return True
      else :
       return False
     o00oOoO0Oo = os . path . join ( O0O , o0Ii1 )
     if not o0Ii1 . lower ( ) == 'none' and not os . path . exists ( o00oOoO0Oo ) :
      wiz . log ( "Repository not installed, installing it" )
      if iiIIIII1i1iI . yesno ( o0OOO , "[COLOR %s]Would you like to install the repository for [COLOR %s]%s[/COLOR]:" % ( iIiIi11 , oOOo0O00o , plugin ) , "[COLOR %s]%s[/COLOR]?[/COLOR]" % ( oOOo0O00o , o0Ii1 ) , yeslabel = "[B][COLOR green]Yes Install[/COLOR][/B]" , nolabel = "[B][COLOR red]No Skip[/COLOR][/B]" ) :
       i1iIi = wiz . parseDOM ( wiz . openURL ( IIi1IiII ) , 'addon' , ret = 'version' , attrs = { 'id' : o0Ii1 } )
       if len ( i1iIi ) > 0 :
        Ii1iiII1i = '%s%s-%s.zip' % ( o0IIIIiI11I , o0Ii1 , i1iIi [ 0 ] )
        wiz . log ( Ii1iiII1i )
        if o0OIiII >= 17 : wiz . addonDatabase ( o0Ii1 , 1 )
        oO00O ( o0Ii1 , Ii1iiII1i )
        wiz . ebi ( 'UpdateAddonRepos()' )
        if 15 - 15: Ooo0O + Ooo0O / i1Ii * i11IiIiiIIIII . OOoooooO + iiIIi1IiIi11
        wiz . log ( "Installing Addon from Kodi" )
        II1iIiiI11i11 = iII11iiIIi11 ( plugin )
        wiz . log ( "Install from Kodi: %s" % II1iIiiI11i11 )
        if II1iIiiI11i11 :
         wiz . refresh ( )
         return True
       else :
        wiz . log ( "[Addon Installer] Repository not installed: Unable to grab url! (%s)" % o0Ii1 )
      else : wiz . log ( "[Addon Installer] Repository for %s not installed: %s" % ( plugin , o0Ii1 ) )
     elif o0Ii1 . lower ( ) == 'none' :
      wiz . log ( "No repository, installing addon" )
      Iiii11I = plugin
      OO0ooo0 = url
      oO00O ( plugin , url )
      wiz . refresh ( )
      return True
     else :
      wiz . log ( "Repository installed, installing addon" )
      II1iIiiI11i11 = iII11iiIIi11 ( plugin , False )
      if II1iIiiI11i11 :
       wiz . refresh ( )
       return True
     if os . path . exists ( os . path . join ( O0O , plugin ) ) : return True
     II1II1iI = wiz . parseDOM ( wiz . openURL ( IIi1IiII ) , 'addon' , ret = 'version' , attrs = { 'id' : plugin } )
     if len ( II1II1iI ) > 0 :
      url = "%s%s-%s.zip" % ( url , plugin , II1II1iI [ 0 ] )
      wiz . log ( str ( url ) )
      if o0OIiII >= 17 : wiz . addonDatabase ( plugin , 1 )
      oO00O ( plugin , url )
      wiz . refresh ( )
     else :
      wiz . log ( "no match" ) ; return False
   else : wiz . log ( "[Addon Installer] Invalid Format" )
  else : wiz . log ( "[Addon Installer] Text File: %s" % ii1i1iiI )
 else : wiz . log ( "[Addon Installer] Not Enabled." )
 if 58 - 58: O0 . i1Ii / OoooooooOO . I1111 / Ooo0O * II111iiii
def iII11iiIIi11 ( plugin , over = True ) :
 if over == True :
  xbmc . sleep ( 2000 )
  if 53 - 53: IiiIII111ii - O0 / I1I1i1 % iiIIi1IiIi11 * ooOo % iii11iiII
 wiz . ebi ( 'RunPlugin(plugin://%s)' % plugin )
 if not wiz . whileWindow ( 'yesnodialog' ) :
  return False
 xbmc . sleep ( 500 )
 if wiz . whileWindow ( 'okdialog' ) :
  return False
 wiz . whileWindow ( 'progressdialog' )
 if os . path . exists ( os . path . join ( O0O , plugin ) ) : return True
 else : return False
 if 69 - 69: oO0
def oO00O ( name , url ) :
 if not wiz . workingURL ( url ) == True : wiz . LogNotify ( "[COLOR %s]Addon Installer[/COLOR]" % oOOo0O00o , '[COLOR %s]%s:[/COLOR] [COLOR %s]Invalid Zip Url![/COLOR]' % ( oOOo0O00o , name , iIiIi11 ) ) ; return
 if not os . path . exists ( o0o0OOO0o0 ) : os . makedirs ( o0o0OOO0o0 )
 oo00 . create ( o0OOO , '[COLOR %s][B]Downloading:[/B][/COLOR] [COLOR %s]%s[/COLOR]' % ( iIiIi11 , oOOo0O00o , name ) , '' , '[COLOR %s]Please Wait[/COLOR]' % iIiIi11 )
 oOOO0ooo = url . split ( '/' )
 I1III1iIi = os . path . join ( o0o0OOO0o0 , oOOO0ooo [ - 1 ] )
 try : os . remove ( I1III1iIi )
 except : pass
 downloader . download ( url , I1III1iIi , oo00 )
 II1iIi1IiIii = '[COLOR %s][B]Installing:[/B][/COLOR] [COLOR %s]%s[/COLOR]' % ( iIiIi11 , oOOo0O00o , name )
 oo00 . update ( 0 , II1iIi1IiIii , '' , '[COLOR %s]Please Wait[/COLOR]' % iIiIi11 )
 OoO00O0 , I1 , Iiii1i11ii1Ii = extract . all ( I1III1iIi , O0O , oo00 , title = II1iIi1IiIii )
 oo00 . update ( 0 , II1iIi1IiIii , '' , '[COLOR %s]Installing Dependencies[/COLOR]' % iIiIi11 )
 i1Oo0oOo000OoO0 ( name )
 IIii1I1i ( name , oo00 )
 oo00 . close ( )
 wiz . ebi ( 'UpdateAddonRepos()' )
 wiz . ebi ( 'UpdateLocalAddons()' )
 wiz . refresh ( )
 if 22 - 22: Ooo0O % I1111 - OoooooooOO * Ooo0O
def IIii1I1i ( name , DP = None ) :
 ii1i = os . path . join ( O0O , name , 'addon.xml' )
 if os . path . exists ( ii1i ) :
  i1IiiiiIi1I = open ( ii1i , mode = 'r' ) ; o0O0Oo00 = i1IiiiiIi1I . read ( ) ; i1IiiiiIi1I . close ( ) ;
  O0Oo0o000oO = wiz . parseDOM ( o0O0Oo00 , 'import' , ret = 'addon' )
  for ooo0O0o0OoOO in O0Oo0o000oO :
   if not 'xbmc.python' in ooo0O0o0OoOO :
    if not DP == None :
     DP . update ( 0 , '' , '[COLOR %s]%s[/COLOR]' % ( oOOo0O00o , ooo0O0o0OoOO ) )
    wiz . createTemp ( ooo0O0o0OoOO )
    if 9 - 9: I1111
    if 60 - 60: OO00O0O0O00Oo
    if 98 - 98: OOoooooO
    if 34 - 34: iIii1I11I1II1 * i11IiIiiIIIII * i11IiIiiIIIII / oO0
    if 28 - 28: I1111 - IIIi1i1I + o0o0Oo0oooo0 + IiiIII111ii / iIii1I11I1II1
    if 26 - 26: iIii1I11I1II1 - O0 . O0
    if 68 - 68: iii11iiII + IIIi1i1I . O0 . IiiIII111ii % i1IIi % iii11iiII
    if 50 - 50: i1Ii + I1I1i1
    if 96 - 96: I1111
    if 92 - 92: Ooo0O / i11iIiiIii + oO0
    if 87 - 87: o0o0Oo0oooo0 % iIii1I11I1II1
    if 72 - 72: iii11iiII . iii11iiII - oO0
    if 48 - 48: Ooo0O - OOoooooO + Ooo0O - ooOo * i11iIiiIii . iiIIi1IiIi11
    if 35 - 35: i1Ii . O0 + Ooo0O + iii11iiII + i1IIi
    if 65 - 65: O0 * ooOo / ooOo . o0o0Oo0oooo0
    if 87 - 87: II111iiii * oO0 % Ooo0O * Ooo0O
    if 58 - 58: iii11iiII . I1I1i1 + ooOo % Ooo0O - I1111
    if 50 - 50: iiIIi1IiIi11 % II111iiii - OOoooooO . i1IIi + O0 % iiIIi1IiIi11
    if 10 - 10: iiIIi1IiIi11 . i1IIi + IiiIII111ii
    if 66 - 66: I1111 % I1I1i1
    if 21 - 21: o0o0Oo0oooo0 - OoooooooOO % i11iIiiIii
    if 71 - 71: i1IIi - i11IiIiiIIIII * OO00O0O0O00Oo + IIIi1i1I - I1111 % oO0
    if 63 - 63: iIii1I11I1II1 + iii11iiII . I1111 / ooOo
    if 84 - 84: i1IIi
    if 42 - 42: II111iiii - I1111 - OoooooooOO . iiIIi1IiIi11 / o0o0Oo0oooo0
    if 56 - 56: i11iIiiIii - iIii1I11I1II1 . II111iiii
def i1Oo0oOo000OoO0 ( addon ) :
 OOOoO000 = os . path . join ( O0O , addon , 'addon.xml' )
 if os . path . exists ( OOOoO000 ) :
  try :
   list = open ( OOOoO000 , mode = 'r' ) ; O00OII1 = list . read ( ) ; list . close ( )
   oO0o00oOOooO0 = wiz . parseDOM ( O00OII1 , 'addon' , ret = 'name' , attrs = { 'id' : addon } )
   i1i1i1I = os . path . join ( O0O , addon , 'icon.png' )
   wiz . LogNotify ( '[COLOR %s]%s[/COLOR]' % ( oOOo0O00o , oO0o00oOOooO0 [ 0 ] ) , '[COLOR %s]Addon Enabled[/COLOR]' % iIiIi11 , '2000' , i1i1i1I )
  except : pass
  if 91 - 91: iii11iiII + OO00O0O0O00Oo . i11IiIiiIIIII
def i1I111i1ii ( url = None ) :
 if not oO0O0OO0O == 'http://' :
  if url == None :
   oO0oOoo0O = wiz . workingURL ( oO0O0OO0O )
   II1iI11 = uservar . YOUTUBEFILE
  else :
   oO0oOoo0O = wiz . workingURL ( url )
   II1iI11 = url
  if oO0oOoo0O == True :
   o0O0Oo00 = wiz . openURL ( II1iI11 ) . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
   O0Oo0o000oO = re . compile ( 'name="(.+?)".+?ection="(.+?)".+?rl="(.+?)".+?con="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( o0O0Oo00 )
   if len ( O0Oo0o000oO ) > 0 :
    for oO0o00oOOooO0 , O00o0O , url , i1i1i1I , oOoo000 , IiI11i1IIiiI in O0Oo0o000oO :
     if O00o0O . lower ( ) == "yes" :
      oo00O00oO000o ( "[B]%s[/B]" % oO0o00oOOooO0 , 'youtube' , url , description = IiI11i1IIiiI , icon = i1i1i1I , fanart = oOoo000 , themeit = OOoO )
     else :
      iiiii1II ( oO0o00oOOooO0 , 'viewVideo' , url = url , description = IiI11i1IIiiI , icon = i1i1i1I , fanart = oOoo000 , themeit = oooOo0OOOoo0 )
   else : wiz . log ( "[YouTube Menu] ERROR: Invalid Format." )
  else :
   wiz . log ( "[YouTube Menu] ERROR: URL for YouTube list not working." )
   iiiii1II ( 'Url for txt file not valid' , '' , themeit = OOoO )
   iiiii1II ( '%s' % oO0oOoo0O , '' , themeit = OOoO )
 else : wiz . log ( "[YouTube Menu] No YouTube list added." )
 iIi1 ( 'files' , 'viewType' )
 if 85 - 85: iii11iiII * i1IIi % ooOo - OOoooooO
def I11I1ii1i ( view = None ) :
 II11Ii111II1 = '[B][COLOR green]ON[/COLOR][/B]' ; O00OOO00Ooo = '[B][COLOR red]OFF[/COLOR][/B]'
 OoOOoooO000 = 'true' if ooOooo000oOO == 'true' else 'false'
 OoO0o000oOo = 'true' if Oo0oOOo == 'true' else 'false'
 Oo00OO00o0oO = 'true' if Oo0OoO00oOO0o == 'true' else 'false'
 iI1 = 'true' if OOO00O == 'true' else 'false'
 I1I1i1i = 'true' if oO0Ii1iIiII1ii1 == 'true' else 'false'
 OOo0O = 'true' if O00O0oOO00O00 == 'true' else 'false'
 oOOoooO0O0 = 'true' if i1Oo00 == 'true' else 'false'
 ii1O0ooooo000 = 'true' if oOooOOOoOo == 'true' else 'false'
 if wiz . Grab_Log ( True ) == False : OooOoOO0OO = 0
 else : OooOoOO0OO = I1iiIiiii1111 ( wiz . Grab_Log ( True ) , True , True )
 if wiz . Grab_Log ( True , True ) == False : I1ii1i11i = 0
 else : I1ii1i11i = I1iiIiiii1111 ( wiz . Grab_Log ( True , True ) , True , True )
 Oooooo0O00o = int ( OooOoOO0OO ) + int ( I1ii1i11i )
 II11ii1 = str ( Oooooo0O00o ) + ' Error(s) Found' if Oooooo0O00o > 0 else 'None Found'
 ii1II1II = ': [COLOR red]Not Found[/COLOR]' if not os . path . exists ( I11iii1Ii ) else ": [COLOR green]%s[/COLOR]" % wiz . convertSize ( os . path . getsize ( I11iii1Ii ) )
 if oOOoooO0O0 == 'true' :
  i11i11II11i = 'true'
  II1Ii1I1i = 'true'
  OOooOooo0OOo0 = 'true'
  oo0o0OoOO0o0 = 'true'
  III1III11II = 'true'
  iIi1iI = 'true'
  OO0Oo = 'true'
  IIiiiiiIiIIi = 'true'
 else :
  i11i11II11i = 'true' if i1i == 'true' else 'false'
  II1Ii1I1i = 'true' if iiI111I1iIiI == 'true' else 'false'
  OOooOooo0OOo0 = 'true' if IIIi1I1IIii1II == 'true' else 'false'
  oo0o0OoOO0o0 = 'true' if O0ii1ii1ii == 'true' else 'false'
  III1III11II = 'true' if oooooOoo0ooo == 'true' else 'false'
  iIi1iI = 'true' if I1I1IiI1 == 'true' else 'false'
  OO0Oo = 'true' if III1iII1I1ii == 'true' else 'false'
  IIiiiiiIiIIi = 'true' if oOOo0 == 'true' else 'false'
 iiIiiIi1 = wiz . getSize ( o0o0OOO0o0 )
 I1Ii11i = wiz . getSize ( oOoOooOo0o0 )
 I1iIiiiI1 = wiz . getCacheSize ( )
 OOO0O00Oo = iiIiiIi1 + I1Ii11i + I1iIiiiI1
 ii1oOOO0ooOO = [ 'Always' , 'Daily' , '3 Days' , 'Weekly' ]
 oo00O00oO000o ( '[B]Cleaning Tools[/B]' , 'maint' , 'clean' , icon = IiIi11iI , themeit = OOOiiiiI )
 if view == "clean" or oO0Ii1iIiII1ii1 == 'true' :
  iiiii1II ( 'Total Clean Up: [COLOR green][B]%s[/B][/COLOR]' % wiz . convertSize ( OOO0O00Oo ) , 'fullclean' , icon = IiIi11iI , themeit = OOoO )
  iiiii1II ( 'Clear Cache: [COLOR green][B]%s[/B][/COLOR]' % wiz . convertSize ( I1iIiiiI1 ) , 'clearcache' , icon = IiIi11iI , themeit = OOoO )
  iiiii1II ( 'Clear Packages: [COLOR green][B]%s[/B][/COLOR]' % wiz . convertSize ( iiIiiIi1 ) , 'clearpackages' , icon = IiIi11iI , themeit = OOoO )
  iiiii1II ( 'Clear Thumbnails: [COLOR green][B]%s[/B][/COLOR]' % wiz . convertSize ( I1Ii11i ) , 'clearthumb' , icon = IiIi11iI , themeit = OOoO )
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
  iiiii1II ( 'View Errors in Log: %s' % ( II11ii1 ) , 'viewerrorlog' , icon = IiIi11iI , themeit = OOoO )
  iiiii1II ( 'View Log File' , 'viewlog' , icon = IiIi11iI , themeit = OOoO )
  iiiii1II ( 'View Wizard Log File' , 'viewwizlog' , icon = IiIi11iI , themeit = OOoO )
  iiiii1II ( 'Clear Wizard Log File%s' % ii1II1II , 'clearwizlog' , icon = IiIi11iI , themeit = OOoO )
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
 iiiii1II ( 'Show All Maintenance: %s' % I1I1i1i . replace ( 'true' , II11Ii111II1 ) . replace ( 'false' , O00OOO00Ooo ) , 'togglesetting' , 'showmaint' , icon = IiIi11iI , themeit = oooOo0OOOoo0 )
 oo00O00oO000o ( '[I]<< Return to Main Menu[/I]' , icon = IiIi11iI , themeit = oooOo0OOOoo0 )
 iiiii1II ( 'Third Party Wizards: %s' % ii1O0ooooo000 . replace ( 'true' , II11Ii111II1 ) . replace ( 'false' , O00OOO00Ooo ) , 'togglesetting' , 'enable3rd' , fanart = OOO00 , icon = IiIi11iI , themeit = OOOiiiiI )
 if ii1O0ooooo000 == 'true' :
  i11IiI1iiI11 = i1Iii1i1I if not i1Iii1i1I == '' else 'Not Set'
  OOoOOOO00 = IiI111111IIII if not IiI111111IIII == '' else 'Not Set'
  iiIi1IIiI = OOO if not OOO == '' else 'Not Set'
  iiiii1II ( 'Edit Third Party Wizard 1: [COLOR %s]%s[/COLOR]' % ( iIiIi11 , i11IiI1iiI11 ) , 'editthird' , '1' , icon = IiIi11iI , themeit = OOoO )
  iiiii1II ( 'Edit Third Party Wizard 2: [COLOR %s]%s[/COLOR]' % ( iIiIi11 , OOoOOOO00 ) , 'editthird' , '2' , icon = IiIi11iI , themeit = OOoO )
  iiiii1II ( 'Edit Third Party Wizard 3: [COLOR %s]%s[/COLOR]' % ( iIiIi11 , iiIi1IIiI ) , 'editthird' , '3' , icon = IiIi11iI , themeit = OOoO )
 iiiii1II ( 'Auto Clean' , '' , fanart = OOO00 , icon = IiIi11iI , themeit = OOOiiiiI )
 iiiii1II ( 'Auto Clean Up On Startup: %s' % OoOOoooO000 . replace ( 'true' , II11Ii111II1 ) . replace ( 'false' , O00OOO00Ooo ) , 'togglesetting' , 'autoclean' , icon = IiIi11iI , themeit = OOoO )
 if OoOOoooO000 == 'true' :
  iiiii1II ( '--- Auto Clean Fequency: [B][COLOR green]%s[/COLOR][/B]' % ii1oOOO0ooOO [ OOoOO0oo0ooO ] , 'changefeq' , icon = IiIi11iI , themeit = OOoO )
  iiiii1II ( '--- Clear Cache on Startup: %s' % OoO0o000oOo . replace ( 'true' , II11Ii111II1 ) . replace ( 'false' , O00OOO00Ooo ) , 'togglesetting' , 'clearcache' , icon = IiIi11iI , themeit = OOoO )
  iiiii1II ( '--- Clear Packages on Startup: %s' % Oo00OO00o0oO . replace ( 'true' , II11Ii111II1 ) . replace ( 'false' , O00OOO00Ooo ) , 'togglesetting' , 'clearpackages' , icon = IiIi11iI , themeit = OOoO )
  iiiii1II ( '--- Clear Old Thumbs on Startup: %s' % iI1 . replace ( 'true' , II11Ii111II1 ) . replace ( 'false' , O00OOO00Ooo ) , 'togglesetting' , 'clearthumbs' , icon = IiIi11iI , themeit = OOoO )
 iiiii1II ( 'Clear Video Cache' , '' , fanart = OOO00 , icon = IiIi11iI , themeit = OOOiiiiI )
 iiiii1II ( 'Include Video Cache in Clear Cache: %s' % OOo0O . replace ( 'true' , II11Ii111II1 ) . replace ( 'false' , O00OOO00Ooo ) , 'togglecache' , 'includevideo' , icon = IiIi11iI , themeit = OOoO )
 if OOo0O == 'true' :
  iiiii1II ( '--- Include All Video Addons: %s' % oOOoooO0O0 . replace ( 'true' , II11Ii111II1 ) . replace ( 'false' , O00OOO00Ooo ) , 'togglecache' , 'includeall' , icon = IiIi11iI , themeit = OOoO )
  iiiii1II ( '--- Include Bob: %s' % i11i11II11i . replace ( 'true' , II11Ii111II1 ) . replace ( 'false' , O00OOO00Ooo ) , 'togglecache' , 'includebob' , icon = IiIi11iI , themeit = OOoO )
  iiiii1II ( '--- Include Phoenix: %s' % II1Ii1I1i . replace ( 'true' , II11Ii111II1 ) . replace ( 'false' , O00OOO00Ooo ) , 'togglecache' , 'includephoenix' , icon = IiIi11iI , themeit = OOoO )
  iiiii1II ( '--- Include Specto: %s' % OOooOooo0OOo0 . replace ( 'true' , II11Ii111II1 ) . replace ( 'false' , O00OOO00Ooo ) , 'togglecache' , 'includespecto' , icon = IiIi11iI , themeit = OOoO )
  iiiii1II ( '--- Include Exodus: %s' % III1III11II . replace ( 'true' , II11Ii111II1 ) . replace ( 'false' , O00OOO00Ooo ) , 'togglecache' , 'includeexodus' , icon = IiIi11iI , themeit = OOoO )
  iiiii1II ( '--- Include Salts: %s' % OO0Oo . replace ( 'true' , II11Ii111II1 ) . replace ( 'false' , O00OOO00Ooo ) , 'togglecache' , 'includesalts' , icon = IiIi11iI , themeit = OOoO )
  iiiii1II ( '--- Include Salts HD Lite: %s' % IIiiiiiIiIIi . replace ( 'true' , II11Ii111II1 ) . replace ( 'false' , O00OOO00Ooo ) , 'togglecache' , 'includesaltslite' , icon = IiIi11iI , themeit = OOoO )
  iiiii1II ( '--- Include One Channel: %s' % iIi1iI . replace ( 'true' , II11Ii111II1 ) . replace ( 'false' , O00OOO00Ooo ) , 'togglecache' , 'includeonechan' , icon = IiIi11iI , themeit = OOoO )
  iiiii1II ( '--- Include Genesis: %s' % oo0o0OoOO0o0 . replace ( 'true' , II11Ii111II1 ) . replace ( 'false' , O00OOO00Ooo ) , 'togglecache' , 'includegenesis' , icon = IiIi11iI , themeit = OOoO )
  iiiii1II ( '--- Enable All Video Addons' , 'togglecache' , 'true' , icon = IiIi11iI , themeit = OOoO )
  iiiii1II ( '--- Disable All Video Addons' , 'togglecache' , 'false' , icon = IiIi11iI , themeit = OOoO )
 iIi1 ( 'files' , 'viewType' )
 if 49 - 49: I1111 - O0 / I1111 * o0o0Oo0oooo0 + OO00O0O0O00Oo
def Iiii1I ( url = None ) :
 if not OoOoO == 'http://' :
  if url == None :
   Ooo000000 = wiz . workingURL ( OoOoO )
   Oo00ooOoO = uservar . ADVANCEDFILE
  else :
   Ooo000000 = wiz . workingURL ( url )
   Oo00ooOoO = url
  iiiii1II ( 'Quick Configure AdvancedSettings.xml' , 'autoadvanced' , icon = IiIi11iI , themeit = OOoO )
  if os . path . exists ( I11II1i ) :
   iiiii1II ( 'View Currect AdvancedSettings.xml' , 'currentsettings' , icon = IiIi11iI , themeit = OOoO )
   iiiii1II ( 'Remove Currect AdvancedSettings.xml' , 'removeadvanced' , icon = IiIi11iI , themeit = OOoO )
  if Ooo000000 == True :
   if O0O0ooOOO == 'No' : iiiii1II ( wiz . sep ( ) , '' , icon = IiIi11iI , themeit = OOoO )
   o0O0Oo00 = wiz . openURL ( Oo00ooOoO ) . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
   O0Oo0o000oO = re . compile ( 'name="(.+?)".+?ection="(.+?)".+?rl="(.+?)".+?con="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( o0O0Oo00 )
   if len ( O0Oo0o000oO ) > 0 :
    for oO0o00oOOooO0 , O00o0O , url , i1i1i1I , oOoo000 , IiI11i1IIiiI in O0Oo0o000oO :
     if O00o0O . lower ( ) == "yes" :
      oo00O00oO000o ( "[B]%s[/B]" % oO0o00oOOooO0 , 'advancedsetting' , url , description = IiI11i1IIiiI , icon = i1i1i1I , fanart = oOoo000 , themeit = OOoO )
     else :
      iiiii1II ( oO0o00oOOooO0 , 'writeadvanced' , oO0o00oOOooO0 , url , description = IiI11i1IIiiI , icon = i1i1i1I , fanart = oOoo000 , themeit = oooOo0OOOoo0 )
   else : wiz . log ( "[Advanced Settings] ERROR: Invalid Format." )
  else : wiz . log ( "[Advanced Settings] URL not working: %s" % Ooo000000 )
 else : wiz . log ( "[Advanced Settings] not Enabled" )
 if 100 - 100: i11iIiiIii / i11iIiiIii
def o00iIiiiII ( name , url ) :
 Ooo000000 = wiz . workingURL ( url )
 if Ooo000000 == True :
  if os . path . exists ( I11II1i ) : Ii1I1 = iiIIIII1i1iI . yesno ( o0OOO , "[COLOR %s]Would you like to overwrite your current Advanced Settings with [COLOR %s]%s[/COLOR]?[/COLOR]" % ( iIiIi11 , oOOo0O00o , name ) , yeslabel = "[B][COLOR green]Overwrite[/COLOR][/B]" , nolabel = "[B][COLOR red]Cancel[/COLOR][/B]" )
  else : Ii1I1 = iiIIIII1i1iI . yesno ( o0OOO , "[COLOR %s]Would you like to download and install [COLOR %s]%s[/COLOR]?[/COLOR]" % ( iIiIi11 , oOOo0O00o , name ) , yeslabel = "[B][COLOR green]Install[/COLOR][/B]" , nolabel = "[B][COLOR red]Cancel[/COLOR][/B]" )
  if 71 - 71: o0o0Oo0oooo0 + iIii1I11I1II1 * IIIi1i1I . OO00O0O0O00Oo % i11iIiiIii % iIii1I11I1II1
  if Ii1I1 == 1 :
   file = wiz . openURL ( url )
   OooOO0oOOo0O = open ( I11II1i , 'w' ) ;
   OooOO0oOOo0O . write ( file )
   OooOO0oOOo0O . close ( )
   iiIIIII1i1iI . ok ( o0OOO , '[COLOR %s]AdvancedSettings.xml file has been successfully written.  Once you click okay it will force close kodi.[/COLOR]' % iIiIi11 )
   wiz . killxbmc ( True )
  else : wiz . log ( "[Advanced Settings] install canceled" ) ; wiz . LogNotify ( '[COLOR %s]%s[/COLOR]' % ( oOOo0O00o , o0OOO ) , "[COLOR %s]Write Cancelled![/COLOR]" % iIiIi11 ) ; return
 else : wiz . log ( "[Advanced Settings] URL not working: %s" % Ooo000000 ) ; wiz . LogNotify ( '[COLOR %s]%s[/COLOR]' % ( oOOo0O00o , o0OOO ) , "[COLOR %s]URL Not Working[/COLOR]" % iIiIi11 )
 if 42 - 42: iiIIi1IiIi11 / I1I1i1 + Ooo0O . Ooo0O % iii11iiII
def Ii1III1 ( ) :
 OooOO0oOOo0O = open ( I11II1i )
 ooIii1ii1II1iI1 = OooOO0oOOo0O . read ( ) . replace ( '\t' , '    ' )
 wiz . TextBox ( o0OOO , ooIii1ii1II1iI1 )
 OooOO0oOOo0O . close ( )
 if 67 - 67: I1111 / oO0 % i11IiIiiIIIII / OO00O0O0O00Oo
def i11IiI1I ( ) :
 if os . path . exists ( I11II1i ) :
  wiz . removeFile ( I11II1i )
 else : LogNotify ( "[COLOR %s]%s[/COLOR]" % ( oOOo0O00o , o0OOO ) , "[COLOR %s]AdvancedSettings.xml not found[/COLOR]" )
 if 70 - 70: I1111 % ooOo / ooOo . i11IiIiiIIIII % OOoooooO . II111iiii
def I1ii1Ii1 ( ) :
 notify . autoConfig ( )
 if 73 - 73: O0 . IIIi1i1I + i11iIiiIii + iIii1I11I1II1 - i11IiIiiIIIII / o0o0Oo0oooo0
def OO0OOOOo0000O ( ) :
 i1Ii11ii = 'http://whatismyipaddress.com/'
 if not wiz . workingURL ( i1Ii11ii ) : return 'Unknown' , 'Unknown' , 'Unknown'
 oOOOOOo = wiz . openURL ( i1Ii11ii ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 if not 'Access Denied' in oOOOOOo :
  i1I11ii = re . compile ( 'whatismyipaddress.com/ip/(.+?)"' ) . findall ( oOOOOOo )
  o0ooO00O0O = i1I11ii [ 0 ] if ( len ( i1I11ii ) > 0 ) else 'Unknown'
  iiiI1iI1 = re . compile ( '"font-size:14px;">(.+?)</td>' ) . findall ( oOOOOOo )
  I1oOoO0OOO00O = iiiI1iI1 [ 0 ] if ( len ( iiiI1iI1 ) > 0 ) else 'Unknown'
  OOOOO0o0OOo = iiiI1iI1 [ 1 ] + ', ' + iiiI1iI1 [ 2 ] + ', ' + iiiI1iI1 [ 3 ] if ( len ( iiiI1iI1 ) > 2 ) else 'Unknown'
  return o0ooO00O0O , I1oOoO0OOO00O , OOOOO0o0OOo
 else : return 'Unknown' , 'Unknown' , 'Unknown'
 if 40 - 40: i1Ii * IIIi1i1I % i11IiIiiIIIII * oO0
def OoOoOOoO ( ) :
 ii1ii1i11I1I = [ 'System.FriendlyName' ,
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
 iiII1iiiiiii = [ ] ; ooOO00oOOo000 = 0
 for iiIiii in ii1ii1i11I1I :
  iiI1ii = wiz . getInfo ( iiIiii )
  O0OooOO = 0
  while iiI1ii == "Busy" and O0OooOO < 10 :
   iiI1ii = wiz . getInfo ( iiIiii ) ; O0OooOO += 1 ; wiz . log ( "%s sleep %s" % ( iiIiii , str ( O0OooOO ) ) ) ; xbmc . sleep ( 200 )
  iiII1iiiiiii . append ( iiI1ii )
  ooOO00oOOo000 += 1
 i1i1 = iiII1iiiiiii [ 8 ] if 'Una' in iiII1iiiiiii [ 8 ] else wiz . convertSize ( int ( float ( iiII1iiiiiii [ 8 ] [ : - 8 ] ) ) * 1024 * 1024 )
 o0oOoOo0 = iiII1iiiiiii [ 9 ] if 'Una' in iiII1iiiiiii [ 9 ] else wiz . convertSize ( int ( float ( iiII1iiiiiii [ 9 ] [ : - 8 ] ) ) * 1024 * 1024 )
 III1IiI1i1i = iiII1iiiiiii [ 10 ] if 'Una' in iiII1iiiiiii [ 10 ] else wiz . convertSize ( int ( float ( iiII1iiiiiii [ 10 ] [ : - 8 ] ) ) * 1024 * 1024 )
 o0OOOOOo0 = wiz . convertSize ( int ( float ( iiII1iiiiiii [ 11 ] [ : - 2 ] ) ) * 1024 * 1024 )
 oooOoO = wiz . convertSize ( int ( float ( iiII1iiiiiii [ 12 ] [ : - 2 ] ) ) * 1024 * 1024 )
 O0Oo0 = wiz . convertSize ( int ( float ( iiII1iiiiiii [ 13 ] [ : - 2 ] ) ) * 1024 * 1024 )
 iIIIi1IiI11I1 , I1oOoO0OOO00O , OOOOO0o0OOo = OO0OOOOo0000O ( )
 if 71 - 71: IiiIII111ii - O0 - iiIIi1IiIi11 . iii11iiII % Ooo0O
 Oo00oO = [ ] ; ooo0 = [ ] ; ii1iIIi11 = [ ] ; iI1IIIII1Ii = [ ] ; iIiI1 = [ ] ; I1IiII1I1i1I1 = [ ] ; II11iiI = [ ]
 if 45 - 45: OoooooooOO
 I1oo = glob . glob ( os . path . join ( O0O , '*/' ) )
 for iiI1IIIii in sorted ( I1oo , key = lambda ooOO00oOOo000 : ooOO00oOOo000 ) :
  iIOO0OOoooo0o = os . path . split ( iiI1IIIii [ : - 1 ] ) [ 1 ]
  if iIOO0OOoooo0o == 'packages' : continue
  IiIi1Ii = os . path . join ( iiI1IIIii , 'addon.xml' )
  if os . path . exists ( IiIi1Ii ) :
   OooOO0oOOo0O = open ( IiIi1Ii )
   ooIii1ii1II1iI1 = OooOO0oOOo0O . read ( )
   iiIIiI11II1 = re . compile ( "<provides>(.+?)</provides>" ) . findall ( ooIii1ii1II1iI1 )
   if len ( iiIIiI11II1 ) == 0 :
    if iIOO0OOoooo0o . startswith ( 'skin' ) : II11iiI . append ( iIOO0OOoooo0o )
    if iIOO0OOoooo0o . startswith ( 'repo' ) : iIiI1 . append ( iIOO0OOoooo0o )
    else : I1IiII1I1i1I1 . append ( iIOO0OOoooo0o )
   elif not ( iiIIiI11II1 [ 0 ] ) . find ( 'executable' ) == - 1 : iI1IIIII1Ii . append ( iIOO0OOoooo0o )
   elif not ( iiIIiI11II1 [ 0 ] ) . find ( 'video' ) == - 1 : ii1iIIi11 . append ( iIOO0OOoooo0o )
   elif not ( iiIIiI11II1 [ 0 ] ) . find ( 'audio' ) == - 1 : ooo0 . append ( iIOO0OOoooo0o )
   elif not ( iiIIiI11II1 [ 0 ] ) . find ( 'image' ) == - 1 : Oo00oO . append ( iIOO0OOoooo0o )
   if 79 - 79: OoooooooOO / oO0 . O0
 iiiii1II ( '[B]Media Center Info:[/B]' , '' , icon = IiIi11iI , themeit = oooOo0OOOoo0 )
 iiiii1II ( '[COLOR %s]Name:[/COLOR] [COLOR %s]%s[/COLOR]' % ( oOOo0O00o , iIiIi11 , iiII1iiiiiii [ 0 ] ) , '' , icon = IiIi11iI , themeit = OOoO )
 iiiii1II ( '[COLOR %s]Version:[/COLOR] [COLOR %s]%s[/COLOR]' % ( oOOo0O00o , iIiIi11 , iiII1iiiiiii [ 1 ] ) , '' , icon = IiIi11iI , themeit = OOoO )
 iiiii1II ( '[COLOR %s]Platform:[/COLOR] [COLOR %s]%s[/COLOR]' % ( oOOo0O00o , iIiIi11 , wiz . platform ( ) . title ( ) ) , '' , icon = IiIi11iI , themeit = OOoO )
 iiiii1II ( '[COLOR %s]CPU Usage:[/COLOR] [COLOR %s]%s[/COLOR]' % ( oOOo0O00o , iIiIi11 , iiII1iiiiiii [ 2 ] ) , '' , icon = IiIi11iI , themeit = OOoO )
 iiiii1II ( '[COLOR %s]Screen Mode:[/COLOR] [COLOR %s]%s[/COLOR]' % ( oOOo0O00o , iIiIi11 , iiII1iiiiiii [ 3 ] ) , '' , icon = IiIi11iI , themeit = OOoO )
 if 79 - 79: IIIi1i1I - II111iiii
 iiiii1II ( '[B]Uptime:[/B]' , '' , icon = IiIi11iI , themeit = oooOo0OOOoo0 )
 iiiii1II ( '[COLOR %s]Current Uptime:[/COLOR] [COLOR %s]%s[/COLOR]' % ( oOOo0O00o , iIiIi11 , iiII1iiiiiii [ 6 ] ) , '' , icon = IiIi11iI , themeit = oooOo0OOOoo0 )
 iiiii1II ( '[COLOR %s]Total Uptime:[/COLOR] [COLOR %s]%s[/COLOR]' % ( oOOo0O00o , iIiIi11 , iiII1iiiiiii [ 7 ] ) , '' , icon = IiIi11iI , themeit = oooOo0OOOoo0 )
 if 43 - 43: i1IIi + O0 % I1111 / IiiIII111ii * ooOo
 iiiii1II ( '[B]Local Storage:[/B]' , '' , icon = IiIi11iI , themeit = oooOo0OOOoo0 )
 iiiii1II ( '[COLOR %s]Used Storage:[/COLOR] [COLOR %s]%s[/COLOR]' % ( oOOo0O00o , iIiIi11 , i1i1 ) , '' , icon = IiIi11iI , themeit = oooOo0OOOoo0 )
 iiiii1II ( '[COLOR %s]Free Storage:[/COLOR] [COLOR %s]%s[/COLOR]' % ( oOOo0O00o , iIiIi11 , o0oOoOo0 ) , '' , icon = IiIi11iI , themeit = oooOo0OOOoo0 )
 iiiii1II ( '[COLOR %s]Total Storage:[/COLOR] [COLOR %s]%s[/COLOR]' % ( oOOo0O00o , iIiIi11 , III1IiI1i1i ) , '' , icon = IiIi11iI , themeit = oooOo0OOOoo0 )
 if 89 - 89: ooOo . Ooo0O + oO0 . O0 % I1I1i1
 iiiii1II ( '[B]Ram Usage:[/B]' , '' , icon = IiIi11iI , themeit = oooOo0OOOoo0 )
 iiiii1II ( '[COLOR %s]Used Memory:[/COLOR] [COLOR %s]%s[/COLOR]' % ( oOOo0O00o , iIiIi11 , o0OOOOOo0 ) , '' , icon = IiIi11iI , themeit = oooOo0OOOoo0 )
 iiiii1II ( '[COLOR %s]Free Memory:[/COLOR] [COLOR %s]%s[/COLOR]' % ( oOOo0O00o , iIiIi11 , oooOoO ) , '' , icon = IiIi11iI , themeit = oooOo0OOOoo0 )
 iiiii1II ( '[COLOR %s]Total Memory:[/COLOR] [COLOR %s]%s[/COLOR]' % ( oOOo0O00o , iIiIi11 , O0Oo0 ) , '' , icon = IiIi11iI , themeit = oooOo0OOOoo0 )
 if 84 - 84: OoooooooOO + OO00O0O0O00Oo / ooOo % iii11iiII % oO0 * ooOo
 iiiii1II ( '[B]Network:[/B]' , '' , icon = IiIi11iI , themeit = oooOo0OOOoo0 )
 iiiii1II ( '[COLOR %s]Local IP:[/COLOR] [COLOR %s]%s[/COLOR]' % ( oOOo0O00o , iIiIi11 , iiII1iiiiiii [ 4 ] ) , '' , icon = IiIi11iI , themeit = oooOo0OOOoo0 )
 iiiii1II ( '[COLOR %s]External IP:[/COLOR] [COLOR %s]%s[/COLOR]' % ( oOOo0O00o , iIiIi11 , iIIIi1IiI11I1 ) , '' , icon = IiIi11iI , themeit = oooOo0OOOoo0 )
 iiiii1II ( '[COLOR %s]Provider:[/COLOR] [COLOR %s]%s[/COLOR]' % ( oOOo0O00o , iIiIi11 , I1oOoO0OOO00O ) , '' , icon = IiIi11iI , themeit = oooOo0OOOoo0 )
 iiiii1II ( '[COLOR %s]Location:[/COLOR] [COLOR %s]%s[/COLOR]' % ( oOOo0O00o , iIiIi11 , OOOOO0o0OOo ) , '' , icon = IiIi11iI , themeit = oooOo0OOOoo0 )
 iiiii1II ( '[COLOR %s]MacAddress:[/COLOR] [COLOR %s]%s[/COLOR]' % ( oOOo0O00o , iIiIi11 , iiII1iiiiiii [ 5 ] ) , '' , icon = IiIi11iI , themeit = oooOo0OOOoo0 )
 if 58 - 58: I1111 - o0o0Oo0oooo0 . i11iIiiIii % i11iIiiIii / i1IIi / IIIi1i1I
 Ii1ii1IiiiiiI = len ( Oo00oO ) + len ( ooo0 ) + len ( ii1iIIi11 ) + len ( iI1IIIII1Ii ) + len ( I1IiII1I1i1I1 ) + len ( II11iiI ) + len ( iIiI1 )
 iiiii1II ( '[B]Addons([COLOR %s]%s[/COLOR]):[/B]' % ( oOOo0O00o , Ii1ii1IiiiiiI ) , '' , icon = IiIi11iI , themeit = oooOo0OOOoo0 )
 iiiii1II ( '[COLOR %s]Video Addons:[/COLOR] [COLOR %s]%s[/COLOR]' % ( oOOo0O00o , iIiIi11 , str ( len ( ii1iIIi11 ) ) ) , '' , icon = IiIi11iI , themeit = oooOo0OOOoo0 )
 iiiii1II ( '[COLOR %s]Program Addons:[/COLOR] [COLOR %s]%s[/COLOR]' % ( oOOo0O00o , iIiIi11 , str ( len ( iI1IIIII1Ii ) ) ) , '' , icon = IiIi11iI , themeit = oooOo0OOOoo0 )
 iiiii1II ( '[COLOR %s]Music Addons:[/COLOR] [COLOR %s]%s[/COLOR]' % ( oOOo0O00o , iIiIi11 , str ( len ( ooo0 ) ) ) , '' , icon = IiIi11iI , themeit = oooOo0OOOoo0 )
 iiiii1II ( '[COLOR %s]Picture Addons:[/COLOR] [COLOR %s]%s[/COLOR]' % ( oOOo0O00o , iIiIi11 , str ( len ( Oo00oO ) ) ) , '' , icon = IiIi11iI , themeit = oooOo0OOOoo0 )
 iiiii1II ( '[COLOR %s]Repositories:[/COLOR] [COLOR %s]%s[/COLOR]' % ( oOOo0O00o , iIiIi11 , str ( len ( iIiI1 ) ) ) , '' , icon = IiIi11iI , themeit = oooOo0OOOoo0 )
 iiiii1II ( '[COLOR %s]Skins:[/COLOR] [COLOR %s]%s[/COLOR]' % ( oOOo0O00o , iIiIi11 , str ( len ( II11iiI ) ) ) , '' , icon = IiIi11iI , themeit = oooOo0OOOoo0 )
 iiiii1II ( '[COLOR %s]Scripts/Modules:[/COLOR] [COLOR %s]%s[/COLOR]' % ( oOOo0O00o , iIiIi11 , str ( len ( I1IiII1I1i1I1 ) ) ) , '' , icon = IiIi11iI , themeit = oooOo0OOOoo0 )
 if 77 - 77: i11iIiiIii
def i1IIii11i1I1 ( ) :
 II11Ii111II1 = '[COLOR green]ON[/COLOR]' ; O00OOO00Ooo = '[COLOR red]OFF[/COLOR]'
 Ii1I1O0oo00oOOO0o = 'true' if o0O0OOO0Ooo == 'true' else 'false'
 II1iI111iiIIiI1I = 'true' if iiIiII1 == 'true' else 'false'
 ooO00Oo = 'true' if OOO00O0O == 'true' else 'false'
 Iiii1Ii1I = 'true' if ooOOoooooo == 'true' else 'false'
 oooOOOOO = 'true' if O0i1II1Iiii1I11 == 'true' else 'false'
 i1iIii = 'true' if II1I == 'true' else 'false'
 o0O0ooooooo00 = 'true' if IiIIIi1iIi == 'true' else 'false'
 iIiI1 = 'true' if IIII == 'true' else 'false'
 super = 'true' if iiIiI == 'true' else 'false'
 I1111ii11IIII = 'true' if o00oooO0Oo == 'true' else 'false'
 if 48 - 48: iIii1I11I1II1 % i1IIi + o0o0Oo0oooo0 % I1I1i1
 oo00O00oO000o ( 'Keep Trakt Data' , 'trakt' , icon = iIIii , themeit = OOOiiiiI )
 oo00O00oO000o ( 'Keep Real Debrid' , 'realdebrid' , icon = o00O0O , themeit = OOOiiiiI )
 oo00O00oO000o ( 'Keep Login Info' , 'login' , icon = ii1iii1i , themeit = OOOiiiiI )
 iiiii1II ( 'Import Save Data' , 'managedata' , 'import' , icon = I1111i , themeit = OOOiiiiI )
 iiiii1II ( 'Export Save Data' , 'managedata' , 'export' , icon = I1111i , themeit = OOOiiiiI )
 iiiii1II ( '- Click to toggle settings -' , '' , themeit = OOoO )
 iiiii1II ( 'Save Trakt: %s' % Ii1I1O0oo00oOOO0o . replace ( 'true' , II11Ii111II1 ) . replace ( 'false' , O00OOO00Ooo ) , 'togglesetting' , 'keeptrakt' , icon = iIIii , themeit = OOOiiiiI )
 iiiii1II ( 'Save Real Debrid: %s' % II1iI111iiIIiI1I . replace ( 'true' , II11Ii111II1 ) . replace ( 'false' , O00OOO00Ooo ) , 'togglesetting' , 'keepdebrid' , icon = o00O0O , themeit = OOOiiiiI )
 iiiii1II ( 'Save Login Info: %s' % ooO00Oo . replace ( 'true' , II11Ii111II1 ) . replace ( 'false' , O00OOO00Ooo ) , 'togglesetting' , 'keeplogin' , icon = ii1iii1i , themeit = OOOiiiiI )
 iiiii1II ( 'Keep \'Sources.xml\': %s' % Iiii1Ii1I . replace ( 'true' , II11Ii111II1 ) . replace ( 'false' , O00OOO00Ooo ) , 'togglesetting' , 'keepsources' , icon = I1111i , themeit = OOOiiiiI )
 iiiii1II ( 'Keep \'Profiles.xml\': %s' % i1iIii . replace ( 'true' , II11Ii111II1 ) . replace ( 'false' , O00OOO00Ooo ) , 'togglesetting' , 'keepprofiles' , icon = I1111i , themeit = OOOiiiiI )
 iiiii1II ( 'Keep \'Advancedsettings.xml\': %s' % oooOOOOO . replace ( 'true' , II11Ii111II1 ) . replace ( 'false' , O00OOO00Ooo ) , 'togglesetting' , 'keepadvanced' , icon = I1111i , themeit = OOOiiiiI )
 iiiii1II ( 'Keep \'Favourites.xml\': %s' % o0O0ooooooo00 . replace ( 'true' , II11Ii111II1 ) . replace ( 'false' , O00OOO00Ooo ) , 'togglesetting' , 'keepfavourites' , icon = I1111i , themeit = OOOiiiiI )
 iiiii1II ( 'Keep Super Favourites: %s' % super . replace ( 'true' , II11Ii111II1 ) . replace ( 'false' , O00OOO00Ooo ) , 'togglesetting' , 'keepsuper' , icon = I1111i , themeit = OOOiiiiI )
 iiiii1II ( 'Keep Installed Repo\'s: %s' % iIiI1 . replace ( 'true' , II11Ii111II1 ) . replace ( 'false' , O00OOO00Ooo ) , 'togglesetting' , 'keeprepos' , icon = I1111i , themeit = OOOiiiiI )
 iiiii1II ( 'Keep My \'WhiteList\': %s' % I1111ii11IIII . replace ( 'true' , II11Ii111II1 ) . replace ( 'false' , O00OOO00Ooo ) , 'togglesetting' , 'keepwhitelist' , icon = I1111i , themeit = OOOiiiiI )
 if I1111ii11IIII == 'true' :
  iiiii1II ( 'Edit My Whitelist' , 'whitelist' , 'edit' , icon = I1111i , themeit = OOOiiiiI )
  iiiii1II ( 'View My Whitelist' , 'whitelist' , 'view' , icon = I1111i , themeit = OOOiiiiI )
  iiiii1II ( 'Clear My Whitelist' , 'whitelist' , 'clear' , icon = I1111i , themeit = OOOiiiiI )
  iiiii1II ( 'Import My Whitelist' , 'whitelist' , 'import' , icon = I1111i , themeit = OOOiiiiI )
  iiiii1II ( 'Export My Whitelist' , 'whitelist' , 'export' , icon = I1111i , themeit = OOOiiiiI )
 iIi1 ( 'files' , 'viewType' )
 if 79 - 79: o0o0Oo0oooo0 % ooOo % IiiIII111ii / i1IIi % I1111
def oo0o00OO ( ) :
 Ii1I1O0oo00oOOO0o = '[COLOR green]ON[/COLOR]' if o0O0OOO0Ooo == 'true' else '[COLOR red]OFF[/COLOR]'
 oOoo00o0oOO = str ( O000OOo00oo ) if not O000OOo00oo == '' else 'Trakt hasnt been saved yet.'
 iiiii1II ( '[I]Register FREE Account at http://trakt.tv[/I]' , '' , icon = iIIii , themeit = OOoO )
 iiiii1II ( 'Save Trakt Data: %s' % Ii1I1O0oo00oOOO0o , 'togglesetting' , 'keeptrakt' , icon = iIIii , themeit = OOoO )
 if o0O0OOO0Ooo == 'true' : iiiii1II ( 'Last Save: %s' % str ( oOoo00o0oOO ) , '' , icon = iIIii , themeit = OOoO )
 if O0O0ooOOO == 'No' : iiiii1II ( wiz . sep ( ) , '' , icon = iIIii , themeit = OOoO )
 if 61 - 61: i1IIi * I1I1i1 + iIii1I11I1II1 / o0o0Oo0oooo0 - O0 * iIii1I11I1II1
 for Ii1I1O0oo00oOOO0o in traktit . ORDER :
  oO0o00oOOooO0 = oOOOoo00 [ Ii1I1O0oo00oOOO0o ] [ 'name' ]
  oOoo0ooOoo = oOOOoo00 [ Ii1I1O0oo00oOOO0o ] [ 'path' ]
  oOooOOo00ooO = oOOOoo00 [ Ii1I1O0oo00oOOO0o ] [ 'saved' ]
  file = oOOOoo00 [ Ii1I1O0oo00oOOO0o ] [ 'file' ]
  o0OO0oooo = wiz . getS ( oOooOOo00ooO )
  I11II1i1 = traktit . traktUser ( Ii1I1O0oo00oOOO0o )
  i1i1i1I = oOOOoo00 [ Ii1I1O0oo00oOOO0o ] [ 'icon' ] if os . path . exists ( oOoo0ooOoo ) else iIIii
  oOoo000 = oOOOoo00 [ Ii1I1O0oo00oOOO0o ] [ 'fanart' ] if os . path . exists ( oOoo0ooOoo ) else OOO00
  iI1IIIii = I1i11ii11 ( 'saveaddon' , 'Trakt' , Ii1I1O0oo00oOOO0o )
  IiI1ii11I1 = I1i11ii11 ( 'save' , 'Trakt' , Ii1I1O0oo00oOOO0o )
  iI1IIIii . append ( ( oooOo0OOOoo0 % '%s Settings' % oO0o00oOOooO0 , 'RunPlugin(plugin://%s/?mode=opensettings&name=%s&url=trakt)' % ( IiII1IiiIiI1 , Ii1I1O0oo00oOOO0o ) ) )
  if 19 - 19: OO00O0O0O00Oo + i1Ii / IIIi1i1I / II111iiii
  iiiii1II ( '[+]-> %s' % oO0o00oOOooO0 , '' , icon = i1i1i1I , fanart = oOoo000 , themeit = OOoO )
  if not os . path . exists ( oOoo0ooOoo ) : iiiii1II ( '[COLOR red]Addon Data: Not Installed[/COLOR]' , '' , icon = i1i1i1I , fanart = oOoo000 , menu = iI1IIIii )
  elif not I11II1i1 : iiiii1II ( '[COLOR red]Addon Data: Not Registered[/COLOR]' , 'authtrakt' , Ii1I1O0oo00oOOO0o , icon = i1i1i1I , fanart = oOoo000 , menu = iI1IIIii )
  else : iiiii1II ( '[COLOR green]Addon Data: %s[/COLOR]' % I11II1i1 , 'authtrakt' , Ii1I1O0oo00oOOO0o , icon = i1i1i1I , fanart = oOoo000 , menu = iI1IIIii )
  if o0OO0oooo == "" :
   if os . path . exists ( file ) : iiiii1II ( '[COLOR red]Saved Data: Save File Found(Import Data)[/COLOR]' , 'importtrakt' , Ii1I1O0oo00oOOO0o , icon = i1i1i1I , fanart = oOoo000 , menu = IiI1ii11I1 )
   else : iiiii1II ( '[COLOR red]Saved Data: Not Saved[/COLOR]' , 'savetrakt' , Ii1I1O0oo00oOOO0o , icon = i1i1i1I , fanart = oOoo000 , menu = IiI1ii11I1 )
  else : iiiii1II ( '[COLOR green]Saved Data: %s[/COLOR]' % o0OO0oooo , '' , icon = i1i1i1I , fanart = oOoo000 , menu = IiI1ii11I1 )
  if 92 - 92: i1IIi % OOoooooO + OOoooooO - iIii1I11I1II1 . IiiIII111ii
 if O0O0ooOOO == 'No' : iiiii1II ( wiz . sep ( ) , '' , themeit = OOoO )
 iiiii1II ( 'Save All Trakt Data' , 'savetrakt' , 'all' , icon = iIIii , themeit = OOoO )
 iiiii1II ( 'Recover All Saved Trakt Data' , 'restoretrakt' , 'all' , icon = iIIii , themeit = OOoO )
 iiiii1II ( 'Import Trakt Data' , 'importtrakt' , 'all' , icon = iIIii , themeit = OOoO )
 iiiii1II ( 'Clear All Saved Trakt Data' , 'cleartrakt' , 'all' , icon = iIIii , themeit = OOoO )
 iiiii1II ( 'Clear All Addon Data' , 'addontrakt' , 'all' , icon = iIIii , themeit = OOoO )
 iIi1 ( 'files' , 'viewType' )
 if 33 - 33: I1I1i1 / O0 + iii11iiII
def o0Ooo0o0Oo ( ) :
 II1iI111iiIIiI1I = '[COLOR green]ON[/COLOR]' if iiIiII1 == 'true' else '[COLOR red]OFF[/COLOR]'
 oOoo00o0oOO = str ( oo0OOo ) if not oo0OOo == '' else 'Real Debrid hasnt been saved yet.'
 iiiii1II ( '[I]http://real-debrid.com is a PAID service.[/I]' , '' , icon = o00O0O , themeit = OOoO )
 iiiii1II ( 'Save Real Debrid Data: %s' % II1iI111iiIIiI1I , 'togglesetting' , 'keepdebrid' , icon = o00O0O , themeit = OOoO )
 if iiIiII1 == 'true' : iiiii1II ( 'Last Save: %s' % str ( oOoo00o0oOO ) , '' , icon = o00O0O , themeit = OOoO )
 if O0O0ooOOO == 'No' : iiiii1II ( wiz . sep ( ) , '' , icon = o00O0O , themeit = OOoO )
 if 55 - 55: iIii1I11I1II1 * iiIIi1IiIi11
 for ooIi11iI in debridit . ORDER :
  oO0o00oOOooO0 = iiIiIIIiiI [ ooIi11iI ] [ 'name' ]
  oOoo0ooOoo = iiIiIIIiiI [ ooIi11iI ] [ 'path' ]
  oOooOOo00ooO = iiIiIIIiiI [ ooIi11iI ] [ 'saved' ]
  file = iiIiIIIiiI [ ooIi11iI ] [ 'file' ]
  o0OO0oooo = wiz . getS ( oOooOOo00ooO )
  I11II1i1 = debridit . debridUser ( ooIi11iI )
  i1i1i1I = iiIiIIIiiI [ ooIi11iI ] [ 'icon' ] if os . path . exists ( oOoo0ooOoo ) else o00O0O
  oOoo000 = iiIiIIIiiI [ ooIi11iI ] [ 'fanart' ] if os . path . exists ( oOoo0ooOoo ) else OOO00
  iI1IIIii = I1i11ii11 ( 'saveaddon' , 'Debrid' , ooIi11iI )
  IiI1ii11I1 = I1i11ii11 ( 'save' , 'Debrid' , ooIi11iI )
  iI1IIIii . append ( ( oooOo0OOOoo0 % '%s Settings' % oO0o00oOOooO0 , 'RunPlugin(plugin://%s/?mode=opensettings&name=%s&url=debrid)' % ( IiII1IiiIiI1 , ooIi11iI ) ) )
  if 22 - 22: iii11iiII
  iiiii1II ( '[+]-> %s' % oO0o00oOOooO0 , '' , icon = i1i1i1I , fanart = oOoo000 , themeit = OOoO )
  if not os . path . exists ( oOoo0ooOoo ) : iiiii1II ( '[COLOR red]Addon Data: Not Installed[/COLOR]' , '' , icon = i1i1i1I , fanart = oOoo000 , menu = iI1IIIii )
  elif not I11II1i1 : iiiii1II ( '[COLOR red]Addon Data: Not Registered[/COLOR]' , 'authdebrid' , ooIi11iI , icon = i1i1i1I , fanart = oOoo000 , menu = iI1IIIii )
  else : iiiii1II ( '[COLOR green]Addon Data: %s[/COLOR]' % I11II1i1 , 'authdebrid' , ooIi11iI , icon = i1i1i1I , fanart = oOoo000 , menu = iI1IIIii )
  if o0OO0oooo == "" :
   if os . path . exists ( file ) : iiiii1II ( '[COLOR red]Saved Data: Save File Found(Import Data)[/COLOR]' , 'importdebrid' , ooIi11iI , icon = i1i1i1I , fanart = oOoo000 , menu = IiI1ii11I1 )
   else : iiiii1II ( '[COLOR red]Saved Data: Not Saved[/COLOR]' , 'savedebrid' , ooIi11iI , icon = i1i1i1I , fanart = oOoo000 , menu = IiI1ii11I1 )
  else : iiiii1II ( '[COLOR green]Saved Data: %s[/COLOR]' % o0OO0oooo , '' , icon = i1i1i1I , fanart = oOoo000 , menu = IiI1ii11I1 )
  if 22 - 22: iiIIi1IiIi11 * i11IiIiiIIIII - Ooo0O * O0 / i11iIiiIii
 if O0O0ooOOO == 'No' : iiiii1II ( wiz . sep ( ) , '' , themeit = OOoO )
 iiiii1II ( 'Save All Real Debrid Data' , 'savedebrid' , 'all' , icon = o00O0O , themeit = OOoO )
 iiiii1II ( 'Recover All Saved Real Debrid Data' , 'restoredebrid' , 'all' , icon = o00O0O , themeit = OOoO )
 iiiii1II ( 'Import Real Debrid Data' , 'importdebrid' , 'all' , icon = o00O0O , themeit = OOoO )
 iiiii1II ( 'Clear All Saved Real Debrid Data' , 'cleardebrid' , 'all' , icon = o00O0O , themeit = OOoO )
 iiiii1II ( 'Clear All Addon Data' , 'addondebrid' , 'all' , icon = o00O0O , themeit = OOoO )
 iIi1 ( 'files' , 'viewType' )
 if 78 - 78: Ooo0O * O0 / OOoooooO + OoooooooOO + iii11iiII
def I1iiIiiIiiI ( ) :
 ooO00Oo = '[COLOR green]ON[/COLOR]' if OOO00O0O == 'true' else '[COLOR red]OFF[/COLOR]'
 oOoo00o0oOO = str ( ooOOO00Ooo ) if not ooOOO00Ooo == '' else 'Login data hasnt been saved yet.'
 iiiii1II ( '[I]Several of these addons are PAID services.[/I]' , '' , icon = ii1iii1i , themeit = OOoO )
 iiiii1II ( 'Save Login Data: %s' % ooO00Oo , 'togglesetting' , 'keeplogin' , icon = ii1iii1i , themeit = OOoO )
 if OOO00O0O == 'true' : iiiii1II ( 'Last Save: %s' % str ( oOoo00o0oOO ) , '' , icon = ii1iii1i , themeit = OOoO )
 if O0O0ooOOO == 'No' : iiiii1II ( wiz . sep ( ) , '' , icon = ii1iii1i , themeit = OOoO )
 if 94 - 94: i1IIi
 for ooO00Oo in loginit . ORDER :
  oO0o00oOOooO0 = iiI1IIIi [ ooO00Oo ] [ 'name' ]
  oOoo0ooOoo = iiI1IIIi [ ooO00Oo ] [ 'path' ]
  oOooOOo00ooO = iiI1IIIi [ ooO00Oo ] [ 'saved' ]
  file = iiI1IIIi [ ooO00Oo ] [ 'file' ]
  o0OO0oooo = wiz . getS ( oOooOOo00ooO )
  I11II1i1 = loginit . loginUser ( ooO00Oo )
  i1i1i1I = iiI1IIIi [ ooO00Oo ] [ 'icon' ] if os . path . exists ( oOoo0ooOoo ) else ii1iii1i
  oOoo000 = iiI1IIIi [ ooO00Oo ] [ 'fanart' ] if os . path . exists ( oOoo0ooOoo ) else OOO00
  iI1IIIii = I1i11ii11 ( 'saveaddon' , 'Login' , ooO00Oo )
  IiI1ii11I1 = I1i11ii11 ( 'save' , 'Login' , ooO00Oo )
  iI1IIIii . append ( ( oooOo0OOOoo0 % '%s Settings' % oO0o00oOOooO0 , 'RunPlugin(plugin://%s/?mode=opensettings&name=%s&url=login)' % ( IiII1IiiIiI1 , ooO00Oo ) ) )
  if 36 - 36: ooOo + Ooo0O
  iiiii1II ( '[+]-> %s' % oO0o00oOOooO0 , '' , icon = i1i1i1I , fanart = oOoo000 , themeit = OOoO )
  if not os . path . exists ( oOoo0ooOoo ) : iiiii1II ( '[COLOR red]Addon Data: Not Installed[/COLOR]' , '' , icon = i1i1i1I , fanart = oOoo000 , menu = iI1IIIii )
  elif not I11II1i1 : iiiii1II ( '[COLOR red]Addon Data: Not Registered[/COLOR]' , 'authlogin' , ooO00Oo , icon = i1i1i1I , fanart = oOoo000 , menu = iI1IIIii )
  else : iiiii1II ( '[COLOR green]Addon Data: %s[/COLOR]' % I11II1i1 , 'authlogin' , ooO00Oo , icon = i1i1i1I , fanart = oOoo000 , menu = iI1IIIii )
  if o0OO0oooo == "" :
   if os . path . exists ( file ) : iiiii1II ( '[COLOR red]Saved Data: Save File Found(Import Data)[/COLOR]' , 'importlogin' , ooO00Oo , icon = i1i1i1I , fanart = oOoo000 , menu = IiI1ii11I1 )
   else : iiiii1II ( '[COLOR red]Saved Data: Not Saved[/COLOR]' , 'savelogin' , ooO00Oo , icon = i1i1i1I , fanart = oOoo000 , menu = IiI1ii11I1 )
  else : iiiii1II ( '[COLOR green]Saved Data: %s[/COLOR]' % o0OO0oooo , '' , icon = i1i1i1I , fanart = oOoo000 , menu = IiI1ii11I1 )
  if 46 - 46: iiIIi1IiIi11
 if O0O0ooOOO == 'No' : iiiii1II ( wiz . sep ( ) , '' , themeit = OOoO )
 iiiii1II ( 'Save All Login Data' , 'savelogin' , 'all' , icon = ii1iii1i , themeit = OOoO )
 iiiii1II ( 'Recover All Saved Login Data' , 'restorelogin' , 'all' , icon = ii1iii1i , themeit = OOoO )
 iiiii1II ( 'Import Login Data' , 'importlogin' , 'all' , icon = ii1iii1i , themeit = OOoO )
 iiiii1II ( 'Clear All Saved Login Data' , 'clearlogin' , 'all' , icon = ii1iii1i , themeit = OOoO )
 iiiii1II ( 'Clear All Addon Data' , 'addonlogin' , 'all' , icon = ii1iii1i , themeit = OOoO )
 iIi1 ( 'files' , 'viewType' )
 if 65 - 65: i1IIi . oO0 / OOoooooO
def I1i1I11111iI1 ( ) :
 if o0OIiII < 17 :
  IIIIIIi = os . path . join ( OOOO , wiz . latestDB ( 'Addons' ) )
  try :
   os . remove ( IIIIIIi )
  except Exception , ii1i1i :
   wiz . log ( "Unable to remove %s, Purging DB" % IIIIIIi )
   wiz . purgeDb ( IIIIIIi )
 else :
  xbmc . log ( "Requested Addons.db be removed but doesnt work in Kod17" )
  if 59 - 59: IIIi1i1I / ooOo * IiiIII111ii % O0 - II111iiii + OoooooooOO
def iI11iiI1I1Iii ( ) :
 I1oo = glob . glob ( os . path . join ( O0O , '*/' ) )
 oO0OIIIiIi1iiI = [ ] ; iI1o0 = [ ]
 for iiI1IIIii in sorted ( I1oo , key = lambda ooOO00oOOo000 : ooOO00oOOo000 ) :
  iIOO0OOoooo0o = os . path . split ( iiI1IIIii [ : - 1 ] ) [ 1 ]
  if iIOO0OOoooo0o in Iii1I1I11iiI1 : continue
  elif iIOO0OOoooo0o in OOo0 : continue
  elif iIOO0OOoooo0o == 'packages' : continue
  IiIi1Ii = os . path . join ( iiI1IIIii , 'addon.xml' )
  if os . path . exists ( IiIi1Ii ) :
   OooOO0oOOo0O = open ( IiIi1Ii )
   ooIii1ii1II1iI1 = OooOO0oOOo0O . read ( )
   O0Oo0o000oO = wiz . parseDOM ( ooIii1ii1II1iI1 , 'addon' , ret = 'id' )
   if 32 - 32: OoooooooOO / II111iiii / IIIi1i1I + IiiIII111ii / O0
   oOO0 = iIOO0OOoooo0o if len ( O0Oo0o000oO ) == 0 else O0Oo0o000oO [ 0 ]
   try :
    iiiI11iIIi1 = xbmcaddon . Addon ( id = oOO0 )
    oO0OIIIiIi1iiI . append ( iiiI11iIIi1 . getAddonInfo ( 'name' ) )
    iI1o0 . append ( oOO0 )
   except :
    pass
 if len ( oO0OIIIiIi1iiI ) == 0 :
  wiz . LogNotify ( "[COLOR %s]%s[/COLOR]" % ( oOOo0O00o , o0OOO ) , "[COLOR %s]No Addons To Remove[/COLOR]" % iIiIi11 )
  return
 if o0OIiII > 16 :
  ooOoo00 = iiIIIII1i1iI . multiselect ( "%s: Select the addons you wish to remove." % o0OOO , oO0OIIIiIi1iiI )
 else :
  ooOoo00 = [ ] ; Ii1I1 = 0
  OoO000Oo0oO = [ "-- Click here to Continue --" ] + oO0OIIIiIi1iiI
  while not Ii1I1 == - 1 :
   Ii1I1 = iiIIIII1i1iI . select ( "%s: Select the addons you wish to remove." % o0OOO , OoO000Oo0oO )
   if Ii1I1 == - 1 : break
   elif Ii1I1 == 0 : break
   else :
    iiiIiiiI1 = ( Ii1I1 - 1 )
    if iiiIiiiI1 in ooOoo00 :
     ooOoo00 . remove ( iiiIiiiI1 )
     OoO000Oo0oO [ Ii1I1 ] = oO0OIIIiIi1iiI [ iiiIiiiI1 ]
    else :
     ooOoo00 . append ( iiiIiiiI1 )
     OoO000Oo0oO [ Ii1I1 ] = "[B][COLOR %s]%s[/COLOR][/B]" % ( oOOo0O00o , oO0OIIIiIi1iiI [ iiiIiiiI1 ] )
 if ooOoo00 == None : return
 if len ( ooOoo00 ) > 0 :
  wiz . addonUpdates ( 'set' )
  for I1IIIIIi1IIiI in ooOoo00 :
   III11I11ii ( iI1o0 [ I1IIIIIi1IIiI ] , oO0OIIIiIi1iiI [ I1IIIIIi1IIiI ] , True )
   if 82 - 82: iii11iiII % II111iiii - iii11iiII + II111iiii
  xbmc . sleep ( 500 )
  if 61 - 61: i11iIiiIii * IIIi1i1I % Ooo0O * OO00O0O0O00Oo - OoooooooOO - I1111
  if I11i1I1I == 1 : o0OOo = 1
  elif I11i1I1I == 2 : o0OOo = 0
  else : o0OOo = iiIIIII1i1iI . yesno ( o0OOO , "[COLOR %s]Would you like to [COLOR %s]Force close[/COLOR] kodi or [COLOR %s]Reload Profile[/COLOR]?[/COLOR]" % ( iIiIi11 , oOOo0O00o , oOOo0O00o ) , yeslabel = "[B][COLOR green]Reload Profile[/COLOR][/B]" , nolabel = "[B][COLOR red]Force Close[/COLOR][/B]" )
  if o0OOo == 1 : wiz . reloadFix ( 'remove addon' )
  else : wiz . addonUpdates ( 'reset' ) ; wiz . killxbmc ( True )
  if 42 - 42: O0 % IiiIII111ii - iIii1I11I1II1 + OO00O0O0O00Oo % ooOo + OOoooooO
def o0OoO0oo0O0o ( ) :
 if os . path . exists ( ooOOOo0oo0O0 ) :
  iiiii1II ( '[COLOR red][B][REMOVE][/B][/COLOR] All Addon_Data' , 'removedata' , 'all' , themeit = oooOo0OOOoo0 )
  iiiii1II ( '[COLOR red][B][REMOVE][/B][/COLOR] All Addon_Data for Uninstalled Addons' , 'removedata' , 'uninstalled' , themeit = oooOo0OOOoo0 )
  iiiii1II ( '[COLOR red][B][REMOVE][/B][/COLOR] All Empty Folders in Addon_Data' , 'removedata' , 'empty' , themeit = oooOo0OOOoo0 )
  iiiii1II ( '[COLOR red][B][REMOVE][/B][/COLOR] %s Addon_Data' % o0OOO , 'resetaddon' , themeit = oooOo0OOOoo0 )
  if O0O0ooOOO == 'No' : iiiii1II ( wiz . sep ( ) , '' , themeit = OOoO )
  I1oo = glob . glob ( os . path . join ( ooOOOo0oo0O0 , '*/' ) )
  for iiI1IIIii in sorted ( I1oo , key = lambda ooOO00oOOo000 : ooOO00oOOo000 ) :
   iIOO0OOoooo0o = iiI1IIIii . replace ( ooOOOo0oo0O0 , '' ) . replace ( '\\' , '' ) . replace ( '/' , '' )
   i1i1i1I = os . path . join ( iiI1IIIii . replace ( ooOOOo0oo0O0 , O0O ) , 'icon.png' )
   oOoo000 = os . path . join ( iiI1IIIii . replace ( ooOOOo0oo0O0 , O0O ) , 'fanart.png' )
   ii1III1iiIi = iIOO0OOoooo0o
   I1ii1iI = { 'audio.' : '[COLOR orange][AUDIO] [/COLOR]' , 'metadata.' : '[COLOR cyan][METADATA] [/COLOR]' , 'module.' : '[COLOR orange][MODULE] [/COLOR]' , 'plugin.' : '[COLOR blue][PLUGIN] [/COLOR]' , 'program.' : '[COLOR orange][PROGRAM] [/COLOR]' , 'repository.' : '[COLOR gold][REPO] [/COLOR]' , 'script.' : '[COLOR green][SCRIPT] [/COLOR]' , 'service.' : '[COLOR green][SERVICE] [/COLOR]' , 'skin.' : '[COLOR dodgerblue][SKIN] [/COLOR]' , 'video.' : '[COLOR orange][VIDEO] [/COLOR]' , 'weather.' : '[COLOR yellow][WEATHER] [/COLOR]' }
   for ooO000OO in I1ii1iI :
    ii1III1iiIi = ii1III1iiIi . replace ( ooO000OO , I1ii1iI [ ooO000OO ] )
   if iIOO0OOoooo0o in Iii1I1I11iiI1 : ii1III1iiIi = '[COLOR green][B][PROTECTED][/B][/COLOR] %s' % ii1III1iiIi
   else : ii1III1iiIi = '[COLOR red][B][REMOVE][/B][/COLOR] %s' % ii1III1iiIi
   iiiii1II ( ' %s' % ii1III1iiIi , 'removedata' , iIOO0OOoooo0o , icon = i1i1i1I , fanart = oOoo000 , themeit = oooOo0OOOoo0 )
 else :
  iiiii1II ( 'No Addon data folder found.' , '' , themeit = OOoO )
 iIi1 ( 'files' , 'viewType' )
 if 43 - 43: OOoooooO * OO00O0O0O00Oo % iii11iiII
def iiiI11 ( ) :
 iiiii1II ( "[I][B][COLOR red]!!Notice: Disabling Some Addons Can Cause Issues!![/COLOR][/B][/I]" , '' , icon = IiIi11iI )
 I1oo = glob . glob ( os . path . join ( O0O , '*/' ) )
 ooOO00oOOo000 = 0
 for iiI1IIIii in sorted ( I1oo , key = lambda ooOO00oOOo000 : ooOO00oOOo000 ) :
  iIOO0OOoooo0o = os . path . split ( iiI1IIIii [ : - 1 ] ) [ 1 ]
  if iIOO0OOoooo0o in Iii1I1I11iiI1 : continue
  if iIOO0OOoooo0o in OOo0 : continue
  o0o00OOOO = os . path . join ( iiI1IIIii , 'addon.xml' )
  if os . path . exists ( o0o00OOOO ) :
   ooOO00oOOo000 += 1
   I1oo = iiI1IIIii . replace ( O0O , '' ) [ 1 : - 1 ]
   OooOO0oOOo0O = open ( o0o00OOOO )
   ooIii1ii1II1iI1 = OooOO0oOOo0O . read ( ) . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
   O0Oo0o000oO = wiz . parseDOM ( ooIii1ii1II1iI1 , 'addon' , ret = 'id' )
   I1i1iii1Ii = wiz . parseDOM ( ooIii1ii1II1iI1 , 'addon' , ret = 'name' )
   try :
    Iiii11I = O0Oo0o000oO [ 0 ]
    oO0o00oOOooO0 = I1i1iii1Ii [ 0 ]
   except :
    continue
   try :
    iiiI11iIIi1 = xbmcaddon . Addon ( id = Iiii11I )
    Ii1iI111 = "[COLOR green][Enabled][/COLOR]"
    i11iIi1iIIIIi = "false"
   except :
    Ii1iI111 = "[COLOR red][Disabled][/COLOR]"
    i11iIi1iIIIIi = "true"
    pass
   i1i1i1I = os . path . join ( iiI1IIIii , 'icon.png' ) if os . path . exists ( os . path . join ( iiI1IIIii , 'icon.png' ) ) else iiiiiIIii
   oOoo000 = os . path . join ( iiI1IIIii , 'fanart.jpg' ) if os . path . exists ( os . path . join ( iiI1IIIii , 'fanart.jpg' ) ) else OOO00
   iiiii1II ( "%s %s" % ( Ii1iI111 , oO0o00oOOooO0 ) , 'toggleaddon' , I1oo , i11iIi1iIIIIi , icon = i1i1i1I , fanart = oOoo000 )
   OooOO0oOOo0O . close ( )
 if ooOO00oOOo000 == 0 :
  iiiii1II ( "No Addons Found to Enable or Disable." , '' , icon = IiIi11iI )
 iIi1 ( 'files' , 'viewType' )
 if 43 - 43: OOoooooO * OO00O0O0O00Oo * II111iiii % iIii1I11I1II1 / oO0 - i1Ii
def oo0O0oOoOoo ( ) :
 ii1oOOO0ooOO = [ 'Every Startup' , 'Every Day' , 'Every Three Days' , 'Every Weekly' ]
 OO0I1iiI1iiI1i1 = iiIIIII1i1iI . select ( "[COLOR %s]How often would you list to Auto Clean on Startup?[/COLOR]" % iIiIi11 , ii1oOOO0ooOO )
 if not OO0I1iiI1iiI1i1 == - 1 :
  wiz . setS ( 'autocleanfeq' , str ( OO0I1iiI1iiI1i1 ) )
  wiz . LogNotify ( '[COLOR %s]Auto Clean Up[/COLOR]' % oOOo0O00o , '[COLOR %s]Fequency Now %s[/COLOR]' % ( iIiIi11 , ii1oOOO0ooOO [ OO0I1iiI1iiI1i1 ] ) )
  if 88 - 88: IIIi1i1I % Ooo0O - i11IiIiiIIIII % IIIi1i1I + i1Ii - iiIIi1IiIi11
def ii1OO0 ( ) :
 iiiii1II ( 'Convert Text Files to 0.1.7' , 'converttext' , themeit = OOOiiiiI )
 iiiii1II ( 'Create QR Code' , 'createqr' , themeit = OOOiiiiI )
 iiiii1II ( 'Test Notifications' , 'testnotify' , themeit = OOOiiiiI )
 iiiii1II ( 'Test Update' , 'testupdate' , themeit = OOOiiiiI )
 iiiii1II ( 'Test First Run' , 'testfirst' , themeit = OOOiiiiI )
 iiiii1II ( 'Test First Run Settings' , 'testfirstrun' , themeit = OOOiiiiI )
 iiiii1II ( 'Test APk' , 'testapk' , themeit = OOOiiiiI )
 if 96 - 96: O0 . iiIIi1IiIi11 - ooOo * Ooo0O
 iIi1 ( 'files' , 'viewType' )
 if 68 - 68: IIIi1i1I - Ooo0O / o0o0Oo0oooo0 - OO00O0O0O00Oo . iiIIi1IiIi11
 if 50 - 50: iIii1I11I1II1 - iiIIi1IiIi11 - i11IiIiiIIIII
 if 60 - 60: iIii1I11I1II1 * OOoooooO
 if 71 - 71: o0o0Oo0oooo0 % Ooo0O % OOoooooO
def I111 ( name , type , theme = None , over = False ) :
 if over == False :
  III1 = wiz . checkBuild ( name , 'url' )
  if III1 == False :
   wiz . LogNotify ( "[COLOR %s]%s[/COLOR]" % ( oOOo0O00o , o0OOO ) , "[COLOR %s]Unabled to find build[/COLOR]" % iIiIi11 )
   return
  OOO000OOo0o0O = wiz . workingURL ( III1 )
  if OOO000OOo0o0O == False :
   wiz . LogNotify ( "[COLOR %s]%s[/COLOR]" % ( oOOo0O00o , o0OOO ) , "[COLOR %s]Build Zip Error: %s[/COLOR]" % ( iIiIi11 , OOO000OOo0o0O ) )
   return
 if type == 'gui' :
  if name == O000oo0O :
   if over == True : I111Iii1 = 1
   else : I111Iii1 = iiIIIII1i1iI . yesno ( o0OOO , '[COLOR %s]Would you like to apply the guifix for:' % iIiIi11 , '[COLOR %s]%s[/COLOR]?[/COLOR]' % ( oOOo0O00o , name ) , nolabel = '[B][COLOR red]No, Cancel[/COLOR][/B]' , yeslabel = '[B][COLOR green]Apply Fix[/COLOR][/B]' )
  else :
   I111Iii1 = iiIIIII1i1iI . yesno ( "%s - [COLOR red]WARNING!![/COLOR]" % o0OOO , "[COLOR %s][COLOR %s]%s[/COLOR] community build is not currently installed." % ( iIiIi11 , oOOo0O00o , name ) , "Would you like to apply the guiFix anyways?.[/COLOR]" , nolabel = '[B][COLOR red]No, Cancel[/COLOR][/B]' , yeslabel = '[B][COLOR green]Apply Fix[/COLOR][/B]' )
  if I111Iii1 :
   i11i = wiz . checkBuild ( name , 'gui' )
   O0o0O00o0o = name . replace ( '\\' , '' ) . replace ( '/' , '' ) . replace ( ':' , '' ) . replace ( '*' , '' ) . replace ( '?' , '' ) . replace ( '"' , '' ) . replace ( '<' , '' ) . replace ( '>' , '' ) . replace ( '|' , '' )
   if not wiz . workingURL ( i11i ) == True : wiz . LogNotify ( "[COLOR %s]%s[/COLOR]" % ( oOOo0O00o , o0OOO ) , '[COLOR %s]GuiFix: Invalid Zip Url![/COLOR]' % iIiIi11 ) ; return
   if not os . path . exists ( o0o0OOO0o0 ) : os . makedirs ( o0o0OOO0o0 )
   oo00 . create ( o0OOO , '[COLOR %s][B]Downloading GuiFix:[/B][/COLOR] [COLOR %s]%s[/COLOR]' % ( iIiIi11 , oOOo0O00o , name ) , '' , 'Please Wait' )
   I1III1iIi = os . path . join ( o0o0OOO0o0 , '%s_guisettings.zip' % O0o0O00o0o )
   try : os . remove ( I1III1iIi )
   except : pass
   downloader . download ( i11i , I1III1iIi , oo00 )
   xbmc . sleep ( 500 )
   II1iIi1IiIii = '[COLOR %s][B]Installing:[/B][/COLOR] [COLOR %s]%s[/COLOR]' % ( iIiIi11 , oOOo0O00o , name )
   oo00 . update ( 0 , II1iIi1IiIii , '' , 'Please Wait' )
   extract . all ( I1III1iIi , oOo00Oo00O , oo00 , title = II1iIi1IiIii )
   oo00 . close ( )
   wiz . defaultSkin ( )
   wiz . lookandFeelData ( 'save' )
   if I11i1I1I == 1 : o0OOo = 1
   elif I11i1I1I == 2 : o0OOo = 0
   else : o0OOo = iiIIIII1i1iI . yesno ( o0OOO , "[COLOR %s]The Gui fix has been installed.  Would you like to Reload the profile or Force Close Kodi?[/COLOR]" % iIiIi11 , yeslabel = "[B][COLOR red]Reload Profile[/COLOR][/B]" , nolabel = "[B][COLOR green]Force Close[/COLOR][/B]" )
   if o0OOo == 1 : wiz . reloadFix ( )
   else : iiIIIII1i1iI . ok ( o0OOO , "[COLOR %s]To save changes you now need to force close Kodi, Press OK to force close Kodi[/COLOR]" % iIiIi11 ) ; wiz . killxbmc ( 'true' )
  else :
   wiz . LogNotify ( "[COLOR %s]%s[/COLOR]" % ( oOOo0O00o , o0OOO ) , '[COLOR %s]GuiFix: Cancelled![/COLOR]' % iIiIi11 )
 elif type == 'fresh' :
  II1IIiiI1 ( name )
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
  O00O00 = int ( o0OIiII ) ; oOooO0OoO = int ( float ( wiz . checkBuild ( name , 'kodi' ) ) )
  if not O00O00 == oOooO0OoO :
   if O00O00 == 16 and oOooO0OoO <= 15 : I1iii = False
   else : I1iii = True
  else : I1iii = False
  if I1iii == True :
   o0oOOOOoo0 = iiIIIII1i1iI . yesno ( "%s - [COLOR red]WARNING!![/COLOR]" % o0OOO , '[COLOR %s]There is a chance that the skin will not appear correctly' % iIiIi11 , 'When installing a %s build on a Kodi %s install' % ( wiz . checkBuild ( name , 'kodi' ) , o0OIiII ) , 'Would you still like to install: [COLOR %s]%s v%s[/COLOR]?[/COLOR]' % ( oOOo0O00o , name , wiz . checkBuild ( name , 'version' ) ) , nolabel = '[B][COLOR red]No, Cancel[/COLOR][/B]' , yeslabel = '[B][COLOR green]Yes, Install[/COLOR][/B]' )
  else :
   if not over == False : o0oOOOOoo0 = 1
   else : o0oOOOOoo0 = iiIIIII1i1iI . yesno ( o0OOO , '[COLOR %s]Would you like to Download and Install:' % iIiIi11 , '[COLOR %s]%s v%s[/COLOR]?[/COLOR]' % ( oOOo0O00o , name , wiz . checkBuild ( name , 'version' ) ) , nolabel = '[B][COLOR red]No, Cancel[/COLOR][/B]' , yeslabel = '[B][COLOR green]Yes, Install[/COLOR][/B]' )
  if o0oOOOOoo0 :
   wiz . clearS ( 'build' )
   i11i = wiz . checkBuild ( name , 'url' )
   O0o0O00o0o = name . replace ( '\\' , '' ) . replace ( '/' , '' ) . replace ( ':' , '' ) . replace ( '*' , '' ) . replace ( '?' , '' ) . replace ( '"' , '' ) . replace ( '<' , '' ) . replace ( '>' , '' ) . replace ( '|' , '' )
   if not wiz . workingURL ( i11i ) == True : wiz . LogNotify ( "[COLOR %s]%s[/COLOR]" % ( oOOo0O00o , o0OOO ) , '[COLOR %s]Build Install: Invalid Zip Url![/COLOR]' % iIiIi11 ) ; return
   if not os . path . exists ( o0o0OOO0o0 ) : os . makedirs ( o0o0OOO0o0 )
   oo00 . create ( o0OOO , '[COLOR %s][B]Downloading:[/B][/COLOR] [COLOR %s]%s v%s[/COLOR]' % ( iIiIi11 , oOOo0O00o , name , wiz . checkBuild ( name , 'version' ) ) , '' , 'Please Wait' )
   I1III1iIi = os . path . join ( o0o0OOO0o0 , '%s.zip' % O0o0O00o0o )
   try : os . remove ( I1III1iIi )
   except : pass
   wiz . add_one ( name )
   downloader . download ( i11i , I1III1iIi , oo00 )
   xbmc . sleep ( 500 )
   II1iIi1IiIii = '[COLOR %s][B]Installing:[/B][/COLOR] [COLOR %s]%s v%s[/COLOR]' % ( iIiIi11 , oOOo0O00o , name , wiz . checkBuild ( name , 'version' ) )
   oo00 . update ( 0 , II1iIi1IiIii , '' , 'Please Wait' )
   OoO00O0 , I1 , Iiii1i11ii1Ii = extract . all ( I1III1iIi , o00 , oo00 , title = II1iIi1IiIii )
   if int ( float ( OoO00O0 ) ) > 0 :
    wiz . fixmetas ( )
    wiz . lookandFeelData ( 'save' )
    wiz . defaultSkin ( )
    if 80 - 80: i11iIiiIii % oO0
    wiz . setS ( 'buildname' , name )
    wiz . setS ( 'buildversion' , wiz . checkBuild ( name , 'version' ) )
    wiz . setS ( 'buildtheme' , '' )
    wiz . setS ( 'latestversion' , wiz . checkBuild ( name , 'version' ) )
    wiz . setS ( 'lastbuildcheck' , str ( OOI1iI1ii1II ) )
    wiz . setS ( 'installed' , 'true' )
    wiz . setS ( 'extract' , str ( OoO00O0 ) )
    wiz . setS ( 'errors' , str ( I1 ) )
    wiz . log ( 'INSTALLED %s: [ERRORS:%s]' % ( OoO00O0 , I1 ) )
    try : os . remove ( I1III1iIi )
    except : pass
    if int ( float ( I1 ) ) > 0 :
     I111Iii1 = iiIIIII1i1iI . yesno ( o0OOO , '[COLOR %s][COLOR %s]%s v%s[/COLOR]' % ( iIiIi11 , oOOo0O00o , name , wiz . checkBuild ( name , 'version' ) ) , 'Completed: [COLOR %s]%s%s[/COLOR] [Errors:[COLOR %s]%s[/COLOR]]' % ( oOOo0O00o , OoO00O0 , '%' , oOOo0O00o , I1 ) , 'Would you like to view the errors?[/COLOR]' , nolabel = '[B][COLOR red]No Thanks[/COLOR][/B]' , yeslabel = '[B][COLOR green]View Errors[/COLOR][/B]' )
     if I111Iii1 :
      if isinstance ( I1 , unicode ) :
       Iiii1i11ii1Ii = Iiii1i11ii1Ii . encode ( 'utf-8' )
      wiz . TextBox ( o0OOO , Iiii1i11ii1Ii )
    oo00 . close ( )
    OOo00OoO = wiz . themeCount ( name )
    if not OOo00OoO == False :
     I111 ( name , 'theme' )
    if o0OIiII >= 17 : wiz . addonDatabase ( IiII1IiiIiI1 , 1 )
    if I11i1I1I == 1 : o0OOo = 1
    elif I11i1I1I == 2 : o0OOo = 0
    else : o0OOo = iiIIIII1i1iI . yesno ( o0OOO , "[COLOR %s]Would you like to [COLOR %s]Force close[/COLOR] kodi or [COLOR %s]Reload Profile[/COLOR]?[/COLOR]" % ( iIiIi11 , oOOo0O00o , oOOo0O00o ) , yeslabel = "[B][COLOR red]Reload Profile[/COLOR][/B]" , nolabel = "[B][COLOR green]Force Close[/COLOR][/B]" )
    if o0OOo == 1 : wiz . reloadFix ( )
    else : wiz . killxbmc ( True )
   else :
    if isinstance ( I1 , unicode ) :
     Iiii1i11ii1Ii = Iiii1i11ii1Ii . encode ( 'utf-8' )
    wiz . TextBox ( "%s: Error Installing Build" % o0OOO , Iiii1i11ii1Ii )
  else :
   wiz . LogNotify ( "[COLOR %s]%s[/COLOR]" % ( oOOo0O00o , o0OOO ) , '[COLOR %s]Build Install: Cancelled![/COLOR]' % iIiIi11 )
 elif type == 'theme' :
  if theme == None :
   OOo00OoO = wiz . checkBuild ( name , 'theme' )
   OOO00o0 = [ ]
   if not OOo00OoO == 'http://' and wiz . workingURL ( OOo00OoO ) == True :
    OOO00o0 = wiz . themeCount ( name , False )
    if len ( OOO00o0 ) > 0 :
     if iiIIIII1i1iI . yesno ( o0OOO , "[COLOR %s]The Build [COLOR %s]%s[/COLOR] comes with [COLOR %s]%s[/COLOR] different themes" % ( iIiIi11 , oOOo0O00o , name , oOOo0O00o , len ( OOO00o0 ) ) , "Would you like to install one now?[/COLOR]" , yeslabel = "[B][COLOR green]Install Theme[/COLOR][/B]" , nolabel = "[B][COLOR red]Cancel Themes[/COLOR][/B]" ) :
      wiz . log ( "Theme List: %s " % str ( OOO00o0 ) )
      OOoOooo = iiIIIII1i1iI . select ( o0OOO , OOO00o0 )
      wiz . log ( "Theme install selected: %s" % OOoOooo )
      if not OOoOooo == - 1 : theme = OOO00o0 [ OOoOooo ] ; O0oO0oo0O0 = True
      else : wiz . LogNotify ( "[COLOR %s]%s[/COLOR]" % ( oOOo0O00o , o0OOO ) , '[COLOR %s]Theme Install: Cancelled![/COLOR]' % iIiIi11 ) ; return
     else : wiz . LogNotify ( "[COLOR %s]%s[/COLOR]" % ( oOOo0O00o , o0OOO ) , '[COLOR %s]Theme Install: Cancelled![/COLOR]' % iIiIi11 ) ; return
   else : wiz . LogNotify ( "[COLOR %s]%s[/COLOR]" % ( oOOo0O00o , o0OOO ) , '[COLOR %s]Theme Install: None Found![/COLOR]' % iIiIi11 )
  else : O0oO0oo0O0 = iiIIIII1i1iI . yesno ( o0OOO , '[COLOR %s]Would you like to install the theme:' % iIiIi11 , '[COLOR %s]%s[/COLOR]' % ( oOOo0O00o , theme ) , 'for [COLOR %s]%s v%s[/COLOR]?[/COLOR]' % ( oOOo0O00o , name , wiz . checkBuild ( name , 'version' ) ) , yeslabel = "[B][COLOR green]Install Theme[/COLOR][/B]" , nolabel = "[B][COLOR red]Cancel Themes[/COLOR][/B]" )
  if O0oO0oo0O0 :
   o0O0OOoo = wiz . checkTheme ( name , theme , 'url' )
   O0o0O00o0o = name . replace ( '\\' , '' ) . replace ( '/' , '' ) . replace ( ':' , '' ) . replace ( '*' , '' ) . replace ( '?' , '' ) . replace ( '"' , '' ) . replace ( '<' , '' ) . replace ( '>' , '' ) . replace ( '|' , '' )
   if not wiz . workingURL ( o0O0OOoo ) == True : wiz . LogNotify ( "[COLOR %s]%s[/COLOR]" % ( oOOo0O00o , o0OOO ) , '[COLOR %s]Theme Install: Invalid Zip Url![/COLOR]' % iIiIi11 ) ; return False
   if not os . path . exists ( o0o0OOO0o0 ) : os . makedirs ( o0o0OOO0o0 )
   oo00 . create ( o0OOO , '[COLOR %s][B]Downloading:[/B][/COLOR] [COLOR %s]%s[/COLOR]' % ( iIiIi11 , oOOo0O00o , theme ) , '' , 'Please Wait' )
   I1III1iIi = os . path . join ( o0o0OOO0o0 , '%s.zip' % O0o0O00o0o )
   try : os . remove ( I1III1iIi )
   except : pass
   downloader . download ( o0O0OOoo , I1III1iIi , oo00 )
   xbmc . sleep ( 500 )
   oo00 . update ( 0 , "" , "Installing %s " % name )
   oo00ooOooO = False
   if OOOoO000 not in [ "fresh" , "normal" ] :
    oo00ooOooO = ooIi111iII ( I1III1iIi ) if not wiz . currSkin ( ) in [ 'skin.confluence' , 'skin.estuary' ] else False
    Oo0OoOo = iiIIIi1i ( I1III1iIi ) if not wiz . currSkin ( ) in [ 'skin.confluence' , 'skin.estuary' ] else False
    if oo00ooOooO == True :
     wiz . lookandFeelData ( 'save' )
     iIi1i1i1II11I = 'skin.confluence' if o0OIiII < 17 else 'skin.estuary'
     O0OOOO0OooOo = xbmc . getSkinDir ( )
     if 13 - 13: O0 % OOoooooO % i11IiIiiIIIII
     skinSwitch . swapSkins ( iIi1i1i1II11I )
     ooOO00oOOo000 = 0
     xbmc . sleep ( 1000 )
     while not xbmc . getCondVisibility ( "Window.isVisible(yesnodialog)" ) and ooOO00oOOo000 < 150 :
      ooOO00oOOo000 += 1
      xbmc . sleep ( 200 )
     if xbmc . getCondVisibility ( "Window.isVisible(yesnodialog)" ) :
      wiz . ebi ( 'SendClick(11)' )
     else : wiz . LogNotify ( "[COLOR %s]%s[/COLOR]" % ( oOOo0O00o , o0OOO ) , '[COLOR %s]Theme Install: Skin Swap Timed Out![/COLOR]' % iIiIi11 ) ; return
     xbmc . sleep ( 500 )
   II1iIi1IiIii = '[COLOR %s][B]Installing Theme:[/B][/COLOR] [COLOR %s]%s[/COLOR]' % ( iIiIi11 , oOOo0O00o , theme )
   oo00 . update ( 0 , II1iIi1IiIii , '' , 'Please Wait' )
   OoO00O0 , I1 , Iiii1i11ii1Ii = extract . all ( I1III1iIi , o00 , oo00 , title = II1iIi1IiIii )
   wiz . setS ( 'buildtheme' , theme )
   wiz . log ( 'INSTALLED %s: [ERRORS:%s]' % ( OoO00O0 , I1 ) )
   oo00 . close ( )
   if OOOoO000 not in [ "fresh" , "normal" ] :
    wiz . forceUpdate ( )
    if o0OIiII >= 17 : wiz . kodi17Fix ( )
    if Oo0OoOo == True :
     wiz . lookandFeelData ( 'save' )
     wiz . defaultSkin ( )
     O0OOOO0OooOo = wiz . getS ( 'defaultskin' )
     skinSwitch . swapSkins ( O0OOOO0OooOo )
     ooOO00oOOo000 = 0
     xbmc . sleep ( 1000 )
     while not xbmc . getCondVisibility ( "Window.isVisible(yesnodialog)" ) and ooOO00oOOo000 < 150 :
      ooOO00oOOo000 += 1
      xbmc . sleep ( 200 )
      if 25 - 25: OoooooooOO % IiiIII111ii * II111iiii - I1111
     if xbmc . getCondVisibility ( "Window.isVisible(yesnodialog)" ) :
      wiz . ebi ( 'SendClick(11)' )
     wiz . lookandFeelData ( 'restore' )
    elif oo00ooOooO == True :
     skinSwitch . swapSkins ( O0OOOO0OooOo )
     ooOO00oOOo000 = 0
     xbmc . sleep ( 1000 )
     while not xbmc . getCondVisibility ( "Window.isVisible(yesnodialog)" ) and ooOO00oOOo000 < 150 :
      ooOO00oOOo000 += 1
      xbmc . sleep ( 200 )
      if 95 - 95: ooOo % OO00O0O0O00Oo * ooOo + O0 . OO00O0O0O00Oo % OoooooooOO
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
   if 6 - 6: o0o0Oo0oooo0 - OOoooooO * I1I1i1 + o0o0Oo0oooo0 % I1I1i1
def OOO00000o0 ( name , url ) :
 if not wiz . workingURL ( url ) :
  LogNotify ( "[COLOR %s]%s[/COLOR]" % ( oOOo0O00o , o0OOO ) , '[COLOR %s]Invalid URL for Build[/COLOR]' % iIiIi11 ) ; return
 type = iiIIIII1i1iI . yesno ( o0OOO , "[COLOR %s]Would you like to preform a [COLOR %s]Fresh Install[/COLOR] or [COLOR %s]Normal Install[/COLOR] for:[/COLOR]" % ( iIiIi11 , oOOo0O00o , oOOo0O00o ) , "[COLOR %s]%s[/COLOR]" % ( oOOo0O00o , name ) , yeslabel = "[B][COLOR green]Fresh Install[/COLOR][/B]" , nolabel = "[B][COLOR red]Normal Install[/COLOR][/B]" )
 if type == 1 :
  II1IIiiI1 ( 'third' , True )
 wiz . clearS ( 'build' )
 O0o0O00o0o = name . replace ( '\\' , '' ) . replace ( '/' , '' ) . replace ( ':' , '' ) . replace ( '*' , '' ) . replace ( '?' , '' ) . replace ( '"' , '' ) . replace ( '<' , '' ) . replace ( '>' , '' ) . replace ( '|' , '' )
 if not os . path . exists ( o0o0OOO0o0 ) : os . makedirs ( o0o0OOO0o0 )
 oo00 . create ( o0OOO , '[COLOR %s][B]Downloading:[/B][/COLOR] [COLOR %s]%s[/COLOR]' % ( iIiIi11 , oOOo0O00o , name ) , '' , 'Please Wait' )
 I1III1iIi = os . path . join ( o0o0OOO0o0 , '%s.zip' % O0o0O00o0o )
 try : os . remove ( I1III1iIi )
 except : pass
 downloader . download ( url , I1III1iIi , oo00 )
 xbmc . sleep ( 500 )
 II1iIi1IiIii = '[COLOR %s][B]Installing:[/B][/COLOR] [COLOR %s]%s[/COLOR]' % ( iIiIi11 , oOOo0O00o , name )
 oo00 . update ( 0 , II1iIi1IiIii , '' , 'Please Wait' )
 OoO00O0 , I1 , Iiii1i11ii1Ii = extract . all ( I1III1iIi , o00 , oo00 , title = II1iIi1IiIii )
 if int ( float ( OoO00O0 ) ) > 0 :
  wiz . fixmetas ( )
  wiz . lookandFeelData ( 'save' )
  wiz . defaultSkin ( )
  if 96 - 96: I1I1i1 * IIIi1i1I - iii11iiII * I1I1i1 * i1IIi
  wiz . setS ( 'installed' , 'true' )
  wiz . setS ( 'extract' , str ( OoO00O0 ) )
  wiz . setS ( 'errors' , str ( I1 ) )
  wiz . log ( 'INSTALLED %s: [ERRORS:%s]' % ( OoO00O0 , I1 ) )
  try : os . remove ( I1III1iIi )
  except : pass
  if int ( float ( I1 ) ) > 0 :
   I111Iii1 = iiIIIII1i1iI . yesno ( o0OOO , '[COLOR %s][COLOR %s]%s[/COLOR]' % ( iIiIi11 , oOOo0O00o , name ) , 'Completed: [COLOR %s]%s%s[/COLOR] [Errors:[COLOR %s]%s[/COLOR]]' % ( oOOo0O00o , OoO00O0 , '%' , oOOo0O00o , I1 ) , 'Would you like to view the errors?[/COLOR]' , nolabel = '[B][COLOR red]No Thanks[/COLOR][/B]' , yeslabel = '[B][COLOR green]View Errors[/COLOR][/B]' )
   if I111Iii1 :
    if isinstance ( I1 , unicode ) :
     Iiii1i11ii1Ii = Iiii1i11ii1Ii . encode ( 'utf-8' )
    wiz . TextBox ( o0OOO , Iiii1i11ii1Ii )
 oo00 . close ( )
 if o0OIiII >= 17 : wiz . addonDatabase ( IiII1IiiIiI1 , 1 )
 if I11i1I1I == 1 : o0OOo = 1
 elif I11i1I1I == 2 : o0OOo = 0
 else : o0OOo = iiIIIII1i1iI . yesno ( o0OOO , "[COLOR %s]Would you like to [COLOR %s]Force close[/COLOR] kodi or [COLOR %s]Reload Profile[/COLOR]?[/COLOR]" % ( iIiIi11 , oOOo0O00o , oOOo0O00o ) , yeslabel = "[B][COLOR green]Reload Profile[/COLOR][/B]" , nolabel = "[B][COLOR red]Force Close[/COLOR][/B]" )
 if o0OOo == 1 : wiz . reloadFix ( )
 else : wiz . killxbmc ( True )
 if 8 - 8: OOoooooO - Ooo0O + iIii1I11I1II1 + i1IIi * IiiIII111ii - iIii1I11I1II1
def ooIi111iII ( path ) :
 i1IiI1iIIIIIi = zipfile . ZipFile ( path )
 for ii1IIIIiI11 in i1IiI1iIIIIIi . infolist ( ) :
  if '/settings.xml' in ii1IIIIiI11 . filename :
   return True
 return False
 if 36 - 36: i1Ii
def iiIIIi1i ( path ) :
 i1IiI1iIIIIIi = zipfile . ZipFile ( path )
 for ii1IIIIiI11 in i1IiI1iIIIIIi . infolist ( ) :
  if '/guisettings.xml' in ii1IIIIiI11 . filename :
   return True
 return False
 if 19 - 19: o0o0Oo0oooo0 . I1I1i1 . OoooooooOO
def O0ooOO ( apk , url , Brackets ) :
 wiz . log ( apk )
 wiz . log ( url )
 if wiz . platform ( ) == 'android' :
  I111Iii1 = iiIIIII1i1iI . yesno ( o0OOO , "[COLOR %s]Would you like to download and install:" % iIiIi11 , "[COLOR %s]%s[/COLOR]" % ( oOOo0O00o , apk ) , yeslabel = "[B][COLOR green]Download[/COLOR][/B]" , nolabel = "[B][COLOR red]Cancel[/COLOR][/B]" )
  if not I111Iii1 : wiz . LogNotify ( "[COLOR %s]%s[/COLOR]" % ( oOOo0O00o , o0OOO ) , '[COLOR %s]ERROR: Install Cancelled[/COLOR]' % iIiIi11 ) ; return
  iIi = apk
  if not os . path . exists ( o0o0OOO0o0 ) : os . makedirs ( o0o0OOO0o0 )
  if not wiz . workingURL ( url ) == True : wiz . LogNotify ( "[COLOR %s]%s[/COLOR]" % ( oOOo0O00o , o0OOO ) , '[COLOR %s]APK Installer: Invalid Apk Url![/COLOR]' % iIiIi11 ) ; return
  oo00 . create ( o0OOO , '[COLOR %s][B]Downloading:[/B][/COLOR] [COLOR %s]%s[/COLOR]' % ( iIiIi11 , oOOo0O00o , iIi ) , '' , 'Please Wait' )
  I1III1iIi = os . path . join ( o0o0OOO0o0 , "%s.apk" % apk . replace ( '\\' , '' ) . replace ( '/' , '' ) . replace ( ':' , '' ) . replace ( '*' , '' ) . replace ( '?' , '' ) . replace ( '"' , '' ) . replace ( '<' , '' ) . replace ( '>' , '' ) . replace ( '|' , '' ) )
  try : os . remove ( I1III1iIi )
  except : pass
  downloader . download ( url , I1III1iIi , oo00 )
  xbmc . sleep ( 100 )
  oo00 . close ( )
  if "Brackets" in Brackets :
   ii1iI1i = zipfile . ZipFile ( I1III1iIi )
   for file in ii1iI1i . namelist ( ) :
    if file . endswith ( '.apk' ) :
     with open ( os . path . join ( o0o0OOO0o0 , os . path . basename ( file ) ) , 'wb' ) as OooOO0oOOo0O :
      i1iiiI = file . split ( '/' ) [ 1 ]
      OooOO0oOOo0O . write ( ii1iI1i . read ( file ) )
      xbmc . sleep ( 500 )
      OooOO0oOOo0O . close ( )
      try :
       os . remove ( I1III1iIi )
      except :
       pass
      I1III1iIi = os . path . join ( o0o0OOO0o0 , i1iiiI )
  iiIIIII1i1iI . ok ( o0OOO , "Launching the APK to be installed" , "Follow the install process to complete." )
  notify . apkInstaller ( apk )
  wiz . ebi ( 'StartAndroidActivity("","android.intent.action.VIEW","application/vnd.android.package-archive","file:' + I1III1iIi + '")' )
 else : wiz . LogNotify ( "[COLOR %s]%s[/COLOR]" % ( oOOo0O00o , o0OOO ) , '[COLOR %s]ERROR: None Android Device[/COLOR]' % iIiIi11 )
 if 75 - 75: OoooooooOO . iii11iiII + I1111 / IiiIII111ii - ooOo % IiiIII111ii
 if 89 - 89: iiIIi1IiIi11 * iIii1I11I1II1 + i11iIiiIii . OoooooooOO
 if 51 - 51: iii11iiII / OOoooooO + I1111 % o0o0Oo0oooo0 / IiiIII111ii
 if 25 - 25: I1I1i1
def I1i1i111Ii1I ( name , url , ) :
 if "NULL" in url :
  iiIIIII1i1iI . ok ( o0OOO , "[COLOR ghostwhite]Not a valid selection, please try again.[/COLOR]" )
  sys . exit ( 1 )
  if 64 - 64: i11iIiiIii . OOoooooO
 I1IiI = xbmcgui . DialogProgress ( )
 I1IiI . create ( o0OOO , "" , "" , 'ROM: ' + name )
 O0o0O00o0o = name . replace ( '\\' , '' ) . replace ( '/' , '' ) . replace ( ':' , '' ) . replace ( '*' , '' ) . replace ( '?' , '' ) . replace ( '"' , '' ) . replace ( '<' , '' ) . replace ( '>' , '' ) . replace ( '|' , '' )
 I1III1iIi = os . path . join ( o0o0OOO0o0 , '%s.zip' % O0o0O00o0o )
 downloader . download ( url , I1III1iIi , I1IiI )
 I1IiI . update ( 0 )
 extract . all ( I1III1iIi , iI , I1IiI )
 iiIIIII1i1iI . ok ( o0OOO , "[COLOR yellow]Download complete, ROM Location: [/COLOR][COLOR white]" + iI + "[/COLOR]" )
 if 93 - 93: O0 - I1111 . ooOo
 if 64 - 64: o0o0Oo0oooo0 + I1I1i1
 if 65 - 65: II111iiii / Ooo0O
 if 42 - 42: i11iIiiIii . O0
 if 75 - 75: OO00O0O0O00Oo + iIii1I11I1II1
def IiiiI1 ( part , whole ) :
 return 100 * float ( part ) / float ( whole )
 if 34 - 34: IiiIII111ii + Ooo0O - i1IIi - i1Ii + iIii1I11I1II1
def I1i11ii11 ( type , add , name ) :
 if type == 'saveaddon' :
  o0Oo00oOO = [ ]
  O0oo = urllib . quote_plus ( add . lower ( ) . replace ( ' ' , '' ) )
  o0000O00oO0O = add . replace ( 'Debrid' , 'Real Debrid' )
  IiiI11i1I = urllib . quote_plus ( name . lower ( ) . replace ( ' ' , '' ) )
  name = name . replace ( 'url' , 'URL Resolver' )
  o0Oo00oOO . append ( ( oooOo0OOOoo0 % name . title ( ) , ' ' ) )
  o0Oo00oOO . append ( ( OOoO % 'Save %s Data' % o0000O00oO0O , 'RunPlugin(plugin://%s/?mode=save%s&name=%s)' % ( IiII1IiiIiI1 , O0oo , IiiI11i1I ) ) )
  o0Oo00oOO . append ( ( OOoO % 'Restore %s Data' % o0000O00oO0O , 'RunPlugin(plugin://%s/?mode=restore%s&name=%s)' % ( IiII1IiiIiI1 , O0oo , IiiI11i1I ) ) )
  o0Oo00oOO . append ( ( OOoO % 'Clear %s Data' % o0000O00oO0O , 'RunPlugin(plugin://%s/?mode=clear%s&name=%s)' % ( IiII1IiiIiI1 , O0oo , IiiI11i1I ) ) )
 elif type == 'save' :
  o0Oo00oOO = [ ]
  O0oo = urllib . quote_plus ( add . lower ( ) . replace ( ' ' , '' ) )
  o0000O00oO0O = add . replace ( 'Debrid' , 'Real Debrid' )
  IiiI11i1I = urllib . quote_plus ( name . lower ( ) . replace ( ' ' , '' ) )
  name = name . replace ( 'url' , 'URL Resolver' )
  o0Oo00oOO . append ( ( oooOo0OOOoo0 % name . title ( ) , ' ' ) )
  o0Oo00oOO . append ( ( OOoO % 'Register %s' % o0000O00oO0O , 'RunPlugin(plugin://%s/?mode=auth%s&name=%s)' % ( IiII1IiiIiI1 , O0oo , IiiI11i1I ) ) )
  o0Oo00oOO . append ( ( OOoO % 'Save %s Data' % o0000O00oO0O , 'RunPlugin(plugin://%s/?mode=save%s&name=%s)' % ( IiII1IiiIiI1 , O0oo , IiiI11i1I ) ) )
  o0Oo00oOO . append ( ( OOoO % 'Restore %s Data' % o0000O00oO0O , 'RunPlugin(plugin://%s/?mode=restore%s&name=%s)' % ( IiII1IiiIiI1 , O0oo , IiiI11i1I ) ) )
  o0Oo00oOO . append ( ( OOoO % 'Import %s Data' % o0000O00oO0O , 'RunPlugin(plugin://%s/?mode=import%s&name=%s)' % ( IiII1IiiIiI1 , O0oo , IiiI11i1I ) ) )
  o0Oo00oOO . append ( ( OOoO % 'Clear Addon %s Data' % o0000O00oO0O , 'RunPlugin(plugin://%s/?mode=addon%s&name=%s)' % ( IiII1IiiIiI1 , O0oo , IiiI11i1I ) ) )
 elif type == 'install' :
  o0Oo00oOO = [ ]
  IiiI11i1I = urllib . quote_plus ( name )
  o0Oo00oOO . append ( ( oooOo0OOOoo0 % name , 'RunAddon(%s, ?mode=viewbuild&name=%s)' % ( IiII1IiiIiI1 , IiiI11i1I ) ) )
  o0Oo00oOO . append ( ( OOoO % 'Fresh Install' , 'RunPlugin(plugin://%s/?mode=install&name=%s&url=fresh)' % ( IiII1IiiIiI1 , IiiI11i1I ) ) )
  o0Oo00oOO . append ( ( OOoO % 'Normal Install' , 'RunPlugin(plugin://%s/?mode=install&name=%s&url=normal)' % ( IiII1IiiIiI1 , IiiI11i1I ) ) )
  o0Oo00oOO . append ( ( OOoO % 'Apply guiFix' , 'RunPlugin(plugin://%s/?mode=install&name=%s&url=gui)' % ( IiII1IiiIiI1 , IiiI11i1I ) ) )
  o0Oo00oOO . append ( ( OOoO % 'Build Information' , 'RunPlugin(plugin://%s/?mode=buildinfo&name=%s)' % ( IiII1IiiIiI1 , IiiI11i1I ) ) )
 o0Oo00oOO . append ( ( oooOo0OOOoo0 % '%s Settings' % o0OOO , 'RunPlugin(plugin://%s/?mode=settings)' % IiII1IiiIiI1 ) )
 return o0Oo00oOO
 if 3 - 3: iIii1I11I1II1 % oO0 . iii11iiII % i11IiIiiIIIII
def I1i1I1Iiiii1 ( state ) :
 O0Ooo0O = [ 'includevideo' , 'includeall' , 'includebob' , 'includephoenix' , 'includespecto' , 'includegenesis' , 'includeexodus' , 'includeonechan' , 'includesalts' , 'includesaltslite' ]
 iii1oOo0OoOOOo0 = [ 'Include Video Addons' , 'Include All Addons' , 'Include Bob' , 'Include Phoenix' , 'Include Specto' , 'Include Genesis' , 'Include Exodus' , 'Include One Channel' , 'Include Salts' , 'Include Salts Lite HD' ]
 if state in [ 'true' , 'false' ] :
  for ii1IIIIiI11 in O0Ooo0O :
   wiz . setS ( ii1IIIIiI11 , state )
 else :
  if not state in [ 'includevideo' , 'includeall' ] and wiz . getS ( 'includeall' ) == 'true' :
   try :
    ii1IIIIiI11 = iii1oOo0OoOOOo0 [ O0Ooo0O . index ( state ) ]
    iiIIIII1i1iI . ok ( o0OOO , "[COLOR %s]You will need to turn off [COLOR %s]Include All Addons[/COLOR] to disable[/COLOR] [COLOR %s]%s[/COLOR]" % ( iIiIi11 , oOOo0O00o , oOOo0O00o , ii1IIIIiI11 ) )
   except :
    wiz . LogNotify ( "[COLOR %s]Toggle Cache[/COLOR]" % oOOo0O00o , "[COLOR %s]Invalid id: %s[/COLOR]" % ( iIiIi11 , state ) )
  else :
   OOoo00 = 'true' if wiz . getS ( state ) == 'false' else 'false'
   wiz . setS ( state , OOoo00 )
   if 22 - 22: OOoooooO / OOoooooO - IiiIII111ii % i11IiIiiIIIII . iii11iiII + i1Ii
def OooO00oo0O0 ( url ) :
 if 'watch?v=' in url :
  ooIii1ii1II1iI1 , i1iI = url . split ( '?' )
  Ooiiii11iI1 = i1iI . split ( '&' )
  for ii1IIIIiI11 in Ooiiii11iI1 :
   if ii1IIIIiI11 . startswith ( 'v=' ) :
    url = ii1IIIIiI11 [ 2 : ]
    break
   else : continue
 elif 'embed' in url or 'youtu.be' in url :
  ooIii1ii1II1iI1 = url . split ( '/' )
  if len ( ooIii1ii1II1iI1 [ - 1 ] ) > 5 :
   url = ooIii1ii1II1iI1 [ - 1 ]
  elif len ( ooIii1ii1II1iI1 [ - 2 ] ) > 5 :
   url = ooIii1ii1II1iI1 [ - 2 ]
 wiz . log ( "YouTube URL: %s" % url )
 yt . PlayVideo ( url )
 if 81 - 81: i11iIiiIii + IiiIII111ii % i11iIiiIii - i1IIi
def ii11i1I1i ( ) :
 Iiiii1I = wiz . Grab_Log ( True )
 IiI = wiz . Grab_Log ( True , True )
 ooOoOo0O00oo = 0 ; iIIi111IiII1i = Iiiii1I
 if not IiI == False and not Iiiii1I == False :
  ooOoOo0O00oo = iiIIIII1i1iI . select ( o0OOO , [ "View %s" % Iiiii1I . replace ( iI11iiiI1II , "" ) , "View %s" % IiI . replace ( iI11iiiI1II , "" ) ] )
  if ooOoOo0O00oo == - 1 : wiz . LogNotify ( '[COLOR %s]View Log[/COLOR]' % oOOo0O00o , '[COLOR %s]View Log Cancelled![/COLOR]' % iIiIi11 ) ; return
 elif Iiiii1I == False and IiI == False :
  wiz . LogNotify ( '[COLOR %s]View Log[/COLOR]' % oOOo0O00o , '[COLOR %s]No Log File Found![/COLOR]' % iIiIi11 )
  return
 elif not Iiiii1I == False : ooOoOo0O00oo = 0
 elif not IiI == False : ooOoOo0O00oo = 1
 if 67 - 67: ooOo % iIii1I11I1II1
 iIIi111IiII1i = Iiiii1I if ooOoOo0O00oo == 0 else IiI
 O00oo0oOoO00O = wiz . Grab_Log ( False ) if ooOoOo0O00oo == 0 else wiz . Grab_Log ( False , True )
 if 7 - 7: II111iiii * OOoooooO . Ooo0O / ooOo
 wiz . TextBox ( "%s - %s" % ( o0OOO , iIIi111IiII1i ) , O00oo0oOoO00O )
 if 43 - 43: IiiIII111ii + iiIIi1IiIi11 + i1IIi - o0o0Oo0oooo0 + I1I1i1
def I1iiIiiii1111 ( log = None , count = None , all = None ) :
 if log == None :
  Iiiii1I = wiz . Grab_Log ( True )
  IiI = wiz . Grab_Log ( True , True )
  if not IiI == False and not Iiiii1I == False :
   ooOoOo0O00oo = iiIIIII1i1iI . select ( o0OOO , [ "View %s: %s error(s)" % ( Iiiii1I . replace ( iI11iiiI1II , "" ) , I1iiIiiii1111 ( Iiiii1I , True , True ) ) , "View %s: %s error(s)" % ( IiI . replace ( iI11iiiI1II , "" ) , I1iiIiiii1111 ( IiI , True , True ) ) ] )
   if ooOoOo0O00oo == - 1 : wiz . LogNotify ( '[COLOR %s]View Log[/COLOR]' % oOOo0O00o , '[COLOR %s]View Log Cancelled![/COLOR]' % iIiIi11 ) ; return
  elif Iiiii1I == False and IiI == False :
   wiz . LogNotify ( '[COLOR %s]View Log[/COLOR]' % oOOo0O00o , '[COLOR %s]No Log File Found![/COLOR]' % iIiIi11 )
   return
  elif not Iiiii1I == False : ooOoOo0O00oo = 0
  elif not IiI == False : ooOoOo0O00oo = 1
  log = Iiiii1I if ooOoOo0O00oo == 0 else IiI
 if log == False :
  if count == None :
   wiz . LogNotify ( "[COLOR %s]%s[/COLOR]" % ( oOOo0O00o , o0OOO ) , "[COLOR %s]Log File not Found[/COLOR]" % iIiIi11 )
   return False
  else :
   return 0
 else :
  if os . path . exists ( log ) :
   OooOO0oOOo0O = open ( log , mode = 'r' ) ; ooIii1ii1II1iI1 = OooOO0oOOo0O . read ( ) . replace ( '\n' , '' ) . replace ( '\r' , '' ) ; OooOO0oOOo0O . close ( )
   O0Oo0o000oO = re . compile ( "-->Python callback/script returned the following error<--(.+?)-->End of Python script error report<--" ) . findall ( ooIii1ii1II1iI1 )
   if not count == None :
    if all == None :
     ooOO00oOOo000 = 0
     for ii1IIIIiI11 in O0Oo0o000oO :
      if IiII1IiiIiI1 in ii1IIIIiI11 : ooOO00oOOo000 += 1
     return ooOO00oOOo000
    else : return len ( O0Oo0o000oO )
   if len ( O0Oo0o000oO ) > 0 :
    ooOO00oOOo000 = 0 ; O00oo0oOoO00O = ""
    for ii1IIIIiI11 in O0Oo0o000oO :
     if all == None and not IiII1IiiIiI1 in ii1IIIIiI11 : continue
     else :
      ooOO00oOOo000 += 1
      O00oo0oOoO00O += "[COLOR red]Error Number %s[/COLOR]\n(PythonToCppException) : -->Python callback/script returned the following error<--%s-->End of Python script error report<--\n\n" % ( ooOO00oOOo000 , ii1IIIIiI11 . replace ( '                                          ' , '\n' ) . replace ( '\\\\' , '\\' ) . replace ( o00 , '' ) )
    if ooOO00oOOo000 > 0 :
     wiz . TextBox ( o0OOO , O00oo0oOoO00O )
    else : wiz . LogNotify ( o0OOO , "No Errors Found in Log" )
   else : wiz . LogNotify ( o0OOO , "No Errors Found in Log" )
  else : wiz . LogNotify ( o0OOO , "Log File not Found" )
  if 54 - 54: oO0 + oO0 + i11IiIiiIIIII % i1IIi % i11iIiiIii
o00oO000 = 10
i11i1ii11Ii1 = 92
Ii11iIiiI = 1
o000 = 2
i11ii1 = 3
Ii111I11 = 4
Oo0O0oo = 104
o0O0 = 105
oO0o0 = 107
ooO = 7
oOoO0 = 110
Iii1II1ii = 100
ooOo00 = 108
if 98 - 98: I1111 . iIii1I11I1II1 % OoooooooOO % Ooo0O - oO0
def oO0I1I1i1I1I1I1 ( default = None ) :
 class oO0I1I1i1I1I1I1 ( xbmcgui . WindowXMLDialog ) :
  def __init__ ( self , * args , ** kwargs ) :
   self . default = kwargs [ 'default' ]
   if 34 - 34: I1111 * IiiIII111ii * Ooo0O
  def onInit ( self ) :
   self . title = 101
   self . msg = 102
   self . scrollbar = 103
   self . upload = 201
   self . kodi = 202
   self . kodiold = 203
   self . wizard = 204
   self . okbutton = 205
   OooOO0oOOo0O = open ( self . default , 'r' )
   self . logmsg = OooOO0oOOo0O . read ( )
   OooOO0oOOo0O . close ( )
   self . titlemsg = "%s: %s" % ( o0OOO , self . default . replace ( iI11iiiI1II , '' ) . replace ( o0 , '' ) )
   self . showdialog ( )
   if 21 - 21: OoooooooOO . o0o0Oo0oooo0 - iIii1I11I1II1 % i1Ii
  def showdialog ( self ) :
   self . getControl ( self . title ) . setLabel ( self . titlemsg )
   self . getControl ( self . msg ) . setText ( wiz . highlightText ( self . logmsg ) )
   self . setFocusId ( self . scrollbar )
   if 55 - 55: O0 % ooOo . OoooooooOO * Ooo0O / OoooooooOO . IiiIII111ii
  def onClick ( self , controlId ) :
   if controlId == self . okbutton : self . close ( )
   elif controlId == self . upload : self . close ( ) ; uploadLog . Main ( )
   elif controlId == self . kodi :
    i1Iii = wiz . Grab_Log ( False )
    oO00oO00O0Oo = wiz . Grab_Log ( True )
    if i1Iii == False :
     self . titlemsg = "%s: View Log Error" % o0OOO
     self . getControl ( self . msg ) . setText ( "Log File Does Not Exists!" )
    else :
     self . titlemsg = "%s: %s" % ( o0OOO , oO00oO00O0Oo . replace ( iI11iiiI1II , '' ) )
     self . getControl ( self . title ) . setLabel ( self . titlemsg )
     self . getControl ( self . msg ) . setText ( wiz . highlightText ( i1Iii ) )
     self . setFocusId ( self . scrollbar )
   elif controlId == self . kodiold :
    i1Iii = wiz . Grab_Log ( False , True )
    oO00oO00O0Oo = wiz . Grab_Log ( True , True )
    if i1Iii == False :
     self . titlemsg = "%s: View Log Error" % o0OOO
     self . getControl ( self . msg ) . setText ( "Log File Does Not Exists!" )
    else :
     self . titlemsg = "%s: %s" % ( o0OOO , oO00oO00O0Oo . replace ( iI11iiiI1II , '' ) )
     self . getControl ( self . title ) . setLabel ( self . titlemsg )
     self . getControl ( self . msg ) . setText ( wiz . highlightText ( i1Iii ) )
     self . setFocusId ( self . scrollbar )
   elif controlId == self . wizard :
    i1Iii = wiz . Grab_Log ( False , False , True )
    oO00oO00O0Oo = wiz . Grab_Log ( True , False , True )
    if i1Iii == False :
     self . titlemsg = "%s: View Log Error" % o0OOO
     self . getControl ( self . msg ) . setText ( "Log File Does Not Exists!" )
    else :
     self . titlemsg = "%s: %s" % ( o0OOO , oO00oO00O0Oo . replace ( o0 , '' ) )
     self . getControl ( self . title ) . setLabel ( self . titlemsg )
     self . getControl ( self . msg ) . setText ( wiz . highlightText ( i1Iii ) )
     self . setFocusId ( self . scrollbar )
     if 88 - 88: IIIi1i1I - i1IIi % i11iIiiIii % II111iiii * OoooooooOO
  def onAction ( self , action ) :
   if action == o00oO000 : self . close ( )
   elif action == i11i1ii11Ii1 : self . close ( )
 if default == None : default = wiz . Grab_Log ( True )
 iIiII1 = oO0I1I1i1I1I1I1 ( "LogViewer.xml" , I1ii11iIi11i . getAddonInfo ( 'path' ) , 'DefaultSkin' , default = default )
 iIiII1 . doModal ( )
 del iIiII1
 if 47 - 47: i11IiIiiIIIII
def III11I11ii ( addon , name , over = False ) :
 if not over == False :
  I111Iii1 = 1
 else :
  I111Iii1 = iiIIIII1i1iI . yesno ( o0OOO , '[COLOR %s]Are you sure you want to delete the addon:' % iIiIi11 , 'Name: [COLOR %s]%s[/COLOR]' % ( oOOo0O00o , name ) , 'ID: [COLOR %s]%s[/COLOR][/COLOR]' % ( oOOo0O00o , addon ) , yeslabel = '[B][COLOR green]Remove Addon[/COLOR][/B]' , nolabel = '[B][COLOR red]Don\'t Remove[/COLOR][/B]' )
 if I111Iii1 == 1 :
  iiI1IIIii = os . path . join ( O0O , addon )
  wiz . log ( "Removing Addon %s" % addon )
  wiz . cleanHouse ( iiI1IIIii )
  xbmc . sleep ( 200 )
  try : shutil . rmtree ( iiI1IIIii )
  except Exception , ii1i1i : wiz . log ( "Error removing %s" % addon , xbmc . LOGNOTICE )
  Ii11IiI ( addon , name , over )
 if over == False :
  wiz . LogNotify ( "[COLOR %s]%s[/COLOR]" % ( oOOo0O00o , o0OOO ) , "[COLOR %s]%s Removed[/COLOR]" % ( iIiIi11 , name ) )
  if 92 - 92: OoooooooOO % ooOo / o0o0Oo0oooo0 * o0o0Oo0oooo0 % i11iIiiIii / OoooooooOO
def Ii11IiI ( addon , name = None , over = False ) :
 if addon == 'all' :
  if iiIIIII1i1iI . yesno ( o0OOO , '[COLOR %s]Would you like to remove [COLOR %s]ALL[/COLOR] addon data stored in you Userdata folder?[/COLOR]' % ( iIiIi11 , oOOo0O00o ) , yeslabel = '[B][COLOR green]Remove Data[/COLOR][/B]' , nolabel = '[B][COLOR red]Don\'t Remove[/COLOR][/B]' ) :
   wiz . cleanHouse ( ooOOOo0oo0O0 )
  else : wiz . LogNotify ( '[COLOR %s]Remove Addon Data[/COLOR]' % oOOo0O00o , '[COLOR %s]Cancelled![/COLOR]' % iIiIi11 )
 elif addon == 'uninstalled' :
  if iiIIIII1i1iI . yesno ( o0OOO , '[COLOR %s]Would you like to remove [COLOR %s]ALL[/COLOR] addon data stored in you Userdata folder for uninstalled addons?[/COLOR]' % ( iIiIi11 , oOOo0O00o ) , yeslabel = '[B][COLOR green]Remove Data[/COLOR][/B]' , nolabel = '[B][COLOR red]Don\'t Remove[/COLOR][/B]' ) :
   o00oO0o0o = 0
   for iiI1IIIii in glob . glob ( os . path . join ( ooOOOo0oo0O0 , '*' ) ) :
    iIOO0OOoooo0o = iiI1IIIii . replace ( ooOOOo0oo0O0 , '' ) . replace ( '\\' , '' ) . replace ( '/' , '' )
    if iIOO0OOoooo0o in Iii1I1I11iiI1 : pass
    elif os . path . exists ( os . path . join ( O0O , iIOO0OOoooo0o ) ) : pass
    else : wiz . cleanHouse ( iiI1IIIii ) ; o00oO0o0o += 1 ; wiz . log ( iiI1IIIii ) ; shutil . rmtree ( iiI1IIIii )
   wiz . LogNotify ( '[COLOR %s]Clean up Uninstalled[/COLOR]' % oOOo0O00o , '[COLOR %s]%s Folders(s) Removed[/COLOR]' % ( iIiIi11 , o00oO0o0o ) )
  else : wiz . LogNotify ( '[COLOR %s]Remove Addon Data[/COLOR]' % oOOo0O00o , '[COLOR %s]Cancelled![/COLOR]' % iIiIi11 )
 elif addon == 'empty' :
  if iiIIIII1i1iI . yesno ( o0OOO , '[COLOR %s]Would you like to remove [COLOR %s]ALL[/COLOR] empty addon data folders in you Userdata folder?[/COLOR]' % ( iIiIi11 , oOOo0O00o ) , yeslabel = '[B][COLOR green]Remove Data[/COLOR][/B]' , nolabel = '[B][COLOR red]Don\'t Remove[/COLOR][/B]' ) :
   o00oO0o0o = wiz . emptyfolder ( ooOOOo0oo0O0 )
   wiz . LogNotify ( '[COLOR %s]Remove Empty Folders[/COLOR]' % oOOo0O00o , '[COLOR %s]%s Folders(s) Removed[/COLOR]' % ( iIiIi11 , o00oO0o0o ) )
  else : wiz . LogNotify ( '[COLOR %s]Remove Empty Folders[/COLOR]' % oOOo0O00o , '[COLOR %s]Cancelled![/COLOR]' % iIiIi11 )
 else :
  IiII1 = os . path . join ( oOo00Oo00O , 'addon_data' , addon )
  if addon in Iii1I1I11iiI1 :
   wiz . LogNotify ( "[COLOR %s]Protected Plugin[/COLOR]" % oOOo0O00o , "[COLOR %s]Not allowed to remove Addon_Data[/COLOR]" % iIiIi11 )
  elif os . path . exists ( IiII1 ) :
   if iiIIIII1i1iI . yesno ( o0OOO , '[COLOR %s]Would you also like to remove the addon data for:[/COLOR]' % iIiIi11 , '[COLOR %s]%s[/COLOR]' % ( oOOo0O00o , addon ) , yeslabel = '[B][COLOR green]Remove Data[/COLOR][/B]' , nolabel = '[B][COLOR red]Don\'t Remove[/COLOR][/B]' ) :
    wiz . cleanHouse ( IiII1 )
    try :
     shutil . rmtree ( IiII1 )
    except :
     wiz . log ( "Error deleting: %s" % IiII1 )
   else :
    wiz . log ( 'Addon data for %s was not removed' % addon )
 wiz . refresh ( )
 if 37 - 37: O0 + OOoooooO * iii11iiII
def IiIII1i1i1I1iII ( type ) :
 if type == 'build' :
  ooOO00oOOo000 = II1IIiiI1 ( 'restore' )
  if ooOO00oOOo000 == False : wiz . LogNotify ( "[COLOR %s]%s[/COLOR]" % ( oOOo0O00o , o0OOO ) , "[COLOR %s]Local Restore Cancelled[/COLOR]" % iIiIi11 ) ; return
 if not wiz . currSkin ( ) in [ 'skin.confluence' , 'skin.estuary' ] :
  wiz . skinToDefault ( )
 wiz . restoreLocal ( type )
 if 48 - 48: iii11iiII . iii11iiII + i11iIiiIii + oO0 % O0
def O0000 ( type ) :
 if type == 'build' :
  ooOO00oOOo000 = II1IIiiI1 ( 'restore' )
  if ooOO00oOOo000 == False : wiz . LogNotify ( "[COLOR %s]%s[/COLOR]" % ( oOOo0O00o , o0OOO ) , "[COLOR %s]External Restore Cancelled[/COLOR]" % iIiIi11 ) ; return
 wiz . restoreExternal ( type )
 if 32 - 32: o0o0Oo0oooo0
def I1I ( name ) :
 if wiz . workingURL ( I1I1i1I ) == True :
  if wiz . checkBuild ( name , 'url' ) :
   name , O0OOO0OOooo00 , OOOoO000 , oOOOO , Ii , Ii1ii111i1 , i1i1i1I , oOoo000 , IiIIiIIIiIii , OooOo00o , IiI11i1IIiiI , oOOo000oOoO0 = wiz . checkBuild ( name , 'all' )
   OooOo00o = 'Yes' if OooOo00o . lower ( ) == 'yes' else 'No'
   O00oo0oOoO00O = "[COLOR %s]Build Name:[/COLOR] [COLOR %s]%s[/COLOR][CR]" % ( iIiIi11 , oOOo0O00o , name )
   O00oo0oOoO00O += "[COLOR %s]Build Version:[/COLOR] [COLOR %s]%s[/COLOR][CR]" % ( iIiIi11 , oOOo0O00o , O0OOO0OOooo00 )
   if not Ii1ii111i1 == "http://" :
    o0oO0oo = wiz . themeCount ( name , False )
    O00oo0oOoO00O += "[COLOR %s]Build Theme(s):[/COLOR] [COLOR %s]%s[/COLOR][CR]" % ( iIiIi11 , oOOo0O00o , ', ' . join ( o0oO0oo ) )
   O00oo0oOoO00O += "[COLOR %s]Kodi Version:[/COLOR] [COLOR %s]%s[/COLOR][CR]" % ( iIiIi11 , oOOo0O00o , Ii )
   O00oo0oOoO00O += "[COLOR %s]Adult Content:[/COLOR] [COLOR %s]%s[/COLOR][CR]" % ( iIiIi11 , oOOo0O00o , OooOo00o )
   O00oo0oOoO00O += "[COLOR %s]Description:[/COLOR] [COLOR %s]%s[/COLOR][CR]" % ( iIiIi11 , oOOo0O00o , IiI11i1IIiiI )
   wiz . TextBox ( o0OOO , O00oo0oOoO00O )
  else : wiz . log ( "Invalid Build Name!" )
 else : wiz . log ( "Build text file not working: %s" % WORKINGURL )
 if 98 - 98: OoooooooOO - ooOo + OOoooooO
def O0I11IIIII ( name ) :
 if wiz . workingURL ( I1I1i1I ) == True :
  OoO = wiz . checkBuild ( name , 'preview' )
  if OoO and not OoO == 'http://' : OooO00oo0O0 ( OoO )
  else : wiz . log ( "[%s]Unable to find url for video preview" % name )
 else : wiz . log ( "Build text file not working: %s" % WORKINGURL )
 if 18 - 18: Ooo0O - iii11iiII * II111iiii + IIIi1i1I
def O0oOOOO00oOOo ( plugin ) :
 o0o00OOOO = os . path . join ( O0O , plugin , 'addon.xml' )
 if os . path . exists ( o0o00OOOO ) :
  i1IiiiiIi1I = open ( o0o00OOOO , mode = 'r' ) ; o0O0Oo00 = i1IiiiiIi1I . read ( ) ; i1IiiiiIi1I . close ( ) ;
  O0Oo0o000oO = wiz . parseDOM ( o0O0Oo00 , 'import' , ret = 'addon' )
  iIIii1I111iIii1i1 = [ ]
  for ooo0O0o0OoOO in O0Oo0o000oO :
   if not 'xbmc.python' in ooo0O0o0OoOO :
    iIIii1I111iIii1i1 . append ( ooo0O0o0OoOO )
  return iIIii1I111iIii1i1
 return [ ]
 if 80 - 80: OO00O0O0O00Oo / i11iIiiIii + OoooooooOO
def III11i1iI11 ( do ) :
 if do == 'import' :
  o0o0OOo0O = os . path . join ( o0 , 'temp' )
  if not os . path . exists ( o0o0OOo0O ) : os . makedirs ( o0o0OOo0O )
  i1IiiiiIi1I = iiIIIII1i1iI . browse ( 1 , '[COLOR %s]Select the location of the SaveData.zip[/COLOR]' % iIiIi11 , 'files' , '.zip' , False , False , o00 )
  if not i1IiiiiIi1I . endswith ( '.zip' ) :
   wiz . LogNotify ( "[COLOR %s]%s[/COLOR]" % ( oOOo0O00o , o0OOO ) , "[COLOR %s]Import Data Error![/COLOR]" % ( iIiIi11 ) )
   return
  OOoO0ooOOOo0 = os . path . join ( O0ooO0Oo00o , 'SaveData.zip' )
  i11iIi1iIIIIi = xbmcvfs . copy ( i1IiiiiIi1I , OOoO0ooOOOo0 )
  wiz . log ( "%s" % str ( i11iIi1iIIIIi ) )
  extract . all ( xbmc . translatePath ( OOoO0ooOOOo0 ) , o0o0OOo0O )
  Ii1I1O0oo00oOOO0o = os . path . join ( o0o0OOo0O , 'trakt' )
  ooO00Oo = os . path . join ( o0o0OOo0O , 'login' )
  ooIi11iI = os . path . join ( o0o0OOo0O , 'debrid' )
  ooOO00oOOo000 = 0
  if os . path . exists ( Ii1I1O0oo00oOOO0o ) :
   ooOO00oOOo000 += 1
   o0oOOO = os . listdir ( Ii1I1O0oo00oOOO0o )
   if not os . path . exists ( traktit . TRAKTFOLD ) : os . makedirs ( traktit . TRAKTFOLD )
   for ii1IIIIiI11 in o0oOOO :
    IIi11 = os . path . join ( traktit . TRAKTFOLD , ii1IIIIiI11 )
    iiI1ii = os . path . join ( Ii1I1O0oo00oOOO0o , ii1IIIIiI11 )
    if os . path . exists ( IIi11 ) :
     if not iiIIIII1i1iI . yesno ( o0OOO , "[COLOR %s]Would you like replace the current [COLOR %s]%s[/COLOR] file?" % ( iIiIi11 , oOOo0O00o , ii1IIIIiI11 ) , yeslabel = "[B][COLOR green]Yes Replace[/COLOR][/B]" , nolabel = "[B][COLOR red]No Skip[/COLOR][/B]" ) : continue
     else : os . remove ( IIi11 )
    shutil . copy ( iiI1ii , IIi11 )
   traktit . importlist ( 'all' )
   traktit . traktIt ( 'restore' , 'all' )
  if os . path . exists ( ooO00Oo ) :
   ooOO00oOOo000 += 1
   o0oOOO = os . listdir ( ooO00Oo )
   if not os . path . exists ( loginit . LOGINFOLD ) : os . makedirs ( loginit . LOGINFOLD )
   for ii1IIIIiI11 in o0oOOO :
    IIi11 = os . path . join ( loginit . LOGINFOLD , ii1IIIIiI11 )
    iiI1ii = os . path . join ( ooO00Oo , ii1IIIIiI11 )
    if os . path . exists ( IIi11 ) :
     if not iiIIIII1i1iI . yesno ( o0OOO , "[COLOR %s]Would you like replace the current [COLOR %s]%s[/COLOR] file?" % ( iIiIi11 , oOOo0O00o , ii1IIIIiI11 ) , yeslabel = "[B][COLOR green]Yes Replace[/COLOR][/B]" , nolabel = "[B][COLOR red]No Skip[/COLOR][/B]" ) : continue
     else : os . remove ( IIi11 )
    shutil . copy ( iiI1ii , IIi11 )
   loginit . importlist ( 'all' )
   loginit . loginIt ( 'restore' , 'all' )
  if os . path . exists ( ooIi11iI ) :
   ooOO00oOOo000 += 1
   o0oOOO = os . listdir ( ooIi11iI )
   if not os . path . exists ( debridit . REALFOLD ) : os . makedirs ( debridit . REALFOLD )
   for ii1IIIIiI11 in o0oOOO :
    IIi11 = os . path . join ( debridit . REALFOLD , ii1IIIIiI11 )
    iiI1ii = os . path . join ( ooIi11iI , ii1IIIIiI11 )
    if os . path . exists ( IIi11 ) :
     if not iiIIIII1i1iI . yesno ( o0OOO , "[COLOR %s]Would you like replace the current [COLOR %s]%s[/COLOR] file?" % ( iIiIi11 , oOOo0O00o , ii1IIIIiI11 ) , yeslabel = "[B][COLOR green]Yes Replace[/COLOR][/B]" , nolabel = "[B][COLOR red]No Skip[/COLOR][/B]" ) : continue
     else : os . remove ( IIi11 )
    shutil . copy ( iiI1ii , IIi11 )
   debridit . importlist ( 'all' )
   debridit . debridIt ( 'restore' , 'all' )
  wiz . cleanHouse ( o0o0OOo0O )
  wiz . removeFolder ( o0o0OOo0O )
  os . remove ( OOoO0ooOOOo0 )
  if ooOO00oOOo000 == 0 : wiz . LogNotify ( "[COLOR %s]%s[/COLOR]" % ( oOOo0O00o , o0OOO ) , "[COLOR %s]Save Data Import Failed[/COLOR]" % iIiIi11 )
  else : wiz . LogNotify ( "[COLOR %s]%s[/COLOR]" % ( oOOo0O00o , o0OOO ) , "[COLOR %s]Save Data Import Complete[/COLOR]" % iIiIi11 )
 elif do == 'export' :
  O0OOO = xbmc . translatePath ( O0ooO0Oo00o )
  dir = [ traktit . TRAKTFOLD , debridit . REALFOLD , loginit . LOGINFOLD ]
  traktit . traktIt ( 'update' , 'all' )
  loginit . loginIt ( 'update' , 'all' )
  debridit . debridIt ( 'update' , 'all' )
  i1IiiiiIi1I = iiIIIII1i1iI . browse ( 3 , '[COLOR %s]Select where you wish to export the savedata zip?[/COLOR]' % iIiIi11 , 'files' , '' , False , True , o00 )
  i1IiiiiIi1I = xbmc . translatePath ( i1IiiiiIi1I )
  iii1iII1I = os . path . join ( O0OOO , 'SaveData.zip' )
  i1Ii11iiIi11IIIi1 = zipfile . ZipFile ( iii1iII1I , mode = 'w' )
  for I1oo in dir :
   if os . path . exists ( I1oo ) :
    o0oOOO = os . listdir ( I1oo )
    for file in o0oOOO :
     i1Ii11iiIi11IIIi1 . write ( os . path . join ( I1oo , file ) , os . path . join ( I1oo , file ) . replace ( o0 , '' ) , zipfile . ZIP_DEFLATED )
  i1Ii11iiIi11IIIi1 . close ( )
  if i1IiiiiIi1I == O0OOO :
   iiIIIII1i1iI . ok ( o0OOO , "[COLOR %s]Save data has been backed up to:[/COLOR]" % ( iIiIi11 ) , "[COLOR %s]%s[/COLOR]" % ( oOOo0O00o , iii1iII1I ) )
  else :
   try :
    xbmcvfs . copy ( iii1iII1I , os . path . join ( i1IiiiiIi1I , 'SaveData.zip' ) )
    iiIIIII1i1iI . ok ( o0OOO , "[COLOR %s]Save data has been backed up to:[/COLOR]" % ( iIiIi11 ) , "[COLOR %s]%s[/COLOR]" % ( oOOo0O00o , os . path . join ( i1IiiiiIi1I , 'SaveData.zip' ) ) )
   except :
    iiIIIII1i1iI . ok ( o0OOO , "[COLOR %s]Save data has been backed up to:[/COLOR]" % ( iIiIi11 ) , "[COLOR %s]%s[/COLOR]" % ( oOOo0O00o , iii1iII1I ) )
    if 93 - 93: i11iIiiIii . I1I1i1
def o0OO ( url ) :
 I1iI = urllib2 . Request ( url )
 I1iI . add_header ( 'User-Agent' , 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3' )
 oO0Ooo0OooOOo = urllib2 . urlopen ( I1iI )
 o0O0Oo00 = oO0Ooo0OooOOo . read ( )
 oO0Ooo0OooOOo . close ( )
 return o0O0Oo00
 if 16 - 16: i1IIi . i1IIi / OO00O0O0O00Oo % o0o0Oo0oooo0 / ooOo * oO0
def IIIii11 ( url ) :
 if url == 'http://' : return False
 try :
  I1iI = urllib2 . Request ( url )
  I1iI . add_header ( 'User-Agent' , USER_AGENT )
  oO0Ooo0OooOOo = urllib2 . urlopen ( I1iI )
  oO0Ooo0OooOOo . close ( )
 except Exception , ii1i1i :
  return ii1i1i
 return True
 if 29 - 29: IiiIII111ii - IiiIII111ii / OOoooooO
 if 49 - 49: i11IiIiiIIIII + IIIi1i1I % I1111 - Ooo0O - O0 - OoooooooOO
 if 4 - 4: II111iiii - IIIi1i1I % Ooo0O * i11iIiiIii
 if 18 - 18: Ooo0O % O0
def II1IIiiI1 ( install = None , over = False ) :
 if o0O0OOO0Ooo == 'true' :
  traktit . autoUpdate ( 'all' )
  wiz . setS ( 'traktlastsave' , str ( I1IiiiiI ) )
 if iiIiII1 == 'true' :
  debridit . autoUpdate ( 'all' )
  wiz . setS ( 'debridlastsave' , str ( I1IiiiiI ) )
 if OOO00O0O == 'true' :
  loginit . autoUpdate ( 'all' )
  wiz . setS ( 'loginlastsave' , str ( I1IiiiiI ) )
 if over == True : o0oOOOOoo0 = 1
 elif install == 'restore' : o0oOOOOoo0 = iiIIIII1i1iI . yesno ( o0OOO , "[COLOR %s]Do you wish to restore your" % iIiIi11 , "Kodi configuration to default settings" , "Before installing the local backup?[/COLOR]" , nolabel = '[B][COLOR red]No, Cancel[/COLOR][/B]' , yeslabel = '[B][COLOR green]Continue[/COLOR][/B]' )
 elif install : o0oOOOOoo0 = iiIIIII1i1iI . yesno ( o0OOO , "[COLOR %s]Do you wish to restore your" % iIiIi11 , "Kodi configuration to default settings" , "Before installing [COLOR %s]%s[/COLOR]?" % ( oOOo0O00o , install ) , nolabel = '[B][COLOR red]No, Cancel[/COLOR][/B]' , yeslabel = '[B][COLOR green]Continue[/COLOR][/B]' )
 else : o0oOOOOoo0 = iiIIIII1i1iI . yesno ( o0OOO , "[COLOR %s]Do you wish to restore your" % iIiIi11 , "Kodi configuration to default settings?[/COLOR]" , nolabel = '[B][COLOR red]No, Cancel[/COLOR][/B]' , yeslabel = '[B][COLOR green]Continue[/COLOR][/B]' )
 if o0oOOOOoo0 :
  if not wiz . currSkin ( ) in [ 'skin.confluence' , 'skin.estuary' ] :
   iIi1i1i1II11I = 'skin.confluence' if o0OIiII < 17 else 'skin.estuary'
   if 66 - 66: iIii1I11I1II1 % i11iIiiIii / ooOo
   if 47 - 47: oO0 * IIIi1i1I + iIii1I11I1II1 - IIIi1i1I / i1Ii
   skinSwitch . swapSkins ( iIi1i1i1II11I )
   ooOO00oOOo000 = 0
   xbmc . sleep ( 1000 )
   while not xbmc . getCondVisibility ( "Window.isVisible(yesnodialog)" ) and ooOO00oOOo000 < 150 :
    ooOO00oOOo000 += 1
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
  oO0ooo0O0Ooo = os . path . abspath ( o00 )
  oo00 . create ( o0OOO , "[COLOR %s]Calculating files and folders" % iIiIi11 , '' , 'Please Wait![/COLOR]' )
  iiI111i1 = sum ( [ len ( o0oOOO ) for IiIii11i1IIiI , I11iIIi , o0oOOO in os . walk ( oO0ooo0O0Ooo ) ] ) ; ii1i1I1 = 0
  oo00 . update ( 0 , "[COLOR %s]Gathering Excludes list." % iIiIi11 )
  Iii1I1I11iiI1 . append ( 'My_Builds' )
  Iii1I1I11iiI1 . append ( 'archive_cache' )
  if IIII == 'true' :
   iIiI1 = glob . glob ( os . path . join ( O0O , 'repo*/' ) )
   for ii1IIIIiI11 in iIiI1 :
    Oo0o0ooO0ooo = os . path . split ( ii1IIIIiI11 [ : - 1 ] ) [ 1 ]
    if not Oo0o0ooO0ooo == Iii1I1I11iiI1 :
     Iii1I1I11iiI1 . append ( Oo0o0ooO0ooo )
  if iiIiI == 'true' :
   Iii1I1I11iiI1 . append ( 'plugin.program.super.favourites' )
  if o00oooO0Oo == 'true' :
   i111IIiIII1i = ''
   I1111ii11IIII = wiz . whiteList ( 'read' )
   if len ( I1111ii11IIII ) > 0 :
    for ii1IIIIiI11 in I1111ii11IIII :
     try : oO0o00oOOooO0 , id , I1oo = ii1IIIIiI11
     except : pass
     if I1oo . startswith ( 'pvr' ) : i111IIiIII1i = id
     ooo0O0o0OoOO = O0oOOOO00oOOo ( I1oo )
     for oooO0 in ooo0O0o0OoOO :
      if not oooO0 in Iii1I1I11iiI1 :
       Iii1I1I11iiI1 . append ( oooO0 )
      Oo0oiiiiII11iIi = O0oOOOO00oOOo ( oooO0 )
      for OO00 in Oo0oiiiiII11iIi :
       if not OO00 in Iii1I1I11iiI1 :
        Iii1I1I11iiI1 . append ( OO00 )
     if not I1oo in Iii1I1I11iiI1 :
      Iii1I1I11iiI1 . append ( I1oo )
    if not i111IIiIII1i == '' : wiz . setS ( 'pvrclient' , I1oo )
  if wiz . getS ( 'pvrclient' ) == '' :
   for ii1IIIIiI11 in Iii1I1I11iiI1 :
    if ii1IIIIiI11 . startswith ( 'pvr' ) :
     wiz . setS ( 'pvrclient' , ii1IIIIiI11 )
  oo00 . update ( 0 , "[COLOR %s]Clearing out files and folders:" % iIiIi11 )
  Oooo = wiz . latestDB ( 'Addons' )
  for O00 , IiIIIIi , o0oOOO in os . walk ( oO0ooo0O0Ooo , topdown = True ) :
   IiIIIIi [ : ] = [ I11iIIi for I11iIIi in IiIIIIi if I11iIIi not in Iii1I1I11iiI1 ]
   for oO0o00oOOooO0 in o0oOOO :
    ii1i1I1 += 1
    I1oo = O00 . replace ( '/' , '\\' ) . split ( '\\' )
    ooOO00oOOo000 = len ( I1oo ) - 1
    if oO0o00oOOooO0 == 'sources.xml' and I1oo [ - 1 ] == 'userdata' and ooOOoooooo == 'true' : wiz . log ( "Keep Sources: %s" % os . path . join ( O00 , oO0o00oOOooO0 ) , xbmc . LOGNOTICE )
    elif oO0o00oOOooO0 == 'favourites.xml' and I1oo [ - 1 ] == 'userdata' and IiIIIi1iIi == 'true' : wiz . log ( "Keep Favourites: %s" % os . path . join ( O00 , oO0o00oOOooO0 ) , xbmc . LOGNOTICE )
    elif oO0o00oOOooO0 == 'profiles.xml' and I1oo [ - 1 ] == 'userdata' and II1I == 'true' : wiz . log ( "Keep Profiles: %s" % os . path . join ( O00 , oO0o00oOOooO0 ) , xbmc . LOGNOTICE )
    elif oO0o00oOOooO0 == 'advancedsettings.xml' and I1oo [ - 1 ] == 'userdata' and O0i1II1Iiii1I11 == 'true' : wiz . log ( "Keep Advanced Settings: %s" % os . path . join ( O00 , oO0o00oOOooO0 ) , xbmc . LOGNOTICE )
    elif oO0o00oOOooO0 in Ooo0oOooo0 : wiz . log ( "Keep Log File: %s" % oO0o00oOOooO0 , xbmc . LOGNOTICE )
    elif oO0o00oOOooO0 . endswith ( '.db' ) :
     try :
      if oO0o00oOOooO0 == Oooo and o0OIiII >= 17 : wiz . log ( "Ignoring %s on v%s" % ( oO0o00oOOooO0 , o0OIiII ) , xbmc . LOGNOTICE )
      else : os . remove ( os . path . join ( O00 , oO0o00oOOooO0 ) )
     except Exception , ii1i1i :
      if not oO0o00oOOooO0 . startswith ( 'Textures13' ) :
       wiz . log ( 'Failed to delete, Purging DB' , xbmc . LOGNOTICE )
       wiz . log ( "-> %s" % ( str ( ii1i1i ) ) , xbmc . LOGNOTICE )
       wiz . purgeDb ( os . path . join ( O00 , oO0o00oOOooO0 ) )
    else :
     oo00 . update ( int ( wiz . percentage ( ii1i1I1 , iiI111i1 ) ) , '' , '[COLOR %s]File: [/COLOR][COLOR %s]%s[/COLOR]' % ( iIiIi11 , oOOo0O00o , oO0o00oOOooO0 ) , '' )
     try : os . remove ( os . path . join ( O00 , oO0o00oOOooO0 ) )
     except Exception , ii1i1i :
      wiz . log ( "Error removing %s" % os . path . join ( O00 , oO0o00oOOooO0 ) , xbmc . LOGNOTICE )
      wiz . log ( "-> / %s" % ( str ( ii1i1i ) ) , xbmc . LOGNOTICE )
   if oo00 . iscanceled ( ) :
    oo00 . close ( )
    wiz . LogNotify ( "[COLOR %s]%s[/COLOR]" % ( oOOo0O00o , o0OOO ) , "[COLOR %s]Fresh Start Cancelled[/COLOR]" % iIiIi11 )
    return False
  for O00 , IiIIIIi , o0oOOO in os . walk ( oO0ooo0O0Ooo , topdown = True ) :
   IiIIIIi [ : ] = [ I11iIIi for I11iIIi in IiIIIIi if I11iIIi not in Iii1I1I11iiI1 ]
   for oO0o00oOOooO0 in IiIIIIi :
    oo00 . update ( 100 , '' , 'Cleaning Up Empty Folder: [COLOR %s]%s[/COLOR]' % ( oOOo0O00o , oO0o00oOOooO0 ) , '' )
    if oO0o00oOOooO0 not in [ "Database" , "userdata" , "temp" , "addons" , "addon_data" ] :
     shutil . rmtree ( os . path . join ( O00 , oO0o00oOOooO0 ) , ignore_errors = True , onerror = None )
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
   I111 ( install , 'normal' , over = True )
  else :
   if I11i1I1I == 1 : o0OOo = 1
   elif I11i1I1I == 2 : o0OOo = 0
   else : o0OOo = iiIIIII1i1iI . yesno ( o0OOO , "[COLOR %s]Would you like to [COLOR %s]Force close[/COLOR] kodi or [COLOR %s]Reload Profile[/COLOR]?[/COLOR]" % ( iIiIi11 , oOOo0O00o , oOOo0O00o ) , yeslabel = "[B][COLOR red]Reload Profile[/COLOR][/B]" , nolabel = "[B][COLOR green]Force Close[/COLOR][/B]" )
   if o0OOo == 1 : wiz . reloadFix ( 'fresh' )
   else : wiz . addonUpdates ( 'reset' ) ; wiz . killxbmc ( True )
 else :
  if not install == 'restore' :
   wiz . LogNotify ( "[COLOR %s]%s[/COLOR]" % ( oOOo0O00o , o0OOO ) , '[COLOR %s]Fresh Install: Cancelled![/COLOR]' % iIiIi11 )
   wiz . refresh ( )
   if 51 - 51: II111iiii . IIIi1i1I . I1111 % II111iiii
   if 41 - 41: o0o0Oo0oooo0 - iii11iiII + OOoooooO - i1IIi
   if 6 - 6: II111iiii
   if 7 - 7: i1IIi
def Oo00oo ( ) :
 if iiIIIII1i1iI . yesno ( o0OOO , '[COLOR %s]Would you like to clear cache?[/COLOR]' % iIiIi11 , nolabel = '[B][COLOR red]No, Cancel[/COLOR][/B]' , yeslabel = '[B][COLOR green]Clear Cache[/COLOR][/B]' ) :
  wiz . clearCache ( )
  if 79 - 79: oO0 / O0 % I1I1i1
  if 71 - 71: OO00O0O0O00Oo / ooOo / O0
def IiIii11I ( ) :
 if iiIIIII1i1iI . yesno ( o0OOO , '[COLOR %s]Would you like to clear cache, packages and thumbnails?[/COLOR]' % iIiIi11 , nolabel = '[B][COLOR red]Cancel Process[/COLOR][/B]' , yeslabel = '[B][COLOR green]Clean All[/COLOR][/B]' ) :
  wiz . clearCache ( )
  wiz . clearPackages ( 'total' )
  Ooo0O00 ( 'total' )
  if 53 - 53: O0 . ooOo
def Ooo0O00 ( type = None ) :
 o0oOOoO000 = wiz . latestDB ( 'Textures' )
 if not type == None : Ii1I1 = 1
 else : Ii1I1 = iiIIIII1i1iI . yesno ( o0OOO , '[COLOR %s]Would you like to delete the %s and Thumbnails folder?' % ( iIiIi11 , o0oOOoO000 ) , "They will repopulate on the next startup[/COLOR]" , nolabel = '[B][COLOR red]Don\'t Delete[/COLOR][/B]' , yeslabel = '[B][COLOR green]Delete Thumbs[/COLOR][/B]' )
 if Ii1I1 == 1 :
  try : wiz . removeFile ( os . join ( OOOO , o0oOOoO000 ) )
  except : wiz . log ( 'Failed to delete, Purging DB.' ) ; wiz . purgeDb ( o0oOOoO000 )
  wiz . removeFolder ( oOoOooOo0o0 )
  if 86 - 86: iIii1I11I1II1 - i11IiIiiIIIII % OOoooooO . iii11iiII * o0o0Oo0oooo0 . i1IIi
 else : wiz . log ( 'Clear thumbnames cancelled' )
 wiz . redoThumbs ( )
 if 75 - 75: i11IiIiiIIIII + OOoooooO / OOoooooO - iii11iiII * I1111 * OOoooooO
def o0OO0ooOOO ( ) :
 i1i1I1Ii1IIii = [ ] ; iIi = [ ]
 for oooOOoo , iI1iii1iIiiI , o0oOOO in os . walk ( o00 ) :
  for OooOO0oOOo0O in fnmatch . filter ( o0oOOO , '*.db' ) :
   if OooOO0oOOo0O != 'Thumbs.db' :
    II1iiiiI1 = os . path . join ( oooOOoo , OooOO0oOOo0O )
    i1i1I1Ii1IIii . append ( II1iiiiI1 )
    dir = II1iiiiI1 . replace ( '\\' , '/' ) . split ( '/' )
    iIi . append ( '(%s) %s' % ( dir [ len ( dir ) - 2 ] , dir [ len ( dir ) - 1 ] ) )
 if o0OIiII >= 16 :
  Ii1I1 = iiIIIII1i1iI . multiselect ( "[COLOR %s]Select DB File to Purge[/COLOR]" % iIiIi11 , iIi )
  if Ii1I1 == None : wiz . LogNotify ( "[COLOR %s]Purge Database[/COLOR]" % oOOo0O00o , "[COLOR %s]Cancelled[/COLOR]" % iIiIi11 )
  elif len ( Ii1I1 ) == 0 : wiz . LogNotify ( "[COLOR %s]Purge Database[/COLOR]" % oOOo0O00o , "[COLOR %s]Cancelled[/COLOR]" % iIiIi11 )
  else :
   for IiiIiiIIII in Ii1I1 : wiz . purgeDb ( i1i1I1Ii1IIii [ IiiIiiIIII ] )
 else :
  Ii1I1 = iiIIIII1i1iI . select ( "[COLOR %s]Select DB File to Purge[/COLOR]" % iIiIi11 , iIi )
  if Ii1I1 == - 1 : wiz . LogNotify ( "[COLOR %s]Purge Database[/COLOR]" % oOOo0O00o , "[COLOR %s]Cancelled[/COLOR]" % iIiIi11 )
  else : wiz . purgeDb ( i1i1I1Ii1IIii [ IiiIiiIIII ] )
  if 88 - 88: I1111 . OO00O0O0O00Oo / i11IiIiiIIIII
  if 47 - 47: I1111 + oO0 . OOoooooO
  if 43 - 43: ooOo - I1I1i1 / I1I1i1 . II111iiii - IiiIII111ii
  if 40 - 40: iiIIi1IiIi11 . o0o0Oo0oooo0 * O0
def IIiiIii11 ( ) :
 OOOoO000 = wiz . workingURL ( O0O0OOOOoo )
 if OOOoO000 == True :
  try :
   id , O00oo0oOoO00O = wiz . splitNotify ( O0O0OOOOoo )
   if id == False : wiz . LogNotify ( "[COLOR %s]%s[/COLOR]" % ( oOOo0O00o , o0OOO ) , "[COLOR %s]Notification: Not Formated Correctly[/COLOR]" % iIiIi11 ) ; return
   notify . notification ( O00oo0oOoO00O , True )
  except Exception , ii1i1i :
   wiz . log ( "Error on Notifications Window: %s" % str ( ii1i1i ) , xbmc . LOGERROR )
 else : wiz . LogNotify ( "[COLOR %s]%s[/COLOR]" % ( oOOo0O00o , o0OOO ) , "[COLOR %s]Invalid URL for Notification[/COLOR]" % iIiIi11 )
 if 74 - 74: i1IIi
def Ii11ii1 ( ) :
 if O000oo0O == "" :
  notify . updateWindow ( )
 else :
  notify . updateWindow ( O000oo0O , oo0OooOOo0 , O00oO , wiz . checkBuild ( O000oo0O , 'icon' ) , wiz . checkBuild ( O000oo0O , 'fanart' ) )
  if 1 - 1: iIii1I11I1II1 % IIIi1i1I . iIii1I11I1II1
def i1IiiI1 ( ) :
 notify . firstRun ( )
 if 83 - 83: iiIIi1IiIi11 - i1Ii % I1111 - OoooooooOO - iii11iiII % OoooooooOO
def Oo00O0O ( ) :
 notify . firstRunSettings ( )
 if 70 - 70: I1111
 if 43 - 43: o0o0Oo0oooo0
 if 57 - 57: ooOo
 if 65 - 65: i11iIiiIii - OOoooooO * i11IiIiiIIIII + OOoooooO / i1Ii + I1I1i1
 if 35 - 35: O0 + Ooo0O - ooOo % IiiIII111ii % II111iiii
def o0OOOO ( display , mode = None , name = None , url = None , menu = None , description = o0OOO , overwrite = True , fanart = OOO00 , icon = iiiiiIIii , themeit = None ) :
 OOoo0OOOo0o = sys . argv [ 0 ]
 if not mode == None : OOoo0OOOo0o += "?mode=%s" % urllib . quote_plus ( mode )
 if not name == None : OOoo0OOOo0o += "&name=" + urllib . quote_plus ( name )
 if not url == None : OOoo0OOOo0o += "&url=" + urllib . quote_plus ( url )
 iI1111i1i11Ii = True
 if themeit : display = themeit % display
 oo0O00o0O0Oo = xbmcgui . ListItem ( display , iconImage = "DefaultFolder.png" , thumbnailImage = icon )
 oo0O00o0O0Oo . setInfo ( type = "Video" , infoLabels = { "Title" : display , "Plot" : description } )
 oo0O00o0O0Oo . setProperty ( "Fanart_Image" , fanart )
 if not menu == None : oo0O00o0O0Oo . addContextMenuItems ( menu , replaceItems = overwrite )
 iI1111i1i11Ii = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = OOoo0OOOo0o , listitem = oo0O00o0O0Oo , isFolder = True )
 return iI1111i1i11Ii
 if 26 - 26: i1IIi / iiIIi1IiIi11 . iiIIi1IiIi11
def I1i11IIIi ( name , url , mode , iconimage , fanart , description ) :
 if 19 - 19: IIIi1i1I * iiIIi1IiIi11 + o0o0Oo0oooo0 - IIIi1i1I + oO0
 OOoo0OOOo0o = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart ) + "&description=" + urllib . quote_plus ( description )
 iI1111i1i11Ii = True
 oo0O00o0O0Oo = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 oo0O00o0O0Oo . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description } )
 oo0O00o0O0Oo . setProperty ( "Fanart_Image" , fanart )
 iI1111i1i11Ii = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = OOoo0OOOo0o , listitem = oo0O00o0O0Oo , isFolder = False )
 if 14 - 14: I1111
def oo00O00oO000o ( display , mode = None , name = None , url = None , menu = None , description = o0OOO , overwrite = True , fanart = OOO00 , icon = iiiiiIIii , themeit = None ) :
 OOoo0OOOo0o = sys . argv [ 0 ]
 if not mode == None : OOoo0OOOo0o += "?mode=%s" % urllib . quote_plus ( mode )
 if not name == None : OOoo0OOOo0o += "&name=" + urllib . quote_plus ( name )
 if not url == None : OOoo0OOOo0o += "&url=" + urllib . quote_plus ( url )
 iI1111i1i11Ii = True
 if themeit : display = themeit % display
 oo0O00o0O0Oo = xbmcgui . ListItem ( display , iconImage = "DefaultFolder.png" , thumbnailImage = icon )
 oo0O00o0O0Oo . setInfo ( type = "Video" , infoLabels = { "Title" : display , "Plot" : description } )
 oo0O00o0O0Oo . setProperty ( "Fanart_Image" , fanart )
 if not menu == None : oo0O00o0O0Oo . addContextMenuItems ( menu , replaceItems = overwrite )
 iI1111i1i11Ii = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = OOoo0OOOo0o , listitem = oo0O00o0O0Oo , isFolder = True )
 return iI1111i1i11Ii
 if 38 - 38: O0
def iiiii1II ( display , mode = None , name = None , url = None , menu = None , description = o0OOO , overwrite = True , fanart = OOO00 , icon = iiiiiIIii , themeit = None ) :
 OOoo0OOOo0o = sys . argv [ 0 ]
 if not mode == None : OOoo0OOOo0o += "?mode=%s" % urllib . quote_plus ( mode )
 if not name == None : OOoo0OOOo0o += "&name=" + urllib . quote_plus ( name )
 if not url == None : OOoo0OOOo0o += "&url=" + urllib . quote_plus ( url )
 iI1111i1i11Ii = True
 if themeit : display = themeit % display
 oo0O00o0O0Oo = xbmcgui . ListItem ( display , iconImage = "DefaultFolder.png" , thumbnailImage = icon )
 oo0O00o0O0Oo . setInfo ( type = "Video" , infoLabels = { "Title" : display , "Plot" : description } )
 oo0O00o0O0Oo . setProperty ( "Fanart_Image" , fanart )
 if not menu == None : oo0O00o0O0Oo . addContextMenuItems ( menu , replaceItems = overwrite )
 iI1111i1i11Ii = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = OOoo0OOOo0o , listitem = oo0O00o0O0Oo , isFolder = False )
 return iI1111i1i11Ii
 if 79 - 79: i1IIi . IIIi1i1I
def o0Ooo0O00 ( name , url , mode , iconimage ) :
 OOoo0OOOo0o = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage )
 iI1111i1i11Ii = True
 oo0O00o0O0Oo = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 oo0O00o0O0Oo . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : name } )
 iI1111i1i11Ii = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = OOoo0OOOo0o , listitem = oo0O00o0O0Oo , isFolder = True )
 return iI1111i1i11Ii
 if 34 - 34: OO00O0O0O00Oo * II111iiii
def oooO00o0 ( name , url , mode , iconimage , fanart , description , installRating ) :
 OOoo0OOOo0o = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart ) + "&description=" + urllib . quote_plus ( description ) + "&installRating=" + urllib . quote_plus ( installRating )
 iI1111i1i11Ii = True
 oo0O00o0O0Oo = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 oo0O00o0O0Oo . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description , "Premiered" : installRating } )
 oo0O00o0O0Oo . setProperty ( "Fanart_Image" , fanart )
 iI1111i1i11Ii = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = OOoo0OOOo0o , listitem = oo0O00o0O0Oo , isFolder = False )
 return iI1111i1i11Ii
 if 71 - 71: i1Ii
def o00OOo0o ( display , mode = None , name = None , url = None , menu = None , description = o0OOO , overwrite = True , fanart = OOO00 , icon = iiiiiIIii , themeit = None ) :
 OOoo0OOOo0o = sys . argv [ 0 ]
 if not mode == None : OOoo0OOOo0o += "?mode=%s" % urllib . quote_plus ( mode )
 if not name == None : OOoo0OOOo0o += "&name=" + urllib . quote_plus ( name )
 if not url == None : OOoo0OOOo0o += "&url=" + urllib . quote_plus ( url )
 iI1111i1i11Ii = True
 if themeit : display = themeit % display
 oo0O00o0O0Oo = xbmcgui . ListItem ( display , iconImage = "DefaultFolder.png" , thumbnailImage = icon )
 oo0O00o0O0Oo . setInfo ( type = "Video" , infoLabels = { "Title" : display , "Plot" : description } )
 oo0O00o0O0Oo . setProperty ( "Fanart_Image" , fanart )
 if not menu == None : oo0O00o0O0Oo . addContextMenuItems ( menu , replaceItems = overwrite )
 iI1111i1i11Ii = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = OOoo0OOOo0o , listitem = oo0O00o0O0Oo , isFolder = False )
 return iI1111i1i11Ii
 if 48 - 48: i11iIiiIii / II111iiii + IiiIII111ii + I1I1i1 . OO00O0O0O00Oo % iii11iiII
def II1 ( display , mode , name = None , url = None , menu = None , overwrite = True , fanart = OOO00 , icon = iiiiiIIii , description = None , themeit = None ) :
 OOoo0OOOo0o = '%s?mode=%s' % ( sys . argv [ 0 ] , urllib . quote_plus ( mode ) )
 if not name == None : OOoo0OOOo0o += "&name=" + urllib . quote_plus ( name )
 if not url == None : OOoo0OOOo0o += "&url=" + urllib . quote_plus ( url )
 if not description == None : OOoo0OOOo0o += "&description=" + urllib . quote_plus ( description )
 iI1111i1i11Ii = True
 if themeit : display = themeit % display
 oo0O00o0O0Oo = xbmcgui . ListItem ( description , iconImage = "DefaultFolder.png" , thumbnailImage = icon )
 oo0O00o0O0Oo . setInfo ( type = "Video" , infoLabels = { "Title" : description , "Plot" : o0OOO } )
 oo0O00o0O0Oo . setProperty ( "Fanart_Image" , fanart )
 if not menu == None : oo0O00o0O0Oo . addContextMenuItems ( menu , replaceItems = overwrite )
 iI1111i1i11Ii = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = OOoo0OOOo0o , listitem = oo0O00o0O0Oo , isFolder = False )
 return iI1111i1i11Ii
 if 88 - 88: OO00O0O0O00Oo . OO00O0O0O00Oo
def O0OoO0oooOO ( name , url , mode , iconimage , fanart , description ) :
 OOoo0OOOo0o = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&fanart=" + urllib . quote_plus ( fanart )
 iI1111i1i11Ii = True
 oo0O00o0O0Oo = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 oo0O00o0O0Oo . setInfo ( type = "Video" , infoLabels = { "Title" : name } )
 oo0O00o0O0Oo . setProperty ( "Fanart_Image" , fanart )
 iI1111i1i11Ii = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = OOoo0OOOo0o , listitem = oo0O00o0O0Oo , isFolder = False )
 return iI1111i1i11Ii
 if 44 - 44: OOoooooO * i11iIiiIii
def II111Ii11II ( name , url , mode , iconimage , fanart , description ) :
 if 14 - 14: OOoooooO * OoooooooOO + I1111
 OOoo0OOOo0o = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart ) + "&description=" + urllib . quote_plus ( description )
 iI1111i1i11Ii = True
 oo0O00o0O0Oo = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 oo0O00o0O0Oo . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description } )
 oo0O00o0O0Oo . setProperty ( "Fanart_Image" , fanart )
 iI1111i1i11Ii = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = OOoo0OOOo0o , listitem = oo0O00o0O0Oo , isFolder = True )
 return iI1111i1i11Ii
 if 6 - 6: i1IIi - i11IiIiiIIIII
 if 89 - 89: OOoooooO - i11IiIiiIIIII . O0 % OoooooooOO . i11iIiiIii
 if 35 - 35: II111iiii / o0o0Oo0oooo0 - O0 . II111iiii
def oO0o000oOO ( name , url , mode , iconimage , fanart , description ) :
 OOoo0OOOo0o = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart ) + "&description=" + urllib . quote_plus ( description )
 iI1111i1i11Ii = True
 oo0O00o0O0Oo = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 oo0O00o0O0Oo . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description } )
 oo0O00o0O0Oo . setProperty ( "Fanart_Image" , fanart )
 if mode == 90 :
  iI1111i1i11Ii = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = OOoo0OOOo0o , listitem = oo0O00o0O0Oo , isFolder = False )
 else :
  iI1111i1i11Ii = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = OOoo0OOOo0o , listitem = oo0O00o0O0Oo , isFolder = True )
 return iI1111i1i11Ii
 if 27 - 27: O0 - i11IiIiiIIIII * II111iiii - iIii1I11I1II1 / OOoooooO
def II1iOOoOooO0o ( ) :
 I1IiiiI = [ ]
 iIiI1111 = sys . argv [ 2 ]
 if len ( iIiI1111 ) >= 2 :
  O0OO00 = sys . argv [ 2 ]
  i1111I = O0OO00 . replace ( '?' , '' )
  if ( O0OO00 [ len ( O0OO00 ) - 1 ] == '/' ) :
   O0OO00 = O0OO00 [ 0 : len ( O0OO00 ) - 2 ]
  OoO00oo0 = i1111I . split ( '&' )
  I1IiiiI = { }
  for oO00oOOo0Oo in range ( len ( OoO00oo0 ) ) :
   oOOO = { }
   oOOO = OoO00oo0 [ oO00oOOo0Oo ] . split ( '=' )
   if ( len ( oOOO ) ) == 2 :
    I1IiiiI [ oOOO [ 0 ] ] = oOOO [ 1 ]
    if 62 - 62: IiiIII111ii - IIIi1i1I % iIii1I11I1II1
  return I1IiiiI
  if 57 - 57: OoooooooOO / o0o0Oo0oooo0
O0OO00 = II1iOOoOooO0o ( )
OOOoO000 = None
oO0o00oOOooO0 = None
iI1ii1iIiii1i = None
O00oOoo0OoO0 = None
oOoo000 = None
IiI11i1IIiiI = None
ooOooo00O = None
oOOo000oOoO0 = None
try :
 ooOooo00O = int ( O0OO00 [ "fav_mode" ] )
except :
 pass
try : iI1ii1iIiii1i = urllib . unquote_plus ( O0OO00 [ "mode" ] )
except : pass
try : oO0o00oOOooO0 = urllib . unquote_plus ( O0OO00 [ "name" ] )
except : pass
try : OOOoO000 = urllib . unquote_plus ( O0OO00 [ "url" ] )
except : pass
try : O00oOoo0OoO0 = urllib . unquote_plus ( O0OO00 [ "iconimage" ] )
except : pass
try : oOoo000 = urllib . unquote_plus ( O0OO00 [ "fanart" ] )
except : pass
try : IiI11i1IIiiI = urllib . unquote_plus ( O0OO00 [ "description" ] )
except : pass
if 5 - 5: i11IiIiiIIIII . II111iiii / i1Ii % i11IiIiiIIIII + IIIi1i1I
print "Mode: " + str ( iI1ii1iIiii1i )
print "URL: " + str ( OOOoO000 )
print "Name: " + str ( oO0o00oOOooO0 )
print "IconImage: " + str ( O00oOoo0OoO0 )
if 35 - 35: I1111
wiz . log ( '[ Version : \'%s\' ] [ Mode : \'%s\' ] [ Name : \'%s\' ] [ Url : \'%s\' ]' % ( O0oo0OO0 , iI1ii1iIiii1i if not iI1ii1iIiii1i == '' else None , oO0o00oOOooO0 , OOOoO000 ) )
if 52 - 52: Ooo0O / iiIIi1IiIi11
def Iii1IIII1Iii ( ) :
 if 94 - 94: IIIi1i1I . I1I1i1 % I1I1i1 % ooOo - iiIIi1IiIi11 / i11iIiiIii
 for file in os . listdir ( Ii11iii11I ) :
  if file . endswith ( ".zip" ) :
   OOOoO000 = xbmc . translatePath ( os . path . join ( Ii11iii11I , file ) )
   O0OoO0oooOO ( file , OOOoO000 , 'read' , iiiiiIIii , iiiiiIIii , '' )
   if 73 - 73: O0 * OO00O0O0O00Oo . i1IIi
def OO00OoOO ( ) :
 iiii1II1ii11 = xbmc . translatePath ( os . path . join ( 'special://' , 'home' ) )
 for file in os . listdir ( Ii11iii11I ) :
  if file . endswith ( ".zip" ) :
   OOOoO000 = xbmc . translatePath ( os . path . join ( Ii11iii11I , file ) )
   oO0o000oOO ( file , OOOoO000 , 'dell' , iiiiiIIii , iiiiiIIii , '' )
   if 37 - 37: OO00O0O0O00Oo - IIIi1i1I - I1111
def iIi1 ( content , viewType ) :
 if 42 - 42: iIii1I11I1II1 % IiiIII111ii - oO0 + iIii1I11I1II1
 if content :
  xbmcplugin . setContent ( int ( sys . argv [ 1 ] ) , content )
 if ADDON . getSetting ( 'auto-view' ) == 'true' :
  xbmc . executebuiltin ( "Container.SetViewMode(%s)" % ADDON . getSetting ( viewType ) )
  if 27 - 27: O0 / I1111
  if 99 - 99: IiiIII111ii - i1Ii * iIii1I11I1II1 . II111iiii
  if 56 - 56: iIii1I11I1II1 % I1111 . OOoooooO % i1Ii . OO00O0O0O00Oo * Ooo0O
  if 41 - 41: iIii1I11I1II1 % i1Ii * IIIi1i1I - OOoooooO
  if 5 - 5: I1111 + I1111 + II111iiii * iIii1I11I1II1 + OoooooooOO
  if 77 - 77: O0 * oO0 * IIIi1i1I + I1111 + oO0 - OO00O0O0O00Oo
  if 10 - 10: oO0 + i1Ii
def iIi1 ( content , viewType ) :
 if wiz . getS ( 'auto-view' ) == 'true' :
  Ooooo00 = wiz . getS ( viewType )
  if Ooooo00 == '50' and o0OIiII >= 17 and I1IIiiIiii == 'skin.estuary' : Ooooo00 = '55'
  if Ooooo00 == '500' and o0OIiII >= 17 and I1IIiiIiii == 'skin.estuary' : Ooooo00 = '50'
  wiz . ebi ( "Container.SetViewMode(%s)" % Ooooo00 )
  if 99 - 99: oO0 - IIIi1i1I
if iI1ii1iIiii1i == None : i1iiIiI1Ii1i ( )
if 10 - 10: II111iiii . I1111
elif iI1ii1iIiii1i == 'wizardupdate' : wiz . wizardUpdate ( )
elif iI1ii1iIiii1i == 'builds' : OoO00 ( )
elif iI1ii1iIiii1i == 'viewbuild' : OoOo00o0OO ( oO0o00oOOooO0 , oOOo000oOoO0 )
elif iI1ii1iIiii1i == 'buildinfo' : I1I ( oO0o00oOOooO0 )
elif iI1ii1iIiii1i == 'buildpreview' : O0I11IIIII ( oO0o00oOOooO0 )
elif iI1ii1iIiii1i == 'install' : I111 ( oO0o00oOOooO0 , OOOoO000 )
elif iI1ii1iIiii1i == 'theme' : I111 ( oO0o00oOOooO0 , oOOo000oOoO0 , iI1ii1iIiii1i , OOOoO000 )
elif iI1ii1iIiii1i == 'viewthirdparty' : OOoOO ( oO0o00oOOooO0 )
elif iI1ii1iIiii1i == 'installthird' : OOO00000o0 ( oO0o00oOOooO0 , OOOoO000 )
elif iI1ii1iIiii1i == 'editthird' : IIi1II ( oO0o00oOOooO0 ) ; wiz . refresh ( )
if 89 - 89: OOoooooO * IiiIII111ii
elif iI1ii1iIiii1i == 'pro' : Main_Menu ( )
if 93 - 93: i1IIi . IiiIII111ii * OO00O0O0O00Oo . OOoooooO
elif iI1ii1iIiii1i == 'maint' : I11I1ii1i ( oO0o00oOOooO0 )
elif iI1ii1iIiii1i == 'speed' : ii1IiIi11 ( )
elif iI1ii1iIiii1i == 'kodi17fix' : wiz . kodi17Fix ( )
elif iI1ii1iIiii1i == 'advancedsetting' : Iiii1I ( oO0o00oOOooO0 )
elif iI1ii1iIiii1i == 'autoadvanced' : I1ii1Ii1 ( ) ; wiz . refresh ( )
elif iI1ii1iIiii1i == 'removeadvanced' : i11IiI1I ( ) ; wiz . refresh ( )
elif iI1ii1iIiii1i == 'asciicheck' : wiz . asciiCheck ( )
elif iI1ii1iIiii1i == 'backupbuild' : wiz . backUpOptions ( 'build' )
elif iI1ii1iIiii1i == 'backupgui' : wiz . backUpOptions ( 'guifix' )
elif iI1ii1iIiii1i == 'backuptheme' : wiz . backUpOptions ( 'theme' )
elif iI1ii1iIiii1i == 'backupaddon' : wiz . backUpOptions ( 'addondata' )
elif iI1ii1iIiii1i == 'oldThumbs' : wiz . oldThumbs ( )
elif iI1ii1iIiii1i == 'clearbackup' : wiz . cleanupBackup ( )
elif iI1ii1iIiii1i == 'convertpath' : wiz . convertSpecial ( o00 )
elif iI1ii1iIiii1i == 'currentsettings' : Ii1III1 ( )
elif iI1ii1iIiii1i == 'fullclean' : IiIii11I ( ) ; wiz . refresh ( )
elif iI1ii1iIiii1i == 'clearcache' : Oo00oo ( ) ; wiz . refresh ( )
elif iI1ii1iIiii1i == 'clearpackages' : wiz . clearPackages ( ) ; wiz . refresh ( )
elif iI1ii1iIiii1i == 'clearcrash' : wiz . clearCrash ( ) ; wiz . refresh ( )
elif iI1ii1iIiii1i == 'clearthumb' : Ooo0O00 ( ) ; wiz . refresh ( )
elif iI1ii1iIiii1i == 'checksources' : wiz . checkSources ( ) ; wiz . refresh ( )
elif iI1ii1iIiii1i == 'checkrepos' : wiz . checkRepos ( ) ; wiz . refresh ( )
elif iI1ii1iIiii1i == 'freshstart' : II1IIiiI1 ( )
elif iI1ii1iIiii1i == 'forceupdate' : wiz . forceUpdate ( )
elif iI1ii1iIiii1i == 'forceprofile' : wiz . reloadProfile ( wiz . getInfo ( 'System.ProfileName' ) )
elif iI1ii1iIiii1i == 'forceclose' : wiz . killxbmc ( )
elif iI1ii1iIiii1i == 'forceskin' : wiz . ebi ( "ReloadSkin()" ) ; wiz . refresh ( )
elif iI1ii1iIiii1i == 'hidepassword' : wiz . hidePassword ( )
elif iI1ii1iIiii1i == 'unhidepassword' : wiz . unhidePassword ( )
elif iI1ii1iIiii1i == 'enableaddons' : iiiI11 ( )
elif iI1ii1iIiii1i == 'toggleaddon' : wiz . toggleAddon ( oO0o00oOOooO0 , OOOoO000 ) ; wiz . refresh ( )
elif iI1ii1iIiii1i == 'togglecache' : I1i1I1Iiiii1 ( oO0o00oOOooO0 ) ; wiz . refresh ( )
elif iI1ii1iIiii1i == 'toggleadult' : wiz . toggleAdult ( ) ; wiz . refresh ( )
elif iI1ii1iIiii1i == 'changefeq' : oo0O0oOoOoo ( ) ; wiz . refresh ( )
elif iI1ii1iIiii1i == 'uploadlog' : uploadLog . Main ( )
elif iI1ii1iIiii1i == 'viewlog' : oO0I1I1i1I1I1I1 ( )
elif iI1ii1iIiii1i == 'viewwizlog' : oO0I1I1i1I1I1I1 ( I11iii1Ii )
elif iI1ii1iIiii1i == 'viewerrorlog' : I1iiIiiii1111 ( all = True )
elif iI1ii1iIiii1i == 'clearwizlog' : OooOO0oOOo0O = open ( I11iii1Ii , 'w' ) ; OooOO0oOOo0O . close ( ) ; wiz . LogNotify ( "[COLOR %s]%s[/COLOR]" % ( oOOo0O00o , o0OOO ) , "[COLOR %s]Wizard Log Cleared![/COLOR]" % iIiIi11 )
elif iI1ii1iIiii1i == 'purgedb' : o0OO0ooOOO ( )
elif iI1ii1iIiii1i == 'fixaddonupdate' : I1i1I11111iI1 ( )
elif iI1ii1iIiii1i == 'removeaddons' : iI11iiI1I1Iii ( )
elif iI1ii1iIiii1i == 'removeaddon' : III11I11ii ( oO0o00oOOooO0 )
elif iI1ii1iIiii1i == 'removeaddondata' : o0OoO0oo0O0o ( )
elif iI1ii1iIiii1i == 'removedata' : Ii11IiI ( oO0o00oOOooO0 )
elif iI1ii1iIiii1i == 'resetaddon' : o00oO0o0o = wiz . cleanHouse ( o0 , ignore = True ) ; wiz . LogNotify ( "[COLOR %s]%s[/COLOR]" % ( oOOo0O00o , o0OOO ) , "[COLOR %s]Addon_Data reset[/COLOR]" % iIiIi11 )
elif iI1ii1iIiii1i == 'systeminfo' : OoOoOOoO ( )
elif iI1ii1iIiii1i == 'restorezip' : IiIII1i1i1I1iII ( 'build' )
elif iI1ii1iIiii1i == 'restoregui' : IiIII1i1i1I1iII ( 'gui' )
elif iI1ii1iIiii1i == 'restoreaddon' : IiIII1i1i1I1iII ( 'addondata' )
elif iI1ii1iIiii1i == 'restoreextzip' : O0000 ( 'build' )
elif iI1ii1iIiii1i == 'restoreextgui' : O0000 ( 'gui' )
elif iI1ii1iIiii1i == 'restoreextaddon' : O0000 ( 'addondata' )
elif iI1ii1iIiii1i == 'writeadvanced' : o00iIiiiII ( oO0o00oOOooO0 , OOOoO000 )
if 54 - 54: iiIIi1IiIi11 . i1IIi . oO0 * I1I1i1 % iiIIi1IiIi11
elif iI1ii1iIiii1i == 'apk1' : IIII1ii ( )
elif iI1ii1iIiii1i == 'apkgame' : IIo0OoO00 ( OOOoO000 )
elif iI1ii1iIiii1i == 'select' : OOooo00 ( OOOoO000 )
elif iI1ii1iIiii1i == 'grab' : o0Oii1111i ( oO0o00oOOooO0 , OOOoO000 )
elif iI1ii1iIiii1i == 'rom' : i1iii1ii ( OOOoO000 )
elif iI1ii1iIiii1i == 'apkscrape1' : APK ( )
elif iI1ii1iIiii1i == 'apkscrape' : OOOOoOo00OO ( oO0o00oOOooO0 )
elif iI1ii1iIiii1i == 'apkshow' : o0oooO ( OOOoO000 )
elif iI1ii1iIiii1i == 'intellaunch' : o00oo0000 ( )
elif iI1ii1iIiii1i == 'intelselect' : O000O ( oO0o00oOOooO0 , OOOoO000 , O00oOoo0OoO0 , oOoo000 , IiI11i1IIiiI )
elif iI1ii1iIiii1i == 'emurom' : II1iIII ( )
elif iI1ii1iIiii1i == 'roms' : I1I11ii ( )
elif iI1ii1iIiii1i == 'snes' : Oo0O0O00Oo ( )
elif iI1ii1iIiii1i == 'nes' : I11I1i1iI ( )
elif iI1ii1iIiii1i == 'gen' : o0oO0Oo ( )
elif iI1ii1iIiii1i == 'atr' : o0i1I11iI1iiI ( )
elif iI1ii1iIiii1i == 'n64' : ii ( )
elif iI1ii1iIiii1i == 'tbg' : i11i11 ( )
elif iI1ii1iIiii1i == 'nds' : O00o ( )
elif iI1ii1iIiii1i == 'ps' : IiiIiIi111iI1 ( )
elif iI1ii1iIiii1i == 'apkinstall' : O0ooOO ( oO0o00oOOooO0 , OOOoO000 , "None" )
elif iI1ii1iIiii1i == 'rominstall' : I1i1i111Ii1I ( oO0o00oOOooO0 , OOOoO000 , )
if 30 - 30: i11IiIiiIIIII
elif iI1ii1iIiii1i == 'youtube' : i1I111i1ii ( oO0o00oOOooO0 )
elif iI1ii1iIiii1i == 'viewVideo' : OooO00oo0O0 ( OOOoO000 )
if 85 - 85: II111iiii + OOoooooO * i11IiIiiIIIII
elif iI1ii1iIiii1i == 'addons' : IiIi1Oo00o000oOO ( oO0o00oOOooO0 )
elif iI1ii1iIiii1i == 'addoninstall' : oooo ( oO0o00oOOooO0 , OOOoO000 )
if 12 - 12: IiiIII111ii . ooOo % I1I1i1
elif iI1ii1iIiii1i == 'savedata' : i1IIii11i1I1 ( )
elif iI1ii1iIiii1i == 'togglesetting' : wiz . setS ( oO0o00oOOooO0 , 'false' if wiz . getS ( oO0o00oOOooO0 ) == 'true' else 'true' ) ; wiz . refresh ( )
elif iI1ii1iIiii1i == 'managedata' : III11i1iI11 ( oO0o00oOOooO0 )
elif iI1ii1iIiii1i == 'whitelist' : wiz . whiteList ( oO0o00oOOooO0 )
if 28 - 28: IiiIII111ii - ooOo % I1111 * OO00O0O0O00Oo
elif iI1ii1iIiii1i == 'trakt' : oo0o00OO ( )
elif iI1ii1iIiii1i == 'savetrakt' : traktit . traktIt ( 'update' , oO0o00oOOooO0 )
elif iI1ii1iIiii1i == 'restoretrakt' : traktit . traktIt ( 'restore' , oO0o00oOOooO0 )
elif iI1ii1iIiii1i == 'addontrakt' : traktit . traktIt ( 'clearaddon' , oO0o00oOOooO0 )
elif iI1ii1iIiii1i == 'cleartrakt' : traktit . clearSaved ( oO0o00oOOooO0 )
elif iI1ii1iIiii1i == 'authtrakt' : traktit . activateTrakt ( oO0o00oOOooO0 ) ; wiz . refresh ( )
elif iI1ii1iIiii1i == 'updatetrakt' : traktit . autoUpdate ( 'all' )
elif iI1ii1iIiii1i == 'importtrakt' : traktit . importlist ( oO0o00oOOooO0 ) ; wiz . refresh ( )
if 80 - 80: iii11iiII * i1Ii
elif iI1ii1iIiii1i == 'realdebrid' : o0Ooo0o0Oo ( )
elif iI1ii1iIiii1i == 'savedebrid' : debridit . debridIt ( 'update' , oO0o00oOOooO0 )
elif iI1ii1iIiii1i == 'restoredebrid' : debridit . debridIt ( 'restore' , oO0o00oOOooO0 )
elif iI1ii1iIiii1i == 'addondebrid' : debridit . debridIt ( 'clearaddon' , oO0o00oOOooO0 )
elif iI1ii1iIiii1i == 'cleardebrid' : debridit . clearSaved ( oO0o00oOOooO0 )
elif iI1ii1iIiii1i == 'authdebrid' : debridit . activateDebrid ( oO0o00oOOooO0 ) ; wiz . refresh ( )
elif iI1ii1iIiii1i == 'updatedebrid' : debridit . autoUpdate ( 'all' )
elif iI1ii1iIiii1i == 'importdebrid' : debridit . importlist ( oO0o00oOOooO0 ) ; wiz . refresh ( )
if 4 - 4: iIii1I11I1II1 . OO00O0O0O00Oo + II111iiii % OoooooooOO
elif iI1ii1iIiii1i == 'login' : I1iiIiiIiiI ( )
elif iI1ii1iIiii1i == 'savelogin' : loginit . loginIt ( 'update' , oO0o00oOOooO0 )
elif iI1ii1iIiii1i == 'restorelogin' : loginit . loginIt ( 'restore' , oO0o00oOOooO0 )
elif iI1ii1iIiii1i == 'addonlogin' : loginit . loginIt ( 'clearaddon' , oO0o00oOOooO0 )
elif iI1ii1iIiii1i == 'clearlogin' : loginit . clearSaved ( oO0o00oOOooO0 )
elif iI1ii1iIiii1i == 'authlogin' : loginit . activateLogin ( oO0o00oOOooO0 ) ; wiz . refresh ( )
elif iI1ii1iIiii1i == 'updatelogin' : loginit . autoUpdate ( 'all' )
elif iI1ii1iIiii1i == 'importlogin' : loginit . importlist ( oO0o00oOOooO0 ) ; wiz . refresh ( )
if 82 - 82: OoooooooOO / OOoooooO * i11IiIiiIIIII * O0 . oO0
elif iI1ii1iIiii1i == 'contact' : notify . contact ( oOO0O00Oo0O0o )
elif iI1ii1iIiii1i == 'settings' : wiz . openS ( oO0o00oOOooO0 ) ; wiz . refresh ( )
elif iI1ii1iIiii1i == 'opensettings' : id = eval ( OOOoO000 . upper ( ) + 'ID' ) [ oO0o00oOOooO0 ] [ 'plugin' ] ; iiIIIII = wiz . addonId ( id ) ; iiIIIII . openSettings ( ) ; wiz . refresh ( )
if 19 - 19: II111iiii / o0o0Oo0oooo0
elif iI1ii1iIiii1i == 'developer' : ii1OO0 ( )
elif iI1ii1iIiii1i == 'converttext' : wiz . convertText ( )
elif iI1ii1iIiii1i == 'createqr' : wiz . createQR ( )
elif iI1ii1iIiii1i == 'testnotify' : IIiiIii11 ( )
elif iI1ii1iIiii1i == 'testupdate' : Ii11ii1 ( )
elif iI1ii1iIiii1i == 'testfirst' : i1IiiI1 ( )
elif iI1ii1iIiii1i == 'testfirstrun' : Oo00O0O ( )
elif iI1ii1iIiii1i == 'testapk' : notify . apkInstaller ( 'SPMC' )
if 80 - 80: o0o0Oo0oooo0 + iIii1I11I1II1 . i1Ii
elif iI1ii1iIiii1i == 'guide' : TvGuide ( )
if 76 - 76: ooOo * iii11iiII
elif iI1ii1iIiii1i == 'recreateaddon' : ReCreate_Addon_ini ( )
elif iI1ii1iIiii1i == 'getlistplay' : Get_List_playlinks ( oO0o00oOOooO0 )
elif iI1ii1iIiii1i == 'resolve' : RESOLVER ( OOOoO000 )
elif iI1ii1iIiii1i == 'streams' : Streams_Menu ( )
elif iI1ii1iIiii1i == 'liveevent' : Live_Events ( oO0o00oOOooO0 )
elif iI1ii1iIiii1i == 'addonopen' : I1ii11iIi11i . openSettings ( sys . argv [ 0 ] )
xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
# dd678faae9ac167bc83abf78e5cb2f3f0688d3a3
