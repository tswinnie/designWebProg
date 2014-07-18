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
        print matt.passer_rating

                #  create instance of my QBR object
        payton = QBR()
        payton.passing = 400
        payton.completion = 90
        payton.yards = 2000
        payton.touchdowns = 20
        payton.interceptions = 9

                #  create instance of my QBR object
        matt = QBR()
        matt.passing = 190
        matt.completion = 300
        matt.yards = 1830
        matt.touchdowns = 50
        matt.interceptions = 9

                #  create instance of my QBR object
        tom = QBR()
        tom.passing = 190
        tom.completion = 700
        tom.yards = 1109
        tom.touchdowns = 29
        tom.interceptions = 20

                #  create instance of my QBR object
        drew = QBR()
        drew.passing = 400
        drew.completion = 290
        drew.yards = 4000
        drew.touchdowns = 200
        drew.interceptions = 40




class QBR(object):  # created class that will hold the data for five players
    def __int__(self):
        self.passing = 0  # this is the passing value
        self.completion = 0  # this is the completion value
        self.yards = 0  # this is the yards gained value
        self.touchdowns = 0  # this is the number of touchdowns value
        self.interceptions = 0  # this is the interceptions by the quarterback
        self.__rating_ = 90  # this my private variable

    @property
    def passer_rating(self):
        return self.__rating_






app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
