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
 OO0Ooooo000Oo = wiz . workingURL ( I1I1i1I )
 if not OO0Ooooo000Oo == True :
  iiiii1II ( '%s Version: %s' % ( ii1iII1II , o0OIiII ) , '' , icon = oO0O00oOOoooO , themeit = OOoO )
  oo00O00oO000o ( 'Save Data Menu' , 'savedata' , icon = I1111i , themeit = OOoO )
  if O0O0ooOOO == 'No' : iiiii1II ( wiz . sep ( ) , '' , themeit = OOoO )
  iiiii1II ( 'Url for txt file not valid' , '' , icon = oO0O00oOOoooO , themeit = OOoO )
  iiiii1II ( '%s' % OO0Ooooo000Oo , '' , icon = oO0O00oOOoooO , themeit = OOoO )
 else :
  O0oOoo0o000O0 , o00oO0o0o , oo0O0Ooooooo , I1IIIiI1I1ii1 , iiiI1I1iIIIi1 , Iii , I1iiiiI1iI = wiz . buildCount ( )
  iIiiiii1i = False ; iiIi1IIiI = [ ]
  if oOooOOOoOo == 'true' :
   if not i1Iii1i1I == '' and not OOoO00 == '' : iIiiiii1i = True ; iiIi1IIiI . append ( '1' )
   if not IiI111111IIII == '' and not i1Iiii111iI1iIi1 == '' : iIiiiii1i = True ; iiIi1IIiI . append ( '2' )
   if not OOO == '' and not oo0OOo0 == '' : iIiiiii1i = True ; iiIi1IIiI . append ( '3' )
  i1oO0OO0 = wiz . openURL ( I1I1i1I ) . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' ) . replace ( 'gui=""' , 'gui="http://"' ) . replace ( 'theme=""' , 'theme="http://"' ) . replace ( 'adult=""' , 'adult="no"' )
  o0O0Oo00 = re . compile ( 'name="(.+?)".+?ersion="(.+?)".+?rl="(.+?)".+?ui="(.+?)".+?odi="(.+?)".+?heme="(.+?)".+?con="(.+?)".+?anart="(.+?)".+?dult="(.+?)".+?escription="(.+?)"' ) . findall ( i1oO0OO0 )
  if O0oOoo0o000O0 == 1 and iIiiiii1i == False :
   for O0Oo0o000oO , O0OOO0OOooo00 , oO0o00oOOooO0 , OOOoO000 , oOOOO , Ii , Ii1ii111i1 , i1i1i1I , oOoo000 , OooOo00o in o0O0Oo00 :
    if not O0Oo000ooO00 == 'true' and oOoo000 . lower ( ) == 'yes' : continue
    if not iii == 'true' and wiz . strTest ( O0Oo0o000oO ) : continue
    IiI11i1IIiiI ( o0O0Oo00 [ 0 ] [ 0 ] )
    return
  iiiii1II ( '%s Version: %s' % ( ii1iII1II , o0OIiII ) , '' , icon = oO0O00oOOoooO , themeit = OOoO )
  oo00O00oO000o ( 'Save Data Menu' , 'savedata' , icon = I1111i , themeit = OOoO )
  if O0O0ooOOO == 'No' : iiiii1II ( wiz . sep ( ) , '' , themeit = OOoO )
  if iIiiiii1i == True :
   for oOOo000oOoO0 in iiIi1IIiI :
    O0Oo0o000oO = eval ( 'THIRD%sNAME' % oOOo000oOoO0 )
    oo00O00oO000o ( "[B]%s[/B]" % O0Oo0o000oO , 'viewthirdparty' , oOOo000oOoO0 , icon = oO0O00oOOoooO , themeit = OOoO )
  if len ( o0O0Oo00 ) >= 1 :
   if oo00O00oO == 'true' :
    for O0Oo0o000oO , O0OOO0OOooo00 , oO0o00oOOooO0 , OOOoO000 , oOOOO , Ii , Ii1ii111i1 , i1i1i1I , oOoo000 , OooOo00o in o0O0Oo00 :
     if not O0Oo000ooO00 == 'true' and oOoo000 . lower ( ) == 'yes' : continue
     if not iii == 'true' and wiz . strTest ( O0Oo0o000oO ) : continue
     OoOo00o0OO = ii1IIIIiI11 ( 'install' , '' , O0Oo0o000oO )
     oo00O00oO000o ( '[%s] %s (v%s)' % ( float ( oOOOO ) , O0Oo0o000oO , O0OOO0OOooo00 ) , 'viewbuild' , O0Oo0o000oO , description = OooOo00o , fanart = i1i1i1I , icon = Ii1ii111i1 , menu = OoOo00o0OO , themeit = oooOo0OOOoo0 )
   else :
    if iiiI1I1iIIIi1 > 0 :
     iI1IIIii = '+' if OOOO0OOoO0O0 == 'false' else '-'
     iiiii1II ( '[B]%s Leia Builds(%s)[/B]' % ( iI1IIIii , iiiI1I1iIIIi1 ) , 'togglesetting' , 'show17' , themeit = OOoO )
     if OOOO0OOoO0O0 == 'true' :
      for O0Oo0o000oO , O0OOO0OOooo00 , oO0o00oOOooO0 , OOOoO000 , oOOOO , Ii , Ii1ii111i1 , i1i1i1I , oOoo000 , OooOo00o in o0O0Oo00 :
       if not O0Oo000ooO00 == 'true' and oOoo000 . lower ( ) == 'yes' : continue
       if not iii == 'true' and wiz . strTest ( O0Oo0o000oO ) : continue
       I1i11ii11 = int ( float ( oOOOO ) )
       if I1i11ii11 == 18 :
        OoOo00o0OO = ii1IIIIiI11 ( 'install' , '' , O0Oo0o000oO )
        oo00O00oO000o ( '[%s] %s (v%s)' % ( float ( oOOOO ) , O0Oo0o000oO , O0OOO0OOooo00 ) , 'viewbuild' , O0Oo0o000oO , description = OooOo00o , fanart = i1i1i1I , icon = Ii1ii111i1 , menu = OoOo00o0OO , themeit = oooOo0OOOoo0 )
    if I1IIIiI1I1ii1 > 0 :
     iI1IIIii = '+' if o00OO00OoO == 'false' else '-'
     iiiii1II ( '[B]%s Krypton Builds(%s)[/B]' % ( iI1IIIii , I1IIIiI1I1ii1 ) , 'togglesetting' , 'show17' , themeit = OOoO )
     if o00OO00OoO == 'true' :
      for O0Oo0o000oO , O0OOO0OOooo00 , oO0o00oOOooO0 , OOOoO000 , oOOOO , Ii , Ii1ii111i1 , i1i1i1I , oOoo000 , OooOo00o in o0O0Oo00 :
       if not O0Oo000ooO00 == 'true' and oOoo000 . lower ( ) == 'yes' : continue
       if not iii == 'true' and wiz . strTest ( O0Oo0o000oO ) : continue
       I1i11ii11 = int ( float ( oOOOO ) )
       if I1i11ii11 == 17 :
        OoOo00o0OO = ii1IIIIiI11 ( 'install' , '' , O0Oo0o000oO )
        oo00O00oO000o ( '[%s] %s (v%s)' % ( float ( oOOOO ) , O0Oo0o000oO , O0OOO0OOooo00 ) , 'viewbuild' , O0Oo0o000oO , description = OooOo00o , fanart = i1i1i1I , icon = Ii1ii111i1 , menu = OoOo00o0OO , themeit = oooOo0OOOoo0 )
    if oo0O0Ooooooo > 0 :
     iI1IIIii = '+' if oOOoo0Oo == 'false' else '-'
     iiiii1II ( '[B]%s Jarvis Builds(%s)[/B]' % ( iI1IIIii , oo0O0Ooooooo ) , 'togglesetting' , 'show16' , themeit = OOoO )
     if oOOoo0Oo == 'true' :
      for O0Oo0o000oO , O0OOO0OOooo00 , oO0o00oOOooO0 , OOOoO000 , oOOOO , Ii , Ii1ii111i1 , i1i1i1I , oOoo000 , OooOo00o in o0O0Oo00 :
       if not O0Oo000ooO00 == 'true' and oOoo000 . lower ( ) == 'yes' : continue
       if not iii == 'true' and wiz . strTest ( O0Oo0o000oO ) : continue
       I1i11ii11 = int ( float ( oOOOO ) )
       if I1i11ii11 == 16 :
        OoOo00o0OO = ii1IIIIiI11 ( 'install' , '' , O0Oo0o000oO )
        oo00O00oO000o ( '[%s] %s (v%s)' % ( float ( oOOOO ) , O0Oo0o000oO , O0OOO0OOooo00 ) , 'viewbuild' , O0Oo0o000oO , description = OooOo00o , fanart = i1i1i1I , icon = Ii1ii111i1 , menu = OoOo00o0OO , themeit = oooOo0OOOoo0 )
    if o00oO0o0o > 0 :
     iI1IIIii = '+' if oO0Oo == 'false' else '-'
     iiiii1II ( '[B]%s Isengard and Below Builds(%s)[/B]' % ( iI1IIIii , o00oO0o0o ) , 'togglesetting' , 'show15' , themeit = OOoO )
     if oO0Oo == 'true' :
      for O0Oo0o000oO , O0OOO0OOooo00 , oO0o00oOOooO0 , OOOoO000 , oOOOO , Ii , Ii1ii111i1 , i1i1i1I , oOoo000 , OooOo00o in o0O0Oo00 :
       if not O0Oo000ooO00 == 'true' and oOoo000 . lower ( ) == 'yes' : continue
       if not iii == 'true' and wiz . strTest ( O0Oo0o000oO ) : continue
       I1i11ii11 = int ( float ( oOOOO ) )
       if I1i11ii11 <= 15 :
        OoOo00o0OO = ii1IIIIiI11 ( 'install' , '' , O0Oo0o000oO )
        oo00O00oO000o ( '[%s] %s (v%s)' % ( float ( oOOOO ) , O0Oo0o000oO , O0OOO0OOooo00 ) , 'viewbuild' , O0Oo0o000oO , description = OooOo00o , fanart = i1i1i1I , icon = Ii1ii111i1 , menu = OoOo00o0OO , themeit = oooOo0OOOoo0 )
  elif I1iiiiI1iI > 0 :
   if Iii > 0 :
    iiiii1II ( 'There is currently only Adult builds' , '' , icon = oO0O00oOOoooO , themeit = OOoO )
    iiiii1II ( 'Enable Show Adults in Addon Settings > Misc' , '' , icon = oO0O00oOOoooO , themeit = OOoO )
   else :
    iiiii1II ( 'Currently No Builds Offered from %s' % o0OOO , '' , icon = oO0O00oOOoooO , themeit = OOoO )
  else : iiiii1II ( 'Text file for builds not formated correctly.' , '' , icon = oO0O00oOOoooO , themeit = OOoO )
 iIi1 ( 'files' , 'viewType' )
 if 81 - 81: iii11iiII - i11IiIiiIIIII % OOoooooO - I1111 / Ooo0O
def IiI11i1IIiiI ( name ) :
 OO0Ooooo000Oo = wiz . workingURL ( I1I1i1I )
 if not OO0Ooooo000Oo == True :
  iiiii1II ( 'Url for txt file not valid' , '' , themeit = OOoO )
  iiiii1II ( '%s' % OO0Ooooo000Oo , '' , themeit = OOoO )
  return
 if wiz . checkBuild ( name , 'version' ) == False :
  iiiii1II ( 'Error reading the txt file.' , '' , themeit = OOoO )
  iiiii1II ( '%s was not found in the builds list.' % name , '' , themeit = OOoO )
  return
 i1oO0OO0 = wiz . openURL ( I1I1i1I ) . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' ) . replace ( 'gui=""' , 'gui="http://"' ) . replace ( 'theme=""' , 'theme="http://"' )
 o0O0Oo00 = re . compile ( 'name="%s".+?ersion="(.+?)".+?rl="(.+?)".+?ui="(.+?)".+?odi="(.+?)".+?heme="(.+?)".+?con="(.+?)".+?anart="(.+?)".+?review="(.+?)".+?dult="(.+?)".+?escription="(.+?)"' % name ) . findall ( i1oO0OO0 )
 for O0OOO0OOooo00 , oO0o00oOOooO0 , OOOoO000 , oOOOO , OOo00OoO , Ii1ii111i1 , i1i1i1I , Ii1iI111 , oOoo000 , OooOo00o in o0O0Oo00 :
  Ii1ii111i1 = Ii1ii111i1 if wiz . workingURL ( Ii1ii111i1 ) else iiiiiIIii
  i1i1i1I = i1i1i1I if wiz . workingURL ( i1i1i1I ) else OOO00
  I111iIi1 = '%s (v%s)' % ( name , O0OOO0OOooo00 )
  if O000oo0O == name and O0OOO0OOooo00 > oo0OooOOo0 :
   I111iIi1 = '%s [COLOR red][CURRENT v%s][/COLOR]' % ( I111iIi1 , oo0OooOOo0 )
  iiiii1II ( I111iIi1 , '' , description = OooOo00o , fanart = i1i1i1I , icon = Ii1ii111i1 , themeit = OO0O000 )
  if O0O0ooOOO == 'No' : iiiii1II ( wiz . sep ( ) , '' , themeit = OOoO )
  oo00O00oO000o ( 'Save Data Menu' , 'savedata' , icon = I1111i , themeit = OOoO )
  iiiii1II ( 'Build Information' , 'buildinfo' , name , description = OooOo00o , fanart = i1i1i1I , icon = Ii1ii111i1 , themeit = OOoO )
  if not Ii1iI111 == "http://" : iiiii1II ( 'View Video Preview' , 'buildpreview' , name , description = OooOo00o , fanart = i1i1i1I , icon = Ii1ii111i1 , themeit = OOoO )
  O0oooo00o0Oo = int ( float ( o0OIiII ) ) ; I1iii = int ( float ( oOOOO ) )
  if not O0oooo00o0Oo == I1iii :
   if O0oooo00o0Oo == 16 and I1iii <= 15 : oO0o0O0Ooo0o = False
   else : oO0o0O0Ooo0o = True
  else : oO0o0O0Ooo0o = False
  if oO0o0O0Ooo0o == True :
   iiiii1II ( '[I]Build designed for kodi version %s(installed: %s)[/I]' % ( str ( oOOOO ) , str ( o0OIiII ) ) , '' , fanart = i1i1i1I , icon = Ii1ii111i1 , themeit = OOoO )
  iiiii1II ( wiz . sep ( 'INSTALL' ) , '' , fanart = i1i1i1I , icon = Ii1ii111i1 , themeit = OOoO )
  iiiii1II ( 'Fresh Install' , 'install' , name , 'fresh' , description = OooOo00o , fanart = i1i1i1I , icon = Ii1ii111i1 , themeit = OOOiiiiI )
  iiiii1II ( 'Standard Install' , 'install' , name , 'normal' , description = OooOo00o , fanart = i1i1i1I , icon = Ii1ii111i1 , themeit = OOOiiiiI )
  if not OOOoO000 == 'http://' : iiiii1II ( 'Apply guiFix' , 'install' , name , 'gui' , description = OooOo00o , fanart = i1i1i1I , icon = Ii1ii111i1 , themeit = OOOiiiiI )
  if not OOo00OoO == 'http://' :
   if wiz . workingURL ( OOo00OoO ) == True :
    iiiii1II ( wiz . sep ( 'THEMES' ) , '' , fanart = i1i1i1I , icon = Ii1ii111i1 , themeit = OOoO )
    i1oO0OO0 = wiz . openURL ( OOo00OoO ) . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
    o0O0Oo00 = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?con="(.+?)".+?anart="(.+?)".+?dult="(.+?)".+?escription="(.+?)"' ) . findall ( i1oO0OO0 )
    for i1Ii11II , IioO0oOOO0Ooo , i1i1I , IiIIi1iII11I1Ii1 , o0o0 , OooOo00o in o0O0Oo00 :
     if not O0Oo000ooO00 == 'true' and o0o0 . lower ( ) == 'yes' : continue
     i1i1I = i1i1I if i1i1I == 'http://' else Ii1ii111i1
     IiIIi1iII11I1Ii1 = IiIIi1iII11I1Ii1 if IiIIi1iII11I1Ii1 == 'http://' else i1i1i1I
     iiiii1II ( i1Ii11II if not i1Ii11II == o0O else "[B]%s (Installed)[/B]" % i1Ii11II , 'theme' , name , i1Ii11II , description = OooOo00o , fanart = IiIIi1iII11I1Ii1 , icon = i1i1I , themeit = OOoO )
 iIi1 ( 'files' , 'viewType' )
 if 59 - 59: iii11iiII + i11iIiiIii
def oo0OOo0O ( number ) :
 O0Oo0o000oO = eval ( 'THIRD%sNAME' % number )
 oO0o00oOOooO0 = eval ( 'THIRD%sURL' % number )
 Ii1IiII = wiz . workingURL ( oO0o00oOOooO0 )
 if not Ii1IiII == True :
  iiiii1II ( 'Url for txt file not valid' , '' , icon = oO0O00oOOoooO , themeit = OOoO )
  iiiii1II ( '%s' % WORKINGURL , '' , icon = oO0O00oOOoooO , themeit = OOoO )
 else :
  type , I1i = wiz . thirdParty ( oO0o00oOOooO0 )
  iiiii1II ( "[B]%s[/B]" % O0Oo0o000oO , '' , themeit = OOoO )
  if O0O0ooOOO == 'No' : iiiii1II ( wiz . sep ( ) , '' , themeit = OOoO )
  if type :
   for O0Oo0o000oO , O0OOO0OOooo00 , oO0o00oOOooO0 , oOOOO , Ii1ii111i1 , i1i1i1I , oOoo000 , OooOo00o in I1i :
    if not O0Oo000ooO00 == 'true' and oOoo000 . lower ( ) == 'yes' : continue
    iiiii1II ( "[%s] %s v%s" % ( oOOOO , O0Oo0o000oO , O0OOO0OOooo00 ) , 'installthird' , O0Oo0o000oO , oO0o00oOOooO0 , icon = Ii1ii111i1 , fanart = i1i1i1I , description = OooOo00o , themeit = oooOo0OOOoo0 )
  else :
   for O0Oo0o000oO , oO0o00oOOooO0 , Ii1ii111i1 , i1i1i1I , OooOo00o in I1i :
    iiiii1II ( O0Oo0o000oO , 'installthird' , O0Oo0o000oO , oO0o00oOOooO0 , icon = Ii1ii111i1 , fanart = i1i1i1I , description = OooOo00o , themeit = oooOo0OOOoo0 )
    if 72 - 72: iIii1I11I1II1
def iiIi ( number ) :
 O0Oo0o000oO = eval ( 'THIRD%sNAME' % number )
 oO0o00oOOooO0 = eval ( 'THIRD%sURL' % number )
 oOIi111 = wiz . getKeyboard ( O0Oo0o000oO , 'Enter the Name of the Wizard' )
 oO0i1iI = wiz . getKeyboard ( oO0o00oOOooO0 , 'Enter the URL of the Wizard Text' )
 if 10 - 10: II111iiii . iiIIi1IiIi11
 wiz . setS ( 'wizard%sname' % number , oOIi111 )
 wiz . setS ( 'wizard%surl' % number , oO0i1iI )
 if 32 - 32: IiiIII111ii . i1Ii . OoooooooOO - I1111 + IIIi1i1I
def ooO0oO00O0o ( name = "" ) :
 if name == 'kodi' :
  ooOO00oOOo000 = 'http://mirrors.kodi.tv/releases/android/arm/'
  IIi = 'http://mirrors.kodi.tv/releases/android/arm/old/'
  i11II11II1 = wiz . openURL ( ooOO00oOOo000 ) . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
  oO0i1iI = wiz . openURL ( IIi ) . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
  II1IOoOo000oOo0oo = 0
  oO0O = re . compile ( '<tr><td><a href="(.+?)">(.+?)</a></td><td>(.+?)</td><td>(.+?)</td></tr>' ) . findall ( i11II11II1 )
  oOOiiiIIiIi = re . compile ( '<tr><td><a href="(.+?)">(.+?)</a></td><td>(.+?)</td><td>(.+?)</td></tr>' ) . findall ( oO0i1iI )
  if 68 - 68: O0 + o0o0Oo0oooo0 / IIIi1i1I - iii11iiII + iIii1I11I1II1 % IiiIII111ii
  iiiii1II ( "Official Kodi Apk\'s" , themeit = OOOiiiiI )
  i1iI1iii11i = False
  for oO0o00oOOooO0 , name , oOO00oO00O0OO , oOo00OO in oO0O :
   if oO0o00oOOooO0 in [ '../' , 'old/' ] : continue
   if not oO0o00oOOooO0 . endswith ( '.apk' ) : continue
   if not oO0o00oOOooO0 . find ( '_' ) == - 1 and i1iI1iii11i == True : continue
   try :
    o0oOO0OO = name . split ( '-' )
    if not oO0o00oOOooO0 . find ( '_' ) == - 1 :
     i1iI1iii11i = True
     oOIi111 , Oo00OoO00o0 = o0oOO0OO [ 2 ] . split ( '_' )
    else :
     oOIi111 = o0oOO0OO [ 2 ]
     Oo00OoO00o0 = ''
    OOoOoO00O0O0o = "[COLOR %s]%s v%s%s %s[/COLOR] [COLOR %s]%s[/COLOR] [COLOR %s]%s[/COLOR]" % ( oOOo0O00o , o0oOO0OO [ 0 ] . title ( ) , o0oOO0OO [ 1 ] , Oo00OoO00o0 . upper ( ) , oOIi111 , iIiIi11 , oOO00oO00O0OO . replace ( ' ' , '' ) , oOOo0O00o , oOo00OO )
    iI1I11i = urljoin ( ooOO00oOOo000 , oO0o00oOOooO0 )
    iiiii1II ( OOoOoO00O0O0o , 'apkinstall' , "%s v%s%s %s" % ( o0oOO0OO [ 0 ] . title ( ) , o0oOO0OO [ 1 ] , Oo00OoO00o0 . upper ( ) , oOIi111 ) , iI1I11i )
    II1IOoOo000oOo0oo += 1
   except :
    wiz . log ( "Error on: %s" % name )
    if 85 - 85: i11iIiiIii - iii11iiII . IiiIII111ii / II111iiii . II111iiii
  for oO0o00oOOooO0 , name , oOO00oO00O0OO , oOo00OO in oOOiiiIIiIi :
   if oO0o00oOOooO0 in [ '../' , 'old/' ] : continue
   if not oO0o00oOOooO0 . endswith ( '.apk' ) : continue
   if not oO0o00oOOooO0 . find ( '_' ) == - 1 : continue
   try :
    o0oOO0OO = name . split ( '-' )
    OOoOoO00O0O0o = "[COLOR %s]%s v%s %s[/COLOR] [COLOR %s]%s[/COLOR] [COLOR %s]%s[/COLOR]" % ( oOOo0O00o , o0oOO0OO [ 0 ] . title ( ) , o0oOO0OO [ 1 ] , o0oOO0OO [ 2 ] , iIiIi11 , oOO00oO00O0OO . replace ( ' ' , '' ) , oOOo0O00o , oOo00OO )
    iI1I11i = urljoin ( IIi , oO0o00oOOooO0 )
    iiiii1II ( OOoOoO00O0O0o , 'apkinstall' , "%s v%s %s" % ( o0oOO0OO [ 0 ] . title ( ) , o0oOO0OO [ 1 ] , o0oOO0OO [ 2 ] ) , iI1I11i )
    II1IOoOo000oOo0oo += 1
   except :
    wiz . log ( "Error on: %s" % name )
  if II1IOoOo000oOo0oo == 0 : iiiii1II ( "Error Kodi Scraper Is Currently Down." )
 elif name == 'spmc' :
  O0o0o = 'https://github.com/koying/SPMC/releases'
  i11II11II1 = wiz . openURL ( O0o0o ) . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
  II1IOoOo000oOo0oo = 0
  oO0O = re . compile ( '<div.+?lass="release-body.+?div class="release-header".+?a href=.+?>(.+?)</a>.+?ul class="release-downloads">(.+?)</ul>.+?/div>' ) . findall ( i11II11II1 )
  if 87 - 87: i11IiIiiIIIII * i1IIi - IiiIII111ii % iii11iiII / OO00O0O0O00Oo
  iiiii1II ( "Official SPMC Apk\'s" , themeit = OOOiiiiI )
  if 39 - 39: ooOo * i11iIiiIii - IIIi1i1I / i1Ii % OO00O0O0O00Oo % i11IiIiiIIIII
  for name , OO00oo0o in oO0O :
   IIIiIi = ''
   oOOiiiIIiIi = re . compile ( '<li>.+?<a href="(.+?)" rel="nofollow">.+?<small class="text-gray float-right">(.+?)</small>.+?strong>(.+?)</strong>.+?</a>.+?</li>' ) . findall ( OO00oo0o )
   for IiiIIIII1iii , IIiiii , iI111i1I1II in oOOiiiIIiIi :
    if iI111i1I1II . find ( 'armeabi' ) == - 1 : continue
    if iI111i1I1II . find ( 'launcher' ) > - 1 : continue
    IIIiIi = urljoin ( 'https://github.com' , IiiIIIII1iii )
    break
   if IIIiIi == '' : continue
   try :
    name = "SPMC %s" % name
    OOoOoO00O0O0o = "[COLOR %s]%s[/COLOR] [COLOR %s]%s[/COLOR]" % ( oOOo0O00o , name , iIiIi11 , IIiiii . replace ( ' ' , '' ) )
    iI1I11i = IIIiIi
    iiiii1II ( OOoOoO00O0O0o , 'apkinstall' , name , iI1I11i )
    II1IOoOo000oOo0oo += 1
   except Exception , O00OO :
    wiz . log ( "Error on: %s / %s" % ( name , str ( O00OO ) ) )
  if II1IOoOo000oOo0oo == 0 : iiiii1II ( "Error SPMC Scraper Is Currently Down." )
  if 29 - 29: Ooo0O % I1111 % i1Ii . I1I1i1 / OoooooooOO * OOoooooO
def o0OoO000O ( ) :
 oo00O00oO000o ( 'Emulators And Roms' , 'emurom' , icon = i111iIi1i1II1 , themeit = OOOiiiiI )
 oo00O00oO000o ( 'SpinzTV APKS' , 'apkshow' , url = OooOo , icon = Ii1IIiI1i , themeit = OOOiiiiI )
 oo00O00oO000o ( '[COLOR deepskyblue]APK Drawer[/COLOR]' , 'intellaunch' , )
 oo00O00oO000o ( 'Official Kodi Apk\'s' , 'apkscrape' , 'kodi' , icon = Oo0O00O000 , themeit = OOOiiiiI )
 oo00O00oO000o ( 'Official SPMC Apk\'s' , 'apkscrape' , 'spmc' , icon = Oo0O00O000 , themeit = OOOiiiiI )
 OOo = iIIiiIIIi1I ( base64 . b64decode ( 'aHR0cHM6Ly93d3cuYXBrZmlsZXMuY29tLw==' ) )
 o0O0Oo00 = re . compile ( 'href="([^"]*)">Applications(.+?)</a>' ) . findall ( OOo )
 oOOiiiIIiIi = re . compile ( 'href="([^"]*)">Games(.+?)</a>' ) . findall ( OOo )
 for oO0o00oOOooO0 , OO0o0o0oo0O in o0O0Oo00 :
  IIiI1I1 ( '[COLOR deepskyblue]Android Apps[/COLOR]' + OO0o0o0oo0O , 'https://www.apkfiles.com' + oO0o00oOOooO0 , 'apkgame' , i1I1i111Ii )
 for oO0o00oOOooO0 , OO0o0o0oo0O in oOOiiiIIiIi :
  IIiI1I1 ( '[COLOR deepskyblue]Android Games[/COLOR]' + OO0o0o0oo0O , 'https://www.apkfiles.com' + oO0o00oOOooO0 , 'apkgame' , i111iIi1i1II1 )
 iIi1 ( 'movies' , 'MAIN' )
 oo00O00oO000o ( 'Spinz Apk Picks' , 'apkshow' , url = ii1I , icon = Oo0O00O000 , themeit = OOOiiiiI )
 if O0Oo000ooO00 == 'true' : oo00O00oO000o ( 'XXX Apk' , 'apkshow' , url = i11III1111iIi , icon = Oo0O00O000 , themeit = OOOiiiiI )
 iIi1 ( 'files' , 'viewType' )
 if 15 - 15: IiiIII111ii * Ooo0O % oO0 * iIii1I11I1II1 - i11iIiiIii
def Oo00OOOOoo0oo ( url ) :
 i1oO0OO0 = iIIiiIIIi1I ( url ) . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
 o0O0Oo00 = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?con="(.+?)".+?anart="(.+?)"' ) . findall ( i1oO0OO0 )
 if len ( o0O0Oo00 ) > 0 :
  for O0Oo0o000oO , url , Ii1ii111i1 , i1i1i1I in o0O0Oo00 :
   iiiii1II ( O0Oo0o000oO , 'apkinstall' , O0Oo0o000oO , url , icon = Ii1ii111i1 , fanart = i1i1i1I , themeit = OOOiiiiI )
  else : wiz . log ( "[APK Menu] ERROR: Invalid Format." )
 else : wiz . log ( "[APK Menu] ERROR: URL for emu list not working." )
 if 80 - 80: OO00O0O0O00Oo * o0o0Oo0oooo0 * II111iiii - O0 . o0o0Oo0oooo0 % ooOo
def II1 ( url ) :
 OOo = iIIiiIIIi1I ( url )
 o0O0Oo00 = re . compile ( '<a href="([^"]*)" >(.+?)</a>' ) . findall ( OOo )
 for url , O0Oo0o000oO in o0O0Oo00 :
  if '/cat' in url :
   IIiI1I1 ( ( O0Oo0o000oO ) . replace ( '&amp;' , ' - ' ) , 'https://www.apkfiles.com' + url , 'select' , O000OO0 + 'APK.png' )
   if 32 - 32: ooOo - oO0 - Ooo0O
def ii ( url ) :
 OOo = iIIiiIIIi1I ( url )
 i11II11II1 = url
 if "page=" in str ( url ) :
  i11II11II1 = url . split ( '?' ) [ 0 ]
 o0O0Oo00 = re . compile ( '<a href="([^"]*)".+?<img src="([^"]*)" class="file_list_icon".+?alt="([^"]*)"' , re . DOTALL ) . findall ( OOo )
 oOOiiiIIiIi = re . compile ( 'class="[^"]*".+?ref="([^"]*)".+?yle=.+?</a>' ) . findall ( OOo )
 for url , I1i11II , O0Oo0o000oO in o0O0Oo00 :
  if 'apk' in url :
   IIiI1I1 ( ( O0Oo0o000oO ) . replace ( '&#39;' , '' ) . replace ( '&amp;' , ' - ' ) . replace ( '&#174;:' , ': ' ) . replace ( '&#174;' , ' ' ) , 'https://www.apkfiles.com' + url , 'grab' , 'http:' + I1i11II )
 if len ( oOOiiiIIiIi ) > 1 :
  oOOiiiIIiIi = str ( oOOiiiIIiIi [ len ( oOOiiiIIiIi ) - 1 ] )
 IIiI1I1 ( 'Next Page' , i11II11II1 + str ( oOOiiiIIiIi ) , 'select' , O000OO0 + 'Next.png' )
 if 31 - 31: IIIi1i1I / i1Ii * I1I1i1 . II111iiii
def oooOO0OO0O ( name , url ) :
 OOo = iIIiiIIIi1I ( url )
 name = name
 o0O0Oo00 = re . compile ( 'href="([^"]*)".+?lass="yellow_button".+?itle=' ) . findall ( OOo )
 for url in o0O0Oo00 :
  url = 'https://www.apkfiles.com' + url
  o00o ( name , url , 'Brackets' )
  if 47 - 47: I1I1i1 + iiIIi1IiIi11 - IIIi1i1I % OoooooooOO
  if 52 - 52: OO00O0O0O00Oo / OOoooooO - i11IiIiiIIIII
  if 49 - 49: o0o0Oo0oooo0 / Ooo0O . i11iIiiIii
  if 21 - 21: o0o0Oo0oooo0 + i11iIiiIii + ooOo * I1I1i1 % iiIIi1IiIi11 % II111iiii
def oOO0OO0OO ( ) :
 xbmc . executebuiltin ( 'Runscript("special://home/addons/plugin.program.SpinzTV/ookla.py")' )
 if 87 - 87: IIIi1i1I + iIii1I11I1II1 - OoooooooOO
 if 8 - 8: OoooooooOO / i11IiIiiIIIII + i1IIi . iiIIi1IiIi11
 if 73 - 73: i1IIi + iiIIi1IiIi11 . i11iIiiIii
 if 5 - 5: IIIi1i1I . oO0 . II111iiii . OoooooooOO
def Oo0OooO0 ( ) :
 if 87 - 87: IIIi1i1I % IiiIII111ii
 if os . path . isfile ( i1i1II ) :
  oo0OOOoOo = True
  IIiiIIi1 = open ( i1i1II )
  ooO000O = IIiiIIi1 . read ( )
  IIiiIIi1 . close ( )
 else :
  xbmcgui . Dialog ( ) . ok ( "[COLOR orange]SpinzTV[/COLOR]" , "[COLOR cyan][B]][[/B]NT3L[B]][[/B]G3NC[B]][[/B][/COLOR]" , "[COLOR ghostwhite]First Time Launching Will Take a Couple Minutes[/COLOR]" , "[COLOR ghostwhite]Please Be Patient![/COLOR]" )
  oo0OOOoOo = False
  if 53 - 53: I1I1i1 . iiIIi1IiIi11 / IiiIII111ii
  if 39 - 39: IiiIII111ii % O0 % o0o0Oo0oooo0 . i1IIi
  if 86 - 86: I1111 * OoooooooOO
  if 71 - 71: iIii1I11I1II1 - iii11iiII . ooOo % OoooooooOO + iii11iiII
  if 26 - 26: Ooo0O + iii11iiII / I1111 % o0o0Oo0oooo0 % oO0 + II111iiii
  if 31 - 31: i11IiIiiIIIII % iii11iiII * i11IiIiiIIIII
  if 45 - 45: i1IIi . ooOo + iii11iiII - OoooooooOO % OOoooooO
  if 1 - 1: iIii1I11I1II1
  if 93 - 93: i1IIi . i11iIiiIii . Ooo0O
  if 99 - 99: i11IiIiiIIIII - OO00O0O0O00Oo - IIIi1i1I % I1111
  if 21 - 21: II111iiii % oO0 . i1IIi - OoooooooOO
 iiOOOO0o = ""
 i1I1iIi1IiI = i1111O0O000OOOo ( )
 for i11ii1Ii1 in i1I1iIi1IiI :
  if oo0OOOoOo == True :
   if i11ii1Ii1 not in ooO000O :
    if 25 - 25: iii11iiII
    if 83 - 83: OO00O0O0O00Oo
    ii111Ii11iii = o00OOoOOO000O0 ( iiOOOO0o , i11ii1Ii1 )
    iiOOOO0o = ii111Ii11iii
    if 92 - 92: oO0 / O0
  else :
   ii111Ii11iii = o00OOoOOO000O0 ( iiOOOO0o , i11ii1Ii1 )
   iiOOOO0o = ii111Ii11iii
   if 80 - 80: I1I1i1 - iii11iiII + OoooooooOO
 if oo0OOOoOo == True :
  IIiiIIi1 = open ( i1i1II , 'a' )
  if 98 - 98: iii11iiII + i1IIi . ooOo - II111iiii - I1I1i1
  if 24 - 24: Ooo0O - i1IIi + i11IiIiiIIIII
 else :
  IIiiIIi1 = open ( i1i1II , 'w' )
  if 38 - 38: OoooooooOO / oO0 . O0 / i1IIi / Ooo0O + iIii1I11I1II1
  if 96 - 96: iiIIi1IiIi11
 IIiiIIi1 . write ( iiOOOO0o )
 IIiiIIi1 . close ( )
 if 18 - 18: iiIIi1IiIi11 * i11IiIiiIIIII - IiiIII111ii
 if 31 - 31: Ooo0O - O0 % o0o0Oo0oooo0 % IIIi1i1I
 IIiiIIi1 = open ( i1i1II )
 ooO000O = IIiiIIi1 . read ( )
 IIiiIIi1 . close ( )
 ooO000O = ooO000O . replace ( '\n' , '' ) . replace ( '\r' , '' )
 o0O0Oo00 = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)".+?nstallRating="(.+?)"' ) . findall ( ooO000O )
 if 45 - 45: oO0 + II111iiii * i11iIiiIii
 if 13 - 13: OoooooooOO * IIIi1i1I - IiiIII111ii / iii11iiII + i11IiIiiIIIII + i1Ii
 for O0Oo0o000oO , oO0o00oOOooO0 , iii1III1i , i1i1i1I , OooOo00o , iiiIi in sorted ( o0O0Oo00 , key = lambda o0O0Oo00 : o0O0Oo00 [ 0 ] ) :
  if oO0o00oOOooO0 in i1I1iIi1IiI :
   II1Iii ( '[COLOR ghostwhite]' + str ( O0Oo0o000oO ) + '[/COLOR]' , oO0o00oOOooO0 , 'intelselect' , iii1III1i , i1i1i1I , OooOo00o , iiiIi )
   if 73 - 73: i11IiIiiIIIII * OoooooooOO . O0 . i1Ii
def i1111O0O000OOOo ( ) :
 if xbmc . getCondVisibility ( 'system.platform.android' ) :
  try :
   i1I1iIi1IiI = subprocess . Popen ( [ 'exec ' '/system/bin/pm list packages -3' '' ] , executable = '/system/bin/sh' , shell = True , stdout = subprocess . PIPE , stderr = subprocess . STDOUT ) . communicate ( ) [ 0 ] . rstrip ( '\n' ) . splitlines ( )
  except :
   i1I1iIi1IiI = [ ]
   if 55 - 55: Ooo0O
  for i11ii1Ii1 in range ( len ( i1I1iIi1IiI ) ) :
   i1I1iIi1IiI [ i11ii1Ii1 ] = i1I1iIi1IiI [ i11ii1Ii1 ] . partition ( ':' ) [ 2 ]
   if 77 - 77: II111iiii
 return i1I1iIi1IiI
 if 16 - 16: ooOo * II111iiii / iIii1I11I1II1 - iiIIi1IiIi11
def o00OOoOOO000O0 ( theList , i ) :
 global theNotList
 IiI1IiI11iII = "https://play.google.com/store/apps/details?id=" + i
 i1oO0OO0 = OOoOO0OO ( IiI1IiI11iII )
 if 26 - 26: iiIIi1IiIi11 . iiIIi1IiIi11
 if i1oO0OO0 != False :
  i1oO0OO0 = i1oO0OO0 . replace ( '\n' , '' ) . replace ( '\r' , '' )
  if 35 - 35: OO00O0O0O00Oo . o0o0Oo0oooo0 * i11iIiiIii
  iiII = r'<div class="id-app-title".tabindex=".">(.+?)</div>'
  o0O0Oo00 = re . search ( iiII , i1oO0OO0 )
  if o0O0Oo00 != None : O0Oo0o000oO = o0O0Oo00 . group ( 1 )
  else : O0Oo0o000oO = i
  if 57 - 57: i11IiIiiIIIII . Ooo0O + II111iiii
  if 43 - 43: OO00O0O0O00Oo % iiIIi1IiIi11
  if 69 - 69: iiIIi1IiIi11 % I1111
  if 86 - 86: IIIi1i1I / IIIi1i1I
  if 28 - 28: i11iIiiIii / I1I1i1 . iIii1I11I1II1 / II111iiii
  iii1III1i = "androidapp://sources/apps/" + str ( i ) + ".png"
  if 72 - 72: OoooooooOO / ooOo + IiiIII111ii / o0o0Oo0oooo0 * IiiIII111ii
  if 34 - 34: O0 * O0 % OoooooooOO + iiIIi1IiIi11 * iIii1I11I1II1 % IiiIII111ii
  if 25 - 25: i11IiIiiIIIII + o0o0Oo0oooo0 . I1I1i1 % o0o0Oo0oooo0 * iii11iiII
  if 32 - 32: i11iIiiIii - OO00O0O0O00Oo
  if 53 - 53: OoooooooOO - i1Ii
  if 87 - 87: IIIi1i1I . ooOo
  i1iIIIiiiI = r'data-expand-to="full-screenshot-[0-9]{1,2}" src="(//\w+?.\w+?.\S+?=h900)"'
  o0O0Oo00 = re . compile ( i1iIIIiiiI ) . findall ( i1oO0OO0 )
  if len ( o0O0Oo00 ) != 0 : i1i1i1I = "https:" + o0O0Oo00 [ len ( o0O0Oo00 ) - 1 ]
  else : i1i1i1I = "None"
  if 94 - 94: O0 - i11IiIiiIIIII - iIii1I11I1II1 % OOoooooO / IiiIII111ii % iiIIi1IiIi11
  iIi1IIi1ii = r'data-video-url="https://www.youtube.com/embed/(\S.+?)\?ps=play.+?"'
  o0O0Oo00 = re . search ( iIi1IIi1ii , i1oO0OO0 )
  if o0O0Oo00 != None : OooOo00o = o0O0Oo00 . group ( 1 )
  else : OooOo00o = "None"
  if 35 - 35: iiIIi1IiIi11 / oO0 * OoooooooOO . II111iiii / Ooo0O
  Iii11i = r'<div class="content" itemprop="numDownloads">\s+?(\d.+?\s-\s\d.+?)\s+?</div>'
  o0O0Oo00 = re . search ( Iii11i , i1oO0OO0 )
  if o0O0Oo00 != None : OOOOOOoO = 'Installed ' + o0O0Oo00 . group ( 1 )
  else : OOOOOOoO = "Installs: N/A"
  if 12 - 12: iiIIi1IiIi11 . i1Ii . o0o0Oo0oooo0 / O0
  OO0oOOo0o = r'<div class="score" aria-label=" Rated .+? stars out of five stars ">(.+?)</div>'
  o0O0Oo00 = re . search ( OO0oOOo0o , i1oO0OO0 )
  if o0O0Oo00 != None : I1 = o0O0Oo00 . group ( 1 ) + " Stars"
  else : I1 = "Rating: N/A"
  iiiIi = I1 + " " + OOOOOOoO
  if 7 - 7: I1111 * i11IiIiiIIIII + II111iiii % i11iIiiIii
  if 8 - 8: OOoooooO * O0
  if 73 - 73: I1I1i1 / IIIi1i1I / i11IiIiiIIIII / I1111
  oO0o00oOOooO0 = i
  theList += 'name="' + O0Oo0o000oO + '"url="' + oO0o00oOOooO0 + '"img="' + iii1III1i + '"fanart="' + i1i1i1I + '"description="' + OooOo00o + '"installRating="' + iiiIi + '"'
  return theList
  if 11 - 11: o0o0Oo0oooo0 + i1Ii - OoooooooOO / I1111
  if 34 - 34: OOoooooO
  if 45 - 45: OOoooooO / Ooo0O / IiiIII111ii
  if 44 - 44: oO0 - IiiIII111ii / II111iiii * I1111 * Ooo0O
  if 73 - 73: I1I1i1 - ooOo * i1IIi / i11iIiiIii * iii11iiII % II111iiii
  if 56 - 56: OoooooooOO * Ooo0O . Ooo0O . oO0
  if 24 - 24: Ooo0O . i11IiIiiIIIII * IiiIII111ii % iiIIi1IiIi11 / iii11iiII
  if 58 - 58: ooOo - oO0 % O0 . ooOo % I1111 % i1Ii
  if 87 - 87: IIIi1i1I - i11iIiiIii
 else :
  if 78 - 78: i11iIiiIii / iIii1I11I1II1 - I1I1i1
  return theList
  if 23 - 23: i11IiIiiIIIII
def iIiiIiiIi ( name , url , iconimage , fanart , videolink ) :
 i1iiIIIi = 0
 if 62 - 62: O0 / ooOo % O0 * I1111 % ooOo
 if videolink != "None" :
  i1iiIIIi += 1
  if 33 - 33: ooOo . IIIi1i1I * I1111 * iIii1I11I1II1
 if i1iiIIIi == 1 : II11 = xbmcgui . Dialog ( ) . select ( '[COLOR deepskyblue]' + name + '[/COLOR]' , [ '[COLOR deepskyblue]Launch[/COLOR]' , '[COLOR ghostwhite]Preview Video[/COLOR]' , '[COLOR tomato]Uninstall[/COLOR]' ] )
 if i1iiIIIi == 0 : II11 = xbmcgui . Dialog ( ) . select ( '[COLOR deepskyblue]' + name + '[/COLOR]' , [ '[COLOR deepskyblue]Launch[/COLOR]' , '[COLOR ghostwhite]No Preview Video[/COLOR]' , '[COLOR tomato]Uninstall[/COLOR]' ] )
 if 12 - 12: OO00O0O0O00Oo
 if 93 - 93: i11iIiiIii % iIii1I11I1II1 % i11iIiiIii + I1I1i1 / I1I1i1 / II111iiii
 if 49 - 49: iii11iiII . oO0 . i11iIiiIii - II111iiii / IiiIII111ii
 if II11 == 1 :
  if videolink != 'None' :
   yt . PlayVideo ( videolink )
 if II11 == 0 :
  ooOo0O0o0 = xbmcgui . Dialog ( ) . yesno ( "[COLOR orange]SpinzTV[/COLOR]" , "[COLOR cyan][B]][[/B]NT3L[B]][[/B]G3NC[B]][[/B][/COLOR]" , "" , "[COLOR ghostwhite]Would You Like To Launch:[/COLOR] [COLOR cyan]" + name + "[/COLOR]" , "[COLOR red]No Way[/COLOR]" , "[COLOR cyan]Heck Ya![/COLOR]" )
  if ooOo0O0o0 == 1 :
   xbmc . executebuiltin ( 'StartAndroidActivity(%s)' % url )
 if II11 == 2 :
  o0oo0O = xbmcgui . Dialog ( ) . yesno ( "[COLOR orange]SpinzTV[/COLOR]" , "[COLOR cyan][B]][[/B]NT3L[B]][[/B]G3NC[B]][[/B][/COLOR]" , "" , "[COLOR ghostwhite]Would You Like To Remove:[/COLOR] [COLOR cyan]" + name + "[/COLOR]" , "[COLOR red]No Way[/COLOR]" , "[COLOR cyan]Heck Ya![/COLOR]" )
  if o0oo0O :
   xbmc . executebuiltin ( 'StartAndroidActivity("","android.intent.action.DELETE","","package:' + url + '")' )
   xbmc . sleep ( 2000 )
   try : shutil . rmtree ( "/sdcard/Android/data/" + url , ignore_errors = True , onerror = None )
   except : pass
   try : shutil . rmtree ( "/sdcard/Android/obb/" + url , ignore_errors = True , onerror = None )
   except : pass
   xbmc . executebuiltin ( 'Container.Refresh' )
   if 19 - 19: OO00O0O0O00Oo + i1IIi . ooOo - Ooo0O
def OOoOO0OO ( url ) :
 try :
  iIi1I1 = urllib2 . Request ( url )
  iIi1I1 . add_header ( 'User-Agent' , 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3' )
  O0oOoo0OoO0O = urllib2 . urlopen ( iIi1I1 )
  i1oO0OO0 = O0oOoo0OoO0O . read ( )
  O0oOoo0OoO0O . close ( )
  return i1oO0OO0
 except :
  return False
  if 63 - 63: OoooooooOO / OOoooooO
  if 91 - 91: i1IIi - iIii1I11I1II1
  if 55 - 55: ooOo * I1I1i1 % OOoooooO . iIii1I11I1II1 * OO00O0O0O00Oo
def o0oo0000 ( ) :
 oo00O00oO000o ( 'Emulators' , 'apkshow' , url = I1i111I , icon = i111iIi1i1II1 , themeit = OOOiiiiI )
 oo00O00oO000o ( 'Roms' , 'roms' , icon = i111iIi1i1II1 , themeit = OOOiiiiI )
 if 42 - 42: OO00O0O0O00Oo + OO00O0O0O00Oo * II111iiii
 if 78 - 78: OoooooooOO
 if 77 - 77: oO0 / i1IIi / Ooo0O % iii11iiII
 if 48 - 48: i11IiIiiIIIII - i1Ii + iIii1I11I1II1 + OoooooooOO
def IiI1i111IiIiIi1 ( ) :
 oo00O00oO000o ( 'NES' , 'nes' , icon = i111iIi1i1II1 , themeit = OOOiiiiI )
 oo00O00oO000o ( 'SNES' , 'snes' , icon = i111iIi1i1II1 , themeit = OOOiiiiI )
 oo00O00oO000o ( 'Nintendo 64' , 'n64' , icon = i111iIi1i1II1 , themeit = OOOiiiiI )
 oo00O00oO000o ( 'Nintendo DS' , 'nds' , icon = i111iIi1i1II1 , themeit = OOOiiiiI )
 oo00O00oO000o ( 'Genesis' , 'gen' , icon = i111iIi1i1II1 , themeit = OOOiiiiI )
 oo00O00oO000o ( 'Playstation' , 'ps' , icon = i111iIi1i1II1 , themeit = OOOiiiiI )
 oo00O00oO000o ( 'Atari' , 'atr' , icon = i111iIi1i1II1 , themeit = OOOiiiiI )
 oo00O00oO000o ( 'PC Engine & Turbo Grafx' , 'tbg' , icon = i111iIi1i1II1 , themeit = OOOiiiiI )
 if 39 - 39: i11IiIiiIIIII - oO0
def OOO0o0OO0OO ( url ) :
 i1oO0OO0 = iIIiiIIIi1I ( url ) . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
 o0O0Oo00 = re . compile ( '.+?ame="(.+?)".+?rl="(.+?)".+?con="(.+?)".+?anart="(.+?)"description="(.+?)"' ) . findall ( i1oO0OO0 )
 if len ( o0O0Oo00 ) > 0 :
  for O0Oo0o000oO , url , Ii1ii111i1 , i1i1i1I , OooOo00o in o0O0Oo00 :
   oOo0O ( O0Oo0o000oO , 'rominstall' , O0Oo0o000oO , url , icon = Ii1ii111i1 , fanart = i1i1i1I , description = OooOo00o , themeit = OOOiiiiI )
  else : wiz . log ( "[ROM Menu] ERROR: Invalid Format." )
 else : wiz . log ( "[ROM Menu] ERROR: URL for apk list not working." )
 if 43 - 43: I1I1i1 . iiIIi1IiIi11 . i11IiIiiIIIII + iIii1I11I1II1
 if 78 - 78: iIii1I11I1II1 % o0o0Oo0oooo0 + oO0 / i1IIi % II111iiii + iii11iiII
 if 91 - 91: iIii1I11I1II1 % I1111 . I1I1i1 + IiiIII111ii + I1I1i1
 if 95 - 95: IiiIII111ii + oO0 * iii11iiII
def I1Ii ( ) :
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
 if 77 - 77: iIii1I11I1II1 - i1IIi . IIIi1i1I
 if 26 - 26: I1I1i1 * i1Ii . i1IIi
 if 59 - 59: O0 + i1IIi - I1I1i1
 if 62 - 62: i11iIiiIii % iii11iiII . i1Ii . iii11iiII
def ooOo0O0O0oOO0 ( ) :
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
 if 10 - 10: Ooo0O + O0
 if 43 - 43: iIii1I11I1II1 / II111iiii % I1I1i1 - iii11iiII
 if 62 - 62: i11IiIiiIIIII
 if 63 - 63: iii11iiII + OOoooooO * IIIi1i1I / I1I1i1 / Ooo0O * iIii1I11I1II1
 if 57 - 57: o0o0Oo0oooo0 - IIIi1i1I / OOoooooO % i11iIiiIii
def I11oOOooo ( ) :
 oo00O00oO000o ( 'Genesis Titles A Thru B' , 'rom' , url = oO , icon = i111iIi1i1II1 , themeit = OOOiiiiI )
 oo00O00oO000o ( 'Genesis Titles C Thru D' , 'rom' , url = IIiIi , icon = Oo0O00O000 , themeit = OOOiiiiI )
 oo00O00oO000o ( 'Genesis Titles E Thru G' , 'rom' , url = OOoOooOoOOOoo , icon = i111iIi1i1II1 , themeit = OOOiiiiI )
 oo00O00oO000o ( 'Genesis Titles H Thru L' , 'rom' , url = Iiii1iI1i , icon = i111iIi1i1II1 , themeit = OOOiiiiI )
 oo00O00oO000o ( 'Genesis Titles M Thru O' , 'rom' , url = I1ii1ii11i1I , icon = i111iIi1i1II1 , themeit = OOOiiiiI )
 oo00O00oO000o ( 'Genesis Titles P Thru R' , 'rom' , url = o0OoOO , icon = i111iIi1i1II1 , themeit = OOOiiiiI )
 oo00O00oO000o ( 'Genesis Titles S Thru T' , 'rom' , url = O0O0Oo00 , icon = i111iIi1i1II1 , themeit = OOOiiiiI )
 oo00O00oO000o ( 'Genesis Titles U Thru Z' , 'rom' , url = oOoO00o , icon = i111iIi1i1II1 , themeit = OOOiiiiI )
 if 80 - 80: ooOo - i11iIiiIii
 if 69 - 69: IIIi1i1I % OoooooooOO . ooOo
 if 34 - 34: IiiIII111ii * o0o0Oo0oooo0 - i1Ii - ooOo - IiiIII111ii
 if 42 - 42: II111iiii * ooOo % i1IIi - IiiIII111ii % i1Ii
 if 36 - 36: i11iIiiIii / IIIi1i1I * oO0 * oO0 + IiiIII111ii * i11IiIiiIIIII
def iIiI1i ( ) :
 oo00O00oO000o ( 'Atari Titles A Thru B' , 'rom' , url = oO00O0 , icon = i111iIi1i1II1 , themeit = OOOiiiiI )
 oo00O00oO000o ( 'Atari Titles C Thru D' , 'rom' , url = IIi1IIIi , icon = Oo0O00O000 , themeit = OOOiiiiI )
 oo00O00oO000o ( 'Atari Titles E Thru G' , 'rom' , url = O00Ooo , icon = i111iIi1i1II1 , themeit = OOOiiiiI )
 oo00O00oO000o ( 'Atari Titles H Thru L' , 'rom' , url = OOOO0OOO , icon = i111iIi1i1II1 , themeit = OOOiiiiI )
 oo00O00oO000o ( 'Atari Titles M Thru O' , 'rom' , url = i1i1ii , icon = i111iIi1i1II1 , themeit = OOOiiiiI )
 oo00O00oO000o ( 'Atari Titles P Thru R' , 'rom' , url = iII1ii1 , icon = i111iIi1i1II1 , themeit = OOOiiiiI )
 oo00O00oO000o ( 'Atari Titles S Thru U' , 'rom' , url = I1i1iiiI1 , icon = i111iIi1i1II1 , themeit = OOOiiiiI )
 oo00O00oO000o ( 'Atari Titles V Thru Z' , 'rom' , url = iIIi , icon = i111iIi1i1II1 , themeit = OOOiiiiI )
 if 31 - 31: IiiIII111ii
 if 78 - 78: i11iIiiIii + I1I1i1 + OO00O0O0O00Oo / I1I1i1 % iIii1I11I1II1 % i1Ii
 if 83 - 83: iIii1I11I1II1 % o0o0Oo0oooo0 % I1I1i1 % OO00O0O0O00Oo . oO0 % O0
 if 47 - 47: I1I1i1
 if 66 - 66: ooOo - i1Ii
def iiIii ( ) :
 oo00O00oO000o ( 'N64 Titles A Thru B' , 'rom' , url = oO0o00oo0 , icon = i111iIi1i1II1 , themeit = OOOiiiiI )
 oo00O00oO000o ( 'N64 Titles C Thru E' , 'rom' , url = ii1IIII , icon = Oo0O00O000 , themeit = OOOiiiiI )
 oo00O00oO000o ( 'N64 Titles F Thru J' , 'rom' , url = oO00oOooooo0 , icon = i111iIi1i1II1 , themeit = OOOiiiiI )
 oo00O00oO000o ( 'N64 Titles K Thru M' , 'rom' , url = oOo , icon = i111iIi1i1II1 , themeit = OOOiiiiI )
 oo00O00oO000o ( 'N64 Titles N Thru R' , 'rom' , url = O0OOooOoO , icon = i111iIi1i1II1 , themeit = OOOiiiiI )
 oo00O00oO000o ( 'N64 Titles S Thru T' , 'rom' , url = i1II1I1Iii1 , icon = i111iIi1i1II1 , themeit = OOOiiiiI )
 oo00O00oO000o ( 'N64 Titles V Thru Z' , 'rom' , url = iiI11Iii , icon = i111iIi1i1II1 , themeit = OOOiiiiI )
 if 28 - 28: IIIi1i1I
 if 52 - 52: ooOo + iIii1I11I1II1
 if 71 - 71: O0 / IIIi1i1I
 if 34 - 34: o0o0Oo0oooo0 . iIii1I11I1II1 % O0
 if 43 - 43: oO0 - iiIIi1IiIi11
def O000O ( ) :
 oo00O00oO000o ( 'PC Engine And Turbo Grafx Titles A Thru B' , 'rom' , url = O0o0O0 , icon = i111iIi1i1II1 , themeit = OOOiiiiI )
 oo00O00oO000o ( 'PC Engine And Turbo Grafx Titles C Thru E' , 'rom' , url = Ii1II1I11i1 , icon = Oo0O00O000 , themeit = OOOiiiiI )
 oo00O00oO000o ( 'PC Engine And Turbo Grafx Titles F Thru I' , 'rom' , url = oOoooooOoO , icon = i111iIi1i1II1 , themeit = OOOiiiiI )
 oo00O00oO000o ( 'PC Engine And Turbo Grafx Titles J Thru M' , 'rom' , url = Ii111 , icon = i111iIi1i1II1 , themeit = OOOiiiiI )
 oo00O00oO000o ( 'PC Engine And Turbo Grafx Titles N Thru Q' , 'rom' , url = I111i1i1111 , icon = i111iIi1i1II1 , themeit = OOOiiiiI )
 oo00O00oO000o ( 'PC Engine And Turbo Grafx Titles R Thru U' , 'rom' , url = IIII1 , icon = i111iIi1i1II1 , themeit = OOOiiiiI )
 oo00O00oO000o ( 'PC Engine And Turbo Grafx Titles V Thru Z' , 'rom' , url = I1I1i , icon = i111iIi1i1II1 , themeit = OOOiiiiI )
 if 98 - 98: iIii1I11I1II1 + OO00O0O0O00Oo % o0o0Oo0oooo0 + i11IiIiiIIIII % o0o0Oo0oooo0
 if 24 - 24: IIIi1i1I * OO00O0O0O00Oo
 if 40 - 40: IiiIII111ii - o0o0Oo0oooo0 * o0o0Oo0oooo0 . o0o0Oo0oooo0 + OoooooooOO
 if 77 - 77: iIii1I11I1II1 . IiiIII111ii % IIIi1i1I / IiiIII111ii
 if 54 - 54: IIIi1i1I + OOoooooO - Ooo0O
def I1I1IiIi1 ( ) :
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
 if 58 - 58: o0o0Oo0oooo0 - iiIIi1IiIi11 - OoooooooOO
 if 96 - 96: iIii1I11I1II1
 if 82 - 82: o0o0Oo0oooo0 + O0 - i1Ii % IIIi1i1I * i11iIiiIii
 if 15 - 15: I1I1i1
def I1iI ( ) :
 oo00O00oO000o ( 'Playstation Titles A' , 'rom' , url = oO00oo0o00o0o , icon = i111iIi1i1II1 , themeit = OOOiiiiI )
 oo00O00oO000o ( 'Playstation Titles B' , 'rom' , url = IiIIIIIi , icon = i111iIi1i1II1 , themeit = OOOiiiiI )
 oo00O00oO000o ( 'Playstation Titles C Thru D' , 'rom' , url = IiIi1iIIi1 , icon = i111iIi1i1II1 , themeit = OOOiiiiI )
 oo00O00oO000o ( 'Playstation Titles E Thru F' , 'rom' , url = O0OoO0ooOO0o , icon = i111iIi1i1II1 , themeit = OOOiiiiI )
 oo00O00oO000o ( 'Playstation Titles G Thru J' , 'rom' , url = OoOo0oOooOoOO , icon = i111iIi1i1II1 , themeit = OOOiiiiI )
 oo00O00oO000o ( 'Playstation Titles K Thru N' , 'rom' , url = oo00ooOoO00 , icon = i111iIi1i1II1 , themeit = OOOiiiiI )
 oo00O00oO000o ( 'Playstation Titles O Thru R' , 'rom' , url = o00oOoOo0 , icon = i111iIi1i1II1 , themeit = OOOiiiiI )
 oo00O00oO000o ( 'Playstation Titles S Thru T' , 'rom' , url = o0O0O0ooo0oOO , icon = i111iIi1i1II1 , themeit = OOOiiiiI )
 oo00O00oO000o ( 'Playstation Titles U Thru Z' , 'rom' , url = oo000 , icon = i111iIi1i1II1 , themeit = OOOiiiiI )
 if 92 - 92: I1111 * OOoooooO
def i1iIIi1 ( url = None ) :
 if not OO == 'http://' :
  if url == None :
   o0o0OoOOOOOo = wiz . workingURL ( OO )
   Ii11iii1II1i = uservar . ADDONFILE
  else :
   o0o0OoOOOOOo = wiz . workingURL ( url )
   Ii11iii1II1i = url
  if o0o0OoOOOOOo == True :
   i1oO0OO0 = wiz . openURL ( Ii11iii1II1i ) . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' ) . replace ( 'repository=""' , 'repository="none"' ) . replace ( 'repositoryurl=""' , 'repositoryurl="http://"' ) . replace ( 'repositoryxml=""' , 'repositoryxml="http://"' )
   o0O0Oo00 = re . compile ( 'name="(.+?)".+?lugin="(.+?)".+?rl="(.+?)".+?epository="(.+?)".+?epositoryxml="(.+?)".+?epositoryurl="(.+?)".+?con="(.+?)".+?anart="(.+?)".+?dult="(.+?)".+?escription="(.+?)"' ) . findall ( i1oO0OO0 )
   if len ( o0O0Oo00 ) > 0 :
    II1IOoOo000oOo0oo = 0
    for O0Oo0o000oO , o0OOoOO , url , iII1 , III1I1 , ii1111Ii1i , Ii1ii111i1 , i1i1i1I , oOoo000 , OooOo00o in o0O0Oo00 :
     if o0OOoOO . lower ( ) == 'section' :
      II1IOoOo000oOo0oo += 1
      oo00O00oO000o ( "[B]%s[/B]" % O0Oo0o000oO , 'addons' , url , description = OooOo00o , icon = Ii1ii111i1 , fanart = i1i1i1I , themeit = OOoO )
     else :
      if not O0Oo000ooO00 == 'true' and oOoo000 . lower ( ) == 'yes' : continue
      try :
       IiI1iiI1III1I = xbmcaddon . Addon ( id = o0OOoOO ) . getAddonInfo ( 'path' )
       if os . path . exists ( IiI1iiI1III1I ) :
        O0Oo0o000oO = "[COLOR green][Installed][/COLOR] %s" % O0Oo0o000oO
      except :
       pass
      II1IOoOo000oOo0oo += 1
      iiiii1II ( O0Oo0o000oO , 'addoninstall' , o0OOoOO , Ii11iii1II1i , description = OooOo00o , icon = Ii1ii111i1 , fanart = i1i1i1I , themeit = oooOo0OOOoo0 )
     if II1IOoOo000oOo0oo < 1 :
      iiiii1II ( "No addons added to this menu yet!" , '' , themeit = oooOo0OOOoo0 )
   else :
    iiiii1II ( 'Text File not formated correctly!' , '' , themeit = OOoO )
    wiz . log ( "[Addon Menu] ERROR: Invalid Format." )
  else :
   wiz . log ( "[Addon Menu] ERROR: URL for Addon list not working." )
   iiiii1II ( 'Url for txt file not valid' , '' , themeit = OOoO )
   iiiii1II ( '%s' % o0o0OoOOOOOo , '' , themeit = OOoO )
 else : wiz . log ( "[Addon Menu] No Addon list added." )
 iIi1 ( 'files' , 'viewType' )
 if 97 - 97: i11iIiiIii / i11IiIiiIIIII * oO0 % o0o0Oo0oooo0 . OoooooooOO
def IIiiI1iii1i ( plugin , url ) :
 if not OO == 'http://' :
  o0o0OoOOOOOo = wiz . workingURL ( url )
  if o0o0OoOOOOOo == True :
   i1oO0OO0 = wiz . openURL ( url ) . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' ) . replace ( 'repository=""' , 'repository="none"' ) . replace ( 'repositoryurl=""' , 'repositoryurl="http://"' ) . replace ( 'repositoryxml=""' , 'repositoryxml="http://"' )
   o0O0Oo00 = re . compile ( 'name="(.+?)".+?lugin="%s".+?rl="(.+?)".+?epository="(.+?)".+?epositoryxml="(.+?)".+?epositoryurl="(.+?)".+?con="(.+?)".+?anart="(.+?)".+?dult="(.+?)".+?escription="(.+?)"' % plugin ) . findall ( i1oO0OO0 )
   if len ( o0O0Oo00 ) > 0 :
    for O0Oo0o000oO , url , iII1 , III1I1 , ii1111Ii1i , Ii1ii111i1 , i1i1i1I , oOoo000 , OooOo00o in o0O0Oo00 :
     if os . path . exists ( os . path . join ( O0O , plugin ) ) :
      iiI1i1I11 = [ 'Launch Addon' , 'Remove Addon' ]
      i1iIiIIi1II1ii = iiIIIII1i1iI . select ( "[COLOR %s]Addon already installed what would you like to do?[/COLOR]" % iIiIi11 , iiI1i1I11 )
      if i1iIiIIi1II1ii == 0 :
       wiz . ebi ( 'RunAddon(%s)' % plugin )
       xbmc . sleep ( 500 )
       return True
      elif i1iIiIIi1II1ii == 1 :
       wiz . cleanHouse ( os . path . join ( O0O , plugin ) )
       try : wiz . removeFolder ( os . path . join ( O0O , plugin ) )
       except : pass
       if iiIIIII1i1iI . yesno ( o0OOO , "[COLOR %s]Would you like to remove the addon_data for:" % iIiIi11 , "[COLOR %s]%s[/COLOR]?[/COLOR]" % ( oOOo0O00o , plugin ) , yeslabel = "[B][COLOR green]Yes Remove[/COLOR][/B]" , nolabel = "[B][COLOR red]No Skip[/COLOR][/B]" ) :
        i1II1Ii1i1 ( plugin )
       wiz . refresh ( )
       return True
      else :
       return False
     I1i1I1I11IiiI = os . path . join ( O0O , iII1 )
     if not iII1 . lower ( ) == 'none' and not os . path . exists ( I1i1I1I11IiiI ) :
      wiz . log ( "Repository not installed, installing it" )
      if iiIIIII1i1iI . yesno ( o0OOO , "[COLOR %s]Would you like to install the repository for [COLOR %s]%s[/COLOR]:" % ( iIiIi11 , oOOo0O00o , plugin ) , "[COLOR %s]%s[/COLOR]?[/COLOR]" % ( oOOo0O00o , iII1 ) , yeslabel = "[B][COLOR green]Yes Install[/COLOR][/B]" , nolabel = "[B][COLOR red]No Skip[/COLOR][/B]" ) :
       i1iIi = wiz . parseDOM ( wiz . openURL ( III1I1 ) , 'addon' , ret = 'version' , attrs = { 'id' : iII1 } )
       if len ( i1iIi ) > 0 :
        I1IiI1iI11 = '%s%s-%s.zip' % ( ii1111Ii1i , iII1 , i1iIi [ 0 ] )
        wiz . log ( I1IiI1iI11 )
        if o0OIiII >= 17 : wiz . addonDatabase ( iII1 , 1 )
        iIi ( iII1 , I1IiI1iI11 )
        wiz . ebi ( 'UpdateAddonRepos()' )
        if 29 - 29: O0 . OO00O0O0O00Oo
        wiz . log ( "Installing Addon from Kodi" )
        OO0o0oO0O000o = I1iI11iii ( plugin )
        wiz . log ( "Install from Kodi: %s" % OO0o0oO0O000o )
        if OO0o0oO0O000o :
         wiz . refresh ( )
         return True
       else :
        wiz . log ( "[Addon Installer] Repository not installed: Unable to grab url! (%s)" % iII1 )
      else : wiz . log ( "[Addon Installer] Repository for %s not installed: %s" % ( plugin , iII1 ) )
     elif iII1 . lower ( ) == 'none' :
      wiz . log ( "No repository, installing addon" )
      oo0oO = plugin
      IiIi1iI11 = url
      iIi ( plugin , url )
      wiz . refresh ( )
      return True
     else :
      wiz . log ( "Repository installed, installing addon" )
      OO0o0oO0O000o = I1iI11iii ( plugin , False )
      if OO0o0oO0O000o :
       wiz . refresh ( )
       return True
     if os . path . exists ( os . path . join ( O0O , plugin ) ) : return True
     iiI1iI1I = wiz . parseDOM ( wiz . openURL ( III1I1 ) , 'addon' , ret = 'version' , attrs = { 'id' : plugin } )
     if len ( iiI1iI1I ) > 0 :
      url = "%s%s-%s.zip" % ( url , plugin , iiI1iI1I [ 0 ] )
      wiz . log ( str ( url ) )
      if o0OIiII >= 17 : wiz . addonDatabase ( plugin , 1 )
      iIi ( plugin , url )
      wiz . refresh ( )
     else :
      wiz . log ( "no match" ) ; return False
   else : wiz . log ( "[Addon Installer] Invalid Format" )
  else : wiz . log ( "[Addon Installer] Text File: %s" % o0o0OoOOOOOo )
 else : wiz . log ( "[Addon Installer] Not Enabled." )
 if 27 - 27: oO0 * OO00O0O0O00Oo - I1111 + IiiIII111ii * IiiIII111ii
def I1iI11iii ( plugin , over = True ) :
 if over == True :
  xbmc . sleep ( 2000 )
  if 55 - 55: OOoooooO
 wiz . ebi ( 'RunPlugin(plugin://%s)' % plugin )
 if not wiz . whileWindow ( 'yesnodialog' ) :
  return False
 xbmc . sleep ( 500 )
 if wiz . whileWindow ( 'okdialog' ) :
  return False
 wiz . whileWindow ( 'progressdialog' )
 if os . path . exists ( os . path . join ( O0O , plugin ) ) : return True
 else : return False
 if 82 - 82: OO00O0O0O00Oo - iii11iiII + I1111
def iIi ( name , url ) :
 if not wiz . workingURL ( url ) == True : wiz . LogNotify ( "[COLOR %s]Addon Installer[/COLOR]" % oOOo0O00o , '[COLOR %s]%s:[/COLOR] [COLOR %s]Invalid Zip Url![/COLOR]' % ( oOOo0O00o , name , iIiIi11 ) ) ; return
 if not os . path . exists ( o0o0OOO0o0 ) : os . makedirs ( o0o0OOO0o0 )
 oo00 . create ( o0OOO , '[COLOR %s][B]Downloading:[/B][/COLOR] [COLOR %s]%s[/COLOR]' % ( iIiIi11 , oOOo0O00o , name ) , '' , '[COLOR %s]Please Wait[/COLOR]' % iIiIi11 )
 OO0iIiiIi11IIi = url . split ( '/' )
 Oo0 = os . path . join ( o0o0OOO0o0 , OO0iIiiIi11IIi [ - 1 ] )
 try : os . remove ( Oo0 )
 except : pass
 downloader . download ( url , Oo0 , oo00 )
 OOoOoO00O0O0o = '[COLOR %s][B]Installing:[/B][/COLOR] [COLOR %s]%s[/COLOR]' % ( iIiIi11 , oOOo0O00o , name )
 oo00 . update ( 0 , OOoOoO00O0O0o , '' , '[COLOR %s]Please Wait[/COLOR]' % iIiIi11 )
 oOII1ii1ii11I1 , o0ooOO0o , ooo0 = extract . all ( Oo0 , O0O , oo00 , title = OOoOoO00O0O0o )
 oo00 . update ( 0 , OOoOoO00O0O0o , '' , '[COLOR %s]Installing Dependencies[/COLOR]' % iIiIi11 )
 i1iI1i1I1 ( name )
 O0Oo0 ( name , oo00 )
 oo00 . close ( )
 wiz . ebi ( 'UpdateAddonRepos()' )
 wiz . ebi ( 'UpdateLocalAddons()' )
 wiz . refresh ( )
 if 80 - 80: ooOo - iIii1I11I1II1 . iii11iiII + I1111 - OO00O0O0O00Oo
def O0Oo0 ( name , DP = None ) :
 iI1iIiiiI1I1 = os . path . join ( O0O , name , 'addon.xml' )
 if os . path . exists ( iI1iIiiiI1I1 ) :
  OOOOOo = open ( iI1iIiiiI1I1 , mode = 'r' ) ; i1oO0OO0 = OOOOOo . read ( ) ; OOOOOo . close ( ) ;
  o0O0Oo00 = wiz . parseDOM ( i1oO0OO0 , 'import' , ret = 'addon' )
  for I1IiiiIiI in o0O0Oo00 :
   if not 'xbmc.python' in I1IiiiIiI :
    if not DP == None :
     DP . update ( 0 , '' , '[COLOR %s]%s[/COLOR]' % ( oOOo0O00o , I1IiiiIiI ) )
    wiz . createTemp ( I1IiiiIiI )
    if 77 - 77: IiiIII111ii / II111iiii - IiiIII111ii / iii11iiII
    if 97 - 97: iii11iiII / IIIi1i1I . II111iiii
    if 44 - 44: IiiIII111ii % i11IiIiiIIIII . OO00O0O0O00Oo
    if 18 - 18: iIii1I11I1II1 + i11IiIiiIIIII * ooOo - iii11iiII / ooOo
    if 78 - 78: i11IiIiiIIIII . i1Ii
    if 38 - 38: o0o0Oo0oooo0 + i1Ii
    if 15 - 15: Ooo0O + i11IiIiiIIIII . OOoooooO - iIii1I11I1II1 / O0 % iIii1I11I1II1
    if 86 - 86: ooOo / IIIi1i1I * IiiIII111ii
    if 64 - 64: OOoooooO / O0 * o0o0Oo0oooo0 * OOoooooO
    if 60 - 60: i11IiIiiIIIII / i1IIi % oO0 / oO0 * oO0 . i11iIiiIii
    if 99 - 99: o0o0Oo0oooo0
    if 77 - 77: I1I1i1
    if 48 - 48: o0o0Oo0oooo0 % oO0 / i11IiIiiIIIII . iIii1I11I1II1 * II111iiii
    if 65 - 65: o0o0Oo0oooo0
    if 31 - 31: i11IiIiiIIIII * o0o0Oo0oooo0 . i1Ii % IiiIII111ii + Ooo0O
    if 47 - 47: O0 * ooOo * I1111 . II111iiii
    if 95 - 95: IiiIII111ii % i1Ii . O0 % OO00O0O0O00Oo
    if 68 - 68: Ooo0O . Ooo0O - oO0 / i11IiIiiIIIII . OOoooooO / i1IIi
    if 12 - 12: oO0 * i1IIi * i11IiIiiIIIII
    if 23 - 23: iii11iiII / O0 / ooOo
    if 49 - 49: i11IiIiiIIIII . I1I1i1 % IIIi1i1I / IiiIII111ii
    if 95 - 95: O0 * o0o0Oo0oooo0 * i1Ii . OOoooooO / iIii1I11I1II1
    if 28 - 28: i1Ii + IIIi1i1I - OOoooooO / iIii1I11I1II1 - ooOo
    if 45 - 45: O0 / i1IIi * IIIi1i1I * I1111
    if 35 - 35: oO0 / iiIIi1IiIi11 % ooOo + iIii1I11I1II1
    if 79 - 79: o0o0Oo0oooo0 / OOoooooO
def i1iI1i1I1 ( addon ) :
 oO0o00oOOooO0 = os . path . join ( O0O , addon , 'addon.xml' )
 if os . path . exists ( oO0o00oOOooO0 ) :
  try :
   list = open ( oO0o00oOOooO0 , mode = 'r' ) ; oOo00o = list . read ( ) ; list . close ( )
   O0Oo0o000oO = wiz . parseDOM ( oOo00o , 'addon' , ret = 'name' , attrs = { 'id' : addon } )
   Ii1ii111i1 = os . path . join ( O0O , addon , 'icon.png' )
   wiz . LogNotify ( '[COLOR %s]%s[/COLOR]' % ( oOOo0O00o , O0Oo0o000oO [ 0 ] ) , '[COLOR %s]Addon Enabled[/COLOR]' % iIiIi11 , '2000' , Ii1ii111i1 )
  except : pass
  if 98 - 98: iii11iiII % i1IIi . ooOo . II111iiii . oO0 / i11iIiiIii
def iIii1I ( url = None ) :
 if not oO0O0OO0O == 'http://' :
  if url == None :
   iii11i1 = wiz . workingURL ( oO0O0OO0O )
   i1IiI1I111iIi = uservar . YOUTUBEFILE
  else :
   iii11i1 = wiz . workingURL ( url )
   i1IiI1I111iIi = url
  if iii11i1 == True :
   i1oO0OO0 = wiz . openURL ( i1IiI1I111iIi ) . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
   o0O0Oo00 = re . compile ( 'name="(.+?)".+?ection="(.+?)".+?rl="(.+?)".+?con="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( i1oO0OO0 )
   if len ( o0O0Oo00 ) > 0 :
    for O0Oo0o000oO , IiiIIi1 , url , Ii1ii111i1 , i1i1i1I , OooOo00o in o0O0Oo00 :
     if IiiIIi1 . lower ( ) == "yes" :
      oo00O00oO000o ( "[B]%s[/B]" % O0Oo0o000oO , 'youtube' , url , description = OooOo00o , icon = Ii1ii111i1 , fanart = i1i1i1I , themeit = OOoO )
     else :
      iiiii1II ( O0Oo0o000oO , 'viewVideo' , url = url , description = OooOo00o , icon = Ii1ii111i1 , fanart = i1i1i1I , themeit = oooOo0OOOoo0 )
   else : wiz . log ( "[YouTube Menu] ERROR: Invalid Format." )
  else :
   wiz . log ( "[YouTube Menu] ERROR: URL for YouTube list not working." )
   iiiii1II ( 'Url for txt file not valid' , '' , themeit = OOoO )
   iiiii1II ( '%s' % iii11i1 , '' , themeit = OOoO )
 else : wiz . log ( "[YouTube Menu] No YouTube list added." )
 iIi1 ( 'files' , 'viewType' )
 if 28 - 28: I1I1i1
def IIiI1Ii1IIiI11i1 ( view = None ) :
 Ii11I1iIiiI = '[B][COLOR green]ON[/COLOR][/B]' ; O0o0OO00 = '[B][COLOR red]OFF[/COLOR][/B]'
 iIi11i = 'true' if ooOooo000oOO == 'true' else 'false'
 ooIII1II1iii1i = 'true' if Oo0oOOo == 'true' else 'false'
 O0OO0oOO = 'true' if Oo0OoO00oOO0o == 'true' else 'false'
 ooooO = 'true' if OOO00O == 'true' else 'false'
 oO0O0 = 'true' if oO0Ii1iIiII1ii1 == 'true' else 'false'
 iI111i11iI1 = 'true' if O00O0oOO00O00 == 'true' else 'false'
 III1ii = 'true' if i1Oo00 == 'true' else 'false'
 iI1III1iIi11 = 'true' if oOooOOOoOo == 'true' else 'false'
 if wiz . Grab_Log ( True ) == False : i11I1I = 0
 else : i11I1I = oo0ooooo00o ( wiz . Grab_Log ( True ) , True , True )
 if wiz . Grab_Log ( True , True ) == False : OoOo = 0
 else : OoOo = oo0ooooo00o ( wiz . Grab_Log ( True , True ) , True , True )
 i111i1iIi1 = int ( i11I1I ) + int ( OoOo )
 OoO0oO = str ( i111i1iIi1 ) + ' Error(s) Found' if i111i1iIi1 > 0 else 'None Found'
 IiiI1iiI1III1i = ': [COLOR red]Not Found[/COLOR]' if not os . path . exists ( I11iii1Ii ) else ": [COLOR green]%s[/COLOR]" % wiz . convertSize ( os . path . getsize ( I11iii1Ii ) )
 if III1ii == 'true' :
  iii1 = 'true'
  i11oooOo = 'true'
  oo0oo0O0 = 'true'
  IiIIiiI = 'true'
  o0o0OO0o00o0O = 'true'
  IIIIIIi1i = 'true'
  iiiii11I1 = 'true'
  Ii1 = 'true'
 else :
  iii1 = 'true' if i1i == 'true' else 'false'
  i11oooOo = 'true' if iiI111I1iIiI == 'true' else 'false'
  oo0oo0O0 = 'true' if IIIi1I1IIii1II == 'true' else 'false'
  IiIIiiI = 'true' if O0ii1ii1ii == 'true' else 'false'
  o0o0OO0o00o0O = 'true' if oooooOoo0ooo == 'true' else 'false'
  IIIIIIi1i = 'true' if I1I1IiI1 == 'true' else 'false'
  iiiii11I1 = 'true' if III1iII1I1ii == 'true' else 'false'
  Ii1 = 'true' if oOOo0 == 'true' else 'false'
 OOOo = wiz . getSize ( o0o0OOO0o0 )
 I1iI1IiI = wiz . getSize ( oOoOooOo0o0 )
 i1i1Ii1I = wiz . getCacheSize ( )
 I1II1III1 = OOOo + I1iI1IiI + i1i1Ii1I
 oooo0O0o0OoOO = [ 'Always' , 'Daily' , '3 Days' , 'Weekly' ]
 oo00O00oO000o ( '[B]Cleaning Tools[/B]' , 'maint' , 'clean' , icon = IiIi11iI , themeit = OOOiiiiI )
 if view == "clean" or oO0Ii1iIiII1ii1 == 'true' :
  iiiii1II ( 'Total Clean Up: [COLOR green][B]%s[/B][/COLOR]' % wiz . convertSize ( I1II1III1 ) , 'fullclean' , icon = IiIi11iI , themeit = OOoO )
  iiiii1II ( 'Clear Cache: [COLOR green][B]%s[/B][/COLOR]' % wiz . convertSize ( i1i1Ii1I ) , 'clearcache' , icon = IiIi11iI , themeit = OOoO )
  iiiii1II ( 'Clear Packages: [COLOR green][B]%s[/B][/COLOR]' % wiz . convertSize ( OOOo ) , 'clearpackages' , icon = IiIi11iI , themeit = OOoO )
  iiiii1II ( 'Clear Thumbnails: [COLOR green][B]%s[/B][/COLOR]' % wiz . convertSize ( I1iI1IiI ) , 'clearthumb' , icon = IiIi11iI , themeit = OOoO )
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
  iiiii1II ( 'View Errors in Log: %s' % ( OoO0oO ) , 'viewerrorlog' , icon = IiIi11iI , themeit = OOoO )
  iiiii1II ( 'View Log File' , 'viewlog' , icon = IiIi11iI , themeit = OOoO )
  iiiii1II ( 'View Wizard Log File' , 'viewwizlog' , icon = IiIi11iI , themeit = OOoO )
  iiiii1II ( 'Clear Wizard Log File%s' % IiiI1iiI1III1i , 'clearwizlog' , icon = IiIi11iI , themeit = OOoO )
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
 iiiii1II ( 'Show All Maintenance: %s' % oO0O0 . replace ( 'true' , Ii11I1iIiiI ) . replace ( 'false' , O0o0OO00 ) , 'togglesetting' , 'showmaint' , icon = IiIi11iI , themeit = oooOo0OOOoo0 )
 oo00O00oO000o ( '[I]<< Return to Main Menu[/I]' , icon = IiIi11iI , themeit = oooOo0OOOoo0 )
 iiiii1II ( 'Third Party Wizards: %s' % iI1III1iIi11 . replace ( 'true' , Ii11I1iIiiI ) . replace ( 'false' , O0o0OO00 ) , 'togglesetting' , 'enable3rd' , fanart = OOO00 , icon = IiIi11iI , themeit = OOOiiiiI )
 if iI1III1iIi11 == 'true' :
  III1 = i1Iii1i1I if not i1Iii1i1I == '' else 'Not Set'
  iiiI1I = IiI111111IIII if not IiI111111IIII == '' else 'Not Set'
  iIiiiii1i = OOO if not OOO == '' else 'Not Set'
  iiiii1II ( 'Edit Third Party Wizard 1: [COLOR %s]%s[/COLOR]' % ( iIiIi11 , III1 ) , 'editthird' , '1' , icon = IiIi11iI , themeit = OOoO )
  iiiii1II ( 'Edit Third Party Wizard 2: [COLOR %s]%s[/COLOR]' % ( iIiIi11 , iiiI1I ) , 'editthird' , '2' , icon = IiIi11iI , themeit = OOoO )
  iiiii1II ( 'Edit Third Party Wizard 3: [COLOR %s]%s[/COLOR]' % ( iIiIi11 , iIiiiii1i ) , 'editthird' , '3' , icon = IiIi11iI , themeit = OOoO )
 iiiii1II ( 'Auto Clean' , '' , fanart = OOO00 , icon = IiIi11iI , themeit = OOOiiiiI )
 iiiii1II ( 'Auto Clean Up On Startup: %s' % iIi11i . replace ( 'true' , Ii11I1iIiiI ) . replace ( 'false' , O0o0OO00 ) , 'togglesetting' , 'autoclean' , icon = IiIi11iI , themeit = OOoO )
 if iIi11i == 'true' :
  iiiii1II ( '--- Auto Clean Fequency: [B][COLOR green]%s[/COLOR][/B]' % oooo0O0o0OoOO [ OOoOO0oo0ooO ] , 'changefeq' , icon = IiIi11iI , themeit = OOoO )
  iiiii1II ( '--- Clear Cache on Startup: %s' % ooIII1II1iii1i . replace ( 'true' , Ii11I1iIiiI ) . replace ( 'false' , O0o0OO00 ) , 'togglesetting' , 'clearcache' , icon = IiIi11iI , themeit = OOoO )
  iiiii1II ( '--- Clear Packages on Startup: %s' % O0OO0oOO . replace ( 'true' , Ii11I1iIiiI ) . replace ( 'false' , O0o0OO00 ) , 'togglesetting' , 'clearpackages' , icon = IiIi11iI , themeit = OOoO )
  iiiii1II ( '--- Clear Old Thumbs on Startup: %s' % ooooO . replace ( 'true' , Ii11I1iIiiI ) . replace ( 'false' , O0o0OO00 ) , 'togglesetting' , 'clearthumbs' , icon = IiIi11iI , themeit = OOoO )
 iiiii1II ( 'Clear Video Cache' , '' , fanart = OOO00 , icon = IiIi11iI , themeit = OOOiiiiI )
 iiiii1II ( 'Include Video Cache in Clear Cache: %s' % iI111i11iI1 . replace ( 'true' , Ii11I1iIiiI ) . replace ( 'false' , O0o0OO00 ) , 'togglecache' , 'includevideo' , icon = IiIi11iI , themeit = OOoO )
 if iI111i11iI1 == 'true' :
  iiiii1II ( '--- Include All Video Addons: %s' % III1ii . replace ( 'true' , Ii11I1iIiiI ) . replace ( 'false' , O0o0OO00 ) , 'togglecache' , 'includeall' , icon = IiIi11iI , themeit = OOoO )
  iiiii1II ( '--- Include Bob: %s' % iii1 . replace ( 'true' , Ii11I1iIiiI ) . replace ( 'false' , O0o0OO00 ) , 'togglecache' , 'includebob' , icon = IiIi11iI , themeit = OOoO )
  iiiii1II ( '--- Include Phoenix: %s' % i11oooOo . replace ( 'true' , Ii11I1iIiiI ) . replace ( 'false' , O0o0OO00 ) , 'togglecache' , 'includephoenix' , icon = IiIi11iI , themeit = OOoO )
  iiiii1II ( '--- Include Specto: %s' % oo0oo0O0 . replace ( 'true' , Ii11I1iIiiI ) . replace ( 'false' , O0o0OO00 ) , 'togglecache' , 'includespecto' , icon = IiIi11iI , themeit = OOoO )
  iiiii1II ( '--- Include Exodus: %s' % o0o0OO0o00o0O . replace ( 'true' , Ii11I1iIiiI ) . replace ( 'false' , O0o0OO00 ) , 'togglecache' , 'includeexodus' , icon = IiIi11iI , themeit = OOoO )
  iiiii1II ( '--- Include Salts: %s' % iiiii11I1 . replace ( 'true' , Ii11I1iIiiI ) . replace ( 'false' , O0o0OO00 ) , 'togglecache' , 'includesalts' , icon = IiIi11iI , themeit = OOoO )
  iiiii1II ( '--- Include Salts HD Lite: %s' % Ii1 . replace ( 'true' , Ii11I1iIiiI ) . replace ( 'false' , O0o0OO00 ) , 'togglecache' , 'includesaltslite' , icon = IiIi11iI , themeit = OOoO )
  iiiii1II ( '--- Include One Channel: %s' % IIIIIIi1i . replace ( 'true' , Ii11I1iIiiI ) . replace ( 'false' , O0o0OO00 ) , 'togglecache' , 'includeonechan' , icon = IiIi11iI , themeit = OOoO )
  iiiii1II ( '--- Include Genesis: %s' % IiIIiiI . replace ( 'true' , Ii11I1iIiiI ) . replace ( 'false' , O0o0OO00 ) , 'togglecache' , 'includegenesis' , icon = IiIi11iI , themeit = OOoO )
  iiiii1II ( '--- Enable All Video Addons' , 'togglecache' , 'true' , icon = IiIi11iI , themeit = OOoO )
  iiiii1II ( '--- Disable All Video Addons' , 'togglecache' , 'false' , icon = IiIi11iI , themeit = OOoO )
 iIi1 ( 'files' , 'viewType' )
 if 91 - 91: oO0 % OOoooooO
def i1i1II1I ( url = None ) :
 if not OoOoO == 'http://' :
  if url == None :
   oO000Oo = wiz . workingURL ( OoOoO )
   Ii1i1i = uservar . ADVANCEDFILE
  else :
   oO000Oo = wiz . workingURL ( url )
   Ii1i1i = url
  iiiii1II ( 'Quick Configure AdvancedSettings.xml' , 'autoadvanced' , icon = IiIi11iI , themeit = OOoO )
  if os . path . exists ( I11II1i ) :
   iiiii1II ( 'View Currect AdvancedSettings.xml' , 'currentsettings' , icon = IiIi11iI , themeit = OOoO )
   iiiii1II ( 'Remove Currect AdvancedSettings.xml' , 'removeadvanced' , icon = IiIi11iI , themeit = OOoO )
  if oO000Oo == True :
   if O0O0ooOOO == 'No' : iiiii1II ( wiz . sep ( ) , '' , icon = IiIi11iI , themeit = OOoO )
   i1oO0OO0 = wiz . openURL ( Ii1i1i ) . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
   o0O0Oo00 = re . compile ( 'name="(.+?)".+?ection="(.+?)".+?rl="(.+?)".+?con="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( i1oO0OO0 )
   if len ( o0O0Oo00 ) > 0 :
    for O0Oo0o000oO , IiiIIi1 , url , Ii1ii111i1 , i1i1i1I , OooOo00o in o0O0Oo00 :
     if IiiIIi1 . lower ( ) == "yes" :
      oo00O00oO000o ( "[B]%s[/B]" % O0Oo0o000oO , 'advancedsetting' , url , description = OooOo00o , icon = Ii1ii111i1 , fanart = i1i1i1I , themeit = OOoO )
     else :
      iiiii1II ( O0Oo0o000oO , 'writeadvanced' , O0Oo0o000oO , url , description = OooOo00o , icon = Ii1ii111i1 , fanart = i1i1i1I , themeit = oooOo0OOOoo0 )
   else : wiz . log ( "[Advanced Settings] ERROR: Invalid Format." )
  else : wiz . log ( "[Advanced Settings] URL not working: %s" % oO000Oo )
 else : wiz . log ( "[Advanced Settings] not Enabled" )
 if 34 - 34: iiIIi1IiIi11
def iIi1IIiIII1 ( name , url ) :
 oO000Oo = wiz . workingURL ( url )
 if oO000Oo == True :
  if os . path . exists ( I11II1i ) : i1Ii11I1II = iiIIIII1i1iI . yesno ( o0OOO , "[COLOR %s]Would you like to overwrite your current Advanced Settings with [COLOR %s]%s[/COLOR]?[/COLOR]" % ( iIiIi11 , oOOo0O00o , name ) , yeslabel = "[B][COLOR green]Overwrite[/COLOR][/B]" , nolabel = "[B][COLOR red]Cancel[/COLOR][/B]" )
  else : i1Ii11I1II = iiIIIII1i1iI . yesno ( o0OOO , "[COLOR %s]Would you like to download and install [COLOR %s]%s[/COLOR]?[/COLOR]" % ( iIiIi11 , oOOo0O00o , name ) , yeslabel = "[B][COLOR green]Install[/COLOR][/B]" , nolabel = "[B][COLOR red]Cancel[/COLOR][/B]" )
  if 77 - 77: IIIi1i1I - Ooo0O - iIii1I11I1II1
  if i1Ii11I1II == 1 :
   file = wiz . openURL ( url )
   IIi1i = open ( I11II1i , 'w' ) ;
   IIi1i . write ( file )
   IIi1i . close ( )
   iiIIIII1i1iI . ok ( o0OOO , '[COLOR %s]AdvancedSettings.xml file has been successfully written.  Once you click okay it will force close kodi.[/COLOR]' % iIiIi11 )
   wiz . killxbmc ( True )
  else : wiz . log ( "[Advanced Settings] install canceled" ) ; wiz . LogNotify ( '[COLOR %s]%s[/COLOR]' % ( oOOo0O00o , o0OOO ) , "[COLOR %s]Write Cancelled![/COLOR]" % iIiIi11 ) ; return
 else : wiz . log ( "[Advanced Settings] URL not working: %s" % oO000Oo ) ; wiz . LogNotify ( '[COLOR %s]%s[/COLOR]' % ( oOOo0O00o , o0OOO ) , "[COLOR %s]URL Not Working[/COLOR]" % iIiIi11 )
 if 21 - 21: IIIi1i1I % IIIi1i1I / I1111
def i1II ( ) :
 IIi1i = open ( I11II1i )
 IiiIi11Ii1iI1 = IIi1i . read ( ) . replace ( '\t' , '    ' )
 wiz . TextBox ( o0OOO , IiiIi11Ii1iI1 )
 IIi1i . close ( )
 if 91 - 91: iii11iiII + OO00O0O0O00Oo . i11IiIiiIIIII
def i1I111i1ii ( ) :
 if os . path . exists ( I11II1i ) :
  wiz . removeFile ( I11II1i )
 else : LogNotify ( "[COLOR %s]%s[/COLOR]" % ( oOOo0O00o , o0OOO ) , "[COLOR %s]AdvancedSettings.xml not found[/COLOR]" )
 if 81 - 81: Ooo0O - i11IiIiiIIIII
def ii1iII1iI111 ( ) :
 notify . autoConfig ( )
 if 94 - 94: iiIIi1IiIi11 % OOoooooO . IIIi1i1I
def O00oOo0O0o00O ( ) :
 ooo0oo00O00Oo = 'http://whatismyipaddress.com/'
 if not wiz . workingURL ( ooo0oo00O00Oo ) : return 'Unknown' , 'Unknown' , 'Unknown'
 OOO000000OOO0 = wiz . openURL ( ooo0oo00O00Oo ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 if not 'Access Denied' in OOO000000OOO0 :
  ooOoOOoooO000 = re . compile ( 'whatismyipaddress.com/ip/(.+?)"' ) . findall ( OOO000000OOO0 )
  OoO0o000oOo = ooOoOOoooO000 [ 0 ] if ( len ( ooOoOOoooO000 ) > 0 ) else 'Unknown'
  Oo00OO00o0oO = re . compile ( '"font-size:14px;">(.+?)</td>' ) . findall ( OOO000000OOO0 )
  iI1 = Oo00OO00o0oO [ 0 ] if ( len ( Oo00OO00o0oO ) > 0 ) else 'Unknown'
  I1I1i1i = Oo00OO00o0oO [ 1 ] + ', ' + Oo00OO00o0oO [ 2 ] + ', ' + Oo00OO00o0oO [ 3 ] if ( len ( Oo00OO00o0oO ) > 2 ) else 'Unknown'
  return OoO0o000oOo , iI1 , I1I1i1i
 else : return 'Unknown' , 'Unknown' , 'Unknown'
 if 87 - 87: o0o0Oo0oooo0 / i1Ii . OOoooooO - iii11iiII / I1111
def iiI1I ( ) :
 ooI111iiiii1 = [ 'System.FriendlyName' ,
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
 OO0ooOoOO0OOo = [ ] ; II1IOoOo000oOo0oo = 0
 for OooOoooo0000 in ooI111iiiii1 :
  I1ii1i11i = wiz . getInfo ( OooOoooo0000 )
  Oooooo0O00o = 0
  while I1ii1i11i == "Busy" and Oooooo0O00o < 10 :
   I1ii1i11i = wiz . getInfo ( OooOoooo0000 ) ; Oooooo0O00o += 1 ; wiz . log ( "%s sleep %s" % ( OooOoooo0000 , str ( Oooooo0O00o ) ) ) ; xbmc . sleep ( 200 )
  OO0ooOoOO0OOo . append ( I1ii1i11i )
  II1IOoOo000oOo0oo += 1
 II11ii1 = OO0ooOoOO0OOo [ 8 ] if 'Una' in OO0ooOoOO0OOo [ 8 ] else wiz . convertSize ( int ( float ( OO0ooOoOO0OOo [ 8 ] [ : - 8 ] ) ) * 1024 * 1024 )
 ii1II1II = OO0ooOoOO0OOo [ 9 ] if 'Una' in OO0ooOoOO0OOo [ 9 ] else wiz . convertSize ( int ( float ( OO0ooOoOO0OOo [ 9 ] [ : - 8 ] ) ) * 1024 * 1024 )
 i11i11II11i = OO0ooOoOO0OOo [ 10 ] if 'Una' in OO0ooOoOO0OOo [ 10 ] else wiz . convertSize ( int ( float ( OO0ooOoOO0OOo [ 10 ] [ : - 8 ] ) ) * 1024 * 1024 )
 II1Ii1I1i = wiz . convertSize ( int ( float ( OO0ooOoOO0OOo [ 11 ] [ : - 2 ] ) ) * 1024 * 1024 )
 OOooOooo0OOo0 = wiz . convertSize ( int ( float ( OO0ooOoOO0OOo [ 12 ] [ : - 2 ] ) ) * 1024 * 1024 )
 oo0o0OoOO0o0 = wiz . convertSize ( int ( float ( OO0ooOoOO0OOo [ 13 ] [ : - 2 ] ) ) * 1024 * 1024 )
 III1III11II , iI1 , I1I1i1i = O00oOo0O0o00O ( )
 if 43 - 43: ooOo
 iiIIIiI1Ii = [ ] ; IIiiiiiIiIIi = [ ] ; iiIiiIi1 = [ ] ; I1Ii11i = [ ] ; I1iIiiiI1 = [ ] ; OOO0O00Oo = [ ] ; ii1oOOO0ooOO = [ ]
 if 3 - 3: OoooooooOO
 O0OoO0o = glob . glob ( os . path . join ( O0O , '*/' ) )
 for I111IIiIII in sorted ( O0OoO0o , key = lambda II1IOoOo000oOo0oo : II1IOoOo000oOo0oo ) :
  OO0OOoo0OOO = os . path . split ( I111IIiIII [ : - 1 ] ) [ 1 ]
  if OO0OOoo0OOO == 'packages' : continue
  ooooOoo0OO = os . path . join ( I111IIiIII , 'addon.xml' )
  if os . path . exists ( ooooOoo0OO ) :
   IIi1i = open ( ooooOoo0OO )
   IiiIi11Ii1iI1 = IIi1i . read ( )
   Oo0O0000Oo00o = re . compile ( "<provides>(.+?)</provides>" ) . findall ( IiiIi11Ii1iI1 )
   if len ( Oo0O0000Oo00o ) == 0 :
    if OO0OOoo0OOO . startswith ( 'skin' ) : ii1oOOO0ooOO . append ( OO0OOoo0OOO )
    if OO0OOoo0OOO . startswith ( 'repo' ) : I1iIiiiI1 . append ( OO0OOoo0OOO )
    else : OOO0O00Oo . append ( OO0OOoo0OOO )
   elif not ( Oo0O0000Oo00o [ 0 ] ) . find ( 'executable' ) == - 1 : I1Ii11i . append ( OO0OOoo0OOO )
   elif not ( Oo0O0000Oo00o [ 0 ] ) . find ( 'video' ) == - 1 : iiIiiIi1 . append ( OO0OOoo0OOO )
   elif not ( Oo0O0000Oo00o [ 0 ] ) . find ( 'audio' ) == - 1 : IIiiiiiIiIIi . append ( OO0OOoo0OOO )
   elif not ( Oo0O0000Oo00o [ 0 ] ) . find ( 'image' ) == - 1 : iiIIIiI1Ii . append ( OO0OOoo0OOO )
   if 20 - 20: I1111 . ooOo * i11iIiiIii / i11iIiiIii
 iiiii1II ( '[B]Media Center Info:[/B]' , '' , icon = IiIi11iI , themeit = oooOo0OOOoo0 )
 iiiii1II ( '[COLOR %s]Name:[/COLOR] [COLOR %s]%s[/COLOR]' % ( oOOo0O00o , iIiIi11 , OO0ooOoOO0OOo [ 0 ] ) , '' , icon = IiIi11iI , themeit = OOoO )
 iiiii1II ( '[COLOR %s]Version:[/COLOR] [COLOR %s]%s[/COLOR]' % ( oOOo0O00o , iIiIi11 , OO0ooOoOO0OOo [ 1 ] ) , '' , icon = IiIi11iI , themeit = OOoO )
 iiiii1II ( '[COLOR %s]Platform:[/COLOR] [COLOR %s]%s[/COLOR]' % ( oOOo0O00o , iIiIi11 , wiz . platform ( ) . title ( ) ) , '' , icon = IiIi11iI , themeit = OOoO )
 iiiii1II ( '[COLOR %s]CPU Usage:[/COLOR] [COLOR %s]%s[/COLOR]' % ( oOOo0O00o , iIiIi11 , OO0ooOoOO0OOo [ 2 ] ) , '' , icon = IiIi11iI , themeit = OOoO )
 iiiii1II ( '[COLOR %s]Screen Mode:[/COLOR] [COLOR %s]%s[/COLOR]' % ( oOOo0O00o , iIiIi11 , OO0ooOoOO0OOo [ 3 ] ) , '' , icon = IiIi11iI , themeit = OOoO )
 if 89 - 89: iiIIi1IiIi11 . i11iIiiIii * O0
 iiiii1II ( '[B]Uptime:[/B]' , '' , icon = IiIi11iI , themeit = oooOo0OOOoo0 )
 iiiii1II ( '[COLOR %s]Current Uptime:[/COLOR] [COLOR %s]%s[/COLOR]' % ( oOOo0O00o , iIiIi11 , OO0ooOoOO0OOo [ 6 ] ) , '' , icon = IiIi11iI , themeit = oooOo0OOOoo0 )
 iiiii1II ( '[COLOR %s]Total Uptime:[/COLOR] [COLOR %s]%s[/COLOR]' % ( oOOo0O00o , iIiIi11 , OO0ooOoOO0OOo [ 7 ] ) , '' , icon = IiIi11iI , themeit = oooOo0OOOoo0 )
 if 44 - 44: i1IIi . ooOo / i11iIiiIii + i1Ii
 iiiii1II ( '[B]Local Storage:[/B]' , '' , icon = IiIi11iI , themeit = oooOo0OOOoo0 )
 iiiii1II ( '[COLOR %s]Used Storage:[/COLOR] [COLOR %s]%s[/COLOR]' % ( oOOo0O00o , iIiIi11 , II11ii1 ) , '' , icon = IiIi11iI , themeit = oooOo0OOOoo0 )
 iiiii1II ( '[COLOR %s]Free Storage:[/COLOR] [COLOR %s]%s[/COLOR]' % ( oOOo0O00o , iIiIi11 , ii1II1II ) , '' , icon = IiIi11iI , themeit = oooOo0OOOoo0 )
 iiiii1II ( '[COLOR %s]Total Storage:[/COLOR] [COLOR %s]%s[/COLOR]' % ( oOOo0O00o , iIiIi11 , i11i11II11i ) , '' , icon = IiIi11iI , themeit = oooOo0OOOoo0 )
 if 27 - 27: iii11iiII
 iiiii1II ( '[B]Ram Usage:[/B]' , '' , icon = IiIi11iI , themeit = oooOo0OOOoo0 )
 iiiii1II ( '[COLOR %s]Used Memory:[/COLOR] [COLOR %s]%s[/COLOR]' % ( oOOo0O00o , iIiIi11 , II1Ii1I1i ) , '' , icon = IiIi11iI , themeit = oooOo0OOOoo0 )
 iiiii1II ( '[COLOR %s]Free Memory:[/COLOR] [COLOR %s]%s[/COLOR]' % ( oOOo0O00o , iIiIi11 , OOooOooo0OOo0 ) , '' , icon = IiIi11iI , themeit = oooOo0OOOoo0 )
 iiiii1II ( '[COLOR %s]Total Memory:[/COLOR] [COLOR %s]%s[/COLOR]' % ( oOOo0O00o , iIiIi11 , oo0o0OoOO0o0 ) , '' , icon = IiIi11iI , themeit = oooOo0OOOoo0 )
 if 52 - 52: OO00O0O0O00Oo % o0o0Oo0oooo0 + iIii1I11I1II1 * IIIi1i1I . IiiIII111ii
 iiiii1II ( '[B]Network:[/B]' , '' , icon = IiIi11iI , themeit = oooOo0OOOoo0 )
 iiiii1II ( '[COLOR %s]Local IP:[/COLOR] [COLOR %s]%s[/COLOR]' % ( oOOo0O00o , iIiIi11 , OO0ooOoOO0OOo [ 4 ] ) , '' , icon = IiIi11iI , themeit = oooOo0OOOoo0 )
 iiiii1II ( '[COLOR %s]External IP:[/COLOR] [COLOR %s]%s[/COLOR]' % ( oOOo0O00o , iIiIi11 , III1III11II ) , '' , icon = IiIi11iI , themeit = oooOo0OOOoo0 )
 iiiii1II ( '[COLOR %s]Provider:[/COLOR] [COLOR %s]%s[/COLOR]' % ( oOOo0O00o , iIiIi11 , iI1 ) , '' , icon = IiIi11iI , themeit = oooOo0OOOoo0 )
 iiiii1II ( '[COLOR %s]Location:[/COLOR] [COLOR %s]%s[/COLOR]' % ( oOOo0O00o , iIiIi11 , I1I1i1i ) , '' , icon = IiIi11iI , themeit = oooOo0OOOoo0 )
 iiiii1II ( '[COLOR %s]MacAddress:[/COLOR] [COLOR %s]%s[/COLOR]' % ( oOOo0O00o , iIiIi11 , OO0ooOoOO0OOo [ 5 ] ) , '' , icon = IiIi11iI , themeit = oooOo0OOOoo0 )
 if 95 - 95: iIii1I11I1II1 . i1Ii - OoooooooOO * I1111 / I1I1i1
 oOo0OO0o0 = len ( iiIIIiI1Ii ) + len ( IIiiiiiIiIIi ) + len ( iiIiiIi1 ) + len ( I1Ii11i ) + len ( OOO0O00Oo ) + len ( ii1oOOO0ooOO ) + len ( I1iIiiiI1 )
 iiiii1II ( '[B]Addons([COLOR %s]%s[/COLOR]):[/B]' % ( oOOo0O00o , oOo0OO0o0 ) , '' , icon = IiIi11iI , themeit = oooOo0OOOoo0 )
 iiiii1II ( '[COLOR %s]Video Addons:[/COLOR] [COLOR %s]%s[/COLOR]' % ( oOOo0O00o , iIiIi11 , str ( len ( iiIiiIi1 ) ) ) , '' , icon = IiIi11iI , themeit = oooOo0OOOoo0 )
 iiiii1II ( '[COLOR %s]Program Addons:[/COLOR] [COLOR %s]%s[/COLOR]' % ( oOOo0O00o , iIiIi11 , str ( len ( I1Ii11i ) ) ) , '' , icon = IiIi11iI , themeit = oooOo0OOOoo0 )
 iiiii1II ( '[COLOR %s]Music Addons:[/COLOR] [COLOR %s]%s[/COLOR]' % ( oOOo0O00o , iIiIi11 , str ( len ( IIiiiiiIiIIi ) ) ) , '' , icon = IiIi11iI , themeit = oooOo0OOOoo0 )
 iiiii1II ( '[COLOR %s]Picture Addons:[/COLOR] [COLOR %s]%s[/COLOR]' % ( oOOo0O00o , iIiIi11 , str ( len ( iiIIIiI1Ii ) ) ) , '' , icon = IiIi11iI , themeit = oooOo0OOOoo0 )
 iiiii1II ( '[COLOR %s]Repositories:[/COLOR] [COLOR %s]%s[/COLOR]' % ( oOOo0O00o , iIiIi11 , str ( len ( I1iIiiiI1 ) ) ) , '' , icon = IiIi11iI , themeit = oooOo0OOOoo0 )
 iiiii1II ( '[COLOR %s]Skins:[/COLOR] [COLOR %s]%s[/COLOR]' % ( oOOo0O00o , iIiIi11 , str ( len ( ii1oOOO0ooOO ) ) ) , '' , icon = IiIi11iI , themeit = oooOo0OOOoo0 )
 iiiii1II ( '[COLOR %s]Scripts/Modules:[/COLOR] [COLOR %s]%s[/COLOR]' % ( oOOo0O00o , iIiIi11 , str ( len ( OOO0O00Oo ) ) ) , '' , icon = IiIi11iI , themeit = oooOo0OOOoo0 )
 if 35 - 35: Ooo0O . Ooo0O % OoooooooOO - IiiIII111ii
def iIII11Iiii1 ( ) :
 Ii11I1iIiiI = '[COLOR green]ON[/COLOR]' ; O0o0OO00 = '[COLOR red]OFF[/COLOR]'
 o0oo0 = 'true' if o0O0OOO0Ooo == 'true' else 'false'
 OoO0OOoO0Oo0 = 'true' if iiIiII1 == 'true' else 'false'
 oO00O = 'true' if OOO00O0O == 'true' else 'false'
 II111IiiiI1 = 'true' if ooOOoooooo == 'true' else 'false'
 oooOO0oo0Oo00 = 'true' if O0i1II1Iiii1I11 == 'true' else 'false'
 oOoO = 'true' if II1I == 'true' else 'false'
 iI111I1III = 'true' if IiIIIi1iIi == 'true' else 'false'
 I1iIiiiI1 = 'true' if IIII == 'true' else 'false'
 super = 'true' if iiIiI == 'true' else 'false'
 i111IiiI1Ii = 'true' if o00oooO0Oo == 'true' else 'false'
 if 72 - 72: O0 . o0o0Oo0oooo0 * Ooo0O + oO0 - I1I1i1
 oo00O00oO000o ( 'Keep Trakt Data' , 'trakt' , icon = iIIii , themeit = OOOiiiiI )
 oo00O00oO000o ( 'Keep Real Debrid' , 'realdebrid' , icon = o00O0O , themeit = OOOiiiiI )
 oo00O00oO000o ( 'Keep Login Info' , 'login' , icon = ii1iii1i , themeit = OOOiiiiI )
 iiiii1II ( 'Import Save Data' , 'managedata' , 'import' , icon = I1111i , themeit = OOOiiiiI )
 iiiii1II ( 'Export Save Data' , 'managedata' , 'export' , icon = I1111i , themeit = OOOiiiiI )
 iiiii1II ( '- Click to toggle settings -' , '' , themeit = OOoO )
 iiiii1II ( 'Save Trakt: %s' % o0oo0 . replace ( 'true' , Ii11I1iIiiI ) . replace ( 'false' , O0o0OO00 ) , 'togglesetting' , 'keeptrakt' , icon = iIIii , themeit = OOOiiiiI )
 iiiii1II ( 'Save Real Debrid: %s' % OoO0OOoO0Oo0 . replace ( 'true' , Ii11I1iIiiI ) . replace ( 'false' , O0o0OO00 ) , 'togglesetting' , 'keepdebrid' , icon = o00O0O , themeit = OOOiiiiI )
 iiiii1II ( 'Save Login Info: %s' % oO00O . replace ( 'true' , Ii11I1iIiiI ) . replace ( 'false' , O0o0OO00 ) , 'togglesetting' , 'keeplogin' , icon = ii1iii1i , themeit = OOOiiiiI )
 iiiii1II ( 'Keep \'Sources.xml\': %s' % II111IiiiI1 . replace ( 'true' , Ii11I1iIiiI ) . replace ( 'false' , O0o0OO00 ) , 'togglesetting' , 'keepsources' , icon = I1111i , themeit = OOOiiiiI )
 iiiii1II ( 'Keep \'Profiles.xml\': %s' % oOoO . replace ( 'true' , Ii11I1iIiiI ) . replace ( 'false' , O0o0OO00 ) , 'togglesetting' , 'keepprofiles' , icon = I1111i , themeit = OOOiiiiI )
 iiiii1II ( 'Keep \'Advancedsettings.xml\': %s' % oooOO0oo0Oo00 . replace ( 'true' , Ii11I1iIiiI ) . replace ( 'false' , O0o0OO00 ) , 'togglesetting' , 'keepadvanced' , icon = I1111i , themeit = OOOiiiiI )
 iiiii1II ( 'Keep \'Favourites.xml\': %s' % iI111I1III . replace ( 'true' , Ii11I1iIiiI ) . replace ( 'false' , O0o0OO00 ) , 'togglesetting' , 'keepfavourites' , icon = I1111i , themeit = OOOiiiiI )
 iiiii1II ( 'Keep Super Favourites: %s' % super . replace ( 'true' , Ii11I1iIiiI ) . replace ( 'false' , O0o0OO00 ) , 'togglesetting' , 'keepsuper' , icon = I1111i , themeit = OOOiiiiI )
 iiiii1II ( 'Keep Installed Repo\'s: %s' % I1iIiiiI1 . replace ( 'true' , Ii11I1iIiiI ) . replace ( 'false' , O0o0OO00 ) , 'togglesetting' , 'keeprepos' , icon = I1111i , themeit = OOOiiiiI )
 iiiii1II ( 'Keep My \'WhiteList\': %s' % i111IiiI1Ii . replace ( 'true' , Ii11I1iIiiI ) . replace ( 'false' , O0o0OO00 ) , 'togglesetting' , 'keepwhitelist' , icon = I1111i , themeit = OOOiiiiI )
 if i111IiiI1Ii == 'true' :
  iiiii1II ( 'Edit My Whitelist' , 'whitelist' , 'edit' , icon = I1111i , themeit = OOOiiiiI )
  iiiii1II ( 'View My Whitelist' , 'whitelist' , 'view' , icon = I1111i , themeit = OOOiiiiI )
  iiiii1II ( 'Clear My Whitelist' , 'whitelist' , 'clear' , icon = I1111i , themeit = OOOiiiiI )
  iiiii1II ( 'Import My Whitelist' , 'whitelist' , 'import' , icon = I1111i , themeit = OOOiiiiI )
  iiiii1II ( 'Export My Whitelist' , 'whitelist' , 'export' , icon = I1111i , themeit = OOOiiiiI )
 iIi1 ( 'files' , 'viewType' )
 if 40 - 40: I1111 + I1111
def o0oo0o00ooO00 ( ) :
 o0oo0 = '[COLOR green]ON[/COLOR]' if o0O0OOO0Ooo == 'true' else '[COLOR red]OFF[/COLOR]'
 IIiIiiI1i = str ( O000OOo00oo ) if not O000OOo00oo == '' else 'Trakt hasnt been saved yet.'
 iiiii1II ( '[I]Register FREE Account at http://trakt.tv[/I]' , '' , icon = iIIii , themeit = OOoO )
 iiiii1II ( 'Save Trakt Data: %s' % o0oo0 , 'togglesetting' , 'keeptrakt' , icon = iIIii , themeit = OOoO )
 if o0O0OOO0Ooo == 'true' : iiiii1II ( 'Last Save: %s' % str ( IIiIiiI1i ) , '' , icon = iIIii , themeit = OOoO )
 if O0O0ooOOO == 'No' : iiiii1II ( wiz . sep ( ) , '' , icon = iIIii , themeit = OOoO )
 if 49 - 49: oO0 . i1Ii . i1IIi * o0o0Oo0oooo0 % iIii1I11I1II1
 for o0oo0 in traktit . ORDER :
  O0Oo0o000oO = oOOOoo00 [ o0oo0 ] [ 'name' ]
  III11I1 = oOOOoo00 [ o0oo0 ] [ 'path' ]
  OOOO0o0O = oOOOoo00 [ o0oo0 ] [ 'saved' ]
  file = oOOOoo00 [ o0oo0 ] [ 'file' ]
  iI111I = wiz . getS ( OOOO0o0O )
  O00OoOoO = traktit . traktUser ( o0oo0 )
  Ii1ii111i1 = oOOOoo00 [ o0oo0 ] [ 'icon' ] if os . path . exists ( III11I1 ) else iIIii
  i1i1i1I = oOOOoo00 [ o0oo0 ] [ 'fanart' ] if os . path . exists ( III11I1 ) else OOO00
  OoOo00o0OO = ii1IIIIiI11 ( 'saveaddon' , 'Trakt' , o0oo0 )
  ooO0o0oo = ii1IIIIiI11 ( 'save' , 'Trakt' , o0oo0 )
  OoOo00o0OO . append ( ( oooOo0OOOoo0 % '%s Settings' % O0Oo0o000oO , 'RunPlugin(plugin://%s/?mode=opensettings&name=%s&url=trakt)' % ( IiII1IiiIiI1 , o0oo0 ) ) )
  if 79 - 79: i1Ii % I1111
  iiiii1II ( '[+]-> %s' % O0Oo0o000oO , '' , icon = Ii1ii111i1 , fanart = i1i1i1I , themeit = OOoO )
  if not os . path . exists ( III11I1 ) : iiiii1II ( '[COLOR red]Addon Data: Not Installed[/COLOR]' , '' , icon = Ii1ii111i1 , fanart = i1i1i1I , menu = OoOo00o0OO )
  elif not O00OoOoO : iiiii1II ( '[COLOR red]Addon Data: Not Registered[/COLOR]' , 'authtrakt' , o0oo0 , icon = Ii1ii111i1 , fanart = i1i1i1I , menu = OoOo00o0OO )
  else : iiiii1II ( '[COLOR green]Addon Data: %s[/COLOR]' % O00OoOoO , 'authtrakt' , o0oo0 , icon = Ii1ii111i1 , fanart = i1i1i1I , menu = OoOo00o0OO )
  if iI111I == "" :
   if os . path . exists ( file ) : iiiii1II ( '[COLOR red]Saved Data: Save File Found(Import Data)[/COLOR]' , 'importtrakt' , o0oo0 , icon = Ii1ii111i1 , fanart = i1i1i1I , menu = ooO0o0oo )
   else : iiiii1II ( '[COLOR red]Saved Data: Not Saved[/COLOR]' , 'savetrakt' , o0oo0 , icon = Ii1ii111i1 , fanart = i1i1i1I , menu = ooO0o0oo )
  else : iiiii1II ( '[COLOR green]Saved Data: %s[/COLOR]' % iI111I , '' , icon = Ii1ii111i1 , fanart = i1i1i1I , menu = ooO0o0oo )
  if 81 - 81: i11iIiiIii + i11iIiiIii * I1111 + i1Ii
 if O0O0ooOOO == 'No' : iiiii1II ( wiz . sep ( ) , '' , themeit = OOoO )
 iiiii1II ( 'Save All Trakt Data' , 'savetrakt' , 'all' , icon = iIIii , themeit = OOoO )
 iiiii1II ( 'Recover All Saved Trakt Data' , 'restoretrakt' , 'all' , icon = iIIii , themeit = OOoO )
 iiiii1II ( 'Import Trakt Data' , 'importtrakt' , 'all' , icon = iIIii , themeit = OOoO )
 iiiii1II ( 'Clear All Saved Trakt Data' , 'cleartrakt' , 'all' , icon = iIIii , themeit = OOoO )
 iiiii1II ( 'Clear All Addon Data' , 'addontrakt' , 'all' , icon = iIIii , themeit = OOoO )
 iIi1 ( 'files' , 'viewType' )
 if 32 - 32: O0 . OoooooooOO
def iiIIiiIi ( ) :
 OoO0OOoO0Oo0 = '[COLOR green]ON[/COLOR]' if iiIiII1 == 'true' else '[COLOR red]OFF[/COLOR]'
 IIiIiiI1i = str ( oo0OOo ) if not oo0OOo == '' else 'Real Debrid hasnt been saved yet.'
 iiiii1II ( '[I]http://real-debrid.com is a PAID service.[/I]' , '' , icon = o00O0O , themeit = OOoO )
 iiiii1II ( 'Save Real Debrid Data: %s' % OoO0OOoO0Oo0 , 'togglesetting' , 'keepdebrid' , icon = o00O0O , themeit = OOoO )
 if iiIiII1 == 'true' : iiiii1II ( 'Last Save: %s' % str ( IIiIiiI1i ) , '' , icon = o00O0O , themeit = OOoO )
 if O0O0ooOOO == 'No' : iiiii1II ( wiz . sep ( ) , '' , icon = o00O0O , themeit = OOoO )
 if 42 - 42: iiIIi1IiIi11 + iIii1I11I1II1
 for II1IiiIII in debridit . ORDER :
  O0Oo0o000oO = iiIiIIIiiI [ II1IiiIII ] [ 'name' ]
  III11I1 = iiIiIIIiiI [ II1IiiIII ] [ 'path' ]
  OOOO0o0O = iiIiIIIiiI [ II1IiiIII ] [ 'saved' ]
  file = iiIiIIIiiI [ II1IiiIII ] [ 'file' ]
  iI111I = wiz . getS ( OOOO0o0O )
  O00OoOoO = debridit . debridUser ( II1IiiIII )
  Ii1ii111i1 = iiIiIIIiiI [ II1IiiIII ] [ 'icon' ] if os . path . exists ( III11I1 ) else o00O0O
  i1i1i1I = iiIiIIIiiI [ II1IiiIII ] [ 'fanart' ] if os . path . exists ( III11I1 ) else OOO00
  OoOo00o0OO = ii1IIIIiI11 ( 'saveaddon' , 'Debrid' , II1IiiIII )
  ooO0o0oo = ii1IIIIiI11 ( 'save' , 'Debrid' , II1IiiIII )
  OoOo00o0OO . append ( ( oooOo0OOOoo0 % '%s Settings' % O0Oo0o000oO , 'RunPlugin(plugin://%s/?mode=opensettings&name=%s&url=debrid)' % ( IiII1IiiIiI1 , II1IiiIII ) ) )
  if 41 - 41: II111iiii * OOoooooO
  iiiii1II ( '[+]-> %s' % O0Oo0o000oO , '' , icon = Ii1ii111i1 , fanart = i1i1i1I , themeit = OOoO )
  if not os . path . exists ( III11I1 ) : iiiii1II ( '[COLOR red]Addon Data: Not Installed[/COLOR]' , '' , icon = Ii1ii111i1 , fanart = i1i1i1I , menu = OoOo00o0OO )
  elif not O00OoOoO : iiiii1II ( '[COLOR red]Addon Data: Not Registered[/COLOR]' , 'authdebrid' , II1IiiIII , icon = Ii1ii111i1 , fanart = i1i1i1I , menu = OoOo00o0OO )
  else : iiiii1II ( '[COLOR green]Addon Data: %s[/COLOR]' % O00OoOoO , 'authdebrid' , II1IiiIII , icon = Ii1ii111i1 , fanart = i1i1i1I , menu = OoOo00o0OO )
  if iI111I == "" :
   if os . path . exists ( file ) : iiiii1II ( '[COLOR red]Saved Data: Save File Found(Import Data)[/COLOR]' , 'importdebrid' , II1IiiIII , icon = Ii1ii111i1 , fanart = i1i1i1I , menu = ooO0o0oo )
   else : iiiii1II ( '[COLOR red]Saved Data: Not Saved[/COLOR]' , 'savedebrid' , II1IiiIII , icon = Ii1ii111i1 , fanart = i1i1i1I , menu = ooO0o0oo )
  else : iiiii1II ( '[COLOR green]Saved Data: %s[/COLOR]' % iI111I , '' , icon = Ii1ii111i1 , fanart = i1i1i1I , menu = ooO0o0oo )
  if 68 - 68: IiiIII111ii - ooOo
 if O0O0ooOOO == 'No' : iiiii1II ( wiz . sep ( ) , '' , themeit = OOoO )
 iiiii1II ( 'Save All Real Debrid Data' , 'savedebrid' , 'all' , icon = o00O0O , themeit = OOoO )
 iiiii1II ( 'Recover All Saved Real Debrid Data' , 'restoredebrid' , 'all' , icon = o00O0O , themeit = OOoO )
 iiiii1II ( 'Import Real Debrid Data' , 'importdebrid' , 'all' , icon = o00O0O , themeit = OOoO )
 iiiii1II ( 'Clear All Saved Real Debrid Data' , 'cleardebrid' , 'all' , icon = o00O0O , themeit = OOoO )
 iiiii1II ( 'Clear All Addon Data' , 'addondebrid' , 'all' , icon = o00O0O , themeit = OOoO )
 iIi1 ( 'files' , 'viewType' )
 if 41 - 41: IIIi1i1I
def I11II1 ( ) :
 oO00O = '[COLOR green]ON[/COLOR]' if OOO00O0O == 'true' else '[COLOR red]OFF[/COLOR]'
 IIiIiiI1i = str ( ooOOO00Ooo ) if not ooOOO00Ooo == '' else 'Login data hasnt been saved yet.'
 iiiii1II ( '[I]Several of these addons are PAID services.[/I]' , '' , icon = ii1iii1i , themeit = OOoO )
 iiiii1II ( 'Save Login Data: %s' % oO00O , 'togglesetting' , 'keeplogin' , icon = ii1iii1i , themeit = OOoO )
 if OOO00O0O == 'true' : iiiii1II ( 'Last Save: %s' % str ( IIiIiiI1i ) , '' , icon = ii1iii1i , themeit = OOoO )
 if O0O0ooOOO == 'No' : iiiii1II ( wiz . sep ( ) , '' , icon = ii1iii1i , themeit = OOoO )
 if 46 - 46: o0o0Oo0oooo0
 for oO00O in loginit . ORDER :
  O0Oo0o000oO = iiI1IIIi [ oO00O ] [ 'name' ]
  III11I1 = iiI1IIIi [ oO00O ] [ 'path' ]
  OOOO0o0O = iiI1IIIi [ oO00O ] [ 'saved' ]
  file = iiI1IIIi [ oO00O ] [ 'file' ]
  iI111I = wiz . getS ( OOOO0o0O )
  O00OoOoO = loginit . loginUser ( oO00O )
  Ii1ii111i1 = iiI1IIIi [ oO00O ] [ 'icon' ] if os . path . exists ( III11I1 ) else ii1iii1i
  i1i1i1I = iiI1IIIi [ oO00O ] [ 'fanart' ] if os . path . exists ( III11I1 ) else OOO00
  OoOo00o0OO = ii1IIIIiI11 ( 'saveaddon' , 'Login' , oO00O )
  ooO0o0oo = ii1IIIIiI11 ( 'save' , 'Login' , oO00O )
  OoOo00o0OO . append ( ( oooOo0OOOoo0 % '%s Settings' % O0Oo0o000oO , 'RunPlugin(plugin://%s/?mode=opensettings&name=%s&url=login)' % ( IiII1IiiIiI1 , oO00O ) ) )
  if 83 - 83: i11iIiiIii * OO00O0O0O00Oo
  iiiii1II ( '[+]-> %s' % O0Oo0o000oO , '' , icon = Ii1ii111i1 , fanart = i1i1i1I , themeit = OOoO )
  if not os . path . exists ( III11I1 ) : iiiii1II ( '[COLOR red]Addon Data: Not Installed[/COLOR]' , '' , icon = Ii1ii111i1 , fanart = i1i1i1I , menu = OoOo00o0OO )
  elif not O00OoOoO : iiiii1II ( '[COLOR red]Addon Data: Not Registered[/COLOR]' , 'authlogin' , oO00O , icon = Ii1ii111i1 , fanart = i1i1i1I , menu = OoOo00o0OO )
  else : iiiii1II ( '[COLOR green]Addon Data: %s[/COLOR]' % O00OoOoO , 'authlogin' , oO00O , icon = Ii1ii111i1 , fanart = i1i1i1I , menu = OoOo00o0OO )
  if iI111I == "" :
   if os . path . exists ( file ) : iiiii1II ( '[COLOR red]Saved Data: Save File Found(Import Data)[/COLOR]' , 'importlogin' , oO00O , icon = Ii1ii111i1 , fanart = i1i1i1I , menu = ooO0o0oo )
   else : iiiii1II ( '[COLOR red]Saved Data: Not Saved[/COLOR]' , 'savelogin' , oO00O , icon = Ii1ii111i1 , fanart = i1i1i1I , menu = ooO0o0oo )
  else : iiiii1II ( '[COLOR green]Saved Data: %s[/COLOR]' % iI111I , '' , icon = Ii1ii111i1 , fanart = i1i1i1I , menu = ooO0o0oo )
  if 49 - 49: Ooo0O * IIIi1i1I + I1I1i1 - i11iIiiIii
 if O0O0ooOOO == 'No' : iiiii1II ( wiz . sep ( ) , '' , themeit = OOoO )
 iiiii1II ( 'Save All Login Data' , 'savelogin' , 'all' , icon = ii1iii1i , themeit = OOoO )
 iiiii1II ( 'Recover All Saved Login Data' , 'restorelogin' , 'all' , icon = ii1iii1i , themeit = OOoO )
 iiiii1II ( 'Import Login Data' , 'importlogin' , 'all' , icon = ii1iii1i , themeit = OOoO )
 iiiii1II ( 'Clear All Saved Login Data' , 'clearlogin' , 'all' , icon = ii1iii1i , themeit = OOoO )
 iiiii1II ( 'Clear All Addon Data' , 'addonlogin' , 'all' , icon = ii1iii1i , themeit = OOoO )
 iIi1 ( 'files' , 'viewType' )
 if 74 - 74: Ooo0O / iIii1I11I1II1 . II111iiii - I1111
def O0Oo0iIIIi1IiI11I1 ( ) :
 if o0OIiII < 17 :
  O0Ooo000 = os . path . join ( OOOO , wiz . latestDB ( 'Addons' ) )
  try :
   os . remove ( O0Ooo000 )
  except Exception , O00OO :
   wiz . log ( "Unable to remove %s, Purging DB" % O0Ooo000 )
   wiz . purgeDb ( O0Ooo000 )
 else :
  xbmc . log ( "Requested Addons.db be removed but doesnt work in Kod17" )
  if 36 - 36: Ooo0O % IiiIII111ii / i11iIiiIii % OO00O0O0O00Oo + I1111
def i1IiI ( ) :
 O0OoO0o = glob . glob ( os . path . join ( O0O , '*/' ) )
 IIIi = [ ] ; Oo0O = [ ]
 for I111IIiIII in sorted ( O0OoO0o , key = lambda II1IOoOo000oOo0oo : II1IOoOo000oOo0oo ) :
  OO0OOoo0OOO = os . path . split ( I111IIiIII [ : - 1 ] ) [ 1 ]
  if OO0OOoo0OOO in Iii1I1I11iiI1 : continue
  elif OO0OOoo0OOO in OOo0 : continue
  elif OO0OOoo0OOO == 'packages' : continue
  ooooOoo0OO = os . path . join ( I111IIiIII , 'addon.xml' )
  if os . path . exists ( ooooOoo0OO ) :
   IIi1i = open ( ooooOoo0OO )
   IiiIi11Ii1iI1 = IIi1i . read ( )
   o0O0Oo00 = wiz . parseDOM ( IiiIi11Ii1iI1 , 'addon' , ret = 'id' )
   if 87 - 87: oO0 + oO0 - oO0 % O0
   iIiI1 = OO0OOoo0OOO if len ( o0O0Oo00 ) == 0 else o0O0Oo00 [ 0 ]
   try :
    IiI1iiI1III1I = xbmcaddon . Addon ( id = iIiI1 )
    IIIi . append ( IiI1iiI1III1I . getAddonInfo ( 'name' ) )
    Oo0O . append ( iIiI1 )
   except :
    pass
 if len ( IIIi ) == 0 :
  wiz . LogNotify ( "[COLOR %s]%s[/COLOR]" % ( oOOo0O00o , o0OOO ) , "[COLOR %s]No Addons To Remove[/COLOR]" % iIiIi11 )
  return
 if o0OIiII > 16 :
  i1iIiIIi1II1ii = iiIIIII1i1iI . multiselect ( "%s: Select the addons you wish to remove." % o0OOO , IIIi )
 else :
  i1iIiIIi1II1ii = [ ] ; i1Ii11I1II = 0
  I1IiII1I1i1I1 = [ "-- Click here to Continue --" ] + IIIi
  while not i1Ii11I1II == - 1 :
   i1Ii11I1II = iiIIIII1i1iI . select ( "%s: Select the addons you wish to remove." % o0OOO , I1IiII1I1i1I1 )
   if i1Ii11I1II == - 1 : break
   elif i1Ii11I1II == 0 : break
   else :
    II11iiI = ( i1Ii11I1II - 1 )
    if II11iiI in i1iIiIIi1II1ii :
     i1iIiIIi1II1ii . remove ( II11iiI )
     I1IiII1I1i1I1 [ i1Ii11I1II ] = IIIi [ II11iiI ]
    else :
     i1iIiIIi1II1ii . append ( II11iiI )
     I1IiII1I1i1I1 [ i1Ii11I1II ] = "[B][COLOR %s]%s[/COLOR][/B]" % ( oOOo0O00o , IIIi [ II11iiI ] )
 if i1iIiIIi1II1ii == None : return
 if len ( i1iIiIIi1II1ii ) > 0 :
  wiz . addonUpdates ( 'set' )
  for iiIiOooooOo in i1iIiIIi1II1ii :
   IIIiiiIiI ( Oo0O [ iiIiOooooOo ] , IIIi [ iiIiOooooOo ] , True )
   if 80 - 80: IIIi1i1I % IIIi1i1I % O0 - i11iIiiIii . iiIIi1IiIi11 / O0
  xbmc . sleep ( 500 )
  if 13 - 13: ooOo + O0 - oO0 % Ooo0O / IiiIII111ii . i1IIi
  if I11i1I1I == 1 : OOOO00OoooO = 1
  elif I11i1I1I == 2 : OOOO00OoooO = 0
  else : OOOO00OoooO = iiIIIII1i1iI . yesno ( o0OOO , "[COLOR %s]Would you like to [COLOR %s]Force close[/COLOR] kodi or [COLOR %s]Reload Profile[/COLOR]?[/COLOR]" % ( iIiIi11 , oOOo0O00o , oOOo0O00o ) , yeslabel = "[B][COLOR green]Reload Profile[/COLOR][/B]" , nolabel = "[B][COLOR red]Force Close[/COLOR][/B]" )
  if OOOO00OoooO == 1 : wiz . reloadFix ( 'remove addon' )
  else : wiz . addonUpdates ( 'reset' ) ; wiz . killxbmc ( True )
  if 7 - 7: oO0 / II111iiii - i11IiIiiIIIII + i1IIi + IiiIII111ii
def i11i11i ( ) :
 if os . path . exists ( ooOOOo0oo0O0 ) :
  iiiii1II ( '[COLOR red][B][REMOVE][/B][/COLOR] All Addon_Data' , 'removedata' , 'all' , themeit = oooOo0OOOoo0 )
  iiiii1II ( '[COLOR red][B][REMOVE][/B][/COLOR] All Addon_Data for Uninstalled Addons' , 'removedata' , 'uninstalled' , themeit = oooOo0OOOoo0 )
  iiiii1II ( '[COLOR red][B][REMOVE][/B][/COLOR] All Empty Folders in Addon_Data' , 'removedata' , 'empty' , themeit = oooOo0OOOoo0 )
  iiiii1II ( '[COLOR red][B][REMOVE][/B][/COLOR] %s Addon_Data' % o0OOO , 'resetaddon' , themeit = oooOo0OOOoo0 )
  if O0O0ooOOO == 'No' : iiiii1II ( wiz . sep ( ) , '' , themeit = OOoO )
  O0OoO0o = glob . glob ( os . path . join ( ooOOOo0oo0O0 , '*/' ) )
  for I111IIiIII in sorted ( O0OoO0o , key = lambda II1IOoOo000oOo0oo : II1IOoOo000oOo0oo ) :
   OO0OOoo0OOO = I111IIiIII . replace ( ooOOOo0oo0O0 , '' ) . replace ( '\\' , '' ) . replace ( '/' , '' )
   Ii1ii111i1 = os . path . join ( I111IIiIII . replace ( ooOOOo0oo0O0 , O0O ) , 'icon.png' )
   i1i1i1I = os . path . join ( I111IIiIII . replace ( ooOOOo0oo0O0 , O0O ) , 'fanart.png' )
   iiI1iI = OO0OOoo0OOO
   Ooo00O0 = { 'audio.' : '[COLOR orange][AUDIO] [/COLOR]' , 'metadata.' : '[COLOR cyan][METADATA] [/COLOR]' , 'module.' : '[COLOR orange][MODULE] [/COLOR]' , 'plugin.' : '[COLOR blue][PLUGIN] [/COLOR]' , 'program.' : '[COLOR orange][PROGRAM] [/COLOR]' , 'repository.' : '[COLOR gold][REPO] [/COLOR]' , 'script.' : '[COLOR green][SCRIPT] [/COLOR]' , 'service.' : '[COLOR green][SERVICE] [/COLOR]' , 'skin.' : '[COLOR dodgerblue][SKIN] [/COLOR]' , 'video.' : '[COLOR orange][VIDEO] [/COLOR]' , 'weather.' : '[COLOR yellow][WEATHER] [/COLOR]' }
   for OoO0OOoO0 in Ooo00O0 :
    iiI1iI = iiI1iI . replace ( OoO0OOoO0 , Ooo00O0 [ OoO0OOoO0 ] )
   if OO0OOoo0OOO in Iii1I1I11iiI1 : iiI1iI = '[COLOR green][B][PROTECTED][/B][/COLOR] %s' % iiI1iI
   else : iiI1iI = '[COLOR red][B][REMOVE][/B][/COLOR] %s' % iiI1iI
   iiiii1II ( ' %s' % iiI1iI , 'removedata' , OO0OOoo0OOO , icon = Ii1ii111i1 , fanart = i1i1i1I , themeit = oooOo0OOOoo0 )
 else :
  iiiii1II ( 'No Addon data folder found.' , '' , themeit = OOoO )
 iIi1 ( 'files' , 'viewType' )
 if 5 - 5: i1IIi . i1IIi
def o0o0oo0Ooo ( ) :
 iiiii1II ( "[I][B][COLOR red]!!Notice: Disabling Some Addons Can Cause Issues!![/COLOR][/B][/I]" , '' , icon = IiIi11iI )
 O0OoO0o = glob . glob ( os . path . join ( O0O , '*/' ) )
 II1IOoOo000oOo0oo = 0
 for I111IIiIII in sorted ( O0OoO0o , key = lambda II1IOoOo000oOo0oo : II1IOoOo000oOo0oo ) :
  OO0OOoo0OOO = os . path . split ( I111IIiIII [ : - 1 ] ) [ 1 ]
  if OO0OOoo0OOO in Iii1I1I11iiI1 : continue
  if OO0OOoo0OOO in OOo0 : continue
  iI1i = os . path . join ( I111IIiIII , 'addon.xml' )
  if os . path . exists ( iI1i ) :
   II1IOoOo000oOo0oo += 1
   O0OoO0o = I111IIiIII . replace ( O0O , '' ) [ 1 : - 1 ]
   IIi1i = open ( iI1i )
   IiiIi11Ii1iI1 = IIi1i . read ( ) . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
   o0O0Oo00 = wiz . parseDOM ( IiiIi11Ii1iI1 , 'addon' , ret = 'id' )
   oOOiiiIIiIi = wiz . parseDOM ( IiiIi11Ii1iI1 , 'addon' , ret = 'name' )
   try :
    oo0oO = o0O0Oo00 [ 0 ]
    O0Oo0o000oO = oOOiiiIIiIi [ 0 ]
   except :
    continue
   try :
    IiI1iiI1III1I = xbmcaddon . Addon ( id = oo0oO )
    iI1IIIii = "[COLOR green][Enabled][/COLOR]"
    i11I = "false"
   except :
    iI1IIIii = "[COLOR red][Disabled][/COLOR]"
    i11I = "true"
    pass
   Ii1ii111i1 = os . path . join ( I111IIiIII , 'icon.png' ) if os . path . exists ( os . path . join ( I111IIiIII , 'icon.png' ) ) else iiiiiIIii
   i1i1i1I = os . path . join ( I111IIiIII , 'fanart.jpg' ) if os . path . exists ( os . path . join ( I111IIiIII , 'fanart.jpg' ) ) else OOO00
   iiiii1II ( "%s %s" % ( iI1IIIii , O0Oo0o000oO ) , 'toggleaddon' , O0OoO0o , i11I , icon = Ii1ii111i1 , fanart = i1i1i1I )
   IIi1i . close ( )
 if II1IOoOo000oOo0oo == 0 :
  iiiii1II ( "No Addons Found to Enable or Disable." , '' , icon = IiIi11iI )
 iIi1 ( 'files' , 'viewType' )
 if 56 - 56: iiIIi1IiIi11 . OO00O0O0O00Oo
def I1i1ii ( ) :
 oooo0O0o0OoOO = [ 'Every Startup' , 'Every Day' , 'Every Three Days' , 'Every Weekly' ]
 O0000oo00oOOO = iiIIIII1i1iI . select ( "[COLOR %s]How often would you list to Auto Clean on Startup?[/COLOR]" % iIiIi11 , oooo0O0o0OoOO )
 if not O0000oo00oOOO == - 1 :
  wiz . setS ( 'autocleanfeq' , str ( O0000oo00oOOO ) )
  wiz . LogNotify ( '[COLOR %s]Auto Clean Up[/COLOR]' % oOOo0O00o , '[COLOR %s]Fequency Now %s[/COLOR]' % ( iIiIi11 , oooo0O0o0OoOO [ O0000oo00oOOO ] ) )
  if 98 - 98: IIIi1i1I . OoooooooOO
def Oo000 ( ) :
 iiiii1II ( 'Convert Text Files to 0.1.7' , 'converttext' , themeit = OOOiiiiI )
 iiiii1II ( 'Create QR Code' , 'createqr' , themeit = OOOiiiiI )
 iiiii1II ( 'Test Notifications' , 'testnotify' , themeit = OOOiiiiI )
 iiiii1II ( 'Test Update' , 'testupdate' , themeit = OOOiiiiI )
 iiiii1II ( 'Test First Run' , 'testfirst' , themeit = OOOiiiiI )
 iiiii1II ( 'Test First Run Settings' , 'testfirstrun' , themeit = OOOiiiiI )
 iiiii1II ( 'Test APk' , 'testapk' , themeit = OOOiiiiI )
 if 97 - 97: O0 / iii11iiII + I1I1i1 . IIIi1i1I % o0o0Oo0oooo0 - o0o0Oo0oooo0
 iIi1 ( 'files' , 'viewType' )
 if 33 - 33: i11IiIiiIIIII % II111iiii + I1111
 if 93 - 93: i1IIi . i1Ii / ooOo + i1Ii
 if 58 - 58: oO0 + O0 . Ooo0O + o0o0Oo0oooo0 - I1111 - o0o0Oo0oooo0
 if 41 - 41: Ooo0O / i1IIi / Ooo0O - iiIIi1IiIi11 . I1I1i1
def Oooooooo00o00 ( name , type , theme = None , over = False ) :
 if over == False :
  O0oo00OOOO = wiz . checkBuild ( name , 'url' )
  if O0oo00OOOO == False :
   wiz . LogNotify ( "[COLOR %s]%s[/COLOR]" % ( oOOo0O00o , o0OOO ) , "[COLOR %s]Unabled to find build[/COLOR]" % iIiIi11 )
   return
  IiIi1II111I = wiz . workingURL ( O0oo00OOOO )
  if IiIi1II111I == False :
   wiz . LogNotify ( "[COLOR %s]%s[/COLOR]" % ( oOOo0O00o , o0OOO ) , "[COLOR %s]Build Zip Error: %s[/COLOR]" % ( iIiIi11 , IiIi1II111I ) )
   return
 if type == 'gui' :
  if name == O000oo0O :
   if over == True : o00oIIi1i1 = 1
   else : o00oIIi1i1 = iiIIIII1i1iI . yesno ( o0OOO , '[COLOR %s]Would you like to apply the guifix for:' % iIiIi11 , '[COLOR %s]%s[/COLOR]?[/COLOR]' % ( oOOo0O00o , name ) , nolabel = '[B][COLOR red]No, Cancel[/COLOR][/B]' , yeslabel = '[B][COLOR green]Apply Fix[/COLOR][/B]' )
  else :
   o00oIIi1i1 = iiIIIII1i1iI . yesno ( "%s - [COLOR red]WARNING!![/COLOR]" % o0OOO , "[COLOR %s][COLOR %s]%s[/COLOR] community build is not currently installed." % ( iIiIi11 , oOOo0O00o , name ) , "Would you like to apply the guiFix anyways?.[/COLOR]" , nolabel = '[B][COLOR red]No, Cancel[/COLOR][/B]' , yeslabel = '[B][COLOR green]Apply Fix[/COLOR][/B]' )
  if o00oIIi1i1 :
   o0O0Ooo = wiz . checkBuild ( name , 'gui' )
   O0oO00oOOooO = name . replace ( '\\' , '' ) . replace ( '/' , '' ) . replace ( ':' , '' ) . replace ( '*' , '' ) . replace ( '?' , '' ) . replace ( '"' , '' ) . replace ( '<' , '' ) . replace ( '>' , '' ) . replace ( '|' , '' )
   if not wiz . workingURL ( o0O0Ooo ) == True : wiz . LogNotify ( "[COLOR %s]%s[/COLOR]" % ( oOOo0O00o , o0OOO ) , '[COLOR %s]GuiFix: Invalid Zip Url![/COLOR]' % iIiIi11 ) ; return
   if not os . path . exists ( o0o0OOO0o0 ) : os . makedirs ( o0o0OOO0o0 )
   oo00 . create ( o0OOO , '[COLOR %s][B]Downloading GuiFix:[/B][/COLOR] [COLOR %s]%s[/COLOR]' % ( iIiIi11 , oOOo0O00o , name ) , '' , 'Please Wait' )
   Oo0 = os . path . join ( o0o0OOO0o0 , '%s_guisettings.zip' % O0oO00oOOooO )
   try : os . remove ( Oo0 )
   except : pass
   downloader . download ( o0O0Ooo , Oo0 , oo00 )
   xbmc . sleep ( 500 )
   OOoOoO00O0O0o = '[COLOR %s][B]Installing:[/B][/COLOR] [COLOR %s]%s[/COLOR]' % ( iIiIi11 , oOOo0O00o , name )
   oo00 . update ( 0 , OOoOoO00O0O0o , '' , 'Please Wait' )
   extract . all ( Oo0 , oOo00Oo00O , oo00 , title = OOoOoO00O0O0o )
   oo00 . close ( )
   wiz . defaultSkin ( )
   wiz . lookandFeelData ( 'save' )
   if I11i1I1I == 1 : OOOO00OoooO = 1
   elif I11i1I1I == 2 : OOOO00OoooO = 0
   else : OOOO00OoooO = iiIIIII1i1iI . yesno ( o0OOO , "[COLOR %s]The Gui fix has been installed.  Would you like to Reload the profile or Force Close Kodi?[/COLOR]" % iIiIi11 , yeslabel = "[B][COLOR red]Reload Profile[/COLOR][/B]" , nolabel = "[B][COLOR green]Force Close[/COLOR][/B]" )
   if OOOO00OoooO == 1 : wiz . reloadFix ( )
   else : iiIIIII1i1iI . ok ( o0OOO , "[COLOR %s]To save changes you now need to force close Kodi, Press OK to force close Kodi[/COLOR]" % iIiIi11 ) ; wiz . killxbmc ( 'true' )
  else :
   wiz . LogNotify ( "[COLOR %s]%s[/COLOR]" % ( oOOo0O00o , o0OOO ) , '[COLOR %s]GuiFix: Cancelled![/COLOR]' % iIiIi11 )
 elif type == 'fresh' :
  IiI ( name )
 elif type == 'normal' :
  if oO0o00oOOooO0 == 'normal' :
   if o0O0OOO0Ooo == 'true' :
    traktit . autoUpdate ( 'all' )
    wiz . setS ( 'traktlastsave' , str ( I1IiiiiI ) )
   if iiIiII1 == 'true' :
    debridit . autoUpdate ( 'all' )
    wiz . setS ( 'debridlastsave' , str ( I1IiiiiI ) )
   if OOO00O0O == 'true' :
    loginit . autoUpdate ( 'all' )
    wiz . setS ( 'loginlastsave' , str ( I1IiiiiI ) )
  Iii1iiI = int ( o0OIiII ) ; ii1IiiII = int ( float ( wiz . checkBuild ( name , 'kodi' ) ) )
  if not Iii1iiI == ii1IiiII :
   if Iii1iiI == 16 and ii1IiiII <= 15 : oO0o0O0Ooo0o = False
   else : oO0o0O0Ooo0o = True
  else : oO0o0O0Ooo0o = False
  if oO0o0O0Ooo0o == True :
   IiiI1II1II1i = iiIIIII1i1iI . yesno ( "%s - [COLOR red]WARNING!![/COLOR]" % o0OOO , '[COLOR %s]There is a chance that the skin will not appear correctly' % iIiIi11 , 'When installing a %s build on a Kodi %s install' % ( wiz . checkBuild ( name , 'kodi' ) , o0OIiII ) , 'Would you still like to install: [COLOR %s]%s v%s[/COLOR]?[/COLOR]' % ( oOOo0O00o , name , wiz . checkBuild ( name , 'version' ) ) , nolabel = '[B][COLOR red]No, Cancel[/COLOR][/B]' , yeslabel = '[B][COLOR green]Yes, Install[/COLOR][/B]' )
  else :
   if not over == False : IiiI1II1II1i = 1
   else : IiiI1II1II1i = iiIIIII1i1iI . yesno ( o0OOO , '[COLOR %s]Would you like to Download and Install:' % iIiIi11 , '[COLOR %s]%s v%s[/COLOR]?[/COLOR]' % ( oOOo0O00o , name , wiz . checkBuild ( name , 'version' ) ) , nolabel = '[B][COLOR red]No, Cancel[/COLOR][/B]' , yeslabel = '[B][COLOR green]Yes, Install[/COLOR][/B]' )
  if IiiI1II1II1i :
   wiz . clearS ( 'build' )
   o0O0Ooo = wiz . checkBuild ( name , 'url' )
   O0oO00oOOooO = name . replace ( '\\' , '' ) . replace ( '/' , '' ) . replace ( ':' , '' ) . replace ( '*' , '' ) . replace ( '?' , '' ) . replace ( '"' , '' ) . replace ( '<' , '' ) . replace ( '>' , '' ) . replace ( '|' , '' )
   if not wiz . workingURL ( o0O0Ooo ) == True : wiz . LogNotify ( "[COLOR %s]%s[/COLOR]" % ( oOOo0O00o , o0OOO ) , '[COLOR %s]Build Install: Invalid Zip Url![/COLOR]' % iIiIi11 ) ; return
   if not os . path . exists ( o0o0OOO0o0 ) : os . makedirs ( o0o0OOO0o0 )
   oo00 . create ( o0OOO , '[COLOR %s][B]Downloading:[/B][/COLOR] [COLOR %s]%s v%s[/COLOR]' % ( iIiIi11 , oOOo0O00o , name , wiz . checkBuild ( name , 'version' ) ) , '' , 'Please Wait' )
   Oo0 = os . path . join ( o0o0OOO0o0 , '%s.zip' % O0oO00oOOooO )
   try : os . remove ( Oo0 )
   except : pass
   downloader . download ( o0O0Ooo , Oo0 , oo00 )
   xbmc . sleep ( 500 )
   OOoOoO00O0O0o = '[COLOR %s][B]Installing:[/B][/COLOR] [COLOR %s]%s v%s[/COLOR]' % ( iIiIi11 , oOOo0O00o , name , wiz . checkBuild ( name , 'version' ) )
   oo00 . update ( 0 , OOoOoO00O0O0o , '' , 'Please Wait' )
   oOII1ii1ii11I1 , o0ooOO0o , ooo0 = extract . all ( Oo0 , o00 , oo00 , title = OOoOoO00O0O0o )
   if int ( float ( oOII1ii1ii11I1 ) ) > 0 :
    wiz . fixmetas ( )
    wiz . lookandFeelData ( 'save' )
    wiz . defaultSkin ( )
    if 1 - 1: O0
    wiz . setS ( 'buildname' , name )
    wiz . setS ( 'buildversion' , wiz . checkBuild ( name , 'version' ) )
    wiz . setS ( 'buildtheme' , '' )
    wiz . setS ( 'latestversion' , wiz . checkBuild ( name , 'version' ) )
    wiz . setS ( 'lastbuildcheck' , str ( OOI1iI1ii1II ) )
    wiz . setS ( 'installed' , 'true' )
    wiz . setS ( 'extract' , str ( oOII1ii1ii11I1 ) )
    wiz . setS ( 'errors' , str ( o0ooOO0o ) )
    wiz . log ( 'INSTALLED %s: [ERRORS:%s]' % ( oOII1ii1ii11I1 , o0ooOO0o ) )
    try : os . remove ( Oo0 )
    except : pass
    if int ( float ( o0ooOO0o ) ) > 0 :
     o00oIIi1i1 = iiIIIII1i1iI . yesno ( o0OOO , '[COLOR %s][COLOR %s]%s v%s[/COLOR]' % ( iIiIi11 , oOOo0O00o , name , wiz . checkBuild ( name , 'version' ) ) , 'Completed: [COLOR %s]%s%s[/COLOR] [Errors:[COLOR %s]%s[/COLOR]]' % ( oOOo0O00o , oOII1ii1ii11I1 , '%' , oOOo0O00o , o0ooOO0o ) , 'Would you like to view the errors?[/COLOR]' , nolabel = '[B][COLOR red]No Thanks[/COLOR][/B]' , yeslabel = '[B][COLOR green]View Errors[/COLOR][/B]' )
     if o00oIIi1i1 :
      if isinstance ( o0ooOO0o , unicode ) :
       ooo0 = ooo0 . encode ( 'utf-8' )
      wiz . TextBox ( o0OOO , ooo0 )
    oo00 . close ( )
    OOo00OoO = wiz . themeCount ( name )
    if not OOo00OoO == False :
     Oooooooo00o00 ( name , 'theme' )
    if o0OIiII >= 17 : wiz . addonDatabase ( IiII1IiiIiI1 , 1 )
    if I11i1I1I == 1 : OOOO00OoooO = 1
    elif I11i1I1I == 2 : OOOO00OoooO = 0
    else : OOOO00OoooO = iiIIIII1i1iI . yesno ( o0OOO , "[COLOR %s]Would you like to [COLOR %s]Force close[/COLOR] kodi or [COLOR %s]Reload Profile[/COLOR]?[/COLOR]" % ( iIiIi11 , oOOo0O00o , oOOo0O00o ) , yeslabel = "[B][COLOR red]Reload Profile[/COLOR][/B]" , nolabel = "[B][COLOR green]Force Close[/COLOR][/B]" )
    if OOOO00OoooO == 1 : wiz . reloadFix ( )
    else : wiz . killxbmc ( True )
   else :
    if isinstance ( o0ooOO0o , unicode ) :
     ooo0 = ooo0 . encode ( 'utf-8' )
    wiz . TextBox ( "%s: Error Installing Build" % o0OOO , ooo0 )
  else :
   wiz . LogNotify ( "[COLOR %s]%s[/COLOR]" % ( oOOo0O00o , o0OOO ) , '[COLOR %s]Build Install: Cancelled![/COLOR]' % iIiIi11 )
 elif type == 'theme' :
  if theme == None :
   OOo00OoO = wiz . checkBuild ( name , 'theme' )
   I11II1i1 = [ ]
   if not OOo00OoO == 'http://' and wiz . workingURL ( OOo00OoO ) == True :
    I11II1i1 = wiz . themeCount ( name , False )
    if len ( I11II1i1 ) > 0 :
     if iiIIIII1i1iI . yesno ( o0OOO , "[COLOR %s]The Build [COLOR %s]%s[/COLOR] comes with [COLOR %s]%s[/COLOR] different themes" % ( iIiIi11 , oOOo0O00o , name , oOOo0O00o , len ( I11II1i1 ) ) , "Would you like to install one now?[/COLOR]" , yeslabel = "[B][COLOR green]Install Theme[/COLOR][/B]" , nolabel = "[B][COLOR red]Cancel Themes[/COLOR][/B]" ) :
      wiz . log ( "Theme List: %s " % str ( I11II1i1 ) )
      IiI1ii11I1 = iiIIIII1i1iI . select ( o0OOO , I11II1i1 )
      wiz . log ( "Theme install selected: %s" % IiI1ii11I1 )
      if not IiI1ii11I1 == - 1 : theme = I11II1i1 [ IiI1ii11I1 ] ; I1i1iI = True
      else : wiz . LogNotify ( "[COLOR %s]%s[/COLOR]" % ( oOOo0O00o , o0OOO ) , '[COLOR %s]Theme Install: Cancelled![/COLOR]' % iIiIi11 ) ; return
     else : wiz . LogNotify ( "[COLOR %s]%s[/COLOR]" % ( oOOo0O00o , o0OOO ) , '[COLOR %s]Theme Install: Cancelled![/COLOR]' % iIiIi11 ) ; return
   else : wiz . LogNotify ( "[COLOR %s]%s[/COLOR]" % ( oOOo0O00o , o0OOO ) , '[COLOR %s]Theme Install: None Found![/COLOR]' % iIiIi11 )
  else : I1i1iI = iiIIIII1i1iI . yesno ( o0OOO , '[COLOR %s]Would you like to install the theme:' % iIiIi11 , '[COLOR %s]%s[/COLOR]' % ( oOOo0O00o , theme ) , 'for [COLOR %s]%s v%s[/COLOR]?[/COLOR]' % ( oOOo0O00o , name , wiz . checkBuild ( name , 'version' ) ) , yeslabel = "[B][COLOR green]Install Theme[/COLOR][/B]" , nolabel = "[B][COLOR red]Cancel Themes[/COLOR][/B]" )
  if I1i1iI :
   I1iI1I1ii1 = wiz . checkTheme ( name , theme , 'url' )
   O0oO00oOOooO = name . replace ( '\\' , '' ) . replace ( '/' , '' ) . replace ( ':' , '' ) . replace ( '*' , '' ) . replace ( '?' , '' ) . replace ( '"' , '' ) . replace ( '<' , '' ) . replace ( '>' , '' ) . replace ( '|' , '' )
   if not wiz . workingURL ( I1iI1I1ii1 ) == True : wiz . LogNotify ( "[COLOR %s]%s[/COLOR]" % ( oOOo0O00o , o0OOO ) , '[COLOR %s]Theme Install: Invalid Zip Url![/COLOR]' % iIiIi11 ) ; return False
   if not os . path . exists ( o0o0OOO0o0 ) : os . makedirs ( o0o0OOO0o0 )
   oo00 . create ( o0OOO , '[COLOR %s][B]Downloading:[/B][/COLOR] [COLOR %s]%s[/COLOR]' % ( iIiIi11 , oOOo0O00o , theme ) , '' , 'Please Wait' )
   Oo0 = os . path . join ( o0o0OOO0o0 , '%s.zip' % O0oO00oOOooO )
   try : os . remove ( Oo0 )
   except : pass
   downloader . download ( I1iI1I1ii1 , Oo0 , oo00 )
   xbmc . sleep ( 500 )
   oo00 . update ( 0 , "" , "Installing %s " % name )
   iIIi1 = False
   if oO0o00oOOooO0 not in [ "fresh" , "normal" ] :
    iIIi1 = o0Ooo0o0Oo ( Oo0 ) if not wiz . currSkin ( ) in [ 'skin.confluence' , 'skin.estuary' ] else False
    oo00ooooOOo00 = ii1i ( Oo0 ) if not wiz . currSkin ( ) in [ 'skin.confluence' , 'skin.estuary' ] else False
    if iIIi1 == True :
     wiz . lookandFeelData ( 'save' )
     OO00Oooo000 = 'skin.confluence' if o0OIiII < 17 else 'skin.estuary'
     iI1ii111iiIii = xbmc . getSkinDir ( )
     if 57 - 57: I1I1i1 / OO00O0O0O00Oo
     skinSwitch . swapSkins ( OO00Oooo000 )
     II1IOoOo000oOo0oo = 0
     xbmc . sleep ( 1000 )
     while not xbmc . getCondVisibility ( "Window.isVisible(yesnodialog)" ) and II1IOoOo000oOo0oo < 150 :
      II1IOoOo000oOo0oo += 1
      xbmc . sleep ( 200 )
     if xbmc . getCondVisibility ( "Window.isVisible(yesnodialog)" ) :
      wiz . ebi ( 'SendClick(11)' )
     else : wiz . LogNotify ( "[COLOR %s]%s[/COLOR]" % ( oOOo0O00o , o0OOO ) , '[COLOR %s]Theme Install: Skin Swap Timed Out![/COLOR]' % iIiIi11 ) ; return
     xbmc . sleep ( 500 )
   OOoOoO00O0O0o = '[COLOR %s][B]Installing Theme:[/B][/COLOR] [COLOR %s]%s[/COLOR]' % ( iIiIi11 , oOOo0O00o , theme )
   oo00 . update ( 0 , OOoOoO00O0O0o , '' , 'Please Wait' )
   oOII1ii1ii11I1 , o0ooOO0o , ooo0 = extract . all ( Oo0 , o00 , oo00 , title = OOoOoO00O0O0o )
   wiz . setS ( 'buildtheme' , theme )
   wiz . log ( 'INSTALLED %s: [ERRORS:%s]' % ( oOII1ii1ii11I1 , o0ooOO0o ) )
   oo00 . close ( )
   if oO0o00oOOooO0 not in [ "fresh" , "normal" ] :
    wiz . forceUpdate ( )
    if o0OIiII >= 17 : wiz . kodi17Fix ( )
    if oo00ooooOOo00 == True :
     wiz . lookandFeelData ( 'save' )
     wiz . defaultSkin ( )
     iI1ii111iiIii = wiz . getS ( 'defaultskin' )
     skinSwitch . swapSkins ( iI1ii111iiIii )
     II1IOoOo000oOo0oo = 0
     xbmc . sleep ( 1000 )
     while not xbmc . getCondVisibility ( "Window.isVisible(yesnodialog)" ) and II1IOoOo000oOo0oo < 150 :
      II1IOoOo000oOo0oo += 1
      xbmc . sleep ( 200 )
      if 13 - 13: OoooooooOO + I1111
     if xbmc . getCondVisibility ( "Window.isVisible(yesnodialog)" ) :
      wiz . ebi ( 'SendClick(11)' )
     wiz . lookandFeelData ( 'restore' )
    elif iIIi1 == True :
     skinSwitch . swapSkins ( iI1ii111iiIii )
     II1IOoOo000oOo0oo = 0
     xbmc . sleep ( 1000 )
     while not xbmc . getCondVisibility ( "Window.isVisible(yesnodialog)" ) and II1IOoOo000oOo0oo < 150 :
      II1IOoOo000oOo0oo += 1
      xbmc . sleep ( 200 )
      if 32 - 32: O0 + IIIi1i1I % Ooo0O
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
   if 7 - 7: oO0 / OOoooooO
def I1i1I11111iI1 ( name , url ) :
 if not wiz . workingURL ( url ) :
  LogNotify ( "[COLOR %s]%s[/COLOR]" % ( oOOo0O00o , o0OOO ) , '[COLOR %s]Invalid URL for Build[/COLOR]' % iIiIi11 ) ; return
 type = iiIIIII1i1iI . yesno ( o0OOO , "[COLOR %s]Would you like to preform a [COLOR %s]Fresh Install[/COLOR] or [COLOR %s]Normal Install[/COLOR] for:[/COLOR]" % ( iIiIi11 , oOOo0O00o , oOOo0O00o ) , "[COLOR %s]%s[/COLOR]" % ( oOOo0O00o , name ) , yeslabel = "[B][COLOR green]Fresh Install[/COLOR][/B]" , nolabel = "[B][COLOR red]Normal Install[/COLOR][/B]" )
 if type == 1 :
  IiI ( 'third' , True )
 wiz . clearS ( 'build' )
 O0oO00oOOooO = name . replace ( '\\' , '' ) . replace ( '/' , '' ) . replace ( ':' , '' ) . replace ( '*' , '' ) . replace ( '?' , '' ) . replace ( '"' , '' ) . replace ( '<' , '' ) . replace ( '>' , '' ) . replace ( '|' , '' )
 if not os . path . exists ( o0o0OOO0o0 ) : os . makedirs ( o0o0OOO0o0 )
 oo00 . create ( o0OOO , '[COLOR %s][B]Downloading:[/B][/COLOR] [COLOR %s]%s[/COLOR]' % ( iIiIi11 , oOOo0O00o , name ) , '' , 'Please Wait' )
 Oo0 = os . path . join ( o0o0OOO0o0 , '%s.zip' % O0oO00oOOooO )
 try : os . remove ( Oo0 )
 except : pass
 downloader . download ( url , Oo0 , oo00 )
 xbmc . sleep ( 500 )
 OOoOoO00O0O0o = '[COLOR %s][B]Installing:[/B][/COLOR] [COLOR %s]%s[/COLOR]' % ( iIiIi11 , oOOo0O00o , name )
 oo00 . update ( 0 , OOoOoO00O0O0o , '' , 'Please Wait' )
 oOII1ii1ii11I1 , o0ooOO0o , ooo0 = extract . all ( Oo0 , o00 , oo00 , title = OOoOoO00O0O0o )
 if int ( float ( oOII1ii1ii11I1 ) ) > 0 :
  wiz . fixmetas ( )
  wiz . lookandFeelData ( 'save' )
  wiz . defaultSkin ( )
  if 32 - 32: ooOo + oO0 - IIIi1i1I + oO0 / i1IIi * IIIi1i1I
  wiz . setS ( 'installed' , 'true' )
  wiz . setS ( 'extract' , str ( oOII1ii1ii11I1 ) )
  wiz . setS ( 'errors' , str ( o0ooOO0o ) )
  wiz . log ( 'INSTALLED %s: [ERRORS:%s]' % ( oOII1ii1ii11I1 , o0ooOO0o ) )
  try : os . remove ( Oo0 )
  except : pass
  if int ( float ( o0ooOO0o ) ) > 0 :
   o00oIIi1i1 = iiIIIII1i1iI . yesno ( o0OOO , '[COLOR %s][COLOR %s]%s[/COLOR]' % ( iIiIi11 , oOOo0O00o , name ) , 'Completed: [COLOR %s]%s%s[/COLOR] [Errors:[COLOR %s]%s[/COLOR]]' % ( oOOo0O00o , oOII1ii1ii11I1 , '%' , oOOo0O00o , o0ooOO0o ) , 'Would you like to view the errors?[/COLOR]' , nolabel = '[B][COLOR red]No Thanks[/COLOR][/B]' , yeslabel = '[B][COLOR green]View Errors[/COLOR][/B]' )
   if o00oIIi1i1 :
    if isinstance ( o0ooOO0o , unicode ) :
     ooo0 = ooo0 . encode ( 'utf-8' )
    wiz . TextBox ( o0OOO , ooo0 )
 oo00 . close ( )
 if o0OIiII >= 17 : wiz . addonDatabase ( IiII1IiiIiI1 , 1 )
 if I11i1I1I == 1 : OOOO00OoooO = 1
 elif I11i1I1I == 2 : OOOO00OoooO = 0
 else : OOOO00OoooO = iiIIIII1i1iI . yesno ( o0OOO , "[COLOR %s]Would you like to [COLOR %s]Force close[/COLOR] kodi or [COLOR %s]Reload Profile[/COLOR]?[/COLOR]" % ( iIiIi11 , oOOo0O00o , oOOo0O00o ) , yeslabel = "[B][COLOR green]Reload Profile[/COLOR][/B]" , nolabel = "[B][COLOR red]Force Close[/COLOR][/B]" )
 if OOOO00OoooO == 1 : wiz . reloadFix ( )
 else : wiz . killxbmc ( True )
 if 90 - 90: IiiIII111ii % IIIi1i1I
def o0Ooo0o0Oo ( path ) :
 iiii1 = zipfile . ZipFile ( path )
 for oOOo000oOoO0 in iiii1 . infolist ( ) :
  if '/settings.xml' in oOOo000oOoO0 . filename :
   return True
 return False
 if 60 - 60: ooOo % IIIi1i1I / I1I1i1 % IIIi1i1I * i11iIiiIii / iiIIi1IiIi11
def ii1i ( path ) :
 iiii1 = zipfile . ZipFile ( path )
 for oOOo000oOoO0 in iiii1 . infolist ( ) :
  if '/guisettings.xml' in oOOo000oOoO0 . filename :
   return True
 return False
 if 34 - 34: OO00O0O0O00Oo - iii11iiII
def o00o ( apk , url , Brackets ) :
 wiz . log ( apk )
 wiz . log ( url )
 if wiz . platform ( ) == 'android' :
  o00oIIi1i1 = iiIIIII1i1iI . yesno ( o0OOO , "[COLOR %s]Would you like to download and install:" % iIiIi11 , "[COLOR %s]%s[/COLOR]" % ( oOOo0O00o , apk ) , yeslabel = "[B][COLOR green]Download[/COLOR][/B]" , nolabel = "[B][COLOR red]Cancel[/COLOR][/B]" )
  if not o00oIIi1i1 : wiz . LogNotify ( "[COLOR %s]%s[/COLOR]" % ( oOOo0O00o , o0OOO ) , '[COLOR %s]ERROR: Install Cancelled[/COLOR]' % iIiIi11 ) ; return
  IIIiIi1iiI = apk
  if not os . path . exists ( o0o0OOO0o0 ) : os . makedirs ( o0o0OOO0o0 )
  if not wiz . workingURL ( url ) == True : wiz . LogNotify ( "[COLOR %s]%s[/COLOR]" % ( oOOo0O00o , o0OOO ) , '[COLOR %s]APK Installer: Invalid Apk Url![/COLOR]' % iIiIi11 ) ; return
  oo00 . create ( o0OOO , '[COLOR %s][B]Downloading:[/B][/COLOR] [COLOR %s]%s[/COLOR]' % ( iIiIi11 , oOOo0O00o , IIIiIi1iiI ) , '' , 'Please Wait' )
  Oo0 = os . path . join ( o0o0OOO0o0 , "%s.apk" % apk . replace ( '\\' , '' ) . replace ( '/' , '' ) . replace ( ':' , '' ) . replace ( '*' , '' ) . replace ( '?' , '' ) . replace ( '"' , '' ) . replace ( '<' , '' ) . replace ( '>' , '' ) . replace ( '|' , '' ) )
  try : os . remove ( Oo0 )
  except : pass
  downloader . download ( url , Oo0 , oo00 )
  xbmc . sleep ( 100 )
  oo00 . close ( )
  if "Brackets" in Brackets :
   iI1o0 = zipfile . ZipFile ( Oo0 )
   for file in iI1o0 . namelist ( ) :
    if file . endswith ( '.apk' ) :
     with open ( os . path . join ( o0o0OOO0o0 , os . path . basename ( file ) ) , 'wb' ) as IIi1i :
      Iiii = file . split ( '/' ) [ 1 ]
      IIi1i . write ( iI1o0 . read ( file ) )
      xbmc . sleep ( 500 )
      IIi1i . close ( )
      try :
       os . remove ( Oo0 )
      except :
       pass
      Oo0 = os . path . join ( o0o0OOO0o0 , Iiii )
  iiIIIII1i1iI . ok ( o0OOO , "Launching the APK to be installed" , "Follow the install process to complete." )
  notify . apkInstaller ( apk )
  wiz . ebi ( 'StartAndroidActivity("","android.intent.action.VIEW","application/vnd.android.package-archive","file:' + Oo0 + '")' )
 else : wiz . LogNotify ( "[COLOR %s]%s[/COLOR]" % ( oOOo0O00o , o0OOO ) , '[COLOR %s]ERROR: None Android Device[/COLOR]' % iIiIi11 )
 if 45 - 45: IiiIII111ii / OOoooooO . OoooooooOO + I1111
 if 51 - 51: iiIIi1IiIi11 % i11iIiiIii % i1Ii + OO00O0O0O00Oo % oO0
 if 16 - 16: o0o0Oo0oooo0 / Ooo0O + O0 - o0o0Oo0oooo0 . OoooooooOO
 if 19 - 19: I1I1i1
def o00OOOOOo0OOo ( name , url , ) :
 if "NULL" in url :
  iiIIIII1i1iI . ok ( o0OOO , "[COLOR ghostwhite]Not a valid selection, please try again.[/COLOR]" )
  sys . exit ( 1 )
  if 44 - 44: i11IiIiiIIIII * I1I1i1
 I1IiI = xbmcgui . DialogProgress ( )
 I1IiI . create ( o0OOO , "" , "" , 'ROM: ' + name )
 O0oO00oOOooO = name . replace ( '\\' , '' ) . replace ( '/' , '' ) . replace ( ':' , '' ) . replace ( '*' , '' ) . replace ( '?' , '' ) . replace ( '"' , '' ) . replace ( '<' , '' ) . replace ( '>' , '' ) . replace ( '|' , '' )
 Oo0 = os . path . join ( o0o0OOO0o0 , '%s.zip' % O0oO00oOOooO )
 downloader . download ( url , Oo0 , I1IiI )
 I1IiI . update ( 0 )
 extract . all ( Oo0 , iI , I1IiI )
 iiIIIII1i1iI . ok ( o0OOO , "[COLOR yellow]Download complete, ROM Location: [/COLOR][COLOR white]" + iI + "[/COLOR]" )
 if 49 - 49: iii11iiII % i11IiIiiIIIII * i11iIiiIii / IIIi1i1I % iii11iiII
 if 70 - 70: o0o0Oo0oooo0 / II111iiii % OOoooooO - iiIIi1IiIi11
 if 2 - 2: OO00O0O0O00Oo - oO0 + I1I1i1 * I1111 / iiIIi1IiIi11
 if 26 - 26: iii11iiII * Ooo0O
 if 31 - 31: i11IiIiiIIIII * IIIi1i1I . IiiIII111ii
def i1Ii11ii1I ( part , whole ) :
 return 100 * float ( part ) / float ( whole )
 if 66 - 66: Ooo0O / OoooooooOO % OO00O0O0O00Oo / iiIIi1IiIi11 + OoooooooOO
def ii1IIIIiI11 ( type , add , name ) :
 if type == 'saveaddon' :
  ii1III1iiIi = [ ]
  I1ii1iI = urllib . quote_plus ( add . lower ( ) . replace ( ' ' , '' ) )
  ooO000OO = add . replace ( 'Debrid' , 'Real Debrid' )
  oOIi111 = urllib . quote_plus ( name . lower ( ) . replace ( ' ' , '' ) )
  name = name . replace ( 'url' , 'URL Resolver' )
  ii1III1iiIi . append ( ( oooOo0OOOoo0 % name . title ( ) , ' ' ) )
  ii1III1iiIi . append ( ( OOoO % 'Save %s Data' % ooO000OO , 'RunPlugin(plugin://%s/?mode=save%s&name=%s)' % ( IiII1IiiIiI1 , I1ii1iI , oOIi111 ) ) )
  ii1III1iiIi . append ( ( OOoO % 'Restore %s Data' % ooO000OO , 'RunPlugin(plugin://%s/?mode=restore%s&name=%s)' % ( IiII1IiiIiI1 , I1ii1iI , oOIi111 ) ) )
  ii1III1iiIi . append ( ( OOoO % 'Clear %s Data' % ooO000OO , 'RunPlugin(plugin://%s/?mode=clear%s&name=%s)' % ( IiII1IiiIiI1 , I1ii1iI , oOIi111 ) ) )
 elif type == 'save' :
  ii1III1iiIi = [ ]
  I1ii1iI = urllib . quote_plus ( add . lower ( ) . replace ( ' ' , '' ) )
  ooO000OO = add . replace ( 'Debrid' , 'Real Debrid' )
  oOIi111 = urllib . quote_plus ( name . lower ( ) . replace ( ' ' , '' ) )
  name = name . replace ( 'url' , 'URL Resolver' )
  ii1III1iiIi . append ( ( oooOo0OOOoo0 % name . title ( ) , ' ' ) )
  ii1III1iiIi . append ( ( OOoO % 'Register %s' % ooO000OO , 'RunPlugin(plugin://%s/?mode=auth%s&name=%s)' % ( IiII1IiiIiI1 , I1ii1iI , oOIi111 ) ) )
  ii1III1iiIi . append ( ( OOoO % 'Save %s Data' % ooO000OO , 'RunPlugin(plugin://%s/?mode=save%s&name=%s)' % ( IiII1IiiIiI1 , I1ii1iI , oOIi111 ) ) )
  ii1III1iiIi . append ( ( OOoO % 'Restore %s Data' % ooO000OO , 'RunPlugin(plugin://%s/?mode=restore%s&name=%s)' % ( IiII1IiiIiI1 , I1ii1iI , oOIi111 ) ) )
  ii1III1iiIi . append ( ( OOoO % 'Import %s Data' % ooO000OO , 'RunPlugin(plugin://%s/?mode=import%s&name=%s)' % ( IiII1IiiIiI1 , I1ii1iI , oOIi111 ) ) )
  ii1III1iiIi . append ( ( OOoO % 'Clear Addon %s Data' % ooO000OO , 'RunPlugin(plugin://%s/?mode=addon%s&name=%s)' % ( IiII1IiiIiI1 , I1ii1iI , oOIi111 ) ) )
 elif type == 'install' :
  ii1III1iiIi = [ ]
  oOIi111 = urllib . quote_plus ( name )
  ii1III1iiIi . append ( ( oooOo0OOOoo0 % name , 'RunAddon(%s, ?mode=viewbuild&name=%s)' % ( IiII1IiiIiI1 , oOIi111 ) ) )
  ii1III1iiIi . append ( ( OOoO % 'Fresh Install' , 'RunPlugin(plugin://%s/?mode=install&name=%s&url=fresh)' % ( IiII1IiiIiI1 , oOIi111 ) ) )
  ii1III1iiIi . append ( ( OOoO % 'Normal Install' , 'RunPlugin(plugin://%s/?mode=install&name=%s&url=normal)' % ( IiII1IiiIiI1 , oOIi111 ) ) )
  ii1III1iiIi . append ( ( OOoO % 'Apply guiFix' , 'RunPlugin(plugin://%s/?mode=install&name=%s&url=gui)' % ( IiII1IiiIiI1 , oOIi111 ) ) )
  ii1III1iiIi . append ( ( OOoO % 'Build Information' , 'RunPlugin(plugin://%s/?mode=buildinfo&name=%s)' % ( IiII1IiiIiI1 , oOIi111 ) ) )
 ii1III1iiIi . append ( ( oooOo0OOOoo0 % '%s Settings' % o0OOO , 'RunPlugin(plugin://%s/?mode=settings)' % IiII1IiiIiI1 ) )
 return ii1III1iiIi
 if 43 - 43: OOoooooO * OO00O0O0O00Oo % iii11iiII
def iiiI11 ( state ) :
 o0o00OOOO = [ 'includevideo' , 'includeall' , 'includebob' , 'includephoenix' , 'includespecto' , 'includegenesis' , 'includeexodus' , 'includeonechan' , 'includesalts' , 'includesaltslite' ]
 i11iIi1iIIIIi = [ 'Include Video Addons' , 'Include All Addons' , 'Include Bob' , 'Include Phoenix' , 'Include Specto' , 'Include Genesis' , 'Include Exodus' , 'Include One Channel' , 'Include Salts' , 'Include Salts Lite HD' ]
 if state in [ 'true' , 'false' ] :
  for oOOo000oOoO0 in o0o00OOOO :
   wiz . setS ( oOOo000oOoO0 , state )
 else :
  if not state in [ 'includevideo' , 'includeall' ] and wiz . getS ( 'includeall' ) == 'true' :
   try :
    oOOo000oOoO0 = i11iIi1iIIIIi [ o0o00OOOO . index ( state ) ]
    iiIIIII1i1iI . ok ( o0OOO , "[COLOR %s]You will need to turn off [COLOR %s]Include All Addons[/COLOR] to disable[/COLOR] [COLOR %s]%s[/COLOR]" % ( iIiIi11 , oOOo0O00o , oOOo0O00o , oOOo000oOoO0 ) )
   except :
    wiz . LogNotify ( "[COLOR %s]Toggle Cache[/COLOR]" % oOOo0O00o , "[COLOR %s]Invalid id: %s[/COLOR]" % ( iIiIi11 , state ) )
  else :
   I1111iiiII1Ii = 'true' if wiz . getS ( state ) == 'false' else 'false'
   wiz . setS ( state , I1111iiiII1Ii )
   if 80 - 80: I1I1i1 % i1Ii
def iIiIiI1i111i ( url ) :
 if 'watch?v=' in url :
  IiiIi11Ii1iI1 , iiiI1i1111II = url . split ( '?' )
  IIII11iiii = iiiI1i1111II . split ( '&' )
  for oOOo000oOoO0 in IIII11iiii :
   if oOOo000oOoO0 . startswith ( 'v=' ) :
    url = oOOo000oOoO0 [ 2 : ]
    break
   else : continue
 elif 'embed' in url or 'youtu.be' in url :
  IiiIi11Ii1iI1 = url . split ( '/' )
  if len ( IiiIi11Ii1iI1 [ - 1 ] ) > 5 :
   url = IiiIi11Ii1iI1 [ - 1 ]
  elif len ( IiiIi11Ii1iI1 [ - 2 ] ) > 5 :
   url = IiiIi11Ii1iI1 [ - 2 ]
 wiz . log ( "YouTube URL: %s" % url )
 yt . PlayVideo ( url )
 if 75 - 75: iIii1I11I1II1 % i1Ii + oO0 * O0 . iiIIi1IiIi11 - OOoooooO
def i1IIiIIIi1 ( ) :
 oOoO00O = wiz . Grab_Log ( True )
 I11I1I1i1i = wiz . Grab_Log ( True , True )
 Oo0oOO0O00 = 0 ; o00OOo0o0O = oOoO00O
 if not I11I1I1i1i == False and not oOoO00O == False :
  Oo0oOO0O00 = iiIIIII1i1iI . select ( o0OOO , [ "View %s" % oOoO00O . replace ( iI11iiiI1II , "" ) , "View %s" % I11I1I1i1i . replace ( iI11iiiI1II , "" ) ] )
  if Oo0oOO0O00 == - 1 : wiz . LogNotify ( '[COLOR %s]View Log[/COLOR]' % oOOo0O00o , '[COLOR %s]View Log Cancelled![/COLOR]' % iIiIi11 ) ; return
 elif oOoO00O == False and I11I1I1i1i == False :
  wiz . LogNotify ( '[COLOR %s]View Log[/COLOR]' % oOOo0O00o , '[COLOR %s]No Log File Found![/COLOR]' % iIiIi11 )
  return
 elif not oOoO00O == False : Oo0oOO0O00 = 0
 elif not I11I1I1i1i == False : Oo0oOO0O00 = 1
 if 14 - 14: iiIIi1IiIi11 - i11IiIiiIIIII * OoooooooOO + iii11iiII . II111iiii
 o00OOo0o0O = oOoO00O if Oo0oOO0O00 == 0 else I11I1I1i1i
 i1i1I11i1I = wiz . Grab_Log ( False ) if Oo0oOO0O00 == 0 else wiz . Grab_Log ( False , True )
 if 85 - 85: OOoooooO . O0 / iii11iiII * OOoooooO - I1111 - i11iIiiIii
 wiz . TextBox ( "%s - %s" % ( o0OOO , o00OOo0o0O ) , i1i1I11i1I )
 if 25 - 25: OOoooooO % Ooo0O - iii11iiII
def oo0ooooo00o ( log = None , count = None , all = None ) :
 if log == None :
  oOoO00O = wiz . Grab_Log ( True )
  I11I1I1i1i = wiz . Grab_Log ( True , True )
  if not I11I1I1i1i == False and not oOoO00O == False :
   Oo0oOO0O00 = iiIIIII1i1iI . select ( o0OOO , [ "View %s: %s error(s)" % ( oOoO00O . replace ( iI11iiiI1II , "" ) , oo0ooooo00o ( oOoO00O , True , True ) ) , "View %s: %s error(s)" % ( I11I1I1i1i . replace ( iI11iiiI1II , "" ) , oo0ooooo00o ( I11I1I1i1i , True , True ) ) ] )
   if Oo0oOO0O00 == - 1 : wiz . LogNotify ( '[COLOR %s]View Log[/COLOR]' % oOOo0O00o , '[COLOR %s]View Log Cancelled![/COLOR]' % iIiIi11 ) ; return
  elif oOoO00O == False and I11I1I1i1i == False :
   wiz . LogNotify ( '[COLOR %s]View Log[/COLOR]' % oOOo0O00o , '[COLOR %s]No Log File Found![/COLOR]' % iIiIi11 )
   return
  elif not oOoO00O == False : Oo0oOO0O00 = 0
  elif not I11I1I1i1i == False : Oo0oOO0O00 = 1
  log = oOoO00O if Oo0oOO0O00 == 0 else I11I1I1i1i
 if log == False :
  if count == None :
   wiz . LogNotify ( "[COLOR %s]%s[/COLOR]" % ( oOOo0O00o , o0OOO ) , "[COLOR %s]Log File not Found[/COLOR]" % iIiIi11 )
   return False
  else :
   return 0
 else :
  if os . path . exists ( log ) :
   IIi1i = open ( log , mode = 'r' ) ; IiiIi11Ii1iI1 = IIi1i . read ( ) . replace ( '\n' , '' ) . replace ( '\r' , '' ) ; IIi1i . close ( )
   o0O0Oo00 = re . compile ( "-->Python callback/script returned the following error<--(.+?)-->End of Python script error report<--" ) . findall ( IiiIi11Ii1iI1 )
   if not count == None :
    if all == None :
     II1IOoOo000oOo0oo = 0
     for oOOo000oOoO0 in o0O0Oo00 :
      if IiII1IiiIiI1 in oOOo000oOoO0 : II1IOoOo000oOo0oo += 1
     return II1IOoOo000oOo0oo
    else : return len ( o0O0Oo00 )
   if len ( o0O0Oo00 ) > 0 :
    II1IOoOo000oOo0oo = 0 ; i1i1I11i1I = ""
    for oOOo000oOoO0 in o0O0Oo00 :
     if all == None and not IiII1IiiIiI1 in oOOo000oOoO0 : continue
     else :
      II1IOoOo000oOo0oo += 1
      i1i1I11i1I += "[COLOR red]Error Number %s[/COLOR]\n(PythonToCppException) : -->Python callback/script returned the following error<--%s-->End of Python script error report<--\n\n" % ( II1IOoOo000oOo0oo , oOOo000oOoO0 . replace ( '                                          ' , '\n' ) . replace ( '\\\\' , '\\' ) . replace ( o00 , '' ) )
    if II1IOoOo000oOo0oo > 0 :
     wiz . TextBox ( o0OOO , i1i1I11i1I )
    else : wiz . LogNotify ( o0OOO , "No Errors Found in Log" )
   else : wiz . LogNotify ( o0OOO , "No Errors Found in Log" )
  else : wiz . LogNotify ( o0OOO , "Log File not Found" )
  if 80 - 80: i1Ii % II111iiii - Ooo0O - iIii1I11I1II1
iIiIIi11iI = 10
ooo00o0o = 92
OOOO00o000o = 1
o0ooooO0 = 2
IIII1ii1 = 3
OOO0O0OOo = 4
Iii1 = 104
OOoOi1IiiI = 105
O0OOO0 = 107
o0OIi = 7
IIi1iiI = 110
o0o = 100
oOO00OO0o0O = 108
if 35 - 35: I1I1i1 * iiIIi1IiIi11 - iIii1I11I1II1 + I1I1i1 . OoooooooOO
def ii111iI1i1 ( default = None ) :
 class ii111iI1i1 ( xbmcgui . WindowXMLDialog ) :
  def __init__ ( self , * args , ** kwargs ) :
   self . default = kwargs [ 'default' ]
   if 80 - 80: I1111 / i1Ii * ooOo % i1Ii
  def onInit ( self ) :
   self . title = 101
   self . msg = 102
   self . scrollbar = 103
   self . upload = 201
   self . kodi = 202
   self . kodiold = 203
   self . wizard = 204
   self . okbutton = 205
   IIi1i = open ( self . default , 'r' )
   self . logmsg = IIi1i . read ( )
   IIi1i . close ( )
   self . titlemsg = "%s: %s" % ( o0OOO , self . default . replace ( iI11iiiI1II , '' ) . replace ( o0 , '' ) )
   self . showdialog ( )
   if 95 - 95: O0 / i11IiIiiIIIII . OO00O0O0O00Oo
  def showdialog ( self ) :
   self . getControl ( self . title ) . setLabel ( self . titlemsg )
   self . getControl ( self . msg ) . setText ( wiz . highlightText ( self . logmsg ) )
   self . setFocusId ( self . scrollbar )
   if 17 - 17: i11IiIiiIIIII
  def onClick ( self , controlId ) :
   if controlId == self . okbutton : self . close ( )
   elif controlId == self . upload : self . close ( ) ; uploadLog . Main ( )
   elif controlId == self . kodi :
    o0OO0OO000OO = wiz . Grab_Log ( False )
    O00o0000OO = wiz . Grab_Log ( True )
    if o0OO0OO000OO == False :
     self . titlemsg = "%s: View Log Error" % o0OOO
     self . getControl ( self . msg ) . setText ( "Log File Does Not Exists!" )
    else :
     self . titlemsg = "%s: %s" % ( o0OOO , O00o0000OO . replace ( iI11iiiI1II , '' ) )
     self . getControl ( self . title ) . setLabel ( self . titlemsg )
     self . getControl ( self . msg ) . setText ( wiz . highlightText ( o0OO0OO000OO ) )
     self . setFocusId ( self . scrollbar )
   elif controlId == self . kodiold :
    o0OO0OO000OO = wiz . Grab_Log ( False , True )
    O00o0000OO = wiz . Grab_Log ( True , True )
    if o0OO0OO000OO == False :
     self . titlemsg = "%s: View Log Error" % o0OOO
     self . getControl ( self . msg ) . setText ( "Log File Does Not Exists!" )
    else :
     self . titlemsg = "%s: %s" % ( o0OOO , O00o0000OO . replace ( iI11iiiI1II , '' ) )
     self . getControl ( self . title ) . setLabel ( self . titlemsg )
     self . getControl ( self . msg ) . setText ( wiz . highlightText ( o0OO0OO000OO ) )
     self . setFocusId ( self . scrollbar )
   elif controlId == self . wizard :
    o0OO0OO000OO = wiz . Grab_Log ( False , False , True )
    O00o0000OO = wiz . Grab_Log ( True , False , True )
    if o0OO0OO000OO == False :
     self . titlemsg = "%s: View Log Error" % o0OOO
     self . getControl ( self . msg ) . setText ( "Log File Does Not Exists!" )
    else :
     self . titlemsg = "%s: %s" % ( o0OOO , O00o0000OO . replace ( o0 , '' ) )
     self . getControl ( self . title ) . setLabel ( self . titlemsg )
     self . getControl ( self . msg ) . setText ( wiz . highlightText ( o0OO0OO000OO ) )
     self . setFocusId ( self . scrollbar )
     if 61 - 61: i1Ii % i1IIi - iiIIi1IiIi11 . OOoooooO - Ooo0O + Ooo0O
  def onAction ( self , action ) :
   if action == iIiIIi11iI : self . close ( )
   elif action == ooo00o0o : self . close ( )
 if default == None : default = wiz . Grab_Log ( True )
 II1i = ii111iI1i1 ( "LogViewer.xml" , I1ii11iIi11i . getAddonInfo ( 'path' ) , 'DefaultSkin' , default = default )
 II1i . doModal ( )
 del II1i
 if 30 - 30: i11IiIiiIIIII / oO0
def IIIiiiIiI ( addon , name , over = False ) :
 if not over == False :
  o00oIIi1i1 = 1
 else :
  o00oIIi1i1 = iiIIIII1i1iI . yesno ( o0OOO , '[COLOR %s]Are you sure you want to delete the addon:' % iIiIi11 , 'Name: [COLOR %s]%s[/COLOR]' % ( oOOo0O00o , name ) , 'ID: [COLOR %s]%s[/COLOR][/COLOR]' % ( oOOo0O00o , addon ) , yeslabel = '[B][COLOR green]Remove Addon[/COLOR][/B]' , nolabel = '[B][COLOR red]Don\'t Remove[/COLOR][/B]' )
 if o00oIIi1i1 == 1 :
  I111IIiIII = os . path . join ( O0O , addon )
  wiz . log ( "Removing Addon %s" % addon )
  wiz . cleanHouse ( I111IIiIII )
  xbmc . sleep ( 200 )
  try : shutil . rmtree ( I111IIiIII )
  except Exception , O00OO : wiz . log ( "Error removing %s" % addon , xbmc . LOGNOTICE )
  i1II1Ii1i1 ( addon , name , over )
 if over == False :
  wiz . LogNotify ( "[COLOR %s]%s[/COLOR]" % ( oOOo0O00o , o0OOO ) , "[COLOR %s]%s Removed[/COLOR]" % ( iIiIi11 , name ) )
  if 22 - 22: IIIi1i1I * iiIIi1IiIi11
def i1II1Ii1i1 ( addon , name = None , over = False ) :
 if addon == 'all' :
  if iiIIIII1i1iI . yesno ( o0OOO , '[COLOR %s]Would you like to remove [COLOR %s]ALL[/COLOR] addon data stored in you Userdata folder?[/COLOR]' % ( iIiIi11 , oOOo0O00o ) , yeslabel = '[B][COLOR green]Remove Data[/COLOR][/B]' , nolabel = '[B][COLOR red]Don\'t Remove[/COLOR][/B]' ) :
   wiz . cleanHouse ( ooOOOo0oo0O0 )
  else : wiz . LogNotify ( '[COLOR %s]Remove Addon Data[/COLOR]' % oOOo0O00o , '[COLOR %s]Cancelled![/COLOR]' % iIiIi11 )
 elif addon == 'uninstalled' :
  if iiIIIII1i1iI . yesno ( o0OOO , '[COLOR %s]Would you like to remove [COLOR %s]ALL[/COLOR] addon data stored in you Userdata folder for uninstalled addons?[/COLOR]' % ( iIiIi11 , oOOo0O00o ) , yeslabel = '[B][COLOR green]Remove Data[/COLOR][/B]' , nolabel = '[B][COLOR red]Don\'t Remove[/COLOR][/B]' ) :
   O0oOoo0o000O0 = 0
   for I111IIiIII in glob . glob ( os . path . join ( ooOOOo0oo0O0 , '*' ) ) :
    OO0OOoo0OOO = I111IIiIII . replace ( ooOOOo0oo0O0 , '' ) . replace ( '\\' , '' ) . replace ( '/' , '' )
    if OO0OOoo0OOO in Iii1I1I11iiI1 : pass
    elif os . path . exists ( os . path . join ( O0O , OO0OOoo0OOO ) ) : pass
    else : wiz . cleanHouse ( I111IIiIII ) ; O0oOoo0o000O0 += 1 ; wiz . log ( I111IIiIII ) ; shutil . rmtree ( I111IIiIII )
   wiz . LogNotify ( '[COLOR %s]Clean up Uninstalled[/COLOR]' % oOOo0O00o , '[COLOR %s]%s Folders(s) Removed[/COLOR]' % ( iIiIi11 , O0oOoo0o000O0 ) )
  else : wiz . LogNotify ( '[COLOR %s]Remove Addon Data[/COLOR]' % oOOo0O00o , '[COLOR %s]Cancelled![/COLOR]' % iIiIi11 )
 elif addon == 'empty' :
  if iiIIIII1i1iI . yesno ( o0OOO , '[COLOR %s]Would you like to remove [COLOR %s]ALL[/COLOR] empty addon data folders in you Userdata folder?[/COLOR]' % ( iIiIi11 , oOOo0O00o ) , yeslabel = '[B][COLOR green]Remove Data[/COLOR][/B]' , nolabel = '[B][COLOR red]Don\'t Remove[/COLOR][/B]' ) :
   O0oOoo0o000O0 = wiz . emptyfolder ( ooOOOo0oo0O0 )
   wiz . LogNotify ( '[COLOR %s]Remove Empty Folders[/COLOR]' % oOOo0O00o , '[COLOR %s]%s Folders(s) Removed[/COLOR]' % ( iIiIi11 , O0oOoo0o000O0 ) )
  else : wiz . LogNotify ( '[COLOR %s]Remove Empty Folders[/COLOR]' % oOOo0O00o , '[COLOR %s]Cancelled![/COLOR]' % iIiIi11 )
 else :
  iIIIiIi1i = os . path . join ( oOo00Oo00O , 'addon_data' , addon )
  if addon in Iii1I1I11iiI1 :
   wiz . LogNotify ( "[COLOR %s]Protected Plugin[/COLOR]" % oOOo0O00o , "[COLOR %s]Not allowed to remove Addon_Data[/COLOR]" % iIiIi11 )
  elif os . path . exists ( iIIIiIi1i ) :
   if iiIIIII1i1iI . yesno ( o0OOO , '[COLOR %s]Would you also like to remove the addon data for:[/COLOR]' % iIiIi11 , '[COLOR %s]%s[/COLOR]' % ( oOOo0O00o , addon ) , yeslabel = '[B][COLOR green]Remove Data[/COLOR][/B]' , nolabel = '[B][COLOR red]Don\'t Remove[/COLOR][/B]' ) :
    wiz . cleanHouse ( iIIIiIi1i )
    try :
     shutil . rmtree ( iIIIiIi1i )
    except :
     wiz . log ( "Error deleting: %s" % iIIIiIi1i )
   else :
    wiz . log ( 'Addon data for %s was not removed' % addon )
 wiz . refresh ( )
 if 36 - 36: o0o0Oo0oooo0
def IiIIIiI ( type ) :
 if type == 'build' :
  II1IOoOo000oOo0oo = IiI ( 'restore' )
  if II1IOoOo000oOo0oo == False : wiz . LogNotify ( "[COLOR %s]%s[/COLOR]" % ( oOOo0O00o , o0OOO ) , "[COLOR %s]Local Restore Cancelled[/COLOR]" % iIiIi11 ) ; return
 if not wiz . currSkin ( ) in [ 'skin.confluence' , 'skin.estuary' ] :
  wiz . skinToDefault ( )
 wiz . restoreLocal ( type )
 if 19 - 19: I1111 . OoooooooOO * I1111 + i1Ii + OoooooooOO
def i11iiI ( type ) :
 if type == 'build' :
  II1IOoOo000oOo0oo = IiI ( 'restore' )
  if II1IOoOo000oOo0oo == False : wiz . LogNotify ( "[COLOR %s]%s[/COLOR]" % ( oOOo0O00o , o0OOO ) , "[COLOR %s]External Restore Cancelled[/COLOR]" % iIiIi11 ) ; return
 wiz . restoreExternal ( type )
 if 67 - 67: oO0 + IiiIII111ii
def o0O00OooooO ( name ) :
 if wiz . workingURL ( I1I1i1I ) == True :
  if wiz . checkBuild ( name , 'url' ) :
   name , O0OOO0OOooo00 , oO0o00oOOooO0 , OOOoO000 , oOOOO , Ii , Ii1ii111i1 , i1i1i1I , Ii1iI111 , oOoo000 , OooOo00o = wiz . checkBuild ( name , 'all' )
   oOoo000 = 'Yes' if oOoo000 . lower ( ) == 'yes' else 'No'
   i1i1I11i1I = "[COLOR %s]Build Name:[/COLOR] [COLOR %s]%s[/COLOR][CR]" % ( iIiIi11 , oOOo0O00o , name )
   i1i1I11i1I += "[COLOR %s]Build Version:[/COLOR] [COLOR %s]%s[/COLOR][CR]" % ( iIiIi11 , oOOo0O00o , O0OOO0OOooo00 )
   if not Ii == "http://" :
    oO00OoO0oo = wiz . themeCount ( name , False )
    i1i1I11i1I += "[COLOR %s]Build Theme(s):[/COLOR] [COLOR %s]%s[/COLOR][CR]" % ( iIiIi11 , oOOo0O00o , ', ' . join ( oO00OoO0oo ) )
   i1i1I11i1I += "[COLOR %s]Kodi Version:[/COLOR] [COLOR %s]%s[/COLOR][CR]" % ( iIiIi11 , oOOo0O00o , oOOOO )
   i1i1I11i1I += "[COLOR %s]Adult Content:[/COLOR] [COLOR %s]%s[/COLOR][CR]" % ( iIiIi11 , oOOo0O00o , oOoo000 )
   i1i1I11i1I += "[COLOR %s]Description:[/COLOR] [COLOR %s]%s[/COLOR][CR]" % ( iIiIi11 , oOOo0O00o , OooOo00o )
   wiz . TextBox ( o0OOO , i1i1I11i1I )
  else : wiz . log ( "Invalid Build Name!" )
 else : wiz . log ( "Build text file not working: %s" % WORKINGURL )
 if 52 - 52: i1Ii % OOoooooO
def I111 ( name ) :
 if wiz . workingURL ( I1I1i1I ) == True :
  oOOooo00OOooO = wiz . checkBuild ( name , 'preview' )
  if oOOooo00OOooO and not oOOooo00OOooO == 'http://' : iIiIiI1i111i ( oOOooo00OOooO )
  else : wiz . log ( "[%s]Unable to find url for video preview" % name )
 else : wiz . log ( "Build text file not working: %s" % WORKINGURL )
 if 31 - 31: ooOo / I1I1i1 + ooOo - II111iiii
def iiiii1i ( plugin ) :
 iI1i = os . path . join ( O0O , plugin , 'addon.xml' )
 if os . path . exists ( iI1i ) :
  OOOOOo = open ( iI1i , mode = 'r' ) ; i1oO0OO0 = OOOOOo . read ( ) ; OOOOOo . close ( ) ;
  o0O0Oo00 = wiz . parseDOM ( i1oO0OO0 , 'import' , ret = 'addon' )
  Ii1iiI = [ ]
  for I1IiiiIiI in o0O0Oo00 :
   if not 'xbmc.python' in I1IiiiIiI :
    Ii1iiI . append ( I1IiiiIiI )
  return Ii1iiI
 return [ ]
 if 87 - 87: Ooo0O % IiiIII111ii
def ooO0o0oO0 ( do ) :
 if do == 'import' :
  o0oOO00o0o = os . path . join ( o0 , 'temp' )
  if not os . path . exists ( o0oOO00o0o ) : os . makedirs ( o0oOO00o0o )
  OOOOOo = iiIIIII1i1iI . browse ( 1 , '[COLOR %s]Select the location of the SaveData.zip[/COLOR]' % iIiIi11 , 'files' , '.zip' , False , False , o00 )
  if not OOOOOo . endswith ( '.zip' ) :
   wiz . LogNotify ( "[COLOR %s]%s[/COLOR]" % ( oOOo0O00o , o0OOO ) , "[COLOR %s]Import Data Error![/COLOR]" % ( iIiIi11 ) )
   return
  I1111o0oO0OoO0o = os . path . join ( O0ooO0Oo00o , 'SaveData.zip' )
  i11I = xbmcvfs . copy ( OOOOOo , I1111o0oO0OoO0o )
  wiz . log ( "%s" % str ( i11I ) )
  extract . all ( xbmc . translatePath ( I1111o0oO0OoO0o ) , o0oOO00o0o )
  o0oo0 = os . path . join ( o0oOO00o0o , 'trakt' )
  oO00O = os . path . join ( o0oOO00o0o , 'login' )
  II1IiiIII = os . path . join ( o0oOO00o0o , 'debrid' )
  II1IOoOo000oOo0oo = 0
  if os . path . exists ( o0oo0 ) :
   II1IOoOo000oOo0oo += 1
   I11I111i1I1 = os . listdir ( o0oo0 )
   if not os . path . exists ( traktit . TRAKTFOLD ) : os . makedirs ( traktit . TRAKTFOLD )
   for oOOo000oOoO0 in I11I111i1I1 :
    iii1O0Ooo0O = os . path . join ( traktit . TRAKTFOLD , oOOo000oOoO0 )
    I1ii1i11i = os . path . join ( o0oo0 , oOOo000oOoO0 )
    if os . path . exists ( iii1O0Ooo0O ) :
     if not iiIIIII1i1iI . yesno ( o0OOO , "[COLOR %s]Would you like replace the current [COLOR %s]%s[/COLOR] file?" % ( iIiIi11 , oOOo0O00o , oOOo000oOoO0 ) , yeslabel = "[B][COLOR green]Yes Replace[/COLOR][/B]" , nolabel = "[B][COLOR red]No Skip[/COLOR][/B]" ) : continue
     else : os . remove ( iii1O0Ooo0O )
    shutil . copy ( I1ii1i11i , iii1O0Ooo0O )
   traktit . importlist ( 'all' )
   traktit . traktIt ( 'restore' , 'all' )
  if os . path . exists ( oO00O ) :
   II1IOoOo000oOo0oo += 1
   I11I111i1I1 = os . listdir ( oO00O )
   if not os . path . exists ( loginit . LOGINFOLD ) : os . makedirs ( loginit . LOGINFOLD )
   for oOOo000oOoO0 in I11I111i1I1 :
    iii1O0Ooo0O = os . path . join ( loginit . LOGINFOLD , oOOo000oOoO0 )
    I1ii1i11i = os . path . join ( oO00O , oOOo000oOoO0 )
    if os . path . exists ( iii1O0Ooo0O ) :
     if not iiIIIII1i1iI . yesno ( o0OOO , "[COLOR %s]Would you like replace the current [COLOR %s]%s[/COLOR] file?" % ( iIiIi11 , oOOo0O00o , oOOo000oOoO0 ) , yeslabel = "[B][COLOR green]Yes Replace[/COLOR][/B]" , nolabel = "[B][COLOR red]No Skip[/COLOR][/B]" ) : continue
     else : os . remove ( iii1O0Ooo0O )
    shutil . copy ( I1ii1i11i , iii1O0Ooo0O )
   loginit . importlist ( 'all' )
   loginit . loginIt ( 'restore' , 'all' )
  if os . path . exists ( II1IiiIII ) :
   II1IOoOo000oOo0oo += 1
   I11I111i1I1 = os . listdir ( II1IiiIII )
   if not os . path . exists ( debridit . REALFOLD ) : os . makedirs ( debridit . REALFOLD )
   for oOOo000oOoO0 in I11I111i1I1 :
    iii1O0Ooo0O = os . path . join ( debridit . REALFOLD , oOOo000oOoO0 )
    I1ii1i11i = os . path . join ( II1IiiIII , oOOo000oOoO0 )
    if os . path . exists ( iii1O0Ooo0O ) :
     if not iiIIIII1i1iI . yesno ( o0OOO , "[COLOR %s]Would you like replace the current [COLOR %s]%s[/COLOR] file?" % ( iIiIi11 , oOOo0O00o , oOOo000oOoO0 ) , yeslabel = "[B][COLOR green]Yes Replace[/COLOR][/B]" , nolabel = "[B][COLOR red]No Skip[/COLOR][/B]" ) : continue
     else : os . remove ( iii1O0Ooo0O )
    shutil . copy ( I1ii1i11i , iii1O0Ooo0O )
   debridit . importlist ( 'all' )
   debridit . debridIt ( 'restore' , 'all' )
  wiz . cleanHouse ( o0oOO00o0o )
  wiz . removeFolder ( o0oOO00o0o )
  os . remove ( I1111o0oO0OoO0o )
  if II1IOoOo000oOo0oo == 0 : wiz . LogNotify ( "[COLOR %s]%s[/COLOR]" % ( oOOo0O00o , o0OOO ) , "[COLOR %s]Save Data Import Failed[/COLOR]" % iIiIi11 )
  else : wiz . LogNotify ( "[COLOR %s]%s[/COLOR]" % ( oOOo0O00o , o0OOO ) , "[COLOR %s]Save Data Import Complete[/COLOR]" % iIiIi11 )
 elif do == 'export' :
  iii1oOo0OoOOOo0 = xbmc . translatePath ( O0ooO0Oo00o )
  dir = [ traktit . TRAKTFOLD , debridit . REALFOLD , loginit . LOGINFOLD ]
  traktit . traktIt ( 'update' , 'all' )
  loginit . loginIt ( 'update' , 'all' )
  debridit . debridIt ( 'update' , 'all' )
  OOOOOo = iiIIIII1i1iI . browse ( 3 , '[COLOR %s]Select where you wish to export the savedata zip?[/COLOR]' % iIiIi11 , 'files' , '' , False , True , o00 )
  OOOOOo = xbmc . translatePath ( OOOOOo )
  OOoo00 = os . path . join ( iii1oOo0OoOOOo0 , 'SaveData.zip' )
  I1I1 = zipfile . ZipFile ( OOoo00 , mode = 'w' )
  for O0OoO0o in dir :
   if os . path . exists ( O0OoO0o ) :
    I11I111i1I1 = os . listdir ( O0OoO0o )
    for file in I11I111i1I1 :
     I1I1 . write ( os . path . join ( O0OoO0o , file ) , os . path . join ( O0OoO0o , file ) . replace ( o0 , '' ) , zipfile . ZIP_DEFLATED )
  I1I1 . close ( )
  if OOOOOo == iii1oOo0OoOOOo0 :
   iiIIIII1i1iI . ok ( o0OOO , "[COLOR %s]Save data has been backed up to:[/COLOR]" % ( iIiIi11 ) , "[COLOR %s]%s[/COLOR]" % ( oOOo0O00o , OOoo00 ) )
  else :
   try :
    xbmcvfs . copy ( OOoo00 , os . path . join ( OOOOOo , 'SaveData.zip' ) )
    iiIIIII1i1iI . ok ( o0OOO , "[COLOR %s]Save data has been backed up to:[/COLOR]" % ( iIiIi11 ) , "[COLOR %s]%s[/COLOR]" % ( oOOo0O00o , os . path . join ( OOOOOo , 'SaveData.zip' ) ) )
   except :
    iiIIIII1i1iI . ok ( o0OOO , "[COLOR %s]Save data has been backed up to:[/COLOR]" % ( iIiIi11 ) , "[COLOR %s]%s[/COLOR]" % ( oOOo0O00o , OOoo00 ) )
    if 78 - 78: i11IiIiiIIIII . iii11iiII + IIIi1i1I * iiIIi1IiIi11 - i1IIi
def iIIiiIIIi1I ( url ) :
 iIi1I1 = urllib2 . Request ( url )
 iIi1I1 . add_header ( 'User-Agent' , 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3' )
 O0oOoo0OoO0O = urllib2 . urlopen ( iIi1I1 )
 i1oO0OO0 = O0oOoo0OoO0O . read ( )
 O0oOoo0OoO0O . close ( )
 return i1oO0OO0
 if 27 - 27: IiiIII111ii % i1IIi . Ooo0O % OO00O0O0O00Oo
def i1iI ( url ) :
 if url == 'http://' : return False
 try :
  iIi1I1 = urllib2 . Request ( url )
  iIi1I1 . add_header ( 'User-Agent' , USER_AGENT )
  O0oOoo0OoO0O = urllib2 . urlopen ( iIi1I1 )
  O0oOoo0OoO0O . close ( )
 except Exception , O00OO :
  return O00OO
 return True
 if 73 - 73: OoooooooOO . Ooo0O / O0 - O0
 if 25 - 25: iIii1I11I1II1 * i11IiIiiIIIII - IIIi1i1I % i11iIiiIii + IiiIII111ii % IIIi1i1I
 if 5 - 5: iIii1I11I1II1 . IIIi1i1I
 if 2 - 2: iIii1I11I1II1 * ooOo % i1IIi % oO0 + OoooooooOO + ooOo
def IiI ( install = None , over = False ) :
 if o0O0OOO0Ooo == 'true' :
  traktit . autoUpdate ( 'all' )
  wiz . setS ( 'traktlastsave' , str ( I1IiiiiI ) )
 if iiIiII1 == 'true' :
  debridit . autoUpdate ( 'all' )
  wiz . setS ( 'debridlastsave' , str ( I1IiiiiI ) )
 if OOO00O0O == 'true' :
  loginit . autoUpdate ( 'all' )
  wiz . setS ( 'loginlastsave' , str ( I1IiiiiI ) )
 if over == True : IiiI1II1II1i = 1
 elif install == 'restore' : IiiI1II1II1i = iiIIIII1i1iI . yesno ( o0OOO , "[COLOR %s]Do you wish to restore your" % iIiIi11 , "Kodi configuration to default settings" , "Before installing the local backup?[/COLOR]" , nolabel = '[B][COLOR red]No, Cancel[/COLOR][/B]' , yeslabel = '[B][COLOR green]Continue[/COLOR][/B]' )
 elif install : IiiI1II1II1i = iiIIIII1i1iI . yesno ( o0OOO , "[COLOR %s]Do you wish to restore your" % iIiIi11 , "Kodi configuration to default settings" , "Before installing [COLOR %s]%s[/COLOR]?" % ( oOOo0O00o , install ) , nolabel = '[B][COLOR red]No, Cancel[/COLOR][/B]' , yeslabel = '[B][COLOR green]Continue[/COLOR][/B]' )
 else : IiiI1II1II1i = iiIIIII1i1iI . yesno ( o0OOO , "[COLOR %s]Do you wish to restore your" % iIiIi11 , "Kodi configuration to default settings?[/COLOR]" , nolabel = '[B][COLOR red]No, Cancel[/COLOR][/B]' , yeslabel = '[B][COLOR green]Continue[/COLOR][/B]' )
 if IiiI1II1II1i :
  if not wiz . currSkin ( ) in [ 'skin.confluence' , 'skin.estuary' ] :
   OO00Oooo000 = 'skin.confluence' if o0OIiII < 17 else 'skin.estuary'
   if 16 - 16: iii11iiII
   if 63 - 63: iiIIi1IiIi11
   skinSwitch . swapSkins ( OO00Oooo000 )
   II1IOoOo000oOo0oo = 0
   xbmc . sleep ( 1000 )
   while not xbmc . getCondVisibility ( "Window.isVisible(yesnodialog)" ) and II1IOoOo000oOo0oo < 150 :
    II1IOoOo000oOo0oo += 1
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
  i1i1iIiI = os . path . abspath ( o00 )
  oo00 . create ( o0OOO , "[COLOR %s]Calculating files and folders" % iIiIi11 , '' , 'Please Wait![/COLOR]' )
  I11iii = sum ( [ len ( I11I111i1I1 ) for IIi111 , oO0o0o0O , I11I111i1I1 in os . walk ( i1i1iIiI ) ] ) ; I111ii1iI = 0
  oo00 . update ( 0 , "[COLOR %s]Gathering Excludes list." % iIiIi11 )
  Iii1I1I11iiI1 . append ( 'My_Builds' )
  Iii1I1I11iiI1 . append ( 'archive_cache' )
  if IIII == 'true' :
   I1iIiiiI1 = glob . glob ( os . path . join ( O0O , 'repo*/' ) )
   for oOOo000oOoO0 in I1iIiiiI1 :
    i1IiI1ii1i = os . path . split ( oOOo000oOoO0 [ : - 1 ] ) [ 1 ]
    if not i1IiI1ii1i == Iii1I1I11iiI1 :
     Iii1I1I11iiI1 . append ( i1IiI1ii1i )
  if iiIiI == 'true' :
   Iii1I1I11iiI1 . append ( 'plugin.program.super.favourites' )
  if o00oooO0Oo == 'true' :
   i1I1I1I = ''
   i111IiiI1Ii = wiz . whiteList ( 'read' )
   if len ( i111IiiI1Ii ) > 0 :
    for oOOo000oOoO0 in i111IiiI1Ii :
     try : O0Oo0o000oO , id , O0OoO0o = oOOo000oOoO0
     except : pass
     if O0OoO0o . startswith ( 'pvr' ) : i1I1I1I = id
     I1IiiiIiI = iiiii1i ( O0OoO0o )
     for iII1III in I1IiiiIiI :
      if not iII1III in Iii1I1I11iiI1 :
       Iii1I1I11iiI1 . append ( iII1III )
      O0oo0oO00o = iiiii1i ( iII1III )
      for I1ii111i1ii1 in O0oo0oO00o :
       if not I1ii111i1ii1 in Iii1I1I11iiI1 :
        Iii1I1I11iiI1 . append ( I1ii111i1ii1 )
     if not O0OoO0o in Iii1I1I11iiI1 :
      Iii1I1I11iiI1 . append ( O0OoO0o )
    if not i1I1I1I == '' : wiz . setS ( 'pvrclient' , O0OoO0o )
  if wiz . getS ( 'pvrclient' ) == '' :
   for oOOo000oOoO0 in Iii1I1I11iiI1 :
    if oOOo000oOoO0 . startswith ( 'pvr' ) :
     wiz . setS ( 'pvrclient' , oOOo000oOoO0 )
  oo00 . update ( 0 , "[COLOR %s]Clearing out files and folders:" % iIiIi11 )
  o0Ii11iIiiI = wiz . latestDB ( 'Addons' )
  for o000 , i11ii1 , I11I111i1I1 in os . walk ( i1i1iIiI , topdown = True ) :
   i11ii1 [ : ] = [ oO0o0o0O for oO0o0o0O in i11ii1 if oO0o0o0O not in Iii1I1I11iiI1 ]
   for O0Oo0o000oO in I11I111i1I1 :
    I111ii1iI += 1
    O0OoO0o = o000 . replace ( '/' , '\\' ) . split ( '\\' )
    II1IOoOo000oOo0oo = len ( O0OoO0o ) - 1
    if O0Oo0o000oO == 'sources.xml' and O0OoO0o [ - 1 ] == 'userdata' and ooOOoooooo == 'true' : wiz . log ( "Keep Sources: %s" % os . path . join ( o000 , O0Oo0o000oO ) , xbmc . LOGNOTICE )
    elif O0Oo0o000oO == 'favourites.xml' and O0OoO0o [ - 1 ] == 'userdata' and IiIIIi1iIi == 'true' : wiz . log ( "Keep Favourites: %s" % os . path . join ( o000 , O0Oo0o000oO ) , xbmc . LOGNOTICE )
    elif O0Oo0o000oO == 'profiles.xml' and O0OoO0o [ - 1 ] == 'userdata' and II1I == 'true' : wiz . log ( "Keep Profiles: %s" % os . path . join ( o000 , O0Oo0o000oO ) , xbmc . LOGNOTICE )
    elif O0Oo0o000oO == 'advancedsettings.xml' and O0OoO0o [ - 1 ] == 'userdata' and O0i1II1Iiii1I11 == 'true' : wiz . log ( "Keep Advanced Settings: %s" % os . path . join ( o000 , O0Oo0o000oO ) , xbmc . LOGNOTICE )
    elif O0Oo0o000oO in Ooo0oOooo0 : wiz . log ( "Keep Log File: %s" % O0Oo0o000oO , xbmc . LOGNOTICE )
    elif O0Oo0o000oO . endswith ( '.db' ) :
     try :
      if O0Oo0o000oO == o0Ii11iIiiI and o0OIiII >= 17 : wiz . log ( "Ignoring %s on v%s" % ( O0Oo0o000oO , o0OIiII ) , xbmc . LOGNOTICE )
      else : os . remove ( os . path . join ( o000 , O0Oo0o000oO ) )
     except Exception , O00OO :
      if not O0Oo0o000oO . startswith ( 'Textures13' ) :
       wiz . log ( 'Failed to delete, Purging DB' , xbmc . LOGNOTICE )
       wiz . log ( "-> %s" % ( str ( O00OO ) ) , xbmc . LOGNOTICE )
       wiz . purgeDb ( os . path . join ( o000 , O0Oo0o000oO ) )
    else :
     oo00 . update ( int ( wiz . percentage ( I111ii1iI , I11iii ) ) , '' , '[COLOR %s]File: [/COLOR][COLOR %s]%s[/COLOR]' % ( iIiIi11 , oOOo0O00o , O0Oo0o000oO ) , '' )
     try : os . remove ( os . path . join ( o000 , O0Oo0o000oO ) )
     except Exception , O00OO :
      wiz . log ( "Error removing %s" % os . path . join ( o000 , O0Oo0o000oO ) , xbmc . LOGNOTICE )
      wiz . log ( "-> / %s" % ( str ( O00OO ) ) , xbmc . LOGNOTICE )
   if oo00 . iscanceled ( ) :
    oo00 . close ( )
    wiz . LogNotify ( "[COLOR %s]%s[/COLOR]" % ( oOOo0O00o , o0OOO ) , "[COLOR %s]Fresh Start Cancelled[/COLOR]" % iIiIi11 )
    return False
  for o000 , i11ii1 , I11I111i1I1 in os . walk ( i1i1iIiI , topdown = True ) :
   i11ii1 [ : ] = [ oO0o0o0O for oO0o0o0O in i11ii1 if oO0o0o0O not in Iii1I1I11iiI1 ]
   for O0Oo0o000oO in i11ii1 :
    oo00 . update ( 100 , '' , 'Cleaning Up Empty Folder: [COLOR %s]%s[/COLOR]' % ( oOOo0O00o , O0Oo0o000oO ) , '' )
    if O0Oo0o000oO not in [ "Database" , "userdata" , "temp" , "addons" , "addon_data" ] :
     shutil . rmtree ( os . path . join ( o000 , O0Oo0o000oO ) , ignore_errors = True , onerror = None )
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
   Oooooooo00o00 ( install , 'normal' , over = True )
  else :
   if I11i1I1I == 1 : OOOO00OoooO = 1
   elif I11i1I1I == 2 : OOOO00OoooO = 0
   else : OOOO00OoooO = iiIIIII1i1iI . yesno ( o0OOO , "[COLOR %s]Would you like to [COLOR %s]Force close[/COLOR] kodi or [COLOR %s]Reload Profile[/COLOR]?[/COLOR]" % ( iIiIi11 , oOOo0O00o , oOOo0O00o ) , yeslabel = "[B][COLOR red]Reload Profile[/COLOR][/B]" , nolabel = "[B][COLOR green]Force Close[/COLOR][/B]" )
   if OOOO00OoooO == 1 : wiz . reloadFix ( 'fresh' )
   else : wiz . addonUpdates ( 'reset' ) ; wiz . killxbmc ( True )
 else :
  if not install == 'restore' :
   wiz . LogNotify ( "[COLOR %s]%s[/COLOR]" % ( oOOo0O00o , o0OOO ) , '[COLOR %s]Fresh Install: Cancelled![/COLOR]' % iIiIi11 )
   wiz . refresh ( )
   if 4 - 4: i11iIiiIii - iii11iiII % oO0 * OO00O0O0O00Oo % I1I1i1
   if 71 - 71: OOoooooO . OOoooooO - iIii1I11I1II1
   if 22 - 22: OoooooooOO / oO0 % iiIIi1IiIi11 * o0o0Oo0oooo0
   if 32 - 32: OoooooooOO % IIIi1i1I % iIii1I11I1II1 / O0
def Ooo0oOOoo0O ( ) :
 if iiIIIII1i1iI . yesno ( o0OOO , '[COLOR %s]Would you like to clear cache?[/COLOR]' % iIiIi11 , nolabel = '[B][COLOR red]No, Cancel[/COLOR][/B]' , yeslabel = '[B][COLOR green]Clear Cache[/COLOR][/B]' ) :
  wiz . clearCache ( )
  if 57 - 57: ooOo . i11iIiiIii * II111iiii + OoooooooOO + IiiIII111ii
  if 73 - 73: O0 % i11IiIiiIIIII + iiIIi1IiIi11 . oO0 . oO0 + i1Ii
def i1i111I ( ) :
 if iiIIIII1i1iI . yesno ( o0OOO , '[COLOR %s]Would you like to clear cache, packages and thumbnails?[/COLOR]' % iIiIi11 , nolabel = '[B][COLOR red]Cancel Process[/COLOR][/B]' , yeslabel = '[B][COLOR green]Clean All[/COLOR][/B]' ) :
  wiz . clearCache ( )
  wiz . clearPackages ( 'total' )
  oO0O0O0OO0O00 ( 'total' )
  if 39 - 39: O0 - OoooooooOO
def oO0O0O0OO0O00 ( type = None ) :
 oo0O00ooo0o = wiz . latestDB ( 'Textures' )
 if not type == None : i1Ii11I1II = 1
 else : i1Ii11I1II = iiIIIII1i1iI . yesno ( o0OOO , '[COLOR %s]Would you like to delete the %s and Thumbnails folder?' % ( iIiIi11 , oo0O00ooo0o ) , "They will repopulate on the next startup[/COLOR]" , nolabel = '[B][COLOR red]Don\'t Delete[/COLOR][/B]' , yeslabel = '[B][COLOR green]Delete Thumbs[/COLOR][/B]' )
 if i1Ii11I1II == 1 :
  try : wiz . removeFile ( os . join ( OOOO , oo0O00ooo0o ) )
  except : wiz . log ( 'Failed to delete, Purging DB.' ) ; wiz . purgeDb ( oo0O00ooo0o )
  wiz . removeFolder ( oOoOooOo0o0 )
  if 29 - 29: OoooooooOO . II111iiii % o0o0Oo0oooo0
 else : wiz . log ( 'Clear thumbnames cancelled' )
 wiz . redoThumbs ( )
 if 26 - 26: iIii1I11I1II1 - oO0 . i1Ii . i1Ii + iIii1I11I1II1 * Ooo0O
def O0Oo00 ( ) :
 Oo0o0ooOoO = [ ] ; IIIiIi1iiI = [ ]
 for iI1Ii11 , Ooo0 , I11I111i1I1 in os . walk ( o00 ) :
  for IIi1i in fnmatch . filter ( I11I111i1I1 , '*.db' ) :
   if IIi1i != 'Thumbs.db' :
    IiiiIIi = os . path . join ( iI1Ii11 , IIi1i )
    Oo0o0ooOoO . append ( IiiiIIi )
    dir = IiiiIIi . replace ( '\\' , '/' ) . split ( '/' )
    IIIiIi1iiI . append ( '(%s) %s' % ( dir [ len ( dir ) - 2 ] , dir [ len ( dir ) - 1 ] ) )
 if o0OIiII >= 16 :
  i1Ii11I1II = iiIIIII1i1iI . multiselect ( "[COLOR %s]Select DB File to Purge[/COLOR]" % iIiIi11 , IIIiIi1iiI )
  if i1Ii11I1II == None : wiz . LogNotify ( "[COLOR %s]Purge Database[/COLOR]" % oOOo0O00o , "[COLOR %s]Cancelled[/COLOR]" % iIiIi11 )
  elif len ( i1Ii11I1II ) == 0 : wiz . LogNotify ( "[COLOR %s]Purge Database[/COLOR]" % oOOo0O00o , "[COLOR %s]Cancelled[/COLOR]" % iIiIi11 )
  else :
   for I1IIIi in i1Ii11I1II : wiz . purgeDb ( Oo0o0ooOoO [ I1IIIi ] )
 else :
  i1Ii11I1II = iiIIIII1i1iI . select ( "[COLOR %s]Select DB File to Purge[/COLOR]" % iIiIi11 , IIIiIi1iiI )
  if i1Ii11I1II == - 1 : wiz . LogNotify ( "[COLOR %s]Purge Database[/COLOR]" % oOOo0O00o , "[COLOR %s]Cancelled[/COLOR]" % iIiIi11 )
  else : wiz . purgeDb ( Oo0o0ooOoO [ I1IIIi ] )
  if 87 - 87: II111iiii % O0 - I1111 . i11IiIiiIIIII / I1I1i1 * iii11iiII
  if 26 - 26: OO00O0O0O00Oo . IiiIII111ii + ooOo . o0o0Oo0oooo0 + iii11iiII
  if 17 - 17: iii11iiII + i11iIiiIii + oO0 % iii11iiII . IIIi1i1I
  if 33 - 33: i11IiIiiIIIII * ooOo % o0o0Oo0oooo0 . i1Ii . OOoooooO . I1111
def o0oO0oo ( ) :
 oO0o00oOOooO0 = wiz . workingURL ( O0O0OOOOoo )
 if oO0o00oOOooO0 == True :
  try :
   id , i1i1I11i1I = wiz . splitNotify ( O0O0OOOOoo )
   if id == False : wiz . LogNotify ( "[COLOR %s]%s[/COLOR]" % ( oOOo0O00o , o0OOO ) , "[COLOR %s]Notification: Not Formated Correctly[/COLOR]" % iIiIi11 ) ; return
   notify . notification ( i1i1I11i1I , True )
  except Exception , O00OO :
   wiz . log ( "Error on Notifications Window: %s" % str ( O00OO ) , xbmc . LOGERROR )
 else : wiz . LogNotify ( "[COLOR %s]%s[/COLOR]" % ( oOOo0O00o , o0OOO ) , "[COLOR %s]Invalid URL for Notification[/COLOR]" % iIiIi11 )
 if 98 - 98: OoooooooOO - ooOo + OOoooooO
def O0I11IIIII ( ) :
 if O000oo0O == "" :
  notify . updateWindow ( )
 else :
  notify . updateWindow ( O000oo0O , oo0OooOOo0 , O00oO , wiz . checkBuild ( O000oo0O , 'icon' ) , wiz . checkBuild ( O000oo0O , 'fanart' ) )
  if 53 - 53: OoooooooOO . OoooooooOO + I1I1i1 - iiIIi1IiIi11 + iii11iiII
def i1111iIII ( ) :
 notify . firstRun ( )
 if 50 - 50: O0 * oO0 + II111iiii . i1IIi + o0o0Oo0oooo0
def ii11I11 ( ) :
 notify . firstRunSettings ( )
 if 75 - 75: Ooo0O
 if 23 - 23: II111iiii * iiIIi1IiIi11
 if 80 - 80: OO00O0O0O00Oo / i11iIiiIii + OoooooooOO
 if 38 - 38: oO0 % OOoooooO + i1IIi * OoooooooOO * IIIi1i1I
 if 83 - 83: iIii1I11I1II1 - OOoooooO - OO00O0O0O00Oo / I1111 - O0
def O00OoO0oo ( display , mode = None , name = None , url = None , menu = None , description = o0OOO , overwrite = True , fanart = OOO00 , icon = iiiiiIIii , themeit = None ) :
 Ii11iI1iI = sys . argv [ 0 ]
 if not mode == None : Ii11iI1iI += "?mode=%s" % urllib . quote_plus ( mode )
 if not name == None : Ii11iI1iI += "&name=" + urllib . quote_plus ( name )
 if not url == None : Ii11iI1iI += "&url=" + urllib . quote_plus ( url )
 o0oO = True
 if themeit : display = themeit % display
 I1Ii1IIIiII = xbmcgui . ListItem ( display , iconImage = "DefaultFolder.png" , thumbnailImage = icon )
 I1Ii1IIIiII . setInfo ( type = "Video" , infoLabels = { "Title" : display , "Plot" : description } )
 I1Ii1IIIiII . setProperty ( "Fanart_Image" , fanart )
 if not menu == None : I1Ii1IIIiII . addContextMenuItems ( menu , replaceItems = overwrite )
 o0oO = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = Ii11iI1iI , listitem = I1Ii1IIIiII , isFolder = True )
 return o0oO
 if 11 - 11: O0 * o0o0Oo0oooo0
def IIii1i ( name , url , mode , iconimage , fanart , description ) :
 if 69 - 69: OO00O0O0O00Oo / OoooooooOO % i11iIiiIii
 Ii11iI1iI = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart ) + "&description=" + urllib . quote_plus ( description )
 o0oO = True
 I1Ii1IIIiII = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 I1Ii1IIIiII . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description } )
 I1Ii1IIIiII . setProperty ( "Fanart_Image" , fanart )
 o0oO = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = Ii11iI1iI , listitem = I1Ii1IIIiII , isFolder = False )
 if 18 - 18: i11iIiiIii - OOoooooO * IIIi1i1I + I1I1i1
def oo00O00oO000o ( display , mode = None , name = None , url = None , menu = None , description = o0OOO , overwrite = True , fanart = OOO00 , icon = iiiiiIIii , themeit = None ) :
 Ii11iI1iI = sys . argv [ 0 ]
 if not mode == None : Ii11iI1iI += "?mode=%s" % urllib . quote_plus ( mode )
 if not name == None : Ii11iI1iI += "&name=" + urllib . quote_plus ( name )
 if not url == None : Ii11iI1iI += "&url=" + urllib . quote_plus ( url )
 o0oO = True
 if themeit : display = themeit % display
 I1Ii1IIIiII = xbmcgui . ListItem ( display , iconImage = "DefaultFolder.png" , thumbnailImage = icon )
 I1Ii1IIIiII . setInfo ( type = "Video" , infoLabels = { "Title" : display , "Plot" : description } )
 I1Ii1IIIiII . setProperty ( "Fanart_Image" , fanart )
 if not menu == None : I1Ii1IIIiII . addContextMenuItems ( menu , replaceItems = overwrite )
 o0oO = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = Ii11iI1iI , listitem = I1Ii1IIIiII , isFolder = True )
 return o0oO
 if 16 - 16: OoooooooOO * i11iIiiIii . OoooooooOO - iIii1I11I1II1 * i1IIi
def iiiii1II ( display , mode = None , name = None , url = None , menu = None , description = o0OOO , overwrite = True , fanart = OOO00 , icon = iiiiiIIii , themeit = None ) :
 Ii11iI1iI = sys . argv [ 0 ]
 if not mode == None : Ii11iI1iI += "?mode=%s" % urllib . quote_plus ( mode )
 if not name == None : Ii11iI1iI += "&name=" + urllib . quote_plus ( name )
 if not url == None : Ii11iI1iI += "&url=" + urllib . quote_plus ( url )
 o0oO = True
 if themeit : display = themeit % display
 I1Ii1IIIiII = xbmcgui . ListItem ( display , iconImage = "DefaultFolder.png" , thumbnailImage = icon )
 I1Ii1IIIiII . setInfo ( type = "Video" , infoLabels = { "Title" : display , "Plot" : description } )
 I1Ii1IIIiII . setProperty ( "Fanart_Image" , fanart )
 if not menu == None : I1Ii1IIIiII . addContextMenuItems ( menu , replaceItems = overwrite )
 o0oO = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = Ii11iI1iI , listitem = I1Ii1IIIiII , isFolder = False )
 return o0oO
 if 33 - 33: OO00O0O0O00Oo % II111iiii
def IIiI1I1 ( name , url , mode , iconimage ) :
 Ii11iI1iI = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage )
 o0oO = True
 I1Ii1IIIiII = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 I1Ii1IIIiII . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : name } )
 o0oO = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = Ii11iI1iI , listitem = I1Ii1IIIiII , isFolder = True )
 return o0oO
 if 49 - 49: oO0 + i11IiIiiIIIII / I1I1i1 + OoooooooOO + iii11iiII / i1Ii
def II1Iii ( name , url , mode , iconimage , fanart , description , installRating ) :
 Ii11iI1iI = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart ) + "&description=" + urllib . quote_plus ( description ) + "&installRating=" + urllib . quote_plus ( installRating )
 o0oO = True
 I1Ii1IIIiII = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 I1Ii1IIIiII . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description , "Premiered" : installRating } )
 I1Ii1IIIiII . setProperty ( "Fanart_Image" , fanart )
 o0oO = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = Ii11iI1iI , listitem = I1Ii1IIIiII , isFolder = False )
 return o0oO
 if 29 - 29: IiiIII111ii - IiiIII111ii / OOoooooO
def I11IIII ( display , mode = None , name = None , url = None , menu = None , description = o0OOO , overwrite = True , fanart = OOO00 , icon = iiiiiIIii , themeit = None ) :
 Ii11iI1iI = sys . argv [ 0 ]
 if not mode == None : Ii11iI1iI += "?mode=%s" % urllib . quote_plus ( mode )
 if not name == None : Ii11iI1iI += "&name=" + urllib . quote_plus ( name )
 if not url == None : Ii11iI1iI += "&url=" + urllib . quote_plus ( url )
 o0oO = True
 if themeit : display = themeit % display
 I1Ii1IIIiII = xbmcgui . ListItem ( display , iconImage = "DefaultFolder.png" , thumbnailImage = icon )
 I1Ii1IIIiII . setInfo ( type = "Video" , infoLabels = { "Title" : display , "Plot" : description } )
 I1Ii1IIIiII . setProperty ( "Fanart_Image" , fanart )
 if not menu == None : I1Ii1IIIiII . addContextMenuItems ( menu , replaceItems = overwrite )
 o0oO = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = Ii11iI1iI , listitem = I1Ii1IIIiII , isFolder = False )
 return o0oO
 if 38 - 38: OoooooooOO . I1I1i1 . II111iiii - iiIIi1IiIi11
def oOo0O ( display , mode , name = None , url = None , menu = None , overwrite = True , fanart = OOO00 , icon = iiiiiIIii , description = None , themeit = None ) :
 Ii11iI1iI = '%s?mode=%s' % ( sys . argv [ 0 ] , urllib . quote_plus ( mode ) )
 if not name == None : Ii11iI1iI += "&name=" + urllib . quote_plus ( name )
 if not url == None : Ii11iI1iI += "&url=" + urllib . quote_plus ( url )
 if not description == None : Ii11iI1iI += "&description=" + urllib . quote_plus ( description )
 o0oO = True
 if themeit : display = themeit % display
 I1Ii1IIIiII = xbmcgui . ListItem ( description , iconImage = "DefaultFolder.png" , thumbnailImage = icon )
 I1Ii1IIIiII . setInfo ( type = "Video" , infoLabels = { "Title" : description , "Plot" : o0OOO } )
 I1Ii1IIIiII . setProperty ( "Fanart_Image" , fanart )
 if not menu == None : I1Ii1IIIiII . addContextMenuItems ( menu , replaceItems = overwrite )
 o0oO = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = Ii11iI1iI , listitem = I1Ii1IIIiII , isFolder = False )
 return o0oO
 if 65 - 65: i11iIiiIii + ooOo / Ooo0O % iii11iiII . IiiIII111ii + iIii1I11I1II1
def iI11I ( name , url , mode , iconimage , fanart , description ) :
 Ii11iI1iI = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&fanart=" + urllib . quote_plus ( fanart )
 o0oO = True
 I1Ii1IIIiII = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 I1Ii1IIIiII . setInfo ( type = "Video" , infoLabels = { "Title" : name } )
 I1Ii1IIIiII . setProperty ( "Fanart_Image" , fanart )
 o0oO = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = Ii11iI1iI , listitem = I1Ii1IIIiII , isFolder = False )
 return o0oO
 if 39 - 39: iIii1I11I1II1 - IIIi1i1I / i1Ii * O0
def oooo0O0Oooo ( name , url , mode , iconimage , fanart , description ) :
 if 39 - 39: IIIi1i1I / OOoooooO * II111iiii * iiIIi1IiIi11
 Ii11iI1iI = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart ) + "&description=" + urllib . quote_plus ( description )
 o0oO = True
 I1Ii1IIIiII = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 I1Ii1IIIiII . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description } )
 I1Ii1IIIiII . setProperty ( "Fanart_Image" , fanart )
 o0oO = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = Ii11iI1iI , listitem = I1Ii1IIIiII , isFolder = True )
 return o0oO
 if 41 - 41: i11iIiiIii * O0 - iiIIi1IiIi11 . II111iiii % I1111 % oO0
 if 32 - 32: iii11iiII + iiIIi1IiIi11 + iIii1I11I1II1 * Ooo0O
 if 62 - 62: i11iIiiIii
def i1Iii ( name , url , mode , iconimage , fanart , description ) :
 Ii11iI1iI = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart ) + "&description=" + urllib . quote_plus ( description )
 o0oO = True
 I1Ii1IIIiII = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 I1Ii1IIIiII . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description } )
 I1Ii1IIIiII . setProperty ( "Fanart_Image" , fanart )
 if mode == 90 :
  o0oO = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = Ii11iI1iI , listitem = I1Ii1IIIiII , isFolder = False )
 else :
  o0oO = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = Ii11iI1iI , listitem = I1Ii1IIIiII , isFolder = True )
 return o0oO
 if 91 - 91: OOoooooO * i1Ii * II111iiii
def oooO0oooOo000 ( ) :
 ooOOO0o = [ ]
 oooO0 = sys . argv [ 2 ]
 if len ( oooO0 ) >= 2 :
  Oo0o = sys . argv [ 2 ]
  iiiiII11iIi = Oo0o . replace ( '?' , '' )
  if ( Oo0o [ len ( Oo0o ) - 1 ] == '/' ) :
   Oo0o = Oo0o [ 0 : len ( Oo0o ) - 2 ]
  OO00 = iiiiII11iIi . split ( '&' )
  ooOOO0o = { }
  for i11ii1Ii1 in range ( len ( OO00 ) ) :
   Oooo = { }
   Oooo = OO00 [ i11ii1Ii1 ] . split ( '=' )
   if ( len ( Oooo ) ) == 2 :
    ooOOO0o [ Oooo [ 0 ] ] = Oooo [ 1 ]
    if 87 - 87: i1Ii . i1IIi % OoooooooOO * i11iIiiIii
  return ooOOO0o
  if 67 - 67: OO00O0O0O00Oo / I1111 . OoooooooOO
Oo0o = oooO0oooOo000 ( )
oO0o00oOOooO0 = None
O0Oo0o000oO = None
OoIIiIIIII1I = None
iii1III1i = None
i1i1i1I = None
OooOo00o = None
ooiiI = None
if 72 - 72: i11IiIiiIIIII . II111iiii * i1IIi
try :
 ooiiI = int ( Oo0o [ "fav_mode" ] )
except :
 pass
try : OoIIiIIIII1I = urllib . unquote_plus ( Oo0o [ "mode" ] )
except : pass
try : O0Oo0o000oO = urllib . unquote_plus ( Oo0o [ "name" ] )
except : pass
try : oO0o00oOOooO0 = urllib . unquote_plus ( Oo0o [ "url" ] )
except : pass
try : iii1III1i = urllib . unquote_plus ( Oo0o [ "iconimage" ] )
except : pass
try : i1i1i1I = urllib . unquote_plus ( Oo0o [ "fanart" ] )
except : pass
try : OooOo00o = urllib . unquote_plus ( Oo0o [ "description" ] )
except : pass
if 79 - 79: oO0 / O0 % I1I1i1
print str ( i1111 ) + ': ' + str ( O0oo0OO0 )
print "Mode: " + str ( OoIIiIIIII1I )
print "URL: " + str ( oO0o00oOOooO0 )
print "Name: " + str ( O0Oo0o000oO )
print "IconImage: " + str ( iii1III1i )
if 71 - 71: OO00O0O0O00Oo / ooOo / O0
wiz . log ( '[ Version : \'%s\' ] [ Mode : \'%s\' ] [ Name : \'%s\' ] [ Url : \'%s\' ]' % ( O0oo0OO0 , OoIIiIIIII1I if not OoIIiIIIII1I == '' else None , O0Oo0o000oO , oO0o00oOOooO0 ) )
if 19 - 19: i11iIiiIii . ooOo + II111iiii / iii11iiII . oO0 * OOoooooO
def oo0O ( ) :
 if 100 - 100: OoooooooOO - O0 . i11IiIiiIIIII / i11IiIiiIIIII + II111iiii * o0o0Oo0oooo0
 for file in os . listdir ( Ii11iii11I ) :
  if file . endswith ( ".zip" ) :
   oO0o00oOOooO0 = xbmc . translatePath ( os . path . join ( Ii11iii11I , file ) )
   iI11I ( file , oO0o00oOOooO0 , 'read' , iiiiiIIii , iiiiiIIii , '' )
   if 37 - 37: Ooo0O
def O00Oo00o00O ( ) :
 i11IoO0000O0Oo00O = xbmc . translatePath ( os . path . join ( 'special://' , 'home' ) )
 for file in os . listdir ( Ii11iii11I ) :
  if file . endswith ( ".zip" ) :
   oO0o00oOOooO0 = xbmc . translatePath ( os . path . join ( Ii11iii11I , file ) )
   i1Iii ( file , oO0o00oOOooO0 , 'dell' , iiiiiIIii , iiiiiIIii , '' )
   if 42 - 42: i11iIiiIii / ooOo - I1111 - OOoooooO + II111iiii % OOoooooO
def iIi1 ( content , viewType ) :
 if 50 - 50: OoooooooOO + IIIi1i1I * ooOo - IiiIII111ii / i11iIiiIii
 if content :
  xbmcplugin . setContent ( int ( sys . argv [ 1 ] ) , content )
 if ADDON . getSetting ( 'auto-view' ) == 'true' :
  xbmc . executebuiltin ( "Container.SetViewMode(%s)" % ADDON . getSetting ( viewType ) )
  if 5 - 5: O0 - ooOo
  if 44 - 44: II111iiii . II111iiii + iii11iiII * IiiIII111ii
  if 16 - 16: II111iiii
  if 100 - 100: O0 - i1IIi
  if 48 - 48: IIIi1i1I % OOoooooO + O0
  if 27 - 27: oO0 / iii11iiII
  if 33 - 33: OoooooooOO % oO0 . O0 / oO0
def iIi1 ( content , viewType ) :
 if wiz . getS ( 'auto-view' ) == 'true' :
  O0OoOo = wiz . getS ( viewType )
  if O0OoOo == '50' and o0OIiII >= 17 and I1IIiiIiii == 'skin.estuary' : O0OoOo = '55'
  if O0OoOo == '500' and o0OIiII >= 17 and I1IIiiIiii == 'skin.estuary' : O0OoOo = '50'
  wiz . ebi ( "Container.SetViewMode(%s)" % O0OoOo )
  if 94 - 94: I1111 + I1111 + oO0 . I1111 * IiiIII111ii
if OoIIiIIIII1I == None : i1iiIiI1Ii1i ( )
if 62 - 62: I1I1i1 / iIii1I11I1II1
elif OoIIiIIIII1I == 'wizardupdate' : wiz . wizardUpdate ( )
elif OoIIiIIIII1I == 'builds' : OoO00 ( )
elif OoIIiIIIII1I == 'viewbuild' : IiI11i1IIiiI ( O0Oo0o000oO )
elif OoIIiIIIII1I == 'buildinfo' : o0O00OooooO ( O0Oo0o000oO )
elif OoIIiIIIII1I == 'buildpreview' : I111 ( O0Oo0o000oO )
elif OoIIiIIIII1I == 'install' : Oooooooo00o00 ( O0Oo0o000oO , oO0o00oOOooO0 )
elif OoIIiIIIII1I == 'theme' : Oooooooo00o00 ( O0Oo0o000oO , OoIIiIIIII1I , oO0o00oOOooO0 )
elif OoIIiIIIII1I == 'viewthirdparty' : oo0OOo0O ( O0Oo0o000oO )
elif OoIIiIIIII1I == 'installthird' : I1i1I11111iI1 ( O0Oo0o000oO , oO0o00oOOooO0 )
elif OoIIiIIIII1I == 'editthird' : iiIi ( O0Oo0o000oO ) ; wiz . refresh ( )
if 55 - 55: IiiIII111ii / I1111 + iiIIi1IiIi11 . i1Ii
elif OoIIiIIIII1I == 'pro' : Main_Menu ( )
if 47 - 47: O0
elif OoIIiIIIII1I == 'maint' : IIiI1Ii1IIiI11i1 ( O0Oo0o000oO )
elif OoIIiIIIII1I == 'speed' : oOO0OO0OO ( )
elif OoIIiIIIII1I == 'kodi17fix' : wiz . kodi17Fix ( )
elif OoIIiIIIII1I == 'advancedsetting' : i1i1II1I ( O0Oo0o000oO )
elif OoIIiIIIII1I == 'autoadvanced' : ii1iII1iI111 ( ) ; wiz . refresh ( )
elif OoIIiIIIII1I == 'removeadvanced' : i1I111i1ii ( ) ; wiz . refresh ( )
elif OoIIiIIIII1I == 'asciicheck' : wiz . asciiCheck ( )
elif OoIIiIIIII1I == 'backupbuild' : wiz . backUpOptions ( 'build' )
elif OoIIiIIIII1I == 'backupgui' : wiz . backUpOptions ( 'guifix' )
elif OoIIiIIIII1I == 'backuptheme' : wiz . backUpOptions ( 'theme' )
elif OoIIiIIIII1I == 'backupaddon' : wiz . backUpOptions ( 'addondata' )
elif OoIIiIIIII1I == 'oldThumbs' : wiz . oldThumbs ( )
elif OoIIiIIIII1I == 'clearbackup' : wiz . cleanupBackup ( )
elif OoIIiIIIII1I == 'convertpath' : wiz . convertSpecial ( o00 )
elif OoIIiIIIII1I == 'currentsettings' : i1II ( )
elif OoIIiIIIII1I == 'fullclean' : i1i111I ( ) ; wiz . refresh ( )
elif OoIIiIIIII1I == 'clearcache' : Ooo0oOOoo0O ( ) ; wiz . refresh ( )
elif OoIIiIIIII1I == 'clearpackages' : wiz . clearPackages ( ) ; wiz . refresh ( )
elif OoIIiIIIII1I == 'clearcrash' : wiz . clearCrash ( ) ; wiz . refresh ( )
elif OoIIiIIIII1I == 'clearthumb' : oO0O0O0OO0O00 ( ) ; wiz . refresh ( )
elif OoIIiIIIII1I == 'checksources' : wiz . checkSources ( ) ; wiz . refresh ( )
elif OoIIiIIIII1I == 'checkrepos' : wiz . checkRepos ( ) ; wiz . refresh ( )
elif OoIIiIIIII1I == 'freshstart' : IiI ( )
elif OoIIiIIIII1I == 'forceupdate' : wiz . forceUpdate ( )
elif OoIIiIIIII1I == 'forceprofile' : wiz . reloadProfile ( wiz . getInfo ( 'System.ProfileName' ) )
elif OoIIiIIIII1I == 'forceclose' : wiz . killxbmc ( )
elif OoIIiIIIII1I == 'forceskin' : wiz . ebi ( "ReloadSkin()" ) ; wiz . refresh ( )
elif OoIIiIIIII1I == 'hidepassword' : wiz . hidePassword ( )
elif OoIIiIIIII1I == 'unhidepassword' : wiz . unhidePassword ( )
elif OoIIiIIIII1I == 'enableaddons' : o0o0oo0Ooo ( )
elif OoIIiIIIII1I == 'toggleaddon' : wiz . toggleAddon ( O0Oo0o000oO , oO0o00oOOooO0 ) ; wiz . refresh ( )
elif OoIIiIIIII1I == 'togglecache' : iiiI11 ( O0Oo0o000oO ) ; wiz . refresh ( )
elif OoIIiIIIII1I == 'toggleadult' : wiz . toggleAdult ( ) ; wiz . refresh ( )
elif OoIIiIIIII1I == 'changefeq' : I1i1ii ( ) ; wiz . refresh ( )
elif OoIIiIIIII1I == 'uploadlog' : uploadLog . Main ( )
elif OoIIiIIIII1I == 'viewlog' : ii111iI1i1 ( )
elif OoIIiIIIII1I == 'viewwizlog' : ii111iI1i1 ( I11iii1Ii )
elif OoIIiIIIII1I == 'viewerrorlog' : oo0ooooo00o ( all = True )
elif OoIIiIIIII1I == 'clearwizlog' : IIi1i = open ( I11iii1Ii , 'w' ) ; IIi1i . close ( ) ; wiz . LogNotify ( "[COLOR %s]%s[/COLOR]" % ( oOOo0O00o , o0OOO ) , "[COLOR %s]Wizard Log Cleared![/COLOR]" % iIiIi11 )
elif OoIIiIIIII1I == 'purgedb' : O0Oo00 ( )
elif OoIIiIIIII1I == 'fixaddonupdate' : O0Oo0iIIIi1IiI11I1 ( )
elif OoIIiIIIII1I == 'removeaddons' : i1IiI ( )
elif OoIIiIIIII1I == 'removeaddon' : IIIiiiIiI ( O0Oo0o000oO )
elif OoIIiIIIII1I == 'removeaddondata' : i11i11i ( )
elif OoIIiIIIII1I == 'removedata' : i1II1Ii1i1 ( O0Oo0o000oO )
elif OoIIiIIIII1I == 'resetaddon' : O0oOoo0o000O0 = wiz . cleanHouse ( o0 , ignore = True ) ; wiz . LogNotify ( "[COLOR %s]%s[/COLOR]" % ( oOOo0O00o , o0OOO ) , "[COLOR %s]Addon_Data reset[/COLOR]" % iIiIi11 )
elif OoIIiIIIII1I == 'systeminfo' : iiI1I ( )
elif OoIIiIIIII1I == 'restorezip' : IiIIIiI ( 'build' )
elif OoIIiIIIII1I == 'restoregui' : IiIIIiI ( 'gui' )
elif OoIIiIIIII1I == 'restoreaddon' : IiIIIiI ( 'addondata' )
elif OoIIiIIIII1I == 'restoreextzip' : i11iiI ( 'build' )
elif OoIIiIIIII1I == 'restoreextgui' : i11iiI ( 'gui' )
elif OoIIiIIIII1I == 'restoreextaddon' : i11iiI ( 'addondata' )
elif OoIIiIIIII1I == 'writeadvanced' : iIi1IIiIII1 ( O0Oo0o000oO , oO0o00oOOooO0 )
if 83 - 83: O0 + o0o0Oo0oooo0 / O0 / i11IiIiiIIIII
elif OoIIiIIIII1I == 'apk1' : o0OoO000O ( )
elif OoIIiIIIII1I == 'apkgame' : II1 ( oO0o00oOOooO0 )
elif OoIIiIIIII1I == 'select' : ii ( oO0o00oOOooO0 )
elif OoIIiIIIII1I == 'grab' : oooOO0OO0O ( O0Oo0o000oO , oO0o00oOOooO0 )
elif OoIIiIIIII1I == 'rom' : OOO0o0OO0OO ( oO0o00oOOooO0 )
elif OoIIiIIIII1I == 'apkscrape1' : APK ( )
elif OoIIiIIIII1I == 'apkscrape' : ooO0oO00O0o ( O0Oo0o000oO )
elif OoIIiIIIII1I == 'apkshow' : Oo00OOOOoo0oo ( oO0o00oOOooO0 )
elif OoIIiIIIII1I == 'intellaunch' : Oo0OooO0 ( )
elif OoIIiIIIII1I == 'intelselect' : iIiiIiiIi ( O0Oo0o000oO , oO0o00oOOooO0 , iii1III1i , i1i1i1I , OooOo00o )
elif OoIIiIIIII1I == 'emurom' : o0oo0000 ( )
elif OoIIiIIIII1I == 'roms' : IiI1i111IiIiIi1 ( )
elif OoIIiIIIII1I == 'snes' : I1Ii ( )
elif OoIIiIIIII1I == 'nes' : ooOo0O0O0oOO0 ( )
elif OoIIiIIIII1I == 'gen' : I11oOOooo ( )
elif OoIIiIIIII1I == 'atr' : iIiI1i ( )
elif OoIIiIIIII1I == 'n64' : iiIii ( )
elif OoIIiIIIII1I == 'tbg' : O000O ( )
elif OoIIiIIIII1I == 'nds' : I1I1IiIi1 ( )
elif OoIIiIIIII1I == 'ps' : I1iI ( )
elif OoIIiIIIII1I == 'apkinstall' : o00o ( O0Oo0o000oO , oO0o00oOOooO0 , "None" )
elif OoIIiIIIII1I == 'rominstall' : o00OOOOOo0OOo ( O0Oo0o000oO , oO0o00oOOooO0 , )
if 68 - 68: i1IIi . i11IiIiiIIIII . i1IIi + i1Ii % ooOo
elif OoIIiIIIII1I == 'youtube' : iIii1I ( O0Oo0o000oO )
elif OoIIiIIIII1I == 'viewVideo' : iIiIiI1i111i ( oO0o00oOOooO0 )
if 32 - 32: o0o0Oo0oooo0 . iIii1I11I1II1 % IIIi1i1I . O0 . o0o0Oo0oooo0 / iiIIi1IiIi11
elif OoIIiIIIII1I == 'addons' : i1iIIi1 ( O0Oo0o000oO )
elif OoIIiIIIII1I == 'addoninstall' : IIiiI1iii1i ( O0Oo0o000oO , oO0o00oOOooO0 )
if 45 - 45: iIii1I11I1II1
elif OoIIiIIIII1I == 'savedata' : iIII11Iiii1 ( )
elif OoIIiIIIII1I == 'togglesetting' : wiz . setS ( O0Oo0o000oO , 'false' if wiz . getS ( O0Oo0o000oO ) == 'true' else 'true' ) ; wiz . refresh ( )
elif OoIIiIIIII1I == 'managedata' : ooO0o0oO0 ( O0Oo0o000oO )
elif OoIIiIIIII1I == 'whitelist' : wiz . whiteList ( O0Oo0o000oO )
if 41 - 41: iiIIi1IiIi11 % iiIIi1IiIi11 - i1Ii % I1111 - OoooooooOO - iiIIi1IiIi11
elif OoIIiIIIII1I == 'trakt' : o0oo0o00ooO00 ( )
elif OoIIiIIIII1I == 'savetrakt' : traktit . traktIt ( 'update' , O0Oo0o000oO )
elif OoIIiIIIII1I == 'restoretrakt' : traktit . traktIt ( 'restore' , O0Oo0o000oO )
elif OoIIiIIIII1I == 'addontrakt' : traktit . traktIt ( 'clearaddon' , O0Oo0o000oO )
elif OoIIiIIIII1I == 'cleartrakt' : traktit . clearSaved ( O0Oo0o000oO )
elif OoIIiIIIII1I == 'authtrakt' : traktit . activateTrakt ( O0Oo0o000oO ) ; wiz . refresh ( )
elif OoIIiIIIII1I == 'updatetrakt' : traktit . autoUpdate ( 'all' )
elif OoIIiIIIII1I == 'importtrakt' : traktit . importlist ( O0Oo0o000oO ) ; wiz . refresh ( )
if 66 - 66: I1I1i1 % o0o0Oo0oooo0
elif OoIIiIIIII1I == 'realdebrid' : iiIIiiIi ( )
elif OoIIiIIIII1I == 'savedebrid' : debridit . debridIt ( 'update' , O0Oo0o000oO )
elif OoIIiIIIII1I == 'restoredebrid' : debridit . debridIt ( 'restore' , O0Oo0o000oO )
elif OoIIiIIIII1I == 'addondebrid' : debridit . debridIt ( 'clearaddon' , O0Oo0o000oO )
elif OoIIiIIIII1I == 'cleardebrid' : debridit . clearSaved ( O0Oo0o000oO )
elif OoIIiIIIII1I == 'authdebrid' : debridit . activateDebrid ( O0Oo0o000oO ) ; wiz . refresh ( )
elif OoIIiIIIII1I == 'updatedebrid' : debridit . autoUpdate ( 'all' )
elif OoIIiIIIII1I == 'importdebrid' : debridit . importlist ( O0Oo0o000oO ) ; wiz . refresh ( )
if 30 - 30: o0o0Oo0oooo0 * Ooo0O % iIii1I11I1II1 % I1111 + i11iIiiIii
elif OoIIiIIIII1I == 'login' : I11II1 ( )
elif OoIIiIIIII1I == 'savelogin' : loginit . loginIt ( 'update' , O0Oo0o000oO )
elif OoIIiIIIII1I == 'restorelogin' : loginit . loginIt ( 'restore' , O0Oo0o000oO )
elif OoIIiIIIII1I == 'addonlogin' : loginit . loginIt ( 'clearaddon' , O0Oo0o000oO )
elif OoIIiIIIII1I == 'clearlogin' : loginit . clearSaved ( O0Oo0o000oO )
elif OoIIiIIIII1I == 'authlogin' : loginit . activateLogin ( O0Oo0o000oO ) ; wiz . refresh ( )
elif OoIIiIIIII1I == 'updatelogin' : loginit . autoUpdate ( 'all' )
elif OoIIiIIIII1I == 'importlogin' : loginit . importlist ( O0Oo0o000oO ) ; wiz . refresh ( )
if 46 - 46: ooOo . i1Ii - i11iIiiIii - OO00O0O0O00Oo
elif OoIIiIIIII1I == 'contact' : notify . contact ( oOO0O00Oo0O0o )
elif OoIIiIIIII1I == 'settings' : wiz . openS ( O0Oo0o000oO ) ; wiz . refresh ( )
elif OoIIiIIIII1I == 'opensettings' : id = eval ( oO0o00oOOooO0 . upper ( ) + 'ID' ) [ O0Oo0o000oO ] [ 'plugin' ] ; oo0O0OO0Oo = wiz . addonId ( id ) ; oo0O0OO0Oo . openSettings ( ) ; wiz . refresh ( )
if 66 - 66: ooOo % IiiIII111ii % II111iiii
elif OoIIiIIIII1I == 'developer' : Oo000 ( )
elif OoIIiIIIII1I == 'converttext' : wiz . convertText ( )
elif OoIIiIIIII1I == 'createqr' : wiz . createQR ( )
elif OoIIiIIIII1I == 'testnotify' : o0oO0oo ( )
elif OoIIiIIIII1I == 'testupdate' : O0I11IIIII ( )
elif OoIIiIIIII1I == 'testfirst' : i1111iIII ( )
elif OoIIiIIIII1I == 'testfirstrun' : ii11I11 ( )
elif OoIIiIIIII1I == 'testapk' : notify . apkInstaller ( 'SPMC' )
if 77 - 77: OO00O0O0O00Oo + IIIi1i1I
elif OoIIiIIIII1I == 'guide' : TvGuide ( )
if 38 - 38: oO0 - IiiIII111ii * I1I1i1
elif OoIIiIIIII1I == 'recreateaddon' : ReCreate_Addon_ini ( )
elif OoIIiIIIII1I == 'getlistplay' : Get_List_playlinks ( O0Oo0o000oO )
elif OoIIiIIIII1I == 'resolve' : RESOLVER ( oO0o00oOOooO0 )
elif OoIIiIIIII1I == 'streams' : Streams_Menu ( )
elif OoIIiIIIII1I == 'liveevent' : Live_Events ( O0Oo0o000oO )
elif OoIIiIIIII1I == 'addonopen' : I1ii11iIi11i . openSettings ( sys . argv [ 0 ] )
xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
# dd678faae9ac167bc83abf78e5cb2f3f0688d3a3
