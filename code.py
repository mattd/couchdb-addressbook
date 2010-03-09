import web
import couchdb

urls = (
    '/', 'index'
)

app = web.application(urls, globals())
render = web.template.render('templates/')

# connect to the database
s = couchdb.Server()
db = s['addressbook']

class index:
    def GET(self):
        records = [db[id] for id in db]
        return render.index(records)

if __name__ == "__main__":
    app.run()
