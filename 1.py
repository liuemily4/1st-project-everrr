number1=input('First number: ')
answer1=int(number1)
operation=input('operation(+, -, x, /): ')
sign=operation
number2=input('Second number: ')
answer2=int(number2)
print('sum =', sum)
sum=answer1+answer2
difference=answer1-answer2
product=answer1*answer2
quotient=answer1//answer2
if sign==('+'):
    print('sum=', sum)
if sign==('-'):
    print('difference=', difference)
if sign==('x'):
    print('product=', product)
if sign==('/'):
    print('quotient=', quotient)