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
I1IiiI = xbmc . translatePath ( 'special://logpath/' )
IIi1IiiiI1Ii = xbmc . translatePath ( 'special://profile/' )
zip = plugintools . get_setting ( "zip" )
I11i11Ii = xbmc . translatePath ( os . path . join ( zip ) )
oO00oOo = os . path . join ( O00ooooo00 , 'addons' )
OOOo0 = os . path . join ( O00ooooo00 , 'userdata' )
Oooo000o = os . path . join ( oO00oOo , OO0o )
IiIi11iIIi1Ii = os . path . join ( oO00oOo , 'packages' )
Oo0O = os . path . join ( OOOo0 , 'addon_data' )
IiI = os . path . join ( OOOo0 , 'addon_data' , OO0o )
ooOo = os . path . join ( OOOo0 , 'advancedsettings.xml' )
Oo = os . path . join ( OOOo0 , 'sources.xml' )
o0O = os . path . join ( OOOo0 , 'favourites.xml' )
IiiIII111iI = os . path . join ( OOOo0 , 'profiles.xml' )
IiII = os . path . join ( OOOo0 , 'guisettings.xml' )
iI1Ii11111iIi = os . path . join ( OOOo0 , 'Thumbnails' )
i1i1II = os . path . join ( OOOo0 , 'Database' )
O0oo0OO0 = os . path . join ( Oooo000o , 'fanart.jpg' )
I1i1iiI1 = os . path . join ( Oooo000o , 'icon.png' )
iiIIIII1i1iI = os . path . join ( Oooo000o , 'resources' , 'art' )
o0oO0 = os . path . join ( IiI , 'wizard.log' )
oo00 = xbmc . getSkinDir ( )
o00 = wiz . getS ( 'buildname' )
Oo0oO0ooo = wiz . getS ( 'buildversion' )
o0oOoO00o = wiz . getS ( 'buildtheme' )
i1 = wiz . getS ( 'latestversion' )
oOOoo00O0O = wiz . getS ( 'show15' )
i1111 = wiz . getS ( 'show16' )
i11 = wiz . getS ( 'autoclean' )
I11 = wiz . getS ( 'clearcache' )
Oo0o0000o0o0 = wiz . getS ( 'clearpackages' )
oOo0oooo00o = wiz . getS ( 'seperate' )
oO0o0o0ooO0oO = wiz . getS ( 'notify' )
oo0o0O00 = wiz . getS ( 'noteid' )
oO = wiz . getS ( 'notedismiss' )
i1iiIIiiI111 = wiz . getS ( 'traktlastsave' )
oooOOOOO = wiz . getS ( 'debridlastsave' )
i1iiIII111ii = wiz . getS ( 'keepfavourites' )
i1iIIi1 = wiz . getS ( 'keepgui' )
ii11iIi1I = wiz . getS ( 'keepsources' )
iI111I11I1I1 = wiz . getS ( 'keepprofiles' )
OOooO0OOoo = wiz . getS ( 'keepadvanced' )
iIii1 = wiz . getS ( 'keeptrakt' )
oOOoO0 = wiz . getS ( 'keepdebrid' )
O0OoO000O0OO = wiz . getS ( 'exodus' )
iiI1IiI = wiz . getS ( 'salts' )
II = wiz . getS ( 'saltshd' )
ooOoOoo0O = wiz . getS ( 'royalwe' )
OooO0 = wiz . getS ( 'velocity' )
II11iiii1Ii = wiz . getS ( 'velocitykids' )
OO0oOoo = wiz . getS ( 'specto' )
O0o0Oo = wiz . getS ( 'trakt' )
Oo00OOOOO = wiz . getS ( 'realexodus' )
O0O = wiz . getS ( 'realspecto' )
O00o0OO = wiz . getS ( 'urlresolver' )
I11i1 = wiz . getS ( 'developer' )
iIi1ii1I1 = date . today ( )
o0 = iIi1ii1I1 + timedelta ( days = 1 )
I11II1i = iIi1ii1I1 + timedelta ( days = 3 )
IIIII = float ( xbmc . getInfoLabel ( "System.BuildVersion" ) [ : 4 ] )
ooooooO0oo = 'plugin.video.exodus'
IIiiiiiiIi1I1 = 'plugin.video.velocity'
I1IIIii = 'plugin.video.velocitykids'
oOoOooOo0o0 = 'plugin.video.salts'
OOOO = 'plugin.video.saltshd.lite'
OOO00 = 'plugin.video.theroyalwe'
iiiiiIIii = 'plugin.video.specto'
O000OO0 = 'script.trakt'
I11iii1Ii = 'script.module.urlresolver'
I1IIiiIiii = os . path . join ( oO00oOo , oOoOooOo0o0 )
O000oo0O = os . path . join ( oO00oOo , OOOO )
OOOOi11i1 = os . path . join ( oO00oOo , ooooooO0oo )
IIIii1II1II = os . path . join ( oO00oOo , IIiiiiiiIi1I1 )
i1I1iI = os . path . join ( oO00oOo , I1IIIii )
oo0OooOOo0 = os . path . join ( oO00oOo , OOO00 )
o0OO00oO = os . path . join ( oO00oOo , iiiiiIIii )
I11i1I1I = os . path . join ( oO00oOo , O000OO0 )
oO0Oo = os . path . join ( oO00oOo , I11iii1Ii )
oOOoo0Oo = uservar . EXCLUDES
o00OO00OoO = uservar . BUILDFILE
OOOO0OOoO0O0 = uservar . APKSPINZFILE
O0Oo000ooO00 = uservar . APKFILE
oO0 = uservar . APKGAMEFILE
Ii1iIiII1ii1 = uservar . APKVIDFILE
ooOooo000oOO = uservar . APKSYSFILE
Oo0oOOo = uservar . SPEEDFILE
Oo0OoO00oOO0o = wiz . workingURL ( o00OO00OoO )
OOO00O = wiz . workingURL ( OOOO0OOoO0O0 )
OOoOO0oo0ooO = wiz . workingURL ( O0Oo000ooO00 )
O0o0O00Oo0o0 = wiz . workingURL ( oO0 )
O00O0oOO00O00 = wiz . workingURL ( Ii1iIiII1ii1 )
i1Oo00 = wiz . workingURL ( ooOooo000oOO )
i1i = wiz . workingURL ( Oo0oOOo )
iiI111I1iIiI = uservar . UPDATECHECK if str ( uservar . UPDATECHECK ) . isdigit ( ) else 1
IIIi1I1IIii1II = iIi1ii1I1 + timedelta ( days = iiI111I1iIiI )
O0 = uservar . NOTIFICATION
ii1ii1ii = uservar . ENABLE
oooooOoo0ooo = uservar . HEADERMESSAGE
I1I1IiI1 = uservar . HIDECONTACT
III1iII1I1ii = uservar . CONTACT
oOOo0 = uservar . HIDESPACERS
oo00O00oO = uservar . COLOR1
iIiIIIi = uservar . COLOR2
ooo00OOOooO = uservar . THEME1
O00OOOoOoo0O = uservar . THEME2
O000OOo00oo = uservar . THEME3
oo0OOo = uservar . THEME4
ooOOO00Ooo = uservar . THEME5
IiIIIi1iIi = uservar . ICONMAINT if not uservar . ICONMAINT == 'http://' else I1i1iiI1
ooOOoooooo = uservar . ICONBUILDS if not uservar . ICONBUILDS == 'http://' else I1i1iiI1
II1I = uservar . ICONSPEED if not uservar . ICONSPEED == 'http://' else I1i1iiI1
O0i1II1Iiii1I11 = uservar . ICONAPK if not uservar . ICONAPK == 'http://' else I1i1iiI1
IIII = uservar . ICONCONTACT if not uservar . ICONCONTACT == 'http://' else I1i1iiI1
iiIiI = uservar . ICONSAVE if not uservar . ICONSAVE == 'http://' else I1i1iiI1
o00oooO0Oo = uservar . ICONREAL if not uservar . ICONREAL == 'http://' else I1i1iiI1
o0O0OOO0Ooo = uservar . ICONTRAKT if not uservar . ICONTRAKT == 'http://' else I1i1iiI1
iiIiII1 = uservar . ICONSETTINGS if not uservar . ICONSETTINGS == 'http://' else I1i1iiI1
OOO00O0O = uservar . ICONKODI if not uservar . ICONKODI == 'http://' else I1i1iiI1
iii = uservar . ICONGAMES if not uservar . ICONGAMES == 'http://' else I1i1iiI1
oOooOOOoOo = uservar . ICONMOVIES if not uservar . ICONMOVIES == 'http://' else I1i1iiI1
i1Iii1i1I = uservar . ICONANDROID if not uservar . ICONANDROID == 'http://' else I1i1iiI1
OOoO00 = uservar . ICONSPMC if not uservar . ICONSPMC == 'http://' else I1i1iiI1
IiI111111IIII = uservar . ICONSPINZ if not uservar . ICONSPINZ == 'http://' else I1i1iiI1
###########################
###### Menu Items   #######
###########################
#addDir (display,mode,name=None,url=None,menu=None,overwrite=True,fanart=FANART,icon=ICON, themeit=None)
#addFile(display,mode,name=None,url=None,menu=None,overwrite=True,fanart=FANART,icon=ICON, themeit=None)
if 37 - 37: ooo0 / I1iI1iIi111i
if 44 - 44: i1IIi % I11IiI % O0ooO0Oo00o
if 77 - 77: iiIIiiIi1Ii11 * Oo0
if 70 - 70: oo
def I1IiiiiI ( ) :
 if len ( o00 ) > 0 :
  o0OIiII = wiz . checkBuild ( o00 , 'version' )
  ii1iII1II = '%s (v%s)' % ( o00 , Oo0oO0ooo )
  if o0OIiII > Oo0oO0ooo : ii1iII1II = '%s [COLOR red][B][UPDATE v%s][/B][/COLOR]' % ( ii1iII1II , o0OIiII )
  Iii1I1I11iiI1 ( ii1iII1II , 'viewbuild' , o00 , themeit = oo0OOo )
  I1I1i1I = wiz . checkBuild ( o00 , 'theme' )
  if not I1I1i1I == 'http://' and wiz . workingURL ( I1I1i1I ) == True :
   ii1I ( 'None' if o0oOoO00o == "" else o0oOoO00o , 'theme' , o00 , themeit = ooOOO00Ooo )
 else : Iii1I1I11iiI1 ( 'None' , 'builds' , themeit = oo0OOo )
 if oOOo0 == 'No' : ii1I ( '============================================' , '' , themeit = O000OOo00oo )
 Iii1I1I11iiI1 ( 'SpinzTV Builds' , 'builds' , icon = ooOOoooooo , themeit = ooo00OOOooO )
 Iii1I1I11iiI1 ( 'Maintenance' , 'maint' , icon = IiIIIi1iIi , themeit = ooo00OOOooO )
 Iii1I1I11iiI1 ( 'Speed Test' , 'speed' , icon = II1I , themeit = ooo00OOOooO )
 Iii1I1I11iiI1 ( 'Apk Installer (ANDROID ONLY!!!)' , 'apk' , icon = O0i1II1Iiii1I11 , themeit = ooo00OOOooO )
 Iii1I1I11iiI1 ( 'Save Data' , 'savedata' , icon = iiIiI , themeit = ooo00OOOooO )
 if I1I1IiI1 == 'No' : ii1I ( 'Contact' , 'contact' , icon = IIII , themeit = ooo00OOOooO )
 if oOOo0 == 'No' : ii1I ( '============================================' , '' , themeit = O000OOo00oo )
 ii1I ( 'Settings' , 'settings' , icon = iiIiII1 , themeit = ooo00OOOooO )
 if I11i1 == 'true' : Iii1I1I11iiI1 ( 'Developer Menu' , 'developer' , icon = iiIiII1 , themeit = ooo00OOOooO )
 O0oO0 ( 'movies' , 'MAIN' )
 if 87 - 87: I1I1II1I11 . IIiiIiII1Ii
 if 88 - 88: IiII111iI1ii1 * I11I1IIII + iIIIiiI1i1
 if 50 - 50: oOo00oOoO000
 if 93 - 93: oo0o % IIii11I1 - II1I11Ii1 % Ii
def i1I11 ( ) :
 if not Oo0OoO00oOO0o == True :
  ii1I ( 'Kodi Version: %s' % IIIII , '' , icon = ooOOoooooo , themeit = O000OOo00oo )
  if oOOo0 == 'No' : ii1I ( '============================================' , '' , themeit = O000OOo00oo )
  ii1I ( 'Url for txt file not valid' , '' , icon = ooOOoooooo , themeit = O000OOo00oo )
  ii1I ( '%s' % Oo0OoO00oOO0o , '' , icon = ooOOoooooo , themeit = O000OOo00oo )
 else :
  oOooOOo0o = wiz . openURL ( o00OO00OoO ) . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
  O0O0ooOOO = re . compile ( 'name="(.+?)".+?ersion="(.+?)".+?rl="(.+?)".+?odi="(.+?)".+?con="(.+?)".+?anart="(.+?)"' ) . findall ( oOooOOo0o )
  if len ( O0O0ooOOO ) == 1 :
   oOOo0O00o ( O0O0ooOOO [ 0 ] [ 0 ] )
  elif len ( O0O0ooOOO ) > 1 :
   ii1I ( 'Kodi Version: %s' % IIIII , '' , icon = ooOOoooooo , themeit = O000OOo00oo )
   if oOOo0 == 'No' : ii1I ( '============================================' , '' , themeit = O000OOo00oo )
   if oOo0oooo00o == 'true' :
    for iIiIi11 , o0OIiII , OOO , iiiiI , oooOo0OOOoo0 , OOoO in O0O0ooOOO :
     OO0O000 = iiIiI1i1 ( 'install' , iIiIi11 )
     Iii1I1I11iiI1 ( '[%s] %s (v%s)' % ( float ( iiiiI ) , iIiIi11 , o0OIiII ) , 'viewbuild' , iIiIi11 , fanart = OOoO , icon = oooOo0OOOoo0 , menu = OO0O000 , themeit = O00OOOoOoo0O )
   else :
    oO0O00oOOoooO = wiz . buildCount ( '15' ) ; IiIi11iI = wiz . buildCount ( '16' )
    if IiIi11iI > 0 :
     if oO0O00oOOoooO > 0 :
      Oo0O00O000 = '+' if i1111 == 'false' else '-'
      ii1I ( '[%s] Jarvis and Above(%s)' % ( Oo0O00O000 , IiIi11iI ) , 'showupdate' , '16' , themeit = O000OOo00oo )
     if i1111 == 'true' :
      for iIiIi11 , o0OIiII , OOO , iiiiI , oooOo0OOOoo0 , OOoO in O0O0ooOOO :
       i11I1IiII1i1i = int ( float ( iiiiI ) )
       if i11I1IiII1i1i >= 16 :
        OO0O000 = iiIiI1i1 ( 'install' , iIiIi11 )
        Iii1I1I11iiI1 ( '[%s] %s (v%s)' % ( float ( iiiiI ) , iIiIi11 , o0OIiII ) , 'viewbuild' , iIiIi11 , fanart = OOoO , icon = oooOo0OOOoo0 , menu = OO0O000 , themeit = O00OOOoOoo0O )
    if oO0O00oOOoooO > 0 :
     if IiIi11iI > 0 :
      Oo0O00O000 = '+' if oOOoo00O0O == 'false' else '-'
      ii1I ( '[%s] Isengard and Below(%s)' % ( Oo0O00O000 , oO0O00oOOoooO ) , 'showupdate' , '15' , themeit = O000OOo00oo )
     if oOOoo00O0O == 'true' :
      for iIiIi11 , o0OIiII , OOO , iiiiI , oooOo0OOOoo0 , OOoO in O0O0ooOOO :
       i11I1IiII1i1i = int ( float ( iiiiI ) )
       if i11I1IiII1i1i <= 15 :
        OO0O000 = iiIiI1i1 ( 'install' , iIiIi11 )
        Iii1I1I11iiI1 ( '[%s] %s (v%s)' % ( float ( iiiiI ) , iIiIi11 , o0OIiII ) , 'viewbuild' , iIiIi11 , fanart = OOoO , icon = oooOo0OOOoo0 , menu = OO0O000 , themeit = O00OOOoOoo0O )
  else : ii1I ( 'Text file for builds not formated correctly.' , '' , icon = ooOOoooooo , themeit = O000OOo00oo )
 O0oO0 ( 'movies' , 'MAIN' )
 if 95 - 95: i1I
def oOOo0O00o ( name ) :
 if not Oo0OoO00oOO0o == True :
  ii1I ( 'Url for txt file not valid' , '' , themeit = O000OOo00oo )
  ii1I ( '%s' % Oo0OoO00oOO0o , '' , themeit = O000OOo00oo )
  return
 if wiz . checkBuild ( name , 'version' ) == False :
  ii1I ( 'Error reading the txt file.' , '' , themeit = O000OOo00oo )
  ii1I ( '%s was not found in the builds list.' % name , '' , themeit = O000OOo00oo )
  return
 oOooOOo0o = wiz . openURL ( o00OO00OoO ) . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
 O0O0ooOOO = re . compile ( 'name="%s".+?ersion="(.+?)".+?rl="(.+?)".+?ui="(.+?)".+?odi="(.+?)".+?heme="(.+?)".+?con="(.+?)".+?anart="(.+?)"' % name ) . findall ( oOooOOo0o )
 for o0OIiII , OOO , O0ooooOOoo0O , iiiiI , I1I1i1I , oooOo0OOOoo0 , OOoO in O0O0ooOOO :
  oooOo0OOOoo0 = oooOo0OOOoo0 if wiz . workingURL ( oooOo0OOOoo0 ) else I1i1iiI1
  OOoO = OOoO if wiz . workingURL ( OOoO ) else O0oo0OO0
  ii1iII1II = '%s (v%s)' % ( name , o0OIiII )
  if o00 == name and o0OIiII > Oo0oO0ooo :
   ii1iII1II = '%s [COLOR red][B][CURRENT v%s][/B][/COLOR]' % ( ii1iII1II , Oo0oO0ooo )
  ii1I ( ii1iII1II , '' , fanart = OOoO , icon = oooOo0OOOoo0 , themeit = O00OOOoOoo0O )
  ii1I ( '===============[ Install ]===================' , '' , fanart = OOoO , icon = oooOo0OOOoo0 , themeit = O000OOo00oo )
  ii1I ( 'Fresh Install' , 'install' , name , 'fresh' , fanart = OOoO , icon = oooOo0OOOoo0 , themeit = ooo00OOOooO )
  ii1I ( 'Standard Install' , 'install' , name , 'normal' , fanart = OOoO , icon = oooOo0OOOoo0 , themeit = ooo00OOOooO )
  if not O0ooooOOoo0O == 'http://' : ii1I ( 'Apply guiFix' , 'install' , name , 'gui' , fanart = OOoO , icon = oooOo0OOOoo0 , themeit = ooo00OOOooO )
  if not I1I1i1I == 'http://' :
   if wiz . workingURL ( I1I1i1I ) == True :
    ii1I ( '===============[ Themes ]==================' , '' , fanart = OOoO , icon = oooOo0OOOoo0 , themeit = O000OOo00oo )
    oOooOOo0o = wiz . openURL ( I1I1i1I ) . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
    O0O0ooOOO = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?con="(.+?)".+?anart="(.+?)"' ) . findall ( oOooOOo0o )
    for II1IiiIi1i , iiI11ii1I1 , Ooo0OOoOoO0 , oOo0OOoO0 in O0O0ooOOO :
     Ooo0OOoOoO0 = Ooo0OOoOoO0 if Ooo0OOoOoO0 == 'http://' else oooOo0OOOoo0
     oOo0OOoO0 = oOo0OOoO0 if oOo0OOoO0 == 'http://' else OOoO
     ii1I ( II1IiiIi1i if not II1IiiIi1i == o0oOoO00o else "[B]%s (Installed)[/B]" % II1IiiIi1i , 'theme' , name , II1IiiIi1i , fanart = oOo0OOoO0 , icon = Ooo0OOoOoO0 , themeit = O000OOo00oo )
     if 11 - 11: IiII111iI1ii1 . oo * II1I11Ii1 * i1IIi + i1I
     if 33 - 33: ooo0 * IIiiIiII1Ii - Ii % Ii
     if 18 - 18: Ii / Oo0 * Ii + Ii * i11iIiiIii * IiII111iI1ii1
     if 11 - 11: i1I / I1I1II1I11 - II1I11Ii1 * i1IIi + i1IIi . I1I1II1I11
def i1I1i111Ii ( ) :
 Iii1I1I11iiI1 ( 'SpinzTV APKS' , 'apkspinz' , icon = IiI111111IIII , themeit = ooo00OOOooO )
 Iii1I1I11iiI1 ( 'Kodi and SPMC' , 'apkkodi' , icon = OOO00O0O , themeit = ooo00OOOooO )
 Iii1I1I11iiI1 ( 'Games' , 'apkgames' , icon = iii , themeit = ooo00OOOooO )
 Iii1I1I11iiI1 ( 'Movie and Video' , 'apkvid' , icon = oOooOOOoOo , themeit = ooo00OOOooO )
 Iii1I1I11iiI1 ( 'System Tools' , 'apksys' , icon = i1Iii1i1I , themeit = ooo00OOOooO )
 Iii1I1I11iiI1 ( 'APK Master List' , 'apkmaster' , icon = O0i1II1Iiii1I11 , themeit = ooo00OOOooO )
 if 67 - 67: iiIIiiIi1Ii11 . I11IiI
def i1i1iI1iiiI ( ) :
 if OOO00O :
  oOooOOo0o = wiz . openURL ( OOOO0OOoO0O0 ) . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
 O0O0ooOOO = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?con="(.+?)".+?anart="(.+?)"' ) . findall ( oOooOOo0o )
 if len ( O0O0ooOOO ) > 0 :
  for iIiIi11 , OOO , oooOo0OOOoo0 , OOoO in O0O0ooOOO :
   ii1I ( iIiIi11 , 'apkinstall' , iIiIi11 , OOO , icon = oooOo0OOOoo0 , fanart = OOoO , themeit = ooo00OOOooO )
  else : wiz . log ( "[APK Menu] ERROR: Invalid Format." )
 else : wiz . log ( "[APK Menu] ERROR: URL for apk list not working." )
 if 51 - 51: iiIIiiIi1Ii11 % Ii . I11I1IIII / I1iI1iIi111i / oOo00oOoO000 . I11I1IIII
def IIIii11 ( ) :
 ii1I ( 'Kodi (v%s)' % wiz . latestApk ( 'kodi' , 'version' ) , 'apkinstall' , 'kodi' , wiz . latestApk ( 'kodi' , 'url' ) , icon = OOO00O0O , themeit = ooo00OOOooO )
 ii1I ( 'SPMC (v%s)' % wiz . latestApk ( 'spmc' , 'version' ) , 'apkinstall' , 'spmc' , wiz . latestApk ( 'spmc' , 'url' ) , icon = OOoO00 , themeit = ooo00OOOooO )
 if 9 - 9: ooo0 % ooo0 - IIiiIiII1Ii
def OoO ( ) :
 if O0o0O00Oo0o0 :
  oOooOOo0o = wiz . openURL ( oO0 ) . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
 O0O0ooOOO = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?con="(.+?)".+?anart="(.+?)"' ) . findall ( oOooOOo0o )
 if len ( O0O0ooOOO ) > 0 :
  for iIiIi11 , OOO , oooOo0OOOoo0 , OOoO in O0O0ooOOO :
   ii1I ( iIiIi11 , 'apkinstall' , iIiIi11 , OOO , icon = oooOo0OOOoo0 , fanart = OOoO , themeit = ooo00OOOooO )
  else : wiz . log ( "[APK Menu] ERROR: Invalid Format." )
 else : wiz . log ( "[APK Menu] ERROR: URL for apk list not working." )
 if 12 - 12: ooo0 - IIiiIiII1Ii
def oOoO00O0 ( ) :
 if O00O0oOO00O00 :
  oOooOOo0o = wiz . openURL ( Ii1iIiII1ii1 ) . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
 O0O0ooOOO = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?con="(.+?)".+?anart="(.+?)"' ) . findall ( oOooOOo0o )
 if len ( O0O0ooOOO ) > 0 :
  for iIiIi11 , OOO , oooOo0OOOoo0 , OOoO in O0O0ooOOO :
   ii1I ( iIiIi11 , 'apkinstall' , iIiIi11 , OOO , icon = oooOo0OOOoo0 , fanart = OOoO , themeit = ooo00OOOooO )
  else : wiz . log ( "[APK Menu] ERROR: Invalid Format." )
 else : wiz . log ( "[APK Menu] ERROR: URL for apk list not working." )
 if 75 - 75: iiIIiiIi1Ii11 . i1I . ooo0 * Ii
def i11II1I11I1 ( ) :
 if i1Oo00 :
  oOooOOo0o = wiz . openURL ( ooOooo000oOO ) . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
 O0O0ooOOO = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?con="(.+?)".+?anart="(.+?)"' ) . findall ( oOooOOo0o )
 if len ( O0O0ooOOO ) > 0 :
  for iIiIi11 , OOO , oooOo0OOOoo0 , OOoO in O0O0ooOOO :
   ii1I ( iIiIi11 , 'apkinstall' , iIiIi11 , OOO , icon = oooOo0OOOoo0 , fanart = OOoO , themeit = ooo00OOOooO )
  else : wiz . log ( "[APK Menu] ERROR: Invalid Format." )
 else : wiz . log ( "[APK Menu] ERROR: URL for apk list not working." )
 if 67 - 67: iiIIiiIi1Ii11 - IIiiIiII1Ii / oOo00oOoO000 - I11IiI
def i1II1 ( ) :
 if OOoOO0oo0ooO :
  oOooOOo0o = wiz . openURL ( O0Oo000ooO00 ) . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
 O0O0ooOOO = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?con="(.+?)".+?anart="(.+?)"' ) . findall ( oOooOOo0o )
 if len ( O0O0ooOOO ) > 0 :
  for iIiIi11 , OOO , oooOo0OOOoo0 , OOoO in O0O0ooOOO :
   ii1I ( iIiIi11 , 'apkinstall' , iIiIi11 , OOO , icon = oooOo0OOOoo0 , fanart = OOoO , themeit = ooo00OOOooO )
  else : wiz . log ( "[APK Menu] ERROR: Invalid Format." )
 else : wiz . log ( "[APK Menu] ERROR: URL for apk list not working." )
 if 25 - 25: Ii / I1iI1iIi111i % IIii11I1
 if 42 - 42: i11iIiiIii * I1iI1iIi111i / IiII111iI1ii1 . i11iIiiIii % oOo00oOoO000
 if 41 - 41: II1I11Ii1 / ooo0
 if 51 - 51: oOo00oOoO000 % iiIIiiIi1Ii11
def OooOo ( ) :
 i11III1111iIi = '[COLOR green]ON[/COLOR]' ; I1i111I = '[COLOR red]OFF[/COLOR]'
 Ooo = 'true' if i11 == 'true' else 'false'
 Oo0oo0O0o00O = 'true' if I11 == 'true' else 'false'
 I1i11 = 'true' if Oo0o0000o0o0 == 'true' else 'false'
 if 12 - 12: I11IiI + I11IiI - IiII111iI1ii1 * Oo0 % Oo0 - O0ooO0Oo00o
 ii1I ( 'Fresh Start' , 'freshstart' , icon = IiIIIi1iIi , themeit = ooo00OOOooO )
 ii1I ( 'Clear Cache' , 'clearcache' , icon = IiIIIi1iIi , themeit = ooo00OOOooO )
 ii1I ( 'Clear Packages' , 'clearpackages' , icon = IiIIIi1iIi , themeit = ooo00OOOooO )
 ii1I ( 'Clear Thumbnails' , 'clearthumb' , icon = IiIIIi1iIi , themeit = ooo00OOOooO )
 ii1I ( 'Purge Databases' , 'purgedb' , icon = IiIIIi1iIi , themeit = ooo00OOOooO )
 Iii1I1I11iiI1 ( 'Remove Addons' , 'removeaddons' , icon = IiIIIi1iIi , themeit = ooo00OOOooO )
 Iii1I1I11iiI1 ( 'Remove Addon Data' , 'removeaddondata' , icon = IiIIIi1iIi , themeit = ooo00OOOooO )
 ii1I ( 'Force Update Addons' , 'forceupdate' , icon = IiIIIi1iIi , themeit = ooo00OOOooO )
 ii1I ( 'Force Close Kodi' , 'forceclose' , icon = IiIIIi1iIi , themeit = ooo00OOOooO )
 ii1I ( 'Upload Kodi log' , 'uploadlog' , icon = IiIIIi1iIi , themeit = ooo00OOOooO )
 ii1I ( 'View Kodi Log File' , 'viewlog' , icon = IiIIIi1iIi , themeit = ooo00OOOooO )
 ii1I ( 'View Wizard Log File' , 'viewwizlog' , icon = IiIIIi1iIi , themeit = ooo00OOOooO )
 ii1I ( 'Clear Wizard Log File' , 'clearwizlog' , icon = IiIIIi1iIi , themeit = ooo00OOOooO )
 ii1I ( '==============[ Auto Clean ]==============' , '' , fanart = O0oo0OO0 , icon = IiIIIi1iIi , themeit = O000OOo00oo )
 ii1I ( 'Auto Clean Up On Startup: %s' % Ooo . replace ( 'true' , i11III1111iIi ) . replace ( 'false' , I1i111I ) , 'togglesetting' , 'autoclean' , icon = IiIIIi1iIi , themeit = ooo00OOOooO )
 if Ooo == 'true' :
  ii1I ( '--- Clear Cache on Startup: %s' % Oo0oo0O0o00O . replace ( 'true' , i11III1111iIi ) . replace ( 'false' , I1i111I ) , 'togglesetting' , 'clearcache' , icon = IiIIIi1iIi , themeit = ooo00OOOooO )
  ii1I ( '--- Clear Packages on Startup: %s' % I1i11 . replace ( 'true' , i11III1111iIi ) . replace ( 'false' , I1i111I ) , 'togglesetting' , 'clearpackages' , icon = IiIIIi1iIi , themeit = ooo00OOOooO )
 O0oO0 ( 'movies' , 'MAIN' )
 if 52 - 52: i1I . IIii11I1 + Ii
 if 38 - 38: I11IiI - O0ooO0Oo00o . Ii
 if 58 - 58: iiIIiiIi1Ii11 . IIii11I1 + I1I1II1I11
 if 66 - 66: IIii11I1 / I11I1IIII * i1IIi + i1IIi % oOo00oOoO000
def IIii1111 ( ) :
 if i1i :
  oOooOOo0o = wiz . openURL ( Oo0oOOo ) . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
 O0O0ooOOO = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?con="(.+?)".+?anart="(.+?)"' ) . findall ( oOooOOo0o )
 if len ( O0O0ooOOO ) > 0 :
  for iIiIi11 , OOO , oooOo0OOOoo0 , OOoO in O0O0ooOOO :
   ii1I ( iIiIi11 , 'speedtest' , iIiIi11 , OOO , icon = oooOo0OOOoo0 , fanart = OOoO , themeit = ooo00OOOooO )
  else : wiz . log ( "[APK Menu] ERROR: Invalid Format." )
 else : wiz . log ( "[APK Menu] ERROR: URL for apk list not working." )
 if 42 - 42: oOo00oOoO000 / IIiiIiII1Ii . I11I1IIII + I11I1IIII % I1I1II1I11 + i11iIiiIii
 if 56 - 56: IIiiIiII1Ii
 if 28 - 28: IIii11I1 . IIii11I1 % I1iI1iIi111i * I1iI1iIi111i . IIiiIiII1Ii / IIii11I1
 if 27 - 27: oo + i1I - I11IiI
def O00oOOooo ( ) :
 i11III1111iIi = '[COLOR green]ON[/COLOR]' ; I1i111I = '[COLOR red]OFF[/COLOR]'
 iI1iIii11Ii = 'true' if iIii1 == 'true' else 'false'
 IIi1i1I11Iii = 'true' if oOOoO0 == 'true' else 'false'
 I1i1i1 = 'true' if ii11iIi1I == 'true' else 'false'
 OoO0O00O0oo0O = 'true' if OOooO0OOoo == 'true' else 'false'
 I1IiI11 = 'true' if iI111I11I1I1 == 'true' else 'false'
 iI1iiiiIii = 'true' if i1iiIII111ii == 'true' else 'false'
 O0ooooOOoo0O = 'true' if i1iIIi1 == 'true' else 'false'
 if 19 - 19: oo - Oo0 . ooo0
 Iii1I1I11iiI1 ( 'Keep Trakt Data' , 'trakt' , icon = iiIiI , themeit = ooo00OOOooO )
 Iii1I1I11iiI1 ( 'Keep Real Debrid' , 'realdebrid' , icon = iiIiI , themeit = ooo00OOOooO )
 ii1I ( '- Click to toggle settings -' , '' , themeit = O000OOo00oo )
 ii1I ( 'Save Trakt: %s' % iI1iIii11Ii . replace ( 'true' , i11III1111iIi ) . replace ( 'false' , I1i111I ) , 'togglesetting' , 'keeptrakt' , icon = iiIiI , themeit = ooo00OOOooO )
 ii1I ( 'Save Real Debrid: %s' % IIi1i1I11Iii . replace ( 'true' , i11III1111iIi ) . replace ( 'false' , I1i111I ) , 'togglesetting' , 'keepdebrid' , icon = iiIiI , themeit = ooo00OOOooO )
 ii1I ( 'Keep \'Sources.xml\': %s' % I1i1i1 . replace ( 'true' , i11III1111iIi ) . replace ( 'false' , I1i111I ) , 'togglesetting' , 'keepsources' , icon = iiIiI , themeit = ooo00OOOooO )
 ii1I ( 'Keep \'Profiles.xml\': %s' % I1IiI11 . replace ( 'true' , i11III1111iIi ) . replace ( 'false' , I1i111I ) , 'togglesetting' , 'keepprofiles' , icon = iiIiI , themeit = ooo00OOOooO )
 ii1I ( 'Keep \'Advancedsettings.xml\': %s' % OoO0O00O0oo0O . replace ( 'true' , i11III1111iIi ) . replace ( 'false' , I1i111I ) , 'togglesetting' , 'keepadvanced' , icon = iiIiI , themeit = ooo00OOOooO )
 ii1I ( 'Keep \'Favourites.xml\': %s' % iI1iiiiIii . replace ( 'true' , i11III1111iIi ) . replace ( 'false' , I1i111I ) , 'togglesetting' , 'keepfavourites' , icon = iiIiI , themeit = ooo00OOOooO )
 ii1I ( 'Keep \'Guisettings.xml\': %s' % O0ooooOOoo0O . replace ( 'true' , i11III1111iIi ) . replace ( 'false' , I1i111I ) , 'togglesetting' , 'keepgui' , icon = iiIiI , themeit = ooo00OOOooO )
 if 60 - 60: O0ooO0Oo00o + Oo0
 if 9 - 9: i1I * i1IIi - I1iI1iIi111i + I1I1II1I11 / oo . oo
def iiIIi ( ) :
 iI1iIii11Ii = '[COLOR green]ON[/COLOR]' if iIii1 == 'true' else '[COLOR red]OFF[/COLOR]'
 iiI1iI111ii1i = str ( i1iiIIiiI111 ) if not i1iiIIiiI111 == '' else 'Trakt hasnt been saved yet.'
 ii1I ( '[I]Register FREE Account at http://trakt.tv[/I]' , '' , icon = o0O0OOO0Ooo , themeit = O000OOo00oo )
 ii1I ( 'Save Trakt Data: %s' % iI1iIii11Ii , 'togglesetting' , 'keeptrakt' , icon = o0O0OOO0Ooo , themeit = O000OOo00oo )
 if iIii1 == 'true' : ii1I ( 'Last Save: %s' % str ( iiI1iI111ii1i ) , '' , icon = o0O0OOO0Ooo , themeit = O000OOo00oo )
 if oOOo0 == 'No' : ii1I ( '============================================' , '' , icon = o0O0OOO0Ooo , themeit = O000OOo00oo )
 Ii1IIiI1IiIII = os . path . join ( oO00oOo , ooooooO0oo , 'icon.png' ) if os . path . exists ( OOOOi11i1 ) else o0O0OOO0Ooo
 OO0Oo000OOOoO = os . path . join ( oO00oOo , ooooooO0oo , 'fanart.jpg' ) if os . path . exists ( OOOOi11i1 ) else O0oo0OO0
 ii1I ( '[+]-- Exodus' , '' , icon = Ii1IIiI1IiIII , fanart = OO0Oo000OOOoO , themeit = O000OOo00oo )
 OO0O000 = iiIiI1i1 ( 'traktaddon' , 'Exodus' ) ; O0i11I1I1I = iiIiI1i1 ( 'trakt' , 'Exodus' )
 if not os . path . exists ( OOOOi11i1 ) : ii1I ( '[COLOR red]Addon Data: Not Installed[/COLOR]' , '' , icon = Ii1IIiI1IiIII , fanart = OO0Oo000OOOoO , menu = OO0O000 )
 elif not traktit . traktUser ( 'exodus' ) : ii1I ( '[COLOR red]Addon Data: Not Registered[/COLOR]' , 'authtrakt' , 'exodus' , icon = Ii1IIiI1IiIII , fanart = OO0Oo000OOOoO , menu = OO0O000 )
 else : ii1I ( '[COLOR green]Addon Data: %s[/COLOR]' % traktit . traktUser ( 'exodus' ) , 'authtrakt' , 'exodus' , icon = Ii1IIiI1IiIII , fanart = OO0Oo000OOOoO , menu = OO0O000 )
 if O0OoO000O0OO == "" : ii1I ( '[COLOR red]Saved Data: Not Saved[/COLOR]' , 'savetrakt' , 'exodus' , icon = Ii1IIiI1IiIII , fanart = OO0Oo000OOOoO , menu = O0i11I1I1I )
 else : ii1I ( '[COLOR green]Saved Data: %s[/COLOR]' % O0OoO000O0OO , '' , icon = Ii1IIiI1IiIII , fanart = OO0Oo000OOOoO , menu = O0i11I1I1I )
 oOOOo00O00O = os . path . join ( oO00oOo , oOoOooOo0o0 , 'icon.png' ) if os . path . exists ( I1IIiiIiii ) else o0O0OOO0Ooo
 iIIIII1I = os . path . join ( oO00oOo , oOoOooOo0o0 , 'fanart.jpg' ) if os . path . exists ( I1IIiiIiii ) else O0oo0OO0
 ii1I ( '[+]-- Salts' , '' , icon = oOOOo00O00O , fanart = iIIIII1I , themeit = O000OOo00oo )
 OO0O000 = iiIiI1i1 ( 'traktaddon' , 'Salts' ) ; O0i11I1I1I = iiIiI1i1 ( 'trakt' , 'Salts' )
 if not os . path . exists ( I1IIiiIiii ) : ii1I ( '[COLOR red]Addon Data: Not Installed[/COLOR]' , '' , icon = oOOOo00O00O , fanart = iIIIII1I , menu = OO0O000 )
 elif not traktit . traktUser ( 'salts' ) : ii1I ( '[COLOR red]Addon Data: Not Registered[/COLOR]' , 'authtrakt' , 'salts' , icon = oOOOo00O00O , fanart = iIIIII1I , menu = OO0O000 )
 else : ii1I ( '[COLOR green]Addon Data: %s[/COLOR]' % traktit . traktUser ( 'salts' ) , 'authtrakt' , 'salts' , icon = oOOOo00O00O , fanart = iIIIII1I , menu = OO0O000 )
 if iiI1IiI == "" : ii1I ( '[COLOR red]Saved Data: Not Saved[/COLOR]' , 'savetrakt' , 'salts' , icon = oOOOo00O00O , fanart = iIIIII1I , menu = O0i11I1I1I )
 else : ii1I ( '[COLOR green]Saved Data: %s[/COLOR]' % iiI1IiI , '' , icon = oOOOo00O00O , fanart = iIIIII1I , menu = O0i11I1I1I )
 ooI1i = os . path . join ( oO00oOo , OOOO , 'icon.png' ) if os . path . exists ( O000oo0O ) else o0O0OOO0Ooo
 iIII = os . path . join ( oO00oOo , OOOO , 'fanart.jpg' ) if os . path . exists ( O000oo0O ) else O0oo0OO0
 ii1I ( '[+]-- Salts HD' , '' , icon = ooI1i , fanart = iIII , themeit = O000OOo00oo )
 OO0O000 = iiIiI1i1 ( 'traktaddon' , 'Salts HD' ) ; O0i11I1I1I = iiIiI1i1 ( 'trakt' , 'Salts HD' )
 if not os . path . exists ( O000oo0O ) : ii1I ( '[COLOR red]Addon Data: Not Installed[/COLOR]' , '' , icon = ooI1i , fanart = iIII , menu = OO0O000 )
 elif not traktit . traktUser ( 'saltshd' ) : ii1I ( '[COLOR red]Addon Data: Not Registered[/COLOR]' , 'authtrakt' , 'saltshd' , icon = ooI1i , fanart = iIII , menu = OO0O000 )
 else : ii1I ( '[COLOR green]Addon Data: %s[/COLOR]' % traktit . traktUser ( 'saltshd' ) , 'authtrakt' , 'saltshd' , icon = ooI1i , fanart = iIII , menu = OO0O000 )
 if II == "" : ii1I ( '[COLOR red]Saved Data: Not Saved[/COLOR]' , 'savetrakt' , 'saltshd' , icon = ooI1i , fanart = iIII , menu = O0i11I1I1I )
 else : ii1I ( '[COLOR green]Saved Data: %s[/COLOR]' % II , '' , icon = ooI1i , fanart = iIII , menu = O0i11I1I1I )
 o0o0O = os . path . join ( oO00oOo , OOO00 , 'icon.png' ) if os . path . exists ( oo0OooOOo0 ) else o0O0OOO0Ooo
 ooooO0oOoOOoO = os . path . join ( oO00oOo , OOO00 , 'fanart.jpg' ) if os . path . exists ( oo0OooOOo0 ) else O0oo0OO0
 ii1I ( '[+]-- Royal We' , '' , icon = o0o0O , fanart = ooooO0oOoOOoO , themeit = O000OOo00oo )
 OO0O000 = iiIiI1i1 ( 'traktaddon' , 'Royal We' ) ; O0i11I1I1I = iiIiI1i1 ( 'trakt' , 'Royal We' )
 if not os . path . exists ( oo0OooOOo0 ) : ii1I ( '[COLOR red]Addon Data: Not Installed[/COLOR]' , '' , icon = o0o0O , fanart = ooooO0oOoOOoO , menu = OO0O000 )
 elif not traktit . traktUser ( 'royalwe' ) : ii1I ( '[COLOR red]Addon Data: Not Registered[/COLOR]' , 'authtrakt' , 'royalwe' , icon = o0o0O , fanart = ooooO0oOoOOoO , menu = OO0O000 )
 else : ii1I ( '[COLOR green]Addon Data: %s[/COLOR]' % traktit . traktUser ( 'royalwe' ) , 'authtrakt' , 'royalwe' , icon = o0o0O , fanart = ooooO0oOoOOoO , menu = OO0O000 )
 if ooOoOoo0O == "" : ii1I ( '[COLOR red]Saved Data: Not Saved[/COLOR]' , 'savetrakt' , 'royalwe' , icon = o0o0O , fanart = ooooO0oOoOOoO , menu = O0i11I1I1I )
 else : ii1I ( '[COLOR green]Saved Data: %s[/COLOR]' % ooOoOoo0O , '' , icon = o0o0O , fanart = ooooO0oOoOOoO , menu = O0i11I1I1I )
 I1i11i = os . path . join ( oO00oOo , IIiiiiiiIi1I1 , 'icon.png' ) if os . path . exists ( IIIii1II1II ) else o0O0OOO0Ooo
 IiIi = os . path . join ( oO00oOo , IIiiiiiiIi1I1 , 'fanart.jpg' ) if os . path . exists ( IIIii1II1II ) else O0oo0OO0
 ii1I ( '[+]-- Velocity' , '' , icon = I1i11i , fanart = IiIi , themeit = O000OOo00oo )
 OO0O000 = iiIiI1i1 ( 'traktaddon' , 'Velocity' ) ; O0i11I1I1I = iiIiI1i1 ( 'trakt' , 'Velocity' )
 if not os . path . exists ( IIIii1II1II ) : ii1I ( '[COLOR red]Addon Data: Not Installed[/COLOR]' , '' , icon = I1i11i , fanart = IiIi , menu = OO0O000 )
 elif not traktit . traktUser ( 'velocity' ) : ii1I ( '[COLOR red]Addon Data: Not Registered[/COLOR]' , 'authtrakt' , 'velocity' , icon = I1i11i , fanart = IiIi , menu = OO0O000 )
 else : ii1I ( '[COLOR green]Addon Data: %s[/COLOR]' % traktit . traktUser ( 'velocity' ) , 'authtrakt' , 'velocity' , icon = I1i11i , fanart = IiIi , menu = OO0O000 )
 if OooO0 == "" : ii1I ( '[COLOR red]Saved Data: Not Saved[/COLOR]' , 'savetrakt' , 'velocity' , icon = I1i11i , fanart = IiIi , menu = O0i11I1I1I )
 else : ii1I ( '[COLOR green]Saved Data: %s[/COLOR]' % OooO0 , '' , icon = I1i11i , fanart = IiIi , menu = O0i11I1I1I )
 OOOOO0O00 = os . path . join ( oO00oOo , I1IIIii , 'icon.png' ) if os . path . exists ( i1I1iI ) else o0O0OOO0Ooo
 Iii = os . path . join ( oO00oOo , I1IIIii , 'fanart.jpg' ) if os . path . exists ( i1I1iI ) else O0oo0OO0
 ii1I ( '[+]-- Velocity Kids' , '' , icon = OOOOO0O00 , fanart = Iii , themeit = O000OOo00oo )
 OO0O000 = iiIiI1i1 ( 'traktaddon' , 'Velocity Kids' ) ; O0i11I1I1I = iiIiI1i1 ( 'trakt' , 'Velocity Kids' )
 if not os . path . exists ( i1I1iI ) : ii1I ( '[COLOR red]Addon Data: Not Installed[/COLOR]' , '' , icon = OOOOO0O00 , fanart = Iii , menu = OO0O000 )
 elif not traktit . traktUser ( 'velocitykids' ) : ii1I ( '[COLOR red]Addon Data: Not Registered[/COLOR]' , 'authtrakt' , 'velocitykids' , icon = OOOOO0O00 , fanart = Iii , menu = OO0O000 )
 else : ii1I ( '[COLOR green]Addon Data: %s[/COLOR]' % traktit . traktUser ( 'velocitykids' ) , 'authtrakt' , 'velocitykids' , icon = OOOOO0O00 , fanart = Iii , menu = OO0O000 )
 if II11iiii1Ii == "" : ii1I ( '[COLOR red]Saved Data: Not Saved[/COLOR]' , 'savetrakt' , 'velocitykids' , icon = OOOOO0O00 , fanart = Iii , menu = O0i11I1I1I )
 else : ii1I ( '[COLOR green]Saved Data: %s[/COLOR]' % II11iiii1Ii , '' , icon = OOOOO0O00 , fanart = Iii , menu = O0i11I1I1I )
 iIIiIiI1I1 = os . path . join ( oO00oOo , iiiiiIIii , 'icon.png' ) if os . path . exists ( o0OO00oO ) else o0O0OOO0Ooo
 ooO = os . path . join ( oO00oOo , iiiiiIIii , 'fanart.jpg' ) if os . path . exists ( o0OO00oO ) else O0oo0OO0
 ii1I ( '[+]-- Specto' , '' , icon = iIIiIiI1I1 , fanart = ooO , themeit = O000OOo00oo )
 OO0O000 = iiIiI1i1 ( 'traktaddon' , 'Specto' ) ; O0i11I1I1I = iiIiI1i1 ( 'trakt' , 'Specto' )
 if not os . path . exists ( o0OO00oO ) : ii1I ( '[COLOR red]Addon Data: Not Installed[/COLOR]' , '' , icon = iIIiIiI1I1 , fanart = ooO , menu = OO0O000 )
 elif not traktit . traktUser ( 'specto' ) : ii1I ( '[COLOR red]Addon Data: Not Registered[/COLOR]' , 'authtrakt' , 'specto' , icon = iIIiIiI1I1 , fanart = ooO , menu = OO0O000 )
 else : ii1I ( '[COLOR green]Addon Data: %s[/COLOR]' % traktit . traktUser ( 'specto' ) , 'authtrakt' , 'specto' , icon = iIIiIiI1I1 , fanart = ooO , menu = OO0O000 )
 if OO0oOoo == "" : ii1I ( '[COLOR red]Saved Data: Not Saved[/COLOR]' , 'savetrakt' , 'specto' , icon = iIIiIiI1I1 , fanart = ooO , menu = O0i11I1I1I )
 else : ii1I ( '[COLOR green]Saved Data: %s[/COLOR]' % OO0oOoo , '' , icon = iIIiIiI1I1 , fanart = ooO , menu = O0i11I1I1I )
 ii = os . path . join ( oO00oOo , O000OO0 , 'icon.png' ) if os . path . exists ( I11i1I1I ) else o0O0OOO0Ooo
 OO0O0Ooo = os . path . join ( oO00oOo , O000OO0 , 'fanart.jpg' ) if os . path . exists ( I11i1I1I ) else O0oo0OO0
 ii1I ( '[+]-- Trakt' , '' , icon = OOOOO0O00 , fanart = OO0O0Ooo , themeit = O000OOo00oo )
 OO0O000 = iiIiI1i1 ( 'traktaddon' , 'Trakt' ) ; O0i11I1I1I = iiIiI1i1 ( 'trakt' , 'Trakt' )
 if not os . path . exists ( I11i1I1I ) : ii1I ( '[COLOR red]Addon Data: Not Installed[/COLOR]' , '' , icon = ii , fanart = OO0O0Ooo , menu = OO0O000 )
 elif not traktit . traktUser ( 'trakt' ) : ii1I ( '[COLOR red]Addon Data: Not Registered[/COLOR]' , 'authtrakt' , 'trakt' , icon = ii , fanart = OO0O0Ooo , menu = OO0O000 )
 else : ii1I ( '[COLOR green]Addon Data: %s[/COLOR]' % traktit . traktUser ( 'trakt' ) , 'authtrakt' , 'trakt' , icon = ii , fanart = OO0O0Ooo , menu = OO0O000 )
 if O0o0Oo == "" : ii1I ( '[COLOR red]Saved Data: Not Saved[/COLOR]' , 'savetrakt' , 'trakt' , icon = ii , fanart = OO0O0Ooo , menu = O0i11I1I1I )
 else : ii1I ( '[COLOR green]Saved Data: %s[/COLOR]' % O0o0Oo , '' , icon = ii , fanart = OO0O0Ooo , menu = O0i11I1I1I )
 if oOOo0 == 'No' : ii1I ( '============================================' , '' , themeit = O000OOo00oo )
 ii1I ( 'Save All Trakt Data' , 'savetrakt' , 'all' , icon = o0O0OOO0Ooo , themeit = O000OOo00oo )
 ii1I ( 'Recover All Saved Trakt Data' , 'restoretrakt' , 'all' , icon = o0O0OOO0Ooo , themeit = O000OOo00oo )
 ii1I ( 'Clear All Saved Trakt Data' , 'cleartrakt' , 'all' , icon = o0O0OOO0Ooo , themeit = O000OOo00oo )
 ii1I ( 'Clear All Addon Data' , 'addontrakt' , 'all' , icon = o0O0OOO0Ooo , themeit = O000OOo00oo )
 O0oO0 ( 'movies' , 'MAIN' )
 if 77 - 77: IIiiIiII1Ii / i1IIi
def IIii11I1i1I ( ) :
 IIi1i1I11Iii = '[COLOR green]ON[/COLOR]' if oOOoO0 == 'true' else '[COLOR red]OFF[/COLOR]'
 iiI1iI111ii1i = str ( oooOOOOO ) if not oooOOOOO == '' else 'Real Debrid hasnt been saved yet.'
 ii1I ( '[I]http://real-debrid.com is a PAID service.[/I]' , '' , icon = o0O0OOO0Ooo , themeit = O000OOo00oo )
 ii1I ( 'Save Real Debrid Data: %s' % IIi1i1I11Iii , 'togglesetting' , 'KEEPREAL' , icon = o00oooO0Oo , themeit = O000OOo00oo )
 if oOOoO0 == 'true' : ii1I ( 'Last Save: %s' % str ( iiI1iI111ii1i ) , '' , icon = o00oooO0Oo , themeit = O000OOo00oo )
 if oOOo0 == 'No' : ii1I ( '============================================' , '' , icon = o00oooO0Oo , themeit = O000OOo00oo )
 Ii1IIiI1IiIII = os . path . join ( oO00oOo , ooooooO0oo , 'icon.png' ) if os . path . exists ( OOOOi11i1 ) else o00oooO0Oo
 OO0Oo000OOOoO = os . path . join ( oO00oOo , ooooooO0oo , 'fanart.jpg' ) if os . path . exists ( OOOOi11i1 ) else O0oo0OO0
 o0o0OO0O00o = debridit . debridUser ( 'exodus' )
 ii1I ( '[+]-- Exodus' , '' , icon = Ii1IIiI1IiIII , fanart = OO0Oo000OOOoO , themeit = O000OOo00oo )
 OO0O000 = iiIiI1i1 ( 'debridaddon' , 'Exodus' ) ; O0i11I1I1I = iiIiI1i1 ( 'debrid' , 'Exodus' )
 if not os . path . exists ( OOOOi11i1 ) : ii1I ( '[COLOR red]Addon Data: Not Installed[/COLOR]' , '' , icon = Ii1IIiI1IiIII , fanart = OO0Oo000OOOoO , menu = OO0O000 )
 elif not o0o0OO0O00o : ii1I ( '[COLOR red]Addon Data: Not Registered[/COLOR]' , 'authdebrid' , 'exodus' , icon = Ii1IIiI1IiIII , fanart = OO0Oo000OOOoO , menu = OO0O000 )
 else : ii1I ( '[COLOR green]Addon Data: %s[/COLOR]' % o0o0OO0O00o , 'authdebrid' , 'exodus' , icon = Ii1IIiI1IiIII , fanart = OO0Oo000OOOoO , menu = OO0O000 )
 if Oo00OOOOO == "" : ii1I ( '[COLOR red]Saved Data: Not Saved[/COLOR]' , 'savedebrid' , 'exodus' , icon = Ii1IIiI1IiIII , fanart = OO0Oo000OOOoO , menu = O0i11I1I1I )
 else : ii1I ( '[COLOR green]Saved Data: %s[/COLOR]' % Oo00OOOOO , '' , icon = Ii1IIiI1IiIII , fanart = OO0Oo000OOOoO , menu = O0i11I1I1I )
 iIIiIiI1I1 = os . path . join ( oO00oOo , iiiiiIIii , 'icon.png' ) if os . path . exists ( o0OO00oO ) else o00oooO0Oo
 ooO = os . path . join ( oO00oOo , iiiiiIIii , 'fanart.jpg' ) if os . path . exists ( o0OO00oO ) else O0oo0OO0
 O0Oooo = debridit . debridUser ( 'specto' )
 ii1I ( '[+]-- Specto' , '' , icon = iIIiIiI1I1 , fanart = ooO , themeit = O000OOo00oo )
 OO0O000 = iiIiI1i1 ( 'debridaddon' , 'Specto' ) ; O0i11I1I1I = iiIiI1i1 ( 'debrid' , 'Specto' )
 if not os . path . exists ( o0OO00oO ) : ii1I ( '[COLOR red]Addon Data: Not Installed[/COLOR]' , '' , icon = iIIiIiI1I1 , fanart = ooO , menu = OO0O000 )
 elif not O0Oooo : ii1I ( '[COLOR red]Addon Data: Not Registered[/COLOR]' , 'authdebrid' , 'specto' , icon = iIIiIiI1I1 , fanart = ooO , menu = OO0O000 )
 else : ii1I ( '[COLOR green]Addon Data: %s[/COLOR]' % O0Oooo , 'authdebrid' , 'specto' , icon = iIIiIiI1I1 , fanart = ooO , menu = OO0O000 )
 if O0O == "" : ii1I ( '[COLOR red]Saved Data: Not Saved[/COLOR]' , 'savedebrid' , 'specto' , icon = iIIiIiI1I1 , fanart = ooO , menu = O0i11I1I1I )
 else : ii1I ( '[COLOR green]Saved Data: %s[/COLOR]' % O0O , '' , icon = iIIiIiI1I1 , fanart = ooO , menu = O0i11I1I1I )
 iiIi1i = os . path . join ( oO00oOo , I11iii1Ii , 'icon.png' ) if os . path . exists ( oO0Oo ) else o00oooO0Oo
 I1i11111i1i11 = os . path . join ( oO00oOo , I11iii1Ii , 'fanart.jpg' ) if os . path . exists ( oO0Oo ) else O0oo0OO0
 OOoOOO0 = debridit . debridUser ( 'url' )
 ii1I ( '[+]-- URL Resolver' , '' , icon = iiIi1i , fanart = I1i11111i1i11 , themeit = O000OOo00oo )
 OO0O000 = iiIiI1i1 ( 'debridaddon' , 'url' ) ; O0i11I1I1I = iiIiI1i1 ( 'debrid' , 'url' )
 if not os . path . exists ( oO0Oo ) : ii1I ( '[COLOR red]Addon Data: Not Installed[/COLOR]' , '' , icon = iiIi1i , fanart = I1i11111i1i11 , menu = OO0O000 )
 elif not OOoOOO0 : ii1I ( '[COLOR red]Addon Data: Not Registered[/COLOR]' , 'authdebrid' , 'url' , icon = iiIi1i , fanart = I1i11111i1i11 , menu = OO0O000 )
 else : ii1I ( '[COLOR green]Addon Data: %s[/COLOR]' % OOoOOO0 , 'authdebrid' , 'url' , icon = iiIi1i , fanart = I1i11111i1i11 , menu = OO0O000 )
 if O00o0OO == "" : ii1I ( '[COLOR red]Saved Data: Not Saved[/COLOR]' , 'savedebrid' , 'url' , icon = iiIi1i , fanart = I1i11111i1i11 , menu = O0i11I1I1I )
 else : ii1I ( '[COLOR green]Saved Data: %s[/COLOR]' % O00o0OO , '' , icon = iiIi1i , fanart = I1i11111i1i11 , menu = O0i11I1I1I )
 if oOOo0 == 'No' : ii1I ( '============================================' , '' , themeit = O000OOo00oo )
 ii1I ( 'Save All Real Debrid Data' , 'savedebrid' , 'all' , icon = o00oooO0Oo , themeit = O000OOo00oo )
 ii1I ( 'Recover All Saved Real Debrid Data' , 'restoredebrid' , 'all' , icon = o00oooO0Oo , themeit = O000OOo00oo )
 ii1I ( 'Clear All Saved Real Debrid Data' , 'cleardebrid' , 'all' , icon = o00oooO0Oo , themeit = O000OOo00oo )
 ii1I ( 'Clear All Addon Data' , 'addondebrid' , 'all' , icon = o00oooO0Oo , themeit = O000OOo00oo )
 O0oO0 ( 'movies' , 'MAIN' )
 if 10 - 10: Ii / i1I + i11iIiiIii / oo0o
def OOOoOoO ( ) :
 for iIIIII1ii1I in glob . glob ( os . path . join ( oO00oOo , '*/' ) ) :
  Ii1i1iI = iIIIII1ii1I . replace ( oO00oOo , '' ) . replace ( '\\' , '' ) . replace ( '/' , '' )
  oooOo0OOOoo0 = os . path . join ( iIIIII1ii1I , 'icon.png' )
  OOoO = os . path . join ( iIIIII1ii1I , 'fanart.png' )
  if Ii1i1iI in oOOoo0Oo : pass
  elif Ii1i1iI == 'packages' : pass
  else :
   IIiI1 = Ii1i1iI
   i1iI1 = { 'audio.' : '[COLOR orange][AUDIO] [/COLOR]' , 'metadata.' : '[COLOR cyan][METADATA] [/COLOR]' , 'module.' : '[COLOR orange][MODULE] [/COLOR]' , 'plugin.' : '[COLOR blue][PLUGIN] [/COLOR]' , 'program.' : '[COLOR orange][PROGRAM] [/COLOR]' , 'repository.' : '[COLOR gold][REPO] [/COLOR]' , 'script.' : '[COLOR green][SCRIPT] [/COLOR]' , 'service.' : '[COLOR green][SERVICE] [/COLOR]' , 'skin.' : '[COLOR dodgerblue][SKIN] [/COLOR]' , 'video.' : '[COLOR orange][VIDEO] [/COLOR]' , 'weather.' : '[COLOR yellow][WEATHER] [/COLOR]' }
   for ii1 in i1iI1 :
    IIiI1 = IIiI1 . replace ( ii1 , i1iI1 [ ii1 ] )
   ii1I ( '[COLOR red][B][REMOVE][/B][/COLOR] %s' % IIiI1 , 'removeaddon' , Ii1i1iI , icon = oooOo0OOOoo0 , fanart = OOoO , themeit = O00OOOoOoo0O )
   if 1 - 1: i1I % I1iI1iIi111i + Oo0 . I1iI1iIi111i % iiIIiiIi1Ii11
def o0o0oOoOO0O ( ) :
 if os . path . exists ( Oo0O ) :
  ii1I ( '[COLOR red][B][REMOVE][/B][/COLOR] All Addon_Data' , 'removedata' , 'all' , themeit = O00OOOoOoo0O )
  ii1I ( '[COLOR red][B][REMOVE][/B][/COLOR] All Addon_Data for Uninstalled Addons' , 'removedata' , 'uninstalled' , themeit = O00OOOoOoo0O )
  ii1I ( '[COLOR red][B][REMOVE][/B][/COLOR] All Empty Folders in Addon_Data' , 'removedata' , 'empty' , themeit = O00OOOoOoo0O )
  ii1I ( '[COLOR red][B][REMOVE][/B][/COLOR] %s Addon_Data' % Oo0Ooo , 'resetaddon' , themeit = O00OOOoOoo0O )
  if oOOo0 == 'No' : ii1I ( '============================================' , '' , themeit = O000OOo00oo )
  for iIIIII1ii1I in glob . glob ( os . path . join ( Oo0O , '*' ) ) :
   Ii1i1iI = iIIIII1ii1I . replace ( Oo0O , '' ) . replace ( '\\' , '' ) . replace ( '/' , '' )
   oooOo0OOOoo0 = os . path . join ( iIIIII1ii1I . replace ( Oo0O , oO00oOo ) , 'icon.png' )
   OOoO = os . path . join ( iIIIII1ii1I . replace ( Oo0O , oO00oOo ) , 'fanart.png' )
   IIiI1 = Ii1i1iI
   i1iI1 = { 'audio.' : '[COLOR orange][AUDIO] [/COLOR]' , 'metadata.' : '[COLOR cyan][METADATA] [/COLOR]' , 'module.' : '[COLOR orange][MODULE] [/COLOR]' , 'plugin.' : '[COLOR blue][PLUGIN] [/COLOR]' , 'program.' : '[COLOR orange][PROGRAM] [/COLOR]' , 'repository.' : '[COLOR gold][REPO] [/COLOR]' , 'script.' : '[COLOR green][SCRIPT] [/COLOR]' , 'service.' : '[COLOR green][SERVICE] [/COLOR]' , 'skin.' : '[COLOR dodgerblue][SKIN] [/COLOR]' , 'video.' : '[COLOR orange][VIDEO] [/COLOR]' , 'weather.' : '[COLOR yellow][WEATHER] [/COLOR]' }
   for ii1 in i1iI1 :
    IIiI1 = IIiI1 . replace ( ii1 , i1iI1 [ ii1 ] )
   if Ii1i1iI in oOOoo0Oo : IIiI1 = '[COLOR green][B][PROTECTED][/B][/COLOR] %s' % IIiI1
   else : IIiI1 = '[COLOR red][B][REMOVE][/B][/COLOR] %s' % IIiI1
   ii1I ( ' %s' % IIiI1 , 'removedata' , Ii1i1iI , icon = oooOo0OOOoo0 , fanart = OOoO , themeit = O00OOOoOoo0O )
 else :
  ii1I ( 'No Addon data folder found.' , '' , themeit = O000OOo00oo )
  if 16 - 16: II1I11Ii1 % I1iI1iIi111i . oo0o
  if 59 - 59: iiIIiiIi1Ii11 * O0ooO0Oo00o . ooo0
  if 56 - 56: oo0o - IIii11I1 % iiIIiiIi1Ii11 - IIiiIiII1Ii
def Oo00O ( ) :
 Iii1I1I11iiI1 ( 'Backup Restore' , 'bre' , icon = I1i1iiI1 , themeit = ooo00OOOooO )
 ii1I ( 'Convert Paths to special' , 'convertpath' , icon = I1i1iiI1 , themeit = ooo00OOOooO )
 ii1I ( 'Test Notifications' , 'testnotify' , icon = I1i1iiI1 , themeit = ooo00OOOooO )
 if 12 - 12: IIiiIiII1Ii - i1I * Ii
 if 14 - 14: Oo0 - oo0o % oo0o * ooo0 . i11iIiiIii / ooo0
 if 79 - 79: IIiiIiII1Ii - oOo00oOoO000 + IIiiIiII1Ii . I11I1IIII
 if 28 - 28: I11IiI - IIii11I1
 if 54 - 54: IIii11I1 - ooo0 % iIIIiiI1i1
def Ooii11i11i1 ( name , type , theme = None ) :
 if type == 'gui' :
  if name == o00 :
   Ooo0o00o0o = ooo0OO . yesno ( Oo0Ooo , 'Would you like to apply the guifix for:' , '%s?' % name , nolabel = 'No, Cancel' , yeslabel = 'Yes, Apply Fix' )
  else :
   Ooo0o00o0o = ooo0OO . yesno ( "%s - [COLOR red]WARNING!![/COLOR]" % Oo0Ooo , "%s SpinzTV build is not currently installed." % name , "Would you like to apply the guiFix anyways?." , yeslabel = "Yes, Apply" , nolabel = "No, Cancel" )
  if Ooo0o00o0o :
   IiIIIIIi = wiz . checkBuild ( name , 'gui' )
   IiIi1iIIi1 = name . replace ( '\\' , '' ) . replace ( '/' , '' ) . replace ( ':' , '' ) . replace ( '*' , '' ) . replace ( '?' , '' ) . replace ( '"' , '' ) . replace ( '<' , '' ) . replace ( '>' , '' ) . replace ( '|' , '' )
   if not wiz . workingURL ( IiIIIIIi ) == True : wiz . LogNotify ( Oo0Ooo , 'guiFix: [COLOR red]Invalid Zip Url![/COLOR]' ) ; return
   if not os . path . exists ( IiIi11iIIi1Ii ) : os . makedirs ( IiIi11iIIi1Ii )
   II1 . create ( Oo0Ooo , 'Downloading %s GuiFix' % name , '' , 'Please Wait' )
   O0OoO0ooOO0o = os . path . join ( IiIi11iIIi1Ii , '%s_guisettings.zip' % IiIi1iIIi1 )
   try : os . remove ( O0OoO0ooOO0o )
   except : pass
   downloader . download ( IiIIIIIi , O0OoO0ooOO0o , II1 )
   xbmc . sleep ( 500 )
   II1 . update ( 0 , "" , "Installing %s GuiFix" % name )
   extract . all ( O0OoO0ooOO0o , OOOo0 , II1 )
   II1 . close ( )
   wiz . killxbmc ( )
  else :
   wiz . LogNotify ( Oo0Ooo , 'guiFix: [COLOR red]Cancelled![/COLOR]' )
 elif type == 'fresh' :
  OoOo0oOooOoOO ( name )
 elif type == 'normal' :
  if OOO == 'normal' :
   if iIii1 == 'true' :
    traktit . autoUpdate ( 'all' )
    wiz . setS ( 'traktlastsave' , str ( I11II1i ) )
   if oOOoO0 == 'true' :
    debridit . autoUpdate ( 'all' )
    wiz . setS ( 'debridlastsave' , str ( I11II1i ) )
  if IIIII < 17.0 and float ( wiz . checkBuild ( name , 'kodi' ) ) >= 17.0 :
   Ooo0o00o0o = ooo0OO . yesno ( "%s - [COLOR red]WARNING!![/COLOR]" % Oo0Ooo , 'There is a chance that the skin will not appear correctly' , 'When installing a %s build on a Kodi %s install' % ( wiz . checkBuild ( name , 'kodi' ) , IIIII ) , 'Would you still like to install: %s v%s?' % ( name , wiz . checkBuild ( name , 'version' ) ) , nolabel = 'No, Cancel' , yeslabel = 'Yes, Install' )
  else :
   Ooo0o00o0o = ooo0OO . yesno ( Oo0Ooo , 'By downloading or using you are agreeing that the author takes no resposibility for the content or reliability of any of the addons included.  The author does not host, distribute or have any control over any of the content that may be provided by any addon. It is the users responsibility to ensure the legality of use within their country. By continuing you are agreeing to the terms and conditions herin. Would you still like to install:' , '%s v%s?' % ( name , wiz . checkBuild ( name , 'version' ) ) , nolabel = 'Disagree, Cancel' , yeslabel = 'Agree, Install' )
  if Ooo0o00o0o :
   IiIIIIIi = wiz . checkBuild ( name , 'url' )
   IiIi1iIIi1 = name . replace ( '\\' , '' ) . replace ( '/' , '' ) . replace ( ':' , '' ) . replace ( '*' , '' ) . replace ( '?' , '' ) . replace ( '"' , '' ) . replace ( '<' , '' ) . replace ( '>' , '' ) . replace ( '|' , '' )
   if not wiz . workingURL ( IiIIIIIi ) == True : wiz . LogNotify ( Oo0Ooo , 'Build Install: [COLOR red]Invalid Zip Url![/COLOR]' ) ; return
   if not os . path . exists ( IiIi11iIIi1Ii ) : os . makedirs ( IiIi11iIIi1Ii )
   II1 . create ( Oo0Ooo , 'Downloading %s ' % name , '' , 'Please Wait' )
   O0OoO0ooOO0o = os . path . join ( IiIi11iIIi1Ii , '%s.zip' % IiIi1iIIi1 )
   try : os . remove ( O0OoO0ooOO0o )
   except : pass
   downloader . download ( IiIIIIIi , O0OoO0ooOO0o , II1 )
   xbmc . sleep ( 500 )
   II1 . update ( 0 , "" , "Installing %s " % name )
   oo00ooOoO00 = extract . all ( O0OoO0ooOO0o , O00ooooo00 , II1 )
   o00oOoOo0 , o0O0O0ooo0oOO , oo000 = oo00ooOoO00 . split ( '/' , 3 )
   wiz . setS ( 'buildname' , name )
   wiz . setS ( 'buildversion' , wiz . checkBuild ( name , 'version' ) )
   wiz . setS ( 'buildtheme' , '' )
   wiz . setS ( 'latestversion' , wiz . checkBuild ( name , 'version' ) )
   wiz . setS ( 'lastbuildcheck' , str ( IIIi1I1IIii1II ) )
   wiz . setS ( 'installed' , 'true' )
   wiz . setS ( 'extract' , str ( o00oOoOo0 ) )
   wiz . setS ( 'errors' , str ( o0O0O0ooo0oOO ) )
   wiz . log ( 'INSTALLED %s: [ERRORS:%s]' % ( o00oOoOo0 , o0O0O0ooo0oOO ) )
   if int ( o0O0O0ooo0oOO ) >= 1 :
    iiOoO = ooo0OO . yesno ( Oo0Ooo , 'INSTALLED %s: [ERRORS:%s]' % ( o00oOoOo0 , o0O0O0ooo0oOO ) , 'Would you like to view the errors?' , nolabel = 'No, Cancel' , yeslabel = 'Yes, View' )
    if iiOoO :
     wiz . TextBoxes ( Oo0Ooo , oo000 . replace ( '\t' , '' ) ) ; xbmc . sleep ( 3000 )
   II1 . close ( )
   I1I1i1I = wiz . checkBuild ( name , 'theme' )
   if not I1I1i1I == 'http://' and wiz . workingURL ( I1I1i1I ) == True : Ooii11i11i1 ( name , 'theme' )
   ooo0OO . ok ( Oo0Ooo , "To save changes you now need to force close Kodi, Press OK to force close Kodi" )
   wiz . killxbmc ( )
  else :
   wiz . LogNotify ( Oo0Ooo , 'Build Install: [COLOR red]Cancelled![/COLOR]' )
 elif type == 'theme' :
  if theme == None :
   I1I1i1I = wiz . checkBuild ( name , 'theme' )
   Iiiiii111i1ii = [ ]
   if not I1I1i1I == 'http://' and wiz . workingURL ( I1I1i1I ) == True :
    oOooOOo0o = wiz . openURL ( I1I1i1I ) . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
    O0O0ooOOO = re . compile ( 'name="(.+?)"' ) . findall ( oOooOOo0o )
    if len ( O0O0ooOOO ) > 0 :
     if ooo0OO . yesno ( Oo0Ooo , "The Build [%s] comes with %s different themes" % ( name , len ( O0O0ooOOO ) ) , "Would you like to install one now?" , yeslabel = "Yes, Install" , nolabel = "No Thanks" ) :
      for II1IiiIi1i in O0O0ooOOO :
       Iiiiii111i1ii . append ( II1IiiIi1i )
      wiz . log ( "Theme List: %s " % str ( Iiiiii111i1ii ) )
      i1i1iII1 = ooo0OO . select ( Oo0Ooo , Iiiiii111i1ii )
      wiz . log ( "Theme install selected: %s" % i1i1iII1 )
      if not i1i1iII1 == - 1 : theme = Iiiiii111i1ii [ i1i1iII1 ] ; iii11i1IIII = True
      else : wiz . LogNotify ( Oo0Ooo , 'Theme Install: [COLOR red]Cancelled![/COLOR]' ) ; return
     else : wiz . LogNotify ( Oo0Ooo , 'Theme Install: [COLOR red]Cancelled![/COLOR]' ) ; return
   else : wiz . LogNotify ( Oo0Ooo , 'Theme Install: [COLOR red]None Found![/COLOR]' )
  else : iii11i1IIII = ooo0OO . yesno ( Oo0Ooo , 'Would you like to install the theme:' , theme , 'for %s v%s?' % ( name , wiz . checkBuild ( name , 'version' ) ) , nolabel = 'No, Cancel' , yeslabel = 'Yes, Install' )
  if iii11i1IIII :
   Iio00 = wiz . checkTheme ( name , theme , 'url' )
   IiIi1iIIi1 = name . replace ( '\\' , '' ) . replace ( '/' , '' ) . replace ( ':' , '' ) . replace ( '*' , '' ) . replace ( '?' , '' ) . replace ( '"' , '' ) . replace ( '<' , '' ) . replace ( '>' , '' ) . replace ( '|' , '' )
   if not wiz . workingURL ( Iio00 ) == True : wiz . LogNotify ( Oo0Ooo , 'Theme Install: [COLOR red]Invalid Zip Url![/COLOR]' ) ; return
   if not os . path . exists ( IiIi11iIIi1Ii ) : os . makedirs ( IiIi11iIIi1Ii )
   II1 . create ( Oo0Ooo , 'Downloading %s ' % name , '' , 'Please Wait' )
   O0OoO0ooOO0o = os . path . join ( IiIi11iIIi1Ii , '%s.zip' % IiIi1iIIi1 )
   try : os . remove ( O0OoO0ooOO0o )
   except : pass
   downloader . download ( Iio00 , O0OoO0ooOO0o , II1 )
   xbmc . sleep ( 500 )
   II1 . update ( 0 , "" , "Installing %s " % name )
   oo00ooOoO00 = extract . all ( O0OoO0ooOO0o , O00ooooo00 , II1 )
   o00oOoOo0 , o0O0O0ooo0oOO , oo000 = oo00ooOoO00 . split ( '/' , 3 )
   wiz . setS ( 'buildtheme' , theme )
   wiz . log ( 'INSTALLED %s: [ERRORS:%s]' % ( o00oOoOo0 , o0O0O0ooo0oOO ) )
   II1 . close ( )
   if OOO not in [ "fresh" , "normal" ] : xbmc . executebuiltin ( "ReloadSkin()" ) ; xbmc . sleep ( 1000 ) ; xbmc . executebuiltin ( "Container.Refresh" )
  else :
   wiz . LogNotify ( Oo0Ooo , 'Theme Install: [COLOR red]Cancelled![/COLOR]' )
   if 34 - 34: I1I1II1I11
   if 17 - 17: Oo0 % iIIIiiI1i1 . I11IiI / i1IIi
   if 28 - 28: I11I1IIII . O0ooO0Oo00o / IiII111iI1ii1 + O0ooO0Oo00o . i1IIi . II1I11Ii1
   if 53 - 53: oo0o % oo0o * IIiiIiII1Ii + I1I1II1I11
def Oooo00 ( apk , url ) :
 if wiz . platform ( ) == 'android' :
  if apk in [ 'kodi' , 'spmc' ] :
   iiOoO = ooo0OO . yesno ( Oo0Ooo , "Would you like to download and install:" , "%s (v%s)" % ( apk . upper ( ) , wiz . latestApk ( apk , 'version' ) ) )
   if not iiOoO : wiz . LogNotify ( Oo0Ooo , '[COLOR red]ERROR:[/COLOR] Install Cancelled' ) ; return
   I111iIi1 = "%s v%s" % ( apk . upper ( ) , wiz . latestApk ( apk , 'version' ) )
  else :
   iiOoO = ooo0OO . yesno ( Oo0Ooo , "Would you like to download and install:" , "%s" % apk )
   if not iiOoO : wiz . LogNotify ( Oo0Ooo , '[COLOR red]ERROR:[/COLOR] Install Cancelled' ) ; return
   I111iIi1 = apk
  if iiOoO :
   if not os . path . exists ( IiIi11iIIi1Ii ) : os . makedirs ( IiIi11iIIi1Ii )
   if not wiz . workingURL ( url ) == True : wiz . LogNotify ( Oo0Ooo , 'APK Installer: [COLOR red]Invalid Apk Url![/COLOR]' ) ; return
   II1 . create ( Oo0Ooo , 'Downloading %s' % I111iIi1 , '' , 'Please Wait' )
   O0OoO0ooOO0o = os . path . join ( IiIi11iIIi1Ii , "%s.apk" % apk )
   try : os . remove ( O0OoO0ooOO0o )
   except : pass
   downloader . download ( url , O0OoO0ooOO0o , II1 )
   xbmc . sleep ( 500 )
   II1 . close ( )
   ooo0OO . ok ( Oo0Ooo , "Launching the APK to be installed" , "Follow the install process to complete." )
   xbmc . executebuiltin ( 'StartAndroidActivity("","android.intent.action.VIEW","application/vnd.android.package-archive","file:' + O0OoO0ooOO0o + '")' )
  else : wiz . LogNotify ( Oo0Ooo , '[COLOR red]ERROR:[/COLOR] Install Cancelled' )
 else : wiz . LogNotify ( Oo0Ooo , '[COLOR red]ERROR:[/COLOR] None Android Device' )
 if 92 - 92: i1I
 if 22 - 22: Oo0 % IIii11I1 * IiII111iI1ii1 / iIIIiiI1i1 % i11iIiiIii * oOo00oOoO000
 if 95 - 95: i1IIi - II1I11Ii1 * iiIIiiIi1Ii11 + I1I1II1I11
 if 10 - 10: IIiiIiII1Ii / i11iIiiIii
 if 92 - 92: oOo00oOoO000 . Ii
def oOO00O0Ooooo00 ( ver ) :
 if ver == '15' : wiz . setS ( 'show15' , 'true' if oOOoo00O0O == 'false' else 'false' )
 elif ver == '16' : wiz . setS ( 'show16' , 'true' if i1111 == 'false' else 'false' )
 xbmc . executebuiltin ( 'Container.Refresh' )
 if 97 - 97: i1I / Ii % I11IiI % IiII111iI1ii1
def ii111I11iI ( part , whole ) :
 return 100 * float ( part ) / float ( whole )
 if 93 - 93: IiII111iI1ii1 / I1iI1iIi111i * I11IiI % i1IIi * ooo0 * oOo00oOoO000
def iiIiI1i1 ( type , name ) :
 if type == 'trakt' :
  Ooooooo = [ ]
  I1IIIiI1I1ii1 = urllib . quote_plus ( name . lower ( ) . replace ( ' ' , '' ) )
  Ooooooo . append ( ( O00OOOoOoo0O % name , ' ' ) )
  Ooooooo . append ( ( O00OOOoOoo0O % 'Save Trakt Data' , 'RunPlugin(plugin://%s/?mode=savetrakt&name=%s)' % ( OO0o , I1IIIiI1I1ii1 ) ) )
  Ooooooo . append ( ( O00OOOoOoo0O % 'Restore Trakt Data' , 'RunPlugin(plugin://%s/?mode=restoretrakt&name=%s)' % ( OO0o , I1IIIiI1I1ii1 ) ) )
  Ooooooo . append ( ( O00OOOoOoo0O % 'Clear Trakt Data' , 'RunPlugin(plugin://%s/?mode=cleartrakt&name=%s)' % ( OO0o , I1IIIiI1I1ii1 ) ) )
 if type == 'traktaddon' :
  Ooooooo = [ ]
  I1IIIiI1I1ii1 = urllib . quote_plus ( name . lower ( ) . replace ( ' ' , '' ) )
  Ooooooo . append ( ( O00OOOoOoo0O % name , ' ' ) )
  Ooooooo . append ( ( O00OOOoOoo0O % 'Register Trakt' , 'RunPlugin(plugin://%s/?mode=authtrakt&name=%s)' % ( OO0o , I1IIIiI1I1ii1 ) ) )
  Ooooooo . append ( ( O00OOOoOoo0O % 'Save Trakt Data' , 'RunPlugin(plugin://%s/?mode=savetrakt&name=%s)' % ( OO0o , I1IIIiI1I1ii1 ) ) )
  Ooooooo . append ( ( O00OOOoOoo0O % 'Restore Trakt Data' , 'RunPlugin(plugin://%s/?mode=restoretrakt&name=%s)' % ( OO0o , I1IIIiI1I1ii1 ) ) )
  Ooooooo . append ( ( O00OOOoOoo0O % 'Clear Addon Trakt Data' , 'RunPlugin(plugin://%s/?mode=addontrakt&name=%s)' % ( OO0o , I1IIIiI1I1ii1 ) ) )
 if type == 'debrid' :
  Ooooooo = [ ]
  I1IIIiI1I1ii1 = urllib . quote_plus ( name . lower ( ) . replace ( ' ' , '' ) )
  Ooooooo . append ( ( O00OOOoOoo0O % name , ' ' ) )
  Ooooooo . append ( ( O00OOOoOoo0O % 'Save Real Debrid Data' , 'RunPlugin(plugin://%s/?mode=savedebrid&name=%s)' % ( OO0o , I1IIIiI1I1ii1 ) ) )
  Ooooooo . append ( ( O00OOOoOoo0O % 'Restore Real Debrid Data' , 'RunPlugin(plugin://%s/?mode=restoredebrid&name=%s)' % ( OO0o , I1IIIiI1I1ii1 ) ) )
  Ooooooo . append ( ( O00OOOoOoo0O % 'Clear Real Debrid Data' , 'RunPlugin(plugin://%s/?mode=cleardebrid&name=%s)' % ( OO0o , I1IIIiI1I1ii1 ) ) )
 if type == 'debridaddon' :
  Ooooooo = [ ]
  I1IIIiI1I1ii1 = urllib . quote_plus ( name . lower ( ) . replace ( ' ' , '' ) )
  Ooooooo . append ( ( O00OOOoOoo0O % name , ' ' ) )
  Ooooooo . append ( ( O00OOOoOoo0O % 'Register Real Debrid' , 'RunPlugin(plugin://%s/?mode=authdebrid&name=%s)' % ( OO0o , I1IIIiI1I1ii1 ) ) )
  Ooooooo . append ( ( O00OOOoOoo0O % 'Save Real Debrid Data' , 'RunPlugin(plugin://%s/?mode=savedebrid&name=%s)' % ( OO0o , I1IIIiI1I1ii1 ) ) )
  Ooooooo . append ( ( O00OOOoOoo0O % 'Restore Real Debrid Data' , 'RunPlugin(plugin://%s/?mode=restoredebrid&name=%s)' % ( OO0o , I1IIIiI1I1ii1 ) ) )
  Ooooooo . append ( ( O00OOOoOoo0O % 'Clear Addon Real Debrid Data' , 'RunPlugin(plugin://%s/?mode=addondebrid&name=%s)' % ( OO0o , I1IIIiI1I1ii1 ) ) )
 if type == 'install' :
  Ooooooo = [ ]
  I1IIIiI1I1ii1 = urllib . quote_plus ( name )
  Ooooooo . append ( ( O00OOOoOoo0O % name , ' ' ) )
  Ooooooo . append ( ( O00OOOoOoo0O % 'Fresh Install' , 'RunPlugin(plugin://%s/?mode=install&name=%s&url=fresh)' % ( OO0o , I1IIIiI1I1ii1 ) ) )
  Ooooooo . append ( ( O00OOOoOoo0O % 'Normal Install Use On Updates' , 'RunPlugin(plugin://%s/?mode=install&name=%s&url=normal)' % ( OO0o , I1IIIiI1I1ii1 ) ) )
  Ooooooo . append ( ( O00OOOoOoo0O % 'Apply guiFix' , 'RunPlugin(plugin://%s/?mode=install&name=%s&url=gui)' % ( OO0o , I1IIIiI1I1ii1 ) ) )
 Ooooooo . append ( ( O00OOOoOoo0O % 'SpinzTV Settings' , 'RunPlugin(plugin://%s/?mode=settings)' % OO0o ) )
 return Ooooooo
 if 30 - 30: ooo0 * i1IIi
def I1iIIIi1 ( ) :
 IiiI1iiiiI1iI = wiz . log_check ( )
 iIiiiii1i = IiiI1iiiiI1iI . replace ( I1IiiI , "" )
 if os . path . exists ( IiiI1iiiiI1iI ) or not IiiI1iiiiI1iI == False :
  iiIi1IIiI = open ( IiiI1iiiiI1iI , mode = 'r' ) ; i1oO0OO0 = iiIi1IIiI . read ( ) ; iiIi1IIiI . close ( )
  wiz . TextBoxes ( "%s - %s" % ( Oo0Ooo , iIiiiii1i ) , i1oO0OO0 )
 else :
  wiz . LogNotify ( 'View Log' , 'No Log File Found!' )
  if 82 - 82: II1I11Ii1 - II1I11Ii1 + I1I1II1I11
def II111Ii1i1 ( ) :
 if os . path . exists ( o0oO0 ) :
  iiIi1IIiI = open ( o0oO0 , mode = 'r' ) ; i1oO0OO0 = iiIi1IIiI . read ( ) ; iiIi1IIiI . close ( )
  wiz . TextBoxes ( "%s - Wizard.log" % Oo0Ooo , i1oO0OO0 )
 else :
  wiz . LogNotify ( 'View Log' , 'Wizard.log not found!' )
  if 98 - 98: oo . oo * I11I1IIII * O0ooO0Oo00o * Ii
def oOooO0 ( addon ) :
 if ooo0OO . yesno ( Oo0Ooo , 'Are you sure you want to delete the addon:' , '[COLOR yellow]%s[/COLOR]' % addon , yeslabel = 'Yes, Remove' , nolabel = 'No, Cancel' ) :
  wiz . cleanHouse ( os . path . join ( oO00oOo , addon ) )
  OOOoO000 ( addon )
  wiz . LogNotify ( 'Remove Addon' , 'Complete!' )
  ooo0OO . ok ( Oo0Ooo , 'The addon has been removed but will remain in the addons list until the next time you reload Kodi.' )
 else : wiz . LogNotify ( 'Remove Addon' , 'Cancelled!' )
 xbmc . executebuiltin ( 'Container.Refresh' )
 if 57 - 57: O0ooO0Oo00o
def OOOoO000 ( addon ) :
 if addon == 'all' :
  if ooo0OO . yesno ( Oo0Ooo , 'Would you like to remove ALL addon data stored in you Userdata folder?' , yeslabel = 'Yes, Remove' , nolabel = 'No, Cancel' ) :
   wiz . cleanHouse ( Oo0O )
  else : wiz . LogNotify ( 'Remove Addon Data' , 'Cancelled!' )
 elif addon == 'uninstalled' :
  if ooo0OO . yesno ( Oo0Ooo , 'Would you like to remove ALL addon data stored in you Userdata folder for uninstalled addons?' , yeslabel = 'Yes, Remove' , nolabel = 'No, Cancel' ) :
   oOOOoo = 0
   for iIIIII1ii1I in glob . glob ( os . path . join ( Oo0O , '*' ) ) :
    Ii1i1iI = iIIIII1ii1I . replace ( Oo0O , '' ) . replace ( '\\' , '' ) . replace ( '/' , '' )
    if Ii1i1iI in oOOoo0Oo : pass
    elif os . path . exists ( os . path . join ( oO00oOo , Ii1i1iI ) ) : pass
    else : wiz . cleanHouse ( iIIIII1ii1I ) ; oOOOoo += 1 ; wiz . log ( iIIIII1ii1I ) ; shutil . rmtree ( iIIIII1ii1I )
   wiz . LogNotify ( 'Clean up Uninstalled' , '[COLOR yellow]%s[/COLOR] Folders(s) Removed' % oOOOoo )
  else : wiz . LogNotify ( 'Remove Addon Data' , 'Cancelled!' )
 elif addon == 'empty' :
  if ooo0OO . yesno ( Oo0Ooo , 'Would you like to remove ALL empty addon data folders in you Userdata folder?' , yeslabel = 'Yes, Remove' , nolabel = 'No, Cancel' ) :
   oOOOoo = wiz . emptyfolder ( Oo0O )
   wiz . LogNotify ( 'Remove Empty Folders' , '[COLOR yellow]%s[/COLOR] Folders(s) Removed' % oOOOoo )
  else : wiz . LogNotify ( 'Remove Empty Folders' , 'Cancelled!' )
 else :
  Ii1ii111i1 = os . path . join ( OOOo0 , 'addon_data' , addon )
  if addon in oOOoo0Oo :
   wiz . LogNotify ( "Protected Plugin" , "Not allowed to remove Addon_Data" )
  elif os . path . exists ( Ii1ii111i1 ) :
   if ooo0OO . yesno ( Oo0Ooo , 'Would you also like to remove the addon data for:' , '[COLOR yellow]%s[/COLOR]' % addon , yeslabel = 'Yes, Remove' , nolabel = 'No, Cancel' ) :
    wiz . cleanHouse ( Ii1ii111i1 )
    try :
     shutil . rmtree ( Ii1ii111i1 )
    except :
     wiz . log ( "Error deleting: %s" % Ii1ii111i1 )
   else :
    wiz . log ( 'Addon data for %s was not removed' % addon )
 xbmc . executebuiltin ( 'Container.Refresh' )
 if 31 - 31: iIIIiiI1i1 + ooo0
 if 87 - 87: i1I
 if 45 - 45: oo / i1IIi - IIii11I1 / oo0o % II1I11Ii1
 if 83 - 83: iiIIiiIi1Ii11 . I1iI1iIi111i - II1I11Ii1 * i11iIiiIii
 if 20 - 20: I11IiI * Ii + O0ooO0Oo00o % IIiiIiII1Ii % I11I1IIII
def OoOo0oOooOoOO ( install = None ) :
 if iIii1 == 'true' :
  traktit . autoUpdate ( 'all' )
  wiz . setS ( 'traktlastsave' , str ( I11II1i ) )
 if oOOoO0 == 'true' :
  debridit . autoUpdate ( 'all' )
  wiz . setS ( 'debridlastsave' , str ( I11II1i ) )
 if oo00 not in [ 'skin.confluence' ] :
  iIi1II = 'skin.confluence'
  iiOoO = ooo0OO . yesno ( Oo0Ooo , "The skin needs to be set back to [COLOR yellow]%s[/COLOR]" % iIi1II [ 5 : ] , "Before doing a fresh install to clear all Texture files!" , "Would you like us to do that for you?" , nolabel = "No, Thanks" , yeslabel = "Yes, Swap Skin" ) ;
  if iiOoO :
   skinSwitch . swapSkins ( iIi1II )
   while not xbmc . getCondVisibility ( "Window.isVisible(yesnodialog)" ) :
    xbmc . sleep ( 200 )
   xbmc . executebuiltin ( "Action(Left)" )
   xbmc . executebuiltin ( "Action(Select)" )
  else : wiz . LogNotify ( Oo0Ooo , 'Fresh Install: [COLOR red]Cancelled![/COLOR]' ) ; return
 if install : Ooo0o00o0o = ooo0OO . yesno ( Oo0Ooo , "Do you wish to restore your" , "Kodi configuration to default settings" , "Before installing %s?" % install , nolabel = 'No, Cancel' , yeslabel = 'Yes, Continue' )
 else : Ooo0o00o0o = ooo0OO . yesno ( Oo0Ooo , "Do you wish to restore your" , "Kodi configuration to default settings?" , nolabel = 'No, Cancel' , yeslabel = 'Yes, Continue' )
 if Ooo0o00o0o :
  I1iIiI11I1 = os . path . abspath ( O00ooooo00 )
  II1 . create ( Oo0Ooo , "Clearing all files and folders:" , '' , '' )
  i1oOOoo0o0OOOO = sum ( [ len ( i1IiII1III ) for i1O00oo , O0OO00O0oOO , i1IiII1III in os . walk ( I1iIiI11I1 ) ] ) ; Ii1iI111 = 0 ;
  try :
   for O0oooo00o0Oo , I1iii , i1IiII1III in os . walk ( I1iIiI11I1 , topdown = True ) :
    I1iii [ : ] = [ O0OO00O0oOO for O0OO00O0oOO in I1iii if O0OO00O0oOO not in oOOoo0Oo ]
    for iIiIi11 in i1IiII1III :
     Ii1iI111 += 1
     oO0o0O0Ooo0o = O0oooo00o0Oo . split ( '\\' )
     i1Ii11II = len ( oO0o0O0Ooo0o ) - 1
     if iIiIi11 == 'sources.xml' and oO0o0O0Ooo0o [ i1Ii11II ] == 'userdata' and ii11iIi1I == 'true' : wiz . log ( "Keep Sources: %s\\%s" % ( O0oooo00o0Oo , iIiIi11 ) )
     elif iIiIi11 == 'favourites.xml' and oO0o0O0Ooo0o [ i1Ii11II ] == 'userdata' and i1iiIII111ii == 'true' : wiz . log ( "Keep Favourites: %s\\%s" % ( O0oooo00o0Oo , iIiIi11 ) )
     elif iIiIi11 == 'profiles.xml' and oO0o0O0Ooo0o [ i1Ii11II ] == 'userdata' and iI111I11I1I1 == 'true' : wiz . log ( "Keep Profiles: %s\\%s" % ( O0oooo00o0Oo , iIiIi11 ) )
     elif iIiIi11 == 'advancedsettings.xml' and oO0o0O0Ooo0o [ i1Ii11II ] == 'userdata' and OOooO0OOoo == 'true' : wiz . log ( "Keep Advanced Settings: %s\\%s" % ( O0oooo00o0Oo , iIiIi11 ) )
     elif iIiIi11 in [ 'xbmc.log' , 'kodi.log' , 'spmc.log' , 'tvmc.log' ] : wiz . log ( "Keep Log File: %s" % iIiIi11 )
     elif iIiIi11 . endswith ( '.db' ) :
      try : os . remove ( os . path . join ( O0oooo00o0Oo , iIiIi11 ) )
      except : wiz . log ( 'Failed to delete, Purging DB.' ) ; wiz . purgeDb ( os . path . join ( O0oooo00o0Oo , iIiIi11 ) )
     else :
      II1 . update ( int ( ii111I11iI ( Ii1iI111 , i1oOOoo0o0OOOO ) ) , '' , 'File: [COLOR yellow]%s[/COLOR]' % iIiIi11 , '' )
      try : os . remove ( os . path . join ( O0oooo00o0Oo , iIiIi11 ) )
      except : wiz . log ( "Error removing %s\\%s" % ( O0oooo00o0Oo , iIiIi11 ) )
   for O0oooo00o0Oo , I1iii , i1IiII1III in os . walk ( I1iIiI11I1 , topdown = True ) :
    I1iii [ : ] = [ O0OO00O0oOO for O0OO00O0oOO in I1iii if O0OO00O0oOO not in oOOoo0Oo ]
    for iIiIi11 in I1iii :
     II1 . update ( 100 , '' , 'Cleaning Up Empty Folder: [COLOR yellow]%s[/COLOR]' % iIiIi11 , '' )
     if iIiIi11 not in [ "Database" , "userdata" , "temp" , "addons" , "addon_data" ] :
      shutil . rmtree ( os . path . join ( O0oooo00o0Oo , iIiIi11 ) , ignore_errors = True , onerror = None )
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
   Ooii11i11i1 ( install , 'normal' )
  else :
   ooo0OO . ok ( Oo0Ooo , "The process is complete, you're now back to a fresh Kodi configuration with SpinzTV Wizard" , "Please reboot your system or restart Kodi in order for the changes to be applied." )
   wiz . killxbmc ( )
 else : wiz . LogNotify ( Oo0Ooo , 'Fresh Install: [COLOR red]Cancelled![/COLOR]' ) ; xbmc . executebuiltin ( 'Container.Refresh' )
 if 18 - 18: O0ooO0Oo00o . i1IIi % I1I1II1I11 % oo0o
 if 9 - 9: oo - Oo0 * i1IIi . Oo0
 if 2 - 2: i1IIi % iIIIiiI1i1
 if 63 - 63: iiIIiiIi1Ii11 % I1iI1iIi111i
def I1ii ( ) :
 if ooo0OO . yesno ( Oo0Ooo , 'Would you like to clear cache?' , nolabel = 'Cancel' , yeslabel = 'Delete' ) :
  wiz . clearCache ( )
  O00O0O ( )
  if 19 - 19: oo * oOo00oOoO000 / oOo00oOoO000 . i1IIi - iIIIiiI1i1 + i11iIiiIii
def O00O0O ( ) :
 oo0OOo0O = wiz . latestDB ( 'Textures' )
 if ooo0OO . yesno ( Oo0Ooo , "Would you like to delete the %s and Thumbnails folder?" % oo0OOo0O , "They will repopulate on startup" , nolabel = 'No, Cancel' , yeslabel = 'Yes, Remove' ) :
  try : wiz . removeFile ( os . join ( i1i1II , oo0OOo0O ) )
  except : wiz . log ( 'Failed to delete, Purging DB.' ) ; wiz . purgeDb ( oo0OOo0O )
  wiz . removeFolder ( iI1Ii11111iIi )
  wiz . killxbmc ( )
 else : wiz . log ( 'Clear thumbnames cancelled' )
 if 39 - 39: i1IIi + I11I1IIII % iIIIiiI1i1 / iIIIiiI1i1
def I1i ( ) :
 ooo = [ ] ; I111iIi1 = [ ]
 for ii1iiIi1 , i111iiI1ii , i1IiII1III in os . walk ( O00ooooo00 ) :
  for iiIi1IIiI in fnmatch . filter ( i1IiII1III , '*.db' ) :
   if iiIi1IIiI != 'Thumbs.db' :
    IIiii = os . path . join ( ii1iiIi1 , iiIi1IIiI )
    ooo . append ( IIiii )
    dir = IIiii . replace ( '\\' , '/' ) . split ( '/' )
    I111iIi1 . append ( '(%s) %s' % ( dir [ len ( dir ) - 2 ] , dir [ len ( dir ) - 1 ] ) )
 if IIIII >= 16 :
  I1i1i = ooo0OO . multiselect ( "Select DB File to Purge" , I111iIi1 )
  if I1i1i == None : wiz . LogNotify ( "Purge Database" , "Cancelled" )
  elif len ( I1i1i ) == 0 : wiz . LogNotify ( "Purge Database" , "Cancelled" )
  else :
   for OOOOooO0oO00O0o in I1i1i : wiz . purgeDb ( ooo [ OOOOooO0oO00O0o ] )
 else :
  I1i1i = ooo0OO . select ( "Select DB File to Purge" , I111iIi1 )
  if I1i1i == - 1 : wiz . LogNotify ( "Purge Database" , "Cancelled" )
  else : wiz . purgeDb ( ooo [ OOOOooO0oO00O0o ] )
  if 70 - 70: Ii
  if 16 - 16: IIii11I1 - i1IIi % Oo0
  if 36 - 36: iIIIiiI1i1
  if 84 - 84: Ii . oo . O0ooO0Oo00o . oOo00oOoO000 / oo0o % IiII111iI1ii1
def OOO0oOoO0O ( ) :
 OOO = wiz . workingURL ( O0 )
 if OOO == True :
  oOooOOo0o = wiz . openURL ( O0 ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
  id , i1oO0OO0 = oOooOOo0o . split ( '|||' )
  notify . TestNotification ( msg = i1oO0OO0 , title = oooooOoo0ooo , BorderWidth = 10 )
 else : wiz . LogNotify ( Oo0Ooo , "Invalid URL for Notification" )
 if 84 - 84: ooo0 * i1IIi - II1I11Ii1 * II1I11Ii1
def i1ii ( ) :
 if oOOo0 == 'No' : ii1I ( '==============BackUp Options===============' , '' , themeit = O000OOo00oo )
 ii1I ( 'Full Backup' , 'full' , icon = I1i1iiI1 , themeit = ooo00OOOooO )
 ii1I ( 'Backup for Builds (Exc: Thumbnails, Databases)' , 'backb' , icon = I1i1iiI1 , themeit = ooo00OOOooO )
 ii1I ( 'Backup addon data' , 'backad' , icon = I1i1iiI1 , themeit = ooo00OOOooO )
 if oOOo0 == 'No' : ii1I ( '==============Restore Options===============' , '' , themeit = O000OOo00oo )
 Iii1I1I11iiI1 ( 'Restore Full Backup' , 'refull' , icon = I1i1iiI1 , themeit = ooo00OOOooO )
 Iii1I1I11iiI1 ( 'Restore Addon Data' , 'refull' , icon = I1i1iiI1 , themeit = ooo00OOOooO )
 if oOOo0 == 'No' : ii1I ( '==============Other Options===============' , '' , themeit = O000OOo00oo )
 Iii1I1I11iiI1 ( 'Delete A Backup' , 'delbu' , icon = I1i1iiI1 , themeit = ooo00OOOooO )
 ii1I ( 'Delete All Backups' , 'delall' , icon = I1i1iiI1 , themeit = ooo00OOOooO )
 ii1I ( 'Select Backup Location' , 'settings' , icon = I1i1iiI1 , themeit = ooo00OOOooO )
 if 65 - 65: I1I1II1I11 / oo % II1I11Ii1
 if 45 - 45: I1I1II1I11
 if 66 - 66: oo
 if 56 - 56: ooo0
 if 61 - 61: IIiiIiII1Ii / iIIIiiI1i1 / Oo0 * ooo0
 if 23 - 23: I11I1IIII - iIIIiiI1i1 + oOo00oOoO000
def Iii1I1I11iiI1 ( display , mode , name = None , url = None , menu = None , overwrite = True , fanart = O0oo0OO0 , icon = I1i1iiI1 , themeit = None ) :
 II11 = '%s?mode=%s' % ( sys . argv [ 0 ] , urllib . quote_plus ( mode ) )
 if not name == None : II11 += "&name=" + urllib . quote_plus ( name )
 if not url == None : II11 += "&url=" + urllib . quote_plus ( url )
 Iiii11iIi1 = True
 if themeit : display = themeit % display
 i1iI11I1II1 = xbmcgui . ListItem ( display , iconImage = "DefaultFolder.png" , thumbnailImage = icon )
 i1iI11I1II1 . setInfo ( type = "Video" , infoLabels = { "Title" : display , "Plot" : Oo0Ooo } )
 i1iI11I1II1 . setProperty ( "Fanart_Image" , fanart )
 if not menu == None : i1iI11I1II1 . addContextMenuItems ( menu , replaceItems = overwrite )
 Iiii11iIi1 = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = II11 , listitem = i1iI11I1II1 , isFolder = True )
 return Iiii11iIi1
 if 14 - 14: i11iIiiIii - IIii11I1 * I1I1II1I11
def ii1I ( display , mode , name = None , url = None , menu = None , overwrite = True , fanart = O0oo0OO0 , icon = I1i1iiI1 , themeit = None ) :
 II11 = '%s?mode=%s' % ( sys . argv [ 0 ] , urllib . quote_plus ( mode ) )
 if not name == None : II11 += "&name=" + urllib . quote_plus ( name )
 if not url == None : II11 += "&url=" + urllib . quote_plus ( url )
 Iiii11iIi1 = True
 if themeit : display = themeit % display
 i1iI11I1II1 = xbmcgui . ListItem ( display , iconImage = "DefaultFolder.png" , thumbnailImage = icon )
 i1iI11I1II1 . setInfo ( type = "Video" , infoLabels = { "Title" : display , "Plot" : Oo0Ooo } )
 i1iI11I1II1 . setProperty ( "Fanart_Image" , fanart )
 if not menu == None : i1iI11I1II1 . addContextMenuItems ( menu , replaceItems = overwrite )
 Iiii11iIi1 = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = II11 , listitem = i1iI11I1II1 , isFolder = False )
 return Iiii11iIi1
 if 51 - 51: IiII111iI1ii1 / I1iI1iIi111i % I11I1IIII + IIiiIiII1Ii * i1I + Ii
def o0OoO00o0000O ( name , url , mode , iconimage , fanart , description ) :
 II11 = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&fanart=" + urllib . quote_plus ( fanart )
 Iiii11iIi1 = True
 i1iI11I1II1 = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 i1iI11I1II1 . setInfo ( type = "Video" , infoLabels = { "Title" : name } )
 i1iI11I1II1 . setProperty ( "Fanart_Image" , fanart )
 Iiii11iIi1 = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = II11 , listitem = i1iI11I1II1 , isFolder = False )
 return Iiii11iIi1
 if 21 - 21: iiIIiiIi1Ii11 / i1I % i1I - IIiiIiII1Ii
def oOO ( name , url , mode , iconimage , fanart , description ) :
 II11 = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart ) + "&description=" + urllib . quote_plus ( description )
 Iiii11iIi1 = True
 i1iI11I1II1 = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 i1iI11I1II1 . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description } )
 i1iI11I1II1 . setProperty ( "Fanart_Image" , fanart )
 if mode == 90 :
  Iiii11iIi1 = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = II11 , listitem = i1iI11I1II1 , isFolder = False )
 else :
  Iiii11iIi1 = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = II11 , listitem = i1iI11I1II1 , isFolder = True )
 return Iiii11iIi1
 if 58 - 58: oOo00oOoO000 + O0ooO0Oo00o * IIii11I1 * i11iIiiIii - I1iI1iIi111i
 if 68 - 68: i1IIi % O0ooO0Oo00o
def Ii1i1i1111 ( ) :
 o0oO0O00oOo = [ ]
 I1111I1II11 = sys . argv [ 2 ]
 if len ( I1111I1II11 ) >= 2 :
  iiiIIIIiIi = sys . argv [ 2 ]
  IiiIIIII1iii = iiiIIIIiIi . replace ( '?' , '' )
  if ( iiiIIIIiIi [ len ( iiiIIIIiIi ) - 1 ] == '/' ) :
   iiiIIIIiIi = iiiIIIIiIi [ 0 : len ( iiiIIIIiIi ) - 2 ]
  IIiiii = IiiIIIII1iii . split ( '&' )
  o0oO0O00oOo = { }
  for iI111i1I1II in range ( len ( IIiiii ) ) :
   O00OO = { }
   O00OO = IIiiii [ iI111i1I1II ] . split ( '=' )
   if ( len ( O00OO ) ) == 2 :
    o0oO0O00oOo [ O00OO [ 0 ] ] = O00OO [ 1 ]
    if 29 - 29: Oo0 % oo % II1I11Ii1 . IIiiIiII1Ii / i1IIi * i1I
  return o0oO0O00oOo
  if 54 - 54: ooo0
iiiIIIIiIi = Ii1i1i1111 ( )
OOO = None
iIiIi11 = None
OOoO000O00oO = None
if 34 - 34: ooo0
try : OOoO000O00oO = urllib . unquote_plus ( iiiIIIIiIi [ "mode" ] )
except : pass
try : iIiIi11 = urllib . unquote_plus ( iiiIIIIiIi [ "name" ] )
except : pass
try : OOO = urllib . unquote_plus ( iiiIIIIiIi [ "url" ] )
except : pass
if 80 - 80: I11IiI - Oo0 / oo - i11iIiiIii
wiz . log ( '[ Version : \'%s\' ] [ Mode : \'%s\' ] [ Name : \'%s\' ] [ Url : \'%s\' ]' % ( iiiii , OOoO000O00oO if not OOoO000O00oO == '' else None , iIiIi11 , OOO ) )
def OO0O0o0o0 ( ) :
 if 31 - 31: oo0o
 for file in os . listdir ( I11i11Ii ) :
  if file . endswith ( ".zip" ) :
   OOO = xbmc . translatePath ( os . path . join ( I11i11Ii , file ) )
   o0OoO00o0000O ( file , OOO , 'read' , I1i1iiI1 , I1i1iiI1 , '' )
   if 44 - 44: I1I1II1I11 - I1iI1iIi111i - Oo0
def Oo0000O0OOooO ( ) :
 O00OOOo0 = xbmc . translatePath ( os . path . join ( 'special://' , 'home' ) )
 for file in os . listdir ( I11i11Ii ) :
  if file . endswith ( ".zip" ) :
   OOO = xbmc . translatePath ( os . path . join ( I11i11Ii , file ) )
   oOO ( file , OOO , 'dell' , I1i1iiI1 , I1i1iiI1 , '' )
   if 20 - 20: II1I11Ii1 % II1I11Ii1
   if 94 - 94: IIiiIiII1Ii + ooo0 / oOo00oOoO000 . iiIIiiIi1Ii11 + iIIIiiI1i1 . I1iI1iIi111i
def O0oO0 ( content , viewType ) :
 if content :
  xbmcplugin . setContent ( int ( sys . argv [ 1 ] ) , content )
 if wiz . getS ( 'auto-view' ) == 'true' :
  xbmc . executebuiltin ( "Container.SetViewMode(%s)" % wiz . getS ( viewType ) )
  if 62 - 62: I1I1II1I11 / iiIIiiIi1Ii11 - IiII111iI1ii1 - iiIIiiIi1Ii11 + i11iIiiIii + I11IiI
if OOoO000O00oO == None : I1IiiiiI ( )
if 23 - 23: IIii11I1 + oOo00oOoO000 . I1I1II1I11 * iiIIiiIi1Ii11 + IiII111iI1ii1
elif OOoO000O00oO == 'builds' : i1I11 ( )
elif OOoO000O00oO == 'showupdate' : oOO00O0Ooooo00 ( iIiIi11 )
elif OOoO000O00oO == 'viewbuild' : oOOo0O00o ( iIiIi11 )
elif OOoO000O00oO == 'install' : Ooii11i11i1 ( iIiIi11 , OOO )
elif OOoO000O00oO == 'theme' : Ooii11i11i1 ( iIiIi11 , OOoO000O00oO , OOO )
if 18 - 18: II1I11Ii1 * IIiiIiII1Ii . II1I11Ii1 / ooo0
elif OOoO000O00oO == 'maint' : OooOo ( )
elif OOoO000O00oO == 'speed' : IIii1111 ( )
elif OOoO000O00oO == 'speedtest' : speedtest . runtest ( OOO )
elif OOoO000O00oO == 'clearcache' : I1ii ( )
elif OOoO000O00oO == 'clearpackages' : wiz . clearPackages ( )
elif OOoO000O00oO == 'clearthumb' : O00O0O ( )
elif OOoO000O00oO == 'freshstart' : OoOo0oOooOoOO ( )
elif OOoO000O00oO == 'forceupdate' : wiz . forceUpdate ( )
elif OOoO000O00oO == 'forceclose' : wiz . killxbmc ( )
elif OOoO000O00oO == 'uploadlog' : uploadLog . LogUploader ( )
elif OOoO000O00oO == 'viewlog' : I1iIIIi1 ( )
elif OOoO000O00oO == 'viewwizlog' : II111Ii1i1 ( )
elif OOoO000O00oO == 'clearwizlog' : iiIi1IIiI = open ( o0oO0 , 'w' ) ; iiIi1IIiI . close ( ) ; wiz . LogNotify ( Oo0Ooo , "Wizard Log Cleared!" )
elif OOoO000O00oO == 'purgedb' : I1i ( )
elif OOoO000O00oO == 'removeaddons' : OOOoOoO ( )
elif OOoO000O00oO == 'removeaddon' : oOooO0 ( iIiIi11 )
elif OOoO000O00oO == 'removeaddondata' : o0o0oOoOO0O ( )
elif OOoO000O00oO == 'removedata' : OOOoO000 ( iIiIi11 )
elif OOoO000O00oO == 'resetaddon' : oOOOoo = wiz . cleanHouse ( IiI , ignore = True ) ; wiz . LogNotify ( Oo0Ooo , "Addon_Data reset" )
if 8 - 8: IIiiIiII1Ii
elif OOoO000O00oO == 'apkspinz' : i1i1iI1iiiI ( )
elif OOoO000O00oO == 'apk' : i1I1i111Ii ( )
elif OOoO000O00oO == 'apkkodi' : IIIii11 ( )
elif OOoO000O00oO == 'apkmaster' : i1II1 ( )
elif OOoO000O00oO == 'apkgames' : OoO ( )
elif OOoO000O00oO == 'apkvid' : oOoO00O0 ( )
elif OOoO000O00oO == 'apksys' : i11II1I11I1 ( )
elif OOoO000O00oO == 'apkinstall' : Oooo00 ( iIiIi11 , OOO )
if 4 - 4: IiII111iI1ii1 + IiII111iI1ii1 * i1I - I1I1II1I11
elif OOoO000O00oO == 'savedata' : O00oOOooo ( )
elif OOoO000O00oO == 'togglesetting' : wiz . setS ( iIiIi11 , 'false' if wiz . getS ( iIiIi11 ) == 'true' else 'true' ) ; xbmc . executebuiltin ( 'Container.Refresh' )
if 78 - 78: oo0o / O0ooO0Oo00o % I1I1II1I11
elif OOoO000O00oO == 'trakt' : iiIIi ( )
elif OOoO000O00oO == 'savetrakt' : traktit . traktIt ( 'update' , iIiIi11 )
elif OOoO000O00oO == 'restoretrakt' : traktit . traktIt ( 'restore' , iIiIi11 )
elif OOoO000O00oO == 'addontrakt' : traktit . traktIt ( 'clearaddon' , iIiIi11 )
elif OOoO000O00oO == 'cleartrakt' : traktit . clearSaved ( iIiIi11 )
elif OOoO000O00oO == 'authtrakt' : traktit . activateTrakt ( iIiIi11 ) ; xbmc . executebuiltin ( 'Container.Refresh' )
if 52 - 52: iIIIiiI1i1 - IIii11I1 * I11I1IIII
elif OOoO000O00oO == 'realdebrid' : IIii11I1i1I ( )
elif OOoO000O00oO == 'savedebrid' : debridit . debridIt ( 'update' , iIiIi11 )
elif OOoO000O00oO == 'restoredebrid' : debridit . debridIt ( 'restore' , iIiIi11 )
elif OOoO000O00oO == 'addondebrid' : debridit . debridIt ( 'clearaddon' , iIiIi11 )
elif OOoO000O00oO == 'cleardebrid' : debridit . clearSaved ( iIiIi11 )
elif OOoO000O00oO == 'authdebrid' : debridit . activateDebrid ( iIiIi11 ) ; xbmc . executebuiltin ( 'Container.Refresh' )
if 17 - 17: i1IIi + iIIIiiI1i1 * oOo00oOoO000 * I1I1II1I11
elif OOoO000O00oO == 'contact' : wiz . TextBoxes ( Oo0Ooo , III1iII1I1ii )
elif OOoO000O00oO == 'settings' : wiz . openS ( ) ; xbmc . executebuiltin ( 'Container.Refresh' )
if 36 - 36: ooo0 + Oo0
elif OOoO000O00oO == 'developer' : Oo00O ( )
elif OOoO000O00oO == 'convertpath' : wiz . convertSpecial ( O00ooooo00 )
elif OOoO000O00oO == 'testnotify' : OOO0oOoO0O ( )
elif OOoO000O00oO == 'bre' : i1ii ( )
elif OOoO000O00oO == 'full' : backuprestore . FullBackup ( )
elif OOoO000O00oO == 'backb' : backuprestore . Backup ( )
elif OOoO000O00oO == 'backad' : backuprestore . ADDON_DATA_BACKUP ( )
elif OOoO000O00oO == 'refull' : OO0O0o0o0 ( )
elif OOoO000O00oO == 'delbu' : Oo0000O0OOooO ( )
elif OOoO000O00oO == 'delall' : backuprestore . DeleteAllBackups ( )
elif OOoO000O00oO == 'read' : backuprestore . READ_ZIP ( OOO )
elif OOoO000O00oO == 'dell' : backuprestore . DeleteBackup ( OOO )
if OOoO000O00oO not in [ '' , 'togglesettings' , 'settings' , 'contact' ] : xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
# dd678faae9ac167bc83abf78e5cb2f3f0688d3a3