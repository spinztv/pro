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
Oo0OoO00oOO0o = uservar . SNESFILE
OOO00O = uservar . EMUFILE
OOoOO0oo0ooO = uservar . NESAFILE
O0o0O00Oo0o0 = uservar . NESCFILE
O00O0oOO00O00 = uservar . NESDFILE
i1Oo00 = uservar . NESFFILE
i1i = uservar . NESHFILE
iiI111I1iIiI = uservar . NESLFILE
IIIi1I1IIii1II = uservar . NESNFILE
O0 = uservar . NESRFILE
ii1ii1ii = uservar . NESTFILE
oooooOoo0ooo = uservar . NESWFILE
I1I1IiI1 = uservar . GENAFILE
III1iII1I1ii = uservar . GENCFILE
oOOo0 = uservar . GENEFILE
oo00O00oO = uservar . GENHFILE
iIiIIIi = uservar . GENMFILE
ooo00OOOooO = uservar . GENPFILE
O00OOOoOoo0O = uservar . GENSFILE
O000OOo00oo = uservar . GENUFILE
oo0OOo = wiz . workingURL ( OOO00O )
ooOOO00Ooo = wiz . workingURL ( Oo0OoO00oOO0o )
IiIIIi1iIi = wiz . workingURL ( OOoOO0oo0ooO )
ooOOoooooo = wiz . workingURL ( O0o0O00Oo0o0 )
II1I = wiz . workingURL ( O00O0oOO00O00 )
O0i1II1Iiii1I11 = wiz . workingURL ( i1Oo00 )
IIII = wiz . workingURL ( i1i )
iiIiI = wiz . workingURL ( iiI111I1iIiI )
o00oooO0Oo = wiz . workingURL ( IIIi1I1IIii1II )
o0O0OOO0Ooo = wiz . workingURL ( O0 )
iiIiII1 = wiz . workingURL ( ii1ii1ii )
OOO00O0O = wiz . workingURL ( oooooOoo0ooo )
iii = wiz . workingURL ( I1I1IiI1 )
oOooOOOoOo = wiz . workingURL ( III1iII1I1ii )
i1Iii1i1I = wiz . workingURL ( oOOo0 )
OOoO00 = wiz . workingURL ( oo00O00oO )
IiI111111IIII = wiz . workingURL ( iIiIIIi )
i1Ii = wiz . workingURL ( ooo00OOOooO )
ii111iI1iIi1 = wiz . workingURL ( O00OOOoOoo0O )
OOO = wiz . workingURL ( O000OOo00oo )
oo0OOo0 = wiz . workingURL ( o00OO00OoO )
I11IiI = wiz . workingURL ( OOOO0OOoO0O0 )
O0ooO0Oo00o = wiz . workingURL ( O0Oo000ooO00 )
ooO0oOOooOo0 = wiz . workingURL ( oO0 )
i1I1ii11i1Iii = wiz . workingURL ( Ii1iIiII1ii1 )
I1IiiiiI = wiz . workingURL ( ooOooo000oOO )
o0OIiII = wiz . workingURL ( Oo0oOOo )
ii1iII1II = uservar . UPDATECHECK if str ( uservar . UPDATECHECK ) . isdigit ( ) else 1
Iii1I1I11iiI1 = iIi1ii1I1 + timedelta ( days = ii1iII1II )
I1I1i1I = uservar . NOTIFICATION
ii1I = uservar . ENABLE
O0oO0 = uservar . HEADERMESSAGE
oO0O0OO0O = uservar . HIDECONTACT
OO = uservar . CONTACT
OoOoO = uservar . HIDESPACERS
Ii1I1i = uservar . COLOR1
OOI1iI1ii1II = uservar . COLOR2
O0O0OOOOoo = uservar . THEME1
oOooO0 = uservar . THEME2
Ii1I1Ii = uservar . THEME3
OOoO0 = uservar . THEME4
OO0Oooo0oOO0O = uservar . THEME5
o00O0 = uservar . ICONMAINT if not uservar . ICONMAINT == 'http://' else I1i1iiI1
oOO0O00Oo0O0o = uservar . ICONBUILDS if not uservar . ICONBUILDS == 'http://' else I1i1iiI1
ii1 = uservar . ICONSPEED if not uservar . ICONSPEED == 'http://' else I1i1iiI1
I1iIIiiIIi1i = uservar . ICONAPK if not uservar . ICONAPK == 'http://' else I1i1iiI1
O0O0ooOOO = uservar . ICONCONTACT if not uservar . ICONCONTACT == 'http://' else I1i1iiI1
oOOo0O00o = uservar . ICONSAVE if not uservar . ICONSAVE == 'http://' else I1i1iiI1
iIiIi11 = uservar . ICONREAL if not uservar . ICONREAL == 'http://' else I1i1iiI1
OOOiiiiI = uservar . ICONTRAKT if not uservar . ICONTRAKT == 'http://' else I1i1iiI1
oooOo0OOOoo0 = uservar . ICONSETTINGS if not uservar . ICONSETTINGS == 'http://' else I1i1iiI1
OOoO = uservar . ICONKODI if not uservar . ICONKODI == 'http://' else I1i1iiI1
OO0O000 = uservar . ICONGAMES if not uservar . ICONGAMES == 'http://' else I1i1iiI1
iiIiI1i1 = uservar . ICONMOVIES if not uservar . ICONMOVIES == 'http://' else I1i1iiI1
oO0O00oOOoooO = uservar . ICONANDROID if not uservar . ICONANDROID == 'http://' else I1i1iiI1
IiIi11iI = uservar . ICONSPMC if not uservar . ICONSPMC == 'http://' else I1i1iiI1
Oo0O00O000 = uservar . ICONSPINZ if not uservar . ICONSPINZ == 'http://' else I1i1iiI1
###########################
###### Menu Items   #######
###########################
#addDir (display,mode,name=None,url=None,menu=None,overwrite=True,fanart=FANART,icon=ICON, themeit=None)
#addFile(display,mode,name=None,url=None,menu=None,overwrite=True,fanart=FANART,icon=ICON, themeit=None)
if 3 - 3: O0OoOO0o * Iii % I1111i
if 14 - 14: Oo0OO / O0OooOo0o
if 29 - 29: i1ii1I1111ii1 % iIiI1
if 70 - 70: O0OO
def ii1iI1I11I ( ) :
 if len ( o00 ) > 0 :
  II1iI = wiz . checkBuild ( o00 , 'version' )
  O0o0o00OO0000 = '%s (v%s)' % ( o00 , Oo0oO0ooo )
  if II1iI > Oo0oO0ooo : O0o0o00OO0000 = '%s [COLOR red][B][UPDATE v%s][/B][/COLOR]' % ( O0o0o00OO0000 , II1iI )
  I1i ( O0o0o00OO0000 , 'viewbuild' , o00 , themeit = OOoO0 )
  O00Oooo = wiz . checkBuild ( o00 , 'theme' )
  if not O00Oooo == 'http://' and wiz . workingURL ( O00Oooo ) == True :
   i11I ( 'None' if o0oOoO00o == "" else o0oOoO00o , 'theme' , o00 , themeit = OO0Oooo0oOO0O )
 else : I1i ( 'None' , 'builds' , themeit = OOoO0 )
 if OoOoO == 'No' : i11I ( '============================================' , '' , themeit = Ii1I1Ii )
 I1i ( 'SpinzTV Builds' , 'builds' , icon = oOO0O00Oo0O0o , themeit = O0O0OOOOoo )
 I1i ( 'Maintenance' , 'maint' , icon = o00O0 , themeit = O0O0OOOOoo )
 I1i ( 'Speed Test' , 'speed' , icon = ii1 , themeit = O0O0OOOOoo )
 I1i ( 'Apk Installer (ANDROID ONLY!!!)' , 'apk' , icon = I1iIIiiIIi1i , themeit = O0O0OOOOoo )
 I1i ( 'Emulators And Roms (ANDROID ONLY!)' , 'emurom' , icon = OO0O000 , themeit = O0O0OOOOoo )
 I1i ( 'Save Data' , 'savedata' , icon = oOOo0O00o , themeit = O0O0OOOOoo )
 if oO0O0OO0O == 'No' : i11I ( 'Contact' , 'contact' , icon = O0O0ooOOO , themeit = O0O0OOOOoo )
 if OoOoO == 'No' : i11I ( '============================================' , '' , themeit = Ii1I1Ii )
 i11I ( 'Settings' , 'settings' , icon = oooOo0OOOoo0 , themeit = O0O0OOOOoo )
 if I11i1 == 'true' : I1i ( 'Developer Menu' , 'developer' , icon = oooOo0OOOoo0 , themeit = O0O0OOOOoo )
 o00Oo0oooooo ( 'movies' , 'MAIN' )
 if 76 - 76: o0oooOO00 / IIiii / oOOOoo00 % IIIIiiIiiI . OOOoO00 . IIiIi11i1i
 if 41 - 41: O0O00O0 % OoOO0o - iII1iIi11i . IiiiiI1i1Iii % oo00oO0o
 if 31 - 31: OOOoO00
 if 23 - 23: IiiiiI1i1Iii . iII1iIi11i
def OO0000o ( ) :
 if not oo0OOo0 == True :
  i11I ( 'Kodi Version: %s' % IIIII , '' , icon = oOO0O00Oo0O0o , themeit = Ii1I1Ii )
  if OoOoO == 'No' : i11I ( '============================================' , '' , themeit = Ii1I1Ii )
  i11I ( 'Url for txt file not valid' , '' , icon = oOO0O00Oo0O0o , themeit = Ii1I1Ii )
  i11I ( '%s' % oo0OOo0 , '' , icon = oOO0O00Oo0O0o , themeit = Ii1I1Ii )
 else :
  i1I1i1 = wiz . openURL ( o00OO00OoO ) . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
  O0OoooO0 = re . compile ( 'name="(.+?)".+?ersion="(.+?)".+?rl="(.+?)".+?odi="(.+?)".+?con="(.+?)".+?anart="(.+?)"' ) . findall ( i1I1i1 )
  if len ( O0OoooO0 ) == 1 :
   ooo0O0o00O ( O0OoooO0 [ 0 ] [ 0 ] )
  elif len ( O0OoooO0 ) > 1 :
   i11I ( 'Kodi Version: %s' % IIIII , '' , icon = oOO0O00Oo0O0o , themeit = Ii1I1Ii )
   if OoOoO == 'No' : i11I ( '============================================' , '' , themeit = Ii1I1Ii )
   if oOo0oooo00o == 'true' :
    for I1i11 , II1iI , IiIi1I1 , IiIIi1 , IIIIiii1IIii , II1i11I in O0OoooO0 :
     ii1I1IIii11 = O0o0oO ( 'install' , I1i11 )
     I1i ( '[%s] %s (v%s)' % ( float ( IiIIi1 ) , I1i11 , II1iI ) , 'viewbuild' , I1i11 , fanart = II1i11I , icon = IIIIiii1IIii , menu = ii1I1IIii11 , themeit = oOooO0 )
   else :
    IIIIiIiIi1 = wiz . buildCount ( '15' ) ; I11iiiiI1i = wiz . buildCount ( '16' )
    if I11iiiiI1i > 0 :
     if IIIIiIiIi1 > 0 :
      iI1i11 = '+' if i1111 == 'false' else '-'
      i11I ( '[%s] Jarvis and Above(%s)' % ( iI1i11 , I11iiiiI1i ) , 'showupdate' , '16' , themeit = Ii1I1Ii )
     if i1111 == 'true' :
      for I1i11 , II1iI , IiIi1I1 , IiIIi1 , IIIIiii1IIii , II1i11I in O0OoooO0 :
       OoOOoooOO0O = int ( float ( IiIIi1 ) )
       if OoOOoooOO0O >= 16 :
        ii1I1IIii11 = O0o0oO ( 'install' , I1i11 )
        I1i ( '[%s] %s (v%s)' % ( float ( IiIIi1 ) , I1i11 , II1iI ) , 'viewbuild' , I1i11 , fanart = II1i11I , icon = IIIIiii1IIii , menu = ii1I1IIii11 , themeit = oOooO0 )
    if IIIIiIiIi1 > 0 :
     if I11iiiiI1i > 0 :
      iI1i11 = '+' if oOOoo00O0O == 'false' else '-'
      i11I ( '[%s] Isengard and Below(%s)' % ( iI1i11 , IIIIiIiIi1 ) , 'showupdate' , '15' , themeit = Ii1I1Ii )
     if oOOoo00O0O == 'true' :
      for I1i11 , II1iI , IiIi1I1 , IiIIi1 , IIIIiii1IIii , II1i11I in O0OoooO0 :
       OoOOoooOO0O = int ( float ( IiIIi1 ) )
       if OoOOoooOO0O <= 15 :
        ii1I1IIii11 = O0o0oO ( 'install' , I1i11 )
        I1i ( '[%s] %s (v%s)' % ( float ( IiIIi1 ) , I1i11 , II1iI ) , 'viewbuild' , I1i11 , fanart = II1i11I , icon = IIIIiii1IIii , menu = ii1I1IIii11 , themeit = oOooO0 )
  else : i11I ( 'Text file for builds not formated correctly.' , '' , icon = oOO0O00Oo0O0o , themeit = Ii1I1Ii )
 o00Oo0oooooo ( 'movies' , 'MAIN' )
 if 86 - 86: IIiii
def ooo0O0o00O ( name ) :
 if not oo0OOo0 == True :
  i11I ( 'Url for txt file not valid' , '' , themeit = Ii1I1Ii )
  i11I ( '%s' % oo0OOo0 , '' , themeit = Ii1I1Ii )
  return
 if wiz . checkBuild ( name , 'version' ) == False :
  i11I ( 'Error reading the txt file.' , '' , themeit = Ii1I1Ii )
  i11I ( '%s was not found in the builds list.' % name , '' , themeit = Ii1I1Ii )
  return
 i1I1i1 = wiz . openURL ( o00OO00OoO ) . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
 O0OoooO0 = re . compile ( 'name="%s".+?ersion="(.+?)".+?rl="(.+?)".+?ui="(.+?)".+?odi="(.+?)".+?heme="(.+?)".+?con="(.+?)".+?anart="(.+?)"' % name ) . findall ( i1I1i1 )
 for II1iI , IiIi1I1 , i1Iii11Ii1i1 , IiIIi1 , O00Oooo , IIIIiii1IIii , II1i11I in O0OoooO0 :
  IIIIiii1IIii = IIIIiii1IIii if wiz . workingURL ( IIIIiii1IIii ) else I1i1iiI1
  II1i11I = II1i11I if wiz . workingURL ( II1i11I ) else O0oo0OO0
  O0o0o00OO0000 = '%s (v%s)' % ( name , II1iI )
  if o00 == name and II1iI > Oo0oO0ooo :
   O0o0o00OO0000 = '%s [COLOR red][B][CURRENT v%s][/B][/COLOR]' % ( O0o0o00OO0000 , Oo0oO0ooo )
  i11I ( O0o0o00OO0000 , '' , fanart = II1i11I , icon = IIIIiii1IIii , themeit = oOooO0 )
  i11I ( '===============[ Install ]===================' , '' , fanart = II1i11I , icon = IIIIiii1IIii , themeit = Ii1I1Ii )
  i11I ( 'Fresh Install' , 'install' , name , 'fresh' , fanart = II1i11I , icon = IIIIiii1IIii , themeit = O0O0OOOOoo )
  i11I ( 'Standard Install' , 'install' , name , 'normal' , fanart = II1i11I , icon = IIIIiii1IIii , themeit = O0O0OOOOoo )
  if not i1Iii11Ii1i1 == 'http://' : i11I ( 'Apply guiFix' , 'install' , name , 'gui' , fanart = II1i11I , icon = IIIIiii1IIii , themeit = O0O0OOOOoo )
  if not O00Oooo == 'http://' :
   if wiz . workingURL ( O00Oooo ) == True :
    i11I ( '===============[ Themes ]==================' , '' , fanart = II1i11I , icon = IIIIiii1IIii , themeit = Ii1I1Ii )
    i1I1i1 = wiz . openURL ( O00Oooo ) . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
    O0OoooO0 = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?con="(.+?)".+?anart="(.+?)"' ) . findall ( i1I1i1 )
    for OOooo0O0o0 , II1iI1I11I , o0OO0 , IiI11ii1I in O0OoooO0 :
     o0OO0 = o0OO0 if o0OO0 == 'http://' else IIIIiii1IIii
     IiI11ii1I = IiI11ii1I if IiI11ii1I == 'http://' else II1i11I
     i11I ( OOooo0O0o0 if not OOooo0O0o0 == o0oOoO00o else "[B]%s (Installed)[/B]" % OOooo0O0o0 , 'theme' , name , OOooo0O0o0 , fanart = IiI11ii1I , icon = o0OO0 , themeit = Ii1I1Ii )
     if 74 - 74: i11iIiiIii . i1ii1I1111ii1
     if 36 - 36: I1111i . O0OO
     if 56 - 56: iIiI1 . oOOOoo00 . i1ii1I1111ii1
     if 39 - 39: O0OoOO0o + IiiiiI1i1Iii
def OoOooOoO ( ) :
 I1i ( 'SpinzTV APKS' , 'apkspinz' , icon = Oo0O00O000 , themeit = O0O0OOOOoo )
 I1i ( 'Kodi and SPMC' , 'apkkodi' , icon = OOoO , themeit = O0O0OOOOoo )
 I1i ( 'Android Games' , 'apkgames' , icon = OO0O000 , themeit = O0O0OOOOoo )
 I1i ( 'Movie and Video' , 'apkvid' , icon = iiIiI1i1 , themeit = O0O0OOOOoo )
 I1i ( 'System Tools' , 'apksys' , icon = oO0O00oOOoooO , themeit = O0O0OOOOoo )
 I1i ( 'APK Master List' , 'apkmaster' , icon = I1iIIiiIIi1i , themeit = O0O0OOOOoo )
 if 43 - 43: O0OooOo0o . IIIIiiIiiI / oOOOoo00
 if 20 - 20: i1ii1I1111ii1
def o0oO000oo ( ) :
 if I11IiI :
  i1I1i1 = wiz . openURL ( OOOO0OOoO0O0 ) . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
 O0OoooO0 = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?con="(.+?)".+?anart="(.+?)"' ) . findall ( i1I1i1 )
 if len ( O0OoooO0 ) > 0 :
  for I1i11 , IiIi1I1 , IIIIiii1IIii , II1i11I in O0OoooO0 :
   i11I ( I1i11 , 'apkinstall' , I1i11 , IiIi1I1 , icon = IIIIiii1IIii , fanart = II1i11I , themeit = O0O0OOOOoo )
  else : wiz . log ( "[APK Menu] ERROR: Invalid Format." )
 else : wiz . log ( "[APK Menu] ERROR: URL for apk list not working." )
 if 95 - 95: oo00oO0o / oo00oO0o
def IIiI1Ii ( ) :
 i11I ( 'Kodi (v%s)' % wiz . latestApk ( 'kodi' , 'version' ) , 'apkinstall' , 'kodi' , wiz . latestApk ( 'kodi' , 'url' ) , icon = OOoO , themeit = O0O0OOOOoo )
 i11I ( 'SPMC (v%s)' % wiz . latestApk ( 'spmc' , 'version' ) , 'apkinstall' , 'spmc' , wiz . latestApk ( 'spmc' , 'url' ) , icon = IiIi11iI , themeit = O0O0OOOOoo )
 if 57 - 57: OOOoO00 - oo00oO0o - IIiIi11i1i + O0OO
def I1IIIiI11i1 ( ) :
 if ooO0oOOooOo0 :
  i1I1i1 = wiz . openURL ( oO0 ) . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
 O0OoooO0 = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?con="(.+?)".+?anart="(.+?)"' ) . findall ( i1I1i1 )
 if len ( O0OoooO0 ) > 0 :
  for I1i11 , IiIi1I1 , IIIIiii1IIii , II1i11I in O0OoooO0 :
   i11I ( I1i11 , 'apkinstall' , I1i11 , IiIi1I1 , icon = IIIIiii1IIii , fanart = II1i11I , themeit = O0O0OOOOoo )
  else : wiz . log ( "[APK Menu] ERROR: Invalid Format." )
 else : wiz . log ( "[APK Menu] ERROR: URL for apk list not working." )
 if 48 - 48: IiiiiI1i1Iii - IIiii % O0O00O0
def IIi1IIIi ( ) :
 I1i ( 'Emulators' , 'emulators' , icon = OO0O000 , themeit = O0O0OOOOoo )
 I1i ( 'Roms' , 'roms' , icon = OO0O000 , themeit = O0O0OOOOoo )
 if 99 - 99: O0O00O0 + O0OO * O0OooOo0o . IIiii - oOOOoo00
def o0OOOo ( ) :
 if oo0OOo :
  i1I1i1 = wiz . openURL ( OOO00O ) . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
 O0OoooO0 = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?con="(.+?)".+?anart="(.+?)"' ) . findall ( i1I1i1 )
 if len ( O0OoooO0 ) > 0 :
  for I1i11 , IiIi1I1 , IIIIiii1IIii , II1i11I in O0OoooO0 :
   i11I ( I1i11 , 'apkinstall' , I1i11 , IiIi1I1 , icon = IIIIiii1IIii , fanart = II1i11I , themeit = O0O0OOOOoo )
  else : wiz . log ( "[APK Menu] ERROR: Invalid Format." )
 else : wiz . log ( "[APK Menu] ERROR: URL for apk list not working." )
 if 11 - 11: Iii * Iii * i1ii1I1111ii1
def iII1ii1 ( ) :
 I1i ( 'SNES' , 'snes' , icon = OO0O000 , themeit = O0O0OOOOoo )
 I1i ( 'NES' , 'nes' , icon = OO0O000 , themeit = O0O0OOOOoo )
 I1i ( 'Genesis' , 'gen' , icon = OO0O000 , themeit = O0O0OOOOoo )
 if 12 - 12: OOOoO00 - oo00oO0o . I1111i / oOOOoo00 . Oo0OO * O0OO
 if 19 - 19: i11iIiiIii + I1111i - iIiI1 - IIiIi11i1i
def Iii1iiIi1II ( ) :
 if ooOOO00Ooo :
  i1I1i1 = wiz . openURL ( Oo0OoO00oOO0o ) . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
 O0OoooO0 = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?con="(.+?)".+?anart="(.+?)"' ) . findall ( i1I1i1 )
 if len ( O0OoooO0 ) > 0 :
  for I1i11 , IiIi1I1 , IIIIiii1IIii , II1i11I in O0OoooO0 :
   i11I ( I1i11 , 'snesrominstall' , I1i11 , IiIi1I1 , icon = IIIIiii1IIii , fanart = II1i11I , themeit = O0O0OOOOoo )
  else : wiz . log ( "[APK Menu] ERROR: Invalid Format." )
 else : wiz . log ( "[APK Menu] ERROR: URL for apk list not working." )
 if 60 - 60: i1ii1I1111ii1 - IIIIiiIiiI * IIiIi11i1i % O0OooOo0o
def ooo ( ) :
 I1i ( 'NES Titles A Thru B' , 'nesa' , icon = OO0O000 , themeit = O0O0OOOOoo )
 I1i ( 'NES Titles C' , 'nesc' , icon = I1iIIiiIIi1i , themeit = O0O0OOOOoo )
 I1i ( 'NES Titles D Thru E' , 'nesd' , icon = OO0O000 , themeit = O0O0OOOOoo )
 I1i ( 'NES Titles F Thru G' , 'nesf' , icon = OO0O000 , themeit = O0O0OOOOoo )
 I1i ( 'NES Titles H Thru K' , 'nesh' , icon = OO0O000 , themeit = O0O0OOOOoo )
 I1i ( 'NES Titles L Thru M' , 'nesl' , icon = OO0O000 , themeit = O0O0OOOOoo )
 I1i ( 'NES Titles N Thru Q' , 'nesn' , icon = OO0O000 , themeit = O0O0OOOOoo )
 I1i ( 'NES Titles R Thru S' , 'nesr' , icon = OO0O000 , themeit = O0O0OOOOoo )
 I1i ( 'NES Titles T Thru V' , 'nest' , icon = OO0O000 , themeit = O0O0OOOOoo )
 I1i ( 'NES Titles W Thru Z' , 'nesw' , icon = OO0O000 , themeit = O0O0OOOOoo )
 if 19 - 19: O0OO - iIiI1 . IIIIiiIiiI / IIIIiiIiiI % oo00oO0o
def ooO ( ) :
 if IiIIIi1iIi :
  i1I1i1 = wiz . openURL ( OOoOO0oo0ooO ) . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
 O0OoooO0 = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?con="(.+?)".+?anart="(.+?)"' ) . findall ( i1I1i1 )
 if len ( O0OoooO0 ) > 0 :
  for I1i11 , IiIi1I1 , IIIIiii1IIii , II1i11I in O0OoooO0 :
   i11I ( I1i11 , 'nesrominstall' , I1i11 , IiIi1I1 , icon = IIIIiii1IIii , fanart = II1i11I , themeit = O0O0OOOOoo )
  else : wiz . log ( "[ROM Menu] ERROR: Invalid Format." )
 else : wiz . log ( "[ROM Menu] ERROR: URL for Rom list not working." )
 if 6 - 6: Iii . oo00oO0o % IIiii
def I1Iii1 ( ) :
 if ooOOoooooo :
  i1I1i1 = wiz . openURL ( O0o0O00Oo0o0 ) . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
 O0OoooO0 = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?con="(.+?)".+?anart="(.+?)"' ) . findall ( i1I1i1 )
 if len ( O0OoooO0 ) > 0 :
  for I1i11 , IiIi1I1 , IIIIiii1IIii , II1i11I in O0OoooO0 :
   i11I ( I1i11 , 'nesrominstall' , I1i11 , IiIi1I1 , icon = IIIIiii1IIii , fanart = II1i11I , themeit = O0O0OOOOoo )
  else : wiz . log ( "[ROM Menu] ERROR: Invalid Format." )
 else : wiz . log ( "[ROM Menu] ERROR: URL for Rom list not working." )
 if 30 - 30: I1111i - o0oooOO00
def Ooo00O0o ( ) :
 if II1I :
  i1I1i1 = wiz . openURL ( O00O0oOO00O00 ) . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
 O0OoooO0 = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?con="(.+?)".+?anart="(.+?)"' ) . findall ( i1I1i1 )
 if len ( O0OoooO0 ) > 0 :
  for I1i11 , IiIi1I1 , IIIIiii1IIii , II1i11I in O0OoooO0 :
   i11I ( I1i11 , 'nesrominstall' , I1i11 , IiIi1I1 , icon = IIIIiii1IIii , fanart = II1i11I , themeit = O0O0OOOOoo )
  else : wiz . log ( "[ROM Menu] ERROR: Invalid Format." )
 else : wiz . log ( "[ROM Menu] ERROR: URL for Rom list not working." )
 if 72 - 72: Iii * O0O00O0 % oo00oO0o / O0OO
def I11i1II ( ) :
 if O0i1II1Iiii1I11 :
  i1I1i1 = wiz . openURL ( i1Oo00 ) . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
 O0OoooO0 = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?con="(.+?)".+?anart="(.+?)"' ) . findall ( i1I1i1 )
 if len ( O0OoooO0 ) > 0 :
  for I1i11 , IiIi1I1 , IIIIiii1IIii , II1i11I in O0OoooO0 :
   i11I ( I1i11 , 'nesrominstall' , I1i11 , IiIi1I1 , icon = IIIIiii1IIii , fanart = II1i11I , themeit = O0O0OOOOoo )
  else : wiz . log ( "[ROM Menu] ERROR: Invalid Format." )
 else : wiz . log ( "[ROM Menu] ERROR: URL for Rom list not working." )
 if 72 - 72: Iii . Oo0OO / iIiI1 . O0OooOo0o
def ooo000o000 ( ) :
 if IIII :
  i1I1i1 = wiz . openURL ( i1i ) . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
 O0OoooO0 = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?con="(.+?)".+?anart="(.+?)"' ) . findall ( i1I1i1 )
 if len ( O0OoooO0 ) > 0 :
  for I1i11 , IiIi1I1 , IIIIiii1IIii , II1i11I in O0OoooO0 :
   i11I ( I1i11 , 'nesrominstall' , I1i11 , IiIi1I1 , icon = IIIIiii1IIii , fanart = II1i11I , themeit = O0O0OOOOoo )
  else : wiz . log ( "[ROM Menu] ERROR: Invalid Format." )
 else : wiz . log ( "[ROM Menu] ERROR: URL for Rom list not working." )
 if 100 - 100: iII1iIi11i . IIiIi11i1i / O0O00O0 % o0oooOO00 % O0OooOo0o - O0OO
def IiIi1I1ii111 ( ) :
 if iiIiI :
  i1I1i1 = wiz . openURL ( iiI111I1iIiI ) . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
 O0OoooO0 = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?con="(.+?)".+?anart="(.+?)"' ) . findall ( i1I1i1 )
 if len ( O0OoooO0 ) > 0 :
  for I1i11 , IiIi1I1 , IIIIiii1IIii , II1i11I in O0OoooO0 :
   i11I ( I1i11 , 'nesrominstall' , I1i11 , IiIi1I1 , icon = IIIIiii1IIii , fanart = II1i11I , themeit = O0O0OOOOoo )
  else : wiz . log ( "[ROM Menu] ERROR: Invalid Format." )
 else : wiz . log ( "[ROM Menu] ERROR: URL for Rom list not working." )
 if 46 - 46: O0OoOO0o + Oo0OO - Oo0OO + O0OooOo0o
def oOOO0oo0 ( ) :
 if o00oooO0Oo :
  i1I1i1 = wiz . openURL ( IIIi1I1IIii1II ) . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
 O0OoooO0 = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?con="(.+?)".+?anart="(.+?)"' ) . findall ( i1I1i1 )
 if len ( O0OoooO0 ) > 0 :
  for I1i11 , IiIi1I1 , IIIIiii1IIii , II1i11I in O0OoooO0 :
   i11I ( I1i11 , 'nesrominstall' , I1i11 , IiIi1I1 , icon = IIIIiii1IIii , fanart = II1i11I , themeit = O0O0OOOOoo )
  else : wiz . log ( "[ROM Menu] ERROR: Invalid Format." )
 else : wiz . log ( "[ROM Menu] ERROR: URL for Rom list not working." )
 if 46 - 46: iII1iIi11i
def ii1iIi1iIiI1i ( ) :
 if o0O0OOO0Ooo :
  i1I1i1 = wiz . openURL ( O0 ) . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
 O0OoooO0 = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?con="(.+?)".+?anart="(.+?)"' ) . findall ( i1I1i1 )
 if len ( O0OoooO0 ) > 0 :
  for I1i11 , IiIi1I1 , IIIIiii1IIii , II1i11I in O0OoooO0 :
   i11I ( I1i11 , 'nesrominstall' , I1i11 , IiIi1I1 , icon = IIIIiii1IIii , fanart = II1i11I , themeit = O0O0OOOOoo )
  else : wiz . log ( "[ROM Menu] ERROR: Invalid Format." )
 else : wiz . log ( "[ROM Menu] ERROR: URL for Rom list not working." )
 if 40 - 40: Oo0OO % OOOoO00
def ooo0o00 ( ) :
 if iiIiII1 :
  i1I1i1 = wiz . openURL ( ii1ii1ii ) . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
 O0OoooO0 = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?con="(.+?)".+?anart="(.+?)"' ) . findall ( i1I1i1 )
 if len ( O0OoooO0 ) > 0 :
  for I1i11 , IiIi1I1 , IIIIiii1IIii , II1i11I in O0OoooO0 :
   i11I ( I1i11 , 'nesrominstall' , I1i11 , IiIi1I1 , icon = IIIIiii1IIii , fanart = II1i11I , themeit = O0O0OOOOoo )
  else : wiz . log ( "[ROM Menu] ERROR: Invalid Format." )
 else : wiz . log ( "[ROM Menu] ERROR: URL for Rom list not working." )
 if 99 - 99: O0OoOO0o . IIiIi11i1i + Iii
def I11IIi ( ) :
 if OOO00O0O :
  i1I1i1 = wiz . openURL ( oooooOoo0ooo ) . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
 O0OoooO0 = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?con="(.+?)".+?anart="(.+?)"' ) . findall ( i1I1i1 )
 if len ( O0OoooO0 ) > 0 :
  for I1i11 , IiIi1I1 , IIIIiii1IIii , II1i11I in O0OoooO0 :
   i11I ( I1i11 , 'nesrominstall' , I1i11 , IiIi1I1 , icon = IIIIiii1IIii , fanart = II1i11I , themeit = O0O0OOOOoo )
  else : wiz . log ( "[ROM Menu] ERROR: Invalid Format." )
 else : wiz . log ( "[ROM Menu] ERROR: URL for Rom list not working." )
 if 66 - 66: IIIIiiIiiI % O0OO . OOOoO00
def o0OIiiiI ( ) :
 I1i ( 'Genesis Titles A Thru B' , 'gena' , icon = OO0O000 , themeit = O0O0OOOOoo )
 I1i ( 'Genesis Titles C Thru D' , 'genc' , icon = I1iIIiiIIi1i , themeit = O0O0OOOOoo )
 I1i ( 'Genesis Titles E Thru G' , 'gene' , icon = OO0O000 , themeit = O0O0OOOOoo )
 I1i ( 'Genesis Titles H Thru L' , 'genh' , icon = OO0O000 , themeit = O0O0OOOOoo )
 I1i ( 'Genesis Titles M Thru O' , 'genm' , icon = OO0O000 , themeit = O0O0OOOOoo )
 I1i ( 'Genesis Titles P Thru R' , 'genp' , icon = OO0O000 , themeit = O0O0OOOOoo )
 I1i ( 'Genesis Titles S Thru T' , 'gens' , icon = OO0O000 , themeit = O0O0OOOOoo )
 I1i ( 'Genesis Titles U Thru Z' , 'genu' , icon = OO0O000 , themeit = O0O0OOOOoo )
 if 61 - 61: OOOoO00 % OOOoO00 * IIiii / IIiii
def o0oOO ( ) :
 if iii :
  i1I1i1 = wiz . openURL ( I1I1IiI1 ) . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
 O0OoooO0 = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?con="(.+?)".+?anart="(.+?)"' ) . findall ( i1I1i1 )
 if len ( O0OoooO0 ) > 0 :
  for I1i11 , IiIi1I1 , IIIIiii1IIii , II1i11I in O0OoooO0 :
   i11I ( I1i11 , 'genrominstall' , I1i11 , IiIi1I1 , icon = IIIIiii1IIii , fanart = II1i11I , themeit = O0O0OOOOoo )
  else : wiz . log ( "[ROM Menu] ERROR: Invalid Format." )
 else : wiz . log ( "[ROM Menu] ERROR: URL for Rom list not working." )
 if 53 - 53: IiiiiI1i1Iii * iII1iIi11i . iIiI1 - O0O00O0 % O0O00O0 * i11iIiiIii
def ii ( ) :
 if oOooOOOoOo :
  i1I1i1 = wiz . openURL ( III1iII1I1ii ) . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
 O0OoooO0 = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?con="(.+?)".+?anart="(.+?)"' ) . findall ( i1I1i1 )
 if len ( O0OoooO0 ) > 0 :
  for I1i11 , IiIi1I1 , IIIIiii1IIii , II1i11I in O0OoooO0 :
   i11I ( I1i11 , 'genrominstall' , I1i11 , IiIi1I1 , icon = IIIIiii1IIii , fanart = II1i11I , themeit = O0O0OOOOoo )
  else : wiz . log ( "[ROM Menu] ERROR: Invalid Format." )
 else : wiz . log ( "[ROM Menu] ERROR: URL for Rom list not working." )
 if 79 - 79: IIiii - IIiIi11i1i + IIiii . IIIIiiIiiI
def ii1III11 ( ) :
 if i1Iii1i1I :
  i1I1i1 = wiz . openURL ( oOOo0 ) . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
 O0OoooO0 = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?con="(.+?)".+?anart="(.+?)"' ) . findall ( i1I1i1 )
 if len ( O0OoooO0 ) > 0 :
  for I1i11 , IiIi1I1 , IIIIiii1IIii , II1i11I in O0OoooO0 :
   i11I ( I1i11 , 'genrominstall' , I1i11 , IiIi1I1 , icon = IIIIiii1IIii , fanart = II1i11I , themeit = O0O0OOOOoo )
  else : wiz . log ( "[ROM Menu] ERROR: Invalid Format." )
 else : wiz . log ( "[ROM Menu] ERROR: URL for Rom list not working." )
 if 7 - 7: OoOO0o % O0OoOO0o . o0oooOO00 + i1ii1I1111ii1 - IIiIi11i1i
def o0o0O00oo0 ( ) :
 if OOoO00 :
  i1I1i1 = wiz . openURL ( oo00O00oO ) . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
 O0OoooO0 = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?con="(.+?)".+?anart="(.+?)"' ) . findall ( i1I1i1 )
 if len ( O0OoooO0 ) > 0 :
  for I1i11 , IiIi1I1 , IIIIiii1IIii , II1i11I in O0OoooO0 :
   i11I ( I1i11 , 'genrominstall' , I1i11 , IiIi1I1 , icon = IIIIiii1IIii , fanart = II1i11I , themeit = O0O0OOOOoo )
  else : wiz . log ( "[ROM Menu] ERROR: Invalid Format." )
 else : wiz . log ( "[ROM Menu] ERROR: URL for Rom list not working." )
 if 27 - 27: i11iIiiIii % O0OooOo0o % IIiIi11i1i . O0OoOO0o - iIiI1 + o0oooOO00
def ooO0o ( ) :
 if IiI111111IIII :
  i1I1i1 = wiz . openURL ( iIiIIIi ) . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
 O0OoooO0 = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?con="(.+?)".+?anart="(.+?)"' ) . findall ( i1I1i1 )
 if len ( O0OoooO0 ) > 0 :
  for I1i11 , IiIi1I1 , IIIIiii1IIii , II1i11I in O0OoooO0 :
   i11I ( I1i11 , 'genrominstall' , I1i11 , IiIi1I1 , icon = IIIIiii1IIii , fanart = II1i11I , themeit = O0O0OOOOoo )
  else : wiz . log ( "[ROM Menu] ERROR: Invalid Format." )
 else : wiz . log ( "[ROM Menu] ERROR: URL for Rom list not working." )
 if 51 - 51: iII1iIi11i
def ii11I1 ( ) :
 if i1Ii :
  i1I1i1 = wiz . openURL ( ooo00OOOooO ) . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
 O0OoooO0 = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?con="(.+?)".+?anart="(.+?)"' ) . findall ( i1I1i1 )
 if len ( O0OoooO0 ) > 0 :
  for I1i11 , IiIi1I1 , IIIIiii1IIii , II1i11I in O0OoooO0 :
   i11I ( I1i11 , 'genrominstall' , I1i11 , IiIi1I1 , icon = IIIIiii1IIii , fanart = II1i11I , themeit = O0O0OOOOoo )
  else : wiz . log ( "[ROM Menu] ERROR: Invalid Format." )
 else : wiz . log ( "[ROM Menu] ERROR: URL for Rom list not working." )
 if 75 - 75: O0OO / O0OooOo0o % O0OoOO0o
def Ii111iIi1iIi ( ) :
 if ii111iI1iIi1 :
  i1I1i1 = wiz . openURL ( O00OOOoOoo0O ) . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
 O0OoooO0 = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?con="(.+?)".+?anart="(.+?)"' ) . findall ( i1I1i1 )
 if len ( O0OoooO0 ) > 0 :
  for I1i11 , IiIi1I1 , IIIIiii1IIii , II1i11I in O0OoooO0 :
   i11I ( I1i11 , 'genrominstall' , I1i11 , IiIi1I1 , icon = IIIIiii1IIii , fanart = II1i11I , themeit = O0O0OOOOoo )
  else : wiz . log ( "[ROM Menu] ERROR: Invalid Format." )
 else : wiz . log ( "[ROM Menu] ERROR: URL for Rom list not working." )
 if 21 - 21: IIIIiiIiiI / oOOOoo00 + O0O00O0 + I1111i
def OoOo ( ) :
 if OOO :
  i1I1i1 = wiz . openURL ( O000OOo00oo ) . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
 O0OoooO0 = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?con="(.+?)".+?anart="(.+?)"' ) . findall ( i1I1i1 )
 if len ( O0OoooO0 ) > 0 :
  for I1i11 , IiIi1I1 , IIIIiii1IIii , II1i11I in O0OoooO0 :
   i11I ( I1i11 , 'genrominstall' , I1i11 , IiIi1I1 , icon = IIIIiii1IIii , fanart = II1i11I , themeit = O0O0OOOOoo )
  else : wiz . log ( "[ROM Menu] ERROR: Invalid Format." )
 else : wiz . log ( "[ROM Menu] ERROR: URL for Rom list not working." )
 if 35 - 35: oo00oO0o * OOOoO00 . IIiIi11i1i * IIiii . o0oooOO00 / O0OoOO0o
def O00 ( ) :
 if i1I1ii11i1Iii :
  i1I1i1 = wiz . openURL ( Ii1iIiII1ii1 ) . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
 O0OoooO0 = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?con="(.+?)".+?anart="(.+?)"' ) . findall ( i1I1i1 )
 if len ( O0OoooO0 ) > 0 :
  for I1i11 , IiIi1I1 , IIIIiii1IIii , II1i11I in O0OoooO0 :
   i11I ( I1i11 , 'apkinstall' , I1i11 , IiIi1I1 , icon = IIIIiii1IIii , fanart = II1i11I , themeit = O0O0OOOOoo )
  else : wiz . log ( "[APK Menu] ERROR: Invalid Format." )
 else : wiz . log ( "[APK Menu] ERROR: URL for apk list not working." )
 if 52 - 52: oo00oO0o + O0OoOO0o . OoOO0o . oOOOoo00 . O0OO
def oo000 ( ) :
 if I1IiiiiI :
  i1I1i1 = wiz . openURL ( ooOooo000oOO ) . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
 O0OoooO0 = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?con="(.+?)".+?anart="(.+?)"' ) . findall ( i1I1i1 )
 if len ( O0OoooO0 ) > 0 :
  for I1i11 , IiIi1I1 , IIIIiii1IIii , II1i11I in O0OoooO0 :
   i11I ( I1i11 , 'apkinstall' , I1i11 , IiIi1I1 , icon = IIIIiii1IIii , fanart = II1i11I , themeit = O0O0OOOOoo )
  else : wiz . log ( "[APK Menu] ERROR: Invalid Format." )
 else : wiz . log ( "[APK Menu] ERROR: URL for apk list not working." )
 if 32 - 32: Oo0OO . O0O00O0
def oOO ( ) :
 if O0ooO0Oo00o :
  i1I1i1 = wiz . openURL ( O0Oo000ooO00 ) . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
 O0OoooO0 = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?con="(.+?)".+?anart="(.+?)"' ) . findall ( i1I1i1 )
 if len ( O0OoooO0 ) > 0 :
  for I1i11 , IiIi1I1 , IIIIiii1IIii , II1i11I in O0OoooO0 :
   i11I ( I1i11 , 'apkinstall' , I1i11 , IiIi1I1 , icon = IIIIiii1IIii , fanart = II1i11I , themeit = O0O0OOOOoo )
  else : wiz . log ( "[APK Menu] ERROR: Invalid Format." )
 else : wiz . log ( "[APK Menu] ERROR: URL for apk list not working." )
 if 54 - 54: i1ii1I1111ii1 / Iii / OOOoO00 . OOOoO00 % OoOO0o . i1ii1I1111ii1
 if 10 - 10: IIiii + OOOoO00
 if 27 - 27: O0OO . IIiIi11i1i + o0oooOO00 / Iii % OoOO0o . oo00oO0o
 if 14 - 14: IIIIiiIiiI + oOOOoo00 - OoOO0o / O0OoOO0o . IiiiiI1i1Iii
def i1iiIiI1Ii1i ( ) :
 i1iIi = '[COLOR green]ON[/COLOR]' ; iiiii1II = '[COLOR red]OFF[/COLOR]'
 O0OOO0OOooo00 = 'true' if i11 == 'true' else 'false'
 I111iIi1 = 'true' if I11 == 'true' else 'false'
 oo00O00oO000o = 'true' if Oo0o0000o0o0 == 'true' else 'false'
 if 71 - 71: oOOOoo00 - oo00oO0o / o0oooOO00 * o0oooOO00 / Oo0OO . Oo0OO
 i11I ( 'Fresh Start' , 'freshstart' , icon = o00O0 , themeit = O0O0OOOOoo )
 i11I ( 'Clear Cache' , 'clearcache' , icon = o00O0 , themeit = O0O0OOOOoo )
 i11I ( 'Clear Packages' , 'clearpackages' , icon = o00O0 , themeit = O0O0OOOOoo )
 i11I ( 'Clear Thumbnails' , 'clearthumb' , icon = o00O0 , themeit = O0O0OOOOoo )
 i11I ( 'Purge Databases' , 'purgedb' , icon = o00O0 , themeit = O0O0OOOOoo )
 I1i ( 'Remove Addons' , 'removeaddons' , icon = o00O0 , themeit = O0O0OOOOoo )
 I1i ( 'Remove Addon Data' , 'removeaddondata' , icon = o00O0 , themeit = O0O0OOOOoo )
 i11I ( 'Force Update Addons' , 'forceupdate' , icon = o00O0 , themeit = O0O0OOOOoo )
 i11I ( 'Force Close Kodi' , 'forceclose' , icon = o00O0 , themeit = O0O0OOOOoo )
 i11I ( 'Upload Kodi log' , 'uploadlog' , icon = o00O0 , themeit = O0O0OOOOoo )
 i11I ( 'View Kodi Log File' , 'viewlog' , icon = o00O0 , themeit = O0O0OOOOoo )
 i11I ( 'View Wizard Log File' , 'viewwizlog' , icon = o00O0 , themeit = O0O0OOOOoo )
 i11I ( 'Clear Wizard Log File' , 'clearwizlog' , icon = o00O0 , themeit = O0O0OOOOoo )
 i11I ( '==============[ Auto Clean ]==============' , '' , fanart = O0oo0OO0 , icon = o00O0 , themeit = Ii1I1Ii )
 i11I ( 'Auto Clean Up On Startup: %s' % O0OOO0OOooo00 . replace ( 'true' , i1iIi ) . replace ( 'false' , iiiii1II ) , 'togglesetting' , 'autoclean' , icon = o00O0 , themeit = O0O0OOOOoo )
 if O0OOO0OOooo00 == 'true' :
  i11I ( '--- Clear Cache on Startup: %s' % I111iIi1 . replace ( 'true' , i1iIi ) . replace ( 'false' , iiiii1II ) , 'togglesetting' , 'clearcache' , icon = o00O0 , themeit = O0O0OOOOoo )
  i11I ( '--- Clear Packages on Startup: %s' % oo00O00oO000o . replace ( 'true' , i1iIi ) . replace ( 'false' , iiiii1II ) , 'togglesetting' , 'clearpackages' , icon = o00O0 , themeit = O0O0OOOOoo )
 o00Oo0oooooo ( 'movies' , 'MAIN' )
 if 53 - 53: IiiiiI1i1Iii
 if 21 - 21: IIiIi11i1i
 if 92 - 92: i11iIiiIii / IiiiiI1i1Iii - OoOO0o % oo00oO0o * IiiiiI1i1Iii + iIiI1
 if 11 - 11: I1111i . IiiiiI1i1Iii
def Oo0000oOo ( ) :
 if o0OIiII :
  i1I1i1 = wiz . openURL ( Oo0oOOo ) . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
 O0OoooO0 = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?con="(.+?)".+?anart="(.+?)"' ) . findall ( i1I1i1 )
 if len ( O0OoooO0 ) > 0 :
  for I1i11 , IiIi1I1 , IIIIiii1IIii , II1i11I in O0OoooO0 :
   i11I ( I1i11 , 'speedtest' , I1i11 , IiIi1I1 , icon = IIIIiii1IIii , fanart = II1i11I , themeit = O0O0OOOOoo )
  else : wiz . log ( "[APK Menu] ERROR: Invalid Format." )
 else : wiz . log ( "[APK Menu] ERROR: URL for apk list not working." )
 if 31 - 31: IIiIi11i1i . IiiiiI1i1Iii * oo00oO0o + i11iIiiIii * IIIIiiIiiI
 if 93 - 93: oOOOoo00 / Iii * Oo0OO % I1111i * O0OoOO0o * IIiIi11i1i
 if 64 - 64: O0OooOo0o + O0OoOO0o / Iii / iIiI1 . oo00oO0o % iII1iIi11i
 if 50 - 50: Iii - iII1iIi11i + OOOoO00
def o0iiiI1I1iIIIi1 ( ) :
 i1iIi = '[COLOR green]ON[/COLOR]' ; iiiii1II = '[COLOR red]OFF[/COLOR]'
 IiiI1iiiiI1iI = 'true' if iIii1 == 'true' else 'false'
 iIiiiii1i = 'true' if oOOoO0 == 'true' else 'false'
 iiIi1IIiI = 'true' if ii11iIi1I == 'true' else 'false'
 i1oO0OO0 = 'true' if OOooO0OOoo == 'true' else 'false'
 o0O0Oo00 = 'true' if iI111I11I1I1 == 'true' else 'false'
 O0Oo0o000oO = 'true' if i1iiIII111ii == 'true' else 'false'
 i1Iii11Ii1i1 = 'true' if i1iIIi1 == 'true' else 'false'
 if 99 - 99: IIIIiiIiiI * O0OooOo0o * IiiiiI1i1Iii
 I1i ( 'Keep Trakt Data' , 'trakt' , icon = oOOo0O00o , themeit = O0O0OOOOoo )
 I1i ( 'Keep Real Debrid' , 'realdebrid' , icon = oOOo0O00o , themeit = O0O0OOOOoo )
 i11I ( '- Click to toggle settings -' , '' , themeit = Ii1I1Ii )
 i11I ( 'Save Trakt: %s' % IiiI1iiiiI1iI . replace ( 'true' , i1iIi ) . replace ( 'false' , iiiii1II ) , 'togglesetting' , 'keeptrakt' , icon = oOOo0O00o , themeit = O0O0OOOOoo )
 i11I ( 'Save Real Debrid: %s' % iIiiiii1i . replace ( 'true' , i1iIi ) . replace ( 'false' , iiiii1II ) , 'togglesetting' , 'keepdebrid' , icon = oOOo0O00o , themeit = O0O0OOOOoo )
 i11I ( 'Keep \'Sources.xml\': %s' % iiIi1IIiI . replace ( 'true' , i1iIi ) . replace ( 'false' , iiiii1II ) , 'togglesetting' , 'keepsources' , icon = oOOo0O00o , themeit = O0O0OOOOoo )
 i11I ( 'Keep \'Profiles.xml\': %s' % o0O0Oo00 . replace ( 'true' , i1iIi ) . replace ( 'false' , iiiii1II ) , 'togglesetting' , 'keepprofiles' , icon = oOOo0O00o , themeit = O0O0OOOOoo )
 i11I ( 'Keep \'Advancedsettings.xml\': %s' % i1oO0OO0 . replace ( 'true' , i1iIi ) . replace ( 'false' , iiiii1II ) , 'togglesetting' , 'keepadvanced' , icon = oOOo0O00o , themeit = O0O0OOOOoo )
 i11I ( 'Keep \'Favourites.xml\': %s' % O0Oo0o000oO . replace ( 'true' , i1iIi ) . replace ( 'false' , iiiii1II ) , 'togglesetting' , 'keepfavourites' , icon = oOOo0O00o , themeit = O0O0OOOOoo )
 i11I ( 'Keep \'Guisettings.xml\': %s' % i1Iii11Ii1i1 . replace ( 'true' , i1iIi ) . replace ( 'false' , iiiii1II ) , 'togglesetting' , 'keepgui' , icon = oOOo0O00o , themeit = O0O0OOOOoo )
 if 92 - 92: iIiI1
 if 40 - 40: o0oooOO00 / iII1iIi11i
def OOOoO000 ( ) :
 IiiI1iiiiI1iI = '[COLOR green]ON[/COLOR]' if iIii1 == 'true' else '[COLOR red]OFF[/COLOR]'
 oOOOO = str ( i1iiIIiiI111 ) if not i1iiIIiiI111 == '' else 'Trakt hasnt been saved yet.'
 i11I ( '[I]Register FREE Account at http://trakt.tv[/I]' , '' , icon = OOOiiiiI , themeit = Ii1I1Ii )
 i11I ( 'Save Trakt Data: %s' % IiiI1iiiiI1iI , 'togglesetting' , 'keeptrakt' , icon = OOOiiiiI , themeit = Ii1I1Ii )
 if iIii1 == 'true' : i11I ( 'Last Save: %s' % str ( oOOOO ) , '' , icon = OOOiiiiI , themeit = Ii1I1Ii )
 if OoOoO == 'No' : i11I ( '============================================' , '' , icon = OOOiiiiI , themeit = Ii1I1Ii )
 Ii = os . path . join ( oO00oOo , ooooooO0oo , 'icon.png' ) if os . path . exists ( OOOOi11i1 ) else OOOiiiiI
 Ii1ii111i1 = os . path . join ( oO00oOo , ooooooO0oo , 'fanart.jpg' ) if os . path . exists ( OOOOi11i1 ) else O0oo0OO0
 i11I ( '[+]-- Exodus' , '' , icon = Ii , fanart = Ii1ii111i1 , themeit = Ii1I1Ii )
 ii1I1IIii11 = O0o0oO ( 'traktaddon' , 'Exodus' ) ; i1i1i1I = O0o0oO ( 'trakt' , 'Exodus' )
 if not os . path . exists ( OOOOi11i1 ) : i11I ( '[COLOR red]Addon Data: Not Installed[/COLOR]' , '' , icon = Ii , fanart = Ii1ii111i1 , menu = ii1I1IIii11 )
 elif not traktit . traktUser ( 'exodus' ) : i11I ( '[COLOR red]Addon Data: Not Registered[/COLOR]' , 'authtrakt' , 'exodus' , icon = Ii , fanart = Ii1ii111i1 , menu = ii1I1IIii11 )
 else : i11I ( '[COLOR green]Addon Data: %s[/COLOR]' % traktit . traktUser ( 'exodus' ) , 'authtrakt' , 'exodus' , icon = Ii , fanart = Ii1ii111i1 , menu = ii1I1IIii11 )
 if O0OoO000O0OO == "" : i11I ( '[COLOR red]Saved Data: Not Saved[/COLOR]' , 'savetrakt' , 'exodus' , icon = Ii , fanart = Ii1ii111i1 , menu = i1i1i1I )
 else : i11I ( '[COLOR green]Saved Data: %s[/COLOR]' % O0OoO000O0OO , '' , icon = Ii , fanart = Ii1ii111i1 , menu = i1i1i1I )
 oOoo000 = os . path . join ( oO00oOo , oOoOooOo0o0 , 'icon.png' ) if os . path . exists ( I1IIiiIiii ) else OOOiiiiI
 OooOo00o = os . path . join ( oO00oOo , oOoOooOo0o0 , 'fanart.jpg' ) if os . path . exists ( I1IIiiIiii ) else O0oo0OO0
 i11I ( '[+]-- Salts' , '' , icon = oOoo000 , fanart = OooOo00o , themeit = Ii1I1Ii )
 ii1I1IIii11 = O0o0oO ( 'traktaddon' , 'Salts' ) ; i1i1i1I = O0o0oO ( 'trakt' , 'Salts' )
 if not os . path . exists ( I1IIiiIiii ) : i11I ( '[COLOR red]Addon Data: Not Installed[/COLOR]' , '' , icon = oOoo000 , fanart = OooOo00o , menu = ii1I1IIii11 )
 elif not traktit . traktUser ( 'salts' ) : i11I ( '[COLOR red]Addon Data: Not Registered[/COLOR]' , 'authtrakt' , 'salts' , icon = oOoo000 , fanart = OooOo00o , menu = ii1I1IIii11 )
 else : i11I ( '[COLOR green]Addon Data: %s[/COLOR]' % traktit . traktUser ( 'salts' ) , 'authtrakt' , 'salts' , icon = oOoo000 , fanart = OooOo00o , menu = ii1I1IIii11 )
 if iiI1IiI == "" : i11I ( '[COLOR red]Saved Data: Not Saved[/COLOR]' , 'savetrakt' , 'salts' , icon = oOoo000 , fanart = OooOo00o , menu = i1i1i1I )
 else : i11I ( '[COLOR green]Saved Data: %s[/COLOR]' % iiI1IiI , '' , icon = oOoo000 , fanart = OooOo00o , menu = i1i1i1I )
 IiI11i1IIiiI = os . path . join ( oO00oOo , OOOO , 'icon.png' ) if os . path . exists ( O000oo0O ) else OOOiiiiI
 oOOo000oOoO0 = os . path . join ( oO00oOo , OOOO , 'fanart.jpg' ) if os . path . exists ( O000oo0O ) else O0oo0OO0
 i11I ( '[+]-- Salts HD' , '' , icon = IiI11i1IIiiI , fanart = oOOo000oOoO0 , themeit = Ii1I1Ii )
 ii1I1IIii11 = O0o0oO ( 'traktaddon' , 'Salts HD' ) ; i1i1i1I = O0o0oO ( 'trakt' , 'Salts HD' )
 if not os . path . exists ( O000oo0O ) : i11I ( '[COLOR red]Addon Data: Not Installed[/COLOR]' , '' , icon = IiI11i1IIiiI , fanart = oOOo000oOoO0 , menu = ii1I1IIii11 )
 elif not traktit . traktUser ( 'saltshd' ) : i11I ( '[COLOR red]Addon Data: Not Registered[/COLOR]' , 'authtrakt' , 'saltshd' , icon = IiI11i1IIiiI , fanart = oOOo000oOoO0 , menu = ii1I1IIii11 )
 else : i11I ( '[COLOR green]Addon Data: %s[/COLOR]' % traktit . traktUser ( 'saltshd' ) , 'authtrakt' , 'saltshd' , icon = IiI11i1IIiiI , fanart = oOOo000oOoO0 , menu = ii1I1IIii11 )
 if II == "" : i11I ( '[COLOR red]Saved Data: Not Saved[/COLOR]' , 'savetrakt' , 'saltshd' , icon = IiI11i1IIiiI , fanart = oOOo000oOoO0 , menu = i1i1i1I )
 else : i11I ( '[COLOR green]Saved Data: %s[/COLOR]' % II , '' , icon = IiI11i1IIiiI , fanart = oOOo000oOoO0 , menu = i1i1i1I )
 OoOo00o0OO = os . path . join ( oO00oOo , OOO00 , 'icon.png' ) if os . path . exists ( oo0OooOOo0 ) else OOOiiiiI
 ii1IIIIiI11 = os . path . join ( oO00oOo , OOO00 , 'fanart.jpg' ) if os . path . exists ( oo0OooOOo0 ) else O0oo0OO0
 i11I ( '[+]-- Royal We' , '' , icon = OoOo00o0OO , fanart = ii1IIIIiI11 , themeit = Ii1I1Ii )
 ii1I1IIii11 = O0o0oO ( 'traktaddon' , 'Royal We' ) ; i1i1i1I = O0o0oO ( 'trakt' , 'Royal We' )
 if not os . path . exists ( oo0OooOOo0 ) : i11I ( '[COLOR red]Addon Data: Not Installed[/COLOR]' , '' , icon = OoOo00o0OO , fanart = ii1IIIIiI11 , menu = ii1I1IIii11 )
 elif not traktit . traktUser ( 'royalwe' ) : i11I ( '[COLOR red]Addon Data: Not Registered[/COLOR]' , 'authtrakt' , 'royalwe' , icon = OoOo00o0OO , fanart = ii1IIIIiI11 , menu = ii1I1IIii11 )
 else : i11I ( '[COLOR green]Addon Data: %s[/COLOR]' % traktit . traktUser ( 'royalwe' ) , 'authtrakt' , 'royalwe' , icon = OoOo00o0OO , fanart = ii1IIIIiI11 , menu = ii1I1IIii11 )
 if ooOoOoo0O == "" : i11I ( '[COLOR red]Saved Data: Not Saved[/COLOR]' , 'savetrakt' , 'royalwe' , icon = OoOo00o0OO , fanart = ii1IIIIiI11 , menu = i1i1i1I )
 else : i11I ( '[COLOR green]Saved Data: %s[/COLOR]' % ooOoOoo0O , '' , icon = OoOo00o0OO , fanart = ii1IIIIiI11 , menu = i1i1i1I )
 iI1IIIii = os . path . join ( oO00oOo , IIiiiiiiIi1I1 , 'icon.png' ) if os . path . exists ( IIIii1II1II ) else OOOiiiiI
 I1i11ii11 = os . path . join ( oO00oOo , IIiiiiiiIi1I1 , 'fanart.jpg' ) if os . path . exists ( IIIii1II1II ) else O0oo0OO0
 i11I ( '[+]-- Velocity' , '' , icon = iI1IIIii , fanart = I1i11ii11 , themeit = Ii1I1Ii )
 ii1I1IIii11 = O0o0oO ( 'traktaddon' , 'Velocity' ) ; i1i1i1I = O0o0oO ( 'trakt' , 'Velocity' )
 if not os . path . exists ( IIIii1II1II ) : i11I ( '[COLOR red]Addon Data: Not Installed[/COLOR]' , '' , icon = iI1IIIii , fanart = I1i11ii11 , menu = ii1I1IIii11 )
 elif not traktit . traktUser ( 'velocity' ) : i11I ( '[COLOR red]Addon Data: Not Registered[/COLOR]' , 'authtrakt' , 'velocity' , icon = iI1IIIii , fanart = I1i11ii11 , menu = ii1I1IIii11 )
 else : i11I ( '[COLOR green]Addon Data: %s[/COLOR]' % traktit . traktUser ( 'velocity' ) , 'authtrakt' , 'velocity' , icon = iI1IIIii , fanart = I1i11ii11 , menu = ii1I1IIii11 )
 if OooO0 == "" : i11I ( '[COLOR red]Saved Data: Not Saved[/COLOR]' , 'savetrakt' , 'velocity' , icon = iI1IIIii , fanart = I1i11ii11 , menu = i1i1i1I )
 else : i11I ( '[COLOR green]Saved Data: %s[/COLOR]' % OooO0 , '' , icon = iI1IIIii , fanart = I1i11ii11 , menu = i1i1i1I )
 OO00O0oOO = os . path . join ( oO00oOo , I1IIIii , 'icon.png' ) if os . path . exists ( i1I1iI ) else OOOiiiiI
 Ii1iI111 = os . path . join ( oO00oOo , I1IIIii , 'fanart.jpg' ) if os . path . exists ( i1I1iI ) else O0oo0OO0
 i11I ( '[+]-- Velocity Kids' , '' , icon = OO00O0oOO , fanart = Ii1iI111 , themeit = Ii1I1Ii )
 ii1I1IIii11 = O0o0oO ( 'traktaddon' , 'Velocity Kids' ) ; i1i1i1I = O0o0oO ( 'trakt' , 'Velocity Kids' )
 if not os . path . exists ( i1I1iI ) : i11I ( '[COLOR red]Addon Data: Not Installed[/COLOR]' , '' , icon = OO00O0oOO , fanart = Ii1iI111 , menu = ii1I1IIii11 )
 elif not traktit . traktUser ( 'velocitykids' ) : i11I ( '[COLOR red]Addon Data: Not Registered[/COLOR]' , 'authtrakt' , 'velocitykids' , icon = OO00O0oOO , fanart = Ii1iI111 , menu = ii1I1IIii11 )
 else : i11I ( '[COLOR green]Addon Data: %s[/COLOR]' % traktit . traktUser ( 'velocitykids' ) , 'authtrakt' , 'velocitykids' , icon = OO00O0oOO , fanart = Ii1iI111 , menu = ii1I1IIii11 )
 if II11iiii1Ii == "" : i11I ( '[COLOR red]Saved Data: Not Saved[/COLOR]' , 'savetrakt' , 'velocitykids' , icon = OO00O0oOO , fanart = Ii1iI111 , menu = i1i1i1I )
 else : i11I ( '[COLOR green]Saved Data: %s[/COLOR]' % II11iiii1Ii , '' , icon = OO00O0oOO , fanart = Ii1iI111 , menu = i1i1i1I )
 O0oooo00o0Oo = os . path . join ( oO00oOo , iiiiiIIii , 'icon.png' ) if os . path . exists ( o0OO00oO ) else OOOiiiiI
 I1iii = os . path . join ( oO00oOo , iiiiiIIii , 'fanart.jpg' ) if os . path . exists ( o0OO00oO ) else O0oo0OO0
 i11I ( '[+]-- Specto' , '' , icon = O0oooo00o0Oo , fanart = I1iii , themeit = Ii1I1Ii )
 ii1I1IIii11 = O0o0oO ( 'traktaddon' , 'Specto' ) ; i1i1i1I = O0o0oO ( 'trakt' , 'Specto' )
 if not os . path . exists ( o0OO00oO ) : i11I ( '[COLOR red]Addon Data: Not Installed[/COLOR]' , '' , icon = O0oooo00o0Oo , fanart = I1iii , menu = ii1I1IIii11 )
 elif not traktit . traktUser ( 'specto' ) : i11I ( '[COLOR red]Addon Data: Not Registered[/COLOR]' , 'authtrakt' , 'specto' , icon = O0oooo00o0Oo , fanart = I1iii , menu = ii1I1IIii11 )
 else : i11I ( '[COLOR green]Addon Data: %s[/COLOR]' % traktit . traktUser ( 'specto' ) , 'authtrakt' , 'specto' , icon = O0oooo00o0Oo , fanart = I1iii , menu = ii1I1IIii11 )
 if OO0oOoo == "" : i11I ( '[COLOR red]Saved Data: Not Saved[/COLOR]' , 'savetrakt' , 'specto' , icon = O0oooo00o0Oo , fanart = I1iii , menu = i1i1i1I )
 else : i11I ( '[COLOR green]Saved Data: %s[/COLOR]' % OO0oOoo , '' , icon = O0oooo00o0Oo , fanart = I1iii , menu = i1i1i1I )
 oO0o0O0Ooo0o = os . path . join ( oO00oOo , O000OO0 , 'icon.png' ) if os . path . exists ( I11i1I1I ) else OOOiiiiI
 i1Ii11II = os . path . join ( oO00oOo , O000OO0 , 'fanart.jpg' ) if os . path . exists ( I11i1I1I ) else O0oo0OO0
 i11I ( '[+]-- Trakt' , '' , icon = OO00O0oOO , fanart = i1Ii11II , themeit = Ii1I1Ii )
 ii1I1IIii11 = O0o0oO ( 'traktaddon' , 'Trakt' ) ; i1i1i1I = O0o0oO ( 'trakt' , 'Trakt' )
 if not os . path . exists ( I11i1I1I ) : i11I ( '[COLOR red]Addon Data: Not Installed[/COLOR]' , '' , icon = oO0o0O0Ooo0o , fanart = i1Ii11II , menu = ii1I1IIii11 )
 elif not traktit . traktUser ( 'trakt' ) : i11I ( '[COLOR red]Addon Data: Not Registered[/COLOR]' , 'authtrakt' , 'trakt' , icon = oO0o0O0Ooo0o , fanart = i1Ii11II , menu = ii1I1IIii11 )
 else : i11I ( '[COLOR green]Addon Data: %s[/COLOR]' % traktit . traktUser ( 'trakt' ) , 'authtrakt' , 'trakt' , icon = oO0o0O0Ooo0o , fanart = i1Ii11II , menu = ii1I1IIii11 )
 if O0o0Oo == "" : i11I ( '[COLOR red]Saved Data: Not Saved[/COLOR]' , 'savetrakt' , 'trakt' , icon = oO0o0O0Ooo0o , fanart = i1Ii11II , menu = i1i1i1I )
 else : i11I ( '[COLOR green]Saved Data: %s[/COLOR]' % O0o0Oo , '' , icon = oO0o0O0Ooo0o , fanart = i1Ii11II , menu = i1i1i1I )
 if OoOoO == 'No' : i11I ( '============================================' , '' , themeit = Ii1I1Ii )
 i11I ( 'Save All Trakt Data' , 'savetrakt' , 'all' , icon = OOOiiiiI , themeit = Ii1I1Ii )
 i11I ( 'Recover All Saved Trakt Data' , 'restoretrakt' , 'all' , icon = OOOiiiiI , themeit = Ii1I1Ii )
 i11I ( 'Clear All Saved Trakt Data' , 'cleartrakt' , 'all' , icon = OOOiiiiI , themeit = Ii1I1Ii )
 i11I ( 'Clear All Addon Data' , 'addontrakt' , 'all' , icon = OOOiiiiI , themeit = Ii1I1Ii )
 o00Oo0oooooo ( 'movies' , 'MAIN' )
 if 18 - 18: O0OooOo0o . I1111i % o0oooOO00 % O0O00O0
def II1IiiIii ( ) :
 iIiiiii1i = '[COLOR green]ON[/COLOR]' if oOOoO0 == 'true' else '[COLOR red]OFF[/COLOR]'
 oOOOO = str ( oooOOOOO ) if not oooOOOOO == '' else 'Real Debrid hasnt been saved yet.'
 i11I ( '[I]http://real-debrid.com is a PAID service.[/I]' , '' , icon = OOOiiiiI , themeit = Ii1I1Ii )
 i11I ( 'Save Real Debrid Data: %s' % iIiiiii1i , 'togglesetting' , 'KEEPREAL' , icon = iIiIi11 , themeit = Ii1I1Ii )
 if oOOoO0 == 'true' : i11I ( 'Last Save: %s' % str ( oOOOO ) , '' , icon = iIiIi11 , themeit = Ii1I1Ii )
 if OoOoO == 'No' : i11I ( '============================================' , '' , icon = iIiIi11 , themeit = Ii1I1Ii )
 Ii = os . path . join ( oO00oOo , ooooooO0oo , 'icon.png' ) if os . path . exists ( OOOOi11i1 ) else iIiIi11
 Ii1ii111i1 = os . path . join ( oO00oOo , ooooooO0oo , 'fanart.jpg' ) if os . path . exists ( OOOOi11i1 ) else O0oo0OO0
 oOo0OoOOo0 = debridit . debridUser ( 'exodus' )
 i11I ( '[+]-- Exodus' , '' , icon = Ii , fanart = Ii1ii111i1 , themeit = Ii1I1Ii )
 ii1I1IIii11 = O0o0oO ( 'debridaddon' , 'Exodus' ) ; i1i1i1I = O0o0oO ( 'debrid' , 'Exodus' )
 if not os . path . exists ( OOOOi11i1 ) : i11I ( '[COLOR red]Addon Data: Not Installed[/COLOR]' , '' , icon = Ii , fanart = Ii1ii111i1 , menu = ii1I1IIii11 )
 elif not oOo0OoOOo0 : i11I ( '[COLOR red]Addon Data: Not Registered[/COLOR]' , 'authdebrid' , 'exodus' , icon = Ii , fanart = Ii1ii111i1 , menu = ii1I1IIii11 )
 else : i11I ( '[COLOR green]Addon Data: %s[/COLOR]' % oOo0OoOOo0 , 'authdebrid' , 'exodus' , icon = Ii , fanart = Ii1ii111i1 , menu = ii1I1IIii11 )
 if Oo00OOOOO == "" : i11I ( '[COLOR red]Saved Data: Not Saved[/COLOR]' , 'savedebrid' , 'exodus' , icon = Ii , fanart = Ii1ii111i1 , menu = i1i1i1I )
 else : i11I ( '[COLOR green]Saved Data: %s[/COLOR]' % Oo00OOOOO , '' , icon = Ii , fanart = Ii1ii111i1 , menu = i1i1i1I )
 O0oooo00o0Oo = os . path . join ( oO00oOo , iiiiiIIii , 'icon.png' ) if os . path . exists ( o0OO00oO ) else iIiIi11
 I1iii = os . path . join ( oO00oOo , iiiiiIIii , 'fanart.jpg' ) if os . path . exists ( o0OO00oO ) else O0oo0OO0
 iII11I1Ii1 = debridit . debridUser ( 'specto' )
 i11I ( '[+]-- Specto' , '' , icon = O0oooo00o0Oo , fanart = I1iii , themeit = Ii1I1Ii )
 ii1I1IIii11 = O0o0oO ( 'debridaddon' , 'Specto' ) ; i1i1i1I = O0o0oO ( 'debrid' , 'Specto' )
 if not os . path . exists ( o0OO00oO ) : i11I ( '[COLOR red]Addon Data: Not Installed[/COLOR]' , '' , icon = O0oooo00o0Oo , fanart = I1iii , menu = ii1I1IIii11 )
 elif not iII11I1Ii1 : i11I ( '[COLOR red]Addon Data: Not Registered[/COLOR]' , 'authdebrid' , 'specto' , icon = O0oooo00o0Oo , fanart = I1iii , menu = ii1I1IIii11 )
 else : i11I ( '[COLOR green]Addon Data: %s[/COLOR]' % iII11I1Ii1 , 'authdebrid' , 'specto' , icon = O0oooo00o0Oo , fanart = I1iii , menu = ii1I1IIii11 )
 if O0O == "" : i11I ( '[COLOR red]Saved Data: Not Saved[/COLOR]' , 'savedebrid' , 'specto' , icon = O0oooo00o0Oo , fanart = I1iii , menu = i1i1i1I )
 else : i11I ( '[COLOR green]Saved Data: %s[/COLOR]' % O0O , '' , icon = O0oooo00o0Oo , fanart = I1iii , menu = i1i1i1I )
 o0o0 = os . path . join ( oO00oOo , I11iii1Ii , 'icon.png' ) if os . path . exists ( oO0Oo ) else iIiIi11
 oOo0oO = os . path . join ( oO00oOo , I11iii1Ii , 'fanart.jpg' ) if os . path . exists ( oO0Oo ) else O0oo0OO0
 IIi1IIIIi = debridit . debridUser ( 'url' )
 i11I ( '[+]-- URL Resolver' , '' , icon = o0o0 , fanart = oOo0oO , themeit = Ii1I1Ii )
 ii1I1IIii11 = O0o0oO ( 'debridaddon' , 'url' ) ; i1i1i1I = O0o0oO ( 'debrid' , 'url' )
 if not os . path . exists ( oO0Oo ) : i11I ( '[COLOR red]Addon Data: Not Installed[/COLOR]' , '' , icon = o0o0 , fanart = oOo0oO , menu = ii1I1IIii11 )
 elif not IIi1IIIIi : i11I ( '[COLOR red]Addon Data: Not Registered[/COLOR]' , 'authdebrid' , 'url' , icon = o0o0 , fanart = oOo0oO , menu = ii1I1IIii11 )
 else : i11I ( '[COLOR green]Addon Data: %s[/COLOR]' % IIi1IIIIi , 'authdebrid' , 'url' , icon = o0o0 , fanart = oOo0oO , menu = ii1I1IIii11 )
 if O00o0OO == "" : i11I ( '[COLOR red]Saved Data: Not Saved[/COLOR]' , 'savedebrid' , 'url' , icon = o0o0 , fanart = oOo0oO , menu = i1i1i1I )
 else : i11I ( '[COLOR green]Saved Data: %s[/COLOR]' % O00o0OO , '' , icon = o0o0 , fanart = oOo0oO , menu = i1i1i1I )
 if OoOoO == 'No' : i11I ( '============================================' , '' , themeit = Ii1I1Ii )
 i11I ( 'Save All Real Debrid Data' , 'savedebrid' , 'all' , icon = iIiIi11 , themeit = Ii1I1Ii )
 i11I ( 'Recover All Saved Real Debrid Data' , 'restoredebrid' , 'all' , icon = iIiIi11 , themeit = Ii1I1Ii )
 i11I ( 'Clear All Saved Real Debrid Data' , 'cleardebrid' , 'all' , icon = iIiIi11 , themeit = Ii1I1Ii )
 i11I ( 'Clear All Addon Data' , 'addondebrid' , 'all' , icon = iIiIi11 , themeit = Ii1I1Ii )
 o00Oo0oooooo ( 'movies' , 'MAIN' )
 if 70 - 70: OOOoO00 / O0OooOo0o - Iii - OoOO0o
def IiiiIi1i ( ) :
 for i1ii in glob . glob ( os . path . join ( oO00oOo , '*/' ) ) :
  O0ooO0ooo0oO = i1ii . replace ( oO00oOo , '' ) . replace ( '\\' , '' ) . replace ( '/' , '' )
  IIIIiii1IIii = os . path . join ( i1ii , 'icon.png' )
  II1i11I = os . path . join ( i1ii , 'fanart.png' )
  if O0ooO0ooo0oO in oOOoo0Oo : pass
  elif O0ooO0ooo0oO == 'packages' : pass
  else :
   iioo0o0OoOOO = O0ooO0ooo0oO
   ooO0oO00O0o = { 'audio.' : '[COLOR orange][AUDIO] [/COLOR]' , 'metadata.' : '[COLOR cyan][METADATA] [/COLOR]' , 'module.' : '[COLOR orange][MODULE] [/COLOR]' , 'plugin.' : '[COLOR blue][PLUGIN] [/COLOR]' , 'program.' : '[COLOR orange][PROGRAM] [/COLOR]' , 'repository.' : '[COLOR gold][REPO] [/COLOR]' , 'script.' : '[COLOR green][SCRIPT] [/COLOR]' , 'service.' : '[COLOR green][SERVICE] [/COLOR]' , 'skin.' : '[COLOR dodgerblue][SKIN] [/COLOR]' , 'video.' : '[COLOR orange][VIDEO] [/COLOR]' , 'weather.' : '[COLOR yellow][WEATHER] [/COLOR]' }
   for ooOO00oOOo000 in ooO0oO00O0o :
    iioo0o0OoOOO = iioo0o0OoOOO . replace ( ooOO00oOOo000 , ooO0oO00O0o [ ooOO00oOOo000 ] )
   i11I ( '[COLOR red][B][REMOVE][/B][/COLOR] %s' % iioo0o0OoOOO , 'removeaddon' , O0ooO0ooo0oO , icon = IIIIiii1IIii , fanart = II1i11I , themeit = oOooO0 )
   if 14 - 14: O0OO . O0OooOo0o . IIiIi11i1i / O0O00O0 % oOOOoo00 - oo00oO0o
def o0oOoO0O ( ) :
 if os . path . exists ( Oo0O ) :
  i11I ( '[COLOR red][B][REMOVE][/B][/COLOR] All Addon_Data' , 'removedata' , 'all' , themeit = oOooO0 )
  i11I ( '[COLOR red][B][REMOVE][/B][/COLOR] All Addon_Data for Uninstalled Addons' , 'removedata' , 'uninstalled' , themeit = oOooO0 )
  i11I ( '[COLOR red][B][REMOVE][/B][/COLOR] All Empty Folders in Addon_Data' , 'removedata' , 'empty' , themeit = oOooO0 )
  i11I ( '[COLOR red][B][REMOVE][/B][/COLOR] %s Addon_Data' % Oo0Ooo , 'resetaddon' , themeit = oOooO0 )
  if OoOoO == 'No' : i11I ( '============================================' , '' , themeit = Ii1I1Ii )
  for i1ii in glob . glob ( os . path . join ( Oo0O , '*' ) ) :
   O0ooO0ooo0oO = i1ii . replace ( Oo0O , '' ) . replace ( '\\' , '' ) . replace ( '/' , '' )
   IIIIiii1IIii = os . path . join ( i1ii . replace ( Oo0O , oO00oOo ) , 'icon.png' )
   II1i11I = os . path . join ( i1ii . replace ( Oo0O , oO00oOo ) , 'fanart.png' )
   iioo0o0OoOOO = O0ooO0ooo0oO
   ooO0oO00O0o = { 'audio.' : '[COLOR orange][AUDIO] [/COLOR]' , 'metadata.' : '[COLOR cyan][METADATA] [/COLOR]' , 'module.' : '[COLOR orange][MODULE] [/COLOR]' , 'plugin.' : '[COLOR blue][PLUGIN] [/COLOR]' , 'program.' : '[COLOR orange][PROGRAM] [/COLOR]' , 'repository.' : '[COLOR gold][REPO] [/COLOR]' , 'script.' : '[COLOR green][SCRIPT] [/COLOR]' , 'service.' : '[COLOR green][SERVICE] [/COLOR]' , 'skin.' : '[COLOR dodgerblue][SKIN] [/COLOR]' , 'video.' : '[COLOR orange][VIDEO] [/COLOR]' , 'weather.' : '[COLOR yellow][WEATHER] [/COLOR]' }
   for ooOO00oOOo000 in ooO0oO00O0o :
    iioo0o0OoOOO = iioo0o0OoOOO . replace ( ooOO00oOOo000 , ooO0oO00O0o [ ooOO00oOOo000 ] )
   if O0ooO0ooo0oO in oOOoo0Oo : iioo0o0OoOOO = '[COLOR green][B][PROTECTED][/B][/COLOR] %s' % iioo0o0OoOOO
   else : iioo0o0OoOOO = '[COLOR red][B][REMOVE][/B][/COLOR] %s' % iioo0o0OoOOO
   i11I ( ' %s' % iioo0o0OoOOO , 'removedata' , O0ooO0ooo0oO , icon = IIIIiii1IIii , fanart = II1i11I , themeit = oOooO0 )
 else :
  i11I ( 'No Addon data folder found.' , '' , themeit = Ii1I1Ii )
  if 84 - 84: O0OoOO0o * I1111i - iII1iIi11i * iII1iIi11i
  if 8 - 8: oo00oO0o / Oo0OO . IIIIiiIiiI
  if 41 - 41: OoOO0o + O0OO
def oOOiiiIIiIi ( ) :
 I1i ( 'Backup Restore' , 'bre' , icon = I1i1iiI1 , themeit = O0O0OOOOoo )
 i11I ( 'Convert Paths to special' , 'convertpath' , icon = I1i1iiI1 , themeit = O0O0OOOOoo )
 i11I ( 'Test Notifications' , 'testnotify' , icon = I1i1iiI1 , themeit = O0O0OOOOoo )
 if 68 - 68: O0OoOO0o + o0oooOO00 / IIIIiiIiiI - OOOoO00 + Iii % O0O00O0
 if 23 - 23: oo00oO0o % IIiii / IIiIi11i1i
 if 5 - 5: Iii
 if 72 - 72: IIIIiiIiiI . IiiiiI1i1Iii / o0oooOO00 + IIiIi11i1i % Iii
 if 42 - 42: oOOOoo00 * o0oooOO00 % oo00oO0o - o0oooOO00 . i11iIiiIii - IiiiiI1i1Iii
def o0oO0oOO ( name , type , theme = None ) :
 if type == 'gui' :
  if name == o00 :
   O000o0 = ooo0OO . yesno ( Oo0Ooo , 'Would you like to apply the guifix for:' , '%s?' % name , nolabel = 'No, Cancel' , yeslabel = 'Yes, Apply Fix' )
  else :
   O000o0 = ooo0OO . yesno ( "%s - [COLOR red]WARNING!![/COLOR]" % Oo0Ooo , "%s SpinzTV build is not currently installed." % name , "Would you like to apply the guiFix anyways?." , yeslabel = "Yes, Apply" , nolabel = "No, Cancel" )
  if O000o0 :
   oO0o000OoOoO0 = wiz . checkBuild ( name , 'gui' )
   OO0ooOOO0O00o = name . replace ( '\\' , '' ) . replace ( '/' , '' ) . replace ( ':' , '' ) . replace ( '*' , '' ) . replace ( '?' , '' ) . replace ( '"' , '' ) . replace ( '<' , '' ) . replace ( '>' , '' ) . replace ( '|' , '' )
   if not wiz . workingURL ( oO0o000OoOoO0 ) == True : wiz . LogNotify ( Oo0Ooo , 'guiFix: [COLOR red]Invalid Zip Url![/COLOR]' ) ; return
   if not os . path . exists ( IiIi11iIIi1Ii ) : os . makedirs ( IiIi11iIIi1Ii )
   II1 . create ( Oo0Ooo , 'Downloading %s GuiFix' % name , '' , 'Please Wait' )
   Ooo0o0oo = os . path . join ( IiIi11iIIi1Ii , '%s_guisettings.zip' % OO0ooOOO0O00o )
   try : os . remove ( Ooo0o0oo )
   except : pass
   downloader . download ( oO0o000OoOoO0 , Ooo0o0oo , II1 )
   xbmc . sleep ( 500 )
   II1 . update ( 0 , "" , "Installing %s GuiFix" % name )
   extract . all ( Ooo0o0oo , OOOo0 , II1 )
   II1 . close ( )
   wiz . killxbmc ( )
  else :
   wiz . LogNotify ( Oo0Ooo , 'guiFix: [COLOR red]Cancelled![/COLOR]' )
 elif type == 'fresh' :
  Ii1i1i1111 ( name )
 elif type == 'normal' :
  if IiIi1I1 == 'normal' :
   if iIii1 == 'true' :
    traktit . autoUpdate ( 'all' )
    wiz . setS ( 'traktlastsave' , str ( I11II1i ) )
   if oOOoO0 == 'true' :
    debridit . autoUpdate ( 'all' )
    wiz . setS ( 'debridlastsave' , str ( I11II1i ) )
  if IIIII < 17.0 and float ( wiz . checkBuild ( name , 'kodi' ) ) >= 17.0 :
   O000o0 = ooo0OO . yesno ( "%s - [COLOR red]WARNING!![/COLOR]" % Oo0Ooo , 'There is a chance that the skin will not appear correctly' , 'When installing a %s build on a Kodi %s install' % ( wiz . checkBuild ( name , 'kodi' ) , IIIII ) , 'Would you still like to install: %s v%s?' % ( name , wiz . checkBuild ( name , 'version' ) ) , nolabel = 'No, Cancel' , yeslabel = 'Yes, Install' )
  else :
   O000o0 = ooo0OO . yesno ( Oo0Ooo , 'By downloading or using you are agreeing that the author takes no resposibility for the content or reliability of any of the addons included.  The author does not host, distribute or have any control over any of the content that may be provided by any addon. It is the users responsibility to ensure the legality of use within their country. By continuing you are agreeing to the terms and conditions herin. Would you still like to install:' , '%s v%s?' % ( name , wiz . checkBuild ( name , 'version' ) ) , nolabel = 'Disagree, Cancel' , yeslabel = 'Agree, Install' )
  if O000o0 :
   oO0o000OoOoO0 = wiz . checkBuild ( name , 'url' )
   OO0ooOOO0O00o = name . replace ( '\\' , '' ) . replace ( '/' , '' ) . replace ( ':' , '' ) . replace ( '*' , '' ) . replace ( '?' , '' ) . replace ( '"' , '' ) . replace ( '<' , '' ) . replace ( '>' , '' ) . replace ( '|' , '' )
   if not wiz . workingURL ( oO0o000OoOoO0 ) == True : wiz . LogNotify ( Oo0Ooo , 'Build Install: [COLOR red]Invalid Zip Url![/COLOR]' ) ; return
   if not os . path . exists ( IiIi11iIIi1Ii ) : os . makedirs ( IiIi11iIIi1Ii )
   II1 . create ( Oo0Ooo , 'Downloading %s ' % name , '' , 'Please Wait' )
   Ooo0o0oo = os . path . join ( IiIi11iIIi1Ii , '%s.zip' % OO0ooOOO0O00o )
   try : os . remove ( Ooo0o0oo )
   except : pass
   downloader . download ( oO0o000OoOoO0 , Ooo0o0oo , II1 )
   xbmc . sleep ( 500 )
   II1 . update ( 0 , "" , "Installing %s " % name )
   o0oO0O00oOo = extract . all ( Ooo0o0oo , O00ooooo00 , II1 )
   I1111I1II11 , iiiIIIIiIi , IiiIIIII1iii = o0oO0O00oOo . split ( '/' , 3 )
   wiz . setS ( 'buildname' , name )
   wiz . setS ( 'buildversion' , wiz . checkBuild ( name , 'version' ) )
   wiz . setS ( 'buildtheme' , '' )
   wiz . setS ( 'latestversion' , wiz . checkBuild ( name , 'version' ) )
   wiz . setS ( 'lastbuildcheck' , str ( Iii1I1I11iiI1 ) )
   wiz . setS ( 'installed' , 'true' )
   wiz . setS ( 'extract' , str ( I1111I1II11 ) )
   wiz . setS ( 'errors' , str ( iiiIIIIiIi ) )
   wiz . log ( 'INSTALLED %s: [ERRORS:%s]' % ( I1111I1II11 , iiiIIIIiIi ) )
   if int ( iiiIIIIiIi ) >= 1 :
    IIiiii = ooo0OO . yesno ( Oo0Ooo , 'INSTALLED %s: [ERRORS:%s]' % ( I1111I1II11 , iiiIIIIiIi ) , 'Would you like to view the errors?' , nolabel = 'No, Cancel' , yeslabel = 'Yes, View' )
    if IIiiii :
     wiz . TextBoxes ( Oo0Ooo , IiiIIIII1iii . replace ( '\t' , '' ) ) ; xbmc . sleep ( 3000 )
   II1 . close ( )
   O00Oooo = wiz . checkBuild ( name , 'theme' )
   if not O00Oooo == 'http://' and wiz . workingURL ( O00Oooo ) == True : o0oO0oOO ( name , 'theme' )
   ooo0OO . ok ( Oo0Ooo , "To save changes you now need to force close Kodi, Press OK to force close Kodi" )
   wiz . killxbmc ( )
  else :
   wiz . LogNotify ( Oo0Ooo , 'Build Install: [COLOR red]Cancelled![/COLOR]' )
 elif type == 'theme' :
  if theme == None :
   O00Oooo = wiz . checkBuild ( name , 'theme' )
   iI111i1I1II = [ ]
   if not O00Oooo == 'http://' and wiz . workingURL ( O00Oooo ) == True :
    i1I1i1 = wiz . openURL ( O00Oooo ) . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
    O0OoooO0 = re . compile ( 'name="(.+?)"' ) . findall ( i1I1i1 )
    if len ( O0OoooO0 ) > 0 :
     if ooo0OO . yesno ( Oo0Ooo , "The Build [%s] comes with %s different themes" % ( name , len ( O0OoooO0 ) ) , "Would you like to install one now?" , yeslabel = "Yes, Install" , nolabel = "No Thanks" ) :
      for OOooo0O0o0 in O0OoooO0 :
       iI111i1I1II . append ( OOooo0O0o0 )
      wiz . log ( "Theme List: %s " % str ( iI111i1I1II ) )
      O00OO = ooo0OO . select ( Oo0Ooo , iI111i1I1II )
      wiz . log ( "Theme install selected: %s" % O00OO )
      if not O00OO == - 1 : theme = iI111i1I1II [ O00OO ] ; II1Ii1iI1i1 = True
      else : wiz . LogNotify ( Oo0Ooo , 'Theme Install: [COLOR red]Cancelled![/COLOR]' ) ; return
     else : wiz . LogNotify ( Oo0Ooo , 'Theme Install: [COLOR red]Cancelled![/COLOR]' ) ; return
   else : wiz . LogNotify ( Oo0Ooo , 'Theme Install: [COLOR red]None Found![/COLOR]' )
  else : II1Ii1iI1i1 = ooo0OO . yesno ( Oo0Ooo , 'Would you like to install the theme:' , theme , 'for %s v%s?' % ( name , wiz . checkBuild ( name , 'version' ) ) , nolabel = 'No, Cancel' , yeslabel = 'Yes, Install' )
  if II1Ii1iI1i1 :
   o0OoO000O = wiz . checkTheme ( name , theme , 'url' )
   OO0ooOOO0O00o = name . replace ( '\\' , '' ) . replace ( '/' , '' ) . replace ( ':' , '' ) . replace ( '*' , '' ) . replace ( '?' , '' ) . replace ( '"' , '' ) . replace ( '<' , '' ) . replace ( '>' , '' ) . replace ( '|' , '' )
   if not wiz . workingURL ( o0OoO000O ) == True : wiz . LogNotify ( Oo0Ooo , 'Theme Install: [COLOR red]Invalid Zip Url![/COLOR]' ) ; return
   if not os . path . exists ( IiIi11iIIi1Ii ) : os . makedirs ( IiIi11iIIi1Ii )
   II1 . create ( Oo0Ooo , 'Downloading %s ' % name , '' , 'Please Wait' )
   Ooo0o0oo = os . path . join ( IiIi11iIIi1Ii , '%s.zip' % OO0ooOOO0O00o )
   try : os . remove ( Ooo0o0oo )
   except : pass
   downloader . download ( o0OoO000O , Ooo0o0oo , II1 )
   xbmc . sleep ( 500 )
   II1 . update ( 0 , "" , "Installing %s " % name )
   o0oO0O00oOo = extract . all ( Ooo0o0oo , O00ooooo00 , II1 )
   I1111I1II11 , iiiIIIIiIi , IiiIIIII1iii = o0oO0O00oOo . split ( '/' , 3 )
   wiz . setS ( 'buildtheme' , theme )
   wiz . log ( 'INSTALLED %s: [ERRORS:%s]' % ( I1111I1II11 , iiiIIIIiIi ) )
   II1 . close ( )
   if IiIi1I1 not in [ "fresh" , "normal" ] : xbmc . executebuiltin ( "ReloadSkin()" ) ; xbmc . sleep ( 1000 ) ; xbmc . executebuiltin ( "Container.Refresh" )
  else :
   wiz . LogNotify ( Oo0Ooo , 'Theme Install: [COLOR red]Cancelled![/COLOR]' )
   if 94 - 94: o0oooOO00 . O0OoOO0o / O0O00O0 . oOOOoo00 - Oo0OO
   if 26 - 26: O0OO - OOOoO00 . IIiii
   if 65 - 65: oOOOoo00 % O0OoOO0o % Iii * O0O00O0
   if 31 - 31: O0O00O0
def iIIiI1I1i ( apk , url ) :
 if wiz . platform ( ) == 'android' :
  if apk in [ 'kodi' , 'spmc' ] :
   IIiiii = ooo0OO . yesno ( Oo0Ooo , "Would you like to download and install:" , "%s (v%s)" % ( apk . upper ( ) , wiz . latestApk ( apk , 'version' ) ) )
   if not IIiiii : wiz . LogNotify ( Oo0Ooo , '[COLOR red]ERROR:[/COLOR] Install Cancelled' ) ; return
   O0O0OOooOO0 = "%s v%s" % ( apk . upper ( ) , wiz . latestApk ( apk , 'version' ) )
  else :
   IIiiii = ooo0OO . yesno ( Oo0Ooo , "Would you like to download and install:" , "%s" % apk )
   if not IIiiii : wiz . LogNotify ( Oo0Ooo , '[COLOR red]ERROR:[/COLOR] Install Cancelled' ) ; return
   O0O0OOooOO0 = apk
  if IIiiii :
   if not os . path . exists ( IiIi11iIIi1Ii ) : os . makedirs ( IiIi11iIIi1Ii )
   if not wiz . workingURL ( url ) == True : wiz . LogNotify ( Oo0Ooo , 'APK Installer: [COLOR red]Invalid Apk Url![/COLOR]' ) ; return
   II1 . create ( Oo0Ooo , 'Downloading %s' % O0O0OOooOO0 , '' , 'Please Wait' )
   Ooo0o0oo = os . path . join ( IiIi11iIIi1Ii , "%s.apk" % apk )
   try : os . remove ( Ooo0o0oo )
   except : pass
   downloader . download ( url , Ooo0o0oo , II1 )
   xbmc . sleep ( 500 )
   II1 . close ( )
   ooo0OO . ok ( Oo0Ooo , "Launching the APK to be installed" , "Follow the install process to complete." )
   xbmc . executebuiltin ( 'StartAndroidActivity("","android.intent.action.VIEW","application/vnd.android.package-archive","file:' + Ooo0o0oo + '")' )
  else : wiz . LogNotify ( Oo0Ooo , '[COLOR red]ERROR:[/COLOR] Install Cancelled' )
 else : wiz . LogNotify ( Oo0Ooo , '[COLOR red]ERROR:[/COLOR] None Android Device' )
 if 31 - 31: i1ii1I1111ii1 * IIIIiiIiiI + I1111i - OoOO0o / I1111i
 if 19 - 19: iII1iIi11i * oo00oO0o * IIiii + O0OoOO0o / O0OoOO0o
 if 73 - 73: Iii / Iii - IIIIiiIiiI
 if 91 - 91: IIIIiiIiiI + i1ii1I1111ii1
def OoOooo ( name , url , ) :
 if "NULL" in url :
  oo00OOoOoO00 = xbmcgui . Dialog ( )
  ooo0OO . ok ( Oo0Ooo , "[COLOR ghostwhite]Not a valid selection, please try again.[/COLOR]" )
  sys . exit ( 1 )
  if 15 - 15: iII1iIi11i / O0OoOO0o . IIiii . i11iIiiIii
 o0OO0O0Oo = xbmc . translatePath ( os . path . join ( '/storage/emulated/0/Download' , '' ) )
 OOOOO = xbmcgui . DialogProgress ( )
 OOOOO . create ( Oo0Ooo , "" , "" , 'APK: ' + name )
 Ooo0o0oo = os . path . join ( o0OO0O0Oo , name + '.smc' )
 downloader . download ( url , Ooo0o0oo , OOOOO )
 oo00OOoOoO00 = xbmcgui . Dialog ( )
 oo00OOoOoO00 . ok ( Oo0Ooo , "[COLOR yellow]Download complete, ROM Location: [/COLOR][COLOR white]" + Ooo0o0oo + "[/COLOR]" )
 if 67 - 67: IIIIiiIiiI % IIiii . I1111i + OOOoO00 * IIiIi11i1i * o0oooOO00
def iiIii1I ( name , url , ) :
 if "NULL" in url :
  oo00OOoOoO00 = xbmcgui . Dialog ( )
  ooo0OO . ok ( Oo0Ooo , "[COLOR ghostwhite]Not a valid selection, please try again.[/COLOR]" )
  sys . exit ( 1 )
  if 47 - 47: oo00oO0o . IIiIi11i1i / IIiii
 o0OO0O0Oo = xbmc . translatePath ( os . path . join ( '/storage/emulated/0/Download' , '' ) )
 OOOOO = xbmcgui . DialogProgress ( )
 OOOOO . create ( Oo0Ooo , "" , "" , 'APK: ' + name )
 Ooo0o0oo = os . path . join ( o0OO0O0Oo , name + '.nes' )
 downloader . download ( url , Ooo0o0oo , OOOOO )
 oo00OOoOoO00 = xbmcgui . Dialog ( )
 oo00OOoOoO00 . ok ( Oo0Ooo , "[COLOR yellow]Download complete, ROM Location: [/COLOR][COLOR white]" + Ooo0o0oo + "[/COLOR]" )
 if 83 - 83: IIiii / OOOoO00 / OOOoO00 + IIiii * IiiiiI1i1Iii + IIiii
def IIIIiii ( name , url , ) :
 if "NULL" in url :
  oo00OOoOoO00 = xbmcgui . Dialog ( )
  ooo0OO . ok ( Oo0Ooo , "[COLOR ghostwhite]Not a valid selection, please try again.[/COLOR]" )
  sys . exit ( 1 )
  if 65 - 65: iIiI1 / IIiIi11i1i
 o0OO0O0Oo = xbmc . translatePath ( os . path . join ( '/storage/emulated/0/Download' , '' ) )
 OOOOO = xbmcgui . DialogProgress ( )
 OOOOO . create ( Oo0Ooo , "" , "" , 'APK: ' + name )
 Ooo0o0oo = os . path . join ( o0OO0O0Oo , name + '.gen' )
 downloader . download ( url , Ooo0o0oo , OOOOO )
 oo00OOoOoO00 = xbmcgui . Dialog ( )
 oo00OOoOoO00 . ok ( Oo0Ooo , "[COLOR yellow]Download complete, ROM Location: [/COLOR][COLOR white]" + Ooo0o0oo + "[/COLOR]" )
 if 12 - 12: IIiIi11i1i % o0oooOO00
 if 48 - 48: OoOO0o . i11iIiiIii
 if 5 - 5: IIIIiiIiiI . oOOOoo00 . O0OooOo0o . I1111i
 if 96 - 96: i11iIiiIii - OOOoO00 % O0OoOO0o / O0OO
 if 100 - 100: OoOO0o / O0O00O0 - I1111i % O0OooOo0o - i1ii1I1111ii1 % o0oooOO00
def ooo0OOiIi1IiI ( ver ) :
 if ver == '15' : wiz . setS ( 'show15' , 'true' if oOOoo00O0O == 'false' else 'false' )
 elif ver == '16' : wiz . setS ( 'show16' , 'true' if i1111 == 'false' else 'false' )
 xbmc . executebuiltin ( 'Container.Refresh' )
 if 14 - 14: iII1iIi11i % IIIIiiIiiI % iIiI1 - i11iIiiIii
def o0OO000ooOo ( part , whole ) :
 return 100 * float ( part ) / float ( whole )
 if 86 - 86: O0OO * I1111i
def O0o0oO ( type , name ) :
 if type == 'trakt' :
  OooO0oOo = [ ]
  oOOo00O0OOOo = urllib . quote_plus ( name . lower ( ) . replace ( ' ' , '' ) )
  OooO0oOo . append ( ( oOooO0 % name , ' ' ) )
  OooO0oOo . append ( ( oOooO0 % 'Save Trakt Data' , 'RunPlugin(plugin://%s/?mode=savetrakt&name=%s)' % ( OO0o , oOOo00O0OOOo ) ) )
  OooO0oOo . append ( ( oOooO0 % 'Restore Trakt Data' , 'RunPlugin(plugin://%s/?mode=restoretrakt&name=%s)' % ( OO0o , oOOo00O0OOOo ) ) )
  OooO0oOo . append ( ( oOooO0 % 'Clear Trakt Data' , 'RunPlugin(plugin://%s/?mode=cleartrakt&name=%s)' % ( OO0o , oOOo00O0OOOo ) ) )
 if type == 'traktaddon' :
  OooO0oOo = [ ]
  oOOo00O0OOOo = urllib . quote_plus ( name . lower ( ) . replace ( ' ' , '' ) )
  OooO0oOo . append ( ( oOooO0 % name , ' ' ) )
  OooO0oOo . append ( ( oOooO0 % 'Register Trakt' , 'RunPlugin(plugin://%s/?mode=authtrakt&name=%s)' % ( OO0o , oOOo00O0OOOo ) ) )
  OooO0oOo . append ( ( oOooO0 % 'Save Trakt Data' , 'RunPlugin(plugin://%s/?mode=savetrakt&name=%s)' % ( OO0o , oOOo00O0OOOo ) ) )
  OooO0oOo . append ( ( oOooO0 % 'Restore Trakt Data' , 'RunPlugin(plugin://%s/?mode=restoretrakt&name=%s)' % ( OO0o , oOOo00O0OOOo ) ) )
  OooO0oOo . append ( ( oOooO0 % 'Clear Addon Trakt Data' , 'RunPlugin(plugin://%s/?mode=addontrakt&name=%s)' % ( OO0o , oOOo00O0OOOo ) ) )
 if type == 'debrid' :
  OooO0oOo = [ ]
  oOOo00O0OOOo = urllib . quote_plus ( name . lower ( ) . replace ( ' ' , '' ) )
  OooO0oOo . append ( ( oOooO0 % name , ' ' ) )
  OooO0oOo . append ( ( oOooO0 % 'Save Real Debrid Data' , 'RunPlugin(plugin://%s/?mode=savedebrid&name=%s)' % ( OO0o , oOOo00O0OOOo ) ) )
  OooO0oOo . append ( ( oOooO0 % 'Restore Real Debrid Data' , 'RunPlugin(plugin://%s/?mode=restoredebrid&name=%s)' % ( OO0o , oOOo00O0OOOo ) ) )
  OooO0oOo . append ( ( oOooO0 % 'Clear Real Debrid Data' , 'RunPlugin(plugin://%s/?mode=cleardebrid&name=%s)' % ( OO0o , oOOo00O0OOOo ) ) )
 if type == 'debridaddon' :
  OooO0oOo = [ ]
  oOOo00O0OOOo = urllib . quote_plus ( name . lower ( ) . replace ( ' ' , '' ) )
  OooO0oOo . append ( ( oOooO0 % name , ' ' ) )
  OooO0oOo . append ( ( oOooO0 % 'Register Real Debrid' , 'RunPlugin(plugin://%s/?mode=authdebrid&name=%s)' % ( OO0o , oOOo00O0OOOo ) ) )
  OooO0oOo . append ( ( oOooO0 % 'Save Real Debrid Data' , 'RunPlugin(plugin://%s/?mode=savedebrid&name=%s)' % ( OO0o , oOOo00O0OOOo ) ) )
  OooO0oOo . append ( ( oOooO0 % 'Restore Real Debrid Data' , 'RunPlugin(plugin://%s/?mode=restoredebrid&name=%s)' % ( OO0o , oOOo00O0OOOo ) ) )
  OooO0oOo . append ( ( oOooO0 % 'Clear Addon Real Debrid Data' , 'RunPlugin(plugin://%s/?mode=addondebrid&name=%s)' % ( OO0o , oOOo00O0OOOo ) ) )
 if type == 'install' :
  OooO0oOo = [ ]
  oOOo00O0OOOo = urllib . quote_plus ( name )
  OooO0oOo . append ( ( oOooO0 % name , ' ' ) )
  OooO0oOo . append ( ( oOooO0 % 'Fresh Install' , 'RunPlugin(plugin://%s/?mode=install&name=%s&url=fresh)' % ( OO0o , oOOo00O0OOOo ) ) )
  OooO0oOo . append ( ( oOooO0 % 'Normal Install Use On Updates' , 'RunPlugin(plugin://%s/?mode=install&name=%s&url=normal)' % ( OO0o , oOOo00O0OOOo ) ) )
  OooO0oOo . append ( ( oOooO0 % 'Apply guiFix' , 'RunPlugin(plugin://%s/?mode=install&name=%s&url=gui)' % ( OO0o , oOOo00O0OOOo ) ) )
 OooO0oOo . append ( ( oOooO0 % 'SpinzTV Settings' , 'RunPlugin(plugin://%s/?mode=settings)' % OO0o ) )
 return OooO0oOo
 if 31 - 31: IIiIi11i1i % OOOoO00 * IIiIi11i1i
def IiII1i1iii1Ii ( ) :
 iI = wiz . log_check ( )
 O0O00OOo = iI . replace ( I1IiiI , "" )
 if os . path . exists ( iI ) or not iI == False :
  OoOOo = open ( iI , mode = 'r' ) ; iii1 = OoOOo . read ( ) ; OoOOo . close ( )
  wiz . TextBoxes ( "%s - %s" % ( Oo0Ooo , O0O00OOo ) , iii1 )
 else :
  wiz . LogNotify ( 'View Log' , 'No Log File Found!' )
  if 78 - 78: oOOOoo00 + IIiIi11i1i - O0OoOO0o
def i1I1iIi1IiI ( ) :
 if os . path . exists ( o0oO0 ) :
  OoOOo = open ( o0oO0 , mode = 'r' ) ; iii1 = OoOOo . read ( ) ; OoOOo . close ( )
  wiz . TextBoxes ( "%s - Wizard.log" % Oo0Ooo , iii1 )
 else :
  wiz . LogNotify ( 'View Log' , 'Wizard.log not found!' )
  if 11 - 11: O0OooOo0o
def O00O00O000OOO ( addon ) :
 if ooo0OO . yesno ( Oo0Ooo , 'Are you sure you want to delete the addon:' , '[COLOR yellow]%s[/COLOR]' % addon , yeslabel = 'Yes, Remove' , nolabel = 'No, Cancel' ) :
  wiz . cleanHouse ( os . path . join ( oO00oOo , addon ) )
  iIOo0O ( addon )
  wiz . LogNotify ( 'Remove Addon' , 'Complete!' )
  ooo0OO . ok ( Oo0Ooo , 'The addon has been removed but will remain in the addons list until the next time you reload Kodi.' )
 else : wiz . LogNotify ( 'Remove Addon' , 'Cancelled!' )
 xbmc . executebuiltin ( 'Container.Refresh' )
 if 1 - 1: O0OoOO0o / OoOO0o % IiiiiI1i1Iii . iIiI1 + iII1iIi11i
def iIOo0O ( addon ) :
 if addon == 'all' :
  if ooo0OO . yesno ( Oo0Ooo , 'Would you like to remove ALL addon data stored in you Userdata folder?' , yeslabel = 'Yes, Remove' , nolabel = 'No, Cancel' ) :
   wiz . cleanHouse ( Oo0O )
  else : wiz . LogNotify ( 'Remove Addon Data' , 'Cancelled!' )
 elif addon == 'uninstalled' :
  if ooo0OO . yesno ( Oo0Ooo , 'Would you like to remove ALL addon data stored in you Userdata folder for uninstalled addons?' , yeslabel = 'Yes, Remove' , nolabel = 'No, Cancel' ) :
   I1Ii11iiiI = 0
   for i1ii in glob . glob ( os . path . join ( Oo0O , '*' ) ) :
    O0ooO0ooo0oO = i1ii . replace ( Oo0O , '' ) . replace ( '\\' , '' ) . replace ( '/' , '' )
    if O0ooO0ooo0oO in oOOoo0Oo : pass
    elif os . path . exists ( os . path . join ( oO00oOo , O0ooO0ooo0oO ) ) : pass
    else : wiz . cleanHouse ( i1ii ) ; I1Ii11iiiI += 1 ; wiz . log ( i1ii ) ; shutil . rmtree ( i1ii )
   wiz . LogNotify ( 'Clean up Uninstalled' , '[COLOR yellow]%s[/COLOR] Folders(s) Removed' % I1Ii11iiiI )
  else : wiz . LogNotify ( 'Remove Addon Data' , 'Cancelled!' )
 elif addon == 'empty' :
  if ooo0OO . yesno ( Oo0Ooo , 'Would you like to remove ALL empty addon data folders in you Userdata folder?' , yeslabel = 'Yes, Remove' , nolabel = 'No, Cancel' ) :
   I1Ii11iiiI = wiz . emptyfolder ( Oo0O )
   wiz . LogNotify ( 'Remove Empty Folders' , '[COLOR yellow]%s[/COLOR] Folders(s) Removed' % I1Ii11iiiI )
  else : wiz . LogNotify ( 'Remove Empty Folders' , 'Cancelled!' )
 else :
  i1II1IiIII111 = os . path . join ( OOOo0 , 'addon_data' , addon )
  if addon in oOOoo0Oo :
   wiz . LogNotify ( "Protected Plugin" , "Not allowed to remove Addon_Data" )
  elif os . path . exists ( i1II1IiIII111 ) :
   if ooo0OO . yesno ( Oo0Ooo , 'Would you also like to remove the addon data for:' , '[COLOR yellow]%s[/COLOR]' % addon , yeslabel = 'Yes, Remove' , nolabel = 'No, Cancel' ) :
    wiz . cleanHouse ( i1II1IiIII111 )
    try :
     shutil . rmtree ( i1II1IiIII111 )
    except :
     wiz . log ( "Error deleting: %s" % i1II1IiIII111 )
   else :
    wiz . log ( 'Addon data for %s was not removed' % addon )
 xbmc . executebuiltin ( 'Container.Refresh' )
 if 50 - 50: O0OooOo0o * oOOOoo00 / O0O00O0 . IIiii + iIiI1 - OOOoO00
 if 18 - 18: o0oooOO00 % i11iIiiIii % oOOOoo00 / IIIIiiIiiI / IIiii / Oo0OO
 if 48 - 48: o0oooOO00 + IIiIi11i1i / iII1iIi11i + O0OooOo0o
 if 18 - 18: oOOOoo00
 if 23 - 23: O0OooOo0o
def Ii1i1i1111 ( install = None ) :
 if iIii1 == 'true' :
  traktit . autoUpdate ( 'all' )
  wiz . setS ( 'traktlastsave' , str ( I11II1i ) )
 if oOOoO0 == 'true' :
  debridit . autoUpdate ( 'all' )
  wiz . setS ( 'debridlastsave' , str ( I11II1i ) )
 if oo00 not in [ 'skin.confluence' ] :
  ii1i1i = 'skin.confluence'
  IIiiii = ooo0OO . yesno ( Oo0Ooo , "The skin needs to be set back to [COLOR yellow]%s[/COLOR]" % ii1i1i [ 5 : ] , "Before doing a fresh install to clear all Texture files!" , "Would you like us to do that for you?" , nolabel = "No, Thanks" , yeslabel = "Yes, Swap Skin" ) ;
  if IIiiii :
   skinSwitch . swapSkins ( ii1i1i )
   while not xbmc . getCondVisibility ( "Window.isVisible(yesnodialog)" ) :
    xbmc . sleep ( 200 )
   xbmc . executebuiltin ( "Action(Left)" )
   xbmc . executebuiltin ( "Action(Select)" )
  else : wiz . LogNotify ( Oo0Ooo , 'Fresh Install: [COLOR red]Cancelled![/COLOR]' ) ; return
 if install : O000o0 = ooo0OO . yesno ( Oo0Ooo , "Do you wish to restore your" , "Kodi configuration to default settings" , "Before installing %s?" % install , nolabel = 'No, Cancel' , yeslabel = 'Yes, Continue' )
 else : O000o0 = ooo0OO . yesno ( Oo0Ooo , "Do you wish to restore your" , "Kodi configuration to default settings?" , nolabel = 'No, Cancel' , yeslabel = 'Yes, Continue' )
 if O000o0 :
  II11iIII1i1I = os . path . abspath ( O00ooooo00 )
  II1 . create ( Oo0Ooo , "Clearing all files and folders:" , '' , '' )
  oOO0oo = sum ( [ len ( IiIIi1I1I11Ii ) for o0OO , OoiiIiI , IiIIi1I1I11Ii in os . walk ( II11iIII1i1I ) ] ) ; o0Ooo0O00 = 0 ;
  try :
   for ii1o0oooO , ooOoo0oO0OoO0 , IiIIi1I1I11Ii in os . walk ( II11iIII1i1I , topdown = True ) :
    ooOoo0oO0OoO0 [ : ] = [ OoiiIiI for OoiiIiI in ooOoo0oO0OoO0 if OoiiIiI not in oOOoo0Oo ]
    for I1i11 in IiIIi1I1I11Ii :
     o0Ooo0O00 += 1
     oOOOOOoOO = ii1o0oooO . split ( '\\' )
     oooo00 = len ( oOOOOOoOO ) - 1
     if I1i11 == 'sources.xml' and oOOOOOoOO [ oooo00 ] == 'userdata' and ii11iIi1I == 'true' : wiz . log ( "Keep Sources: %s\\%s" % ( ii1o0oooO , I1i11 ) )
     elif I1i11 == 'favourites.xml' and oOOOOOoOO [ oooo00 ] == 'userdata' and i1iiIII111ii == 'true' : wiz . log ( "Keep Favourites: %s\\%s" % ( ii1o0oooO , I1i11 ) )
     elif I1i11 == 'profiles.xml' and oOOOOOoOO [ oooo00 ] == 'userdata' and iI111I11I1I1 == 'true' : wiz . log ( "Keep Profiles: %s\\%s" % ( ii1o0oooO , I1i11 ) )
     elif I1i11 == 'advancedsettings.xml' and oOOOOOoOO [ oooo00 ] == 'userdata' and OOooO0OOoo == 'true' : wiz . log ( "Keep Advanced Settings: %s\\%s" % ( ii1o0oooO , I1i11 ) )
     elif I1i11 in [ 'xbmc.log' , 'kodi.log' , 'spmc.log' , 'tvmc.log' ] : wiz . log ( "Keep Log File: %s" % I1i11 )
     elif I1i11 . endswith ( '.db' ) :
      try : os . remove ( os . path . join ( ii1o0oooO , I1i11 ) )
      except : wiz . log ( 'Failed to delete, Purging DB.' ) ; wiz . purgeDb ( os . path . join ( ii1o0oooO , I1i11 ) )
     else :
      II1 . update ( int ( o0OO000ooOo ( o0Ooo0O00 , oOO0oo ) ) , '' , 'File: [COLOR yellow]%s[/COLOR]' % I1i11 , '' )
      try : os . remove ( os . path . join ( ii1o0oooO , I1i11 ) )
      except : wiz . log ( "Error removing %s\\%s" % ( ii1o0oooO , I1i11 ) )
   for ii1o0oooO , ooOoo0oO0OoO0 , IiIIi1I1I11Ii in os . walk ( II11iIII1i1I , topdown = True ) :
    ooOoo0oO0OoO0 [ : ] = [ OoiiIiI for OoiiIiI in ooOoo0oO0OoO0 if OoiiIiI not in oOOoo0Oo ]
    for I1i11 in ooOoo0oO0OoO0 :
     II1 . update ( 100 , '' , 'Cleaning Up Empty Folder: [COLOR yellow]%s[/COLOR]' % I1i11 , '' )
     if I1i11 not in [ "Database" , "userdata" , "temp" , "addons" , "addon_data" ] :
      shutil . rmtree ( os . path . join ( ii1o0oooO , I1i11 ) , ignore_errors = True , onerror = None )
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
   o0oO0oOO ( install , 'normal' )
  else :
   ooo0OO . ok ( Oo0Ooo , "The process is complete, you're now back to a fresh Kodi configuration with SpinzTV Wizard" , "Please reboot your system or restart Kodi in order for the changes to be applied." )
   wiz . killxbmc ( )
 else : wiz . LogNotify ( Oo0Ooo , 'Fresh Install: [COLOR red]Cancelled![/COLOR]' ) ; xbmc . executebuiltin ( 'Container.Refresh' )
 if 35 - 35: IiiiiI1i1Iii . o0oooOO00 * i11iIiiIii
 if 44 - 44: i11iIiiIii / iIiI1
 if 42 - 42: I1111i + iIiI1 % O0OooOo0o + O0OO
 if 24 - 24: OoOO0o * O0OooOo0o % OoOO0o % iII1iIi11i + I1111i
def IiIiiiIii ( ) :
 if ooo0OO . yesno ( Oo0Ooo , 'Would you like to clear cache?' , nolabel = 'Cancel' , yeslabel = 'Delete' ) :
  wiz . clearCache ( )
  IiiIIi11I1 ( )
  if 34 - 34: O0OoOO0o * O0OoOO0o % I1111i + OoOO0o * Iii % O0O00O0
def IiiIIi11I1 ( ) :
 I1iI1I1 = wiz . latestDB ( 'Textures' )
 if ooo0OO . yesno ( Oo0Ooo , "Would you like to delete the %s and Thumbnails folder?" % I1iI1I1 , "They will repopulate on startup" , nolabel = 'No, Cancel' , yeslabel = 'Yes, Remove' ) :
  try : wiz . removeFile ( os . join ( i1i1II , I1iI1I1 ) )
  except : wiz . log ( 'Failed to delete, Purging DB.' ) ; wiz . purgeDb ( I1iI1I1 )
  wiz . removeFolder ( iI1Ii11111iIi )
  wiz . killxbmc ( )
 else : wiz . log ( 'Clear thumbnames cancelled' )
 if 48 - 48: i1ii1I1111ii1 / i11iIiiIii - IIiii * IIIIiiIiiI / I1111i
def OoOoi1i ( ) :
 IIIiiiI = [ ] ; O0O0OOooOO0 = [ ]
 for OoO00oo00 , Oo0Oo0O , IiIIi1I1I11Ii in os . walk ( O00ooooo00 ) :
  for OoOOo in fnmatch . filter ( IiIIi1I1I11Ii , '*.db' ) :
   if OoOOo != 'Thumbs.db' :
    iiiI1i11Ii = os . path . join ( OoO00oo00 , OoOOo )
    IIIiiiI . append ( iiiI1i11Ii )
    dir = iiiI1i11Ii . replace ( '\\' , '/' ) . split ( '/' )
    O0O0OOooOO0 . append ( '(%s) %s' % ( dir [ len ( dir ) - 2 ] , dir [ len ( dir ) - 1 ] ) )
 if IIIII >= 16 :
  iIiII = ooo0OO . multiselect ( "Select DB File to Purge" , O0O0OOooOO0 )
  if iIiII == None : wiz . LogNotify ( "Purge Database" , "Cancelled" )
  elif len ( iIiII ) == 0 : wiz . LogNotify ( "Purge Database" , "Cancelled" )
  else :
   for i1i1IIIIIIIi in iIiII : wiz . purgeDb ( IIIiiiI [ i1i1IIIIIIIi ] )
 else :
  iIiII = ooo0OO . select ( "Select DB File to Purge" , O0O0OOooOO0 )
  if iIiII == - 1 : wiz . LogNotify ( "Purge Database" , "Cancelled" )
  else : wiz . purgeDb ( IIIiiiI [ i1i1IIIIIIIi ] )
  if 65 - 65: IIiii
  if 7 - 7: iII1iIi11i . o0oooOO00 / oOOOoo00 . OOOoO00 * IIiIi11i1i - O0OooOo0o
  if 37 - 37: IiiiiI1i1Iii . o0oooOO00 / O0OoOO0o * OoOO0o
  if 7 - 7: O0OO * IIiIi11i1i + O0OooOo0o % i11iIiiIii
def i1i1IiIiIi1Ii ( ) :
 IiIi1I1 = wiz . workingURL ( I1I1i1I )
 if IiIi1I1 == True :
  i1I1i1 = wiz . openURL ( I1I1i1I ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
  id , iii1 = i1I1i1 . split ( '|||' )
  notify . TestNotification ( msg = iii1 , title = O0oO0 , BorderWidth = 10 )
 else : wiz . LogNotify ( Oo0Ooo , "Invalid URL for Notification" )
 if 64 - 64: OOOoO00 + I1111i * I1111i
def i1I ( ) :
 if OoOoO == 'No' : i11I ( '==============BackUp Options===============' , '' , themeit = Ii1I1Ii )
 i11I ( 'Full Backup' , 'full' , icon = I1i1iiI1 , themeit = O0O0OOOOoo )
 i11I ( 'Backup for Builds (Exc: Thumbnails, Databases)' , 'backb' , icon = I1i1iiI1 , themeit = O0O0OOOOoo )
 i11I ( 'Backup addon data' , 'backad' , icon = I1i1iiI1 , themeit = O0O0OOOOoo )
 if OoOoO == 'No' : i11I ( '==============Restore Options===============' , '' , themeit = Ii1I1Ii )
 I1i ( 'Restore Full Backup' , 'refull' , icon = I1i1iiI1 , themeit = O0O0OOOOoo )
 I1i ( 'Restore Addon Data' , 'refull' , icon = I1i1iiI1 , themeit = O0O0OOOOoo )
 if OoOoO == 'No' : i11I ( '==============Other Options===============' , '' , themeit = Ii1I1Ii )
 I1i ( 'Delete A Backup' , 'delbu' , icon = I1i1iiI1 , themeit = O0O0OOOOoo )
 i11I ( 'Delete All Backups' , 'delall' , icon = I1i1iiI1 , themeit = O0O0OOOOoo )
 i11I ( 'Select Backup Location' , 'settings' , icon = I1i1iiI1 , themeit = O0O0OOOOoo )
 if 36 - 36: i1ii1I1111ii1 * iIiI1
 if 77 - 77: IIIIiiIiiI % Oo0OO - O0O00O0
 if 93 - 93: O0OO * iIiI1
 if 73 - 73: IIiii - i1ii1I1111ii1 * Oo0OO / i11iIiiIii * OOOoO00 % O0OooOo0o
 if 56 - 56: I1111i * iIiI1 . iIiI1 . oOOOoo00
 if 24 - 24: iIiI1 . IIiIi11i1i * O0O00O0 % OoOO0o / OOOoO00
def I1i ( display , mode , name = None , url = None , menu = None , overwrite = True , fanart = O0oo0OO0 , icon = I1i1iiI1 , themeit = None ) :
 Oo0Ooo0O0 = '%s?mode=%s' % ( sys . argv [ 0 ] , urllib . quote_plus ( mode ) )
 if not name == None : Oo0Ooo0O0 += "&name=" + urllib . quote_plus ( name )
 if not url == None : Oo0Ooo0O0 += "&url=" + urllib . quote_plus ( url )
 IiIIi1IiiIiI = True
 if themeit : display = themeit % display
 iIIIIiiIii = xbmcgui . ListItem ( display , iconImage = "DefaultFolder.png" , thumbnailImage = icon )
 iIIIIiiIii . setInfo ( type = "Video" , infoLabels = { "Title" : display , "Plot" : Oo0Ooo } )
 iIIIIiiIii . setProperty ( "Fanart_Image" , fanart )
 if not menu == None : iIIIIiiIii . addContextMenuItems ( menu , replaceItems = overwrite )
 IiIIi1IiiIiI = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = Oo0Ooo0O0 , listitem = iIIIIiiIii , isFolder = True )
 return IiIIi1IiiIiI
 if 58 - 58: iIiI1
def i11I ( display , mode , name = None , url = None , menu = None , overwrite = True , fanart = O0oo0OO0 , icon = I1i1iiI1 , themeit = None ) :
 Oo0Ooo0O0 = '%s?mode=%s' % ( sys . argv [ 0 ] , urllib . quote_plus ( mode ) )
 if not name == None : Oo0Ooo0O0 += "&name=" + urllib . quote_plus ( name )
 if not url == None : Oo0Ooo0O0 += "&url=" + urllib . quote_plus ( url )
 IiIIi1IiiIiI = True
 if themeit : display = themeit % display
 iIIIIiiIii = xbmcgui . ListItem ( display , iconImage = "DefaultFolder.png" , thumbnailImage = icon )
 iIIIIiiIii . setInfo ( type = "Video" , infoLabels = { "Title" : display , "Plot" : Oo0Ooo } )
 iIIIIiiIii . setProperty ( "Fanart_Image" , fanart )
 if not menu == None : iIIIIiiIii . addContextMenuItems ( menu , replaceItems = overwrite )
 IiIIi1IiiIiI = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = Oo0Ooo0O0 , listitem = iIIIIiiIii , isFolder = False )
 return IiIIi1IiiIiI
 if 9 - 9: Iii % oOOOoo00 . OOOoO00 + I1111i
def Oo0o ( name , url , mode , iconimage , fanart , description ) :
 Oo0Ooo0O0 = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&fanart=" + urllib . quote_plus ( fanart )
 IiIIi1IiiIiI = True
 iIIIIiiIii = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 iIIIIiiIii . setInfo ( type = "Video" , infoLabels = { "Title" : name } )
 iIIIIiiIii . setProperty ( "Fanart_Image" , fanart )
 IiIIi1IiiIiI = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = Oo0Ooo0O0 , listitem = iIIIIiiIii , isFolder = False )
 return IiIIi1IiiIiI
 if 93 - 93: OOOoO00
def iIii1Ooo0oO0 ( name , url , mode , iconimage , fanart , description ) :
 Oo0Ooo0O0 = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart ) + "&description=" + urllib . quote_plus ( description )
 IiIIi1IiiIiI = True
 iIIIIiiIii = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 iIIIIiiIii . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description } )
 iIIIIiiIii . setProperty ( "Fanart_Image" , fanart )
 if mode == 90 :
  IiIIi1IiiIiI = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = Oo0Ooo0O0 , listitem = iIIIIiiIii , isFolder = False )
 else :
  IiIIi1IiiIiI = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = Oo0Ooo0O0 , listitem = iIIIIiiIii , isFolder = True )
 return IiIIi1IiiIiI
 if 86 - 86: O0OoOO0o
 if 95 - 95: OoOO0o * OOOoO00 . o0oooOO00 . Oo0OO . Oo0OO - IIiii
def ii1iIIiii1 ( ) :
 ooOo0O0o0 = [ ]
 o0oo0O = sys . argv [ 2 ]
 if len ( o0oo0O ) >= 2 :
  I1iiIII = sys . argv [ 2 ]
  iIi1I1 = I1iiIII . replace ( '?' , '' )
  if ( I1iiIII [ len ( I1iiIII ) - 1 ] == '/' ) :
   I1iiIII = I1iiIII [ 0 : len ( I1iiIII ) - 2 ]
  O0oOoo0OoO0O = iIi1I1 . split ( '&' )
  ooOo0O0o0 = { }
  for oo00IiI1 in range ( len ( O0oOoo0OoO0O ) ) :
   oOo00o00oO = { }
   oOo00o00oO = O0oOoo0OoO0O [ oo00IiI1 ] . split ( '=' )
   if ( len ( oOo00o00oO ) ) == 2 :
    ooOo0O0o0 [ oOo00o00oO [ 0 ] ] = oOo00o00oO [ 1 ]
    if 95 - 95: i1ii1I1111ii1
  return ooOo0O0o0
  if 88 - 88: iII1iIi11i % O0OO + IiiiiI1i1Iii + IiiiiI1i1Iii * O0OooOo0o
I1iiIII = ii1iIIiii1 ( )
IiIi1I1 = None
I1i11 = None
o0Oo = None
if 57 - 57: OOOoO00 / iIiI1
try : o0Oo = urllib . unquote_plus ( I1iiIII [ "mode" ] )
except : pass
try : I1i11 = urllib . unquote_plus ( I1iiIII [ "name" ] )
except : pass
try : IiIi1I1 = urllib . unquote_plus ( I1iiIII [ "url" ] )
except : pass
if 69 - 69: IIIIiiIiiI - iIiI1 % iII1iIi11i
wiz . log ( '[ Version : \'%s\' ] [ Mode : \'%s\' ] [ Name : \'%s\' ] [ Url : \'%s\' ]' % ( iiiii , o0Oo if not o0Oo == '' else None , I1i11 , IiIi1I1 ) )
def ii1i ( ) :
 if 27 - 27: oo00oO0o % O0OoOO0o % IiiiiI1i1Iii
 for file in os . listdir ( I11i11Ii ) :
  if file . endswith ( ".zip" ) :
   IiIi1I1 = xbmc . translatePath ( os . path . join ( I11i11Ii , file ) )
   Oo0o ( file , IiIi1I1 , 'read' , I1i1iiI1 , I1i1iiI1 , '' )
   if 99 - 99: i1ii1I1111ii1 + Oo0OO + i11iIiiIii + iIiI1 % IIIIiiIiiI / IIiIi11i1i
def O0OO0o0OO0OO ( ) :
 oOo0O = xbmc . translatePath ( os . path . join ( 'special://' , 'home' ) )
 for file in os . listdir ( I11i11Ii ) :
  if file . endswith ( ".zip" ) :
   IiIi1I1 = xbmc . translatePath ( os . path . join ( I11i11Ii , file ) )
   iIii1Ooo0oO0 ( file , IiIi1I1 , 'dell' , I1i1iiI1 , I1i1iiI1 , '' )
   if 43 - 43: IIiii . OoOO0o . IIiIi11i1i + Iii
   if 78 - 78: Iii % o0oooOO00 + oOOOoo00 / Oo0OO % O0OooOo0o + OOOoO00
def o00Oo0oooooo ( content , viewType ) :
 if content :
  xbmcplugin . setContent ( int ( sys . argv [ 1 ] ) , content )
 if wiz . getS ( 'auto-view' ) == 'true' :
  xbmc . executebuiltin ( "Container.SetViewMode(%s)" % wiz . getS ( viewType ) )
  if 91 - 91: Iii % O0OO . IIiii + O0O00O0 + IIiii
if o0Oo == None : ii1iI1I11I ( )
if 95 - 95: O0O00O0 + oOOOoo00 * OOOoO00
elif o0Oo == 'builds' : OO0000o ( )
elif o0Oo == 'showupdate' : ooo0OOiIi1IiI ( I1i11 )
elif o0Oo == 'viewbuild' : ooo0O0o00O ( I1i11 )
elif o0Oo == 'install' : o0oO0oOO ( I1i11 , IiIi1I1 )
elif o0Oo == 'theme' : o0oO0oOO ( I1i11 , o0Oo , IiIi1I1 )
if 16 - 16: IIiIi11i1i / i1ii1I1111ii1 + O0OO % Iii - Oo0OO . IIIIiiIiiI
elif o0Oo == 'maint' : i1iiIiI1Ii1i ( )
elif o0Oo == 'speed' : Oo0000oOo ( )
elif o0Oo == 'speedtest' : speedtest . runtest ( IiIi1I1 )
elif o0Oo == 'clearcache' : IiIiiiIii ( )
elif o0Oo == 'clearpackages' : wiz . clearPackages ( )
elif o0Oo == 'clearthumb' : IiiIIi11I1 ( )
elif o0Oo == 'freshstart' : Ii1i1i1111 ( )
elif o0Oo == 'forceupdate' : wiz . forceUpdate ( )
elif o0Oo == 'forceclose' : wiz . killxbmc ( )
elif o0Oo == 'uploadlog' : uploadLog . LogUploader ( )
elif o0Oo == 'viewlog' : IiII1i1iii1Ii ( )
elif o0Oo == 'viewwizlog' : i1I1iIi1IiI ( )
elif o0Oo == 'clearwizlog' : OoOOo = open ( o0oO0 , 'w' ) ; OoOOo . close ( ) ; wiz . LogNotify ( Oo0Ooo , "Wizard Log Cleared!" )
elif o0Oo == 'purgedb' : OoOoi1i ( )
elif o0Oo == 'removeaddons' : IiiiIi1i ( )
elif o0Oo == 'removeaddon' : O00O00O000OOO ( I1i11 )
elif o0Oo == 'removeaddondata' : o0oOoO0O ( )
elif o0Oo == 'removedata' : iIOo0O ( I1i11 )
elif o0Oo == 'resetaddon' : I1Ii11iiiI = wiz . cleanHouse ( IiI , ignore = True ) ; wiz . LogNotify ( Oo0Ooo , "Addon_Data reset" )
if 26 - 26: IIiii * iII1iIi11i . Oo0OO
elif o0Oo == 'apkspinz' : o0oO000oo ( )
elif o0Oo == 'apk' : OoOooOoO ( )
elif o0Oo == 'apkkodi' : IIiI1Ii ( )
elif o0Oo == 'apkmaster' : oOO ( )
elif o0Oo == 'apkgames' : I1IIIiI11i1 ( )
elif o0Oo == 'emurom' : IIi1IIIi ( )
elif o0Oo == 'emulators' : o0OOOo ( )
elif o0Oo == 'roms' : iII1ii1 ( )
elif o0Oo == 'snes' : Iii1iiIi1II ( )
elif o0Oo == 'nes' : ooo ( )
elif o0Oo == 'nesa' : ooO ( )
elif o0Oo == 'nesc' : I1Iii1 ( )
elif o0Oo == 'nesd' : Ooo00O0o ( )
elif o0Oo == 'nesf' : I11i1II ( )
elif o0Oo == 'nesh' : ooo000o000 ( )
elif o0Oo == 'nesl' : IiIi1I1ii111 ( )
elif o0Oo == 'nesn' : oOOO0oo0 ( )
elif o0Oo == 'nesr' : ii1iIi1iIiI1i ( )
elif o0Oo == 'nest' : ooo0o00 ( )
elif o0Oo == 'nesw' : I11IIi ( )
elif o0Oo == 'gen' : o0OIiiiI ( )
elif o0Oo == 'gena' : o0oOO ( )
elif o0Oo == 'genc' : ii ( )
elif o0Oo == 'gene' : ii1III11 ( )
elif o0Oo == 'genh' : o0o0O00oo0 ( )
elif o0Oo == 'genm' : ooO0o ( )
elif o0Oo == 'genp' : ii11I1 ( )
elif o0Oo == 'gens' : Ii111iIi1iIi ( )
elif o0Oo == 'genu' : OoOo ( )
elif o0Oo == 'apkvid' : O00 ( )
elif o0Oo == 'apksys' : oo000 ( )
elif o0Oo == 'apkinstall' : iIIiI1I1i ( I1i11 , IiIi1I1 )
elif o0Oo == 'snesrominstall' : OoOooo ( I1i11 , IiIi1I1 , )
elif o0Oo == 'nesrominstall' : iiIii1I ( I1i11 , IiIi1I1 )
elif o0Oo == 'genrominstall' : IIIIiii ( I1i11 , IiIi1I1 )
if 59 - 59: O0OoOO0o + Oo0OO - IIiii
if 62 - 62: i11iIiiIii % OOOoO00 . iII1iIi11i . OOOoO00
elif o0Oo == 'savedata' : o0iiiI1I1iIIIi1 ( )
elif o0Oo == 'togglesetting' : wiz . setS ( I1i11 , 'false' if wiz . getS ( I1i11 ) == 'true' else 'true' ) ; xbmc . executebuiltin ( 'Container.Refresh' )
if 84 - 84: i11iIiiIii * O0OO
elif o0Oo == 'trakt' : OOOoO000 ( )
elif o0Oo == 'savetrakt' : traktit . traktIt ( 'update' , I1i11 )
elif o0Oo == 'restoretrakt' : traktit . traktIt ( 'restore' , I1i11 )
elif o0Oo == 'addontrakt' : traktit . traktIt ( 'clearaddon' , I1i11 )
elif o0Oo == 'cleartrakt' : traktit . clearSaved ( I1i11 )
elif o0Oo == 'authtrakt' : traktit . activateTrakt ( I1i11 ) ; xbmc . executebuiltin ( 'Container.Refresh' )
if 18 - 18: OOOoO00 - O0O00O0 - o0oooOO00 / IiiiiI1i1Iii - O0OoOO0o
elif o0Oo == 'realdebrid' : II1IiiIii ( )
elif o0Oo == 'savedebrid' : debridit . debridIt ( 'update' , I1i11 )
elif o0Oo == 'restoredebrid' : debridit . debridIt ( 'restore' , I1i11 )
elif o0Oo == 'addondebrid' : debridit . debridIt ( 'clearaddon' , I1i11 )
elif o0Oo == 'cleardebrid' : debridit . clearSaved ( I1i11 )
elif o0Oo == 'authdebrid' : debridit . activateDebrid ( I1i11 ) ; xbmc . executebuiltin ( 'Container.Refresh' )
if 30 - 30: O0OoOO0o + oOOOoo00 + O0OooOo0o
elif o0Oo == 'contact' : wiz . TextBoxes ( Oo0Ooo , OO )
elif o0Oo == 'settings' : wiz . openS ( ) ; xbmc . executebuiltin ( 'Container.Refresh' )
if 14 - 14: IIiii / OOOoO00 - Iii - IIIIiiIiiI % oo00oO0o
elif o0Oo == 'developer' : oOOiiiIIiIi ( )
elif o0Oo == 'convertpath' : wiz . convertSpecial ( O00ooooo00 )
elif o0Oo == 'testnotify' : i1i1IiIiIi1Ii ( )
elif o0Oo == 'bre' : i1I ( )
elif o0Oo == 'full' : backuprestore . FullBackup ( )
elif o0Oo == 'backb' : backuprestore . Backup ( )
elif o0Oo == 'backad' : backuprestore . ADDON_DATA_BACKUP ( )
elif o0Oo == 'refull' : ii1i ( )
elif o0Oo == 'delbu' : O0OO0o0OO0OO ( )
elif o0Oo == 'delall' : backuprestore . DeleteAllBackups ( )
elif o0Oo == 'read' : backuprestore . READ_ZIP ( IiIi1I1 )
elif o0Oo == 'dell' : backuprestore . DeleteBackup ( IiIi1I1 )
if o0Oo not in [ '' , 'togglesettings' , 'settings' , 'contact' ] : xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
# dd678faae9ac167bc83abf78e5cb2f3f0688d3a3