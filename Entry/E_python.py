'''
Author: your name
Date: 2022-04-07 08:56:42
LastEditTime: 2022-04-25 15:21:03
LastEditors: Please set LastEditors
Description: 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
FilePath: \Py-test\Entry\E_python.py
'''

print('HELLO WORLD')

#变量

message = 'Hello Python World'

print(message)

message = 'Hello Python Crash Course world'

print(message)

# 在程序中可随时修改变量的值，而Python将始终记录变量的最新值。

#字符串

name = 'ada lovelace'

print(name.title())

# title()以首字母大写的方式显示每个单词，即将每个单词的首字母都改为大写

# 改为全部大写或全部小写

name = 'Ada Lovelace'

print(name.upper())

print(name.lower())

# 合并(拼接)字符串

first_name = 'ada'

last_name = 'lovelace'

full_name = first_name + ' ' + last_name

print(full_name)

print('Hello,' + full_name.title()+ ' !')

message = 'Hello,' + full_name.title() + ' !'

print(message)

# 制表符和换行符

print('\tPython')  #\t制表符

print('Language:\nPython\nC\nJavaScript') # \n换行符

print('Language: \n\tPython\n\tC\n\tJavaScript')

#删除空白

favorite_language = 'python '

favorite_language

favorite_language.rstrip()  #暂时删除

favorite_language  

# 若要永久删除，必须将删除操作的结果存回到变量中：

favorite_language = 'python '

favorite_language = favorite_language.rstrip()

favorite_language

#剔除字符串的开头空白或同时剔除字符串俩端的空白

favorite_language = '  python  '

favorite_language.rstrip()  #删除末尾空白

favorite_language.lstrip()  #删除开头空白

favorite_language.strip()  #删除俩端空白

#数字

# 整数

2+3

3-2

2*3

3/2

# 俩个乘号代表乘方运算

3 ** 2

3 ** 3

10 ** 6

2 + 3 * 4

(2 + 3) **4

# 浮点数

0.1 + 0.1

0.2 + 0.2

2 * 0.1

2 * 0.2

# 注意，包含的小数位数可能是不确定的

0.2 + 0.1

3 * 0.1

#使用函数str()避免类型错误

age = 25 

message = 'Happy' + str(age) + 'rd Birthday'

message

import this

from debugpy import debug_this_thread


#列表

# Python中，用方括号([])来表示列表，并用逗号来分割其中的元素

bicycles = ['trek', 'cannodale', 'redline', 'specialized']

print(bicycles)

# 访问列表元素

#  列表是有序集合

bicycles = ['trek', 'cannodale', 'redline', 'specilalized']

print(bicycles[0])

print(bicycles[0].title())

#  索引从0开始而非1

print(bicycles[1])

print(bicycles[3])

# 索引指定为-1，可让python返回最后一个列表元素

print(bicycles[-1])

print(bicycles[-2])

# 使用列表中的各个值

bicycles = [' trek ', ' cannonale ',' redline ', ' specialized ']

message = 'My first bicycles was a ' + bicycles[0].lstrip().title()+ '.'

print(message)


# 列表中添加元素

motorcycles = ['honda', 'yamaha', 'suzuki']

print(motorcycles)

motorcycles.append('ducati')  #方法append添加元素至列表末尾

print(motorcycles)

motorcycles = []

motorcycles.append('honda')

motorcycles.append('yamaha')

motorcycles.append('suzuki')

print(motorcycles)

#  列表中插入元素

motorcycles.insert(0, 'ducati')

print(motorcycles)


# 列表中删除元素

#  使用del语句删除元素

motorcycles = ['honda', 'yamaha', 'suzuki']

print(motorcycles)

del motorcycles[0]

print(motorcycles)

#  使用方法pop()删除元素

motorcycles = ['honda', 'yamaha', 'suzuki']

print(motorcycles)

popend_motorcycles = motorcycles.pop()

print(motorcycles)

print(popend_motorcycles)

motorcycles = ['honda', 'yamaha', 'suzuki']

last_owned = motorcycles.pop()

print('The last motorcycles I owned was a ' + last_owned.title() + '.')

#   弹出列表中任何位置处的元素

motorcycles = ['honda', 'yamaha', ' suzuki ']

first_owned = motorcycles.pop(0)

print('The first motorcycle I owned was a ' + first_owned.title().rstrip()+ '.')

#   根据值删除元素

motorcycles = ['honda', 'yamha', 'suzuki', 'ducati']

print(motorcycles)

motorcycles.remove('ducati')

print(motorcycles)

motorcycles = ['honda', 'yamha', 'suzuki', 'ducati']

print(motorcycles)

too_expensive = 'ducati'

motorcycles.remove(too_expensive)

print(motorcycles)

print('\nA ' + too_expensive.title() + 'is too expensive for me.')

#方法remove()只删除第一个指定的值。如果要删除的值可能在列表中出现多次，就需要

#使用循环来判断是否删除了所有这样的值。

list_of_guessts = ['  MRk  ','  ccc  ','  apple  ','  dd  ']

message = '\n\t真诚邀请' + list_of_guessts[0].title().rstrip()+'...'

print(message)

print('\n\t 无法参加的是' + list_of_guessts[-1])

list_of_guessts.insert(3,'ooo')

print(list_of_guessts)

del list_of_guessts[4]

list_of_guessts.append('pp')

last_pepole = list_of_guessts[-1]

print('谢谢' + last_pepole.title().rstrip() + '下次继续')


# 方法sort()对列表进行永久性排序

cars = ['bmw', 'audi', 'toyota', 'subaru']

cars.sort()

print(cars)

cars = ['bmw', 'audi', 'toyota', 'subaru']

cars.sort(reverse = True)  #  顺序相反排序

print(cars)    #修改是永久性的

# 函数sorted() 对列表进行临时排序

cars = ['bmw', 'audi', 'toyota', 'subaru']

print('Here is the original list:')

print(cars)

print('\nHere is the sorted list:')

print(sorted(cars, reverse=True))  #也可以通过True进行反转排序

print('\nHere is the original list again:')

print(cars)

#  倒着打印列表可以用方法reverse()

cars = ['bmw', 'audi', 'toyota', 'subaru']

print(cars)

cars.reverse()   #只是反转列表的排序顺序

print(cars)  #reverse()方法是永久修改 但再次调用即可恢复原样

#  确定列表的长度  函数len()

cars = ['bmw', 'audi', 'toyota', 'subaru']

len(cars)

# 练习

zhz = ['hf','cy','zh','alr','smz','cqm']

print(zhz)

print(sorted(zhz))

print(zhz)

print(sorted(zhz, reverse=True))

print(zhz)

zhz.reverse()

print(zhz)

zhz.reverse()

print(zhz)

zhz.sort()

print(zhz)

zhz.sort(reverse=True)

print(zhz)

#for循环

magicians = ['alice', 'david','carolina']

for magician in magicians:

    print(magician)

# for循环执行更多的操作

maicians = ['alice', 'david', 'carolina']

for magican in maicians:

    print(magican.title() + ' , that was a great trick')

    print("I can 't wait to see your next trick," + magican.title() + ".\n" )

# for循环结束后的操作

magicians = ['alice', 'david', 'carolina']

for magican in magicians:

    print(magican.title() + ' , that was agreat trick')

    print("I can 't wait to see your next trick," +magician.title() + ".\n")


print('Thank you , ereryone. Thar was a great  magic show!')

#练习

pizzaaa =  ['beijingkaoya','heniu','jinqiangyu']

for pizzaa in pizzaaa:

    print(pizzaa.title() + ' I like pepperroni pizza')

    print('I very like pepeerroni pizza')

print(pizzaa.title() + 'I really love pizza')


pizzaaaa = ['beijingkaoya', 'heniu', 'jinqiangyu']

for pizzaaa in pizzaaaa:

    for pizzaa in pizzaaaa:

        print(pizzaa.title() + ' I like pepperroni pizza')

        print('I very like pepeerroni pizza\n')

    print(pizzaaa.title() + 'I really love pizza')

#  使用函数range()

for value in range(1,5):

    print(value)

for value in range(1,6):

    print(value)

# 使用range()创建数字列表

numbers = list(range(1,6))

print(numbers)

even_numbers = list(range(2,11,2))  #从2开始 不断加2 直到终值11

print(even_numbers)

squares = []

for value in range(1,11):

    square = value ** 2

    squares.append(square)

print(squares)

squares = []

for value in range(1,11):

    squares.append(value ** 2)

print(squares)

# 数字列表的统计

numbers = list(range(0,20))

for value in numbers:

     value =sum(numbers)

print(value)

# 列表解析

squares = [value ** 2 for value in range(1,11)]

print(squares)

squares = [value + value for value in range(1,11)]

print(squares)

# 练习

numbers = list(range(1,21))

for value in numbers:

      print(numbers)

numbers = [value for value in range(1,21)]

print(numbers)

numbers = []

for value in range(1,21):

    numbers.append(value)

print(numbers)


numbers = list(range(1,1000001))

for value in numbers:

    print(value)

numbers = list(range(1,1000001))

min(numbers)

max(numbers)

sum(numbers)

even_numbers = list(range(1,21,2))

for value in even_numbers:

    print(value)

even_numbers = list(range(3,31,3))

for value in even_numbers:

    print(value)

even_numbers = list(range(1,11))

for value in even_numbers:

    print(value ** 3) 

numbers = [value ** 2 for value in range(1,11)]

print(numbers)


#切片

players = ['charles', 'martina', 'michael', 'florence', 'eli']

print(players[0:3])

pleyers = ['charles', 'martina', 'michael', 'florence', 'eli']

print(players[1:4])

players = ['charles', 'martina', 'michael', 'florence', 'eli']

print(players[:4])

players = ['charles', 'martina', 'michael', 'florence', 'eli']

print(players[2:])

players = ['charles', 'martina', 'michael', 'florence', 'eli']

print(players[-3:])

# 遍历切片

players = ['charles', 'martina', 'michael', 'florence', 'eli']

print('Here are the first three players on my team : ')

for player in players[:3]:

    print(player.title())

# 复制列表

my_foods = ['pizza', 'falafel', 'carrot cake']

friend_foods = my_foods[:]

print('My favorite foods are: ')

print(my_foods)


print('\nMy friends favorite foods are: ')

print(friend_foods)

my_foods = ['pizza', 'falafel', 'carrot cake']

friend_foods = my_foods[:]

my_foods.append('cannoli')

friend_foods.append('ice cream')

print('My favorite foods are: ')

print(my_foods)


print('\nMy friend favorite foods are: ')

print(friend_foods)

#练习

my_foods = ['pizza', 'falafel', 'carrot cake', 'colo','the']

print('The first three items in the list are\n')

print(my_foods[:3])

print('Three items from the middle of the list are\n')

print(my_foods[1:4])

print('The last three items in the list are\n')

print(my_foods[-3:])

mylike_pizza = ['beij','yidali','meiguo']

worldlike_pizza = mylike_pizza[:]

mylike_pizza.append('moxige')

worldlike_pizza.append('zhongya')


for value_mylike_pizza in mylike_pizza:

    print('My favorite pizza are: ' + value_mylike_pizza)

for value_worldlike_pizza in worldlike_pizza:

    print('My friend favorite pizza are: ' + value_worldlike_pizza)

my_foods = ['pizza', 'falafel', 'carrot cake']

friend_foods = my_foods[:]

my_foods.append('cannoli')

friend_foods.append('ice cream')

for value_my_foods in my_foods:

    print('My like are :' + value_my_foods)

for value_friend_foods in friend_foods:

    print('My friend like are :' + value_friend_foods)

#元组
# 元组不可变 列表可变

dimensions  = (200, 50)

print(dimensions[0])

print(dimensions[1])

# 遍历元组中的所有值

dimensions =(200 ,50)

for value_dimensions in dimensions:

    print(value_dimensions)

#修改元组变量

dimensions = (200 ,50)

print('Original dimensions: ')

for value_dimensions1 in dimensions:

    print(value_dimensions1)

dimensions = (400 ,100)

print('\nModified dimensions:')

for value_dimensions2 in dimensions:

    print(value_dimensions2)

#练习

cat_foods = ('kaoya','huoguo','niupai','haixian','malatang')

print('今日供应：')

for value_cat_foods1 in cat_foods:

    print(value_cat_foods1)

cat_foods = ('kaoya', 'roubing', 'yangpai','haixian','malatang')

print('明日供应：')

for value_cat_foods2 in cat_foods:

    print(value_cat_foods2)

#if语句

cars = ['audi', 'bmw', 'subaru','toyota']

for value_cars in  cars:

    if value_cars == 'bmw':

        print(value_cars.upper())

    else:

        print(value_cars.title())

#  条件测试

car = 'bmw'

car == 'bmw'

car = 'bmw'

car == 'audi'

# 检查是否相等时不考虑大小写

car = 'Audi'

car == 'audi'

car = 'Audi'

car.lower() == 'audi'

car = 'audi'

car.upper() == 'AUDI'

car.title() == 'Audi'

car

# 检查是否不相等

requested_topping = 'mushrooms'

if requested_topping != 'anchovies':

   print('Hold the anchovices!')

#  比较数字

age = 18

age == 18

age = 20

age != 21

answer = 17

if answer != 42:

    print('The is not the correct answer. Please try again!')

age = 19

age < 21

age <= 21

age > 21

age >= 21

# 检查多个条件 and

age_0 = 22

age_1 = 18

age_0 >= 21 and age_1 >= 21

age_1 = 22

age_0 >= 21 and age_1 >=21

age_0 = 24

age_1 = 21

(age_0 >= 21) and (age_1 >= 21)


# 使用or检查多个条件

age_0 = 22

age_1 = 18

age_0 >= 21 or age_1 >= 21


age_0 = 18

(age_0 >= 21) or (age_1 >= 21)

#  检查特定值是否包含在列表中

requested_topping = ['mushrooms', 'onions', 'pineapple']

'mushrooms' in requested_topping

'pepperoni' in requested_topping

# 检查特定值是否不包含在列表中

banned_users = ['andrew','carolina','david']

user = 'marie'

if user not in banned_users:

    print(user.title() + ' , you can post a response if you wish. ')

# 练习

car_0 = 'Apple'

car_0 == 'apple'

car_0 != 'pp'

car_0.lower() == 'apple'

car_0.upper() == 'Apple'

car_1 = 15

car_2 = 20

car_1 == car_2

car_1 != car_2

car_1 >= car_2

car_1 <= car_2

(car_1 >= 15) and (car_2 >= 20)

(car_1 <= 15) or (car_2 >= 30)

eat_topping = ['Apple','Bmw','Car']

'apple' in eat_topping

'Apple' in eat_topping

eat_topping = ['Apple','Bmw','Car']

eat_user = 'cc'

if eat_user not in eat_topping:

    print(eat_user.title() + ' , 确实不在')


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

# 字典

alien_0 = {'color': 'green', 'points': 5}

print(alien_0['color'])

print(alien_0['points'])

new_points = alien_0['points']

print('You just earned'+ str(new_points) + 'points!')

# 添加键值对

alien_0 = {'color':'green','points':5}

print(alien_0)

alien_0['x_position'] = 0

alien_0['y_position'] = 25

print(alien_0)
 

#  空字典

alien_0 = {}

alien_0 ['color']  = 'green'

alien_0 ['points'] = 5

print(alien_0)


# 修改字典中的值

alien_0 = {'color':'green'}

print('The alien is '+ alien_0 ['color'] + '.')

alien_0 ['color'] = 'yellow'

print('The alien is now ' + alien_0 ['color'] + '.')


alien_0 = {'x_position':0, 'y_position':25, 'speed':'fast'}

print('Original x_position: ' + str(alien_0 ['x_position']))

#向右移动外星人

#据外星人当前速度觉得将其移动多远

if alien_0 ['speed'] =='slow':

    x_increment = 1

elif alien_0 ['speed'] == 'medium':

    x_increment = 2

else:

    #这个外星人的速度一定很快

    x_increment = 3

# 新位置等于老位置加上增量

alien_0 ['x_position'] = alien_0 ['x_position'] + x_increment

print('New x_position: ' + str(alien_0 ['x_position']))

# 删除键值对

alien_0 = {'color':'green', 'points': 5}

print(alien_0)

del alien_0 ['points']

print(alien_0)

#删除的键值对永远消失

# 由类似对象组成的字典

favorite_languages ={
   'jeb':'Python', 
   'sarah':'C',  
   'edward':'ruby',  
   'phil':'Python',
}

print(favorite_languages)

print('Sarah favorite language is ' +
    favorite_languages ['sarah'].lower() + 
    '.'        
)

#练习

friends_0 = {'first_name':'w', 
             'lat_name':'ll', 
             'age': 26, 
             'city':'ly',
}

print(friends_0)


like_number ={'kobe':24,
              'jojon':23,
              'james':23,
              'curry':30,
              'kd':35,
              }

print(friends_0)


cihui_0 ={
          'lower':'全部小写',
          'title':'首字母大写',
          'upper':'全部大写',
          'str':'转换字符串',
          '[]':'列表',
          '()':'元组',
          '{}':'字典'
}

print('lower的含义是'+
      str(cihui_0['lower']) +
      '\ntitle的含义是'+
      str(cihui_0['title']) +
      '\nupper的含义是'+
      str(cihui_0['upper']) +
      '\n[]的含义是'+
      str(cihui_0['[]']) +
      '\n()的含义是'+
      str(cihui_0['()']) +
      '\n{}的含义是'+
      str(cihui_0['{}'])
)

# 遍历字典

user_0 ={
    'username':'efermi',
    'first':'enrico',
    'last':'fermi',

}

for ley ,value in user_0.items():

    print('\nKey:' + ley)

    print('Value:' + value)

favorite_languages = {
    'jen':'Python',
    'sarah':'C',
    'edward':'rudy',
    'phil':'python'
}

for name,language in favorite_languages.items():

    print(name.title() + ' S favorite language is ' +
          language.title() +'.')


# 遍历字典中的所有键

favorite_languages = {
    'jen':'python',
    'sarah':'c',
    'edward':'ruby',
    'phil':'python',
}

for name in favorite_languages.keys():

    print(name.title())


favorite_languages ={
    'jen':'python',
    'sarah':'c',
    'edward':'ruby',
    'phil':'python',
}

friends = ['phil','sarah']

for name in favorite_languages.keys():

    print(name.title())

    if name in friends:

     print('Hi ' +name.title() +
          ', I see your favorite language is ' +
        favorite_languages[name].title() +'!')


favorite_languages ={
    'jen':'python',
    'sarah':'c',
    'edward':'ruby',
    'phil':'python',
}

if 'erin' not in favorite_languages.keys():

    print('Erin, please take our poll !')


favorite_languages ={
    'jen':'python',
    'sarah':'c',
    'edward':'ruby',
    'phil':'python',
}

for name in sorted(favorite_languages.keys()):

    print(name.title() + ' , thank you for taking the poll.')

# 遍历字典中的所有值

favorite_languages = {
    'jen':'python',
    'sarah':'c',
    'edward':'ruby',
    'phil':'python',     
}

print('The following languages have been mentioned:')

for language in favorite_languages.values():

    print(language.title())


favorite_languages = {
    'jen':'python',
    'sarah':'c',
    'edward':'ruby',
    'phil':'python'
}

print('The following languages have been mentioned:')

for language in set(favorite_languages.values()):

    print(language.title())

#练习

cihui_0 ={
          'lower':'全部小写',
          'title':'首字母大写',
          'upper':'全部大写',
          'str':'转换字符串',
          '[]':'列表',
          '()':'元组',
          '{}':'字典',
          'items':'字典的键值对方法',
          'keys':'字典中键',
          'values':'字典中值',
          'sroted':'排序函数',
          'set':'序列'
}

for n, v in cihui_0.items():

    print(str(n) +'\t含义为: ' +str(v))


rivers_0 = {
    'China':'Yangtze',
    'Egypt':'Nile',
    'Germany':'Danube',
}

for name,value in sorted(rivers_0.items()):

    print('\nThe ' + name.title() +' runs through '+ value.title())

for value in sorted(rivers_0.values()):

    print('\n该河流的大写是:' + value.upper())

for name in sorted(rivers_0.keys()):

    print('\n该国家的大写是:' + name.upper())


favorite_languages = {
    'jen':'python',
    'sarah':'c',
    'edward':'rudy',
    'phil':'python',
    'mark':'c++',
    'evrn':'MySQL',
}

personnel = ['phil','mark']

for name in sorted(favorite_languages.keys()):

    print(name.title())

    if name in personnel:

        print('Hi\t'+ name.title() +'musst receive an investigation ' +
             favorite_languages[name]+ '.\n')
    
    else:

        print('Go back\n')


#嵌套

# 字典列表

alien_0 = {'color':'green', 'points': 5}

alien_1 = {'color':'yellow', 'points':10}

alien_2 = {'color':'red','points':15}

aliens = [alien_0, alien_1, alien_2]

for value_alien in aliens:

    print(value_alien)


#   创建一个用于存储外星人的空列表

aliens = []

#    创建30个绿色的外星人

for value_alien in range(30):

    new_alien = {'color':'green', 'points':5, 'speed':'slow'}

    aliens.append(new_alien)

#      显示前五个外星人

for five_alien in aliens [:5]:

    print(five_alien)

print('...')

#       显示创建了多少个外星人

print('Total number of aliens: ' + str(len(aliens)))


aliens = []

for aliens_number in range(0 ,30):

    new_alien = {'color':'green', 'points':5, 'speed':'slow',}

    aliens.append(new_alien)

for update_aliens in aliens[0:3]:

    if update_aliens['color'] == 'green':

        update_aliens['color'] = 'yellow'

        update_aliens['speed'] = 'medium'

        update_aliens['points'] = 10

    elif update_aliens['color'] == 'yellow':

        update_aliens['color'] = 'red'

        update_aliens['speed'] = 'fast'

        update_aliens['points'] = 15


for five_aliens in aliens[0:5]:

    print(five_aliens)

print('...')

#  字典中存储列表

#   存储所点披萨的信息

pizza = {
    'crust':'thick',
    'topping':['mushrooms', 'extra cheese'],
}

#    概述所点的披萨

print('You ordered a ' + pizza['crust'] + ' -crust pizza' +
     'with the following topping:') 

for value_topping in pizza['topping']:

    print('\t' + value_topping)


favorite_languages ={
    'jen':['python','ruby'],
    'sarah':['c'],
    'edward':['ruby','go'],
    'phil':['python','haskell'],
}

for name,languages in sorted(favorite_languages.items()):

    print('\n' + name.title() + ' favorite languages are :')

 
     
    for language in languages:

        print('\t' + language.title())


# 在字典中存储字典

users = {
    'aeinstein':{
        'first':'albert',
        'last':'einstein',
        'location':'princeton',
    },

    'mcurie':{
        'first':'marie',
        'last':'curie',
        'location':'paris',
    },
}

for username, user_info in users.items():

    print('\nUsername:' + username)

    full_name = user_info['first'] + '---' + user_info['last']

    location = user_info['location']

    print('\t Full name: ' + full_name.title())

    print('\t Location: ' + location.title() )


#练习

acquaintance_0 = {
    'first':'mark',
    'last':'evrn',
}


acquaintance_1 = {
    'first':'james',
    'last':'wede',
}

acquaintance_2 = {
    'first':'curry',
    'last':'green',
}


people = [acquaintance_0,acquaintance_1,acquaintance_2]

for value in people:

    print(value)


raddit = {
    'type':'a',
    'master':'mark',
}

turtles = {
    'type':'b',
    'master':'evrn',
}

bear = {
    'type':'c',
    'master':'james',
}

pets = [raddit, turtles, bear,]

for value_pets in pets:

    print(value_pets)


favorite_language = {
    'mark':['shanghai','shenzhen','shenyang'],
    'james':['jiuzaigou','zhangjiajie',],
    'jorin':['gonggashan','huashan','taishan',],
}

for name,like in sorted( favorite_language.items()):

    print('\nThe ' + name.title() + ' like is :')

    for value_like in like:

        print('\n' + value_like.title())

numbers = {
    'mark':[3,9,10],
    'james':[23,24],
    'jorin':[100,1000]
}

for name, like_numbers in sorted(numbers.items()):

    print('\n  The ' + name.title() + ' like is :')

    for value_like_numbers in like_numbers:

        print('\n' + str(value_like_numbers))


cities = {
    'beijing':{
        'country':'china',
        'population':40000000,
        'fact':'imperial palace',
    },
    'newwork':{
        'country':'united states',
        'population':3000000,
        'fact':'central park',
    },
    'paris':{
        'country':'france',
        'population':1500000,
        'fact':'notre dame cathedral',
    }
}

for city, information in sorted(cities.items()):

    print('\nCity name: ' + city.title())

    value_country = information['country']

    value_population = information['population']

    value_fact = information['fact']

    print('\t  Country: ' + value_country)

    print('\t  Population: ' + str(value_population))

    print('\t  Fact: ' + value_fact)


# 函数input()的工作原理

message = input('The me somthing, and I will repeat it back to you:')

print(message)


# 编写清晰的程序

name = input('Please enter your name: ')

print('Hello ' + name.title() + ' !')


prompt = 'If you tell us who you are, we can personalize the messages you see'

prompt += '\nWhat is your first name?'

name = input(prompt)

print('\nHello, ' + name.upper() + ' !')

# 使用int()来获取数值输入

age = input('How old are you?')

age = int(age)

age >= 18

height = input('How tall are you, ininches?')

height = int(height)

if  80 > height >= 36:

    print('\nYou are tall enough to ride!')

elif height >=80:

    print('\n be careful')

else:

    print('\n no')


# 求模运算符

4%3

5%3

6%3

7%3


number = input('Enter a number, and I tell you if it is even or odd')

number = int(number)

if number % 2 == 0:

    print('\n The number ' + str(number) + ' is even.')

else:

    print('\n The number ' + str(number) + ' is odd.')

#练习

car_0 = input('what kind of car to rent?')

print('Let me see if i can find you a '+ car_0.upper())

eat_0 = input('How many people eat?')

eat_0 = int(eat_0)

if eat_0 > 8:

    print('no no no ' + str(eat_0) +'too much')

else:

    print('please the ' + str(eat_0) + ' eat')


number = input('Please tell number ')

number = int(number)

if number % 10 == 0:

    print('\n The number ' + str(number) + ' is 10 integer !')

else:

    print('\n The number ' + str(number) + ' is not 10 integer ! ')


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

    message = input(pizz_0)

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


#定义函数


def green_user():

    """显示简单的问候语"""

    print('Hello!')

green_user()


#向函数传递信息

def greet_user(username):

    print('Hello,' + username.title() + '!')

greet_user('curry')

greet_user('jams')


# 实参与形参

def display_message():

    print('实参与形参')


def favorite_book(title):

    print('One of my favorite books is '+ title.title()+' in Wonderland')

favorite_book('apple')

favorite_book('banana')

# 传递实参

#   位置实参

def describe_pet(animal_type, pet_name):

    """显示宠物的信息"""

    print('\nI have a ' + animal_type + ' .')
    print('My' + animal_type + ' name is ' + pet_name.title() + ' .')

describe_pet('hamster', 'harry')

describe_pet('dog', 'willie')


#   关键字实参

def describe_pet(animal_type, pet_name):

    """显示宠物的信息"""

    print('\nI have a ' + animal_type + ' .')

    print('My ' + animal_type + ' name is ' + pet_name.title() + ' .')

describe_pet(animal_type= 'hamster', pet_name='harry')

 
#    默认值

def describe_pet(pet_name, animal_type='dog'):

    print('\nI have a ' + animal_type + ' .')

    print('My ' + animal_type + ' name is ' + pet_name.title())

describe_pet(pet_name='willie')

describe_pet('olo')


#   等效函数的调用

def describe_pet(pet_name, animal_type='dog'):

    print('\nI have a ' + animal_type + ' .')

    print('My ' + animal_type + ' name is ' + pet_name.title() + ' .')

describe_pet('willie')

describe_pet(pet_name= 'willie')


describe_pet('harry', 'hamster')

describe_pet(pet_name = 'harry', animal_type = 'hamster')

describe_pet(animal_type = 'hamster', pet_name = 'harry')


# 练习

def make_shirt(size, words='I love Python'):

    print('T恤的尺码是: ' + str(size) + ' 字样是： ' + words.title())

make_shirt(20, 'apple')

make_shirt(32)

make_shirt('大号')

make_shirt(size = '中号')

make_shirt(words = 'apple', size = '中号')


def  describe_city(city, country = 'china'):

    print(city.title() +' is in ' + country.upper())

describe_city('shanghai')

describe_city('beijing')

describe_city(city = 'newyork', country = 'usa')

#返回值

# 返回简单值

def get_formatted_name(first_name, last_name):

    """返回整洁的姓名"""

    full_name = first_name + ' '+last_name

    return full_name.title()

musician = get_formatted_name('jimi', 'hendrix')

print(musician)


# 让实参变成可选的

def get_formatted_name(first_name, middle_name, last_name):

    fullname = first_name + ' '+ middle_name +' '+ last_name

    return fullname.title()

musician = get_formatted_name('join', 'lee', 'hooker')

print(musician)


def get_formatted_name(first_name, last_name, middle_name=''):

    if middle_name:

        full_name = first_name +' '+ middle_name + ' '+ last_name

    else:

        full_name = first_name + ' ' + last_name

    return full_name.title()

musician = get_formatted_name('jimi', 'hendrix')

print(musician)

musician = get_formatted_name('john', 'hooker', 'lee')

print(musician)


#  返回字典

def build_person(first_name, last_name):

    person = {'first': first_name, 'last':last_name}

    return person

musician = build_person('jimi', 'hendrix')

print(musician)


def build_person(first_name, last_name, age=''):

    person = {'first':first_name, 'last':last_name}

    if age:

        person['age_0'] = age

    return person

musician = build_person('jimi','hendrix', age=27)

print(musician)

# 结合使用函数和while循环

def get_formatted_name(first_name, last_name):

    full_name = first_name + ' ' + last_name

    return full_name


while True:

    print('\nPlease tell me your name:')

    print("(enter 'q' at any time to quit!)")

    f_name = input('First name:')

    if f_name == 'q':

        break

    l_name = input('Last name:')

    if l_name == 'q':

        break

    formatted_name = get_formatted_name(f_name, l_name)

    print('\nHello, '+ formatted_name.title() + ' !')


def city_country(country, city):

    c_c = country + ', ' +city

    return c_c

city_cou =city_country('china','beijing')

print(city_cou.title())

city_cou = city_country('usa', 'newyork')

print(city_cou.upper())

city_cou = city_country('FRANCE', 'PARIS')

print(city_cou.lower())



def make_album(album, singer,song_number = ''):

    person = {'album':album, 'singer':singer}

    if song_number:

        person['song_number'] = song_number

    return person

message = make_album('pop','lol')

print(message)

message = make_album('aa','cc','9')

print(message)

message =make_album(singer='lml', song_number='10', album ='upu',)

print(message)

while True:

    print('\n Please tell your like album information')

    print("(enter 'quit' at any time to quit)")

    a_album = input('Tell album')

    if a_album == 'quit':

        break
    
    s_singer = input('Tell singer')

    if s_singer == 'quit':

        break

    s_song_number = input('Tell song_number')

    if s_song_number == 'quit':

        break

    information = make_album(a_album, s_singer,s_song_number)

    print('\nHello, ' + str(information) + ' !')


#  传递列表

def greet_users(names):

    """向列表中的每个用户都发出简单的问候"""

    for name in names:

        msg = 'Hello, ' + name.title() + '!'

        print(msg)


usernames = ['hannah', 'ty', 'margot']

greet_users(usernames)


#   首先创建一个列表，其中包含一些要打印的设计

unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron',]

completed_models = []

#    模拟打印每个设计，直到没有未打印的设计为止
#    打印每个设计后，都将其移到列表compleeted_models中

while unprinted_designs:

    current_design = unprinted_designs.pop()

    #模拟根据设计制作3D打印模型的过程

    print('Printing model:' + current_design)

    completed_models.append(current_design)

#   显示打印好的所有模型

print('\nThe following models have been printed:')

for completed_model in completed_models:

    print(completed_model) 
  

def print_models(unprinted_designs, completed_models):

    """
    模拟打印每个设计，直到没有未打印的设计为止
    打印每个设计后, 都将一道列表completed_models中
    
    """

    while unprinted_designs:

        current_design = unprinted_designs.pop()

        # 模拟根据设计制作3D打印模型的过程

        print('Printing model:' + current_design)

        completed_models.append(current_design)


def show_completed_models(comp):

    """显示打印好的所有模型"""

    print('\nThe following models have been printed:')

    for value_completed_models in comp:

        print(value_completed_models)

unprinted_designs = ['iphone case', 'robot', 'dodecahedron']

completed_models = []

print_models(unprinted_designs, completed_models)

show_completed_models(completed_models)


# 禁止函数修改列表

def print_models(unprinted_designs,completed_models):

    while unprinted_designs:

        current_design = unprinted_designs.pop()

        print('Printing model: ' + current_design)

        completed_models.append(current_design)



def show_completed_models(completed_models):

    print('\nThe following models have been printed:')

    for value in completed_models:

        print(value)

unprinted_designs = ['iphone case', 'robot pendant', 'doedcahedron']

completed_models = []

print_models(unprinted_designs[:], completed_models)

show_completed_models(completed_models)

print(unprinted_designs)



#练习

def show_magicians(magicians):

    for name in magicians:

        print('\nHello, '+ name.title())


magicians = ['dante','vergil','leo',]

make_great(magicians)

magicians

def show_magicians(magicians):

    for name in magicians:

        print('\nHello: ' + name.title())

def make_great(update_magicians):

    n = len(update_magicians)

    for i  in range(0,n):

        update_magicians[i] = update_magicians + ' the Great'

        print(update_magicians[i])

    return update_magicians

update_magicians = ['dante', 'vergil', 'leo']

make_great(update_magicians)


def show_magicians(magicians):

    for value in magicians:

        print('\nHello, ' + value.title())

def make_great(update_magicians,):

    n = len(update_magicians)

    for i in range(0, n):

        update_magicians[i] = update_magicians[i] + ' the Great'

        print(update_magicians[i])

    return update_magicians

magicians = ['dante','vergil', 'leo']

value_update_magicians = []

value_update_magicians = make_great(magicians[:])

show_magicians(magicians)

show_magicians(value_update_magicians)

print(magicians)

print(value_update_magicians)


def show_magicians(names):

    for name in names:

        msg = ('\nHello: ' + name.title() + ' !')

        print(msg)

names = ['caofu', 'wangshi', 'pop']

show_magicians(names)


magicians = ['caofu', 'wangshi','magicians']

great_magicians = []

def make_great(magicians, great_magicians):

    while magicians:

        magician = magicians.pop()

        great_magician = magician + ' the Great'

        great_magicians.append(great_magician)

def show_magicians(great_magicans):

    for name in great_magicans:

        msg = ('\nHello: ' + name + ' !')

        print(msg)

make_great(magicians, great_magicians)

show_magicians(great_magicians)


magicians = ['curry', 'james', 'magic',]

great_magicians = []

def make_great(m,g):

    while m:

        mag = m.pop()

        great = mag + ' the Great'

        g.append(great)

def  show_magician(great_0):

    for name in great_0:

        msg = ('\nHello, ' + name + ' !')

        print(msg)

make_great(g=great_magicians, m=magicians[:])

show_magician(great_magicians)

show_magician(magicians)