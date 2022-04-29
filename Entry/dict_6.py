'''
Author: your name
Date: 2022-04-27 10:03:00
LastEditTime: 2022-04-27 10:03:00
LastEditors: Please set LastEditors
Description: 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
FilePath: \Py-test\Entry\dict_6.py
'''
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
