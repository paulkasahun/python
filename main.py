
# name=input(" What is your name\n")
# age = input('how old are you?\n')
# school= input('where you goes to school\n')
# print(name+'\n'+age+'\n'+school)
#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
'''
int()
float()
str()
bool()

these functions converts any type to their type
they are called type casters

'''

# firstNumber = int(input("first number\n"))
# secondNumber = int(input("second Number\n"))
#
# sum = firstNumber+secondNumber
# prod = firstNumber*secondNumber
# divs= firstNumber/secondNumber if secondNumber!=0 else print("error")
# print(sum,prod,divs)
'''
what would happen if you did not 
cast
the input is always string
and addition will provide string concat
str multiplication will cause error
and str sub too
division too

firstNumber = input('first:')
secrets= input('second:')
print(firstNumber+secrets)
print((firstNumber*secrets))

'''

'''when you cast cast exactly what kind of input will
the user gives
instead of casting to int
cast to float because float is better than int
'''

first = float(input('first'))
second = float(input('second'))

print(second+first)