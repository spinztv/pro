import xbmc, xbmcaddon, xbmcgui, xbmcplugin,os,sys
import shutil
import urllib2,urllib
import re
import time
import plugintools
import zipfile
import ntpath
import base64
import uservar
from os import listdir
from os.path import isfile, join
from shutil import copyfile
from resources.libs import extract, downloader, notify, debridit, traktit, skinSwitch, uploadLog, wizard as wiz

dp           =  xbmcgui.DialogProgress()
AddonTitle= uservar.ADDONTITLE
AddonID = uservar.ADDON_ID
selfAddon = xbmcaddon.Addon(id=AddonID)
backupfull = selfAddon.getSetting('backup_database')
backupaddons = selfAddon.getSetting('backup_addon_data')
PACKAGES = xbmc.translatePath(os.path.join('special://home/addons/' + 'packages'))
dialog = xbmcgui.Dialog()  
ICON = xbmc.translatePath(os.path.join('special://home/addons/' + AddonID, 'icon.png'))
mastercopy   =  selfAddon.getSetting('mastercopy')
HOME         =  xbmc.translatePath('special://home/')
USERDATA     =  xbmc.translatePath(os.path.join('special://home/userdata',''))
zip = plugintools.get_setting("zip")
USB          =  xbmc.translatePath(os.path.join(zip))
HOME         =  xbmc.translatePath('special://home/')
EXCLUDES_FOLDER     =  xbmc.translatePath(os.path.join(USERDATA,'BACKUP'))
ADDON_DATA   =  xbmc.translatePath(os.path.join(USERDATA,'addon_data'))

def _get_keyboard( default="", heading="", hidden=False ):
    """ shows a keyboard and returns a value """
    keyboard = xbmc.Keyboard( default, heading, hidden )
    keyboard.doModal()
    if ( keyboard.isConfirmed() ):
        return unicode( keyboard.getText(), "utf-8" )
    return default

def Backup():
    guisuccess=1
    if not os.path.exists(USB):
        os.makedirs(USB)
    if os.path.exists(PACKAGES):
        shutil.rmtree(PACKAGES)
    vq = _get_keyboard( heading="Enter a name for this backup" )
    if ( not vq ): return False, 0
    title = urllib.quote_plus(vq)
    backup_zip = xbmc.translatePath(os.path.join(USB,title+'.zip'))
    exclude_dirs =  ['backupdir','cache', 'Thumbnails','temp','Databases']
    exclude_files = ["spmc.log","spmc.old.log","xbmc.log","xbmc.old.log","kodi.log","kodi.old.log","Textures13.db"]
    message_header = "Creating full backup..."
    message_header2 = "Creating full backup..."
    message1 = "Archiving..."
    message2 = ""
    message3 = "Please Wait"
    FIX_SPECIAL(USERDATA)
    ARCHIVE_CB(HOME, backup_zip, message_header2, message1, message2, message3, exclude_dirs, exclude_files)  
    time.sleep(1)
    name = "[COLOR ghostwhite][B]BACKUP[/B][/COLOR]"
    dialog.ok("[COLOR green][B]SUCCESS![/B][/COLOR]", 'The backup was completed successfully!.',"Backup Location: ",'[COLOR=yellow]'+backup_zip+'[/COLOR]')

def FullBackup():
    guisuccess=1
    if not os.path.exists(USB):
        os.makedirs(USB)
    vq = _get_keyboard( heading="Enter a name for this backup" )
    if ( not vq ): return False, 0
    title = urllib.quote_plus(vq)
    backup_zip = xbmc.translatePath(os.path.join(USB,title+'.zip'))
    exclude_dirs =  ['backupdir','cache','temp']
    exclude_files = ["spmc.log","spmc.old.log","xbmc.log","xbmc.old.log","kodi.log","kodi.old.log"]
    message_header = "Creating full backup..."
    message_header2 = "Creating full backup..."
    message1 = "Archiving..."
    message2 = ""
    message3 = "Please Wait"
    FIX_SPECIAL(USERDATA)
    ARCHIVE_CB(HOME, backup_zip, message_header2, message1, message2, message3, exclude_dirs, exclude_files)  
    time.sleep(1)
    name = "[COLOR ghostwhite][B]BACKUP[/B][/COLOR]"
    dialog.ok("[COLOR green][B]SUCCESS![/B][/COLOR]", 'The backup was completed successfully!.',"Backup Location: ",'[COLOR=yellow]'+backup_zip+'[/COLOR]')

def TV_GUIDE_BACKUP():
    guisuccess=1
    if not os.path.exists(USB):
        os.makedirs(USB)
    vq = _get_keyboard( heading="Enter a name for this backup" )
    if ( not vq ): return False, 0
    title = urllib.quote_plus(vq)
    backup_zip = xbmc.translatePath(os.path.join(USB,title+'_tv_guide.zip'))
    exclude_dirs =  ['']
    exclude_files = [""]
    message_header = "Creating full backup..."
    message_header2 = "Creating full backup..."
    message1 = "Archiving..."
    message2 = ""
    message3 = "Please Wait"
    ARCHIVE_CB(GUIDE, backup_zip, message_header2, message1, message2, message3, exclude_dirs, exclude_files)  
    time.sleep(1)
    name = "[COLOR ghostwhite][B]BACKUP[/B][/COLOR]"
    dialog.ok("[COLOR green][B]SUCCESS![/B][/COLOR]", 'The backup was completed successfully!.',"Backup Location: ",'[COLOR=yellow]'+backup_zip+'[/COLOR]')

def ADDON_DATA_BACKUP():
    guisuccess=1
    if not os.path.exists(USB):
        os.makedirs(USB)
    vq = _get_keyboard( heading="Enter a name for this backup" )
    if ( not vq ): return False, 0
    title = urllib.quote_plus(vq)
    backup_zip = xbmc.translatePath(os.path.join(USB,title+'_addon_data.zip'))
    exclude_dirs =  ['']
    exclude_files = [""]
    message_header = "Creating full backup..."
    message_header2 = "Creating full backup..."
    message1 = "Archiving..."
    message2 = ""
    message3 = "Please Wait"
    FIX_SPECIAL(ADDON_DATA)
    ARCHIVE_CB(ADDON_DATA, backup_zip, message_header2, message1, message2, message3, exclude_dirs, exclude_files)  
    time.sleep(1)
    name = "[COLOR ghostwhite][B]BACKUP[/B][/COLOR]"
    dialog.ok("[COLOR green][B]SUCCESS![/B][/COLOR]", 'The backup was completed successfully!.',"Backup Location: ",'[COLOR=yellow]'+backup_zip+'[/COLOR]')

def ARCHIVE_CB(sourcefile, destfile, message_header, message1, message2, message3, exclude_dirs, exclude_files):
    zipobj = zipfile.ZipFile(destfile , 'w', zipfile.ZIP_DEFLATED)
    rootlen = len(sourcefile)
    for_progress = []
    ITEM =[]
    dp.create(message_header, message1, message2, message3)
    for base, dirs, files in os.walk(sourcefile):
        for file in files:
            ITEM.append(file)
    N_ITEM =len(ITEM)
    for base, dirs, files in os.walk(sourcefile):
        dirs[:] = [d for d in dirs if d not in exclude_dirs]
        files[:] = [f for f in files if f not in exclude_files]
        for file in files:
            for_progress.append(file) 
            progress = len(for_progress) / float(N_ITEM) * 100  
            dp.update(int(progress),"Backing Up",'[COLOR yellow]%s[/COLOR]'%file, 'Please Wait')
            fn = os.path.join(base, file)
            zipobj.write(fn, fn[rootlen:])  
    zipobj.close()
    dp.close()

def FIX_SPECIAL(url):
    HOME         =  xbmc.translatePath('special://home')
    dialog = xbmcgui.Dialog()
    dp.create(AddonTitle,"Renaming paths...",'', 'Please Wait')
    for root, dirs, files in os.walk(url):  #Search all xml files and replace physical with special
        for file in files:
            if file.endswith(".xml"):
                 dp.update(0,"Fixing","[COLOR yellow]" + file + "[/COLOR]", "Please wait.....")
                 a=open((os.path.join(root, file))).read()
                 b=a.replace(HOME, 'special://home/')
                 f = open((os.path.join(root, file)), mode='w')
                 f.write(str(b))
                 f.close()
				
def Restore():

	for file in os.listdir(USB):
		if file.endswith(".zip"):
			url =  xbmc.translatePath(os.path.join(USB,file))
		
def READ_ZIP(url):

	if not "_addon_data" in url:
		if not "tv_guide" in url:
			if dialog.yesno(AddonTitle,"[COLOR yellow]" + url + "[/COLOR]","Do you want to restore this backup?"):
				skinswap()
				wiz.WIPE_BACKUPRESTORE()
				_out = xbmc.translatePath(os.path.join('special://','home'))
			else:
				sys.exit(1)
		else:
			if dialog.yesno(AddonTitle,"[COLOR yellow]" + url + "[/COLOR]","Do you want to restore this backup?"):
				_out = GUIDE
			else:
				sys.exit(1)
	else:
		if dialog.yesno(AddonTitle,"[COLOR yellow]" + url + "[/COLOR]","Do you want to restore this backup?"):
			_out = ADDON_DATA
		else:
			sys.exit(1)

	_in = url
	dp.create(AddonTitle,"Restoring File:",_in,'Please Wait...')
	unzip(_in, _out, dp)
	name = "[COLOR ghostwhite][B]RESTORE[/B][/COLOR]"
	
	if not "addon_data" in url:
		if not "tv_guide" in url:
			dialog.ok(AddonTitle,'Restore Successful, please restart XBMC/Kodi for changes to take effect.','','')
			wiz.killxbmc()
		else:
			dialog.ok(AddonTitle,'Your TV Guide settings have been restored.','','')
	else:
		dialog.ok(AddonTitle,'Your Addon Data settings have been restored.','','')

def unzip(_in, _out, dp):
	__in = zipfile.ZipFile(_in,  'r')
	
	nofiles = float(len(__in.infolist()))
	count   = 0
	
	try:
		for item in __in.infolist():
			count += 1
			update = (count / nofiles) * 100
			
			if dp.iscanceled():
				dialog = xbmcgui.Dialog()
				dialog.ok(AddonTitle, 'Extraction was cancelled.')
				
				sys.exit()
				dp.close()
			
			try:
				dp.update(int(update))
				__in.extract(item, _out)
			
			except Exception, e:
				print str(e)

	except Exception, e:
		print str(e)
		return False
		
	return True
		
def ListBackDel():
	addonfolder = xbmc.translatePath(os.path.join('special://','home'))
	for file in os.listdir(USB):
		if file.endswith(".zip"):
			url =  xbmc.translatePath(os.path.join(USB,file))
			
def DeleteBackup(url):
	if dialog.yesno(AddonTitle,"[COLOR yellow]" + url + "[/COLOR]","Do you want to delete this backup?"):
		os.remove(url)
		dialog.ok(AddonTitle,"[COLOR yellow]" + url + "[/COLOR]","Successfully deleted.")
		
def DeleteAllBackups():
	if dialog.yesno(AddonTitle,"Do you want to delete all backups?"):
		shutil.rmtree(USB)
		os.makedirs(USB)
		dialog.ok(AddonTitle,"All backups successfully deleted.")

def skinswap():

	skin         =  xbmc.getSkinDir()
	KODIV        =  float(xbmc.getInfoLabel("System.BuildVersion")[:4])
	skinswapped = 0

	#SWITCH THE SKIN IF THE CURRENT SKIN IS NOT CONFLUENCE
	if skin not in ['skin.confluence','skin.estuary']:
		choice = xbmcgui.Dialog().yesno(AddonTitle, '[COLOR red][B]We can see that you are not using the default confluence skin.[/B][/COLOR]','[COLOR red][B]CLICK YES TO ATTEMPT TO AUTO SWITCH TO CONFLUENCE[/B][/COLOR]','[COLOR red][B]PLEASE DO NOT DO PRESS ANY BUTTONS OR MOVE THE MOUSE WHILE THIS PROCESS IS TAKING PLACE, IT IS AUTOMATIC[/B][/COLOR]', yeslabel='[B][COLOR green]YES[/COLOR][/B]',nolabel='[B][COLOR red]NO[/COLOR][/B]')
		if choice == 0:
			sys.exit(1)
		skin = 'skin.estuary' if KODIV >= 17 else 'skin.confluence'
		skinSwitch.swapSkins(skin)
		skinswapped = 1
		time.sleep(1)
	
	#IF A SKIN SWAP HAS HAPPENED CHECK IF AN OK DIALOG (CONFLUENCE INFO SCREEN) IS PRESENT, PRESS OK IF IT IS PRESENT
	if skinswapped == 1:
		if not xbmc.getCondVisibility("Window.isVisible(yesnodialog)"):
			xbmc.executebuiltin( "Action(Select)" )
	
	#IF THERE IS NOT A YES NO DIALOG (THE SCREEN ASKING YOU TO SWITCH TO CONFLUENCE) THEN SLEEP UNTIL IT APPEARS
	if skinswapped == 1:
		while not xbmc.getCondVisibility("Window.isVisible(yesnodialog)"):
			time.sleep(1)
	
	#WHILE THE YES NO DIALOG IS PRESENT PRESS LEFT AND THEN SELECT TO CONFIRM THE SWITCH TO CONFLUENCE.
	if skinswapped == 1:
		while xbmc.getCondVisibility("Window.isVisible(yesnodialog)"):
			xbmc.executebuiltin( "Action(Left)" )
			xbmc.executebuiltin( "Action(Select)" )
			time.sleep(1)
	
	skin         =  xbmc.getSkinDir()

	#CHECK IF THE SKIN IS NOT CONFLUENCE
	if skin not in ['skin.confluence','skin.estuary']:
		choice = xbmcgui.Dialog().yesno(AddonTitle, '[COLOR red][B]ERROR: AUTOSWITCH WAS NOT SUCCESFULL[/B][/COLOR]','[COLOR red][B]CLICK YES TO MANUALLY SWITCH TO CONFLUENCE NOW[/B][/COLOR]','[COLOR red][B]YOU CAN PRESS NO AND ATTEMPT THE AUTO SWITCH AGAIN IF YOU WISH[/B][/COLOR]', yeslabel='[B][COLOR green]YES[/COLOR][/B]',nolabel='[B][COLOR red]NO[/COLOR][/B]')
		if choice == 1:
			xbmc.executebuiltin("ActivateWindow(appearancesettings)")
			return
		else:
			sys.exit(1)

##############################    END    #########################################
