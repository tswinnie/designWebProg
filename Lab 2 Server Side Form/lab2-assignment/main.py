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
<title></title>
<link href='http://fonts.googleapis.com/css?family=Lato:300,400,300italic,400italic' rel='stylesheet' type='text/css'>
<style type="text/css">
body{
background: #1abc9c;
font-family: 'Lato', sans-serif;
}

.container{

width: 980px;
margin: 0 auto;


}

form {
margin: 0 auto;
width: 348px;
background: #e74c3c;
padding: 20px;
border-radius: 8px;
box-shadow: 1px 1px 1px 1px #c0392b;
height: 655px;
}

input{
border: none;
width: 335px;
height: 48px;
border-radius: 5px;
background: #ecf0f1;
margin: 6px;
font-size: 16px;
font-weight: bold;
}

select{
order: none;
width: 335px;
height: 48px;
border-radius: 5px;
background: #ecf0f1;
margin: 6px;
font-size: 16px;
font-weight: bold;
}

#submit{

background: #2980b9;
color: #fff;
cursor:pointer;
}

#submit:hover{

background: #3498db;
color: #fff;

}

#titleText{

width: 364px;
font-size: 32px;
font-weight: 300;
color: #fff;

}

#confirmation {
text-align: center;
height: 82px;
background: #ecf0f1;
margin-bottom: -50px;
border-radius: 5px;
}



</style>
'''
        page_body = '''
<body>
<div class="container">
<form method ="GET" action="">
<h2 id="titleText">Get Your Car Loan Today!</h2>
<label>First Name:</label><input type="text" name="first" /><br>
<label>Last Name:</label><input type="text" name="last" /><br>


<label>How Much:</label><select name="small_loan">
  <option  value="$500 - $1000" >$500 - $1000</option>
    <option  value="$1000 - $2000" >$1000 - $2000</option>
        <option  value="$2000 - $3000" >$2000 - $3000</option>
</select>
<br>
<label>How Long:</label><select name="loan_date">
  <option  value="30 days - 60 days" >30 days - 60 days</option>
    <option  value="60 days - 90 days" >60 days - 90 days</option>
        <option  value="90 days - 120 days" >90 days - 120 days</option>
</select>
<label>Car Loan:</label><input type="checkbox" name= "car" value="Car Loan" style="margin-top: -9px;" /><br>

<br>
<input id="submit" type="submit" value="submit" />
<h3 id="confirmation">Your Confirmation</h3>




        '''
        page_close = '''
</form>
</div>
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
