'''
Author: your name
Date: 2022-04-27 10:04:12
LastEditTime: 2022-04-27 10:05:22
LastEditors: Please set LastEditors
Description: 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
FilePath: \Py-test\Entry\while_circulate_7.py
'''
# while循环

current_number = 1

while current_number <= 5:

    print(current_number)

    current_number += 1

# 让用户选择何使退出

prompt = '\nTell me somthing, and I will repeat it back to you:'

prompt = '\nEnter QUIT to end the program'

message = ''

while message != 'qiut':

    message = input(prompt)

    print(message)


prompt = '\nTell me somthing, and I will repeat it back to you:'

prompt = '\nEnt quit to end the program'

message = ''

while message != 'quit':

    message = input(prompt)

    if message != 'quit':

        print(message)

# 使用标志

prompt = '\nTell me somthing, and I will repeat it back to you:'

prompt = '\nEnter quit to end the program'

active = True

while active:

    message = input(prompt)

    if message == 'quit':

        active = False

    else:

        print(message)

# 使用break退出循环

prompt = '\nPlease enter the name of a city you have visited:'

prompt = '\n(Enter quit whem you are finished.)'

while True:

    city = input(prompt)

    if city == 'quit':

        break

    else:

        print('I love to go to ' + city.title() + '!')


# 在循环中使用continue

current_number = 0 

current_number = input()

current_number = int(current_number)

while current_number < 10:

    current_number += 1

    if current_number % 2 == 0:

        continue

    print(current_number)

# 避免无限循环

x = 1 

while x <= 5:

    print(x)

    x += 1

# 练习

pizza_0 = '\n请输入你要的配料'

message = ''

while message != 'quit':

    message = input(pizza_0)

    if message == 'quit':

        print('\n谢谢光临')

    else:

        print('\t您点的配料为'+ message.title()+ '!')


age_0 = input('\n请问您的年龄是多少？')

age_0 = int(age_0)

for  value in age_0:
    
    if value < 3:

        print('\n您的年龄为： ' + str(value)+ ' 免费') 

    elif 3 <=  value < 12:

        print('\n您的年龄为： ' + str(value)+ ' 票价为10')

    else:

        print('\n您的年龄为： ' + str(value) + ' 票价为15')

age_0 = '\n你的年龄是多少？'

while True :

    money = input(age_0)

    moneg = int()

    if money == int():

        if money < 3:

            print('\n你的年龄为' + str(money) + '  票价为免费')

        elif 3 <= money < 12:

            print('\n你的年龄为： ' + str(money) + '  票价为10')

        else:

            print('\n你的年龄为：' + str(money) + ' 票价为15')

    else:

        break


age_0 = '\n你的年龄是多少?'

for money in age_0:

    money = input(age_0)

    moneg = int()

    if money < 3:

            print('\n你的年龄为' + str(money) + '  票价为免费')

    elif 3 <= money < 12:

            print('\n你的年龄为： ' + str(money) + '  票价为10')

    else:

            print('\n你的年龄为：' + str(money) + ' 票价为15')


pizza_0 = '\n请输入你要的披萨配料?'

acitve = True

while active:

    message = input(pizza_0)

    if message == 'quit':

        active = False

    else:

        print(message)


pizza_0 = '\n请输入您要的披萨配料?'

active_0 = True

while active_0:

    message = input(pizza_0)

    if message == 'quit':

        acitve_0 = False

    else:

        print(message)


pizz_0 = '\n请输入你要的披萨配料?'

while True:

    message = input(pizz_0)

    if message =='quit':

        break

    else:

        print(message)


pizz_0 = '\n请输入你要的披萨配料'

message = ''

while message != 'quit':

    message = input(pizza_0)

    if message != 'quit':

        print(message)


age_0 = input('\n 您的年龄是？')

message = int(age_0)


if message < 3:

        print('免费')

elif   3 <= message < 12:

        print('10')

else:

        print('15')


age_c = input()

age_c = int(age_c)

while age_c :

    if age_c < 3:

        print('1')

        break

    elif  3 <= age_c < 12:

        print('10')

        break

    else:

        print('年龄为：' +str(age_c) + '!')

        break


# 使用while循环来处理列表和字典

# 在列表之间移动元素

#    首先创建一个待验证的用户列表
#     和一个用于存储已验证用户的空列表

unconfirmed_users = ['alice','brian','candace']

confirmed_users = []

#     验证每个用户，直到没有未验证用户为止
#      将每个经过验证的列表都移到已验证用户列表中

while unconfirmed_users:

    current_user = unconfirmed_users.pop()

    print('Verifying user: ' + current_user.title())

    confirmed_users.append(current_user)

#    显示所有已验证的用户

print('\nThe following users have been confirmed: ')

for value_confirmed_users in confirmed_users:

    print(value_confirmed_users.title())

#  删除包含特定值的所有列表元素

pets = ['dog','cat','dog','goldfish','cat','rabbit','cat']

print(pets)

while 'cat' in pets:

    pets.remove('cat')

print(pets)

# 使用胡勇输入来填充字典

responses = {}

#  设置一个标志, 指出调查是否继续

polling_active = True

while polling_active:

    #提示输入被调查者的名字和回答：

    name = input('\nWhat is your name?')

    response = input('\nWhich mountaion would you like to climb someday?')

    #将答卷存储在字典中

    responses[name] = response

    #看看是否还有人药参与调查

    repeat = input('Wpuld you like to let another person respond? (yes/ no)')

    if repeat == 'no':

        polling_active = False

# 调查结束，显示结果

print('\n --- Poll Results ---')

for name,response in responses.items():

    print(name + ' would like to climb' + response + '.')

#练习

sandwich_orders = ['金枪鱼三明治', '鸡排三明治','牛肉三明治']

finished_sanwiches = []

while sandwich_orders:
   
    moveyuansu = sandwich_orders.pop()

    print('\n' + str(moveyuansu))

    print('I made your tuna sandwich')

    finished_sanwiches.append(moveyuansu)

print('\n已经制作好的三明治'+ str(finished_sanwiches))


sandwich_orders = ['jinqiangyu','pastrami','jipai','niurou',
'pastrami', 'pastrami','niurou','jipai',]

print('\n五香牛肉卖完了')

while  'pastrami' in sandwich_orders:

    sandwich_orders.remove('pastrami')

print(sandwich_orders)


resort = {}

resort_active = True

while resort_active:

    name = input('\nWhat is your name?')

    place = input('\nwhere is your want go?')

    resort[name] = place

    consultation = input('\n (yes or no)')

    if consultation == 'no':

        resort_active = False


print('\n--- investigation closed ---')

for name,value in sorted(resort.items()):

    print(name.title() + ' 欢迎：' +value.title())
