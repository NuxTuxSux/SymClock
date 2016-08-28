from twisted.internet import reactor
from twisted.web.server import Site
from twisted.web.resource import Resource
import time


class Page(Resource):
    isLeaf = True

    def __init__(self,page):
        self.page = page
    def render_GET(self, request):
        #return "<html><body>%s</body></html>" % (time.ctime(),)
        return self.page

def publishPage(page):
    resource = Page(page)
    factory = Site(resource)
    reactor.listenTCP(80, factory)
    reactor.run()


page = "<html><body><h1>Pippo</h1><br><h3>dei formaggi</h3></body></html>"