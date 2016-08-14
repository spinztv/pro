import os, xbmc, xbmcaddon
import base64
#########################################################
### User Edit Variables #################################
#########################################################
ADDON_ID       = xbmcaddon.Addon().getAddonInfo('id')
ADDONTITLE     = 'SpinzTV'
EXCLUDES       = [ADDON_ID, 'repository.SpinzTV']
# Text File with build info in it.
BUILDFILE      = base64.b64decode('aHR0cDovL3NwaW56dHYuY29tL3dpemFyZC9zcGluenR2d2l6YXJkLnR4dA==')
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