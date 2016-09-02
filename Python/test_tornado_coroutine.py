
import tornado.ioloop
import tornado.web
from tornado import gen
from tornado.httpclient import AsyncHTTPClient

class MainHandler(tornado.web.RequestHandler):
    @gen.coroutine
    def get(self):
        response = yield self.fetch_json("http://www.baidu.com")
        self.write(response)

    @gen.coroutine
    def fetch_json(self, url):
        response = yield AsyncHTTPClient().fetch(url)
        raise gen.Return(response.body)
application = tornado.web.Application([
                                                    (r"/", MainHandler),
                                                        ])


if __name__ == "__main__":
    application.listen(8888)
    tornado.ioloop.IOLoop.current().start()
