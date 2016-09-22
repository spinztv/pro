import xbmc , xbmcaddon , xbmcgui , xbmcplugin , os , sys , xbmcvfs , glob
import shutil
import urllib2 , urllib
import re
import uservar
import fnmatch
import speedtest
import backuprestore
import plugintools
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
Ii1iIiII1ii1 = uservar . APKGAMEFILE
ooOooo000oOO = uservar . APKVIDFILE
Oo0oOOo = uservar . APKSYSFILE
Oo0OoO00oOO0o = uservar . SPEEDFILE
OOO00O = uservar . SNESFILE
OOoOO0oo0ooO = uservar . EMUFILE
O0o0O00Oo0o0 = uservar . NESAFILE
O00O0oOO00O00 = uservar . NESCFILE
i1Oo00 = uservar . NESDFILE
i1i = uservar . NESFFILE
iiI111I1iIiI = uservar . NESHFILE
IIIi1I1IIii1II = uservar . NESLFILE
O0 = uservar . NESNFILE
ii1ii1ii = uservar . NESRFILE
oooooOoo0ooo = uservar . NESTFILE
I1I1IiI1 = uservar . NESWFILE
III1iII1I1ii = uservar . GENAFILE
oOOo0 = uservar . GENCFILE
oo00O00oO = uservar . GENEFILE
iIiIIIi = uservar . GENHFILE
ooo00OOOooO = uservar . GENMFILE
O00OOOoOoo0O = uservar . GENPFILE
O000OOo00oo = uservar . GENSFILE
oo0OOo = uservar . GENUFILE
ooOOO00Ooo = uservar . ATRAFILE
IiIIIi1iIi = uservar . ATRCFILE
ooOOoooooo = uservar . ATREFILE
II1I = uservar . ATRHFILE
O0i1II1Iiii1I11 = uservar . ATRMFILE
IIII = uservar . ATRPFILE
iiIiI = uservar . ATRSFILE
o00oooO0Oo = uservar . ATRVFILE
o0O0OOO0Ooo = uservar . N64FILE
iiIiII1 = uservar . TGAFILE
OOO00O0O = uservar . TGCFILE
iii = uservar . TGFFILE
oOooOOOoOo = uservar . TGJFILE
i1Iii1i1I = uservar . TGNFILE
OOoO00 = uservar . TGRFILE
IiI111111IIII = uservar . TGVFILE
i1Ii = wiz . workingURL ( OOoOO0oo0ooO )
ii111iI1iIi1 = wiz . workingURL ( OOO00O )
OOO = wiz . workingURL ( O0o0O00Oo0o0 )
oo0OOo0 = wiz . workingURL ( O00O0oOO00O00 )
I11IiI = wiz . workingURL ( i1Oo00 )
O0ooO0Oo00o = wiz . workingURL ( i1i )
ooO0oOOooOo0 = wiz . workingURL ( iiI111I1iIiI )
i1I1ii11i1Iii = wiz . workingURL ( IIIi1I1IIii1II )
I1IiiiiI = wiz . workingURL ( O0 )
o0OIiII = wiz . workingURL ( ii1ii1ii )
ii1iII1II = wiz . workingURL ( oooooOoo0ooo )
Iii1I1I11iiI1 = wiz . workingURL ( I1I1IiI1 )
I1I1i1I = wiz . workingURL ( III1iII1I1ii )
ii1I = wiz . workingURL ( oOOo0 )
O0oO0 = wiz . workingURL ( oo00O00oO )
oO0O0OO0O = wiz . workingURL ( iIiIIIi )
OO = wiz . workingURL ( ooo00OOOooO )
OoOoO = wiz . workingURL ( O00OOOoOoo0O )
Ii1I1i = wiz . workingURL ( O000OOo00oo )
OOI1iI1ii1II = wiz . workingURL ( oo0OOo )
O0O0OOOOoo = wiz . workingURL ( ooOOO00Ooo )
oOooO0 = wiz . workingURL ( IiIIIi1iIi )
Ii1I1Ii = wiz . workingURL ( ooOOoooooo )
OOoO0 = wiz . workingURL ( II1I )
OO0Oooo0oOO0O = wiz . workingURL ( O0i1II1Iiii1I11 )
o00O0 = wiz . workingURL ( IIII )
oOO0O00Oo0O0o = wiz . workingURL ( iiIiI )
ii1 = wiz . workingURL ( o00oooO0Oo )
I1iIIiiIIi1i = wiz . workingURL ( o0O0OOO0Ooo )
O0O0ooOOO = wiz . workingURL ( iiIiII1 )
oOOo0O00o = wiz . workingURL ( OOO00O0O )
iIiIi11 = wiz . workingURL ( iii )
OOOiiiiI = wiz . workingURL ( oOooOOOoOo )
oooOo0OOOoo0 = wiz . workingURL ( i1Iii1i1I )
OOoO = wiz . workingURL ( OOoO00 )
OO0O000 = wiz . workingURL ( IiI111111IIII )
iiIiI1i1 = wiz . workingURL ( OOOO0OOoO0O0 )
oO0O00oOOoooO = wiz . workingURL ( O0Oo000ooO00 )
IiIi11iI = wiz . workingURL ( oO0 )
Oo0O00O000 = wiz . workingURL ( Ii1iIiII1ii1 )
i11I1IiII1i1i = wiz . workingURL ( ooOooo000oOO )
oo = wiz . workingURL ( Oo0oOOo )
I1111i = wiz . workingURL ( Oo0OoO00oOO0o )
iIIii = uservar . UPDATECHECK if str ( uservar . UPDATECHECK ) . isdigit ( ) else 1
o00O0O = o0 + timedelta ( days = iIIii )
ii1iii1i = uservar . NOTIFICATION
Iii1I1111ii = uservar . ENABLE
ooOoO00 = uservar . HEADERMESSAGE
Ii1IIiI1i = uservar . HIDECONTACT
o0O00Oo0 = uservar . CONTACT
IiII111i1i11 = uservar . HIDESPACERS
i111iIi1i1II1 = uservar . COLOR1
oooO = uservar . COLOR2
i1I1i111Ii = uservar . THEME1
ooo = uservar . THEME2
i1i1iI1iiiI = uservar . THEME3
Ooo0oOooo0 = uservar . THEME4
oOOOoo00 = uservar . THEME5
iiIiIIIiiI = uservar . ICONMAINT if not uservar . ICONMAINT == 'http://' else iiIIIII1i1iI
iiI1IIIi = uservar . ICONBUILDS if not uservar . ICONBUILDS == 'http://' else iiIIIII1i1iI
II11IiIi11 = uservar . ICONSPEED if not uservar . ICONSPEED == 'http://' else iiIIIII1i1iI
IIOOO0O00O0OOOO = uservar . ICONAPK if not uservar . ICONAPK == 'http://' else iiIIIII1i1iI
I1iiii1I = uservar . ICONCONTACT if not uservar . ICONCONTACT == 'http://' else iiIIIII1i1iI
OOo0 = uservar . ICONSAVE if not uservar . ICONSAVE == 'http://' else iiIIIII1i1iI
oO00ooooO0o = uservar . ICONREAL if not uservar . ICONREAL == 'http://' else iiIIIII1i1iI
oo0o = uservar . ICONTRAKT if not uservar . ICONTRAKT == 'http://' else iiIIIII1i1iI
o0oO0oooOoo = uservar . ICONSETTINGS if not uservar . ICONSETTINGS == 'http://' else iiIIIII1i1iI
I1III1111iIi = uservar . ICONKODI if not uservar . ICONKODI == 'http://' else iiIIIII1i1iI
I1i111I = uservar . ICONGAMES if not uservar . ICONGAMES == 'http://' else iiIIIII1i1iI
Ooo = uservar . ICONMOVIES if not uservar . ICONMOVIES == 'http://' else iiIIIII1i1iI
Oo0oo0O0o00O = uservar . ICONANDROID if not uservar . ICONANDROID == 'http://' else iiIIIII1i1iI
I1i11 = uservar . ICONSPMC if not uservar . ICONSPMC == 'http://' else iiIIIII1i1iI
IiIi1I1 = uservar . ICONSPINZ if not uservar . ICONSPINZ == 'http://' else iiIIIII1i1iI
###########################
###### Menu Items   #######
###########################
#addDir (display,mode,name=None,url=None,menu=None,overwrite=True,fanart=FANART,icon=ICON, themeit=None)
#addFile(display,mode,name=None,url=None,menu=None,overwrite=True,fanart=FANART,icon=ICON, themeit=None)
if 39 - 39: Ii1I11I + oo0 + iI1II - o0OOo0o0O0O
if 65 - 65: I11I1i1iIII1I
if 49 - 49: oo0o0000 . iI1i . iI1i11
if 66 - 66: iiiiII1I % Ii * ooOo0o0O00 * i1I1 + o0O0oO0O00O0o / II1I1Ii
def Ooo0O0oooo ( ) :
 if len ( Oo0oO0ooo ) > 0 :
  iiI = wiz . checkBuild ( Oo0oO0ooo , 'version' )
  oOIIiIi = '%s (v%s)' % ( Oo0oO0ooo , o0oOoO00o )
  if iiI > o0oOoO00o : oOIIiIi = '%s [COLOR red][B][UPDATE v%s][/B][/COLOR]' % ( oOIIiIi , iiI )
  OOoOooOoOOOoo ( oOIIiIi , 'viewbuild' , Oo0oO0ooo , themeit = Ooo0oOooo0 )
  Iiii1iI1i = wiz . checkBuild ( Oo0oO0ooo , 'theme' )
  if not Iiii1iI1i == 'http://' and wiz . workingURL ( Iiii1iI1i ) == True :
   I1ii1ii11i1I ( 'None' if i1 == "" else i1 , 'theme' , Oo0oO0ooo , themeit = oOOOoo00 )
 else : OOoOooOoOOOoo ( 'None' , 'builds' , themeit = Ooo0oOooo0 )
 if IiII111i1i11 == 'No' : I1ii1ii11i1I ( '============================================' , '' , themeit = i1i1iI1iiiI )
 OOoOooOoOOOoo ( 'SpinzTV Builds' , 'builds' , icon = iiI1IIIi , themeit = i1I1i111Ii )
 OOoOooOoOOOoo ( 'Maintenance' , 'maint' , icon = iiIiIIIiiI , themeit = i1I1i111Ii )
 OOoOooOoOOOoo ( 'Speed Test' , 'speed' , icon = II11IiIi11 , themeit = i1I1i111Ii )
 OOoOooOoOOOoo ( 'Apk Installer (ANDROID ONLY!!!)' , 'apk' , icon = IIOOO0O00O0OOOO , themeit = i1I1i111Ii )
 OOoOooOoOOOoo ( 'Emulators And Roms (ANDROID ONLY!)' , 'emurom' , icon = I1i111I , themeit = i1I1i111Ii )
 OOoOooOoOOOoo ( 'Save Data' , 'savedata' , icon = OOo0 , themeit = i1I1i111Ii )
 if Ii1IIiI1i == 'No' : I1ii1ii11i1I ( 'Contact' , 'contact' , icon = I1iiii1I , themeit = i1I1i111Ii )
 if IiII111i1i11 == 'No' : I1ii1ii11i1I ( '============================================' , '' , themeit = i1i1iI1iiiI )
 I1ii1ii11i1I ( 'Settings' , 'settings' , icon = o0oO0oooOoo , themeit = i1I1i111Ii )
 if iIi1ii1I1 == 'true' : OOoOooOoOOOoo ( 'Developer Menu' , 'developer' , icon = o0oO0oooOoo , themeit = i1I1i111Ii )
 o0OoOO ( 'movies' , 'MAIN' )
 if 55 - 55: oOo000OOOo - O0i11I1I1I - IIIi11I11 - iIIIII1I + ooI1i
 if 32 - 32: iiiiII1I / iI1i11 + o0O0oO0O00O0o
 if 32 - 32: oo0 % O0i11I1I1I
 if 65 - 65: ooI1i . iI1II / ooOo0o0O00 . o0OOo0o0O0O * iI1i11
def IiIiII1 ( ) :
 if not iiIiI1i1 == True :
  I1ii1ii11i1I ( 'Kodi Version: %s' % ooooooO0oo , '' , icon = iiI1IIIi , themeit = i1i1iI1iiiI )
  if IiII111i1i11 == 'No' : I1ii1ii11i1I ( '============================================' , '' , themeit = i1i1iI1iiiI )
  I1ii1ii11i1I ( 'Url for txt file not valid' , '' , icon = iiI1IIIi , themeit = i1i1iI1iiiI )
  I1ii1ii11i1I ( '%s' % iiIiI1i1 , '' , icon = iiI1IIIi , themeit = i1i1iI1iiiI )
 else :
  Iii1iiIi1II = wiz . openURL ( OOOO0OOoO0O0 ) . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
  OO0O00oOo = re . compile ( 'name="(.+?)".+?ersion="(.+?)".+?rl="(.+?)".+?odi="(.+?)".+?con="(.+?)".+?anart="(.+?)"' ) . findall ( Iii1iiIi1II )
  if len ( OO0O00oOo ) == 1 :
   ii1II ( OO0O00oOo [ 0 ] [ 0 ] )
  elif len ( OO0O00oOo ) > 1 :
   I1ii1ii11i1I ( 'Kodi Version: %s' % ooooooO0oo , '' , icon = iiI1IIIi , themeit = i1i1iI1iiiI )
   if IiII111i1i11 == 'No' : I1ii1ii11i1I ( '============================================' , '' , themeit = i1i1iI1iiiI )
   if oO0o0o0ooO0oO == 'true' :
    for iI1I , iiI , OooOoOo , III1I1Iii1iiI , i1Iii11I1i , Oo00o0OO0O00o in OO0O00oOo :
     O0Oooo = iiIi1i ( 'install' , iI1I )
     OOoOooOoOOOoo ( '[%s] %s (v%s)' % ( float ( III1I1Iii1iiI ) , iI1I , iiI ) , 'viewbuild' , iI1I , fanart = Oo00o0OO0O00o , icon = i1Iii11I1i , menu = O0Oooo , themeit = ooo )
   else :
    I1i11111i1i11 = wiz . buildCount ( '15' ) ; OOoOOO0 = wiz . buildCount ( '16' )
    if OOoOOO0 > 0 :
     if I1i11111i1i11 > 0 :
      I1I1i = '+' if i11 == 'false' else '-'
      I1ii1ii11i1I ( '[%s] Jarvis and Above(%s)' % ( I1I1i , OOoOOO0 ) , 'showupdate' , '16' , themeit = i1i1iI1iiiI )
     if i11 == 'true' :
      for iI1I , iiI , OooOoOo , III1I1Iii1iiI , i1Iii11I1i , Oo00o0OO0O00o in OO0O00oOo :
       I1IIIiIiIi = int ( float ( III1I1Iii1iiI ) )
       if I1IIIiIiIi >= 16 :
        O0Oooo = iiIi1i ( 'install' , iI1I )
        OOoOooOoOOOoo ( '[%s] %s (v%s)' % ( float ( III1I1Iii1iiI ) , iI1I , iiI ) , 'viewbuild' , iI1I , fanart = Oo00o0OO0O00o , icon = i1Iii11I1i , menu = O0Oooo , themeit = ooo )
    if I1i11111i1i11 > 0 :
     if OOoOOO0 > 0 :
      I1I1i = '+' if i1111 == 'false' else '-'
      I1ii1ii11i1I ( '[%s] Isengard and Below(%s)' % ( I1I1i , I1i11111i1i11 ) , 'showupdate' , '15' , themeit = i1i1iI1iiiI )
     if i1111 == 'true' :
      for iI1I , iiI , OooOoOo , III1I1Iii1iiI , i1Iii11I1i , Oo00o0OO0O00o in OO0O00oOo :
       I1IIIiIiIi = int ( float ( III1I1Iii1iiI ) )
       if I1IIIiIiIi <= 15 :
        O0Oooo = iiIi1i ( 'install' , iI1I )
        OOoOooOoOOOoo ( '[%s] %s (v%s)' % ( float ( III1I1Iii1iiI ) , iI1I , iiI ) , 'viewbuild' , iI1I , fanart = Oo00o0OO0O00o , icon = i1Iii11I1i , menu = O0Oooo , themeit = ooo )
  else : I1ii1ii11i1I ( 'Text file for builds not formated correctly.' , '' , icon = iiI1IIIi , themeit = i1i1iI1iiiI )
 o0OoOO ( 'movies' , 'MAIN' )
 if 27 - 27: ooOo0o0O00 + iiiiII1I - o0O0oO0O00O0o + Ii1I11I . oOo000OOOo
def ii1II ( name ) :
 if not iiIiI1i1 == True :
  I1ii1ii11i1I ( 'Url for txt file not valid' , '' , themeit = i1i1iI1iiiI )
  I1ii1ii11i1I ( '%s' % iiIiI1i1 , '' , themeit = i1i1iI1iiiI )
  return
 if wiz . checkBuild ( name , 'version' ) == False :
  I1ii1ii11i1I ( 'Error reading the txt file.' , '' , themeit = i1i1iI1iiiI )
  I1ii1ii11i1I ( '%s was not found in the builds list.' % name , '' , themeit = i1i1iI1iiiI )
  return
 Iii1iiIi1II = wiz . openURL ( OOOO0OOoO0O0 ) . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
 OO0O00oOo = re . compile ( 'name="%s".+?ersion="(.+?)".+?rl="(.+?)".+?ui="(.+?)".+?odi="(.+?)".+?heme="(.+?)".+?con="(.+?)".+?anart="(.+?)"' % name ) . findall ( Iii1iiIi1II )
 for iiI , OooOoOo , iIi1i1iIi1iI , III1I1Iii1iiI , Iiii1iI1i , i1Iii11I1i , Oo00o0OO0O00o in OO0O00oOo :
  i1Iii11I1i = i1Iii11I1i if wiz . workingURL ( i1Iii11I1i ) else iiIIIII1i1iI
  Oo00o0OO0O00o = Oo00o0OO0O00o if wiz . workingURL ( Oo00o0OO0O00o ) else I1i1iiI1
  oOIIiIi = '%s (v%s)' % ( name , iiI )
  if Oo0oO0ooo == name and iiI > o0oOoO00o :
   oOIIiIi = '%s [COLOR red][B][CURRENT v%s][/B][/COLOR]' % ( oOIIiIi , o0oOoO00o )
  I1ii1ii11i1I ( oOIIiIi , '' , fanart = Oo00o0OO0O00o , icon = i1Iii11I1i , themeit = ooo )
  I1ii1ii11i1I ( '===============[ Install ]===================' , '' , fanart = Oo00o0OO0O00o , icon = i1Iii11I1i , themeit = i1i1iI1iiiI )
  I1ii1ii11i1I ( 'Fresh Install' , 'install' , name , 'fresh' , fanart = Oo00o0OO0O00o , icon = i1Iii11I1i , themeit = i1I1i111Ii )
  I1ii1ii11i1I ( 'Standard Install' , 'install' , name , 'normal' , fanart = Oo00o0OO0O00o , icon = i1Iii11I1i , themeit = i1I1i111Ii )
  if not iIi1i1iIi1iI == 'http://' : I1ii1ii11i1I ( 'Apply guiFix' , 'install' , name , 'gui' , fanart = Oo00o0OO0O00o , icon = i1Iii11I1i , themeit = i1I1i111Ii )
  if not Iiii1iI1i == 'http://' :
   if wiz . workingURL ( Iiii1iI1i ) == True :
    I1ii1ii11i1I ( '===============[ Themes ]==================' , '' , fanart = Oo00o0OO0O00o , icon = i1Iii11I1i , themeit = i1i1iI1iiiI )
    Iii1iiIi1II = wiz . openURL ( Iiii1iI1i ) . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
    OO0O00oOo = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?con="(.+?)".+?anart="(.+?)"' ) . findall ( Iii1iiIi1II )
    for iiIi1iI1iIii , o00OooO0oo , o0o0oOoOO0O , i1ii1II1ii in OO0O00oOo :
     o0o0oOoOO0O = o0o0oOoOO0O if o0o0oOoOO0O == 'http://' else i1Iii11I1i
     i1ii1II1ii = i1ii1II1ii if i1ii1II1ii == 'http://' else Oo00o0OO0O00o
     I1ii1ii11i1I ( iiIi1iI1iIii if not iiIi1iI1iIii == i1 else "[B]%s (Installed)[/B]" % iiIi1iI1iIii , 'theme' , name , iiIi1iI1iIii , fanart = i1ii1II1ii , icon = o0o0oOoOO0O , themeit = i1i1iI1iiiI )
     if 28 - 28: ooOo0o0O00
     if 61 - 61: o0O0oO0O00O0o % o0O0oO0O00O0o * Ii / Ii
     if 75 - 75: IIIi11I11 . ooI1i
     if 50 - 50: iiiiII1I
def O00o0OO0000oo ( ) :
 OOoOooOoOOOoo ( 'SpinzTV APKS' , 'apkspinz' , icon = IiIi1I1 , themeit = i1I1i111Ii )
 OOoOooOoOOOoo ( 'My Android APPS' , 'apkin' , icon = IIOOO0O00O0OOOO , themeit = i1I1i111Ii )
 OOoOooOoOOOoo ( 'Kodi and SPMC' , 'apkkodi' , icon = I1III1111iIi , themeit = i1I1i111Ii )
 OOoOooOoOOOoo ( 'Android Games' , 'apkgames' , icon = I1i111I , themeit = i1I1i111Ii )
 OOoOooOoOOOoo ( 'Movie and Video' , 'apkvid' , icon = Ooo , themeit = i1I1i111Ii )
 OOoOooOoOOOoo ( 'System Tools' , 'apksys' , icon = Oo0oo0O0o00O , themeit = i1I1i111Ii )
 OOoOooOoOOOoo ( 'APK Master List' , 'apkmaster' , icon = IIOOO0O00O0OOOO , themeit = i1I1i111Ii )
 if 27 - 27: Ii1I11I
 if 79 - 79: Ii - II1I1Ii + Ii . i1I1
def ii1III11 ( ) :
 if oO0O00oOOoooO :
  Iii1iiIi1II = wiz . openURL ( O0Oo000ooO00 ) . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
 OO0O00oOo = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?con="(.+?)".+?anart="(.+?)"' ) . findall ( Iii1iiIi1II )
 if len ( OO0O00oOo ) > 0 :
  for iI1I , OooOoOo , i1Iii11I1i , Oo00o0OO0O00o in OO0O00oOo :
   I1ii1ii11i1I ( iI1I , 'apkinstall' , iI1I , OooOoOo , icon = i1Iii11I1i , fanart = Oo00o0OO0O00o , themeit = i1I1i111Ii )
  else : wiz . log ( "[APK Menu] ERROR: Invalid Format." )
 else : wiz . log ( "[APK Menu] ERROR: URL for apk list not working." )
 if 7 - 7: O0i11I1I1I % Ii1I11I . iiiiII1I + oo0o0000 - II1I1Ii
def o0o0O00oo0 ( ) :
 xbmc . executebuiltin ( 'ActivateWindow(10001,"androidapp://sources/apps/",return)' )
 if 27 - 27: i11iIiiIii % I11I1i1iIII1I % II1I1Ii . Ii1I11I - iI1i + iiiiII1I
def ooO0o ( ) :
 I1ii1ii11i1I ( 'Kodi (v%s)' % wiz . latestApk ( 'kodi' , 'version' ) , 'apkinstall' , 'kodi' , wiz . latestApk ( 'kodi' , 'url' ) , icon = I1III1111iIi , themeit = i1I1i111Ii )
 I1ii1ii11i1I ( 'SPMC (v%s)' % wiz . latestApk ( 'spmc' , 'version' ) , 'apkinstall' , 'spmc' , wiz . latestApk ( 'spmc' , 'url' ) , icon = I1i11 , themeit = i1I1i111Ii )
 if 51 - 51: IIIi11I11
def ii11I1 ( ) :
 if Oo0O00O000 :
  Iii1iiIi1II = wiz . openURL ( Ii1iIiII1ii1 ) . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
 OO0O00oOo = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?con="(.+?)".+?anart="(.+?)"' ) . findall ( Iii1iiIi1II )
 if len ( OO0O00oOo ) > 0 :
  for iI1I , OooOoOo , i1Iii11I1i , Oo00o0OO0O00o in OO0O00oOo :
   I1ii1ii11i1I ( iI1I , 'apkinstall' , iI1I , OooOoOo , icon = i1Iii11I1i , fanart = Oo00o0OO0O00o , themeit = i1I1i111Ii )
  else : wiz . log ( "[APK Menu] ERROR: Invalid Format." )
 else : wiz . log ( "[APK Menu] ERROR: URL for apk list not working." )
 if 75 - 75: iI1i11 / I11I1i1iIII1I % Ii1I11I
def Ii111iIi1iIi ( ) :
 OOoOooOoOOOoo ( 'Emulators' , 'emulators' , icon = I1i111I , themeit = i1I1i111Ii )
 OOoOooOoOOOoo ( 'Roms' , 'roms' , icon = I1i111I , themeit = i1I1i111Ii )
 if 21 - 21: i1I1 / ooOo0o0O00 + oOo000OOOo + iI1II
def OoOo ( ) :
 if i1Ii :
  Iii1iiIi1II = wiz . openURL ( OOoOO0oo0ooO ) . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
 OO0O00oOo = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?con="(.+?)".+?anart="(.+?)"' ) . findall ( Iii1iiIi1II )
 if len ( OO0O00oOo ) > 0 :
  for iI1I , OooOoOo , i1Iii11I1i , Oo00o0OO0O00o in OO0O00oOo :
   I1ii1ii11i1I ( iI1I , 'apkinstall' , iI1I , OooOoOo , icon = i1Iii11I1i , fanart = Oo00o0OO0O00o , themeit = i1I1i111Ii )
  else : wiz . log ( "[APK Menu] ERROR: Invalid Format." )
 else : wiz . log ( "[APK Menu] ERROR: URL for emu list not working." )
 if 35 - 35: ooI1i * o0O0oO0O00O0o . II1I1Ii * Ii . iiiiII1I / Ii1I11I
 if 100 - 100: iIIIII1I . Ii * iI1i % Ii1I11I * Ii1I11I
 if 14 - 14: ooOo0o0O00 . ooI1i + I11I1i1iIII1I / O0i11I1I1I / II1I1Ii
 if 74 - 74: Ii1I11I / o0OOo0o0O0O
def OoO ( ) :
 OOoOooOoOOOoo ( 'SNES' , 'snes' , icon = I1i111I , themeit = i1I1i111Ii )
 OOoOooOoOOOoo ( 'NES' , 'nes' , icon = I1i111I , themeit = i1I1i111Ii )
 OOoOooOoOOOoo ( 'N64' , 'n64' , icon = I1i111I , themeit = i1I1i111Ii )
 OOoOooOoOOOoo ( 'Genesis' , 'gen' , icon = I1i111I , themeit = i1I1i111Ii )
 OOoOooOoOOOoo ( 'Atari' , 'atr' , icon = I1i111I , themeit = i1I1i111Ii )
 OOoOooOoOOOoo ( 'PC Engine & Turbo Grafx' , 'tbg' , icon = I1i111I , themeit = i1I1i111Ii )
 if 41 - 41: o0OOo0o0O0O * I11I1i1iIII1I / iI1II . o0O0oO0O00O0o
def O0iII1 ( ) :
 if ii111iI1iIi1 :
  Iii1iiIi1II = wiz . openURL ( OOO00O ) . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
 OO0O00oOo = re . compile ( '.+?ame="(.+?)".+?rl="(.+?)".+?con="(.+?)".+?anart="(.+?)"description="(.+?)"' ) . findall ( Iii1iiIi1II )
 if len ( OO0O00oOo ) > 0 :
  for iI1I , OooOoOo , i1Iii11I1i , Oo00o0OO0O00o , IIII1i in OO0O00oOo :
   Ii1IIIIi1ii1I ( iI1I , 'rominstall' , iI1I , OooOoOo , icon = i1Iii11I1i , fanart = Oo00o0OO0O00o , description = IIII1i , themeit = i1I1i111Ii )
  else : wiz . log ( "[ROM Menu] ERROR: Invalid Format." )
 else : wiz . log ( "[ROM Menu] ERROR: URL for apk list not working." )
 if 13 - 13: oo0o0000 % iiiiII1I . ooOo0o0O00 / iI1i % o0O0oO0O00O0o . iI1II
def i1iIi ( ) :
 OOoOooOoOOOoo ( 'NES Titles A Thru B' , 'nesa' , icon = I1i111I , themeit = i1I1i111Ii )
 OOoOooOoOOOoo ( 'NES Titles C' , 'nesc' , icon = IIOOO0O00O0OOOO , themeit = i1I1i111Ii )
 OOoOooOoOOOoo ( 'NES Titles D Thru E' , 'nesd' , icon = I1i111I , themeit = i1I1i111Ii )
 OOoOooOoOOOoo ( 'NES Titles F Thru G' , 'nesf' , icon = I1i111I , themeit = i1I1i111Ii )
 OOoOooOoOOOoo ( 'NES Titles H Thru K' , 'nesh' , icon = I1i111I , themeit = i1I1i111Ii )
 OOoOooOoOOOoo ( 'NES Titles L Thru M' , 'nesl' , icon = I1i111I , themeit = i1I1i111Ii )
 OOoOooOoOOOoo ( 'NES Titles N Thru Q' , 'nesn' , icon = I1i111I , themeit = i1I1i111Ii )
 OOoOooOoOOOoo ( 'NES Titles R Thru S' , 'nesr' , icon = I1i111I , themeit = i1I1i111Ii )
 OOoOooOoOOOoo ( 'NES Titles T Thru V' , 'nest' , icon = I1i111I , themeit = i1I1i111Ii )
 OOoOooOoOOOoo ( 'NES Titles W Thru Z' , 'nesw' , icon = I1i111I , themeit = i1I1i111Ii )
 if 30 - 30: Ii1I11I - oo0 / iI1II
def O0000OOO0 ( ) :
 if OOO :
  Iii1iiIi1II = wiz . openURL ( O0o0O00Oo0o0 ) . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
 OO0O00oOo = re . compile ( '.+?ame="(.+?)".+?rl="(.+?)".+?con="(.+?)".+?anart="(.+?)"description="(.+?)"' ) . findall ( Iii1iiIi1II )
 if len ( OO0O00oOo ) > 0 :
  for iI1I , OooOoOo , i1Iii11I1i , Oo00o0OO0O00o , IIII1i in OO0O00oOo :
   Ii1IIIIi1ii1I ( iI1I , 'rominstall' , iI1I , OooOoOo , icon = i1Iii11I1i , fanart = Oo00o0OO0O00o , description = IIII1i , themeit = i1I1i111Ii )
  else : wiz . log ( "[ROM Menu] ERROR: Invalid Format." )
 else : wiz . log ( "[ROM Menu] ERROR: URL for rom list not working." )
 if 51 - 51: oo0o0000 / IIIi11I11 / oOo000OOOo
def I111iIi1 ( ) :
 if oo0OOo0 :
  Iii1iiIi1II = wiz . openURL ( O00O0oOO00O00 ) . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
 OO0O00oOo = re . compile ( '.+?ame="(.+?)".+?rl="(.+?)".+?con="(.+?)".+?anart="(.+?)"description="(.+?)"' ) . findall ( Iii1iiIi1II )
 if len ( OO0O00oOo ) > 0 :
  for iI1I , OooOoOo , i1Iii11I1i , Oo00o0OO0O00o , IIII1i in OO0O00oOo :
   Ii1IIIIi1ii1I ( iI1I , 'rominstall' , iI1I , OooOoOo , icon = i1Iii11I1i , fanart = Oo00o0OO0O00o , description = IIII1i , themeit = i1I1i111Ii )
  else : wiz . log ( "[ROM Menu] ERROR: Invalid Format." )
 else : wiz . log ( "[ROM Menu] ERROR: URL for rom list not working." )
 if 92 - 92: ooI1i
def II11iI111i1 ( ) :
 if I11IiI :
  Iii1iiIi1II = wiz . openURL ( i1Oo00 ) . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
 OO0O00oOo = re . compile ( '.+?ame="(.+?)".+?rl="(.+?)".+?con="(.+?)".+?anart="(.+?)"description="(.+?)"' ) . findall ( Iii1iiIi1II )
 if len ( OO0O00oOo ) > 0 :
  for iI1I , OooOoOo , i1Iii11I1i , Oo00o0OO0O00o , IIII1i in OO0O00oOo :
   Ii1IIIIi1ii1I ( iI1I , 'rominstall' , iI1I , OooOoOo , icon = i1Iii11I1i , fanart = Oo00o0OO0O00o , description = IIII1i , themeit = i1I1i111Ii )
  else : wiz . log ( "[ROM Menu] ERROR: Invalid Format." )
 else : wiz . log ( "[ROM Menu] ERROR: URL for rom list not working." )
 if 95 - 95: iI1II - IIIi11I11 * oo0o0000 + iiiiII1I
def iIi1 ( ) :
 if O0ooO0Oo00o :
  Iii1iiIi1II = wiz . openURL ( i1i ) . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
 OO0O00oOo = re . compile ( '.+?ame="(.+?)".+?rl="(.+?)".+?con="(.+?)".+?anart="(.+?)"description="(.+?)"' ) . findall ( Iii1iiIi1II )
 if len ( OO0O00oOo ) > 0 :
  for iI1I , OooOoOo , i1Iii11I1i , Oo00o0OO0O00o , IIII1i in OO0O00oOo :
   Ii1IIIIi1ii1I ( iI1I , 'rominstall' , iI1I , OooOoOo , icon = i1Iii11I1i , fanart = Oo00o0OO0O00o , description = IIII1i , themeit = i1I1i111Ii )
  else : wiz . log ( "[ROM Menu] ERROR: Invalid Format." )
 else : wiz . log ( "[ROM Menu] ERROR: URL for rom list not working." )
 if 21 - 21: II1I1Ii
def OoO00 ( ) :
 if ooO0oOOooOo0 :
  Iii1iiIi1II = wiz . openURL ( iiI111I1iIiI ) . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
 OO0O00oOo = re . compile ( '.+?ame="(.+?)".+?rl="(.+?)".+?con="(.+?)".+?anart="(.+?)"description="(.+?)"' ) . findall ( Iii1iiIi1II )
 if len ( OO0O00oOo ) > 0 :
  for iI1I , OooOoOo , i1Iii11I1i , Oo00o0OO0O00o , IIII1i in OO0O00oOo :
   Ii1IIIIi1ii1I ( iI1I , 'rominstall' , iI1I , OooOoOo , icon = i1Iii11I1i , fanart = Oo00o0OO0O00o , description = IIII1i , themeit = i1I1i111Ii )
  else : wiz . log ( "[ROM Menu] ERROR: Invalid Format." )
 else : wiz . log ( "[ROM Menu] ERROR: URL for rom list not working." )
 if 85 - 85: iI1i * iI1i * oo0o0000 . iI1II . oOo000OOOo * ooI1i
def o000oOoo0o000 ( ) :
 if i1I1ii11i1Iii :
  Iii1iiIi1II = wiz . openURL ( IIIi1I1IIii1II ) . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
 OO0O00oOo = re . compile ( '.+?ame="(.+?)".+?rl="(.+?)".+?con="(.+?)".+?anart="(.+?)"description="(.+?)"' ) . findall ( Iii1iiIi1II )
 if len ( OO0O00oOo ) > 0 :
  for iI1I , OooOoOo , i1Iii11I1i , Oo00o0OO0O00o , IIII1i in OO0O00oOo :
   Ii1IIIIi1ii1I ( iI1I , 'rominstall' , iI1I , OooOoOo , icon = i1Iii11I1i , fanart = Oo00o0OO0O00o , description = IIII1i , themeit = i1I1i111Ii )
  else : wiz . log ( "[ROM Menu] ERROR: Invalid Format." )
 else : wiz . log ( "[ROM Menu] ERROR: URL for rom list not working." )
 if 40 - 40: i11iIiiIii * iIIIII1I - o0OOo0o0O0O * iIIIII1I - II1I1Ii . o0OOo0o0O0O
def oo0O0Ooooooo ( ) :
 if I1IiiiiI :
  Iii1iiIi1II = wiz . openURL ( O0 ) . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
 OO0O00oOo = re . compile ( '.+?ame="(.+?)".+?rl="(.+?)".+?con="(.+?)".+?anart="(.+?)"description="(.+?)"' ) . findall ( Iii1iiIi1II )
 if len ( OO0O00oOo ) > 0 :
  for iI1I , OooOoOo , i1Iii11I1i , Oo00o0OO0O00o , IIII1i in OO0O00oOo :
   Ii1IIIIi1ii1I ( iI1I , 'rominstall' , iI1I , OooOoOo , icon = i1Iii11I1i , fanart = Oo00o0OO0O00o , description = IIII1i , themeit = i1I1i111Ii )
  else : wiz . log ( "[ROM Menu] ERROR: Invalid Format." )
 else : wiz . log ( "[ROM Menu] ERROR: URL for rom list not working." )
 if 39 - 39: IIIi11I11 * iI1i + oo0 - IIIi11I11 + o0O0oO0O00O0o
def o0iiiI1I1iIIIi1 ( ) :
 if o0OIiII :
  Iii1iiIi1II = wiz . openURL ( ii1ii1ii ) . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
 OO0O00oOo = re . compile ( '.+?ame="(.+?)".+?rl="(.+?)".+?con="(.+?)".+?anart="(.+?)"description="(.+?)"' ) . findall ( Iii1iiIi1II )
 if len ( OO0O00oOo ) > 0 :
  for iI1I , OooOoOo , i1Iii11I1i , Oo00o0OO0O00o , IIII1i in OO0O00oOo :
   Ii1IIIIi1ii1I ( iI1I , 'rominstall' , iI1I , OooOoOo , icon = i1Iii11I1i , fanart = Oo00o0OO0O00o , description = IIII1i , themeit = i1I1i111Ii )
  else : wiz . log ( "[ROM Menu] ERROR: Invalid Format." )
 else : wiz . log ( "[ROM Menu] ERROR: URL for rom list not working." )
 if 17 - 17: oo0 . iI1II / II1I1Ii % I11I1i1iIII1I % o0OOo0o0O0O / i11iIiiIii
def OOOIiiiii1iI ( ) :
 if ii1iII1II :
  Iii1iiIi1II = wiz . openURL ( oooooOoo0ooo ) . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
 OO0O00oOo = re . compile ( '.+?ame="(.+?)".+?rl="(.+?)".+?con="(.+?)".+?anart="(.+?)"description="(.+?)"' ) . findall ( Iii1iiIi1II )
 if len ( OO0O00oOo ) > 0 :
  for iI1I , OooOoOo , i1Iii11I1i , Oo00o0OO0O00o , IIII1i in OO0O00oOo :
   Ii1IIIIi1ii1I ( iI1I , 'rominstall' , iI1I , OooOoOo , icon = i1Iii11I1i , fanart = Oo00o0OO0O00o , description = IIII1i , themeit = i1I1i111Ii )
  else : wiz . log ( "[ROM Menu] ERROR: Invalid Format." )
 else : wiz . log ( "[ROM Menu] ERROR: URL for rom list not working." )
 if 49 - 49: Ii . IIIi11I11 / iI1i11 + I11I1i1iIII1I
def ii11i ( ) :
 if Iii1I1I11iiI1 :
  Iii1iiIi1II = wiz . openURL ( I1I1IiI1 ) . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
 OO0O00oOo = re . compile ( '.+?ame="(.+?)".+?rl="(.+?)".+?con="(.+?)".+?anart="(.+?)"description="(.+?)"' ) . findall ( Iii1iiIi1II )
 if len ( OO0O00oOo ) > 0 :
  for iI1I , OooOoOo , i1Iii11I1i , Oo00o0OO0O00o , IIII1i in OO0O00oOo :
   Ii1IIIIi1ii1I ( iI1I , 'rominstall' , iI1I , OooOoOo , icon = i1Iii11I1i , fanart = Oo00o0OO0O00o , description = IIII1i , themeit = i1I1i111Ii )
  else : wiz . log ( "[ROM Menu] ERROR: Invalid Format." )
 else : wiz . log ( "[ROM Menu] ERROR: URL for rom list not working." )
 if 35 - 35: ooOo0o0O00 * O0i11I1I1I - iI1i11 % Ii
def oOo00O000Oo0 ( ) :
 OOoOooOoOOOoo ( 'Genesis Titles A Thru B' , 'gena' , icon = I1i111I , themeit = i1I1i111Ii )
 OOoOooOoOOOoo ( 'Genesis Titles C Thru D' , 'genc' , icon = IIOOO0O00O0OOOO , themeit = i1I1i111Ii )
 OOoOooOoOOOoo ( 'Genesis Titles E Thru G' , 'gene' , icon = I1i111I , themeit = i1I1i111Ii )
 OOoOooOoOOOoo ( 'Genesis Titles H Thru L' , 'genh' , icon = I1i111I , themeit = i1I1i111Ii )
 OOoOooOoOOOoo ( 'Genesis Titles M Thru O' , 'genm' , icon = I1i111I , themeit = i1I1i111Ii )
 OOoOooOoOOOoo ( 'Genesis Titles P Thru R' , 'genp' , icon = I1i111I , themeit = i1I1i111Ii )
 OOoOooOoOOOoo ( 'Genesis Titles S Thru T' , 'gens' , icon = I1i111I , themeit = i1I1i111Ii )
 OOoOooOoOOOoo ( 'Genesis Titles U Thru Z' , 'genu' , icon = I1i111I , themeit = i1I1i111Ii )
 if 18 - 18: O0i11I1I1I * iI1i11 . iI1i11 * i1I1 * I11I1i1iIII1I * iIIIII1I
def oOooO0OOOoO000 ( ) :
 if I1I1i1I :
  Iii1iiIi1II = wiz . openURL ( III1iII1I1ii ) . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
 OO0O00oOo = re . compile ( '.+?ame="(.+?)".+?rl="(.+?)".+?con="(.+?)".+?anart="(.+?)"description="(.+?)"' ) . findall ( Iii1iiIi1II )
 if len ( OO0O00oOo ) > 0 :
  for iI1I , OooOoOo , i1Iii11I1i , Oo00o0OO0O00o , IIII1i in OO0O00oOo :
   Ii1IIIIi1ii1I ( iI1I , 'rominstall' , iI1I , OooOoOo , icon = i1Iii11I1i , fanart = Oo00o0OO0O00o , description = IIII1i , themeit = i1I1i111Ii )
  else : wiz . log ( "[ROM Menu] ERROR: Invalid Format." )
 else : wiz . log ( "[ROM Menu] ERROR: URL for rom list not working." )
 if 57 - 57: I11I1i1iIII1I
def oOOOoo ( ) :
 if ii1I :
  Iii1iiIi1II = wiz . openURL ( oOOo0 ) . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
 OO0O00oOo = re . compile ( '.+?ame="(.+?)".+?rl="(.+?)".+?con="(.+?)".+?anart="(.+?)"description="(.+?)"' ) . findall ( Iii1iiIi1II )
 if len ( OO0O00oOo ) > 0 :
  for iI1I , OooOoOo , i1Iii11I1i , Oo00o0OO0O00o , IIII1i in OO0O00oOo :
   Ii1IIIIi1ii1I ( iI1I , 'rominstall' , iI1I , OooOoOo , icon = i1Iii11I1i , fanart = Oo00o0OO0O00o , description = IIII1i , themeit = i1I1i111Ii )
  else : wiz . log ( "[ROM Menu] ERROR: Invalid Format." )
 else : wiz . log ( "[ROM Menu] ERROR: URL for rom list not working." )
 if 15 - 15: i11iIiiIii % oo0o0000 * II1I1Ii / iIIIII1I
def oooO0o0o0O0 ( ) :
 if O0oO0 :
  Iii1iiIi1II = wiz . openURL ( oo00O00oO ) . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
 OO0O00oOo = re . compile ( '.+?ame="(.+?)".+?rl="(.+?)".+?con="(.+?)".+?anart="(.+?)"description="(.+?)"' ) . findall ( Iii1iiIi1II )
 if len ( OO0O00oOo ) > 0 :
  for iI1I , OooOoOo , i1Iii11I1i , Oo00o0OO0O00o , IIII1i in OO0O00oOo :
   Ii1IIIIi1ii1I ( iI1I , 'rominstall' , iI1I , OooOoOo , icon = i1Iii11I1i , fanart = Oo00o0OO0O00o , description = IIII1i , themeit = i1I1i111Ii )
  else : wiz . log ( "[ROM Menu] ERROR: Invalid Format." )
 else : wiz . log ( "[ROM Menu] ERROR: URL for rom list not working." )
 if 27 - 27: iI1II - O0i11I1I1I / II1I1Ii
def OOooOo00oo0 ( ) :
 if oO0O0OO0O :
  Iii1iiIi1II = wiz . openURL ( iIiIIIi ) . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
 OO0O00oOo = re . compile ( '.+?ame="(.+?)".+?rl="(.+?)".+?con="(.+?)".+?anart="(.+?)"description="(.+?)"' ) . findall ( Iii1iiIi1II )
 if len ( OO0O00oOo ) > 0 :
  for iI1I , OooOoOo , i1Iii11I1i , Oo00o0OO0O00o , IIII1i in OO0O00oOo :
   Ii1IIIIi1ii1I ( iI1I , 'rominstall' , iI1I , OooOoOo , icon = i1Iii11I1i , fanart = Oo00o0OO0O00o , description = IIII1i , themeit = i1I1i111Ii )
  else : wiz . log ( "[ROM Menu] ERROR: Invalid Format." )
 else : wiz . log ( "[ROM Menu] ERROR: URL for rom list not working." )
 if 84 - 84: iIIIII1I + II1I1Ii
def IIiiIIi1 ( ) :
 if OO :
  Iii1iiIi1II = wiz . openURL ( ooo00OOOooO ) . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
 OO0O00oOo = re . compile ( '.+?ame="(.+?)".+?rl="(.+?)".+?con="(.+?)".+?anart="(.+?)"description="(.+?)"' ) . findall ( Iii1iiIi1II )
 if len ( OO0O00oOo ) > 0 :
  for iI1I , OooOoOo , i1Iii11I1i , Oo00o0OO0O00o , IIII1i in OO0O00oOo :
   Ii1IIIIi1ii1I ( iI1I , 'rominstall' , iI1I , OooOoOo , icon = i1Iii11I1i , fanart = Oo00o0OO0O00o , description = IIII1i , themeit = i1I1i111Ii )
  else : wiz . log ( "[ROM Menu] ERROR: Invalid Format." )
 else : wiz . log ( "[ROM Menu] ERROR: URL for rom list not working." )
 if 59 - 59: IIIi11I11 . o0O0oO0O00O0o % I11I1i1iIII1I
def i11I1iIi ( ) :
 if OoOoO :
  Iii1iiIi1II = wiz . openURL ( O00OOOoOoo0O ) . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
 OO0O00oOo = re . compile ( '.+?ame="(.+?)".+?rl="(.+?)".+?con="(.+?)".+?anart="(.+?)"description="(.+?)"' ) . findall ( Iii1iiIi1II )
 if len ( OO0O00oOo ) > 0 :
  for iI1I , OooOoOo , i1Iii11I1i , Oo00o0OO0O00o , IIII1i in OO0O00oOo :
   Ii1IIIIi1ii1I ( iI1I , 'rominstall' , iI1I , OooOoOo , icon = i1Iii11I1i , fanart = Oo00o0OO0O00o , description = IIII1i , themeit = i1I1i111Ii )
  else : wiz . log ( "[ROM Menu] ERROR: Invalid Format." )
 else : wiz . log ( "[ROM Menu] ERROR: URL for rom list not working." )
 if 79 - 79: iIIIII1I . i1I1 - I11I1i1iIII1I . oo0o0000 % ooI1i
def oOoO00 ( ) :
 if Ii1I1i :
  Iii1iiIi1II = wiz . openURL ( O000OOo00oo ) . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
 OO0O00oOo = re . compile ( '.+?ame="(.+?)".+?rl="(.+?)".+?con="(.+?)".+?anart="(.+?)"description="(.+?)"' ) . findall ( Iii1iiIi1II )
 if len ( OO0O00oOo ) > 0 :
  for iI1I , OooOoOo , i1Iii11I1i , Oo00o0OO0O00o , IIII1i in OO0O00oOo :
   Ii1IIIIi1ii1I ( iI1I , 'rominstall' , iI1I , OooOoOo , icon = i1Iii11I1i , fanart = Oo00o0OO0O00o , description = IIII1i , themeit = i1I1i111Ii )
  else : wiz . log ( "[ROM Menu] ERROR: Invalid Format." )
 else : wiz . log ( "[ROM Menu] ERROR: URL for rom list not working." )
 if 40 - 40: Ii
def OOOooo ( ) :
 if OOI1iI1ii1II :
  Iii1iiIi1II = wiz . openURL ( oo0OOo ) . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
 OO0O00oOo = re . compile ( '.+?ame="(.+?)".+?rl="(.+?)".+?con="(.+?)".+?anart="(.+?)"description="(.+?)"' ) . findall ( Iii1iiIi1II )
 if len ( OO0O00oOo ) > 0 :
  for iI1I , OooOoOo , i1Iii11I1i , Oo00o0OO0O00o , IIII1i in OO0O00oOo :
   Ii1IIIIi1ii1I ( iI1I , 'rominstall' , iI1I , OooOoOo , icon = i1Iii11I1i , fanart = Oo00o0OO0O00o , description = IIII1i , themeit = i1I1i111Ii )
  else : wiz . log ( "[ROM Menu] ERROR: Invalid Format." )
 else : wiz . log ( "[ROM Menu] ERROR: URL for rom list not working." )
 if 99 - 99: I11I1i1iIII1I * IIIi11I11 % oo0 / oOo000OOOo
def OOO00O0oOOo ( ) :
 OOoOooOoOOOoo ( 'Atari Titles A Thru B' , 'atra' , icon = I1i111I , themeit = i1I1i111Ii )
 OOoOooOoOOOoo ( 'Atari Titles C Thru D' , 'atrc' , icon = IIOOO0O00O0OOOO , themeit = i1I1i111Ii )
 OOoOooOoOOOoo ( 'Atari Titles E Thru G' , 'atre' , icon = I1i111I , themeit = i1I1i111Ii )
 OOoOooOoOOOoo ( 'Atari Titles H Thru L' , 'atrh' , icon = I1i111I , themeit = i1I1i111Ii )
 OOoOooOoOOOoo ( 'Atari Titles M Thru O' , 'atrm' , icon = I1i111I , themeit = i1I1i111Ii )
 OOoOooOoOOOoo ( 'Atari Titles P Thru R' , 'atrp' , icon = I1i111I , themeit = i1I1i111Ii )
 OOoOooOoOOOoo ( 'Atari Titles S Thru U' , 'atrs' , icon = I1i111I , themeit = i1I1i111Ii )
 OOoOooOoOOOoo ( 'Atari Titles V Thru Z' , 'atrv' , icon = I1i111I , themeit = i1I1i111Ii )
 if 71 - 71: II1I1Ii / Ii / iIIIII1I % o0O0oO0O00O0o
def O0oooo00o0Oo ( ) :
 if O0O0OOOOoo :
  Iii1iiIi1II = wiz . openURL ( ooOOO00Ooo ) . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
 OO0O00oOo = re . compile ( '.+?ame="(.+?)".+?rl="(.+?)".+?con="(.+?)".+?anart="(.+?)"description="(.+?)"' ) . findall ( Iii1iiIi1II )
 if len ( OO0O00oOo ) > 0 :
  for iI1I , OooOoOo , i1Iii11I1i , Oo00o0OO0O00o , IIII1i in OO0O00oOo :
   Ii1IIIIi1ii1I ( iI1I , 'rominstall' , iI1I , OooOoOo , icon = i1Iii11I1i , fanart = Oo00o0OO0O00o , description = IIII1i , themeit = i1I1i111Ii )
  else : wiz . log ( "[ROM Menu] ERROR: Invalid Format." )
 else : wiz . log ( "[ROM Menu] ERROR: URL for rom list not working." )
 if 36 - 36: oOo000OOOo / I11I1i1iIII1I / IIIi11I11 / IIIi11I11 + ooOo0o0O00
def oO0Ooo0ooOO0 ( ) :
 if oOooO0 :
  Iii1iiIi1II = wiz . openURL ( IiIIIi1iIi ) . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
 OO0O00oOo = re . compile ( '.+?ame="(.+?)".+?rl="(.+?)".+?con="(.+?)".+?anart="(.+?)"description="(.+?)"' ) . findall ( Iii1iiIi1II )
 if len ( OO0O00oOo ) > 0 :
  for iI1I , OooOoOo , i1Iii11I1i , Oo00o0OO0O00o , IIII1i in OO0O00oOo :
   Ii1IIIIi1ii1I ( iI1I , 'rominstall' , iI1I , OooOoOo , icon = i1Iii11I1i , fanart = Oo00o0OO0O00o , description = IIII1i , themeit = i1I1i111Ii )
  else : wiz . log ( "[ROM Menu] ERROR: Invalid Format." )
 else : wiz . log ( "[ROM Menu] ERROR: URL for rom list not working." )
 if 46 - 46: oOo000OOOo % iiiiII1I
def ooo0o0O0o ( ) :
 if Ii1I1Ii :
  Iii1iiIi1II = wiz . openURL ( ooOOoooooo ) . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
 OO0O00oOo = re . compile ( '.+?ame="(.+?)".+?rl="(.+?)".+?con="(.+?)".+?anart="(.+?)"description="(.+?)"' ) . findall ( Iii1iiIi1II )
 if len ( OO0O00oOo ) > 0 :
  for iI1I , OooOoOo , i1Iii11I1i , Oo00o0OO0O00o , IIII1i in OO0O00oOo :
   Ii1IIIIi1ii1I ( iI1I , 'rominstall' , iI1I , OooOoOo , icon = i1Iii11I1i , fanart = Oo00o0OO0O00o , description = IIII1i , themeit = i1I1i111Ii )
  else : wiz . log ( "[ROM Menu] ERROR: Invalid Format." )
 else : wiz . log ( "[ROM Menu] ERROR: URL for rom list not working." )
 if 62 - 62: ooI1i + i11iIiiIii + iI1i / i11iIiiIii
def I1Ii ( ) :
 if OOoO0 :
  Iii1iiIi1II = wiz . openURL ( II1I ) . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
 OO0O00oOo = re . compile ( '.+?ame="(.+?)".+?rl="(.+?)".+?con="(.+?)".+?anart="(.+?)"description="(.+?)"' ) . findall ( Iii1iiIi1II )
 if len ( OO0O00oOo ) > 0 :
  for iI1I , OooOoOo , i1Iii11I1i , Oo00o0OO0O00o , IIII1i in OO0O00oOo :
   Ii1IIIIi1ii1I ( iI1I , 'rominstall' , iI1I , OooOoOo , icon = i1Iii11I1i , fanart = Oo00o0OO0O00o , description = IIII1i , themeit = i1I1i111Ii )
  else : wiz . log ( "[ROM Menu] ERROR: Invalid Format." )
 else : wiz . log ( "[ROM Menu] ERROR: URL for rom list not working." )
 if 70 - 70: iI1i . iI1II - O0i11I1I1I
def iII11I1Ii1 ( ) :
 if OO0Oooo0oOO0O :
  Iii1iiIi1II = wiz . openURL ( O0i1II1Iiii1I11 ) . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
 OO0O00oOo = re . compile ( '.+?ame="(.+?)".+?rl="(.+?)".+?con="(.+?)".+?anart="(.+?)"description="(.+?)"' ) . findall ( Iii1iiIi1II )
 if len ( OO0O00oOo ) > 0 :
  for iI1I , OooOoOo , i1Iii11I1i , Oo00o0OO0O00o , IIII1i in OO0O00oOo :
   Ii1IIIIi1ii1I ( iI1I , 'rominstall' , iI1I , OooOoOo , icon = i1Iii11I1i , fanart = Oo00o0OO0O00o , description = IIII1i , themeit = i1I1i111Ii )
  else : wiz . log ( "[ROM Menu] ERROR: Invalid Format." )
 else : wiz . log ( "[ROM Menu] ERROR: URL for rom list not working." )
 if 92 - 92: II1I1Ii / II1I1Ii . ooOo0o0O00
def ii1iIi1II ( ) :
 if o00O0 :
  Iii1iiIi1II = wiz . openURL ( IIII ) . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
 OO0O00oOo = re . compile ( '.+?ame="(.+?)".+?rl="(.+?)".+?con="(.+?)".+?anart="(.+?)"description="(.+?)"' ) . findall ( Iii1iiIi1II )
 if len ( OO0O00oOo ) > 0 :
  for iI1I , OooOoOo , i1Iii11I1i , Oo00o0OO0O00o , IIII1i in OO0O00oOo :
   Ii1IIIIi1ii1I ( iI1I , 'rominstall' , iI1I , OooOoOo , icon = i1Iii11I1i , fanart = Oo00o0OO0O00o , description = IIII1i , themeit = i1I1i111Ii )
  else : wiz . log ( "[ROM Menu] ERROR: Invalid Format." )
 else : wiz . log ( "[ROM Menu] ERROR: URL for rom list not working." )
 if 2 - 2: iI1i + iiiiII1I - o0O0oO0O00O0o . oo0o0000 - o0O0oO0O00O0o
def oo0o0oooo ( ) :
 if oOO0O00Oo0O0o :
  Iii1iiIi1II = wiz . openURL ( iiIiI ) . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
 OO0O00oOo = re . compile ( '.+?ame="(.+?)".+?rl="(.+?)".+?con="(.+?)".+?anart="(.+?)"description="(.+?)"' ) . findall ( Iii1iiIi1II )
 if len ( OO0O00oOo ) > 0 :
  for iI1I , OooOoOo , i1Iii11I1i , Oo00o0OO0O00o , IIII1i in OO0O00oOo :
   Ii1IIIIi1ii1I ( iI1I , 'rominstall' , iI1I , OooOoOo , icon = i1Iii11I1i , fanart = Oo00o0OO0O00o , description = IIII1i , themeit = i1I1i111Ii )
  else : wiz . log ( "[ROM Menu] ERROR: Invalid Format." )
 else : wiz . log ( "[ROM Menu] ERROR: URL for rom list not working." )
 if 20 - 20: o0OOo0o0O0O - II1I1Ii
def ii1ii11 ( ) :
 if ii1 :
  Iii1iiIi1II = wiz . openURL ( o00oooO0Oo ) . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
 OO0O00oOo = re . compile ( '.+?ame="(.+?)".+?rl="(.+?)".+?con="(.+?)".+?anart="(.+?)"description="(.+?)"' ) . findall ( Iii1iiIi1II )
 if len ( OO0O00oOo ) > 0 :
  for iI1I , OooOoOo , i1Iii11I1i , Oo00o0OO0O00o , IIII1i in OO0O00oOo :
   Ii1IIIIi1ii1I ( iI1I , 'rominstall' , iI1I , OooOoOo , icon = i1Iii11I1i , fanart = Oo00o0OO0O00o , description = IIII1i , themeit = i1I1i111Ii )
  else : wiz . log ( "[ROM Menu] ERROR: Invalid Format." )
 else : wiz . log ( "[ROM Menu] ERROR: URL for rom list not working." )
 if 84 - 84: Ii1I11I . II1I1Ii - I11I1i1iIII1I . ooI1i / I11I1i1iIII1I
def iii1 ( ) :
 if I1iIIiiIIi1i :
  Iii1iiIi1II = wiz . openURL ( o0O0OOO0Ooo ) . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
 OO0O00oOo = re . compile ( '.+?ame="(.+?)".+?rl="(.+?)".+?con="(.+?)".+?anart="(.+?)"description="(.+?)"' ) . findall ( Iii1iiIi1II )
 if len ( OO0O00oOo ) > 0 :
  for iI1I , OooOoOo , i1Iii11I1i , Oo00o0OO0O00o , IIII1i in OO0O00oOo :
   Ii1IIIIi1ii1I ( iI1I , 'rominstall' , iI1I , OooOoOo , icon = i1Iii11I1i , fanart = Oo00o0OO0O00o , description = IIII1i , themeit = i1I1i111Ii )
  else : wiz . log ( "[ROM Menu] ERROR: Invalid Format." )
 else : wiz . log ( "[ROM Menu] ERROR: URL for rom list not working." )
 if 32 - 32: oOo000OOOo . IIIi11I11 . iI1II - iI1i11 + i1I1
def ooO0oO00O0o ( ) :
 OOoOooOoOOOoo ( 'PC Engine And Turbo Grafx Titles A Thru B' , 'tga' , icon = I1i111I , themeit = i1I1i111Ii )
 OOoOooOoOOOoo ( 'PC Engine And Turbo Grafx Titles C Thru E' , 'tgc' , icon = IIOOO0O00O0OOOO , themeit = i1I1i111Ii )
 OOoOooOoOOOoo ( 'PC Engine And Turbo Grafx Titles F Thru I' , 'tgf' , icon = I1i111I , themeit = i1I1i111Ii )
 OOoOooOoOOOoo ( 'PC Engine And Turbo Grafx Titles J Thru M' , 'tgj' , icon = I1i111I , themeit = i1I1i111Ii )
 OOoOooOoOOOoo ( 'PC Engine And Turbo Grafx Titles N Thru Q' , 'tgn' , icon = I1i111I , themeit = i1I1i111Ii )
 OOoOooOoOOOoo ( 'PC Engine And Turbo Grafx Titles R Thru U' , 'tgr' , icon = I1i111I , themeit = i1I1i111Ii )
 OOoOooOoOOOoo ( 'PC Engine And Turbo Grafx Titles V Thru Z' , 'tgv' , icon = I1i111I , themeit = i1I1i111Ii )
 if 70 - 70: iIIIII1I
def i11iIIi11 ( ) :
 if O0O0ooOOO :
  Iii1iiIi1II = wiz . openURL ( iiIiII1 ) . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
 OO0O00oOo = re . compile ( '.+?ame="(.+?)".+?rl="(.+?)".+?con="(.+?)".+?anart="(.+?)"description="(.+?)"' ) . findall ( Iii1iiIi1II )
 if len ( OO0O00oOo ) > 0 :
  for iI1I , OooOoOo , i1Iii11I1i , Oo00o0OO0O00o , IIII1i in OO0O00oOo :
   Ii1IIIIi1ii1I ( iI1I , 'rominstall' , iI1I , OooOoOo , icon = i1Iii11I1i , fanart = Oo00o0OO0O00o , description = IIII1i , themeit = i1I1i111Ii )
  else : wiz . log ( "[ROM Menu] ERROR: Invalid Format." )
 else : wiz . log ( "[ROM Menu] ERROR: URL for rom list not working." )
 if 98 - 98: iIIIII1I
def ii ( ) :
 if oOOo0O00o :
  Iii1iiIi1II = wiz . openURL ( OOO00O0O ) . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
 OO0O00oOo = re . compile ( '.+?ame="(.+?)".+?rl="(.+?)".+?con="(.+?)".+?anart="(.+?)"description="(.+?)"' ) . findall ( Iii1iiIi1II )
 if len ( OO0O00oOo ) > 0 :
  for iI1I , OooOoOo , i1Iii11I1i , Oo00o0OO0O00o , IIII1i in OO0O00oOo :
   Ii1IIIIi1ii1I ( iI1I , 'rominstall' , iI1I , OooOoOo , icon = i1Iii11I1i , fanart = Oo00o0OO0O00o , description = IIII1i , themeit = i1I1i111Ii )
  else : wiz . log ( "[ROM Menu] ERROR: Invalid Format." )
 else : wiz . log ( "[ROM Menu] ERROR: URL for rom list not working." )
 if 32 - 32: oOo000OOOo % ooOo0o0O00 - o0O0oO0O00O0o * Ii + II1I1Ii
def II1IOoOo000oOo0oo ( ) :
 if iIiIi11 :
  Iii1iiIi1II = wiz . openURL ( iii ) . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
 OO0O00oOo = re . compile ( '.+?ame="(.+?)".+?rl="(.+?)".+?con="(.+?)".+?anart="(.+?)"description="(.+?)"' ) . findall ( Iii1iiIi1II )
 if len ( OO0O00oOo ) > 0 :
  for iI1I , OooOoOo , i1Iii11I1i , Oo00o0OO0O00o , IIII1i in OO0O00oOo :
   Ii1IIIIi1ii1I ( iI1I , 'rominstall' , iI1I , OooOoOo , icon = i1Iii11I1i , fanart = Oo00o0OO0O00o , description = IIII1i , themeit = i1I1i111Ii )
  else : wiz . log ( "[ROM Menu] ERROR: Invalid Format." )
 else : wiz . log ( "[ROM Menu] ERROR: URL for rom list not working." )
 if 65 - 65: iiiiII1I / iI1i11 % IIIi11I11
def iIiIIii ( ) :
 if OOOiiiiI :
  Iii1iiIi1II = wiz . openURL ( oOooOOOoOo ) . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
 OO0O00oOo = re . compile ( '.+?ame="(.+?)".+?rl="(.+?)".+?con="(.+?)".+?anart="(.+?)"description="(.+?)"' ) . findall ( Iii1iiIi1II )
 if len ( OO0O00oOo ) > 0 :
  for iI1I , OooOoOo , i1Iii11I1i , Oo00o0OO0O00o , IIII1i in OO0O00oOo :
   Ii1IIIIi1ii1I ( iI1I , 'rominstall' , iI1I , OooOoOo , icon = i1Iii11I1i , fanart = Oo00o0OO0O00o , description = IIII1i , themeit = i1I1i111Ii )
  else : wiz . log ( "[ROM Menu] ERROR: Invalid Format." )
 else : wiz . log ( "[ROM Menu] ERROR: URL for rom list not working." )
 if 61 - 61: Ii / o0O0oO0O00O0o / iI1i * Ii1I11I
def iIII1i1i ( ) :
 if oooOo0OOOoo0 :
  Iii1iiIi1II = wiz . openURL ( i1Iii1i1I ) . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
 OO0O00oOo = re . compile ( '.+?ame="(.+?)".+?rl="(.+?)".+?con="(.+?)".+?anart="(.+?)"description="(.+?)"' ) . findall ( Iii1iiIi1II )
 if len ( OO0O00oOo ) > 0 :
  for iI1I , OooOoOo , i1Iii11I1i , Oo00o0OO0O00o , IIII1i in OO0O00oOo :
   Ii1IIIIi1ii1I ( iI1I , 'rominstall' , iI1I , OooOoOo , icon = i1Iii11I1i , fanart = Oo00o0OO0O00o , description = IIII1i , themeit = i1I1i111Ii )
  else : wiz . log ( "[ROM Menu] ERROR: Invalid Format." )
 else : wiz . log ( "[ROM Menu] ERROR: URL for rom list not working." )
 if 35 - 35: I11I1i1iIII1I * II1I1Ii - iI1II . II1I1Ii . II1I1Ii
def I1II ( ) :
 if OOoO :
  Iii1iiIi1II = wiz . openURL ( OOoO00 ) . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
 OO0O00oOo = re . compile ( '.+?ame="(.+?)".+?rl="(.+?)".+?con="(.+?)".+?anart="(.+?)"description="(.+?)"' ) . findall ( Iii1iiIi1II )
 if len ( OO0O00oOo ) > 0 :
  for iI1I , OooOoOo , i1Iii11I1i , Oo00o0OO0O00o , IIII1i in OO0O00oOo :
   Ii1IIIIi1ii1I ( iI1I , 'rominstall' , iI1I , OooOoOo , icon = i1Iii11I1i , fanart = Oo00o0OO0O00o , description = IIII1i , themeit = i1I1i111Ii )
  else : wiz . log ( "[ROM Menu] ERROR: Invalid Format." )
 else : wiz . log ( "[ROM Menu] ERROR: URL for rom list not working." )
 if 79 - 79: iI1i11 . O0i11I1I1I * oOo000OOOo - o0O0oO0O00O0o + ooI1i
def ii11II1i ( ) :
 if OO0O000 :
  Iii1iiIi1II = wiz . openURL ( IiI111111IIII ) . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
 OO0O00oOo = re . compile ( '.+?ame="(.+?)".+?rl="(.+?)".+?con="(.+?)".+?anart="(.+?)"description="(.+?)"' ) . findall ( Iii1iiIi1II )
 if len ( OO0O00oOo ) > 0 :
  for iI1I , OooOoOo , i1Iii11I1i , Oo00o0OO0O00o , IIII1i in OO0O00oOo :
   Ii1IIIIi1ii1I ( iI1I , 'rominstall' , iI1I , OooOoOo , icon = i1Iii11I1i , fanart = Oo00o0OO0O00o , description = IIII1i , themeit = i1I1i111Ii )
  else : wiz . log ( "[ROM Menu] ERROR: Invalid Format." )
 else : wiz . log ( "[ROM Menu] ERROR: URL for rom list not working." )
 if 58 - 58: iI1i . IIIi11I11 - iI1i - iIIIII1I * oOo000OOOo
 if 28 - 28: iiiiII1I * iI1i11 . II1I1Ii % II1I1Ii / II1I1Ii * iIIIII1I
 if 64 - 64: I11I1i1iIII1I - oo0o0000
 if 68 - 68: ooI1i - o0O0oO0O00O0o - oo0 / iiiiII1I + o0O0oO0O00O0o - iI1i11
def O00Oo ( ) :
 if i11I1IiII1i1i :
  Iii1iiIi1II = wiz . openURL ( ooOooo000oOO ) . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
 OO0O00oOo = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?con="(.+?)".+?anart="(.+?)"' ) . findall ( Iii1iiIi1II )
 if len ( OO0O00oOo ) > 0 :
  for iI1I , OooOoOo , i1Iii11I1i , Oo00o0OO0O00o in OO0O00oOo :
   I1ii1ii11i1I ( iI1I , 'apkinstall' , iI1I , OooOoOo , icon = i1Iii11I1i , fanart = Oo00o0OO0O00o , themeit = i1I1i111Ii )
  else : wiz . log ( "[APK Menu] ERROR: Invalid Format." )
 else : wiz . log ( "[APK Menu] ERROR: URL for apk list not working." )
 if 15 - 15: oOo000OOOo / I11I1i1iIII1I . O0i11I1I1I / I11I1i1iIII1I % oOo000OOOo
def I11Oo00oO0O ( ) :
 if oo :
  Iii1iiIi1II = wiz . openURL ( Oo0oOOo ) . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
 OO0O00oOo = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?con="(.+?)".+?anart="(.+?)"' ) . findall ( Iii1iiIi1II )
 if len ( OO0O00oOo ) > 0 :
  for iI1I , OooOoOo , i1Iii11I1i , Oo00o0OO0O00o in OO0O00oOo :
   I1ii1ii11i1I ( iI1I , 'apkinstall' , iI1I , OooOoOo , icon = i1Iii11I1i , fanart = Oo00o0OO0O00o , themeit = i1I1i111Ii )
  else : wiz . log ( "[APK Menu] ERROR: Invalid Format." )
 else : wiz . log ( "[APK Menu] ERROR: URL for apk list not working." )
 if 96 - 96: ooOo0o0O00 / I11I1i1iIII1I . oOo000OOOo - O0i11I1I1I * II1I1Ii * i1I1
def O00oo0ooO ( ) :
 if IiIi11iI :
  Iii1iiIi1II = wiz . openURL ( oO0 ) . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
 OO0O00oOo = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?con="(.+?)".+?anart="(.+?)"' ) . findall ( Iii1iiIi1II )
 if len ( OO0O00oOo ) > 0 :
  for iI1I , OooOoOo , i1Iii11I1i , Oo00o0OO0O00o in OO0O00oOo :
   I1ii1ii11i1I ( iI1I , 'apkinstall' , iI1I , OooOoOo , icon = i1Iii11I1i , fanart = Oo00o0OO0O00o , themeit = i1I1i111Ii )
  else : wiz . log ( "[APK Menu] ERROR: Invalid Format." )
 else : wiz . log ( "[APK Menu] ERROR: URL for apk list not working." )
 if 38 - 38: oo0 - I11I1i1iIII1I - oo0o0000
 if 71 - 71: iI1II
 if 33 - 33: iIIIII1I
 if 62 - 62: ooOo0o0O00 + oOo000OOOo + o0OOo0o0O0O / iI1II
 if 7 - 7: Ii + o0OOo0o0O0O . oo0o0000 / iI1i
def I111i1I1 ( ) :
 O0o00OOo00O0O = '[COLOR green]ON[/COLOR]' ; II1i = '[COLOR red]OFF[/COLOR]'
 OoOOoO000O00oO = 'true' if I11 == 'true' else 'false'
 i1OoOO = 'true' if Oo0o0000o0o0 == 'true' else 'false'
 iIII1I1i1i = 'true' if oOo0oooo00o == 'true' else 'false'
 if 79 - 79: oOo000OOOo . iI1i11
 I1ii1ii11i1I ( 'Fresh Start' , 'freshstart' , icon = iiIiIIIiiI , themeit = i1I1i111Ii )
 I1ii1ii11i1I ( 'Clear Cache' , 'clearcache' , icon = iiIiIIIiiI , themeit = i1I1i111Ii )
 I1ii1ii11i1I ( 'Clear Packages' , 'clearpackages' , icon = iiIiIIIiiI , themeit = i1I1i111Ii )
 I1ii1ii11i1I ( 'Clear Thumbnails' , 'clearthumb' , icon = iiIiIIIiiI , themeit = i1I1i111Ii )
 I1ii1ii11i1I ( 'Purge Databases' , 'purgedb' , icon = iiIiIIIiiI , themeit = i1I1i111Ii )
 OOoOooOoOOOoo ( 'Remove Addons' , 'removeaddons' , icon = iiIiIIIiiI , themeit = i1I1i111Ii )
 OOoOooOoOOOoo ( 'Remove Addon Data' , 'removeaddondata' , icon = iiIiIIIiiI , themeit = i1I1i111Ii )
 I1ii1ii11i1I ( 'Force Update Addons' , 'forceupdate' , icon = iiIiIIIiiI , themeit = i1I1i111Ii )
 I1ii1ii11i1I ( 'Force Close Kodi' , 'forceclose' , icon = iiIiIIIiiI , themeit = i1I1i111Ii )
 I1ii1ii11i1I ( 'Upload Kodi log' , 'uploadlog' , icon = iiIiIIIiiI , themeit = i1I1i111Ii )
 I1ii1ii11i1I ( 'View Kodi Log File' , 'viewlog' , icon = iiIiIIIiiI , themeit = i1I1i111Ii )
 I1ii1ii11i1I ( 'View Wizard Log File' , 'viewwizlog' , icon = iiIiIIIiiI , themeit = i1I1i111Ii )
 I1ii1ii11i1I ( 'Clear Wizard Log File' , 'clearwizlog' , icon = iiIiIIIiiI , themeit = i1I1i111Ii )
 I1ii1ii11i1I ( '==============[ Auto Clean ]==============' , '' , fanart = I1i1iiI1 , icon = iiIiIIIiiI , themeit = i1i1iI1iiiI )
 I1ii1ii11i1I ( 'Auto Clean Up On Startup: %s' % OoOOoO000O00oO . replace ( 'true' , O0o00OOo00O0O ) . replace ( 'false' , II1i ) , 'togglesetting' , 'autoclean' , icon = iiIiIIIiiI , themeit = i1I1i111Ii )
 if OoOOoO000O00oO == 'true' :
  I1ii1ii11i1I ( '--- Clear Cache on Startup: %s' % i1OoOO . replace ( 'true' , O0o00OOo00O0O ) . replace ( 'false' , II1i ) , 'togglesetting' , 'clearcache' , icon = iiIiIIIiiI , themeit = i1I1i111Ii )
  I1ii1ii11i1I ( '--- Clear Packages on Startup: %s' % iIII1I1i1i . replace ( 'true' , O0o00OOo00O0O ) . replace ( 'false' , II1i ) , 'togglesetting' , 'clearpackages' , icon = iiIiIIIiiI , themeit = i1I1i111Ii )
 o0OoOO ( 'movies' , 'MAIN' )
 if 40 - 40: Ii + iI1i . Ii % ooI1i
 if 15 - 15: oOo000OOOo * iI1i % ooOo0o0O00 * oo0 - i11iIiiIii
 if 60 - 60: oo0o0000 * iIIIII1I % iI1i11 + i1I1
 if 52 - 52: o0OOo0o0O0O
def o000 ( ) :
 if I1111i :
  Iii1iiIi1II = wiz . openURL ( Oo0OoO00oOO0o ) . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
 OO0O00oOo = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?con="(.+?)".+?anart="(.+?)"' ) . findall ( Iii1iiIi1II )
 if len ( OO0O00oOo ) > 0 :
  for iI1I , OooOoOo , i1Iii11I1i , Oo00o0OO0O00o in OO0O00oOo :
   I1ii1ii11i1I ( iI1I , 'speedtest' , iI1I , OooOoOo , icon = i1Iii11I1i , fanart = Oo00o0OO0O00o , themeit = i1I1i111Ii )
  else : wiz . log ( "[APK Menu] ERROR: Invalid Format." )
 else : wiz . log ( "[APK Menu] ERROR: URL for apk list not working." )
 if 94 - 94: Ii + Ii1I11I / II1I1Ii . oo0o0000 + o0O0oO0O00O0o . oo0
 if 62 - 62: iiiiII1I / oo0o0000 - ooOo0o0O00 - oo0o0000 + i11iIiiIii + o0OOo0o0O0O
 if 23 - 23: O0i11I1I1I + II1I1Ii . iiiiII1I * oo0o0000 + ooOo0o0O00
 if 18 - 18: IIIi11I11 * Ii . IIIi11I11 / Ii1I11I
def iiIII1II ( ) :
 O0o00OOo00O0O = '[COLOR green]ON[/COLOR]' ; II1i = '[COLOR red]OFF[/COLOR]'
 oOo00oOOOOO = 'true' if oOOoO0 == 'true' else 'false'
 OoOOo0O00 = 'true' if O0OoO000O0OO == 'true' else 'false'
 iIiI = 'true' if iI111I11I1I1 == 'true' else 'false'
 iIIIi1i1I11i = 'true' if iIii1 == 'true' else 'false'
 oOO0OO0OO = 'true' if OOooO0OOoo == 'true' else 'false'
 oOOoooO = 'true' if i1iIIi1 == 'true' else 'false'
 iIi1i1iIi1iI = 'true' if ii11iIi1I == 'true' else 'false'
 if 22 - 22: II1I1Ii + oo0
 OOoOooOoOOOoo ( 'Keep Trakt Data' , 'trakt' , icon = OOo0 , themeit = i1I1i111Ii )
 OOoOooOoOOOoo ( 'Keep Real Debrid' , 'realdebrid' , icon = OOo0 , themeit = i1I1i111Ii )
 I1ii1ii11i1I ( '- Click to toggle settings -' , '' , themeit = i1i1iI1iiiI )
 I1ii1ii11i1I ( 'Save Trakt: %s' % oOo00oOOOOO . replace ( 'true' , O0o00OOo00O0O ) . replace ( 'false' , II1i ) , 'togglesetting' , 'keeptrakt' , icon = OOo0 , themeit = i1I1i111Ii )
 I1ii1ii11i1I ( 'Save Real Debrid: %s' % OoOOo0O00 . replace ( 'true' , O0o00OOo00O0O ) . replace ( 'false' , II1i ) , 'togglesetting' , 'keepdebrid' , icon = OOo0 , themeit = i1I1i111Ii )
 I1ii1ii11i1I ( 'Keep \'Sources.xml\': %s' % iIiI . replace ( 'true' , O0o00OOo00O0O ) . replace ( 'false' , II1i ) , 'togglesetting' , 'keepsources' , icon = OOo0 , themeit = i1I1i111Ii )
 I1ii1ii11i1I ( 'Keep \'Profiles.xml\': %s' % oOO0OO0OO . replace ( 'true' , O0o00OOo00O0O ) . replace ( 'false' , II1i ) , 'togglesetting' , 'keepprofiles' , icon = OOo0 , themeit = i1I1i111Ii )
 I1ii1ii11i1I ( 'Keep \'Advancedsettings.xml\': %s' % iIIIi1i1I11i . replace ( 'true' , O0o00OOo00O0O ) . replace ( 'false' , II1i ) , 'togglesetting' , 'keepadvanced' , icon = OOo0 , themeit = i1I1i111Ii )
 I1ii1ii11i1I ( 'Keep \'Favourites.xml\': %s' % oOOoooO . replace ( 'true' , O0o00OOo00O0O ) . replace ( 'false' , II1i ) , 'togglesetting' , 'keepfavourites' , icon = OOo0 , themeit = i1I1i111Ii )
 I1ii1ii11i1I ( 'Keep \'Guisettings.xml\': %s' % iIi1i1iIi1iI . replace ( 'true' , O0o00OOo00O0O ) . replace ( 'false' , II1i ) , 'togglesetting' , 'keepgui' , icon = OOo0 , themeit = i1I1i111Ii )
 if 24 - 24: iiiiII1I % o0OOo0o0O0O + O0i11I1I1I . i11iIiiIii . ooOo0o0O00
 if 17 - 17: ooOo0o0O00 . I11I1i1iIII1I . ooI1i / ooOo0o0O00
def oOooO00o0O ( ) :
 oOo00oOOOOO = '[COLOR green]ON[/COLOR]' if oOOoO0 == 'true' else '[COLOR red]OFF[/COLOR]'
 OOo0iiIii1IIi = str ( oooOOOOO ) if not oooOOOOO == '' else 'Trakt hasnt been saved yet.'
 I1ii1ii11i1I ( '[I]Register FREE Account at http://trakt.tv[/I]' , '' , icon = oo0o , themeit = i1i1iI1iiiI )
 I1ii1ii11i1I ( 'Save Trakt Data: %s' % oOo00oOOOOO , 'togglesetting' , 'keeptrakt' , icon = oo0o , themeit = i1i1iI1iiiI )
 if oOOoO0 == 'true' : I1ii1ii11i1I ( 'Last Save: %s' % str ( OOo0iiIii1IIi ) , '' , icon = oo0o , themeit = i1i1iI1iiiI )
 if IiII111i1i11 == 'No' : I1ii1ii11i1I ( '============================================' , '' , icon = oo0o , themeit = i1i1iI1iiiI )
 ii1IiIiI1 = os . path . join ( OOOo0 , IIiiiiiiIi1I1 , 'icon.png' ) if os . path . exists ( IIIii1II1II ) else oo0o
 OOOoOo00O = os . path . join ( OOOo0 , IIiiiiiiIi1I1 , 'fanart.jpg' ) if os . path . exists ( IIIii1II1II ) else I1i1iiI1
 I1ii1ii11i1I ( '[+]-- Exodus' , '' , icon = ii1IiIiI1 , fanart = OOOoOo00O , themeit = i1i1iI1iiiI )
 O0Oooo = iiIi1i ( 'traktaddon' , 'Exodus' ) ; O0ooOo0o0Oo = iiIi1i ( 'trakt' , 'Exodus' )
 if not os . path . exists ( IIIii1II1II ) : I1ii1ii11i1I ( '[COLOR red]Addon Data: Not Installed[/COLOR]' , '' , icon = ii1IiIiI1 , fanart = OOOoOo00O , menu = O0Oooo )
 elif not traktit . traktUser ( 'exodus' ) : I1ii1ii11i1I ( '[COLOR red]Addon Data: Not Registered[/COLOR]' , 'authtrakt' , 'exodus' , icon = ii1IiIiI1 , fanart = OOOoOo00O , menu = O0Oooo )
 else : I1ii1ii11i1I ( '[COLOR green]Addon Data: %s[/COLOR]' % traktit . traktUser ( 'exodus' ) , 'authtrakt' , 'exodus' , icon = ii1IiIiI1 , fanart = OOOoOo00O , menu = O0Oooo )
 if iiI1IiI == "" : I1ii1ii11i1I ( '[COLOR red]Saved Data: Not Saved[/COLOR]' , 'savetrakt' , 'exodus' , icon = ii1IiIiI1 , fanart = OOOoOo00O , menu = O0ooOo0o0Oo )
 else : I1ii1ii11i1I ( '[COLOR green]Saved Data: %s[/COLOR]' % iiI1IiI , '' , icon = ii1IiIiI1 , fanart = OOOoOo00O , menu = O0ooOo0o0Oo )
 OooO0oOo = os . path . join ( OOOo0 , OOOO , 'icon.png' ) if os . path . exists ( O000oo0O ) else oo0o
 oOOo00O0OOOo = os . path . join ( OOOo0 , OOOO , 'fanart.jpg' ) if os . path . exists ( O000oo0O ) else I1i1iiI1
 I1ii1ii11i1I ( '[+]-- Salts' , '' , icon = OooO0oOo , fanart = oOOo00O0OOOo , themeit = i1i1iI1iiiI )
 O0Oooo = iiIi1i ( 'traktaddon' , 'Salts' ) ; O0ooOo0o0Oo = iiIi1i ( 'trakt' , 'Salts' )
 if not os . path . exists ( O000oo0O ) : I1ii1ii11i1I ( '[COLOR red]Addon Data: Not Installed[/COLOR]' , '' , icon = OooO0oOo , fanart = oOOo00O0OOOo , menu = O0Oooo )
 elif not traktit . traktUser ( 'salts' ) : I1ii1ii11i1I ( '[COLOR red]Addon Data: Not Registered[/COLOR]' , 'authtrakt' , 'salts' , icon = OooO0oOo , fanart = oOOo00O0OOOo , menu = O0Oooo )
 else : I1ii1ii11i1I ( '[COLOR green]Addon Data: %s[/COLOR]' % traktit . traktUser ( 'salts' ) , 'authtrakt' , 'salts' , icon = OooO0oOo , fanart = oOOo00O0OOOo , menu = O0Oooo )
 if II == "" : I1ii1ii11i1I ( '[COLOR red]Saved Data: Not Saved[/COLOR]' , 'savetrakt' , 'salts' , icon = OooO0oOo , fanart = oOOo00O0OOOo , menu = O0ooOo0o0Oo )
 else : I1ii1ii11i1I ( '[COLOR green]Saved Data: %s[/COLOR]' % II , '' , icon = OooO0oOo , fanart = oOOo00O0OOOo , menu = O0ooOo0o0Oo )
 i11I1I1iiI = os . path . join ( OOOo0 , OOO00 , 'icon.png' ) if os . path . exists ( OOOOi11i1 ) else oo0o
 I1i1iii1Ii = os . path . join ( OOOo0 , OOO00 , 'fanart.jpg' ) if os . path . exists ( OOOOi11i1 ) else I1i1iiI1
 I1ii1ii11i1I ( '[+]-- Salts HD' , '' , icon = i11I1I1iiI , fanart = I1i1iii1Ii , themeit = i1i1iI1iiiI )
 O0Oooo = iiIi1i ( 'traktaddon' , 'Salts HD' ) ; O0ooOo0o0Oo = iiIi1i ( 'trakt' , 'Salts HD' )
 if not os . path . exists ( OOOOi11i1 ) : I1ii1ii11i1I ( '[COLOR red]Addon Data: Not Installed[/COLOR]' , '' , icon = i11I1I1iiI , fanart = I1i1iii1Ii , menu = O0Oooo )
 elif not traktit . traktUser ( 'saltshd' ) : I1ii1ii11i1I ( '[COLOR red]Addon Data: Not Registered[/COLOR]' , 'authtrakt' , 'saltshd' , icon = i11I1I1iiI , fanart = I1i1iii1Ii , menu = O0Oooo )
 else : I1ii1ii11i1I ( '[COLOR green]Addon Data: %s[/COLOR]' % traktit . traktUser ( 'saltshd' ) , 'authtrakt' , 'saltshd' , icon = i11I1I1iiI , fanart = I1i1iii1Ii , menu = O0Oooo )
 if ooOoOoo0O == "" : I1ii1ii11i1I ( '[COLOR red]Saved Data: Not Saved[/COLOR]' , 'savetrakt' , 'saltshd' , icon = i11I1I1iiI , fanart = I1i1iii1Ii , menu = O0ooOo0o0Oo )
 else : I1ii1ii11i1I ( '[COLOR green]Saved Data: %s[/COLOR]' % ooOoOoo0O , '' , icon = i11I1I1iiI , fanart = I1i1iii1Ii , menu = O0ooOo0o0Oo )
 iI = os . path . join ( OOOo0 , iiiiiIIii , 'icon.png' ) if os . path . exists ( o0OO00oO ) else oo0o
 O0O00OOo = os . path . join ( OOOo0 , iiiiiIIii , 'fanart.jpg' ) if os . path . exists ( o0OO00oO ) else I1i1iiI1
 I1ii1ii11i1I ( '[+]-- Royal We' , '' , icon = iI , fanart = O0O00OOo , themeit = i1i1iI1iiiI )
 O0Oooo = iiIi1i ( 'traktaddon' , 'Royal We' ) ; O0ooOo0o0Oo = iiIi1i ( 'trakt' , 'Royal We' )
 if not os . path . exists ( o0OO00oO ) : I1ii1ii11i1I ( '[COLOR red]Addon Data: Not Installed[/COLOR]' , '' , icon = iI , fanart = O0O00OOo , menu = O0Oooo )
 elif not traktit . traktUser ( 'royalwe' ) : I1ii1ii11i1I ( '[COLOR red]Addon Data: Not Registered[/COLOR]' , 'authtrakt' , 'royalwe' , icon = iI , fanart = O0O00OOo , menu = O0Oooo )
 else : I1ii1ii11i1I ( '[COLOR green]Addon Data: %s[/COLOR]' % traktit . traktUser ( 'royalwe' ) , 'authtrakt' , 'royalwe' , icon = iI , fanart = O0O00OOo , menu = O0Oooo )
 if OooO0 == "" : I1ii1ii11i1I ( '[COLOR red]Saved Data: Not Saved[/COLOR]' , 'savetrakt' , 'royalwe' , icon = iI , fanart = O0O00OOo , menu = O0ooOo0o0Oo )
 else : I1ii1ii11i1I ( '[COLOR green]Saved Data: %s[/COLOR]' % OooO0 , '' , icon = iI , fanart = O0O00OOo , menu = O0ooOo0o0Oo )
 OoOOo = os . path . join ( OOOo0 , I1IIIii , 'icon.png' ) if os . path . exists ( i1I1iI ) else oo0o
 iii1oOO0oo = os . path . join ( OOOo0 , I1IIIii , 'fanart.jpg' ) if os . path . exists ( i1I1iI ) else I1i1iiI1
 I1ii1ii11i1I ( '[+]-- Velocity' , '' , icon = OoOOo , fanart = iii1oOO0oo , themeit = i1i1iI1iiiI )
 O0Oooo = iiIi1i ( 'traktaddon' , 'Velocity' ) ; O0ooOo0o0Oo = iiIi1i ( 'trakt' , 'Velocity' )
 if not os . path . exists ( i1I1iI ) : I1ii1ii11i1I ( '[COLOR red]Addon Data: Not Installed[/COLOR]' , '' , icon = OoOOo , fanart = iii1oOO0oo , menu = O0Oooo )
 elif not traktit . traktUser ( 'velocity' ) : I1ii1ii11i1I ( '[COLOR red]Addon Data: Not Registered[/COLOR]' , 'authtrakt' , 'velocity' , icon = OoOOo , fanart = iii1oOO0oo , menu = O0Oooo )
 else : I1ii1ii11i1I ( '[COLOR green]Addon Data: %s[/COLOR]' % traktit . traktUser ( 'velocity' ) , 'authtrakt' , 'velocity' , icon = OoOOo , fanart = iii1oOO0oo , menu = O0Oooo )
 if II11iiii1Ii == "" : I1ii1ii11i1I ( '[COLOR red]Saved Data: Not Saved[/COLOR]' , 'savetrakt' , 'velocity' , icon = OoOOo , fanart = iii1oOO0oo , menu = O0ooOo0o0Oo )
 else : I1ii1ii11i1I ( '[COLOR green]Saved Data: %s[/COLOR]' % II11iiii1Ii , '' , icon = OoOOo , fanart = iii1oOO0oo , menu = O0ooOo0o0Oo )
 II1iIi1IiIii = os . path . join ( OOOo0 , oOoOooOo0o0 , 'icon.png' ) if os . path . exists ( oo0OooOOo0 ) else oo0o
 I111I11I111 = os . path . join ( OOOo0 , oOoOooOo0o0 , 'fanart.jpg' ) if os . path . exists ( oo0OooOOo0 ) else I1i1iiI1
 I1ii1ii11i1I ( '[+]-- Velocity Kids' , '' , icon = II1iIi1IiIii , fanart = I111I11I111 , themeit = i1i1iI1iiiI )
 O0Oooo = iiIi1i ( 'traktaddon' , 'Velocity Kids' ) ; O0ooOo0o0Oo = iiIi1i ( 'trakt' , 'Velocity Kids' )
 if not os . path . exists ( oo0OooOOo0 ) : I1ii1ii11i1I ( '[COLOR red]Addon Data: Not Installed[/COLOR]' , '' , icon = II1iIi1IiIii , fanart = I111I11I111 , menu = O0Oooo )
 elif not traktit . traktUser ( 'velocitykids' ) : I1ii1ii11i1I ( '[COLOR red]Addon Data: Not Registered[/COLOR]' , 'authtrakt' , 'velocitykids' , icon = II1iIi1IiIii , fanart = I111I11I111 , menu = O0Oooo )
 else : I1ii1ii11i1I ( '[COLOR green]Addon Data: %s[/COLOR]' % traktit . traktUser ( 'velocitykids' ) , 'authtrakt' , 'velocitykids' , icon = II1iIi1IiIii , fanart = I111I11I111 , menu = O0Oooo )
 if OO0oOoo == "" : I1ii1ii11i1I ( '[COLOR red]Saved Data: Not Saved[/COLOR]' , 'savetrakt' , 'velocitykids' , icon = II1iIi1IiIii , fanart = I111I11I111 , menu = O0ooOo0o0Oo )
 else : I1ii1ii11i1I ( '[COLOR green]Saved Data: %s[/COLOR]' % OO0oOoo , '' , icon = II1iIi1IiIii , fanart = I111I11I111 , menu = O0ooOo0o0Oo )
 iiiiI11ii = os . path . join ( OOOo0 , O000OO0 , 'icon.png' ) if os . path . exists ( I11i1I1I ) else oo0o
 O0i1i1II1i11 = os . path . join ( OOOo0 , O000OO0 , 'fanart.jpg' ) if os . path . exists ( I11i1I1I ) else I1i1iiI1
 I1ii1ii11i1I ( '[+]-- Specto' , '' , icon = iiiiI11ii , fanart = O0i1i1II1i11 , themeit = i1i1iI1iiiI )
 O0Oooo = iiIi1i ( 'traktaddon' , 'Specto' ) ; O0ooOo0o0Oo = iiIi1i ( 'trakt' , 'Specto' )
 if not os . path . exists ( I11i1I1I ) : I1ii1ii11i1I ( '[COLOR red]Addon Data: Not Installed[/COLOR]' , '' , icon = iiiiI11ii , fanart = O0i1i1II1i11 , menu = O0Oooo )
 elif not traktit . traktUser ( 'specto' ) : I1ii1ii11i1I ( '[COLOR red]Addon Data: Not Registered[/COLOR]' , 'authtrakt' , 'specto' , icon = iiiiI11ii , fanart = O0i1i1II1i11 , menu = O0Oooo )
 else : I1ii1ii11i1I ( '[COLOR green]Addon Data: %s[/COLOR]' % traktit . traktUser ( 'specto' ) , 'authtrakt' , 'specto' , icon = iiiiI11ii , fanart = O0i1i1II1i11 , menu = O0Oooo )
 if O0o0Oo == "" : I1ii1ii11i1I ( '[COLOR red]Saved Data: Not Saved[/COLOR]' , 'savetrakt' , 'specto' , icon = iiiiI11ii , fanart = O0i1i1II1i11 , menu = O0ooOo0o0Oo )
 else : I1ii1ii11i1I ( '[COLOR green]Saved Data: %s[/COLOR]' % O0o0Oo , '' , icon = iiiiI11ii , fanart = O0i1i1II1i11 , menu = O0ooOo0o0Oo )
 o00o = os . path . join ( OOOo0 , I11iii1Ii , 'icon.png' ) if os . path . exists ( oO0Oo ) else oo0o
 iii11II1I = os . path . join ( OOOo0 , I11iii1Ii , 'fanart.jpg' ) if os . path . exists ( oO0Oo ) else I1i1iiI1
 I1ii1ii11i1I ( '[+]-- Trakt' , '' , icon = II1iIi1IiIii , fanart = iii11II1I , themeit = i1i1iI1iiiI )
 O0Oooo = iiIi1i ( 'traktaddon' , 'Trakt' ) ; O0ooOo0o0Oo = iiIi1i ( 'trakt' , 'Trakt' )
 if not os . path . exists ( oO0Oo ) : I1ii1ii11i1I ( '[COLOR red]Addon Data: Not Installed[/COLOR]' , '' , icon = o00o , fanart = iii11II1I , menu = O0Oooo )
 elif not traktit . traktUser ( 'trakt' ) : I1ii1ii11i1I ( '[COLOR red]Addon Data: Not Registered[/COLOR]' , 'authtrakt' , 'trakt' , icon = o00o , fanart = iii11II1I , menu = O0Oooo )
 else : I1ii1ii11i1I ( '[COLOR green]Addon Data: %s[/COLOR]' % traktit . traktUser ( 'trakt' ) , 'authtrakt' , 'trakt' , icon = o00o , fanart = iii11II1I , menu = O0Oooo )
 if Oo00OOOOO == "" : I1ii1ii11i1I ( '[COLOR red]Saved Data: Not Saved[/COLOR]' , 'savetrakt' , 'trakt' , icon = o00o , fanart = iii11II1I , menu = O0ooOo0o0Oo )
 else : I1ii1ii11i1I ( '[COLOR green]Saved Data: %s[/COLOR]' % Oo00OOOOO , '' , icon = o00o , fanart = iii11II1I , menu = O0ooOo0o0Oo )
 if IiII111i1i11 == 'No' : I1ii1ii11i1I ( '============================================' , '' , themeit = i1i1iI1iiiI )
 I1ii1ii11i1I ( 'Save All Trakt Data' , 'savetrakt' , 'all' , icon = oo0o , themeit = i1i1iI1iiiI )
 I1ii1ii11i1I ( 'Recover All Saved Trakt Data' , 'restoretrakt' , 'all' , icon = oo0o , themeit = i1i1iI1iiiI )
 I1ii1ii11i1I ( 'Clear All Saved Trakt Data' , 'cleartrakt' , 'all' , icon = oo0o , themeit = i1i1iI1iiiI )
 I1ii1ii11i1I ( 'Clear All Addon Data' , 'addontrakt' , 'all' , icon = oo0o , themeit = i1i1iI1iiiI )
 o0OoOO ( 'movies' , 'MAIN' )
 if 5 - 5: iiiiII1I - IIIi11I11 * IIIi11I11
def IiiIi1IIII1i ( ) :
 OoOOo0O00 = '[COLOR green]ON[/COLOR]' if O0OoO000O0OO == 'true' else '[COLOR red]OFF[/COLOR]'
 OOo0iiIii1IIi = str ( i1iiIII111ii ) if not i1iiIII111ii == '' else 'Real Debrid hasnt been saved yet.'
 I1ii1ii11i1I ( '[I]http://real-debrid.com is a PAID service.[/I]' , '' , icon = oo0o , themeit = i1i1iI1iiiI )
 I1ii1ii11i1I ( 'Save Real Debrid Data: %s' % OoOOo0O00 , 'togglesetting' , 'KEEPREAL' , icon = oO00ooooO0o , themeit = i1i1iI1iiiI )
 if O0OoO000O0OO == 'true' : I1ii1ii11i1I ( 'Last Save: %s' % str ( OOo0iiIii1IIi ) , '' , icon = oO00ooooO0o , themeit = i1i1iI1iiiI )
 if IiII111i1i11 == 'No' : I1ii1ii11i1I ( '============================================' , '' , icon = oO00ooooO0o , themeit = i1i1iI1iiiI )
 ii1IiIiI1 = os . path . join ( OOOo0 , IIiiiiiiIi1I1 , 'icon.png' ) if os . path . exists ( IIIii1II1II ) else oO00ooooO0o
 OOOoOo00O = os . path . join ( OOOo0 , IIiiiiiiIi1I1 , 'fanart.jpg' ) if os . path . exists ( IIIii1II1II ) else I1i1iiI1
 O0ooOoO = debridit . debridUser ( 'exodus' )
 I1ii1ii11i1I ( '[+]-- Exodus' , '' , icon = ii1IiIiI1 , fanart = OOOoOo00O , themeit = i1i1iI1iiiI )
 O0Oooo = iiIi1i ( 'debridaddon' , 'Exodus' ) ; O0ooOo0o0Oo = iiIi1i ( 'debrid' , 'Exodus' )
 if not os . path . exists ( IIIii1II1II ) : I1ii1ii11i1I ( '[COLOR red]Addon Data: Not Installed[/COLOR]' , '' , icon = ii1IiIiI1 , fanart = OOOoOo00O , menu = O0Oooo )
 elif not O0ooOoO : I1ii1ii11i1I ( '[COLOR red]Addon Data: Not Registered[/COLOR]' , 'authdebrid' , 'exodus' , icon = ii1IiIiI1 , fanart = OOOoOo00O , menu = O0Oooo )
 else : I1ii1ii11i1I ( '[COLOR green]Addon Data: %s[/COLOR]' % O0ooOoO , 'authdebrid' , 'exodus' , icon = ii1IiIiI1 , fanart = OOOoOo00O , menu = O0Oooo )
 if O0O == "" : I1ii1ii11i1I ( '[COLOR red]Saved Data: Not Saved[/COLOR]' , 'savedebrid' , 'exodus' , icon = ii1IiIiI1 , fanart = OOOoOo00O , menu = O0ooOo0o0Oo )
 else : I1ii1ii11i1I ( '[COLOR green]Saved Data: %s[/COLOR]' % O0O , '' , icon = ii1IiIiI1 , fanart = OOOoOo00O , menu = O0ooOo0o0Oo )
 iiiiI11ii = os . path . join ( OOOo0 , O000OO0 , 'icon.png' ) if os . path . exists ( I11i1I1I ) else oO00ooooO0o
 O0i1i1II1i11 = os . path . join ( OOOo0 , O000OO0 , 'fanart.jpg' ) if os . path . exists ( I11i1I1I ) else I1i1iiI1
 IIIIiI1iiiIiii = debridit . debridUser ( 'specto' )
 I1ii1ii11i1I ( '[+]-- Specto' , '' , icon = iiiiI11ii , fanart = O0i1i1II1i11 , themeit = i1i1iI1iiiI )
 O0Oooo = iiIi1i ( 'debridaddon' , 'Specto' ) ; O0ooOo0o0Oo = iiIi1i ( 'debrid' , 'Specto' )
 if not os . path . exists ( I11i1I1I ) : I1ii1ii11i1I ( '[COLOR red]Addon Data: Not Installed[/COLOR]' , '' , icon = iiiiI11ii , fanart = O0i1i1II1i11 , menu = O0Oooo )
 elif not IIIIiI1iiiIiii : I1ii1ii11i1I ( '[COLOR red]Addon Data: Not Registered[/COLOR]' , 'authdebrid' , 'specto' , icon = iiiiI11ii , fanart = O0i1i1II1i11 , menu = O0Oooo )
 else : I1ii1ii11i1I ( '[COLOR green]Addon Data: %s[/COLOR]' % IIIIiI1iiiIiii , 'authdebrid' , 'specto' , icon = iiiiI11ii , fanart = O0i1i1II1i11 , menu = O0Oooo )
 if O00o0OO == "" : I1ii1ii11i1I ( '[COLOR red]Saved Data: Not Saved[/COLOR]' , 'savedebrid' , 'specto' , icon = iiiiI11ii , fanart = O0i1i1II1i11 , menu = O0ooOo0o0Oo )
 else : I1ii1ii11i1I ( '[COLOR green]Saved Data: %s[/COLOR]' % O00o0OO , '' , icon = iiiiI11ii , fanart = O0i1i1II1i11 , menu = O0ooOo0o0Oo )
 ii1i1i = os . path . join ( OOOo0 , I1IIiiIiii , 'icon.png' ) if os . path . exists ( oOOoo0Oo ) else oO00ooooO0o
 II11iIII1i1I = os . path . join ( OOOo0 , I1IIiiIiii , 'fanart.jpg' ) if os . path . exists ( oOOoo0Oo ) else I1i1iiI1
 oOO0oo = debridit . debridUser ( 'url' )
 I1ii1ii11i1I ( '[+]-- URL Resolver' , '' , icon = ii1i1i , fanart = II11iIII1i1I , themeit = i1i1iI1iiiI )
 O0Oooo = iiIi1i ( 'debridaddon' , 'url' ) ; O0ooOo0o0Oo = iiIi1i ( 'debrid' , 'url' )
 if not os . path . exists ( oOOoo0Oo ) : I1ii1ii11i1I ( '[COLOR red]Addon Data: Not Installed[/COLOR]' , '' , icon = ii1i1i , fanart = II11iIII1i1I , menu = O0Oooo )
 elif not oOO0oo : I1ii1ii11i1I ( '[COLOR red]Addon Data: Not Registered[/COLOR]' , 'authdebrid' , 'url' , icon = ii1i1i , fanart = II11iIII1i1I , menu = O0Oooo )
 else : I1ii1ii11i1I ( '[COLOR green]Addon Data: %s[/COLOR]' % oOO0oo , 'authdebrid' , 'url' , icon = ii1i1i , fanart = II11iIII1i1I , menu = O0Oooo )
 if I11i1 == "" : I1ii1ii11i1I ( '[COLOR red]Saved Data: Not Saved[/COLOR]' , 'savedebrid' , 'url' , icon = ii1i1i , fanart = II11iIII1i1I , menu = O0ooOo0o0Oo )
 else : I1ii1ii11i1I ( '[COLOR green]Saved Data: %s[/COLOR]' % I11i1 , '' , icon = ii1i1i , fanart = II11iIII1i1I , menu = O0ooOo0o0Oo )
 if IiII111i1i11 == 'No' : I1ii1ii11i1I ( '============================================' , '' , themeit = i1i1iI1iiiI )
 I1ii1ii11i1I ( 'Save All Real Debrid Data' , 'savedebrid' , 'all' , icon = oO00ooooO0o , themeit = i1i1iI1iiiI )
 I1ii1ii11i1I ( 'Recover All Saved Real Debrid Data' , 'restoredebrid' , 'all' , icon = oO00ooooO0o , themeit = i1i1iI1iiiI )
 I1ii1ii11i1I ( 'Clear All Saved Real Debrid Data' , 'cleardebrid' , 'all' , icon = oO00ooooO0o , themeit = i1i1iI1iiiI )
 I1ii1ii11i1I ( 'Clear All Addon Data' , 'addondebrid' , 'all' , icon = oO00ooooO0o , themeit = i1i1iI1iiiI )
 o0OoOO ( 'movies' , 'MAIN' )
 if 13 - 13: iI1II * i1I1 - oOo000OOOo / o0O0oO0O00O0o + II1I1Ii + IIIi11I11
def iii1III1i ( ) :
 for iiiIi in glob . glob ( os . path . join ( OOOo0 , '*/' ) ) :
  II1Iii = iiiIi . replace ( OOOo0 , '' ) . replace ( '\\' , '' ) . replace ( '/' , '' )
  i1Iii11I1i = os . path . join ( iiiIi , 'icon.png' )
  Oo00o0OO0O00o = os . path . join ( iiiIi , 'fanart.png' )
  if II1Iii in o00OO00OoO : pass
  elif II1Iii == 'packages' : pass
  else :
   O0oooo0OoO0oo = II1Iii
   IiiiIi1iI1iI = { 'audio.' : '[COLOR orange][AUDIO] [/COLOR]' , 'metadata.' : '[COLOR cyan][METADATA] [/COLOR]' , 'module.' : '[COLOR orange][MODULE] [/COLOR]' , 'plugin.' : '[COLOR blue][PLUGIN] [/COLOR]' , 'program.' : '[COLOR orange][PROGRAM] [/COLOR]' , 'repository.' : '[COLOR gold][REPO] [/COLOR]' , 'script.' : '[COLOR green][SCRIPT] [/COLOR]' , 'service.' : '[COLOR green][SERVICE] [/COLOR]' , 'skin.' : '[COLOR dodgerblue][SKIN] [/COLOR]' , 'video.' : '[COLOR orange][VIDEO] [/COLOR]' , 'weather.' : '[COLOR yellow][WEATHER] [/COLOR]' }
   for OO00o in IiiiIi1iI1iI :
    O0oooo0OoO0oo = O0oooo0OoO0oo . replace ( OO00o , IiiiIi1iI1iI [ OO00o ] )
   I1ii1ii11i1I ( '[COLOR red][B][REMOVE][/B][/COLOR] %s' % O0oooo0OoO0oo , 'removeaddon' , II1Iii , icon = i1Iii11I1i , fanart = Oo00o0OO0O00o , themeit = ooo )
   if 60 - 60: ooOo0o0O00 - i1I1 - oo0o0000 / Ii
def oooo00 ( ) :
 if os . path . exists ( IiI ) :
  I1ii1ii11i1I ( '[COLOR red][B][REMOVE][/B][/COLOR] All Addon_Data' , 'removedata' , 'all' , themeit = ooo )
  I1ii1ii11i1I ( '[COLOR red][B][REMOVE][/B][/COLOR] All Addon_Data for Uninstalled Addons' , 'removedata' , 'uninstalled' , themeit = ooo )
  I1ii1ii11i1I ( '[COLOR red][B][REMOVE][/B][/COLOR] All Empty Folders in Addon_Data' , 'removedata' , 'empty' , themeit = ooo )
  I1ii1ii11i1I ( '[COLOR red][B][REMOVE][/B][/COLOR] %s Addon_Data' % Oo0Ooo , 'resetaddon' , themeit = ooo )
  if IiII111i1i11 == 'No' : I1ii1ii11i1I ( '============================================' , '' , themeit = i1i1iI1iiiI )
  for iiiIi in glob . glob ( os . path . join ( IiI , '*' ) ) :
   II1Iii = iiiIi . replace ( IiI , '' ) . replace ( '\\' , '' ) . replace ( '/' , '' )
   i1Iii11I1i = os . path . join ( iiiIi . replace ( IiI , OOOo0 ) , 'icon.png' )
   Oo00o0OO0O00o = os . path . join ( iiiIi . replace ( IiI , OOOo0 ) , 'fanart.png' )
   O0oooo0OoO0oo = II1Iii
   IiiiIi1iI1iI = { 'audio.' : '[COLOR orange][AUDIO] [/COLOR]' , 'metadata.' : '[COLOR cyan][METADATA] [/COLOR]' , 'module.' : '[COLOR orange][MODULE] [/COLOR]' , 'plugin.' : '[COLOR blue][PLUGIN] [/COLOR]' , 'program.' : '[COLOR orange][PROGRAM] [/COLOR]' , 'repository.' : '[COLOR gold][REPO] [/COLOR]' , 'script.' : '[COLOR green][SCRIPT] [/COLOR]' , 'service.' : '[COLOR green][SERVICE] [/COLOR]' , 'skin.' : '[COLOR dodgerblue][SKIN] [/COLOR]' , 'video.' : '[COLOR orange][VIDEO] [/COLOR]' , 'weather.' : '[COLOR yellow][WEATHER] [/COLOR]' }
   for OO00o in IiiiIi1iI1iI :
    O0oooo0OoO0oo = O0oooo0OoO0oo . replace ( OO00o , IiiiIi1iI1iI [ OO00o ] )
   if II1Iii in o00OO00OoO : O0oooo0OoO0oo = '[COLOR green][B][PROTECTED][/B][/COLOR] %s' % O0oooo0OoO0oo
   else : O0oooo0OoO0oo = '[COLOR red][B][REMOVE][/B][/COLOR] %s' % O0oooo0OoO0oo
   I1ii1ii11i1I ( ' %s' % O0oooo0OoO0oo , 'removedata' , II1Iii , icon = i1Iii11I1i , fanart = Oo00o0OO0O00o , themeit = ooo )
 else :
  I1ii1ii11i1I ( 'No Addon data folder found.' , '' , themeit = i1i1iI1iiiI )
  if 35 - 35: iIIIII1I . iiiiII1I * i11iIiiIii
  if 44 - 44: i11iIiiIii / iI1i
  if 42 - 42: iI1II + iI1i % I11I1i1iIII1I + iI1i11
def I11i11I1iiII ( ) :
 OOoOooOoOOOoo ( 'Backup Restore' , 'bre' , icon = iiIIIII1i1iI , themeit = i1I1i111Ii )
 I1ii1ii11i1I ( 'Convert Paths to special' , 'convertpath' , icon = iiIIIII1i1iI , themeit = i1I1i111Ii )
 I1ii1ii11i1I ( 'Test Notifications' , 'testnotify' , icon = iiIIIII1i1iI , themeit = i1I1i111Ii )
 if 28 - 28: i11iIiiIii / Ii . oo0 / I11I1i1iIII1I
 if 72 - 72: iI1II / oo0o0000 + oOo000OOOo / iiiiII1I * oOo000OOOo
 if 34 - 34: Ii1I11I * Ii1I11I % iI1II + O0i11I1I1I * oo0 % oOo000OOOo
 if 25 - 25: II1I1Ii + iiiiII1I . Ii % iiiiII1I * o0O0oO0O00O0o
 if 32 - 32: i11iIiiIii - iIIIII1I
def oo00ooOoo ( name , type , theme = None ) :
 if type == 'gui' :
  if name == Oo0oO0ooo :
   iii1IIIiiiI = ooo0OO . yesno ( Oo0Ooo , 'Would you like to apply the guifix for:' , '%s?' % name , nolabel = 'No, Cancel' , yeslabel = 'Yes, Apply Fix' )
  else :
   iii1IIIiiiI = ooo0OO . yesno ( "%s - [COLOR red]WARNING!![/COLOR]" % Oo0Ooo , "%s SpinzTV build is not currently installed." % name , "Would you like to apply the guiFix anyways?." , yeslabel = "Yes, Apply" , nolabel = "No, Cancel" )
  if iii1IIIiiiI :
   OoO00oo00 = wiz . checkBuild ( name , 'gui' )
   Oo0Oo0O = name . replace ( '\\' , '' ) . replace ( '/' , '' ) . replace ( ':' , '' ) . replace ( '*' , '' ) . replace ( '?' , '' ) . replace ( '"' , '' ) . replace ( '<' , '' ) . replace ( '>' , '' ) . replace ( '|' , '' )
   if not wiz . workingURL ( OoO00oo00 ) == True : wiz . LogNotify ( Oo0Ooo , 'guiFix: [COLOR red]Invalid Zip Url![/COLOR]' ) ; return
   if not os . path . exists ( Oo0O ) : os . makedirs ( Oo0O )
   II1 . create ( Oo0Ooo , 'Downloading %s GuiFix' % name , '' , 'Please Wait' )
   iiiI1i11Ii = os . path . join ( Oo0O , '%s_guisettings.zip' % Oo0Oo0O )
   try : os . remove ( iiiI1i11Ii )
   except : pass
   downloader . download ( OoO00oo00 , iiiI1i11Ii , II1 )
   xbmc . sleep ( 500 )
   II1 . update ( 0 , "" , "Installing %s GuiFix" % name )
   extract . all ( iiiI1i11Ii , Oooo000o , II1 )
   II1 . close ( )
   wiz . killxbmc ( )
  else :
   wiz . LogNotify ( Oo0Ooo , 'guiFix: [COLOR red]Cancelled![/COLOR]' )
 elif type == 'fresh' :
  iIiII ( name )
 elif type == 'normal' :
  if OooOoOo == 'normal' :
   if oOOoO0 == 'true' :
    traktit . autoUpdate ( 'all' )
    wiz . setS ( 'traktlastsave' , str ( IIIII ) )
   if O0OoO000O0OO == 'true' :
    debridit . autoUpdate ( 'all' )
    wiz . setS ( 'debridlastsave' , str ( IIIII ) )
  if ooooooO0oo < 17.0 and float ( wiz . checkBuild ( name , 'kodi' ) ) >= 17.0 :
   iii1IIIiiiI = ooo0OO . yesno ( "%s - [COLOR red]WARNING!![/COLOR]" % Oo0Ooo , 'There is a chance that the skin will not appear correctly' , 'When installing a %s build on a Kodi %s install' % ( wiz . checkBuild ( name , 'kodi' ) , ooooooO0oo ) , 'Would you still like to install: %s v%s?' % ( name , wiz . checkBuild ( name , 'version' ) ) , nolabel = 'No, Cancel' , yeslabel = 'Yes, Install' )
  else :
   iii1IIIiiiI = ooo0OO . yesno ( Oo0Ooo , 'By downloading or using you are agreeing that the author takes no resposibility for the content or reliability of any of the addons included.  The author does not host, distribute or have any control over any of the content that may be provided by any addon. It is the users responsibility to ensure the legality of use within their country. By continuing you are agreeing to the terms and conditions herin. Would you still like to install:' , '%s v%s?' % ( name , wiz . checkBuild ( name , 'version' ) ) , nolabel = 'Disagree, Cancel' , yeslabel = 'Agree, Install' )
  if iii1IIIiiiI :
   OoO00oo00 = wiz . checkBuild ( name , 'url' )
   Oo0Oo0O = name . replace ( '\\' , '' ) . replace ( '/' , '' ) . replace ( ':' , '' ) . replace ( '*' , '' ) . replace ( '?' , '' ) . replace ( '"' , '' ) . replace ( '<' , '' ) . replace ( '>' , '' ) . replace ( '|' , '' )
   if not wiz . workingURL ( OoO00oo00 ) == True : wiz . LogNotify ( Oo0Ooo , 'Build Install: [COLOR red]Invalid Zip Url![/COLOR]' ) ; return
   if not os . path . exists ( Oo0O ) : os . makedirs ( Oo0O )
   II1 . create ( Oo0Ooo , 'Downloading %s ' % name , '' , 'Please Wait' )
   iiiI1i11Ii = os . path . join ( Oo0O , '%s.zip' % Oo0Oo0O )
   try : os . remove ( iiiI1i11Ii )
   except : pass
   downloader . download ( OoO00oo00 , iiiI1i11Ii , II1 )
   xbmc . sleep ( 500 )
   II1 . update ( 0 , "" , "Installing %s " % name )
   i1i1IIIIIIIi = extract . all ( iiiI1i11Ii , O00ooooo00 , II1 )
   oo0o0oOo , OO0oOOo0o , I1 = i1i1IIIIIIIi . split ( '/' , 3 )
   wiz . setS ( 'buildname' , name )
   wiz . setS ( 'buildversion' , wiz . checkBuild ( name , 'version' ) )
   wiz . setS ( 'buildtheme' , '' )
   wiz . setS ( 'latestversion' , wiz . checkBuild ( name , 'version' ) )
   wiz . setS ( 'lastbuildcheck' , str ( o00O0O ) )
   wiz . setS ( 'installed' , 'true' )
   wiz . setS ( 'extract' , str ( oo0o0oOo ) )
   wiz . setS ( 'errors' , str ( OO0oOOo0o ) )
   wiz . log ( 'INSTALLED %s: [ERRORS:%s]' % ( oo0o0oOo , OO0oOOo0o ) )
   if int ( OO0oOOo0o ) >= 1 :
    III11iiii11i1 = ooo0OO . yesno ( Oo0Ooo , 'INSTALLED %s: [ERRORS:%s]' % ( oo0o0oOo , OO0oOOo0o ) , 'Would you like to view the errors?' , nolabel = 'No, Cancel' , yeslabel = 'Yes, View' )
    if III11iiii11i1 :
     wiz . TextBoxes ( Oo0Ooo , I1 . replace ( '\t' , '' ) ) ; xbmc . sleep ( 3000 )
   II1 . close ( )
   Iiii1iI1i = wiz . checkBuild ( name , 'theme' )
   if not Iiii1iI1i == 'http://' and wiz . workingURL ( Iiii1iI1i ) == True : oo00ooOoo ( name , 'theme' )
   ooo0OO . ok ( Oo0Ooo , "To save changes you now need to force close Kodi, Press OK to force close Kodi" )
   wiz . killxbmc ( )
  else :
   wiz . LogNotify ( Oo0Ooo , 'Build Install: [COLOR red]Cancelled![/COLOR]' )
 elif type == 'theme' :
  if theme == None :
   Iiii1iI1i = wiz . checkBuild ( name , 'theme' )
   ooOo0OoO = [ ]
   if not Iiii1iI1i == 'http://' and wiz . workingURL ( Iiii1iI1i ) == True :
    Iii1iiIi1II = wiz . openURL ( Iiii1iI1i ) . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
    OO0O00oOo = re . compile ( 'name="(.+?)"' ) . findall ( Iii1iiIi1II )
    if len ( OO0O00oOo ) > 0 :
     if ooo0OO . yesno ( Oo0Ooo , "The Build [%s] comes with %s different themes" % ( name , len ( OO0O00oOo ) ) , "Would you like to install one now?" , yeslabel = "Yes, Install" , nolabel = "No Thanks" ) :
      for iiIi1iI1iIii in OO0O00oOo :
       ooOo0OoO . append ( iiIi1iI1iIii )
      wiz . log ( "Theme List: %s " % str ( ooOo0OoO ) )
      i1iiIIi1I = ooo0OO . select ( Oo0Ooo , ooOo0OoO )
      wiz . log ( "Theme install selected: %s" % i1iiIIi1I )
      if not i1iiIIi1I == - 1 : theme = ooOo0OoO [ i1iiIIi1I ] ; iiI1I1IIi11i1 = True
      else : wiz . LogNotify ( Oo0Ooo , 'Theme Install: [COLOR red]Cancelled![/COLOR]' ) ; return
     else : wiz . LogNotify ( Oo0Ooo , 'Theme Install: [COLOR red]Cancelled![/COLOR]' ) ; return
   else : wiz . LogNotify ( Oo0Ooo , 'Theme Install: [COLOR red]None Found![/COLOR]' )
  else : iiI1I1IIi11i1 = ooo0OO . yesno ( Oo0Ooo , 'Would you like to install the theme:' , theme , 'for %s v%s?' % ( name , wiz . checkBuild ( name , 'version' ) ) , nolabel = 'No, Cancel' , yeslabel = 'Yes, Install' )
  if iiI1I1IIi11i1 :
   i1II1iii1i = wiz . checkTheme ( name , theme , 'url' )
   Oo0Oo0O = name . replace ( '\\' , '' ) . replace ( '/' , '' ) . replace ( ':' , '' ) . replace ( '*' , '' ) . replace ( '?' , '' ) . replace ( '"' , '' ) . replace ( '<' , '' ) . replace ( '>' , '' ) . replace ( '|' , '' )
   if not wiz . workingURL ( i1II1iii1i ) == True : wiz . LogNotify ( Oo0Ooo , 'Theme Install: [COLOR red]Invalid Zip Url![/COLOR]' ) ; return
   if not os . path . exists ( Oo0O ) : os . makedirs ( Oo0O )
   II1 . create ( Oo0Ooo , 'Downloading %s ' % name , '' , 'Please Wait' )
   iiiI1i11Ii = os . path . join ( Oo0O , '%s.zip' % Oo0Oo0O )
   try : os . remove ( iiiI1i11Ii )
   except : pass
   downloader . download ( i1II1iii1i , iiiI1i11Ii , II1 )
   xbmc . sleep ( 500 )
   II1 . update ( 0 , "" , "Installing %s " % name )
   i1i1IIIIIIIi = extract . all ( iiiI1i11Ii , O00ooooo00 , II1 )
   oo0o0oOo , OO0oOOo0o , I1 = i1i1IIIIIIIi . split ( '/' , 3 )
   wiz . setS ( 'buildtheme' , theme )
   wiz . log ( 'INSTALLED %s: [ERRORS:%s]' % ( oo0o0oOo , OO0oOOo0o ) )
   II1 . close ( )
   if OooOoOo not in [ "fresh" , "normal" ] : xbmc . executebuiltin ( "ReloadSkin()" ) ; xbmc . sleep ( 1000 ) ; xbmc . executebuiltin ( "Container.Refresh" )
  else :
   wiz . LogNotify ( Oo0Ooo , 'Theme Install: [COLOR red]Cancelled![/COLOR]' )
   if 83 - 83: ooOo0o0O00 / iIIIII1I - i11iIiiIii . oo0 + iI1i
   if 59 - 59: Ii1I11I % iI1i
   if 92 - 92: oOo000OOOo % O0i11I1I1I / ooOo0o0O00 % ooOo0o0O00 * oo0o0000
   if 74 - 74: Ii1I11I . oo0o0000 % iI1i11 % IIIi11I11
def oOo0OooOo ( apk , url ) :
 if wiz . platform ( ) == 'android' :
  if apk in [ 'kodi' , 'spmc' ] :
   III11iiii11i1 = ooo0OO . yesno ( Oo0Ooo , "Would you like to download and install:" , "%s (v%s)" % ( apk . upper ( ) , wiz . latestApk ( apk , 'version' ) ) )
   if not III11iiii11i1 : wiz . LogNotify ( Oo0Ooo , '[COLOR red]ERROR:[/COLOR] Install Cancelled' ) ; return
   o0iIiiIiiIi = "%s v%s" % ( apk . upper ( ) , wiz . latestApk ( apk , 'version' ) )
  else :
   III11iiii11i1 = ooo0OO . yesno ( Oo0Ooo , "Would you like to download and install:" , "%s" % apk )
   if not III11iiii11i1 : wiz . LogNotify ( Oo0Ooo , '[COLOR red]ERROR:[/COLOR] Install Cancelled' ) ; return
   o0iIiiIiiIi = apk
  if III11iiii11i1 :
   if not os . path . exists ( Oo0O ) : os . makedirs ( Oo0O )
   if not wiz . workingURL ( url ) == True : wiz . LogNotify ( Oo0Ooo , 'APK Installer: [COLOR red]Invalid Apk Url![/COLOR]' ) ; return
   II1 . create ( Oo0Ooo , 'Downloading %s' % o0iIiiIiiIi , '' , 'Please Wait' )
   iiiI1i11Ii = os . path . join ( Oo0O , "%s.apk" % apk )
   try : os . remove ( iiiI1i11Ii )
   except : pass
   downloader . download ( url , iiiI1i11Ii , II1 )
   xbmc . sleep ( 500 )
   II1 . close ( )
   ooo0OO . ok ( Oo0Ooo , "Launching the APK to be installed" , "Follow the install process to complete." )
   xbmc . executebuiltin ( 'StartAndroidActivity("","android.intent.action.VIEW","application/vnd.android.package-archive","file:' + iiiI1i11Ii + '")' )
  else : wiz . LogNotify ( Oo0Ooo , '[COLOR red]ERROR:[/COLOR] Install Cancelled' )
 else : wiz . LogNotify ( Oo0Ooo , '[COLOR red]ERROR:[/COLOR] None Android Device' )
 if 40 - 40: Ii
 if 78 - 78: oo0
 if 56 - 56: iI1II - II1I1Ii - o0OOo0o0O0O
 if 8 - 8: iIIIII1I / o0O0oO0O00O0o . oo0o0000 + ooOo0o0O00 / i11iIiiIii
def I1Iii1iI1 ( name , url , ) :
 if "NULL" in url :
  ooo0OO . ok ( Oo0Ooo , "[COLOR ghostwhite]Not a valid selection, please try again.[/COLOR]" )
  sys . exit ( 1 )
  if 86 - 86: Ii1I11I
 O0o0oOooOoOo = xbmcgui . DialogProgress ( )
 O0o0oOooOoOo . create ( Oo0Ooo , "" , "" , 'ROM: ' + name )
 Oo0Oo0O = name . replace ( '\\' , '' ) . replace ( '/' , '' ) . replace ( ':' , '' ) . replace ( '*' , '' ) . replace ( '?' , '' ) . replace ( '"' , '' ) . replace ( '<' , '' ) . replace ( '>' , '' ) . replace ( '|' , '' )
 iiiI1i11Ii = os . path . join ( Oo0O , '%s.zip' % Oo0Oo0O )
 downloader . download ( url , iiiI1i11Ii , O0o0oOooOoOo )
 i1i1IIIIIIIi = extract . all ( iiiI1i11Ii , I1IiiI , O0o0oOooOoOo )
 ooo0OO . ok ( Oo0Ooo , "[COLOR yellow]Download complete, ROM Location: [/COLOR][COLOR white]" + iiiI1i11Ii + "[/COLOR]" )
 if 49 - 49: o0O0oO0O00O0o . ooOo0o0O00 . i11iIiiIii - I11I1i1iIII1I / oOo000OOOo
 if 62 - 62: o0O0oO0O00O0o
 if 1 - 1: IIIi11I11 / IIIi11I11 - i11iIiiIii
 if 87 - 87: iI1i / Ii1I11I * IIIi11I11 / Ii
 if 19 - 19: iIIIII1I + o0OOo0o0O0O . oo0o0000 - iI1i
def iIi1I1 ( ver ) :
 if ver == '15' : wiz . setS ( 'show15' , 'true' if i1111 == 'false' else 'false' )
 elif ver == '16' : wiz . setS ( 'show16' , 'true' if i11 == 'false' else 'false' )
 xbmc . executebuiltin ( 'Container.Refresh' )
 if 63 - 63: O0i11I1I1I * ooOo0o0O00 . iI1II / o0O0oO0O00O0o * iI1i . ooI1i
def Ooo0 ( part , whole ) :
 return 100 * float ( part ) / float ( whole )
 if 91 - 91: o0OOo0o0O0O - oo0
def iiIi1i ( type , name ) :
 if type == 'trakt' :
  Oo0Oo00o00oO = [ ]
  o0000 = urllib . quote_plus ( name . lower ( ) . replace ( ' ' , '' ) )
  Oo0Oo00o00oO . append ( ( ooo % name , ' ' ) )
  Oo0Oo00o00oO . append ( ( ooo % 'Save Trakt Data' , 'RunPlugin(plugin://%s/?mode=savetrakt&name=%s)' % ( OO0o , o0000 ) ) )
  Oo0Oo00o00oO . append ( ( ooo % 'Restore Trakt Data' , 'RunPlugin(plugin://%s/?mode=restoretrakt&name=%s)' % ( OO0o , o0000 ) ) )
  Oo0Oo00o00oO . append ( ( ooo % 'Clear Trakt Data' , 'RunPlugin(plugin://%s/?mode=cleartrakt&name=%s)' % ( OO0o , o0000 ) ) )
 if type == 'traktaddon' :
  Oo0Oo00o00oO = [ ]
  o0000 = urllib . quote_plus ( name . lower ( ) . replace ( ' ' , '' ) )
  Oo0Oo00o00oO . append ( ( ooo % name , ' ' ) )
  Oo0Oo00o00oO . append ( ( ooo % 'Register Trakt' , 'RunPlugin(plugin://%s/?mode=authtrakt&name=%s)' % ( OO0o , o0000 ) ) )
  Oo0Oo00o00oO . append ( ( ooo % 'Save Trakt Data' , 'RunPlugin(plugin://%s/?mode=savetrakt&name=%s)' % ( OO0o , o0000 ) ) )
  Oo0Oo00o00oO . append ( ( ooo % 'Restore Trakt Data' , 'RunPlugin(plugin://%s/?mode=restoretrakt&name=%s)' % ( OO0o , o0000 ) ) )
  Oo0Oo00o00oO . append ( ( ooo % 'Clear Addon Trakt Data' , 'RunPlugin(plugin://%s/?mode=addontrakt&name=%s)' % ( OO0o , o0000 ) ) )
 if type == 'debrid' :
  Oo0Oo00o00oO = [ ]
  o0000 = urllib . quote_plus ( name . lower ( ) . replace ( ' ' , '' ) )
  Oo0Oo00o00oO . append ( ( ooo % name , ' ' ) )
  Oo0Oo00o00oO . append ( ( ooo % 'Save Real Debrid Data' , 'RunPlugin(plugin://%s/?mode=savedebrid&name=%s)' % ( OO0o , o0000 ) ) )
  Oo0Oo00o00oO . append ( ( ooo % 'Restore Real Debrid Data' , 'RunPlugin(plugin://%s/?mode=restoredebrid&name=%s)' % ( OO0o , o0000 ) ) )
  Oo0Oo00o00oO . append ( ( ooo % 'Clear Real Debrid Data' , 'RunPlugin(plugin://%s/?mode=cleardebrid&name=%s)' % ( OO0o , o0000 ) ) )
 if type == 'debridaddon' :
  Oo0Oo00o00oO = [ ]
  o0000 = urllib . quote_plus ( name . lower ( ) . replace ( ' ' , '' ) )
  Oo0Oo00o00oO . append ( ( ooo % name , ' ' ) )
  Oo0Oo00o00oO . append ( ( ooo % 'Register Real Debrid' , 'RunPlugin(plugin://%s/?mode=authdebrid&name=%s)' % ( OO0o , o0000 ) ) )
  Oo0Oo00o00oO . append ( ( ooo % 'Save Real Debrid Data' , 'RunPlugin(plugin://%s/?mode=savedebrid&name=%s)' % ( OO0o , o0000 ) ) )
  Oo0Oo00o00oO . append ( ( ooo % 'Restore Real Debrid Data' , 'RunPlugin(plugin://%s/?mode=restoredebrid&name=%s)' % ( OO0o , o0000 ) ) )
  Oo0Oo00o00oO . append ( ( ooo % 'Clear Addon Real Debrid Data' , 'RunPlugin(plugin://%s/?mode=addondebrid&name=%s)' % ( OO0o , o0000 ) ) )
 if type == 'install' :
  Oo0Oo00o00oO = [ ]
  o0000 = urllib . quote_plus ( name )
  Oo0Oo00o00oO . append ( ( ooo % name , ' ' ) )
  Oo0Oo00o00oO . append ( ( ooo % 'Fresh Install' , 'RunPlugin(plugin://%s/?mode=install&name=%s&url=fresh)' % ( OO0o , o0000 ) ) )
  Oo0Oo00o00oO . append ( ( ooo % 'Normal Install Use On Updates' , 'RunPlugin(plugin://%s/?mode=install&name=%s&url=normal)' % ( OO0o , o0000 ) ) )
  Oo0Oo00o00oO . append ( ( ooo % 'Apply guiFix' , 'RunPlugin(plugin://%s/?mode=install&name=%s&url=gui)' % ( OO0o , o0000 ) ) )
 Oo0Oo00o00oO . append ( ( ooo % 'SpinzTV Settings' , 'RunPlugin(plugin://%s/?mode=settings)' % OO0o ) )
 return Oo0Oo00o00oO
 if 42 - 42: iIIIII1I + iIIIII1I * I11I1i1iIII1I
def o0Oo ( ) :
 o0O0 = wiz . log_check ( )
 I1I1Iiii1 = o0O0 . replace ( IIi1IiiiI1Ii , "" )
 if os . path . exists ( o0O0 ) or not o0O0 == False :
  i111i1 = open ( o0O0 , mode = 'r' ) ; OoOoOo0 = i111i1 . read ( ) ; i111i1 . close ( )
  wiz . TextBoxes ( "%s - %s" % ( Oo0Ooo , I1I1Iiii1 ) , OoOoOo0 )
 else :
  wiz . LogNotify ( 'View Log' , 'No Log File Found!' )
  if 39 - 39: II1I1Ii - ooOo0o0O00
def OOO0o0OO0OO ( ) :
 if os . path . exists ( oo00 ) :
  i111i1 = open ( oo00 , mode = 'r' ) ; OoOoOo0 = i111i1 . read ( ) ; i111i1 . close ( )
  wiz . TextBoxes ( "%s - Wizard.log" % Oo0Ooo , OoOoOo0 )
 else :
  wiz . LogNotify ( 'View Log' , 'Wizard.log not found!' )
  if 64 - 64: I11I1i1iIII1I
def iIIIiIi1I1i ( addon ) :
 if ooo0OO . yesno ( Oo0Ooo , 'Are you sure you want to delete the addon:' , '[COLOR yellow]%s[/COLOR]' % addon , yeslabel = 'Yes, Remove' , nolabel = 'No, Cancel' ) :
  wiz . cleanHouse ( os . path . join ( OOOo0 , addon ) )
  OoOOoO0oOo ( addon )
  wiz . LogNotify ( 'Remove Addon' , 'Complete!' )
  ooo0OO . ok ( Oo0Ooo , 'The addon has been removed but will remain in the addons list until the next time you reload Kodi.' )
 else : wiz . LogNotify ( 'Remove Addon' , 'Cancelled!' )
 xbmc . executebuiltin ( 'Container.Refresh' )
 if 70 - 70: II1I1Ii % oo0 . iI1i + iI1i - Ii % iIIIII1I
def OoOOoO0oOo ( addon ) :
 if addon == 'all' :
  if ooo0OO . yesno ( Oo0Ooo , 'Would you like to remove ALL addon data stored in you Userdata folder?' , yeslabel = 'Yes, Remove' , nolabel = 'No, Cancel' ) :
   wiz . cleanHouse ( IiI )
  else : wiz . LogNotify ( 'Remove Addon Data' , 'Cancelled!' )
 elif addon == 'uninstalled' :
  if ooo0OO . yesno ( Oo0Ooo , 'Would you like to remove ALL addon data stored in you Userdata folder for uninstalled addons?' , yeslabel = 'Yes, Remove' , nolabel = 'No, Cancel' ) :
   i1IIi1i1Ii1 = 0
   for iiiIi in glob . glob ( os . path . join ( IiI , '*' ) ) :
    II1Iii = iiiIi . replace ( IiI , '' ) . replace ( '\\' , '' ) . replace ( '/' , '' )
    if II1Iii in o00OO00OoO : pass
    elif os . path . exists ( os . path . join ( OOOo0 , II1Iii ) ) : pass
    else : wiz . cleanHouse ( iiiIi ) ; i1IIi1i1Ii1 += 1 ; wiz . log ( iiiIi ) ; shutil . rmtree ( iiiIi )
   wiz . LogNotify ( 'Clean up Uninstalled' , '[COLOR yellow]%s[/COLOR] Folders(s) Removed' % i1IIi1i1Ii1 )
  else : wiz . LogNotify ( 'Remove Addon Data' , 'Cancelled!' )
 elif addon == 'empty' :
  if ooo0OO . yesno ( Oo0Ooo , 'Would you like to remove ALL empty addon data folders in you Userdata folder?' , yeslabel = 'Yes, Remove' , nolabel = 'No, Cancel' ) :
   i1IIi1i1Ii1 = wiz . emptyfolder ( IiI )
   wiz . LogNotify ( 'Remove Empty Folders' , '[COLOR yellow]%s[/COLOR] Folders(s) Removed' % i1IIi1i1Ii1 )
  else : wiz . LogNotify ( 'Remove Empty Folders' , 'Cancelled!' )
 else :
  Iii = os . path . join ( Oooo000o , 'addon_data' , addon )
  if addon in o00OO00OoO :
   wiz . LogNotify ( "Protected Plugin" , "Not allowed to remove Addon_Data" )
  elif os . path . exists ( Iii ) :
   if ooo0OO . yesno ( Oo0Ooo , 'Would you also like to remove the addon data for:' , '[COLOR yellow]%s[/COLOR]' % addon , yeslabel = 'Yes, Remove' , nolabel = 'No, Cancel' ) :
    wiz . cleanHouse ( Iii )
    try :
     shutil . rmtree ( Iii )
    except :
     wiz . log ( "Error deleting: %s" % Iii )
   else :
    wiz . log ( 'Addon data for %s was not removed' % addon )
 xbmc . executebuiltin ( 'Container.Refresh' )
 if 63 - 63: IIIi11I11 + Ii
 if 1 - 1: ooOo0o0O00 / iI1i11 + i1I1 . Ii / ooOo0o0O00 - O0i11I1I1I
 if 5 - 5: o0O0oO0O00O0o
 if 4 - 4: O0i11I1I1I % iIIIII1I / iI1i11 . o0O0oO0O00O0o / o0O0oO0O00O0o - ooOo0o0O00
 if 79 - 79: ooOo0o0O00 + iIIIII1I
def iIiII ( install = None ) :
 if oOOoO0 == 'true' :
  traktit . autoUpdate ( 'all' )
  wiz . setS ( 'traktlastsave' , str ( IIIII ) )
 if O0OoO000O0OO == 'true' :
  debridit . autoUpdate ( 'all' )
  wiz . setS ( 'debridlastsave' , str ( IIIII ) )
 if o00 not in [ 'skin.confluence' ] :
  iIiIIi = 'skin.confluence'
  III11iiii11i1 = ooo0OO . yesno ( Oo0Ooo , "The skin needs to be set back to [COLOR yellow]%s[/COLOR]" % iIiIIi [ 5 : ] , "Before doing a fresh install to clear all Texture files!" , "Would you like us to do that for you?" , nolabel = "No, Thanks" , yeslabel = "Yes, Swap Skin" ) ;
  if III11iiii11i1 :
   skinSwitch . swapSkins ( iIiIIi )
   while not xbmc . getCondVisibility ( "Window.isVisible(yesnodialog)" ) :
    xbmc . sleep ( 200 )
   xbmc . executebuiltin ( "Action(Left)" )
   xbmc . executebuiltin ( "Action(Select)" )
  else : wiz . LogNotify ( Oo0Ooo , 'Fresh Install: [COLOR red]Cancelled![/COLOR]' ) ; return
 if install : iii1IIIiiiI = ooo0OO . yesno ( Oo0Ooo , "Do you wish to restore your" , "Kodi configuration to default settings" , "Before installing %s?" % install , nolabel = 'No, Cancel' , yeslabel = 'Yes, Continue' )
 else : iii1IIIiiiI = ooo0OO . yesno ( Oo0Ooo , "Do you wish to restore your" , "Kodi configuration to default settings?" , nolabel = 'No, Cancel' , yeslabel = 'Yes, Continue' )
 if iii1IIIiiiI :
  III1I = os . path . abspath ( O00ooooo00 )
  II1 . create ( Oo0Ooo , "Clearing all files and folders:" , '' , '' )
  I1I111iIi = sum ( [ len ( OoOOOO ) for I1iiIi111I , Iiii1iIii , OoOOOO in os . walk ( III1I ) ] ) ; oOoooO000O = 0 ;
  try :
   for III1I11i1iIi , OO0oo0O0OOO0 , OoOOOO in os . walk ( III1I , topdown = True ) :
    OO0oo0O0OOO0 [ : ] = [ Iiii1iIii for Iiii1iIii in OO0oo0O0OOO0 if Iiii1iIii not in o00OO00OoO ]
    for iI1I in OoOOOO :
     oOoooO000O += 1
     OoOOoIii1 = III1I11i1iIi . split ( '\\' )
     OoOOo00 = len ( OoOOoIii1 ) - 1
     if iI1I == 'sources.xml' and OoOOoIii1 [ OoOOo00 ] == 'userdata' and iI111I11I1I1 == 'true' : wiz . log ( "Keep Sources: %s\\%s" % ( III1I11i1iIi , iI1I ) )
     elif iI1I == 'favourites.xml' and OoOOoIii1 [ OoOOo00 ] == 'userdata' and i1iIIi1 == 'true' : wiz . log ( "Keep Favourites: %s\\%s" % ( III1I11i1iIi , iI1I ) )
     elif iI1I == 'profiles.xml' and OoOOoIii1 [ OoOOo00 ] == 'userdata' and OOooO0OOoo == 'true' : wiz . log ( "Keep Profiles: %s\\%s" % ( III1I11i1iIi , iI1I ) )
     elif iI1I == 'advancedsettings.xml' and OoOOoIii1 [ OoOOo00 ] == 'userdata' and iIii1 == 'true' : wiz . log ( "Keep Advanced Settings: %s\\%s" % ( III1I11i1iIi , iI1I ) )
     elif iI1I in [ 'xbmc.log' , 'kodi.log' , 'spmc.log' , 'tvmc.log' ] : wiz . log ( "Keep Log File: %s" % iI1I )
     elif iI1I . endswith ( '.db' ) :
      try : os . remove ( os . path . join ( III1I11i1iIi , iI1I ) )
      except : wiz . log ( 'Failed to delete, Purging DB.' ) ; wiz . purgeDb ( os . path . join ( III1I11i1iIi , iI1I ) )
     else :
      II1 . update ( int ( Ooo0 ( oOoooO000O , I1I111iIi ) ) , '' , 'File: [COLOR yellow]%s[/COLOR]' % iI1I , '' )
      try : os . remove ( os . path . join ( III1I11i1iIi , iI1I ) )
      except : wiz . log ( "Error removing %s\\%s" % ( III1I11i1iIi , iI1I ) )
   for III1I11i1iIi , OO0oo0O0OOO0 , OoOOOO in os . walk ( III1I , topdown = True ) :
    OO0oo0O0OOO0 [ : ] = [ Iiii1iIii for Iiii1iIii in OO0oo0O0OOO0 if Iiii1iIii not in o00OO00OoO ]
    for iI1I in OO0oo0O0OOO0 :
     II1 . update ( 100 , '' , 'Cleaning Up Empty Folder: [COLOR yellow]%s[/COLOR]' % iI1I , '' )
     if iI1I not in [ "Database" , "userdata" , "temp" , "addons" , "addon_data" ] :
      shutil . rmtree ( os . path . join ( III1I11i1iIi , iI1I ) , ignore_errors = True , onerror = None )
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
   oo00ooOoo ( install , 'normal' )
  else :
   ooo0OO . ok ( Oo0Ooo , "The process is complete, you're now back to a fresh Kodi configuration with SpinzTV Wizard" , "Please reboot your system or restart Kodi in order for the changes to be applied." )
   wiz . killxbmc ( )
 else : wiz . LogNotify ( Oo0Ooo , 'Fresh Install: [COLOR red]Cancelled![/COLOR]' ) ; xbmc . executebuiltin ( 'Container.Refresh' )
 if 53 - 53: IIIi11I11 . iIIIII1I % oo0 % iiiiII1I % II1I1Ii
 if 53 - 53: iIIIII1I
 if 69 - 69: iiiiII1I . Ii . oo0o0000 - ooOo0o0O00
 if 32 - 32: iI1II / oo0o0000 / oo0 + I11I1i1iIII1I . i1I1 . Ii
def ii1ii ( ) :
 if ooo0OO . yesno ( Oo0Ooo , 'Would you like to clear cache?' , nolabel = 'Cancel' , yeslabel = 'Delete' ) :
  wiz . clearCache ( )
  IIiI1i ( )
  if 6 - 6: ooOo0o0O00 / O0i11I1I1I - o0O0oO0O00O0o
def IIiI1i ( ) :
 o00O00Oo00O = wiz . latestDB ( 'Textures' )
 if ooo0OO . yesno ( Oo0Ooo , "Would you like to delete the %s and Thumbnails folder?" % o00O00Oo00O , "They will repopulate on startup" , nolabel = 'No, Cancel' , yeslabel = 'Yes, Remove' ) :
  try : wiz . removeFile ( os . join ( O0oo0OO0 , o00O00Oo00O ) )
  except : wiz . log ( 'Failed to delete, Purging DB.' ) ; wiz . purgeDb ( o00O00Oo00O )
  wiz . removeFolder ( i1i1II )
  wiz . killxbmc ( )
 else : wiz . log ( 'Clear thumbnames cancelled' )
 if 46 - 46: iiiiII1I % o0OOo0o0O0O / i1I1 * iI1i * o0O0oO0O00O0o
def OOoOOOo0Ooo0 ( ) :
 o0OOOOO0O = [ ] ; o0iIiiIiiIi = [ ]
 for I1I1IiIi1 , oOO0o0oo0 , OoOOOO in os . walk ( O00ooooo00 ) :
  for i111i1 in fnmatch . filter ( OoOOOO , '*.db' ) :
   if i111i1 != 'Thumbs.db' :
    oOo000O = os . path . join ( I1I1IiIi1 , i111i1 )
    o0OOOOO0O . append ( oOo000O )
    dir = oOo000O . replace ( '\\' , '/' ) . split ( '/' )
    o0iIiiIiiIi . append ( '(%s) %s' % ( dir [ len ( dir ) - 2 ] , dir [ len ( dir ) - 1 ] ) )
 if ooooooO0oo >= 16 :
  iII = ooo0OO . multiselect ( "Select DB File to Purge" , o0iIiiIiiIi )
  if iII == None : wiz . LogNotify ( "Purge Database" , "Cancelled" )
  elif len ( iII ) == 0 : wiz . LogNotify ( "Purge Database" , "Cancelled" )
  else :
   for ooO0o0O0Oo in iII : wiz . purgeDb ( o0OOOOO0O [ ooO0o0O0Oo ] )
 else :
  iII = ooo0OO . select ( "Select DB File to Purge" , o0iIiiIiiIi )
  if iII == - 1 : wiz . LogNotify ( "Purge Database" , "Cancelled" )
  else : wiz . purgeDb ( o0OOOOO0O [ ooO0o0O0Oo ] )
  if 1 - 1: oo0 + iI1i / Ii1I11I - O0i11I1I1I % IIIi11I11 + IIIi11I11
  if 24 - 24: oo0o0000 + iI1i + o0O0oO0O00O0o - iI1II + iI1i
  if 93 - 93: ooI1i . oo0 % i11iIiiIii . iiiiII1I % ooI1i + Ii1I11I
  if 65 - 65: oOo000OOOo + iI1i11 - iI1II
def OOoOO0o ( ) :
 OooOoOo = wiz . workingURL ( ii1iii1i )
 if OooOoOo == True :
  Iii1iiIi1II = wiz . openURL ( ii1iii1i ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
  id , OoOoOo0 = Iii1iiIi1II . split ( '|||' )
  notify . TestNotification ( msg = OoOoOo0 , title = ooOoO00 , BorderWidth = 10 )
 else : wiz . LogNotify ( Oo0Ooo , "Invalid URL for Notification" )
 if 51 - 51: iI1i - ooOo0o0O00 * II1I1Ii
def ii1111Ii1i ( ) :
 if IiII111i1i11 == 'No' : I1ii1ii11i1I ( '==============BackUp Options===============' , '' , themeit = i1i1iI1iiiI )
 I1ii1ii11i1I ( 'Full Backup' , 'full' , icon = iiIIIII1i1iI , themeit = i1I1i111Ii )
 I1ii1ii11i1I ( 'Backup for Builds (Exc: Thumbnails, Databases)' , 'backb' , icon = iiIIIII1i1iI , themeit = i1I1i111Ii )
 I1ii1ii11i1I ( 'Backup addon data' , 'backad' , icon = iiIIIII1i1iI , themeit = i1I1i111Ii )
 if IiII111i1i11 == 'No' : I1ii1ii11i1I ( '==============Restore Options===============' , '' , themeit = i1i1iI1iiiI )
 OOoOooOoOOOoo ( 'Restore Full Backup' , 'refull' , icon = iiIIIII1i1iI , themeit = i1I1i111Ii )
 OOoOooOoOOOoo ( 'Restore Addon Data' , 'refull' , icon = iiIIIII1i1iI , themeit = i1I1i111Ii )
 if IiII111i1i11 == 'No' : I1ii1ii11i1I ( '==============Other Options===============' , '' , themeit = i1i1iI1iiiI )
 OOoOooOoOOOoo ( 'Delete A Backup' , 'delbu' , icon = iiIIIII1i1iI , themeit = i1I1i111Ii )
 I1ii1ii11i1I ( 'Delete All Backups' , 'delall' , icon = iiIIIII1i1iI , themeit = i1I1i111Ii )
 I1ii1ii11i1I ( 'Select Backup Location' , 'settings' , icon = iiIIIII1i1iI , themeit = i1I1i111Ii )
 if 48 - 48: Ii1I11I * oOo000OOOo - Ii1I11I / oOo000OOOo + iiiiII1I
 if 52 - 52: iI1i11 % oOo000OOOo * I11I1i1iIII1I
 if 4 - 4: II1I1Ii % Ii1I11I - iI1II + ooI1i . i1I1 % I11I1i1iIII1I
 if 9 - 9: I11I1i1iIII1I * I11I1i1iIII1I . i11iIiiIii * oo0
 if 18 - 18: iI1i11 . I11I1i1iIII1I % iiiiII1I % oOo000OOOo
 if 87 - 87: oo0 . iI1II * iiiiII1I
def OOoOooOoOOOoo ( display , mode , name = None , url = None , menu = None , overwrite = True , fanart = I1i1iiI1 , icon = iiIIIII1i1iI , themeit = None ) :
 OOOo = '%s?mode=%s' % ( sys . argv [ 0 ] , urllib . quote_plus ( mode ) )
 if not name == None : OOOo += "&name=" + urllib . quote_plus ( name )
 if not url == None : OOOo += "&url=" + urllib . quote_plus ( url )
 o0ooOo00O = True
 if themeit : display = themeit % display
 Ii1i1I1 = xbmcgui . ListItem ( display , iconImage = "DefaultFolder.png" , thumbnailImage = icon )
 Ii1i1I1 . setInfo ( type = "Video" , infoLabels = { "Title" : display , "Plot" : Oo0Ooo } )
 Ii1i1I1 . setProperty ( "Fanart_Image" , fanart )
 if not menu == None : Ii1i1I1 . addContextMenuItems ( menu , replaceItems = overwrite )
 o0ooOo00O = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = OOOo , listitem = Ii1i1I1 , isFolder = True )
 return o0ooOo00O
 if 97 - 97: iIIIII1I . ooI1i - iIIIII1I + oo0o0000 * I11I1i1iIII1I
 if 10 - 10: oOo000OOOo + II1I1Ii % iI1II - oo0o0000
def Ii1IIIIi1ii1I ( display , mode , name = None , url = None , menu = None , overwrite = True , fanart = I1i1iiI1 , icon = iiIIIII1i1iI , description = None , themeit = None ) :
 OOOo = '%s?mode=%s' % ( sys . argv [ 0 ] , urllib . quote_plus ( mode ) )
 if not name == None : OOOo += "&name=" + urllib . quote_plus ( name )
 if not url == None : OOOo += "&url=" + urllib . quote_plus ( url )
 if not description == None : OOOo += "&description=" + urllib . quote_plus ( description )
 o0ooOo00O = True
 if themeit : display = themeit % display
 Ii1i1I1 = xbmcgui . ListItem ( description , iconImage = "DefaultFolder.png" , thumbnailImage = icon )
 Ii1i1I1 . setInfo ( type = "Video" , infoLabels = { "Title" : description , "Plot" : Oo0Ooo } )
 Ii1i1I1 . setProperty ( "Fanart_Image" , fanart )
 if not menu == None : Ii1i1I1 . addContextMenuItems ( menu , replaceItems = overwrite )
 o0ooOo00O = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = OOOo , listitem = Ii1i1I1 , isFolder = False )
 return o0ooOo00O
 if 70 - 70: o0O0oO0O00O0o - O0i11I1I1I
def I1ii1ii11i1I ( display , mode , name = None , url = None , menu = None , overwrite = True , fanart = I1i1iiI1 , icon = iiIIIII1i1iI , themeit = None ) :
 OOOo = '%s?mode=%s' % ( sys . argv [ 0 ] , urllib . quote_plus ( mode ) )
 if not name == None : OOOo += "&name=" + urllib . quote_plus ( name )
 if not url == None : OOOo += "&url=" + urllib . quote_plus ( url )
 o0ooOo00O = True
 if themeit : display = themeit % display
 Ii1i1I1 = xbmcgui . ListItem ( display , iconImage = "DefaultFolder.png" , thumbnailImage = icon )
 Ii1i1I1 . setInfo ( type = "Video" , infoLabels = { "Title" : display , "Plot" : Oo0Ooo } )
 Ii1i1I1 . setProperty ( "Fanart_Image" , fanart )
 if not menu == None : Ii1i1I1 . addContextMenuItems ( menu , replaceItems = overwrite )
 o0ooOo00O = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = OOOo , listitem = Ii1i1I1 , isFolder = False )
 return o0ooOo00O
 if 2 - 2: oo0
def iiii1 ( name , url , mode , iconimage , fanart , description ) :
 OOOo = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&fanart=" + urllib . quote_plus ( fanart )
 o0ooOo00O = True
 Ii1i1I1 = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 Ii1i1I1 . setInfo ( type = "Video" , infoLabels = { "Title" : name } )
 Ii1i1I1 . setProperty ( "Fanart_Image" , fanart )
 o0ooOo00O = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = OOOo , listitem = Ii1i1I1 , isFolder = False )
 return o0ooOo00O
 if 66 - 66: i1I1 * oo0 % oo0 * IIIi11I11 - ooI1i - IIIi11I11
def o0O0oO0 ( name , url , mode , iconimage , fanart , description ) :
 OOOo = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart ) + "&description=" + urllib . quote_plus ( description )
 o0ooOo00O = True
 Ii1i1I1 = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 Ii1i1I1 . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description } )
 Ii1i1I1 . setProperty ( "Fanart_Image" , fanart )
 if mode == 90 :
  o0ooOo00O = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = OOOo , listitem = Ii1i1I1 , isFolder = False )
 else :
  o0ooOo00O = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = OOOo , listitem = Ii1i1I1 , isFolder = True )
 return o0ooOo00O
 if 77 - 77: Ii1I11I . oOo000OOOo
 if 39 - 39: ooI1i . I11I1i1iIII1I
def iIiIi1iI11iiI ( ) :
 iiI1Ii11II1I = [ ]
 I1Ii11II1I1 = sys . argv [ 2 ]
 if len ( I1Ii11II1I1 ) >= 2 :
  IiI1iI1IiiIi1 = sys . argv [ 2 ]
  OoO0oo = IiI1iI1IiiIi1 . replace ( '?' , '' )
  if ( IiI1iI1IiiIi1 [ len ( IiI1iI1IiiIi1 ) - 1 ] == '/' ) :
   IiI1iI1IiiIi1 = IiI1iI1IiiIi1 [ 0 : len ( IiI1iI1IiiIi1 ) - 2 ]
  OoOoO0O = OoO0oo . split ( '&' )
  iiI1Ii11II1I = { }
  for o0i1I11iI1iiI in range ( len ( OoOoO0O ) ) :
   I1ii = { }
   I1ii = OoOoO0O [ o0i1I11iI1iiI ] . split ( '=' )
   if ( len ( I1ii ) ) == 2 :
    iiI1Ii11II1I [ I1ii [ 0 ] ] = I1ii [ 1 ]
    if 80 - 80: ooOo0o0O00 / oo0 % iiiiII1I
  return iiI1Ii11II1I
  if 80 - 80: iI1i11 % O0i11I1I1I
IiI1iI1IiiIi1 = iIiIi1iI11iiI ( )
OooOoOo = None
iI1I = None
O0Oo0 = None
if 80 - 80: oo0o0000 - oo0 . o0O0oO0O00O0o + iI1i11 - iIIIII1I
try : O0Oo0 = urllib . unquote_plus ( IiI1iI1IiiIi1 [ "mode" ] )
except : pass
try : iI1I = urllib . unquote_plus ( IiI1iI1IiiIi1 [ "name" ] )
except : pass
try : OooOoOo = urllib . unquote_plus ( IiI1iI1IiiIi1 [ "url" ] )
except : pass
if 5 - 5: O0i11I1I1I
wiz . log ( '[ Version : \'%s\' ] [ Mode : \'%s\' ] [ Name : \'%s\' ] [ Url : \'%s\' ]' % ( iiiii , O0Oo0 if not O0Oo0 == '' else None , iI1I , OooOoOo ) )
def OOiI1 ( ) :
 if 42 - 42: o0O0oO0O00O0o % i1I1 / iI1i11 - i1I1 * i11iIiiIii
 for file in os . listdir ( oO00oOo ) :
  if file . endswith ( ".zip" ) :
   OooOoOo = xbmc . translatePath ( os . path . join ( oO00oOo , file ) )
   iiii1 ( file , OooOoOo , 'read' , iiIIIII1i1iI , iiIIIII1i1iI , '' )
   if 19 - 19: i1I1 * oo0o0000 % i11iIiiIii
def iiI1Ii1I ( ) :
 i11Ii1iIiII = xbmc . translatePath ( os . path . join ( 'special://' , 'home' ) )
 for file in os . listdir ( oO00oOo ) :
  if file . endswith ( ".zip" ) :
   OooOoOo = xbmc . translatePath ( os . path . join ( oO00oOo , file ) )
   o0O0oO0 ( file , OooOoOo , 'dell' , iiIIIII1i1iI , iiIIIII1i1iI , '' )
   if 81 - 81: II1I1Ii . iI1II * iiiiII1I % IIIi11I11 . II1I1Ii
   if 60 - 60: o0O0oO0O00O0o / oo0o0000
def o0OoOO ( content , viewType ) :
 if content :
  xbmcplugin . setContent ( int ( sys . argv [ 1 ] ) , content )
 if wiz . getS ( 'auto-view' ) == 'true' :
  xbmc . executebuiltin ( "Container.SetViewMode(%s)" % wiz . getS ( viewType ) )
  if 78 - 78: II1I1Ii . IIIi11I11
if O0Oo0 == None : Ooo0O0oooo ( )
if 38 - 38: iiiiII1I + IIIi11I11
elif O0Oo0 == 'builds' : IiIiII1 ( )
elif O0Oo0 == 'showupdate' : iIi1I1 ( iI1I )
elif O0Oo0 == 'viewbuild' : ii1II ( iI1I )
elif O0Oo0 == 'install' : oo00ooOoo ( iI1I , OooOoOo )
elif O0Oo0 == 'theme' : oo00ooOoo ( iI1I , O0Oo0 , OooOoOo )
if 15 - 15: iI1i + II1I1Ii . ooI1i - oo0 / Ii1I11I % oo0
elif O0Oo0 == 'maint' : I111i1I1 ( )
elif O0Oo0 == 'speed' : o000 ( )
elif O0Oo0 == 'speedtest' : speedtest . runtest ( OooOoOo )
elif O0Oo0 == 'clearcache' : ii1ii ( )
elif O0Oo0 == 'clearpackages' : wiz . clearPackages ( )
elif O0Oo0 == 'clearthumb' : IIiI1i ( )
elif O0Oo0 == 'freshstart' : iIiII ( )
elif O0Oo0 == 'forceupdate' : wiz . forceUpdate ( )
elif O0Oo0 == 'forceclose' : wiz . killxbmc ( )
elif O0Oo0 == 'uploadlog' : uploadLog . LogUploader ( )
elif O0Oo0 == 'viewlog' : o0Oo ( )
elif O0Oo0 == 'viewwizlog' : OOO0o0OO0OO ( )
elif O0Oo0 == 'clearwizlog' : i111i1 = open ( oo00 , 'w' ) ; i111i1 . close ( ) ; wiz . LogNotify ( Oo0Ooo , "Wizard Log Cleared!" )
elif O0Oo0 == 'purgedb' : OOoOOOo0Ooo0 ( )
elif O0Oo0 == 'removeaddons' : iii1III1i ( )
elif O0Oo0 == 'removeaddon' : iIIIiIi1I1i ( iI1I )
elif O0Oo0 == 'removeaddondata' : oooo00 ( )
elif O0Oo0 == 'removedata' : OoOOoO0oOo ( iI1I )
elif O0Oo0 == 'resetaddon' : i1IIi1i1Ii1 = wiz . cleanHouse ( ooOo , ignore = True ) ; wiz . LogNotify ( Oo0Ooo , "Addon_Data reset" )
if 86 - 86: oo0o0000 / i1I1 * oOo000OOOo
elif O0Oo0 == 'apkspinz' : ii1III11 ( )
elif O0Oo0 == 'apkin' : o0o0O00oo0 ( )
elif O0Oo0 == 'apk' : O00o0OO0000oo ( )
elif O0Oo0 == 'apkkodi' : ooO0o ( )
elif O0Oo0 == 'apkmaster' : O00oo0ooO ( )
elif O0Oo0 == 'apkgames' : ii11I1 ( )
elif O0Oo0 == 'emurom' : Ii111iIi1iIi ( )
elif O0Oo0 == 'emulators' : OoOo ( )
elif O0Oo0 == 'roms' : OoO ( )
elif O0Oo0 == 'snes' : O0iII1 ( )
elif O0Oo0 == 'nes' : i1iIi ( )
elif O0Oo0 == 'nesa' : O0000OOO0 ( )
elif O0Oo0 == 'nesc' : I111iIi1 ( )
elif O0Oo0 == 'nesd' : II11iI111i1 ( )
elif O0Oo0 == 'nesf' : iIi1 ( )
elif O0Oo0 == 'nesh' : OoO00 ( )
elif O0Oo0 == 'nesl' : o000oOoo0o000 ( )
elif O0Oo0 == 'nesn' : oo0O0Ooooooo ( )
elif O0Oo0 == 'nesr' : o0iiiI1I1iIIIi1 ( )
elif O0Oo0 == 'nest' : OOOIiiiii1iI ( )
elif O0Oo0 == 'nesw' : ii11i ( )
elif O0Oo0 == 'gen' : oOo00O000Oo0 ( )
elif O0Oo0 == 'gena' : oOooO0OOOoO000 ( )
elif O0Oo0 == 'genc' : oOOOoo ( )
elif O0Oo0 == 'gene' : oooO0o0o0O0 ( )
elif O0Oo0 == 'genh' : OOooOo00oo0 ( )
elif O0Oo0 == 'genm' : IIiiIIi1 ( )
elif O0Oo0 == 'genp' : i11I1iIi ( )
elif O0Oo0 == 'gens' : oOoO00 ( )
elif O0Oo0 == 'genu' : OOOooo ( )
elif O0Oo0 == 'atr' : OOO00O0oOOo ( )
elif O0Oo0 == 'atra' : O0oooo00o0Oo ( )
elif O0Oo0 == 'atrc' : oO0Ooo0ooOO0 ( )
elif O0Oo0 == 'atre' : ooo0o0O0o ( )
elif O0Oo0 == 'atrh' : I1Ii ( )
elif O0Oo0 == 'atrm' : iII11I1Ii1 ( )
elif O0Oo0 == 'atrp' : ii1iIi1II ( )
elif O0Oo0 == 'atrs' : oo0o0oooo ( )
elif O0Oo0 == 'atrv' : ii1ii11 ( )
elif O0Oo0 == 'n64' : iii1 ( )
elif O0Oo0 == 'tbg' : ooO0oO00O0o ( )
elif O0Oo0 == 'tga' : i11iIIi11 ( )
elif O0Oo0 == 'tgc' : ii ( )
elif O0Oo0 == 'tgf' : II1IOoOo000oOo0oo ( )
elif O0Oo0 == 'tgj' : iIiIIii ( )
elif O0Oo0 == 'tgn' : iIII1i1i ( )
elif O0Oo0 == 'tgr' : I1II ( )
elif O0Oo0 == 'tgv' : ii11II1i ( )
elif O0Oo0 == 'apkvid' : O00Oo ( )
elif O0Oo0 == 'apksys' : I11Oo00oO0O ( )
elif O0Oo0 == 'apkinstall' : oOo0OooOo ( iI1I , OooOoOo )
elif O0Oo0 == 'rominstall' : I1Iii1iI1 ( iI1I , OooOoOo , )
if 64 - 64: ooI1i / Ii1I11I * iiiiII1I * ooI1i
if 60 - 60: II1I1Ii / o0OOo0o0O0O % ooOo0o0O00 / ooOo0o0O00 * ooOo0o0O00 . i11iIiiIii
elif O0Oo0 == 'savedata' : iiIII1II ( )
elif O0Oo0 == 'togglesetting' : wiz . setS ( iI1I , 'false' if wiz . getS ( iI1I ) == 'true' else 'true' ) ; xbmc . executebuiltin ( 'Container.Refresh' )
if 99 - 99: iiiiII1I
elif O0Oo0 == 'trakt' : oOooO00o0O ( )
elif O0Oo0 == 'savetrakt' : traktit . traktIt ( 'update' , iI1I )
elif O0Oo0 == 'restoretrakt' : traktit . traktIt ( 'restore' , iI1I )
elif O0Oo0 == 'addontrakt' : traktit . traktIt ( 'clearaddon' , iI1I )
elif O0Oo0 == 'cleartrakt' : traktit . clearSaved ( iI1I )
elif O0Oo0 == 'authtrakt' : traktit . activateTrakt ( iI1I ) ; xbmc . executebuiltin ( 'Container.Refresh' )
if 77 - 77: Ii
elif O0Oo0 == 'realdebrid' : IiiIi1IIII1i ( )
elif O0Oo0 == 'savedebrid' : debridit . debridIt ( 'update' , iI1I )
elif O0Oo0 == 'restoredebrid' : debridit . debridIt ( 'restore' , iI1I )
elif O0Oo0 == 'addondebrid' : debridit . debridIt ( 'clearaddon' , iI1I )
elif O0Oo0 == 'cleardebrid' : debridit . clearSaved ( iI1I )
elif O0Oo0 == 'authdebrid' : debridit . activateDebrid ( iI1I ) ; xbmc . executebuiltin ( 'Container.Refresh' )
if 48 - 48: iiiiII1I % ooOo0o0O00 / II1I1Ii . oo0 * I11I1i1iIII1I
elif O0Oo0 == 'contact' : wiz . TextBoxes ( Oo0Ooo , o0O00Oo0 )
elif O0Oo0 == 'settings' : wiz . openS ( ) ; xbmc . executebuiltin ( 'Container.Refresh' )
if 65 - 65: iiiiII1I
elif O0Oo0 == 'developer' : I11i11I1iiII ( )
elif O0Oo0 == 'convertpath' : wiz . convertSpecial ( O00ooooo00 )
elif O0Oo0 == 'testnotify' : OOoOO0o ( )
elif O0Oo0 == 'bre' : ii1111Ii1i ( )
elif O0Oo0 == 'full' : backuprestore . FullBackup ( )
elif O0Oo0 == 'backb' : backuprestore . Backup ( )
elif O0Oo0 == 'backad' : backuprestore . ADDON_DATA_BACKUP ( )
elif O0Oo0 == 'refull' : OOiI1 ( )
elif O0Oo0 == 'delbu' : iiI1Ii1I ( )
elif O0Oo0 == 'delall' : backuprestore . DeleteAllBackups ( )
elif O0Oo0 == 'read' : backuprestore . READ_ZIP ( OooOoOo )
elif O0Oo0 == 'dell' : backuprestore . DeleteBackup ( OooOoOo )
if O0Oo0 not in [ '' , 'togglesettings' , 'settings' , 'contact' ] : xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
# dd678faae9ac167bc83abf78e5cb2f3f0688d3a3