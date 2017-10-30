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
  if i11I1II == 1 :
   if 71 - 71: OO00O0O0O00Oo % i1IIi - II111iiii - iii11iiII + iii11iiII * OOoooooO
   if II1IOoOo000oOo0oo ( III ) :
    oO0O ( base64 . b64decode ( o0o0 ) )
    ii11II1i = OOOO000o0 ( 'Type Your Pin Here' )
    i11II11II1 ( ii11II1i )
    time . sleep ( 7 )
    OO0Ooooo000Oo ( )
    if 51 - 51: iIii1I11I1II1 / o0o0Oo0oooo0 + iii11iiII - i11IiIiiIIIII + iiIIi1IiIi11
   else :
    IiIi1 ( base64 . b64decode ( o0o0 ) )
    ii11II1i = OOOO000o0 ( 'Type Your Pin Here' )
    i11II11II1 ( ii11II1i )
    time . sleep ( 7 )
    OO0Ooooo000Oo ( )
    if 29 - 29: I1I1i1 % iIii1I11I1II1 . OoooooooOO % OoooooooOO % II111iiii / iiIIi1IiIi11
  if i11I1II == 2 :
   sys . exit ( )
   if 70 - 70: i11iIiiIii % iiIIi1IiIi11
def I11Ii11iI1 ( st ) :
 import re
 st = re . sub ( '\[.+\]' , '' , st )
 import string
 IiIiiI11111I1 = 0
 for O0oo0ooOOOO in st :
  if O0oo0ooOOOO in 'lij|\' ' : IiIiiI11111I1 += 37
  elif O0oo0ooOOOO in '![]fI.,:;/\\t' : IiIiiI11111I1 += 50
  elif O0oo0ooOOOO in '`-(){}r"' : IiIiiI11111I1 += 60
  elif O0oo0ooOOOO in '*^zcsJkvxy' : IiIiiI11111I1 += 85
  elif O0oo0ooOOOO in 'aebdhnopqug#$L+<>=?_~FZT' + string . digits : IiIiiI11111I1 += 95
  elif O0oo0ooOOOO in 'BSPEAKVXY&UwNRCHD' : IiIiiI11111I1 += 112
  elif O0oo0ooOOOO in 'QGOMm%W@' : IiIiiI11111I1 += 135
  else : IiIiiI11111I1 += 50
 return int ( IiIiiI11111I1 * 6.5 / 100 )
 if 14 - 14: ooOo / OoooooooOO % ooOo . O0
def OOOO000o0 ( Heading = xbmcaddon . Addon ( ) . getAddonInfo ( 'name' ) ) :
 OOOO0oooo = xbmc . Keyboard ( '' , Heading )
 OOOO0oooo . doModal ( )
 if ( OOOO0oooo . isConfirmed ( ) ) :
  return OOOO0oooo . getText ( )
  if 51 - 51: O0 - i1IIi / ooOo
def iI111i1I1II ( url ) :
 if 96 - 96: OO00O0O0O00Oo / Ooo0O * II111iiii - iiIIi1IiIi11 * Ooo0O
 import webbrowser
 if 81 - 81: i1Ii . I1I1i1 / OO00O0O0O00Oo
 IiIi1 = webbrowser . open
 i111iiI1ii = xbmc . executebuiltin
 II1IOoOo000oOo0oo = lambda ooOO00oOOo000 : xbmc . getCondVisibility ( str ( ooOO00oOOo000 ) )
 oO0O = lambda ooOO00oOOo000 : i111iiI1ii ( 'StartAndroidActivity(,android.intent.action.VIEW,,%s)' % ( ooOO00oOOo000 ) )
 if 17 - 17: i11iIiiIii - iii11iiII . i1Ii % iIii1I11I1II1 + i11IiIiiIIIII - OOoooooO
 III = 'System.Platform.Android'
 if 78 - 78: i11IiIiiIIIII * o0o0Oo0oooo0 . O0 / O0
 if II1IOoOo000oOo0oo ( III ) : oO0O ( base64 . b64decode ( url ) )
 else : IiIi1 ( base64 . b64decode ( url ) )
 if 80 - 80: i1IIi - Ooo0O / I1111 - i11iIiiIii
 if 68 - 68: IIIi1i1I - oO0 % O0 % OO00O0O0O00Oo
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
 for O0OOO0OOooo00 , OOOoO000 , oOOOO , Ii , OOo00OoO , i1i1i1I , oOoo000 , Ii1II , OooOo00o , IiI11i1IIiiI , counter in O0Oo0o000oO :
  i1i1i1I = i1i1i1I if wiz . workingURL ( i1i1i1I ) else iiiiiIIii
  oOoo000 = oOoo000 if wiz . workingURL ( oOoo000 ) else OOO00
  I111iIi1 = '%s (v%s)' % ( name , O0OOO0OOooo00 )
  if O000oo0O == name and O0OOO0OOooo00 > oo0OooOOo0 :
   I111iIi1 = '%s [COLOR red][CURRENT v%s][/COLOR]' % ( I111iIi1 , oo0OooOOo0 )
  iiiii1II ( I111iIi1 , '' , description = IiI11i1IIiiI , fanart = oOoo000 , icon = i1i1i1I , themeit = OO0O000 )
  if O0O0ooOOO == 'No' : iiiii1II ( wiz . sep ( ) , '' , themeit = OOoO )
  oo00O00oO000o ( 'Save Data Menu' , 'savedata' , icon = I1111i , themeit = OOoO )
  iiiii1II ( 'Build Information' , 'buildinfo' , name , description = IiI11i1IIiiI , fanart = oOoo000 , icon = i1i1i1I , themeit = OOoO )
  if not Ii1II == "http://" : iiiii1II ( 'View Video Preview' , 'buildpreview' , name , description = IiI11i1IIiiI , fanart = oOoo000 , icon = i1i1i1I , themeit = OOoO )
  ooO0O0o0 = int ( float ( o0OIiII ) ) ; OO0OOooOO0 = int ( float ( Ii ) )
  if not ooO0O0o0 == OO0OOooOO0 :
   if ooO0O0o0 == 16 and OO0OOooOO0 <= 15 : IIIIIii1ii11 = False
   else : IIIIIii1ii11 = True
  else : IIIIIii1ii11 = False
  if IIIIIii1ii11 == True :
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
    for OOOooo0OooOoO , oOoOOOo , ii1Io0OOoOoO00 , I1iii , oOO0OO0O , IiI11i1IIiiI , counter in O0Oo0o000oO :
     if not O0Oo000ooO00 == 'true' and oOO0OO0O . lower ( ) == 'yes' : continue
     ii1Io0OOoOoO00 = ii1Io0OOoOoO00 if ii1Io0OOoOoO00 == 'http://' else i1i1i1I
     I1iii = I1iii if I1iii == 'http://' else oOoo000
     iiiii1II ( OOOooo0OooOoO if not OOOooo0OooOoO == o0O else "[B]%s (Installed)[/B]" % OOOooo0OooOoO , 'theme' , name , OOOooo0OooOoO , description = IiI11i1IIiiI , fanart = I1iii , icon = ii1Io0OOoOoO00 , themeit = OOoO )
 iIi1 ( 'files' , 'viewType' )
 if 78 - 78: IiiIII111ii / II111iiii % o0o0Oo0oooo0
def oO00OoOO ( number ) :
 oO0o00oOOooO0 = eval ( 'THIRD%sNAME' % number )
 OOOoO000 = eval ( 'THIRD%sURL' % number )
 I11IIiIiI = wiz . workingURL ( OOOoO000 )
 if not I11IIiIiI == True :
  iiiii1II ( 'Url for txt file not valid' , '' , icon = oO0O00oOOoooO , themeit = OOoO )
  iiiii1II ( '%s' % WORKINGURL , '' , icon = oO0O00oOOoooO , themeit = OOoO )
 else :
  type , iIIIi1i1I11i = wiz . thirdParty ( OOOoO000 )
  iiiii1II ( "[B]%s[/B]" % oO0o00oOOooO0 , '' , themeit = OOoO )
  if O0O0ooOOO == 'No' : iiiii1II ( wiz . sep ( ) , '' , themeit = OOoO )
  if type :
   for oO0o00oOOooO0 , O0OOO0OOooo00 , OOOoO000 , Ii , i1i1i1I , oOoo000 , OooOo00o , IiI11i1IIiiI in iIIIi1i1I11i :
    if not O0Oo000ooO00 == 'true' and OooOo00o . lower ( ) == 'yes' : continue
    iiiii1II ( "[%s] %s v%s" % ( Ii , oO0o00oOOooO0 , O0OOO0OOooo00 ) , 'installthird' , oO0o00oOOooO0 , OOOoO000 , icon = i1i1i1I , fanart = oOoo000 , description = IiI11i1IIiiI , themeit = oooOo0OOOoo0 )
  else :
   for oO0o00oOOooO0 , OOOoO000 , i1i1i1I , oOoo000 , IiI11i1IIiiI in iIIIi1i1I11i :
    iiiii1II ( oO0o00oOOooO0 , 'installthird' , oO0o00oOOooO0 , OOOoO000 , icon = i1i1i1I , fanart = oOoo000 , description = IiI11i1IIiiI , themeit = oooOo0OOOoo0 )
    if 55 - 55: Ooo0O - iii11iiII
def O0OO0O ( number ) :
 oO0o00oOOooO0 = eval ( 'THIRD%sNAME' % number )
 OOOoO000 = eval ( 'THIRD%sURL' % number )
 IiiiIiiI = wiz . getKeyboard ( oO0o00oOOooO0 , 'Enter the Name of the Wizard' )
 o00O = wiz . getKeyboard ( OOOoO000 , 'Enter the URL of the Wizard Text' )
 if 48 - 48: iiIIi1IiIi11 . i11iIiiIii
 wiz . setS ( 'wizard%sname' % number , IiiiIiiI )
 wiz . setS ( 'wizard%surl' % number , o00O )
 if 5 - 5: IIIi1i1I . oO0 . II111iiii . OoooooooOO
def Oo0OooO0 ( name = "" ) :
 if name == 'kodi' :
  oO00oOo0OOO = 'http://mirrors.kodi.tv/releases/android/arm/'
  ii1ooO = 'http://mirrors.kodi.tv/releases/android/arm/old/'
  oOoOoO000OO = wiz . openURL ( oO00oOo0OOO ) . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
  o00O = wiz . openURL ( ii1ooO ) . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
  ooOO00oOOo000 = 0
  ii11II11 = re . compile ( '<tr><td><a href="(.+?)".+?>(.+?)</a></td><td>(.+?)</td><td>(.+?)</td></tr>' ) . findall ( oOoOoO000OO )
  oOooOo00OooO0oO = re . compile ( '<tr><td><a href="(.+?)".+?>(.+?)</a></td><td>(.+?)</td><td>(.+?)</td></tr>' ) . findall ( o00O )
  if 16 - 16: i1Ii / Ooo0O + iii11iiII / IiiIII111ii
  iiiii1II ( "Official Kodi Apk\'s" , themeit = OOOiiiiI )
  IIIiiI1 = False
  for OOOoO000 , name , IiIiiI11111I1 , O0O0ooOOOO0o in ii11II11 :
   if OOOoO000 in [ '../' , 'old/' ] : continue
   if not OOOoO000 . endswith ( '.apk' ) : continue
   if not OOOoO000 . find ( '_' ) == - 1 and IIIiiI1 == True : continue
   try :
    iIiiiiI1II1I1 = name . split ( '-' )
    if not OOOoO000 . find ( '_' ) == - 1 :
     IIIiiI1 = True
     IiiiIiiI , OoO0ooO = iIiiiiI1II1I1 [ 2 ] . split ( '_' )
    else :
     IiiiIiiI = iIiiiiI1II1I1 [ 2 ]
     OoO0ooO = ''
    oooo = "[COLOR %s]%s v%s%s %s[/COLOR] [COLOR %s]%s[/COLOR] [COLOR %s]%s[/COLOR]" % ( oOOo0O00o , iIiiiiI1II1I1 [ 0 ] . title ( ) , iIiiiiI1II1I1 [ 1 ] , OoO0ooO . upper ( ) , IiiiIiiI , iIiIi11 , IiIiiI11111I1 . replace ( ' ' , '' ) , oOOo0O00o , O0O0ooOOOO0o )
    IIIII1iii11 = urljoin ( oO00oOo0OOO , OOOoO000 )
    iiiii1II ( oooo , 'apkinstall' , "%s v%s%s %s" % ( iIiiiiI1II1I1 [ 0 ] . title ( ) , iIiiiiI1II1I1 [ 1 ] , OoO0ooO . upper ( ) , IiiiIiiI ) , IIIII1iii11 )
    ooOO00oOOo000 += 1
   except :
    wiz . log ( "Error on: %s" % name )
    if 35 - 35: IIIi1i1I / OO00O0O0O00Oo / II111iiii - iIii1I11I1II1 + II111iiii . OO00O0O0O00Oo
  for OOOoO000 , name , IiIiiI11111I1 , O0O0ooOOOO0o in oOooOo00OooO0oO :
   if OOOoO000 in [ '../' , 'old/' ] : continue
   if not OOOoO000 . endswith ( '.apk' ) : continue
   if not OOOoO000 . find ( '_' ) == - 1 : continue
   try :
    iIiiiiI1II1I1 = name . split ( '-' )
    oooo = "[COLOR %s]%s v%s %s[/COLOR] [COLOR %s]%s[/COLOR] [COLOR %s]%s[/COLOR]" % ( oOOo0O00o , iIiiiiI1II1I1 [ 0 ] . title ( ) , iIiiiiI1II1I1 [ 1 ] , iIiiiiI1II1I1 [ 2 ] , iIiIi11 , IiIiiI11111I1 . replace ( ' ' , '' ) , oOOo0O00o , O0O0ooOOOO0o )
    IIIII1iii11 = urljoin ( ii1ooO , OOOoO000 )
    iiiii1II ( oooo , 'apkinstall' , "%s v%s %s" % ( iIiiiiI1II1I1 [ 0 ] . title ( ) , iIiiiiI1II1I1 [ 1 ] , iIiiiiI1II1I1 [ 2 ] ) , IIIII1iii11 )
    ooOO00oOOo000 += 1
   except :
    wiz . log ( "Error on: %s" % name )
  if ooOO00oOOo000 == 0 : iiiii1II ( "Error Kodi Scraper Is Currently Down." )
 elif name == 'spmc' :
  O0O00O000OOO = 'https://github.com/koying/SPMC/releases'
  oOoOoO000OO = wiz . openURL ( O0O00O000OOO ) . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
  ooOO00oOOo000 = 0
  ii11II11 = re . compile ( '<div.+?lass="release-body.+?div class="release-header".+?a href=.+?>(.+?)</a>.+?ul class="release-downloads">(.+?)</ul>.+?/div>' ) . findall ( oOoOoO000OO )
  if 3 - 3: O0
  iiiii1II ( "Official SPMC Apk\'s" , themeit = OOOiiiiI )
  if 64 - 64: i1IIi % OOoooooO / i11iIiiIii - i1IIi % iii11iiII . iiIIi1IiIi11
  for name , II1i111 in ii11II11 :
   i1iiiIii11 = ''
   oOooOo00OooO0oO = re . compile ( '<li>.+?<a href="(.+?)" rel="nofollow">.+?<small class="text-gray float-right">(.+?)</small>.+?strong>(.+?)</strong>.+?</a>.+?</li>' ) . findall ( II1i111 )
   for OOoOOO000O0 , oOo0 , II1i11I1 in oOooOo00OooO0oO :
    if II1i11I1 . find ( 'armeabi' ) == - 1 : continue
    if II1i11I1 . find ( 'launcher' ) > - 1 : continue
    i1iiiIii11 = urljoin ( 'https://github.com' , OOoOOO000O0 )
    break
   if i1iiiIii11 == '' : continue
   try :
    name = "SPMC %s" % name
    oooo = "[COLOR %s]%s[/COLOR] [COLOR %s]%s[/COLOR]" % ( oOOo0O00o , name , iIiIi11 , oOo0 . replace ( ' ' , '' ) )
    IIIII1iii11 = i1iiiIii11
    iiiii1II ( oooo , 'apkinstall' , name , IIIII1iii11 )
    ooOO00oOOo000 += 1
   except Exception , iiIiIiII :
    wiz . log ( "Error on: %s / %s" % ( name , str ( iiIiIiII ) ) )
  if ooOO00oOOo000 == 0 : iiiii1II ( "Error SPMC Scraper Is Currently Down." )
  if 37 - 37: i11IiIiiIIIII / i1Ii + II111iiii
def iiiiiIIi ( ) :
 oo00O00oO000o ( 'Emulators And Roms' , 'emurom' , icon = i111iIi1i1II1 , themeit = OOOiiiiI )
 oo00O00oO000o ( 'SpinzTV APKS' , 'apkshow' , url = OooOo , icon = Ii1IIiI1i , themeit = OOOiiiiI )
 oo00O00oO000o ( '[COLOR deepskyblue]APK Drawer[/COLOR]' , 'intellaunch' , )
 oo00O00oO000o ( 'Official Kodi Apk\'s' , 'apkscrape' , 'kodi' , icon = Oo0O00O000 , themeit = OOOiiiiI )
 oo00O00oO000o ( 'Official SPMC Apk\'s' , 'apkscrape' , 'spmc' , icon = Oo0O00O000 , themeit = OOOiiiiI )
 ooO00O00oOO = I1 ( base64 . b64decode ( 'aHR0cHM6Ly93d3cuYXBrZmlsZXMuY29tLw==' ) )
 O0Oo0o000oO = re . compile ( 'href="([^"]*)">Applications(.+?)</a>' ) . findall ( ooO00O00oOO )
 oOooOo00OooO0oO = re . compile ( 'href="([^"]*)">Games(.+?)</a>' ) . findall ( ooO00O00oOO )
 for OOOoO000 , IIII1ii in O0Oo0o000oO :
  IiIIi1I1I11Ii ( '[COLOR deepskyblue]Android Apps[/COLOR]' + IIII1ii , 'https://www.apkfiles.com' + OOOoO000 , 'apkgame' , i1I1i111Ii )
 for OOOoO000 , IIII1ii in oOooOo00OooO0oO :
  IiIIi1I1I11Ii ( '[COLOR deepskyblue]Android Games[/COLOR]' + IIII1ii , 'https://www.apkfiles.com' + OOOoO000 , 'apkgame' , i111iIi1i1II1 )
 iIi1 ( 'movies' , 'MAIN' )
 oo00O00oO000o ( 'Spinz Apk Picks' , 'apkshow' , url = ii1I , icon = Oo0O00O000 , themeit = OOOiiiiI )
 if O0Oo000ooO00 == 'true' : oo00O00oO000o ( 'XXX Apk' , 'apkshow' , url = i11III1111iIi , icon = Oo0O00O000 , themeit = OOOiiiiI )
 iIi1 ( 'files' , 'viewType' )
 if 64 - 64: OoooooooOO
def oO0oooooo ( url ) :
 o0O0Oo00 = I1 ( url ) . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
 O0Oo0o000oO = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?con="(.+?)".+?anart="(.+?)"' ) . findall ( o0O0Oo00 )
 if len ( O0Oo0o000oO ) > 0 :
  for oO0o00oOOooO0 , url , i1i1i1I , oOoo000 in O0Oo0o000oO :
   iiiii1II ( oO0o00oOOooO0 , 'apkinstall' , oO0o00oOOooO0 , url , icon = i1i1i1I , fanart = oOoo000 , themeit = OOOiiiiI )
  else : wiz . log ( "[APK Menu] ERROR: Invalid Format." )
 else : wiz . log ( "[APK Menu] ERROR: URL for emu list not working." )
 if 65 - 65: i1Ii + Ooo0O
def Ooo0O0 ( url ) :
 ooO00O00oOO = I1 ( url )
 O0Oo0o000oO = re . compile ( '<a href="([^"]*)" >(.+?)</a>' ) . findall ( ooO00O00oOO )
 for url , oO0o00oOOooO0 in O0Oo0o000oO :
  if '/cat' in url :
   IiIIi1I1I11Ii ( ( oO0o00oOOooO0 ) . replace ( '&amp;' , ' - ' ) , 'https://www.apkfiles.com' + url , 'select' , O000OO0 + 'APK.png' )
   if 71 - 71: OoooooooOO
def iIiI1iiiI1ii ( url ) :
 ooO00O00oOO = I1 ( url )
 oOoOoO000OO = url
 if "page=" in str ( url ) :
  oOoOoO000OO = url . split ( '?' ) [ 0 ]
 O0Oo0o000oO = re . compile ( '<a href="([^"]*)".+?<img src="([^"]*)" class="file_list_icon".+?alt="([^"]*)"' , re . DOTALL ) . findall ( ooO00O00oOO )
 oOooOo00OooO0oO = re . compile ( 'class="[^"]*".+?ref="([^"]*)".+?yle=.+?</a>' ) . findall ( ooO00O00oOO )
 for url , I1i , oO0o00oOOooO0 in O0Oo0o000oO :
  if 'apk' in url :
   IiIIi1I1I11Ii ( ( oO0o00oOOooO0 ) . replace ( '&#39;' , '' ) . replace ( '&amp;' , ' - ' ) . replace ( '&#174;:' , ': ' ) . replace ( '&#174;' , ' ' ) , 'https://www.apkfiles.com' + url , 'grab' , 'http:' + I1i )
 if len ( oOooOo00OooO0oO ) > 1 :
  oOooOo00OooO0oO = str ( oOooOo00OooO0oO [ len ( oOooOo00OooO0oO ) - 1 ] )
 IiIIi1I1I11Ii ( 'Next Page' , oOoOoO000OO + str ( oOooOo00OooO0oO ) , 'select' , O000OO0 + 'Next.png' )
 if 67 - 67: o0o0Oo0oooo0 / I1I1i1 * I1111 / iii11iiII * oO0 / IIIi1i1I
def OOoOO0OO ( name , url ) :
 ooO00O00oOO = I1 ( url )
 name = name
 O0Oo0o000oO = re . compile ( 'href="([^"]*)".+?lass="yellow_button".+?itle=' ) . findall ( ooO00O00oOO )
 for url in O0Oo0o000oO :
  url = 'https://www.apkfiles.com' + url
  i1oo00OoO ( name , url , 'Brackets' )
  if 30 - 30: Ooo0O . I1111
  if 57 - 57: i11IiIiiIIIII . Ooo0O + II111iiii
  if 43 - 43: OO00O0O0O00Oo % iiIIi1IiIi11
  if 69 - 69: iiIIi1IiIi11 % I1111
def oOOoO ( ) :
 xbmc . executebuiltin ( 'Runscript("special://home/addons/plugin.program.SpinzTV/ookla.py")' )
 if 19 - 19: i11iIiiIii
 if 54 - 54: II111iiii . i11IiIiiIIIII
 if 73 - 73: o0o0Oo0oooo0 . ooOo
 if 32 - 32: o0o0Oo0oooo0 * ooOo % OOoooooO * IiiIII111ii . O0
def i11i1i1I1iI1 ( ) :
 if 53 - 53: iii11iiII + ooOo / i11iIiiIii - I1I1i1 * IIIi1i1I / OoooooooOO
 if os . path . isfile ( i1i1II ) :
  OoOo = True
  i1iIIIiiiI = open ( i1i1II )
  OoO00oo00 = i1iIIIiiiI . read ( )
  i1iIIIiiiI . close ( )
 else :
  xbmcgui . Dialog ( ) . ok ( "[COLOR orange]SpinzTV[/COLOR]" , "[COLOR cyan][B]][[/B]NT3L[B]][[/B]G3NC[B]][[/B][/COLOR]" , "[COLOR ghostwhite]First Time Launching Will Take a Couple Minutes[/COLOR]" , "[COLOR ghostwhite]Please Be Patient![/COLOR]" )
  OoOo = False
  if 76 - 76: OoooooooOO + Ooo0O % i1Ii . I1111 + II111iiii
  if 70 - 70: ooOo / i11IiIiiIIIII
  if 28 - 28: oO0 * OoooooooOO . II111iiii / i11iIiiIii + IIIi1i1I
  if 38 - 38: i1Ii . IiiIII111ii
  if 24 - 24: I1I1i1 - I1I1i1 + oO0 + ooOo - IIIi1i1I
  if 12 - 12: iiIIi1IiIi11 . i1Ii . o0o0Oo0oooo0 / O0
  if 58 - 58: I1I1i1 - II111iiii % IIIi1i1I + OO00O0O0O00Oo . o0o0Oo0oooo0 / i1Ii
  if 8 - 8: oO0 . I1111 * i11IiIiiIIIII + II111iiii % i11iIiiIii
  if 8 - 8: OOoooooO * O0
  if 73 - 73: I1I1i1 / IIIi1i1I / i11IiIiiIIIII / I1111
  if 11 - 11: o0o0Oo0oooo0 + i1Ii - OoooooooOO / I1111
 iIIi1iI1I1IIi = ""
 O0OO0 = O0ooo0o0 ( )
 for oO0ooOoO in O0OO0 :
  if OoOo == True :
   if oO0ooOoO not in OoO00oo00 :
    if 59 - 59: O0 % Ooo0O
    if 92 - 92: IiiIII111ii % iiIIi1IiIi11 / oO0 % oO0 * ooOo
    OooO00oOOo0Oo = IIiIIIIii ( iIIi1iI1I1IIi , oO0ooOoO )
    iIIi1iI1I1IIi = OooO00oOOo0Oo
    if 40 - 40: O0
  else :
   OooO00oOOo0Oo = IIiIIIIii ( iIIi1iI1I1IIi , oO0ooOoO )
   iIIi1iI1I1IIi = OooO00oOOo0Oo
   if 58 - 58: Ooo0O
 if OoOo == True :
  i1iIIIiiiI = open ( i1i1II , 'a' )
  if 9 - 9: iIii1I11I1II1 % oO0 . iii11iiII + OoooooooOO
  if 62 - 62: O0 / ooOo % O0 * I1111 % ooOo
 else :
  i1iIIIiiiI = open ( i1i1II , 'w' )
  if 33 - 33: ooOo . IIIi1i1I * I1111 * iIii1I11I1II1
  if 5 - 5: Ooo0O / i1Ii % O0 . OO00O0O0O00Oo * i1Ii
 i1iIIIiiiI . write ( iIIi1iI1I1IIi )
 i1iIIIiiiI . close ( )
 if 83 - 83: iii11iiII
 if 12 - 12: i1IIi . i1IIi - I1I1i1
 i1iIIIiiiI = open ( i1i1II )
 OoO00oo00 = i1iIIIiiiI . read ( )
 i1iIIIiiiI . close ( )
 OoO00oo00 = OoO00oo00 . replace ( '\n' , '' ) . replace ( '\r' , '' )
 O0Oo0o000oO = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)".+?nstallRating="(.+?)"' ) . findall ( OoO00oo00 )
 if 26 - 26: iIii1I11I1II1 % i11iIiiIii % oO0
 if 67 - 67: OoooooooOO
 for oO0o00oOOooO0 , OOOoO000 , IiIiIi1I1 , oOoo000 , IiI11i1IIiiI , IiI1ii1Ii in sorted ( O0Oo0o000oO , key = lambda O0Oo0o000oO : O0Oo0o000oO [ 0 ] ) :
  if OOOoO000 in O0OO0 :
   oooOOOoOOOo0O ( '[COLOR ghostwhite]' + str ( oO0o00oOOooO0 ) + '[/COLOR]' , OOOoO000 , 'intelselect' , IiIiIi1I1 , oOoo000 , IiI11i1IIiiI , IiI1ii1Ii )
   if 82 - 82: i1Ii * i11iIiiIii % II111iiii - OoooooooOO
def O0ooo0o0 ( ) :
 if xbmc . getCondVisibility ( 'system.platform.android' ) :
  try :
   O0OO0 = subprocess . Popen ( [ 'exec ' '/system/bin/pm list packages -3' '' ] , executable = '/system/bin/sh' , shell = True , stdout = subprocess . PIPE , stderr = subprocess . STDOUT ) . communicate ( ) [ 0 ] . rstrip ( '\n' ) . splitlines ( )
  except :
   O0OO0 = [ ]
   if 90 - 90: Ooo0O . IIIi1i1I * i1IIi - i1IIi
  for oO0ooOoO in range ( len ( O0OO0 ) ) :
   O0OO0 [ oO0ooOoO ] = O0OO0 [ oO0ooOoO ] . partition ( ':' ) [ 2 ]
   if 16 - 16: ooOo * i1IIi - I1I1i1 . i1Ii % i11IiIiiIIIII / I1I1i1
 return O0OO0
 if 14 - 14: iIii1I11I1II1 * OO00O0O0O00Oo * oO0 / iIii1I11I1II1 * i1Ii / i11IiIiiIIIII
def IIiIIIIii ( theList , i ) :
 global theNotList
 OOO000 = "https://play.google.com/store/apps/details?id=" + i
 o0O0Oo00 = Ii1 ( OOO000 )
 if 62 - 62: i1IIi - i1IIi
 if o0O0Oo00 != False :
  o0O0Oo00 = o0O0Oo00 . replace ( '\n' , '' ) . replace ( '\r' , '' )
  if 69 - 69: o0o0Oo0oooo0 % IIIi1i1I - i11IiIiiIIIII
  Iiii1ii = r'<div class="id-app-title".tabindex=".">(.+?)</div>'
  O0Oo0o000oO = re . search ( Iiii1ii , o0O0Oo00 )
  if O0Oo0o000oO != None : oO0o00oOOooO0 = O0Oo0o000oO . group ( 1 )
  else : oO0o00oOOooO0 = i
  if 42 - 42: IiiIII111ii * OO00O0O0O00Oo . i1Ii * ooOo + o0o0Oo0oooo0
  if 25 - 25: i11IiIiiIIIII . ooOo + IIIi1i1I
  if 75 - 75: i1Ii - I1I1i1 % iiIIi1IiIi11 + i11iIiiIii
  if 100 - 100: i11IiIiiIIIII + I1I1i1 - i11iIiiIii - II111iiii
  if 40 - 40: o0o0Oo0oooo0 % I1111
  IiIiIi1I1 = "androidapp://sources/apps/" + str ( i ) + ".png"
  if 62 - 62: I1I1i1
  if 15 - 15: i11IiIiiIIIII + IiiIII111ii . iii11iiII * I1111 . o0o0Oo0oooo0
  if 18 - 18: i1IIi % II111iiii + OO00O0O0O00Oo % IiiIII111ii
  if 72 - 72: iIii1I11I1II1
  if 45 - 45: Ooo0O - I1I1i1 % OO00O0O0O00Oo
  if 38 - 38: OO00O0O0O00Oo % iii11iiII - OoooooooOO
  oOo0OOoooO = r'data-expand-to="full-screenshot-[0-9]{1,2}" src="(//\w+?.\w+?.\S+?=h900)"'
  O0Oo0o000oO = re . compile ( oOo0OOoooO ) . findall ( o0O0Oo00 )
  if len ( O0Oo0o000oO ) != 0 : oOoo000 = "https:" + O0Oo0o000oO [ len ( O0Oo0o000oO ) - 1 ]
  else : oOoo000 = "None"
  if 26 - 26: I1I1i1 * i1Ii . i1IIi
  ooOoOO = r'data-video-url="https://www.youtube.com/embed/(\S.+?)\?ps=play.+?"'
  O0Oo0o000oO = re . search ( ooOoOO , o0O0Oo00 )
  if O0Oo0o000oO != None : IiI11i1IIiiI = O0Oo0o000oO . group ( 1 )
  else : IiI11i1IIiiI = "None"
  if 56 - 56: iIii1I11I1II1 . i11iIiiIii - iii11iiII * II111iiii * OO00O0O0O00Oo
  i1I1 = r'<div class="content" itemprop="numDownloads">\s+?(\d.+?\s-\s\d.+?)\s+?</div>'
  O0Oo0o000oO = re . search ( i1I1 , o0O0Oo00 )
  if O0Oo0o000oO != None : OOO0 = 'Installed ' + O0Oo0o000oO . group ( 1 )
  else : OOO0 = "Installs: N/A"
  if 10 - 10: Ooo0O + O0
  Ii1iI = r'<div class="score" aria-label=" Rated .+? stars out of five stars ">(.+?)</div>'
  O0Oo0o000oO = re . search ( Ii1iI , o0O0Oo00 )
  if O0Oo0o000oO != None : Oo0O0O000 = O0Oo0o000oO . group ( 1 ) + " Stars"
  else : Oo0O0O000 = "Rating: N/A"
  IiI1ii1Ii = Oo0O0O000 + " " + OOO0
  if 29 - 29: I1I1i1 / Ooo0O * oO0 . I1I1i1
  if 64 - 64: IIIi1i1I / OOoooooO % i11iIiiIii
  if 3 - 3: iiIIi1IiIi11 . OOoooooO % ooOo + oO0
  OOOoO000 = i
  theList += 'name="' + oO0o00oOOooO0 + '"url="' + OOOoO000 + '"img="' + IiIiIi1I1 + '"fanart="' + oOoo000 + '"description="' + IiI11i1IIiiI + '"installRating="' + IiI1ii1Ii + '"'
  return theList
  if 64 - 64: i1IIi
  if 29 - 29: I1I1i1 / i11iIiiIii / ooOo % IIIi1i1I % i11iIiiIii
  if 18 - 18: iii11iiII + OO00O0O0O00Oo
  if 80 - 80: IIIi1i1I + I1I1i1 * IiiIII111ii + I1111
  if 75 - 75: i11IiIiiIIIII / I1I1i1 / iii11iiII / i1Ii % OOoooooO + II111iiii
  if 4 - 4: iiIIi1IiIi11 - Ooo0O - i1Ii - i11IiIiiIIIII % i11iIiiIii / I1111
  if 50 - 50: OOoooooO + i1IIi
  if 31 - 31: IiiIII111ii
  if 78 - 78: i11iIiiIii + I1I1i1 + OO00O0O0O00Oo / I1I1i1 % iIii1I11I1II1 % i1Ii
 else :
  if 83 - 83: iIii1I11I1II1 % o0o0Oo0oooo0 % I1I1i1 % OO00O0O0O00Oo . oO0 % O0
  return theList
  if 47 - 47: I1I1i1
def oo0ooooO ( name , url , iconimage , fanart , videolink ) :
 iiIIi = 0
 if 36 - 36: i11IiIiiIIIII . II111iiii
 if videolink != "None" :
  iiIIi += 1
  if 25 - 25: IIIi1i1I
 if iiIIi == 1 : iI1 = xbmcgui . Dialog ( ) . select ( '[COLOR deepskyblue]' + name + '[/COLOR]' , [ '[COLOR deepskyblue]Launch[/COLOR]' , '[COLOR ghostwhite]Preview Video[/COLOR]' , '[COLOR tomato]Uninstall[/COLOR]' ] )
 if iiIIi == 0 : iI1 = xbmcgui . Dialog ( ) . select ( '[COLOR deepskyblue]' + name + '[/COLOR]' , [ '[COLOR deepskyblue]Launch[/COLOR]' , '[COLOR ghostwhite]No Preview Video[/COLOR]' , '[COLOR tomato]Uninstall[/COLOR]' ] )
 if 11 - 11: I1111
 if 18 - 18: iiIIi1IiIi11 - IIIi1i1I % iiIIi1IiIi11 / i11IiIiiIIIII
 if 68 - 68: IiiIII111ii * iIii1I11I1II1 + OO00O0O0O00Oo % o0o0Oo0oooo0
 if iI1 == 1 :
  if videolink != 'None' :
   yt . PlayVideo ( videolink )
 if iI1 == 0 :
  IIii1I1I1I = xbmcgui . Dialog ( ) . yesno ( "[COLOR orange]SpinzTV[/COLOR]" , "[COLOR cyan][B]][[/B]NT3L[B]][[/B]G3NC[B]][[/B][/COLOR]" , "" , "[COLOR ghostwhite]Would You Like To Launch:[/COLOR] [COLOR cyan]" + name + "[/COLOR]" , "[COLOR red]No Way[/COLOR]" , "[COLOR cyan]Heck Ya![/COLOR]" )
  if IIii1I1I1I == 1 :
   xbmc . executebuiltin ( 'StartAndroidActivity(%s)' % url )
 if iI1 == 2 :
  OoOOOo0 = xbmcgui . Dialog ( ) . yesno ( "[COLOR orange]SpinzTV[/COLOR]" , "[COLOR cyan][B]][[/B]NT3L[B]][[/B]G3NC[B]][[/B][/COLOR]" , "" , "[COLOR ghostwhite]Would You Like To Remove:[/COLOR] [COLOR cyan]" + name + "[/COLOR]" , "[COLOR red]No Way[/COLOR]" , "[COLOR cyan]Heck Ya![/COLOR]" )
  if OoOOOo0 :
   xbmc . executebuiltin ( 'StartAndroidActivity("","android.intent.action.DELETE","","package:' + url + '")' )
   xbmc . sleep ( 2000 )
   try : shutil . rmtree ( "/sdcard/Android/data/" + url , ignore_errors = True , onerror = None )
   except : pass
   try : shutil . rmtree ( "/sdcard/Android/obb/" + url , ignore_errors = True , onerror = None )
   except : pass
   xbmc . executebuiltin ( 'Container.Refresh' )
   if 61 - 61: iIii1I11I1II1
def Ii1 ( url ) :
 try :
  OO0OO = urllib2 . Request ( url )
  OO0OO . add_header ( 'User-Agent' , 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3' )
  I1II1I1I = urllib2 . urlopen ( OO0OO )
  o0O0Oo00 = I1II1I1I . read ( )
  I1II1I1I . close ( )
  return o0O0Oo00
 except :
  return False
  if 79 - 79: iii11iiII / OO00O0O0O00Oo . o0o0Oo0oooo0 - oO0
  if 47 - 47: OoooooooOO % O0 * iiIIi1IiIi11 . IiiIII111ii
  if 38 - 38: O0 - i1Ii % OO00O0O0O00Oo
def ooO ( ) :
 oo00O00oO000o ( 'Emulators' , 'apkshow' , url = I1i111I , icon = i111iIi1i1II1 , themeit = OOOiiiiI )
 oo00O00oO000o ( 'Roms' , 'roms' , icon = i111iIi1i1II1 , themeit = OOOiiiiI )
 if 39 - 39: iii11iiII / oO0 / ooOo * OO00O0O0O00Oo
 if 44 - 44: O0 + OOoooooO . iIii1I11I1II1 + Ooo0O / O0 - i11IiIiiIIIII
 if 83 - 83: i1Ii * i11IiIiiIIIII / Ooo0O
 if 32 - 32: I1I1i1 + o0o0Oo0oooo0 - OoooooooOO
def Ii11iii1II1i ( ) :
 oo00O00oO000o ( 'NES' , 'nes' , icon = i111iIi1i1II1 , themeit = OOOiiiiI )
 oo00O00oO000o ( 'SNES' , 'snes' , icon = i111iIi1i1II1 , themeit = OOOiiiiI )
 oo00O00oO000o ( 'Nintendo 64' , 'n64' , icon = i111iIi1i1II1 , themeit = OOOiiiiI )
 oo00O00oO000o ( 'Nintendo DS' , 'nds' , icon = i111iIi1i1II1 , themeit = OOOiiiiI )
 oo00O00oO000o ( 'Genesis' , 'gen' , icon = i111iIi1i1II1 , themeit = OOOiiiiI )
 oo00O00oO000o ( 'Playstation' , 'ps' , icon = i111iIi1i1II1 , themeit = OOOiiiiI )
 oo00O00oO000o ( 'Atari' , 'atr' , icon = i111iIi1i1II1 , themeit = OOOiiiiI )
 oo00O00oO000o ( 'PC Engine & Turbo Grafx' , 'tbg' , icon = i111iIi1i1II1 , themeit = OOOiiiiI )
 if 65 - 65: IiiIII111ii + I1111 - OoooooooOO
def OOoOO0o ( url ) :
 o0O0Oo00 = I1 ( url ) . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
 O0Oo0o000oO = re . compile ( '.+?ame="(.+?)".+?rl="(.+?)".+?con="(.+?)".+?anart="(.+?)"description="(.+?)"' ) . findall ( o0O0Oo00 )
 if len ( O0Oo0o000oO ) > 0 :
  for oO0o00oOOooO0 , url , i1i1i1I , oOoo000 , IiI11i1IIiiI in O0Oo0o000oO :
   oO0O0oO0 ( oO0o00oOOooO0 , 'rominstall' , oO0o00oOOooO0 , url , icon = i1i1i1I , fanart = oOoo000 , description = IiI11i1IIiiI , themeit = OOOiiiiI )
  else : wiz . log ( "[ROM Menu] ERROR: Invalid Format." )
 else : wiz . log ( "[ROM Menu] ERROR: URL for apk list not working." )
 if 15 - 15: OOoooooO * o0o0Oo0oooo0 % i1Ii . o0o0Oo0oooo0 . i11IiIiiIIIII
 if 97 - 97: IIIi1i1I
 if 80 - 80: ooOo . IiiIII111ii
 if 47 - 47: i11IiIiiIIIII + OOoooooO + II111iiii % i11iIiiIii
def OOoOoo00Oo ( ) :
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
 if 9 - 9: II111iiii * II111iiii . i11iIiiIii * iIii1I11I1II1
 if 18 - 18: I1111 . II111iiii % o0o0Oo0oooo0 % IiiIII111ii
 if 87 - 87: iIii1I11I1II1 . OoooooooOO * o0o0Oo0oooo0
 if 100 - 100: I1111 / i1IIi - ooOo % IiiIII111ii - iIii1I11I1II1
def i11II ( ) :
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
 if 71 - 71: i1Ii . OO00O0O0O00Oo . I1111
 if 68 - 68: i11iIiiIii % IIIi1i1I * I1111 * i1Ii * II111iiii + O0
 if 66 - 66: i11IiIiiIIIII % oO0 % OoooooooOO
 if 34 - 34: I1I1i1 / iiIIi1IiIi11 % O0 . I1111 . i1IIi
 if 29 - 29: O0 . OO00O0O0O00Oo
def OO0o0oO0O000o ( ) :
 oo00O00oO000o ( 'Genesis Titles A Thru B' , 'rom' , url = oO , icon = i111iIi1i1II1 , themeit = OOOiiiiI )
 oo00O00oO000o ( 'Genesis Titles C Thru D' , 'rom' , url = IIiIi , icon = Oo0O00O000 , themeit = OOOiiiiI )
 oo00O00oO000o ( 'Genesis Titles E Thru G' , 'rom' , url = OOoOooOoOOOoo , icon = i111iIi1i1II1 , themeit = OOOiiiiI )
 oo00O00oO000o ( 'Genesis Titles H Thru L' , 'rom' , url = Iiii1iI1i , icon = i111iIi1i1II1 , themeit = OOOiiiiI )
 oo00O00oO000o ( 'Genesis Titles M Thru O' , 'rom' , url = I1ii1ii11i1I , icon = i111iIi1i1II1 , themeit = OOOiiiiI )
 oo00O00oO000o ( 'Genesis Titles P Thru R' , 'rom' , url = o0OoOO , icon = i111iIi1i1II1 , themeit = OOOiiiiI )
 oo00O00oO000o ( 'Genesis Titles S Thru T' , 'rom' , url = O0O0Oo00 , icon = i111iIi1i1II1 , themeit = OOOiiiiI )
 oo00O00oO000o ( 'Genesis Titles U Thru Z' , 'rom' , url = oOoO00o , icon = i111iIi1i1II1 , themeit = OOOiiiiI )
 if 47 - 47: OO00O0O0O00Oo - I1111 / IiiIII111ii * OoooooooOO / IiiIII111ii . Ooo0O
 if 34 - 34: OOoooooO
 if 27 - 27: OO00O0O0O00Oo + OoooooooOO - o0o0Oo0oooo0
 if 15 - 15: IIIi1i1I / i11IiIiiIIIII * O0 . II111iiii - I1111
 if 90 - 90: IIIi1i1I
def O00OO ( ) :
 oo00O00oO000o ( 'Atari Titles A Thru B' , 'rom' , url = oO00O0 , icon = i111iIi1i1II1 , themeit = OOOiiiiI )
 oo00O00oO000o ( 'Atari Titles C Thru D' , 'rom' , url = IIi1IIIi , icon = Oo0O00O000 , themeit = OOOiiiiI )
 oo00O00oO000o ( 'Atari Titles E Thru G' , 'rom' , url = O00Ooo , icon = i111iIi1i1II1 , themeit = OOOiiiiI )
 oo00O00oO000o ( 'Atari Titles H Thru L' , 'rom' , url = OOOO0OOO , icon = i111iIi1i1II1 , themeit = OOOiiiiI )
 oo00O00oO000o ( 'Atari Titles M Thru O' , 'rom' , url = i1i1ii , icon = i111iIi1i1II1 , themeit = OOOiiiiI )
 oo00O00oO000o ( 'Atari Titles P Thru R' , 'rom' , url = iII1ii1 , icon = i111iIi1i1II1 , themeit = OOOiiiiI )
 oo00O00oO000o ( 'Atari Titles S Thru U' , 'rom' , url = I1i1iiiI1 , icon = i111iIi1i1II1 , themeit = OOOiiiiI )
 oo00O00oO000o ( 'Atari Titles V Thru Z' , 'rom' , url = iIIi , icon = i111iIi1i1II1 , themeit = OOOiiiiI )
 if 94 - 94: iiIIi1IiIi11 + IiiIII111ii % I1I1i1
 if 1 - 1: o0o0Oo0oooo0 % OO00O0O0O00Oo - iii11iiII + IIIi1i1I + O0 * I1I1i1
 if 97 - 97: o0o0Oo0oooo0
 if 77 - 77: i11iIiiIii / OoooooooOO + i1Ii % IIIi1i1I
 if 36 - 36: IIIi1i1I
def o0OO ( ) :
 oo00O00oO000o ( 'N64 Titles A Thru B' , 'rom' , url = oO0o00oo0 , icon = i111iIi1i1II1 , themeit = OOOiiiiI )
 oo00O00oO000o ( 'N64 Titles C Thru E' , 'rom' , url = ii1IIII , icon = Oo0O00O000 , themeit = OOOiiiiI )
 oo00O00oO000o ( 'N64 Titles F Thru J' , 'rom' , url = oO00oOooooo0 , icon = i111iIi1i1II1 , themeit = OOOiiiiI )
 oo00O00oO000o ( 'N64 Titles K Thru M' , 'rom' , url = oOo , icon = i111iIi1i1II1 , themeit = OOOiiiiI )
 oo00O00oO000o ( 'N64 Titles N Thru R' , 'rom' , url = O0OOooOoO , icon = i111iIi1i1II1 , themeit = OOOiiiiI )
 oo00O00oO000o ( 'N64 Titles S Thru T' , 'rom' , url = i1II1I1Iii1 , icon = i111iIi1i1II1 , themeit = OOOiiiiI )
 oo00O00oO000o ( 'N64 Titles V Thru Z' , 'rom' , url = iiI11Iii , icon = i111iIi1i1II1 , themeit = OOOiiiiI )
 if 7 - 7: I1I1i1 / I1111 * i11iIiiIii * O0
 if 79 - 79: iIii1I11I1II1
 if 81 - 81: iii11iiII + iIii1I11I1II1 * OO00O0O0O00Oo - iIii1I11I1II1 . iii11iiII
 if 48 - 48: i11IiIiiIIIII . OoooooooOO . ooOo . o0o0Oo0oooo0 % oO0 / iiIIi1IiIi11
 if 11 - 11: i1IIi % I1111 % iiIIi1IiIi11
def O0Oo0 ( ) :
 oo00O00oO000o ( 'PC Engine And Turbo Grafx Titles A Thru B' , 'rom' , url = O0o0O0 , icon = i111iIi1i1II1 , themeit = OOOiiiiI )
 oo00O00oO000o ( 'PC Engine And Turbo Grafx Titles C Thru E' , 'rom' , url = Ii1II1I11i1 , icon = Oo0O00O000 , themeit = OOOiiiiI )
 oo00O00oO000o ( 'PC Engine And Turbo Grafx Titles F Thru I' , 'rom' , url = oOoooooOoO , icon = i111iIi1i1II1 , themeit = OOOiiiiI )
 oo00O00oO000o ( 'PC Engine And Turbo Grafx Titles J Thru M' , 'rom' , url = Ii111 , icon = i111iIi1i1II1 , themeit = OOOiiiiI )
 oo00O00oO000o ( 'PC Engine And Turbo Grafx Titles N Thru Q' , 'rom' , url = I111i1i1111 , icon = i111iIi1i1II1 , themeit = OOOiiiiI )
 oo00O00oO000o ( 'PC Engine And Turbo Grafx Titles R Thru U' , 'rom' , url = IIII1 , icon = i111iIi1i1II1 , themeit = OOOiiiiI )
 oo00O00oO000o ( 'PC Engine And Turbo Grafx Titles V Thru Z' , 'rom' , url = I1I1i , icon = i111iIi1i1II1 , themeit = OOOiiiiI )
 if 80 - 80: ooOo - iIii1I11I1II1 . iii11iiII + I1111 - OO00O0O0O00Oo
 if 5 - 5: iiIIi1IiIi11
 if 62 - 62: o0o0Oo0oooo0 . OoooooooOO . iii11iiII . I1111 * iiIIi1IiIi11
 if 78 - 78: IIIi1i1I / I1111 - IIIi1i1I * OoooooooOO . o0o0Oo0oooo0
 if 96 - 96: ooOo % i1IIi . I1I1i1 . O0
def Ii1Iii11 ( ) :
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
 if 97 - 97: iii11iiII / IIIi1i1I . II111iiii
 if 44 - 44: IiiIII111ii % i11IiIiiIIIII . OO00O0O0O00Oo
 if 18 - 18: iIii1I11I1II1 + i11IiIiiIIIII * ooOo - iii11iiII / ooOo
 if 78 - 78: i11IiIiiIIIII . i1Ii
def iI1i1II ( ) :
 oo00O00oO000o ( 'Playstation Titles A' , 'rom' , url = oO00oo0o00o0o , icon = i111iIi1i1II1 , themeit = OOOiiiiI )
 oo00O00oO000o ( 'Playstation Titles B' , 'rom' , url = IiIIIIIi , icon = i111iIi1i1II1 , themeit = OOOiiiiI )
 oo00O00oO000o ( 'Playstation Titles C Thru D' , 'rom' , url = IiIi1iIIi1 , icon = i111iIi1i1II1 , themeit = OOOiiiiI )
 oo00O00oO000o ( 'Playstation Titles E Thru F' , 'rom' , url = O0OoO0ooOO0o , icon = i111iIi1i1II1 , themeit = OOOiiiiI )
 oo00O00oO000o ( 'Playstation Titles G Thru J' , 'rom' , url = OoOo0oOooOoOO , icon = i111iIi1i1II1 , themeit = OOOiiiiI )
 oo00O00oO000o ( 'Playstation Titles K Thru N' , 'rom' , url = oo00ooOoO00 , icon = i111iIi1i1II1 , themeit = OOOiiiiI )
 oo00O00oO000o ( 'Playstation Titles O Thru R' , 'rom' , url = o00oOoOo0 , icon = i111iIi1i1II1 , themeit = OOOiiiiI )
 oo00O00oO000o ( 'Playstation Titles S Thru T' , 'rom' , url = o0O0O0ooo0oOO , icon = i111iIi1i1II1 , themeit = OOOiiiiI )
 oo00O00oO000o ( 'Playstation Titles U Thru Z' , 'rom' , url = oo000 , icon = i111iIi1i1II1 , themeit = OOOiiiiI )
 if 14 - 14: OOoooooO - iIii1I11I1II1 / O0 % i1Ii . o0o0Oo0oooo0
def iI1IIi11i1I1 ( url = None ) :
 if not OO == 'http://' :
  if url == None :
   O00oo = wiz . workingURL ( OO )
   OoOo0oO0o = uservar . ADDONFILE
  else :
   O00oo = wiz . workingURL ( url )
   OoOo0oO0o = url
  if O00oo == True :
   o0O0Oo00 = wiz . openURL ( OoOo0oO0o ) . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' ) . replace ( 'repository=""' , 'repository="none"' ) . replace ( 'repositoryurl=""' , 'repositoryurl="http://"' ) . replace ( 'repositoryxml=""' , 'repositoryxml="http://"' )
   O0Oo0o000oO = re . compile ( 'name="(.+?)".+?lugin="(.+?)".+?rl="(.+?)".+?epository="(.+?)".+?epositoryxml="(.+?)".+?epositoryurl="(.+?)".+?con="(.+?)".+?anart="(.+?)".+?dult="(.+?)".+?escription="(.+?)"' ) . findall ( o0O0Oo00 )
   if len ( O0Oo0o000oO ) > 0 :
    ooOO00oOOo000 = 0
    for oO0o00oOOooO0 , o0OoOo00ooO , url , i111i , II1III1i1iiI , I11i11i1 , i1i1i1I , oOoo000 , OooOo00o , IiI11i1IIiiI in O0Oo0o000oO :
     if o0OoOo00ooO . lower ( ) == 'section' :
      ooOO00oOOo000 += 1
      oo00O00oO000o ( "[B]%s[/B]" % oO0o00oOOooO0 , 'addons' , url , description = IiI11i1IIiiI , icon = i1i1i1I , fanart = oOoo000 , themeit = OOoO )
     else :
      if not O0Oo000ooO00 == 'true' and OooOo00o . lower ( ) == 'yes' : continue
      try :
       OOOii1i1iiI = xbmcaddon . Addon ( id = o0OoOo00ooO ) . getAddonInfo ( 'path' )
       if os . path . exists ( OOOii1i1iiI ) :
        oO0o00oOOooO0 = "[COLOR green][Installed][/COLOR] %s" % oO0o00oOOooO0
      except :
       pass
      ooOO00oOOo000 += 1
      iiiii1II ( oO0o00oOOooO0 , 'addoninstall' , o0OoOo00ooO , OoOo0oO0o , description = IiI11i1IIiiI , icon = i1i1i1I , fanart = oOoo000 , themeit = oooOo0OOOoo0 )
     if ooOO00oOOo000 < 1 :
      iiiii1II ( "No addons added to this menu yet!" , '' , themeit = oooOo0OOOoo0 )
   else :
    iiiii1II ( 'Text File not formated correctly!' , '' , themeit = OOoO )
    wiz . log ( "[Addon Menu] ERROR: Invalid Format." )
  else :
   wiz . log ( "[Addon Menu] ERROR: URL for Addon list not working." )
   iiiii1II ( 'Url for txt file not valid' , '' , themeit = OOoO )
   iiiii1II ( '%s' % O00oo , '' , themeit = OOoO )
 else : wiz . log ( "[Addon Menu] No Addon list added." )
 iIi1 ( 'files' , 'viewType' )
 if 94 - 94: i1IIi * i1IIi % II111iiii + iii11iiII
def iIIi11 ( plugin , url ) :
 if not OO == 'http://' :
  O00oo = wiz . workingURL ( url )
  if O00oo == True :
   o0O0Oo00 = wiz . openURL ( url ) . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' ) . replace ( 'repository=""' , 'repository="none"' ) . replace ( 'repositoryurl=""' , 'repositoryurl="http://"' ) . replace ( 'repositoryxml=""' , 'repositoryxml="http://"' )
   O0Oo0o000oO = re . compile ( 'name="(.+?)".+?lugin="%s".+?rl="(.+?)".+?epository="(.+?)".+?epositoryxml="(.+?)".+?epositoryurl="(.+?)".+?con="(.+?)".+?anart="(.+?)".+?dult="(.+?)".+?escription="(.+?)"' % plugin ) . findall ( o0O0Oo00 )
   if len ( O0Oo0o000oO ) > 0 :
    for oO0o00oOOooO0 , url , i111i , II1III1i1iiI , I11i11i1 , i1i1i1I , oOoo000 , OooOo00o , IiI11i1IIiiI in O0Oo0o000oO :
     if os . path . exists ( os . path . join ( O0O , plugin ) ) :
      o0000o0Oo = [ 'Launch Addon' , 'Remove Addon' ]
      ooo0O0OOo0OoO = iiIIIII1i1iI . select ( "[COLOR %s]Addon already installed what would you like to do?[/COLOR]" % iIiIi11 , o0000o0Oo )
      if ooo0O0OOo0OoO == 0 :
       wiz . ebi ( 'RunAddon(%s)' % plugin )
       xbmc . sleep ( 500 )
       return True
      elif ooo0O0OOo0OoO == 1 :
       wiz . cleanHouse ( os . path . join ( O0O , plugin ) )
       try : wiz . removeFolder ( os . path . join ( O0O , plugin ) )
       except : pass
       if iiIIIII1i1iI . yesno ( o0OOO , "[COLOR %s]Would you like to remove the addon_data for:" % iIiIi11 , "[COLOR %s]%s[/COLOR]?[/COLOR]" % ( oOOo0O00o , plugin ) , yeslabel = "[B][COLOR green]Yes Remove[/COLOR][/B]" , nolabel = "[B][COLOR red]No Skip[/COLOR][/B]" ) :
        Ii1i1 ( plugin )
       wiz . refresh ( )
       return True
      else :
       return False
     oOoO00 = os . path . join ( O0O , i111i )
     if not i111i . lower ( ) == 'none' and not os . path . exists ( oOoO00 ) :
      wiz . log ( "Repository not installed, installing it" )
      if iiIIIII1i1iI . yesno ( o0OOO , "[COLOR %s]Would you like to install the repository for [COLOR %s]%s[/COLOR]:" % ( iIiIi11 , oOOo0O00o , plugin ) , "[COLOR %s]%s[/COLOR]?[/COLOR]" % ( oOOo0O00o , i111i ) , yeslabel = "[B][COLOR green]Yes Install[/COLOR][/B]" , nolabel = "[B][COLOR red]No Skip[/COLOR][/B]" ) :
       i1iIi = wiz . parseDOM ( wiz . openURL ( II1III1i1iiI ) , 'addon' , ret = 'version' , attrs = { 'id' : i111i } )
       if len ( i1iIi ) > 0 :
        i1ii1iIIi11i111I = '%s%s-%s.zip' % ( I11i11i1 , i111i , i1iIi [ 0 ] )
        wiz . log ( i1ii1iIIi11i111I )
        if o0OIiII >= 17 : wiz . addonDatabase ( i111i , 1 )
        ii ( i111i , i1ii1iIIi11i111I )
        wiz . ebi ( 'UpdateAddonRepos()' )
        if 13 - 13: oO0 / i11iIiiIii
        wiz . log ( "Installing Addon from Kodi" )
        iIii1I = iii11i1 ( plugin )
        wiz . log ( "Install from Kodi: %s" % iIii1I )
        if iIii1I :
         wiz . refresh ( )
         return True
       else :
        wiz . log ( "[Addon Installer] Repository not installed: Unable to grab url! (%s)" % i111i )
      else : wiz . log ( "[Addon Installer] Repository for %s not installed: %s" % ( plugin , i111i ) )
     elif i111i . lower ( ) == 'none' :
      wiz . log ( "No repository, installing addon" )
      i1IiI1I111iIi = plugin
      IiiIIi1 = url
      ii ( plugin , url )
      wiz . refresh ( )
      return True
     else :
      wiz . log ( "Repository installed, installing addon" )
      iIii1I = iii11i1 ( plugin , False )
      if iIii1I :
       wiz . refresh ( )
       return True
     if os . path . exists ( os . path . join ( O0O , plugin ) ) : return True
     iI1iIiiI = wiz . parseDOM ( wiz . openURL ( II1III1i1iiI ) , 'addon' , ret = 'version' , attrs = { 'id' : plugin } )
     if len ( iI1iIiiI ) > 0 :
      url = "%s%s-%s.zip" % ( url , plugin , iI1iIiiI [ 0 ] )
      wiz . log ( str ( url ) )
      if o0OIiII >= 17 : wiz . addonDatabase ( plugin , 1 )
      ii ( plugin , url )
      wiz . refresh ( )
     else :
      wiz . log ( "no match" ) ; return False
   else : wiz . log ( "[Addon Installer] Invalid Format" )
  else : wiz . log ( "[Addon Installer] Text File: %s" % O00oo )
 else : wiz . log ( "[Addon Installer] Not Enabled." )
 if 95 - 95: iIii1I11I1II1 + Ooo0O * II111iiii + OOoooooO + O0 * i11IiIiiIIIII
def iii11i1 ( plugin , over = True ) :
 if over == True :
  xbmc . sleep ( 2000 )
  if 45 - 45: II111iiii % OOoooooO % i1Ii + oO0 . i1IIi . o0o0Oo0oooo0
 wiz . ebi ( 'RunPlugin(plugin://%s)' % plugin )
 if not wiz . whileWindow ( 'yesnodialog' ) :
  return False
 xbmc . sleep ( 500 )
 if wiz . whileWindow ( 'okdialog' ) :
  return False
 wiz . whileWindow ( 'progressdialog' )
 if os . path . exists ( os . path . join ( O0O , plugin ) ) : return True
 else : return False
 if 87 - 87: OOoooooO . O0 % OO00O0O0O00Oo + oO0 + IiiIII111ii % iIii1I11I1II1
def ii ( name , url ) :
 if not wiz . workingURL ( url ) == True : wiz . LogNotify ( "[COLOR %s]Addon Installer[/COLOR]" % oOOo0O00o , '[COLOR %s]%s:[/COLOR] [COLOR %s]Invalid Zip Url![/COLOR]' % ( oOOo0O00o , name , iIiIi11 ) ) ; return
 if not os . path . exists ( o0o0OOO0o0 ) : os . makedirs ( o0o0OOO0o0 )
 oo00 . create ( o0OOO , '[COLOR %s][B]Downloading:[/B][/COLOR] [COLOR %s]%s[/COLOR]' % ( iIiIi11 , oOOo0O00o , name ) , '' , '[COLOR %s]Please Wait[/COLOR]' % iIiIi11 )
 ii11iIIi = url . split ( '/' )
 i1II1II1iii1i = os . path . join ( o0o0OOO0o0 , ii11iIIi [ - 1 ] )
 try : os . remove ( i1II1II1iii1i )
 except : pass
 downloader . download ( url , i1II1II1iii1i , oo00 )
 oooo = '[COLOR %s][B]Installing:[/B][/COLOR] [COLOR %s]%s[/COLOR]' % ( iIiIi11 , oOOo0O00o , name )
 oo00 . update ( 0 , oooo , '' , '[COLOR %s]Please Wait[/COLOR]' % iIiIi11 )
 O0OO0oOO , ooooO , oO0O0 = extract . all ( i1II1II1iii1i , O0O , oo00 , title = oooo )
 oo00 . update ( 0 , oooo , '' , '[COLOR %s]Installing Dependencies[/COLOR]' % iIiIi11 )
 iI111i11iI1 ( name )
 III1ii ( name , oo00 )
 oo00 . close ( )
 wiz . ebi ( 'UpdateAddonRepos()' )
 wiz . ebi ( 'UpdateLocalAddons()' )
 wiz . refresh ( )
 if 23 - 23: IIIi1i1I * iiIIi1IiIi11
def III1ii ( name , DP = None ) :
 O0oOo00O = os . path . join ( O0O , name , 'addon.xml' )
 if os . path . exists ( O0oOo00O ) :
  i1I1I1i1i1i = open ( O0oOo00O , mode = 'r' ) ; o0O0Oo00 = i1I1I1i1i1i . read ( ) ; i1I1I1i1i1i . close ( ) ;
  O0Oo0o000oO = wiz . parseDOM ( o0O0Oo00 , 'import' , ret = 'addon' )
  for ii1o0oo0Ooooo0 in O0Oo0o000oO :
   if not 'xbmc.python' in ii1o0oo0Ooooo0 :
    if not DP == None :
     DP . update ( 0 , '' , '[COLOR %s]%s[/COLOR]' % ( oOOo0O00o , ii1o0oo0Ooooo0 ) )
    wiz . createTemp ( ii1o0oo0Ooooo0 )
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
    if 87 - 87: II111iiii * oO0 % Ooo0O * Ooo0O
    if 58 - 58: iii11iiII . I1I1i1 + ooOo % Ooo0O - I1111
    if 50 - 50: iiIIi1IiIi11 % II111iiii - OOoooooO . i1IIi + O0 % iiIIi1IiIi11
    if 10 - 10: iiIIi1IiIi11 . i1IIi + IiiIII111ii
def iI111i11iI1 ( addon ) :
 OOOoO000 = os . path . join ( O0O , addon , 'addon.xml' )
 if os . path . exists ( OOOoO000 ) :
  try :
   list = open ( OOOoO000 , mode = 'r' ) ; oOOoOOO0oo0 = list . read ( ) ; list . close ( )
   oO0o00oOOooO0 = wiz . parseDOM ( oOOoOOO0oo0 , 'addon' , ret = 'name' , attrs = { 'id' : addon } )
   i1i1i1I = os . path . join ( O0O , addon , 'icon.png' )
   wiz . LogNotify ( '[COLOR %s]%s[/COLOR]' % ( oOOo0O00o , oO0o00oOOooO0 [ 0 ] ) , '[COLOR %s]Addon Enabled[/COLOR]' % iIiIi11 , '2000' , i1i1i1I )
  except : pass
  if 87 - 87: OOoooooO / o0o0Oo0oooo0 % I1I1i1 * IIIi1i1I
def oOOOoo0o ( url = None ) :
 if not oO0O0OO0O == 'http://' :
  if url == None :
   iiiI1IiIIii = wiz . workingURL ( oO0O0OO0O )
   IIIIiii = uservar . YOUTUBEFILE
  else :
   iiiI1IiIIii = wiz . workingURL ( url )
   IIIIiii = url
  if iiiI1IiIIii == True :
   o0O0Oo00 = wiz . openURL ( IIIIiii ) . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
   O0Oo0o000oO = re . compile ( 'name="(.+?)".+?ection="(.+?)".+?rl="(.+?)".+?con="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( o0O0Oo00 )
   if len ( O0Oo0o000oO ) > 0 :
    for oO0o00oOOooO0 , Ii11Ii1iI , url , i1i1i1I , oOoo000 , IiI11i1IIiiI in O0Oo0o000oO :
     if Ii11Ii1iI . lower ( ) == "yes" :
      oo00O00oO000o ( "[B]%s[/B]" % oO0o00oOOooO0 , 'youtube' , url , description = IiI11i1IIiiI , icon = i1i1i1I , fanart = oOoo000 , themeit = OOoO )
     else :
      iiiii1II ( oO0o00oOOooO0 , 'viewVideo' , url = url , description = IiI11i1IIiiI , icon = i1i1i1I , fanart = oOoo000 , themeit = oooOo0OOOoo0 )
   else : wiz . log ( "[YouTube Menu] ERROR: Invalid Format." )
  else :
   wiz . log ( "[YouTube Menu] ERROR: URL for YouTube list not working." )
   iiiii1II ( 'Url for txt file not valid' , '' , themeit = OOoO )
   iiiii1II ( '%s' % iiiI1IiIIii , '' , themeit = OOoO )
 else : wiz . log ( "[YouTube Menu] No YouTube list added." )
 iIi1 ( 'files' , 'viewType' )
 if 87 - 87: Ooo0O + O0 - i11IiIiiIIIII * iIii1I11I1II1 . OO00O0O0O00Oo % I1I1i1
def Oo0oo0oOO0oOo ( view = None ) :
 IiIII1i = '[B][COLOR green]ON[/COLOR][/B]' ; I11I11i1I1I11 = '[B][COLOR red]OFF[/COLOR][/B]'
 oo0O0o00 = 'true' if ooOooo000oOO == 'true' else 'false'
 I1ii1i = 'true' if Oo0oOOo == 'true' else 'false'
 II11Ii111II1 = 'true' if Oo0OoO00oOO0o == 'true' else 'false'
 O00OOO00Ooo = 'true' if OOO00O == 'true' else 'false'
 OoOOoooO000 = 'true' if oO0Ii1iIiII1ii1 == 'true' else 'false'
 OoO0o000oOo = 'true' if O00O0oOO00O00 == 'true' else 'false'
 Oo00OO00o0oO = 'true' if i1Oo00 == 'true' else 'false'
 iI1I1I1i1i = 'true' if oOooOOOoOo == 'true' else 'false'
 if wiz . Grab_Log ( True ) == False : OOo0O = 0
 else : OOo0O = oOOoooO0O0 ( wiz . Grab_Log ( True ) , True , True )
 if wiz . Grab_Log ( True , True ) == False : ii1O0ooooo000 = 0
 else : ii1O0ooooo000 = oOOoooO0O0 ( wiz . Grab_Log ( True , True ) , True , True )
 OooOoOO0OO = int ( OOo0O ) + int ( ii1O0ooooo000 )
 I1iiIiiii1111 = str ( OooOoOO0OO ) + ' Error(s) Found' if OooOoOO0OO > 0 else 'None Found'
 I1ii1i11i = ': [COLOR red]Not Found[/COLOR]' if not os . path . exists ( I11iii1Ii ) else ": [COLOR green]%s[/COLOR]" % wiz . convertSize ( os . path . getsize ( I11iii1Ii ) )
 if Oo00OO00o0oO == 'true' :
  Oooooo0O00o = 'true'
  II11ii1 = 'true'
  ii1II1II = 'true'
  i11i11II11i = 'true'
  II1Ii1I1i = 'true'
  OOooOooo0OOo0 = 'true'
  oo0o0OoOO0o0 = 'true'
  III1III11II = 'true'
 else :
  Oooooo0O00o = 'true' if i1i == 'true' else 'false'
  II11ii1 = 'true' if iiI111I1iIiI == 'true' else 'false'
  ii1II1II = 'true' if IIIi1I1IIii1II == 'true' else 'false'
  i11i11II11i = 'true' if O0ii1ii1ii == 'true' else 'false'
  II1Ii1I1i = 'true' if oooooOoo0ooo == 'true' else 'false'
  OOooOooo0OOo0 = 'true' if I1I1IiI1 == 'true' else 'false'
  oo0o0OoOO0o0 = 'true' if III1iII1I1ii == 'true' else 'false'
  III1III11II = 'true' if oOOo0 == 'true' else 'false'
 iIi1iI = wiz . getSize ( o0o0OOO0o0 )
 OO0Oo = wiz . getSize ( oOoOooOo0o0 )
 IIiiiiiIiIIi = wiz . getCacheSize ( )
 iiIiiIi1 = iIi1iI + OO0Oo + IIiiiiiIiIIi
 I1Ii11i = [ 'Always' , 'Daily' , '3 Days' , 'Weekly' ]
 oo00O00oO000o ( '[B]Cleaning Tools[/B]' , 'maint' , 'clean' , icon = IiIi11iI , themeit = OOOiiiiI )
 if view == "clean" or oO0Ii1iIiII1ii1 == 'true' :
  iiiii1II ( 'Total Clean Up: [COLOR green][B]%s[/B][/COLOR]' % wiz . convertSize ( iiIiiIi1 ) , 'fullclean' , icon = IiIi11iI , themeit = OOoO )
  iiiii1II ( 'Clear Cache: [COLOR green][B]%s[/B][/COLOR]' % wiz . convertSize ( IIiiiiiIiIIi ) , 'clearcache' , icon = IiIi11iI , themeit = OOoO )
  iiiii1II ( 'Clear Packages: [COLOR green][B]%s[/B][/COLOR]' % wiz . convertSize ( iIi1iI ) , 'clearpackages' , icon = IiIi11iI , themeit = OOoO )
  iiiii1II ( 'Clear Thumbnails: [COLOR green][B]%s[/B][/COLOR]' % wiz . convertSize ( OO0Oo ) , 'clearthumb' , icon = IiIi11iI , themeit = OOoO )
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
  iiiii1II ( 'View Errors in Log: %s' % ( I1iiIiiii1111 ) , 'viewerrorlog' , icon = IiIi11iI , themeit = OOoO )
  iiiii1II ( 'View Log File' , 'viewlog' , icon = IiIi11iI , themeit = OOoO )
  iiiii1II ( 'View Wizard Log File' , 'viewwizlog' , icon = IiIi11iI , themeit = OOoO )
  iiiii1II ( 'Clear Wizard Log File%s' % I1ii1i11i , 'clearwizlog' , icon = IiIi11iI , themeit = OOoO )
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
 iiiii1II ( 'Show All Maintenance: %s' % OoOOoooO000 . replace ( 'true' , IiIII1i ) . replace ( 'false' , I11I11i1I1I11 ) , 'togglesetting' , 'showmaint' , icon = IiIi11iI , themeit = oooOo0OOOoo0 )
 oo00O00oO000o ( '[I]<< Return to Main Menu[/I]' , icon = IiIi11iI , themeit = oooOo0OOOoo0 )
 iiiii1II ( 'Third Party Wizards: %s' % iI1I1I1i1i . replace ( 'true' , IiIII1i ) . replace ( 'false' , I11I11i1I1I11 ) , 'togglesetting' , 'enable3rd' , fanart = OOO00 , icon = IiIi11iI , themeit = OOOiiiiI )
 if iI1I1I1i1i == 'true' :
  I1iIiiiI1 = i1Iii1i1I if not i1Iii1i1I == '' else 'Not Set'
  OOO0O00Oo = IiI111111IIII if not IiI111111IIII == '' else 'Not Set'
  iiIi1IIiI = OOO if not OOO == '' else 'Not Set'
  iiiii1II ( 'Edit Third Party Wizard 1: [COLOR %s]%s[/COLOR]' % ( iIiIi11 , I1iIiiiI1 ) , 'editthird' , '1' , icon = IiIi11iI , themeit = OOoO )
  iiiii1II ( 'Edit Third Party Wizard 2: [COLOR %s]%s[/COLOR]' % ( iIiIi11 , OOO0O00Oo ) , 'editthird' , '2' , icon = IiIi11iI , themeit = OOoO )
  iiiii1II ( 'Edit Third Party Wizard 3: [COLOR %s]%s[/COLOR]' % ( iIiIi11 , iiIi1IIiI ) , 'editthird' , '3' , icon = IiIi11iI , themeit = OOoO )
 iiiii1II ( 'Auto Clean' , '' , fanart = OOO00 , icon = IiIi11iI , themeit = OOOiiiiI )
 iiiii1II ( 'Auto Clean Up On Startup: %s' % oo0O0o00 . replace ( 'true' , IiIII1i ) . replace ( 'false' , I11I11i1I1I11 ) , 'togglesetting' , 'autoclean' , icon = IiIi11iI , themeit = OOoO )
 if oo0O0o00 == 'true' :
  iiiii1II ( '--- Auto Clean Fequency: [B][COLOR green]%s[/COLOR][/B]' % I1Ii11i [ OOoOO0oo0ooO ] , 'changefeq' , icon = IiIi11iI , themeit = OOoO )
  iiiii1II ( '--- Clear Cache on Startup: %s' % I1ii1i . replace ( 'true' , IiIII1i ) . replace ( 'false' , I11I11i1I1I11 ) , 'togglesetting' , 'clearcache' , icon = IiIi11iI , themeit = OOoO )
  iiiii1II ( '--- Clear Packages on Startup: %s' % II11Ii111II1 . replace ( 'true' , IiIII1i ) . replace ( 'false' , I11I11i1I1I11 ) , 'togglesetting' , 'clearpackages' , icon = IiIi11iI , themeit = OOoO )
  iiiii1II ( '--- Clear Old Thumbs on Startup: %s' % O00OOO00Ooo . replace ( 'true' , IiIII1i ) . replace ( 'false' , I11I11i1I1I11 ) , 'togglesetting' , 'clearthumbs' , icon = IiIi11iI , themeit = OOoO )
 iiiii1II ( 'Clear Video Cache' , '' , fanart = OOO00 , icon = IiIi11iI , themeit = OOOiiiiI )
 iiiii1II ( 'Include Video Cache in Clear Cache: %s' % OoO0o000oOo . replace ( 'true' , IiIII1i ) . replace ( 'false' , I11I11i1I1I11 ) , 'togglecache' , 'includevideo' , icon = IiIi11iI , themeit = OOoO )
 if OoO0o000oOo == 'true' :
  iiiii1II ( '--- Include All Video Addons: %s' % Oo00OO00o0oO . replace ( 'true' , IiIII1i ) . replace ( 'false' , I11I11i1I1I11 ) , 'togglecache' , 'includeall' , icon = IiIi11iI , themeit = OOoO )
  iiiii1II ( '--- Include Bob: %s' % Oooooo0O00o . replace ( 'true' , IiIII1i ) . replace ( 'false' , I11I11i1I1I11 ) , 'togglecache' , 'includebob' , icon = IiIi11iI , themeit = OOoO )
  iiiii1II ( '--- Include Phoenix: %s' % II11ii1 . replace ( 'true' , IiIII1i ) . replace ( 'false' , I11I11i1I1I11 ) , 'togglecache' , 'includephoenix' , icon = IiIi11iI , themeit = OOoO )
  iiiii1II ( '--- Include Specto: %s' % ii1II1II . replace ( 'true' , IiIII1i ) . replace ( 'false' , I11I11i1I1I11 ) , 'togglecache' , 'includespecto' , icon = IiIi11iI , themeit = OOoO )
  iiiii1II ( '--- Include Exodus: %s' % II1Ii1I1i . replace ( 'true' , IiIII1i ) . replace ( 'false' , I11I11i1I1I11 ) , 'togglecache' , 'includeexodus' , icon = IiIi11iI , themeit = OOoO )
  iiiii1II ( '--- Include Salts: %s' % oo0o0OoOO0o0 . replace ( 'true' , IiIII1i ) . replace ( 'false' , I11I11i1I1I11 ) , 'togglecache' , 'includesalts' , icon = IiIi11iI , themeit = OOoO )
  iiiii1II ( '--- Include Salts HD Lite: %s' % III1III11II . replace ( 'true' , IiIII1i ) . replace ( 'false' , I11I11i1I1I11 ) , 'togglecache' , 'includesaltslite' , icon = IiIi11iI , themeit = OOoO )
  iiiii1II ( '--- Include One Channel: %s' % OOooOooo0OOo0 . replace ( 'true' , IiIII1i ) . replace ( 'false' , I11I11i1I1I11 ) , 'togglecache' , 'includeonechan' , icon = IiIi11iI , themeit = OOoO )
  iiiii1II ( '--- Include Genesis: %s' % i11i11II11i . replace ( 'true' , IiIII1i ) . replace ( 'false' , I11I11i1I1I11 ) , 'togglecache' , 'includegenesis' , icon = IiIi11iI , themeit = OOoO )
  iiiii1II ( '--- Enable All Video Addons' , 'togglecache' , 'true' , icon = IiIi11iI , themeit = OOoO )
  iiiii1II ( '--- Disable All Video Addons' , 'togglecache' , 'false' , icon = IiIi11iI , themeit = OOoO )
 iIi1 ( 'files' , 'viewType' )
 if 13 - 13: iIii1I11I1II1
def IiIIII1iiIIi ( url = None ) :
 if not OoOoO == 'http://' :
  if url == None :
   i1I1IiI1ii = wiz . workingURL ( OoOoO )
   O00OOoOOOO00O = uservar . ADVANCEDFILE
  else :
   i1I1IiI1ii = wiz . workingURL ( url )
   O00OOoOOOO00O = url
  iiiii1II ( 'Quick Configure AdvancedSettings.xml' , 'autoadvanced' , icon = IiIi11iI , themeit = OOoO )
  if os . path . exists ( I11II1i ) :
   iiiii1II ( 'View Currect AdvancedSettings.xml' , 'currentsettings' , icon = IiIi11iI , themeit = OOoO )
   iiiii1II ( 'Remove Currect AdvancedSettings.xml' , 'removeadvanced' , icon = IiIi11iI , themeit = OOoO )
  if i1I1IiI1ii == True :
   if O0O0ooOOO == 'No' : iiiii1II ( wiz . sep ( ) , '' , icon = IiIi11iI , themeit = OOoO )
   o0O0Oo00 = wiz . openURL ( O00OOoOOOO00O ) . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
   O0Oo0o000oO = re . compile ( 'name="(.+?)".+?ection="(.+?)".+?rl="(.+?)".+?con="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( o0O0Oo00 )
   if len ( O0Oo0o000oO ) > 0 :
    for oO0o00oOOooO0 , Ii11Ii1iI , url , i1i1i1I , oOoo000 , IiI11i1IIiiI in O0Oo0o000oO :
     if Ii11Ii1iI . lower ( ) == "yes" :
      oo00O00oO000o ( "[B]%s[/B]" % oO0o00oOOooO0 , 'advancedsetting' , url , description = IiI11i1IIiiI , icon = i1i1i1I , fanart = oOoo000 , themeit = OOoO )
     else :
      iiiii1II ( oO0o00oOOooO0 , 'writeadvanced' , oO0o00oOOooO0 , url , description = IiI11i1IIiiI , icon = i1i1i1I , fanart = oOoo000 , themeit = oooOo0OOOoo0 )
   else : wiz . log ( "[Advanced Settings] ERROR: Invalid Format." )
  else : wiz . log ( "[Advanced Settings] URL not working: %s" % i1I1IiI1ii )
 else : wiz . log ( "[Advanced Settings] not Enabled" )
 if 72 - 72: ooOo + i1Ii . o0o0Oo0oooo0 + o0o0Oo0oooo0
def ooooOoo0OO ( name , url ) :
 i1I1IiI1ii = wiz . workingURL ( url )
 if i1I1IiI1ii == True :
  if os . path . exists ( I11II1i ) : Oo0 = iiIIIII1i1iI . yesno ( o0OOO , "[COLOR %s]Would you like to overwrite your current Advanced Settings with [COLOR %s]%s[/COLOR]?[/COLOR]" % ( iIiIi11 , oOOo0O00o , name ) , yeslabel = "[B][COLOR green]Overwrite[/COLOR][/B]" , nolabel = "[B][COLOR red]Cancel[/COLOR][/B]" )
  else : Oo0 = iiIIIII1i1iI . yesno ( o0OOO , "[COLOR %s]Would you like to download and install [COLOR %s]%s[/COLOR]?[/COLOR]" % ( iIiIi11 , oOOo0O00o , name ) , yeslabel = "[B][COLOR green]Install[/COLOR][/B]" , nolabel = "[B][COLOR red]Cancel[/COLOR][/B]" )
  if 96 - 96: i11IiIiiIIIII % IiiIII111ii % IIIi1i1I * i11IiIiiIIIII / iii11iiII
  if Oo0 == 1 :
   file = wiz . openURL ( url )
   iiI1iiii1 = open ( I11II1i , 'w' ) ;
   iiI1iiii1 . write ( file )
   iiI1iiii1 . close ( )
   iiIIIII1i1iI . ok ( o0OOO , '[COLOR %s]AdvancedSettings.xml file has been successfully written.  Once you click okay it will force close kodi.[/COLOR]' % iIiIi11 )
   wiz . killxbmc ( True )
  else : wiz . log ( "[Advanced Settings] install canceled" ) ; wiz . LogNotify ( '[COLOR %s]%s[/COLOR]' % ( oOOo0O00o , o0OOO ) , "[COLOR %s]Write Cancelled![/COLOR]" % iIiIi11 ) ; return
 else : wiz . log ( "[Advanced Settings] URL not working: %s" % i1I1IiI1ii ) ; wiz . LogNotify ( '[COLOR %s]%s[/COLOR]' % ( oOOo0O00o , o0OOO ) , "[COLOR %s]URL Not Working[/COLOR]" % iIiIi11 )
 if 36 - 36: iiIIi1IiIi11
def oOooOO ( ) :
 iiI1iiii1 = open ( I11II1i )
 Ii1I1 = iiI1iiii1 . read ( ) . replace ( '\t' , '    ' )
 wiz . TextBox ( o0OOO , Ii1I1 )
 iiI1iiii1 . close ( )
 if 71 - 71: o0o0Oo0oooo0 + iIii1I11I1II1 * IIIi1i1I . OO00O0O0O00Oo % i11iIiiIii % iIii1I11I1II1
def OooOO0oOOo0O ( ) :
 if os . path . exists ( I11II1i ) :
  wiz . removeFile ( I11II1i )
 else : LogNotify ( "[COLOR %s]%s[/COLOR]" % ( oOOo0O00o , o0OOO ) , "[COLOR %s]AdvancedSettings.xml not found[/COLOR]" )
 if 42 - 42: iiIIi1IiIi11 / I1I1i1 + Ooo0O . Ooo0O % iii11iiII
def Ii1III1 ( ) :
 notify . autoConfig ( )
 if 80 - 80: iIii1I11I1II1 . iiIIi1IiIi11 . OO00O0O0O00Oo
def iii1II1iI1IIi ( ) :
 Ii11iiI1 = 'http://whatismyipaddress.com/'
 if not wiz . workingURL ( Ii11iiI1 ) : return 'Unknown' , 'Unknown' , 'Unknown'
 oO0OOOoooO00o0o = wiz . openURL ( Ii11iiI1 ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 if not 'Access Denied' in oO0OOOoooO00o0o :
  I1ii1Ii1 = re . compile ( 'whatismyipaddress.com/ip/(.+?)"' ) . findall ( oO0OOOoooO00o0o )
  OoO = I1ii1Ii1 [ 0 ] if ( len ( I1ii1Ii1 ) > 0 ) else 'Unknown'
  oOiI111I1III = re . compile ( '"font-size:14px;">(.+?)</td>' ) . findall ( oO0OOOoooO00o0o )
  i111IiiI1Ii = oOiI111I1III [ 0 ] if ( len ( oOiI111I1III ) > 0 ) else 'Unknown'
  OooOOOOOo = oOiI111I1III [ 1 ] + ', ' + oOiI111I1III [ 2 ] + ', ' + oOiI111I1III [ 3 ] if ( len ( oOiI111I1III ) > 2 ) else 'Unknown'
  return OoO , i111IiiI1Ii , OooOOOOOo
 else : return 'Unknown' , 'Unknown' , 'Unknown'
 if 50 - 50: OO00O0O0O00Oo + OOoooooO + iiIIi1IiIi11
def ii11iiI11I ( ) :
 OoOooO = [ 'System.FriendlyName' ,
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
 o0oOo00 = [ ] ; ooOO00oOOo000 = 0
 for IiI1III in OoOooO :
  O0O0OOO = wiz . getInfo ( IiI1III )
  I1IIi = 0
  while O0O0OOO == "Busy" and I1IIi < 10 :
   O0O0OOO = wiz . getInfo ( IiI1III ) ; I1IIi += 1 ; wiz . log ( "%s sleep %s" % ( IiI1III , str ( I1IIi ) ) ) ; xbmc . sleep ( 200 )
  o0oOo00 . append ( O0O0OOO )
  ooOO00oOOo000 += 1
 I11I11I11IiIi = o0oOo00 [ 8 ] if 'Una' in o0oOo00 [ 8 ] else wiz . convertSize ( int ( float ( o0oOo00 [ 8 ] [ : - 8 ] ) ) * 1024 * 1024 )
 OOii1ii1i11I1I = o0oOo00 [ 9 ] if 'Una' in o0oOo00 [ 9 ] else wiz . convertSize ( int ( float ( o0oOo00 [ 9 ] [ : - 8 ] ) ) * 1024 * 1024 )
 iiII1iiiiiii = o0oOo00 [ 10 ] if 'Una' in o0oOo00 [ 10 ] else wiz . convertSize ( int ( float ( o0oOo00 [ 10 ] [ : - 8 ] ) ) * 1024 * 1024 )
 iiIiii = wiz . convertSize ( int ( float ( o0oOo00 [ 11 ] [ : - 2 ] ) ) * 1024 * 1024 )
 iiI1ii = wiz . convertSize ( int ( float ( o0oOo00 [ 12 ] [ : - 2 ] ) ) * 1024 * 1024 )
 O0OooOO = wiz . convertSize ( int ( float ( o0oOo00 [ 13 ] [ : - 2 ] ) ) * 1024 * 1024 )
 i1i1 , i111IiiI1Ii , OooOOOOOo = iii1II1iI1IIi ( )
 if 68 - 68: IiiIII111ii - ooOo
 ii1I11II1 = [ ] ; i1i1i1IOOOOOo = [ ] ; OOooO = [ ] ; i1i1Ii1Ii = [ ] ; oOo0OoO = [ ] ; O000O0 = [ ] ; o0O00Oo0o0Oooo0 = [ ]
 if 36 - 36: IIIi1i1I
 IIIi = glob . glob ( os . path . join ( O0O , '*/' ) )
 for Oo0O in sorted ( IIIi , key = lambda ooOO00oOOo000 : ooOO00oOOo000 ) :
  OOOO0Oo = os . path . split ( Oo0O [ : - 1 ] ) [ 1 ]
  if OOOO0Oo == 'packages' : continue
  iIiI1 = os . path . join ( Oo0O , 'addon.xml' )
  if os . path . exists ( iIiI1 ) :
   iiI1iiii1 = open ( iIiI1 )
   Ii1I1 = iiI1iiii1 . read ( )
   I1IiII1I1i1I1 = re . compile ( "<provides>(.+?)</provides>" ) . findall ( Ii1I1 )
   if len ( I1IiII1I1i1I1 ) == 0 :
    if OOOO0Oo . startswith ( 'skin' ) : o0O00Oo0o0Oooo0 . append ( OOOO0Oo )
    if OOOO0Oo . startswith ( 'repo' ) : oOo0OoO . append ( OOOO0Oo )
    else : O000O0 . append ( OOOO0Oo )
   elif not ( I1IiII1I1i1I1 [ 0 ] ) . find ( 'executable' ) == - 1 : i1i1Ii1Ii . append ( OOOO0Oo )
   elif not ( I1IiII1I1i1I1 [ 0 ] ) . find ( 'video' ) == - 1 : OOooO . append ( OOOO0Oo )
   elif not ( I1IiII1I1i1I1 [ 0 ] ) . find ( 'audio' ) == - 1 : i1i1i1IOOOOOo . append ( OOOO0Oo )
   elif not ( I1IiII1I1i1I1 [ 0 ] ) . find ( 'image' ) == - 1 : ii1I11II1 . append ( OOOO0Oo )
   if 28 - 28: Ooo0O + i1Ii % II111iiii / I1111 + i11iIiiIii
 iiiii1II ( '[B]Media Center Info:[/B]' , '' , icon = IiIi11iI , themeit = oooOo0OOOoo0 )
 iiiii1II ( '[COLOR %s]Name:[/COLOR] [COLOR %s]%s[/COLOR]' % ( oOOo0O00o , iIiIi11 , o0oOo00 [ 0 ] ) , '' , icon = IiIi11iI , themeit = OOoO )
 iiiii1II ( '[COLOR %s]Version:[/COLOR] [COLOR %s]%s[/COLOR]' % ( oOOo0O00o , iIiIi11 , o0oOo00 [ 1 ] ) , '' , icon = IiIi11iI , themeit = OOoO )
 iiiii1II ( '[COLOR %s]Platform:[/COLOR] [COLOR %s]%s[/COLOR]' % ( oOOo0O00o , iIiIi11 , wiz . platform ( ) . title ( ) ) , '' , icon = IiIi11iI , themeit = OOoO )
 iiiii1II ( '[COLOR %s]CPU Usage:[/COLOR] [COLOR %s]%s[/COLOR]' % ( oOOo0O00o , iIiIi11 , o0oOo00 [ 2 ] ) , '' , icon = IiIi11iI , themeit = OOoO )
 iiiii1II ( '[COLOR %s]Screen Mode:[/COLOR] [COLOR %s]%s[/COLOR]' % ( oOOo0O00o , iIiIi11 , o0oOo00 [ 3 ] ) , '' , icon = IiIi11iI , themeit = OOoO )
 if 20 - 20: oO0
 iiiii1II ( '[B]Uptime:[/B]' , '' , icon = IiIi11iI , themeit = oooOo0OOOoo0 )
 iiiii1II ( '[COLOR %s]Current Uptime:[/COLOR] [COLOR %s]%s[/COLOR]' % ( oOOo0O00o , iIiIi11 , o0oOo00 [ 6 ] ) , '' , icon = IiIi11iI , themeit = oooOo0OOOoo0 )
 iiiii1II ( '[COLOR %s]Total Uptime:[/COLOR] [COLOR %s]%s[/COLOR]' % ( oOOo0O00o , iIiIi11 , o0oOo00 [ 7 ] ) , '' , icon = IiIi11iI , themeit = oooOo0OOOoo0 )
 if 3 - 3: I1111 * i1IIi . ooOo . O0 - o0o0Oo0oooo0
 iiiii1II ( '[B]Local Storage:[/B]' , '' , icon = IiIi11iI , themeit = oooOo0OOOoo0 )
 iiiii1II ( '[COLOR %s]Used Storage:[/COLOR] [COLOR %s]%s[/COLOR]' % ( oOOo0O00o , iIiIi11 , I11I11I11IiIi ) , '' , icon = IiIi11iI , themeit = oooOo0OOOoo0 )
 iiiii1II ( '[COLOR %s]Free Storage:[/COLOR] [COLOR %s]%s[/COLOR]' % ( oOOo0O00o , iIiIi11 , OOii1ii1i11I1I ) , '' , icon = IiIi11iI , themeit = oooOo0OOOoo0 )
 iiiii1II ( '[COLOR %s]Total Storage:[/COLOR] [COLOR %s]%s[/COLOR]' % ( oOOo0O00o , iIiIi11 , iiII1iiiiiii ) , '' , icon = IiIi11iI , themeit = oooOo0OOOoo0 )
 if 81 - 81: ooOo - iIii1I11I1II1 / ooOo / O0
 iiiii1II ( '[B]Ram Usage:[/B]' , '' , icon = IiIi11iI , themeit = oooOo0OOOoo0 )
 iiiii1II ( '[COLOR %s]Used Memory:[/COLOR] [COLOR %s]%s[/COLOR]' % ( oOOo0O00o , iIiIi11 , iiIiii ) , '' , icon = IiIi11iI , themeit = oooOo0OOOoo0 )
 iiiii1II ( '[COLOR %s]Free Memory:[/COLOR] [COLOR %s]%s[/COLOR]' % ( oOOo0O00o , iIiIi11 , iiI1ii ) , '' , icon = IiIi11iI , themeit = oooOo0OOOoo0 )
 iiiii1II ( '[COLOR %s]Total Memory:[/COLOR] [COLOR %s]%s[/COLOR]' % ( oOOo0O00o , iIiIi11 , O0OooOO ) , '' , icon = IiIi11iI , themeit = oooOo0OOOoo0 )
 if 34 - 34: IiiIII111ii * IiiIII111ii - oO0 - O0 . i11iIiiIii
 iiiii1II ( '[B]Network:[/B]' , '' , icon = IiIi11iI , themeit = oooOo0OOOoo0 )
 iiiii1II ( '[COLOR %s]Local IP:[/COLOR] [COLOR %s]%s[/COLOR]' % ( oOOo0O00o , iIiIi11 , o0oOo00 [ 4 ] ) , '' , icon = IiIi11iI , themeit = oooOo0OOOoo0 )
 iiiii1II ( '[COLOR %s]External IP:[/COLOR] [COLOR %s]%s[/COLOR]' % ( oOOo0O00o , iIiIi11 , i1i1 ) , '' , icon = IiIi11iI , themeit = oooOo0OOOoo0 )
 iiiii1II ( '[COLOR %s]Provider:[/COLOR] [COLOR %s]%s[/COLOR]' % ( oOOo0O00o , iIiIi11 , i111IiiI1Ii ) , '' , icon = IiIi11iI , themeit = oooOo0OOOoo0 )
 iiiii1II ( '[COLOR %s]Location:[/COLOR] [COLOR %s]%s[/COLOR]' % ( oOOo0O00o , iIiIi11 , OooOOOOOo ) , '' , icon = IiIi11iI , themeit = oooOo0OOOoo0 )
 iiiii1II ( '[COLOR %s]MacAddress:[/COLOR] [COLOR %s]%s[/COLOR]' % ( oOOo0O00o , iIiIi11 , o0oOo00 [ 5 ] ) , '' , icon = IiIi11iI , themeit = oooOo0OOOoo0 )
 if 32 - 32: iIii1I11I1II1 . I1111 * IIIi1i1I / iii11iiII . II111iiii - Ooo0O
 IIIiIII11IiiiIi1 = len ( ii1I11II1 ) + len ( i1i1i1IOOOOOo ) + len ( OOooO ) + len ( i1i1Ii1Ii ) + len ( O000O0 ) + len ( o0O00Oo0o0Oooo0 ) + len ( oOo0OoO )
 iiiii1II ( '[B]Addons([COLOR %s]%s[/COLOR]):[/B]' % ( oOOo0O00o , IIIiIII11IiiiIi1 ) , '' , icon = IiIi11iI , themeit = oooOo0OOOoo0 )
 iiiii1II ( '[COLOR %s]Video Addons:[/COLOR] [COLOR %s]%s[/COLOR]' % ( oOOo0O00o , iIiIi11 , str ( len ( OOooO ) ) ) , '' , icon = IiIi11iI , themeit = oooOo0OOOoo0 )
 iiiii1II ( '[COLOR %s]Program Addons:[/COLOR] [COLOR %s]%s[/COLOR]' % ( oOOo0O00o , iIiIi11 , str ( len ( i1i1Ii1Ii ) ) ) , '' , icon = IiIi11iI , themeit = oooOo0OOOoo0 )
 iiiii1II ( '[COLOR %s]Music Addons:[/COLOR] [COLOR %s]%s[/COLOR]' % ( oOOo0O00o , iIiIi11 , str ( len ( i1i1i1IOOOOOo ) ) ) , '' , icon = IiIi11iI , themeit = oooOo0OOOoo0 )
 iiiii1II ( '[COLOR %s]Picture Addons:[/COLOR] [COLOR %s]%s[/COLOR]' % ( oOOo0O00o , iIiIi11 , str ( len ( ii1I11II1 ) ) ) , '' , icon = IiIi11iI , themeit = oooOo0OOOoo0 )
 iiiii1II ( '[COLOR %s]Repositories:[/COLOR] [COLOR %s]%s[/COLOR]' % ( oOOo0O00o , iIiIi11 , str ( len ( oOo0OoO ) ) ) , '' , icon = IiIi11iI , themeit = oooOo0OOOoo0 )
 iiiii1II ( '[COLOR %s]Skins:[/COLOR] [COLOR %s]%s[/COLOR]' % ( oOOo0O00o , iIiIi11 , str ( len ( o0O00Oo0o0Oooo0 ) ) ) , '' , icon = IiIi11iI , themeit = oooOo0OOOoo0 )
 iiiii1II ( '[COLOR %s]Scripts/Modules:[/COLOR] [COLOR %s]%s[/COLOR]' % ( oOOo0O00o , iIiIi11 , str ( len ( O000O0 ) ) ) , '' , icon = IiIi11iI , themeit = oooOo0OOOoo0 )
 if 20 - 20: II111iiii - i11IiIiiIIIII + i1IIi + IiiIII111ii
def i11i11i ( ) :
 IiIII1i = '[COLOR green]ON[/COLOR]' ; I11I11i1I1I11 = '[COLOR red]OFF[/COLOR]'
 iiI1iI = 'true' if o0O0OOO0Ooo == 'true' else 'false'
 Ooo00O0 = 'true' if iiIiII1 == 'true' else 'false'
 OoO0OOoO0 = 'true' if OOO00O0O == 'true' else 'false'
 iiI11i = 'true' if ooOOoooooo == 'true' else 'false'
 o0Oo = 'true' if O0i1II1Iiii1I11 == 'true' else 'false'
 iiI1i = 'true' if II1I == 'true' else 'false'
 i11I = 'true' if IiIIIi1iIi == 'true' else 'false'
 oOo0OoO = 'true' if IIII == 'true' else 'false'
 super = 'true' if iiIiI == 'true' else 'false'
 o0oO0o0oo0O0 = 'true' if o00oooO0Oo == 'true' else 'false'
 if 98 - 98: i1Ii * iIii1I11I1II1 . IiiIII111ii * Ooo0O / oO0 + OOoooooO
 oo00O00oO000o ( 'Keep Trakt Data' , 'trakt' , icon = iIIii , themeit = OOOiiiiI )
 oo00O00oO000o ( 'Keep Real Debrid' , 'realdebrid' , icon = o00O0O , themeit = OOOiiiiI )
 oo00O00oO000o ( 'Keep Login Info' , 'login' , icon = ii1iii1i , themeit = OOOiiiiI )
 iiiii1II ( 'Import Save Data' , 'managedata' , 'import' , icon = I1111i , themeit = OOOiiiiI )
 iiiii1II ( 'Export Save Data' , 'managedata' , 'export' , icon = I1111i , themeit = OOOiiiiI )
 iiiii1II ( '- Click to toggle settings -' , '' , themeit = OOoO )
 iiiii1II ( 'Save Trakt: %s' % iiI1iI . replace ( 'true' , IiIII1i ) . replace ( 'false' , I11I11i1I1I11 ) , 'togglesetting' , 'keeptrakt' , icon = iIIii , themeit = OOOiiiiI )
 iiiii1II ( 'Save Real Debrid: %s' % Ooo00O0 . replace ( 'true' , IiIII1i ) . replace ( 'false' , I11I11i1I1I11 ) , 'togglesetting' , 'keepdebrid' , icon = o00O0O , themeit = OOOiiiiI )
 iiiii1II ( 'Save Login Info: %s' % OoO0OOoO0 . replace ( 'true' , IiIII1i ) . replace ( 'false' , I11I11i1I1I11 ) , 'togglesetting' , 'keeplogin' , icon = ii1iii1i , themeit = OOOiiiiI )
 iiiii1II ( 'Keep \'Sources.xml\': %s' % iiI11i . replace ( 'true' , IiIII1i ) . replace ( 'false' , I11I11i1I1I11 ) , 'togglesetting' , 'keepsources' , icon = I1111i , themeit = OOOiiiiI )
 iiiii1II ( 'Keep \'Profiles.xml\': %s' % iiI1i . replace ( 'true' , IiIII1i ) . replace ( 'false' , I11I11i1I1I11 ) , 'togglesetting' , 'keepprofiles' , icon = I1111i , themeit = OOOiiiiI )
 iiiii1II ( 'Keep \'Advancedsettings.xml\': %s' % o0Oo . replace ( 'true' , IiIII1i ) . replace ( 'false' , I11I11i1I1I11 ) , 'togglesetting' , 'keepadvanced' , icon = I1111i , themeit = OOOiiiiI )
 iiiii1II ( 'Keep \'Favourites.xml\': %s' % i11I . replace ( 'true' , IiIII1i ) . replace ( 'false' , I11I11i1I1I11 ) , 'togglesetting' , 'keepfavourites' , icon = I1111i , themeit = OOOiiiiI )
 iiiii1II ( 'Keep Super Favourites: %s' % super . replace ( 'true' , IiIII1i ) . replace ( 'false' , I11I11i1I1I11 ) , 'togglesetting' , 'keepsuper' , icon = I1111i , themeit = OOOiiiiI )
 iiiii1II ( 'Keep Installed Repo\'s: %s' % oOo0OoO . replace ( 'true' , IiIII1i ) . replace ( 'false' , I11I11i1I1I11 ) , 'togglesetting' , 'keeprepos' , icon = I1111i , themeit = OOOiiiiI )
 iiiii1II ( 'Keep My \'WhiteList\': %s' % o0oO0o0oo0O0 . replace ( 'true' , IiIII1i ) . replace ( 'false' , I11I11i1I1I11 ) , 'togglesetting' , 'keepwhitelist' , icon = I1111i , themeit = OOOiiiiI )
 if o0oO0o0oo0O0 == 'true' :
  iiiii1II ( 'Edit My Whitelist' , 'whitelist' , 'edit' , icon = I1111i , themeit = OOOiiiiI )
  iiiii1II ( 'View My Whitelist' , 'whitelist' , 'view' , icon = I1111i , themeit = OOOiiiiI )
  iiiii1II ( 'Clear My Whitelist' , 'whitelist' , 'clear' , icon = I1111i , themeit = OOOiiiiI )
  iiiii1II ( 'Import My Whitelist' , 'whitelist' , 'import' , icon = I1111i , themeit = OOOiiiiI )
  iiiii1II ( 'Export My Whitelist' , 'whitelist' , 'export' , icon = I1111i , themeit = OOOiiiiI )
 iIi1 ( 'files' , 'viewType' )
 if 25 - 25: IIIi1i1I
def Iii11111iiI ( ) :
 iiI1iI = '[COLOR green]ON[/COLOR]' if o0O0OOO0Ooo == 'true' else '[COLOR red]OFF[/COLOR]'
 o0OOOOoO = str ( O000OOo00oo ) if not O000OOo00oo == '' else 'Trakt hasnt been saved yet.'
 iiiii1II ( '[I]Register FREE Account at http://trakt.tv[/I]' , '' , icon = iIIii , themeit = OOoO )
 iiiii1II ( 'Save Trakt Data: %s' % iiI1iI , 'togglesetting' , 'keeptrakt' , icon = iIIii , themeit = OOoO )
 if o0O0OOO0Ooo == 'true' : iiiii1II ( 'Last Save: %s' % str ( o0OOOOoO ) , '' , icon = iIIii , themeit = OOoO )
 if O0O0ooOOO == 'No' : iiiii1II ( wiz . sep ( ) , '' , icon = iIIii , themeit = OOoO )
 if 70 - 70: II111iiii + OO00O0O0O00Oo + i11iIiiIii - i1IIi / i1Ii
 for iiI1iI in traktit . ORDER :
  oO0o00oOOooO0 = oOOOoo00 [ iiI1iI ] [ 'name' ]
  iI1IIiiIIIII = oOOOoo00 [ iiI1iI ] [ 'path' ]
  i1iIii = oOOOoo00 [ iiI1iI ] [ 'saved' ]
  file = oOOOoo00 [ iiI1iI ] [ 'file' ]
  o0O0ooooooo00 = wiz . getS ( i1iIii )
  I1111ii11IIII = traktit . traktUser ( iiI1iI )
  i1i1i1I = oOOOoo00 [ iiI1iI ] [ 'icon' ] if os . path . exists ( iI1IIiiIIIII ) else iIIii
  oOoo000 = oOOOoo00 [ iiI1iI ] [ 'fanart' ] if os . path . exists ( iI1IIiiIIIII ) else OOO00
  iI1IIIii = I1i11ii11 ( 'saveaddon' , 'Trakt' , iiI1iI )
  IiIi1II111I = I1i11ii11 ( 'save' , 'Trakt' , iiI1iI )
  iI1IIIii . append ( ( oooOo0OOOoo0 % '%s Settings' % oO0o00oOOooO0 , 'RunPlugin(plugin://%s/?mode=opensettings&name=%s&url=trakt)' % ( IiII1IiiIiI1 , iiI1iI ) ) )
  if 80 - 80: IiiIII111ii / iii11iiII
  iiiii1II ( '[+]-> %s' % oO0o00oOOooO0 , '' , icon = i1i1i1I , fanart = oOoo000 , themeit = OOoO )
  if not os . path . exists ( iI1IIiiIIIII ) : iiiii1II ( '[COLOR red]Addon Data: Not Installed[/COLOR]' , '' , icon = i1i1i1I , fanart = oOoo000 , menu = iI1IIIii )
  elif not I1111ii11IIII : iiiii1II ( '[COLOR red]Addon Data: Not Registered[/COLOR]' , 'authtrakt' , iiI1iI , icon = i1i1i1I , fanart = oOoo000 , menu = iI1IIIii )
  else : iiiii1II ( '[COLOR green]Addon Data: %s[/COLOR]' % I1111ii11IIII , 'authtrakt' , iiI1iI , icon = i1i1i1I , fanart = oOoo000 , menu = iI1IIIii )
  if o0O0ooooooo00 == "" :
   if os . path . exists ( file ) : iiiii1II ( '[COLOR red]Saved Data: Save File Found(Import Data)[/COLOR]' , 'importtrakt' , iiI1iI , icon = i1i1i1I , fanart = oOoo000 , menu = IiIi1II111I )
   else : iiiii1II ( '[COLOR red]Saved Data: Not Saved[/COLOR]' , 'savetrakt' , iiI1iI , icon = i1i1i1I , fanart = oOoo000 , menu = IiIi1II111I )
  else : iiiii1II ( '[COLOR green]Saved Data: %s[/COLOR]' % o0O0ooooooo00 , '' , icon = i1i1i1I , fanart = oOoo000 , menu = IiIi1II111I )
  if 21 - 21: Ooo0O - iIii1I11I1II1 - OO00O0O0O00Oo
 if O0O0ooOOO == 'No' : iiiii1II ( wiz . sep ( ) , '' , themeit = OOoO )
 iiiii1II ( 'Save All Trakt Data' , 'savetrakt' , 'all' , icon = iIIii , themeit = OOoO )
 iiiii1II ( 'Recover All Saved Trakt Data' , 'restoretrakt' , 'all' , icon = iIIii , themeit = OOoO )
 iiiii1II ( 'Import Trakt Data' , 'importtrakt' , 'all' , icon = iIIii , themeit = OOoO )
 iiiii1II ( 'Clear All Saved Trakt Data' , 'cleartrakt' , 'all' , icon = iIIii , themeit = OOoO )
 iiiii1II ( 'Clear All Addon Data' , 'addontrakt' , 'all' , icon = iIIii , themeit = OOoO )
 iIi1 ( 'files' , 'viewType' )
 if 1 - 1: ooOo * iii11iiII + IiiIII111ii + ooOo - i11iIiiIii
def O0oO00oOOooO ( ) :
 Ooo00O0 = '[COLOR green]ON[/COLOR]' if iiIiII1 == 'true' else '[COLOR red]OFF[/COLOR]'
 o0OOOOoO = str ( oo0OOo ) if not oo0OOo == '' else 'Real Debrid hasnt been saved yet.'
 iiiii1II ( '[I]http://real-debrid.com is a PAID service.[/I]' , '' , icon = o00O0O , themeit = OOoO )
 iiiii1II ( 'Save Real Debrid Data: %s' % Ooo00O0 , 'togglesetting' , 'keepdebrid' , icon = o00O0O , themeit = OOoO )
 if iiIiII1 == 'true' : iiiii1II ( 'Last Save: %s' % str ( o0OOOOoO ) , '' , icon = o00O0O , themeit = OOoO )
 if O0O0ooOOO == 'No' : iiiii1II ( wiz . sep ( ) , '' , icon = o00O0O , themeit = OOoO )
 if 46 - 46: iIii1I11I1II1 . i11iIiiIii - o0o0Oo0oooo0 % O0 / II111iiii * i1IIi
 for oOIiiIIi in debridit . ORDER :
  oO0o00oOOooO0 = iiIiIIIiiI [ oOIiiIIi ] [ 'name' ]
  iI1IIiiIIIII = iiIiIIIiiI [ oOIiiIIi ] [ 'path' ]
  i1iIii = iiIiIIIiiI [ oOIiiIIi ] [ 'saved' ]
  file = iiIiIIIiiI [ oOIiiIIi ] [ 'file' ]
  o0O0ooooooo00 = wiz . getS ( i1iIii )
  I1111ii11IIII = debridit . debridUser ( oOIiiIIi )
  i1i1i1I = iiIiIIIiiI [ oOIiiIIi ] [ 'icon' ] if os . path . exists ( iI1IIiiIIIII ) else o00O0O
  oOoo000 = iiIiIIIiiI [ oOIiiIIi ] [ 'fanart' ] if os . path . exists ( iI1IIiiIIIII ) else OOO00
  iI1IIIii = I1i11ii11 ( 'saveaddon' , 'Debrid' , oOIiiIIi )
  IiIi1II111I = I1i11ii11 ( 'save' , 'Debrid' , oOIiiIIi )
  iI1IIIii . append ( ( oooOo0OOOoo0 % '%s Settings' % oO0o00oOOooO0 , 'RunPlugin(plugin://%s/?mode=opensettings&name=%s&url=debrid)' % ( IiII1IiiIiI1 , oOIiiIIi ) ) )
  if 96 - 96: i1IIi . i11IiIiiIIIII + IIIi1i1I + oO0 * iii11iiII - II111iiii
  iiiii1II ( '[+]-> %s' % oO0o00oOOooO0 , '' , icon = i1i1i1I , fanart = oOoo000 , themeit = OOoO )
  if not os . path . exists ( iI1IIiiIIIII ) : iiiii1II ( '[COLOR red]Addon Data: Not Installed[/COLOR]' , '' , icon = i1i1i1I , fanart = oOoo000 , menu = iI1IIIii )
  elif not I1111ii11IIII : iiiii1II ( '[COLOR red]Addon Data: Not Registered[/COLOR]' , 'authdebrid' , oOIiiIIi , icon = i1i1i1I , fanart = oOoo000 , menu = iI1IIIii )
  else : iiiii1II ( '[COLOR green]Addon Data: %s[/COLOR]' % I1111ii11IIII , 'authdebrid' , oOIiiIIi , icon = i1i1i1I , fanart = oOoo000 , menu = iI1IIIii )
  if o0O0ooooooo00 == "" :
   if os . path . exists ( file ) : iiiii1II ( '[COLOR red]Saved Data: Save File Found(Import Data)[/COLOR]' , 'importdebrid' , oOIiiIIi , icon = i1i1i1I , fanart = oOoo000 , menu = IiIi1II111I )
   else : iiiii1II ( '[COLOR red]Saved Data: Not Saved[/COLOR]' , 'savedebrid' , oOIiiIIi , icon = i1i1i1I , fanart = oOoo000 , menu = IiIi1II111I )
  else : iiiii1II ( '[COLOR green]Saved Data: %s[/COLOR]' % o0O0ooooooo00 , '' , icon = i1i1i1I , fanart = oOoo000 , menu = IiIi1II111I )
  if 1 - 1: O0
 if O0O0ooOOO == 'No' : iiiii1II ( wiz . sep ( ) , '' , themeit = OOoO )
 iiiii1II ( 'Save All Real Debrid Data' , 'savedebrid' , 'all' , icon = o00O0O , themeit = OOoO )
 iiiii1II ( 'Recover All Saved Real Debrid Data' , 'restoredebrid' , 'all' , icon = o00O0O , themeit = OOoO )
 iiiii1II ( 'Import Real Debrid Data' , 'importdebrid' , 'all' , icon = o00O0O , themeit = OOoO )
 iiiii1II ( 'Clear All Saved Real Debrid Data' , 'cleardebrid' , 'all' , icon = o00O0O , themeit = OOoO )
 iiiii1II ( 'Clear All Addon Data' , 'addondebrid' , 'all' , icon = o00O0O , themeit = OOoO )
 iIi1 ( 'files' , 'viewType' )
 if 40 - 40: OO00O0O0O00Oo - o0o0Oo0oooo0 * i11IiIiiIIIII - i1Ii / o0o0Oo0oooo0
def OO0oo ( ) :
 OoO0OOoO0 = '[COLOR green]ON[/COLOR]' if OOO00O0O == 'true' else '[COLOR red]OFF[/COLOR]'
 o0OOOOoO = str ( ooOOO00Ooo ) if not ooOOO00Ooo == '' else 'Login data hasnt been saved yet.'
 iiiii1II ( '[I]Several of these addons are PAID services.[/I]' , '' , icon = ii1iii1i , themeit = OOoO )
 iiiii1II ( 'Save Login Data: %s' % OoO0OOoO0 , 'togglesetting' , 'keeplogin' , icon = ii1iii1i , themeit = OOoO )
 if OOO00O0O == 'true' : iiiii1II ( 'Last Save: %s' % str ( o0OOOOoO ) , '' , icon = ii1iii1i , themeit = OOoO )
 if O0O0ooOOO == 'No' : iiiii1II ( wiz . sep ( ) , '' , icon = ii1iii1i , themeit = OOoO )
 if 90 - 90: OO00O0O0O00Oo + oO0 / OO00O0O0O00Oo + i1Ii / II111iiii
 for OoO0OOoO0 in loginit . ORDER :
  oO0o00oOOooO0 = iiI1IIIi [ OoO0OOoO0 ] [ 'name' ]
  iI1IIiiIIIII = iiI1IIIi [ OoO0OOoO0 ] [ 'path' ]
  i1iIii = iiI1IIIi [ OoO0OOoO0 ] [ 'saved' ]
  file = iiI1IIIi [ OoO0OOoO0 ] [ 'file' ]
  o0O0ooooooo00 = wiz . getS ( i1iIii )
  I1111ii11IIII = loginit . loginUser ( OoO0OOoO0 )
  i1i1i1I = iiI1IIIi [ OoO0OOoO0 ] [ 'icon' ] if os . path . exists ( iI1IIiiIIIII ) else ii1iii1i
  oOoo000 = iiI1IIIi [ OoO0OOoO0 ] [ 'fanart' ] if os . path . exists ( iI1IIiiIIIII ) else OOO00
  iI1IIIii = I1i11ii11 ( 'saveaddon' , 'Login' , OoO0OOoO0 )
  IiIi1II111I = I1i11ii11 ( 'save' , 'Login' , OoO0OOoO0 )
  iI1IIIii . append ( ( oooOo0OOOoo0 % '%s Settings' % oO0o00oOOooO0 , 'RunPlugin(plugin://%s/?mode=opensettings&name=%s&url=login)' % ( IiII1IiiIiI1 , OoO0OOoO0 ) ) )
  if 63 - 63: iii11iiII * i11IiIiiIIIII
  iiiii1II ( '[+]-> %s' % oO0o00oOOooO0 , '' , icon = i1i1i1I , fanart = oOoo000 , themeit = OOoO )
  if not os . path . exists ( iI1IIiiIIIII ) : iiiii1II ( '[COLOR red]Addon Data: Not Installed[/COLOR]' , '' , icon = i1i1i1I , fanart = oOoo000 , menu = iI1IIIii )
  elif not I1111ii11IIII : iiiii1II ( '[COLOR red]Addon Data: Not Registered[/COLOR]' , 'authlogin' , OoO0OOoO0 , icon = i1i1i1I , fanart = oOoo000 , menu = iI1IIIii )
  else : iiiii1II ( '[COLOR green]Addon Data: %s[/COLOR]' % I1111ii11IIII , 'authlogin' , OoO0OOoO0 , icon = i1i1i1I , fanart = oOoo000 , menu = iI1IIIii )
  if o0O0ooooooo00 == "" :
   if os . path . exists ( file ) : iiiii1II ( '[COLOR red]Saved Data: Save File Found(Import Data)[/COLOR]' , 'importlogin' , OoO0OOoO0 , icon = i1i1i1I , fanart = oOoo000 , menu = IiIi1II111I )
   else : iiiii1II ( '[COLOR red]Saved Data: Not Saved[/COLOR]' , 'savelogin' , OoO0OOoO0 , icon = i1i1i1I , fanart = oOoo000 , menu = IiIi1II111I )
  else : iiiii1II ( '[COLOR green]Saved Data: %s[/COLOR]' % o0O0ooooooo00 , '' , icon = i1i1i1I , fanart = oOoo000 , menu = IiIi1II111I )
  if 22 - 22: oO0 * O0 * iIii1I11I1II1
 if O0O0ooOOO == 'No' : iiiii1II ( wiz . sep ( ) , '' , themeit = OOoO )
 iiiii1II ( 'Save All Login Data' , 'savelogin' , 'all' , icon = ii1iii1i , themeit = OOoO )
 iiiii1II ( 'Recover All Saved Login Data' , 'restorelogin' , 'all' , icon = ii1iii1i , themeit = OOoO )
 iiiii1II ( 'Import Login Data' , 'importlogin' , 'all' , icon = ii1iii1i , themeit = OOoO )
 iiiii1II ( 'Clear All Saved Login Data' , 'clearlogin' , 'all' , icon = ii1iii1i , themeit = OOoO )
 iiiii1II ( 'Clear All Addon Data' , 'addonlogin' , 'all' , icon = ii1iii1i , themeit = OOoO )
 iIi1 ( 'files' , 'viewType' )
 if 77 - 77: II111iiii + I1I1i1
def i1I11Iii1i ( ) :
 if o0OIiII < 17 :
  oOI11 = os . path . join ( OOOO , wiz . latestDB ( 'Addons' ) )
  try :
   os . remove ( oOI11 )
  except Exception , iiIiIiII :
   wiz . log ( "Unable to remove %s, Purging DB" % oOI11 )
   wiz . purgeDb ( oOI11 )
 else :
  xbmc . log ( "Requested Addons.db be removed but doesnt work in Kod17" )
  if 18 - 18: iIii1I11I1II1
def Ii11iI ( ) :
 IIIi = glob . glob ( os . path . join ( O0O , '*/' ) )
 ii111I11Ii = [ ] ; i11IiiI1Ii1 = [ ]
 for Oo0O in sorted ( IIIi , key = lambda ooOO00oOOo000 : ooOO00oOOo000 ) :
  OOOO0Oo = os . path . split ( Oo0O [ : - 1 ] ) [ 1 ]
  if OOOO0Oo in Iii1I1I11iiI1 : continue
  elif OOOO0Oo in OOo0 : continue
  elif OOOO0Oo == 'packages' : continue
  iIiI1 = os . path . join ( Oo0O , 'addon.xml' )
  if os . path . exists ( iIiI1 ) :
   iiI1iiii1 = open ( iIiI1 )
   Ii1I1 = iiI1iiii1 . read ( )
   O0Oo0o000oO = wiz . parseDOM ( Ii1I1 , 'addon' , ret = 'id' )
   if 23 - 23: iiIIi1IiIi11 % OoooooooOO / iIii1I11I1II1 + oO0 / i1IIi / I1I1i1
   oOoO = OOOO0Oo if len ( O0Oo0o000oO ) == 0 else O0Oo0o000oO [ 0 ]
   try :
    OOOii1i1iiI = xbmcaddon . Addon ( id = oOoO )
    ii111I11Ii . append ( OOOii1i1iiI . getAddonInfo ( 'name' ) )
    i11IiiI1Ii1 . append ( oOoO )
   except :
    pass
 if len ( ii111I11Ii ) == 0 :
  wiz . LogNotify ( "[COLOR %s]%s[/COLOR]" % ( oOOo0O00o , o0OOO ) , "[COLOR %s]No Addons To Remove[/COLOR]" % iIiIi11 )
  return
 if o0OIiII > 16 :
  ooo0O0OOo0OoO = iiIIIII1i1iI . multiselect ( "%s: Select the addons you wish to remove." % o0OOO , ii111I11Ii )
 else :
  ooo0O0OOo0OoO = [ ] ; Oo0 = 0
  ii1IIii = [ "-- Click here to Continue --" ] + ii111I11Ii
  while not Oo0 == - 1 :
   Oo0 = iiIIIII1i1iI . select ( "%s: Select the addons you wish to remove." % o0OOO , ii1IIii )
   if Oo0 == - 1 : break
   elif Oo0 == 0 : break
   else :
    IiI11i1I11111 = ( Oo0 - 1 )
    if IiI11i1I11111 in ooo0O0OOo0OoO :
     ooo0O0OOo0OoO . remove ( IiI11i1I11111 )
     ii1IIii [ Oo0 ] = ii111I11Ii [ IiI11i1I11111 ]
    else :
     ooo0O0OOo0OoO . append ( IiI11i1I11111 )
     ii1IIii [ Oo0 ] = "[B][COLOR %s]%s[/COLOR][/B]" % ( oOOo0O00o , ii111I11Ii [ IiI11i1I11111 ] )
 if ooo0O0OOo0OoO == None : return
 if len ( ooo0O0OOo0OoO ) > 0 :
  wiz . addonUpdates ( 'set' )
  for Ii1IIIIIIiI1 in ooo0O0OOo0OoO :
   Ii11IiIiiii1 ( i11IiiI1Ii1 [ Ii1IIIIIIiI1 ] , ii111I11Ii [ Ii1IIIIIIiI1 ] , True )
   if 60 - 60: ooOo % IIIi1i1I / I1I1i1 % IIIi1i1I * i11iIiiIii / iiIIi1IiIi11
  xbmc . sleep ( 500 )
  if 34 - 34: OO00O0O0O00Oo - iii11iiII
  if I11i1I1I == 1 : IIIiIi1iiI = 1
  elif I11i1I1I == 2 : IIIiIi1iiI = 0
  else : IIIiIi1iiI = iiIIIII1i1iI . yesno ( o0OOO , "[COLOR %s]Would you like to [COLOR %s]Force close[/COLOR] kodi or [COLOR %s]Reload Profile[/COLOR]?[/COLOR]" % ( iIiIi11 , oOOo0O00o , oOOo0O00o ) , yeslabel = "[B][COLOR green]Reload Profile[/COLOR][/B]" , nolabel = "[B][COLOR red]Force Close[/COLOR][/B]" )
  if IIIiIi1iiI == 1 : wiz . reloadFix ( 'remove addon' )
  else : wiz . addonUpdates ( 'reset' ) ; wiz . killxbmc ( True )
  if 15 - 15: oO0 . iiIIi1IiIi11
def o0Iiii ( ) :
 if os . path . exists ( ooOOOo0oo0O0 ) :
  iiiii1II ( '[COLOR red][B][REMOVE][/B][/COLOR] All Addon_Data' , 'removedata' , 'all' , themeit = oooOo0OOOoo0 )
  iiiii1II ( '[COLOR red][B][REMOVE][/B][/COLOR] All Addon_Data for Uninstalled Addons' , 'removedata' , 'uninstalled' , themeit = oooOo0OOOoo0 )
  iiiii1II ( '[COLOR red][B][REMOVE][/B][/COLOR] All Empty Folders in Addon_Data' , 'removedata' , 'empty' , themeit = oooOo0OOOoo0 )
  iiiii1II ( '[COLOR red][B][REMOVE][/B][/COLOR] %s Addon_Data' % o0OOO , 'resetaddon' , themeit = oooOo0OOOoo0 )
  if O0O0ooOOO == 'No' : iiiii1II ( wiz . sep ( ) , '' , themeit = OOoO )
  IIIi = glob . glob ( os . path . join ( ooOOOo0oo0O0 , '*/' ) )
  for Oo0O in sorted ( IIIi , key = lambda ooOO00oOOo000 : ooOO00oOOo000 ) :
   OOOO0Oo = Oo0O . replace ( ooOOOo0oo0O0 , '' ) . replace ( '\\' , '' ) . replace ( '/' , '' )
   i1i1i1I = os . path . join ( Oo0O . replace ( ooOOOo0oo0O0 , O0O ) , 'icon.png' )
   oOoo000 = os . path . join ( Oo0O . replace ( ooOOOo0oo0O0 , O0O ) , 'fanart.png' )
   I1i1I = OOOO0Oo
   i1111iI1 = { 'audio.' : '[COLOR orange][AUDIO] [/COLOR]' , 'metadata.' : '[COLOR cyan][METADATA] [/COLOR]' , 'module.' : '[COLOR orange][MODULE] [/COLOR]' , 'plugin.' : '[COLOR blue][PLUGIN] [/COLOR]' , 'program.' : '[COLOR orange][PROGRAM] [/COLOR]' , 'repository.' : '[COLOR gold][REPO] [/COLOR]' , 'script.' : '[COLOR green][SCRIPT] [/COLOR]' , 'service.' : '[COLOR green][SERVICE] [/COLOR]' , 'skin.' : '[COLOR dodgerblue][SKIN] [/COLOR]' , 'video.' : '[COLOR orange][VIDEO] [/COLOR]' , 'weather.' : '[COLOR yellow][WEATHER] [/COLOR]' }
   for Oo0oOOOOo in i1111iI1 :
    I1i1I = I1i1I . replace ( Oo0oOOOOo , i1111iI1 [ Oo0oOOOOo ] )
   if OOOO0Oo in Iii1I1I11iiI1 : I1i1I = '[COLOR green][B][PROTECTED][/B][/COLOR] %s' % I1i1I
   else : I1i1I = '[COLOR red][B][REMOVE][/B][/COLOR] %s' % I1i1I
   iiiii1II ( ' %s' % I1i1I , 'removedata' , OOOO0Oo , icon = i1i1i1I , fanart = oOoo000 , themeit = oooOo0OOOoo0 )
 else :
  iiiii1II ( 'No Addon data folder found.' , '' , themeit = OOoO )
 iIi1 ( 'files' , 'viewType' )
 if 14 - 14: OoooooooOO . I1I1i1 . i11IiIiiIIIII
def I1IIIIIi1IIiI ( ) :
 iiiii1II ( "[I][B][COLOR red]!!Notice: Disabling Some Addons Can Cause Issues!![/COLOR][/B][/I]" , '' , icon = IiIi11iI )
 IIIi = glob . glob ( os . path . join ( O0O , '*/' ) )
 ooOO00oOOo000 = 0
 for Oo0O in sorted ( IIIi , key = lambda ooOO00oOOo000 : ooOO00oOOo000 ) :
  OOOO0Oo = os . path . split ( Oo0O [ : - 1 ] ) [ 1 ]
  if OOOO0Oo in Iii1I1I11iiI1 : continue
  if OOOO0Oo in OOo0 : continue
  III11I11ii = os . path . join ( Oo0O , 'addon.xml' )
  if os . path . exists ( III11I11ii ) :
   ooOO00oOOo000 += 1
   IIIi = Oo0O . replace ( O0O , '' ) [ 1 : - 1 ]
   iiI1iiii1 = open ( III11I11ii )
   Ii1I1 = iiI1iiii1 . read ( ) . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
   O0Oo0o000oO = wiz . parseDOM ( Ii1I1 , 'addon' , ret = 'id' )
   oOooOo00OooO0oO = wiz . parseDOM ( Ii1I1 , 'addon' , ret = 'name' )
   try :
    i1IiI1I111iIi = O0Oo0o000oO [ 0 ]
    oO0o00oOOooO0 = oOooOo00OooO0oO [ 0 ]
   except :
    continue
   try :
    OOOii1i1iiI = xbmcaddon . Addon ( id = i1IiI1I111iIi )
    Ii1iI111 = "[COLOR green][Enabled][/COLOR]"
    O0OoO0oO00 = "false"
   except :
    Ii1iI111 = "[COLOR red][Disabled][/COLOR]"
    O0OoO0oO00 = "true"
    pass
   i1i1i1I = os . path . join ( Oo0O , 'icon.png' ) if os . path . exists ( os . path . join ( Oo0O , 'icon.png' ) ) else iiiiiIIii
   oOoo000 = os . path . join ( Oo0O , 'fanart.jpg' ) if os . path . exists ( os . path . join ( Oo0O , 'fanart.jpg' ) ) else OOO00
   iiiii1II ( "%s %s" % ( Ii1iI111 , oO0o00oOOooO0 ) , 'toggleaddon' , IIIi , O0OoO0oO00 , icon = i1i1i1I , fanart = oOoo000 )
   iiI1iiii1 . close ( )
 if ooOO00oOOo000 == 0 :
  iiiii1II ( "No Addons Found to Enable or Disable." , '' , icon = IiIi11iI )
 iIi1 ( 'files' , 'viewType' )
 if 2 - 2: OO00O0O0O00Oo - oO0 + I1I1i1 * I1111 / iiIIi1IiIi11
def iIIiI11iI1Ii1 ( ) :
 I1Ii11i = [ 'Every Startup' , 'Every Day' , 'Every Three Days' , 'Every Weekly' ]
 o00oo = iiIIIII1i1iI . select ( "[COLOR %s]How often would you list to Auto Clean on Startup?[/COLOR]" % iIiIi11 , I1Ii11i )
 if not o00oo == - 1 :
  wiz . setS ( 'autocleanfeq' , str ( o00oo ) )
  wiz . LogNotify ( '[COLOR %s]Auto Clean Up[/COLOR]' % oOOo0O00o , '[COLOR %s]Fequency Now %s[/COLOR]' % ( iIiIi11 , I1Ii11i [ o00oo ] ) )
  if 70 - 70: i11IiIiiIIIII - Ooo0O / OoooooooOO % OoooooooOO
def oooo0o0OOO0 ( ) :
 iiiii1II ( 'Convert Text Files to 0.1.7' , 'converttext' , themeit = OOOiiiiI )
 iiiii1II ( 'Create QR Code' , 'createqr' , themeit = OOOiiiiI )
 iiiii1II ( 'Test Notifications' , 'testnotify' , themeit = OOOiiiiI )
 iiiii1II ( 'Test Update' , 'testupdate' , themeit = OOOiiiiI )
 iiiii1II ( 'Test First Run' , 'testfirst' , themeit = OOOiiiiI )
 iiiii1II ( 'Test First Run Settings' , 'testfirstrun' , themeit = OOOiiiiI )
 iiiii1II ( 'Test APk' , 'testapk' , themeit = OOOiiiiI )
 if 17 - 17: II111iiii + ooOo
 iIi1 ( 'files' , 'viewType' )
 if 59 - 59: iIii1I11I1II1 % IiiIII111ii . i11iIiiIii
 if 59 - 59: I1I1i1 . IIIi1i1I . IiiIII111ii * o0o0Oo0oooo0 * I1111 + Ooo0O
 if 90 - 90: OO00O0O0O00Oo % Ooo0O - Ooo0O . iIii1I11I1II1 / iii11iiII + i11IiIiiIIIII
 if 89 - 89: IIIi1i1I
def o0OOOOOo00 ( name , type , theme = None , over = False ) :
 if over == False :
  oo0oOO = wiz . checkBuild ( name , 'url' )
  if oo0oOO == False :
   wiz . LogNotify ( "[COLOR %s]%s[/COLOR]" % ( oOOo0O00o , o0OOO ) , "[COLOR %s]Unabled to find build[/COLOR]" % iIiIi11 )
   return
  IIO000oooOO0Oo0 = wiz . workingURL ( oo0oOO )
  if IIO000oooOO0Oo0 == False :
   wiz . LogNotify ( "[COLOR %s]%s[/COLOR]" % ( oOOo0O00o , o0OOO ) , "[COLOR %s]Build Zip Error: %s[/COLOR]" % ( iIiIi11 , IIO000oooOO0Oo0 ) )
   return
 if type == 'gui' :
  if name == O000oo0O :
   if over == True : I1iIiIii = 1
   else : I1iIiIii = iiIIIII1i1iI . yesno ( o0OOO , '[COLOR %s]Would you like to apply the guifix for:' % iIiIi11 , '[COLOR %s]%s[/COLOR]?[/COLOR]' % ( oOOo0O00o , name ) , nolabel = '[B][COLOR red]No, Cancel[/COLOR][/B]' , yeslabel = '[B][COLOR green]Apply Fix[/COLOR][/B]' )
  else :
   I1iIiIii = iiIIIII1i1iI . yesno ( "%s - [COLOR red]WARNING!![/COLOR]" % o0OOO , "[COLOR %s][COLOR %s]%s[/COLOR] community build is not currently installed." % ( iIiIi11 , oOOo0O00o , name ) , "Would you like to apply the guiFix anyways?.[/COLOR]" , nolabel = '[B][COLOR red]No, Cancel[/COLOR][/B]' , yeslabel = '[B][COLOR green]Apply Fix[/COLOR][/B]' )
  if I1iIiIii :
   OO0I1iiI1iiI1i1 = wiz . checkBuild ( name , 'gui' )
   OOOO00OOO00 = name . replace ( '\\' , '' ) . replace ( '/' , '' ) . replace ( ':' , '' ) . replace ( '*' , '' ) . replace ( '?' , '' ) . replace ( '"' , '' ) . replace ( '<' , '' ) . replace ( '>' , '' ) . replace ( '|' , '' )
   if not wiz . workingURL ( OO0I1iiI1iiI1i1 ) == True : wiz . LogNotify ( "[COLOR %s]%s[/COLOR]" % ( oOOo0O00o , o0OOO ) , '[COLOR %s]GuiFix: Invalid Zip Url![/COLOR]' % iIiIi11 ) ; return
   if not os . path . exists ( o0o0OOO0o0 ) : os . makedirs ( o0o0OOO0o0 )
   oo00 . create ( o0OOO , '[COLOR %s][B]Downloading GuiFix:[/B][/COLOR] [COLOR %s]%s[/COLOR]' % ( iIiIi11 , oOOo0O00o , name ) , '' , 'Please Wait' )
   i1II1II1iii1i = os . path . join ( o0o0OOO0o0 , '%s_guisettings.zip' % OOOO00OOO00 )
   try : os . remove ( i1II1II1iii1i )
   except : pass
   downloader . download ( OO0I1iiI1iiI1i1 , i1II1II1iii1i , oo00 )
   xbmc . sleep ( 500 )
   oooo = '[COLOR %s][B]Installing:[/B][/COLOR] [COLOR %s]%s[/COLOR]' % ( iIiIi11 , oOOo0O00o , name )
   oo00 . update ( 0 , oooo , '' , 'Please Wait' )
   extract . all ( i1II1II1iii1i , oOo00Oo00O , oo00 , title = oooo )
   oo00 . close ( )
   wiz . defaultSkin ( )
   wiz . lookandFeelData ( 'save' )
   if I11i1I1I == 1 : IIIiIi1iiI = 1
   elif I11i1I1I == 2 : IIIiIi1iiI = 0
   else : IIIiIi1iiI = iiIIIII1i1iI . yesno ( o0OOO , "[COLOR %s]The Gui fix has been installed.  Would you like to Reload the profile or Force Close Kodi?[/COLOR]" % iIiIi11 , yeslabel = "[B][COLOR red]Reload Profile[/COLOR][/B]" , nolabel = "[B][COLOR green]Force Close[/COLOR][/B]" )
   if IIIiIi1iiI == 1 : wiz . reloadFix ( )
   else : iiIIIII1i1iI . ok ( o0OOO , "[COLOR %s]To save changes you now need to force close Kodi, Press OK to force close Kodi[/COLOR]" % iIiIi11 ) ; wiz . killxbmc ( 'true' )
  else :
   wiz . LogNotify ( "[COLOR %s]%s[/COLOR]" % ( oOOo0O00o , o0OOO ) , '[COLOR %s]GuiFix: Cancelled![/COLOR]' % iIiIi11 )
 elif type == 'fresh' :
  ii1OO0 ( name )
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
  OoOoO00OOoOOOo0 = int ( o0OIiII ) ; oOoO00O = int ( float ( wiz . checkBuild ( name , 'kodi' ) ) )
  if not OoOoO00OOoOOOo0 == oOoO00O :
   if OoOoO00OOoOOOo0 == 16 and oOoO00O <= 15 : IIIIIii1ii11 = False
   else : IIIIIii1ii11 = True
  else : IIIIIii1ii11 = False
  if IIIIIii1ii11 == True :
   I11I1I1i1i = iiIIIII1i1iI . yesno ( "%s - [COLOR red]WARNING!![/COLOR]" % o0OOO , '[COLOR %s]There is a chance that the skin will not appear correctly' % iIiIi11 , 'When installing a %s build on a Kodi %s install' % ( wiz . checkBuild ( name , 'kodi' ) , o0OIiII ) , 'Would you still like to install: [COLOR %s]%s v%s[/COLOR]?[/COLOR]' % ( oOOo0O00o , name , wiz . checkBuild ( name , 'version' ) ) , nolabel = '[B][COLOR red]No, Cancel[/COLOR][/B]' , yeslabel = '[B][COLOR green]Yes, Install[/COLOR][/B]' )
  else :
   if not over == False : I11I1I1i1i = 1
   else : I11I1I1i1i = iiIIIII1i1iI . yesno ( o0OOO , '[COLOR %s]Would you like to Download and Install:' % iIiIi11 , '[COLOR %s]%s v%s[/COLOR]?[/COLOR]' % ( oOOo0O00o , name , wiz . checkBuild ( name , 'version' ) ) , nolabel = '[B][COLOR red]No, Cancel[/COLOR][/B]' , yeslabel = '[B][COLOR green]Yes, Install[/COLOR][/B]' )
  if I11I1I1i1i :
   wiz . clearS ( 'build' )
   OO0I1iiI1iiI1i1 = wiz . checkBuild ( name , 'url' )
   OOOO00OOO00 = name . replace ( '\\' , '' ) . replace ( '/' , '' ) . replace ( ':' , '' ) . replace ( '*' , '' ) . replace ( '?' , '' ) . replace ( '"' , '' ) . replace ( '<' , '' ) . replace ( '>' , '' ) . replace ( '|' , '' )
   if not wiz . workingURL ( OO0I1iiI1iiI1i1 ) == True : wiz . LogNotify ( "[COLOR %s]%s[/COLOR]" % ( oOOo0O00o , o0OOO ) , '[COLOR %s]Build Install: Invalid Zip Url![/COLOR]' % iIiIi11 ) ; return
   if not os . path . exists ( o0o0OOO0o0 ) : os . makedirs ( o0o0OOO0o0 )
   oo00 . create ( o0OOO , '[COLOR %s][B]Downloading:[/B][/COLOR] [COLOR %s]%s v%s[/COLOR]' % ( iIiIi11 , oOOo0O00o , name , wiz . checkBuild ( name , 'version' ) ) , '' , 'Please Wait' )
   i1II1II1iii1i = os . path . join ( o0o0OOO0o0 , '%s.zip' % OOOO00OOO00 )
   try : os . remove ( i1II1II1iii1i )
   except : pass
   wiz . add_one ( name )
   downloader . download ( OO0I1iiI1iiI1i1 , i1II1II1iii1i , oo00 )
   xbmc . sleep ( 500 )
   oooo = '[COLOR %s][B]Installing:[/B][/COLOR] [COLOR %s]%s v%s[/COLOR]' % ( iIiIi11 , oOOo0O00o , name , wiz . checkBuild ( name , 'version' ) )
   oo00 . update ( 0 , oooo , '' , 'Please Wait' )
   O0OO0oOO , ooooO , oO0O0 = extract . all ( i1II1II1iii1i , o00 , oo00 , title = oooo )
   if int ( float ( O0OO0oOO ) ) > 0 :
    wiz . fixmetas ( )
    wiz . lookandFeelData ( 'save' )
    wiz . defaultSkin ( )
    if 74 - 74: O0 % OoooooooOO * Ooo0O + iii11iiII * iiIIi1IiIi11
    wiz . setS ( 'buildname' , name )
    wiz . setS ( 'buildversion' , wiz . checkBuild ( name , 'version' ) )
    wiz . setS ( 'buildtheme' , '' )
    wiz . setS ( 'latestversion' , wiz . checkBuild ( name , 'version' ) )
    wiz . setS ( 'lastbuildcheck' , str ( OOI1iI1ii1II ) )
    wiz . setS ( 'installed' , 'true' )
    wiz . setS ( 'extract' , str ( O0OO0oOO ) )
    wiz . setS ( 'errors' , str ( ooooO ) )
    wiz . log ( 'INSTALLED %s: [ERRORS:%s]' % ( O0OO0oOO , ooooO ) )
    try : os . remove ( i1II1II1iii1i )
    except : pass
    if int ( float ( ooooO ) ) > 0 :
     I1iIiIii = iiIIIII1i1iI . yesno ( o0OOO , '[COLOR %s][COLOR %s]%s v%s[/COLOR]' % ( iIiIi11 , oOOo0O00o , name , wiz . checkBuild ( name , 'version' ) ) , 'Completed: [COLOR %s]%s%s[/COLOR] [Errors:[COLOR %s]%s[/COLOR]]' % ( oOOo0O00o , O0OO0oOO , '%' , oOOo0O00o , ooooO ) , 'Would you like to view the errors?[/COLOR]' , nolabel = '[B][COLOR red]No Thanks[/COLOR][/B]' , yeslabel = '[B][COLOR green]View Errors[/COLOR][/B]' )
     if I1iIiIii :
      if isinstance ( ooooO , unicode ) :
       oO0O0 = oO0O0 . encode ( 'utf-8' )
      wiz . TextBox ( o0OOO , oO0O0 )
    oo00 . close ( )
    OOo00OoO = wiz . themeCount ( name )
    if not OOo00OoO == False :
     o0OOOOOo00 ( name , 'theme' )
    if o0OIiII >= 17 : wiz . addonDatabase ( IiII1IiiIiI1 , 1 )
    if I11i1I1I == 1 : IIIiIi1iiI = 1
    elif I11i1I1I == 2 : IIIiIi1iiI = 0
    else : IIIiIi1iiI = iiIIIII1i1iI . yesno ( o0OOO , "[COLOR %s]Would you like to [COLOR %s]Force close[/COLOR] kodi or [COLOR %s]Reload Profile[/COLOR]?[/COLOR]" % ( iIiIi11 , oOOo0O00o , oOOo0O00o ) , yeslabel = "[B][COLOR red]Reload Profile[/COLOR][/B]" , nolabel = "[B][COLOR green]Force Close[/COLOR][/B]" )
    if IIIiIi1iiI == 1 : wiz . reloadFix ( )
    else : wiz . killxbmc ( True )
   else :
    if isinstance ( ooooO , unicode ) :
     oO0O0 = oO0O0 . encode ( 'utf-8' )
    wiz . TextBox ( "%s: Error Installing Build" % o0OOO , oO0O0 )
  else :
   wiz . LogNotify ( "[COLOR %s]%s[/COLOR]" % ( oOOo0O00o , o0OOO ) , '[COLOR %s]Build Install: Cancelled![/COLOR]' % iIiIi11 )
 elif type == 'theme' :
  if theme == None :
   OOo00OoO = wiz . checkBuild ( name , 'theme' )
   O000OO = [ ]
   if not OOo00OoO == 'http://' and wiz . workingURL ( OOo00OoO ) == True :
    O000OO = wiz . themeCount ( name , False )
    if len ( O000OO ) > 0 :
     if iiIIIII1i1iI . yesno ( o0OOO , "[COLOR %s]The Build [COLOR %s]%s[/COLOR] comes with [COLOR %s]%s[/COLOR] different themes" % ( iIiIi11 , oOOo0O00o , name , oOOo0O00o , len ( O000OO ) ) , "Would you like to install one now?[/COLOR]" , yeslabel = "[B][COLOR green]Install Theme[/COLOR][/B]" , nolabel = "[B][COLOR red]Cancel Themes[/COLOR][/B]" ) :
      wiz . log ( "Theme List: %s " % str ( O000OO ) )
      I1Ii = iiIIIII1i1iI . select ( o0OOO , O000OO )
      wiz . log ( "Theme install selected: %s" % I1Ii )
      if not I1Ii == - 1 : theme = O000OO [ I1Ii ] ; O00Ooo0ooo0 = True
      else : wiz . LogNotify ( "[COLOR %s]%s[/COLOR]" % ( oOOo0O00o , o0OOO ) , '[COLOR %s]Theme Install: Cancelled![/COLOR]' % iIiIi11 ) ; return
     else : wiz . LogNotify ( "[COLOR %s]%s[/COLOR]" % ( oOOo0O00o , o0OOO ) , '[COLOR %s]Theme Install: Cancelled![/COLOR]' % iIiIi11 ) ; return
   else : wiz . LogNotify ( "[COLOR %s]%s[/COLOR]" % ( oOOo0O00o , o0OOO ) , '[COLOR %s]Theme Install: None Found![/COLOR]' % iIiIi11 )
  else : O00Ooo0ooo0 = iiIIIII1i1iI . yesno ( o0OOO , '[COLOR %s]Would you like to install the theme:' % iIiIi11 , '[COLOR %s]%s[/COLOR]' % ( oOOo0O00o , theme ) , 'for [COLOR %s]%s v%s[/COLOR]?[/COLOR]' % ( oOOo0O00o , name , wiz . checkBuild ( name , 'version' ) ) , yeslabel = "[B][COLOR green]Install Theme[/COLOR][/B]" , nolabel = "[B][COLOR red]Cancel Themes[/COLOR][/B]" )
  if O00Ooo0ooo0 :
   oO00o0O00o = wiz . checkTheme ( name , theme , 'url' )
   OOOO00OOO00 = name . replace ( '\\' , '' ) . replace ( '/' , '' ) . replace ( ':' , '' ) . replace ( '*' , '' ) . replace ( '?' , '' ) . replace ( '"' , '' ) . replace ( '<' , '' ) . replace ( '>' , '' ) . replace ( '|' , '' )
   if not wiz . workingURL ( oO00o0O00o ) == True : wiz . LogNotify ( "[COLOR %s]%s[/COLOR]" % ( oOOo0O00o , o0OOO ) , '[COLOR %s]Theme Install: Invalid Zip Url![/COLOR]' % iIiIi11 ) ; return False
   if not os . path . exists ( o0o0OOO0o0 ) : os . makedirs ( o0o0OOO0o0 )
   oo00 . create ( o0OOO , '[COLOR %s][B]Downloading:[/B][/COLOR] [COLOR %s]%s[/COLOR]' % ( iIiIi11 , oOOo0O00o , theme ) , '' , 'Please Wait' )
   i1II1II1iii1i = os . path . join ( o0o0OOO0o0 , '%s.zip' % OOOO00OOO00 )
   try : os . remove ( i1II1II1iii1i )
   except : pass
   downloader . download ( oO00o0O00o , i1II1II1iii1i , oo00 )
   xbmc . sleep ( 500 )
   oo00 . update ( 0 , "" , "Installing %s " % name )
   o0OOOooO00OO00O = False
   if OOOoO000 not in [ "fresh" , "normal" ] :
    o0OOOooO00OO00O = OoOOooO0O ( i1II1II1iii1i ) if not wiz . currSkin ( ) in [ 'skin.confluence' , 'skin.estuary' ] else False
    Ii11iIII = o0ooOO0OOO00o ( i1II1II1iii1i ) if not wiz . currSkin ( ) in [ 'skin.confluence' , 'skin.estuary' ] else False
    if o0OOOooO00OO00O == True :
     wiz . lookandFeelData ( 'save' )
     OoOoO0ooooO0 = 'skin.confluence' if o0OIiII < 17 else 'skin.estuary'
     IIII1ii1 = xbmc . getSkinDir ( )
     if 52 - 52: I1111 - iii11iiII - OOoooooO - I1I1i1 + i1IIi
     skinSwitch . swapSkins ( OoOoO0ooooO0 )
     ooOO00oOOo000 = 0
     xbmc . sleep ( 1000 )
     while not xbmc . getCondVisibility ( "Window.isVisible(yesnodialog)" ) and ooOO00oOOo000 < 150 :
      ooOO00oOOo000 += 1
      xbmc . sleep ( 200 )
     if xbmc . getCondVisibility ( "Window.isVisible(yesnodialog)" ) :
      wiz . ebi ( 'SendClick(11)' )
     else : wiz . LogNotify ( "[COLOR %s]%s[/COLOR]" % ( oOOo0O00o , o0OOO ) , '[COLOR %s]Theme Install: Skin Swap Timed Out![/COLOR]' % iIiIi11 ) ; return
     xbmc . sleep ( 500 )
   oooo = '[COLOR %s][B]Installing Theme:[/B][/COLOR] [COLOR %s]%s[/COLOR]' % ( iIiIi11 , oOOo0O00o , theme )
   oo00 . update ( 0 , oooo , '' , 'Please Wait' )
   O0OO0oOO , ooooO , oO0O0 = extract . all ( i1II1II1iii1i , o00 , oo00 , title = oooo )
   wiz . setS ( 'buildtheme' , theme )
   wiz . log ( 'INSTALLED %s: [ERRORS:%s]' % ( O0OO0oOO , ooooO ) )
   oo00 . close ( )
   if OOOoO000 not in [ "fresh" , "normal" ] :
    wiz . forceUpdate ( )
    if o0OIiII >= 17 : wiz . kodi17Fix ( )
    if Ii11iIII == True :
     wiz . lookandFeelData ( 'save' )
     wiz . defaultSkin ( )
     IIII1ii1 = wiz . getS ( 'defaultskin' )
     skinSwitch . swapSkins ( IIII1ii1 )
     ooOO00oOOo000 = 0
     xbmc . sleep ( 1000 )
     while not xbmc . getCondVisibility ( "Window.isVisible(yesnodialog)" ) and ooOO00oOOo000 < 150 :
      ooOO00oOOo000 += 1
      xbmc . sleep ( 200 )
      if 10 - 10: OoooooooOO / iiIIi1IiIi11 / IIIi1i1I * Ooo0O / iIii1I11I1II1
     if xbmc . getCondVisibility ( "Window.isVisible(yesnodialog)" ) :
      wiz . ebi ( 'SendClick(11)' )
     wiz . lookandFeelData ( 'restore' )
    elif o0OOOooO00OO00O == True :
     skinSwitch . swapSkins ( IIII1ii1 )
     ooOO00oOOo000 = 0
     xbmc . sleep ( 1000 )
     while not xbmc . getCondVisibility ( "Window.isVisible(yesnodialog)" ) and ooOO00oOOo000 < 150 :
      ooOO00oOOo000 += 1
      xbmc . sleep ( 200 )
      if 63 - 63: II111iiii
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
   if 39 - 39: O0 + I1111 / I1I1i1 % i11IiIiiIIIII . iii11iiII * OoooooooOO
def IIIi1IiIiii ( name , url ) :
 if not wiz . workingURL ( url ) :
  LogNotify ( "[COLOR %s]%s[/COLOR]" % ( oOOo0O00o , o0OOO ) , '[COLOR %s]Invalid URL for Build[/COLOR]' % iIiIi11 ) ; return
 type = iiIIIII1i1iI . yesno ( o0OOO , "[COLOR %s]Would you like to preform a [COLOR %s]Fresh Install[/COLOR] or [COLOR %s]Normal Install[/COLOR] for:[/COLOR]" % ( iIiIi11 , oOOo0O00o , oOOo0O00o ) , "[COLOR %s]%s[/COLOR]" % ( oOOo0O00o , name ) , yeslabel = "[B][COLOR green]Fresh Install[/COLOR][/B]" , nolabel = "[B][COLOR red]Normal Install[/COLOR][/B]" )
 if type == 1 :
  ii1OO0 ( 'third' , True )
 wiz . clearS ( 'build' )
 OOOO00OOO00 = name . replace ( '\\' , '' ) . replace ( '/' , '' ) . replace ( ':' , '' ) . replace ( '*' , '' ) . replace ( '?' , '' ) . replace ( '"' , '' ) . replace ( '<' , '' ) . replace ( '>' , '' ) . replace ( '|' , '' )
 if not os . path . exists ( o0o0OOO0o0 ) : os . makedirs ( o0o0OOO0o0 )
 oo00 . create ( o0OOO , '[COLOR %s][B]Downloading:[/B][/COLOR] [COLOR %s]%s[/COLOR]' % ( iIiIi11 , oOOo0O00o , name ) , '' , 'Please Wait' )
 i1II1II1iii1i = os . path . join ( o0o0OOO0o0 , '%s.zip' % OOOO00OOO00 )
 try : os . remove ( i1II1II1iii1i )
 except : pass
 downloader . download ( url , i1II1II1iii1i , oo00 )
 xbmc . sleep ( 500 )
 oooo = '[COLOR %s][B]Installing:[/B][/COLOR] [COLOR %s]%s[/COLOR]' % ( iIiIi11 , oOOo0O00o , name )
 oo00 . update ( 0 , oooo , '' , 'Please Wait' )
 O0OO0oOO , ooooO , oO0O0 = extract . all ( i1II1II1iii1i , o00 , oo00 , title = oooo )
 if int ( float ( O0OO0oOO ) ) > 0 :
  wiz . fixmetas ( )
  wiz . lookandFeelData ( 'save' )
  wiz . defaultSkin ( )
  if 55 - 55: IIIi1i1I
  wiz . setS ( 'installed' , 'true' )
  wiz . setS ( 'extract' , str ( O0OO0oOO ) )
  wiz . setS ( 'errors' , str ( ooooO ) )
  wiz . log ( 'INSTALLED %s: [ERRORS:%s]' % ( O0OO0oOO , ooooO ) )
  try : os . remove ( i1II1II1iii1i )
  except : pass
  if int ( float ( ooooO ) ) > 0 :
   I1iIiIii = iiIIIII1i1iI . yesno ( o0OOO , '[COLOR %s][COLOR %s]%s[/COLOR]' % ( iIiIi11 , oOOo0O00o , name ) , 'Completed: [COLOR %s]%s%s[/COLOR] [Errors:[COLOR %s]%s[/COLOR]]' % ( oOOo0O00o , O0OO0oOO , '%' , oOOo0O00o , ooooO ) , 'Would you like to view the errors?[/COLOR]' , nolabel = '[B][COLOR red]No Thanks[/COLOR][/B]' , yeslabel = '[B][COLOR green]View Errors[/COLOR][/B]' )
   if I1iIiIii :
    if isinstance ( ooooO , unicode ) :
     oO0O0 = oO0O0 . encode ( 'utf-8' )
    wiz . TextBox ( o0OOO , oO0O0 )
 oo00 . close ( )
 if o0OIiII >= 17 : wiz . addonDatabase ( IiII1IiiIiI1 , 1 )
 if I11i1I1I == 1 : IIIiIi1iiI = 1
 elif I11i1I1I == 2 : IIIiIi1iiI = 0
 else : IIIiIi1iiI = iiIIIII1i1iI . yesno ( o0OOO , "[COLOR %s]Would you like to [COLOR %s]Force close[/COLOR] kodi or [COLOR %s]Reload Profile[/COLOR]?[/COLOR]" % ( iIiIi11 , oOOo0O00o , oOOo0O00o ) , yeslabel = "[B][COLOR green]Reload Profile[/COLOR][/B]" , nolabel = "[B][COLOR red]Force Close[/COLOR][/B]" )
 if IIIiIi1iiI == 1 : wiz . reloadFix ( )
 else : wiz . killxbmc ( True )
 if 37 - 37: i1Ii / i11iIiiIii / Ooo0O
def OoOOooO0O ( path ) :
 o0o = zipfile . ZipFile ( path )
 for ii1IIIIiI11 in o0o . infolist ( ) :
  if '/settings.xml' in ii1IIIIiI11 . filename :
   return True
 return False
 if 73 - 73: o0o0Oo0oooo0 % I1I1i1
def o0ooOO0OOO00o ( path ) :
 o0o = zipfile . ZipFile ( path )
 for ii1IIIIiI11 in o0o . infolist ( ) :
  if '/guisettings.xml' in ii1IIIIiI11 . filename :
   return True
 return False
 if 71 - 71: IIIi1i1I - OoooooooOO * Ooo0O * i11IiIiiIIIII + I1I1i1 * oO0
def i1oo00OoO ( apk , url , Brackets ) :
 wiz . log ( apk )
 wiz . log ( url )
 if wiz . platform ( ) == 'android' :
  I1iIiIii = iiIIIII1i1iI . yesno ( o0OOO , "[COLOR %s]Would you like to download and install:" % iIiIi11 , "[COLOR %s]%s[/COLOR]" % ( oOOo0O00o , apk ) , yeslabel = "[B][COLOR green]Download[/COLOR][/B]" , nolabel = "[B][COLOR red]Cancel[/COLOR][/B]" )
  if not I1iIiIii : wiz . LogNotify ( "[COLOR %s]%s[/COLOR]" % ( oOOo0O00o , o0OOO ) , '[COLOR %s]ERROR: Install Cancelled[/COLOR]' % iIiIi11 ) ; return
  ooOi1i111 = apk
  if not os . path . exists ( o0o0OOO0o0 ) : os . makedirs ( o0o0OOO0o0 )
  if not wiz . workingURL ( url ) == True : wiz . LogNotify ( "[COLOR %s]%s[/COLOR]" % ( oOOo0O00o , o0OOO ) , '[COLOR %s]APK Installer: Invalid Apk Url![/COLOR]' % iIiIi11 ) ; return
  oo00 . create ( o0OOO , '[COLOR %s][B]Downloading:[/B][/COLOR] [COLOR %s]%s[/COLOR]' % ( iIiIi11 , oOOo0O00o , ooOi1i111 ) , '' , 'Please Wait' )
  i1II1II1iii1i = os . path . join ( o0o0OOO0o0 , "%s.apk" % apk . replace ( '\\' , '' ) . replace ( '/' , '' ) . replace ( ':' , '' ) . replace ( '*' , '' ) . replace ( '?' , '' ) . replace ( '"' , '' ) . replace ( '<' , '' ) . replace ( '>' , '' ) . replace ( '|' , '' ) )
  try : os . remove ( i1II1II1iii1i )
  except : pass
  downloader . download ( url , i1II1II1iii1i , oo00 )
  xbmc . sleep ( 100 )
  oo00 . close ( )
  if "Brackets" in Brackets :
   Ii11IiI111 = zipfile . ZipFile ( i1II1II1iii1i )
   for file in Ii11IiI111 . namelist ( ) :
    if file . endswith ( '.apk' ) :
     with open ( os . path . join ( o0o0OOO0o0 , os . path . basename ( file ) ) , 'wb' ) as iiI1iiii1 :
      IIiii11ii1II1 = file . split ( '/' ) [ 1 ]
      iiI1iiii1 . write ( Ii11IiI111 . read ( file ) )
      xbmc . sleep ( 500 )
      iiI1iiii1 . close ( )
      try :
       os . remove ( i1II1II1iii1i )
      except :
       pass
      i1II1II1iii1i = os . path . join ( o0o0OOO0o0 , IIiii11ii1II1 )
  iiIIIII1i1iI . ok ( o0OOO , "Launching the APK to be installed" , "Follow the install process to complete." )
  notify . apkInstaller ( apk )
  wiz . ebi ( 'StartAndroidActivity("","android.intent.action.VIEW","application/vnd.android.package-archive","file:' + i1II1II1iii1i + '")' )
 else : wiz . LogNotify ( "[COLOR %s]%s[/COLOR]" % ( oOOo0O00o , o0OOO ) , '[COLOR %s]ERROR: None Android Device[/COLOR]' % iIiIi11 )
 if 97 - 97: i11IiIiiIIIII - I1I1i1 + OOoooooO
 if 89 - 89: IIIi1i1I + i11IiIiiIIIII * i11IiIiiIIIII % i1IIi % i11IiIiiIIIII
 if 96 - 96: I1I1i1 * IIIi1i1I - iii11iiII * I1I1i1 * i1IIi
 if 8 - 8: OOoooooO - Ooo0O + iIii1I11I1II1 + i1IIi * IiiIII111ii - iIii1I11I1II1
def i1IiI1iIIIIIi ( name , url , ) :
 if "NULL" in url :
  iiIIIII1i1iI . ok ( o0OOO , "[COLOR ghostwhite]Not a valid selection, please try again.[/COLOR]" )
  sys . exit ( 1 )
  if 36 - 36: i1Ii
 I1IiI = xbmcgui . DialogProgress ( )
 I1IiI . create ( o0OOO , "" , "" , 'ROM: ' + name )
 OOOO00OOO00 = name . replace ( '\\' , '' ) . replace ( '/' , '' ) . replace ( ':' , '' ) . replace ( '*' , '' ) . replace ( '?' , '' ) . replace ( '"' , '' ) . replace ( '<' , '' ) . replace ( '>' , '' ) . replace ( '|' , '' )
 i1II1II1iii1i = os . path . join ( o0o0OOO0o0 , '%s.zip' % OOOO00OOO00 )
 downloader . download ( url , i1II1II1iii1i , I1IiI )
 I1IiI . update ( 0 )
 extract . all ( i1II1II1iii1i , iI , I1IiI )
 iiIIIII1i1iI . ok ( o0OOO , "[COLOR yellow]Download complete, ROM Location: [/COLOR][COLOR white]" + iI + "[/COLOR]" )
 if 19 - 19: o0o0Oo0oooo0 . I1I1i1 . OoooooooOO
 if 13 - 13: iii11iiII . Ooo0O / II111iiii
 if 43 - 43: iIii1I11I1II1 % I1111
 if 84 - 84: Ooo0O
 if 44 - 44: OoooooooOO * i11iIiiIii / Ooo0O
def OoOoO00o00 ( part , whole ) :
 return 100 * float ( part ) / float ( whole )
 if 51 - 51: Ooo0O * iIii1I11I1II1 . OoooooooOO . IiiIII111ii - iii11iiII / ooOo
def I1i11ii11 ( type , add , name ) :
 if type == 'saveaddon' :
  OoO0ooOI1i1i111Ii1I = [ ]
  oo0 = urllib . quote_plus ( add . lower ( ) . replace ( ' ' , '' ) )
  oooOoOoOO = add . replace ( 'Debrid' , 'Real Debrid' )
  IiiiIiiI = urllib . quote_plus ( name . lower ( ) . replace ( ' ' , '' ) )
  name = name . replace ( 'url' , 'URL Resolver' )
  OoO0ooOI1i1i111Ii1I . append ( ( oooOo0OOOoo0 % name . title ( ) , ' ' ) )
  OoO0ooOI1i1i111Ii1I . append ( ( OOoO % 'Save %s Data' % oooOoOoOO , 'RunPlugin(plugin://%s/?mode=save%s&name=%s)' % ( IiII1IiiIiI1 , oo0 , IiiiIiiI ) ) )
  OoO0ooOI1i1i111Ii1I . append ( ( OOoO % 'Restore %s Data' % oooOoOoOO , 'RunPlugin(plugin://%s/?mode=restore%s&name=%s)' % ( IiII1IiiIiI1 , oo0 , IiiiIiiI ) ) )
  OoO0ooOI1i1i111Ii1I . append ( ( OOoO % 'Clear %s Data' % oooOoOoOO , 'RunPlugin(plugin://%s/?mode=clear%s&name=%s)' % ( IiII1IiiIiI1 , oo0 , IiiiIiiI ) ) )
 elif type == 'save' :
  OoO0ooOI1i1i111Ii1I = [ ]
  oo0 = urllib . quote_plus ( add . lower ( ) . replace ( ' ' , '' ) )
  oooOoOoOO = add . replace ( 'Debrid' , 'Real Debrid' )
  IiiiIiiI = urllib . quote_plus ( name . lower ( ) . replace ( ' ' , '' ) )
  name = name . replace ( 'url' , 'URL Resolver' )
  OoO0ooOI1i1i111Ii1I . append ( ( oooOo0OOOoo0 % name . title ( ) , ' ' ) )
  OoO0ooOI1i1i111Ii1I . append ( ( OOoO % 'Register %s' % oooOoOoOO , 'RunPlugin(plugin://%s/?mode=auth%s&name=%s)' % ( IiII1IiiIiI1 , oo0 , IiiiIiiI ) ) )
  OoO0ooOI1i1i111Ii1I . append ( ( OOoO % 'Save %s Data' % oooOoOoOO , 'RunPlugin(plugin://%s/?mode=save%s&name=%s)' % ( IiII1IiiIiI1 , oo0 , IiiiIiiI ) ) )
  OoO0ooOI1i1i111Ii1I . append ( ( OOoO % 'Restore %s Data' % oooOoOoOO , 'RunPlugin(plugin://%s/?mode=restore%s&name=%s)' % ( IiII1IiiIiI1 , oo0 , IiiiIiiI ) ) )
  OoO0ooOI1i1i111Ii1I . append ( ( OOoO % 'Import %s Data' % oooOoOoOO , 'RunPlugin(plugin://%s/?mode=import%s&name=%s)' % ( IiII1IiiIiI1 , oo0 , IiiiIiiI ) ) )
  OoO0ooOI1i1i111Ii1I . append ( ( OOoO % 'Clear Addon %s Data' % oooOoOoOO , 'RunPlugin(plugin://%s/?mode=addon%s&name=%s)' % ( IiII1IiiIiI1 , oo0 , IiiiIiiI ) ) )
 elif type == 'install' :
  OoO0ooOI1i1i111Ii1I = [ ]
  IiiiIiiI = urllib . quote_plus ( name )
  OoO0ooOI1i1i111Ii1I . append ( ( oooOo0OOOoo0 % name , 'RunAddon(%s, ?mode=viewbuild&name=%s)' % ( IiII1IiiIiI1 , IiiiIiiI ) ) )
  OoO0ooOI1i1i111Ii1I . append ( ( OOoO % 'Fresh Install' , 'RunPlugin(plugin://%s/?mode=install&name=%s&url=fresh)' % ( IiII1IiiIiI1 , IiiiIiiI ) ) )
  OoO0ooOI1i1i111Ii1I . append ( ( OOoO % 'Normal Install' , 'RunPlugin(plugin://%s/?mode=install&name=%s&url=normal)' % ( IiII1IiiIiI1 , IiiiIiiI ) ) )
  OoO0ooOI1i1i111Ii1I . append ( ( OOoO % 'Apply guiFix' , 'RunPlugin(plugin://%s/?mode=install&name=%s&url=gui)' % ( IiII1IiiIiI1 , IiiiIiiI ) ) )
  OoO0ooOI1i1i111Ii1I . append ( ( OOoO % 'Build Information' , 'RunPlugin(plugin://%s/?mode=buildinfo&name=%s)' % ( IiII1IiiIiI1 , IiiiIiiI ) ) )
 OoO0ooOI1i1i111Ii1I . append ( ( oooOo0OOOoo0 % '%s Settings' % o0OOO , 'RunPlugin(plugin://%s/?mode=settings)' % IiII1IiiIiI1 ) )
 return OoO0ooOI1i1i111Ii1I
 if 51 - 51: II111iiii / Ooo0O / ooOo + i11iIiiIii
def iiI1ii1Iii ( state ) :
 Ii1I1IIIiI1i = [ 'includevideo' , 'includeall' , 'includebob' , 'includephoenix' , 'includespecto' , 'includegenesis' , 'includeexodus' , 'includeonechan' , 'includesalts' , 'includesaltslite' ]
 o0Oo00oOO = [ 'Include Video Addons' , 'Include All Addons' , 'Include Bob' , 'Include Phoenix' , 'Include Specto' , 'Include Genesis' , 'Include Exodus' , 'Include One Channel' , 'Include Salts' , 'Include Salts Lite HD' ]
 if state in [ 'true' , 'false' ] :
  for ii1IIIIiI11 in Ii1I1IIIiI1i :
   wiz . setS ( ii1IIIIiI11 , state )
 else :
  if not state in [ 'includevideo' , 'includeall' ] and wiz . getS ( 'includeall' ) == 'true' :
   try :
    ii1IIIIiI11 = o0Oo00oOO [ Ii1I1IIIiI1i . index ( state ) ]
    iiIIIII1i1iI . ok ( o0OOO , "[COLOR %s]You will need to turn off [COLOR %s]Include All Addons[/COLOR] to disable[/COLOR] [COLOR %s]%s[/COLOR]" % ( iIiIi11 , oOOo0O00o , oOOo0O00o , ii1IIIIiI11 ) )
   except :
    wiz . LogNotify ( "[COLOR %s]Toggle Cache[/COLOR]" % oOOo0O00o , "[COLOR %s]Invalid id: %s[/COLOR]" % ( iIiIi11 , state ) )
  else :
   O0oo = 'true' if wiz . getS ( state ) == 'false' else 'false'
   wiz . setS ( state , O0oo )
   if 56 - 56: i1Ii * OO00O0O0O00Oo
def O00oO0O ( url ) :
 if 'watch?v=' in url :
  Ii1I1 , IiiI111I11 = url . split ( '?' )
  oO0Ooooo000 = IiiI111I11 . split ( '&' )
  for ii1IIIIiI11 in oO0Ooooo000 :
   if ii1IIIIiI11 . startswith ( 'v=' ) :
    url = ii1IIIIiI11 [ 2 : ]
    break
   else : continue
 elif 'embed' in url or 'youtu.be' in url :
  Ii1I1 = url . split ( '/' )
  if len ( Ii1I1 [ - 1 ] ) > 5 :
   url = Ii1I1 [ - 1 ]
  elif len ( Ii1I1 [ - 2 ] ) > 5 :
   url = Ii1I1 [ - 2 ]
 wiz . log ( "YouTube URL: %s" % url )
 yt . PlayVideo ( url )
 if 46 - 46: ooOo - i11IiIiiIIIII / OoooooooOO - i1IIi . i11iIiiIii
def Ii1Ii1IiIIIi1 ( ) :
 OOoo00 = wiz . Grab_Log ( True )
 I1I1 = wiz . Grab_Log ( True , True )
 O0OOO0ooO00o = 0 ; I1iii1 = OOoo00
 if not I1I1 == False and not OOoo00 == False :
  O0OOO0ooO00o = iiIIIII1i1iI . select ( o0OOO , [ "View %s" % OOoo00 . replace ( iI11iiiI1II , "" ) , "View %s" % I1I1 . replace ( iI11iiiI1II , "" ) ] )
  if O0OOO0ooO00o == - 1 : wiz . LogNotify ( '[COLOR %s]View Log[/COLOR]' % oOOo0O00o , '[COLOR %s]View Log Cancelled![/COLOR]' % iIiIi11 ) ; return
 elif OOoo00 == False and I1I1 == False :
  wiz . LogNotify ( '[COLOR %s]View Log[/COLOR]' % oOOo0O00o , '[COLOR %s]No Log File Found![/COLOR]' % iIiIi11 )
  return
 elif not OOoo00 == False : O0OOO0ooO00o = 0
 elif not I1I1 == False : O0OOO0ooO00o = 1
 if 19 - 19: IIIi1i1I % OoooooooOO . OoooooooOO
 I1iii1 = OOoo00 if O0OOO0ooO00o == 0 else I1I1
 IiIiI11IIi11Iii = wiz . Grab_Log ( False ) if O0OOO0ooO00o == 0 else wiz . Grab_Log ( False , True )
 if 9 - 9: IIIi1i1I
 wiz . TextBox ( "%s - %s" % ( o0OOO , I1iii1 ) , IiIiI11IIi11Iii )
 if 2 - 2: iIii1I11I1II1 * ooOo % i1IIi % oO0 + OoooooooOO + ooOo
def oOOoooO0O0 ( log = None , count = None , all = None ) :
 if log == None :
  OOoo00 = wiz . Grab_Log ( True )
  I1I1 = wiz . Grab_Log ( True , True )
  if not I1I1 == False and not OOoo00 == False :
   O0OOO0ooO00o = iiIIIII1i1iI . select ( o0OOO , [ "View %s: %s error(s)" % ( OOoo00 . replace ( iI11iiiI1II , "" ) , oOOoooO0O0 ( OOoo00 , True , True ) ) , "View %s: %s error(s)" % ( I1I1 . replace ( iI11iiiI1II , "" ) , oOOoooO0O0 ( I1I1 , True , True ) ) ] )
   if O0OOO0ooO00o == - 1 : wiz . LogNotify ( '[COLOR %s]View Log[/COLOR]' % oOOo0O00o , '[COLOR %s]View Log Cancelled![/COLOR]' % iIiIi11 ) ; return
  elif OOoo00 == False and I1I1 == False :
   wiz . LogNotify ( '[COLOR %s]View Log[/COLOR]' % oOOo0O00o , '[COLOR %s]No Log File Found![/COLOR]' % iIiIi11 )
   return
  elif not OOoo00 == False : O0OOO0ooO00o = 0
  elif not I1I1 == False : O0OOO0ooO00o = 1
  log = OOoo00 if O0OOO0ooO00o == 0 else I1I1
 if log == False :
  if count == None :
   wiz . LogNotify ( "[COLOR %s]%s[/COLOR]" % ( oOOo0O00o , o0OOO ) , "[COLOR %s]Log File not Found[/COLOR]" % iIiIi11 )
   return False
  else :
   return 0
 else :
  if os . path . exists ( log ) :
   iiI1iiii1 = open ( log , mode = 'r' ) ; Ii1I1 = iiI1iiii1 . read ( ) . replace ( '\n' , '' ) . replace ( '\r' , '' ) ; iiI1iiii1 . close ( )
   O0Oo0o000oO = re . compile ( "-->Python callback/script returned the following error<--(.+?)-->End of Python script error report<--" ) . findall ( Ii1I1 )
   if not count == None :
    if all == None :
     ooOO00oOOo000 = 0
     for ii1IIIIiI11 in O0Oo0o000oO :
      if IiII1IiiIiI1 in ii1IIIIiI11 : ooOO00oOOo000 += 1
     return ooOO00oOOo000
    else : return len ( O0Oo0o000oO )
   if len ( O0Oo0o000oO ) > 0 :
    ooOO00oOOo000 = 0 ; IiIiI11IIi11Iii = ""
    for ii1IIIIiI11 in O0Oo0o000oO :
     if all == None and not IiII1IiiIiI1 in ii1IIIIiI11 : continue
     else :
      ooOO00oOOo000 += 1
      IiIiI11IIi11Iii += "[COLOR red]Error Number %s[/COLOR]\n(PythonToCppException) : -->Python callback/script returned the following error<--%s-->End of Python script error report<--\n\n" % ( ooOO00oOOo000 , ii1IIIIiI11 . replace ( '                                          ' , '\n' ) . replace ( '\\\\' , '\\' ) . replace ( o00 , '' ) )
    if ooOO00oOOo000 > 0 :
     wiz . TextBox ( o0OOO , IiIiI11IIi11Iii )
    else : wiz . LogNotify ( o0OOO , "No Errors Found in Log" )
   else : wiz . LogNotify ( o0OOO , "No Errors Found in Log" )
  else : wiz . LogNotify ( o0OOO , "Log File not Found" )
  if 16 - 16: iii11iiII
oooO0o0oOoO = 10
I11iii = 92
IIi111 = 1
oO0o0o0O = 2
I111ii1iI = 3
i1IiI1ii1i = 4
i1I1I1I = 104
iII1III = 105
O0oo0oO00o = 107
I1ii111i1ii1 = 7
o0Ii11iIiiI = 110
o000 = 100
i11ii1 = 108
if 4 - 4: i11iIiiIii - iii11iiII % oO0 * OO00O0O0O00Oo % I1I1i1
def o0OoOoo ( default = None ) :
 class o0OoOoo ( xbmcgui . WindowXMLDialog ) :
  def __init__ ( self , * args , ** kwargs ) :
   self . default = kwargs [ 'default' ]
   if 75 - 75: iiIIi1IiIi11 * ooOo + iiIIi1IiIi11 - OoooooooOO
  def onInit ( self ) :
   self . title = 101
   self . msg = 102
   self . scrollbar = 103
   self . upload = 201
   self . kodi = 202
   self . kodiold = 203
   self . wizard = 204
   self . okbutton = 205
   iiI1iiii1 = open ( self . default , 'r' )
   self . logmsg = iiI1iiii1 . read ( )
   iiI1iiii1 . close ( )
   self . titlemsg = "%s: %s" % ( o0OOO , self . default . replace ( iI11iiiI1II , '' ) . replace ( o0 , '' ) )
   self . showdialog ( )
   if 81 - 81: iIii1I11I1II1 / IIIi1i1I . i11iIiiIii * II111iiii
  def showdialog ( self ) :
   self . getControl ( self . title ) . setLabel ( self . titlemsg )
   self . getControl ( self . msg ) . setText ( wiz . highlightText ( self . logmsg ) )
   self . setFocusId ( self . scrollbar )
   if 55 - 55: oO0
  def onClick ( self , controlId ) :
   if controlId == self . okbutton : self . close ( )
   elif controlId == self . upload : self . close ( ) ; uploadLog . Main ( )
   elif controlId == self . kodi :
    oOoo0OO0 = wiz . Grab_Log ( False )
    iiIiIi1111iI1 = wiz . Grab_Log ( True )
    if oOoo0OO0 == False :
     self . titlemsg = "%s: View Log Error" % o0OOO
     self . getControl ( self . msg ) . setText ( "Log File Does Not Exists!" )
    else :
     self . titlemsg = "%s: %s" % ( o0OOO , iiIiIi1111iI1 . replace ( iI11iiiI1II , '' ) )
     self . getControl ( self . title ) . setLabel ( self . titlemsg )
     self . getControl ( self . msg ) . setText ( wiz . highlightText ( oOoo0OO0 ) )
     self . setFocusId ( self . scrollbar )
   elif controlId == self . kodiold :
    oOoo0OO0 = wiz . Grab_Log ( False , True )
    iiIiIi1111iI1 = wiz . Grab_Log ( True , True )
    if oOoo0OO0 == False :
     self . titlemsg = "%s: View Log Error" % o0OOO
     self . getControl ( self . msg ) . setText ( "Log File Does Not Exists!" )
    else :
     self . titlemsg = "%s: %s" % ( o0OOO , iiIiIi1111iI1 . replace ( iI11iiiI1II , '' ) )
     self . getControl ( self . title ) . setLabel ( self . titlemsg )
     self . getControl ( self . msg ) . setText ( wiz . highlightText ( oOoo0OO0 ) )
     self . setFocusId ( self . scrollbar )
   elif controlId == self . wizard :
    oOoo0OO0 = wiz . Grab_Log ( False , False , True )
    iiIiIi1111iI1 = wiz . Grab_Log ( True , False , True )
    if oOoo0OO0 == False :
     self . titlemsg = "%s: View Log Error" % o0OOO
     self . getControl ( self . msg ) . setText ( "Log File Does Not Exists!" )
    else :
     self . titlemsg = "%s: %s" % ( o0OOO , iiIiIi1111iI1 . replace ( o0 , '' ) )
     self . getControl ( self . title ) . setLabel ( self . titlemsg )
     self . getControl ( self . msg ) . setText ( wiz . highlightText ( oOoo0OO0 ) )
     self . setFocusId ( self . scrollbar )
     if 11 - 11: oO0 . oO0 + II111iiii * o0o0Oo0oooo0 . i1Ii
  def onAction ( self , action ) :
   if action == oooO0o0oOoO : self . close ( )
   elif action == I11iii : self . close ( )
 if default == None : default = wiz . Grab_Log ( True )
 I1I1i1I1I1I1 = o0OoOoo ( "LogViewer.xml" , I1ii11iIi11i . getAddonInfo ( 'path' ) , 'DefaultSkin' , default = default )
 I1I1i1I1I1I1 . doModal ( )
 del I1I1i1I1I1I1
 if 34 - 34: I1111 * IiiIII111ii * Ooo0O
def Ii11IiIiiii1 ( addon , name , over = False ) :
 if not over == False :
  I1iIiIii = 1
 else :
  I1iIiIii = iiIIIII1i1iI . yesno ( o0OOO , '[COLOR %s]Are you sure you want to delete the addon:' % iIiIi11 , 'Name: [COLOR %s]%s[/COLOR]' % ( oOOo0O00o , name ) , 'ID: [COLOR %s]%s[/COLOR][/COLOR]' % ( oOOo0O00o , addon ) , yeslabel = '[B][COLOR green]Remove Addon[/COLOR][/B]' , nolabel = '[B][COLOR red]Don\'t Remove[/COLOR][/B]' )
 if I1iIiIii == 1 :
  Oo0O = os . path . join ( O0O , addon )
  wiz . log ( "Removing Addon %s" % addon )
  wiz . cleanHouse ( Oo0O )
  xbmc . sleep ( 200 )
  try : shutil . rmtree ( Oo0O )
  except Exception , iiIiIiII : wiz . log ( "Error removing %s" % addon , xbmc . LOGNOTICE )
  Ii1i1 ( addon , name , over )
 if over == False :
  wiz . LogNotify ( "[COLOR %s]%s[/COLOR]" % ( oOOo0O00o , o0OOO ) , "[COLOR %s]%s Removed[/COLOR]" % ( iIiIi11 , name ) )
  if 21 - 21: OoooooooOO . o0o0Oo0oooo0 - iIii1I11I1II1 % i1Ii
def Ii1i1 ( addon , name = None , over = False ) :
 if addon == 'all' :
  if iiIIIII1i1iI . yesno ( o0OOO , '[COLOR %s]Would you like to remove [COLOR %s]ALL[/COLOR] addon data stored in you Userdata folder?[/COLOR]' % ( iIiIi11 , oOOo0O00o ) , yeslabel = '[B][COLOR green]Remove Data[/COLOR][/B]' , nolabel = '[B][COLOR red]Don\'t Remove[/COLOR][/B]' ) :
   wiz . cleanHouse ( ooOOOo0oo0O0 )
  else : wiz . LogNotify ( '[COLOR %s]Remove Addon Data[/COLOR]' % oOOo0O00o , '[COLOR %s]Cancelled![/COLOR]' % iIiIi11 )
 elif addon == 'uninstalled' :
  if iiIIIII1i1iI . yesno ( o0OOO , '[COLOR %s]Would you like to remove [COLOR %s]ALL[/COLOR] addon data stored in you Userdata folder for uninstalled addons?[/COLOR]' % ( iIiIi11 , oOOo0O00o ) , yeslabel = '[B][COLOR green]Remove Data[/COLOR][/B]' , nolabel = '[B][COLOR red]Don\'t Remove[/COLOR][/B]' ) :
   o00oO0o0o = 0
   for Oo0O in glob . glob ( os . path . join ( ooOOOo0oo0O0 , '*' ) ) :
    OOOO0Oo = Oo0O . replace ( ooOOOo0oo0O0 , '' ) . replace ( '\\' , '' ) . replace ( '/' , '' )
    if OOOO0Oo in Iii1I1I11iiI1 : pass
    elif os . path . exists ( os . path . join ( O0O , OOOO0Oo ) ) : pass
    else : wiz . cleanHouse ( Oo0O ) ; o00oO0o0o += 1 ; wiz . log ( Oo0O ) ; shutil . rmtree ( Oo0O )
   wiz . LogNotify ( '[COLOR %s]Clean up Uninstalled[/COLOR]' % oOOo0O00o , '[COLOR %s]%s Folders(s) Removed[/COLOR]' % ( iIiIi11 , o00oO0o0o ) )
  else : wiz . LogNotify ( '[COLOR %s]Remove Addon Data[/COLOR]' % oOOo0O00o , '[COLOR %s]Cancelled![/COLOR]' % iIiIi11 )
 elif addon == 'empty' :
  if iiIIIII1i1iI . yesno ( o0OOO , '[COLOR %s]Would you like to remove [COLOR %s]ALL[/COLOR] empty addon data folders in you Userdata folder?[/COLOR]' % ( iIiIi11 , oOOo0O00o ) , yeslabel = '[B][COLOR green]Remove Data[/COLOR][/B]' , nolabel = '[B][COLOR red]Don\'t Remove[/COLOR][/B]' ) :
   o00oO0o0o = wiz . emptyfolder ( ooOOOo0oo0O0 )
   wiz . LogNotify ( '[COLOR %s]Remove Empty Folders[/COLOR]' % oOOo0O00o , '[COLOR %s]%s Folders(s) Removed[/COLOR]' % ( iIiIi11 , o00oO0o0o ) )
  else : wiz . LogNotify ( '[COLOR %s]Remove Empty Folders[/COLOR]' % oOOo0O00o , '[COLOR %s]Cancelled![/COLOR]' % iIiIi11 )
 else :
  Oooo0ooOoo0 = os . path . join ( oOo00Oo00O , 'addon_data' , addon )
  if addon in Iii1I1I11iiI1 :
   wiz . LogNotify ( "[COLOR %s]Protected Plugin[/COLOR]" % oOOo0O00o , "[COLOR %s]Not allowed to remove Addon_Data[/COLOR]" % iIiIi11 )
  elif os . path . exists ( Oooo0ooOoo0 ) :
   if iiIIIII1i1iI . yesno ( o0OOO , '[COLOR %s]Would you also like to remove the addon data for:[/COLOR]' % iIiIi11 , '[COLOR %s]%s[/COLOR]' % ( oOOo0O00o , addon ) , yeslabel = '[B][COLOR green]Remove Data[/COLOR][/B]' , nolabel = '[B][COLOR red]Don\'t Remove[/COLOR][/B]' ) :
    wiz . cleanHouse ( Oooo0ooOoo0 )
    try :
     shutil . rmtree ( Oooo0ooOoo0 )
    except :
     wiz . log ( "Error deleting: %s" % Oooo0ooOoo0 )
   else :
    wiz . log ( 'Addon data for %s was not removed' % addon )
 wiz . refresh ( )
 if 26 - 26: i1Ii / iIii1I11I1II1 - iIii1I11I1II1
def oO00oO00O0Oo ( type ) :
 if type == 'build' :
  ooOO00oOOo000 = ii1OO0 ( 'restore' )
  if ooOO00oOOo000 == False : wiz . LogNotify ( "[COLOR %s]%s[/COLOR]" % ( oOOo0O00o , o0OOO ) , "[COLOR %s]Local Restore Cancelled[/COLOR]" % iIiIi11 ) ; return
 if not wiz . currSkin ( ) in [ 'skin.confluence' , 'skin.estuary' ] :
  wiz . skinToDefault ( )
 wiz . restoreLocal ( type )
 if 88 - 88: IIIi1i1I - i1IIi % i11iIiiIii % II111iiii * OoooooooOO
def iIiII1 ( type ) :
 if type == 'build' :
  ooOO00oOOo000 = ii1OO0 ( 'restore' )
  if ooOO00oOOo000 == False : wiz . LogNotify ( "[COLOR %s]%s[/COLOR]" % ( oOOo0O00o , o0OOO ) , "[COLOR %s]External Restore Cancelled[/COLOR]" % iIiIi11 ) ; return
 wiz . restoreExternal ( type )
 if 47 - 47: i11IiIiiIIIII
def Oooo0O0Oooo ( name ) :
 if wiz . workingURL ( I1I1i1I ) == True :
  if wiz . checkBuild ( name , 'url' ) :
   name , O0OOO0OOooo00 , OOOoO000 , oOOOO , Ii , Ii1ii111i1 , i1i1i1I , oOoo000 , Ii1II , OooOo00o , IiI11i1IIiiI , oOOo000oOoO0 = wiz . checkBuild ( name , 'all' )
   OooOo00o = 'Yes' if OooOo00o . lower ( ) == 'yes' else 'No'
   IiIiI11IIi11Iii = "[COLOR %s]Build Name:[/COLOR] [COLOR %s]%s[/COLOR][CR]" % ( iIiIi11 , oOOo0O00o , name )
   IiIiI11IIi11Iii += "[COLOR %s]Build Version:[/COLOR] [COLOR %s]%s[/COLOR][CR]" % ( iIiIi11 , oOOo0O00o , O0OOO0OOooo00 )
   if not Ii1ii111i1 == "http://" :
    IiII1 = wiz . themeCount ( name , False )
    IiIiI11IIi11Iii += "[COLOR %s]Build Theme(s):[/COLOR] [COLOR %s]%s[/COLOR][CR]" % ( iIiIi11 , oOOo0O00o , ', ' . join ( IiII1 ) )
   IiIiI11IIi11Iii += "[COLOR %s]Kodi Version:[/COLOR] [COLOR %s]%s[/COLOR][CR]" % ( iIiIi11 , oOOo0O00o , Ii )
   IiIiI11IIi11Iii += "[COLOR %s]Adult Content:[/COLOR] [COLOR %s]%s[/COLOR][CR]" % ( iIiIi11 , oOOo0O00o , OooOo00o )
   IiIiI11IIi11Iii += "[COLOR %s]Description:[/COLOR] [COLOR %s]%s[/COLOR][CR]" % ( iIiIi11 , oOOo0O00o , IiI11i1IIiiI )
   wiz . TextBox ( o0OOO , IiIiI11IIi11Iii )
  else : wiz . log ( "Invalid Build Name!" )
 else : wiz . log ( "Build text file not working: %s" % WORKINGURL )
 if 37 - 37: O0 + OOoooooO * iii11iiII
def IiI ( name ) :
 if wiz . workingURL ( I1I1i1I ) == True :
  II1i1i1I1iII = wiz . checkBuild ( name , 'preview' )
  if II1i1i1I1iII and not II1i1i1I1iII == 'http://' : O00oO0O ( II1i1i1I1iII )
  else : wiz . log ( "[%s]Unable to find url for video preview" % name )
 else : wiz . log ( "Build text file not working: %s" % WORKINGURL )
 if 48 - 48: iii11iiII . iii11iiII + i11iIiiIii + oO0 % O0
def O0000 ( plugin ) :
 III11I11ii = os . path . join ( O0O , plugin , 'addon.xml' )
 if os . path . exists ( III11I11ii ) :
  i1I1I1i1i1i = open ( III11I11ii , mode = 'r' ) ; o0O0Oo00 = i1I1I1i1i1i . read ( ) ; i1I1I1i1i1i . close ( ) ;
  O0Oo0o000oO = wiz . parseDOM ( o0O0Oo00 , 'import' , ret = 'addon' )
  ii1i1II = [ ]
  for ii1o0oo0Ooooo0 in O0Oo0o000oO :
   if not 'xbmc.python' in ii1o0oo0Ooooo0 :
    ii1i1II . append ( ii1o0oo0Ooooo0 )
  return ii1i1II
 return [ ]
 if 1 - 1: iIii1I11I1II1 % OOoooooO + O0
def IIiII11 ( do ) :
 if do == 'import' :
  oo0O00OOOOO = os . path . join ( o0 , 'temp' )
  if not os . path . exists ( oo0O00OOOOO ) : os . makedirs ( oo0O00OOOOO )
  i1I1I1i1i1i = iiIIIII1i1iI . browse ( 1 , '[COLOR %s]Select the location of the SaveData.zip[/COLOR]' % iIiIi11 , 'files' , '.zip' , False , False , o00 )
  if not i1I1I1i1i1i . endswith ( '.zip' ) :
   wiz . LogNotify ( "[COLOR %s]%s[/COLOR]" % ( oOOo0O00o , o0OOO ) , "[COLOR %s]Import Data Error![/COLOR]" % ( iIiIi11 ) )
   return
  OoOII11IiI1 = os . path . join ( O0ooO0Oo00o , 'SaveData.zip' )
  O0OoO0oO00 = xbmcvfs . copy ( i1I1I1i1i1i , OoOII11IiI1 )
  wiz . log ( "%s" % str ( O0OoO0oO00 ) )
  extract . all ( xbmc . translatePath ( OoOII11IiI1 ) , oo0O00OOOOO )
  iiI1iI = os . path . join ( oo0O00OOOOO , 'trakt' )
  OoO0OOoO0 = os . path . join ( oo0O00OOOOO , 'login' )
  oOIiiIIi = os . path . join ( oo0O00OOOOO , 'debrid' )
  ooOO00oOOo000 = 0
  if os . path . exists ( iiI1iI ) :
   ooOO00oOOo000 += 1
   OoOOOO00oOO = os . listdir ( iiI1iI )
   if not os . path . exists ( traktit . TRAKTFOLD ) : os . makedirs ( traktit . TRAKTFOLD )
   for ii1IIIIiI11 in OoOOOO00oOO :
    iiIIiIi = os . path . join ( traktit . TRAKTFOLD , ii1IIIIiI11 )
    O0O0OOO = os . path . join ( iiI1iI , ii1IIIIiI11 )
    if os . path . exists ( iiIIiIi ) :
     if not iiIIIII1i1iI . yesno ( o0OOO , "[COLOR %s]Would you like replace the current [COLOR %s]%s[/COLOR] file?" % ( iIiIi11 , oOOo0O00o , ii1IIIIiI11 ) , yeslabel = "[B][COLOR green]Yes Replace[/COLOR][/B]" , nolabel = "[B][COLOR red]No Skip[/COLOR][/B]" ) : continue
     else : os . remove ( iiIIiIi )
    shutil . copy ( O0O0OOO , iiIIiIi )
   traktit . importlist ( 'all' )
   traktit . traktIt ( 'restore' , 'all' )
  if os . path . exists ( OoO0OOoO0 ) :
   ooOO00oOOo000 += 1
   OoOOOO00oOO = os . listdir ( OoO0OOoO0 )
   if not os . path . exists ( loginit . LOGINFOLD ) : os . makedirs ( loginit . LOGINFOLD )
   for ii1IIIIiI11 in OoOOOO00oOO :
    iiIIiIi = os . path . join ( loginit . LOGINFOLD , ii1IIIIiI11 )
    O0O0OOO = os . path . join ( OoO0OOoO0 , ii1IIIIiI11 )
    if os . path . exists ( iiIIiIi ) :
     if not iiIIIII1i1iI . yesno ( o0OOO , "[COLOR %s]Would you like replace the current [COLOR %s]%s[/COLOR] file?" % ( iIiIi11 , oOOo0O00o , ii1IIIIiI11 ) , yeslabel = "[B][COLOR green]Yes Replace[/COLOR][/B]" , nolabel = "[B][COLOR red]No Skip[/COLOR][/B]" ) : continue
     else : os . remove ( iiIIiIi )
    shutil . copy ( O0O0OOO , iiIIiIi )
   loginit . importlist ( 'all' )
   loginit . loginIt ( 'restore' , 'all' )
  if os . path . exists ( oOIiiIIi ) :
   ooOO00oOOo000 += 1
   OoOOOO00oOO = os . listdir ( oOIiiIIi )
   if not os . path . exists ( debridit . REALFOLD ) : os . makedirs ( debridit . REALFOLD )
   for ii1IIIIiI11 in OoOOOO00oOO :
    iiIIiIi = os . path . join ( debridit . REALFOLD , ii1IIIIiI11 )
    O0O0OOO = os . path . join ( oOIiiIIi , ii1IIIIiI11 )
    if os . path . exists ( iiIIiIi ) :
     if not iiIIIII1i1iI . yesno ( o0OOO , "[COLOR %s]Would you like replace the current [COLOR %s]%s[/COLOR] file?" % ( iIiIi11 , oOOo0O00o , ii1IIIIiI11 ) , yeslabel = "[B][COLOR green]Yes Replace[/COLOR][/B]" , nolabel = "[B][COLOR red]No Skip[/COLOR][/B]" ) : continue
     else : os . remove ( iiIIiIi )
    shutil . copy ( O0O0OOO , iiIIiIi )
   debridit . importlist ( 'all' )
   debridit . debridIt ( 'restore' , 'all' )
  wiz . cleanHouse ( oo0O00OOOOO )
  wiz . removeFolder ( oo0O00OOOOO )
  os . remove ( OoOII11IiI1 )
  if ooOO00oOOo000 == 0 : wiz . LogNotify ( "[COLOR %s]%s[/COLOR]" % ( oOOo0O00o , o0OOO ) , "[COLOR %s]Save Data Import Failed[/COLOR]" % iIiIi11 )
  else : wiz . LogNotify ( "[COLOR %s]%s[/COLOR]" % ( oOOo0O00o , o0OOO ) , "[COLOR %s]Save Data Import Complete[/COLOR]" % iIiIi11 )
 elif do == 'export' :
  O000oO = xbmc . translatePath ( O0ooO0Oo00o )
  dir = [ traktit . TRAKTFOLD , debridit . REALFOLD , loginit . LOGINFOLD ]
  traktit . traktIt ( 'update' , 'all' )
  loginit . loginIt ( 'update' , 'all' )
  debridit . debridIt ( 'update' , 'all' )
  i1I1I1i1i1i = iiIIIII1i1iI . browse ( 3 , '[COLOR %s]Select where you wish to export the savedata zip?[/COLOR]' % iIiIi11 , 'files' , '' , False , True , o00 )
  i1I1I1i1i1i = xbmc . translatePath ( i1I1I1i1i1i )
  ii11Ii1IiiI1 = os . path . join ( O000oO , 'SaveData.zip' )
  O00o0o = zipfile . ZipFile ( ii11Ii1IiiI1 , mode = 'w' )
  for IIIi in dir :
   if os . path . exists ( IIIi ) :
    OoOOOO00oOO = os . listdir ( IIIi )
    for file in OoOOOO00oOO :
     O00o0o . write ( os . path . join ( IIIi , file ) , os . path . join ( IIIi , file ) . replace ( o0 , '' ) , zipfile . ZIP_DEFLATED )
  O00o0o . close ( )
  if i1I1I1i1i1i == O000oO :
   iiIIIII1i1iI . ok ( o0OOO , "[COLOR %s]Save data has been backed up to:[/COLOR]" % ( iIiIi11 ) , "[COLOR %s]%s[/COLOR]" % ( oOOo0O00o , ii11Ii1IiiI1 ) )
  else :
   try :
    xbmcvfs . copy ( ii11Ii1IiiI1 , os . path . join ( i1I1I1i1i1i , 'SaveData.zip' ) )
    iiIIIII1i1iI . ok ( o0OOO , "[COLOR %s]Save data has been backed up to:[/COLOR]" % ( iIiIi11 ) , "[COLOR %s]%s[/COLOR]" % ( oOOo0O00o , os . path . join ( i1I1I1i1i1i , 'SaveData.zip' ) ) )
   except :
    iiIIIII1i1iI . ok ( o0OOO , "[COLOR %s]Save data has been backed up to:[/COLOR]" % ( iIiIi11 ) , "[COLOR %s]%s[/COLOR]" % ( oOOo0O00o , ii11Ii1IiiI1 ) )
    if 65 - 65: oO0 % IIIi1i1I . OoooooooOO * I1I1i1 * I1111
def I1 ( url ) :
 OO0OO = urllib2 . Request ( url )
 OO0OO . add_header ( 'User-Agent' , 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3' )
 I1II1I1I = urllib2 . urlopen ( OO0OO )
 o0O0Oo00 = I1II1I1I . read ( )
 I1II1I1I . close ( )
 return o0O0Oo00
 if 10 - 10: IIIi1i1I - iiIIi1IiIi11 % II111iiii - OO00O0O0O00Oo - i1IIi
def iIi11iI1i ( url ) :
 if url == 'http://' : return False
 try :
  OO0OO = urllib2 . Request ( url )
  OO0OO . add_header ( 'User-Agent' , USER_AGENT )
  I1II1I1I = urllib2 . urlopen ( OO0OO )
  I1II1I1I . close ( )
 except Exception , iiIiIiII :
  return iiIiIiII
 return True
 if 46 - 46: i1IIi + II111iiii * i1IIi - IiiIII111ii
 if 79 - 79: II111iiii - IIIi1i1I * oO0 - o0o0Oo0oooo0 . oO0
 if 11 - 11: O0 * o0o0Oo0oooo0
 if 37 - 37: o0o0Oo0oooo0 + O0 . O0 * Ooo0O % OO00O0O0O00Oo / iiIIi1IiIi11
def ii1OO0 ( install = None , over = False ) :
 if o0O0OOO0Ooo == 'true' :
  traktit . autoUpdate ( 'all' )
  wiz . setS ( 'traktlastsave' , str ( I1IiiiiI ) )
 if iiIiII1 == 'true' :
  debridit . autoUpdate ( 'all' )
  wiz . setS ( 'debridlastsave' , str ( I1IiiiiI ) )
 if OOO00O0O == 'true' :
  loginit . autoUpdate ( 'all' )
  wiz . setS ( 'loginlastsave' , str ( I1IiiiiI ) )
 if over == True : I11I1I1i1i = 1
 elif install == 'restore' : I11I1I1i1i = iiIIIII1i1iI . yesno ( o0OOO , "[COLOR %s]Do you wish to restore your" % iIiIi11 , "Kodi configuration to default settings" , "Before installing the local backup?[/COLOR]" , nolabel = '[B][COLOR red]No, Cancel[/COLOR][/B]' , yeslabel = '[B][COLOR green]Continue[/COLOR][/B]' )
 elif install : I11I1I1i1i = iiIIIII1i1iI . yesno ( o0OOO , "[COLOR %s]Do you wish to restore your" % iIiIi11 , "Kodi configuration to default settings" , "Before installing [COLOR %s]%s[/COLOR]?" % ( oOOo0O00o , install ) , nolabel = '[B][COLOR red]No, Cancel[/COLOR][/B]' , yeslabel = '[B][COLOR green]Continue[/COLOR][/B]' )
 else : I11I1I1i1i = iiIIIII1i1iI . yesno ( o0OOO , "[COLOR %s]Do you wish to restore your" % iIiIi11 , "Kodi configuration to default settings?[/COLOR]" , nolabel = '[B][COLOR red]No, Cancel[/COLOR][/B]' , yeslabel = '[B][COLOR green]Continue[/COLOR][/B]' )
 if I11I1I1i1i :
  if not wiz . currSkin ( ) in [ 'skin.confluence' , 'skin.estuary' ] :
   OoOoO0ooooO0 = 'skin.confluence' if o0OIiII < 17 else 'skin.estuary'
   if 18 - 18: OoooooooOO
   if 57 - 57: OOoooooO . o0o0Oo0oooo0 * I1I1i1 - OoooooooOO
   skinSwitch . swapSkins ( OoOoO0ooooO0 )
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
  OooO = os . path . abspath ( o00 )
  oo00 . create ( o0OOO , "[COLOR %s]Calculating files and folders" % iIiIi11 , '' , 'Please Wait![/COLOR]' )
  IiiIiI1IIi1IIIii = sum ( [ len ( OoOOOO00oOO ) for OOO0o , O0O00OO , OoOOOO00oOO in os . walk ( OooO ) ] ) ; IIiiiI = 0
  oo00 . update ( 0 , "[COLOR %s]Gathering Excludes list." % iIiIi11 )
  Iii1I1I11iiI1 . append ( 'My_Builds' )
  Iii1I1I11iiI1 . append ( 'archive_cache' )
  if IIII == 'true' :
   oOo0OoO = glob . glob ( os . path . join ( O0O , 'repo*/' ) )
   for ii1IIIIiI11 in oOo0OoO :
    oO0Oooo0OoO = os . path . split ( ii1IIIIiI11 [ : - 1 ] ) [ 1 ]
    if not oO0Oooo0OoO == Iii1I1I11iiI1 :
     Iii1I1I11iiI1 . append ( oO0Oooo0OoO )
  if iiIiI == 'true' :
   Iii1I1I11iiI1 . append ( 'plugin.program.super.favourites' )
  if o00oooO0Oo == 'true' :
   Iiii1IIIIiiI11 = ''
   o0oO0o0oo0O0 = wiz . whiteList ( 'read' )
   if len ( o0oO0o0oo0O0 ) > 0 :
    for ii1IIIIiI11 in o0oO0o0oo0O0 :
     try : oO0o00oOOooO0 , id , IIIi = ii1IIIIiI11
     except : pass
     if IIIi . startswith ( 'pvr' ) : Iiii1IIIIiiI11 = id
     ii1o0oo0Ooooo0 = O0000 ( IIIi )
     for I1iii1I in ii1o0oo0Ooooo0 :
      if not I1iii1I in Iii1I1I11iiI1 :
       Iii1I1I11iiI1 . append ( I1iii1I )
      oooII111 = O0000 ( I1iii1I )
      for I11iIi in oooII111 :
       if not I11iIi in Iii1I1I11iiI1 :
        Iii1I1I11iiI1 . append ( I11iIi )
     if not IIIi in Iii1I1I11iiI1 :
      Iii1I1I11iiI1 . append ( IIIi )
    if not Iiii1IIIIiiI11 == '' : wiz . setS ( 'pvrclient' , IIIi )
  if wiz . getS ( 'pvrclient' ) == '' :
   for ii1IIIIiI11 in Iii1I1I11iiI1 :
    if ii1IIIIiI11 . startswith ( 'pvr' ) :
     wiz . setS ( 'pvrclient' , ii1IIIIiI11 )
  oo00 . update ( 0 , "[COLOR %s]Clearing out files and folders:" % iIiIi11 )
  Ii1IIiII1I = wiz . latestDB ( 'Addons' )
  for OOOii , Iii1I11 , OoOOOO00oOO in os . walk ( OooO , topdown = True ) :
   Iii1I11 [ : ] = [ O0O00OO for O0O00OO in Iii1I11 if O0O00OO not in Iii1I1I11iiI1 ]
   for oO0o00oOOooO0 in OoOOOO00oOO :
    IIiiiI += 1
    IIIi = OOOii . replace ( '/' , '\\' ) . split ( '\\' )
    ooOO00oOOo000 = len ( IIIi ) - 1
    if oO0o00oOOooO0 == 'sources.xml' and IIIi [ - 1 ] == 'userdata' and ooOOoooooo == 'true' : wiz . log ( "Keep Sources: %s" % os . path . join ( OOOii , oO0o00oOOooO0 ) , xbmc . LOGNOTICE )
    elif oO0o00oOOooO0 == 'favourites.xml' and IIIi [ - 1 ] == 'userdata' and IiIIIi1iIi == 'true' : wiz . log ( "Keep Favourites: %s" % os . path . join ( OOOii , oO0o00oOOooO0 ) , xbmc . LOGNOTICE )
    elif oO0o00oOOooO0 == 'profiles.xml' and IIIi [ - 1 ] == 'userdata' and II1I == 'true' : wiz . log ( "Keep Profiles: %s" % os . path . join ( OOOii , oO0o00oOOooO0 ) , xbmc . LOGNOTICE )
    elif oO0o00oOOooO0 == 'advancedsettings.xml' and IIIi [ - 1 ] == 'userdata' and O0i1II1Iiii1I11 == 'true' : wiz . log ( "Keep Advanced Settings: %s" % os . path . join ( OOOii , oO0o00oOOooO0 ) , xbmc . LOGNOTICE )
    elif oO0o00oOOooO0 in Ooo0oOooo0 : wiz . log ( "Keep Log File: %s" % oO0o00oOOooO0 , xbmc . LOGNOTICE )
    elif oO0o00oOOooO0 . endswith ( '.db' ) :
     try :
      if oO0o00oOOooO0 == Ii1IIiII1I and o0OIiII >= 17 : wiz . log ( "Ignoring %s on v%s" % ( oO0o00oOOooO0 , o0OIiII ) , xbmc . LOGNOTICE )
      else : os . remove ( os . path . join ( OOOii , oO0o00oOOooO0 ) )
     except Exception , iiIiIiII :
      if not oO0o00oOOooO0 . startswith ( 'Textures13' ) :
       wiz . log ( 'Failed to delete, Purging DB' , xbmc . LOGNOTICE )
       wiz . log ( "-> %s" % ( str ( iiIiIiII ) ) , xbmc . LOGNOTICE )
       wiz . purgeDb ( os . path . join ( OOOii , oO0o00oOOooO0 ) )
    else :
     oo00 . update ( int ( wiz . percentage ( IIiiiI , IiiIiI1IIi1IIIii ) ) , '' , '[COLOR %s]File: [/COLOR][COLOR %s]%s[/COLOR]' % ( iIiIi11 , oOOo0O00o , oO0o00oOOooO0 ) , '' )
     try : os . remove ( os . path . join ( OOOii , oO0o00oOOooO0 ) )
     except Exception , iiIiIiII :
      wiz . log ( "Error removing %s" % os . path . join ( OOOii , oO0o00oOOooO0 ) , xbmc . LOGNOTICE )
      wiz . log ( "-> / %s" % ( str ( iiIiIiII ) ) , xbmc . LOGNOTICE )
   if oo00 . iscanceled ( ) :
    oo00 . close ( )
    wiz . LogNotify ( "[COLOR %s]%s[/COLOR]" % ( oOOo0O00o , o0OOO ) , "[COLOR %s]Fresh Start Cancelled[/COLOR]" % iIiIi11 )
    return False
  for OOOii , Iii1I11 , OoOOOO00oOO in os . walk ( OooO , topdown = True ) :
   Iii1I11 [ : ] = [ O0O00OO for O0O00OO in Iii1I11 if O0O00OO not in Iii1I1I11iiI1 ]
   for oO0o00oOOooO0 in Iii1I11 :
    oo00 . update ( 100 , '' , 'Cleaning Up Empty Folder: [COLOR %s]%s[/COLOR]' % ( oOOo0O00o , oO0o00oOOooO0 ) , '' )
    if oO0o00oOOooO0 not in [ "Database" , "userdata" , "temp" , "addons" , "addon_data" ] :
     shutil . rmtree ( os . path . join ( OOOii , oO0o00oOOooO0 ) , ignore_errors = True , onerror = None )
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
   o0OOOOOo00 ( install , 'normal' , over = True )
  else :
   if I11i1I1I == 1 : IIIiIi1iiI = 1
   elif I11i1I1I == 2 : IIIiIi1iiI = 0
   else : IIIiIi1iiI = iiIIIII1i1iI . yesno ( o0OOO , "[COLOR %s]Would you like to [COLOR %s]Force close[/COLOR] kodi or [COLOR %s]Reload Profile[/COLOR]?[/COLOR]" % ( iIiIi11 , oOOo0O00o , oOOo0O00o ) , yeslabel = "[B][COLOR red]Reload Profile[/COLOR][/B]" , nolabel = "[B][COLOR green]Force Close[/COLOR][/B]" )
   if IIIiIi1iiI == 1 : wiz . reloadFix ( 'fresh' )
   else : wiz . addonUpdates ( 'reset' ) ; wiz . killxbmc ( True )
 else :
  if not install == 'restore' :
   wiz . LogNotify ( "[COLOR %s]%s[/COLOR]" % ( oOOo0O00o , o0OOO ) , '[COLOR %s]Fresh Install: Cancelled![/COLOR]' % iIiIi11 )
   wiz . refresh ( )
   if 94 - 94: IiiIII111ii / OO00O0O0O00Oo . ooOo . iiIIi1IiIi11 - OoooooooOO / iIii1I11I1II1
   if 47 - 47: i1Ii
   if 76 - 76: I1111 * iIii1I11I1II1 + oO0 - OOoooooO - i11IiIiiIIIII / i1IIi
   if 27 - 27: oO0 . i1Ii
def Oo0o ( ) :
 if iiIIIII1i1iI . yesno ( o0OOO , '[COLOR %s]Would you like to clear cache?[/COLOR]' % iIiIi11 , nolabel = '[B][COLOR red]No, Cancel[/COLOR][/B]' , yeslabel = '[B][COLOR green]Clear Cache[/COLOR][/B]' ) :
  wiz . clearCache ( )
  if 2 - 2: OoooooooOO % iIii1I11I1II1
  if 21 - 21: i1Ii - ooOo % OoooooooOO + I1I1i1
def o00O0o ( ) :
 if iiIIIII1i1iI . yesno ( o0OOO , '[COLOR %s]Would you like to clear cache, packages and thumbnails?[/COLOR]' % iIiIi11 , nolabel = '[B][COLOR red]Cancel Process[/COLOR][/B]' , yeslabel = '[B][COLOR green]Clean All[/COLOR][/B]' ) :
  wiz . clearCache ( )
  wiz . clearPackages ( 'total' )
  i1Ii1 ( 'total' )
  if 75 - 75: OoooooooOO * i11iIiiIii
def i1Ii1 ( type = None ) :
 o0oOo = wiz . latestDB ( 'Textures' )
 if not type == None : Oo0 = 1
 else : Oo0 = iiIIIII1i1iI . yesno ( o0OOO , '[COLOR %s]Would you like to delete the %s and Thumbnails folder?' % ( iIiIi11 , o0oOo ) , "They will repopulate on the next startup[/COLOR]" , nolabel = '[B][COLOR red]Don\'t Delete[/COLOR][/B]' , yeslabel = '[B][COLOR green]Delete Thumbs[/COLOR][/B]' )
 if Oo0 == 1 :
  try : wiz . removeFile ( os . join ( OOOO , o0oOo ) )
  except : wiz . log ( 'Failed to delete, Purging DB.' ) ; wiz . purgeDb ( o0oOo )
  wiz . removeFolder ( oOoOooOo0o0 )
  if 51 - 51: II111iiii . IIIi1i1I . I1111 % II111iiii
 else : wiz . log ( 'Clear thumbnames cancelled' )
 wiz . redoThumbs ( )
 if 41 - 41: o0o0Oo0oooo0 - iii11iiII + OOoooooO - i1IIi
def iiiiI ( ) :
 o00iIiI1iI1Ii1 = [ ] ; ooOi1i111 = [ ]
 for iioO , ii11I , OoOOOO00oOO in os . walk ( o00 ) :
  for iiI1iiii1 in fnmatch . filter ( OoOOOO00oOO , '*.db' ) :
   if iiI1iiii1 != 'Thumbs.db' :
    Ooo0O00 = os . path . join ( iioO , iiI1iiii1 )
    o00iIiI1iI1Ii1 . append ( Ooo0O00 )
    dir = Ooo0O00 . replace ( '\\' , '/' ) . split ( '/' )
    ooOi1i111 . append ( '(%s) %s' % ( dir [ len ( dir ) - 2 ] , dir [ len ( dir ) - 1 ] ) )
 if o0OIiII >= 16 :
  Oo0 = iiIIIII1i1iI . multiselect ( "[COLOR %s]Select DB File to Purge[/COLOR]" % iIiIi11 , ooOi1i111 )
  if Oo0 == None : wiz . LogNotify ( "[COLOR %s]Purge Database[/COLOR]" % oOOo0O00o , "[COLOR %s]Cancelled[/COLOR]" % iIiIi11 )
  elif len ( Oo0 ) == 0 : wiz . LogNotify ( "[COLOR %s]Purge Database[/COLOR]" % oOOo0O00o , "[COLOR %s]Cancelled[/COLOR]" % iIiIi11 )
  else :
   for oooo0oOOoO000 in Oo0 : wiz . purgeDb ( o00iIiI1iI1Ii1 [ oooo0oOOoO000 ] )
 else :
  Oo0 = iiIIIII1i1iI . select ( "[COLOR %s]Select DB File to Purge[/COLOR]" % iIiIi11 , ooOi1i111 )
  if Oo0 == - 1 : wiz . LogNotify ( "[COLOR %s]Purge Database[/COLOR]" % oOOo0O00o , "[COLOR %s]Cancelled[/COLOR]" % iIiIi11 )
  else : wiz . purgeDb ( o00iIiI1iI1Ii1 [ oooo0oOOoO000 ] )
  if 86 - 86: iIii1I11I1II1 - i11IiIiiIIIII % OOoooooO . iii11iiII * o0o0Oo0oooo0 . i1IIi
  if 75 - 75: i11IiIiiIIIII + OOoooooO / OOoooooO - iii11iiII * I1111 * OOoooooO
  if 53 - 53: i1Ii % Ooo0O
  if 42 - 42: i11iIiiIii / ooOo - I1111 - OOoooooO + II111iiii % OOoooooO
def Ii1IIii ( ) :
 OOOoO000 = wiz . workingURL ( O0O0OOOOoo )
 if OOOoO000 == True :
  try :
   id , IiIiI11IIi11Iii = wiz . splitNotify ( O0O0OOOOoo )
   if id == False : wiz . LogNotify ( "[COLOR %s]%s[/COLOR]" % ( oOOo0O00o , o0OOO ) , "[COLOR %s]Notification: Not Formated Correctly[/COLOR]" % iIiIi11 ) ; return
   notify . notification ( IiIiI11IIi11Iii , True )
  except Exception , iiIiIiII :
   wiz . log ( "Error on Notifications Window: %s" % str ( iiIiIiII ) , xbmc . LOGERROR )
 else : wiz . LogNotify ( "[COLOR %s]%s[/COLOR]" % ( oOOo0O00o , o0OOO ) , "[COLOR %s]Invalid URL for Notification[/COLOR]" % iIiIi11 )
 if 80 - 80: i11iIiiIii
def IiIi ( ) :
 if O000oo0O == "" :
  notify . updateWindow ( )
 else :
  notify . updateWindow ( O000oo0O , oo0OooOOo0 , O00oO , wiz . checkBuild ( O000oo0O , 'icon' ) , wiz . checkBuild ( O000oo0O , 'fanart' ) )
  if 36 - 36: iii11iiII * IiiIII111ii
def i1iIii1II1i ( ) :
 notify . firstRun ( )
 if 27 - 27: oO0 / iii11iiII
def IiiIiiIIII ( ) :
 notify . firstRunSettings ( )
 if 88 - 88: I1111 . OO00O0O0O00Oo / i11IiIiiIIIII
 if 47 - 47: I1111 + oO0 . OOoooooO
 if 43 - 43: ooOo - I1I1i1 / I1I1i1 . II111iiii - IiiIII111ii
 if 40 - 40: iiIIi1IiIi11 . o0o0Oo0oooo0 * O0
 if 6 - 6: ooOo - II111iiii . ooOo + i11IiIiiIIIII . iii11iiII
def oo0O ( display , mode = None , name = None , url = None , menu = None , description = o0OOO , overwrite = True , fanart = OOO00 , icon = iiiiiIIii , themeit = None ) :
 Iii1iI1iiIii = sys . argv [ 0 ]
 if not mode == None : Iii1iI1iiIii += "?mode=%s" % urllib . quote_plus ( mode )
 if not name == None : Iii1iI1iiIii += "&name=" + urllib . quote_plus ( name )
 if not url == None : Iii1iI1iiIii += "&url=" + urllib . quote_plus ( url )
 iIiiI111I11 = True
 if themeit : display = themeit % display
 OOo0Oo0 = xbmcgui . ListItem ( display , iconImage = "DefaultFolder.png" , thumbnailImage = icon )
 OOo0Oo0 . setInfo ( type = "Video" , infoLabels = { "Title" : display , "Plot" : description } )
 OOo0Oo0 . setProperty ( "Fanart_Image" , fanart )
 if not menu == None : OOo0Oo0 . addContextMenuItems ( menu , replaceItems = overwrite )
 iIiiI111I11 = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = Iii1iI1iiIii , listitem = OOo0Oo0 , isFolder = True )
 return iIiiI111I11
 if 55 - 55: iii11iiII / o0o0Oo0oooo0 * iii11iiII
def IIIiiiI1Ii1 ( name , url , mode , iconimage , fanart , description ) :
 if 97 - 97: II111iiii % Ooo0O * i1Ii
 Iii1iI1iiIii = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart ) + "&description=" + urllib . quote_plus ( description )
 iIiiI111I11 = True
 OOo0Oo0 = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 OOo0Oo0 . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description } )
 OOo0Oo0 . setProperty ( "Fanart_Image" , fanart )
 iIiiI111I11 = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = Iii1iI1iiIii , listitem = OOo0Oo0 , isFolder = False )
 if 51 - 51: Ooo0O % iii11iiII . Ooo0O
def oo00O00oO000o ( display , mode = None , name = None , url = None , menu = None , description = o0OOO , overwrite = True , fanart = OOO00 , icon = iiiiiIIii , themeit = None ) :
 Iii1iI1iiIii = sys . argv [ 0 ]
 if not mode == None : Iii1iI1iiIii += "?mode=%s" % urllib . quote_plus ( mode )
 if not name == None : Iii1iI1iiIii += "&name=" + urllib . quote_plus ( name )
 if not url == None : Iii1iI1iiIii += "&url=" + urllib . quote_plus ( url )
 iIiiI111I11 = True
 if themeit : display = themeit % display
 OOo0Oo0 = xbmcgui . ListItem ( display , iconImage = "DefaultFolder.png" , thumbnailImage = icon )
 OOo0Oo0 . setInfo ( type = "Video" , infoLabels = { "Title" : display , "Plot" : description } )
 OOo0Oo0 . setProperty ( "Fanart_Image" , fanart )
 if not menu == None : OOo0Oo0 . addContextMenuItems ( menu , replaceItems = overwrite )
 iIiiI111I11 = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = Iii1iI1iiIii , listitem = OOo0Oo0 , isFolder = True )
 return iIiiI111I11
 if 72 - 72: IiiIII111ii % IiiIII111ii / ooOo
def iiiii1II ( display , mode = None , name = None , url = None , menu = None , description = o0OOO , overwrite = True , fanart = OOO00 , icon = iiiiiIIii , themeit = None ) :
 Iii1iI1iiIii = sys . argv [ 0 ]
 if not mode == None : Iii1iI1iiIii += "?mode=%s" % urllib . quote_plus ( mode )
 if not name == None : Iii1iI1iiIii += "&name=" + urllib . quote_plus ( name )
 if not url == None : Iii1iI1iiIii += "&url=" + urllib . quote_plus ( url )
 iIiiI111I11 = True
 if themeit : display = themeit % display
 OOo0Oo0 = xbmcgui . ListItem ( display , iconImage = "DefaultFolder.png" , thumbnailImage = icon )
 OOo0Oo0 . setInfo ( type = "Video" , infoLabels = { "Title" : display , "Plot" : description } )
 OOo0Oo0 . setProperty ( "Fanart_Image" , fanart )
 if not menu == None : OOo0Oo0 . addContextMenuItems ( menu , replaceItems = overwrite )
 iIiiI111I11 = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = Iii1iI1iiIii , listitem = OOo0Oo0 , isFolder = False )
 return iIiiI111I11
 if 40 - 40: Ooo0O - iii11iiII + OO00O0O0O00Oo - I1I1i1 % ooOo . OOoooooO
def IiIIi1I1I11Ii ( name , url , mode , iconimage ) :
 Iii1iI1iiIii = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage )
 iIiiI111I11 = True
 OOo0Oo0 = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 OOo0Oo0 . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : name } )
 iIiiI111I11 = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = Iii1iI1iiIii , listitem = OOo0Oo0 , isFolder = True )
 return iIiiI111I11
 if 35 - 35: i11iIiiIii + OoooooooOO * iIii1I11I1II1 . OO00O0O0O00Oo
def oooOOOoOOOo0O ( name , url , mode , iconimage , fanart , description , installRating ) :
 Iii1iI1iiIii = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart ) + "&description=" + urllib . quote_plus ( description ) + "&installRating=" + urllib . quote_plus ( installRating )
 iIiiI111I11 = True
 OOo0Oo0 = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 OOo0Oo0 . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description , "Premiered" : installRating } )
 OOo0Oo0 . setProperty ( "Fanart_Image" , fanart )
 iIiiI111I11 = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = Iii1iI1iiIii , listitem = OOo0Oo0 , isFolder = False )
 return iIiiI111I11
 if 48 - 48: iiIIi1IiIi11 * i1IIi % OoooooooOO * IiiIII111ii * I1111
def I1iO0o0O0OooOoo ( display , mode = None , name = None , url = None , menu = None , description = o0OOO , overwrite = True , fanart = OOO00 , icon = iiiiiIIii , themeit = None ) :
 Iii1iI1iiIii = sys . argv [ 0 ]
 if not mode == None : Iii1iI1iiIii += "?mode=%s" % urllib . quote_plus ( mode )
 if not name == None : Iii1iI1iiIii += "&name=" + urllib . quote_plus ( name )
 if not url == None : Iii1iI1iiIii += "&url=" + urllib . quote_plus ( url )
 iIiiI111I11 = True
 if themeit : display = themeit % display
 OOo0Oo0 = xbmcgui . ListItem ( display , iconImage = "DefaultFolder.png" , thumbnailImage = icon )
 OOo0Oo0 . setInfo ( type = "Video" , infoLabels = { "Title" : display , "Plot" : description } )
 OOo0Oo0 . setProperty ( "Fanart_Image" , fanart )
 if not menu == None : OOo0Oo0 . addContextMenuItems ( menu , replaceItems = overwrite )
 iIiiI111I11 = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = Iii1iI1iiIii , listitem = OOo0Oo0 , isFolder = False )
 return iIiiI111I11
 if 17 - 17: OoooooooOO % IIIi1i1I - i1IIi % i1Ii % Ooo0O
def oO0O0oO0 ( display , mode , name = None , url = None , menu = None , overwrite = True , fanart = OOO00 , icon = iiiiiIIii , description = None , themeit = None ) :
 Iii1iI1iiIii = '%s?mode=%s' % ( sys . argv [ 0 ] , urllib . quote_plus ( mode ) )
 if not name == None : Iii1iI1iiIii += "&name=" + urllib . quote_plus ( name )
 if not url == None : Iii1iI1iiIii += "&url=" + urllib . quote_plus ( url )
 if not description == None : Iii1iI1iiIii += "&description=" + urllib . quote_plus ( description )
 iIiiI111I11 = True
 if themeit : display = themeit % display
 OOo0Oo0 = xbmcgui . ListItem ( description , iconImage = "DefaultFolder.png" , thumbnailImage = icon )
 OOo0Oo0 . setInfo ( type = "Video" , infoLabels = { "Title" : description , "Plot" : o0OOO } )
 OOo0Oo0 . setProperty ( "Fanart_Image" , fanart )
 if not menu == None : OOo0Oo0 . addContextMenuItems ( menu , replaceItems = overwrite )
 iIiiI111I11 = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = Iii1iI1iiIii , listitem = OOo0Oo0 , isFolder = False )
 return iIiiI111I11
 if 41 - 41: OoooooooOO . OO00O0O0O00Oo % o0o0Oo0oooo0 - iiIIi1IiIi11
def oOOooO ( name , url , mode , iconimage , fanart , description ) :
 Iii1iI1iiIii = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&fanart=" + urllib . quote_plus ( fanart )
 iIiiI111I11 = True
 OOo0Oo0 = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 OOo0Oo0 . setInfo ( type = "Video" , infoLabels = { "Title" : name } )
 OOo0Oo0 . setProperty ( "Fanart_Image" , fanart )
 iIiiI111I11 = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = Iii1iI1iiIii , listitem = OOo0Oo0 , isFolder = False )
 return iIiiI111I11
 if 38 - 38: O0
def ooOi1i1i11iI11II ( name , url , mode , iconimage , fanart , description ) :
 if 6 - 6: o0o0Oo0oooo0 . II111iiii * ooOo . ooOo / IiiIII111ii
 Iii1iI1iiIii = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart ) + "&description=" + urllib . quote_plus ( description )
 iIiiI111I11 = True
 OOo0Oo0 = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 OOo0Oo0 . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description } )
 OOo0Oo0 . setProperty ( "Fanart_Image" , fanart )
 iIiiI111I11 = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = Iii1iI1iiIii , listitem = OOo0Oo0 , isFolder = True )
 return iIiiI111I11
 if 14 - 14: OO00O0O0O00Oo % i1Ii - O0 / OO00O0O0O00Oo
 if 91 - 91: i11iIiiIii % OO00O0O0O00Oo * IIIi1i1I - oO0 . OO00O0O0O00Oo
 if 28 - 28: i11iIiiIii
def Oo00oo0 ( name , url , mode , iconimage , fanart , description ) :
 Iii1iI1iiIii = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart ) + "&description=" + urllib . quote_plus ( description )
 iIiiI111I11 = True
 OOo0Oo0 = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 OOo0Oo0 . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description } )
 OOo0Oo0 . setProperty ( "Fanart_Image" , fanart )
 if mode == 90 :
  iIiiI111I11 = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = Iii1iI1iiIii , listitem = OOo0Oo0 , isFolder = False )
 else :
  iIiiI111I11 = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = Iii1iI1iiIii , listitem = OOo0Oo0 , isFolder = True )
 return iIiiI111I11
 if 82 - 82: iii11iiII * oO0 % IiiIII111ii . iii11iiII
def iI1oOoo ( ) :
 o00O0o00oo = [ ]
 iIiiII = sys . argv [ 2 ]
 if len ( iIiiII ) >= 2 :
  iII1I = sys . argv [ 2 ]
  o00oOOo0Oo = iII1I . replace ( '?' , '' )
  if ( iII1I [ len ( iII1I ) - 1 ] == '/' ) :
   iII1I = iII1I [ 0 : len ( iII1I ) - 2 ]
  Oooo0o0oO = o00oOOo0Oo . split ( '&' )
  o00O0o00oo = { }
  for oO0ooOoO in range ( len ( Oooo0o0oO ) ) :
   o0OOoOooO0ooO = { }
   o0OOoOooO0ooO = Oooo0o0oO [ oO0ooOoO ] . split ( '=' )
   if ( len ( o0OOoOooO0ooO ) ) == 2 :
    o00O0o00oo [ o0OOoOooO0ooO [ 0 ] ] = o0OOoOooO0ooO [ 1 ]
    if 50 - 50: i11iIiiIii + OoooooooOO / O0 + I1I1i1 / i11iIiiIii + IIIi1i1I
  return o00O0o00oo
  if 90 - 90: iiIIi1IiIi11 * IiiIII111ii - iiIIi1IiIi11 + I1111 + i11IiIiiIIIII % O0
iII1I = iI1oOoo ( )
OOOoO000 = None
oO0o00oOOooO0 = None
i111IIIIiI = None
IiIiIi1I1 = None
oOoo000 = None
IiI11i1IIiiI = None
Oo0oOOO = None
oOOo000oOoO0 = None
try :
 Oo0oOOO = int ( iII1I [ "fav_mode" ] )
except :
 pass
try : i111IIIIiI = urllib . unquote_plus ( iII1I [ "mode" ] )
except : pass
try : oO0o00oOOooO0 = urllib . unquote_plus ( iII1I [ "name" ] )
except : pass
try : OOOoO000 = urllib . unquote_plus ( iII1I [ "url" ] )
except : pass
try : IiIiIi1I1 = urllib . unquote_plus ( iII1I [ "iconimage" ] )
except : pass
try : oOoo000 = urllib . unquote_plus ( iII1I [ "fanart" ] )
except : pass
try : IiI11i1IIiiI = urllib . unquote_plus ( iII1I [ "description" ] )
except : pass
if 62 - 62: IiiIII111ii - IIIi1i1I % iIii1I11I1II1
print "Mode: " + str ( i111IIIIiI )
print "URL: " + str ( OOOoO000 )
print "Name: " + str ( oO0o00oOOooO0 )
print "IconImage: " + str ( IiIiIi1I1 )
if 57 - 57: OoooooooOO / o0o0Oo0oooo0
wiz . log ( '[ Version : \'%s\' ] [ Mode : \'%s\' ] [ Name : \'%s\' ] [ Url : \'%s\' ]' % ( O0oo0OO0 , i111IIIIiI if not i111IIIIiI == '' else None , oO0o00oOOooO0 , OOOoO000 ) )
if 44 - 44: o0o0Oo0oooo0 * i1IIi * O0
def oooo0o0oO ( ) :
 if 15 - 15: iIii1I11I1II1 . iii11iiII . oO0 * i11iIiiIii
 for file in os . listdir ( Ii11iii11I ) :
  if file . endswith ( ".zip" ) :
   OOOoO000 = xbmc . translatePath ( os . path . join ( Ii11iii11I , file ) )
   oOOooO ( file , OOOoO000 , 'read' , iiiiiIIii , iiiiiIIii , '' )
   if 72 - 72: i11IiIiiIIIII
def i1I1IIiIIi ( ) :
 iII1ii1IIII = xbmc . translatePath ( os . path . join ( 'special://' , 'home' ) )
 for file in os . listdir ( Ii11iii11I ) :
  if file . endswith ( ".zip" ) :
   OOOoO000 = xbmc . translatePath ( os . path . join ( Ii11iii11I , file ) )
   Oo00oo0 ( file , OOOoO000 , 'dell' , iiiiiIIii , iiiiiIIii , '' )
   if 98 - 98: i11iIiiIii . OO00O0O0O00Oo * IIIi1i1I . iiIIi1IiIi11
def iIi1 ( content , viewType ) :
 if 52 - 52: oO0 - i1IIi + i11iIiiIii % Ooo0O % OOoooooO
 if content :
  xbmcplugin . setContent ( int ( sys . argv [ 1 ] ) , content )
 if ADDON . getSetting ( 'auto-view' ) == 'true' :
  xbmc . executebuiltin ( "Container.SetViewMode(%s)" % ADDON . getSetting ( viewType ) )
  if 8 - 8: OO00O0O0O00Oo
  if 23 - 23: I1I1i1 - i11IiIiiIIIII + I1I1i1 * O0
  if 48 - 48: II111iiii + II111iiii * i1IIi / IiiIII111ii
  if 37 - 37: iIii1I11I1II1 % i11IiIiiIIIII / i1Ii
  if 37 - 37: OO00O0O0O00Oo - IIIi1i1I - I1111
  if 42 - 42: iIii1I11I1II1 % IiiIII111ii - oO0 + iIii1I11I1II1
  if 27 - 27: O0 / I1111
def iIi1 ( content , viewType ) :
 if wiz . getS ( 'auto-view' ) == 'true' :
  O000oooO0 = wiz . getS ( viewType )
  if O000oooO0 == '50' and o0OIiII >= 17 and I1IIiiIiii == 'skin.estuary' : O000oooO0 = '55'
  if O000oooO0 == '500' and o0OIiII >= 17 and I1IIiiIiii == 'skin.estuary' : O000oooO0 = '50'
  wiz . ebi ( "Container.SetViewMode(%s)" % O000oooO0 )
  if 75 - 75: i11iIiiIii
if i111IIIIiI == None : i1iiIiI1Ii1i ( )
if 44 - 44: iIii1I11I1II1 * OO00O0O0O00Oo * Ooo0O * oO0 + i11IiIiiIIIII
elif i111IIIIiI == 'wizardupdate' : wiz . wizardUpdate ( )
elif i111IIIIiI == 'builds' : OoO00 ( )
elif i111IIIIiI == 'viewbuild' : OoOo00o0OO ( oO0o00oOOooO0 , oOOo000oOoO0 )
elif i111IIIIiI == 'buildinfo' : Oooo0O0Oooo ( oO0o00oOOooO0 )
elif i111IIIIiI == 'buildpreview' : IiI ( oO0o00oOOooO0 )
elif i111IIIIiI == 'install' : o0OOOOOo00 ( oO0o00oOOooO0 , OOOoO000 )
elif i111IIIIiI == 'theme' : o0OOOOOo00 ( oO0o00oOOooO0 , oOOo000oOoO0 , i111IIIIiI , OOOoO000 )
elif i111IIIIiI == 'viewthirdparty' : oO00OoOO ( oO0o00oOOooO0 )
elif i111IIIIiI == 'installthird' : IIIi1IiIiii ( oO0o00oOOooO0 , OOOoO000 )
elif i111IIIIiI == 'editthird' : O0OO0O ( oO0o00oOOooO0 ) ; wiz . refresh ( )
if 12 - 12: oO0 * OOoooooO - i11IiIiiIIIII . I1111 + I1111 + iiIIi1IiIi11
elif i111IIIIiI == 'pro' : Main_Menu ( )
if 29 - 29: OoooooooOO . OO00O0O0O00Oo % OO00O0O0O00Oo
elif i111IIIIiI == 'maint' : Oo0oo0oOO0oOo ( oO0o00oOOooO0 )
elif i111IIIIiI == 'speed' : oOOoO ( )
elif i111IIIIiI == 'kodi17fix' : wiz . kodi17Fix ( )
elif i111IIIIiI == 'advancedsetting' : IiIIII1iiIIi ( oO0o00oOOooO0 )
elif i111IIIIiI == 'autoadvanced' : Ii1III1 ( ) ; wiz . refresh ( )
elif i111IIIIiI == 'removeadvanced' : OooOO0oOOo0O ( ) ; wiz . refresh ( )
elif i111IIIIiI == 'asciicheck' : wiz . asciiCheck ( )
elif i111IIIIiI == 'backupbuild' : wiz . backUpOptions ( 'build' )
elif i111IIIIiI == 'backupgui' : wiz . backUpOptions ( 'guifix' )
elif i111IIIIiI == 'backuptheme' : wiz . backUpOptions ( 'theme' )
elif i111IIIIiI == 'backupaddon' : wiz . backUpOptions ( 'addondata' )
elif i111IIIIiI == 'oldThumbs' : wiz . oldThumbs ( )
elif i111IIIIiI == 'clearbackup' : wiz . cleanupBackup ( )
elif i111IIIIiI == 'convertpath' : wiz . convertSpecial ( o00 )
elif i111IIIIiI == 'currentsettings' : oOooOO ( )
elif i111IIIIiI == 'fullclean' : o00O0o ( ) ; wiz . refresh ( )
elif i111IIIIiI == 'clearcache' : Oo0o ( ) ; wiz . refresh ( )
elif i111IIIIiI == 'clearpackages' : wiz . clearPackages ( ) ; wiz . refresh ( )
elif i111IIIIiI == 'clearcrash' : wiz . clearCrash ( ) ; wiz . refresh ( )
elif i111IIIIiI == 'clearthumb' : i1Ii1 ( ) ; wiz . refresh ( )
elif i111IIIIiI == 'checksources' : wiz . checkSources ( ) ; wiz . refresh ( )
elif i111IIIIiI == 'checkrepos' : wiz . checkRepos ( ) ; wiz . refresh ( )
elif i111IIIIiI == 'freshstart' : ii1OO0 ( )
elif i111IIIIiI == 'forceupdate' : wiz . forceUpdate ( )
elif i111IIIIiI == 'forceprofile' : wiz . reloadProfile ( wiz . getInfo ( 'System.ProfileName' ) )
elif i111IIIIiI == 'forceclose' : wiz . killxbmc ( )
elif i111IIIIiI == 'forceskin' : wiz . ebi ( "ReloadSkin()" ) ; wiz . refresh ( )
elif i111IIIIiI == 'hidepassword' : wiz . hidePassword ( )
elif i111IIIIiI == 'unhidepassword' : wiz . unhidePassword ( )
elif i111IIIIiI == 'enableaddons' : I1IIIIIi1IIiI ( )
elif i111IIIIiI == 'toggleaddon' : wiz . toggleAddon ( oO0o00oOOooO0 , OOOoO000 ) ; wiz . refresh ( )
elif i111IIIIiI == 'togglecache' : iiI1ii1Iii ( oO0o00oOOooO0 ) ; wiz . refresh ( )
elif i111IIIIiI == 'toggleadult' : wiz . toggleAdult ( ) ; wiz . refresh ( )
elif i111IIIIiI == 'changefeq' : iIIiI11iI1Ii1 ( ) ; wiz . refresh ( )
elif i111IIIIiI == 'uploadlog' : uploadLog . Main ( )
elif i111IIIIiI == 'viewlog' : o0OoOoo ( )
elif i111IIIIiI == 'viewwizlog' : o0OoOoo ( I11iii1Ii )
elif i111IIIIiI == 'viewerrorlog' : oOOoooO0O0 ( all = True )
elif i111IIIIiI == 'clearwizlog' : iiI1iiii1 = open ( I11iii1Ii , 'w' ) ; iiI1iiii1 . close ( ) ; wiz . LogNotify ( "[COLOR %s]%s[/COLOR]" % ( oOOo0O00o , o0OOO ) , "[COLOR %s]Wizard Log Cleared![/COLOR]" % iIiIi11 )
elif i111IIIIiI == 'purgedb' : iiiiI ( )
elif i111IIIIiI == 'fixaddonupdate' : i1I11Iii1i ( )
elif i111IIIIiI == 'removeaddons' : Ii11iI ( )
elif i111IIIIiI == 'removeaddon' : Ii11IiIiiii1 ( oO0o00oOOooO0 )
elif i111IIIIiI == 'removeaddondata' : o0Iiii ( )
elif i111IIIIiI == 'removedata' : Ii1i1 ( oO0o00oOOooO0 )
elif i111IIIIiI == 'resetaddon' : o00oO0o0o = wiz . cleanHouse ( o0 , ignore = True ) ; wiz . LogNotify ( "[COLOR %s]%s[/COLOR]" % ( oOOo0O00o , o0OOO ) , "[COLOR %s]Addon_Data reset[/COLOR]" % iIiIi11 )
elif i111IIIIiI == 'systeminfo' : ii11iiI11I ( )
elif i111IIIIiI == 'restorezip' : oO00oO00O0Oo ( 'build' )
elif i111IIIIiI == 'restoregui' : oO00oO00O0Oo ( 'gui' )
elif i111IIIIiI == 'restoreaddon' : oO00oO00O0Oo ( 'addondata' )
elif i111IIIIiI == 'restoreextzip' : iIiII1 ( 'build' )
elif i111IIIIiI == 'restoreextgui' : iIiII1 ( 'gui' )
elif i111IIIIiI == 'restoreextaddon' : iIiII1 ( 'addondata' )
elif i111IIIIiI == 'writeadvanced' : ooooOoo0OO ( oO0o00oOOooO0 , OOOoO000 )
if 9 - 9: Ooo0O - Ooo0O - I1I1i1 + OO00O0O0O00Oo - II111iiii . ooOo
elif i111IIIIiI == 'apk1' : iiiiiIIi ( )
elif i111IIIIiI == 'apkgame' : Ooo0O0 ( OOOoO000 )
elif i111IIIIiI == 'select' : iIiI1iiiI1ii ( OOOoO000 )
elif i111IIIIiI == 'grab' : OOoOO0OO ( oO0o00oOOooO0 , OOOoO000 )
elif i111IIIIiI == 'rom' : OOoOO0o ( OOOoO000 )
elif i111IIIIiI == 'apkscrape1' : APK ( )
elif i111IIIIiI == 'apkscrape' : Oo0OooO0 ( oO0o00oOOooO0 )
elif i111IIIIiI == 'apkshow' : oO0oooooo ( OOOoO000 )
elif i111IIIIiI == 'intellaunch' : i11i1i1I1iI1 ( )
elif i111IIIIiI == 'intelselect' : oo0ooooO ( oO0o00oOOooO0 , OOOoO000 , IiIiIi1I1 , oOoo000 , IiI11i1IIiiI )
elif i111IIIIiI == 'emurom' : ooO ( )
elif i111IIIIiI == 'roms' : Ii11iii1II1i ( )
elif i111IIIIiI == 'snes' : OOoOoo00Oo ( )
elif i111IIIIiI == 'nes' : i11II ( )
elif i111IIIIiI == 'gen' : OO0o0oO0O000o ( )
elif i111IIIIiI == 'atr' : O00OO ( )
elif i111IIIIiI == 'n64' : o0OO ( )
elif i111IIIIiI == 'tbg' : O0Oo0 ( )
elif i111IIIIiI == 'nds' : Ii1Iii11 ( )
elif i111IIIIiI == 'ps' : iI1i1II ( )
elif i111IIIIiI == 'apkinstall' : i1oo00OoO ( oO0o00oOOooO0 , OOOoO000 , "None" )
elif i111IIIIiI == 'rominstall' : i1IiI1iIIIIIi ( oO0o00oOOooO0 , OOOoO000 , )
if 57 - 57: iiIIi1IiIi11 - ooOo + OoooooooOO / iiIIi1IiIi11 . OOoooooO % i1IIi
elif i111IIIIiI == 'youtube' : oOOOoo0o ( oO0o00oOOooO0 )
elif i111IIIIiI == 'viewVideo' : O00oO0O ( OOOoO000 )
if 52 - 52: O0 - iIii1I11I1II1 / I1111 / i1Ii
elif i111IIIIiI == 'addons' : iI1IIi11i1I1 ( oO0o00oOOooO0 )
elif i111IIIIiI == 'addoninstall' : iIIi11 ( oO0o00oOOooO0 , OOOoO000 )
if 29 - 29: IiiIII111ii * iii11iiII * i1IIi . IiiIII111ii * OO00O0O0O00Oo . OOoooooO
elif i111IIIIiI == 'savedata' : i11i11i ( )
elif i111IIIIiI == 'togglesetting' : wiz . setS ( oO0o00oOOooO0 , 'false' if wiz . getS ( oO0o00oOOooO0 ) == 'true' else 'true' ) ; wiz . refresh ( )
elif i111IIIIiI == 'managedata' : IIiII11 ( oO0o00oOOooO0 )
elif i111IIIIiI == 'whitelist' : wiz . whiteList ( oO0o00oOOooO0 )
if 54 - 54: iiIIi1IiIi11 . i1IIi . oO0 * I1I1i1 % iiIIi1IiIi11
elif i111IIIIiI == 'trakt' : Iii11111iiI ( )
elif i111IIIIiI == 'savetrakt' : traktit . traktIt ( 'update' , oO0o00oOOooO0 )
elif i111IIIIiI == 'restoretrakt' : traktit . traktIt ( 'restore' , oO0o00oOOooO0 )
elif i111IIIIiI == 'addontrakt' : traktit . traktIt ( 'clearaddon' , oO0o00oOOooO0 )
elif i111IIIIiI == 'cleartrakt' : traktit . clearSaved ( oO0o00oOOooO0 )
elif i111IIIIiI == 'authtrakt' : traktit . activateTrakt ( oO0o00oOOooO0 ) ; wiz . refresh ( )
elif i111IIIIiI == 'updatetrakt' : traktit . autoUpdate ( 'all' )
elif i111IIIIiI == 'importtrakt' : traktit . importlist ( oO0o00oOOooO0 ) ; wiz . refresh ( )
if 30 - 30: i11IiIiiIIIII
elif i111IIIIiI == 'realdebrid' : O0oO00oOOooO ( )
elif i111IIIIiI == 'savedebrid' : debridit . debridIt ( 'update' , oO0o00oOOooO0 )
elif i111IIIIiI == 'restoredebrid' : debridit . debridIt ( 'restore' , oO0o00oOOooO0 )
elif i111IIIIiI == 'addondebrid' : debridit . debridIt ( 'clearaddon' , oO0o00oOOooO0 )
elif i111IIIIiI == 'cleardebrid' : debridit . clearSaved ( oO0o00oOOooO0 )
elif i111IIIIiI == 'authdebrid' : debridit . activateDebrid ( oO0o00oOOooO0 ) ; wiz . refresh ( )
elif i111IIIIiI == 'updatedebrid' : debridit . autoUpdate ( 'all' )
elif i111IIIIiI == 'importdebrid' : debridit . importlist ( oO0o00oOOooO0 ) ; wiz . refresh ( )
if 85 - 85: II111iiii + OOoooooO * i11IiIiiIIIII
elif i111IIIIiI == 'login' : OO0oo ( )
elif i111IIIIiI == 'savelogin' : loginit . loginIt ( 'update' , oO0o00oOOooO0 )
elif i111IIIIiI == 'restorelogin' : loginit . loginIt ( 'restore' , oO0o00oOOooO0 )
elif i111IIIIiI == 'addonlogin' : loginit . loginIt ( 'clearaddon' , oO0o00oOOooO0 )
elif i111IIIIiI == 'clearlogin' : loginit . clearSaved ( oO0o00oOOooO0 )
elif i111IIIIiI == 'authlogin' : loginit . activateLogin ( oO0o00oOOooO0 ) ; wiz . refresh ( )
elif i111IIIIiI == 'updatelogin' : loginit . autoUpdate ( 'all' )
elif i111IIIIiI == 'importlogin' : loginit . importlist ( oO0o00oOOooO0 ) ; wiz . refresh ( )
if 12 - 12: IiiIII111ii . ooOo % I1I1i1
elif i111IIIIiI == 'contact' : notify . contact ( oOO0O00Oo0O0o )
elif i111IIIIiI == 'settings' : wiz . openS ( oO0o00oOOooO0 ) ; wiz . refresh ( )
elif i111IIIIiI == 'opensettings' : id = eval ( OOOoO000 . upper ( ) + 'ID' ) [ oO0o00oOOooO0 ] [ 'plugin' ] ; I11i1I11 = wiz . addonId ( id ) ; I11i1I11 . openSettings ( ) ; wiz . refresh ( )
if 32 - 32: i1Ii - IIIi1i1I . iIii1I11I1II1 . OO00O0O0O00Oo + II111iiii % OoooooooOO
elif i111IIIIiI == 'developer' : oooo0o0OOO0 ( )
elif i111IIIIiI == 'converttext' : wiz . convertText ( )
elif i111IIIIiI == 'createqr' : wiz . createQR ( )
elif i111IIIIiI == 'testnotify' : Ii1IIii ( )
elif i111IIIIiI == 'testupdate' : IiIi ( )
elif i111IIIIiI == 'testfirst' : i1iIii1II1i ( )
elif i111IIIIiI == 'testfirstrun' : IiiIiiIIII ( )
elif i111IIIIiI == 'testapk' : notify . apkInstaller ( 'SPMC' )
if 82 - 82: OoooooooOO / OOoooooO * i11IiIiiIIIII * O0 . oO0
elif i111IIIIiI == 'guide' : TvGuide ( )
if 21 - 21: II111iiii + Ooo0O
elif i111IIIIiI == 'recreateaddon' : ReCreate_Addon_ini ( )
elif i111IIIIiI == 'getlistplay' : Get_List_playlinks ( oO0o00oOOooO0 )
elif i111IIIIiI == 'resolve' : RESOLVER ( OOOoO000 )
elif i111IIIIiI == 'streams' : Streams_Menu ( )
elif i111IIIIiI == 'liveevent' : Live_Events ( oO0o00oOOooO0 )
elif i111IIIIiI == 'addonopen' : I1ii11iIi11i . openSettings ( sys . argv [ 0 ] )
xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
# dd678faae9ac167bc83abf78e5cb2f3f0688d3a3
