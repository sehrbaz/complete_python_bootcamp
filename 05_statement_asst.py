#01 - Use for, split(), and if to create a Statement that will print out words that start with 's':
st = 'Print only the words that start with s in this sentence'

for s in st.split():
    if s[0] == 's':
        print s

#02 - Use range() to print all the even numbers from 0 to 10.
range(0, 11, 2)

#or
lst = xrange(11)
lst = [number for number in xrange(11) if number % 2 == 0]
print (lst)

#or
for i in xrange(11):
    if i % 2 == 0:
        print i

#03 - Use List comprehension to create a list of all numbers between 1 and 50 that are divisible by 3.
l = [number for number in xrange(1,50) if number % 3 == 0]
print l

#04 - Go through the string below and if the length of a word is even print "even!"
st = 'Print every word in this sentence that has an even number of letters'

for word in st.split():
    if len(word) % 2 == 0:
        print word

#05 -
'''
Write a program that prints the integers from 1 to 100. But for multiples of
three print "Fizz" instead of the number, and for the multiples of five print
"Buzz". For numbers which are multiples of both three and five print "FizzBuzz".
'''

for i in xrange(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        print 'FizzBuzz'
    elif i % 3 == 0:
        print 'Fizz'
    elif i % 5 == 0:
        print 'Buzz'
    else:
        print i

#06 - Use List Comprehension to create a list of the first letters of every word in the string below:
st = 'Create a list of the first letters of every word in this string'

list = [word[0] for word in st.split()]
