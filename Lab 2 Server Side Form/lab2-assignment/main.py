'''
Tyrone Swinnie
Design for Web Programming
7/16/14
Lab 2 Server Side Form
'''


import webapp2

class MainHandler(webapp2.RequestHandler):
    def get(self):
        page_head = '''<!DOCTYPE HTML>
<html>
<head>
<title></title>'''
        page_body = '''
<body>
<form method ="GET" action="">
<label>First Name</label><input type="text" name="first" />
<label>Last Name</label><input type="text" name="last" />
<input type="checkbox" name="personal" value="Bike">Personal Loan<br>
<input type="checkbox" name="car" value="car">Car Loan<br>
<input type="checkbox" name="home" value="home">Home Loan<br>
<select>
  <option name="one">$500 - $1000</option>
  <option name="two">$2000 - $3000</option>
  <option name="three">$3000 - $4000</option>
</select>
<input type="submit" value="submit" />




        '''
        page_close = '''
</form>
</body>
</html>
        '''
        if self.request.GET:
            first_name = self.request.GET['first']
            last_name = self.request.GET['last']
            # personal = self.request.GET['personal']
            # car = self.request.GET['car']
            # home = self.request.GET['home']
            # option_one = self.request.GET['one']
            # option_two = self.request.GET['two']
            # option_three = self.request.GET['three']
            self.response.write(first_name + last_name)
        else:
            self.response.write(page_head + page_body + page_close)













app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
