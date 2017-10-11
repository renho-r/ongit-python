import tornado.auth
import tornado.escape
import tornado.ioloop
import tornado.web
import os.path
import json
import tornado.gen
from tornado.options import define, options, parse_command_line
from controler.LedControler import LedControler

define("port", default=8888, help="run on the given port", type=int)
define("debug", default=False, help="run in debug mode")

class BaseHandler(tornado.web.RequestHandler):
    @tornado.web.asynchronous
    def get(self):
        self.render("index/html/index.html")
class MainHandler(BaseHandler):
    @tornado.web.asynchronous
    def get(self):
        self.render("index/html/index.html")
class LedHandler(BaseHandler):
    @tornado.web.asynchronous
    def get(self):
        action = self.get_argument('action')
        if 'on' == action:
            lc = LedControler()
            lc.on()
            self.write(json.dumps({"flag": "Pause ok"}))
        elif 'll' == action:
            lc = LedControler()
            data = lc.ll()
            self.write(json.dumps(data))
        else:
            lc = LedControler()
            lc.off()
            self.write(json.dumps({"flag": "Pause ok"}))
        self.finish()
def main():
    parse_command_line()
    app = tornado.web.Application(
        [
            (r"/", MainHandler),
            (r"/led", LedHandler)
        ],
        template_path=os.path.join(os.path.dirname(__file__), "templates"),
        static_path=os.path.join(os.path.dirname(__file__), "static"),
        debug=options.debug,
        )
    app.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()


if __name__ == "__main__":
    main()