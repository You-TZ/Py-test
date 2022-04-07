'''
Author: your name
Date: 2022-03-29 09:52:55
LastEditTime: 2022-03-30 10:21:58
LastEditors: Please set LastEditors
Description: 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
FilePath: \Py-test\L-Python\python-3-Iterators.py
'''

#可以直接作用于for循环的数据类型有以下几种：

#一类是集合数据类型，如list、tuple、dict、set、str等；

#一类是generator，包括生成器和带yield的generator function。

#这些可以直接作用于for循环的对象统称为可迭代对象：Iterable。

#可以使用isinstance()判断一个对象是否是Iterable对象：

from collections.abc import Iterable
from typing import Iterator

isinstance ([], Iterable)

isinstance ({}, Iterable)

isinstance ('abc', Iterable)

isinstance ( (x * x for x in range(10)), Iterable )

isinstance (100, Iterable)

isinstance (range(10), Iterable)

#生成器不但可以作用于for循环，还可以被next()函数不断调用并返回下一个值，

#直到最后抛出StopIteration错误表示无法继续返回下一个值了。

#可以被next()函数调用并不断返回下一个值的对象称为迭代器：Iterator。

#可以使用isinstance()判断一个对象是否是Iterator对象：

isinstance (iter([]), Iterator)

isinstance (iter('abc'), Iterator)

isinstance (iter(range(10)), Iterator)

isinstance ((range(10)), Iterator)

#为什么list、dict、str等数据类型不是Iterator？

#因为Python的Iterator对象表示的是一个数据流，Iterator对象可以被next()函数调用并不断返回下一个数据，

#直到没有数据时抛出StopIteration错误。可以把这个数据流看做是一个有序序列，

#但我们却不能提前知道序列的长度，只能不断通过next()函数实现按需计算下一个数据，

#所以Iterator的计算是惰性的，只有在需要返回下一个数据时它才会计算。

#Iterator甚至可以表示一个无限大的数据流，例如全体自然数。而使用list是永远不可能存储全体自然数的。

#凡是可作用于for循环的对象都是Iterable类型；

#凡是可作用于next()函数的对象都是Iterator类型，它们表示一个惰性计算的序列；  xxx

#实现了`__next__`方法的对象都可以被 next() 作用, 但如果该对象没有实现`__iter__`方法，则不是 Iterator类型。

#例如:

class Count:

    def __init__(self, start, end):
        """" count inergers in [start, end] """ 

        self.start = start - 1

        self.end = end
    
    def __next__(self):

        if self.start >= self.end:

            raise StopIteration

        self.start += 1

        return self.start

count = Count(1, 3)

next(count)

from collections.abc import Iterator

isinstance (count, Iterator)

#实际上，在 collections.abc 的中可以知道（refs: Collections Abstract Base Classes, Iterator Types）：

#Iterable 对象需要实现 __iter__ 方法

#Iterator 继承自 Iterable, 因而也必须实现 __iter__ 方法， 并且原则上此方法应直接返回 `self`, 即对象本身，但非强制。

#Iterator 还需要实现 __next__ 方法

#总而言之，一个 Iterator 对象需且仅需同时具有 __iter__ 和 __next__ 方法。如：

class IteratorExample:

    def __iter__(self):

        pass

    def __next__(self):

        pass

isinstance (IteratorExample(), Iterator)

#集合数据类型如list、dict、str等是Iterable但不是Iterator，不过可以通过iter()函数获得一个Iterator对象。

#Python的for循环本质上就是通过不断调用next()函数实现的，例如：

for x in [1,2,3,4,5]:

    pass

#实际上完全等价于：

#首先获得Iterator对象

it = iter([1,2,3,4,5])

#循环

while True:

    try:

        #获得下一个值

        x = next(it)
    
    except StopIteration:

        #遇到StopIteration就退出循环

        break

print(it)


#可迭代对象是Python中一个非常庞大的概念，它主要包括如下三类：

#迭代器
#序列
#字典
           #/ --迭代器(iterator) ---生成器(generator)
          #/
         #/           / -- 字符串(str)
        #/           /  -- 列表(list)
#可迭代对象  ----序列
        #\           \  -- 元组(tuple)
         #\           \ -- 集合(set)
          #\
           #\ --字典(dict)

#从上图可以看出不同概念之间的关系，迭代器是可迭代对象的一个子集，而生成器又是迭代器的一个子集，

#是一种特殊的迭代器。除了迭代器之外，Python中还有序列、字典等可迭代对象。

#现在已经直观的了解了可迭代对象与迭代器、生成器之间的关系，那么用Python语言怎么表述它们的区别呢？

#可迭代对象需要实现__iter__方法迭代器不仅要实现__iter__方法，还需要实现__next__方法在使用层面，

#可迭代对象可以通过in和not in访问对象中的元素，举一个例子，

x = set([1,2,3,4,5])

print(x)

print(type(x))

print(1 in x)

print(2 not in x)

for x in x:

    print(x)

#前面提到，可迭代对象实现了__iter__方法，但是它没有实现__next__，

#这也是判定迭代器和其他可迭代对象的关键之处，

#可以看一下通过next访问上述示例中可迭代对象X会报错

x = set([1,2,3,4,5])

next(x)

#迭代器迭代器是可迭代对象的一个子集，它是一个可以记住遍历的位置的对象，

#它与列表、元组、集合、字符串这些可迭代对象的区别就在于next方法的实现，

#其他列表、元组、集合、字符串这些可迭代对象可以很简单的转化成迭代器，

#通过Python内置的iter函数能够轻松把可迭代对象转化为迭代器，下面来看一个例子，

x = [1,2,3,4,5]

print(type(x))

y = iter(x)

print(type(y))

print(next(y))

print(next(y))

print(next(y))

#从上述示例中我们可以看出两点：

#通过iter函数把list转化成了迭代器

#可迭代器能够记住遍历位置，能够通过next方法不断从前往后访问

#除了Python内置的iter之外，还可以通过Python内置的工具包itertools创建迭代器，其中函数包括，
# count
# cycle
# repeat
# accumulate
# chain
# compress
# dropwhile
# islice
# product
# permutations
# combinations......

#itertools中包含很多用于创建迭代器的实用方法，如果感兴趣嗯可以访问官方文档进行详细了解。

#当然，也可以自己通过实现__iter__和__next__方法来定义迭代器，

class Iterator(object):

    def __init__(self, array) :

        self.x = array

        self.index = 0

    def __iter__(self):

        return self

    def __next__(self):

        if self.index < len (self.x):

            value = self.x[self.index]

            self.index += 1
        
        else:

            raise StopIteration

        return value

it = Iterator([1,3,5,7,9])

print(type(it))

for i in it:

    print(i)
        
#生成器

#从文章开头的流程图可以直观的看出，生成器是迭代器的子集，换句话说，生成器一定是迭代器，

#但是迭代器不全是生成器对象。提及生成器就不得不提及一个Python中的关键字yiled，

#在Python中一个函数可以用yiled替代return返回值，这样的话这个函数就变成了一个生成器对象，

#举个例子对比一下:

def generator(array):

    for i in array:

        return i

gen = generator([1,2,3,4,5])

print(type(gen))

#这是我们常见的return返回方式，这样的话generator函数获取的是一个int型对象，

#下面看一下换成yield关键字，

def generator(array):

    for i in array:

        yield(i)

gen = generator ([1,3,5,7,9])

print(type(gen))

#这样的话获取的是一个生成器generator，除了yield之外，在Python3.3之后还加入了yield from获取生成器，

#允许一个生成器将其部分操作委派给另一个生成器，使得生成器的用法变得更加简洁，

#yield from后面需要加上可迭代对象，这样可以把可迭代对象变成生成器，

#当然，这里的可迭代对象不仅包含列表、元组，还包含迭代器、生成器。yield from相对于yield的有几个主要优点：

#代码更加简洁
#可以用于生成器嵌套
#易于异常处理

#下面就从简洁代码方面举个例子说明一下，

def generator(array):

    for sub_array in array:

        yield from sub_array

gen = generator([(1,2,3),(4,5,6,7)])

print(type(gen))

#当我们需要访问多层/多维可迭代对象时，我们就不需要逐层的去用for ... in ...去访问，

#可以简单的通过yiled from把生成器委派给子生成器，

#除此之外还可以通过生成器表达式的方法得到生成式，后面会介绍。

print(next(gen))

print(next(gen))

print(next(gen))

print(next(gen))

print(next(gen))

#通过上面示例可以看出，生成器可以像迭代器那样使用iter和next方法。

#首先它对比于迭代器在编码方面更加简洁，这是显而易见的，

#其次生成器运行速度更快，最后一点，也是需要着重说明的一点：节省内存。

#如果我们使用其他可迭代对象处理庞大的数据时，当创建或者返回值时会申请用于存储整个可迭代对象的内存，

#显然这是非常浪费的，因为有的元素当前我们用不到，也不会去访问，但它却一直占用这内存。

#这时候就体现了生成器的优点，它不是一次性把所有的结果都返回，而是当我们每读取一次，

#它会返回一个结果，当我们不读取时，它就是一个生成器表达式，几乎不占用内存。

#生成器表达式

#首先来看一个对比示例，

x = [1,2,3,4,5]

it = [i for i in x]

gen = (i for i in x)

print(type(x))

print(type(it))

print(type(gen))

#首先说一下it = [i for i in X]，这种用法叫做列表生成式，

# 在很多编程规范中非常推崇的一种替代for循环的方式，

# 仔细看一下代码会发现，it = [i for i in X]与gen = (i for i in X)的区别非常小，

# 只是一个用了中括号，一个用了小括号，但是它们的区别缺失非常大的，

# 使用中括号的叫做列表生成式，获得的返回值是一个列表，而使用小括号叫做生成器表达式，

# 获得的返回结果是一个生成器，这也是前面提到的，

# 除了使用yield和yield from两个关键字外还可以使用生成器表达式获得生成器。













