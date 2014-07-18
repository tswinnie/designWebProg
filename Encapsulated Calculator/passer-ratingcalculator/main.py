'''
Tyrone Swinnie
7/17/14
Design for Web
Encapsulated Calculator
'''


import webapp2

class MainHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write('Hello world!')

class QBR(object):
    def __int__(self):
        self.passing = 0
        self.completion = 0
        self.yards = 0
        self.touchdowns = 0
        self.interceptions = 0
        self.__rating__ = 0








app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
