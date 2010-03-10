from uuid import uuid4

import web
from couchdb.client import Server, PermanentView

urls = (
    '/', 'index'
)

app = web.application(urls, globals())
render = web.template.render('templates/')

# connect to the database
s = Server()
db = s['addressbook']

class index:
    def GET(self):
        view = PermanentView(db.resource.url + '/_design/results/_view/all', 'all')
        results = [row.value for row in view().rows]
        return render.index(results)

    def POST(self):
        i = web.input()
        for k, v in i.items():
            if not v:
                del i[k]
        if i.items():
            db[uuid4().hex] = i 
        raise web.seeother('/')

if __name__ == "__main__":
    app.run()
