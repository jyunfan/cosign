# -*- coding: utf-8 -*-
#std
import logging
from datetime import datetime,date
import codecs
#gae
from google.appengine.api import taskqueue, memcache
from google.appengine.ext import db
from google.appengine.ext.db import stats
#3rd
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
        """ Generate csv file """

        fields = ('name', 'phone')
        tmpsignlist = db.Query(Sign).order('count')

        # Generate csv content
        #   Special case: add double quote to phone numbers to preserve
        #   leading zeros in phone number
        signlist = [u'姓名,出生年月日,地址,電話']
        for s in tmpsignlist:
            signlist.append('"%s",%s,"%s",="%s"' % (s.name, s.birth, s.addr, s.phone))
        csv = "\n".join(signlist)

        web.header('Content-type','text/csv; charset=utf-8')
        web.header('Content-Disposition', 'filename=cosign.csv')

        # Add BOM for Windows users
        return codecs.BOM_UTF8 + csv.encode("utf-8")

def main():
    web.application(urls, globals()).cgirun()

if __name__ == '__main__':
    main()
