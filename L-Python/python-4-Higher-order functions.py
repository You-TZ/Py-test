'''
Author: your name
Date: 2022-03-31 09:02:22
LastEditTime: 2022-04-02 10:29:15
LastEditors: Please set LastEditors
Description: 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
FilePath: \Py-test\L-Python\python-4-Higher-order functions.py
'''
#Python内建了map()和reduce()函数。

#map()函数接收两个参数，一个是函数，一个是Iterable，map将传入的函数依次作用到序列的每个元素，并把结果作为新的Iterator返回。

#举例说明，比如我们有一个函数f(x)=x2，要把这个函数作用在一个list [1, 2, 3, 4, 5, 6, 7, 8, 9]上，就可以用map()实现如下：

#            f(x) = x * x
#
#                  │
#                  │
#  ┌───┬───┬───┬───┼───┬───┬───┬───┐
#  │   │   │   │   │   │   │   │   │
#  ▼   ▼   ▼   ▼   ▼   ▼   ▼   ▼   ▼
#
#[ 1   2   3   4   5   6   7   8   9 ]
#
#  │   │   │   │   │   │   │   │   │
#  │   │   │   │   │   │   │   │   │
#  ▼   ▼   ▼   ▼   ▼   ▼   ▼   ▼   ▼
#
#[ 1   4   9  16  25  36  49  64  81 ]

def f(x):

    return x * x

r = map(f, [1,2,3,4,5,6,7,8,9])

list(r)

#map()传入的第一个参数是f，即函数对象本身。由于结果r是一个Iterator，Iterator是惰性序列，

#因此通过list()函数让它把整个序列都计算出来并返回一个list。

#你可能会想，不需要map()函数，写一个循环，也可以计算出结果：

L = []

for n in  range(1,10):

    L.append(n)

print(L)

#map()作为高阶函数，事实上它把运算规则抽象了，

#因此，我们不但可以计算简单的f(x)=x2，还可以计算任意复杂的函数，

#比如，把这个list所有数字转为字符串：

list(map(str, [1,2,3,4,5]))



#reduce的用法。reduce把一个函数作用在一个序列[x1, x2, x3, ...]上，

#这个函数必须接收两个参数，reduce把结果继续和序列的下一个元素做累积计算，其效果就是：

#比方说对一个序列求和，就可以用reduce实现：

from filecmp import cmp
from functools import reduce
from sre_parse import DIGITS 

def add(x,y):

    return x + y

reduce(add, [1,3,5,7,9])

#当然求和运算可以直接用Python内建函数sum()，没必要动用reduce。

#但是如果要把序列[1, 3, 5, 7, 9]变换成整数13579，reduce就可以派上用场：

from functools import reduce

def fn(x,y):

    return x * 10 + y

reduce(fn, [1,3,5,7,9])

#如果考虑到字符串str也是一个序列，对上面的例子稍加改动，配合map()，我们就可以写出把str转换为int的函数：

from functools import reduce

def fn (x, y):

    return x * 10 + y

def char2num(s):

    digits = {'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9}

    return digits[s]

reduce (fn,map(char2num,'13579'))

#整理成一个str2int的函数就是：

from functools import reduce

DIGITS = {'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9}

def str2int(s):

    def fn (x, y):

        return x * 10 + y

    def char2num(s):

        return DIGITS[s]

    return reduce(fn, map(char2num, s)) 

#还可以用lambda函数进一步简化成：

from functools import reduce

DIGITS = {'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9}

def char2num(s):

    return DIGITS[s]

def str2int(s):

    return reduce (lambda x, y: x * 10 + y ,map(char2num,s))

#假设Python没有提供int()函数，你完全可以自己写一个把字符串转化为整数的函数，而且只需要几行代码！

#练习

#利用map()函数，把用户输入的不规范的英文名字，变为首字母大写，其他小写的规范名字。

#输入：['adam', 'LISA', 'barT']，输出：['Adam', 'Lisa', 'Bart']：

def normailze(name):

    return name[0].upper() + name[1:].lower()

# 测试:
L1 = ['adam', 'LISA', 'barT']

L2 = list(map(normailze, L1))

print(L2)

#Python提供的sum()函数可以接受一个list并求和，

#请编写一个prod()函数，可以接受一个list并利用reduce()求积：

from functools import reduce

def prod(L):

    return reduce(lambda x, y : x*y, L)

print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))

if prod([3, 5, 7, 9]) == 945:

    print('测试成功!')

else:

    print('测试失败!')

#利用map和reduce编写一个str2float函数，把字符串'123.456'转换成浮点数123.456：

from functools import reduce

def str2float(s):

     DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}

     ss = s.split(".")

     def char2num(s):
         
         return DIGITS[s]
    
     return reduce(lambda x, y: x * 10 + y,map(char2num,ss[0])) + reduce(lambda x, y : x * 10 + y,map(char2num,ss[1])) * pow(0.1,len(ss[1]))

print('str2float(\'123.456\') =', str2float('123.456'))

if abs(str2float('123.456') - 123.456) < 0.00001:

    print('测试成功!')

else:

    print('测试失败!')

#Python内建的filter()函数用于过滤序列。

#和map()类似，filter()也接收一个函数和一个序列。和map()不同的是，filter()把传入的函数依次作用于每个元素，然后根据返回值是True还是False决定保留还是丢弃该元素。

#例如，在一个list中，删掉偶数，只保留奇数，可以这么写：

def is_odd(n):

    return n % 2 == 1

list(filter(is_odd, [1,2,4,5,6,9,10,15]))


#把一个序列中的空字符串删掉，可以这么写：

def not_empty(s):

    return s and s.strip(',a')  #删除,和 a

list(filter(not_empty,['a','', 'b', None, 'c', '', ',']))

#可见用filter()这个高阶函数，关键在于正确实现一个“筛选”函数。

#注意到filter()函数返回的是一个Iterator，也就是一个惰性序列，

#所以要强迫filter()完成计算结果，需要用list()函数获得所有结果并返回list。

#用filter求素数
#计算素数的一个方法是埃氏筛法，它的算法理解起来非常简单：

#首先，列出从2开始的所有自然数，构造一个序列：

#2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, ...

#取序列的第一个数2，它一定是素数，然后用2把序列的2的倍数筛掉：

#3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, ...

#取新序列的第一个数3，它一定是素数，然后用3把序列的3的倍数筛掉：

#5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, ...

#取新序列的第一个数5，然后用5把序列的5的倍数筛掉：

#7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, ...

#不断筛下去，就可以得到所有的素数。

#用Python来实现这个算法，可以先构造一个从3开始的奇数序列：

def _odd_iter():

    n = 1

    while True:

        n = n + 2

        yield n

#注意这是一个生成器，并且是一个无限序列。

#然后定义一个筛选函数：

def _not_divisible(n):

    return lambda x :x % n > 0

#最后，定义一个生成器，不断返回下一个素数：

def primes():

    yield 2

    it = _odd_iter()   #初始序列

    while True:

        n = next(it)     #返回序列的第一个数

        yield n

        it = filter(_not_divisible(n), it)   #构造新序列

#这个生成器先返回第一个素数2，然后，利用filter()不断产生筛选后的新的序列。

#由于primes()也是一个无限序列，所以调用时需要设置一个退出循环的条件：

#打印1000以内的素数

for n in primes():

    if n < 1000:
        
        print(n)
    
    else:

        break

#注意到Iterator是惰性计算的序列，

#所以我们可以用Python表示“全体自然数”，“全体素数”这样的序列，而代码非常简洁。

#练习

#回数是指从左向右读和从右向左读都是一样的数，例如12321，909。请利用filter()筛选出回数：

def is_palindrome(n):

    return str(n) == str(n) [::-1]

# 测试:

output = filter(is_palindrome, range(1, 1000))

print('1~1000:', list(output))

if list(filter(is_palindrome, range(1, 200))) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 22, 33, 44, 55, 66, 77, 88, 99, 101, 111, 121, 131, 141, 151, 161, 171, 181, 191]:

    print('测试成功!')

else:
    
    print('测试失败!')

a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 22, 33, 44, 55, 66, 77, 88, 99, 101, 111, 121, 131, 141, 151, 161, 171, 181, 191]

print(a[-1])

print(a[:-1])

print(a[::-1])

#排序算法
#排序也是在程序中经常用到的算法。无论使用冒泡排序还是快速排序，排序的核心是比较两个元素的大小。

#如果是数字，我们可以直接比较，但如果是字符串或者两个dict呢？直接比较数学上的大小是没有意义的，

#因此，比较的过程必须通过函数抽象出来。

#Python内置的sorted()函数就可以对list进行排序：

sorted([36,5,-12,9,-21])

#sorted()函数也是一个高阶函数，它还可以接收一个key函数来实现自定义的排序，例如按绝对值大小排序：

sorted([36,5,-12,9,-21], key=abs)

#key指定的函数将作用于list的每一个元素上，并根据key函数返回的结果进行排序。对比原始的list和经过key=abs处理过的list：

#list = [36, 5, -12, 9, -21]

#keys = [36, 5,  12, 9,  21]
#然后sorted()函数按照keys进行排序，并按照对应关系返回list相应的元素：

#keys排序结果 => [5, 9,  12,  21, 36]
#                |  |    |    |   |
#最终结果     => [5, 9, -12, -21, 36]

#我们再看一个字符串排序的例子：

sorted (['bob', 'about', 'Zoo', 'Credit'])

#现在，我们提出排序应该忽略大小写，按照字母序排序。要实现这个算法，不必对现有代码大加改动，

#只要我们能用一个key函数把字符串映射为忽略大小写排序即可。

#忽略大小写来比较两个字符串，实际上就是先把字符串都变成大写（或者都变成小写），再比较。

#这样，我们给sorted传入key函数，即可实现忽略大小写的排序：

sorted (['bob', 'about', 'Zoo', 'Credit'], key=str.lower)

#要进行反向排序，不必改动key函数，可以传入第三个参数reverse=True：

sorted (['bob', 'about', 'Zoo', 'Credit'], key=str.lower, reverse=True)

#小结

#sorted()也是一个高阶函数。用sorted()排序的关键在于实现一个映射函数。

#练习

#假设我们用一组tuple表示学生名字和成绩：

L = [('Bob',75), ('Adam', 92), ('Bart',66), ('Lisa',88)]

#请用sorted()对上述列表分别按名字排序：

def by_name(t):

    return t[0]

L2 = sorted (L, key=by_name)

print(L2)

def by_score(c):

    return c[1]

L3 = sorted (L, key=by_score, reverse=True)

print(L3)


#sorted 语法：

#sorted(iterable, cmp=None, key=None, reverse=False)

#参数说明：

#iterable -- 可迭代对象。

#cmp -- 比较的函数，这个具有两个参数，参数的值都是从可迭代对象中取出，此函数必须遵守的规则为，大于则返回1，小于则返回-1，等于则返回0。

#key -- 主要是用来进行比较的元素，只有一个参数，具体的函数的参数就是取自于可迭代对象中，指定可迭代对象中的一个元素来进行排序。

#reverse -- 排序规则，reverse = True 降序 ， reverse = False 升序（默认）。

L = [('b',2), ('a', 1), ('c', 3), ('d', 4)]

sorted(L, key=lambda x :x[1])

students = [('join', 'A', 15), ('kane', 'B', 12), ('dave','B', 10)]

sorted (students, key=lambda s : s[2])

sorted (students, key=lambda s : s[2], reverse=True)