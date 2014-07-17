'''
Tyrone Swinnie
Design for Web Programming
7/16/14
Lab 2 Server Side Form
'''


import webapp2

class MainHandler(webapp2.RequestHandler):
    def get(self):

        # Create the page so that I can create a form
        # create the form inside the html code like I normally would in an HTML document

        page_head = '''<!DOCTYPE HTML>
<html>
<head>
<title></title>'''
        page_body = '''
<body>
<form method ="GET" action="">
<label>First Name</label><input type="text" name="first" />
<label>Last Name</label><input type="text" name="last" /><br>
<label>Car Loan</label><input type="checkbox" name= "car" value="Car Loan" />


<select name="small_loan">
  <option  value="$500 - $1000" >$500 - $1000</option>
    <option  value="$1000 - $2000" >$1000 - $2000</option>
        <option  value="$2000 - $3000" >$2000 - $3000</option>
</select>

<select name="loan_date">
  <option  value="30 days - 60 days" >30 days - 60 days</option>
    <option  value="60 days - 90 days" >60 days - 90 days</option>
        <option  value="90 days - 120 days" >90 days - 120 days/option>
</select>

<input type="submit" value="submit" />




        '''
        page_close = '''
</form>
</body>
</html>
        '''
        # I am going to store the information that are collected from the user into a variable
        if self.request.GET:
            first_name = self.request.GET['first']  # this gets the value for the first name
            last_name = self.request.GET['last']  # this gets the last name value
            car_loan = self.request.GET['car']  # this gets the car loan check box value
            drop = self.request.GET['small_loan']  # this gets the drop down selection value
            loan = self.request.GET['loan_date']  # this gets the days for the loan value drop down
            # return the values that the user put in the form after the submit button
            self.response.write(page_head + page_body + first_name + ' ' + last_name + ' ' + car_loan + ' ' + drop + ' ' + loan + page_close)
        else:
            # if the user does not input any values then do this
            self.response.write(page_head + page_body + page_close)













app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
