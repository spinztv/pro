from concurrent.futures import ThreadPoolExecutor
from concurrent.futures import as_completed
from concurrent.futures import wait
from resources import sources
import xbmcaddon
import importlib
import xbmcgui
import urllib

addon_id = 'plugin.video.spinzstrictlyhd'
addon = xbmcaddon.Addon(id=addon_id)

class Sites:
    def __init__(self):
        self.sources = []
        self.sources = sources.__all__
        self.links = []
        self.pDialog = xbmcgui.DialogProgress()
        self.pDialog.create('Strictly HD','Initializing scrapers...')
        
    def search(self, term):
        src = 1
        total = len(self.sources)
        pool = ThreadPoolExecutor(len(self.sources)) # 1 per source
        futures = [pool.submit(self.thread, source, urllib.quote_plus(term)) for source in self.sources]
        #[self.links.extend(r.result()) for r in as_completed(futures)]
        for r in as_completed(futures):
            percent = int((float(src) / total) * 100)
            self.pDialog.update(percent, "Searching Lucifer's little black book","Page %s" % str(src))
            self.links.extend(r.result())
            src += 1
        self.pDialog.close()
        return self.links
        
    def thread(self, source, term):
        print '=====searching for ({}) on ({})====='.format(term,source)
        source = importlib.import_module('.'+source, package='resources.sources')
        return source.SEARCH(term)
