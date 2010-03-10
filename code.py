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
        return render.index(view())

    def POST(self):
        i = web.input()
        db[uuid4().hex] = {'first_name': i.first_name, 'last_name': i.last_name}
        raise web.seeother('/')

if __name__ == "__main__":
    app.run()
