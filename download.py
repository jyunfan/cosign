#std
import logging
from datetime import datetime,date
import codecs
#gae
from google.appengine.api import taskqueue, memcache
from google.appengine.ext import db
from google.appengine.ext.db import stats
#3rd
from BeautifulSoup import BeautifulSoup
import web #http://webpy.org/
from web import form
#local
from model import Sign
from util import increment

urls = (
    '/download', 'download',
)

class download:
    def GET(self):
        signlist = db.Query(Sign).order('count')
        render = web.template.render('templates')
        web.header('Content-type','text/csv; charset=BIG5')
        web.header('Content-Disposition', 'filename=cosign.csv')
        return codecs.BOM_UTF8 + str(render.signlist(signlist))

def main():
    web.application(urls, globals()).cgirun()

if __name__ == '__main__':
    main()

