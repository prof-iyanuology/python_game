# ### EXCEPTION HANDLING IN PYTHON
# num= input('please enter interger: ')
# try:
#     if num > 0:
#         print("it's integer ")
# except:
#     print ('check the number') 

# print('@@@@@@@@@@@@@')
# x=input('enter value ')
# x = int(x)
# try:
#     result = x/0
# except ZeroDivisionError:
#     print('invalid')

# print("@@@@############")
# age = int(input('please enter your age: '))
# try:
#    if age >18:
#     print('Eligible')
# except:
#     print('Not eligible')

# print('$$$$$$$$$$$$$')
# # x = 5
# try:
#     if x > 0:
#         print('integer')
# except Exception as message:
#     print(message)
#     print('some error in your code: ')

# ###########
# x = 5
# try:
#     if x/0:
#         print('integer')
# except Exception as message:
#     print(message)
#     print('some error in your code: ')

########################################################################################################################
try:
    real = int(input('Please enter the number '))
    print(30/real)
except ZeroDivisionError:
    print("you can't divide by zero")
except ValueError:
    print("check your number: ")
######################################

print("**********************")
try:
    age = int(input('please enter your age: '))
    if age <= 0:
        print("your age can't be zero or negative!")
    elif age < 18:
        print('you are not eligible: ')
    elif age >= 18 and age <= 60:
        print("congratulation! you are qualified")
    elif age > 60:
        print("you are too old, sorryy")
except ValueError:
    print("please enter valid age! ")
else:
    print('congrat!')

print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
try:
    file = open('soap.py', 'r')
    content = file.read()
except FileNotFoundError:
    print("file direction not found!")
else:
    print(f"file details are {content}")
finally:
    print('file close')
    
############################ RAISE EXCEPTION
def number_power(value):
    try:
        output = value * value
    except ValueError as e:
        print(f'Error: {e}')
