'''
Author: your name
Date: 2022-04-27 09:57:55
LastEditTime: 2022-04-27 09:58:58
LastEditors: Please set LastEditors
Description: 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
FilePath: \Py-test\Entry\last.py
'''
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
