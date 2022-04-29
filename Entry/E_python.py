'''
Author: your name
Date: 2022-04-07 08:56:42
LastEditTime: 2022-04-29 10:56:29
LastEditors: Please set LastEditors
Description: 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
FilePath: \Py-test\Entry\E_python.py
'''



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


#  传递任意数量的实参

def make_pizza(*toppings):

    print(toppings)

make_pizza('pepperoni')

make_pizza('mushrooms','green peppers','extra cheese')

def make_pizza(*toppings):

    print('\nMaking a pizza with the following toppings:')

    for topping in toppings:

        print('- ' + topping)

make_pizza('peooeroni')

make_pizza('mushrooms','green peppers', 'extra cheese')


#  结合使用位置实参和任意数量实参

def make_pizza(size, *toppings):

    print('\nMaking a ' + str(size)
          + '-inch pizza with the following topping:')

    for topping in toppings:

        print('- ' + topping.title())

make_pizza(16,'pepperoni')

make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')


#   使用任意数量的关键字

def build_profile(first, last, **user_info):

    profile = {}

    profile['first'] = first

    profile['last'] = last

    for key , value in user_info.items():

        profile[key] = value

    return profile

user_profile = build_profile('albert', 'einstein', 
               location = 'princeton', field = 'physics')

print(user_profile)


#  练习


def  sandwich (*sandwichname):

    print('\n现有三明治为')

    for value in sandwichname:

        print('-' + value.title())

sandwich('jinqingyu')

sandwich('jinqiangyu','shuangdanjipai', 'zhizunjuwuba')

sandwich('shuangdanjipai', 'zhizunjuwuba')


def build_profile(first, last, **user_info):

    profile = {}

    profile['first'] = first

    profile['last'] = last

    for key, value in user_info.items():

        profile[key] = value

    return profile


user_profile = build_profile('kames', 'pop', work = 'int',
                      country = 'china', age = 16)  

print(user_profile)


def build_car(manufacturer, model ,**car_type):

    profile = {}

    profile['manufacturer'] = manufacturer

    profile['model'] = model

    for key, value in car_type.items():

        profile[key] = value

    return profile

user_car = build_car('subaru', 'outback', 
                 color = 'blue', tow_package = True)

print(user_car)



# 将函数存储在模块中

#   导入整个模块

def make_pizza_0427(size,*toppings):

    print('\nMaking a ' + str(size) + 
          '-inch pizza with the following toppings:')

    for topping in toppings:

        print('-' + topping)


import E_python

E_python.make_pizza_0427(16, 'pepperoni')

E_python.make_pizza_0427(12,'mushrooms','green peppers', 'extra cheese')



#  导入特定的函数

from E_python import make_pizza_0427

make_pizza_0427(16, 'pepperoni')

make_pizza_0427(12, 'mushrooms', 'green peppers', 'extra cheese')

#  使用as给模块指定别名

import E_python as p

p.make_pizza_0427(16, 'pepperponi')

p.make_pizza_0427(12, 'mushrooms', 'green peppers', 'extra cheese')

#   导入模块中的所有函数

from  E_python import *

make_pizza_0427(16, 'pepperoni')

make_pizza_0427(12, 'mushrooms', 'green peppers', 'extra cheese')



# 练习

def build_user_0(first, last, **user_info):

    profile = {}

    profile['first'] = first

    profile['last'] = last

    for key, value in user_info:

        profile[key] = value

    return profile



import E_python

from E_python import build_user_0

from E_python import build_user as user

import E_python as mn

from E_python import *


#  类

class Dog():

    def __init__(self, name, age):

        self.name1 = name

        self.age1 = age

    def sit(self):

        print(self.name1.title() + ' is now sitting')

    def roll_over(self):

        print(self.name1.title() + ' rolled over!')
        
my_dog = Dog('willie', 6)

your_dog = Dog('lucy', 3)


print('My dog name is ' + my_dog.name1.title() + '.')

print('My dog is ' + str(my_dog.age1) + ' years old')

my_dog.sit()

print('\nYour dog name is ' + your_dog.name1.title() + ' .')

print('\nYour dog is ' + str(your_dog.age1) + ' years old')

your_dog.sit()

my_dog.roll_over()

# 练习

class Restaurant():

    def __init__(self, restaurant_name, cusine_type):

        self.name = restaurant_name

        self.type = cusine_type

    def describe_restaurant(self):

        print('\n' + self.name.title())

        print(self.type.title())

    def open_restaurant(self):

        print(self.name.title() + ' 正在营业')

restaurant = Restaurant('apple', 'curry')

res = Restaurant('pop', 'james')

rant = Restaurant('loqa', 'kd')

print('\n该餐厅为:' + restaurant.name.title())

print('\n类别为:' +restaurant.type.title())

restaurant.describe_restaurant()

restaurant.open_restaurant()

res.describe_restaurant()

res.open_restaurant()

rant.describe_restaurant()

rant.open_restaurant()


class User():

    def __init__(self, first_name, last_name,):

        self.first = first_name

        self.last = last_name   

    def describe_user(self):

        print('\n用户基本信息:' + self.first.title() + ' 和 ' + self.last.title())

    def greet_user(self):

        print('\n你好' + self.first.title() + ' 个性化为 ' )

user_curry = User('first', 'last')

user_james = User('james', 'lod',)

user_curry.describe_user()

user_curry.greet_user()


user_james.describe_user()

user_james.greet_user()

# 使用类和实例

class Car():

    """一次模拟汽车的简单尝试"""

    def __init__(self, make, model, year):

        """初始化描述汽车的属性"""
        
        self.make =make

        self.model = model

        self.year = year

    
    def get_descriptive_name(self):

        """返回整洁的描述性信息"""

        long_name = str(self.year) + ' ' + self.make + ' ' + self.model

        return long_name.title()

my_new_car = Car('audi','a4', 2016)

print(my_new_car.get_descriptive_name())


#  给属性添加默认值

class Car():

    def __init__(self, make, model, year):

        self.make = make

        self.model = model

        self.year = year

        self.odometer_reading = 0

    def get_descriptive_name(self):

        long_name = str(self.year) + ' ' + self.make + ' ' + self.model

        return long_name.title()

    def read_odometer_reading(self):

        print('This car has ' + str(self.odometer_reading) + ' mules on it')

my_new_car = Car('audi', 'a4', 2017)

print(my_new_car.get_descriptive_name())

my_new_car.read_odometer_reading()


#  修改熟悉的值


my_new_car.odometer_reading = 23

my_new_car.read_odometer_reading()


class Car():

    def __init__ (self, make, model, year):

        self.make = make

        self.model = model

        self.year = year

        self.odometer_reading = 0

    def get_descriptive_name(self):

        long_name = str(self.year) + ' ' + self.make + ' ' + self.model

        return long_name

    def read_odometer(self):

        print('This car has ' + str(self.odometer_reading) + ' mules on it')

    def update_odometer(self, mileage):

        if mileage >= self.odometer_reading:

            self.odometer_reading = mileage
        
        else:

            print('You cant roll back an odometer!')

    def increment_odometer(self, miles):

        self.odometer_reading += miles

my_new_car = Car('audi', 'a4' ,2018)

print(my_new_car.get_descriptive_name())

my_new_car.update_odometer(23500)

my_new_car.read_odometer()

#  通过方法对属性的值进行递增

my_new_car.increment_odometer(150)

my_new_car.read_odometer()

#练习

class Restaurant():

    def __init__ (self, make, type):

        self.make = make

        self.type = type

        self.number_served = 0

    def get_res(self):

        long_res = self.make + ' ' + self.type

        return long_res.title()

    def read_munber(self):

        print('就餐人数为:' + str(self.number_served))

    def set_number_served(self,numbers):

        if numbers >= self.number_served:

            self.number_served = numbers

        else:

            print('请问就餐人数')

    def increment_number_served(self):

        self.number_served += 1

user_1 = Restaurant('ergou', 'yang')

print(user_1.get_res())

user_1.set_number_served(10)

user_1.read_munber()

user_1.increment_number_served()

user_1.read_munber()


class User():

    def __init__ (self, first_name, last_name):

        self.first = first_name

        self.last = last_name

        self.login_attempts = 0

    def describe_user(self):

        print('\n用户基本信息为:' + self.first.title()
              + ' ' + self.last.title())

    def greet_user(self):

        full_name = self.first + ' ' + self.last

        print('\n你好:' + full_name.title())

    def incrment_login_attempts(self):

        self.login_attempts += 1

    def reset_login_attempts(self):

        self.login_attempts = 0

user_u = User('lqo', 'plpo')

user_u.describe_user()

user_u.greet_user()

user_u.incrment_login_attempts()

print(user_u.login_attempts)

user_u.incrment_login_attempts()

user_u.incrment_login_attempts()

print(user_u.login_attempts)

user_u.reset_login_attempts()

print(user_u.login_attempts)




    



