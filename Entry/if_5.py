'''
Author: your name
Date: 2022-04-27 10:02:42
LastEditTime: 2022-04-27 10:02:43
LastEditors: Please set LastEditors
Description: 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
FilePath: \Py-test\Entry\if_5.py
'''
# if

age = 19

if age >= 19:

    print('You are old enough to vote!')

# if-else语句

age = 17 

if age >= 18:

    print('You are old enough to vote!')

else:

    print('Sorry, you are too young to vote.')


# if-elif-else 语句

age = 12

if age < 4:

    print('Your admission cost is $0.')

elif age < 18:

    print('Your admission cost is $5.')

else:

    print('Your admission cost is $10.')


age = 12

if age < 4:

    price = 0

elif age < 18:

    price = 5

else:

    price = 10

print('Your admission cost is $ ' + str(price) + '.')

# 使用多个elif代码块

age = 12 

if age < 4:

    price = 0

elif age < 18:

    price = 5

elif age < 65:

    price = 10

else:

    price = 5

print('Your admission cost is $ ' + str(price) + ' .')

# 省略else代码块

age = 12

if age < 4:

    price = 0

elif age < 18:

    price = 5

elif age <  65:

    price = 10

elif age >= 65:

    price = 5

print('Your admission cost is $' + str(price) + ' .')

# 测试多个条件

requested_toppings = ['mushrooms', 'extra cheese']

if 'mushrooms' in requested_toppings:

    print('Adding mushrooms')

if 'pepperoni' in requested_toppings:

    print('Adding pepperoni')

if 'extra cheese' in requested_toppings:

    print('Adding extra cheese')

print('\nFinished making your pizza')

#练习

alien_color = 'green'

if 'green' in alien_color:

    price = 5

print('\nPlayer get '+ str(price) + '.')


alien_color = 'red'

if 'green' in alien_color:

    price = 5

else:

    print('NO')

alien_color = 'red'

if 'red' in alien_color:

    print('GET five\n')

else:

    print('GET ten')

alien_color = 'green'

if 'red' in alien_color:

    print('GET FIVE\n')

else:

    print('GET TEN')


alien_color = 'green'

if 'red' in alien_color:

    price = 5

elif 'green' in alien_color:

    price = 10

elif 'yellow' in alien_color:

    price = 15

print('\tPlayer get '+ str(price) + '.') 


age  = 65

if age < 2:

    print('婴儿')

elif 2 <= age < 4 :

    print('蹒跚学步')

elif 4 <= age < 13:

    print('儿童')

elif 13 <= age < 20:

    print('青少年')

elif 20 <= age < 65:

    print('成年人')

else:

    print('老年人')


favorite_fruits = ['watermelon','strawberry','cherry','durian']

if 'watermelon'  in favorite_fruits:

    print('You really like watermelon')

if 'bananas' in favorite_fruits:

    print('You really like bananas')

if 'cherry' in favorite_fruits:

    print('You really like cherry')

if 'durian' in favorite_fruits:

    print('You really like durian')

if 'drink' in favorite_fruits:

    print('You really like drink')

print('\n thank you')


favorite_fruits = ['Watermelon','Strawberry','CHEEY','durian']

for value_favorite_fruits in favorite_fruits:

    if value_favorite_fruits.upper() in favorite_fruits:

        print('OK\t 无需更改\t' + value_favorite_fruits)

    else:

        print('NO\t 需要更改\t' + value_favorite_fruits)


# if语句

# 检查特殊元素

requested_topping = ['mushrooms', 'green peppers','extra cheese']

for value_requested_topping in requested_topping:

    print('Adding' + value_requested_topping + ' .')

print('\nFinished making your pizza!')
    
requested_topping = ['mushrooms','green peppers','extra cheese']

for value_requested_topping in requested_topping:

    if value_requested_topping == 'green peppers':

        print('Sorry, we are out of green pepers right now.')

    else:

        print('Adding' + value_requested_topping +'.')

print('\nFinished making your pizza')


# 确定列表不是空的

requested_topping =[]

if requested_topping:

    for value_requested_topping in requested_topping:

        print('Adding' + value_requested_topping + '.')

else:

    print('Are you sure you want a plain pizza?')


#  使用多个列表

available_topping = ['mushrooms', 'olives', 'green peppers',
'pepperoni', 'pineapple', 'extra cheese']

requested_topping = ['mushrooms', 'frcnch frics', 'extra cheese']

available_topping = ['mushrooms', 'olives', 'green peppers', 
 'pepperoni', 'pineapple', 'extra cheese'] 

requested_topping = ['mushrooms', 'french fries', 'extra cheese'] 

for vlaue_requested_topping in requested_topping:

     if value_requested_topping in available_topping:

           print('Adding ' + value_requested_topping + '.')

     else:

           print('Sorry, we dont have' + value_requested_topping + '.')

print('\nFinished making your pizza')


available_toppings = ['mushrooms', 'olives', 'green peppers', 
 'pepperoni', 'pineapple', 'extra cheese'] 

requested_toppings = ['mushrooms', 'french fries', 'extra cheese'] 

for requested_topping in requested_toppings: 

      if requested_topping in available_toppings: 

            print("Adding " + requested_topping + ".") 
      else: 

        print("Sorry, we don't have " + requested_topping + ".")

print("\nFinished making your pizza!")



available_topping = ['mushrooms','olives','green peppers',
 'pepperoni','pineapple','extra cheese']

ruquested_topping = ['mushrooms','french fries','extra cheese']

for value_requested_topping in requested_topping:

    if value_requested_topping in available_topping:

        print('Adding' + value_requested_topping + '')

    else:

        print('Sorry, we dont have' + value_requested_topping +' .')

print('\nFinished making your pizza')


#练习

login_user = ('admin','tz','hot','sin','title')

for value_login_user in login_user:

    if value_login_user == 'admin':

        print('Hello ' + value_login_user +', would you like to see a status report')

    else:

        print('Hello ' +value_login_user +'thank you for logging in again')

login_user = []

if value_login_user in login_user:

    for value_login_user in login_user:

        if value_login_user == 'admin':

          print('Hello' + value_login_user +', would you like to see a status report')

        else:

           print('Hello' + value_login_user +'thank you for logging in again')

else:

    print('We need to find some users')


current_users = ['admin','user','tz','you','hot']


new_users = ['cos','sin','tin','Admin','User']


for value_new_users in new_users:

    if value_new_users.lower() in current_users:

        print('已使用')

    else:

        print('未使用')

ordinal = [1,2,3,4,5,6,7,8,9]

for value_ordinal in ordinal:

    if value_ordinal == 1:

        print('1th')

    elif value_ordinal == 2:

        print('\n2th')

    elif value_ordinal == 3:

        print('\n3th')

    elif value_ordinal == 4:

        print('\n4th')

    elif value_ordinal == 5:

        print('\n5th')

    elif value_ordinal == 6:

        print('\n6th')

    elif value_ordinal == 7:

        print('\n7th')

    elif value_ordinal == 8:

        print('\n8th')

    else:

        print('\n9th')