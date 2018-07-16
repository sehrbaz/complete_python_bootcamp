# Errors and Exceptions Homework
# Problem 1
for i in ['a','b','c']:
    try:
        print i**2
    except:
        print('Oops an error...')
        
# Problem 2
x = 5
y = 0

try:
    z = z/y
except ZeroDivisionError:
    print('Oops, division by zero :(')
finally:
    print('All Done.')
    
# Problem 3
def ask():

    while True:
    try:
        x = int(input('Input an integer: '))
    except:
        print('An error occurred! Please try again!')
        continue
    else:
        break
    
    print('Thank you, you number squared is:', x**2)