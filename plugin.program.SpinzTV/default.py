import xbmc , xbmcaddon , xbmcgui , xbmcplugin , os , sys , xbmcvfs , glob
import shutil
import urllib2 , urllib
import re
import uservar
import fnmatch
import speedtest
import backuprestore
import plugintools
import base64
import time
import platform , subprocess
import zipfile
try : from sqlite3 import dbapi2 as database
except : from pysqlite2 import dbapi2 as database
from datetime import date , datetime , timedelta
from resources . libs import extract , downloader , notify , debridit , traktit , skinSwitch , uploadLog , wizard as wiz
if 64 - 64: i11iIiiIii
OO0o = uservar . ADDON_ID
Oo0Ooo = uservar . ADDONTITLE
O0O0OO0O0O0 = wiz . addonId ( OO0o )
iiiii = wiz . addonInfo ( OO0o , 'version' )
ooo0OO = xbmcgui . Dialog ( )
II1 = xbmcgui . DialogProgress ( )
O00ooooo00 = xbmc . translatePath ( 'special://home/' )
I1IiiI = xbmc . translatePath ( os . path . join ( '//storage//emulated//0//Download' , '' ) )
IIi1IiiiI1Ii = xbmc . translatePath ( 'special://logpath/' )
I11i11Ii = xbmc . translatePath ( 'special://profile/' )
zip = plugintools . get_setting ( "zip" )
oO00oOo = xbmc . translatePath ( os . path . join ( zip ) )
OOOo0 = os . path . join ( O00ooooo00 , 'addons' )
Oooo000o = os . path . join ( O00ooooo00 , 'userdata' )
IiIi11iIIi1Ii = os . path . join ( OOOo0 , OO0o )
Oo0O = os . path . join ( OOOo0 , 'packages' )
IiI = os . path . join ( Oooo000o , 'addon_data' )
ooOo = os . path . join ( Oooo000o , 'addon_data' , OO0o )
Oo = os . path . join ( Oooo000o , 'advancedsettings.xml' )
o0O = os . path . join ( Oooo000o , 'sources.xml' )
IiiIII111iI = os . path . join ( Oooo000o , 'favourites.xml' )
IiII = os . path . join ( Oooo000o , 'profiles.xml' )
iI1Ii11111iIi = os . path . join ( Oooo000o , 'guisettings.xml' )
i1i1II = os . path . join ( Oooo000o , 'Thumbnails' )
O0oo0OO0 = os . path . join ( Oooo000o , 'Database' )
I1i1iiI1 = os . path . join ( IiIi11iIIi1Ii , 'fanart.jpg' )
iiIIIII1i1iI = os . path . join ( IiIi11iIIi1Ii , 'icon.png' )
o0oO0 = os . path . join ( IiIi11iIIi1Ii , 'resources' , 'art' )
oo00 = os . path . join ( ooOo , 'wizard.log' )
o00 = xbmc . getSkinDir ( )
Oo0oO0ooo = wiz . getS ( 'buildname' )
o0oOoO00o = wiz . getS ( 'buildversion' )
i1 = wiz . getS ( 'buildtheme' )
oOOoo00O0O = wiz . getS ( 'latestversion' )
i1111 = wiz . getS ( 'show15' )
i11 = wiz . getS ( 'show16' )
I11 = wiz . getS ( 'autoclean' )
Oo0o0000o0o0 = wiz . getS ( 'clearcache' )
oOo0oooo00o = wiz . getS ( 'clearpackages' )
oO0o0o0ooO0oO = wiz . getS ( 'seperate' )
oo0o0O00 = wiz . getS ( 'notify' )
oO = wiz . getS ( 'noteid' )
i1iiIIiiI111 = wiz . getS ( 'notedismiss' )
oooOOOOO = wiz . getS ( 'traktlastsave' )
i1iiIII111ii = wiz . getS ( 'debridlastsave' )
i1iIIi1 = wiz . getS ( 'keepfavourites' )
ii11iIi1I = wiz . getS ( 'keepgui' )
iI111I11I1I1 = wiz . getS ( 'keepsources' )
OOooO0OOoo = wiz . getS ( 'keepprofiles' )
iIii1 = wiz . getS ( 'keepadvanced' )
oOOoO0 = wiz . getS ( 'keeptrakt' )
O0OoO000O0OO = wiz . getS ( 'keepdebrid' )
iiI1IiI = wiz . getS ( 'exodus' )
II = wiz . getS ( 'salts' )
ooOoOoo0O = wiz . getS ( 'saltshd' )
OooO0 = wiz . getS ( 'royalwe' )
II11iiii1Ii = wiz . getS ( 'velocity' )
OO0oOoo = wiz . getS ( 'velocitykids' )
O0o0Oo = wiz . getS ( 'specto' )
Oo00OOOOO = wiz . getS ( 'trakt' )
O0O = wiz . getS ( 'realexodus' )
O00o0OO = wiz . getS ( 'realspecto' )
I11i1 = wiz . getS ( 'urlresolver' )
iIi1ii1I1 = wiz . getS ( 'developer' )
o0 = date . today ( )
I11II1i = o0 + timedelta ( days = 1 )
IIIII = o0 + timedelta ( days = 3 )
ooooooO0oo = float ( xbmc . getInfoLabel ( "System.BuildVersion" ) [ : 4 ] )
IIiiiiiiIi1I1 = 'plugin.video.exodus'
I1IIIii = 'plugin.video.velocity'
oOoOooOo0o0 = 'plugin.video.velocitykids'
OOOO = 'plugin.video.salts'
OOO00 = 'plugin.video.saltshd.lite'
iiiiiIIii = 'plugin.video.theroyalwe'
O000OO0 = 'plugin.video.specto'
I11iii1Ii = 'script.trakt'
I1IIiiIiii = 'script.module.urlresolver'
O000oo0O = os . path . join ( OOOo0 , OOOO )
OOOOi11i1 = os . path . join ( OOOo0 , OOO00 )
IIIii1II1II = os . path . join ( OOOo0 , IIiiiiiiIi1I1 )
i1I1iI = os . path . join ( OOOo0 , I1IIIii )
oo0OooOOo0 = os . path . join ( OOOo0 , oOoOooOo0o0 )
o0OO00oO = os . path . join ( OOOo0 , iiiiiIIii )
I11i1I1I = os . path . join ( OOOo0 , O000OO0 )
oO0Oo = os . path . join ( OOOo0 , I11iii1Ii )
oOOoo0Oo = os . path . join ( OOOo0 , I1IIiiIiii )
o00OO00OoO = uservar . EXCLUDES
OOOO0OOoO0O0 = uservar . BUILDFILE
O0Oo000ooO00 = uservar . APKSPINZFILE
oO0 = uservar . APKFILE
Ii1iIiII1ii1 = uservar . APKVIDFILE
ooOooo000oOO = uservar . APKSYSFILE
Oo0oOOo = uservar . SPEEDFILE
Oo0OoO00oOO0o = uservar . SNESFILE
OOO00O = uservar . SNESAFILE
OOoOO0oo0ooO = uservar . SNESCFILE
O0o0O00Oo0o0 = uservar . SNESFFILE
O00O0oOO00O00 = uservar . SNESIFILE
i1Oo00 = uservar . SNESLFILE
i1i = uservar . SNESNFILE
iiI111I1iIiI = uservar . SNESPFILE
IIIi1I1IIii1II = uservar . SNESSFILE
O0 = uservar . SNESTFILE
ii1ii1ii = uservar . SNESWFILE
oooooOoo0ooo = uservar . EMUFILE
I1I1IiI1 = uservar . NESAFILE
III1iII1I1ii = uservar . NESCFILE
oOOo0 = uservar . NESDFILE
oo00O00oO = uservar . NESFFILE
iIiIIIi = uservar . NESHFILE
ooo00OOOooO = uservar . NESLFILE
O00OOOoOoo0O = uservar . NESNFILE
O000OOo00oo = uservar . NESRFILE
oo0OOo = uservar . NESTFILE
ooOOO00Ooo = uservar . NESWFILE
IiIIIi1iIi = uservar . GENAFILE
ooOOoooooo = uservar . GENCFILE
II1I = uservar . GENEFILE
O0i1II1Iiii1I11 = uservar . GENHFILE
IIII = uservar . GENMFILE
iiIiI = uservar . GENPFILE
o00oooO0Oo = uservar . GENSFILE
o0O0OOO0Ooo = uservar . GENUFILE
iiIiII1 = uservar . ATRAFILE
OOO00O0O = uservar . ATRCFILE
iii = uservar . ATREFILE
oOooOOOoOo = uservar . ATRHFILE
i1Iii1i1I = uservar . ATRMFILE
OOoO00 = uservar . ATRPFILE
IiI111111IIII = uservar . ATRSFILE
i1Ii = uservar . ATRVFILE
ii111iI1iIi1 = uservar . N64FILE
OOO = uservar . N64AFILE
oo0OOo0 = uservar . N64CFILE
I11IiI = uservar . N64FFILE
O0ooO0Oo00o = uservar . N64KFILE
ooO0oOOooOo0 = uservar . N64NFILE
i1I1ii11i1Iii = uservar . N64SFILE
I1IiiiiI = uservar . N64VFILE
o0OIiII = uservar . TGAFILE
ii1iII1II = uservar . TGCFILE
Iii1I1I11iiI1 = uservar . TGFFILE
I1I1i1I = uservar . TGJFILE
ii1I = uservar . TGNFILE
O0oO0 = uservar . TGRFILE
oO0O0OO0O = uservar . TGVFILE
OO = uservar . NDSAFILE
OoOoO = uservar . NDSBFILE
Ii1I1i = uservar . NDSCFILE
OOI1iI1ii1II = uservar . NDSDFILE
O0O0OOOOoo = uservar . NDSEFILE
oOooO0 = uservar . NDSGFILE
Ii1I1Ii = uservar . NDSIFILE
OOoO0 = uservar . NDSKFILE
OO0Oooo0oOO0O = uservar . NDSMFILE
o00O0 = uservar . NDSNFILE
oOO0O00Oo0O0o = uservar . NDSPFILE
ii1 = uservar . NDSRFILE
I1iIIiiIIi1i = uservar . NDSSFILE
O0O0ooOOO = uservar . NDSTFILE
oOOo0O00o = uservar . NDSVFILE
iIiIi11 = wiz . workingURL ( oooooOoo0ooo )
OOOiiiiI = wiz . workingURL ( Oo0OoO00oOO0o )
oooOo0OOOoo0 = wiz . workingURL ( OOO00O )
OOoO = wiz . workingURL ( OOoOO0oo0ooO )
OO0O000 = wiz . workingURL ( O0o0O00Oo0o0 )
iiIiI1i1 = wiz . workingURL ( O00O0oOO00O00 )
oO0O00oOOoooO = wiz . workingURL ( i1Oo00 )
IiIi11iI = wiz . workingURL ( i1i )
Oo0O00O000 = wiz . workingURL ( iiI111I1iIiI )
i11I1IiII1i1i = wiz . workingURL ( IIIi1I1IIii1II )
oo = wiz . workingURL ( O0 )
I1111i = wiz . workingURL ( ii1ii1ii )
iIIii = wiz . workingURL ( I1I1IiI1 )
o00O0O = wiz . workingURL ( III1iII1I1ii )
ii1iii1i = wiz . workingURL ( oOOo0 )
Iii1I1111ii = wiz . workingURL ( oo00O00oO )
ooOoO00 = wiz . workingURL ( iIiIIIi )
Ii1IIiI1i = wiz . workingURL ( ooo00OOOooO )
o0O00Oo0 = wiz . workingURL ( O00OOOoOoo0O )
IiII111i1i11 = wiz . workingURL ( O000OOo00oo )
i111iIi1i1II1 = wiz . workingURL ( oo0OOo )
oooO = wiz . workingURL ( ooOOO00Ooo )
i1I1i111Ii = wiz . workingURL ( IiIIIi1iIi )
ooo = wiz . workingURL ( ooOOoooooo )
i1i1iI1iiiI = wiz . workingURL ( II1I )
Ooo0oOooo0 = wiz . workingURL ( O0i1II1Iiii1I11 )
oOOOoo00 = wiz . workingURL ( IIII )
iiIiIIIiiI = wiz . workingURL ( iiIiI )
iiI1IIIi = wiz . workingURL ( o00oooO0Oo )
II11IiIi11 = wiz . workingURL ( o0O0OOO0Ooo )
IIOOO0O00O0OOOO = wiz . workingURL ( iiIiII1 )
I1iiii1I = wiz . workingURL ( OOO00O0O )
OOo0 = wiz . workingURL ( iii )
oO00ooooO0o = wiz . workingURL ( oOooOOOoOo )
oo0o = wiz . workingURL ( i1Iii1i1I )
o0oO0oooOoo = wiz . workingURL ( OOoO00 )
I1III1111iIi = wiz . workingURL ( IiI111111IIII )
I1i111I = wiz . workingURL ( i1Ii )
Ooo = wiz . workingURL ( ii111iI1iIi1 )
Oo0oo0O0o00O = wiz . workingURL ( OOO )
I1i11 = wiz . workingURL ( oo0OOo0 )
IiIi1I1 = wiz . workingURL ( I11IiI )
IiIIi1 = wiz . workingURL ( O0ooO0Oo00o )
IIIIiii1IIii = wiz . workingURL ( ooO0oOOooOo0 )
II1i11I = wiz . workingURL ( i1I1ii11i1Iii )
ii1I1IIii11 = wiz . workingURL ( I1IiiiiI )
O0o0oO = wiz . workingURL ( o0OIiII )
IIIIiIiIi1 = wiz . workingURL ( ii1iII1II )
I11iiiiI1i = wiz . workingURL ( Iii1I1I11iiI1 )
iI1i11 = wiz . workingURL ( I1I1i1I )
OoOOoooOO0O = wiz . workingURL ( ii1I )
ooo00Ooo = wiz . workingURL ( O0oO0 )
Oo0o0O00 = wiz . workingURL ( oO0O0OO0O )
ii1I1i11 = wiz . workingURL ( OO )
OOo0O0oo0OO0O = wiz . workingURL ( OoOoO )
OO0 = wiz . workingURL ( Ii1I1i )
o0Oooo = wiz . workingURL ( OOI1iI1ii1II )
iiI = wiz . workingURL ( O0O0OOOOoo )
oOIIiIi = wiz . workingURL ( oOooO0 )
OOoOooOoOOOoo = wiz . workingURL ( Ii1I1Ii )
Iiii1iI1i = wiz . workingURL ( OOoO0 )
I1ii1ii11i1I = wiz . workingURL ( OO0Oooo0oOO0O )
o0OoOO = wiz . workingURL ( o00O0 )
O0O0Oo00 = wiz . workingURL ( oOO0O00Oo0O0o )
oOoO00o = wiz . workingURL ( ii1 )
oO00O0 = wiz . workingURL ( I1iIIiiIIi1i )
IIi1IIIi = wiz . workingURL ( O0O0ooOOO )
O00Ooo = wiz . workingURL ( oOOo0O00o )
OOOO0OOO = wiz . workingURL ( OOOO0OOoO0O0 )
i1i1ii = wiz . workingURL ( O0Oo000ooO00 )
iII1ii1 = wiz . workingURL ( oO0 )
I1i1iiiI1 = wiz . workingURL ( Ii1iIiII1ii1 )
iIIi = wiz . workingURL ( ooOooo000oOO )
oO0o00oo0 = wiz . workingURL ( Oo0oOOo )
ii1IIII = uservar . UPDATECHECK if str ( uservar . UPDATECHECK ) . isdigit ( ) else 1
oO00oOooooo0 = o0 + timedelta ( days = ii1IIII )
oOo = uservar . NOTIFICATION
O0OOooOoO = uservar . ENABLE
i1II1I1Iii1 = uservar . HEADERMESSAGE
iiI11Iii = uservar . HIDECONTACT
O0o0O0 = uservar . CONTACT
Ii1II1I11i1 = uservar . HIDESPACERS
oOoooooOoO = uservar . COLOR1
Ii111 = uservar . COLOR2
I111i1i1111 = uservar . THEME1
IIII1 = uservar . THEME2
I1I1i = uservar . THEME3
I1IIIiIiIi = uservar . THEME4
IIIII1 = uservar . THEME5
iIi1Ii1i1iI = uservar . ICONMAINT if not uservar . ICONMAINT == 'http://' else iiIIIII1i1iI
IIiI1 = uservar . ICONBUILDS if not uservar . ICONBUILDS == 'http://' else iiIIIII1i1iI
i1iI1 = uservar . ICONSPEED if not uservar . ICONSPEED == 'http://' else iiIIIII1i1iI
ii1I1IiiI1ii1i = uservar . ICONAPK if not uservar . ICONAPK == 'http://' else iiIIIII1i1iI
O0o = uservar . ICONCONTACT if not uservar . ICONCONTACT == 'http://' else iiIIIII1i1iI
oO0OoO00o = uservar . ICONSAVE if not uservar . ICONSAVE == 'http://' else iiIIIII1i1iI
II1iiiiII = uservar . ICONREAL if not uservar . ICONREAL == 'http://' else iiIIIII1i1iI
O0OoOO0oo0 = uservar . ICONTRAKT if not uservar . ICONTRAKT == 'http://' else iiIIIII1i1iI
oOO = uservar . ICONSETTINGS if not uservar . ICONSETTINGS == 'http://' else iiIIIII1i1iI
O0o0OO0000ooo = uservar . ICONKODI if not uservar . ICONKODI == 'http://' else iiIIIII1i1iI
iIIII1iIIii = uservar . ICONGAMES if not uservar . ICONGAMES == 'http://' else iiIIIII1i1iI
oOOO00o000o = uservar . ICONMOVIES if not uservar . ICONMOVIES == 'http://' else iiIIIII1i1iI
iIi11i1 = uservar . ICONANDROID if not uservar . ICONANDROID == 'http://' else iiIIIII1i1iI
oO00oo0o00o0o = uservar . ICONSPMC if not uservar . ICONSPMC == 'http://' else iiIIIII1i1iI
IiIIIIIi = uservar . ICONSPINZ if not uservar . ICONSPINZ == 'http://' else iiIIIII1i1iI
###########################
###### Menu Items   #######
###########################
#addDir (display,mode,name=None,url=None,menu=None,overwrite=True,fanart=FANART,icon=ICON, themeit=None)
#addFile(display,mode,name=None,url=None,menu=None,overwrite=True,fanart=FANART,icon=ICON, themeit=None)
if 11 - 11: I1 % i11OOoO0ooOO0 / OoOo0oOooOoOO / oo00ooOoO00
if 96 - 96: OoOoOo00o0
if 90 - 90: Iii % I1iii11 % ii % OoO
if 41 - 41: iii11 * IiiII % IIII1i % Ii1IIIIi1ii1I
def IiiIiI1Ii1i ( ) :
 if len ( Oo0oO0ooo ) > 0 :
  i1iIi = wiz . checkBuild ( Oo0oO0ooo , 'version' )
  iiiii1II = '%s (v%s)' % ( Oo0oO0ooo , o0oOoO00o )
  if i1iIi > o0oOoO00o : iiiii1II = '%s [COLOR red][B][UPDATE v%s][/B][/COLOR]' % ( iiiii1II , i1iIi )
  O0OOO0OOooo00 ( iiiii1II , 'viewbuild' , Oo0oO0ooo , themeit = I1IIIiIiIi )
  I111iIi1 = wiz . checkBuild ( Oo0oO0ooo , 'theme' )
  if not I111iIi1 == 'http://' and wiz . workingURL ( I111iIi1 ) == True :
   oo00O00oO000o ( 'None' if i1 == "" else i1 , 'theme' , Oo0oO0ooo , themeit = IIIII1 )
 else : O0OOO0OOooo00 ( 'None' , 'builds' , themeit = I1IIIiIiIi )
 if Ii1II1I11i1 == 'No' : oo00O00oO000o ( '============================================' , '' , themeit = I1I1i )
 O0OOO0OOooo00 ( 'SpinzTV Builds' , 'builds' , icon = IIiI1 , themeit = I111i1i1111 )
 O0OOO0OOooo00 ( 'Maintenance' , 'maint' , icon = iIi1Ii1i1iI , themeit = I111i1i1111 )
 O0OOO0OOooo00 ( 'Speed Test' , 'speed' , icon = i1iI1 , themeit = I111i1i1111 )
 O0OOO0OOooo00 ( 'Apk Installer (ANDROID ONLY!!!)' , 'apk1' , icon = ii1I1IiiI1ii1i , themeit = I111i1i1111 )
 O0OOO0OOooo00 ( 'Emulators And Roms (ANDROID ONLY!)' , 'emurom' , icon = iIIII1iIIii , themeit = I111i1i1111 )
 O0OOO0OOooo00 ( 'Save Data' , 'savedata' , icon = oO0OoO00o , themeit = I111i1i1111 )
 if iiI11Iii == 'No' : oo00O00oO000o ( 'Contact' , 'contact' , icon = O0o , themeit = I111i1i1111 )
 if Ii1II1I11i1 == 'No' : oo00O00oO000o ( '============================================' , '' , themeit = I1I1i )
 oo00O00oO000o ( 'Settings' , 'settings' , icon = oOO , themeit = I111i1i1111 )
 if iIi1ii1I1 == 'true' : O0OOO0OOooo00 ( 'Developer Menu' , 'developer' , icon = oOO , themeit = I111i1i1111 )
 OOo00OoO ( 'movies' , 'MAIN' )
 if 10 - 10: ooo000ooO0000 / oOoooo000Oo00
 if 93 - 93: o0o00 / IiI11iI1i1i1i * I1Iiiiiii * OOOOoO0O0oo0 + OoOoOo00o0
 if 32 - 32: OoOo0oOooOoOO . ooo000ooO0000 + IiI11iI1i1i1i - IiiII . OoO - i11iIiiIii
 if 95 - 95: IiI11iI1i1i1i
def ii11 ( ) :
 if not OOOO0OOO == True :
  oo00O00oO000o ( 'Kodi Version: %s' % ooooooO0oo , '' , icon = IIiI1 , themeit = I1I1i )
  if Ii1II1I11i1 == 'No' : oo00O00oO000o ( '============================================' , '' , themeit = I1I1i )
  oo00O00oO000o ( 'Url for txt file not valid' , '' , icon = IIiI1 , themeit = I1I1i )
  oo00O00oO000o ( '%s' % OOOO0OOO , '' , icon = IIiI1 , themeit = I1I1i )
 else :
  oooO0 = wiz . openURL ( OOOO0OOoO0O0 ) . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
  iiIIiii = re . compile ( 'name="(.+?)".+?ersion="(.+?)".+?rl="(.+?)".+?odi="(.+?)".+?con="(.+?)".+?anart="(.+?)"' ) . findall ( oooO0 )
  if len ( iiIIiii ) == 1 :
   iiIIIiIi1IIi ( iiIIiii [ 0 ] [ 0 ] )
  elif len ( iiIIiii ) > 1 :
   oo00O00oO000o ( 'Kodi Version: %s' % ooooooO0oo , '' , icon = IIiI1 , themeit = I1I1i )
   if Ii1II1I11i1 == 'No' : oo00O00oO000o ( '============================================' , '' , themeit = I1I1i )
   if oO0o0o0ooO0oO == 'true' :
    for ii11i , i1iIi , III11II1I1Ii1 , O00Oo0o000oO , oO0o00oOOooO0 , OOOoO000 in iiIIiii :
     oOOOO = Ii ( 'install' , ii11i )
     O0OOO0OOooo00 ( '[%s] %s (v%s)' % ( float ( O00Oo0o000oO ) , ii11i , i1iIi ) , 'viewbuild' , ii11i , fanart = OOOoO000 , icon = oO0o00oOOooO0 , menu = oOOOO , themeit = IIII1 )
   else :
    Ii1ii111i1 = wiz . buildCount ( '15' ) ; i1i1i1I = wiz . buildCount ( '16' )
    if i1i1i1I > 0 :
     if Ii1ii111i1 > 0 :
      oOoo000 = '+' if i11 == 'false' else '-'
      oo00O00oO000o ( '[%s] Jarvis and Above(%s)' % ( oOoo000 , i1i1i1I ) , 'showupdate' , '16' , themeit = I1I1i )
     if i11 == 'true' :
      for ii11i , i1iIi , III11II1I1Ii1 , O00Oo0o000oO , oO0o00oOOooO0 , OOOoO000 in iiIIiii :
       OooOo00o = int ( float ( O00Oo0o000oO ) )
       if OooOo00o >= 16 :
        oOOOO = Ii ( 'install' , ii11i )
        O0OOO0OOooo00 ( '[%s] %s (v%s)' % ( float ( O00Oo0o000oO ) , ii11i , i1iIi ) , 'viewbuild' , ii11i , fanart = OOOoO000 , icon = oO0o00oOOooO0 , menu = oOOOO , themeit = IIII1 )
    if Ii1ii111i1 > 0 :
     if i1i1i1I > 0 :
      oOoo000 = '+' if i1111 == 'false' else '-'
      oo00O00oO000o ( '[%s] Isengard and Below(%s)' % ( oOoo000 , Ii1ii111i1 ) , 'showupdate' , '15' , themeit = I1I1i )
     if i1111 == 'true' :
      for ii11i , i1iIi , III11II1I1Ii1 , O00Oo0o000oO , oO0o00oOOooO0 , OOOoO000 in iiIIiii :
       OooOo00o = int ( float ( O00Oo0o000oO ) )
       if OooOo00o <= 15 :
        oOOOO = Ii ( 'install' , ii11i )
        O0OOO0OOooo00 ( '[%s] %s (v%s)' % ( float ( O00Oo0o000oO ) , ii11i , i1iIi ) , 'viewbuild' , ii11i , fanart = OOOoO000 , icon = oO0o00oOOooO0 , menu = oOOOO , themeit = IIII1 )
  else : oo00O00oO000o ( 'Text file for builds not formated correctly.' , '' , icon = IIiI1 , themeit = I1I1i )
 OOo00OoO ( 'movies' , 'MAIN' )
 if 20 - 20: oo00ooOoO00 * I1Iiiiiii + OoOoOo00o0 % iii11 % IIII1i
def iiIIIiIi1IIi ( name ) :
 if not OOOO0OOO == True :
  oo00O00oO000o ( 'Url for txt file not valid' , '' , themeit = I1I1i )
  oo00O00oO000o ( '%s' % OOOO0OOO , '' , themeit = I1I1i )
  return
 if wiz . checkBuild ( name , 'version' ) == False :
  oo00O00oO000o ( 'Error reading the txt file.' , '' , themeit = I1I1i )
  oo00O00oO000o ( '%s was not found in the builds list.' % name , '' , themeit = I1I1i )
  return
 oooO0 = wiz . openURL ( OOOO0OOoO0O0 ) . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
 iiIIiii = re . compile ( 'name="%s".+?ersion="(.+?)".+?rl="(.+?)".+?ui="(.+?)".+?odi="(.+?)".+?heme="(.+?)".+?con="(.+?)".+?anart="(.+?)"' % name ) . findall ( oooO0 )
 for i1iIi , III11II1I1Ii1 , iIi1II , O00Oo0o000oO , I111iIi1 , oO0o00oOOooO0 , OOOoO000 in iiIIiii :
  oO0o00oOOooO0 = oO0o00oOOooO0 if wiz . workingURL ( oO0o00oOOooO0 ) else iiIIIII1i1iI
  OOOoO000 = OOOoO000 if wiz . workingURL ( OOOoO000 ) else I1i1iiI1
  iiiii1II = '%s (v%s)' % ( name , i1iIi )
  if Oo0oO0ooo == name and i1iIi > o0oOoO00o :
   iiiii1II = '%s [COLOR red][B][CURRENT v%s][/B][/COLOR]' % ( iiiii1II , o0oOoO00o )
  oo00O00oO000o ( iiiii1II , '' , fanart = OOOoO000 , icon = oO0o00oOOooO0 , themeit = IIII1 )
  oo00O00oO000o ( '===============[ Install ]===================' , '' , fanart = OOOoO000 , icon = oO0o00oOOooO0 , themeit = I1I1i )
  oo00O00oO000o ( 'Fresh Install' , 'install' , name , 'fresh' , fanart = OOOoO000 , icon = oO0o00oOOooO0 , themeit = I111i1i1111 )
  oo00O00oO000o ( 'Standard Install' , 'install' , name , 'normal' , fanart = OOOoO000 , icon = oO0o00oOOooO0 , themeit = I111i1i1111 )
  if not iIi1II == 'http://' : oo00O00oO000o ( 'Apply guiFix' , 'install' , name , 'gui' , fanart = OOOoO000 , icon = oO0o00oOOooO0 , themeit = I111i1i1111 )
  if not I111iIi1 == 'http://' :
   if wiz . workingURL ( I111iIi1 ) == True :
    oo00O00oO000o ( '===============[ Themes ]==================' , '' , fanart = OOOoO000 , icon = oO0o00oOOooO0 , themeit = I1I1i )
    oooO0 = wiz . openURL ( I111iIi1 ) . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
    iiIIiii = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?con="(.+?)".+?anart="(.+?)"' ) . findall ( oooO0 )
    for I1iIiI11I1 , i1oOOoo0o0OOOO , i1IiII1III , i1O00oo in iiIIiii :
     i1IiII1III = i1IiII1III if i1IiII1III == 'http://' else oO0o00oOOooO0
     i1O00oo = i1O00oo if i1O00oo == 'http://' else OOOoO000
     oo00O00oO000o ( I1iIiI11I1 if not I1iIiI11I1 == i1 else "[B]%s (Installed)[/B]" % I1iIiI11I1 , 'theme' , name , I1iIiI11I1 , fanart = i1O00oo , icon = i1IiII1III , themeit = I1I1i )
     if 77 - 77: o0o00 % Ii1IIIIi1ii1I - ooo000ooO0000 % OOOOoO0O0oo0 - ii / I1iii11
     if 4 - 4: OoOo0oOooOoOO - oo00ooOoO00 % oOoooo000Oo00 - Ii1IIIIi1ii1I * iii11
     if 85 - 85: OoOo0oOooOoOO * i11OOoO0ooOO0 . o0o00 / OoOo0oOooOoOO % Iii % I1
     if 36 - 36: oOoooo000Oo00 / OoOoOo00o0 / IiI11iI1i1i1i / IiI11iI1i1i1i + IiiII
def oO0Ooo0ooOO0 ( ) :
 O0OOO0OOooo00 ( 'SpinzTV APKS' , 'apkspinz' , icon = IiIIIIIi , themeit = I111i1i1111 )
 O0OOO0OOooo00 ( 'My Android APPS' , 'apkin' , icon = ii1I1IiiI1ii1i , themeit = I111i1i1111 )
 O0OOO0OOooo00 ( 'Kodi and SPMC' , 'apkkodi' , icon = O0o0OO0000ooo , themeit = I111i1i1111 )
 i1IIiIii1i = ooOOO0OooOo ( base64 . b64decode ( 'aHR0cHM6Ly93d3cuYXBrZmlsZXMuY29tLw==' ) )
 iiIIiii = re . compile ( 'href="([^"]*)">Applications(.+?)</a>' ) . findall ( i1IIiIii1i )
 I1Ii = re . compile ( 'href="([^"]*)">Games(.+?)</a>' ) . findall ( i1IIiIii1i )
 for III11II1I1Ii1 , oOOIi1II in iiIIiii :
  O0Oo00 ( '[COLOR deepskyblue]Android Apps[/COLOR]' + oOOIi1II , 'https://www.apkfiles.com' + III11II1I1Ii1 , 'apkgame' , o0oO0 + 'apps.png' )
 for III11II1I1Ii1 , oOOIi1II in I1Ii :
  O0Oo00 ( '[COLOR deepskyblue]Android Games[/COLOR]' + oOOIi1II , 'https://www.apkfiles.com' + III11II1I1Ii1 , 'apkgame' , o0oO0 + 'GAMES.png' )
 OOo00OoO ( 'movies' , 'MAIN' )
 O0OOO0OOooo00 ( 'Spinz Apk Picks' , 'apkmaster' , icon = ii1I1IiiI1ii1i , themeit = I111i1i1111 )
 if 41 - 41: i11OOoO0ooOO0 % ooo000ooO0000
 if 59 - 59: Ii1IIIIi1ii1I + i11iIiiIii
def oo0OOo0O ( url ) :
 i1IIiIii1i = ooOOO0OooOo ( url )
 iiIIiii = re . compile ( '<a href="([^"]*)" >(.+?)</a>' ) . findall ( i1IIiIii1i )
 for url , ii11i in iiIIiii :
  if '/cat' in url :
   O0Oo00 ( ( ii11i ) . replace ( '&amp;' , ' - ' ) , 'https://www.apkfiles.com' + url , 'select' , o0oO0 + 'APK.png' )
   if 39 - 39: OoOo0oOooOoOO + IIII1i % Ii1IIIIi1ii1I / Ii1IIIIi1ii1I
def I1i ( url ) :
 i1IIiIii1i = ooOOO0OooOo ( url )
 oooii1iiIi1 = url
 if "page=" in str ( url ) :
  oooii1iiIi1 = url . split ( '?' ) [ 0 ]
 iiIIiii = re . compile ( '<a href="([^"]*)".+?<img src="([^"]*)" class="file_list_icon".+?alt="([^"]*)"' , re . DOTALL ) . findall ( i1IIiIii1i )
 I1Ii = re . compile ( 'class="[^"]*".+?ref="([^"]*)".+?yle=.+?</a>' ) . findall ( i1IIiIii1i )
 for url , i111iiI1ii , ii11i in iiIIiii :
  if 'apk' in url :
   O0Oo00 ( ( ii11i ) . replace ( '&#39;' , '' ) . replace ( '&amp;' , ' - ' ) . replace ( '&#174;:' , ': ' ) . replace ( '&#174;' , ' ' ) , 'https://www.apkfiles.com' + url , 'grab' , 'http:' + i111iiI1ii )
 if len ( I1Ii ) > 1 :
  I1Ii = str ( I1Ii [ len ( I1Ii ) - 1 ] )
 O0Oo00 ( 'Next Page' , oooii1iiIi1 + str ( I1Ii ) , 'select' , o0oO0 + 'Next.png' )
 if 24 - 24: OoO / OoOo0oOooOoOO . OoOoOo00o0 . Iii % I1 % oOoooo000Oo00
def IiIII1i1i ( name , url ) :
 i1IIiIii1i = ooOOO0OooOo ( url )
 name = name
 iiIIiii = re . compile ( 'href="([^"]*)".+?lass="yellow_button".+?itle=' ) . findall ( i1IIiIii1i )
 for url in iiIIiii :
  url = 'https://www.apkfiles.com' + url
  II11I ( name , url , 'Brackets' )
  if 80 - 80: Ii1IIIIi1ii1I
def III ( ) :
 if i1i1ii :
  oooO0 = wiz . openURL ( O0Oo000ooO00 ) . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
 iiIIiii = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?con="(.+?)".+?anart="(.+?)"' ) . findall ( oooO0 )
 if len ( iiIIiii ) > 0 :
  for ii11i , III11II1I1Ii1 , oO0o00oOOooO0 , OOOoO000 in iiIIiii :
   oo00O00oO000o ( ii11i , 'apkinstall' , ii11i , III11II1I1Ii1 , icon = oO0o00oOOooO0 , fanart = OOOoO000 , themeit = I111i1i1111 )
  else : wiz . log ( "[APK Menu] ERROR: Invalid Format." )
 else : wiz . log ( "[APK Menu] ERROR: URL for apk list not working." )
 if 81 - 81: I1iii11 / i11iIiiIii + o0o00 % i11OOoO0ooOO0 * I1Iiiiiii
def iiI1II11II1i ( ) :
 xbmc . executebuiltin ( 'ActivateWindow(10001,"androidapp://sources/apps/",return)' )
 if 67 - 67: Ii1IIIIi1ii1I + I1iii11
def OoOo000oOo0oo ( ) :
 oo00O00oO000o ( 'Kodi (v%s)' % wiz . latestApk ( 'kodi' , 'version' ) , 'apkinstall' , 'kodi' , wiz . latestApk ( 'kodi' , 'url' ) , icon = O0o0OO0000ooo , themeit = I111i1i1111 )
 oo00O00oO000o ( 'SPMC (v%s)' % wiz . latestApk ( 'spmc' , 'version' ) , 'apkinstall' , 'spmc' , wiz . latestApk ( 'spmc' , 'url' ) , icon = oO00oo0o00o0o , themeit = I111i1i1111 )
 if 65 - 65: OoO / ii % IiI11iI1i1i1i
def iIiIIii ( ) :
 if iII1ii1 :
  oooO0 = wiz . openURL ( oO0 ) . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
 iiIIiii = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?con="(.+?)".+?anart="(.+?)"' ) . findall ( oooO0 )
 if len ( iiIIiii ) > 0 :
  for ii11i , III11II1I1Ii1 , oO0o00oOOooO0 , OOOoO000 in iiIIiii :
   oo00O00oO000o ( ii11i , 'apkinstall' , ii11i , III11II1I1Ii1 , icon = oO0o00oOOooO0 , fanart = OOOoO000 , themeit = I111i1i1111 )
  else : wiz . log ( "[APK Menu] ERROR: Invalid Format." )
 else : wiz . log ( "[APK Menu] ERROR: URL for apk list not working." )
 if 61 - 61: iii11 / Ii1IIIIi1ii1I / I1iii11 * I1
def iIII1i1i ( ) :
 O0OOO0OOooo00 ( 'Emulators' , 'emulators' , icon = iIIII1iIIii , themeit = I111i1i1111 )
 O0OOO0OOooo00 ( 'Roms' , 'roms' , icon = iIIII1iIIii , themeit = I111i1i1111 )
 if 35 - 35: OoOoOo00o0 * ooo000ooO0000 - OoOo0oOooOoOO . ooo000ooO0000 . ooo000ooO0000
def I1II ( ) :
 if iIiIi11 :
  oooO0 = wiz . openURL ( oooooOoo0ooo ) . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
 iiIIiii = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?con="(.+?)".+?anart="(.+?)"' ) . findall ( oooO0 )
 if len ( iiIIiii ) > 0 :
  for ii11i , III11II1I1Ii1 , oO0o00oOOooO0 , OOOoO000 in iiIIiii :
   oo00O00oO000o ( ii11i , 'apkinstall' , ii11i , III11II1I1Ii1 , icon = oO0o00oOOooO0 , fanart = OOOoO000 , themeit = I111i1i1111 )
  else : wiz . log ( "[APK Menu] ERROR: Invalid Format." )
 else : wiz . log ( "[APK Menu] ERROR: URL for emu list not working." )
 if 79 - 79: ii . o0o00 * oOoooo000Oo00 - Ii1IIIIi1ii1I + OOOOoO0O0oo0
 if 14 - 14: i11iIiiIii - o0o00 * OoO
 if 51 - 51: IiiII / i11OOoO0ooOO0 % IIII1i + iii11 * OOOOoO0O0oo0 + I1Iiiiiii
 if 77 - 77: OOOOoO0O0oo0 * OoO
def i1i1111IiI ( ) :
 O0OOO0OOooo00 ( 'NES' , 'nes' , icon = iIIII1iIIii , themeit = I111i1i1111 )
 O0OOO0OOooo00 ( 'SNES' , 'snes' , icon = iIIII1iIIii , themeit = I111i1i1111 )
 O0OOO0OOooo00 ( 'Nintendo 64' , 'n64' , icon = iIIII1iIIii , themeit = I111i1i1111 )
 O0OOO0OOooo00 ( 'Nintendo DS' , 'nds' , icon = iIIII1iIIii , themeit = I111i1i1111 )
 O0OOO0OOooo00 ( 'Genesis' , 'gen' , icon = iIIII1iIIii , themeit = I111i1i1111 )
 O0OOO0OOooo00 ( 'Atari' , 'atr' , icon = iIIII1iIIii , themeit = I111i1i1111 )
 O0OOO0OOooo00 ( 'PC Engine & Turbo Grafx' , 'tbg' , icon = iIIII1iIIii , themeit = I111i1i1111 )
 if 30 - 30: OOOOoO0O0oo0 % OOOOoO0O0oo0 - iii11
 if 70 - 70: I1iii11 . OoO
 if 58 - 58: ooo000ooO0000 + OoOoOo00o0 * o0o00 * i11iIiiIii - i11OOoO0ooOO0
def oooo00o0o0o ( ) :
 O0OOO0OOooo00 ( 'SNES Titles A Thru B' , 'snesa' , icon = iIIII1iIIii , themeit = I111i1i1111 )
 O0OOO0OOooo00 ( 'SNES Titles C Thru E' , 'snesc' , icon = ii1I1IiiI1ii1i , themeit = I111i1i1111 )
 O0OOO0OOooo00 ( 'SNES Titles F Thru H' , 'snesf' , icon = iIIII1iIIii , themeit = I111i1i1111 )
 O0OOO0OOooo00 ( 'SNES Titles I Thru K' , 'snesi' , icon = iIIII1iIIii , themeit = I111i1i1111 )
 O0OOO0OOooo00 ( 'SNES Titles L Thru M' , 'snesl' , icon = iIIII1iIIii , themeit = I111i1i1111 )
 O0OOO0OOooo00 ( 'SNES Titles N Thru O' , 'snesn' , icon = iIIII1iIIii , themeit = I111i1i1111 )
 O0OOO0OOooo00 ( 'SNES Titles P Thru R' , 'snesp' , icon = iIIII1iIIii , themeit = I111i1i1111 )
 O0OOO0OOooo00 ( 'SNES Titles S' , 'sness' , icon = iIIII1iIIii , themeit = I111i1i1111 )
 O0OOO0OOooo00 ( 'SNES Titles T Thru V' , 'snest' , icon = iIIII1iIIii , themeit = I111i1i1111 )
 O0OOO0OOooo00 ( 'SNES Titles W Thru Z' , 'snesw' , icon = iIIII1iIIii , themeit = I111i1i1111 )
 if 87 - 87: ooo000ooO0000 * oo00ooOoO00 - oOoooo000Oo00 % Ii1IIIIi1ii1I / I1Iiiiiii
def IiIiiI11111I1 ( ) :
 if oooOo0OOOoo0 :
  oooO0 = wiz . openURL ( OOO00O ) . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
  iiIIiii = re . compile ( '.+?ame="(.+?)".+?rl="(.+?)".+?con="(.+?)".+?anart="(.+?)"description="(.+?)"' ) . findall ( oooO0 )
 if len ( iiIIiii ) > 0 :
  for ii11i , III11II1I1Ii1 , oO0o00oOOooO0 , OOOoO000 , O0oo0ooOOOO in iiIIiii :
   Ii1ii ( ii11i , 'rominstall' , ii11i , III11II1I1Ii1 , icon = oO0o00oOOooO0 , fanart = OOOoO000 , description = O0oo0ooOOOO , themeit = I111i1i1111 )
  else : wiz . log ( "[ROM Menu] ERROR: Invalid Format." )
 else : wiz . log ( "[ROM Menu] ERROR: URL for apk list not working." )
 if 33 - 33: I1Iiiiiii
def OOO0ooo ( ) :
 if OOoO :
  oooO0 = wiz . openURL ( OOoOO0oo0ooO ) . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
  iiIIiii = re . compile ( '.+?ame="(.+?)".+?rl="(.+?)".+?con="(.+?)".+?anart="(.+?)"description="(.+?)"' ) . findall ( oooO0 )
 if len ( iiIIiii ) > 0 :
  for ii11i , III11II1I1Ii1 , oO0o00oOOooO0 , OOOoO000 , O0oo0ooOOOO in iiIIiii :
   Ii1ii ( ii11i , 'rominstall' , ii11i , III11II1I1Ii1 , icon = oO0o00oOOooO0 , fanart = OOOoO000 , description = O0oo0ooOOOO , themeit = I111i1i1111 )
  else : wiz . log ( "[ROM Menu] ERROR: Invalid Format." )
 else : wiz . log ( "[ROM Menu] ERROR: URL for apk list not working." )
 if 7 - 7: iii11 + oo00ooOoO00 . Iii / I1iii11
def I111i1I1 ( ) :
 if OO0O000 :
  oooO0 = wiz . openURL ( O0o0O00Oo0o0 ) . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
  iiIIiii = re . compile ( '.+?ame="(.+?)".+?rl="(.+?)".+?con="(.+?)".+?anart="(.+?)"description="(.+?)"' ) . findall ( oooO0 )
 if len ( iiIIiii ) > 0 :
  for ii11i , III11II1I1Ii1 , oO0o00oOOooO0 , OOOoO000 , O0oo0ooOOOO in iiIIiii :
   Ii1ii ( ii11i , 'rominstall' , ii11i , III11II1I1Ii1 , icon = oO0o00oOOooO0 , fanart = OOOoO000 , description = O0oo0ooOOOO , themeit = I111i1i1111 )
  else : wiz . log ( "[ROM Menu] ERROR: Invalid Format." )
 else : wiz . log ( "[ROM Menu] ERROR: URL for apk list not working." )
 if 62 - 62: Ii1IIIIi1ii1I * I1Iiiiiii / I1iii11 * iii11
def II1Ii1iI1i1 ( ) :
 if iiIiI1i1 :
  oooO0 = wiz . openURL ( O00O0oOO00O00 ) . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
  iiIIiii = re . compile ( '.+?ame="(.+?)".+?rl="(.+?)".+?con="(.+?)".+?anart="(.+?)"description="(.+?)"' ) . findall ( oooO0 )
 if len ( iiIIiii ) > 0 :
  for ii11i , III11II1I1Ii1 , oO0o00oOOooO0 , OOOoO000 , O0oo0ooOOOO in iiIIiii :
   Ii1ii ( ii11i , 'rominstall' , ii11i , III11II1I1Ii1 , icon = oO0o00oOOooO0 , fanart = OOOoO000 , description = O0oo0ooOOOO , themeit = I111i1i1111 )
  else : wiz . log ( "[ROM Menu] ERROR: Invalid Format." )
 else : wiz . log ( "[ROM Menu] ERROR: URL for apk list not working." )
 if 54 - 54: I1
def OOoO000O00oO ( ) :
 if oO0O00oOOoooO :
  oooO0 = wiz . openURL ( i1Oo00 ) . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
  iiIIiii = re . compile ( '.+?ame="(.+?)".+?rl="(.+?)".+?con="(.+?)".+?anart="(.+?)"description="(.+?)"' ) . findall ( oooO0 )
 if len ( iiIIiii ) > 0 :
  for ii11i , III11II1I1Ii1 , oO0o00oOOooO0 , OOOoO000 , O0oo0ooOOOO in iiIIiii :
   Ii1ii ( ii11i , 'rominstall' , ii11i , III11II1I1Ii1 , icon = oO0o00oOOooO0 , fanart = OOOoO000 , description = O0oo0ooOOOO , themeit = I111i1i1111 )
  else : wiz . log ( "[ROM Menu] ERROR: Invalid Format." )
 else : wiz . log ( "[ROM Menu] ERROR: URL for apk list not working." )
 if 34 - 34: I1
def OooOOOo0 ( ) :
 if IiIi11iI :
  oooO0 = wiz . openURL ( i1i ) . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
  iiIIiii = re . compile ( '.+?ame="(.+?)".+?rl="(.+?)".+?con="(.+?)".+?anart="(.+?)"description="(.+?)"' ) . findall ( oooO0 )
 if len ( iiIIiii ) > 0 :
  for ii11i , III11II1I1Ii1 , oO0o00oOOooO0 , OOOoO000 , O0oo0ooOOOO in iiIIiii :
   Ii1ii ( ii11i , 'rominstall' , ii11i , III11II1I1Ii1 , icon = oO0o00oOOooO0 , fanart = OOOoO000 , description = O0oo0ooOOOO , themeit = I111i1i1111 )
  else : wiz . log ( "[ROM Menu] ERROR: Invalid Format." )
 else : wiz . log ( "[ROM Menu] ERROR: URL for apk list not working." )
 if 54 - 54: oOoooo000Oo00 - ooo000ooO0000 - I1Iiiiiii . i11OOoO0ooOO0
def o0OIIiI1I1 ( ) :
 if Oo0O00O000 :
  oooO0 = wiz . openURL ( iiI111I1iIiI ) . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
  iiIIiii = re . compile ( '.+?ame="(.+?)".+?rl="(.+?)".+?con="(.+?)".+?anart="(.+?)"description="(.+?)"' ) . findall ( oooO0 )
 if len ( iiIIiii ) > 0 :
  for ii11i , III11II1I1Ii1 , oO0o00oOOooO0 , OOOoO000 , O0oo0ooOOOO in iiIIiii :
   Ii1ii ( ii11i , 'rominstall' , ii11i , III11II1I1Ii1 , icon = oO0o00oOOooO0 , fanart = OOOoO000 , description = O0oo0ooOOOO , themeit = I111i1i1111 )
  else : wiz . log ( "[ROM Menu] ERROR: Invalid Format." )
 else : wiz . log ( "[ROM Menu] ERROR: URL for apk list not working." )
 if 15 - 15: oOoooo000Oo00 * I1iii11 % IiiII * i11OOoO0ooOO0 - i11iIiiIii
def Oo00OOOOoo0oo ( ) :
 if Oo0O00O000 :
  oooO0 = wiz . openURL ( iiI111I1iIiI ) . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
  iiIIiii = re . compile ( '.+?ame="(.+?)".+?rl="(.+?)".+?con="(.+?)".+?anart="(.+?)"description="(.+?)"' ) . findall ( oooO0 )
 if len ( iiIIiii ) > 0 :
  for ii11i , III11II1I1Ii1 , oO0o00oOOooO0 , OOOoO000 , O0oo0ooOOOO in iiIIiii :
   Ii1ii ( ii11i , 'rominstall' , ii11i , III11II1I1Ii1 , icon = oO0o00oOOooO0 , fanart = OOOoO000 , description = O0oo0ooOOOO , themeit = I111i1i1111 )
  else : wiz . log ( "[ROM Menu] ERROR: Invalid Format." )
 else : wiz . log ( "[ROM Menu] ERROR: URL for apk list not working." )
 if 80 - 80: I1Iiiiiii * OoO * OoOoOo00o0 - I1 . OoO % Iii
def II1iiIIIiIii ( ) :
 if oo :
  oooO0 = wiz . openURL ( O0 ) . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
  iiIIiii = re . compile ( '.+?ame="(.+?)".+?rl="(.+?)".+?con="(.+?)".+?anart="(.+?)"description="(.+?)"' ) . findall ( oooO0 )
 if len ( iiIIiii ) > 0 :
  for ii11i , III11II1I1Ii1 , oO0o00oOOooO0 , OOOoO000 , O0oo0ooOOOO in iiIIiii :
   Ii1ii ( ii11i , 'rominstall' , ii11i , III11II1I1Ii1 , icon = oO0o00oOOooO0 , fanart = OOOoO000 , description = O0oo0ooOOOO , themeit = I111i1i1111 )
  else : wiz . log ( "[ROM Menu] ERROR: Invalid Format." )
 else : wiz . log ( "[ROM Menu] ERROR: URL for apk list not working." )
 if 23 - 23: o0o00 + ooo000ooO0000 . OoO * Iii + IiiII
def I1iIi1iiiIiI ( ) :
 if I1111i :
  oooO0 = wiz . openURL ( ii1ii1ii ) . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
  iiIIiii = re . compile ( '.+?ame="(.+?)".+?rl="(.+?)".+?con="(.+?)".+?anart="(.+?)"description="(.+?)"' ) . findall ( oooO0 )
 if len ( iiIIiii ) > 0 :
  for ii11i , III11II1I1Ii1 , oO0o00oOOooO0 , OOOoO000 , O0oo0ooOOOO in iiIIiii :
   Ii1ii ( ii11i , 'rominstall' , ii11i , III11II1I1Ii1 , icon = oO0o00oOOooO0 , fanart = OOOoO000 , description = O0oo0ooOOOO , themeit = I111i1i1111 )
  else : wiz . log ( "[ROM Menu] ERROR: Invalid Format." )
 else : wiz . log ( "[ROM Menu] ERROR: URL for apk list not working." )
 if 41 - 41: IiiII * OOOOoO0O0oo0 - oOoooo000Oo00 + I1iii11
 if 23 - 23: OoOoOo00o0 % iii11 + iii11 + o0o00 - o0o00
 if 62 - 62: iii11
def iI11IIiIiIii1 ( ) :
 O0OOO0OOooo00 ( 'NES Titles A Thru B' , 'nesa' , icon = iIIII1iIIii , themeit = I111i1i1111 )
 O0OOO0OOooo00 ( 'NES Titles C' , 'nesc' , icon = ii1I1IiiI1ii1i , themeit = I111i1i1111 )
 O0OOO0OOooo00 ( 'NES Titles D Thru E' , 'nesd' , icon = iIIII1iIIii , themeit = I111i1i1111 )
 O0OOO0OOooo00 ( 'NES Titles F Thru G' , 'nesf' , icon = iIIII1iIIii , themeit = I111i1i1111 )
 O0OOO0OOooo00 ( 'NES Titles H Thru K' , 'nesh' , icon = iIIII1iIIii , themeit = I111i1i1111 )
 O0OOO0OOooo00 ( 'NES Titles L Thru M' , 'nesl' , icon = iIIII1iIIii , themeit = I111i1i1111 )
 O0OOO0OOooo00 ( 'NES Titles N Thru Q' , 'nesn' , icon = iIIII1iIIii , themeit = I111i1i1111 )
 O0OOO0OOooo00 ( 'NES Titles R Thru S' , 'nesr' , icon = iIIII1iIIii , themeit = I111i1i1111 )
 O0OOO0OOooo00 ( 'NES Titles T Thru V' , 'nest' , icon = iIIII1iIIii , themeit = I111i1i1111 )
 O0OOO0OOooo00 ( 'NES Titles W Thru Z' , 'nesw' , icon = iIIII1iIIii , themeit = I111i1i1111 )
 if 37 - 37: i11iIiiIii + Iii * ooo000ooO0000
def OoOoOOO0OO0O ( ) :
 if iIIii :
  oooO0 = wiz . openURL ( I1I1IiI1 ) . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
 iiIIiii = re . compile ( '.+?ame="(.+?)".+?rl="(.+?)".+?con="(.+?)".+?anart="(.+?)"description="(.+?)"' ) . findall ( oooO0 )
 if len ( iiIIiii ) > 0 :
  for ii11i , III11II1I1Ii1 , oO0o00oOOooO0 , OOOoO000 , O0oo0ooOOOO in iiIIiii :
   Ii1ii ( ii11i , 'rominstall' , ii11i , III11II1I1Ii1 , icon = oO0o00oOOooO0 , fanart = OOOoO000 , description = O0oo0ooOOOO , themeit = I111i1i1111 )
  else : wiz . log ( "[ROM Menu] ERROR: Invalid Format." )
 else : wiz . log ( "[ROM Menu] ERROR: URL for rom list not working." )
 if 36 - 36: OoO + iii11 - OoOo0oOooOoOO . IIII1i . OoOo0oOooOoOO / I1iii11
def o00O ( ) :
 if o00O0O :
  oooO0 = wiz . openURL ( III1iII1I1ii ) . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
 iiIIiii = re . compile ( '.+?ame="(.+?)".+?rl="(.+?)".+?con="(.+?)".+?anart="(.+?)"description="(.+?)"' ) . findall ( oooO0 )
 if len ( iiIIiii ) > 0 :
  for ii11i , III11II1I1Ii1 , oO0o00oOOooO0 , OOOoO000 , O0oo0ooOOOO in iiIIiii :
   Ii1ii ( ii11i , 'rominstall' , ii11i , III11II1I1Ii1 , icon = oO0o00oOOooO0 , fanart = OOOoO000 , description = O0oo0ooOOOO , themeit = I111i1i1111 )
  else : wiz . log ( "[ROM Menu] ERROR: Invalid Format." )
 else : wiz . log ( "[ROM Menu] ERROR: URL for rom list not working." )
 if 48 - 48: o0o00 . i11iIiiIii
def IIi ( ) :
 if ii1iii1i :
  oooO0 = wiz . openURL ( oOOo0 ) . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
 iiIIiii = re . compile ( '.+?ame="(.+?)".+?rl="(.+?)".+?con="(.+?)".+?anart="(.+?)"description="(.+?)"' ) . findall ( oooO0 )
 if len ( iiIIiii ) > 0 :
  for ii11i , III11II1I1Ii1 , oO0o00oOOooO0 , OOOoO000 , O0oo0ooOOOO in iiIIiii :
   Ii1ii ( ii11i , 'rominstall' , ii11i , III11II1I1Ii1 , icon = oO0o00oOOooO0 , fanart = OOOoO000 , description = O0oo0ooOOOO , themeit = I111i1i1111 )
  else : wiz . log ( "[ROM Menu] ERROR: Invalid Format." )
 else : wiz . log ( "[ROM Menu] ERROR: URL for rom list not working." )
 if 58 - 58: OoOoOo00o0
def IIi1IiiI1 ( ) :
 if Iii1I1111ii :
  oooO0 = wiz . openURL ( oo00O00oO ) . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
 iiIIiii = re . compile ( '.+?ame="(.+?)".+?rl="(.+?)".+?con="(.+?)".+?anart="(.+?)"description="(.+?)"' ) . findall ( oooO0 )
 if len ( iiIIiii ) > 0 :
  for ii11i , III11II1I1Ii1 , oO0o00oOOooO0 , OOOoO000 , O0oo0ooOOOO in iiIIiii :
   Ii1ii ( ii11i , 'rominstall' , ii11i , III11II1I1Ii1 , icon = oO0o00oOOooO0 , fanart = OOOoO000 , description = O0oo0ooOOOO , themeit = I111i1i1111 )
  else : wiz . log ( "[ROM Menu] ERROR: Invalid Format." )
 else : wiz . log ( "[ROM Menu] ERROR: URL for rom list not working." )
 if 87 - 87: IIII1i % oOoooo000Oo00
def oo0OOOoOo ( ) :
 if ooOoO00 :
  oooO0 = wiz . openURL ( iIiIIIi ) . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
 iiIIiii = re . compile ( '.+?ame="(.+?)".+?rl="(.+?)".+?con="(.+?)".+?anart="(.+?)"description="(.+?)"' ) . findall ( oooO0 )
 if len ( iiIIiii ) > 0 :
  for ii11i , III11II1I1Ii1 , oO0o00oOOooO0 , OOOoO000 , O0oo0ooOOOO in iiIIiii :
   Ii1ii ( ii11i , 'rominstall' , ii11i , III11II1I1Ii1 , icon = oO0o00oOOooO0 , fanart = OOOoO000 , description = O0oo0ooOOOO , themeit = I111i1i1111 )
  else : wiz . log ( "[ROM Menu] ERROR: Invalid Format." )
 else : wiz . log ( "[ROM Menu] ERROR: URL for rom list not working." )
 if 21 - 21: ii - I1 . IIII1i + oOoooo000Oo00 . i11OOoO0ooOO0 - OoO
def I11IIIiIi11 ( ) :
 if Ii1IIiI1i :
  oooO0 = wiz . openURL ( ooo00OOOooO ) . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
 iiIIiii = re . compile ( '.+?ame="(.+?)".+?rl="(.+?)".+?con="(.+?)".+?anart="(.+?)"description="(.+?)"' ) . findall ( oooO0 )
 if len ( iiIIiii ) > 0 :
  for ii11i , III11II1I1Ii1 , oO0o00oOOooO0 , OOOoO000 , O0oo0ooOOOO in iiIIiii :
   Ii1ii ( ii11i , 'rominstall' , ii11i , III11II1I1Ii1 , icon = oO0o00oOOooO0 , fanart = OOOoO000 , description = O0oo0ooOOOO , themeit = I111i1i1111 )
  else : wiz . log ( "[ROM Menu] ERROR: Invalid Format." )
 else : wiz . log ( "[ROM Menu] ERROR: URL for rom list not working." )
 if 39 - 39: oOoooo000Oo00 % I1 % OoO . oo00ooOoO00
def oOo00OooO0oO ( ) :
 if o0O00Oo0 :
  oooO0 = wiz . openURL ( O00OOOoOoo0O ) . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
 iiIIiii = re . compile ( '.+?ame="(.+?)".+?rl="(.+?)".+?con="(.+?)".+?anart="(.+?)"description="(.+?)"' ) . findall ( oooO0 )
 if len ( iiIIiii ) > 0 :
  for ii11i , III11II1I1Ii1 , oO0o00oOOooO0 , OOOoO000 , O0oo0ooOOOO in iiIIiii :
   Ii1ii ( ii11i , 'rominstall' , ii11i , III11II1I1Ii1 , icon = oO0o00oOOooO0 , fanart = OOOoO000 , description = O0oo0ooOOOO , themeit = I111i1i1111 )
  else : wiz . log ( "[ROM Menu] ERROR: Invalid Format." )
 else : wiz . log ( "[ROM Menu] ERROR: URL for rom list not working." )
 if 16 - 16: IiI11iI1i1i1i / I1iii11 + Ii1IIIIi1ii1I / oOoooo000Oo00
def IIIiiI1 ( ) :
 if IiII111i1i11 :
  oooO0 = wiz . openURL ( O000OOo00oo ) . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
 iiIIiii = re . compile ( '.+?ame="(.+?)".+?rl="(.+?)".+?con="(.+?)".+?anart="(.+?)"description="(.+?)"' ) . findall ( oooO0 )
 if len ( iiIIiii ) > 0 :
  for ii11i , III11II1I1Ii1 , oO0o00oOOooO0 , OOOoO000 , O0oo0ooOOOO in iiIIiii :
   Ii1ii ( ii11i , 'rominstall' , ii11i , III11II1I1Ii1 , icon = oO0o00oOOooO0 , fanart = OOOoO000 , description = O0oo0ooOOOO , themeit = I111i1i1111 )
  else : wiz . log ( "[ROM Menu] ERROR: Invalid Format." )
 else : wiz . log ( "[ROM Menu] ERROR: URL for rom list not working." )
 if 74 - 74: ooo000ooO0000 - Ii1IIIIi1ii1I + oo00ooOoO00 . Iii + Ii1IIIIi1ii1I - ooo000ooO0000
def IiIiiiiI1 ( ) :
 if i111iIi1i1II1 :
  oooO0 = wiz . openURL ( oo0OOo ) . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
 iiIIiii = re . compile ( '.+?ame="(.+?)".+?rl="(.+?)".+?con="(.+?)".+?anart="(.+?)"description="(.+?)"' ) . findall ( oooO0 )
 if len ( iiIIiii ) > 0 :
  for ii11i , III11II1I1Ii1 , oO0o00oOOooO0 , OOOoO000 , O0oo0ooOOOO in iiIIiii :
   Ii1ii ( ii11i , 'rominstall' , ii11i , III11II1I1Ii1 , icon = oO0o00oOOooO0 , fanart = OOOoO000 , description = O0oo0ooOOOO , themeit = I111i1i1111 )
  else : wiz . log ( "[ROM Menu] ERROR: Invalid Format." )
 else : wiz . log ( "[ROM Menu] ERROR: URL for rom list not working." )
 if 62 - 62: IiiII % o0o00 * ii - oo00ooOoO00
def OoOOo ( ) :
 if oooO :
  oooO0 = wiz . openURL ( ooOOO00Ooo ) . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
 iiIIiii = re . compile ( '.+?ame="(.+?)".+?rl="(.+?)".+?con="(.+?)".+?anart="(.+?)"description="(.+?)"' ) . findall ( oooO0 )
 if len ( iiIIiii ) > 0 :
  for ii11i , III11II1I1Ii1 , oO0o00oOOooO0 , OOOoO000 , O0oo0ooOOOO in iiIIiii :
   Ii1ii ( ii11i , 'rominstall' , ii11i , III11II1I1Ii1 , icon = oO0o00oOOooO0 , fanart = OOOoO000 , description = O0oo0ooOOOO , themeit = I111i1i1111 )
  else : wiz . log ( "[ROM Menu] ERROR: Invalid Format." )
 else : wiz . log ( "[ROM Menu] ERROR: URL for rom list not working." )
 if 17 - 17: oo00ooOoO00
 if 1 - 1: OOOOoO0O0oo0
 if 78 - 78: IiiII + ooo000ooO0000 - I1
def i1I1iIi1IiI ( ) :
 O0OOO0OOooo00 ( 'Genesis Titles A Thru B' , 'gena' , icon = iIIII1iIIii , themeit = I111i1i1111 )
 O0OOO0OOooo00 ( 'Genesis Titles C Thru D' , 'genc' , icon = ii1I1IiiI1ii1i , themeit = I111i1i1111 )
 O0OOO0OOooo00 ( 'Genesis Titles E Thru G' , 'gene' , icon = iIIII1iIIii , themeit = I111i1i1111 )
 O0OOO0OOooo00 ( 'Genesis Titles H Thru L' , 'genh' , icon = iIIII1iIIii , themeit = I111i1i1111 )
 O0OOO0OOooo00 ( 'Genesis Titles M Thru O' , 'genm' , icon = iIIII1iIIii , themeit = I111i1i1111 )
 O0OOO0OOooo00 ( 'Genesis Titles P Thru R' , 'genp' , icon = iIIII1iIIii , themeit = I111i1i1111 )
 O0OOO0OOooo00 ( 'Genesis Titles S Thru T' , 'gens' , icon = iIIII1iIIii , themeit = I111i1i1111 )
 O0OOO0OOooo00 ( 'Genesis Titles U Thru Z' , 'genu' , icon = iIIII1iIIii , themeit = I111i1i1111 )
 if 11 - 11: OoOoOo00o0
def O00O00O000OOO ( ) :
 if i1I1i111Ii :
  oooO0 = wiz . openURL ( IiIIIi1iIi ) . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
 iiIIiii = re . compile ( '.+?ame="(.+?)".+?rl="(.+?)".+?con="(.+?)".+?anart="(.+?)"description="(.+?)"' ) . findall ( oooO0 )
 if len ( iiIIiii ) > 0 :
  for ii11i , III11II1I1Ii1 , oO0o00oOOooO0 , OOOoO000 , O0oo0ooOOOO in iiIIiii :
   Ii1ii ( ii11i , 'rominstall' , ii11i , III11II1I1Ii1 , icon = oO0o00oOOooO0 , fanart = OOOoO000 , description = O0oo0ooOOOO , themeit = I111i1i1111 )
  else : wiz . log ( "[ROM Menu] ERROR: Invalid Format." )
 else : wiz . log ( "[ROM Menu] ERROR: URL for rom list not working." )
 if 3 - 3: I1
def Ooo0Oo0oo0 ( ) :
 if ooo :
  oooO0 = wiz . openURL ( ooOOoooooo ) . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
 iiIIiii = re . compile ( '.+?ame="(.+?)".+?rl="(.+?)".+?con="(.+?)".+?anart="(.+?)"description="(.+?)"' ) . findall ( oooO0 )
 if len ( iiIIiii ) > 0 :
  for ii11i , III11II1I1Ii1 , oO0o00oOOooO0 , OOOoO000 , O0oo0ooOOOO in iiIIiii :
   Ii1ii ( ii11i , 'rominstall' , ii11i , III11II1I1Ii1 , icon = oO0o00oOOooO0 , fanart = OOOoO000 , description = O0oo0ooOOOO , themeit = I111i1i1111 )
  else : wiz . log ( "[ROM Menu] ERROR: Invalid Format." )
 else : wiz . log ( "[ROM Menu] ERROR: URL for rom list not working." )
 if 83 - 83: I1Iiiiiii
def ii111Ii11iii ( ) :
 if i1i1iI1iiiI :
  oooO0 = wiz . openURL ( II1I ) . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
 iiIIiii = re . compile ( '.+?ame="(.+?)".+?rl="(.+?)".+?con="(.+?)".+?anart="(.+?)"description="(.+?)"' ) . findall ( oooO0 )
 if len ( iiIIiii ) > 0 :
  for ii11i , III11II1I1Ii1 , oO0o00oOOooO0 , OOOoO000 , O0oo0ooOOOO in iiIIiii :
   Ii1ii ( ii11i , 'rominstall' , ii11i , III11II1I1Ii1 , icon = oO0o00oOOooO0 , fanart = OOOoO000 , description = O0oo0ooOOOO , themeit = I111i1i1111 )
  else : wiz . log ( "[ROM Menu] ERROR: Invalid Format." )
 else : wiz . log ( "[ROM Menu] ERROR: URL for rom list not working." )
 if 62 - 62: i11OOoO0ooOO0
def OO0OoOOO0 ( ) :
 if Ooo0oOooo0 :
  oooO0 = wiz . openURL ( O0i1II1Iiii1I11 ) . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
 iiIIiii = re . compile ( '.+?ame="(.+?)".+?rl="(.+?)".+?con="(.+?)".+?anart="(.+?)"description="(.+?)"' ) . findall ( oooO0 )
 if len ( iiIIiii ) > 0 :
  for ii11i , III11II1I1Ii1 , oO0o00oOOooO0 , OOOoO000 , O0oo0ooOOOO in iiIIiii :
   Ii1ii ( ii11i , 'rominstall' , ii11i , III11II1I1Ii1 , icon = oO0o00oOOooO0 , fanart = OOOoO000 , description = O0oo0ooOOOO , themeit = I111i1i1111 )
  else : wiz . log ( "[ROM Menu] ERROR: Invalid Format." )
 else : wiz . log ( "[ROM Menu] ERROR: URL for rom list not working." )
 if 90 - 90: OOOOoO0O0oo0 + OoOoOo00o0 * IiiII / oOoooo000Oo00 . iii11 + iii11
def I11I ( ) :
 if oOOOoo00 :
  oooO0 = wiz . openURL ( IIII ) . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
 iiIIiii = re . compile ( '.+?ame="(.+?)".+?rl="(.+?)".+?con="(.+?)".+?anart="(.+?)"description="(.+?)"' ) . findall ( oooO0 )
 if len ( iiIIiii ) > 0 :
  for ii11i , III11II1I1Ii1 , oO0o00oOOooO0 , OOOoO000 , O0oo0ooOOOO in iiIIiii :
   Ii1ii ( ii11i , 'rominstall' , ii11i , III11II1I1Ii1 , icon = oO0o00oOOooO0 , fanart = OOOoO000 , description = O0oo0ooOOOO , themeit = I111i1i1111 )
  else : wiz . log ( "[ROM Menu] ERROR: Invalid Format." )
 else : wiz . log ( "[ROM Menu] ERROR: URL for rom list not working." )
 if 69 - 69: oo00ooOoO00
def ooOoOOOOo ( ) :
 if iiIiIIIiiI :
  oooO0 = wiz . openURL ( iiIiI ) . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
 iiIIiii = re . compile ( '.+?ame="(.+?)".+?rl="(.+?)".+?con="(.+?)".+?anart="(.+?)"description="(.+?)"' ) . findall ( oooO0 )
 if len ( iiIIiii ) > 0 :
  for ii11i , III11II1I1Ii1 , oO0o00oOOooO0 , OOOoO000 , O0oo0ooOOOO in iiIIiii :
   Ii1ii ( ii11i , 'rominstall' , ii11i , III11II1I1Ii1 , icon = oO0o00oOOooO0 , fanart = OOOoO000 , description = O0oo0ooOOOO , themeit = I111i1i1111 )
  else : wiz . log ( "[ROM Menu] ERROR: Invalid Format." )
 else : wiz . log ( "[ROM Menu] ERROR: URL for rom list not working." )
 if 71 - 71: OoOoOo00o0 * i11OOoO0ooOO0 / IiiII
def iiIIi ( ) :
 if iiI1IIIi :
  oooO0 = wiz . openURL ( o00oooO0Oo ) . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
 iiIIiii = re . compile ( '.+?ame="(.+?)".+?rl="(.+?)".+?con="(.+?)".+?anart="(.+?)"description="(.+?)"' ) . findall ( oooO0 )
 if len ( iiIIiii ) > 0 :
  for ii11i , III11II1I1Ii1 , oO0o00oOOooO0 , OOOoO000 , O0oo0ooOOOO in iiIIiii :
   Ii1ii ( ii11i , 'rominstall' , ii11i , III11II1I1Ii1 , icon = oO0o00oOOooO0 , fanart = OOOoO000 , description = O0oo0ooOOOO , themeit = I111i1i1111 )
  else : wiz . log ( "[ROM Menu] ERROR: Invalid Format." )
 else : wiz . log ( "[ROM Menu] ERROR: URL for rom list not working." )
 if 96 - 96: o0o00
def i1I11iIII1i1I ( ) :
 if II11IiIi11 :
  oooO0 = wiz . openURL ( o0O0OOO0Ooo ) . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
 iiIIiii = re . compile ( '.+?ame="(.+?)".+?rl="(.+?)".+?con="(.+?)".+?anart="(.+?)"description="(.+?)"' ) . findall ( oooO0 )
 if len ( iiIIiii ) > 0 :
  for ii11i , III11II1I1Ii1 , oO0o00oOOooO0 , OOOoO000 , O0oo0ooOOOO in iiIIiii :
   Ii1ii ( ii11i , 'rominstall' , ii11i , III11II1I1Ii1 , icon = oO0o00oOOooO0 , fanart = OOOoO000 , description = O0oo0ooOOOO , themeit = I111i1i1111 )
  else : wiz . log ( "[ROM Menu] ERROR: Invalid Format." )
 else : wiz . log ( "[ROM Menu] ERROR: URL for rom list not working." )
 if 63 - 63: I1iii11 + I1Iiiiiii - OoOoOo00o0
 if 2 - 2: IiI11iI1i1i1i
 if 97 - 97: IIII1i - OoOo0oOooOoOO
def oO00OoOoo0 ( ) :
 O0OOO0OOooo00 ( 'Atari Titles A Thru B' , 'atra' , icon = iIIII1iIIii , themeit = I111i1i1111 )
 O0OOO0OOooo00 ( 'Atari Titles C Thru D' , 'atrc' , icon = ii1I1IiiI1ii1i , themeit = I111i1i1111 )
 O0OOO0OOooo00 ( 'Atari Titles E Thru G' , 'atre' , icon = iIIII1iIIii , themeit = I111i1i1111 )
 O0OOO0OOooo00 ( 'Atari Titles H Thru L' , 'atrh' , icon = iIIII1iIIii , themeit = I111i1i1111 )
 O0OOO0OOooo00 ( 'Atari Titles M Thru O' , 'atrm' , icon = iIIII1iIIii , themeit = I111i1i1111 )
 O0OOO0OOooo00 ( 'Atari Titles P Thru R' , 'atrp' , icon = iIIII1iIIii , themeit = I111i1i1111 )
 O0OOO0OOooo00 ( 'Atari Titles S Thru U' , 'atrs' , icon = iIIII1iIIii , themeit = I111i1i1111 )
 O0OOO0OOooo00 ( 'Atari Titles V Thru Z' , 'atrv' , icon = iIIII1iIIii , themeit = I111i1i1111 )
 if 34 - 34: o0o00 - OoOo0oOooOoOO . Iii / OoOoOo00o0
def II1II ( ) :
 if IIOOO0O00O0OOOO :
  oooO0 = wiz . openURL ( iiIiII1 ) . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
 iiIIiii = re . compile ( '.+?ame="(.+?)".+?rl="(.+?)".+?con="(.+?)".+?anart="(.+?)"description="(.+?)"' ) . findall ( oooO0 )
 if len ( iiIIiii ) > 0 :
  for ii11i , III11II1I1Ii1 , oO0o00oOOooO0 , OOOoO000 , O0oo0ooOOOO in iiIIiii :
   Ii1ii ( ii11i , 'rominstall' , ii11i , III11II1I1Ii1 , icon = oO0o00oOOooO0 , fanart = OOOoO000 , description = O0oo0ooOOOO , themeit = I111i1i1111 )
  else : wiz . log ( "[ROM Menu] ERROR: Invalid Format." )
 else : wiz . log ( "[ROM Menu] ERROR: URL for rom list not working." )
 if 97 - 97: i11iIiiIii / Ii1IIIIi1ii1I % I1Iiiiiii
def ooo0 ( ) :
 if I1iiii1I :
  oooO0 = wiz . openURL ( OOO00O0O ) . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
 iiIIiii = re . compile ( '.+?ame="(.+?)".+?rl="(.+?)".+?con="(.+?)".+?anart="(.+?)"description="(.+?)"' ) . findall ( oooO0 )
 if len ( iiIIiii ) > 0 :
  for ii11i , III11II1I1Ii1 , oO0o00oOOooO0 , OOOoO000 , O0oo0ooOOOO in iiIIiii :
   Ii1ii ( ii11i , 'rominstall' , ii11i , III11II1I1Ii1 , icon = oO0o00oOOooO0 , fanart = OOOoO000 , description = O0oo0ooOOOO , themeit = I111i1i1111 )
  else : wiz . log ( "[ROM Menu] ERROR: Invalid Format." )
 else : wiz . log ( "[ROM Menu] ERROR: URL for rom list not working." )
 if 55 - 55: I1iii11
def ooO0o ( ) :
 if OOo0 :
  oooO0 = wiz . openURL ( iii ) . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
 iiIIiii = re . compile ( '.+?ame="(.+?)".+?rl="(.+?)".+?con="(.+?)".+?anart="(.+?)"description="(.+?)"' ) . findall ( oooO0 )
 if len ( iiIIiii ) > 0 :
  for ii11i , III11II1I1Ii1 , oO0o00oOOooO0 , OOOoO000 , O0oo0ooOOOO in iiIIiii :
   Ii1ii ( ii11i , 'rominstall' , ii11i , III11II1I1Ii1 , icon = oO0o00oOOooO0 , fanart = OOOoO000 , description = O0oo0ooOOOO , themeit = I111i1i1111 )
  else : wiz . log ( "[ROM Menu] ERROR: Invalid Format." )
 else : wiz . log ( "[ROM Menu] ERROR: URL for rom list not working." )
 if 25 - 25: i11OOoO0ooOO0 - o0o00
def IiI1IiI11iII ( ) :
 if oO00ooooO0o :
  oooO0 = wiz . openURL ( oOooOOOoOo ) . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
 iiIIiii = re . compile ( '.+?ame="(.+?)".+?rl="(.+?)".+?con="(.+?)".+?anart="(.+?)"description="(.+?)"' ) . findall ( oooO0 )
 if len ( iiIIiii ) > 0 :
  for ii11i , III11II1I1Ii1 , oO0o00oOOooO0 , OOOoO000 , O0oo0ooOOOO in iiIIiii :
   Ii1ii ( ii11i , 'rominstall' , ii11i , III11II1I1Ii1 , icon = oO0o00oOOooO0 , fanart = OOOoO000 , description = O0oo0ooOOOO , themeit = I111i1i1111 )
  else : wiz . log ( "[ROM Menu] ERROR: Invalid Format." )
 else : wiz . log ( "[ROM Menu] ERROR: URL for rom list not working." )
 if 64 - 64: IIII1i - Iii / o0o00 - ii
def ii11I ( ) :
 if oo0o :
  oooO0 = wiz . openURL ( i1Iii1i1I ) . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
 iiIIiii = re . compile ( '.+?ame="(.+?)".+?rl="(.+?)".+?con="(.+?)".+?anart="(.+?)"description="(.+?)"' ) . findall ( oooO0 )
 if len ( iiIIiii ) > 0 :
  for ii11i , III11II1I1Ii1 , oO0o00oOOooO0 , OOOoO000 , O0oo0ooOOOO in iiIIiii :
   Ii1ii ( ii11i , 'rominstall' , ii11i , III11II1I1Ii1 , icon = oO0o00oOOooO0 , fanart = OOOoO000 , description = O0oo0ooOOOO , themeit = I111i1i1111 )
  else : wiz . log ( "[ROM Menu] ERROR: Invalid Format." )
 else : wiz . log ( "[ROM Menu] ERROR: URL for rom list not working." )
 if 47 - 47: I1Iiiiiii
def oOiI ( ) :
 if o0oO0oooOoo :
  oooO0 = wiz . openURL ( OOoO00 ) . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
 iiIIiii = re . compile ( '.+?ame="(.+?)".+?rl="(.+?)".+?con="(.+?)".+?anart="(.+?)"description="(.+?)"' ) . findall ( oooO0 )
 if len ( iiIIiii ) > 0 :
  for ii11i , III11II1I1Ii1 , oO0o00oOOooO0 , OOOoO000 , O0oo0ooOOOO in iiIIiii :
   Ii1ii ( ii11i , 'rominstall' , ii11i , III11II1I1Ii1 , icon = oO0o00oOOooO0 , fanart = OOOoO000 , description = O0oo0ooOOOO , themeit = I111i1i1111 )
  else : wiz . log ( "[ROM Menu] ERROR: Invalid Format." )
 else : wiz . log ( "[ROM Menu] ERROR: URL for rom list not working." )
 if 42 - 42: OoOo0oOooOoOO + I1iii11 % OoOoOo00o0 + ii
def I11i11I1iiII ( ) :
 if I1III1111iIi :
  oooO0 = wiz . openURL ( IiI111111IIII ) . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
 iiIIiii = re . compile ( '.+?ame="(.+?)".+?rl="(.+?)".+?con="(.+?)".+?anart="(.+?)"description="(.+?)"' ) . findall ( oooO0 )
 if len ( iiIIiii ) > 0 :
  for ii11i , III11II1I1Ii1 , oO0o00oOOooO0 , OOOoO000 , O0oo0ooOOOO in iiIIiii :
   Ii1ii ( ii11i , 'rominstall' , ii11i , III11II1I1Ii1 , icon = oO0o00oOOooO0 , fanart = OOOoO000 , description = O0oo0ooOOOO , themeit = I111i1i1111 )
  else : wiz . log ( "[ROM Menu] ERROR: Invalid Format." )
 else : wiz . log ( "[ROM Menu] ERROR: URL for rom list not working." )
 if 28 - 28: i11iIiiIii / iii11 . i11OOoO0ooOO0 / OoOoOo00o0
def OoOO ( ) :
 if I1i111I :
  oooO0 = wiz . openURL ( i1Ii ) . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
 iiIIiii = re . compile ( '.+?ame="(.+?)".+?rl="(.+?)".+?con="(.+?)".+?anart="(.+?)"description="(.+?)"' ) . findall ( oooO0 )
 if len ( iiIIiii ) > 0 :
  for ii11i , III11II1I1Ii1 , oO0o00oOOooO0 , OOOoO000 , O0oo0ooOOOO in iiIIiii :
   Ii1ii ( ii11i , 'rominstall' , ii11i , III11II1I1Ii1 , icon = oO0o00oOOooO0 , fanart = OOOoO000 , description = O0oo0ooOOOO , themeit = I111i1i1111 )
  else : wiz . log ( "[ROM Menu] ERROR: Invalid Format." )
 else : wiz . log ( "[ROM Menu] ERROR: URL for rom list not working." )
 if 32 - 32: OoO * Iii % OOOOoO0O0oo0 * oOoooo000Oo00 . I1
 if 48 - 48: o0o00 * o0o00
 if 13 - 13: oOoooo000Oo00 / ooo000ooO0000 + OoO . iii11 % OOOOoO0O0oo0
def IiIi1 ( ) :
 O0OOO0OOooo00 ( 'N64 Titles A Thru B' , 'n64a' , icon = iIIII1iIIii , themeit = I111i1i1111 )
 O0OOO0OOooo00 ( 'N64 Titles C Thru E' , 'n64c' , icon = ii1I1IiiI1ii1i , themeit = I111i1i1111 )
 O0OOO0OOooo00 ( 'N64 Titles F Thru J' , 'n64f' , icon = iIIII1iIIii , themeit = I111i1i1111 )
 O0OOO0OOooo00 ( 'N64 Titles K Thru M' , 'n64k' , icon = iIIII1iIIii , themeit = I111i1i1111 )
 O0OOO0OOooo00 ( 'N64 Titles N Thru R' , 'n64n' , icon = iIIII1iIIii , themeit = I111i1i1111 )
 O0OOO0OOooo00 ( 'N64 Titles S Thru T' , 'n64s' , icon = iIIII1iIIii , themeit = I111i1i1111 )
 O0OOO0OOooo00 ( 'N64 Titles V Thru Z' , 'n64v' , icon = iIIII1iIIii , themeit = I111i1i1111 )
 if 53 - 53: OoOo0oOooOoOO - IiI11iI1i1i1i
def oOoi1i ( ) :
 if Oo0oo0O0o00O :
  oooO0 = wiz . openURL ( OOO ) . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
 iiIIiii = re . compile ( '.+?ame="(.+?)".+?rl="(.+?)".+?con="(.+?)".+?anart="(.+?)"description="(.+?)"' ) . findall ( oooO0 )
 if len ( iiIIiii ) > 0 :
  for ii11i , III11II1I1Ii1 , oO0o00oOOooO0 , OOOoO000 , O0oo0ooOOOO in iiIIiii :
   Ii1ii ( ii11i , 'rominstall' , ii11i , III11II1I1Ii1 , icon = oO0o00oOOooO0 , fanart = OOOoO000 , description = O0oo0ooOOOO , themeit = I111i1i1111 )
  else : wiz . log ( "[ROM Menu] ERROR: Invalid Format." )
 else : wiz . log ( "[ROM Menu] ERROR: URL for rom list not working." )
 if 5 - 5: IiiII + I1 + I1 . I1Iiiiiii - OOOOoO0O0oo0
def o00oo0000 ( ) :
 if I1i11 :
  oooO0 = wiz . openURL ( oo0OOo0 ) . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
 iiIIiii = re . compile ( '.+?ame="(.+?)".+?rl="(.+?)".+?con="(.+?)".+?anart="(.+?)"description="(.+?)"' ) . findall ( oooO0 )
 if len ( iiIIiii ) > 0 :
  for ii11i , III11II1I1Ii1 , oO0o00oOOooO0 , OOOoO000 , O0oo0ooOOOO in iiIIiii :
   Ii1ii ( ii11i , 'rominstall' , ii11i , III11II1I1Ii1 , icon = oO0o00oOOooO0 , fanart = OOOoO000 , description = O0oo0ooOOOO , themeit = I111i1i1111 )
  else : wiz . log ( "[ROM Menu] ERROR: Invalid Format." )
 else : wiz . log ( "[ROM Menu] ERROR: URL for rom list not working." )
 if 44 - 44: I1iii11 % i11OOoO0ooOO0
def oo0ooO0 ( ) :
 if IiIi1I1 :
  oooO0 = wiz . openURL ( I11IiI ) . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
 iiIIiii = re . compile ( '.+?ame="(.+?)".+?rl="(.+?)".+?con="(.+?)".+?anart="(.+?)"description="(.+?)"' ) . findall ( oooO0 )
 if len ( iiIIiii ) > 0 :
  for ii11i , III11II1I1Ii1 , oO0o00oOOooO0 , OOOoO000 , O0oo0ooOOOO in iiIIiii :
   Ii1ii ( ii11i , 'rominstall' , ii11i , III11II1I1Ii1 , icon = oO0o00oOOooO0 , fanart = OOOoO000 , description = O0oo0ooOOOO , themeit = I111i1i1111 )
  else : wiz . log ( "[ROM Menu] ERROR: Invalid Format." )
 else : wiz . log ( "[ROM Menu] ERROR: URL for rom list not working." )
 if 28 - 28: IiiII * OoOo0oOooOoOO . OoOoOo00o0 / i11iIiiIii + IIII1i
def i1oOOOOOOOoO ( ) :
 if IiIIi1 :
  oooO0 = wiz . openURL ( O0ooO0Oo00o ) . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
 iiIIiii = re . compile ( '.+?ame="(.+?)".+?rl="(.+?)".+?con="(.+?)".+?anart="(.+?)"description="(.+?)"' ) . findall ( oooO0 )
 if len ( iiIIiii ) > 0 :
  for ii11i , III11II1I1Ii1 , oO0o00oOOooO0 , OOOoO000 , O0oo0ooOOOO in iiIIiii :
   Ii1ii ( ii11i , 'rominstall' , ii11i , III11II1I1Ii1 , icon = oO0o00oOOooO0 , fanart = OOOoO000 , description = O0oo0ooOOOO , themeit = I111i1i1111 )
  else : wiz . log ( "[ROM Menu] ERROR: Invalid Format." )
 else : wiz . log ( "[ROM Menu] ERROR: URL for rom list not working." )
 if 12 - 12: o0o00 . IiI11iI1i1i1i . OoO / I1
def OO0oOOo0o ( ) :
 if IIIIiii1IIii :
  oooO0 = wiz . openURL ( ooO0oOOooOo0 ) . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
 iiIIiii = re . compile ( '.+?ame="(.+?)".+?rl="(.+?)".+?con="(.+?)".+?anart="(.+?)"description="(.+?)"' ) . findall ( oooO0 )
 if len ( iiIIiii ) > 0 :
  for ii11i , III11II1I1Ii1 , oO0o00oOOooO0 , OOOoO000 , O0oo0ooOOOO in iiIIiii :
   Ii1ii ( ii11i , 'rominstall' , ii11i , III11II1I1Ii1 , icon = oO0o00oOOooO0 , fanart = OOOoO000 , description = O0oo0ooOOOO , themeit = I111i1i1111 )
  else : wiz . log ( "[ROM Menu] ERROR: Invalid Format." )
 else : wiz . log ( "[ROM Menu] ERROR: URL for rom list not working." )
 if 50 - 50: o0o00 . IiiII . ii * ooo000ooO0000 + OoOoOo00o0 % i11iIiiIii
def i1i1IiIiIi1Ii ( ) :
 if II1i11I :
  oooO0 = wiz . openURL ( i1I1ii11i1Iii ) . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
 iiIIiii = re . compile ( '.+?ame="(.+?)".+?rl="(.+?)".+?con="(.+?)".+?anart="(.+?)"description="(.+?)"' ) . findall ( oooO0 )
 if len ( iiIIiii ) > 0 :
  for ii11i , III11II1I1Ii1 , oO0o00oOOooO0 , OOOoO000 , O0oo0ooOOOO in iiIIiii :
   Ii1ii ( ii11i , 'rominstall' , ii11i , III11II1I1Ii1 , icon = oO0o00oOOooO0 , fanart = OOOoO000 , description = O0oo0ooOOOO , themeit = I111i1i1111 )
  else : wiz . log ( "[ROM Menu] ERROR: Invalid Format." )
 else : wiz . log ( "[ROM Menu] ERROR: URL for rom list not working." )
 if 64 - 64: Ii1IIIIi1ii1I + OoOo0oOooOoOO * OoOo0oOooOoOO
def i1I ( ) :
 if ii1I1IIii11 :
  oooO0 = wiz . openURL ( I1IiiiiI ) . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
 iiIIiii = re . compile ( '.+?ame="(.+?)".+?rl="(.+?)".+?con="(.+?)".+?anart="(.+?)"description="(.+?)"' ) . findall ( oooO0 )
 if len ( iiIIiii ) > 0 :
  for ii11i , III11II1I1Ii1 , oO0o00oOOooO0 , OOOoO000 , O0oo0ooOOOO in iiIIiii :
   Ii1ii ( ii11i , 'rominstall' , ii11i , III11II1I1Ii1 , icon = oO0o00oOOooO0 , fanart = OOOoO000 , description = O0oo0ooOOOO , themeit = I111i1i1111 )
  else : wiz . log ( "[ROM Menu] ERROR: Invalid Format." )
 else : wiz . log ( "[ROM Menu] ERROR: URL for rom list not working." )
 if 36 - 36: Iii * I1iii11
 if 77 - 77: IIII1i % oo00ooOoO00 - oOoooo000Oo00
 if 93 - 93: ii * I1iii11
def OO0ooo0o0 ( ) :
 O0OOO0OOooo00 ( 'PC Engine And Turbo Grafx Titles A Thru B' , 'tga' , icon = iIIII1iIIii , themeit = I111i1i1111 )
 O0OOO0OOooo00 ( 'PC Engine And Turbo Grafx Titles C Thru E' , 'tgc' , icon = ii1I1IiiI1ii1i , themeit = I111i1i1111 )
 O0OOO0OOooo00 ( 'PC Engine And Turbo Grafx Titles F Thru I' , 'tgf' , icon = iIIII1iIIii , themeit = I111i1i1111 )
 O0OOO0OOooo00 ( 'PC Engine And Turbo Grafx Titles J Thru M' , 'tgj' , icon = iIIII1iIIii , themeit = I111i1i1111 )
 O0OOO0OOooo00 ( 'PC Engine And Turbo Grafx Titles N Thru Q' , 'tgn' , icon = iIIII1iIIii , themeit = I111i1i1111 )
 O0OOO0OOooo00 ( 'PC Engine And Turbo Grafx Titles R Thru U' , 'tgr' , icon = iIIII1iIIii , themeit = I111i1i1111 )
 O0OOO0OOooo00 ( 'PC Engine And Turbo Grafx Titles V Thru Z' , 'tgv' , icon = iIIII1iIIii , themeit = I111i1i1111 )
 if 69 - 69: IiiII - I1Iiiiiii
def iiIIi1 ( ) :
 if O0o0oO :
  oooO0 = wiz . openURL ( o0OIiII ) . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
 iiIIiii = re . compile ( '.+?ame="(.+?)".+?rl="(.+?)".+?con="(.+?)".+?anart="(.+?)"description="(.+?)"' ) . findall ( oooO0 )
 if len ( iiIIiii ) > 0 :
  for ii11i , III11II1I1Ii1 , oO0o00oOOooO0 , OOOoO000 , O0oo0ooOOOO in iiIIiii :
   Ii1ii ( ii11i , 'rominstall' , ii11i , III11II1I1Ii1 , icon = oO0o00oOOooO0 , fanart = OOOoO000 , description = O0oo0ooOOOO , themeit = I111i1i1111 )
  else : wiz . log ( "[ROM Menu] ERROR: Invalid Format." )
 else : wiz . log ( "[ROM Menu] ERROR: URL for rom list not working." )
 if 10 - 10: ooo000ooO0000 * oOoooo000Oo00 % OoOo0oOooOoOO
def O0Oo0Ooo ( ) :
 if IIIIiIiIi1 :
  oooO0 = wiz . openURL ( ii1iII1II ) . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
 iiIIiii = re . compile ( '.+?ame="(.+?)".+?rl="(.+?)".+?con="(.+?)".+?anart="(.+?)"description="(.+?)"' ) . findall ( oooO0 )
 if len ( iiIIiii ) > 0 :
  for ii11i , III11II1I1Ii1 , oO0o00oOOooO0 , OOOoO000 , O0oo0ooOOOO in iiIIiii :
   Ii1ii ( ii11i , 'rominstall' , ii11i , III11II1I1Ii1 , icon = oO0o00oOOooO0 , fanart = OOOoO000 , description = O0oo0ooOOOO , themeit = I111i1i1111 )
  else : wiz . log ( "[ROM Menu] ERROR: Invalid Format." )
 else : wiz . log ( "[ROM Menu] ERROR: URL for rom list not working." )
 if 78 - 78: ii % IiI11iI1i1i1i * oo00ooOoO00
def O0iI ( ) :
 if I11iiiiI1i :
  oooO0 = wiz . openURL ( Iii1I1I11iiI1 ) . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
 iiIIiii = re . compile ( '.+?ame="(.+?)".+?rl="(.+?)".+?con="(.+?)".+?anart="(.+?)"description="(.+?)"' ) . findall ( oooO0 )
 if len ( iiIIiii ) > 0 :
  for ii11i , III11II1I1Ii1 , oO0o00oOOooO0 , OOOoO000 , O0oo0ooOOOO in iiIIiii :
   Ii1ii ( ii11i , 'rominstall' , ii11i , III11II1I1Ii1 , icon = oO0o00oOOooO0 , fanart = OOOoO000 , description = O0oo0ooOOOO , themeit = I111i1i1111 )
  else : wiz . log ( "[ROM Menu] ERROR: Invalid Format." )
 else : wiz . log ( "[ROM Menu] ERROR: URL for rom list not working." )
 if 15 - 15: I1 / I1iii11 % IiiII + iii11
def iiiIiI ( ) :
 if iI1i11 :
  oooO0 = wiz . openURL ( I1I1i1I ) . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
 iiIIiii = re . compile ( '.+?ame="(.+?)".+?rl="(.+?)".+?con="(.+?)".+?anart="(.+?)"description="(.+?)"' ) . findall ( oooO0 )
 if len ( iiIIiii ) > 0 :
  for ii11i , III11II1I1Ii1 , oO0o00oOOooO0 , OOOoO000 , O0oo0ooOOOO in iiIIiii :
   Ii1ii ( ii11i , 'rominstall' , ii11i , III11II1I1Ii1 , icon = oO0o00oOOooO0 , fanart = OOOoO000 , description = O0oo0ooOOOO , themeit = I111i1i1111 )
  else : wiz . log ( "[ROM Menu] ERROR: Invalid Format." )
 else : wiz . log ( "[ROM Menu] ERROR: URL for rom list not working." )
 if 9 - 9: i11OOoO0ooOO0 % IiiII . Ii1IIIIi1ii1I + OoOo0oOooOoOO
def Oo0o ( ) :
 if OoOOoooOO0O :
  oooO0 = wiz . openURL ( ii1I ) . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
 iiIIiii = re . compile ( '.+?ame="(.+?)".+?rl="(.+?)".+?con="(.+?)".+?anart="(.+?)"description="(.+?)"' ) . findall ( oooO0 )
 if len ( iiIIiii ) > 0 :
  for ii11i , III11II1I1Ii1 , oO0o00oOOooO0 , OOOoO000 , O0oo0ooOOOO in iiIIiii :
   Ii1ii ( ii11i , 'rominstall' , ii11i , III11II1I1Ii1 , icon = oO0o00oOOooO0 , fanart = OOOoO000 , description = O0oo0ooOOOO , themeit = I111i1i1111 )
  else : wiz . log ( "[ROM Menu] ERROR: Invalid Format." )
 else : wiz . log ( "[ROM Menu] ERROR: URL for rom list not working." )
 if 93 - 93: Ii1IIIIi1ii1I
def iIii1Ooo0oO0 ( ) :
 if ooo00Ooo :
  oooO0 = wiz . openURL ( O0oO0 ) . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
 iiIIiii = re . compile ( '.+?ame="(.+?)".+?rl="(.+?)".+?con="(.+?)".+?anart="(.+?)"description="(.+?)"' ) . findall ( oooO0 )
 if len ( iiIIiii ) > 0 :
  for ii11i , III11II1I1Ii1 , oO0o00oOOooO0 , OOOoO000 , O0oo0ooOOOO in iiIIiii :
   Ii1ii ( ii11i , 'rominstall' , ii11i , III11II1I1Ii1 , icon = oO0o00oOOooO0 , fanart = OOOoO000 , description = O0oo0ooOOOO , themeit = I111i1i1111 )
  else : wiz . log ( "[ROM Menu] ERROR: Invalid Format." )
 else : wiz . log ( "[ROM Menu] ERROR: URL for rom list not working." )
 if 86 - 86: I1
def O0o0oOooOoOo ( ) :
 if Oo0o0O00 :
  oooO0 = wiz . openURL ( oO0O0OO0O ) . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
 iiIIiii = re . compile ( '.+?ame="(.+?)".+?rl="(.+?)".+?con="(.+?)".+?anart="(.+?)"description="(.+?)"' ) . findall ( oooO0 )
 if len ( iiIIiii ) > 0 :
  for ii11i , III11II1I1Ii1 , oO0o00oOOooO0 , OOOoO000 , O0oo0ooOOOO in iiIIiii :
   Ii1ii ( ii11i , 'rominstall' , ii11i , III11II1I1Ii1 , icon = oO0o00oOOooO0 , fanart = OOOoO000 , description = O0oo0ooOOOO , themeit = I111i1i1111 )
  else : wiz . log ( "[ROM Menu] ERROR: Invalid Format." )
 else : wiz . log ( "[ROM Menu] ERROR: URL for rom list not working." )
 if 49 - 49: Ii1IIIIi1ii1I . IiiII . i11iIiiIii - OoOoOo00o0 / oOoooo000Oo00
 if 62 - 62: Ii1IIIIi1ii1I
 if 1 - 1: IiI11iI1i1i1i / IiI11iI1i1i1i - i11iIiiIii
def OO0oIiII1iiI ( ) :
 O0OOO0OOooo00 ( 'Nintendo DS Titles A' , 'ndsa' , icon = iIIII1iIIii , themeit = I111i1i1111 )
 O0OOO0OOooo00 ( 'Nintendo DS Titles B' , 'ndsb' , icon = iIIII1iIIii , themeit = I111i1i1111 )
 O0OOO0OOooo00 ( 'Nintendo DS Titles C' , 'ndsc' , icon = iIIII1iIIii , themeit = I111i1i1111 )
 O0OOO0OOooo00 ( 'Nintendo DS Titles D' , 'ndsd' , icon = iIIII1iIIii , themeit = I111i1i1111 )
 O0OOO0OOooo00 ( 'Nintendo DS Titles E Thru F' , 'ndse' , icon = iIIII1iIIii , themeit = I111i1i1111 )
 O0OOO0OOooo00 ( 'Nintendo DS Titles G Thru H' , 'ndsg' , icon = iIIII1iIIii , themeit = I111i1i1111 )
 O0OOO0OOooo00 ( 'Nintendo DS Titles I Thru J' , 'ndsi' , icon = iIIII1iIIii , themeit = I111i1i1111 )
 O0OOO0OOooo00 ( 'Nintendo DS Titles K Thru L' , 'ndsk' , icon = iIIII1iIIii , themeit = I111i1i1111 )
 O0OOO0OOooo00 ( 'Nintendo DS Titles M' , 'ndsm' , icon = iIIII1iIIii , themeit = I111i1i1111 )
 O0OOO0OOooo00 ( 'Nintendo DS Titles N Thru O' , 'ndsn' , icon = iIIII1iIIii , themeit = I111i1i1111 )
 O0OOO0OOooo00 ( 'Nintendo DS Titles P Thru Q' , 'ndsp' , icon = iIIII1iIIii , themeit = I111i1i1111 )
 O0OOO0OOooo00 ( 'Nintendo DS Titles R' , 'ndsr' , icon = iIIII1iIIii , themeit = I111i1i1111 )
 O0OOO0OOooo00 ( 'Nintendo DS Titles S' , 'ndss' , icon = iIIII1iIIii , themeit = I111i1i1111 )
 O0OOO0OOooo00 ( 'Nintendo DS Titles T Thru U' , 'ndst' , icon = iIIII1iIIii , themeit = I111i1i1111 )
 O0OOO0OOooo00 ( 'Nintendo DS Titles V Thru Z' , 'ndsv' , icon = iIIII1iIIii , themeit = I111i1i1111 )
 if 34 - 34: Iii . IIII1i + oo00ooOoO00
def OO000oOoo0O ( ) :
 if ii1I1i11 :
  oooO0 = wiz . openURL ( OO ) . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
 iiIIiii = re . compile ( '.+?ame="(.+?)".+?rl="(.+?)".+?con="(.+?)".+?anart="(.+?)"description="(.+?)"' ) . findall ( oooO0 )
 if len ( iiIIiii ) > 0 :
  for ii11i , III11II1I1Ii1 , oO0o00oOOooO0 , OOOoO000 , O0oo0ooOOOO in iiIIiii :
   Ii1ii ( ii11i , 'rominstall' , ii11i , III11II1I1Ii1 , icon = oO0o00oOOooO0 , fanart = OOOoO000 , description = O0oo0ooOOOO , themeit = I111i1i1111 )
  else : wiz . log ( "[ROM Menu] ERROR: Invalid Format." )
 else : wiz . log ( "[ROM Menu] ERROR: URL for rom list not working." )
 if 9 - 9: IIII1i * oo00ooOoO00 - oo00ooOoO00
def IiIiiI11i1Ii ( ) :
 if OOo0O0oo0OO0O :
  oooO0 = wiz . openURL ( OoOoO ) . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
 iiIIiii = re . compile ( '.+?ame="(.+?)".+?rl="(.+?)".+?con="(.+?)".+?anart="(.+?)"description="(.+?)"' ) . findall ( oooO0 )
 if len ( iiIIiii ) > 0 :
  for ii11i , III11II1I1Ii1 , oO0o00oOOooO0 , OOOoO000 , O0oo0ooOOOO in iiIIiii :
   Ii1ii ( ii11i , 'rominstall' , ii11i , III11II1I1Ii1 , icon = oO0o00oOOooO0 , fanart = OOOoO000 , description = O0oo0ooOOOO , themeit = I111i1i1111 )
  else : wiz . log ( "[ROM Menu] ERROR: Invalid Format." )
 else : wiz . log ( "[ROM Menu] ERROR: URL for rom list not working." )
 if 100 - 100: I1Iiiiiii . Iii * I1Iiiiiii - Iii . ooo000ooO0000 * oOoooo000Oo00
def oO000o ( ) :
 if OO0 :
  oooO0 = wiz . openURL ( Ii1I1i ) . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
 iiIIiii = re . compile ( '.+?ame="(.+?)".+?rl="(.+?)".+?con="(.+?)".+?anart="(.+?)"description="(.+?)"' ) . findall ( oooO0 )
 if len ( iiIIiii ) > 0 :
  for ii11i , III11II1I1Ii1 , oO0o00oOOooO0 , OOOoO000 , O0oo0ooOOOO in iiIIiii :
   Ii1ii ( ii11i , 'rominstall' , ii11i , III11II1I1Ii1 , icon = oO0o00oOOooO0 , fanart = OOOoO000 , description = O0oo0ooOOOO , themeit = I111i1i1111 )
  else : wiz . log ( "[ROM Menu] ERROR: Invalid Format." )
 else : wiz . log ( "[ROM Menu] ERROR: URL for rom list not working." )
 if 78 - 78: OoOo0oOooOoOO
def OOoo0 ( ) :
 if o0Oooo :
  oooO0 = wiz . openURL ( OOI1iI1ii1II ) . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
 iiIIiii = re . compile ( '.+?ame="(.+?)".+?rl="(.+?)".+?con="(.+?)".+?anart="(.+?)"description="(.+?)"' ) . findall ( oooO0 )
 if len ( iiIIiii ) > 0 :
  for ii11i , III11II1I1Ii1 , oO0o00oOOooO0 , OOOoO000 , O0oo0ooOOOO in iiIIiii :
   Ii1ii ( ii11i , 'rominstall' , ii11i , III11II1I1Ii1 , icon = oO0o00oOOooO0 , fanart = OOOoO000 , description = O0oo0ooOOOO , themeit = I111i1i1111 )
  else : wiz . log ( "[ROM Menu] ERROR: Invalid Format." )
 else : wiz . log ( "[ROM Menu] ERROR: URL for rom list not working." )
 if 36 - 36: iii11 + ooo000ooO0000 - IiI11iI1i1i1i + i11OOoO0ooOO0 + OoOo0oOooOoOO
def IiI1i111IiIiIi1 ( ) :
 if iiI :
  oooO0 = wiz . openURL ( O0O0OOOOoo ) . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
 iiIIiii = re . compile ( '.+?ame="(.+?)".+?rl="(.+?)".+?con="(.+?)".+?anart="(.+?)"description="(.+?)"' ) . findall ( oooO0 )
 if len ( iiIIiii ) > 0 :
  for ii11i , III11II1I1Ii1 , oO0o00oOOooO0 , OOOoO000 , O0oo0ooOOOO in iiIIiii :
   Ii1ii ( ii11i , 'rominstall' , ii11i , III11II1I1Ii1 , icon = oO0o00oOOooO0 , fanart = OOOoO000 , description = O0oo0ooOOOO , themeit = I111i1i1111 )
  else : wiz . log ( "[ROM Menu] ERROR: Invalid Format." )
 else : wiz . log ( "[ROM Menu] ERROR: URL for rom list not working." )
 if 39 - 39: ooo000ooO0000 - IiiII
def OOO0o0OO0OO ( ) :
 if oOIIiIi :
  oooO0 = wiz . openURL ( oOooO0 ) . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
 iiIIiii = re . compile ( '.+?ame="(.+?)".+?rl="(.+?)".+?con="(.+?)".+?anart="(.+?)"description="(.+?)"' ) . findall ( oooO0 )
 if len ( iiIIiii ) > 0 :
  for ii11i , III11II1I1Ii1 , oO0o00oOOooO0 , OOOoO000 , O0oo0ooOOOO in iiIIiii :
   Ii1ii ( ii11i , 'rominstall' , ii11i , III11II1I1Ii1 , icon = oO0o00oOOooO0 , fanart = OOOoO000 , description = O0oo0ooOOOO , themeit = I111i1i1111 )
  else : wiz . log ( "[ROM Menu] ERROR: Invalid Format." )
 else : wiz . log ( "[ROM Menu] ERROR: URL for rom list not working." )
 if 64 - 64: OoOoOo00o0
def iIIIiIi1I1i ( ) :
 if OOoOooOoOOOoo :
  oooO0 = wiz . openURL ( Ii1I1Ii ) . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
 iiIIiii = re . compile ( '.+?ame="(.+?)".+?rl="(.+?)".+?con="(.+?)".+?anart="(.+?)"description="(.+?)"' ) . findall ( oooO0 )
 if len ( iiIIiii ) > 0 :
  for ii11i , III11II1I1Ii1 , oO0o00oOOooO0 , OOOoO000 , O0oo0ooOOOO in iiIIiii :
   Ii1ii ( ii11i , 'rominstall' , ii11i , III11II1I1Ii1 , icon = oO0o00oOOooO0 , fanart = OOOoO000 , description = O0oo0ooOOOO , themeit = I111i1i1111 )
  else : wiz . log ( "[ROM Menu] ERROR: Invalid Format." )
 else : wiz . log ( "[ROM Menu] ERROR: URL for rom list not working." )
 if 78 - 78: i11OOoO0ooOO0 % OoO + IiiII / oo00ooOoO00 % OoOoOo00o0 + Ii1IIIIi1ii1I
def OooOOOO0O0 ( ) :
 if Iiii1iI1i :
  oooO0 = wiz . openURL ( OOoO0 ) . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
 iiIIiii = re . compile ( '.+?ame="(.+?)".+?rl="(.+?)".+?con="(.+?)".+?anart="(.+?)"description="(.+?)"' ) . findall ( oooO0 )
 if len ( iiIIiii ) > 0 :
  for ii11i , III11II1I1Ii1 , oO0o00oOOooO0 , OOOoO000 , O0oo0ooOOOO in iiIIiii :
   Ii1ii ( ii11i , 'rominstall' , ii11i , III11II1I1Ii1 , icon = oO0o00oOOooO0 , fanart = OOOoO000 , description = O0oo0ooOOOO , themeit = I111i1i1111 )
  else : wiz . log ( "[ROM Menu] ERROR: Invalid Format." )
 else : wiz . log ( "[ROM Menu] ERROR: URL for rom list not working." )
 if 38 - 38: I1Iiiiiii % Ii1IIIIi1ii1I - OoOo0oOooOoOO
def oOo0OOoooO ( ) :
 if I1ii1ii11i1I :
  oooO0 = wiz . openURL ( OO0Oooo0oOO0O ) . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
 iiIIiii = re . compile ( '.+?ame="(.+?)".+?rl="(.+?)".+?con="(.+?)".+?anart="(.+?)"description="(.+?)"' ) . findall ( oooO0 )
 if len ( iiIIiii ) > 0 :
  for ii11i , III11II1I1Ii1 , oO0o00oOOooO0 , OOOoO000 , O0oo0ooOOOO in iiIIiii :
   Ii1ii ( ii11i , 'rominstall' , ii11i , III11II1I1Ii1 , icon = oO0o00oOOooO0 , fanart = OOOoO000 , description = O0oo0ooOOOO , themeit = I111i1i1111 )
  else : wiz . log ( "[ROM Menu] ERROR: Invalid Format." )
 else : wiz . log ( "[ROM Menu] ERROR: URL for rom list not working." )
 if 26 - 26: iii11 * IiI11iI1i1i1i . oo00ooOoO00
def ooOoOO ( ) :
 if o0OoOO :
  oooO0 = wiz . openURL ( o00O0 ) . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
 iiIIiii = re . compile ( '.+?ame="(.+?)".+?rl="(.+?)".+?con="(.+?)".+?anart="(.+?)"description="(.+?)"' ) . findall ( oooO0 )
 if len ( iiIIiii ) > 0 :
  for ii11i , III11II1I1Ii1 , oO0o00oOOooO0 , OOOoO000 , O0oo0ooOOOO in iiIIiii :
   Ii1ii ( ii11i , 'rominstall' , ii11i , III11II1I1Ii1 , icon = oO0o00oOOooO0 , fanart = OOOoO000 , description = O0oo0ooOOOO , themeit = I111i1i1111 )
  else : wiz . log ( "[ROM Menu] ERROR: Invalid Format." )
 else : wiz . log ( "[ROM Menu] ERROR: URL for rom list not working." )
 if 56 - 56: i11OOoO0ooOO0 . i11iIiiIii - Ii1IIIIi1ii1I * OoOoOo00o0 * I1Iiiiiii
def i1I1 ( ) :
 if O0O0Oo00 :
  oooO0 = wiz . openURL ( oOO0O00Oo0O0o ) . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
 iiIIiii = re . compile ( '.+?ame="(.+?)".+?rl="(.+?)".+?con="(.+?)".+?anart="(.+?)"description="(.+?)"' ) . findall ( oooO0 )
 if len ( iiIIiii ) > 0 :
  for ii11i , III11II1I1Ii1 , oO0o00oOOooO0 , OOOoO000 , O0oo0ooOOOO in iiIIiii :
   Ii1ii ( ii11i , 'rominstall' , ii11i , III11II1I1Ii1 , icon = oO0o00oOOooO0 , fanart = OOOoO000 , description = O0oo0ooOOOO , themeit = I111i1i1111 )
  else : wiz . log ( "[ROM Menu] ERROR: Invalid Format." )
 else : wiz . log ( "[ROM Menu] ERROR: URL for rom list not working." )
 if 60 - 60: OoO / I1Iiiiiii - OoOoOo00o0 . I1iii11 + I1
def Ii1iI ( ) :
 if oOoO00o :
  oooO0 = wiz . openURL ( ii1 ) . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
 iiIIiii = re . compile ( '.+?ame="(.+?)".+?rl="(.+?)".+?con="(.+?)".+?anart="(.+?)"description="(.+?)"' ) . findall ( oooO0 )
 if len ( iiIIiii ) > 0 :
  for ii11i , III11II1I1Ii1 , oO0o00oOOooO0 , OOOoO000 , O0oo0ooOOOO in iiIIiii :
   Ii1ii ( ii11i , 'rominstall' , ii11i , III11II1I1Ii1 , icon = oO0o00oOOooO0 , fanart = OOOoO000 , description = O0oo0ooOOOO , themeit = I111i1i1111 )
  else : wiz . log ( "[ROM Menu] ERROR: Invalid Format." )
 else : wiz . log ( "[ROM Menu] ERROR: URL for rom list not working." )
 if 53 - 53: i11OOoO0ooOO0 - IIII1i % OoO * I1Iiiiiii % OOOOoO0O0oo0
def II1Ii ( ) :
 if oO00O0 :
  oooO0 = wiz . openURL ( I1iIIiiIIi1i ) . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
 iiIIiii = re . compile ( '.+?ame="(.+?)".+?rl="(.+?)".+?con="(.+?)".+?anart="(.+?)"description="(.+?)"' ) . findall ( oooO0 )
 if len ( iiIIiii ) > 0 :
  for ii11i , III11II1I1Ii1 , oO0o00oOOooO0 , OOOoO000 , O0oo0ooOOOO in iiIIiii :
   Ii1ii ( ii11i , 'rominstall' , ii11i , III11II1I1Ii1 , icon = oO0o00oOOooO0 , fanart = OOOoO000 , description = O0oo0ooOOOO , themeit = I111i1i1111 )
  else : wiz . log ( "[ROM Menu] ERROR: Invalid Format." )
 else : wiz . log ( "[ROM Menu] ERROR: URL for rom list not working." )
 if 57 - 57: OoO - IIII1i / OOOOoO0O0oo0 % i11iIiiIii
def I11oOOooo ( ) :
 if IIi1IIIi :
  oooO0 = wiz . openURL ( O0O0ooOOO ) . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
 iiIIiii = re . compile ( '.+?ame="(.+?)".+?rl="(.+?)".+?con="(.+?)".+?anart="(.+?)"description="(.+?)"' ) . findall ( oooO0 )
 if len ( iiIIiii ) > 0 :
  for ii11i , III11II1I1Ii1 , oO0o00oOOooO0 , OOOoO000 , O0oo0ooOOOO in iiIIiii :
   Ii1ii ( ii11i , 'rominstall' , ii11i , III11II1I1Ii1 , icon = oO0o00oOOooO0 , fanart = OOOoO000 , description = O0oo0ooOOOO , themeit = I111i1i1111 )
  else : wiz . log ( "[ROM Menu] ERROR: Invalid Format." )
 else : wiz . log ( "[ROM Menu] ERROR: URL for rom list not working." )
 if 80 - 80: Iii - i11iIiiIii
def oOoooO000O ( ) :
 if O00Ooo :
  oooO0 = wiz . openURL ( oOOo0O00o ) . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
 iiIIiii = re . compile ( '.+?ame="(.+?)".+?rl="(.+?)".+?con="(.+?)".+?anart="(.+?)"description="(.+?)"' ) . findall ( oooO0 )
 if len ( iiIIiii ) > 0 :
  for ii11i , III11II1I1Ii1 , oO0o00oOOooO0 , OOOoO000 , O0oo0ooOOOO in iiIIiii :
   Ii1ii ( ii11i , 'rominstall' , ii11i , III11II1I1Ii1 , icon = oO0o00oOOooO0 , fanart = OOOoO000 , description = O0oo0ooOOOO , themeit = I111i1i1111 )
  else : wiz . log ( "[ROM Menu] ERROR: Invalid Format." )
 else : wiz . log ( "[ROM Menu] ERROR: URL for rom list not working." )
 if 49 - 49: iii11 * oOoooo000Oo00 + ooo000ooO0000 + o0o00
 if 30 - 30: iii11 / Ii1IIIIi1ii1I / IiI11iI1i1i1i % OOOOoO0O0oo0 + OoOoOo00o0
 if 4 - 4: o0o00 - I1iii11 - IiI11iI1i1i1i - ooo000ooO0000 % i11iIiiIii / ii
 if 50 - 50: OOOOoO0O0oo0 + oo00ooOoO00
def i11IiIIi11I ( ) :
 o000o0O0Oo00 = '[COLOR green]ON[/COLOR]' ; ooOOoOo = '[COLOR red]OFF[/COLOR]'
 oooOiiIIi = 'true' if I11 == 'true' else 'false'
 i1iiIIiI1iiI = 'true' if Oo0o0000o0o0 == 'true' else 'false'
 I11Ii111I = 'true' if oOo0oooo00o == 'true' else 'false'
 if 98 - 98: i11OOoO0ooOO0 + I1Iiiiiii % OoO + ooo000ooO0000 % OoO
 oo00O00oO000o ( 'Fresh Start' , 'freshstart' , icon = iIi1Ii1i1iI , themeit = I111i1i1111 )
 oo00O00oO000o ( 'Clear Cache' , 'clearcache' , icon = iIi1Ii1i1iI , themeit = I111i1i1111 )
 oo00O00oO000o ( 'Clear Packages' , 'clearpackages' , icon = iIi1Ii1i1iI , themeit = I111i1i1111 )
 oo00O00oO000o ( 'Clear Thumbnails' , 'clearthumb' , icon = iIi1Ii1i1iI , themeit = I111i1i1111 )
 oo00O00oO000o ( 'Purge Databases' , 'purgedb' , icon = iIi1Ii1i1iI , themeit = I111i1i1111 )
 O0OOO0OOooo00 ( 'Remove Addons' , 'removeaddons' , icon = iIi1Ii1i1iI , themeit = I111i1i1111 )
 O0OOO0OOooo00 ( 'Remove Addon Data' , 'removeaddondata' , icon = iIi1Ii1i1iI , themeit = I111i1i1111 )
 oo00O00oO000o ( 'Force Update Addons' , 'forceupdate' , icon = iIi1Ii1i1iI , themeit = I111i1i1111 )
 oo00O00oO000o ( 'Force Close Kodi' , 'forceclose' , icon = iIi1Ii1i1iI , themeit = I111i1i1111 )
 oo00O00oO000o ( 'Upload Kodi log' , 'uploadlog' , icon = iIi1Ii1i1iI , themeit = I111i1i1111 )
 oo00O00oO000o ( 'View Kodi Log File' , 'viewlog' , icon = iIi1Ii1i1iI , themeit = I111i1i1111 )
 oo00O00oO000o ( 'View Wizard Log File' , 'viewwizlog' , icon = iIi1Ii1i1iI , themeit = I111i1i1111 )
 oo00O00oO000o ( 'Clear Wizard Log File' , 'clearwizlog' , icon = iIi1Ii1i1iI , themeit = I111i1i1111 )
 oo00O00oO000o ( '==============[ Auto Clean ]==============' , '' , fanart = I1i1iiI1 , icon = iIi1Ii1i1iI , themeit = I1I1i )
 oo00O00oO000o ( 'Auto Clean Up On Startup: %s' % oooOiiIIi . replace ( 'true' , o000o0O0Oo00 ) . replace ( 'false' , ooOOoOo ) , 'togglesetting' , 'autoclean' , icon = iIi1Ii1i1iI , themeit = I111i1i1111 )
 if oooOiiIIi == 'true' :
  oo00O00oO000o ( '--- Clear Cache on Startup: %s' % i1iiIIiI1iiI . replace ( 'true' , o000o0O0Oo00 ) . replace ( 'false' , ooOOoOo ) , 'togglesetting' , 'clearcache' , icon = iIi1Ii1i1iI , themeit = I111i1i1111 )
  oo00O00oO000o ( '--- Clear Packages on Startup: %s' % I11Ii111I . replace ( 'true' , o000o0O0Oo00 ) . replace ( 'false' , ooOOoOo ) , 'togglesetting' , 'clearpackages' , icon = iIi1Ii1i1iI , themeit = I111i1i1111 )
 OOo00OoO ( 'movies' , 'MAIN' )
 if 24 - 24: IIII1i * I1Iiiiiii
 if 40 - 40: oOoooo000Oo00 - OoO * OoO . OoO + OoOo0oOooOoOO
 if 77 - 77: i11OOoO0ooOO0 . oOoooo000Oo00 % IIII1i / oOoooo000Oo00
 if 54 - 54: IIII1i + OOOOoO0O0oo0 - I1iii11
def I1I1IiIi1 ( ) :
 if oO0o00oo0 :
  oooO0 = wiz . openURL ( Oo0oOOo ) . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
 iiIIiii = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?con="(.+?)".+?anart="(.+?)"' ) . findall ( oooO0 )
 if len ( iiIIiii ) > 0 :
  for ii11i , III11II1I1Ii1 , oO0o00oOOooO0 , OOOoO000 in iiIIiii :
   oo00O00oO000o ( ii11i , 'speedtest' , ii11i , III11II1I1Ii1 , icon = oO0o00oOOooO0 , fanart = OOOoO000 , themeit = I111i1i1111 )
  else : wiz . log ( "[APK Menu] ERROR: Invalid Format." )
 else : wiz . log ( "[APK Menu] ERROR: URL for apk list not working." )
 if 58 - 58: OoO - o0o00 - OoOo0oOooOoOO
 if 96 - 96: i11OOoO0ooOO0
 if 82 - 82: OoO + I1 - IiI11iI1i1i1i % IIII1i * i11iIiiIii
 if 15 - 15: iii11
def I1iI ( ) :
 o000o0O0Oo00 = '[COLOR green]ON[/COLOR]' ; ooOOoOo = '[COLOR red]OFF[/COLOR]'
 oO0Ooo0OooOOo = 'true' if oOOoO0 == 'true' else 'false'
 O00o0O = 'true' if O0OoO000O0OO == 'true' else 'false'
 iIIIiI = 'true' if iI111I11I1I1 == 'true' else 'false'
 O00 = 'true' if iIii1 == 'true' else 'false'
 i1iiIII1IIiIIII = 'true' if OOooO0OOoo == 'true' else 'false'
 I1iIIII1 = 'true' if i1iIIi1 == 'true' else 'false'
 iIi1II = 'true' if ii11iIi1I == 'true' else 'false'
 if 57 - 57: OoO . i11OOoO0ooOO0 % OOOOoO0O0oo0 % oOoooo000Oo00 * OoO
 O0OOO0OOooo00 ( 'Keep Trakt Data' , 'trakt' , icon = oO0OoO00o , themeit = I111i1i1111 )
 O0OOO0OOooo00 ( 'Keep Real Debrid' , 'realdebrid' , icon = oO0OoO00o , themeit = I111i1i1111 )
 oo00O00oO000o ( '- Click to toggle settings -' , '' , themeit = I1I1i )
 oo00O00oO000o ( 'Save Trakt: %s' % oO0Ooo0OooOOo . replace ( 'true' , o000o0O0Oo00 ) . replace ( 'false' , ooOOoOo ) , 'togglesetting' , 'keeptrakt' , icon = oO0OoO00o , themeit = I111i1i1111 )
 oo00O00oO000o ( 'Save Real Debrid: %s' % O00o0O . replace ( 'true' , o000o0O0Oo00 ) . replace ( 'false' , ooOOoOo ) , 'togglesetting' , 'keepdebrid' , icon = oO0OoO00o , themeit = I111i1i1111 )
 oo00O00oO000o ( 'Keep \'Sources.xml\': %s' % iIIIiI . replace ( 'true' , o000o0O0Oo00 ) . replace ( 'false' , ooOOoOo ) , 'togglesetting' , 'keepsources' , icon = oO0OoO00o , themeit = I111i1i1111 )
 oo00O00oO000o ( 'Keep \'Profiles.xml\': %s' % i1iiIII1IIiIIII . replace ( 'true' , o000o0O0Oo00 ) . replace ( 'false' , ooOOoOo ) , 'togglesetting' , 'keepprofiles' , icon = oO0OoO00o , themeit = I111i1i1111 )
 oo00O00oO000o ( 'Keep \'Advancedsettings.xml\': %s' % O00 . replace ( 'true' , o000o0O0Oo00 ) . replace ( 'false' , ooOOoOo ) , 'togglesetting' , 'keepadvanced' , icon = oO0OoO00o , themeit = I111i1i1111 )
 oo00O00oO000o ( 'Keep \'Favourites.xml\': %s' % I1iIIII1 . replace ( 'true' , o000o0O0Oo00 ) . replace ( 'false' , ooOOoOo ) , 'togglesetting' , 'keepfavourites' , icon = oO0OoO00o , themeit = I111i1i1111 )
 oo00O00oO000o ( 'Keep \'Guisettings.xml\': %s' % iIi1II . replace ( 'true' , o000o0O0Oo00 ) . replace ( 'false' , ooOOoOo ) , 'togglesetting' , 'keepgui' , icon = oO0OoO00o , themeit = I111i1i1111 )
 if 8 - 8: OoO . OOOOoO0O0oo0 % IIII1i . Iii % Iii . oOoooo000Oo00
 if 47 - 47: ooo000ooO0000 + OOOOoO0O0oo0 + OoOoOo00o0 % i11iIiiIii
def OOoOoo00Oo ( ) :
 oO0Ooo0OooOOo = '[COLOR green]ON[/COLOR]' if oOOoO0 == 'true' else '[COLOR red]OFF[/COLOR]'
 Iiii1iiiIiI1 = str ( oooOOOOO ) if not oooOOOOO == '' else 'Trakt hasnt been saved yet.'
 oo00O00oO000o ( '[I]Register FREE Account at http://trakt.tv[/I]' , '' , icon = O0OoOO0oo0 , themeit = I1I1i )
 oo00O00oO000o ( 'Save Trakt Data: %s' % oO0Ooo0OooOOo , 'togglesetting' , 'keeptrakt' , icon = O0OoOO0oo0 , themeit = I1I1i )
 if oOOoO0 == 'true' : oo00O00oO000o ( 'Last Save: %s' % str ( Iiii1iiiIiI1 ) , '' , icon = O0OoOO0oo0 , themeit = I1I1i )
 if Ii1II1I11i1 == 'No' : oo00O00oO000o ( '============================================' , '' , icon = O0OoOO0oo0 , themeit = I1I1i )
 I11Iii1 = os . path . join ( OOOo0 , IIiiiiiiIi1I1 , 'icon.png' ) if os . path . exists ( IIIii1II1II ) else O0OoOO0oo0
 i1iIIi1II1iiI = os . path . join ( OOOo0 , IIiiiiiiIi1I1 , 'fanart.jpg' ) if os . path . exists ( IIIii1II1II ) else I1i1iiI1
 oo00O00oO000o ( '[+]-- Exodus' , '' , icon = I11Iii1 , fanart = i1iIIi1II1iiI , themeit = I1I1i )
 oOOOO = Ii ( 'traktaddon' , 'Exodus' ) ; III1Ii1i1I1 = Ii ( 'trakt' , 'Exodus' )
 if not os . path . exists ( IIIii1II1II ) : oo00O00oO000o ( '[COLOR red]Addon Data: Not Installed[/COLOR]' , '' , icon = I11Iii1 , fanart = i1iIIi1II1iiI , menu = oOOOO )
 elif not traktit . traktUser ( 'exodus' ) : oo00O00oO000o ( '[COLOR red]Addon Data: Not Registered[/COLOR]' , 'authtrakt' , 'exodus' , icon = I11Iii1 , fanart = i1iIIi1II1iiI , menu = oOOOO )
 else : oo00O00oO000o ( '[COLOR green]Addon Data: %s[/COLOR]' % traktit . traktUser ( 'exodus' ) , 'authtrakt' , 'exodus' , icon = I11Iii1 , fanart = i1iIIi1II1iiI , menu = oOOOO )
 if iiI1IiI == "" : oo00O00oO000o ( '[COLOR red]Saved Data: Not Saved[/COLOR]' , 'savetrakt' , 'exodus' , icon = I11Iii1 , fanart = i1iIIi1II1iiI , menu = III1Ii1i1I1 )
 else : oo00O00oO000o ( '[COLOR green]Saved Data: %s[/COLOR]' % iiI1IiI , '' , icon = I11Iii1 , fanart = i1iIIi1II1iiI , menu = III1Ii1i1I1 )
 O0O00OooO = os . path . join ( OOOo0 , OOOO , 'icon.png' ) if os . path . exists ( O000oo0O ) else O0OoOO0oo0
 I1IiI1iI11 = os . path . join ( OOOo0 , OOOO , 'fanart.jpg' ) if os . path . exists ( O000oo0O ) else I1i1iiI1
 oo00O00oO000o ( '[+]-- Salts' , '' , icon = O0O00OooO , fanart = I1IiI1iI11 , themeit = I1I1i )
 oOOOO = Ii ( 'traktaddon' , 'Salts' ) ; III1Ii1i1I1 = Ii ( 'trakt' , 'Salts' )
 if not os . path . exists ( O000oo0O ) : oo00O00oO000o ( '[COLOR red]Addon Data: Not Installed[/COLOR]' , '' , icon = O0O00OooO , fanart = I1IiI1iI11 , menu = oOOOO )
 elif not traktit . traktUser ( 'salts' ) : oo00O00oO000o ( '[COLOR red]Addon Data: Not Registered[/COLOR]' , 'authtrakt' , 'salts' , icon = O0O00OooO , fanart = I1IiI1iI11 , menu = oOOOO )
 else : oo00O00oO000o ( '[COLOR green]Addon Data: %s[/COLOR]' % traktit . traktUser ( 'salts' ) , 'authtrakt' , 'salts' , icon = O0O00OooO , fanart = I1IiI1iI11 , menu = oOOOO )
 if II == "" : oo00O00oO000o ( '[COLOR red]Saved Data: Not Saved[/COLOR]' , 'savetrakt' , 'salts' , icon = O0O00OooO , fanart = I1IiI1iI11 , menu = III1Ii1i1I1 )
 else : oo00O00oO000o ( '[COLOR green]Saved Data: %s[/COLOR]' % II , '' , icon = O0O00OooO , fanart = I1IiI1iI11 , menu = III1Ii1i1I1 )
 iIi = os . path . join ( OOOo0 , OOO00 , 'icon.png' ) if os . path . exists ( OOOOi11i1 ) else O0OoOO0oo0
 iiO0O0o0oO0O00 = os . path . join ( OOOo0 , OOO00 , 'fanart.jpg' ) if os . path . exists ( OOOOi11i1 ) else I1i1iiI1
 oo00O00oO000o ( '[+]-- Salts HD' , '' , icon = iIi , fanart = iiO0O0o0oO0O00 , themeit = I1I1i )
 oOOOO = Ii ( 'traktaddon' , 'Salts HD' ) ; III1Ii1i1I1 = Ii ( 'trakt' , 'Salts HD' )
 if not os . path . exists ( OOOOi11i1 ) : oo00O00oO000o ( '[COLOR red]Addon Data: Not Installed[/COLOR]' , '' , icon = iIi , fanart = iiO0O0o0oO0O00 , menu = oOOOO )
 elif not traktit . traktUser ( 'saltshd' ) : oo00O00oO000o ( '[COLOR red]Addon Data: Not Registered[/COLOR]' , 'authtrakt' , 'saltshd' , icon = iIi , fanart = iiO0O0o0oO0O00 , menu = oOOOO )
 else : oo00O00oO000o ( '[COLOR green]Addon Data: %s[/COLOR]' % traktit . traktUser ( 'saltshd' ) , 'authtrakt' , 'saltshd' , icon = iIi , fanart = iiO0O0o0oO0O00 , menu = oOOOO )
 if ooOoOoo0O == "" : oo00O00oO000o ( '[COLOR red]Saved Data: Not Saved[/COLOR]' , 'savetrakt' , 'saltshd' , icon = iIi , fanart = iiO0O0o0oO0O00 , menu = III1Ii1i1I1 )
 else : oo00O00oO000o ( '[COLOR green]Saved Data: %s[/COLOR]' % ooOoOoo0O , '' , icon = iIi , fanart = iiO0O0o0oO0O00 , menu = III1Ii1i1I1 )
 o0O0oO0 = os . path . join ( OOOo0 , iiiiiIIii , 'icon.png' ) if os . path . exists ( o0OO00oO ) else O0OoOO0oo0
 oo0 = os . path . join ( OOOo0 , iiiiiIIii , 'fanart.jpg' ) if os . path . exists ( o0OO00oO ) else I1i1iiI1
 oo00O00oO000o ( '[+]-- Royal We' , '' , icon = o0O0oO0 , fanart = oo0 , themeit = I1I1i )
 oOOOO = Ii ( 'traktaddon' , 'Royal We' ) ; III1Ii1i1I1 = Ii ( 'trakt' , 'Royal We' )
 if not os . path . exists ( o0OO00oO ) : oo00O00oO000o ( '[COLOR red]Addon Data: Not Installed[/COLOR]' , '' , icon = o0O0oO0 , fanart = oo0 , menu = oOOOO )
 elif not traktit . traktUser ( 'royalwe' ) : oo00O00oO000o ( '[COLOR red]Addon Data: Not Registered[/COLOR]' , 'authtrakt' , 'royalwe' , icon = o0O0oO0 , fanart = oo0 , menu = oOOOO )
 else : oo00O00oO000o ( '[COLOR green]Addon Data: %s[/COLOR]' % traktit . traktUser ( 'royalwe' ) , 'authtrakt' , 'royalwe' , icon = o0O0oO0 , fanart = oo0 , menu = oOOOO )
 if OooO0 == "" : oo00O00oO000o ( '[COLOR red]Saved Data: Not Saved[/COLOR]' , 'savetrakt' , 'royalwe' , icon = o0O0oO0 , fanart = oo0 , menu = III1Ii1i1I1 )
 else : oo00O00oO000o ( '[COLOR green]Saved Data: %s[/COLOR]' % OooO0 , '' , icon = o0O0oO0 , fanart = oo0 , menu = III1Ii1i1I1 )
 i1i1IiIi1 = os . path . join ( OOOo0 , I1IIIii , 'icon.png' ) if os . path . exists ( i1I1iI ) else O0OoOO0oo0
 I1iiIiI1iI1I = os . path . join ( OOOo0 , I1IIIii , 'fanart.jpg' ) if os . path . exists ( i1I1iI ) else I1i1iiI1
 oo00O00oO000o ( '[+]-- Velocity' , '' , icon = i1i1IiIi1 , fanart = I1iiIiI1iI1I , themeit = I1I1i )
 oOOOO = Ii ( 'traktaddon' , 'Velocity' ) ; III1Ii1i1I1 = Ii ( 'trakt' , 'Velocity' )
 if not os . path . exists ( i1I1iI ) : oo00O00oO000o ( '[COLOR red]Addon Data: Not Installed[/COLOR]' , '' , icon = i1i1IiIi1 , fanart = I1iiIiI1iI1I , menu = oOOOO )
 elif not traktit . traktUser ( 'velocity' ) : oo00O00oO000o ( '[COLOR red]Addon Data: Not Registered[/COLOR]' , 'authtrakt' , 'velocity' , icon = i1i1IiIi1 , fanart = I1iiIiI1iI1I , menu = oOOOO )
 else : oo00O00oO000o ( '[COLOR green]Addon Data: %s[/COLOR]' % traktit . traktUser ( 'velocity' ) , 'authtrakt' , 'velocity' , icon = i1i1IiIi1 , fanart = I1iiIiI1iI1I , menu = oOOOO )
 if II11iiii1Ii == "" : oo00O00oO000o ( '[COLOR red]Saved Data: Not Saved[/COLOR]' , 'savetrakt' , 'velocity' , icon = i1i1IiIi1 , fanart = I1iiIiI1iI1I , menu = III1Ii1i1I1 )
 else : oo00O00oO000o ( '[COLOR green]Saved Data: %s[/COLOR]' % II11iiii1Ii , '' , icon = i1i1IiIi1 , fanart = I1iiIiI1iI1I , menu = III1Ii1i1I1 )
 III1II111Ii1 = os . path . join ( OOOo0 , oOoOooOo0o0 , 'icon.png' ) if os . path . exists ( oo0OooOOo0 ) else O0OoOO0oo0
 o0O0OO0o = os . path . join ( OOOo0 , oOoOooOo0o0 , 'fanart.jpg' ) if os . path . exists ( oo0OooOOo0 ) else I1i1iiI1
 oo00O00oO000o ( '[+]-- Velocity Kids' , '' , icon = III1II111Ii1 , fanart = o0O0OO0o , themeit = I1I1i )
 oOOOO = Ii ( 'traktaddon' , 'Velocity Kids' ) ; III1Ii1i1I1 = Ii ( 'trakt' , 'Velocity Kids' )
 if not os . path . exists ( oo0OooOOo0 ) : oo00O00oO000o ( '[COLOR red]Addon Data: Not Installed[/COLOR]' , '' , icon = III1II111Ii1 , fanart = o0O0OO0o , menu = oOOOO )
 elif not traktit . traktUser ( 'velocitykids' ) : oo00O00oO000o ( '[COLOR red]Addon Data: Not Registered[/COLOR]' , 'authtrakt' , 'velocitykids' , icon = III1II111Ii1 , fanart = o0O0OO0o , menu = oOOOO )
 else : oo00O00oO000o ( '[COLOR green]Addon Data: %s[/COLOR]' % traktit . traktUser ( 'velocitykids' ) , 'authtrakt' , 'velocitykids' , icon = III1II111Ii1 , fanart = o0O0OO0o , menu = oOOOO )
 if OO0oOoo == "" : oo00O00oO000o ( '[COLOR red]Saved Data: Not Saved[/COLOR]' , 'savetrakt' , 'velocitykids' , icon = III1II111Ii1 , fanart = o0O0OO0o , menu = III1Ii1i1I1 )
 else : oo00O00oO000o ( '[COLOR green]Saved Data: %s[/COLOR]' % OO0oOoo , '' , icon = III1II111Ii1 , fanart = o0O0OO0o , menu = III1Ii1i1I1 )
 OOOoOo = os . path . join ( OOOo0 , O000OO0 , 'icon.png' ) if os . path . exists ( I11i1I1I ) else O0OoOO0oo0
 OOoO0oo0O = os . path . join ( OOOo0 , O000OO0 , 'fanart.jpg' ) if os . path . exists ( I11i1I1I ) else I1i1iiI1
 oo00O00oO000o ( '[+]-- Specto' , '' , icon = OOOoOo , fanart = OOoO0oo0O , themeit = I1I1i )
 oOOOO = Ii ( 'traktaddon' , 'Specto' ) ; III1Ii1i1I1 = Ii ( 'trakt' , 'Specto' )
 if not os . path . exists ( I11i1I1I ) : oo00O00oO000o ( '[COLOR red]Addon Data: Not Installed[/COLOR]' , '' , icon = OOOoOo , fanart = OOoO0oo0O , menu = oOOOO )
 elif not traktit . traktUser ( 'specto' ) : oo00O00oO000o ( '[COLOR red]Addon Data: Not Registered[/COLOR]' , 'authtrakt' , 'specto' , icon = OOOoOo , fanart = OOoO0oo0O , menu = oOOOO )
 else : oo00O00oO000o ( '[COLOR green]Addon Data: %s[/COLOR]' % traktit . traktUser ( 'specto' ) , 'authtrakt' , 'specto' , icon = OOOoOo , fanart = OOoO0oo0O , menu = oOOOO )
 if O0o0Oo == "" : oo00O00oO000o ( '[COLOR red]Saved Data: Not Saved[/COLOR]' , 'savetrakt' , 'specto' , icon = OOOoOo , fanart = OOoO0oo0O , menu = III1Ii1i1I1 )
 else : oo00O00oO000o ( '[COLOR green]Saved Data: %s[/COLOR]' % O0o0Oo , '' , icon = OOOoOo , fanart = OOoO0oo0O , menu = III1Ii1i1I1 )
 iiI1I1ii = os . path . join ( OOOo0 , I11iii1Ii , 'icon.png' ) if os . path . exists ( oO0Oo ) else O0OoOO0oo0
 o00IiI1iiII1i1i = os . path . join ( OOOo0 , I11iii1Ii , 'fanart.jpg' ) if os . path . exists ( oO0Oo ) else I1i1iiI1
 oo00O00oO000o ( '[+]-- Trakt' , '' , icon = III1II111Ii1 , fanart = o00IiI1iiII1i1i , themeit = I1I1i )
 oOOOO = Ii ( 'traktaddon' , 'Trakt' ) ; III1Ii1i1I1 = Ii ( 'trakt' , 'Trakt' )
 if not os . path . exists ( oO0Oo ) : oo00O00oO000o ( '[COLOR red]Addon Data: Not Installed[/COLOR]' , '' , icon = iiI1I1ii , fanart = o00IiI1iiII1i1i , menu = oOOOO )
 elif not traktit . traktUser ( 'trakt' ) : oo00O00oO000o ( '[COLOR red]Addon Data: Not Registered[/COLOR]' , 'authtrakt' , 'trakt' , icon = iiI1I1ii , fanart = o00IiI1iiII1i1i , menu = oOOOO )
 else : oo00O00oO000o ( '[COLOR green]Addon Data: %s[/COLOR]' % traktit . traktUser ( 'trakt' ) , 'authtrakt' , 'trakt' , icon = iiI1I1ii , fanart = o00IiI1iiII1i1i , menu = oOOOO )
 if Oo00OOOOO == "" : oo00O00oO000o ( '[COLOR red]Saved Data: Not Saved[/COLOR]' , 'savetrakt' , 'trakt' , icon = iiI1I1ii , fanart = o00IiI1iiII1i1i , menu = III1Ii1i1I1 )
 else : oo00O00oO000o ( '[COLOR green]Saved Data: %s[/COLOR]' % Oo00OOOOO , '' , icon = iiI1I1ii , fanart = o00IiI1iiII1i1i , menu = III1Ii1i1I1 )
 if Ii1II1I11i1 == 'No' : oo00O00oO000o ( '============================================' , '' , themeit = I1I1i )
 oo00O00oO000o ( 'Save All Trakt Data' , 'savetrakt' , 'all' , icon = O0OoOO0oo0 , themeit = I1I1i )
 oo00O00oO000o ( 'Recover All Saved Trakt Data' , 'restoretrakt' , 'all' , icon = O0OoOO0oo0 , themeit = I1I1i )
 oo00O00oO000o ( 'Clear All Saved Trakt Data' , 'cleartrakt' , 'all' , icon = O0OoOO0oo0 , themeit = I1I1i )
 oo00O00oO000o ( 'Clear All Addon Data' , 'addontrakt' , 'all' , icon = O0OoOO0oo0 , themeit = I1I1i )
 OOo00OoO ( 'movies' , 'MAIN' )
 if 18 - 18: Iii
def oO0o ( ) :
 O00o0O = '[COLOR green]ON[/COLOR]' if O0OoO000O0OO == 'true' else '[COLOR red]OFF[/COLOR]'
 Iiii1iiiIiI1 = str ( i1iiIII111ii ) if not i1iiIII111ii == '' else 'Real Debrid hasnt been saved yet.'
 oo00O00oO000o ( '[I]http://real-debrid.com is a PAID service.[/I]' , '' , icon = O0OoOO0oo0 , themeit = I1I1i )
 oo00O00oO000o ( 'Save Real Debrid Data: %s' % O00o0O , 'togglesetting' , 'KEEPREAL' , icon = II1iiiiII , themeit = I1I1i )
 if O0OoO000O0OO == 'true' : oo00O00oO000o ( 'Last Save: %s' % str ( Iiii1iiiIiI1 ) , '' , icon = II1iiiiII , themeit = I1I1i )
 if Ii1II1I11i1 == 'No' : oo00O00oO000o ( '============================================' , '' , icon = II1iiiiII , themeit = I1I1i )
 I11Iii1 = os . path . join ( OOOo0 , IIiiiiiiIi1I1 , 'icon.png' ) if os . path . exists ( IIIii1II1II ) else II1iiiiII
 i1iIIi1II1iiI = os . path . join ( OOOo0 , IIiiiiiiIi1I1 , 'fanart.jpg' ) if os . path . exists ( IIIii1II1II ) else I1i1iiI1
 I1I1 = debridit . debridUser ( 'exodus' )
 oo00O00oO000o ( '[+]-- Exodus' , '' , icon = I11Iii1 , fanart = i1iIIi1II1iiI , themeit = I1I1i )
 oOOOO = Ii ( 'debridaddon' , 'Exodus' ) ; III1Ii1i1I1 = Ii ( 'debrid' , 'Exodus' )
 if not os . path . exists ( IIIii1II1II ) : oo00O00oO000o ( '[COLOR red]Addon Data: Not Installed[/COLOR]' , '' , icon = I11Iii1 , fanart = i1iIIi1II1iiI , menu = oOOOO )
 elif not I1I1 : oo00O00oO000o ( '[COLOR red]Addon Data: Not Registered[/COLOR]' , 'authdebrid' , 'exodus' , icon = I11Iii1 , fanart = i1iIIi1II1iiI , menu = oOOOO )
 else : oo00O00oO000o ( '[COLOR green]Addon Data: %s[/COLOR]' % I1I1 , 'authdebrid' , 'exodus' , icon = I11Iii1 , fanart = i1iIIi1II1iiI , menu = oOOOO )
 if O0O == "" : oo00O00oO000o ( '[COLOR red]Saved Data: Not Saved[/COLOR]' , 'savedebrid' , 'exodus' , icon = I11Iii1 , fanart = i1iIIi1II1iiI , menu = III1Ii1i1I1 )
 else : oo00O00oO000o ( '[COLOR green]Saved Data: %s[/COLOR]' % O0O , '' , icon = I11Iii1 , fanart = i1iIIi1II1iiI , menu = III1Ii1i1I1 )
 OOOoOo = os . path . join ( OOOo0 , O000OO0 , 'icon.png' ) if os . path . exists ( I11i1I1I ) else II1iiiiII
 OOoO0oo0O = os . path . join ( OOOo0 , O000OO0 , 'fanart.jpg' ) if os . path . exists ( I11i1I1I ) else I1i1iiI1
 O0Oo0 = debridit . debridUser ( 'specto' )
 oo00O00oO000o ( '[+]-- Specto' , '' , icon = OOOoOo , fanart = OOoO0oo0O , themeit = I1I1i )
 oOOOO = Ii ( 'debridaddon' , 'Specto' ) ; III1Ii1i1I1 = Ii ( 'debrid' , 'Specto' )
 if not os . path . exists ( I11i1I1I ) : oo00O00oO000o ( '[COLOR red]Addon Data: Not Installed[/COLOR]' , '' , icon = OOOoOo , fanart = OOoO0oo0O , menu = oOOOO )
 elif not O0Oo0 : oo00O00oO000o ( '[COLOR red]Addon Data: Not Registered[/COLOR]' , 'authdebrid' , 'specto' , icon = OOOoOo , fanart = OOoO0oo0O , menu = oOOOO )
 else : oo00O00oO000o ( '[COLOR green]Addon Data: %s[/COLOR]' % O0Oo0 , 'authdebrid' , 'specto' , icon = OOOoOo , fanart = OOoO0oo0O , menu = oOOOO )
 if O00o0OO == "" : oo00O00oO000o ( '[COLOR red]Saved Data: Not Saved[/COLOR]' , 'savedebrid' , 'specto' , icon = OOOoOo , fanart = OOoO0oo0O , menu = III1Ii1i1I1 )
 else : oo00O00oO000o ( '[COLOR green]Saved Data: %s[/COLOR]' % O00o0OO , '' , icon = OOOoOo , fanart = OOoO0oo0O , menu = III1Ii1i1I1 )
 OOooO0OO0 = os . path . join ( OOOo0 , I1IIiiIiii , 'icon.png' ) if os . path . exists ( oOOoo0Oo ) else II1iiiiII
 iI1iIiiiI1I1 = os . path . join ( OOOo0 , I1IIiiIiii , 'fanart.jpg' ) if os . path . exists ( oOOoo0Oo ) else I1i1iiI1
 OOOOOo = debridit . debridUser ( 'url' )
 oo00O00oO000o ( '[+]-- URL Resolver' , '' , icon = OOooO0OO0 , fanart = iI1iIiiiI1I1 , themeit = I1I1i )
 oOOOO = Ii ( 'debridaddon' , 'url' ) ; III1Ii1i1I1 = Ii ( 'debrid' , 'url' )
 if not os . path . exists ( oOOoo0Oo ) : oo00O00oO000o ( '[COLOR red]Addon Data: Not Installed[/COLOR]' , '' , icon = OOooO0OO0 , fanart = iI1iIiiiI1I1 , menu = oOOOO )
 elif not OOOOOo : oo00O00oO000o ( '[COLOR red]Addon Data: Not Registered[/COLOR]' , 'authdebrid' , 'url' , icon = OOooO0OO0 , fanart = iI1iIiiiI1I1 , menu = oOOOO )
 else : oo00O00oO000o ( '[COLOR green]Addon Data: %s[/COLOR]' % OOOOOo , 'authdebrid' , 'url' , icon = OOooO0OO0 , fanart = iI1iIiiiI1I1 , menu = oOOOO )
 if I11i1 == "" : oo00O00oO000o ( '[COLOR red]Saved Data: Not Saved[/COLOR]' , 'savedebrid' , 'url' , icon = OOooO0OO0 , fanart = iI1iIiiiI1I1 , menu = III1Ii1i1I1 )
 else : oo00O00oO000o ( '[COLOR green]Saved Data: %s[/COLOR]' % I11i1 , '' , icon = OOooO0OO0 , fanart = iI1iIiiiI1I1 , menu = III1Ii1i1I1 )
 if Ii1II1I11i1 == 'No' : oo00O00oO000o ( '============================================' , '' , themeit = I1I1i )
 oo00O00oO000o ( 'Save All Real Debrid Data' , 'savedebrid' , 'all' , icon = II1iiiiII , themeit = I1I1i )
 oo00O00oO000o ( 'Recover All Saved Real Debrid Data' , 'restoredebrid' , 'all' , icon = II1iiiiII , themeit = I1I1i )
 oo00O00oO000o ( 'Clear All Saved Real Debrid Data' , 'cleardebrid' , 'all' , icon = II1iiiiII , themeit = I1I1i )
 oo00O00oO000o ( 'Clear All Addon Data' , 'addondebrid' , 'all' , icon = II1iiiiII , themeit = I1I1i )
 OOo00OoO ( 'movies' , 'MAIN' )
 if 50 - 50: oOoooo000Oo00 - i11iIiiIii + i11OOoO0ooOO0 / I1 - oOoooo000Oo00 + iii11
def Iii111Ii1 ( ) :
 for III11 in glob . glob ( os . path . join ( OOOo0 , '*/' ) ) :
  Ii1Ii11Iii1i1 = III11 . replace ( OOOo0 , '' ) . replace ( '\\' , '' ) . replace ( '/' , '' )
  oO0o00oOOooO0 = os . path . join ( III11 , 'icon.png' )
  OOOoO000 = os . path . join ( III11 , 'fanart.png' )
  if Ii1Ii11Iii1i1 in o00OO00OoO : pass
  elif Ii1Ii11Iii1i1 == 'packages' : pass
  else :
   i1IiII1i1I = Ii1Ii11Iii1i1
   iI1ii1ii1I = { 'audio.' : '[COLOR orange][AUDIO] [/COLOR]' , 'metadata.' : '[COLOR cyan][METADATA] [/COLOR]' , 'module.' : '[COLOR orange][MODULE] [/COLOR]' , 'plugin.' : '[COLOR blue][PLUGIN] [/COLOR]' , 'program.' : '[COLOR orange][PROGRAM] [/COLOR]' , 'repository.' : '[COLOR gold][REPO] [/COLOR]' , 'script.' : '[COLOR green][SCRIPT] [/COLOR]' , 'service.' : '[COLOR green][SERVICE] [/COLOR]' , 'skin.' : '[COLOR dodgerblue][SKIN] [/COLOR]' , 'video.' : '[COLOR orange][VIDEO] [/COLOR]' , 'weather.' : '[COLOR yellow][WEATHER] [/COLOR]' }
   for iI1IIi11i1I1 in iI1ii1ii1I :
    i1IiII1i1I = i1IiII1i1I . replace ( iI1IIi11i1I1 , iI1ii1ii1I [ iI1IIi11i1I1 ] )
   oo00O00oO000o ( '[COLOR red][B][REMOVE][/B][/COLOR] %s' % i1IiII1i1I , 'removeaddon' , Ii1Ii11Iii1i1 , icon = oO0o00oOOooO0 , fanart = OOOoO000 , themeit = IIII1 )
   if 60 - 60: ooo000ooO0000 / oo00ooOoO00 % IiiII / IiiII * IiiII . i11iIiiIii
def o0oOO00 ( ) :
 if os . path . exists ( IiI ) :
  oo00O00oO000o ( '[COLOR red][B][REMOVE][/B][/COLOR] All Addon_Data' , 'removedata' , 'all' , themeit = IIII1 )
  oo00O00oO000o ( '[COLOR red][B][REMOVE][/B][/COLOR] All Addon_Data for Uninstalled Addons' , 'removedata' , 'uninstalled' , themeit = IIII1 )
  oo00O00oO000o ( '[COLOR red][B][REMOVE][/B][/COLOR] All Empty Folders in Addon_Data' , 'removedata' , 'empty' , themeit = IIII1 )
  oo00O00oO000o ( '[COLOR red][B][REMOVE][/B][/COLOR] %s Addon_Data' % Oo0Ooo , 'resetaddon' , themeit = IIII1 )
  if Ii1II1I11i1 == 'No' : oo00O00oO000o ( '============================================' , '' , themeit = I1I1i )
  for III11 in glob . glob ( os . path . join ( IiI , '*' ) ) :
   Ii1Ii11Iii1i1 = III11 . replace ( IiI , '' ) . replace ( '\\' , '' ) . replace ( '/' , '' )
   oO0o00oOOooO0 = os . path . join ( III11 . replace ( IiI , OOOo0 ) , 'icon.png' )
   OOOoO000 = os . path . join ( III11 . replace ( IiI , OOOo0 ) , 'fanart.png' )
   i1IiII1i1I = Ii1Ii11Iii1i1
   iI1ii1ii1I = { 'audio.' : '[COLOR orange][AUDIO] [/COLOR]' , 'metadata.' : '[COLOR cyan][METADATA] [/COLOR]' , 'module.' : '[COLOR orange][MODULE] [/COLOR]' , 'plugin.' : '[COLOR blue][PLUGIN] [/COLOR]' , 'program.' : '[COLOR orange][PROGRAM] [/COLOR]' , 'repository.' : '[COLOR gold][REPO] [/COLOR]' , 'script.' : '[COLOR green][SCRIPT] [/COLOR]' , 'service.' : '[COLOR green][SERVICE] [/COLOR]' , 'skin.' : '[COLOR dodgerblue][SKIN] [/COLOR]' , 'video.' : '[COLOR orange][VIDEO] [/COLOR]' , 'weather.' : '[COLOR yellow][WEATHER] [/COLOR]' }
   for iI1IIi11i1I1 in iI1ii1ii1I :
    i1IiII1i1I = i1IiII1i1I . replace ( iI1IIi11i1I1 , iI1ii1ii1I [ iI1IIi11i1I1 ] )
   if Ii1Ii11Iii1i1 in o00OO00OoO : i1IiII1i1I = '[COLOR green][B][PROTECTED][/B][/COLOR] %s' % i1IiII1i1I
   else : i1IiII1i1I = '[COLOR red][B][REMOVE][/B][/COLOR] %s' % i1IiII1i1I
   oo00O00oO000o ( ' %s' % i1IiII1i1I , 'removedata' , Ii1Ii11Iii1i1 , icon = oO0o00oOOooO0 , fanart = OOOoO000 , themeit = IIII1 )
 else :
  oo00O00oO000o ( 'No Addon data folder found.' , '' , themeit = I1I1i )
  if 46 - 46: i11iIiiIii - ooo000ooO0000
  if 95 - 95: OoOoOo00o0
  if 65 - 65: OoO
def I1iI11I1III1 ( ) :
 O0OOO0OOooo00 ( 'Backup Restore' , 'bre' , icon = iiIIIII1i1iI , themeit = I111i1i1111 )
 oo00O00oO000o ( 'Convert Paths to special' , 'convertpath' , icon = iiIIIII1i1iI , themeit = I111i1i1111 )
 oo00O00oO000o ( 'Test Notifications' , 'testnotify' , icon = iiIIIII1i1iI , themeit = I111i1i1111 )
 if 8 - 8: i11iIiiIii / OoOoOo00o0 + iii11 * oOoooo000Oo00 % IiI11iI1i1i1i . ooo000ooO0000
 if 6 - 6: IiI11iI1i1i1i % I1iii11 . I1iii11 - IiiII / ooo000ooO0000 . oo00ooOoO00
 if 99 - 99: OoO . I1Iiiiiii
 if 59 - 59: ooo000ooO0000 / I1iii11 / Ii1IIIIi1ii1I / I1 / OoO + iii11
 if 13 - 13: iii11 % IIII1i / I1Iiiiiii % I1Iiiiiii % I1
def o0Ii1 ( name , type , theme = None ) :
 if type == 'gui' :
  if name == Oo0oO0ooo :
   IIi1IiII = ooo0OO . yesno ( Oo0Ooo , 'Would you like to apply the guifix for:' , '%s?' % name , nolabel = 'No, Cancel' , yeslabel = 'Yes, Apply Fix' )
  else :
   IIi1IiII = ooo0OO . yesno ( "%s - [COLOR red]WARNING!![/COLOR]" % Oo0Ooo , "%s SpinzTV build is not currently installed." % name , "Would you like to apply the guiFix anyways?." , yeslabel = "Yes, Apply" , nolabel = "No, Cancel" )
  if IIi1IiII :
   o0IIIIiI11I = wiz . checkBuild ( name , 'gui' )
   iiiI11iIIi1 = name . replace ( '\\' , '' ) . replace ( '/' , '' ) . replace ( ':' , '' ) . replace ( '*' , '' ) . replace ( '?' , '' ) . replace ( '"' , '' ) . replace ( '<' , '' ) . replace ( '>' , '' ) . replace ( '|' , '' )
   if not wiz . workingURL ( o0IIIIiI11I ) == True : wiz . LogNotify ( Oo0Ooo , 'guiFix: [COLOR red]Invalid Zip Url![/COLOR]' ) ; return
   if not os . path . exists ( Oo0O ) : os . makedirs ( Oo0O )
   II1 . create ( Oo0Ooo , 'Downloading %s GuiFix' % name , '' , 'Please Wait' )
   o00OoooooooOo = os . path . join ( Oo0O , '%s_guisettings.zip' % iiiI11iIIi1 )
   try : os . remove ( o00OoooooooOo )
   except : pass
   downloader . download ( o0IIIIiI11I , o00OoooooooOo , II1 )
   xbmc . sleep ( 500 )
   II1 . update ( 0 , "" , "Installing %s GuiFix" % name )
   extract . all ( o00OoooooooOo , Oooo000o , II1 )
   II1 . close ( )
   wiz . killxbmc ( )
  else :
   wiz . LogNotify ( Oo0Ooo , 'guiFix: [COLOR red]Cancelled![/COLOR]' )
 elif type == 'fresh' :
  iIii1I ( name )
 elif type == 'normal' :
  if III11II1I1Ii1 == 'normal' :
   if oOOoO0 == 'true' :
    traktit . autoUpdate ( 'all' )
    wiz . setS ( 'traktlastsave' , str ( IIIII ) )
   if O0OoO000O0OO == 'true' :
    debridit . autoUpdate ( 'all' )
    wiz . setS ( 'debridlastsave' , str ( IIIII ) )
  if ooooooO0oo < 17.0 and float ( wiz . checkBuild ( name , 'kodi' ) ) >= 17.0 :
   IIi1IiII = ooo0OO . yesno ( "%s - [COLOR red]WARNING!![/COLOR]" % Oo0Ooo , 'There is a chance that the skin will not appear correctly' , 'When installing a %s build on a Kodi %s install' % ( wiz . checkBuild ( name , 'kodi' ) , ooooooO0oo ) , 'Would you still like to install: %s v%s?' % ( name , wiz . checkBuild ( name , 'version' ) ) , nolabel = 'No, Cancel' , yeslabel = 'Yes, Install' )
  else :
   IIi1IiII = ooo0OO . yesno ( Oo0Ooo , 'By downloading or using you are agreeing that the author takes no resposibility for the content or reliability of any of the addons included.  The author does not host, distribute or have any control over any of the content that may be provided by any addon. It is the users responsibility to ensure the legality of use within their country. By continuing you are agreeing to the terms and conditions herin. Would you still like to install:' , '%s v%s?' % ( name , wiz . checkBuild ( name , 'version' ) ) , nolabel = 'Disagree, Cancel' , yeslabel = 'Agree, Install' )
  if IIi1IiII :
   o0IIIIiI11I = wiz . checkBuild ( name , 'url' )
   iiiI11iIIi1 = name . replace ( '\\' , '' ) . replace ( '/' , '' ) . replace ( ':' , '' ) . replace ( '*' , '' ) . replace ( '?' , '' ) . replace ( '"' , '' ) . replace ( '<' , '' ) . replace ( '>' , '' ) . replace ( '|' , '' )
   if not wiz . workingURL ( o0IIIIiI11I ) == True : wiz . LogNotify ( Oo0Ooo , 'Build Install: [COLOR red]Invalid Zip Url![/COLOR]' ) ; return
   if not os . path . exists ( Oo0O ) : os . makedirs ( Oo0O )
   II1 . create ( Oo0Ooo , 'Downloading %s ' % name , '' , 'Please Wait' )
   o00OoooooooOo = os . path . join ( Oo0O , '%s.zip' % iiiI11iIIi1 )
   try : os . remove ( o00OoooooooOo )
   except : pass
   downloader . download ( o0IIIIiI11I , o00OoooooooOo , II1 )
   xbmc . sleep ( 500 )
   II1 . update ( 0 , "" , "Installing %s " % name )
   iii11i1 = extract . all ( o00OoooooooOo , O00ooooo00 , II1 )
   i1IiI1I111iIi , IiiIIi1 , iI1iIiiI = iii11i1 . split ( '/' , 3 )
   wiz . setS ( 'buildname' , name )
   wiz . setS ( 'buildversion' , wiz . checkBuild ( name , 'version' ) )
   wiz . setS ( 'buildtheme' , '' )
   wiz . setS ( 'latestversion' , wiz . checkBuild ( name , 'version' ) )
   wiz . setS ( 'lastbuildcheck' , str ( oO00oOooooo0 ) )
   wiz . setS ( 'installed' , 'true' )
   wiz . setS ( 'extract' , str ( i1IiI1I111iIi ) )
   wiz . setS ( 'errors' , str ( IiiIIi1 ) )
   wiz . log ( 'INSTALLED %s: [ERRORS:%s]' % ( i1IiI1I111iIi , IiiIIi1 ) )
   if int ( IiiIIi1 ) >= 1 :
    Oo0OOo = ooo0OO . yesno ( Oo0Ooo , 'INSTALLED %s: [ERRORS:%s]' % ( i1IiI1I111iIi , IiiIIi1 ) , 'Would you like to view the errors?' , nolabel = 'No, Cancel' , yeslabel = 'Yes, View' )
    if Oo0OOo :
     wiz . TextBoxes ( Oo0Ooo , iI1iIiiI . replace ( '\t' , '' ) ) ; xbmc . sleep ( 3000 )
   II1 . close ( )
   I111iIi1 = wiz . checkBuild ( name , 'theme' )
   if not I111iIi1 == 'http://' and wiz . workingURL ( I111iIi1 ) == True : o0Ii1 ( name , 'theme' )
   ooo0OO . ok ( Oo0Ooo , "To save changes you now need to force close Kodi, Press OK to force close Kodi" )
   wiz . killxbmc ( )
  else :
   wiz . LogNotify ( Oo0Ooo , 'Build Install: [COLOR red]Cancelled![/COLOR]' )
 elif type == 'theme' :
  if theme == None :
   I111iIi1 = wiz . checkBuild ( name , 'theme' )
   Ii1I11i11I1i = [ ]
   if not I111iIi1 == 'http://' and wiz . workingURL ( I111iIi1 ) == True :
    oooO0 = wiz . openURL ( I111iIi1 ) . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
    iiIIiii = re . compile ( 'name="(.+?)"' ) . findall ( oooO0 )
    if len ( iiIIiii ) > 0 :
     if ooo0OO . yesno ( Oo0Ooo , "The Build [%s] comes with %s different themes" % ( name , len ( iiIIiii ) ) , "Would you like to install one now?" , yeslabel = "Yes, Install" , nolabel = "No Thanks" ) :
      for I1iIiI11I1 in iiIIiii :
       Ii1I11i11I1i . append ( I1iIiI11I1 )
      wiz . log ( "Theme List: %s " % str ( Ii1I11i11I1i ) )
      oO00 = ooo0OO . select ( Oo0Ooo , Ii1I11i11I1i )
      wiz . log ( "Theme install selected: %s" % oO00 )
      if not oO00 == - 1 : theme = Ii1I11i11I1i [ oO00 ] ; IiI1II11iiI = True
      else : wiz . LogNotify ( Oo0Ooo , 'Theme Install: [COLOR red]Cancelled![/COLOR]' ) ; return
     else : wiz . LogNotify ( Oo0Ooo , 'Theme Install: [COLOR red]Cancelled![/COLOR]' ) ; return
   else : wiz . LogNotify ( Oo0Ooo , 'Theme Install: [COLOR red]None Found![/COLOR]' )
  else : IiI1II11iiI = ooo0OO . yesno ( Oo0Ooo , 'Would you like to install the theme:' , theme , 'for %s v%s?' % ( name , wiz . checkBuild ( name , 'version' ) ) , nolabel = 'No, Cancel' , yeslabel = 'Yes, Install' )
  if IiI1II11iiI :
   o0oOOooo00O = wiz . checkTheme ( name , theme , 'url' )
   iiiI11iIIi1 = name . replace ( '\\' , '' ) . replace ( '/' , '' ) . replace ( ':' , '' ) . replace ( '*' , '' ) . replace ( '?' , '' ) . replace ( '"' , '' ) . replace ( '<' , '' ) . replace ( '>' , '' ) . replace ( '|' , '' )
   if not wiz . workingURL ( o0oOOooo00O ) == True : wiz . LogNotify ( Oo0Ooo , 'Theme Install: [COLOR red]Invalid Zip Url![/COLOR]' ) ; return
   if not os . path . exists ( Oo0O ) : os . makedirs ( Oo0O )
   II1 . create ( Oo0Ooo , 'Downloading %s ' % name , '' , 'Please Wait' )
   o00OoooooooOo = os . path . join ( Oo0O , '%s.zip' % iiiI11iIIi1 )
   try : os . remove ( o00OoooooooOo )
   except : pass
   downloader . download ( o0oOOooo00O , o00OoooooooOo , II1 )
   xbmc . sleep ( 500 )
   II1 . update ( 0 , "" , "Installing %s " % name )
   iii11i1 = extract . all ( o00OoooooooOo , O00ooooo00 , II1 )
   i1IiI1I111iIi , IiiIIi1 , iI1iIiiI = iii11i1 . split ( '/' , 3 )
   wiz . setS ( 'buildtheme' , theme )
   wiz . log ( 'INSTALLED %s: [ERRORS:%s]' % ( i1IiI1I111iIi , IiiIIi1 ) )
   II1 . close ( )
   if III11II1I1Ii1 not in [ "fresh" , "normal" ] : xbmc . executebuiltin ( "ReloadSkin()" ) ; xbmc . sleep ( 1000 ) ; xbmc . executebuiltin ( "Container.Refresh" )
  else :
   wiz . LogNotify ( Oo0Ooo , 'Theme Install: [COLOR red]Cancelled![/COLOR]' )
   if 66 - 66: OoO + oo00ooOoO00 % OoOoOo00o0 . I1 * IiiII % IiiII
   if 87 - 87: Ii1IIIIi1ii1I + iii11 . o0o00 - OoOo0oOooOoOO
   if 6 - 6: i11OOoO0ooOO0 * OoOo0oOooOoOO
   if 28 - 28: I1iii11 * iii11 / I1Iiiiiii
def II11I ( apk , url , Brackets ) :
 if wiz . platform ( ) == 'android' :
  if apk in [ 'kodi' , 'spmc' ] :
   Oo0OOo = ooo0OO . yesno ( Oo0Ooo , "Would you like to download and install:" , "%s (v%s)" % ( apk . upper ( ) , wiz . latestApk ( apk , 'version' ) ) )
   if not Oo0OOo : wiz . LogNotify ( Oo0Ooo , '[COLOR red]ERROR:[/COLOR] Install Cancelled' ) ; return
   Oo0OOo00oO0oOO = "%s v%s" % ( apk . upper ( ) , wiz . latestApk ( apk , 'version' ) )
  else :
   Oo0OOo = ooo0OO . yesno ( Oo0Ooo , "Would you like to download and install:" , "%s" % apk )
   if not Oo0OOo : wiz . LogNotify ( Oo0Ooo , '[COLOR red]ERROR:[/COLOR] Install Cancelled' ) ; return
   Oo0OOo00oO0oOO = apk
  if Oo0OOo :
   if not os . path . exists ( Oo0O ) : os . makedirs ( Oo0O )
   if not wiz . workingURL ( url ) == True : wiz . LogNotify ( Oo0Ooo , 'APK Installer: [COLOR red]Invalid Apk Url![/COLOR]' ) ; return
   II1 . create ( Oo0Ooo , 'Downloading %s' % Oo0OOo00oO0oOO , '' , 'Please Wait' )
   o00OoooooooOo = os . path . join ( Oo0O , "%s.apk" % apk )
   try : os . remove ( o00OoooooooOo )
   except : pass
   downloader . download ( url , o00OoooooooOo , II1 )
   xbmc . sleep ( 500 )
   II1 . close ( )
   if "Brackets" in Brackets :
    iiiii1I1III1 = zipfile . ZipFile ( o00OoooooooOo )
    for file in iiiii1I1III1 . namelist ( ) :
     if file . endswith ( '.apk' ) :
      with open ( os . path . join ( Oo0O , os . path . basename ( file ) ) , 'wb' ) as i1oO00O :
       oo0o0ooooo = file . split ( '/' ) [ 1 ]
       i1oO00O . write ( iiiii1I1III1 . read ( file ) )
       xbmc . sleep ( 500 )
       i1oO00O . close ( )
       try :
        os . remove ( o00OoooooooOo )
       except :
        pass
       o00OoooooooOo = os . path . join ( Oo0O , oo0o0ooooo )
   ooo0OO . ok ( Oo0Ooo , "Launching the APK to be installed" , "Follow the install process to complete." )
   xbmc . executebuiltin ( 'StartAndroidActivity("","android.intent.action.VIEW","application/vnd.android.package-archive","file:' + o00OoooooooOo + '")' )
  else : wiz . LogNotify ( Oo0Ooo , '[COLOR red]ERROR:[/COLOR] Install Cancelled' )
 else : wiz . LogNotify ( Oo0Ooo , '[COLOR red]ERROR:[/COLOR] None Android Device' )
 if 70 - 70: oOoooo000Oo00 . i11iIiiIii % oOoooo000Oo00 . I1 - i11OOoO0ooOO0
 if 26 - 26: Ii1IIIIi1ii1I
 if 76 - 76: oo00ooOoO00 * OoOo0oOooOoOO * I1 + I1Iiiiiii * I1Iiiiiii
 if 35 - 35: iii11
def ooOoooo0 ( name , url , ) :
 if "NULL" in url :
  ooo0OO . ok ( Oo0Ooo , "[COLOR ghostwhite]Not a valid selection, please try again.[/COLOR]" )
  sys . exit ( 1 )
  if 54 - 54: oo00ooOoO00 . ooo000ooO0000 - IiiII + OOOOoO0O0oo0 + I1iii11 / I1iii11
 i1ii1IiiiiIi1I = xbmcgui . DialogProgress ( )
 i1ii1IiiiiIi1I . create ( Oo0Ooo , "" , "" , 'ROM: ' + name )
 iiiI11iIIi1 = name . replace ( '\\' , '' ) . replace ( '/' , '' ) . replace ( ':' , '' ) . replace ( '*' , '' ) . replace ( '?' , '' ) . replace ( '"' , '' ) . replace ( '<' , '' ) . replace ( '>' , '' ) . replace ( '|' , '' )
 o00OoooooooOo = os . path . join ( Oo0O , '%s.zip' % iiiI11iIIi1 )
 downloader . download ( url , o00OoooooooOo , i1ii1IiiiiIi1I )
 iii11i1 = extract . all ( o00OoooooooOo , I1IiiI , i1ii1IiiiiIi1I )
 ooo0OO . ok ( Oo0Ooo , "[COLOR yellow]Download complete, ROM Location: [/COLOR][COLOR white]" + o00OoooooooOo + "[/COLOR]" )
 if 56 - 56: OoOo0oOooOoOO * I1
 if 85 - 85: OoOo0oOooOoOO % OoO * i11OOoO0ooOO0
 if 44 - 44: i11OOoO0ooOO0 . IiiII + I1Iiiiiii . OOOOoO0O0oo0
 if 7 - 7: IiiII + i11OOoO0ooOO0 * ooo000ooO0000 * ooo000ooO0000 / OoOoOo00o0 - oOoooo000Oo00
 if 65 - 65: IIII1i + OoO + OoOoOo00o0
def oOOoo ( ver ) :
 if ver == '15' : wiz . setS ( 'show15' , 'true' if i1111 == 'false' else 'false' )
 elif ver == '16' : wiz . setS ( 'show16' , 'true' if i11 == 'false' else 'false' )
 xbmc . executebuiltin ( 'Container.Refresh' )
 if 6 - 6: Ii1IIIIi1ii1I
def ooOoo000oO ( part , whole ) :
 return 100 * float ( part ) / float ( whole )
 if 50 - 50: IiI11iI1i1i1i + iii11
def Ii ( type , name ) :
 if type == 'trakt' :
  o0OoOOo = [ ]
  O0Oo0iI1II1III1 = urllib . quote_plus ( name . lower ( ) . replace ( ' ' , '' ) )
  o0OoOOo . append ( ( IIII1 % name , ' ' ) )
  o0OoOOo . append ( ( IIII1 % 'Save Trakt Data' , 'RunPlugin(plugin://%s/?mode=savetrakt&name=%s)' % ( OO0o , O0Oo0iI1II1III1 ) ) )
  o0OoOOo . append ( ( IIII1 % 'Restore Trakt Data' , 'RunPlugin(plugin://%s/?mode=restoretrakt&name=%s)' % ( OO0o , O0Oo0iI1II1III1 ) ) )
  o0OoOOo . append ( ( IIII1 % 'Clear Trakt Data' , 'RunPlugin(plugin://%s/?mode=cleartrakt&name=%s)' % ( OO0o , O0Oo0iI1II1III1 ) ) )
 if type == 'traktaddon' :
  o0OoOOo = [ ]
  O0Oo0iI1II1III1 = urllib . quote_plus ( name . lower ( ) . replace ( ' ' , '' ) )
  o0OoOOo . append ( ( IIII1 % name , ' ' ) )
  o0OoOOo . append ( ( IIII1 % 'Register Trakt' , 'RunPlugin(plugin://%s/?mode=authtrakt&name=%s)' % ( OO0o , O0Oo0iI1II1III1 ) ) )
  o0OoOOo . append ( ( IIII1 % 'Save Trakt Data' , 'RunPlugin(plugin://%s/?mode=savetrakt&name=%s)' % ( OO0o , O0Oo0iI1II1III1 ) ) )
  o0OoOOo . append ( ( IIII1 % 'Restore Trakt Data' , 'RunPlugin(plugin://%s/?mode=restoretrakt&name=%s)' % ( OO0o , O0Oo0iI1II1III1 ) ) )
  o0OoOOo . append ( ( IIII1 % 'Clear Addon Trakt Data' , 'RunPlugin(plugin://%s/?mode=addontrakt&name=%s)' % ( OO0o , O0Oo0iI1II1III1 ) ) )
 if type == 'debrid' :
  o0OoOOo = [ ]
  O0Oo0iI1II1III1 = urllib . quote_plus ( name . lower ( ) . replace ( ' ' , '' ) )
  o0OoOOo . append ( ( IIII1 % name , ' ' ) )
  o0OoOOo . append ( ( IIII1 % 'Save Real Debrid Data' , 'RunPlugin(plugin://%s/?mode=savedebrid&name=%s)' % ( OO0o , O0Oo0iI1II1III1 ) ) )
  o0OoOOo . append ( ( IIII1 % 'Restore Real Debrid Data' , 'RunPlugin(plugin://%s/?mode=restoredebrid&name=%s)' % ( OO0o , O0Oo0iI1II1III1 ) ) )
  o0OoOOo . append ( ( IIII1 % 'Clear Real Debrid Data' , 'RunPlugin(plugin://%s/?mode=cleardebrid&name=%s)' % ( OO0o , O0Oo0iI1II1III1 ) ) )
 if type == 'debridaddon' :
  o0OoOOo = [ ]
  O0Oo0iI1II1III1 = urllib . quote_plus ( name . lower ( ) . replace ( ' ' , '' ) )
  o0OoOOo . append ( ( IIII1 % name , ' ' ) )
  o0OoOOo . append ( ( IIII1 % 'Register Real Debrid' , 'RunPlugin(plugin://%s/?mode=authdebrid&name=%s)' % ( OO0o , O0Oo0iI1II1III1 ) ) )
  o0OoOOo . append ( ( IIII1 % 'Save Real Debrid Data' , 'RunPlugin(plugin://%s/?mode=savedebrid&name=%s)' % ( OO0o , O0Oo0iI1II1III1 ) ) )
  o0OoOOo . append ( ( IIII1 % 'Restore Real Debrid Data' , 'RunPlugin(plugin://%s/?mode=restoredebrid&name=%s)' % ( OO0o , O0Oo0iI1II1III1 ) ) )
  o0OoOOo . append ( ( IIII1 % 'Clear Addon Real Debrid Data' , 'RunPlugin(plugin://%s/?mode=addondebrid&name=%s)' % ( OO0o , O0Oo0iI1II1III1 ) ) )
 if type == 'install' :
  o0OoOOo = [ ]
  O0Oo0iI1II1III1 = urllib . quote_plus ( name )
  o0OoOOo . append ( ( IIII1 % name , ' ' ) )
  o0OoOOo . append ( ( IIII1 % 'Fresh Install' , 'RunPlugin(plugin://%s/?mode=install&name=%s&url=fresh)' % ( OO0o , O0Oo0iI1II1III1 ) ) )
  o0OoOOo . append ( ( IIII1 % 'Normal Install Use On Updates' , 'RunPlugin(plugin://%s/?mode=install&name=%s&url=normal)' % ( OO0o , O0Oo0iI1II1III1 ) ) )
  o0OoOOo . append ( ( IIII1 % 'Apply guiFix' , 'RunPlugin(plugin://%s/?mode=install&name=%s&url=gui)' % ( OO0o , O0Oo0iI1II1III1 ) ) )
 o0OoOOo . append ( ( IIII1 % 'SpinzTV Settings' , 'RunPlugin(plugin://%s/?mode=settings)' % OO0o ) )
 return o0OoOOo
 if 62 - 62: Iii * i11iIiiIii . o0o00
def I1iIIIiI ( ) :
 OoiI1I1 = wiz . log_check ( )
 I1III1i1I = OoiI1I1 . replace ( IIi1IiiiI1Ii , "" )
 if os . path . exists ( OoiI1I1 ) or not OoiI1I1 == False :
  i1oO00O = open ( OoiI1I1 , mode = 'r' ) ; OOOOO0 = i1oO00O . read ( ) ; i1oO00O . close ( )
  wiz . TextBoxes ( "%s - %s" % ( Oo0Ooo , I1III1i1I ) , OOOOO0 )
 else :
  wiz . LogNotify ( 'View Log' , 'No Log File Found!' )
  if 79 - 79: OoOoOo00o0 - OOOOoO0O0oo0 . oo00ooOoO00 + I1 % I1 * Iii
def Ii1Ii1I ( ) :
 if os . path . exists ( oo00 ) :
  i1oO00O = open ( oo00 , mode = 'r' ) ; OOOOO0 = i1oO00O . read ( ) ; i1oO00O . close ( )
  wiz . TextBoxes ( "%s - Wizard.log" % Oo0Ooo , OOOOO0 )
 else :
  wiz . LogNotify ( 'View Log' , 'Wizard.log not found!' )
  if 54 - 54: IIII1i + OoO
def o0O00O ( addon ) :
 if ooo0OO . yesno ( Oo0Ooo , 'Are you sure you want to delete the addon:' , '[COLOR yellow]%s[/COLOR]' % addon , yeslabel = 'Yes, Remove' , nolabel = 'No, Cancel' ) :
  wiz . cleanHouse ( os . path . join ( OOOo0 , addon ) )
  O0OOOOOoo ( addon )
  wiz . LogNotify ( 'Remove Addon' , 'Complete!' )
  ooo0OO . ok ( Oo0Ooo , 'The addon has been removed but will remain in the addons list until the next time you reload Kodi.' )
 else : wiz . LogNotify ( 'Remove Addon' , 'Cancelled!' )
 xbmc . executebuiltin ( 'Container.Refresh' )
 if 69 - 69: Iii + o0o00
def O0OOOOOoo ( addon ) :
 if addon == 'all' :
  if ooo0OO . yesno ( Oo0Ooo , 'Would you like to remove ALL addon data stored in you Userdata folder?' , yeslabel = 'Yes, Remove' , nolabel = 'No, Cancel' ) :
   wiz . cleanHouse ( IiI )
  else : wiz . LogNotify ( 'Remove Addon Data' , 'Cancelled!' )
 elif addon == 'uninstalled' :
  if ooo0OO . yesno ( Oo0Ooo , 'Would you like to remove ALL addon data stored in you Userdata folder for uninstalled addons?' , yeslabel = 'Yes, Remove' , nolabel = 'No, Cancel' ) :
   i1IiII = 0
   for III11 in glob . glob ( os . path . join ( IiI , '*' ) ) :
    Ii1Ii11Iii1i1 = III11 . replace ( IiI , '' ) . replace ( '\\' , '' ) . replace ( '/' , '' )
    if Ii1Ii11Iii1i1 in o00OO00OoO : pass
    elif os . path . exists ( os . path . join ( OOOo0 , Ii1Ii11Iii1i1 ) ) : pass
    else : wiz . cleanHouse ( III11 ) ; i1IiII += 1 ; wiz . log ( III11 ) ; shutil . rmtree ( III11 )
   wiz . LogNotify ( 'Clean up Uninstalled' , '[COLOR yellow]%s[/COLOR] Folders(s) Removed' % i1IiII )
  else : wiz . LogNotify ( 'Remove Addon Data' , 'Cancelled!' )
 elif addon == 'empty' :
  if ooo0OO . yesno ( Oo0Ooo , 'Would you like to remove ALL empty addon data folders in you Userdata folder?' , yeslabel = 'Yes, Remove' , nolabel = 'No, Cancel' ) :
   i1IiII = wiz . emptyfolder ( IiI )
   wiz . LogNotify ( 'Remove Empty Folders' , '[COLOR yellow]%s[/COLOR] Folders(s) Removed' % i1IiII )
  else : wiz . LogNotify ( 'Remove Empty Folders' , 'Cancelled!' )
 else :
  i1II = os . path . join ( Oooo000o , 'addon_data' , addon )
  if addon in o00OO00OoO :
   wiz . LogNotify ( "Protected Plugin" , "Not allowed to remove Addon_Data" )
  elif os . path . exists ( i1II ) :
   if ooo0OO . yesno ( Oo0Ooo , 'Would you also like to remove the addon data for:' , '[COLOR yellow]%s[/COLOR]' % addon , yeslabel = 'Yes, Remove' , nolabel = 'No, Cancel' ) :
    wiz . cleanHouse ( i1II )
    try :
     shutil . rmtree ( i1II )
    except :
     wiz . log ( "Error deleting: %s" % i1II )
   else :
    wiz . log ( 'Addon data for %s was not removed' % addon )
 xbmc . executebuiltin ( 'Container.Refresh' )
 if 44 - 44: OoOo0oOooOoOO . OoOoOo00o0 . Ii1IIIIi1ii1I % OoOo0oOooOoOO
def ooOOO0OooOo ( url ) :
 Oo0oO00 = urllib2 . Request ( url )
 Oo0oO00 . add_header ( 'User-Agent' , 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3' )
 ii11ii11I = urllib2 . urlopen ( Oo0oO00 )
 oooO0 = ii11ii11I . read ( )
 ii11ii11I . close ( )
 return oooO0
 if 83 - 83: OoOoOo00o0 * oo00ooOoO00 * o0o00 . IiiII / ooo000ooO0000 + oo00ooOoO00
 if 43 - 43: OoOo0oOooOoOO
 if 97 - 97: IiiII / I1iii11 + I1Iiiiiii
 if 32 - 32: OOOOoO0O0oo0 % I1Iiiiiii * I1iii11
 if 72 - 72: OOOOoO0O0oo0 . o0o00 - I1Iiiiiii - oOoooo000Oo00 % oo00ooOoO00
def iIii1I ( install = None ) :
 if oOOoO0 == 'true' :
  traktit . autoUpdate ( 'all' )
  wiz . setS ( 'traktlastsave' , str ( IIIII ) )
 if O0OoO000O0OO == 'true' :
  debridit . autoUpdate ( 'all' )
  wiz . setS ( 'debridlastsave' , str ( IIIII ) )
 if o00 not in [ 'skin.confluence' ] :
  oO0o00O0O0oo0 = 'skin.confluence'
  Oo0OOo = ooo0OO . yesno ( Oo0Ooo , "The skin needs to be set back to [COLOR yellow]%s[/COLOR]" % oO0o00O0O0oo0 [ 5 : ] , "Before doing a fresh install to clear all Texture files!" , "Would you like us to do that for you?" , nolabel = "No, Thanks" , yeslabel = "Yes, Swap Skin" ) ;
  if Oo0OOo :
   skinSwitch . swapSkins ( oO0o00O0O0oo0 )
   while not xbmc . getCondVisibility ( "Window.isVisible(yesnodialog)" ) :
    xbmc . sleep ( 200 )
   xbmc . executebuiltin ( "Action(Left)" )
   xbmc . executebuiltin ( "Action(Select)" )
  else : wiz . LogNotify ( Oo0Ooo , 'Fresh Install: [COLOR red]Cancelled![/COLOR]' ) ; return
 if install : IIi1IiII = ooo0OO . yesno ( Oo0Ooo , "Do you wish to restore your" , "Kodi configuration to default settings" , "Before installing %s?" % install , nolabel = 'No, Cancel' , yeslabel = 'Yes, Continue' )
 else : IIi1IiII = ooo0OO . yesno ( Oo0Ooo , "Do you wish to restore your" , "Kodi configuration to default settings?" , nolabel = 'No, Cancel' , yeslabel = 'Yes, Continue' )
 if IIi1IiII :
  i1I11Ii111II = os . path . abspath ( O00ooooo00 )
  II1 . create ( Oo0Ooo , "Clearing all files and folders:" , '' , '' )
  O000OOO00Ooo = sum ( [ len ( OoOOoooO000 ) for OoO0o000oOo , Oo00OO00o0oO , OoOOoooO000 in os . walk ( i1I11Ii111II ) ] ) ; iI1 = 0 ;
  try :
   for I1I1i1i , OOo0O , OoOOoooO000 in os . walk ( i1I11Ii111II , topdown = True ) :
    OOo0O [ : ] = [ Oo00OO00o0oO for Oo00OO00o0oO in OOo0O if Oo00OO00o0oO not in o00OO00OoO ]
    for ii11i in OoOOoooO000 :
     iI1 += 1
     oOOoooO0O0 = I1I1i1i . split ( '\\' )
     ii1O0ooooo000 = len ( oOOoooO0O0 ) - 1
     if ii11i == 'sources.xml' and oOOoooO0O0 [ ii1O0ooooo000 ] == 'userdata' and iI111I11I1I1 == 'true' : wiz . log ( "Keep Sources: %s\\%s" % ( I1I1i1i , ii11i ) )
     elif ii11i == 'favourites.xml' and oOOoooO0O0 [ ii1O0ooooo000 ] == 'userdata' and i1iIIi1 == 'true' : wiz . log ( "Keep Favourites: %s\\%s" % ( I1I1i1i , ii11i ) )
     elif ii11i == 'profiles.xml' and oOOoooO0O0 [ ii1O0ooooo000 ] == 'userdata' and OOooO0OOoo == 'true' : wiz . log ( "Keep Profiles: %s\\%s" % ( I1I1i1i , ii11i ) )
     elif ii11i == 'advancedsettings.xml' and oOOoooO0O0 [ ii1O0ooooo000 ] == 'userdata' and iIii1 == 'true' : wiz . log ( "Keep Advanced Settings: %s\\%s" % ( I1I1i1i , ii11i ) )
     elif ii11i in [ 'xbmc.log' , 'kodi.log' , 'spmc.log' , 'tvmc.log' ] : wiz . log ( "Keep Log File: %s" % ii11i )
     elif ii11i . endswith ( '.db' ) :
      try : os . remove ( os . path . join ( I1I1i1i , ii11i ) )
      except : wiz . log ( 'Failed to delete, Purging DB.' ) ; wiz . purgeDb ( os . path . join ( I1I1i1i , ii11i ) )
     else :
      II1 . update ( int ( ooOoo000oO ( iI1 , O000OOO00Ooo ) ) , '' , 'File: [COLOR yellow]%s[/COLOR]' % ii11i , '' )
      try : os . remove ( os . path . join ( I1I1i1i , ii11i ) )
      except : wiz . log ( "Error removing %s\\%s" % ( I1I1i1i , ii11i ) )
   for I1I1i1i , OOo0O , OoOOoooO000 in os . walk ( i1I11Ii111II , topdown = True ) :
    OOo0O [ : ] = [ Oo00OO00o0oO for Oo00OO00o0oO in OOo0O if Oo00OO00o0oO not in o00OO00OoO ]
    for ii11i in OOo0O :
     II1 . update ( 100 , '' , 'Cleaning Up Empty Folder: [COLOR yellow]%s[/COLOR]' % ii11i , '' )
     if ii11i not in [ "Database" , "userdata" , "temp" , "addons" , "addon_data" ] :
      shutil . rmtree ( os . path . join ( I1I1i1i , ii11i ) , ignore_errors = True , onerror = None )
   II1 . close ( )
   wiz . clearS ( 'build' )
  except :
   ooo0OO . ok ( Oo0Ooo , "Problem found" , "Your settings has not been changed" )
   import traceback
   wiz . log ( traceback . format_exc ( ) )
   wiz . log ( "freshstart.main_list NOT removed" )
  II1 . close ( )
  if install :
   ooo0OO . ok ( Oo0Ooo , "Your current setup for kodi has been cleared!" , "Now we will install: %s v%s" % ( install , wiz . checkBuild ( install , 'version' ) ) )
   o0Ii1 ( install , 'normal' )
  else :
   ooo0OO . ok ( Oo0Ooo , "The process is complete, you're now back to a fresh Kodi configuration with SpinzTV Wizard" , "Please reboot your system or restart Kodi in order for the changes to be applied." )
   wiz . killxbmc ( )
 else : wiz . LogNotify ( Oo0Ooo , 'Fresh Install: [COLOR red]Cancelled![/COLOR]' ) ; xbmc . executebuiltin ( 'Container.Refresh' )
 if 97 - 97: i11iIiiIii % IIII1i / I1iii11 / I1iii11
 if 97 - 97: OoOoOo00o0 - I1Iiiiiii - i11OOoO0ooOO0 * Iii
 if 54 - 54: i11OOoO0ooOO0
 if 5 - 5: IiI11iI1i1i1i
def Oo0O0oo0o00o0 ( ) :
 if ooo0OO . yesno ( Oo0Ooo , 'Would you like to clear cache?' , nolabel = 'Cancel' , yeslabel = 'Delete' ) :
  wiz . clearCache ( )
  Ooi1I11 ( )
  if 5 - 5: OoO % o0o00 + IiI11iI1i1i1i
def Ooi1I11 ( ) :
 iiiIi1II1III = wiz . latestDB ( 'Textures' )
 if ooo0OO . yesno ( Oo0Ooo , "Would you like to delete the %s and Thumbnails folder?" % iiiIi1II1III , "They will repopulate on startup" , nolabel = 'No, Cancel' , yeslabel = 'Yes, Remove' ) :
  try : wiz . removeFile ( os . join ( O0oo0OO0 , iiiIi1II1III ) )
  except : wiz . log ( 'Failed to delete, Purging DB.' ) ; wiz . purgeDb ( iiiIi1II1III )
  wiz . removeFolder ( i1i1II )
  wiz . killxbmc ( )
 else : wiz . log ( 'Clear thumbnames cancelled' )
 if 8 - 8: IiI11iI1i1i1i % Ii1IIIIi1ii1I . I1iii11 % OOOOoO0O0oo0 - o0o00
def iII1Ii1I1i1 ( ) :
 OooOooo0 = [ ] ; Oo0OOo00oO0oOO = [ ]
 for i11i , oo0OoOO0o0o , OoOOoooO000 in os . walk ( O00ooooo00 ) :
  for i1oO00O in fnmatch . filter ( OoOOoooO000 , '*.db' ) :
   if i1oO00O != 'Thumbs.db' :
    OO0OOO00 = os . path . join ( i11i , i1oO00O )
    OooOooo0 . append ( OO0OOO00 )
    dir = OO0OOO00 . replace ( '\\' , '/' ) . split ( '/' )
    Oo0OOo00oO0oOO . append ( '(%s) %s' % ( dir [ len ( dir ) - 2 ] , dir [ len ( dir ) - 1 ] ) )
 if ooooooO0oo >= 16 :
  ooOOo0o = ooo0OO . multiselect ( "Select DB File to Purge" , Oo0OOo00oO0oOO )
  if ooOOo0o == None : wiz . LogNotify ( "Purge Database" , "Cancelled" )
  elif len ( ooOOo0o ) == 0 : wiz . LogNotify ( "Purge Database" , "Cancelled" )
  else :
   for IiI1Iii1 in ooOOo0o : wiz . purgeDb ( OooOooo0 [ IiI1Iii1 ] )
 else :
  ooOOo0o = ooo0OO . select ( "Select DB File to Purge" , Oo0OOo00oO0oOO )
  if ooOOo0o == - 1 : wiz . LogNotify ( "Purge Database" , "Cancelled" )
  else : wiz . purgeDb ( OooOooo0 [ IiI1Iii1 ] )
  if 85 - 85: i11iIiiIii / i11iIiiIii . ii . I1
  if 67 - 67: OoOoOo00o0 / iii11 . Ii1IIIIi1ii1I . OoOo0oOooOoOO
  if 19 - 19: IiI11iI1i1i1i . IiiII / OoO
  if 68 - 68: OOOOoO0O0oo0 / OoOo0oOooOoOO * ooo000ooO0000 / IIII1i
def ooooO000 ( ) :
 III11II1I1Ii1 = wiz . workingURL ( oOo )
 if III11II1I1Ii1 == True :
  oooO0 = wiz . openURL ( oOo ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
  id , OOOOO0 = oooO0 . split ( '|||' )
  notify . TestNotification ( msg = OOOOO0 , title = i1II1I1Iii1 , BorderWidth = 10 )
 else : wiz . LogNotify ( Oo0Ooo , "Invalid URL for Notification" )
 if 61 - 61: OOOOoO0O0oo0 - Ii1IIIIi1ii1I + Ii1IIIIi1ii1I
def iiiIiIIII1iiIIi ( ) :
 if Ii1II1I11i1 == 'No' : oo00O00oO000o ( '==============BackUp Options===============' , '' , themeit = I1I1i )
 oo00O00oO000o ( 'Full Backup' , 'full' , icon = iiIIIII1i1iI , themeit = I111i1i1111 )
 oo00O00oO000o ( 'Backup for Builds (Exc: Thumbnails, Databases)' , 'backb' , icon = iiIIIII1i1iI , themeit = I111i1i1111 )
 oo00O00oO000o ( 'Backup addon data' , 'backad' , icon = iiIIIII1i1iI , themeit = I111i1i1111 )
 if Ii1II1I11i1 == 'No' : oo00O00oO000o ( '==============Restore Options===============' , '' , themeit = I1I1i )
 O0OOO0OOooo00 ( 'Restore Full Backup' , 'refull' , icon = iiIIIII1i1iI , themeit = I111i1i1111 )
 O0OOO0OOooo00 ( 'Restore Addon Data' , 'refull' , icon = iiIIIII1i1iI , themeit = I111i1i1111 )
 if Ii1II1I11i1 == 'No' : oo00O00oO000o ( '==============Other Options===============' , '' , themeit = I1I1i )
 O0OOO0OOooo00 ( 'Delete A Backup' , 'delbu' , icon = iiIIIII1i1iI , themeit = I111i1i1111 )
 oo00O00oO000o ( 'Delete All Backups' , 'delall' , icon = iiIIIII1i1iI , themeit = I111i1i1111 )
 oo00O00oO000o ( 'Select Backup Location' , 'settings' , icon = iiIIIII1i1iI , themeit = I111i1i1111 )
 if 17 - 17: ooo000ooO0000
 if 97 - 97: IiiII * IiiII / o0o00
 if 6 - 6: IIII1i
 if 72 - 72: ooo000ooO0000 * IiiII - OoO / IiiII + Ii1IIIIi1ii1I - o0o00
 if 49 - 49: ii - I1 / ii * OoO + I1Iiiiiii
 if 35 - 35: OoOoOo00o0 . Iii / oo00ooOoO00 / Iii * IIII1i
def O0OOO0OOooo00 ( display , mode , name = None , url = None , menu = None , overwrite = True , fanart = I1i1iiI1 , icon = iiIIIII1i1iI , themeit = None ) :
 Oo0 = '%s?mode=%s' % ( sys . argv [ 0 ] , urllib . quote_plus ( mode ) )
 if not name == None : Oo0 += "&name=" + urllib . quote_plus ( name )
 if not url == None : Oo0 += "&url=" + urllib . quote_plus ( url )
 O0000Oo00o = True
 if themeit : display = themeit % display
 II1ii = xbmcgui . ListItem ( display , iconImage = "DefaultFolder.png" , thumbnailImage = icon )
 II1ii . setInfo ( type = "Video" , infoLabels = { "Title" : display , "Plot" : Oo0Ooo } )
 II1ii . setProperty ( "Fanart_Image" , fanart )
 if not menu == None : II1ii . addContextMenuItems ( menu , replaceItems = overwrite )
 O0000Oo00o = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = Oo0 , listitem = II1ii , isFolder = True )
 return O0000Oo00o
 if 89 - 89: o0o00 . i11iIiiIii * I1
def O0Oo00 ( name , url , mode , iconimage ) :
 Oo0 = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage )
 O0000Oo00o = True
 II1ii = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 II1ii . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : name } )
 O0000Oo00o = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = Oo0 , listitem = II1ii , isFolder = True )
 return O0000Oo00o
 if 44 - 44: oo00ooOoO00 . Iii / i11iIiiIii + IiI11iI1i1i1i
def Ii1ii ( display , mode , name = None , url = None , menu = None , overwrite = True , fanart = I1i1iiI1 , icon = iiIIIII1i1iI , description = None , themeit = None ) :
 Oo0 = '%s?mode=%s' % ( sys . argv [ 0 ] , urllib . quote_plus ( mode ) )
 if not name == None : Oo0 += "&name=" + urllib . quote_plus ( name )
 if not url == None : Oo0 += "&url=" + urllib . quote_plus ( url )
 if not description == None : Oo0 += "&description=" + urllib . quote_plus ( description )
 O0000Oo00o = True
 if themeit : display = themeit % display
 II1ii = xbmcgui . ListItem ( description , iconImage = "DefaultFolder.png" , thumbnailImage = icon )
 II1ii . setInfo ( type = "Video" , infoLabels = { "Title" : description , "Plot" : Oo0Ooo } )
 II1ii . setProperty ( "Fanart_Image" , fanart )
 if not menu == None : II1ii . addContextMenuItems ( menu , replaceItems = overwrite )
 O0000Oo00o = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = Oo0 , listitem = II1ii , isFolder = False )
 return O0000Oo00o
 if 27 - 27: Ii1IIIIi1ii1I
def oo00O00oO000o ( display , mode , name = None , url = None , menu = None , overwrite = True , fanart = I1i1iiI1 , icon = iiIIIII1i1iI , themeit = None ) :
 Oo0 = '%s?mode=%s' % ( sys . argv [ 0 ] , urllib . quote_plus ( mode ) )
 if not name == None : Oo0 += "&name=" + urllib . quote_plus ( name )
 if not url == None : Oo0 += "&url=" + urllib . quote_plus ( url )
 O0000Oo00o = True
 if themeit : display = themeit % display
 II1ii = xbmcgui . ListItem ( display , iconImage = "DefaultFolder.png" , thumbnailImage = icon )
 II1ii . setInfo ( type = "Video" , infoLabels = { "Title" : display , "Plot" : Oo0Ooo } )
 II1ii . setProperty ( "Fanart_Image" , fanart )
 if not menu == None : II1ii . addContextMenuItems ( menu , replaceItems = overwrite )
 O0000Oo00o = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = Oo0 , listitem = II1ii , isFolder = False )
 return O0000Oo00o
 if 52 - 52: I1Iiiiiii % OoO + i11OOoO0ooOO0 * IIII1i . oOoooo000Oo00
def OoOooOO0oOOo0O ( name , url , mode , iconimage , fanart , description ) :
 Oo0 = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&fanart=" + urllib . quote_plus ( fanart )
 O0000Oo00o = True
 II1ii = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 II1ii . setInfo ( type = "Video" , infoLabels = { "Title" : name } )
 II1ii . setProperty ( "Fanart_Image" , fanart )
 O0000Oo00o = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = Oo0 , listitem = II1ii , isFolder = False )
 return O0000Oo00o
 if 42 - 42: o0o00 / iii11 + I1iii11 . I1iii11 % Ii1IIIIi1ii1I
def Ii1III1 ( name , url , mode , iconimage , fanart , description ) :
 Oo0 = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart ) + "&description=" + urllib . quote_plus ( description )
 O0000Oo00o = True
 II1ii = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 II1ii . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description } )
 II1ii . setProperty ( "Fanart_Image" , fanart )
 if mode == 90 :
  O0000Oo00o = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = Oo0 , listitem = II1ii , isFolder = False )
 else :
  O0000Oo00o = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = Oo0 , listitem = II1ii , isFolder = True )
 return O0000Oo00o
 if 80 - 80: i11OOoO0ooOO0 . o0o00 . I1Iiiiiii
 if 9 - 9: OoOo0oOooOoOO * I1
def O0oO0OOoO ( ) :
 O00oo = [ ]
 OOoO0O000O = sys . argv [ 2 ]
 if len ( OOoO0O000O ) >= 2 :
  iI = sys . argv [ 2 ]
  O0oI1ii1Ii1 = iI . replace ( '?' , '' )
  if ( iI [ len ( iI ) - 1 ] == '/' ) :
   iI = iI [ 0 : len ( iI ) - 2 ]
  OoOoOiI111I1III = O0oI1ii1Ii1 . split ( '&' )
  O00oo = { }
  for i111IiiI1Ii in range ( len ( OoOoOiI111I1III ) ) :
   OooOOOOOo = { }
   OooOOOOOo = OoOoOiI111I1III [ i111IiiI1Ii ] . split ( '=' )
   if ( len ( OooOOOOOo ) ) == 2 :
    O00oo [ OooOOOOOo [ 0 ] ] = OooOOOOOo [ 1 ]
    if 50 - 50: I1Iiiiiii + OOOOoO0O0oo0 + o0o00
  return O00oo
  if 15 - 15: ooo000ooO0000
iI = O0oO0OOoO ( )
III11II1I1Ii1 = None
ii11i = None
IiiI11I1IIiI = None
if 5 - 5: I1iii11
if 100 - 100: oOoooo000Oo00 + i11OOoO0ooOO0
try : IiiI11I1IIiI = urllib . unquote_plus ( iI [ "mode" ] )
except : pass
try : ii11i = urllib . unquote_plus ( iI [ "name" ] )
except : pass
try : III11II1I1Ii1 = urllib . unquote_plus ( iI [ "url" ] )
except : pass
if 59 - 59: IiI11iI1i1i1i
if 89 - 89: OoO % i11OOoO0ooOO0
wiz . log ( '[ Version : \'%s\' ] [ Mode : \'%s\' ] [ Name : \'%s\' ] [ Url : \'%s\' ]' % ( iiiii , IiiI11I1IIiI if not IiiI11I1IIiI == '' else None , ii11i , III11II1I1Ii1 ) )
def III11I1 ( ) :
 if 61 - 61: OoO - ii + Iii * Ii1IIIIi1ii1I % ii
 for file in os . listdir ( oO00oOo ) :
  if file . endswith ( ".zip" ) :
   III11II1I1Ii1 = xbmc . translatePath ( os . path . join ( oO00oOo , file ) )
   OoOooOO0oOOo0O ( file , III11II1I1Ii1 , 'read' , iiIIIII1i1iI , iiIIIII1i1iI , '' )
   if 24 - 24: OOOOoO0O0oo0 - ooo000ooO0000 * IIII1i
def O00OoOoO ( ) :
 ooO0o0oo = xbmc . translatePath ( os . path . join ( 'special://' , 'home' ) )
 for file in os . listdir ( oO00oOo ) :
  if file . endswith ( ".zip" ) :
   III11II1I1Ii1 = xbmc . translatePath ( os . path . join ( oO00oOo , file ) )
   Ii1III1 ( file , III11II1I1Ii1 , 'dell' , iiIIIII1i1iI , iiIIIII1i1iI , '' )
   if 79 - 79: IiI11iI1i1i1i % ii
   if 81 - 81: i11iIiiIii + i11iIiiIii * ii + IiI11iI1i1i1i
def OOo00OoO ( content , viewType ) :
 if content :
  xbmcplugin . setContent ( int ( sys . argv [ 1 ] ) , content )
 if wiz . getS ( 'auto-view' ) == 'true' :
  xbmc . executebuiltin ( "Container.SetViewMode(%s)" % wiz . getS ( viewType ) )
  if 32 - 32: I1 . OoOo0oOooOoOO
if IiiI11I1IIiI == None : IiiIiI1Ii1i ( )
if 15 - 15: Iii . ii
elif IiiI11I1IIiI == 'builds' : ii11 ( )
elif IiiI11I1IIiI == 'showupdate' : oOOoo ( ii11i )
elif IiiI11I1IIiI == 'viewbuild' : iiIIIiIi1IIi ( ii11i )
elif IiiI11I1IIiI == 'install' : o0Ii1 ( ii11i , III11II1I1Ii1 )
elif IiiI11I1IIiI == 'theme' : o0Ii1 ( ii11i , IiiI11I1IIiI , III11II1I1Ii1 )
if 17 - 17: i11iIiiIii / I1iii11 . ii / Iii
elif IiiI11I1IIiI == 'maint' : i11IiIIi11I ( )
elif IiiI11I1IIiI == 'speed' : I1I1IiIi1 ( )
elif IiiI11I1IIiI == 'speedtest' : speedtest . runtest ( III11II1I1Ii1 )
elif IiiI11I1IIiI == 'clearcache' : Oo0O0oo0o00o0 ( )
elif IiiI11I1IIiI == 'clearpackages' : wiz . clearPackages ( )
elif IiiI11I1IIiI == 'clearthumb' : Ooi1I11 ( )
elif IiiI11I1IIiI == 'freshstart' : iIii1I ( )
elif IiiI11I1IIiI == 'forceupdate' : wiz . forceUpdate ( )
elif IiiI11I1IIiI == 'forceclose' : wiz . killxbmc ( )
elif IiiI11I1IIiI == 'uploadlog' : uploadLog . LogUploader ( )
elif IiiI11I1IIiI == 'viewlog' : I1iIIIiI ( )
elif IiiI11I1IIiI == 'viewwizlog' : Ii1Ii1I ( )
elif IiiI11I1IIiI == 'clearwizlog' : i1oO00O = open ( oo00 , 'w' ) ; i1oO00O . close ( ) ; wiz . LogNotify ( Oo0Ooo , "Wizard Log Cleared!" )
elif IiiI11I1IIiI == 'purgedb' : iII1Ii1I1i1 ( )
elif IiiI11I1IIiI == 'removeaddons' : Iii111Ii1 ( )
elif IiiI11I1IIiI == 'removeaddon' : o0O00O ( ii11i )
elif IiiI11I1IIiI == 'removeaddondata' : o0oOO00 ( )
elif IiiI11I1IIiI == 'removedata' : O0OOOOOoo ( ii11i )
elif IiiI11I1IIiI == 'resetaddon' : i1IiII = wiz . cleanHouse ( ooOo , ignore = True ) ; wiz . LogNotify ( Oo0Ooo , "Addon_Data reset" )
if 38 - 38: oo00ooOoO00 . IiiII % oOoooo000Oo00 + i11OOoO0ooOO0 + I1
elif IiiI11I1IIiI == 'apk1' : oO0Ooo0ooOO0 ( )
elif IiiI11I1IIiI == 'apkgame' : oo0OOo0O ( III11II1I1Ii1 )
elif IiiI11I1IIiI == 'select' : I1i ( III11II1I1Ii1 )
elif IiiI11I1IIiI == 'grab' : IiIII1i1i ( ii11i , III11II1I1Ii1 )
elif IiiI11I1IIiI == 8 : APKSearch ( III11II1I1Ii1 )
elif IiiI11I1IIiI == 'apkscrape' : APK ( )
elif IiiI11I1IIiI == 'apkspinz' : III ( )
elif IiiI11I1IIiI == 'apkin' : iiI1II11II1i ( )
elif IiiI11I1IIiI == 'apkkodi' : OoOo000oOo0oo ( )
elif IiiI11I1IIiI == 'apkmaster' : iIiIIii ( )
elif IiiI11I1IIiI == 'emurom' : iIII1i1i ( )
elif IiiI11I1IIiI == 'emulators' : I1II ( )
elif IiiI11I1IIiI == 'roms' : i1i1111IiI ( )
elif IiiI11I1IIiI == 'snes' : oooo00o0o0o ( )
elif IiiI11I1IIiI == 'snesa' : IiIiiI11111I1 ( )
elif IiiI11I1IIiI == 'snesc' : OOO0ooo ( )
elif IiiI11I1IIiI == 'snesf' : I111i1I1 ( )
elif IiiI11I1IIiI == 'snesi' : II1Ii1iI1i1 ( )
elif IiiI11I1IIiI == 'snesl' : OOoO000O00oO ( )
elif IiiI11I1IIiI == 'snesn' : OooOOOo0 ( )
elif IiiI11I1IIiI == 'snesp' : o0OIIiI1I1 ( )
elif IiiI11I1IIiI == 'sness' : Oo00OOOOoo0oo ( )
elif IiiI11I1IIiI == 'snest' : II1iiIIIiIii ( )
elif IiiI11I1IIiI == 'snesw' : I1iIi1iiiIiI ( )
elif IiiI11I1IIiI == 'nes' : iI11IIiIiIii1 ( )
elif IiiI11I1IIiI == 'nesa' : OoOoOOO0OO0O ( )
elif IiiI11I1IIiI == 'nesc' : o00O ( )
elif IiiI11I1IIiI == 'nesd' : IIi ( )
elif IiiI11I1IIiI == 'nesf' : IIi1IiiI1 ( )
elif IiiI11I1IIiI == 'nesh' : oo0OOOoOo ( )
elif IiiI11I1IIiI == 'nesl' : I11IIIiIi11 ( )
elif IiiI11I1IIiI == 'nesn' : oOo00OooO0oO ( )
elif IiiI11I1IIiI == 'nesr' : IIIiiI1 ( )
elif IiiI11I1IIiI == 'nest' : IiIiiiiI1 ( )
elif IiiI11I1IIiI == 'nesw' : OoOOo ( )
elif IiiI11I1IIiI == 'gen' : i1I1iIi1IiI ( )
elif IiiI11I1IIiI == 'gena' : O00O00O000OOO ( )
elif IiiI11I1IIiI == 'genc' : Ooo0Oo0oo0 ( )
elif IiiI11I1IIiI == 'gene' : ii111Ii11iii ( )
elif IiiI11I1IIiI == 'genh' : OO0OoOOO0 ( )
elif IiiI11I1IIiI == 'genm' : I11I ( )
elif IiiI11I1IIiI == 'genp' : ooOoOOOOo ( )
elif IiiI11I1IIiI == 'gens' : iiIIi ( )
elif IiiI11I1IIiI == 'genu' : i1I11iIII1i1I ( )
elif IiiI11I1IIiI == 'atr' : oO00OoOoo0 ( )
elif IiiI11I1IIiI == 'atra' : II1II ( )
elif IiiI11I1IIiI == 'atrc' : ooo0 ( )
elif IiiI11I1IIiI == 'atre' : ooO0o ( )
elif IiiI11I1IIiI == 'atrh' : IiI1IiI11iII ( )
elif IiiI11I1IIiI == 'atrm' : ii11I ( )
elif IiiI11I1IIiI == 'atrp' : oOiI ( )
elif IiiI11I1IIiI == 'atrs' : I11i11I1iiII ( )
elif IiiI11I1IIiI == 'atrv' : OoOO ( )
elif IiiI11I1IIiI == 'n64' : IiIi1 ( )
elif IiiI11I1IIiI == 'n64a' : oOoi1i ( )
elif IiiI11I1IIiI == 'n64c' : o00oo0000 ( )
elif IiiI11I1IIiI == 'n64f' : oo0ooO0 ( )
elif IiiI11I1IIiI == 'n64k' : i1oOOOOOOOoO ( )
elif IiiI11I1IIiI == 'n64n' : OO0oOOo0o ( )
elif IiiI11I1IIiI == 'n64s' : i1i1IiIiIi1Ii ( )
elif IiiI11I1IIiI == 'n64v' : i1I ( )
elif IiiI11I1IIiI == 'tbg' : OO0ooo0o0 ( )
elif IiiI11I1IIiI == 'tga' : iiIIi1 ( )
elif IiiI11I1IIiI == 'tgc' : O0Oo0Ooo ( )
elif IiiI11I1IIiI == 'tgf' : O0iI ( )
elif IiiI11I1IIiI == 'tgj' : iiiIiI ( )
elif IiiI11I1IIiI == 'tgn' : Oo0o ( )
elif IiiI11I1IIiI == 'tgr' : iIii1Ooo0oO0 ( )
elif IiiI11I1IIiI == 'tgv' : O0o0oOooOoOo ( )
elif IiiI11I1IIiI == 'nds' : OO0oIiII1iiI ( )
elif IiiI11I1IIiI == 'ndsa' : OO000oOoo0O ( )
elif IiiI11I1IIiI == 'ndsb' : IiIiiI11i1Ii ( )
elif IiiI11I1IIiI == 'ndsc' : oO000o ( )
elif IiiI11I1IIiI == 'ndsd' : OOoo0 ( )
elif IiiI11I1IIiI == 'ndse' : IiI1i111IiIiIi1 ( )
elif IiiI11I1IIiI == 'ndsg' : OOO0o0OO0OO ( )
elif IiiI11I1IIiI == 'ndsi' : iIIIiIi1I1i ( )
elif IiiI11I1IIiI == 'ndsk' : OooOOOO0O0 ( )
elif IiiI11I1IIiI == 'ndsm' : oOo0OOoooO ( )
elif IiiI11I1IIiI == 'ndsn' : ooOoOO ( )
elif IiiI11I1IIiI == 'ndsp' : i1I1 ( )
elif IiiI11I1IIiI == 'ndsr' : Ii1iI ( )
elif IiiI11I1IIiI == 'ndss' : II1Ii ( )
elif IiiI11I1IIiI == 'ndst' : I11oOOooo ( )
elif IiiI11I1IIiI == 'ndsv' : oOoooO000O ( )
elif IiiI11I1IIiI == 'apkinstall' : II11I ( ii11i , III11II1I1Ii1 , "None" )
elif IiiI11I1IIiI == 'rominstall' : ooOoooo0 ( ii11i , III11II1I1Ii1 , )
if 47 - 47: ii + IiI11iI1i1i1i / OoOoOo00o0
if 97 - 97: IiiII / Iii % I1 + oo00ooOoO00 - OOOOoO0O0oo0
elif IiiI11I1IIiI == 'savedata' : I1iI ( )
elif IiiI11I1IIiI == 'togglesetting' : wiz . setS ( ii11i , 'false' if wiz . getS ( ii11i ) == 'true' else 'true' ) ; xbmc . executebuiltin ( 'Container.Refresh' )
if 38 - 38: iii11 % I1Iiiiiii + i11iIiiIii + o0o00 + OOOOoO0O0oo0 / i11iIiiIii
elif IiiI11I1IIiI == 'trakt' : OOoOoo00Oo ( )
elif IiiI11I1IIiI == 'savetrakt' : traktit . traktIt ( 'update' , ii11i )
elif IiiI11I1IIiI == 'restoretrakt' : traktit . traktIt ( 'restore' , ii11i )
elif IiiI11I1IIiI == 'addontrakt' : traktit . traktIt ( 'clearaddon' , ii11i )
elif IiiI11I1IIiI == 'cleartrakt' : traktit . clearSaved ( ii11i )
elif IiiI11I1IIiI == 'authtrakt' : traktit . activateTrakt ( ii11i ) ; xbmc . executebuiltin ( 'Container.Refresh' )
if 94 - 94: o0o00 - I1iii11 + IIII1i
elif IiiI11I1IIiI == 'realdebrid' : oO0o ( )
elif IiiI11I1IIiI == 'savedebrid' : debridit . debridIt ( 'update' , ii11i )
elif IiiI11I1IIiI == 'restoredebrid' : debridit . debridIt ( 'restore' , ii11i )
elif IiiI11I1IIiI == 'addondebrid' : debridit . debridIt ( 'clearaddon' , ii11i )
elif IiiI11I1IIiI == 'cleardebrid' : debridit . clearSaved ( ii11i )
elif IiiI11I1IIiI == 'authdebrid' : debridit . activateDebrid ( ii11i ) ; xbmc . executebuiltin ( 'Container.Refresh' )
if 59 - 59: ooo000ooO0000 . Iii - i11OOoO0ooOO0 + i11OOoO0ooOO0
elif IiiI11I1IIiI == 'contact' : wiz . TextBoxes ( Oo0Ooo , O0o0O0 )
elif IiiI11I1IIiI == 'settings' : wiz . openS ( ) ; xbmc . executebuiltin ( 'Container.Refresh' )
if 56 - 56: IIII1i + OOOOoO0O0oo0
elif IiiI11I1IIiI == 'developer' : I1iI11I1III1 ( )
elif IiiI11I1IIiI == 'convertpath' : wiz . convertSpecial ( O00ooooo00 )
elif IiiI11I1IIiI == 'testnotify' : ooooO000 ( )
elif IiiI11I1IIiI == 'bre' : iiiIiIIII1iiIIi ( )
elif IiiI11I1IIiI == 'full' : backuprestore . FullBackup ( )
elif IiiI11I1IIiI == 'backb' : backuprestore . Backup ( )
elif IiiI11I1IIiI == 'backad' : backuprestore . ADDON_DATA_BACKUP ( )
elif IiiI11I1IIiI == 'refull' : III11I1 ( )
elif IiiI11I1IIiI == 'delbu' : O00OoOoO ( )
elif IiiI11I1IIiI == 'delall' : backuprestore . DeleteAllBackups ( )
elif IiiI11I1IIiI == 'read' : backuprestore . READ_ZIP ( III11II1I1Ii1 )
elif IiiI11I1IIiI == 'dell' : backuprestore . DeleteBackup ( III11II1I1Ii1 )
if IiiI11I1IIiI not in [ '' , 'togglesettings' , 'settings' , 'contact' ] : xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
# dd678faae9ac167bc83abf78e5cb2f3f0688d3a3