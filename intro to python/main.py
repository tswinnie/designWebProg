#
# response = raw_input("enter your name")
#
# first_name = "Tyrone"
# last_name = "Swinnie"

# print "hello there,", response

# birth_year = 1986
# current_year = 2014
#
# age = current_year - birth_year
#
# print age

'''
create a conditional statement

'''

# budget = 100
# shopping_cart = ["nike","addidas","converse"]
# '''
# create an object array similar to javascript
# '''
#
# stores = dict()
# stores = {"walmart":"shaq shoes", "famous footwear": "Jordans"}
#
# if budget > 50:
#     brand = "Air Force Ones"
#     print "You get some fresh " + stores["famous footwear"]
# elif budget >= 25:
#     print "You get some fresh " + shopping_cart[1]
#
# else:
#     print "You get some fresh " + shopping_cart[2]
#
#
#change the content of an html page

# title = "tyrone's website"
# body = "new image"
# message = '''
# <!DOCTYPE HTML>
# <html>
# <head>
# <title>{title}</title>
# </head>
#
# <body>
#
# {body}
#
#
# </body>
#
# </html>
#
# '''
#
# print message

def getAge(c, b):
    age = c - b

    return age

a = getAge(2014, 1986)

print a
