# coding:utf-8
import os.path
import tornado.httpserver
import tornado.web
import tornado.ioloop
from tornado.options import define, options

from sqlalchemy.orm import sessionmaker,scoped_session

from models import engine,Todo

define("port", default=8888, help="run port", type=int)
define("mysql_host", default="127.0.0.1:3306", help="db host")
define("mysql_database", default="todo", help="db name")
define("mysql_user", default="root", help="db user")
define("mysql_password", default="8354210", help="db password")


TEMPLATE_PATH = os.path.join(os.path.dirname(__file__), "templates")  
STATIC_PATH = os.path.join(os.path.dirname(__file__), "static") 


class Application(tornado.web.Application):

    def __init__(self):
        handlers = [
            (r"/", IndexHandler),
#              (r"/todo/new", NewHandler),
            #  (r"/todo/(\d+)/edit", EditHandler),
            #  (r"/todo/(\d+)/delete", DeleteHandler),
            #  (r"/todo/(\d+)/finish", FinishHandler),
        ]
        settings = dict(
            template_path=TEMPLATE_PATH,
            static_path=STATIC_PATH,
            debug=True
        )
        tornado.web.Application.__init__(self, handlers, **settings)
 #         self.db = torndb.Connection(
            #  host=options.mysql_host,
            #  database=options.mysql_database,
            #  user=options.mysql_user,
            #  password=options.mysql_password
        #  )
        self.db = scoped_session(sessionmaker(bind=engine))

class IndexHandler(tornado.web.RequestHandler):

    def get(self):
        title = "todo"
        db = self.application.db
        #  todos = db.query("select * from todo order by post_date desc")
        todos = self.application.db.query(Todo).all()
        self.render("index.html", todos=todos, title=title)


def main():  
    tornado.options.parse_command_line()  
    app = tornado.httpserver.HTTPServer(Application())  
    app.listen(options.port)  
    tornado.ioloop.IOLoop.instance().start()  
                      
if __name__ == "__main__":  
    main()  
