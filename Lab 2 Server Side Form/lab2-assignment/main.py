'''
Tyrone Swinnie
Design for Web Programming
7/16/14
Lab 2 Server Side Form
'''


import webapp2

class MainHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write('Hello Tyrone')

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
