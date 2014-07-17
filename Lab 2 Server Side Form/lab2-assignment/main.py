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
<label>Last Name</label><input type="text" name="last" /><br>
<input type="checkbox" name= "car" value="Car Loan" />Car Loan<br>

<select>
  <option vale="one">$500 - $1000</option>
  <option value="two">$2000 - $3000</option>
  <option value="three">$3000 - $4000</option>
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
            car_loan = self.request.GET['car']
            # option_two = self.request.GET['two']
            # option_three = self.request.GET['three']
            self.response.write(first_name + last_name + car_loan)
        else:
            self.response.write(page_head + page_body + page_close)













app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
