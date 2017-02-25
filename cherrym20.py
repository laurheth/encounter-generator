import cherrypy
import m20mon
class encountergen(object):
    def index(self,lvl=1):
#        lvl=cherrypy.request.params.get(lvl)
        lvl=int(lvl)
        output=m20mon.makeencounter(lvl)
        return output
    def static(self,filename):
        f=open('static/'+filename)
        output="<br>"
        for line in f:
            output+=line+"</br>"
        return output
    index.exposed = True
    static.exposed= True

root=encountergen()
cherrypy.quickstart(root)
