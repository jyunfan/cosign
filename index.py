#std
import logging
from datetime import datetime,date
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
    '/', 'index',
    '/cosign', 'index',
    '/summary', 'summary'
)

myform = form.Form( 
    form.Textbox("name")
)

class index:
    def GET(self):
        web.seeother('/static/chen.html')

    def POST(self):
        i = web.input()
        counter = increment("sign", 0)+1
        obj = Sign(
                count = counter,
                date  = datetime.utcnow().date(),
                name  = i.name,
                birth = date(int(i.birthyear), int(i.birthmonth), int(i.birthdate)),
                addr  = i.addr,
                phone = i.phone)
        obj.put()
        counter = increment("sign", 1)
        render = web.template.render('templates')
        return render.thanks(i.name)

class summary:
    def GET(self):
        count = increment("sign", 0)
        render = web.template.render('templates')
        signlist = [{'text':'1-1000','url':'url'}]
        return render.summary(signlist)

def main():
    web.application(urls, globals()).cgirun()

if __name__ == '__main__':
    main()

