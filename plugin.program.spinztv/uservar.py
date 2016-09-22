import os, xbmc, xbmcaddon
import base64
#########################################################
### User Edit Variables #################################
#########################################################
ADDON_ID       = xbmcaddon.Addon().getAddonInfo('id')
ADDONTITLE     = 'SpinzTV'
EXCLUDES       = [ADDON_ID, 'repository.SpinzTV', 'plugin.video.spinztvwiz', 'plugin.video.spinz', 'script.xtcodes.installer']
# Text File with build info in it.
BUILDFILE      = base64.b64decode('aHR0cDovL3NwZXoudHYvc3Bpbnovd2l6YXJkdHh0L3NwaW56d2l6YXJkLnR4dA==')
# How often you would list it to check for build updates in days
# 0 being every startup of kodi
UPDATECHECK    = 0
# Speed Test File
SPEEDFILE    = base64.b64decode('aHR0cDovL3NwZXoudHYvc3Bpbnovc3BlZWQvc3BlZWR0ZXN0LnR4dA==')

# Text File with apk info in it.
APKSPINZFILE = base64.b64decode('aHR0cDovL3NwZXoudHYvc3BpbnovYXBrdHh0cy9TcGluemFway50eHQ=')
APKFILE      = base64.b64decode('aHR0cDovL3NwZXoudHYvc3BpbnovYXBrdHh0cy9TcGluelRWLWFway50eHQ=')
APKGAMEFILE  = base64.b64decode('aHR0cDovL3NwZXoudHYvc3BpbnovYXBrdHh0cy9TcGluelRWLWdhbWVhcGsudHh0')
APKVIDFILE   = base64.b64decode('aHR0cDovL3NwZXoudHYvc3BpbnovYXBrdHh0cy9TcGluelRWLXZpZGVvYXBrLnR4dA==')
APKSYSFILE   = base64.b64decode('aHR0cDovL3NwZXoudHYvc3BpbnovYXBrdHh0cy9TcGluelRWLWFuZHJvaWR0b29sc2Fway50eHQ=')
SNESFILE  = base64.b64decode('aHR0cDovL3NwZXoudHYvc3BpbnovZW11bGF0b3Itcm9tdHh0L1JPTVNUWFQvU05FUy50eHQ=')
EMUFILE   = base64.b64decode('aHR0cDovL3NwZXoudHYvc3BpbnovZW11bGF0b3Itcm9tdHh0L2VtdWxhdG9yLnR4dA==')
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
TGAFILE	  = base64.b64decode('aHR0cDovL3NwZXoudHYvc3BpbnovZW11bGF0b3Itcm9tdHh0L1JPTVNUWFQvVEdBLUIudHh0')
TGCFILE	  = base64.b64decode('aHR0cDovL3NwZXoudHYvc3BpbnovZW11bGF0b3Itcm9tdHh0L1JPTVNUWFQvVEdDLUUudHh0')
TGFFILE	  = base64.b64decode('aHR0cDovL3NwZXoudHYvc3BpbnovZW11bGF0b3Itcm9tdHh0L1JPTVNUWFQvVEdGLUkudHh0')
TGJFILE	  = base64.b64decode('aHR0cDovL3NwZXoudHYvc3BpbnovZW11bGF0b3Itcm9tdHh0L1JPTVNUWFQvVEdKLU0udHh0')
TGNFILE	  = base64.b64decode('aHR0cDovL3NwZXoudHYvc3BpbnovZW11bGF0b3Itcm9tdHh0L1JPTVNUWFQvVEdOLVEudHh0')
TGRFILE	  = base64.b64decode('aHR0cDovL3NwZXoudHYvc3BpbnovZW11bGF0b3Itcm9tdHh0L1JPTVNUWFQvVEdSLVUudHh0')
TGVFILE	  = base64.b64decode('aHR0cDovL3NwZXoudHYvc3BpbnovZW11bGF0b3Itcm9tdHh0L1JPTVNUWFQvVEdWLVoudHh0')
# Dont need to edit just here for icons stored locally
HOME           = xbmc.translatePath('special://home/')
PLUGIN         = os.path.join(HOME,     'addons',    ADDON_ID)
ART            = os.path.join(PLUGIN,   'resources', 'art')

#########################################################
### THEMING MENU ITEMS ##################################
#########################################################
# If you want to use locally stored icons the place them in the Resources/Art/
# folder of the wizard then use os.path.join(ART, 'imagename.png')
# do not place quotes around os.path.join
# Example:  ICONMAINT     = os.path.join(ART, 'mainticon.png')
#           ICONSETTINGS  = os.path.join(ART, 'settingsicon.png')
# Leave as http:// for default icon
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

# Hide the ====== seperators 'Yes' or 'No'
HIDESPACERS    = 'No'

# You can edit these however you want, just make sure that you have a %s in each of the
# THEME's so it grabs the text from the menu item
COLOR1         = 'deepskyblue'
COLOR2         = 'white'
# Primary menu items   / %s is the menu item and is required
THEME1         = '[COLOR '+COLOR1+']%s[/COLOR]'
# Build Names          / %s is the menu item and is required
THEME2         = '[COLOR '+COLOR2+']%s[/COLOR]'
# Alternate items      / %s is the menu item and is required
THEME3         = '[COLOR '+COLOR1+']%s[/COLOR]'
# Current Build Header / %s is the menu item and is required
THEME4         = '[COLOR '+COLOR1+']Current Build:[/COLOR] [COLOR '+COLOR2+']%s[/COLOR]'
# Current Theme Header / %s is the menu item and is required
THEME5         = '[COLOR '+COLOR1+']Current Theme:[/COLOR] [COLOR '+COLOR2+']%s[/COLOR]'

# Message for Contact Page
# Enable 'Contact' menu item 'Yes' hide or 'No' dont hide
HIDECONTACT    = 'No'
# You can add \n to do line breaks
CONTACT        = 'Thank you for choosing SpinzTV.\r\n\r\nContact us on facebook at http://facebook.com/groups/spinztv\r\n\r\nWebsite: www.spinztv.com'
#########################################################

#########################################################
### AUTO UPDATE #########################################
########## FOR THOSE WITH NO REPO #######################
# Enable Auto Update 'Yes' or 'No'
AUTOUPDATE     = 'No'
# Url to wizard version
WIZARDFILE     = 'http://'
#########################################################

#########################################################
### AUTO INSTALL ########################################
########## REPO IF NOT INSTALLED ########################
# Enable Auto Install 'Yes' or 'No'
AUTOINSTALL    = 'Yes'
# Addon ID for the repository
REPOID         = 'repository.SpinzTV'
# Url to Addons.xml file in your repo folder(this is so we can get the latest version)
REPOADDONXML   = base64.b64decode('aHR0cDovL3Jhdy5naXRodWIuY29tL3NwaW56dHYvcHJvL21hc3Rlci8vX3JlcG8vYWRkb25zLnhtbA==')
# Url to folder zip is located in
REPOZIPURL     = base64.b64decode('aHR0cDovL3Jhdy5naXRodWIuY29tL3NwaW56dHYvcHJvL21hc3Rlci8vX3JlcG8vcmVwb3NpdG9yeS5TcGluelRWLw==')
#########################################################

#########################################################
### NOTIFICATION WINDOW##################################
#########################################################
# Enable Notification screen Yes or No
ENABLE         = 'No'
# Url to notification file
NOTIFICATION   = ''
# Use either 'Text' or 'Image'
HEADERTYPE     = ''
# Font size of header
FONTHEADER     = ''
HEADERMESSAGE  = ''
# url to image if using Image 424x180
HEADERIMAGE    = ''
# Font for Notification Window
FONTSETTINGS   = ''
# Background for Notification Window
BACKGROUND     = ''
#########################################################