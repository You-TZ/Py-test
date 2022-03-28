'''
Author: your name
Date: 2022-03-24 09:02:32
LastEditTime: 2022-03-24 17:11:23
LastEditors: Please set LastEditors
Description: 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
FilePath: \sss\python-3-iterate.py
'''
#如果给定一个list或tuple，我们可以通过for循环来遍历这个list或tuple，这种遍历我们称为迭代（Iteration）。
#在Python中，迭代是通过for ... in来完成的，而很多语言比如C语言，迭代list是通过下标完成的，比如C代码：

#for (i = 0 ; i < length ; i ++){
 #   n = list[i];
#}

#可以看出，Python的for循环抽象程度要高于C的for循环，
# 因为Python的for循环不仅可以用在list或tuple上，还可以作用在其他可迭代对象上。

#list这种数据类型虽然有下标，但很多其他数据类型是没有下标的，
# 但是，只要是可迭代对象，无论有无下标，都可以迭代，比如dict就可以迭代：

d = {'a':1,'b':2,'c':3}

for key in d:

    print(key)

#因为dict的存储不是按照list的方式顺序排列，所以，迭代出的结果顺序很可能不一样。

#默认情况下，dict迭代的是key。如果要迭代value，可以用for value in d.values()，

# 如果要同时迭代key和value，可以用for k, v in d.items()。

#由于字符串也是可迭代对象，因此，也可以作用于for循环：

d = {'a':1,'b':2,'c':3,'d':4}

for  v in d.values():

    print(v)

for k , v in d.items():

    print(k , v)

for ch in 'ABCDE':

    print(ch)

#所以，当我们使用for循环时，只要作用于一个可迭代对象，for循环就可以正常运行，

# 而我们不太关心该对象究竟是list还是其他数据类型。

#那么，如何判断一个对象是可迭代对象呢？方法是通过collections.abc模块的Iterable类型判断：

from collections.abc import Iterable
from re import A

isinstance ('abc' , Iterable)

isinstance ([1 , 2 , 3] , Iterable)

isinstance (123 , Iterable)

#如果要对list实现类似Java那样的下标循环怎么办？

# Python内置的enumerate函数可以把一个list变成索引-元素对，

#这样就可以在for循环中同时迭代索引和元素本身：

for i , value in enumerate (['A','B','C']):

    print(i , value)

#上面的for循环里，同时引用了两个变量，在Python里是很常见的，比如下面的代码：

for x , y in [(1,3),(2,4),(3,6)]:

    print(x , y)




def findMinAndMax(L):

    min = None

    max = None

    if len(L) != 0 :

        min = L [0]

        max = L [0]

        for v in L :

            if (min > v) :

                min = v
            
            if (max < v) :

                max = v
    
    return min , max

# 测试
if findMinAndMax([]) != (None, None):
    print('测试失败!')
elif findMinAndMax([7]) != (7, 7):
    print('测试失败!')
elif findMinAndMax([7, 1]) != (1, 7):
    print('测试失败!')
elif findMinAndMax([7, 1, 3, 9, 5]) != (1, 9):
    print('测试失败!')
else:
    print('测试成功!')
    




def findMinAndMax(L):
    
    min = None

    max = None

    if len(L) != 0:

        min = L[0]

        max = L[0]

        for value in L:

            if(min > value):

                min = value

            if(max < value):

                max = value

    return min,max



