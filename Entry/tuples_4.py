'''
Author: your name
Date: 2022-04-27 10:01:00
LastEditTime: 2022-04-27 10:01:01
LastEditors: Please set LastEditors
Description: 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
FilePath: \Py-test\Entry\tuples_4.py
'''
元组
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