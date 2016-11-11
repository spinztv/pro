import xbmc, xbmcaddon, xbmcgui, xbmcplugin, os, sys, xbmcvfs, glob
import shutil
import urllib2,urllib
import re
import base64
from datetime import date, datetime, timedelta
from resources.libs import extract, downloader, notify, debridit, traktit, skinSwitch, uploadLog, wizard as wiz

ADDON_ID       = xbmcaddon.Addon().getAddonInfo('id')
ADDONTITLE     = 'SpinzTV'
ADDON          = wiz.addonId(ADDON_ID)
VERSION        = wiz.addonInfo(ADDON_ID,'version')
ADDONPATH      = wiz.addonInfo(ADDON_ID,'path')
ADDONID        = wiz.addonInfo(ADDON_ID,'id')
DIALOG         = xbmcgui.Dialog()
DP             = xbmcgui.DialogProgress()
HOME           = xbmc.translatePath('special://home/')
PROFILE        = xbmc.translatePath('special://profile/')
KODIHOME       = xbmc.translatePath('special://xbmc/')
ADDONS         = os.path.join(HOME,     'addons')
KODIADDONS     = os.path.join(KODIHOME, 'addons')
USERDATA       = os.path.join(HOME,     'userdata')
PLUGIN         = os.path.join(ADDONS,   ADDON_ID)
PACKAGES       = os.path.join(ADDONS,   'packages')
ADDONDATA      = os.path.join(USERDATA, 'addon_data', ADDON_ID)
FANART         = os.path.join(PLUGIN,   'fanart.jpg')
ICON           = os.path.join(PLUGIN,   'icon.png')
ART            = os.path.join(PLUGIN,   'resources', 'art')
SKIN           = xbmc.getSkinDir()
DEFAULTSKIN    = wiz.getS('defaultskin')
DEFAULTNAME    = wiz.getS('defaultskinname')
DEFAULTIGNORE  = wiz.getS('defaultskinignore')
BUILDNAME      = wiz.getS('buildname')
BUILDVERSION   = wiz.getS('buildversion')
BUILDLATEST    = wiz.getS('latestversion')
BUILDCHECK     = wiz.getS('lastbuildcheck')
DISABLEUPDATE  = wiz.getS('disableupdate')
AUTOCLEANUP    = wiz.getS('autoclean')
AUTOCACHE      = wiz.getS('clearcache')
AUTOPACKAGES   = wiz.getS('clearpackages')
AUTOTHUMBS     = wiz.getS('clearthumbs')
AUTOFEQ        = wiz.getS('autocleanfeq')
AUTODELAY      = wiz.getS('delayautoclean')
AUTONEXTRUN    = wiz.getS('nextautocleanup')
TRAKTSAVE      = wiz.getS('traktlastsave')
REALSAVE       = wiz.getS('debridlastsave')
KEEPTRAKT      = wiz.getS('keeptrakt')
KEEPREAL       = wiz.getS('keepdebrid')
KEEPLOGIN      = wiz.getS('keeplogin')
INSTALLED      = wiz.getS('installed')
EXTRACT        = wiz.getS('extract')
EXTERROR       = wiz.getS('errors')
NOTIFY         = wiz.getS('notify')
NOTEDISMISS    = wiz.getS('notedismiss')
NOTEID         = wiz.getS('noteid')
BACKUPLOCATION = ADDON.getSetting('path') if not ADDON.getSetting('path') == '' else 'special://home/'
MYBUILDS       = os.path.join(BACKUPLOCATION, 'My_Builds', '')
NOTEID         = 0 if NOTEID == "" else int(NOTEID)
AUTOFEQ        = int(AUTOFEQ) if AUTOFEQ.isdigit() else 0
TODAY          = date.today()
TOMORROW       = TODAY + timedelta(days=1)
TWODAYS        = TODAY + timedelta(days=2)
THREEDAYS      = TODAY + timedelta(days=3)
ONEWEEK        = TODAY + timedelta(days=7)
KODIV          = float(xbmc.getInfoLabel("System.BuildVersion")[:4])
EXCLUDES       = [ADDON_ID, 'repository.SpinzTV', 'plugin.video.spinztvwiz', 'plugin.video.spinz', 'script.xtcodes.installer']
BUILDFILE      = base64.b64decode('aHR0cDovL3NwZXoudHYvc3Bpbnovd2l6YXJkdHh0L3NwaW56d2l6YXJkMS50eHQ=')
UPDATECHECK    = 0
NEXTCHECK      = TODAY + timedelta(days=UPDATECHECK)
# Url to notification file
NOTIFICATION   = ''
# Enable Notification screen Yes or No
ENABLE         = 'No'
HEADERMESSAGE  = ''
# Enable Auto Update 'Yes' or 'No'
AUTOUPDATE     = 'No'
# Url to wizard version
WIZARDFILE     = 'http://'
# Enable Auto Install 'Yes' or 'No'
AUTOINSTALL    = 'Yes'
# Addon ID for the repository
REPOID         = 'repository.SpinzTV'
# Url to Addons.xml file in your repo folder(this is so we can get the latest version)
REPOADDONXML   = base64.b64decode('aHR0cDovL3Jhdy5naXRodWIuY29tL3NwaW56dHYvcHJvL21hc3Rlci8vX3JlcG8vYWRkb25zLnhtbA==')
# Url to folder zip is located in
REPOZIPURL     = base64.b64decode('aHR0cDovL3Jhdy5naXRodWIuY29tL3NwaW56dHYvcHJvL21hc3Rlci8vX3JlcG8vcmVwb3NpdG9yeS5TcGluelRWLw==')
WORKING        = True if wiz.workingURL(BUILDFILE) == True else False
FAILED         = False

###########################
#### Check Updates   ######
###########################
def checkUpdate():
	BUILDNAME      = wiz.getS('buildname')
	BUILDVERSION   = wiz.getS('buildversion')
	link           = wiz.openURL(BUILDFILE).replace('\n','').replace('\r','').replace('\t','')
	match          = re.compile('name="%s".+?ersion="(.+?)"' % BUILDNAME).findall(link)
	if len(match) > 0:
		version = match[0]
		wiz.setS('latestversion', version)
		if version > BUILDVERSION:
			if DISABLEUPDATE == 'false':
				wiz.log("[Check Updates] [Installed Version: %s] [Current Version: %s] Opening Update Window" % (BUILDVERSION, version), xbmc.LOGNOTICE)
				notify.updateWindow()
			else: wiz.log("[Check Updates] [Installed Version: %s] [Current Version: %s] Update Window Disabled" % (BUILDVERSION, version), xbmc.LOGNOTICE)
		else: wiz.log("[Check Updates] [Installed Version: %s] [Current Version: %s]" % (BUILDVERSION, version), xbmc.LOGNOTICE)
	else: wiz.log("[Check Updates] ERROR: Unable to find build version in build text file", xbmc.LOGERROR)

def checkSkin():
	wiz.log("[Build Check] Invalid Skin Check Start")
	DEFAULTSKIN   = wiz.getS('defaultskin')
	DEFAULTNAME   = wiz.getS('defaultskinname')
	DEFAULTIGNORE = wiz.getS('defaultskinignore')
	gotoskin = False
	if not DEFAULTSKIN == '':
		if os.path.exists(os.path.join(ADDONS, DEFAULTSKIN)):
			if DIALOG.yesno(ADDONTITLE, "[COLOR %s]It seems that the skin has been set back to [COLOR %s]%s[/COLOR]" % (COLOR2, COLOR1, SKIN[5:].title()), "Would you like to set the skin back to:[/COLOR]", '[COLOR %s]%s[/COLOR]' % (COLOR1, DEFAULTNAME)):
				gotoskin = DEFAULTSKIN
				gotoname = DEFAULTNAME
			else: wiz.log("Skin was not reset", xbmc.LOGNOTICE); wiz.setS('defaultskinignore', 'true'); gotoskin = False
		else: wiz.setS('defaultskin', ''); wiz.setS('defaultskinname', ''); DEFAULTSKIN = ''; DEFAULTNAME = ''
	if DEFAULTSKIN == '':
		skinname = []
		skinlist = []
		for folder in glob.glob(os.path.join(ADDONS, 'skin.*/')):
			xml = "%s/addon.xml" % folder
			if os.path.exists(xml):
				f  = open(xml,mode='r'); g = f.read().replace('\n','').replace('\r','').replace('\t',''); f.close();
				match = re.compile('<addon.+?id="(.+?)".+?>').findall(g)
				match2 = re.compile('<addon.+?name="(.+?)".+?>').findall(g)
				wiz.log("%s: %s" % (folder, str(match[0])), xbmc.LOGNOTICE)
				if len(match) > 0: skinlist.append(str(match[0])); skinname.append(str(match2[0]))
				else: wiz.log("ID not found for %s" % folder, xbmc.LOGNOTICE)
			else: wiz.log("ID not found for %s" % folder, xbmc.LOGNOTICE)
		if len(skinlist) > 0:
			if len(skinlist) > 1:
				if DIALOG.yesno(ADDONTITLE, "[COLOR %s]It seems that the skin has been set back to [COLOR %s]%s[/COLOR]" % (COLOR2, COLOR1, SKIN[5:].title()), "Would you like to view a list of avaliable skins?[/COLOR]"):
					choice = DIALOG.select("Select skin to switch to!", skinname)
					if choice == -1: wiz.log("Skin was not reset", xbmc.LOGNOTICE); wiz.setS('defaultskinignore', 'true')
					else: 
						gotoskin = skinlist[choice]
						gotoname = skinname[choice]
				else: wiz.log("Skin was not reset", xbmc.LOGNOTICE); wiz.setS('defaultskinignore', 'true')
			else:
				if DIALOG.yesno(ADDONTITLE, "[COLOR %s]It seems that the skin has been set back to [COLOR %s]%s[/COLOR]" % (COLOR2, COLOR1, SKIN[5:].title()), "Would you like to set the skin back to:[/COLOR]", '[COLOR %s]%s[/COLOR]' % (COLOR1, skinname[0])):
					gotoskin = skinlist[0]
					gotoname = skinname[0]
				else: wiz.log("Skin was not reset", xbmc.LOGNOTICE); wiz.setS('defaultskinignore', 'true')
		else: wiz.log("No skins found in addons folder.", xbmc.LOGNOTICE); wiz.setS('defaultskinignore', 'true'); gotoskin = False
	if gotoskin:
		skinSwitch.swapSkins(gotoskin)
		x = 0
		xbmc.sleep(1000)
		while not xbmc.getCondVisibility("Window.isVisible(yesnodialog)") and x < 150:
			x += 1
			xbmc.sleep(200)

		if xbmc.getCondVisibility("Window.isVisible(yesnodialog)"):
			wiz.ebi('SendClick(11)')
			wiz.lookandFeelData('restore')
		else: wiz.LogNotify(ADDONTITLE,'[COLOR red]Skin Swap Timed Out![/COLOR]')
	wiz.log("[Build Check] Invalid Skin Check End", xbmc.LOGNOTICE)

while xbmc.Player().isPlayingVideo():
	xbmc.sleep(1000)

wiz.log("[Path Check] Started", xbmc.LOGNOTICE)
path = os.path.split(ADDONPATH)
if not ADDONID == path[1]: DIALOG.ok(ADDONTITLE, '[COLOR %s]Please make sure that the plugin folder is the same as the ADDON_ID.[/COLOR]' % COLOR2, '[COLOR %s]Plugin ID:[/COLOR] [COLOR %s]%s[/COLOR]' % (COLOR2, COLOR1, ADDONID), '[COLOR %s]Plugin Folder:[/COLOR] [COLOR %s]%s[/COLOR]' % (COLOR2, COLOR1, path)); wiz.log("[Path Check] ADDON_ID and plugin folder doesnt match. %s / %s " % (ADDONID, path))
else: wiz.log("[Path Check] Good!", xbmc.LOGNOTICE)

if KODIADDONS in ADDONPATH:
	wiz.log("Copying path to addons dir", xbmc.LOGNOTICE)
	if not os.path.exists(ADDONS): os.makedirs(ADDONS)
	newpath = xbmc.translatePath(os.path.join('special://home/addons/', ADDONID))
	if os.path.exists(newpath):
		wiz.log("Folder already exists, cleaning House", xbmc.LOGNOTICE)
		wiz.cleanHouse(newpath)
		wiz.removeFolder(newpath)
	try:
		wiz.copytree(ADDONPATH, newpath)
	except Exception, e:
		pass
	wiz.forceUpdate(True)

BACKUPLOCATION = xbmc.translatePath(BACKUPLOCATION)
MYBUILDS       = os.path.join(BACKUPLOCATION, 'My_Builds')
if not os.path.exists(BACKUPLOCATION): os.makedirs(BACKUPLOCATION)
if not os.path.exists(MYBUILDS): os.makedirs(MYBUILDS)	

wiz.log("[Auto Install Repo] Started", xbmc.LOGNOTICE)
if AUTOINSTALL == 'Yes' and not os.path.exists(os.path.join(ADDONS, REPOID)):
	workingxml = wiz.workingURL(REPOADDONXML)
	if workingxml == True:
		link    = wiz.openURL(REPOADDONXML).replace('\n','').replace('\r','').replace('\t','')
		match   = re.compile('<addon.+?id="%s".+?ersion="(.+?)".+?>' % REPOID).findall(link)
		if len(match) == 0:
			wiz.log("Invalid URL for Repo Zip", xbmc.LOGERROR)
		else:
			installzip = '%s-%s.zip' % (REPOID, match[0])
			workingrepo = wiz.workingURL(REPOZIPURL+installzip)
			if workingrepo == True:
				DP.create(ADDONTITLE,'Downloading Repo...','', 'Please Wait')
				if not os.path.exists(PACKAGES): os.makedirs(PACKAGES)
				lib=os.path.join(PACKAGES, installzip)
				try: os.remove(lib)
				except: pass
				downloader.download(REPOZIPURL+installzip,lib, DP)
				extract.all(lib, ADDONS, DP)
				f = open(os.path.join(ADDONS, REPOID, 'addon.xml'), mode='r').read()
				match = re.compile('<addon.+?id="%s".+?ame="(.+?)".+?>' % REPOID).findall(f)
				wiz.LogNotify(match[0], "Add-on updated", icon=os.path.join(ADDONS, REPOID, 'icon.png'))
				DP.close()
				xbmc.sleep(500)
				wiz.forceUpdate(True)
				wiz.log("[Auto Install Repo] Successfully Installed", xbmc.LOGNOTICE)
			else: 
				wiz.LogNotify("Repo Install Error", "Invalid url for zip!")
				wiz.log("[Auto Install Repo] Was unable to create a working url for repository. %s" % workingrepo, xbmc.LOGERROR)
	else: 
		wiz.LogNotify("Repo Install Error", "Invalid addon.xml file!")
		wiz.log("[Auto Install Repo] Unable to read the addon.xml file.", xbmc.LOGERROR)
elif not AUTOINSTALL == 'Yes': wiz.log("[Auto Install Repo] Not Enabled", xbmc.LOGNOTICE)
elif os.path.exists(os.path.join(ADDONS, REPOID)): wiz.log("[Auto Install Repo] Repository already installed")

wiz.log("[Auto Update Wizard] Started", xbmc.LOGNOTICE)
if AUTOUPDATE == 'Yes':
	wiz.wizardUpdate('startup')
else: wiz.log("[Auto Update Wizard] Not Enabled", xbmc.LOGNOTICE)

wiz.log("[Notifications] Started", xbmc.LOGNOTICE)
if ENABLE == 'Yes':
	if not NOTIFY == 'true':
		url = wiz.workingURL(NOTIFICATION)
		if url == True:
			link  = wiz.openURL(NOTIFICATION).replace('\r','').replace('\t','')
			id, msg = link.split('|||')
			if int(id) == int(NOTEID):
				if NOTEDISMISS == 'false':
					notify.notification(msg=msg)
				else: wiz.log("[Notifications] id[%s] Dismissed" % int(id), xbmc.LOGNOTICE)
			elif int(id) > int(NOTEID):
				wiz.log("[Notifications] id: %s" % str(int(id)), xbmc.LOGNOTICE)
				wiz.setS('noteid', str(int(id)))
				wiz.setS('notedismiss', 'false')
				notify.notification(msg=msg)
				wiz.log("[Notifications] Complete", xbmc.LOGNOTICE)
		else: wiz.log("[Notifications] URL(%s): %s" % (NOTIFICATION, url), xbmc.LOGNOTICE)
	else: wiz.log("[Notifications] Turned Off", xbmc.LOGNOTICE)
else: wiz.log("[Notifications] Not Enabled", xbmc.LOGNOTICE)

wiz.log("[Installed Check] Started", xbmc.LOGNOTICE)
if INSTALLED == 'true':
	if KODIV >= 17:
		wiz.kodi17Fix()
		if SKIN in ['skin.confluence', 'skin.estuary']:
			checkSkin()
		FAILED = True
	elif not EXTRACT == '100':
		wiz.log("[Installed Check] Build was extracted %s/100 with [ERRORS: %s]" % (EXTRACT, EXTERROR), xbmc.LOGNOTICE)
		yes=DIALOG.yesno(ADDONTITLE, '[COLOR %s]%s[/COLOR] [COLOR %s]was not installed correctly!' % (COLOR1, COLOR2, BUILDNAME), 'Installed: [COLOR %s]%s[/COLOR] / Error Count: [COLOR %s]%s[/COLOR]' % (COLOR1, EXTRACT, COLOR1, EXTERROR), 'Would you like to try again?[/COLOR]', nolabel='[B]No Thanks![/B]', yeslabel='[B]Retry Install[/B]')
		wiz.clearS('build')
		FAILED = True
		if yes: 
			wiz.ebi("PlayMedia(plugin://%s/?mode=install&name=%s&url=fresh)" % (ADDON_ID, urllib.quote_plus(BUILDNAME)))
			wiz.log("[Installed Check] Fresh Install Re-activated", xbmc.LOGNOTICE)
		else: wiz.log("[Installed Check] Reinstall Ignored")
	elif SKIN in ['skin.confluence', 'skin.estuary']:
		wiz.log("[Installed Check] Incorrect skin: %s" % SKIN, xbmc.LOGNOTICE)
		gui = wiz.checkBuild(BUILDNAME, 'gui')
		FAILED = True
		if gui == 'http://':
			wiz.log("[Installed Check] Guifix was set to http://", xbmc.LOGNOTICE)
			DIALOG.ok(ADDONTITLE, "[COLOR %s]It looks like the skin settings was not applied to the build." % COLOR2, "Sadly no gui fix was attatched to the build", "You will need to reinstall the build and make sure to do a force close[/COLOR]")
		elif wiz.workingURL(gui):
			yes=DIALOG.yesno(ADDONTITLE, '%s was not installed correctly!' % BUILDNAME, 'It looks like the skin settings was not applied to the build.', 'Would you like to apply the GuiFix?', nolabel='[B]No, Cancel[/B]', yeslabel='[B]Apply Fix[/B]')
			if yes: wiz.ebi("PlayMedia(plugin://%s/?mode=install&name=%s&url=gui)" % (ADDON_ID, urllib.quote_plus(BUILDNAME))); wiz.log("[Installed Check] Guifix attempting to install")
			else: wiz.log('[Installed Check] Guifix url working but cancelled: %s' % gui, xbmc.LOGNOTICE)
		else:
			DIALOG.ok(ADDONTITLE, "[COLOR %s]It looks like the skin settings was not applied to the build." % COLOR2, "Sadly no gui fix was attatched to the build", "You will need to reinstall the build and make sure to do a force close[/COLOR]")
			wiz.log('[Installed Check] Guifix url not working: %s' % gui, xbmc.LOGNOTICE)
	else:
		wiz.log('[Installed Check] Install seems to be completed correctly', xbmc.LOGNOTICE)
	if KEEPTRAKT == 'true': traktit.traktIt('restore', 'all'); wiz.log('[Installed Check] Restoring Trakt Data', xbmc.LOGNOTICE)
	if KEEPREAL  == 'true': debridit.debridIt('restore', 'all'); wiz.log('[Installed Check] Restoring Real Debrid Data', xbmc.LOGNOTICE)
	if KEEPLOGIN == 'true': loginit.loginIt('restore', 'all'); wiz.log('[Installed Check] Restoring Login Data', xbmc.LOGNOTICE)
	wiz.clearS('install')
else: wiz.log("[Installed Check] Not Enabled", xbmc.LOGNOTICE)

if FAILED == False:
	wiz.log("[Build Check] Started", xbmc.LOGNOTICE)
	if not WORKING:
		wiz.log("[Build Check] Not a valid URL for Build File: %s" % BUILDFILE, xbmc.LOGNOTICE)
	elif BUILDCHECK == '' and BUILDNAME == '':
		wiz.log("[Build Check] First Run", xbmc.LOGNOTICE)
		notify.firstRun()
		wiz.setS('lastbuildcheck', str(NEXTCHECK))
	elif not BUILDNAME == '':
		wiz.log("[Build Check] Build Installed", xbmc.LOGNOTICE)
		if SKIN in ['skin.confluence', 'skin.estuary'] and not DEFAULTIGNORE == 'true':
			checkSkin()
			wiz.log("[Build Check] Build Installed: Checking Updates", xbmc.LOGNOTICE)
			wiz.setS('lastbuildcheck', str(NEXTCHECK))
			checkUpdate()
		elif BUILDCHECK <= str(TODAY):
			wiz.log("[Build Check] Build Installed: Checking Updates", xbmc.LOGNOTICE)
			wiz.setS('lastbuildcheck', str(NEXTCHECK))
			checkUpdate()
		else: 
			wiz.log("[Build Check] Build Installed: Next check isnt until: %s / TODAY is: %s" % (BUILDCHECK, str(TODAY)), xbmc.LOGNOTICE)

wiz.log("[Trakt Data] Started", xbmc.LOGNOTICE)
if KEEPTRAKT == 'true':
	if TRAKTSAVE <= str(TODAY):
		wiz.log("[Trakt Data] Saving all Data", xbmc.LOGNOTICE)
		traktit.autoUpdate('all')
		wiz.setS('traktlastsave', str(THREEDAYS))
	else: 
		wiz.log("[Trakt Data] Next Auto Save isnt until: %s / TODAY is: %s" % (TRAKTSAVE, str(TODAY)), xbmc.LOGNOTICE)
else: wiz.log("[Trakt Data] Not Enabled", xbmc.LOGNOTICE)

wiz.log("[Real Debrid Data] Started", xbmc.LOGNOTICE)
if KEEPREAL == 'true':
	if REALSAVE <= str(TODAY):
		wiz.log("[Real Debrid Data] Saving all Data", xbmc.LOGNOTICE)
		debridit.autoUpdate('all')
		wiz.setS('debridlastsave', str(THREEDAYS))
	else: 
		wiz.log("[Real Debrid Data] Next Auto Save isnt until: %s / TODAY is: %s" % (REALSAVE, str(TODAY)), xbmc.LOGNOTICE)
else: wiz.log("[Real Debrid Data] Not Enabled", xbmc.LOGNOTICE)

wiz.log("[Login Data] Started", xbmc.LOGNOTICE)
if AUTOCLEANUP == 'true':
	service = False
	days = [TODAY, TOMORROW, THREEDAYS, ONEWEEK]
	feq = int(float(AUTOFEQ))
	if AUTONEXTRUN <= str(TODAY) or feq == 0:
		service = True
		next_run = days[feq]
		wiz.setS('nextautocleanup', str(next_run))
	else: wiz.log("[Auto Clean Up] Next Clean Up %s" % AUTONEXTRUN, xbmc.LOGNOTICE)
	if service == True:
		if AUTOCACHE == 'true': wiz.log('[Auto Clean Up] Cache: On', xbmc.LOGNOTICE); wiz.clearCache()
		else: wiz.log('[Auto Clean Up] Cache: Off', xbmc.LOGNOTICE)
		if AUTOTHUMBS == 'true': wiz.log('[Auto Clean Up] Old Thumbs: On', xbmc.LOGNOTICE); wiz.oldThumbs()
		else: wiz.log('[Auto Clean Up] Old Thumbs: Off', xbmc.LOGNOTICE)
		if AUTOPACKAGES == 'true': wiz.log('[Auto Clean Up] Packages: On', xbmc.LOGNOTICE); wiz.clearPackagesStartup()
		else: wiz.log('[Auto Clean Up] Packages: Off', xbmc.LOGNOTICE)
else: wiz.log('[Auto Clean Up] Turned off', xbmc.LOGNOTICE)