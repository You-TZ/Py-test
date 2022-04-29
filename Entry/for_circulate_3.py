'''
Author: your name
Date: 2022-04-27 09:59:50
LastEditTime: 2022-04-27 09:59:51
LastEditors: Please set LastEditors
Description: 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
FilePath: \Py-test\Entry\for_circulate_3.py
'''
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