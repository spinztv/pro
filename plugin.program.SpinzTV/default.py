import xbmc, xbmcaddon, xbmcgui, xbmcplugin, os, sys, xbmcvfs, glob
import shutil
import urllib2,urllib
import re
import fnmatch
import backuprestore
import plugintools
import base64
import time
import platform, subprocess
import zipfile
import yt
import ookla
try:    from sqlite3 import dbapi2 as database
except: from pysqlite2 import dbapi2 as database
from datetime import date, datetime, timedelta
from resources.libs import extract, downloader, notify, debridit, traktit, loginit, skinSwitch, uploadLog, yt, wizard as wiz

ADDON_ID       = xbmcaddon.Addon().getAddonInfo('id')
ADDONTITLE     = 'SpinzTV'
ADDON          = wiz.addonId(ADDON_ID)
Addon 		   = xbmcaddon.Addon(ADDON_ID)
addonDir 	   = Addon.getAddonInfo('path').decode("utf-8")
iiNT3LiiListAPK = xbmc.translatePath(os.path.join(addonDir,"resources","iiNT3LiiList.txt"))
VERSION        = wiz.addonInfo(ADDON_ID,'version')
ADDONPATH        = wiz.addonInfo(ADDON_ID,'path')
USER_AGENT     = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3'
DIALOG         = xbmcgui.Dialog()
DP             = xbmcgui.DialogProgress()
HOME           = xbmc.translatePath('special://home/')
ROMLOCATION    = xbmc.translatePath(os.path.join('//storage//emulated//0//Download',''))
LOG            = xbmc.translatePath('special://logpath/')
PROFILE        = xbmc.translatePath('special://profile/')
ADDONS           = os.path.join(HOME,      'addons')
zip            = plugintools.get_setting("zip")
USB            = xbmc.translatePath(os.path.join(zip))
ADDONS         = os.path.join(HOME,     'addons')
USERDATA       = os.path.join(HOME,     'userdata')
PLUGIN         = os.path.join(ADDONS,   ADDON_ID)
PACKAGES       = os.path.join(ADDONS,   'packages')
ADDOND         = os.path.join(USERDATA, 'addon_data')
ADDONDATA      = os.path.join(USERDATA, 'addon_data', ADDON_ID)
ADVANCED       = os.path.join(USERDATA, 'advancedsettings.xml')
SOURCES        = os.path.join(USERDATA, 'sources.xml')
FAVOURITES     = os.path.join(USERDATA, 'favourites.xml')
PROFILES       = os.path.join(USERDATA, 'profiles.xml')
GUISETTINGS    = os.path.join(USERDATA,  'guisettings.xml')
THUMBS         = os.path.join(USERDATA, 'Thumbnails')
DATABASE       = os.path.join(USERDATA, 'Database')
FANART         = os.path.join(PLUGIN,   'fanart.jpg')
ICON           = os.path.join(PLUGIN,   'icon.png')
ART            = os.path.join(PLUGIN,   'resources', 'art')
WIZLOG         = os.path.join(ADDONDATA, 'wizard.log')
SKIN           = xbmc.getSkinDir()
BUILDNAME      = wiz.getS('buildname')
DEFAULTSKIN    = wiz.getS('defaultskin')
DEFAULTNAME    = wiz.getS('defaultskinname')
DEFAULTIGNORE  = wiz.getS('defaultskinignore')
BUILDVERSION   = wiz.getS('buildversion')
BUILDTHEME     = wiz.getS('buildtheme')
BUILDLATEST    = wiz.getS('latestversion')
SHOW15         = wiz.getS('show15')
SHOW16         = wiz.getS('show16')
SHOW17         = wiz.getS('show17')
SHOWADULT      = wiz.getS('adult')
SHOWMAINT      = wiz.getS('showmaint')
AUTOCLEANUP    = wiz.getS('autoclean')
AUTOCACHE      = wiz.getS('clearcache')
AUTOPACKAGES   = wiz.getS('clearpackages')
AUTOTHUMBS       = wiz.getS('clearthumbs')
AUTOFEQ          = wiz.getS('autocleanfeq')
AUTODELAY        = wiz.getS('delayautoclean')
AUTONEXTRUN      = wiz.getS('nextautocleanup')
INCLUDEVIDEO     = wiz.getS('includevideo')
INCLUDEALL       = wiz.getS('includeall')
INCLUDEBOB       = wiz.getS('includebob')
INCLUDEPHOENIX   = wiz.getS('includephoenix')
INCLUDESPECTO    = wiz.getS('includespecto')
INCLUDEGENESIS   = wiz.getS('includegenesis')
INCLUDEEXODUS    = wiz.getS('includeexodus')
INCLUDEONECHAN   = wiz.getS('includeonechan')
INCLUDESALTS     = wiz.getS('includesalts')
INCLUDESALTSHD   = wiz.getS('includesaltslite')
SEPERATE       = wiz.getS('seperate')
NOTIFY         = wiz.getS('notify')
NOTEID         = wiz.getS('noteid')
NOTEDISMISS    = wiz.getS('notedismiss')
TRAKTSAVE      = wiz.getS('traktlastsave')
REALSAVE       = wiz.getS('debridlastsave')
KEEPFAVS       = wiz.getS('keepfavourites')
KEEPGUI        = wiz.getS('keepgui')
KEEPSOURCES    = wiz.getS('keepsources')
KEEPPROFILES   = wiz.getS('keepprofiles')
KEEPADVANCED   = wiz.getS('keepadvanced')
KEEPTRAKT      = wiz.getS('keeptrakt')
KEEPREAL       = wiz.getS('keepdebrid')
KEEPLOGIN        = wiz.getS('keeplogin')
LOGINSAVE        = wiz.getS('loginlastsave')
TRAKT_EXODUS   = wiz.getS('exodus')
TRAKT_SALTS    = wiz.getS('salts')
TRAKT_SALTSHD  = wiz.getS('saltshd')
TRAKT_ROYALWE  = wiz.getS('royalwe')
TRAKT_VELOCITY = wiz.getS('velocity')
TRAKT_VELOKIDS = wiz.getS('velocitykids')
TRAKT_SPECTO   = wiz.getS('specto')
TRAKT_TRAKT    = wiz.getS('trakt')
REAL_EXODUS    = wiz.getS('realexodus')
REAL_SPECTO    = wiz.getS('realspecto')
REAL_URL       = wiz.getS('urlresolver')
DEVELOPER      = wiz.getS('developer')
BACKUPLOCATION   = ADDON.getSetting('path') if not ADDON.getSetting('path') == '' else 'special://home/'
MYBUILDS         = os.path.join(BACKUPLOCATION, 'My_Builds', '')
AUTOFEQ          = int(float(AUTOFEQ)) if AUTOFEQ.isdigit() else 0
TODAY          = date.today()
TOMORROW       = TODAY + timedelta(days=1)
THREEDAYS      = TODAY + timedelta(days=3)
KODIV          = float(xbmc.getInfoLabel("System.BuildVersion")[:4])
MCNAME         = "Kodi"
EXODUS         = 'plugin.video.exodus'
VELOCITY       = 'plugin.video.velocity'
VELOCITYKIDS   = 'plugin.video.velocitykids'
SALTS          = 'plugin.video.salts'
SALTSHD        = 'plugin.video.saltshd.lite'
ROYALWE        = 'plugin.video.theroyalwe'
SPECTO         = 'plugin.video.specto'
TRAKT          = 'script.trakt'
URLRESOLVER    = 'script.module.urlresolver'
PATHSALTS      = os.path.join(ADDONS, SALTS)
PATHSALTSHD    = os.path.join(ADDONS, SALTSHD)
PATHEXODUS     = os.path.join(ADDONS, EXODUS)
PATHVELOCITY   = os.path.join(ADDONS, VELOCITY)
PATHVELOCITYKI = os.path.join(ADDONS, VELOCITYKIDS)
PATHROYALWE    = os.path.join(ADDONS, ROYALWE)
PATHSPECTO     = os.path.join(ADDONS, SPECTO)
PATHTRAKT      = os.path.join(ADDONS, TRAKT)
PATHURL        = os.path.join(ADDONS, URLRESOLVER)
EXCLUDES       = [ADDON_ID, 'repository.SpinzTV', 'plugin.video.spinztvwiz', 'plugin.video.spinz', 'script.xtcodes.installer']
# 0 being every startup of kodi
UPDATECHECK    = 0
NEXTCHECK      = TODAY + timedelta(days=UPDATECHECK)
# Url to notification file
NOTIFICATION   = ''
# Enable Notification screen Yes or No
ENABLE         = 'No'
HEADERMESSAGE  = 'SpinzTV'
# Enable 'Contact' menu item 'Yes' hide or 'No' dont hide
HIDECONTACT    = 'No'
# You can add \n to do line breaks
CONTACT        = 'Thank you for choosing SpinzTV.\r\n\r\nContact us on facebook at http://facebook.com/groups/spinztv\r\n\r\nWebsite: www.spinztv.com'
# Hide the ====== seperators 'Yes' or 'No'
HIDESPACERS    = 'No'
COLOR1         = 'deepskyblue'
COLOR2         = 'white'
THEME1         = '[COLOR '+COLOR1+']%s[/COLOR]'
THEME2         = '[COLOR '+COLOR2+']%s[/COLOR]'
THEME3         = '[COLOR '+COLOR1+']%s[/COLOR]'
THEME4         = '[COLOR '+COLOR1+']Current Build:[/COLOR] [COLOR '+COLOR2+']%s[/COLOR]'
THEME5         = '[COLOR '+COLOR1+']Current Theme:[/COLOR] [COLOR '+COLOR2+']%s[/COLOR]'
AUTOUPDATE     = 'No'
ICONMAINT      = os.path.join(ART, 'mainticon.png')
ICONBUILDS     = os.path.join(ART, 'buildsicon.png')
ICONCONTACT    = os.path.join(ART, 'contacticon.png')
ICONAPK        = os.path.join(ART, 'apkicon.png')
ICONSAVE       = os.path.join(ART, 'saveicon.png')
ICONTRAKT      = os.path.join(ART, 'trakticon.png')
ICONREAL       = os.path.join(ART, 'realicon.png')
ICONSETTINGS   = os.path.join(ART, 'settingsicon.png')
ICONSPINZ      = os.path.join(ART, 'spinzicon.png')
ICONKODI       = os.path.join(ART, 'kodiicon.png')
ICONSPMC       = os.path.join(ART, 'kodiicon.png')
ICONGAMES      = os.path.join(ART, 'gamesicon.png')
ICONMOVIES     = os.path.join(ART, 'moviesicon.png')
ICONANDROID    = os.path.join(ART, 'droidicon.png')
ICONSPEED      = os.path.join(ART, 'speedicon.png')
ICONADDONS       = os.path.join(ART, 'spinzicon.png')
ICONYOUTUBE      = os.path.join(ART, 'spinzicon.png')
ICONLOGIN        = os.path.join(ART, 'spinzicon.png')
LOGFILES         = wiz.LOGFILES
TRAKTID          = traktit.TRAKTID
DEBRIDID         = debridit.DEBRIDID
LOGINID          = loginit.LOGINID
MODURL           = 'http://tribeca.tvaddons.ag/tools/maintenance/modules/'

###########################
###### URLS NEEDED ########
###########################
BUILDFILE      = base64.b64decode('aHR0cDovL3NwZXoudHYvc3Bpbnovd2l6YXJkdHh0L3NwaW56d2l6YXJkMS50eHQ=')
SPEEDFILE    = base64.b64decode('aHR0cDovL3NwZXoudHYvc3Bpbnovc3BlZWQvc3BlZWR0ZXN0LnR4dA==')
APKSPINZFILE = base64.b64decode('aHR0cDovL3NwZXoudHYvc3BpbnovYXBrdHh0cy9TcGluemFway50eHQ=')
VIDBUILDFILE = base64.b64decode('aHR0cDovL3NwZXoudHYvc3BpbnovdmlkZW90eHRzL2J1aWxkdmlkcy50eHQ=')
# Text File for addon installer.  Leave as 'http://' to ignore
ADDONFILE      = base64.b64decode('aHR0cDovL2FmdGVybWF0aHdpemFyZC5uZXQvcmVwby93aXphcmQvYWRkb25zLnR4dA==')
# Text File for advanced settings.  Leave as 'http://' to ignore
ADVANCEDFILE   = 'http://'
APKFILE      = base64.b64decode('aHR0cDovL3NwZXoudHYvc3BpbnovYXBrdHh0cy9TcGluelRWLWFway50eHQ=')
APKXXXFILE   = base64.b64decode('aHR0cDovL3NwZXoudHYvc3BpbnovYXBrdHh0cy94eHhhcGtzLnR4dA==')
SNESFILE  = base64.b64decode('aHR0cDovL3NwZXoudHYvc3BpbnovZW11bGF0b3Itcm9tdHh0L1JPTVNUWFQvU05FUy50eHQ=')
EMUFILE   = base64.b64decode('aHR0cDovL3NwZXoudHYvc3BpbnovZW11bGF0b3Itcm9tdHh0L2VtdWxhdG9yLnR4dA==')
SNESAFILE = base64.b64decode('aHR0cDovL3NwZXoudHYvc3BpbnovZW11bGF0b3Itcm9tdHh0L1JPTVNUWFQvU05FU0EtQi50eHQ=')
SNESCFILE = base64.b64decode('aHR0cDovL3NwZXoudHYvc3BpbnovZW11bGF0b3Itcm9tdHh0L1JPTVNUWFQvU05FU0MtRS50eHQ=')
SNESFFILE = base64.b64decode('aHR0cDovL3NwZXoudHYvc3BpbnovZW11bGF0b3Itcm9tdHh0L1JPTVNUWFQvU05FU0YtSC50eHQ=')
SNESIFILE = base64.b64decode('aHR0cDovL3NwZXoudHYvc3BpbnovZW11bGF0b3Itcm9tdHh0L1JPTVNUWFQvU05FU0ktSy50eHQ=')
SNESLFILE = base64.b64decode('aHR0cDovL3NwZXoudHYvc3BpbnovZW11bGF0b3Itcm9tdHh0L1JPTVNUWFQvU05FU0wtTS50eHQ=')
SNESNFILE = base64.b64decode('aHR0cDovL3NwZXoudHYvc3BpbnovZW11bGF0b3Itcm9tdHh0L1JPTVNUWFQvU05FU04tTy50eHQ=')
SNESPFILE = base64.b64decode('aHR0cDovL3NwZXoudHYvc3BpbnovZW11bGF0b3Itcm9tdHh0L1JPTVNUWFQvU05FU1AtUi50eHQ=')
SNESSFILE = base64.b64decode('aHR0cDovL3NwZXoudHYvc3BpbnovZW11bGF0b3Itcm9tdHh0L1JPTVNUWFQvU05FU1MudHh0')
SNESTFILE = base64.b64decode('aHR0cDovL3NwZXoudHYvc3BpbnovZW11bGF0b3Itcm9tdHh0L1JPTVNUWFQvU05FU1QtVi50eHQ=')
SNESWFILE = base64.b64decode('aHR0cDovL3NwZXoudHYvc3BpbnovZW11bGF0b3Itcm9tdHh0L1JPTVNUWFQvU05FU1ctWi50eHQ=')
NESAFILE  = base64.b64decode('aHR0cDovL3NwZXoudHYvc3BpbnovZW11bGF0b3Itcm9tdHh0L1JPTVNUWFQvTkVTQS1CLnR4dA==')
NESCFILE  = base64.b64decode('aHR0cDovL3NwZXoudHYvc3BpbnovZW11bGF0b3Itcm9tdHh0L1JPTVNUWFQvTkVTQy50eHQ=')
NESDFILE  = base64.b64decode('aHR0cDovL3NwZXoudHYvc3BpbnovZW11bGF0b3Itcm9tdHh0L1JPTVNUWFQvTkVTRC1FLnR4dA==')
NESFFILE  = base64.b64decode('aHR0cDovL3NwZXoudHYvc3BpbnovZW11bGF0b3Itcm9tdHh0L1JPTVNUWFQvTkVTRi1HLnR4dA==')
NESHFILE  = base64.b64decode('aHR0cDovL3NwZXoudHYvc3BpbnovZW11bGF0b3Itcm9tdHh0L1JPTVNUWFQvTkVTSC1LLnR4dA==')
NESLFILE  = base64.b64decode('aHR0cDovL3NwZXoudHYvc3BpbnovZW11bGF0b3Itcm9tdHh0L1JPTVNUWFQvTkVTTC1NLnR4dA==')
NESNFILE  = base64.b64decode('aHR0cDovL3NwZXoudHYvc3BpbnovZW11bGF0b3Itcm9tdHh0L1JPTVNUWFQvTkVTTi1RLnR4dA==')
NESRFILE  = base64.b64decode('aHR0cDovL3NwZXoudHYvc3BpbnovZW11bGF0b3Itcm9tdHh0L1JPTVNUWFQvTkVTUi1TLnR4dA==')
NESTFILE  = base64.b64decode('aHR0cDovL3NwZXoudHYvc3BpbnovZW11bGF0b3Itcm9tdHh0L1JPTVNUWFQvTkVTVC1WLnR4dA==')
NESWFILE  = base64.b64decode('aHR0cDovL3NwZXoudHYvc3BpbnovZW11bGF0b3Itcm9tdHh0L1JPTVNUWFQvTkVTVy1aLnR4dA==')
GENAFILE  = base64.b64decode('aHR0cDovL3NwZXoudHYvc3BpbnovZW11bGF0b3Itcm9tdHh0L1JPTVNUWFQvR0VOQS1CLnR4dA==')
GENCFILE  = base64.b64decode('aHR0cDovL3NwZXoudHYvc3BpbnovZW11bGF0b3Itcm9tdHh0L1JPTVNUWFQvR0VOQy1ELnR4dA==')
GENEFILE  = base64.b64decode('aHR0cDovL3NwZXoudHYvc3BpbnovZW11bGF0b3Itcm9tdHh0L1JPTVNUWFQvR0VORS1HLnR4dA==')
GENHFILE  = base64.b64decode('aHR0cDovL3NwZXoudHYvc3BpbnovZW11bGF0b3Itcm9tdHh0L1JPTVNUWFQvR0VOSC1MLnR4dA==')
GENMFILE  = base64.b64decode('aHR0cDovL3NwZXoudHYvc3BpbnovZW11bGF0b3Itcm9tdHh0L1JPTVNUWFQvR0VOTS1PLnR4dA==')
GENPFILE  = base64.b64decode('aHR0cDovL3NwZXoudHYvc3BpbnovZW11bGF0b3Itcm9tdHh0L1JPTVNUWFQvR0VOUC1SLnR4dA==')
GENSFILE  = base64.b64decode('aHR0cDovL3NwZXoudHYvc3BpbnovZW11bGF0b3Itcm9tdHh0L1JPTVNUWFQvR0VOUy1ULnR4dA==')
GENUFILE  = base64.b64decode('aHR0cDovL3NwZXoudHYvc3BpbnovZW11bGF0b3Itcm9tdHh0L1JPTVNUWFQvR0VOVS1aLnR4dA==')
ATRAFILE  = base64.b64decode('aHR0cDovL3NwZXoudHYvc3BpbnovZW11bGF0b3Itcm9tdHh0L1JPTVNUWFQvQVRSQS1CLnR4dA==')
ATRCFILE  = base64.b64decode('aHR0cDovL3NwZXoudHYvc3BpbnovZW11bGF0b3Itcm9tdHh0L1JPTVNUWFQvQVRSQy1ELnR4dA==')
ATREFILE  = base64.b64decode('aHR0cDovL3NwZXoudHYvc3BpbnovZW11bGF0b3Itcm9tdHh0L1JPTVNUWFQvQVRSRS1HLnR4dA==')
ATRHFILE  = base64.b64decode('aHR0cDovL3NwZXoudHYvc3BpbnovZW11bGF0b3Itcm9tdHh0L1JPTVNUWFQvQVRSSC1MLnR4dA==')
ATRMFILE  = base64.b64decode('aHR0cDovL3NwZXoudHYvc3BpbnovZW11bGF0b3Itcm9tdHh0L1JPTVNUWFQvQVRSTS1PLnR4dA==')
ATRPFILE  = base64.b64decode('aHR0cDovL3NwZXoudHYvc3BpbnovZW11bGF0b3Itcm9tdHh0L1JPTVNUWFQvQVRSUC1SLnR4dA==')
ATRSFILE  = base64.b64decode('aHR0cDovL3NwZXoudHYvc3BpbnovZW11bGF0b3Itcm9tdHh0L1JPTVNUWFQvQVRSUy1VLnR4dA==')
ATRVFILE  = base64.b64decode('aHR0cDovL3NwZXoudHYvc3BpbnovZW11bGF0b3Itcm9tdHh0L1JPTVNUWFQvQVRSVi1aLnR4dA==')
N64FILE	  = base64.b64decode('aHR0cDovL3NwZXoudHYvc3BpbnovZW11bGF0b3Itcm9tdHh0L1JPTVNUWFQvTjY0LnR4dA==')
N64AFILE  = base64.b64decode('aHR0cDovL3NwZXoudHYvc3BpbnovZW11bGF0b3Itcm9tdHh0L1JPTVNUWFQvTjY0QS1CLnR4dA==')
N64CFILE  = base64.b64decode('aHR0cDovL3NwZXoudHYvc3BpbnovZW11bGF0b3Itcm9tdHh0L1JPTVNUWFQvTjY0Qy1FLnR4dA==')
N64FFILE  = base64.b64decode('aHR0cDovL3NwZXoudHYvc3BpbnovZW11bGF0b3Itcm9tdHh0L1JPTVNUWFQvTjY0Ri1KLnR4dA==')
N64KFILE  = base64.b64decode('aHR0cDovL3NwZXoudHYvc3BpbnovZW11bGF0b3Itcm9tdHh0L1JPTVNUWFQvTjY0Sy1NLnR4dA==')
N64NFILE  = base64.b64decode('aHR0cDovL3NwZXoudHYvc3BpbnovZW11bGF0b3Itcm9tdHh0L1JPTVNUWFQvTjY0Ti1SLnR4dA==')
N64SFILE  = base64.b64decode('aHR0cDovL3NwZXoudHYvc3BpbnovZW11bGF0b3Itcm9tdHh0L1JPTVNUWFQvTjY0Uy1ULnR4dA==')
N64VFILE  = base64.b64decode('aHR0cDovL3NwZXoudHYvc3BpbnovZW11bGF0b3Itcm9tdHh0L1JPTVNUWFQvTjY0Vi1aLnR4dA==')
TGAFILE	  = base64.b64decode('aHR0cDovL3NwZXoudHYvc3BpbnovZW11bGF0b3Itcm9tdHh0L1JPTVNUWFQvVEdBLUIudHh0')
TGCFILE	  = base64.b64decode('aHR0cDovL3NwZXoudHYvc3BpbnovZW11bGF0b3Itcm9tdHh0L1JPTVNUWFQvVEdDLUUudHh0')
TGFFILE	  = base64.b64decode('aHR0cDovL3NwZXoudHYvc3BpbnovZW11bGF0b3Itcm9tdHh0L1JPTVNUWFQvVEdGLUkudHh0')
TGJFILE	  = base64.b64decode('aHR0cDovL3NwZXoudHYvc3BpbnovZW11bGF0b3Itcm9tdHh0L1JPTVNUWFQvVEdKLU0udHh0')
TGNFILE	  = base64.b64decode('aHR0cDovL3NwZXoudHYvc3BpbnovZW11bGF0b3Itcm9tdHh0L1JPTVNUWFQvVEdOLVEudHh0')
TGRFILE	  = base64.b64decode('aHR0cDovL3NwZXoudHYvc3BpbnovZW11bGF0b3Itcm9tdHh0L1JPTVNUWFQvVEdSLVUudHh0')
TGVFILE	  = base64.b64decode('aHR0cDovL3NwZXoudHYvc3BpbnovZW11bGF0b3Itcm9tdHh0L1JPTVNUWFQvVEdWLVoudHh0')
NDSAFILE  = base64.b64decode('aHR0cDovL3NwZXoudHYvc3BpbnovZW11bGF0b3Itcm9tdHh0L1JPTVNUWFQvTkRTQS50eHQ=')
NDSBFILE  = base64.b64decode('aHR0cDovL3NwZXoudHYvc3BpbnovZW11bGF0b3Itcm9tdHh0L1JPTVNUWFQvTkRTQi50eHQ=')
NDSCFILE  = base64.b64decode('aHR0cDovL3NwZXoudHYvc3BpbnovZW11bGF0b3Itcm9tdHh0L1JPTVNUWFQvTkRTQy50eHQ=')
NDSDFILE  = base64.b64decode('aHR0cDovL3NwZXoudHYvc3BpbnovZW11bGF0b3Itcm9tdHh0L1JPTVNUWFQvTkRTRC50eHQ=')
NDSEFILE  = base64.b64decode('aHR0cDovL3NwZXoudHYvc3BpbnovZW11bGF0b3Itcm9tdHh0L1JPTVNUWFQvTkRTRS1GLnR4dA==')
NDSGFILE  = base64.b64decode('aHR0cDovL3NwZXoudHYvc3BpbnovZW11bGF0b3Itcm9tdHh0L1JPTVNUWFQvTkRTRy1ILnR4dA==')
NDSIFILE  = base64.b64decode('aHR0cDovL3NwZXoudHYvc3BpbnovZW11bGF0b3Itcm9tdHh0L1JPTVNUWFQvTkRTSS1KLnR4dA==')
NDSKFILE  = base64.b64decode('aHR0cDovL3NwZXoudHYvc3BpbnovZW11bGF0b3Itcm9tdHh0L1JPTVNUWFQvTkRTSy1MLnR4dA==')
NDSMFILE  = base64.b64decode('aHR0cDovL3NwZXoudHYvc3BpbnovZW11bGF0b3Itcm9tdHh0L1JPTVNUWFQvTkRTTS50eHQ=')
NDSNFILE  = base64.b64decode('aHR0cDovL3NwZXoudHYvc3BpbnovZW11bGF0b3Itcm9tdHh0L1JPTVNUWFQvTkRTTi1PLnR4dA==')
NDSPFILE  = base64.b64decode('aHR0cDovL3NwZXoudHYvc3BpbnovZW11bGF0b3Itcm9tdHh0L1JPTVNUWFQvTkRTUC1RLnR4dA==')
NDSRFILE  = base64.b64decode('aHR0cDovL3NwZXoudHYvc3BpbnovZW11bGF0b3Itcm9tdHh0L1JPTVNUWFQvTkRTUi50eHQ=')
NDSSFILE  = base64.b64decode('aHR0cDovL3NwZXoudHYvc3BpbnovZW11bGF0b3Itcm9tdHh0L1JPTVNUWFQvTkRTUy50eHQ=')
NDSTFILE  = base64.b64decode('aHR0cDovL3NwZXoudHYvc3BpbnovZW11bGF0b3Itcm9tdHh0L1JPTVNUWFQvTkRTVC1VLnR4dA==')
NDSVFILE  = base64.b64decode('aHR0cDovL3NwZXoudHYvc3BpbnovZW11bGF0b3Itcm9tdHh0L1JPTVNUWFQvTkRTVi1aLnR4dA==')
PSAFILE   = base64.b64decode('aHR0cDovL3NwZXoudHYvc3BpbnovZW11bGF0b3Itcm9tdHh0L1JPTVNUWFQvUFNBLnR4dA==')
PSBFILE   = base64.b64decode('aHR0cDovL3NwZXoudHYvc3BpbnovZW11bGF0b3Itcm9tdHh0L1JPTVNUWFQvUFNCLnR4dA==')
PSCFILE   = base64.b64decode('aHR0cDovL3NwZXoudHYvc3BpbnovZW11bGF0b3Itcm9tdHh0L1JPTVNUWFQvUFNDLUQudHh0')
PSEFILE   = base64.b64decode('aHR0cDovL3NwZXoudHYvc3BpbnovZW11bGF0b3Itcm9tdHh0L1JPTVNUWFQvUFNFLUYudHh0')
PSGFILE   = base64.b64decode('aHR0cDovL3NwZXoudHYvc3BpbnovZW11bGF0b3Itcm9tdHh0L1JPTVNUWFQvUFNHLUoudHh0')
PSKFILE   = base64.b64decode('aHR0cDovL3NwZXoudHYvc3BpbnovZW11bGF0b3Itcm9tdHh0L1JPTVNUWFQvUFNLLU4udHh0')
PSOFILE   = base64.b64decode('aHR0cDovL3NwZXoudHYvc3BpbnovZW11bGF0b3Itcm9tdHh0L1JPTVNUWFQvUFNPLVIudHh0')
PSSFILE   = base64.b64decode('aHR0cDovL3NwZXoudHYvc3BpbnovZW11bGF0b3Itcm9tdHh0L1JPTVNUWFQvUFNTLVQudHh0')
PSUFILE   = base64.b64decode('aHR0cDovL3NwZXoudHYvc3BpbnovZW11bGF0b3Itcm9tdHh0L1JPTVNUWFQvUFNVLVoudHh0')
###########################
##### WORKINGURLS #########
###########################
WORKINGURL     = wiz.workingURL(BUILDFILE)
###########################
###### Menu Items   #######
###########################
#addDir (display,mode,name=None,url=None,menu=None,overwrite=True,fanart=FANART,icon=ICON, themeit=None)
#addFile(display,mode,name=None,url=None,menu=None,overwrite=True,fanart=FANART,icon=ICON, themeit=None)

########################################
##########Main Menu Display#############
########################################
def index():
	if AUTOUPDATE == 'Yes':
		if wiz.workingURL(WIZARDFILE) == True:
			ver = wiz.checkWizard('version')
			if ver > VERSION: addFile('%s [v%s] [COLOR red][B][UPDATE v%s][/B][/COLOR]' % (ADDONTITLE, VERSION, ver), 'wizardupdate', themeit=THEME2)
			else: addFile('%s [v%s]' % (ADDONTITLE, VERSION), '', themeit=THEME2)
		else: addFile('%s [v%s]' % (ADDONTITLE, VERSION), '', themeit=THEME2)
	else: addFile('%s [v%s]' % (ADDONTITLE, VERSION), '', themeit=THEME2)
	if len(BUILDNAME) > 0:
		version = wiz.checkBuild(BUILDNAME, 'version')
		build = '%s (v%s)' % (BUILDNAME, BUILDVERSION)
		if version > BUILDVERSION: build = '%s [COLOR red][B][UPDATE v%s][/B][/COLOR]' % (build, version)
		addDir(build,'viewbuild',BUILDNAME, themeit=THEME4)
		themefile = wiz.checkBuild(BUILDNAME, 'theme')
		if not themefile == 'http://' and wiz.workingURL(themefile) == True:
			addFile('None' if BUILDTHEME == "" else BUILDTHEME, 'theme', BUILDNAME, themeit=THEME5)
	else: addDir('None', 'builds', themeit=THEME4)
	if HIDESPACERS == 'No': addFile('============================================', '', themeit=THEME3)
	addDir ('SpinzTV Builds'        ,'builds',   icon=ICONBUILDS,   themeit=THEME1)
	addDir ('Maintenance'   ,'maint',    icon=ICONMAINT,    themeit=THEME1)
	addFile ('Speed Test'   ,'speed',    icon=ICONSPEED,    themeit=THEME1)
	addDir ('Android Zone' ,'apk1',      icon=ICONAPK,      themeit=THEME1)
	if not ADDONFILE == 'http://': addDir1 ('Addon Installer' ,'addons', icon=ICONADDONS, themeit=THEME1)
	addDir ('Save Data'     ,'savedata', icon=ICONSAVE,     themeit=THEME1)
	if HIDECONTACT == 'No': addFile('Contact'      ,'contact',  icon=ICONCONTACT,  themeit=THEME1)
	if HIDESPACERS == 'No': addFile('============================================', '', themeit=THEME3)
	addFile('Settings'      ,'settings', icon=ICONSETTINGS, themeit=THEME1)
	if DEVELOPER == 'true': addDir ('Developer Menu','developer', icon=ICONSETTINGS, themeit=THEME1)
	setView('movies', 'MAIN')

########################################
###########Builds Menu Display##########
########################################
def buildMenu():
	WORKINGURL       = wiz.workingURL(BUILDFILE)
	if not WORKINGURL == True:
		addFile1('%s Version: %s' % (MCNAME, KODIV), '', icon=ICONBUILDS, themeit=THEME3)
		if HIDESPACERS == 'No': addFile(wiz.sep(), '', themeit=THEME3)
		addFile1('Url for txt file not valid', '', icon=ICONBUILDS, themeit=THEME3)
		addFile1('%s' % WORKINGURL, '', icon=ICONBUILDS, themeit=THEME3)
	else:	
		link  = wiz.openURL(BUILDFILE).replace('\n','').replace('\r','').replace('\t','').replace('gui=""', 'gui="http://"').replace('theme=""', 'theme="http://"')
		match = re.compile('name="(.+?)".+?ersion="(.+?)".+?rl="(.+?)".+?ui="(.+?)".+?odi="(.+?)".+?heme="(.+?)".+?con="(.+?)".+?anart="(.+?)".+?dult="(.+?)".+?escription="(.+?)"').findall(link)
		if len(match) == 1:
			viewBuild(match[0][0])
		elif len(match) > 1:
			addFile1('[B]%s Version: %s[/B]' % (MCNAME, KODIV), '', icon=ICONBUILDS, themeit=THEME2)
			addDir ('Video Preview Of Builds'    ,'youtube', url=VIDBUILDFILE, icon=ICONSPINZ, themeit=THEME1)
			addDir1 ('Save Data Menu'       ,'savedata', icon=ICONSAVE,     themeit=THEME3)
			if HIDESPACERS == 'No': addFile(wiz.sep(), '', themeit=THEME3)
			if SEPERATE == 'true':
				for name, version, url, gui, kodi, theme, icon, fanart, adult, description in match:
					if not SHOWADULT == 'true' and adult.lower() == 'yes': continue
					menu = createMenu('install', '', name)
					addDir1('[%s] %s (v%s)' % (float(kodi), name, version), 'viewbuild', name, description=description, fanart=fanart,icon=icon, menu=menu, themeit=THEME2)
			else:
				count15 = wiz.buildCount('15'); count16 = wiz.buildCount('16'); count17 = wiz.buildCount('17');
				if count17 > 0:
					state = '+' if SHOW17 == 'false' else '-'
					addFile1('[B]%s Krypton Builds(%s)[/B]' % (state, count16), 'togglesetting',  'show17', themeit=THEME3)
					if SHOW17 == 'true':
						for name, version, url, gui, kodi, theme, icon, fanart, adult, description in match:
							if not SHOWADULT == 'true' and adult.lower() == 'yes': continue
							kodiv = int(float(kodi))
							if kodiv == 17:
								menu = createMenu('install', '', name)
								addDir1('[%s] %s (v%s)' % (float(kodi), name, version), 'viewbuild', name, description=description, fanart=fanart,icon=icon, menu=menu, themeit=THEME2)
				if count16 > 0:
					state = '+' if SHOW16 == 'false' else '-'
					addFile1('[B]%s Jarvis Builds(%s)[/B]' % (state, count16), 'togglesetting',  'show16', themeit=THEME3)
					if SHOW16 == 'true':
						for name, version, url, gui, kodi, theme, icon, fanart, adult, description in match:
							if not SHOWADULT == 'true' and adult.lower() == 'yes': continue
							kodiv = int(float(kodi))
							if kodiv == 16:
								menu = createMenu('install', '', name)
								addDir1('[%s] %s (v%s)' % (float(kodi), name, version), 'viewbuild', name, description=description, fanart=fanart,icon=icon, menu=menu, themeit=THEME2)
				if count15 > 0:
					state = '+' if SHOW15 == 'false' else '-'
					addFile('[B]%s Isengard and Below Builds(%s)[/B]' % (state, count15), 'togglesetting',  'show15', themeit=THEME3)
					if SHOW15 == 'true':
						for name, version, url, gui, kodi, theme, icon, fanart, adult, description in match:
							if not SHOWADULT == 'true' and adult.lower() == 'yes': continue
							kodiv = int(float(kodi))
							if kodiv <= 15:
								menu = createMenu('install', '', name)
								addDir1('[%s] %s (v%s)' % (float(kodi), name, version), 'viewbuild', name, description=description, fanart=fanart,icon=icon, menu=menu, themeit=THEME2)
		else: addFile('Text file for builds not formated correctly.', '', icon=ICONBUILDS, themeit=THEME3)
	setView('files', 'viewType')

def viewBuild(name):
	WORKINGURL = wiz.workingURL(BUILDFILE)
	if not WORKINGURL == True:
		addFile1('Url for txt file not valid', '', themeit=THEME3)
		addFile1('%s' % WORKINGURL, '', themeit=THEME3)
		return
	if wiz.checkBuild(name, 'version') == False: 
		addFile1('Error reading the txt file.', '', themeit=THEME3)
		addFile1('%s was not found in the builds list.' % name, '', themeit=THEME3)
		return
	link = wiz.openURL(BUILDFILE).replace('\n','').replace('\r','').replace('\t','').replace('gui=""', 'gui="http://"').replace('theme=""', 'theme="http://"')
	match = re.compile('name="%s".+?ersion="(.+?)".+?rl="(.+?)".+?ui="(.+?)".+?odi="(.+?)".+?heme="(.+?)".+?con="(.+?)".+?anart="(.+?)".+?dult="(.+?)".+?escription="(.+?)"' % name).findall(link)
	for version, url, gui, kodi, themefile, icon, fanart, adult, description in match:
		icon        = icon   if wiz.workingURL(icon)   else ICON
		fanart      = fanart if wiz.workingURL(fanart) else FANART
		build       = '%s (v%s)' % (name, version)
		if BUILDNAME == name and version > BUILDVERSION:
			build = '%s [COLOR red][CURRENT v%s][/COLOR]' % (build, BUILDVERSION)
		addFile1(build, '', description=description, fanart=fanart, icon=icon, themeit=THEME4)
		if HIDESPACERS == 'No': addFile(wiz.sep(), '', themeit=THEME3)
		addFile1('Build Information'    ,'buildinfo', name, description=description, fanart=fanart, icon=icon, themeit=THEME3)
		addDir1 ('Save Data Menu'       ,'savedata', icon=ICONSAVE,     themeit=THEME3)
		temp1 = int(float(KODIV)); temp2 = int(float(kodi))
		if not temp1 == temp2: 
			if temp1 == 16 and temp2 <= 15: warning = False
			else: warning = True
		else: warning = False
		if warning == True:
			addFile('[I]Build designed for kodi version %s(installed: %s)[/I]' % (str(kodi), str(KODIV)), '', fanart=fanart, icon=icon, themeit=THEME3)
		addFile1(wiz.sep('INSTALL'), '', fanart=fanart, icon=icon, themeit=THEME3)
		addFile1('Fresh Install'   , 'install', name, 'fresh'  , description=description, fanart=fanart, icon=icon, themeit=THEME1)
		addFile1('Standard Install', 'install', name, 'normal' , description=description, fanart=fanart, icon=icon, themeit=THEME1)
		if not gui == 'http://': addFile1('Apply guiFix'    , 'install', name, 'gui'     , description=description, fanart=fanart, icon=icon, themeit=THEME1)
		if not themefile == 'http://':
			if wiz.workingURL(themefile) == True:
				addFile1(wiz.sep('THEMES'), '', fanart=fanart, icon=icon, themeit=THEME3)
				link  = wiz.openURL(themefile).replace('\n','').replace('\r','').replace('\t','')
				match = re.compile('name="(.+?)".+?rl="(.+?)".+?con="(.+?)".+?anart="(.+?)".+?escription="(.+?)"').findall(link)
				for themename, themeurl, themeicon, themefanart, description in match:
					themeicon   = themeicon   if themeicon   == 'http://' else icon
					themefanart = themefanart if themefanart == 'http://' else fanart
					addFile1(themename if not themename == BUILDTHEME else "[B]%s (Installed)[/B]" % themename, 'theme', name, themename, description=description, fanart=themefanart, icon=themeicon, themeit=THEME3)
	setView('files', 'viewType')

########## Search ################
##################################
#def Search(searchtext):
 #       search_entered = ''
  #      keyboard = xbmc.Keyboard(search_entered,searchtext)
   #     keyboard.doModal()
    #    if keyboard.isConfirmed():
     #       search_entered =  keyboard.getText() .replace('!','').replace("'",'').replace(',','').lower().replace('?','').replace('.','').replace(' ','\n').splitlines()
      #      if search_entered == None:
       #         return False          
        #return search_entered

##################################
#########APK Menu's###############
##################################
def apkMenu():
	addDir ('Emulators And Roms'        ,'emurom',    icon=ICONGAMES, themeit=THEME1)
	addDir ('SpinzTV APKS'    ,'apkshow', url=APKSPINZFILE, icon=ICONSPINZ, themeit=THEME1)
	addDir ('[COLOR deepskyblue]APK Drawer[/COLOR]', 'intellaunch',)
	addDir ('Kodi and SPMC'        ,'apkkodi',    icon=ICONKODI, themeit=THEME1)
	html=OPEN_URL(base64.b64decode('aHR0cHM6Ly93d3cuYXBrZmlsZXMuY29tLw=='))
	match = re.compile('href="([^"]*)">Applications(.+?)</a>').findall(html)
	match2 = re.compile('href="([^"]*)">Games(.+?)</a>').findall(html)
	for url,count in match:
		addDir2('[COLOR deepskyblue]Android Apps[/COLOR]'+count,'https://www.apkfiles.com'+url,'apkgame',ART+'apps.png')
	for url,count in match2:
		addDir2('[COLOR deepskyblue]Android Games[/COLOR]'+count,'https://www.apkfiles.com'+url,'apkgame',ART+'GAMES.png')
	setView('movies', 'MAIN')
	addDir ('Spinz Apk Picks'        ,'apkshow', url=APKFILE,   icon=ICONAPK, themeit=THEME1)
	if SHOWADULT == 'true': addDir ('XXX Apk'        ,'apkshow', url=APKXXXFILE,   icon=ICONAPK, themeit=THEME1)

def apkshowMenu(url):
	if not workingURL(url) == True: return False
	link = OPEN_URL(url).replace('\n','').replace('\r','').replace('\t','')
	match = re.compile('name="(.+?)".+?rl="(.+?)".+?con="(.+?)".+?anart="(.+?)"').findall(link)
	if len(match) > 0:
		for name, url, icon, fanart in match:
			addFile(name, 'apkinstall', name, url, icon=icon, fanart=fanart, themeit=THEME1)
		else: wiz.log("[APK Menu] ERROR: Invalid Format.")
	else: wiz.log("[APK Menu] ERROR: URL for emu list not working.")

def APKGAME(url):
	html=OPEN_URL(url)
	match = re.compile('<a href="([^"]*)" >(.+?)</a>').findall(html)
	for url,name in match:
		if '/cat' in url:
			addDir2((name).replace('&amp;',' - '),'https://www.apkfiles.com'+url,'select',ART+'APK.png')

def APKSELECT2(url):
	html=OPEN_URL(url)
	url1 = url
	if "page=" in str(url):
		url1 = url.split('?')[0]
	match = re.compile('<a href="([^"]*)".+?<img src="([^"]*)" class="file_list_icon".+?alt="([^"]*)"',re.DOTALL).findall(html)
	match2 = re.compile('class="[^"]*".+?ref="([^"]*)".+?yle=.+?</a>').findall(html)
	for url,img,name in match:
		if 'apk' in url:
			addDir2((name).replace('&#39;','').replace('&amp;',' - ').replace('&#174;:',': ').replace('&#174;',' '),'https://www.apkfiles.com'+url,'grab','http:'+img)
	if len(match2) > 1:
		match2 = str(match2[len(match2) - 1])
	addDir2('Next Page',url1+str(match2),'select',ART+'Next.png')

def APKGRAB(name,url):
	html=OPEN_URL(url)
	name=name
	match = re.compile('href="([^"]*)".+?lass="yellow_button".+?itle=').findall(html)
	for url in match:
		url = 'https://www.apkfiles.com'+url
		apkInstaller(name,url,'Brackets')

def apkkodiMenu():
	addFile('Kodi (v%s)' % wiz.latestApk('kodi','version')     ,'apkinstall',  'kodi', wiz.latestApk('kodi','url'), icon=ICONKODI, themeit=THEME1)
	addFile('SPMC (v%s)' % wiz.latestApk('spmc','version')     ,'apkinstall',  'spmc', wiz.latestApk('spmc','url'), icon=ICONSPMC, themeit=THEME1)

############################
##### Intelli Stuff ########
############################
def iiNT3LiiLauncher():
	#global theNotList
	if os.path.isfile(iiNT3LiiListAPK):
		iiNT3LiiThere = True
		iiNT3LiiList = open(iiNT3LiiListAPK)
		iiNT3LiiRead = iiNT3LiiList.read()
		iiNT3LiiList.close()
	else:
		xbmcgui.Dialog().ok("[COLOR orange]SpinzTV[/COLOR]","[COLOR cyan][B]][[/B]NT3L[B]][[/B]G3NC[B]][[/B][/COLOR]","[COLOR ghostwhite]First Time Launching Will Take a Couple Minutes[/COLOR]","[COLOR ghostwhite]Please Be Patient![/COLOR]")
		iiNT3LiiThere = False

	#if os.path.isfile(iiNT3LiiNotAPK):
	#	iiNT3LiiNotThere = True
	#	iiNT3LiiNotList = open(iiNT3LiiNotAPK)
	#	iiNT3LiiNotRead = iiNT3LiiNotList.read()
	#	iiNT3LiiNotList.close()

	#else:
	#	iiNT3LiiNotThere = False

	#theNotList = ""
	theList = ""
	InstalledAPK = iiNT3LiiAPK()
	for i in InstalledAPK:
		if iiNT3LiiThere==True:
			if i not in iiNT3LiiRead:
				#if iiNT3LiiNotThere==True:
				#if i not in iiNT3LiiNotRead:
				getList = iiNT3LiiScrape(theList,i)
				theList=getList

		else:
			getList = iiNT3LiiScrape(theList,i)
			theList=getList

	if iiNT3LiiThere==True:
		iiNT3LiiList = open(iiNT3LiiListAPK,'a')
		#iiNT3LiiNotList = open(iiNT3LiiNotAPK,'a')

	else:
		iiNT3LiiList = open(iiNT3LiiListAPK,'w')
		#iiNT3LiiNotList = open(iiNT3LiiNotAPK,'w')

	iiNT3LiiList.write(theList)
	iiNT3LiiList.close()
	#iiNT3LiiNotList.write(theNotList)
	#iiNT3LiiNotList.close()
	iiNT3LiiList = open(iiNT3LiiListAPK)
	iiNT3LiiRead = iiNT3LiiList.read()
	iiNT3LiiList.close()
	iiNT3LiiRead = iiNT3LiiRead.replace('\n','').replace('\r','')
	match = re.compile('name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)".+?nstallRating="(.+?)"').findall(iiNT3LiiRead)


	for name,url,iconimage,fanart,description,installRating in sorted(match, key=lambda match: match[0]):
		if url in InstalledAPK:
			addDir88('[COLOR ghostwhite]'+str(name)+'[/COLOR]',url,'intelselect',iconimage,fanart,description,installRating)

def iiNT3LiiAPK():
	if xbmc.getCondVisibility('system.platform.android'):
		try:
			InstalledAPK = subprocess.Popen(['exec ''/system/bin/pm list packages -3'''], executable='/system/bin/sh', shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT).communicate()[0].rstrip('\n').splitlines()
		except:
			InstalledAPK = []

		for i in range(len(InstalledAPK)):
			InstalledAPK[i] = InstalledAPK[i].partition(':')[2]

	return InstalledAPK

def iiNT3LiiScrape(theList,i):
	global theNotList
	iiNT3Liiurl = "https://play.google.com/store/apps/details?id=" +i
	link = iiNT3LiiCheckURL(iiNT3Liiurl)

	if link !=False:
		link = link.replace('\n','').replace('\r','')
		# Title
		regexTitle = r'<div class="id-app-title".tabindex=".">(.+?)</div>'
		match = re.search(regexTitle, link)
		if match != None: name = match.group(1)
		else: name = i
		# Icon
		#regexIcon = r'<img class="cover-image" src="(.+?w[0-9]{2,3})"'
		#match = re.search(regexIcon, link)
		#if match != None: iconimage = "https:"+match.group(1)
		#else:
		iconimage = "androidapp://sources/apps/"+str(i)+".png"
		# Banner
		#regexBanner = r'<img class="video-image" src="(.+?.[jp][np]?[g])"'
		#match = re.search(regexBanner, link)
		#if match != None: Banner = "https:" +match.group(1)
		#else: Banner = "None"
		# BackDrop
		regexBackdrop = r'data-expand-to="full-screenshot-[0-9]{1,2}" src="(//\w+?.\w+?.\S+?=h900)"'
		match = re.compile(regexBackdrop).findall(link)
		if len(match) != 0: fanart = "https:" +match[len(match) - 1]
		else: fanart = "None"
		# VideoLink
		regexVideo = r'data-video-url="https://www.youtube.com/embed/(\S.+?)\?ps=play.+?"'
		match = re.search(regexVideo, link)
		if match != None: description = match.group(1)
		else: description = "None"
		# Total Installs
		regexInstall = r'<div class="content" itemprop="numDownloads">\s+?(\d.+?\s-\s\d.+?)\s+?</div>'
		match = re.search(regexInstall, link)
		if match != None: numInstalled = 'Installed '+match.group(1)
		else: numInstalled = "Installs: N/A"
		# Apps Rating
		regexRating = r'<div class="score" aria-label=" Rated .+? stars out of five stars ">(.+?)</div>'
		match = re.search(regexRating, link)
		if match != None: appRating = match.group(1)+ " Stars"
		else: appRating = "Rating: N/A"
		installRating = appRating+ " " +numInstalled
		#regex = r'(Rating:).(.+?)(Stars).(Installs:).+?(\d.+?\s-\s\d.+?)\s'
		#match = re.compile(regex).findall(installRating)

		url = i
		theList += 'name="'+name+'"url="'+url+'"img="'+iconimage+'"fanart="'+fanart+'"description="'+description+'"installRating="'+installRating+'"'
		return theList
#
#			else:
#				theNotList +=  'url="'+i+'"'
#				return theList
#
#		else:
#			theNotList +=  'url="'+i+'"'
#			return theList
#
	else:
#		theNotList += 'url="'+i+'"'
		return theList

def iiNT3LiiSelector(name,url,iconimage,fanart,videolink):
	menuTotal=0

	if videolink != "None":
		menuTotal += 1

	if menuTotal==1: MenuItem = xbmcgui.Dialog().select('[COLOR deepskyblue]'+name+'[/COLOR]', ['[COLOR deepskyblue]Launch[/COLOR]','[COLOR ghostwhite]Preview Video[/COLOR]','[COLOR tomato]Uninstall[/COLOR]'])
	if menuTotal==0: MenuItem = xbmcgui.Dialog().select('[COLOR deepskyblue]'+name+'[/COLOR]', ['[COLOR deepskyblue]Launch[/COLOR]','[COLOR ghostwhite]No Preview Video[/COLOR]','[COLOR tomato]Uninstall[/COLOR]'])



	if MenuItem==1:
		if videolink != 'None':
			yt.PlayVideo(videolink)
	if MenuItem==0:
		startAPK = xbmcgui.Dialog().yesno("[COLOR orange]SpinzTV[/COLOR]","[COLOR cyan][B]][[/B]NT3L[B]][[/B]G3NC[B]][[/B][/COLOR]","","[COLOR ghostwhite]Would You Like To Launch:[/COLOR] [COLOR cyan]"+name+"[/COLOR]","[COLOR red]No Way[/COLOR]","[COLOR cyan]Heck Ya![/COLOR]")
		if startAPK==1:
			xbmc.executebuiltin('StartAndroidActivity(%s)'% url)
	if MenuItem==2:
		apkRemover = xbmcgui.Dialog().yesno("[COLOR orange]SpinzTV[/COLOR]","[COLOR cyan][B]][[/B]NT3L[B]][[/B]G3NC[B]][[/B][/COLOR]","","[COLOR ghostwhite]Would You Like To Remove:[/COLOR] [COLOR cyan]"+name+"[/COLOR]","[COLOR red]No Way[/COLOR]","[COLOR cyan]Heck Ya![/COLOR]")
		if apkRemover:
			xbmc.executebuiltin('StartAndroidActivity("","android.intent.action.DELETE","","package:'+url+'")')
			xbmc.sleep(2000)
			try: shutil.rmtree("/sdcard/Android/data/"+url,ignore_errors=True, onerror=None)
			except: pass
			try: shutil.rmtree("/sdcard/Android/obb/"+url,ignore_errors=True, onerror=None)
			except: pass
			xbmc.executebuiltin('Container.Refresh')

def iiNT3LiiCheckURL(url):
	try:
		req = urllib2.Request(url)
		req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
		response = urllib2.urlopen(req)
		link=response.read()
		response.close()
		return link
	except:
		return False
############################
####### EMULATOR ###########
############################
def emuromMenu():
	addDir ('Emulators'    ,'apkshow', url=EMUFILE, icon=ICONGAMES, themeit=THEME1)
	addDir ('Roms'        ,'roms',     icon=ICONGAMES, themeit=THEME1)
	
####################################
######ROM STUFF#####################
####################################
def romsMenu():
		addDir ('NES'        ,'nes',    icon=ICONGAMES, themeit=THEME1)
		addDir ('SNES'        ,'snes',    icon=ICONGAMES, themeit=THEME1)
		addDir ('Nintendo 64'        ,'n64',    icon=ICONGAMES, themeit=THEME1)
		addDir ('Nintendo DS'        ,'nds',    icon=ICONGAMES, themeit=THEME1)
		addDir ('Genesis'        ,'gen',    icon=ICONGAMES, themeit=THEME1)
		addDir ('Playstation'        ,'ps',    icon=ICONGAMES, themeit=THEME1)
		addDir ('Atari'        ,'atr',    icon=ICONGAMES, themeit=THEME1)
		addDir ('PC Engine & Turbo Grafx'        ,'tbg',    icon=ICONGAMES, themeit=THEME1)

def romMenu(url):
	if not workingURL(url) == True: return False
	link = OPEN_URL(url).replace('\n','').replace('\r','').replace('\t','')
	match = re.compile('.+?ame="(.+?)".+?rl="(.+?)".+?con="(.+?)".+?anart="(.+?)"description="(.+?)"').findall(link)
	if len(match) > 0:
		for name, url, icon, fanart, description in match:
			addFILE(name, 'rominstall', name, url, icon=icon, fanart=fanart, description=description, themeit=THEME1)
		else: wiz.log("[ROM Menu] ERROR: Invalid Format.")
	else: wiz.log("[ROM Menu] ERROR: URL for apk list not working.")

#####################################
#########   SNES     ################
#####################################
def snesMenu():
		addDir ('SNES Titles A Thru B', 'rom', url=SNESAFILE, icon=ICONGAMES, themeit=THEME1)
		addDir ('SNES Titles C Thru E', 'rom', url=SNESCFILE, icon=ICONGAMES, themeit=THEME1)
		addDir ('SNES Titles F Thru H', 'rom', url=SNESFFILE, icon=ICONGAMES, themeit=THEME1)
		addDir ('SNES Titles I Thru K', 'rom', url=SNESIFILE, icon=ICONGAMES, themeit=THEME1)
		addDir ('SNES Titles L Thru M', 'rom', url=SNESLFILE, icon=ICONGAMES, themeit=THEME1)
		addDir ('SNES Titles N Thru O', 'rom', url=SNESNFILE, icon=ICONGAMES, themeit=THEME1)
		addDir ('SNES Titles P Thru R', 'rom', url=SNESPFILE, icon=ICONGAMES, themeit=THEME1)
		addDir ('SNES Titles S', 'rom', url=SNESSFILE, icon=ICONGAMES, themeit=THEME1)
		addDir ('SNES Titles T Thru V', 'rom', url=SNESTFILE, icon=ICONGAMES, themeit=THEME1)
		addDir ('SNES Titles W Thru Z', 'rom', url=SNESWFILE, icon=ICONGAMES, themeit=THEME1)

############################################################
######################   NES    ############################
############################################################
def nesMenu():
		addDir ('NES Titles A Thru B', 'rom', url=NESAFILE, icon=ICONGAMES, themeit=THEME1)
		addDir ('NES Titles C', 'rom', url=NESCFILE, icon=ICONAPK, themeit=THEME1)
		addDir ('NES Titles D Thru E', 'rom', url=NESDFILE, icon=ICONGAMES, themeit=THEME1)
		addDir ('NES Titles F Thru G', 'rom', url=NESFFILE, icon=ICONGAMES, themeit=THEME1)
		addDir ('NES Titles H Thru K', 'rom', url=NESHFILE, icon=ICONGAMES, themeit=THEME1)
		addDir ('NES Titles L Thru M', 'rom', url=NESLFILE, icon=ICONGAMES, themeit=THEME1)
		addDir ('NES Titles N Thru Q', 'rom', url=NESNFILE, icon=ICONGAMES, themeit=THEME1)
		addDir ('NES Titles R Thru S', 'rom', url=NESRFILE, icon=ICONGAMES, themeit=THEME1)
		addDir ('NES Titles T Thru V', 'rom', url=NESTFILE, icon=ICONGAMES, themeit=THEME1)
		addDir ('NES Titles W Thru Z', 'rom', url=NESWFILE, icon=ICONGAMES, themeit=THEME1)


#################################################
#############  GENESIS  #########################
#################################################
def genMenu():
		addDir ('Genesis Titles A Thru B', 'rom', url=GENAFILE, icon=ICONGAMES, themeit=THEME1)
		addDir ('Genesis Titles C Thru D', 'rom', url=GENCFILE, icon=ICONAPK, themeit=THEME1)
		addDir ('Genesis Titles E Thru G', 'rom', url=GENEFILE, icon=ICONGAMES, themeit=THEME1)
		addDir ('Genesis Titles H Thru L', 'rom', url=GENHFILE, icon=ICONGAMES, themeit=THEME1)
		addDir ('Genesis Titles M Thru O', 'rom', url=GENMFILE, icon=ICONGAMES, themeit=THEME1)
		addDir ('Genesis Titles P Thru R', 'rom', url=GENPFILE, icon=ICONGAMES, themeit=THEME1)
		addDir ('Genesis Titles S Thru T', 'rom', url=GENSFILE, icon=ICONGAMES, themeit=THEME1)
		addDir ('Genesis Titles U Thru Z', 'rom', url=GENUFILE, icon=ICONGAMES, themeit=THEME1)


########################################################
############  ATARI   ##################################
########################################################
def atrMenu():
		addDir ('Atari Titles A Thru B', 'rom', url=ATRAFILE, icon=ICONGAMES, themeit=THEME1)
		addDir ('Atari Titles C Thru D', 'rom', url=ATRCFILE, icon=ICONAPK, themeit=THEME1)
		addDir ('Atari Titles E Thru G', 'rom', url=ATREFILE, icon=ICONGAMES, themeit=THEME1)
		addDir ('Atari Titles H Thru L', 'rom', url=ATRHFILE, icon=ICONGAMES, themeit=THEME1)
		addDir ('Atari Titles M Thru O', 'rom', url=ATRMFILE, icon=ICONGAMES, themeit=THEME1)
		addDir ('Atari Titles P Thru R', 'rom', url=ATRPFILE, icon=ICONGAMES, themeit=THEME1)
		addDir ('Atari Titles S Thru U', 'rom', url=ATRSFILE, icon=ICONGAMES, themeit=THEME1)
		addDir ('Atari Titles V Thru Z', 'rom', url=ATRVFILE, icon=ICONGAMES, themeit=THEME1)


############################################################
################# N64 ######################################
############################################################
def n64Menu():
		addDir ('N64 Titles A Thru B', 'rom', url=N64AFILE, icon=ICONGAMES, themeit=THEME1)
		addDir ('N64 Titles C Thru E', 'rom', url=N64CFILE, icon=ICONAPK, themeit=THEME1)
		addDir ('N64 Titles F Thru J', 'rom', url=N64FFILE, icon=ICONGAMES, themeit=THEME1)
		addDir ('N64 Titles K Thru M', 'rom', url=N64KFILE, icon=ICONGAMES, themeit=THEME1)
		addDir ('N64 Titles N Thru R', 'rom', url=N64NFILE,  icon=ICONGAMES, themeit=THEME1)
		addDir ('N64 Titles S Thru T', 'rom', url=N64SFILE, icon=ICONGAMES, themeit=THEME1)
		addDir ('N64 Titles V Thru Z', 'rom', url=N64VFILE, icon=ICONGAMES, themeit=THEME1)


##############################################################################
############# TURBO AND PC ENGINE  ###########################################
##############################################################################
def tbgMenu():
		addDir ('PC Engine And Turbo Grafx Titles A Thru B', 'rom', url=TGAFILE, icon=ICONGAMES, themeit=THEME1)
		addDir ('PC Engine And Turbo Grafx Titles C Thru E', 'rom', url=TGCFILE, icon=ICONAPK, themeit=THEME1)
		addDir ('PC Engine And Turbo Grafx Titles F Thru I', 'rom', url=TGFFILE, icon=ICONGAMES, themeit=THEME1)
		addDir ('PC Engine And Turbo Grafx Titles J Thru M', 'rom', url=TGJFILE, icon=ICONGAMES, themeit=THEME1)
		addDir ('PC Engine And Turbo Grafx Titles N Thru Q', 'rom', url=TGNFILE, icon=ICONGAMES, themeit=THEME1)
		addDir ('PC Engine And Turbo Grafx Titles R Thru U', 'rom', url=TGRFILE, icon=ICONGAMES, themeit=THEME1)
		addDir ('PC Engine And Turbo Grafx Titles V Thru Z', 'rom', url=TGVFILE, icon=ICONGAMES, themeit=THEME1)


############################################
##########  NDS  ###########################
############################################
def ndsMenu():
		addDir ('Nintendo DS Titles A', 'rom', url=NDSAFILE, icon=ICONGAMES, themeit=THEME1)
		addDir ('Nintendo DS Titles B', 'rom', url=NDSBFILE, icon=ICONGAMES, themeit=THEME1)
		addDir ('Nintendo DS Titles C', 'rom', url=NDSCFILE, icon=ICONGAMES, themeit=THEME1)
		addDir ('Nintendo DS Titles D', 'rom', url=NDSDFILE, icon=ICONGAMES, themeit=THEME1)
		addDir ('Nintendo DS Titles E Thru F', 'rom', url=NDSEFILE, icon=ICONGAMES, themeit=THEME1)		
		addDir ('Nintendo DS Titles G Thru H', 'rom', url=NDSGFILE, icon=ICONGAMES, themeit=THEME1)
		addDir ('Nintendo DS Titles I Thru J', 'rom', url=NDSIFILE, icon=ICONGAMES, themeit=THEME1)
		addDir ('Nintendo DS Titles K Thru L', 'rom', url=NDSKFILE, icon=ICONGAMES, themeit=THEME1)
		addDir ('Nintendo DS Titles M', 'rom', url=NDSMFILE, icon=ICONGAMES, themeit=THEME1)
		addDir ('Nintendo DS Titles N Thru O', 'rom', url=NDSNFILE, icon=ICONGAMES, themeit=THEME1)		
		addDir ('Nintendo DS Titles P Thru Q', 'rom', url=NDSPFILE, icon=ICONGAMES, themeit=THEME1)
		addDir ('Nintendo DS Titles R', 'rom', url=NDSRFILE, icon=ICONGAMES, themeit=THEME1)
		addDir ('Nintendo DS Titles S', 'rom', url=NDSSFILE, icon=ICONGAMES, themeit=THEME1)
		addDir ('Nintendo DS Titles T Thru U', 'rom', url=NDSTFILE, icon=ICONGAMES, themeit=THEME1)		
		addDir ('Nintendo DS Titles V Thru Z', 'rom', url=NDSVFILE, icon=ICONGAMES, themeit=THEME1)

####################################
######## PLAYSTATION ###############
####################################
def psMenu():
		addDir ('Playstation Titles A', 'rom', url=PSAFILE, icon=ICONGAMES, themeit=THEME1)
		addDir ('Playstation Titles B', 'rom', url=PSBFILE, icon=ICONGAMES, themeit=THEME1)
		addDir ('Playstation Titles C Thru D', 'rom', url=PSCFILE, icon=ICONGAMES, themeit=THEME1)
		addDir ('Playstation Titles E Thru F', 'rom', url=PSEFILE, icon=ICONGAMES, themeit=THEME1)
		addDir ('Playstation Titles G Thru J', 'rom', url=PSGFILE, icon=ICONGAMES, themeit=THEME1)
		addDir ('Playstation Titles K Thru N', 'rom', url=PSKFILE, icon=ICONGAMES, themeit=THEME1)
		addDir ('Playstation Titles O Thru R', 'rom', url=PSOFILE, icon=ICONGAMES, themeit=THEME1)
		addDir ('Playstation Titles S Thru T', 'rom', url=PSSFILE, icon=ICONGAMES, themeit=THEME1)
		addDir ('Playstation Titles U Thru Z', 'rom', url=PSUFILE, icon=ICONGAMES, themeit=THEME1)
####################################
####### Addon Menu #################
####################################
def addonMenu():
	if not ADDONFILE == 'http://':
		ADDONWORKING = wiz.workingURL(ADDONFILE)
		if ADDONWORKING == True:
			link = wiz.openURL(ADDONFILE).replace('\n','').replace('\r','').replace('\t','').replace('repository=""', 'repository="none"').replace('repositoryurl=""', 'repositoryurl="http://"').replace('repositoryxml=""', 'repositoryxml="http://"')
			match = re.compile('name="(.+?)".+?lugin="(.+?)".+?rl="(.+?)".+?epository="(.+?)".+?epositoryxml="(.+?)".+?epositoryurl="(.+?)".+?con="(.+?)".+?anart="(.+?)".+?dult="(.+?)".+?escription="(.+?)"').findall(link)
			if len(match) > 0:
				for name, plugin, url, repository, repositoryxml, repositoryurl, icon, fanart, adult, description in match:
					if not SHOWADULT == 'true' and adult.lower() == 'yes': continue
					try:
						add    = xbmcaddon.Addon(id=plugin)
						name   = "[COLOR green][Installed][/COLOR] %s" % name
					except:
						pass
					addFile1(name, 'addoninstall', plugin, description=description, icon=icon, fanart=fanart, themeit=THEME2)
			else: wiz.log("[Addon Menu] ERROR: Invalid Format.")
		else: 
			wiz.log("[Addon Menu] ERROR: URL for Addon list not working.")
			addFile1('Url for txt file not valid', '', themeit=THEME3)
			addFile1('%s' % ADDONWORKING, '', themeit=THEME3)
	else: wiz.log("[Addon Menu] No Addon list added.")
	setView('files', 'viewType')

def addonInstaller(plugin):
	if not ADDONFILE == 'http://':
		ADDONWORKING = wiz.workingURL(ADDONFILE)
		if ADDONWORKING == True:
			link = wiz.openURL(ADDONFILE).replace('\n','').replace('\r','').replace('\t','').replace('repository=""', 'repository="none"').replace('repositoryurl=""', 'repositoryurl="http://"').replace('repositoryxml=""', 'repositoryxml="http://"')
			match = re.compile('name="(.+?)".+?lugin="%s".+?rl="(.+?)".+?epository="(.+?)".+?epositoryxml="(.+?)".+?epositoryurl="(.+?)".+?con="(.+?)".+?anart="(.+?)".+?dult="(.+?)".+?escription="(.+?)"' % plugin).findall(link)
			if len(match) > 0:
				for name, url, repository, repositoryxml, repositoryurl, icon, fanart, adult, description in match:
					if os.path.exists(os.path.join(ADDONS, plugin)):
						if DIALOG.yesno(ADDONTITLE, "[COLOR %s]Would you like to remove and reinstall:" % COLOR2, "[COLOR %s]%s[/COLOR]?[/COLOR]" % (COLOR1, plugin), yeslabel="[B]Yes Remove[/B]", nolabel="[B]No Skip[/B]"):
							wiz.cleanHouse(os.path.join(ADDONS, plugin))
							if DIALOG.yesno(ADDONTITLE, "[COLOR %s]Would you like to remove the addon_data for:" % COLOR2, "[COLOR %s]%s[/COLOR]?[/COLOR]" % (COLOR1, plugin), yeslabel="[B]Yes Remove[/B]", nolabel="[B]No Skip[/B]"):
								removeAddonData(plugin)
						else: wiz.log("[Addon Installer] %s wasnt re-installed" % plugin); return False
					repo = os.path.join(ADDONS, repository)
					if not repository.lower() == 'none' and not os.path.exists(repo):
						wiz.log("Repository not installed, installing it")
						if DIALOG.yesno(ADDONTITLE, "[COLOR %s]Would you like to install the repository for [COLOR %s]%s[/COLOR]:" % (COLOR2, COLOR1, plugin), "[COLOR %s]%s[/COLOR]?[/COLOR]" % (COLOR1, repository), yeslabel="[B]Yes Install[/B]", nolabel="[B]No Skip[/B]"): 
							link1  = wiz.openURL(repositoryxml).replace('\r','').replace('\t','')
							match1 = re.compile('<addon.+?d="%s".+?ersion="(.+?)".+?>' % repository).findall(link1)
							match2 = re.compile('<addon.+?ersion="(.+?)".+?d="%s".+?>' % repository).findall(link1)
							wiz.log("Match 1: %s / Match 2: %s" % (len(match1), len(match2)))
							if len(match1) > 0: version = match1[0]
							elif len(match2) > 0: version = match2[0]
							else: wiz.log("No Match")
							repozip = '%s%s-%s.zip' % (repositoryurl, repository, version)
							wiz.log(repozip)
							installAddon(repository, repozip)
							wiz.ebi('UpdateAddonRepos()')
							wiz.log("Installing Addon from Kodi")
							xbmc.sleep(1000)
							install = installFromKodi(plugin)
							if install:
								wiz.refresh()
								return True
						else: wiz.log("[Addon Installer] Repository for %s not installed: %s" % (plugin, repository))
					elif repository.lower() == 'none':
						wiz.log("No repository, installing addon")
						pluginid = plugin
						zipurl = url
						installAddon(plugin, url)
						wiz.refresh()
						return True
					else:
						wiz.log("Repository installed, installing addon")
						install = installFromKodi(plugin)
						if install:
							wiz.refresh()
							return True
					link2  = wiz.openURL(repositoryxml).replace('\r','').replace('\t','')
					match3 = re.compile('<addon.+?id="%s".+?ersion="(.+?)".+?>' % plugin).findall(link2)
					match4 = re.compile('<addon.+?ersion="(.+?)".+?id="%s".+?>' % plugin).findall(link2)
					if len(match3) > 0: version = match3[0]
					elif len(match4) > 0: version = match4[0]
					else: wiz.log("no match")
					url = "%s%s-%s.zip" % (url, plugin, version)
					wiz.log(str(url))
					installAddon(plugin, url)
					wiz.refresh()
			else: wiz.log("[Addon Installer] Invalid Format")
		else: wiz.log("[Addon Installer] Text File: %s" % ADDONWORKING)
	else: wiz.log("[Addon Installer] Not Enabled.")

def installFromKodi(plugin):
	wiz.log("Running Plugin")
	wiz.ebi('RunPlugin(plugin://%s)' % plugin)
	xbmc.sleep(500)
	if not wiz.whileWindow('yesnodialog'):
		return False
	xbmc.sleep(500)
	if wiz.whileWindow('okdialog'):
		return False
	prog = wiz.whileWindow('progressdialog')
	xbmc.sleep(1000)
	wiz.log("Download complete")
	if os.path.exists(os.path.join(ADDONS, plugin)): return True
	else: return False

def installAddon(name, url):
	if not wiz.workingURL(url) == True: wiz.LogNotify("Addon Installer", '%s: [COLOR red]Invalid Zip Url![/COLOR]' % name); return
	if not os.path.exists(PACKAGES): os.makedirs(PACKAGES)
	DP.create(ADDONTITLE,'[COLOR %s][B]Downloading:[/B][/COLOR] [COLOR %s]%s[/COLOR]' % (COLOR2, COLOR1, name),'', 'Please Wait')
	urlsplit = url.split('/')
	lib=os.path.join(PACKAGES, urlsplit[-1])
	try: os.remove(lib)
	except: pass
	downloader.download(url, lib, DP)
	xbmc.sleep(500)
	title = '[COLOR %s][B]Installing:[/B][/COLOR] [COLOR %s]%s[/COLOR]' % (COLOR2, COLOR1, name)
	DP.update(0, title,'', 'Please Wait')
	percent, errors, error = extract.all(lib,ADDONS,DP, title=title)
	DP.close()
	installed(name)
	installDep(name)
	xbmc.sleep(500)
	wiz.ebi('UpdateAddonRepos()')
	wiz.ebi('UpdateLocalAddons()')
	xbmc.sleep(500)
	wiz.refresh()

def installDep(name):
	dep=os.path.join(ADDONS,name,'addon.xml')
	if os.path.exists(dep):
		source=open(dep,mode='r'); link=source.read(); source.close(); 
		match=re.compile('import addon="(.+?)"').findall(link)
		for depends in match:
			if not 'xbmc.python' in depends:
				dependspath=os.path.join(ADDONS, depends)
				if not os.path.exists(dependspath):
					depzip = '%s%s.zip' % (MODURL, depends)
					lib=os.path.join(PACKAGES, '%s.zip' % depends)
					try: os.remove(lib)
					except: pass
					DP.update(0, '[COLOR %s][B]Downloading Dependency:[/B][/COLOR] [COLOR %s]%s[/COLOR]' % (COLOR2, COLOR1, depends),'', 'Please Wait')
					downloader.download(depzip, lib, DP)
					xbmc.sleep(100)
					title = '[COLOR %s][B]Installing Dependency:[/B][/COLOR] [COLOR %s]%s[/COLOR]' % (COLOR2, COLOR1, depends)
					DP.update(0, title,'', 'Please Wait')
					percent, errors, error = extract.all(lib,ADDONS,DP, title=title)
					installed(depends)
					installDep(depends)
					xbmc.sleep(100)
					DP.close()

def installed(addon):
	url = os.path.join(ADDONS,addon,'addon.xml')
	if os.path.exists(url):
		list  = open(url,mode='r'); g = list.read().replace('\n','').replace('\r',''); list.close()
		match = re.compile('<addon.+?name="(.+?)".+?>').findall(g)
		icon  = os.path.join(ADDONS,addon,'icon.png')
		wiz.LogNotify(match[0],'Addon Enabled', '2000', icon)

def youtubeMenu(url):
	if not workingURL(url) == True: return False
	link = wiz.openURL(url).replace('\n','').replace('\r','').replace('\t','')
	match = re.compile('name="(.+?)".+?rl="(.+?)".+?con="(.+?)".+?anart="(.+?)".+?escription="(.+?)"').findall(link)
	if len(match) > 0:
		for name, url, icon, fanart, description in match:
			addFile1(name, 'viewVideo', url=url, description=description, icon=icon, fanart=fanart, themeit=THEME2)
		else: wiz.log("[YouTube Menu] ERROR: Invalid Format.")
	else: 
		wiz.log("[YouTube Menu] ERROR: URL for YouTube list not working.")
		addFile1('Url for txt file not valid', '', themeit=THEME3)
	setView('files', 'viewType')
####################################
##########Maintenance Menu##########
####################################
def maintMenu(view=None):
	on = '[B][COLOR green]ON[/COLOR][/B]'; off = '[B][COLOR red]OFF[/COLOR][/B]'
	autoclean   = 'true' if AUTOCLEANUP    == 'true' else 'false'
	cache       = 'true' if AUTOCACHE      == 'true' else 'false'
	packages    = 'true' if AUTOPACKAGES   == 'true' else 'false'
	thumbs      = 'true' if AUTOTHUMBS     == 'true' else 'false'
	delay       = 'true' if AUTODELAY      == 'true' else 'false'
	maint       = 'true' if SHOWMAINT      == 'true' else 'false'
	includevid  = 'true' if INCLUDEVIDEO   == 'true' else 'false'
	includeall  = 'true' if INCLUDEALL     == 'true' else 'false'
	if wiz.Grab_Log(True) == False: kodilog = 0
	else: kodilog = errorChecking(wiz.Grab_Log(True), True)
	if wiz.Grab_Log(True, True) == False: kodioldlog = 0
	else: kodioldlog = errorChecking(wiz.Grab_Log(True,True), True)
	errorsinlog = int(kodilog) + int(kodioldlog)
	wizlogsize = ': [COLOR red]Not Found[/COLOR]' if not os.path.exists(WIZLOG) else ": [COLOR green]%s[/COLOR]" % wiz.convertSize(os.path.getsize(WIZLOG))
	if includeall == 'true':
		includebob = 'true'
		includepho = 'true'
		includespe = 'true'
		includegen = 'true'
		includeexo = 'true'
		includeone = 'true'
		includesal = 'true'
		includeshd = 'true'
	else:
		includebob = 'true' if INCLUDEBOB     == 'true' else 'false'
		includepho = 'true' if INCLUDEPHOENIX == 'true' else 'false'
		includespe = 'true' if INCLUDESPECTO  == 'true' else 'false'
		includegen = 'true' if INCLUDEGENESIS == 'true' else 'false'
		includeexo = 'true' if INCLUDEEXODUS  == 'true' else 'false'
		includeone = 'true' if INCLUDEONECHAN == 'true' else 'false'
		includesal = 'true' if INCLUDESALTS   == 'true' else 'false'
		includeshd = 'true' if INCLUDESALTSHD == 'true' else 'false'
	sizepack   = wiz.getSize(PACKAGES)
	sizethumb  = wiz.getSize(THUMBS)
	sizecache  = wiz.getCacheSize()
	totalsize  = sizepack+sizethumb+sizecache
	feq        = ['Always', 'Daily', '3 Days', 'Weekly']
	addFile1('Show All Maintenance: %s' % maint.replace('true',on).replace('false',off) ,'togglesetting', 'showmaint', icon=ICONMAINT, themeit=THEME2)
	addFile1('Auto Clean', '', fanart=FANART, icon=ICONMAINT, themeit=THEME1)
	addFile1('Auto Clean Up On Startup: %s' % autoclean.replace('true',on).replace('false',off) ,'togglesetting', 'autoclean',   icon=ICONMAINT, themeit=THEME3)
	addDir ('[B]Cleaning Tools[/B]'       ,'maint', 'clean',  icon=ICONMAINT, themeit=THEME1)
	if autoclean == 'true':
		addFile1('--- Auto Clean Fequency: [B][COLOR green]%s[/COLOR][/B]' % feq[AUTOFEQ], 'changefeq', icon=ICONMAINT, themeit=THEME3)
		addFile1('--- Clear Cache on Startup: %s' % cache.replace('true',on).replace('false',off), 'togglesetting', 'clearcache', icon=ICONMAINT, themeit=THEME3)
		addFile1('--- Clear Packages on Startup: %s' % packages.replace('true',on).replace('false',off), 'togglesetting', 'clearpackages', icon=ICONMAINT, themeit=THEME3)
		addFile1('--- Clear Old Thumbs on Startup: %s' % thumbs.replace('true',on).replace('false',off), 'togglesetting', 'clearthumbs', icon=ICONMAINT, themeit=THEME3)
		addFile1('--- Delay Clear Packages: %s' % delay.replace('true',on).replace('false',off), 'togglesetting', 'delayautoclean', icon=ICONMAINT, themeit=THEME3)
	addFile1('Clear Video Cache', '', fanart=FANART, icon=ICONMAINT, themeit=THEME1)
	addFile1('Include Video Cache in Clear Cache: %s' % includevid.replace('true',on).replace('false',off), 'togglecache', 'includevideo', icon=ICONMAINT, themeit=THEME3)
	if view == "clean" or SHOWMAINT == 'true': 
		addFile1('Total Clean Up: [COLOR green][B]%s[/B][/COLOR]' % wiz.convertSize(totalsize)  ,'fullclean',       icon=ICONMAINT, themeit=THEME3)
		addFile1('Clear Cache: [COLOR green][B]%s[/B][/COLOR]' % wiz.convertSize(sizecache)     ,'clearcache',      icon=ICONMAINT, themeit=THEME3)
		addFile1('Clear Packages: [COLOR green][B]%s[/B][/COLOR]' % wiz.convertSize(sizepack)   ,'clearpackages',   icon=ICONMAINT, themeit=THEME3)
		addFile1('Clear Thumbnails: [COLOR green][B]%s[/B][/COLOR]' % wiz.convertSize(sizethumb),'clearthumb',      icon=ICONMAINT, themeit=THEME3)
		addFile1('Clear Crash Logs',     'clearcrash',      icon=ICONMAINT, themeit=THEME3)
		addFile1('Purge Databases',      'purgedb',         icon=ICONMAINT, themeit=THEME3)
		addFile1('Fresh Start',          'freshstart',      icon=ICONMAINT, themeit=THEME3)
	addDir1 ('[B]Addon Tools[/B]',       'maint', 'addon',  icon=ICONMAINT, themeit=THEME1)
	if view == "addon" or SHOWMAINT == 'true': 
		addDir1 ('Remove Addons',        'removeaddons',    icon=ICONMAINT, themeit=THEME3)
		addDir1 ('Remove Addon Data',    'removeaddondata', icon=ICONMAINT, themeit=THEME3)
		addDir1 ('Enable/Disable Addons','enableaddons',    icon=ICONMAINT, themeit=THEME3)
		addFile1('Enable/Disable Adult Addons', 'toggleadult', icon=ICONMAINT, themeit=THEME3)
		addFile1('Force Update Addons',  'forceupdate',     icon=ICONMAINT, themeit=THEME3)
		addFile1('Hide Passwords On Keyboard Entry',   'hidepassword',   icon=ICONMAINT, themeit=THEME3)
		addFile1('Unhide Passwords On Keyboard Entry', 'unhidepassword', icon=ICONMAINT, themeit=THEME3)
	addDir1 ('[B]Misc Maintenance[/B]'     ,'maint', 'misc',   icon=ICONMAINT, themeit=THEME1)
	if view == "misc" or SHOWMAINT == 'true': 
		addFile1('Reload Skin',          'forceskin',       icon=ICONMAINT, themeit=THEME3)
		addFile1('Force Close Kodi',     'forceclose',      icon=ICONMAINT, themeit=THEME3)
		addFile1('Upload Kodi.log',      'uploadlog',       icon=ICONMAINT, themeit=THEME3)
		addFile1('View Errors in Log: %s Error(s)' % (errorsinlog), 'viewerrorlog',    icon=ICONMAINT, themeit=THEME3)
		addFile1('View Log File',        'viewlog',         icon=ICONMAINT, themeit=THEME3)
		addFile1('View Wizard Log File', 'viewwizlog',      icon=ICONMAINT, themeit=THEME3)
		addFile1('Clear Wizard Log File %s' % wizlogsize,'clearwizlog',     icon=ICONMAINT, themeit=THEME3)
	addDir1 ('[B]Back up/Restore[/B]'     ,'maint', 'backup',   icon=ICONMAINT, themeit=THEME1)
	if view == "backup" or SHOWMAINT == 'true':
		addFile1('Clean Up Back Up Folder',        'clearbackup',     icon=ICONMAINT,   themeit=THEME3)
		addFile1('Back Up Location: [COLOR %s]%s[/COLOR]' % (COLOR2, MYBUILDS),'settings', 'Maintenance', icon=ICONMAINT, themeit=THEME3)
		addFile1('[Back Up]: Build',               'backupbuild',     icon=ICONMAINT,   themeit=THEME3)
		addFile1('[Back Up]: GuiFix',              'backupgui',       icon=ICONMAINT,   themeit=THEME3)
		addFile1('[Back Up]: Theme',               'backuptheme',     icon=ICONMAINT,   themeit=THEME3)
		addFile1('[Back Up]: Addon_data',          'backupaddon',     icon=ICONMAINT,   themeit=THEME3)
		addFile1('[Restore]: Local Build',         'restorezip',      icon=ICONMAINT,   themeit=THEME3)
		addFile1('[Restore]: Local GuiFix',        'restoregui',      icon=ICONMAINT,   themeit=THEME3)
		addFile1('[Restore]: Local Addon_data',    'restoreaddon',    icon=ICONMAINT,   themeit=THEME3)
		addFile1('[Restore]: External Build',      'restoreextzip',   icon=ICONMAINT,   themeit=THEME3)
		addFile1('[Restore]: External GuiFix',     'restoreextgui',   icon=ICONMAINT,   themeit=THEME3)
		addFile1('[Restore]: External Addon_data', 'restoreextaddon', icon=ICONMAINT,   themeit=THEME3)
	addDir1 ('[B]System Tweaks/Fixes[/B]',       'maint', 'tweaks', icon=ICONMAINT, themeit=THEME1)
	if view == "tweaks" or SHOWMAINT == 'true': 
		if not ADVANCEDFILE == 'http://': addDir ('Advanced Settings',            'advancedsetting',  icon=ICONMAINT, themeit=THEME3)
		else: addFile('Advanced Settings',      'autoadvanced',      icon=ICONMAINT, themeit=THEME3)
		addFile1('Scan Sources for broken links','checksources',      icon=ICONMAINT, themeit=THEME3)
		addFile1('Scan For Broken Repositories', 'checkrepos',        icon=ICONMAINT, themeit=THEME3)
		addFile1('Fix Addons Not Updating',      'fixaddonupdate',    icon=ICONMAINT, themeit=THEME3)
		addFile1('Remove special character filenames',  'asciicheck', icon=ICONMAINT, themeit=THEME3)
		addFile1('Convert Paths to special',            'convertpath',icon=ICONMAINT, themeit=THEME3)
		addDir1 ('System Information',           'systeminfo',        icon=ICONMAINT, themeit=THEME3)
	if includevid == 'true':
		addFile1('--- Include All Video Addons: %s' % includeall.replace('true',on).replace('false',off), 'togglecache', 'includeall', icon=ICONMAINT, themeit=THEME3)
		addFile1('--- Include Bob: %s' % includebob.replace('true',on).replace('false',off), 'togglecache', 'includebob', icon=ICONMAINT, themeit=THEME3)
		addFile1('--- Include Phoenix: %s' % includepho.replace('true',on).replace('false',off), 'togglecache', 'includephoenix', icon=ICONMAINT, themeit=THEME3)
		addFile1('--- Include Specto: %s' % includespe.replace('true',on).replace('false',off), 'togglecache', 'includespecto', icon=ICONMAINT, themeit=THEME3)
		addFile1('--- Include Exodus: %s' % includeexo.replace('true',on).replace('false',off), 'togglecache', 'includeexodus', icon=ICONMAINT, themeit=THEME3)
		addFile1('--- Include Salts: %s' % includesal.replace('true',on).replace('false',off), 'togglecache', 'includesalts', icon=ICONMAINT, themeit=THEME3)
		addFile1('--- Include Salts HD Lite: %s' % includeshd.replace('true',on).replace('false',off), 'togglecache', 'includesaltslite', icon=ICONMAINT, themeit=THEME3)
		addFile1('--- Include One Channel: %s' % includeone.replace('true',on).replace('false',off), 'togglecache', 'includeonechan', icon=ICONMAINT, themeit=THEME3)
		addFile1('--- Include Genesis: %s' % includegen.replace('true',on).replace('false',off), 'togglecache', 'includegenesis', icon=ICONMAINT, themeit=THEME3)
		addFile1('--- Enable All Video Addons', 'togglecache', 'true', icon=ICONMAINT, themeit=THEME3)
		addFile1('--- Disable All Video Addons', 'togglecache', 'false', icon=ICONMAINT, themeit=THEME3)
	addDir1 ('[I]<< Return to Main Menu[/I]', icon=ICONMAINT, themeit=THEME2)
	setView('files', 'viewType')

def advancedWindow():
	if not ADVANCEDFILE == 'http://':
		addFile1('Configure Wizard', 'autoadvanced', icon=ICONMAINT, themeit=THEME3)
		if os.path.exists(ADVANCED): addFile('View Currect AdvancedSettings.xml', 'currentsettings', icon=ICONMAINT, themeit=THEME3)
		ADVANCEDWORKING = wiz.workingURL(ADVANCEDFILE)
		if ADVANCEDWORKING == True:
			if HIDESPACERS == 'No': addFile(wiz.sep(), '', icon=ICONMAINT, themeit=THEME3)
			link = wiz.openURL(ADVANCEDFILE).replace('\n','').replace('\r','').replace('\t','')
			match = re.compile('name="(.+?)".+?rl="(.+?)".+?con="(.+?)".+?anart="(.+?)".+?escription="(.+?)"').findall(link)
			if len(match) > 0:
				for name, url, icon, fanart, description in match:
					addFile1(name, 'writeadvanced', name, description=description, icon=icon, fanart=fanart, themeit=THEME2)
			else: wiz.log("[Advanced Settings] ERROR: Invalid Format.")
		else: wiz.log("[Advanced Settings] URL not working: %s" % ADVANCEDWORKING)
	else: wiz.log("[Advanced Settings] not Enabled")

def writeAdvanced(name):
	if not ADVANCEDFILE == 'http://':
		ADVANCEDWORKING = wiz.workingURL(ADVANCEDFILE)
		if ADVANCEDWORKING == True:
			link = wiz.openURL(ADVANCEDFILE).replace('\n','').replace('\r','').replace('\t','')
			match = re.compile('name="%s".+?rl="(.+?)"' % name).findall(link)
			if len(match) > 0: advancedurl = match[0]
			else: wiz.log("[Advanced Settings] ERROR: Invalid Format."); wiz.LogNotify(ADDONTITLE, "Invalid File Format"); return
			
			if os.path.exists(ADVANCED): choice = DIALOG.yesno(ADDONTITLE, "[COLOR %s]Would you like to overwrite your current Advanced Settings with [COLOR %s]%s[/COLOR]?[/COLOR]" % (COLOR1, COLOR2, name), yeslabel="[B]Overwrite[/B]", nolabel="[B]Cancel[/B]")
			else: choice = DIALOG.yesno(ADDONTITLE, "[COLOR %s]Would you like to download and install [COLOR %s]%s[/COLOR]?[/COLOR]" % (COLOR1, COLOR2, name), yeslabel="[B]Install[/B]", nolabel="[B]Cancel[/B]")
			
			if choice == 1:
				file = wiz.openURL(advancedurl)
				f = open(ADVANCED, 'w'); 
				f.write(file)
				f.close()
				DIALOG.ok(ADDONTITLE, '[COLOR %s]AdvancedSettings.xml file has been successfully written.  Once you click okay it will force close kodi.[/COLOR]' % COLOR2)
				wiz.killxbmc(True)
			else: wiz.log("[Advanced Settings] install canceled"); wiz.LogNotify(ADDONTITLE, "Write Cancelled!"); return
		else: wiz.log("[Advanced Settings] URL not working: %s" % ADVANCEDWORKING); wiz.LogNotify(ADDONTITLE, "URL Not Working")
	else: wiz.log("[Advanced Settings] not Enabled"); wiz.LogNotify(ADDONTITLE, "Not Enabled")

def viewAdvanced():
	f = open(ADVANCED)
	a = f.read().replace('\t', '    ')
	wiz.TextBoxes(ADDONTITLE, a)
	f.close()

def showAutoAdvanced():
	notify.autoConfig()

def getIP():
	site  = 'http://whatismyipaddress.com/'
	if not wiz.workingURL(site): return 'Unknown', 'Unknown', 'Unknown'
	page  = wiz.openURL(site).replace('\n','').replace('\r','')
	if not 'Access Denied' in page:
		ipmatch   = re.compile('whatismyipaddress.com/ip/(.+?)"').findall(page)
		ipfinal   = ipmatch[0] if (len(ipmatch) > 0) else 'Unknown'
		details   = re.compile('"font-size:14px;">(.+?)</td>').findall(page)
		provider  = details[0] if (len(details) > 0) else 'Unknown'
		location  = details[1]+', '+details[2]+', '+details[3] if (len(details) > 2) else 'Unknown'
		return ipfinal, provider, location
	else: return 'Unknown', 'Unknown', 'Unknown'

def systemInfo():
	infoLabel = ['System.FriendlyName', 
				 'System.BuildVersion', 
				 'System.CpuUsage',
				 'System.ScreenMode',
				 'Network.IPAddress',
				 'Network.MacAddress',
				 'System.Uptime',
				 'System.TotalUptime',
				 'System.FreeSpace',
				 'System.UsedSpace',
				 'System.TotalSpace',
				 'System.Memory(free)',
				 'System.Memory(used)',
				 'System.Memory(total)']
	data      = []; x = 0
	for info in infoLabel:
		temp = wiz.getInfo(info)
		y = 0
		while temp == "Busy" and y < 10:
			temp = wiz.getInfo(info); y += 1; wiz.log("%s sleep %s" % (info, str(y))); xbmc.sleep(200)
		data.append(temp)
		x += 1
	storage_free  = data[8] if 'Una' in data[8] else wiz.convertSize(int(float(data[8][:-8]))*1024*1024)
	storage_used  = data[9] if 'Una' in data[9] else wiz.convertSize(int(float(data[9][:-8]))*1024*1024)
	storage_total = data[10] if 'Una' in data[10] else wiz.convertSize(int(float(data[10][:-8]))*1024*1024)
	ram_free      = wiz.convertSize(int(float(data[11][:-2]))*1024*1024)
	ram_used      = wiz.convertSize(int(float(data[12][:-2]))*1024*1024)
	ram_total     = wiz.convertSize(int(float(data[13][:-2]))*1024*1024)
	exter_ip, provider, location = getIP()

	addFile1('[B]Media Center Info:[/B]', '', icon=ICONMAINT, themeit=THEME2)
	addFile1('[COLOR %s]Name:[/COLOR] [COLOR %s]%s[/COLOR]' % (COLOR1, COLOR2, data[0]), '', icon=ICONMAINT, themeit=THEME3)
	addFile1('[COLOR %s]Version:[/COLOR] [COLOR %s]%s[/COLOR]' % (COLOR1, COLOR2, data[1]), '', icon=ICONMAINT, themeit=THEME3)
	addFile1('[COLOR %s]Platform:[/COLOR] [COLOR %s]%s[/COLOR]' % (COLOR1, COLOR2, wiz.platform().title()), '', icon=ICONMAINT, themeit=THEME3)
	addFile1('[COLOR %s]CPU Usage:[/COLOR] [COLOR %s]%s[/COLOR]' % (COLOR1, COLOR2, data[2]), '', icon=ICONMAINT, themeit=THEME3)
	addFile1('[COLOR %s]Screen Mode:[/COLOR] [COLOR %s]%s[/COLOR]' % (COLOR1, COLOR2, data[3]), '', icon=ICONMAINT, themeit=THEME3)
	
	addFile1('[B]Uptime:[/B]', '', icon=ICONMAINT, themeit=THEME2)
	addFile1('[COLOR %s]Current Uptime:[/COLOR] [COLOR %s]%s[/COLOR]' % (COLOR1, COLOR2, data[6]), '', icon=ICONMAINT, themeit=THEME2)
	addFile1('[COLOR %s]Total Uptime:[/COLOR] [COLOR %s]%s[/COLOR]' % (COLOR1, COLOR2, data[7]), '', icon=ICONMAINT, themeit=THEME2)
	
	addFile1('[B]Local Storage:[/B]', '', icon=ICONMAINT, themeit=THEME2)
	addFile1('[COLOR %s]Used Storage:[/COLOR] [COLOR %s]%s[/COLOR]' % (COLOR1, COLOR2, storage_free), '', icon=ICONMAINT, themeit=THEME2)
	addFile1('[COLOR %s]Free Storage:[/COLOR] [COLOR %s]%s[/COLOR]' % (COLOR1, COLOR2, storage_used), '', icon=ICONMAINT, themeit=THEME2)
	addFile1('[COLOR %s]Total Storage:[/COLOR] [COLOR %s]%s[/COLOR]' % (COLOR1, COLOR2, storage_total), '', icon=ICONMAINT, themeit=THEME2)
	
	addFile1('[B]Ram Usage:[/B]', '', icon=ICONMAINT, themeit=THEME2)
	addFile1('[COLOR %s]Used Memory:[/COLOR] [COLOR %s]%s[/COLOR]' % (COLOR1, COLOR2, ram_free), '', icon=ICONMAINT, themeit=THEME2)
	addFile1('[COLOR %s]Free Memory:[/COLOR] [COLOR %s]%s[/COLOR]' % (COLOR1, COLOR2, ram_used), '', icon=ICONMAINT, themeit=THEME2)
	addFile1('[COLOR %s]Total Memory:[/COLOR] [COLOR %s]%s[/COLOR]' % (COLOR1, COLOR2, ram_total), '', icon=ICONMAINT, themeit=THEME2)
	
	addFile1('[B]Network:[/B]', '', icon=ICONMAINT, themeit=THEME2)
	addFile1('[COLOR %s]Local IP:[/COLOR] [COLOR %s]%s[/COLOR]' % (COLOR1, COLOR2, data[4]), '', icon=ICONMAINT, themeit=THEME2)
	addFile1('[COLOR %s]External IP:[/COLOR] [COLOR %s]%s[/COLOR]' % (COLOR1, COLOR2, exter_ip), '', icon=ICONMAINT, themeit=THEME2)
	addFile1('[COLOR %s]Provider:[/COLOR] [COLOR %s]%s[/COLOR]' % (COLOR1, COLOR2, provider), '', icon=ICONMAINT, themeit=THEME2)
	addFile1('[COLOR %s]Location:[/COLOR] [COLOR %s]%s[/COLOR]' % (COLOR1, COLOR2, location), '', icon=ICONMAINT, themeit=THEME2)
	addFile('[COLOR %s]MacAddress:[/COLOR] [COLOR %s]%s[/COLOR]' % (COLOR1, COLOR2, data[5]), '', icon=ICONMAINT, themeit=THEME2)

#######################################
##########Speed Test Menu##############
#######################################
def speedMenu():
	xbmc.executebuiltin('Runscript("special://home/addons/plugin.program.SpinzTV/ookla.py")')

#####################################
#############Save Menu###############
#####################################
def saveMenu():
	on = '[COLOR green]ON[/COLOR]'; off = '[COLOR red]OFF[/COLOR]'
	trakt      = 'true' if KEEPTRAKT     == 'true' else 'false'
	real       = 'true' if KEEPREAL      == 'true' else 'false'
	login      = 'true' if KEEPLOGIN     == 'true' else 'false'
	sources    = 'true' if KEEPSOURCES   == 'true' else 'false'
	advanced   = 'true' if KEEPADVANCED  == 'true' else 'false'
	profiles   = 'true' if KEEPPROFILES  == 'true' else 'false'
	favourites = 'true' if KEEPFAVS      == 'true' else 'false'

	addDir1 ('Keep Trakt Data'               ,'trakt',         icon=ICONTRAKT, themeit=THEME1)
	addDir1 ('Keep Real Debrid'              ,'realdebrid',    icon=ICONREAL, themeit=THEME1)
	addDir1 ('Keep Login Info'               ,'login',         icon=ICONLOGIN, themeit=THEME1)
	addFile1('- Click to toggle settings -', '', themeit=THEME3)
	addFile1('Save Trakt: %s' % trakt.replace('true',on).replace('false',off)                       ,'togglesetting', 'keeptrakt',      icon=ICONTRAKT, themeit=THEME1)
	addFile1('Save Real Debrid: %s' % real.replace('true',on).replace('false',off)                  ,'togglesetting', 'keepdebrid',     icon=ICONREAL,  themeit=THEME1)
	addFile1('Save Login Info: %s' % login.replace('true',on).replace('false',off)                  ,'togglesetting', 'keeplogin',      icon=ICONLOGIN, themeit=THEME1)
	addFile1('Keep \'Sources.xml\': %s' % sources.replace('true',on).replace('false',off)           ,'togglesetting', 'keepsources',    icon=ICONSAVE,  themeit=THEME1)
	addFile1('Keep \'Profiles.xml\': %s' % profiles.replace('true',on).replace('false',off)         ,'togglesetting', 'keepprofiles',   icon=ICONSAVE,  themeit=THEME1)
	addFile1('Keep \'Advancedsettings.xml\': %s' % advanced.replace('true',on).replace('false',off) ,'togglesetting', 'keepadvanced',   icon=ICONSAVE,  themeit=THEME1)
	addFile1('Keep \'Favourites.xml\': %s' % favourites.replace('true',on).replace('false',off)     ,'togglesetting', 'keepfavourites', icon=ICONSAVE,  themeit=THEME1)
	setView('files', 'viewType')


def traktMenu():
	trakt = '[COLOR green]ON[/COLOR]' if KEEPTRAKT == 'true' else '[COLOR red]OFF[/COLOR]'
	last = str(TRAKTSAVE) if not TRAKTSAVE == '' else 'Trakt hasnt been saved yet.'
	addFile1('[I]Register FREE Account at http://trakt.tv[/I]', '', icon=ICONTRAKT, themeit=THEME3)
	addFile1('Save Trakt Data: %s' % trakt, 'togglesetting', 'keeptrakt', icon=ICONTRAKT, themeit=THEME3)
	if KEEPTRAKT == 'true': addFile('Last Save: %s' % str(last), '', icon=ICONTRAKT, themeit=THEME3)
	if HIDESPACERS == 'No': addFile(wiz.sep(), '', icon=ICONTRAKT, themeit=THEME3)
	
	for trakt in traktit.ORDER:
		name   = TRAKTID[trakt]['name']
		path   = TRAKTID[trakt]['path']
		saved  = TRAKTID[trakt]['saved']
		file   = TRAKTID[trakt]['file']
		user   = wiz.getS(saved)
		auser  = traktit.traktUser(trakt)
		icon   = TRAKTID[trakt]['icon']   if os.path.exists(path) else ICONTRAKT
		fanart = TRAKTID[trakt]['fanart'] if os.path.exists(path) else FANART
		menu = createMenu('saveaddon', 'Trakt', trakt)
		menu2 = createMenu('save', 'Trakt', trakt)
		menu.append((THEME2 % '%s Settings' % name,              'RunPlugin(plugin://%s/?mode=opensettings&name=%s&url=trakt)' %   (ADDON_ID, trakt)))
		
		addFile1('[+]-> %s' % name,     '', icon=icon, fanart=fanart, themeit=THEME3)
		if not os.path.exists(path): addFile('[COLOR red]Addon Data: Not Installed[/COLOR]', '', icon=icon, fanart=fanart, menu=menu)
		elif not auser:              addFile('[COLOR red]Addon Data: Not Registered[/COLOR]','authtrakt', trakt, icon=icon, fanart=fanart, menu=menu)
		else:                        addFile('[COLOR green]Addon Data: %s[/COLOR]' % auser,'authtrakt', trakt, icon=icon, fanart=fanart, menu=menu)
		if user == "":
			if os.path.exists(file): addFile('[COLOR red]Saved Data: Save File Found(Import Data)[/COLOR]','importtrakt', trakt, icon=icon, fanart=fanart, menu=menu2)
			else :                   addFile('[COLOR red]Saved Data: Not Saved[/COLOR]','savetrakt', trakt, icon=icon, fanart=fanart, menu=menu2)
		else:                        addFile('[COLOR green]Saved Data: %s[/COLOR]' % user, '', icon=icon, fanart=fanart, menu=menu2)
	
	if HIDESPACERS == 'No': addFile(wiz.sep(), '', themeit=THEME3)
	addFile1('Save All Trakt Data',          'savetrakt',    'all', icon=ICONTRAKT,  themeit=THEME3)
	addFile1('Recover All Saved Trakt Data', 'restoretrakt', 'all', icon=ICONTRAKT,  themeit=THEME3)
	addFile1('Import Trakt Data',            'importtrakt',  'all', icon=ICONTRAKT,  themeit=THEME3)
	addFile1('Clear All Saved Trakt Data',   'cleartrakt',   'all', icon=ICONTRAKT,  themeit=THEME3)
	addFile1('Clear All Addon Data',         'addontrakt',   'all', icon=ICONTRAKT,  themeit=THEME3)
	setView('files', 'viewType')

def realMenu():
	real = '[COLOR green]ON[/COLOR]' if KEEPREAL == 'true' else '[COLOR red]OFF[/COLOR]'
	last = str(REALSAVE) if not REALSAVE == '' else 'Real Debrid hasnt been saved yet.'
	addFile1('[I]http://real-debrid.com is a PAID service.[/I]', '', icon=ICONREAL, themeit=THEME3)
	addFile1('Save Real Debrid Data: %s' % real, 'togglesetting', 'keepdebrid', icon=ICONREAL, themeit=THEME3)
	if KEEPREAL == 'true': addFile('Last Save: %s' % str(last), '', icon=ICONREAL, themeit=THEME3)
	if HIDESPACERS == 'No': addFile(wiz.sep(), '', icon=ICONREAL, themeit=THEME3)
	
	for debrid in debridit.ORDER:
		name   = DEBRIDID[debrid]['name']
		path   = DEBRIDID[debrid]['path']
		saved  = DEBRIDID[debrid]['saved']
		file   = DEBRIDID[debrid]['file']
		user   = wiz.getS(saved)
		auser  = debridit.debridUser(debrid)
		icon   = DEBRIDID[debrid]['icon']   if os.path.exists(path) else ICONREAL
		fanart = DEBRIDID[debrid]['fanart'] if os.path.exists(path) else FANART
		menu = createMenu('saveaddon', 'Debrid', debrid)
		menu2 = createMenu('save', 'Debrid', debrid)
		menu.append((THEME2 % '%s Settings' % name,              'RunPlugin(plugin://%s/?mode=opensettings&name=%s&url=debrid)' %   (ADDON_ID, debrid)))
		
		addFile1('[+]-> %s' % name,     '', icon=icon, fanart=fanart, themeit=THEME3)
		if not os.path.exists(path): addFile1('[COLOR red]Addon Data: Not Installed[/COLOR]', '', icon=icon, fanart=fanart, menu=menu)
		elif not auser:              addFile1('[COLOR red]Addon Data: Not Registered[/COLOR]','authdebrid', debrid, icon=icon, fanart=fanart, menu=menu)
		else:                        addFile1('[COLOR green]Addon Data: %s[/COLOR]' % auser,'authdebrid', debrid, icon=icon, fanart=fanart, menu=menu)
		if user == "":
			if os.path.exists(file): addFile1('[COLOR red]Saved Data: Save File Found(Import Data)[/COLOR]','importdebrid', debrid, icon=icon, fanart=fanart, menu=menu2)
			else :                   addFile1('[COLOR red]Saved Data: Not Saved[/COLOR]','savedebrid', debrid, icon=icon, fanart=fanart, menu=menu2)
		else:                        addFile1('[COLOR green]Saved Data: %s[/COLOR]' % user, '', icon=icon, fanart=fanart, menu=menu2)
	
	if HIDESPACERS == 'No': addFile(wiz.sep(), '', themeit=THEME3)
	addFile1('Save All Real Debrid Data',          'savedebrid',    'all', icon=ICONREAL,  themeit=THEME3)
	addFile1('Recover All Saved Real Debrid Data', 'restoredebrid', 'all', icon=ICONREAL,  themeit=THEME3)
	addFile1('Import Real Debrid Data',            'importdebrid',  'all', icon=ICONREAL,  themeit=THEME3)
	addFile1('Clear All Saved Real Debrid Data',   'cleardebrid',   'all', icon=ICONREAL,  themeit=THEME3)
	addFile1('Clear All Addon Data',               'addondebrid',   'all', icon=ICONREAL,  themeit=THEME3)
	setView('files', 'viewType')

def removeAddonMenu():
	fold = glob.glob(os.path.join(ADDONS, '*/'))
	for folder in sorted(fold, key = lambda x: x):
		foldername = folder.replace(ADDONS, '').replace('\\', '').replace('/', '')
		icon = os.path.join(folder, 'icon.png')
		fanart = os.path.join(folder, 'fanart.png')
		if foldername in EXCLUDES: pass
		elif foldername == 'packages': pass
		else:
			folderdisplay = foldername
			replace = {'audio.':'[COLOR orange][AUDIO] [/COLOR]', 'metadata.':'[COLOR cyan][METADATA] [/COLOR]', 'module.':'[COLOR orange][MODULE] [/COLOR]', 'plugin.':'[COLOR blue][PLUGIN] [/COLOR]', 'program.':'[COLOR orange][PROGRAM] [/COLOR]', 'repository.':'[COLOR gold][REPO] [/COLOR]', 'script.':'[COLOR green][SCRIPT] [/COLOR]', 'service.':'[COLOR green][SERVICE] [/COLOR]', 'skin.':'[COLOR dodgerblue][SKIN] [/COLOR]', 'video.':'[COLOR orange][VIDEO] [/COLOR]', 'weather.':'[COLOR yellow][WEATHER] [/COLOR]'}
			for rep in replace:
				folderdisplay = folderdisplay.replace(rep, replace[rep])
			addFile1('[COLOR red][B][REMOVE][/B][/COLOR] %s' % folderdisplay, 'removeaddon', foldername, icon=icon, fanart=fanart, themeit=THEME2)
	setView('files', 'viewType')

def removeAddonDataMenu():
	if os.path.exists(ADDOND):
		addFile1('[COLOR red][B][REMOVE][/B][/COLOR] All Addon_Data', 'removedata', 'all', themeit=THEME2)
		addFile1('[COLOR red][B][REMOVE][/B][/COLOR] All Addon_Data for Uninstalled Addons', 'removedata', 'uninstalled', themeit=THEME2)
		addFile1('[COLOR red][B][REMOVE][/B][/COLOR] All Empty Folders in Addon_Data', 'removedata', 'empty', themeit=THEME2)
		addFile1('[COLOR red][B][REMOVE][/B][/COLOR] %s Addon_Data' % ADDONTITLE, 'resetaddon', themeit=THEME2)
		if HIDESPACERS == 'No': addFile(wiz.sep(), '', themeit=THEME3)
		fold = glob.glob(os.path.join(ADDOND, '*/'))
		for folder in sorted(fold, key = lambda x: x):
			foldername = folder.replace(ADDOND, '').replace('\\', '').replace('/', '')
			icon = os.path.join(folder.replace(ADDOND, ADDONS), 'icon.png')
			fanart = os.path.join(folder.replace(ADDOND, ADDONS), 'fanart.png')
			folderdisplay = foldername
			replace = {'audio.':'[COLOR orange][AUDIO] [/COLOR]', 'metadata.':'[COLOR cyan][METADATA] [/COLOR]', 'module.':'[COLOR orange][MODULE] [/COLOR]', 'plugin.':'[COLOR blue][PLUGIN] [/COLOR]', 'program.':'[COLOR orange][PROGRAM] [/COLOR]', 'repository.':'[COLOR gold][REPO] [/COLOR]', 'script.':'[COLOR green][SCRIPT] [/COLOR]', 'service.':'[COLOR green][SERVICE] [/COLOR]', 'skin.':'[COLOR dodgerblue][SKIN] [/COLOR]', 'video.':'[COLOR orange][VIDEO] [/COLOR]', 'weather.':'[COLOR yellow][WEATHER] [/COLOR]'}
			for rep in replace:
				folderdisplay = folderdisplay.replace(rep, replace[rep])
			if foldername in EXCLUDES: folderdisplay = '[COLOR green][B][PROTECTED][/B][/COLOR] %s' % folderdisplay
			else: folderdisplay = '[COLOR red][B][REMOVE][/B][/COLOR] %s' % folderdisplay
			addFile(' %s' % folderdisplay, 'removedata', foldername, icon=icon, fanart=fanart, themeit=THEME2)
	else:
		addFile1('No Addon data folder found.', '', themeit=THEME3)
	setView('files', 'viewType')

def enableAddons():
	addFile1("[I][B][COLOR red]!!Notice: Disabling Some Addons Can Cause Issues!![/COLOR][/B][/I]", '', icon=ICONMAINT)
	fold = glob.glob(os.path.join(ADDONS, '*/'))
	for folder in sorted(fold, key = lambda x: x):
		if ADDON_ID in folder: continue
		addonxml = os.path.join(folder, 'addon.xml')
		if os.path.exists(addonxml):
			fold   = folder.replace(ADDONS, '')[1:-1]
			f      = open(addonxml)
			a      = f.read().replace('\n','').replace('\r','').replace('\t','')
			match  = re.compile('<addo.+?id="(.+?)".+?>').findall(a)
			match2 = re.compile('<addo.+? name="(.+?)".+?>').findall(a)
			try:
				pluginid = match[0]
				name = match2[0]
			except:
				continue
			try:
				add    = xbmcaddon.Addon(id=pluginid)
				state  = "[COLOR green][Enabled][/COLOR]"
				goto   = "false"
			except:
				state  = "[COLOR red][Disabled][/COLOR]"
				goto   = "true"
				pass
			icon   = os.path.join(folder, 'icon.png') if os.path.exists(os.path.join(folder, 'icon.png')) else ICON
			fanart = os.path.join(folder, 'fanart.jpg') if os.path.exists(os.path.join(folder, 'fanart.jpg')) else FANART
			addFile1("%s %s" % (state, name), 'toggleaddon', fold, goto, icon=icon, fanart=fanart)
			f.close()
	setView('files', 'viewType')

def changeFeq():
	feq        = ['Every Startup', 'Every Day', 'Every Three Days', 'Every Weekly']
	change     = DIALOG.select("[COLOR %s]How often would you list to Auto Clean on Startup?[/COLOR]" % COLOR2, feq)
	if not change == -1: 
		wiz.setS('autocleanfeq', str(change))
		wiz.LogNotify('Auto Clean Up', 'Fequency Now %s' % feq[change])

##############################################
########Developer Menu If Selected############
##############################################
def developer():
	addFile1('Test Update'                        , 'testupdate',            themeit=THEME1)
	addFile1('Test First Run'                     , 'testfirst',             themeit=THEME1)
	setView('files', 'viewType')
	addFile('Convert Paths to special'                    , 'convertpath', icon=ICON, themeit=THEME1)
	addFile1('Test Notifications'                          , 'testnotify',  icon=ICON, themeit=THEME1)

###########################
###### Build Install ######
###########################

def buildWizard(name, type, theme=None):
	testbuild = wiz.checkBuild(name, 'url')
	if testbuild == False:
		wiz.LogNotify(ADDONTITLE, "Unabled to find build")
		return
	if type == 'gui':
		if name == BUILDNAME:
			yes = DIALOG.yesno(ADDONTITLE, '[COLOR %s]Would you like to apply the guifix for:' % COLOR2, '[COLOR %s]%s[/COLOR]?[/COLOR]' % (COLOR1, name), nolabel='[B]No, Cancel[/B]',yeslabel='[B]Apply Fix[/B]')
		else: 
			yes = DIALOG.yesno("%s - [COLOR red]WARNING!![/COLOR]" % ADDONTITLE, "[COLOR %s][COLOR %s]%s[/COLOR] community build is not currently installed." % (COLOR2, COLOR1, name), "Would you like to apply the guiFix anyways?.[/COLOR]", nolabel='[B]No, Cancel[/B]',yeslabel='[B]Apply Fix[/B]')
		if yes:
			buildzip = wiz.checkBuild(name,'gui')
			zipname = name.replace('\\', '').replace('/', '').replace(':', '').replace('*', '').replace('?', '').replace('"', '').replace('<', '').replace('>', '').replace('|', '')
			if not wiz.workingURL(buildzip) == True: wiz.LogNotify(ADDONTITLE, 'GuiFix: [COLOR red]Invalid Zip Url![/COLOR]'); return
			if not os.path.exists(PACKAGES): os.makedirs(PACKAGES)
			DP.create(ADDONTITLE,'[COLOR %s][B]Downloading GuiFix:[/B][/COLOR] [COLOR %s]%s[/COLOR]' % (COLOR2, COLOR1, name),'', 'Please Wait')
			lib=os.path.join(PACKAGES, '%s_guisettings.zip' % zipname)
			try: os.remove(lib)
			except: pass
			downloader.download(buildzip, lib, DP)
			xbmc.sleep(500)
			title = '[COLOR %s][B]Installing:[/B][/COLOR] [COLOR %s]%s[/COLOR]' % (COLOR2, COLOR1, name)
			DP.update(0, title,'', 'Please Wait')
			extract.all(lib,USERDATA,DP, title=title)
			DP.close()
			wiz.defaultSkin()
			wiz.lookandFeelData('save')
			DIALOG.ok(ADDONTITLE, "[COLOR %s]To save changes you now need to force close Kodi, Press OK to force close Kodi[/COLOR]" % COLOR2)
			wiz.killxbmc('true')
		else:
			wiz.LogNotify(ADDONTITLE, 'GuiFix: [COLOR red]Cancelled![/COLOR]')
	elif type == 'fresh':
		freshStart(name)
	elif type == 'normal':
		if url == 'normal':
			if KEEPTRAKT == 'true':
				traktit.autoUpdate('all')
				wiz.setS('traktlastsave', str(THREEDAYS))
			if KEEPREAL == 'true':
				debridit.autoUpdate('all')
				wiz.setS('debridlastsave', str(THREEDAYS))
			if KEEPLOGIN == 'true':
				loginit.autoUpdate('all')
				wiz.setS('loginlastsave', str(THREEDAYS))
		temp_kodiv = int(KODIV); buildv = int(float(wiz.checkBuild(name, 'kodi')))
		if not temp_kodiv == buildv: 
			if temp_kodiv == 16 and buildv <= 15: warning = False
			else: warning = True
		else: warning = False
		if warning == True:
			yes_pressed = DIALOG.yesno("%s - [COLOR red]WARNING!![/COLOR]" % ADDONTITLE, '[COLOR %s]There is a chance that the skin will not appear correctly' % COLOR2, 'When installing a %s build on a Kodi %s install' % (wiz.checkBuild(name, 'kodi'), KODIV), 'Would you still like to install: [COLOR %s]%s v%s[/COLOR]?[/COLOR]' % (COLOR1, name, wiz.checkBuild(name,'version')), nolabel='[B]No, Cancel[/B]',yeslabel='[B]Yes, Install[/B]')
		else:
			yes_pressed = DIALOG.yesno(ADDONTITLE, '[COLOR %s]Would you like to Download and Install:' % COLOR2, '[COLOR %s]%s v%s[/COLOR]?[/COLOR]' % (COLOR1, name, wiz.checkBuild(name,'version')), nolabel='[B]No, Cancel[/B]',yeslabel='[B]Yes, Install[/B]')
		if yes_pressed:
			wiz.clearS('build')
			buildzip = wiz.checkBuild(name, 'url')
			zipname = name.replace('\\', '').replace('/', '').replace(':', '').replace('*', '').replace('?', '').replace('"', '').replace('<', '').replace('>', '').replace('|', '')
			if not wiz.workingURL(buildzip) == True: wiz.LogNotify(ADDONTITLE, 'Build Install: [COLOR red]Invalid Zip Url![/COLOR]'); return
			if not os.path.exists(PACKAGES): os.makedirs(PACKAGES)
			DP.create(ADDONTITLE,'[COLOR %s][B]Downloading:[/B][/COLOR] [COLOR %s]%s v%s[/COLOR]' % (COLOR2, COLOR1, name, wiz.checkBuild(name,'version')),'', 'Please Wait')
			lib=os.path.join(PACKAGES, '%s.zip' % zipname)
			try: os.remove(lib)
			except: pass
			downloader.download(buildzip, lib, DP)
			xbmc.sleep(500)
			title = '[COLOR %s][B]Installing:[/B][/COLOR] [COLOR %s]%s v%s[/COLOR]' % (COLOR2, COLOR1, name, wiz.checkBuild(name,'version'))
			DP.update(0, title,'', 'Please Wait')
			percent, errors, error = extract.all(lib,HOME,DP, title=title)
			if int(float(percent)) > 0:
				wiz.lookandFeelData('save')
				wiz.defaultSkin()
				wiz.setS('buildname', name)
				wiz.setS('buildversion', wiz.checkBuild( name,'version'))
				wiz.setS('buildtheme', '')
				wiz.setS('latestversion', wiz.checkBuild( name,'version'))
				wiz.setS('lastbuildcheck', str(NEXTCHECK))
				wiz.setS('installed', 'true')
				wiz.setS('extract', str(percent))
				wiz.setS('errors', str(errors))
				wiz.log('INSTALLED %s: [ERRORS:%s]' % (percent, errors))
				if int(float(errors)) > 0:
					yes=DIALOG.yesno(ADDONTITLE, '[COLOR %s][COLOR %s]%s v%s[/COLOR]' % (COLOR2, COLOR1, name, wiz.checkBuild( name,'version')), 'Completed: [COLOR %s]%s%s[/COLOR] [Errors:[COLOR %s]%s[/COLOR]]' % (COLOR1, percent, '%', COLOR1, errors), 'Would you like to view the errors?[/COLOR]', nolabel='[B]No Thanks[/B]',yeslabel='[B]View Errors[/B]')
					if yes:
						if isinstance(errors, unicode):
							error = error.encode('utf-8')
						wiz.TextBoxes(ADDONTITLE, error)
				DP.close()
				themefile = wiz.checkBuild(name, 'theme')
				if not themefile == 'http://':
					works = wiz.workingURL(themefile)
					if works == True: buildWizard(name, 'theme')
					else: wiz.log("Theme File Not Working: %s" % works)
				DIALOG.ok(ADDONTITLE, "[COLOR %s]To save changes you now need to force close Kodi, Press OK to force close Kodi[/COLOR]" % COLOR2)
				wiz.killxbmc('true')
			else:
				if isinstance(errors, unicode):
					error = error.encode('utf-8')
				wiz.TextBoxes("%s: Error Installing Build" % ADDONTITLE, error)
		else:
			wiz.LogNotify(ADDONTITLE, 'Build Install: [COLOR red]Cancelled![/COLOR]')
	elif type == 'theme':
		if theme == None:
			themefile = wiz.checkBuild(name, 'theme')
			themelist = []
			if not themefile == 'http://' and wiz.workingURL(themefile) == True:
				link  = wiz.openURL(themefile).replace('\n','').replace('\r','').replace('\t','')
				match = re.compile('name="(.+?)"').findall(link)
				if len(match) > 0:
					if DIALOG.yesno(ADDONTITLE, "[COLOR %s]The Build [COLOR %s]%s[/COLOR] comes with [COLOR %s]%s[/COLOR] different themes" % (COLOR2, COLOR1, name, COLOR1, len(match)), "Would you like to install one now?[/COLOR]", yeslabel="[B]Install Theme[/B]", nolabel="[B]Cancel Themes[/B]"):
						for themename in match:
							themelist.append(themename)
						wiz.log("Theme List: %s " % str(themelist))
						ret = DIALOG.select(ADDONTITLE, themelist)
						wiz.log("Theme install selected: %s" % ret)
						if not ret == -1: theme = themelist[ret]; installtheme = True
						else: wiz.LogNotify(ADDONTITLE,'Theme Install: [COLOR red]Cancelled![/COLOR]'); return
					else: wiz.LogNotify(ADDONTITLE,'Theme Install: [COLOR red]Cancelled![/COLOR]'); return
			else: wiz.LogNotify(ADDONTITLE,'Theme Install: [COLOR red]None Found![/COLOR]')
		else: installtheme = DIALOG.yesno(ADDONTITLE, '[COLOR %s]Would you like to install the theme:' % COLOR2, '[COLOR %s]%s[/COLOR]' % (COLOR1, theme), 'for [COLOR %s]%s v%s[/COLOR]?[/COLOR]' % (COLOR1, name, wiz.checkBuild(name,'version')), yeslabel="[B]Install Theme[/B]", nolabel="[B]Cancel Themes[/B]")
		if installtheme:
			themezip = wiz.checkTheme(name, theme, 'url')
			zipname = name.replace('\\', '').replace('/', '').replace(':', '').replace('*', '').replace('?', '').replace('"', '').replace('<', '').replace('>', '').replace('|', '')
			if not wiz.workingURL(themezip) == True: wiz.LogNotify(ADDONTITLE, 'Theme Install: [COLOR red]Invalid Zip Url![/COLOR]'); return False
			if not os.path.exists(PACKAGES): os.makedirs(PACKAGES)
			DP.create(ADDONTITLE,'[COLOR %s][B]Downloading:[/B][/COLOR] [COLOR %s]%s[/COLOR]' % (COLOR2, COLOR1, name),'', 'Please Wait')
			lib=os.path.join(PACKAGES, '%s.zip' % zipname)
			try: os.remove(lib)
			except: pass
			downloader.download(themezip, lib, DP)
			xbmc.sleep(500)
			DP.update(0,"", "Installing %s " % name)
			test = False
			if url not in ["fresh", "normal"]:
				test = testTheme(lib) if not wiz.currSkin() in ['skin.confluence', 'skin.estuary'] else False
				if test == True:
					wiz.lookandFeelData('save')
					skin     = 'skin.confluence' if KODIV < 17 else 'skin.estuary'
					gotoskin = xbmc.getSkinDir()
					if DIALOG.yesno(ADDONTITLE, "[COLOR %s]Installing the theme [COLOR %s]%s[/COLOR] requires the skin to be swaped back to [COLOR %s]%s[/COLOR]" % (COLOR2, COLOR1, theme, COLOR1, skin[5:]), "Would you like to switch the skin?[/COLOR]", yeslabel="[B]Switch Skin[/B]", nolabel="[B]Don't Switch[/B]"):
						skinSwitch.swapSkins(skin)
						x = 0
						xbmc.sleep(1000)
						while not xbmc.getCondVisibility("Window.isVisible(yesnodialog)") and x < 150:
							x += 1
							xbmc.sleep(200)

						if xbmc.getCondVisibility("Window.isVisible(yesnodialog)"):
							wiz.ebi('SendClick(11)')
						else: wiz.LogNotify(ADDONTITLE,'Theme Install: [COLOR red]Skin Swap Timed Out![/COLOR]'); return
						xbmc.sleep(500)
					else: wiz.log("Theme Installer: %s skin swap ignored." % theme)
			title = '[COLOR %s][B]Installing Theme:[/B][/COLOR] [COLOR %s]%s[/COLOR]' % (COLOR2, COLOR1, name)
			DP.update(0, title,'', 'Please Wait')
			percent, errors, error = extract.all(lib,HOME,DP, title=title)
			wiz.setS('buildtheme', theme)
			wiz.log('INSTALLED %s: [ERRORS:%s]' % (percent, errors))
			DP.close()
			if url not in ["fresh", "normal"]: 
				if test == True:
					skinSwitch.swapSkins(gotoskin)
					x = 0
					xbmc.sleep(1000)
					while not xbmc.getCondVisibility("Window.isVisible(yesnodialog)") and x < 150:
						x += 1
						xbmc.sleep(200)

					if xbmc.getCondVisibility("Window.isVisible(yesnodialog)"):
						wiz.ebi('SendClick(11)')
					else: wiz.LogNotify(ADDONTITLE,'Theme Install: [COLOR red]Skin Swap Timed Out![/COLOR]'); return
					wiz.lookandFeelData('restore')
				else:
					wiz.ebi("ReloadSkin()")
					xbmc.sleep(1000)
					wiz.ebi("Container.Refresh") 
		else:
			wiz.LogNotify(ADDONTITLE, 'Theme Install: [COLOR red]Cancelled![/COLOR]')

def testTheme(path):
	zfile = zipfile.ZipFile(path)
	for item in zfile.infolist():
		if '/settings.xml' in item.filename:
			return True
	return False

def testGui(path):
	zfile = zipfile.ZipFile(path)
	for item in zfile.infolist():
		if '/guisettings.xml' in item.filename:
			return True
	return False

####################################
##########APK Installer#############
####################################
def apkInstaller(apk, url, Brackets):
	if wiz.platform() == 'android':
		if apk in ['kodi', 'spmc']:
			yes=DIALOG.yesno(ADDONTITLE, "Would you like to download and install:", "%s (v%s)" % (apk.upper(),wiz.latestApk(apk,'version')))
			if not yes: wiz.LogNotify(ADDONTITLE, '[COLOR red]ERROR:[/COLOR] Install Cancelled'); return
			display = "%s v%s" % (apk.upper(), wiz.latestApk(apk, 'version'))
		else:
			yes=DIALOG.yesno(ADDONTITLE, "Would you like to download and install:", "%s" % apk)
			if not yes: wiz.LogNotify(ADDONTITLE, '[COLOR red]ERROR:[/COLOR] Install Cancelled'); return
			display = apk
		if yes:
			if not os.path.exists(PACKAGES): os.makedirs(PACKAGES)
			if not wiz.workingURL(url) == True: wiz.LogNotify(ADDONTITLE, 'APK Installer: [COLOR red]Invalid Apk Url![/COLOR]'); return
			DP.create(ADDONTITLE,'Downloading %s' % display,'', 'Please Wait')
			lib=os.path.join(PACKAGES, "%s.apk" % apk)
			try: os.remove(lib)
			except: pass
			downloader.download(url, lib, DP)
			xbmc.sleep(500)
			DP.close()
			if "Brackets" in Brackets:
				zf = zipfile.ZipFile(lib)
				for file in  zf.namelist():
					if file.endswith('.apk'):
						with open(os.path.join(PACKAGES,os.path.basename(file)), 'wb') as f:
							file2 = file.split('/')[1]
							f.write(zf.read(file))
							xbmc.sleep(500)
							f.close()
							try:
								os.remove(lib)
							except:
								pass
							lib = os.path.join(PACKAGES, file2)
			DIALOG.ok(ADDONTITLE, "Launching the APK to be installed", "Follow the install process to complete.")
			xbmc.executebuiltin('StartAndroidActivity("","android.intent.action.VIEW","application/vnd.android.package-archive","file:'+lib+'")')
		else: wiz.LogNotify(ADDONTITLE, '[COLOR red]ERROR:[/COLOR] Install Cancelled')
	else: wiz.LogNotify(ADDONTITLE, '[COLOR red]ERROR:[/COLOR] None Android Device')

###########################
#####ROM Installer#########
###########################
def INSTALLROM(name,url,):
	if "NULL" in url:
		DIALOG.ok(ADDONTITLE, "[COLOR ghostwhite]Not a valid selection, please try again.[/COLOR]")
		sys.exit(1)

	dp = xbmcgui.DialogProgress()
	dp.create(ADDONTITLE,"","",'ROM: ' + name)
	zipname = name.replace('\\', '').replace('/', '').replace(':', '').replace('*', '').replace('?', '').replace('"', '').replace('<', '').replace('>', '').replace('|', '')
	lib=os.path.join(PACKAGES, '%s.zip' % zipname)
	downloader.download(url, lib, dp)
	dp.update(0)
	extract.all(lib,ROMLOCATION,dp)
	DIALOG.ok(ADDONTITLE, "[COLOR yellow]Download complete, ROM Location: [/COLOR][COLOR white]" + ROMLOCATION + "[/COLOR]")

###########################
###### Misc Functions######
###########################

def percentage(part, whole):
	return 100 * float(part)/float(whole)

def createMenu(type, add, name):
	if   type == 'saveaddon':
		menu_items=[]
		add2  = urllib.quote_plus(add.lower().replace(' ', ''))
		add3  = add.replace('Debrid', 'Real Debrid')
		name2 = urllib.quote_plus(name.lower().replace(' ', ''))
		name = name.replace('url', 'URL Resolver')
		menu_items.append((THEME2 % name.title(),             ' '))
		menu_items.append((THEME3 % 'Save %s Data' % add3,               'RunPlugin(plugin://%s/?mode=save%s&name=%s)' %    (ADDON_ID, add2, name2)))
		menu_items.append((THEME3 % 'Restore %s Data' % add3,            'RunPlugin(plugin://%s/?mode=restore%s&name=%s)' % (ADDON_ID, add2, name2)))
		menu_items.append((THEME3 % 'Clear %s Data' % add3,              'RunPlugin(plugin://%s/?mode=clear%s&name=%s)' %   (ADDON_ID, add2, name2)))
	elif type == 'save'    :
		menu_items=[]
		add2  = urllib.quote_plus(add.lower().replace(' ', ''))
		add3  = add.replace('Debrid', 'Real Debrid')
		name2 = urllib.quote_plus(name.lower().replace(' ', ''))
		name = name.replace('url', 'URL Resolver')
		menu_items.append((THEME2 % name.title(),             ' '))
		menu_items.append((THEME3 % 'Register %s' % add3,                'RunPlugin(plugin://%s/?mode=auth%s&name=%s)' %    (ADDON_ID, add2, name2)))
		menu_items.append((THEME3 % 'Save %s Data' % add3,               'RunPlugin(plugin://%s/?mode=save%s&name=%s)' %    (ADDON_ID, add2, name2)))
		menu_items.append((THEME3 % 'Restore %s Data' % add3,            'RunPlugin(plugin://%s/?mode=restore%s&name=%s)' % (ADDON_ID, add2, name2)))
		menu_items.append((THEME3 % 'Import %s Data' % add3,             'RunPlugin(plugin://%s/?mode=import%s&name=%s)' %  (ADDON_ID, add2, name2)))
		menu_items.append((THEME3 % 'Clear Addon %s Data' % add3,        'RunPlugin(plugin://%s/?mode=addon%s&name=%s)' %   (ADDON_ID, add2, name2)))
	elif type == 'install'  :
		menu_items=[]
		name2 = urllib.quote_plus(name)
		menu_items.append((THEME2 % name,                                'RunAddon(%s, ?mode=viewbuild&name=%s)'  % (ADDON_ID, name2)))
		menu_items.append((THEME3 % 'Fresh Install',                     'RunPlugin(plugin://%s/?mode=install&name=%s&url=fresh)'  % (ADDON_ID, name2)))
		menu_items.append((THEME3 % 'Normal Install',                    'RunPlugin(plugin://%s/?mode=install&name=%s&url=normal)' % (ADDON_ID, name2)))
		menu_items.append((THEME3 % 'Apply guiFix',                      'RunPlugin(plugin://%s/?mode=install&name=%s&url=gui)'    % (ADDON_ID, name2)))
		menu_items.append((THEME3 % 'Build Information',                 'RunPlugin(plugin://%s/?mode=buildinfo&name=%s)'  % (ADDON_ID, name2)))
	menu_items.append((THEME2 % '%s Settings' % ADDONTITLE,              'RunPlugin(plugin://%s/?mode=settings)' % ADDON_ID))
	return menu_items

def toggleCache(state):
	cachelist = ['includevideo', 'includeall', 'includebob', 'includephoenix', 'includespecto', 'includegenesis', 'includeexodus', 'includeonechan', 'includesalts', 'includesaltslite']
	titlelist = ['Include Video Addons', 'Include All Addons', 'Include Bob', 'Include Phoenix', 'Include Specto', 'Include Genesis', 'Include Exodus', 'Include One Channel', 'Include Salts', 'Include Salts Lite HD']
	if state in ['true', 'false']:
		for item in cachelist:
			wiz.setS(item, state)
	else:
		if not state in ['includevideo', 'includeall'] and wiz.getS('includeall') == 'true':
			try:
				item = titlelist[cachelist.index(state)]
				DIALOG.ok(ADDONTITLE, "[COLOR %s]You will need to turn off [COLOR %s]Include All Addons[/COLOR] to disable[/COLOR] [COLOR %s]%s[/COLOR]" % (COLOR2, COLOR1, COLOR1, item))
			except:
				wiz.LogNotify("Toggle Cache", "Invalid id: %s" % state)
		else:
			new = 'true' if wiz.getS(state) == 'false' else 'false'
			wiz.setS(state, new)

def playVideo(url):
	if 'watch?v=' in url:
		a, b = url.split('?')
		find = b.split('&')
		for item in find:
			if item.startswith('v='):
				url = item[2:]
				break
			else: continue
	elif 'embed' in url or 'youtu.be' in url:
		a = url.split('/')
		if len(a[-1]) > 5:
			url = a[-1]
		elif len(a[-2]) > 5:
			url = a[-2]
	wiz.log("YouTube URL: %s" % url)
	yt.PlayVideo(url)

def viewLogFile():
	mainlog = wiz.Grab_Log(True)
	oldlog  = wiz.Grab_Log(True, True)
	which = 0; logtype = mainlog
	if not oldlog == False and not mainlog == False:
		which = DIALOG.select(ADDONTITLE, ["View %s" % mainlog.replace(LOG, ""), "View %s" % oldlog.replace(LOG, "")])
		if which == -1: wiz.LogNotify('View Log', 'View Log Cancelled!'); return
	elif mainlog == False and oldlog == False:
		wiz.LogNotify('View Log', 'No Log File Found!')
		return
	elif not mainlog == False: which = 0
	elif not oldlog == False: which = 1
	
	logtype = mainlog if which == 0 else oldlog
	msg     = wiz.Grab_Log(False) if which == 0 else wiz.Grab_Log(False, True)
	
	wiz.TextBoxes("%s - %s" % (ADDONTITLE, logtype), msg)

def errorChecking(log=None, count=None, all=None):
	if log == None:
		mainlog = wiz.Grab_Log(True)
		oldlog  = wiz.Grab_Log(True, True)
		if not oldlog == False and not mainlog == False:
			which = DIALOG.select(ADDONTITLE, ["View %s: %s error(s)" % (mainlog.replace(LOG, ""), errorChecking(mainlog, True)), "View %s: %s error(s)" % (oldlog.replace(LOG, ""), errorChecking(oldlog, True))])
			if which == -1: wiz.LogNotify('View Log', 'View Log Cancelled!'); return
		elif mainlog == False and oldlog == False:
			wiz.LogNotify('View Log', 'No Log File Found!')
			return
		elif not mainlog == False: which = 0
		elif not oldlog == False: which = 1
		log = mainlog if which == 0 else oldlog
	if log == False:
		if count == None:
			wiz.LogNotify(ADDONTITLE, "Log File not Found")
			return False
		else: 
			return 0
	else:
		if os.path.exists(log):
			f = open(log,mode='r'); a = f.read().replace('\n', '').replace('\r', ''); f.close()
			match = re.compile("-->Python callback/script returned the following error<--(.+?)-->End of Python script error report<--").findall(a)
			if not count == None:
				if all == None: 
					x = 0
					for item in match:
						if ADDON_ID in item: x += 1
					return x
				else: return len(match)
			if len(match) > 0:
				x = 0; msg = ""
				for item in match:
					if all == None and not ADDON_ID in item: continue
					else: 
						x += 1
						msg += "[COLOR red]Error Number %s[/COLOR]\n(PythonToCppException) : -->Python callback/script returned the following error<--%s-->End of Python script error report<--\n\n" % (x, item.replace('                                          ', '\n').replace('\\\\','\\').replace(HOME, ''))
				if x > 0:
					if KODIV >= 16: DIALOG.textviewer(ADDONTITLE, msg)
					else: wiz.TextBoxes(ADDONTITLE, msg)
				else: wiz.LogNotify(ADDONTITLE, "No Errors Found in Log")
			else: wiz.LogNotify(ADDONTITLE, "No Errors Found in Log")
		else: wiz.LogNotify(ADDONTITLE, "Log File not Found")

def viewWizLogFile():
	if os.path.exists(WIZLOG):
		f = open(WIZLOG,mode='r'); msg = f.read(); f.close()
		wiz.TextBoxes("%s - Wizard.log" % ADDONTITLE, msg)
	else:
		wiz.LogNotify('View Log', 'Wizard.log not found!')

def removeAddon(addon):
	if DIALOG.yesno(ADDONTITLE, '[COLOR %s]Are you sure you want to delete the addon:'% COLOR1, '[COLOR %s]%s[/COLOR]?[/COLOR]' % (COLOR1, addon), yeslabel='[B]Remove Addon[/B]', nolabel='[B]Don\'t Remove[/B]'):
		wiz.cleanHouse(os.path.join(ADDONS, addon))
		removeAddonData(addon)
		wiz.LogNotify('Remove Addon', 'Complete!')
		DIALOG.ok(ADDONTITLE, '[COLOR %s]The addon has been removed but will remain in the addons list until the next time you reload Kodi.[/COLOR]')
	else: wiz.LogNotify('Remove Addon', 'Cancelled!')
	wiz.refresh()

def removeAddonData(addon):
	if addon == 'all':
		if DIALOG.yesno(ADDONTITLE, '[COLOR %s]Would you like to remove [COLOR %s]ALL[/COLOR] addon data stored in you Userdata folder?[/COLOR]' % (COLOR2, COLOR1), yeslabel='[B]Remove Data[/B]', nolabel='[B]Don\'t Remove[/B]'):
			wiz.cleanHouse(ADDOND)
		else: wiz.LogNotify('Remove Addon Data', 'Cancelled!')
	elif addon == 'uninstalled':
		if DIALOG.yesno(ADDONTITLE, '[COLOR %s]Would you like to remove [COLOR %s]ALL[/COLOR] addon data stored in you Userdata folder for uninstalled addons?[/COLOR]' % (COLOR2, COLOR1), yeslabel='[B]Remove Data[/B]', nolabel='[B]Don\'t Remove[/B]'):
			total = 0
			for folder in glob.glob(os.path.join(ADDOND, '*')):
				foldername = folder.replace(ADDOND, '').replace('\\', '').replace('/', '')
				if foldername in EXCLUDES: pass
				elif os.path.exists(os.path.join(ADDONS, foldername)): pass
				else: wiz.cleanHouse(folder); total += 1; wiz.log(folder); shutil.rmtree(folder)
			wiz.LogNotify('Clean up Uninstalled', '[COLOR yellow]%s[/COLOR] Folders(s) Removed' % total)
		else: wiz.LogNotify('Remove Addon Data', 'Cancelled!')
	elif addon == 'empty':
		if DIALOG.yesno(ADDONTITLE, '[COLOR %s]Would you like to remove [COLOR %s]ALL[/COLOR] empty addon data folders in you Userdata folder?[/COLOR]' % (COLOR2, COLOR1), yeslabel='[B]Remove Data[/B]', nolabel='[B]Don\'t Remove[/B]'):
			total = wiz.emptyfolder(ADDOND)
			wiz.LogNotify('Remove Empty Folders', '[COLOR yellow]%s[/COLOR] Folders(s) Removed' % total)
		else: wiz.LogNotify('Remove Empty Folders', 'Cancelled!')
	else:
		addon_data = os.path.join(USERDATA, 'addon_data', addon)
		if addon in EXCLUDES:
			wiz.LogNotify("Protected Plugin", "Not allowed to remove Addon_Data")
		elif os.path.exists(addon_data):  
			if DIALOG.yesno(ADDONTITLE, '[COLOR %s]Would you also like to remove the addon data for:[/COLOR]' % COLOR2, '[COLOR %s]%s[/COLOR]' % (COLOR1, addon), yeslabel='[B]Remove Data[/B]', nolabel='[B]Don\'t Remove[/B]'):
				wiz.cleanHouse(addon_data)
				try:
					shutil.rmtree(addon_data)
				except:
					wiz.log("Error deleting: %s" % addon_data)
			else: 
				wiz.log('Addon data for %s was not removed' % addon)
	wiz.refresh()

def restoreit(type):
	if type == 'build':
		x = freshStart('restore')
		if x == False: wiz.LogNotify(ADDONTITLE, "Local Restore Cancelled"); return
	wiz.restoreLocal(type)

def restoreextit(type):
	if type == 'build':
		x = freshStart('restore')
		if x == False: wiz.LogNotify(ADDONTITLE, "External Restore Cancelled"); return
	wiz.restoreExternal(type)

def buildInfo(name):
	if wiz.workingURL(BUILDFILE) == True:
		if wiz.checkBuild(name, 'url'):
			name, version, url, gui, kodi, theme, icon, fanart, adult, description = wiz.checkBuild(name, 'all')
			adult = 'Yes' if adult.lower() == 'yes' else 'No'
			msg  = "[COLOR %s]Build Name:[/COLOR] [COLOR %s]%s[/COLOR][CR]" % (COLOR2, COLOR1, name)
			msg += "[COLOR %s]Build Version:[/COLOR] [COLOR %s]%s[/COLOR][CR]" % (COLOR2, COLOR1, version)
			if not theme == "http://": 
				themecount = wiz.themeCount(name, False)
				msg += "[COLOR %s]Build Theme(s):[/COLOR] [COLOR %s]%s[/COLOR][CR]" % (COLOR2, COLOR1, ', '.join(themecount))
			msg += "[COLOR %s]Kodi Version:[/COLOR] [COLOR %s]%s[/COLOR][CR]" % (COLOR2, COLOR1, kodi)
			msg += "[COLOR %s]Adult Content:[/COLOR] [COLOR %s]%s[/COLOR][CR]" % (COLOR2, COLOR1, adult)
			msg += "[COLOR %s]Description:[/COLOR] [COLOR %s]%s[/COLOR][CR]" % (COLOR2, COLOR1, description)
			wiz.TextBoxes(ADDONTITLE, msg)
		else: wiz.log("Invalid Build Name!")
	else: wiz.log("Build text file not working: %s" % WORKINGURL)

def OPEN_URL(url):
	req = urllib2.Request(url)
	req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
	response = urllib2.urlopen(req)
	link=response.read()
	response.close()
	return link

def workingURL(url):
	if url == 'http://': return False
	try: 
		req = urllib2.Request(url)
		req.add_header('User-Agent', USER_AGENT)
		response = urllib2.urlopen(req)
		response.close()
	except Exception, e:
		return e
	return True


###########################
###### Fresh Install ######
###########################

def freshStart(install=None, over=False):
	if KEEPTRAKT == 'true':
		traktit.autoUpdate('all')
		wiz.setS('traktlastsave', str(THREEDAYS))
	if KEEPREAL == 'true':
		debridit.autoUpdate('all')
		wiz.setS('debridlastsave', str(THREEDAYS))
	if KEEPLOGIN == 'true':
		loginit.autoUpdate('all')
		wiz.setS('loginlastsave', str(THREEDAYS))
	if over == True: yes_pressed = 1
	elif install == 'restore': yes_pressed=DIALOG.yesno(ADDONTITLE, "[COLOR %s]Do you wish to restore your" % COLOR2, "Kodi configuration to default settings", "Before installing the local backup?[/COLOR]", nolabel='[B]No, Cancel[/B]', yeslabel='[B]Continue[/B]')
	elif install: yes_pressed=DIALOG.yesno(ADDONTITLE, "[COLOR %s]Do you wish to restore your" % COLOR2, "Kodi configuration to default settings", "Before installing [COLOR %s]%s[/COLOR]?" % (COLOR1, install), nolabel='[B]No, Cancel[/B]', yeslabel='[B]Continue[/B]')
	else: yes_pressed=DIALOG.yesno(ADDONTITLE, "[COLOR %s]Do you wish to restore your" % COLOR2, "Kodi configuration to default settings?[/COLOR]", nolabel='[B]No, Cancel[/B]', yeslabel='[B]Continue[/B]')
	if yes_pressed:
		if not wiz.currSkin() in ['skin.confluence', 'skin.estuary']:
			skin = 'skin.confluence' if KODIV < 17 else 'skin.estuary'
			yes=DIALOG.yesno(ADDONTITLE, "[COLOR %s]The skin needs to be set back to [COLOR %s]%s[/COLOR]" % (COLOR2, COLOR1, skin[5:]), "Before doing a fresh install to clear all Texture files,", "Would you like us to do that for you?[/COLOR]", yeslabel="[B]Switch Skins[/B]", nolabel="[B]I'll Do It[/B]");
			if yes:
				skinSwitch.swapSkins(skin)
				x = 0
				xbmc.sleep(1000)
				while not xbmc.getCondVisibility("Window.isVisible(yesnodialog)") and x < 150:
					x += 1
					xbmc.sleep(200)
					wiz.ebi('SendAction(Select)')
				if xbmc.getCondVisibility("Window.isVisible(yesnodialog)"):
					wiz.ebi('SendClick(11)')
				else: wiz.LogNotify(ADDONTITLE,'Fresh Install: [COLOR red]Skin Swap Timed Out![/COLOR]'); return False
				xbmc.sleep(1000)
			else: wiz.LogNotify(ADDONTITLE,'Fresh Install: [COLOR red]Cancelled![/COLOR]'); return False
		if not wiz.currSkin() in ['skin.confluence', 'skin.estuary']:
			wiz.LogNotify(ADDONTITLE,'Fresh Install: [COLOR red]Skin Swap Failed![/COLOR]')
			return
		DP.create(ADDONTITLE,"[COLOR %s]Clearing all files and folders:" % COLOR2,'', 'Please Wait![/COLOR]')
		xbmcPath=os.path.abspath(HOME)
		total_files = sum([len(files) for r, d, files in os.walk(xbmcPath)]); del_file = 0
		for root, dirs, files in os.walk(xbmcPath,topdown=True):
			EXCLUDES.append('My_Builds')
			dirs[:] = [d for d in dirs if d not in EXCLUDES]
			for name in files:
				del_file += 1
				fold = root.split('\\')
				x = len(fold)-1
				if name == 'sources.xml' and fold[-1] == 'userdata' and KEEPSOURCES == 'true': wiz.log("Keep Sources: %s" % os.path.join(root, name))
				elif name == 'favourites.xml' and fold[-1] == 'userdata' and KEEPFAVS == 'true': wiz.log("Keep Favourites: %s" % os.path.join(root, name))
				elif name == 'profiles.xml' and fold[-1] == 'userdata' and KEEPPROFILES == 'true': wiz.log("Keep Profiles: %s" % os.path.join(root, name))
				elif name == 'advancedsettings.xml' and fold[-1] == 'userdata' and KEEPADVANCED == 'true':  wiz.log("Keep Advanced Settings: %s" % os.path.join(root, name))
				elif name in LOGFILES: wiz.log("Keep Log File: %s" % name)
				elif name.endswith('.db'):
					try:
						if name.endswith('.db') and name.startswith('Addon') and KODIV >= 17: wiz.log("Ignoring %s on v%s" % (name, KODIV))
						else: os.remove(os.path.join(root,name))
					except Exception, e: 
						wiz.log('Failed to delete, Purging DB')
						wiz.log("-> %s / %s" % (Exception, str(e)))
						wiz.purgeDb(os.path.join(root,name))
				else:
					DP.update(int(percentage(del_file, total_files)), '', '[COLOR %s]File: [/COLOR][COLOR %s]%s[/COLOR]' % (COLOR2, COLOR1, name), '')
					try: os.remove(os.path.join(root,name))
					except Exception, e: 
						wiz.log("Error removing %s" % os.path.join(root, name))
						wiz.log("-> %s / %s" % (Exception, str(e)))
			if DP.iscanceled(): 
				DP.close()
				wiz.LogNotify(ADDONTITLE, "Fresh Start Cancelled")
				return False
		for root, dirs, files in os.walk(xbmcPath,topdown=True):
			dirs[:] = [d for d in dirs if d not in EXCLUDES]
			for name in dirs:
				DP.update(100, '', 'Cleaning Up Empty Folder: [COLOR %s]%s[/COLOR]' % (COLOR1, name), '')
				if name not in ["Database","userdata","temp","addons","addon_data"]:
					shutil.rmtree(os.path.join(root,name),ignore_errors=True, onerror=None)
			if DP.iscanceled(): 
				DP.close()
				wiz.LogNotify(ADDONTITLE, "Fresh Start Cancelled")
				return False
		DP.close()
		wiz.clearS('build')
		if install == 'restore': 
			DIALOG.ok(ADDONTITLE, "[COLOR %s]Your current setup for kodi has been cleared!" % COLOR2, "Now we will install the local backup[/COLOR]")
		elif install: 
			DIALOG.ok(ADDONTITLE, "[COLOR %s]Your current setup for kodi has been cleared!" % COLOR2, "Now we will install: [COLOR %s]%s v%s[/COLOR][/COLOR]" % (COLOR1, install, wiz.checkBuild(install,'version')))
			buildWizard(install, 'normal')
		else:
			DIALOG.ok(ADDONTITLE, "[COLOR %s]The process is complete, you're now back to a fresh Kodi configuration with [COLOR %s]%s[/COLOR]" % (COLOR2, COLOR1, ADDONTITLE), "Kodi will now force close, Please relaunch Kodi.[/COLOR]")
			wiz.killxbmc()
	else: 
		if not install == 'restore': wiz.LogNotify(ADDONTITLE,'Fresh Install: [COLOR red]Cancelled![/COLOR]'); wiz.refresh()

#############################
###DELETE CACHE##############
####THANKS GUYS @ NaN #######
def clearCache():
	if DIALOG.yesno(ADDONTITLE, '[COLOR %s]Would you like to clear cache?[/COLOR]' % COLOR2, nolabel='[B]No, Cancel[/B]', yeslabel='[B]Clear Cache[/B]'):
		wiz.clearCache()
		clearThumb()

def totalClean():
	if DIALOG.yesno(ADDONTITLE, '[COLOR %s]Would you like to clear cache, packages and thumbnails?[/COLOR]' % COLOR2, nolabel='[B]Cancel Process[/B]',yeslabel='[B]Clean All[/B]'):
		wiz.clearCache('total')
		wiz.clearPackages('total')
		clearThumb('total')
		wiz.killxbmc()

def clearThumb(type=None):
	latest = wiz.latestDB('Textures')
	if not type == None: choice = 1
	else: choice = DIALOG.yesno(ADDONTITLE, '[COLOR %s]Would you like to delete the %s and Thumbnails folder?' % (COLOR2, latest), "They will repopulate on the next startup[/COLOR]", nolabel='[B]Don\'t Delete[/B]', yeslabel='[B]Delete Thumbs[/B]')
	if choice == 1:
		try: wiz.removeFile(os.join(DATABASE, latest))
		except: wiz.log('Failed to delete, Purging DB.'); wiz.purgeDb(latest)
		wiz.removeFolder(THUMBS)
		if not type == 'total': wiz.killxbmc()
	else: wiz.log('Clear thumbnames cancelled')

def purgeDb():
	DB = []; display = []
	for dirpath, dirnames, files in os.walk(HOME):
		for f in fnmatch.filter(files, '*.db'):
			if f != 'Thumbs.db':
				found = os.path.join(dirpath, f)
				DB.append(found)
				dir = found.replace('\\', '/').split('/')
				display.append('(%s) %s' % (dir[len(dir)-2], dir[len(dir)-1]))
	if KODIV >= 16: 
		choice = DIALOG.multiselect("[COLOR %s]Select DB File to Purge[/COLOR]" % COLOR2, display)
		if choice == None: wiz.LogNotify("Purge Database", "Cancelled")
		elif len(choice) == 0: wiz.LogNotify("Purge Database", "Cancelled")
		else: 
			for purge in choice: wiz.purgeDb(DB[purge])
	else:
		choice = DIALOG.select("[COLOR %s]Select DB File to Purge[/COLOR]" % COLOR2, display)
		if choice == -1: wiz.LogNotify("Purge Database", "Cancelled")
		else: wiz.purgeDb(DB[purge])

##########################
### DEVELOPER MENU #######
##########################
def testnotify():
	url = wiz.workingURL(NOTIFICATION)
	if url == True:
		link  = wiz.openURL(NOTIFICATION).replace('\r','').replace('\t','')
		id, msg = link.split('|||')
		notify.testNotification(msg)
	else: wiz.LogNotify(ADDONTITLE, "Invalid URL for Notification")

def testupdate():
	notify.updateWindow()

def testfirst():
	notify.firstRun()

def testinstaller():
	notify.apkInstaller('SPMC')

def BACKUPMENU():
		if HIDESPACERS == 'No': addFile('==============BackUp Options===============', '', themeit=THEME3)
		addFile('Full Backup'                    , 'full', icon=ICON, themeit=THEME1)
		addFile('Backup for Builds (Exc: Thumbnails, Databases)'                    , 'backb', icon=ICON, themeit=THEME1)
		addFile('Backup addon data'                    , 'backad', icon=ICON, themeit=THEME1)
		if HIDESPACERS == 'No': addFile('==============Restore Options===============', '', themeit=THEME3)
		addDir('Restore Full Backup'                    , 'refull', icon=ICON, themeit=THEME1)
		addDir('Restore Addon Data'                    , 'refull', icon=ICON, themeit=THEME1)
		if HIDESPACERS == 'No': addFile('==============Other Options===============', '', themeit=THEME3)
		addDir('Delete A Backup'                    , 'delbu', icon=ICON, themeit=THEME1)
		addFile('Delete All Backups'                    , 'delall', icon=ICON, themeit=THEME1)
		addFile('Select Backup Location'                    , 'settings', icon=ICON, themeit=THEME1)


###########################
## Making the Directory####
###########################

def addDir1(display, mode=None, name=None, url=None, menu=None, description=ADDONTITLE, overwrite=True, fanart=FANART, icon=ICON, themeit=None):
	u = sys.argv[0]
	if not mode == None: u += "?mode=%s" % urllib.quote_plus(mode)
	if not name == None: u += "&name="+urllib.quote_plus(name)
	if not url == None: u += "&url="+urllib.quote_plus(url)
	ok=True
	if themeit: display = themeit % display
	liz=xbmcgui.ListItem(display, iconImage="DefaultFolder.png", thumbnailImage=icon)
	liz.setInfo( type="Video", infoLabels={ "Title": display, "Plot": description} )
	liz.setProperty( "Fanart_Image", fanart )
	if not menu == None: liz.addContextMenuItems(menu, replaceItems=overwrite)
	ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=True)
	return ok

def addDir(display,mode,name=None,url=None,menu=None,overwrite=True,fanart=FANART,icon=ICON, themeit=None):
	u='%s?mode=%s' % (sys.argv[0], urllib.quote_plus(mode))
	if not name == None: u += "&name="+urllib.quote_plus(name)
	if not url == None: u += "&url="+urllib.quote_plus(url)
	ok=True
	if themeit: display = themeit % display
	liz=xbmcgui.ListItem(display, iconImage="DefaultFolder.png", thumbnailImage=icon)
	liz.setInfo( type="Video", infoLabels={ "Title": display, "Plot": ADDONTITLE} )
	liz.setProperty( "Fanart_Image", fanart )
	if not menu == None: liz.addContextMenuItems(menu, replaceItems=overwrite)
	ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=True)
	return ok

def addDir2(name,url,mode,iconimage):
		u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)+"&iconimage="+urllib.quote_plus(iconimage)
		ok=True
		liz=xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage=iconimage)
		liz.setInfo( type="Video", infoLabels={ "Title": name, "Plot": name } )
		ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=True)
		return ok

def addDir88(name,url,mode,iconimage,fanart,description,installRating):
		u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)+"&iconimage="+urllib.quote_plus(iconimage)+"&fanart="+urllib.quote_plus(fanart)+"&description="+urllib.quote_plus(description)+"&installRating="+urllib.quote_plus(installRating)
		ok=True
		liz=xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage=iconimage)
		liz.setInfo( type="Video", infoLabels={ "Title": name, "Plot": description, "Premiered": installRating  } )
		liz.setProperty( "Fanart_Image", fanart )
		ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=False)
		return ok

def addFile1(display, mode=None, name=None, url=None, menu=None, description=ADDONTITLE, overwrite=True, fanart=FANART, icon=ICON, themeit=None):
	u = sys.argv[0]
	if not mode == None: u += "?mode=%s" % urllib.quote_plus(mode)
	if not name == None: u += "&name="+urllib.quote_plus(name)
	if not url == None: u += "&url="+urllib.quote_plus(url)
	ok=True
	if themeit: display = themeit % display
	liz=xbmcgui.ListItem(display, iconImage="DefaultFolder.png", thumbnailImage=icon)
	liz.setInfo( type="Video", infoLabels={ "Title": display, "Plot": description} )
	liz.setProperty( "Fanart_Image", fanart )
	if not menu == None: liz.addContextMenuItems(menu, replaceItems=overwrite)
	ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=False)
	return ok

def addFILE(display,mode,name=None,url=None,menu=None,overwrite=True,fanart=FANART,icon=ICON,description=None, themeit=None):
	u='%s?mode=%s' % (sys.argv[0], urllib.quote_plus(mode))
	if not name == None: u += "&name="+urllib.quote_plus(name)
	if not url == None: u += "&url="+urllib.quote_plus(url)
	if not description == None: u += "&description="+urllib.quote_plus(description)
	ok=True
	if themeit: display = themeit % display
	liz=xbmcgui.ListItem(description, iconImage="DefaultFolder.png", thumbnailImage=icon)
	liz.setInfo( type="Video", infoLabels={ "Title": description, "Plot": ADDONTITLE} )
	liz.setProperty( "Fanart_Image", fanart )
	if not menu == None: liz.addContextMenuItems(menu, replaceItems=overwrite)
	ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=False)
	return ok

def addFile(display,mode,name=None,url=None,menu=None,overwrite=True,fanart=FANART,icon=ICON, themeit=None):
	u='%s?mode=%s' % (sys.argv[0], urllib.quote_plus(mode))
	if not name == None: u += "&name="+urllib.quote_plus(name)
	if not url == None: u += "&url="+urllib.quote_plus(url)
	ok=True
	if themeit: display = themeit % display
	liz=xbmcgui.ListItem(display, iconImage="DefaultFolder.png", thumbnailImage=icon)
	liz.setInfo( type="Video", infoLabels={ "Title": display, "Plot": ADDONTITLE} )
	liz.setProperty( "Fanart_Image", fanart )
	if not menu == None: liz.addContextMenuItems(menu, replaceItems=overwrite)
	ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=False)
	return ok

def addItem(name,url,mode,iconimage,fanart,description):
	u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)+"&fanart="+urllib.quote_plus(fanart)
	ok=True
	liz=xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage=iconimage)
	liz.setInfo( type="Video", infoLabels={ "Title": name } )
	liz.setProperty( "Fanart_Image", fanart )
	ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=False)
	return ok

def addDIR(name,url,mode,iconimage,fanart,description):
		u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)+"&iconimage="+urllib.quote_plus(iconimage)+"&fanart="+urllib.quote_plus(fanart)+"&description="+urllib.quote_plus(description)
		ok=True
		liz=xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage=iconimage)
		liz.setInfo( type="Video", infoLabels={ "Title": name, "Plot": description } )
		liz.setProperty( "Fanart_Image", fanart )
		if mode==90 :
			ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=False)
		else:
			ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=True)
		return ok


def get_params():
	param=[]
	paramstring=sys.argv[2]
	if len(paramstring)>=2:
		params=sys.argv[2]
		cleanedparams=params.replace('?','')
		if (params[len(params)-1]=='/'):
			params=params[0:len(params)-2]
		pairsofparams=cleanedparams.split('&')
		param={}
		for i in range(len(pairsofparams)):
			splitparams={}
			splitparams=pairsofparams[i].split('=')
			if (len(splitparams))==2:
				param[splitparams[0]]=splitparams[1]

		return param

params=get_params()
url=None
name=None
mode=None
iconimage=None
fanart=None
description=None

try:     mode=urllib.unquote_plus(params["mode"])
except:  pass
try:     name=urllib.unquote_plus(params["name"])
except:  pass
try:     url=urllib.unquote_plus(params["url"])
except:  pass
try:	 iconimage=urllib.unquote_plus(params["iconimage"])
except:	 pass
try:	 fanart=urllib.unquote_plus(params["fanart"])
except:	 pass
try:	 description=urllib.unquote_plus(params["description"])
except:	 pass
		
wiz.log('[ Version : \'%s\' ] [ Mode : \'%s\' ] [ Name : \'%s\' ] [ Url : \'%s\' ]' % (VERSION, mode if not mode == '' else None, name, url))
def Restore():

	for file in os.listdir(USB):
		if file.endswith(".zip"):
			url =  xbmc.translatePath(os.path.join(USB,file))
			addItem(file,url,'read',ICON,ICON,'')

def ListBackDel():
	addonfolder = xbmc.translatePath(os.path.join('special://','home'))
	for file in os.listdir(USB):
		if file.endswith(".zip"):
			url =  xbmc.translatePath(os.path.join(USB,file))
			addDIR(file,url,'dell',ICON,ICON,'')

def setView(content, viewType):
	#if content:
	#	xbmcplugin.setContent(int(sys.argv[1]), content)
	if wiz.getS('auto-view')=='true':
		wiz.ebi("Container.SetViewMode(%s)" % wiz.getS(viewType) )

if   mode==None             : index()

elif mode=='wizardupdate'   : wiz.wizardUpdate()
elif mode=='builds'         : buildMenu()
elif mode=='viewbuild'      : viewBuild(name)
elif mode=='buildinfo'      : buildInfo(name)
elif mode=='install'        : buildWizard(name, url)
elif mode=='theme'          : buildWizard(name, mode, url)

elif mode=='maint'          : maintMenu(name)
elif mode=='speed'          : speedMenu()
elif mode=='advancedsetting': advancedWindow()
elif mode=='autoadvanced'   : showAutoAdvanced(); wiz.refresh()
elif mode=='asciicheck'     : wiz.asciiCheck()
elif mode=='backupbuild'    : wiz.backUpOptions('build')
elif mode=='backupgui'      : wiz.backUpOptions('guifix')
elif mode=='backuptheme'    : wiz.backUpOptions('theme')
elif mode=='backupaddon'    : wiz.backUpOptions('addondata')
elif mode=='clearbackup'    : wiz.cleanupBackup()
elif mode=='convertpath'    : wiz.convertSpecial(HOME)
elif mode=='currentsettings': viewAdvanced()
elif mode=='fullclean'      : totalClean(); wiz.refresh()
elif mode=='clearcache'     : clearCache(); wiz.refresh()
elif mode=='clearpackages'  : wiz.clearPackages(); wiz.refresh()
elif mode=='clearcrash'     : wiz.clearCrash(); wiz.refresh()
elif mode=='clearthumb'     : clearThumb(); wiz.refresh()
elif mode=='checksources'   : wiz.checkSources(); wiz.refresh()
elif mode=='checkrepos'     : wiz.checkRepos(); wiz.refresh()
elif mode=='freshstart'     : freshStart()
elif mode=='forceupdate'    : wiz.forceUpdate()
elif mode=='forceclose'     : wiz.killxbmc()
elif mode=='forceskin'      : wiz.ebi("ReloadSkin()"); wiz.refresh()
elif mode=='hidepassword'   : wiz.hidePassword()
elif mode=='unhidepassword' : wiz.unhidePassword()
elif mode=='enableaddons'   : enableAddons()
elif mode=='toggleaddon'    : wiz.toggleAddon(name, url); wiz.refresh()
elif mode=='togglecache'    : toggleCache(name); wiz.refresh()
elif mode=='toggleadult'    : wiz.toggleAdult(); wiz.refresh()
elif mode=='changefeq'      : changeFeq(); wiz.refresh()
elif mode=='uploadlog'      : uploadLog.Main()
elif mode=='viewlog'        : viewLogFile()
elif mode=='viewwizlog'     : viewWizLogFile()
elif mode=='viewerrorlog'   : errorChecking()
elif mode=='clearwizlog'    : f = open(WIZLOG, 'w'); f.close(); wiz.LogNotify(ADDONTITLE, "Wizard Log Cleared!")
elif mode=='purgedb'        : purgeDb()
elif mode=='fixaddonupdate' : wiz.purgeDb(os.path.join(DATABASE, wiz.latestDB('Addons')))
elif mode=='removeaddons'   : removeAddonMenu()
elif mode=='removeaddon'    : removeAddon(name)
elif mode=='removeaddondata': removeAddonDataMenu()
elif mode=='removedata'     : removeAddonData(name)
elif mode=='resetaddon'     : total = wiz.cleanHouse(ADDONDATA, ignore=True); wiz.LogNotify(ADDONTITLE, "Addon_Data reset")
elif mode=='systeminfo'     : systemInfo()
elif mode=='restorezip'     : restoreit('build')
elif mode=='restoregui'     : restoreit('gui')
elif mode=='restoreaddon'   : restoreit('addondata')
elif mode=='restoreextzip'  : restoreextit('build')
elif mode=='restoreextgui'  : restoreextit('gui')
elif mode=='restoreextaddon': restoreextit('addondata')
elif mode=='writeadvanced'  : writeAdvanced(name)

elif mode=='apk1'			: apkMenu()
elif mode=='apkgame'        : APKGAME(url)
elif mode=='select'         : APKSELECT2(url)
elif mode=='grab'           : APKGRAB(name,url)
elif mode=='rom'            : romMenu(url)
elif mode=='apkscrape'      : APK()
elif mode=='apkshow'		: apkshowMenu(url)
elif mode=='apkkodi'        : apkkodiMenu()
elif mode=='intellaunch'	: iiNT3LiiLauncher()
elif mode=='intelselect'	: iiNT3LiiSelector(name,url,iconimage,fanart,description)
elif mode=='emurom'         : emuromMenu()
elif mode=='roms'           : romsMenu()
elif mode=='snes'			: snesMenu()
elif mode=='nes'            : nesMenu()
elif mode=='gen'            : genMenu()
elif mode=='atr'            : atrMenu()
elif mode=='n64'            : n64Menu()
elif mode=='tbg'            : tbgMenu()
elif mode=='nds'			: ndsMenu()
elif mode=='ps'				: psMenu()
elif mode=='apkinstall'     : apkInstaller(name, url,"None")
elif mode=='rominstall'     : INSTALLROM(name,url,)

elif mode=='youtube'        : youtubeMenu(url)
elif mode=='viewVideo'      : playVideo(url)

elif mode=='savedata'       : saveMenu()
elif mode=='togglesetting'  : wiz.setS(name, 'false' if wiz.getS(name) == 'true' else 'true'); wiz.refresh()

elif mode=='trakt'          : traktMenu()
elif mode=='savetrakt'      : traktit.traktIt('update',      name)
elif mode=='restoretrakt'   : traktit.traktIt('restore',     name)
elif mode=='addontrakt'     : traktit.traktIt('clearaddon',  name)
elif mode=='cleartrakt'     : traktit.clearSaved(name)
elif mode=='authtrakt'      : traktit.activateTrakt(name); wiz.refresh()
elif mode=='updatetrakt'    : traktit.autoUpdate('all')
elif mode=='importtrakt'    : traktit.importlist(name); wiz.refresh()

elif mode=='realdebrid'     : realMenu()
elif mode=='savedebrid'     : debridit.debridIt('update',      name)
elif mode=='restoredebrid'  : debridit.debridIt('restore',     name)
elif mode=='addondebrid'    : debridit.debridIt('clearaddon',  name)
elif mode=='cleardebrid'    : debridit.clearSaved(name)
elif mode=='authdebrid'     : debridit.activateDebrid(name); wiz.refresh()
elif mode=='updatedebrid'   : debridit.autoUpdate('all')
elif mode=='importdebrid'   : debridit.importlist(name); wiz.refresh()

elif mode=='addons'         : addonMenu()
elif mode=='addoninstall'   : addonInstaller(name)

elif mode=='contact'        : notify.contact(CONTACT)
elif mode=='settings'       : wiz.openS(name); wiz.refresh()
elif mode=='opensettings'   : id = eval(url.upper()+'ID')[name]['plugin']; addonid = wiz.addonId(id); addonid.openSettings(); wiz.refresh()

elif mode=='developer'      : developer()
elif mode=='converttext'    : wiz.convertText(name)
elif mode=='testnotify'     : testnotify()
elif mode=='bre'            : BACKUPMENU()
elif mode=='full'           : backuprestore.FullBackup()
elif mode=='backb'          : backuprestore.Backup()
elif mode=='backad'         : backuprestore.ADDON_DATA_BACKUP()
elif mode=='refull'         : Restore()
elif mode=='delbu'          : ListBackDel()
elif mode=='delall'         : backuprestore.DeleteAllBackups()
elif mode=='read'           : backuprestore.READ_ZIP(url)
elif mode=='dell'           : backuprestore.DeleteBackup(url)
elif mode=='testupdate'     : testupdate()
elif mode=='testfirst'      : testfirst()
if mode not in ['', 'togglesettings', 'settings', 'contact']: xbmcplugin.endOfDirectory(int(sys.argv[1]))
