#    Title: stephens_hobbies.py
#    Author: Kailee Stephens
#    Date: 11 September 2022
#    Description: Exercise 5.3 - Python Conditionals, Lists, and Loops

# Create a list of at least 5 hobbies.
myHobbies = ['crocheting','reading','paddleboarding', 'listening to music', 'Playing frisbee with my dog']

# Use a for loop to iterate over the list of hobbies and print them to the console window.
for hobby in myHobbies :
    print(hobby)
    
# create a list of days.
days = ['Monday','Tuesday','Wednesday','Thursday','Friday', 'Saturday','Sunday' ]

# use a for loop to iterate over the list of days and add an if...else statement to display what the day is.
# For saturday and sunday display a message indicating you are off and should enjoy your hobbies. 
# For all other days display a message indicating it is a work day.
for day in days:
    if day == 'Saturday' or day == 'Sunday':
        print("Today is your day off! Enjoy your hobbies!")
    else:
        print('Today is work day.')