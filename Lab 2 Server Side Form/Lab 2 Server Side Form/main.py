'''
Tyrone Swinnie
7/16/14
Design for Web programming
Lab 2 Server Side Form
'''
import webapp2

class MainHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write('Hello world!')

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
