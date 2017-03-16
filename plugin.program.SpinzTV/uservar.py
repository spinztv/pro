import os, xbmc, xbmcaddon
import base64

#########################################################
### User Edit Variables #################################
#########################################################
ADDON_ID       = xbmcaddon.Addon().getAddonInfo('id')
ADDONTITLE     = 'SpinzTV Wizard'
EXCLUDES       = [ADDON_ID, 'repository.SpinzTV', 'plugin.program.SpinzTV', 'script.module.beautifulsoup', 'script.module.beautifulsoup4', 'script.module.urlresolver', 'script.module.requests', 'script.module.addon.common', 'script.module.simplejson', 'script.module.buggalo', 'script.module.t0mm0.common']
# Text File with build info in it.
BUILDFILE      = 'http://stvmc.net/builds/wiztxt/spinzwizard1.txt'
# How often you would list it to check for build updates in days
# 0 being every startup of kodi
UPDATECHECK    = 0
# Text File with apk info in it.
APKFILE        = 'http://stvmc.net/APK/apktxts/SpinzTV-apk.txt'
# Text File with Youtube Videos urls.  Leave as 'http://' to ignore
YOUTUBETITLE   = ''
YOUTUBEFILE    = 'http://'
# Text File for addon installer.  Leave as 'http://' to ignore
ADDONFILE      = 'http://'
# Text File for advanced settings.  Leave as 'http://' to ignore
ADVANCEDFILE   = 'http://'

# Dont need to edit just here for icons stored locally
PATH           = xbmcaddon.Addon().getAddonInfo('path')
ART            = os.path.join(PATH, 'resources', 'art')

#########################################################
### THEMING MENU ITEMS ##################################
#########################################################
# If you want to use locally stored icons the place them in the Resources/Art/
# folder of the wizard then use os.path.join(ART, 'imagename.png')
# do not place quotes around os.path.join
# Example:  ICONMAINT     = os.path.join(ART, 'mainticon.png')
#           ICONSETTINGS  = 'http://aftermathwizard.net/repo/wizard/settings.png'
# Leave as http:// for default icon
ICONBUILDS     = 'http://stvmc.net/wizicons/buildsicon.png'
ICONMAINT      = 'http://stvmc.net/wizicons/mainticon.png'
ICONAPK        = 'http://stvmc.net/wizicons/apkicon.png'
ICONADDONS     = 'http://stvmc.net/wizicons/kodiicon.png'
ICONYOUTUBE    = 'http://'
ICONSAVE       = 'http://stvmc.net/wizicons/saveicon.png'
ICONTRAKT      = 'http://stvmc.net/wizicons/trakticon.png'
ICONREAL       = 'http://stvmc.net/wizicons/realicon.png'
ICONLOGIN      = 'http://stvmc.net/wizicons/buildsicon.png'
ICONCONTACT    = 'http://stvmc.net/wizicons/contacticon.png'
ICONSETTINGS   = 'http://stvmc.net/wizicons/settingsicon.png'
ICONSPINZ      = 'http://stvmc.net/wizicons/spinzicon.png'
ICONKODI       = 'http://stvmc.net/wizicons/kodiicon.png'
ICONSPMC       = 'http://stvmc.net/wizicons/kodiicon.png'
ICONGAMES      = 'http://stvmc.net/wizicons/gamesicon.png'
ICONMOVIES     = 'http://stvmc.net/wizicons/moviesicon.png'
ICONANDROID    = 'http://stvmc.net/wizicons/droidicon.png'
ICONSPEED      = 'http://stvmc.net/wizicons/speedicon.png'
ICONPRO        = 'http://stvmc.net/wizicons/proicon.png'
ICONADDONS     = 'http://stvmc.net/wizicons/spinzicon.png'
ICONYOUTUBE    = 'http://stvmc.net/wizicons/spinzicon.png'
ICONLOGIN      = 'http://stvmc.net/wizicons/spinzicon.png'
# Hide the ====== seperators 'Yes' or 'No'
HIDESPACERS    = 'No'
# Character used in seperator
SPACER         = '='

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
CONTACT        = 'Thank You For Choosing Spinz-TV\r\n\r\nFaceBook: https://www.facebook.com/groups/614286415341465/\r\n\r\nTwitter: @spinz_tv and @cspez85\r\n\r\nGoogle+: https://plus.google.com/u/0/communities/117878085291902485577'
#Images used for the contact window.  http:// for default icon and fanart
CONTACTICON    = 'http://'
CONTACTFANART  = 'http://'
#########################################################

#########################################################
### AUTO UPDATE #########################################
########## FOR THOSE WITH NO REPO #######################
# Enable Auto Update 'Yes' or 'No'
AUTOUPDATE     = 'No'
# Url to wizard version
WIZARDFILE     = ''
#########################################################

#########################################################
### AUTO INSTALL ########################################
########## REPO IF NOT INSTALLED ########################
# Enable Auto Install 'Yes' or 'No'
AUTOINSTALL    = 'yes'
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
ENABLE         = 'Yes'
# Url to notification file
NOTIFICATION   = 'http://stvmc.net/builds/wiztxt/notify.txt'
# Use either 'Text' or 'Image'
HEADERTYPE     = 'Text'
HEADERMESSAGE  = 'Spinz-TV'
# url to image if using Image 424x180
HEADERIMAGE    = ''
# Background for Notification Window
BACKGROUND     = 'http://stvmc.net/wizicons/notify.png'
#########################################################
