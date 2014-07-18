'''
Tyrone Swinnie
7/17/14
Design for Web
Encapsulated Calculator
'''


import webapp2

class MainHandler(webapp2.RequestHandler):
    def get(self):

        #  create instance of my QBR object
        matt = QBR()
        matt.passing = 200
        matt.completion = 180
        matt.yards = 1000
        matt.touchdowns = 100
        matt.interceptions = 3
        



class QBR(object):  # created class that will hold the data for five players
    def __int__(self):
        self.passing = 0  # this is the passing value
        self.completion = 0  # this is the completion value
        self.yards = 0  # this is the yards gained value
        self.touchdowns = 0  # this is the number of touchdowns value
        self.interceptions = 0  # this is the interceptions by the quarterback
        self.__rating__ = 0  # this my private variable








app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
