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

<select name="small_loan">
  <option  value="$500 - $1000" >$500 - $1000</option>
    <option  value="$1000 - $2000" >$1000 - $2000</option>
        <option  value="$2000 - $3000" >$2000 - $3000</option>
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
            # drop_two = self.request.GET['small_loanTwo']
            self.response.write(first_name + last_name + car_loan + drop)
        else:
            self.response.write(page_head + page_body + page_close)













app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
