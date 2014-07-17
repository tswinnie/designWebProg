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
        if self.request.GET:
            first_name = self.request.GET['first']
            last_name = self.request.GET['last']
            car_loan = self.request.GET['car']
            drop = self.request.GET['small_loan']
            loan = self.request.GET['loan_date']
            self.response.write(page_head + page_body + first_name + ' '  '\n' + last_name + ' ' + '\n' + car_loan + '\n' + ' ' + '\n' + drop + ' ' + loan + '\n' + page_close)
        else:
            self.response.write(page_head + page_body + page_close)













app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
