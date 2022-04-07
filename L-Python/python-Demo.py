'''
Author: your name
Date: 2022-03-14 09:12:18
LastEditTime: 2022-03-31 10:05:45
LastEditors: Please set LastEditors
Description: 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
FilePath: \sss\python-Demo.py
'''
#Python69个内置函数
#01数据类型
#bool()
#描述：测试一个对象是True, 还是False.bool 是 int 的子类。

#语法：class bool([x])

#参数：x -- 要进行转换的参数。
from audioop import reverse
import re


bool([0,0,0])
bool([])
issubclass(bool,int)
True + True
12/True

#int()
#描述：int() 函数用于将一个字符串或数字转换为整型。 x可能为字符串或数值，
# 将x 转换为一个普通整数。如果参数是字符串，
# 那么它可能包含符号和小数点。如果超出了普通整数的表示范围，一个长整数被返回。

#语法：int(x, base =10)
#参数：

#x -- 字符串或数字。
#base -- 进制数，默认十进制
int('12',16)
int('10',20)
int('3',6)
int('3',6)

#float()
#描述：将一个字符串或整数转换为浮点数

#语法：class float([x])

#参数：x -- 整数或字符串
float(3)
float('123')

#complex()
#描述：创建一个复数

#语法：class complex([real[, imag]])

#参数：

#real -- int, long, float或字符串；
#imag -- int, long, float；
complex(1,2)
complex('1')
complex('1+5j')
complex('1+2.0j')

#02 进制转换
#bin()
#描述：bin() 返回一个整数 int 或者长整数 long int 的二进制表示。将十进制转换为二进制

#语法：bin(x)

#参数：x -- int 或者 long int 数字
bin(2)
bin(20)
bin(10)
bin(1)
bin(3)
bin(4)

#oct()
#描述：将十进制转换为八进制 otc() 将给的参数转换成八进制

#语法：oct(x)

#参数：x -- 整数。
oct(8)
oct(16)
oct(15)
oct(43)

#hex()
#描述：hex() 函数用于将10进制整数转换成16进制，以字符串形式表示。

#语法：hex(x)

#参数：x -- 10进制整数。
hex(43)  #43等于2b
hex(15)
dict()
dict(a= 'a', b = 'b', t = 't')

#03 数学运算
#abs()
#描述：返回数字绝对值或复数的模

#语法：abs( x )

#参数：x 数值表达式。

abs(-6)
abs(-3.14)
abs(1+2j)
abs(-1+4j)

#divmod()
#描述：divmod() 函数把除数和余数运算结果结合起来，返回一个包含商和余数的元组(a // b, a % b)。

#语法：divmod(a, b)

#参数：a: 数字--被除数

#b: 数字--除数
divmod(11,3)
divmod(12,3)
divmod(0,5)

#round()
#描述：round() 函数返回浮点数x的四舍五入值。

#语法：round( x [, n] )

#参数
#x -- 数值表达式。
#n --代表小数点后保留几位

round(3.143435566,5)

pow()
#描述：pow(x，y) 方法返回x的y次方的值，等价于x**y。
# 函数是计算x的y次方，如果z在存在，则再对结果进行取模，其结果等效于pow(x,y) %z
#取模和取余的区别
#取余运算 在计算商值时 商值向0方向舍入；靠近0原则
#取模运算 在计算商值时 商值向负无穷方向舍入；尽可能让商值小的原则(不超多商值的最大值)
#计算步骤
#假设有整数a和b，那么取模/取余运算可以分为两步运算：

#求整数商：c = a/b;
#计算模/余数：r = a - (c*b);
#总计算模/余数：a mod b = a - b[a/b] ([a/b]表示整数商)

#例：返回 5 的 3 次方取余 4（等同于 (5 * 5 * 5) % 4）：
#参数：

#x -- 数值表达式。
#y -- 数值表达式。
#z -- 数值表达式。

#语法：pow(x, y[, z])
pow(5,2)
pow(5,3,5)
pow(2,2,2)
pow(10,10,5)
pow(4,3,5)
pow(5,3,4)
x=5
y=2
z=2
pow(x,y,z)
x= 5
y = 2
print(x % y)

#sum()
#描述：sum() 方法对系列进行求和计算。

#语法：sum(iterable[, start])

#参数：

#iterable -- 可迭代对象，如：列表、元组、集合。
#start -- 指定相加的参数，如果没有设置这个值，默认为0

a =[1,2,3,5,8,9]
sum(a)
b =(1,3,5)
sum(b)
sum(a,10)

#min()
#描述：min() 方法返回给定参数的最小值，参数可以为序列。

#语法：min( x, y, z, .... )

#参数：

#x -- 数值表达式。
#y -- 数值表达式。
#z -- 数值表达式。
min(80,100,1000)
min([80,100,1000])
d =(90,100,101)
min(d)

#max()
#描述：max() 方法返回给定参数的最大值，参数可以为序列。

#语法：max( x, y, z, .... )

#参数：

#x -- 数值表达式。
#y -- 数值表达式。
#z -- 数值表达式。
max(3,1,4,2,1)
max([5,4,2,7,8,7])
di = {'a':10,'b':45,'c':12}
max(di)


#二、数据结构相关
#01 序列数据类型
#1）列表和元组
#list()
#描述：list() 函数创建列表或者用于将序列转换为列表。

#语法：list( iterable )

#参数：iterable -- 可迭代序列。

#序列为元组时
s= (345,'xtz','zara','abc')
list(s)
#序列为字符串
s = '( ఠൠఠ )ﾉ(′д｀ )…彡…彡'
list(s)
#序列为字典
s ={'names':'哥哥','age':35,'address':'Hangzhou'}
list(s)

#tuple()
#描述： 元组 tuple() 函数将列表转换为元组。

#语法：tuple( iterable )

#参数：iterable -- 要转换为元组的可迭代序列。
tuple([1,2,3,4])
tuple({'a':2,'v':5})
tuple('大漠孤烟直，长河落日圆')
v = {'a':1,'b':'七七八','c':'23'}
tuple(v)

#2）集合数据类型
# dict()
# 描述：创建数据字典
# 语法：
# class dict(**kwarg)
# class dict(mapping, **kwarg)
# class dict(iterable, **kwarg)
# 参数：**kwargs -- 关键字
# mapping -- 元素的容器。
# iterable -- 可迭代对象。

#创建空字典
dict()
#传入关键字
dict(a='a',b='b',c='c')
#映射函数方式来构造字典
dict(zip(['one','two','three'],[1,2,3]))
#可迭代对象方式来构造字典
dict([('one',1),('two',6),('three',8)])

#set()
#描述：set() 函数创建一个无序不重复元素集，可进行关系测试，删除重复数据，还可以计算交集、差集、并集等。

#语法：class set([iterable])

#参数：iterable -- 可迭代对象对象；
#返回一个set对象，可实现去重
a = [1,2,2,34,4,5,4]
set(a)
a = (3,3,3,5,1,2)
set(a)

#frozenset()
#描述：frozenset() 返回一个冻结的集合，冻结后集合不能再添加或删除任何元素。

#语法：class frozenset([iterable])

#参数：iterable -- 可迭代的对象，比如列表、字典、元组等等。

frozenset([1,1,3,4,5,6,5,4])
a = ([7,3,1,4,2,1])
frozenset(a)

#3）字符串
#str()
#述：str() 函数将对象转化为适于人阅读的形式。将字符类型、数值类型等转换为字符串类型

#语法：class str(object='')

#参数：object -- 对象。

#案例：
integ = 100
str(integ)

v = {'tengxun':'腾讯','google':'谷歌'}
str(v)

v = {'tengxun':111,'google':222}
str(v)

v = ([1,2,3])
str(v)
#format() 
# 描述：Python2.6 开始，新增了一种格式化字符串的函数 str.format()，它增强了字符串格式化的功能。基本语法是通过 {} 和 : 来代替以前的 % 。
# 使用format()来格式化字符串时，使用在字符串中使用{}作为占位符，占位符的内容将引用format()中的参数进行替换。可以是位置参数、命名参数或者兼而有之。
# format 函数可以接受不限个参数，位置可以不按顺序。
# 语法：format(value, format_spec)
# 参数：
#位置参数
'{}:您{}购买的{}到了！请下楼取快递'.format('快递小哥','淘宝','快递')
#给批量客户发短息
n_list = ['张麻子','师爷','黄四郎','武举人']
for name in n_list:
    print('{0}:来了！！！'.format(name))
for n in n_list:
    print('{0}:快来！！！'.format(n.center(4,'*')))

'{0},{1} and {2}'.format('gao','fu','shuai')

x = 3
y = 5
'{0} + {1} = {2}'.format(x,y,x+y)

#命名参数
'{name1},{name2} and {name3}' .format(name1 = 'gao', name2 = 'fu', name3 = 'shuai')

#混合位置参数，命名参数
'{name1}, {0} and {name2} or {1}'.format('AA','BB',name1 = 'aa',name2 ='bb')

#for循环进行批量处理
['vec_{0}'.format(i) for i in range(1,5)]
['f_{}'.format(r) for r in list('abcde')]

#bytes() 
#描述：将一个字符串转换成字节类型
#语法：class bytes([source[, encoding[, errors]]])
#参数：如果 source 为整数，则返回一个长度为 source 的初始化数组；
# 如果 source 为字符串，则按照指定的 encoding 将字符串转换为字节序列；
# 如果 source 为可迭代类型，则元素必须为[0 ,255] 中的整数；
# 如果 source 为与 buffer 接口一致的对象，则此对象也可以被用于初始化 bytearray。
# 如果没有输入任何参数，默认就是初始化数组为0个元素。
s = 15
bytes(s)

s = '苹果'
bytes(s,encoding='utf-8')

s = ([5,3,1,2])
bytes(s)

s = (5,6,4,2,3)
bytes(s)

#bytearray()
#描述：返回一个新字节数组. 这个数字的元素是可变的, 并且每个元素的值得范围是[0,256)
#语法：class bytearray([source[, encoding[, errors]]])
#参数：如果 source 为整数，则返回一个长度为 source 的初始化数组；
#如果 source 为字符串，则按照指定的 encoding 将字符串转换为字节序列；
#如果 source 为可迭代类型，则元素必须为[0 ,255] 中的整数；
#如果 source 为与 buffer 接口一致的对象，则此对象也可以被用于初始化 bytearray。
#如果没有输入任何参数，默认就是初始化数组为0个元素。
bytearray()
bytearray(123)
bytearray([1,3,5])
bytearray('腾讯','utf-8')

#ord()
#描述：查看某个ascii对应的十进制数

#语法：ord(c)

#参数：c -- 字符。
ord('A')
ord('a')
ord('~')

#chr()
#描述：chr() 用一个范围在 range（256）内的（就是0～255）整数作参数，返回一个对应的字符。

#语法：chr(i)

#参数：i -- 可以是10进制也可以是16进制的形式的数字。
#查看十进制整数对应得ASCII字符
chr(65)
chr(97)
chr(126)

#ascii()
#描述：ascii() 函数返回任何对象（字符串，元组，列表等）的可读版本。
#ascii() 函数会将所有非 ascii 字符替换为转义字符：
#å 将替换为 \xe5。
#语法：ascii(object)
#参数：object--对象，可以是元组、列表、字典、字符串、set()创建的集合。
ascii('中国')
ascii('吉林加油')
ascii('My name is Stale')
#元组
print(ascii((1,2)))
print(type(ascii((1,2))))
#ASCII码表具体如下所示(节选)
# Bin(二进制)      Oct(八进制)       Dec(十进制)     Hex(十六进制)    缩写/字符     解释
# 0000 0000        00                 0              0x00            NUL(null)   空字符
# 0010 0001        041                33             0x21              !         叹号
# 0010 0010        042                34             0x22              "         双引号
# 0010 1010        052                42             0x2A              *         星号
# ...              ...                ...            ...               ...       ...
# 0111 1101        0175               125            0x7D              }         闭花括号
# 0111 1110        0176               126            0x7E              ~         波浪号
# 0111 1111        0177               127            0x7F              DEL(delete) 删除

repr()
#返回一个对象的string形式

#03 数据结构处理相关函数
#len()
#描述：len() 函数返回对象（字符、列表、元组等）长度或项目个数。

#语法：len(s)

#参数：s -- 对象。
#字典的长度
dic = {'a':1,'b':3}
len(dic)

#字符串长度
s = 'aassdf'
len(s)

#列表元素个数
l = [1,2,4,5,3]
len(l)

#sorted()
# 描述：sorted()函数对所有可迭代的对象进行排序操作。
# 语法：sorted(iterable,  key=None, reverse=False)
# 参数：
# iterable--可迭代对象。
# key--主要是用来进行比较的元素,只有一个参数,具体的函数的参数就是取自于可迭代对象中,
# 指定可迭代对象中的一个元素来进行排序。
# reverse -- 排序规则,reverse=True降序 ,reverse = False升序(默认)。
a = [5,6,14,7,345,234,12]
b = sorted(a,reverse=True)
a
b

#利用key
L = [('b',2),('a',1),('c',5),('d',4)]
sorted(L, key=lambda x:x[1],reverse=True)

#按年龄排序
students = [('join','A',15),
            ('jane','B',12),
            ('dave','C',34),
            ('jack','D',21)]
sorted(students,key=lambda s:s[2])
#按降序
sorted(students,key=lambda p:p[2],reverse=True)

#降序排列
a = [1,4,2,5,7,32,11]
sorted(a,reverse = True)

#sort 与 sorted 区别：
# sort 是应用在list 的方法，sorted可以对所有可迭代的对象进行排序操作；
# list的sort 方法返回的是对已经存在的列表进行操作，无返回值，
# 而内建函数sorted方法返回的是一个新的 list，而不是在原来的基础上进行的操作。

#reversed()
#描述：reversed函数返回一个反转的迭代器。
#语法：reversed(seq)
#参数：seq -- 要转换的序列，可以是 tuple, string, list 或 range.
#反转列表
rev = reversed([32,453,131,21,31,12])
list(rev)
#反转字符串
rev = reversed('实践是检验真理的唯一标准')
list(rev)
''.join(rev)

s = '我的世界开始下雪'
''.join(reversed(s))

#slice()
#描述：slice() 函数实现切片对象，主要用在切片操作函数里的参数传递。
# 返回一个表示由 range(start, stop, step) 所指定索引集的 slice对象
#语法：
#class slice(stop)
#class slice(start, stop[, step])
#参数：
#start -- 起始位置
#stop -- 结束位置
#step -- 间距
a = [7,2,5,8,9]
a[slice(0,5,2)] #等价于a[0:5:2]
c = [7,2,5,4,9,10,11,12]
c[slice(0,7,2)]

a = list(range(10))
a[slice(5)]


#enumerate()
# 描述：enumerate() 函数用于将一个可遍历的数据对象
# (如列表、元组或字符串)组合为一个索引序列，同时列出数据和数据下标，一般用在for循环当中。
# 返回一个可以枚举的对象，该对象的next()方法将返回一个元组。
# enumerate在字典上是枚举、列举的意思。
# 语法：enumerate(sequence, [start=0])
# 参数：sequence -- 一个序列、迭代器或其他支持迭代对象。           
# start -- 下标起始位置。
L = ['Spring','Summer','Fall','Winter']
enumerate(L)
#<enumerate at 0x1d036885b80> 生成的额外的迭代器，无法直接查看

list(enumerate(L)) #列表形式，可以看到内部结构，默认下标从0开始
list(enumerate(L,start=1)) #下标从1开始

for i,v in enumerate(L):
    print(i,v)
for i,v in enumerate(L,1):
    print(i,v)

s = ['a','b','c']

for i,v in enumerate(s,2):
    print(i,v)

#普通的for循环
i = 0
seq = ['one','two','three']
for element in seq:
    print(i,seq[i])
    i += 1
#普通循环的对比案例
seq = ['four','five','six']
for i,element in enumerate(seq):
    print(i,element)

seq = ['seven','eight','nine']
for i ,element in enumerate(seq,2):
    print(i,element)

#all() 
# 描述：接受一个迭代器，如果迭代器(元组或列表)的所有元素都为真，
# 那么返回True，否则返回False，元素除了是0、空、None、False外都算 True。
# 注意：空元组、空列表返回值为True，这里要特别注意。
# 语法：all(iterable)
# 参数：iterable -- 元组或列表
all([1,2,43,0,2])
all([1,2,3,435])
all(['a','v','','d'])
all([]) #空列表为真
all(()) #元组为真

#any()
#描述：接受一个迭代器，如果迭代器里有一个元素为真，那么返回True，
# 否则返回False，元素除了是 0、空、None、False 外都算 True。

#语法：any(iterable)

#参数：iterable -- 元组或列表
any([0,0,0,[]])
any([])
any((0,1))
any((0,'',False))
any([]) #空列表
any(()) #空元组

#zip() 
# 描述：zip() 函数用于将可迭代的对象作为参数，将对象中对应的元素打包成一个个元组，
# 然后返回由这些元组组成的对象，这样做的好处是节约了不少的内存。
# 我们可以使用 list() 转换来输出列表。，如果各个迭代器的元素个数不一致，
# 则返回列表长度与最短的对象相同，利用 * 号操作符，可以将元组解压为列表。
# 语法：zip([iterable, ...])
# 参数：iterable 一个或多个迭代器

#创建一个聚合了来自每个可迭代对象中的元素的迭代器：
x = [3,2,1]
y = [4,5,6]
list(zip(y,x))
list(zip(x,y))

#搭配for循环，数字于字符串组合
a = range(5)
b = list('abcde')
[str(x)+str(y) for x,y in zip(a,b)]

#数数相乘
list1 = [2,3,4]
list2 = [5,6,7]
for x,y in zip(list1,list2):
    print(x,'*',y,'--',x*y)

#元素个数与最短的列表一致
x = [3,2,1]
b = ('abcde')
list(zip(x,b))

#与zip想法，zip(*)可理解为解压，返回二维矩阵式
a = range(5)
b = list('abcde')
a1,a2 = zip(*zip(a,b))
a1
a2

#filter()
# 描述：filter() 函数用于过滤序列，过滤掉不符合条件的元素，
# 返回由符合条件元素组成的新列表。该接收两个参数，第一个为函数，第二个为序列，
# 序列的每个元素作为参数传递给函数进行判断，然后返回 True 或 False，最后将返回 True 的元素放到新列表中。
# 语法：filter(function, iterable)
# 参数：
# function -- 判断函数。
# iterable -- 可迭代对象。
fill = filter(lambda x: x>10,[1,22,2,45,21,6,31])
fill
list(fill)

def is_odd(n):
    return n % 2 == 1
newlist = filter(is_odd,range(10))
print(list(newlist))


#map()
#  描述：map() 会根据提供的函数对指定序列做映射。返
# 回一个将 function 应用于 iterable 中每一项并输出其结果的迭代器
# 语法：map(function, iterable, ...)
# 参数：
# function -- 函数
# iterable -- 一个或多个序列

def square(x):          #计算平方数
    return x ** 2
list(map(square,[1,3,5,6]))    #计算列表各个元素的平方

list(map(lambda k: k ** 2,[1,2,3,4])) #使用lambda匿名函数

#提供俩个列表，对相同位置的列表的数据进行相加
list(map(lambda x, y: x+y,[1,3,5,7,9],range(5)))
list(map(lambda x:x%2==1, [1,2,3,5,13,4]))


#三、和作用域相关
#locals()
#描述：locals() 函数会以字典类型返回当前位置的全部局部变量。对于函数, 方法, lambda 函式, 类, 以及实现了 __call__ 方法的类实例, 它都返回 True。

#语法：locals()

def runoob(arg):
    z = 1
    print(locals())
runoob(4)

#globals()
#描述： 函数会以字典类型返回当前位置的全部全局变量。

#语法：globals()

#参数：无

a = 'runoob'
print(globals()) # # globals 函数返回一个全局变量的字典，包括所有导入的变量。


#四、迭代器生成器
# range() 
# 描述：range() 函数可创建一个整数列表，一般用在 for 循环中。
# 语法：range(start, stop[, step])
# 参数：
# start: 计数从 start 开始。默认是从 0 开始。例如range（5）等价于range（0， 5）;
# stop: 计数到 stop 结束，但不包括 stop。例如：range（0， 5） 是[0, 1, 2, 3, 4]没有5
# step：步长，默认为1。例如：range（0，5）等价于 range(0, 5, 1)

list(range(10))
list(range(1,11))  #从1开始到11
list(range(0,30,5))
list(range(0,20,2))

for i in range(5):
    print(i)


#next() 
# 描述：next() 返回迭代器的下一个项目。next() 函数要和生成迭代器的iter() 函数一起使用。
# 语法：next(iterator[, default])
# 参数：iterator -- 迭代器
# default -- 可选，用于设置在没有下一个元素时返回该默认值，如果不设置，
# 又没有下一个元素则会触发StopIteration异常。
# 不加默认值的情况，最后会报错StopIteration

it = iter([5,3,4,1])
next(it)
next(it)
next(it)
next(it)
#加默认值的情况，最后迭代完了，会返回默认值
it = iter([0,1,2,3,4,5])
next(it,'结束了')
next(it,'结束了')
next(it,'结束了')
next(it,'结束了')
next(it,'结束了')
next(it,'结束了')
next(it,'结束了')

#iter()
# 描述：返回一个 iterator 对象
# 语法：iter(object[, sentinel])
# 参数：object -- 支持迭代的集合对象。
# sentinel -- 如果传递了第二个参数，则参数 object 必须是一个可调用的对象（如，函数），
# 此时，iter 创建了一个迭代器对象，每次调用这个迭代器对象的__next__()方法时，都会调用 object。

iter([1,2,3,4,5,6])

v =iter([0,1,2,3,4,5])

for i in v:
    print(i)

#五、字符串类型代码的执行
# eval() 
# 描述：将字符串str 当成有效的表达式来求值并返回计算结果取出字符串中内容
# 语法：eval(expression[, globals[, locals]])
# 参数：
# expression -- 表达式。
# globals -- 变量作用域，全局命名空间，如果被提供，则必须是一个字典对象。
# locals -- 变量作用域，局部命名空间，如果被提供，可以是任何映射对象。

s = '1 + 3 + 5'
eval(s)

#要统计图片的数量
str1 = "['https://1.jpg','https://2.jpg']"
len(eval(str1))

len(str1)

#exec() 
# 描述：执行储存在字符串或文件中的Python语句，相比于eval，exec可以执行更复杂的Python代码。
# 语法：exec(object, globals, locals)
# 参数：
# object-- 要执行的表达式。
# globals -- 可选。包含全局参数的字典。
# locals -- 可选。包含局部参数的字典。

#执行字符串或compile方法编译过的字符串，没有返回值
s = "print('hello,world')"
r = compile(s,'<string>','exec')  #编译为字节代码对象
exec(r)

x = 10
expr ="""
z = 30
sum = x + y + z
print(sum)  
 """
def func():
    y = 20
    exec(expr)
    exec(expr,{'x':1,'y':2})
    exec(expr,{'x':1,'y':2},{'y':3,'z':10})
func()

#compile()
# 描述：compile() 将 source 编译成代码或 AST 对象，将字符串类型的代码编码, 
# 代码对象能够通过exec语句来执行或者eval()进行求值
# 语法：compile(source, filename, mode[, flags[, dont_inherit]])
# 参数：
# source -- 字符串或者AST（Abstract Syntax Trees）对象。
# filename -- 代码文件名称，如果不是从文件读取代码则传递一些可辨认的值。
# mode -- 指定编译代码的种类。可以指定为 exec, eval, single。
# flags -- 变量作用域，局部命名空间，如果被提供，可以是任何映射对象。
# flags和dont_inherit是用来控制编译源码时的标志

#将字符串编译成python能识别或可以执行的代码，也可以将文字读成字符串再编译。
s = "print('helloworld')"
r = compile(s,"<strint>",'exec')
r
exec(r)

str = "for i in range(0,5): print(i)"
c = compile(str,'','exec') #编译为字节代码对象
c
exec(c)

#六、输入输出
# print() 
# 描述：print() 方法用于打印输出，最常见的一个函数。
# 在 Python3.3 版增加了 flush 关键字参数。print 在 Python3.x 是一个函数，
# 但在 Python2.x 版本不是一个函数，只是一个关键字。
# 语法：print(*objects, sep=' ', end='\n', file=sys.stdout, flush=False)
# 参数：
# objects -- 复数，表示可以一次输出多个对象。输出多个对象时，需要用 , 分隔。
# sep -- 用来间隔多个对象，默认值是一个空格。
# end -- 用来设定以什么结尾。默认值是换行符 \n，我们可以换成其他字符串。
# file -- 要写入的文件对象。
# flush -- 输出是否被缓存通常决定于 file，但如果 flush 关键字参数为 True，流会被强制刷新

print('hello World')

#设置间隔符
print('www','baidu','com',sep='.')

#input()
#描述：Python3.x 中 input() 函数接受一个标准输入数据，返回为 string 类型。获取用户输入内容

#语法：input([prompt])

#参数：prompt:--提示信息

a = input("input:")
input:1234
print(a)

#输入三角形的三边长
a,b,c = (input('三角形的边长：').spilt())
a = int(a)
b = int(b)
c = int(c)

#计算三角形的半周长p
p = (a+b+c)/2

#计算三角形的面积s
s = (p*(p-a)*(p-b)*(p-c))**0.5

#输出三角形的面积
print('三角形面积为：',format(s,'.2f'))


#hash() 
# 描述：返回该对象的哈希值（如果它有的话）。哈希值是整数。
# 它们在字典查找元素时用来快速比较字典的键。
# 相同大小的数字变量有相同的哈希值（即使它们类型不同，如 1 和 1.0），
# hash表.用空间换的时间 比较耗费内存，hash() 函数可以应用于数字、字符串和对象，
# 不能直接应用于 list、set、dictionary。
# 语法：hash(object)
# 参数：object -- 对象

#在hash()对对象使用时，所得的结果不仅和对象的内容有关，还和对象的id(),也就是内存地址有关
class Test:
    def __init__(self,i):
        self.i = i
for i in range(10):
    t =Test(1)
    print(hash(t),id(t))
#hash() 函数的用途：
# hash() 函数的对象字符不管有多长，返回的hash值都是固定长度的，
# 也用于校验程序在传输过程中是否被第三方（木马）修改，
# 如果程序（字符）在传输过程中被修改hash值即发生变化，
# 如果没有被修改，则hash值和原始的hash值吻合，只要验证hash值是否匹配即可验证程序是否带木马（病毒）。
nam1 = '正常'
nam2 = '正常真诚的'
print(hash(nam1))
print(hash(nam2))

#memoryview()
# 描述：memoryview() 函数返回给定参数的内存查看对象(Momory view)。
# 返回由给定实参创建的“内存视图”对象， Python 代码访问一个对象的内部数据，
# 只要该对象支持缓冲区协议 而无需进行拷贝
# 语法：memoryview(obj)
# 参数：obj -- 对象

bytearray()
bytearray([1,2,3])
bytearray('中国','utf-8')

v = memoryview(bytearray('abcdefg','utf-8'))
v[1]
v[-1]
v[1:4]
v[1:4].tobytes()

#八、文件读写
# open() 
# 描述：open() 函数用于打开一个文件，创建一个file对象，相关的方法才可以调用它进行读写。
# 所以open（）读取文件分为两步
# 。语法：open(name[, mode[, buffering]])
# 参数：
# name : 一个包含了你要访问的文件名称的字符串值。
# mode : mode决定了打开文件的模式：只读，写入，追加等。所有可取值见如下的完全列表。
# 这个参数是非强制的，默认文件访问模式为只读(r)。
# buffering : 如果 buffering 的值被设为 0，就不会有寄存。
# 如果 buffering 的值取 1，访问文件时会寄存行。如果将 buffering 的值设为大于1的整数，
# 表明了这就是的寄存区的缓冲大小。如果取负值，寄存区的缓冲大小则为系统默认。

#打开文件的模式：
# r： 打开一个文件用于只读，文件的指针将会放在文件的开头，这是默认模式。
# w：打开一个文件用于写入，如果文件存在则打开文件，并从开头开始编辑，即原有内容会被删除。
#  如果该文件不存在，创建新文件。
# a：打开一个文件用于追加，如果文件已存在，文件指针将会放在文件的结尾，
#  如果文件不存在，创建新文件进行写入。r+：打开一个文件用于读写，文件指针将会放在文件的开头。
# w+：打开一个文件用于读写。如果该文件已存在，删除原有内容并从开头开始编辑；
#  如果该文件不存在，创建新文件。
# a+：打开一个文件用于读写。
#  如果该文件已存在，文件指针将会放在文件的结尾，如果该文件不存在，创建新文件用于读写。
# rb：以二进制格式打开一个文件用于只读。文件指针将会放在文件的开头。这是默认模式。
# rb+：以二进制格式打开一个文件用于读写。文件指针将会放在文件的开头。
# wb：以二进制格式打开一个文件只用于写入。如果该文件已存在则打开文件，并从开头开始编辑
#  ，即原有内容会被删除。如果该文件不存在，创建新文件。
# wb+：以二进制格式打开一个文件用于读写。如果该文件已存在则打开文件，并从开头开始编辑，
#  即原有内容会被删除。如果该文件不存在，创建新文件。
# ab：以二进制格式打开一个文件用于追加。如果该文件已存在，文件指针将会放在文件的结尾。
#  也就是说，新的内容将会被写入到已有内容之后。如果该文件不存在，创建新文件进行写入。
# ab+：以二进制格式打开一个文件用于追加。如果该文件已存在，文件指针将会放在文件的结尾。
#  如果该文件不存在，创建新文件用于读写。
#  注意：当读取音视频、图片等二进制文件时，需要采用二进制的读取方法。
# file对象方法
# file.read([size])：size 未指定则返回整个文件，如果文件大小>2 倍内存则有问题，
#  f.read()读到文件尾时返回""(空字串)。
# file.readline()：返回一行。
# file.readlines([size]) ：返回包含size行的列表, size 未指定则返回全部行。
# for line in file: print(line)：通过迭代器访问。
# file.write()：如果要写入字符串以外的数据,先将他转换为字符串。
# file.tell()：返回一个整数,表示当前文件指针的位置(就是到文件头的比特数)。
# file.seek(偏移量,[起始位置])：用来移动文件指针。偏移量: 单位为比特，可正可负；
# 起始位置: 0 - 文件头, 默认值; 1 - 当前位置; 2 - 文件尾
#file.close()：关闭文件

file = open('C:/Users/JTZ/Desktop/test.txt',encoding='utf-8') #打开文件
file.read() #直接显示文件所有内容
file.readline #显示第一行
file.close() #关闭文件

#逐行读取
file = open('C:/Users/JTZ/Desktop/test.txt')
for line in file:
    print(line)
    
#九、模块相关
# __ import__()
# 描述：该函数会导入 name 模块，有可能使用给定的 globals 和 locals 来确定如何在包的上下文中解读名称。 
# fromlist 给出了应该从由 name 指定的模块导入对象或子模块的名称。 
# 标准实现完全不使用其 locals 参数，而仅使用 globals 参数来确定 import 语句的包上下文。
# level 指定是使用绝对还是相对导入。 0 (默认值) 意味着仅执行绝对导入。 
# 语法：__import__(name, globals=None, locals=None, fromlist=(), level=0) 
# 参数：object -- 对象

#语句 import spam的结果将为与以下代码作用相同的字节码：

spam = __import__('spam.ham',globals(),locals(),[],0)

#十、获取帮助
#help()
#描述：返回对象的帮助文档

#语法：help(object)

#参数：object -- 对象

help('sys')  #查看sys模块的帮助
help('str')  #查看str数据类型的帮助
a = [1,2,3]
help(a)  #查看列表list帮助信息
help(a.append) #显示list的append方法的帮助


#十、对象调用
# callable()
# 描述：callable() 函数用于检查一个对象是否是可调用的。
# 如果返回 True，object 仍然可能调用失败；但如果返回 False，调用对象object绝对不会成功。
# 对于函数、方法、lambda 函式、 类以及实现了 __call__ 方法的类实例, 它都返回True。
# 这个函数一开始在 Python 3.0 被移除了，但在 Python 3.2 被重新加入。
# 语法：callable(object)
# 参数：object -- 对象

#检查一个数字
callable(0)

#创建一个函数
def add(x,y):
    return x*y
callable(add)

#创建一个带有_call_方法的类
class Dogs:
    def __call__(self):
        return 0
callable(Dogs)


#十一、内置属性
# dir() 
# 描述：dir() 查看对象的内置属性, 访问的是对象中的__dir__()方法，函数不带参数时，
# 返回当前范围内的变量、方法和定义的类型列表；带参数时，返回参数的属性、方法列表。
# 如果参数包含方法__dir__()，该方法将被调用，如果参数不包含__dir__()，
# 该方法将最大限度地收集参数信息。
# 语法：dir(object)
# 参数：object 对象、变量、类型。

#获得当前模块的属性列表
dir()
#查看列表的方法，使用dir([])或者dir(list())#查看列表的方法
print(dir(list()))
#dir()访问的是对象中的_dir_()方法，因此下面的调用也能得到相同的结果
list().__dir__()

#hasattr()
#描述：函数用于判断对象是否包含对应的属性。

#语法：hasattr(object, name)

#参数：

#object -- 对象。
#name -- 字符串，属性名
class Coordinate:
    x = 10
    y = -5
    z = 0
point1 = Coordinate()
print(hasattr(point1,'x'))
print(hasattr(point1,'y'))
print(hasattr(point1,'z'))
print(hasattr(point1,'yes'))
