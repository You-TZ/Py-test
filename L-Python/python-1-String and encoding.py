#在最新的Python 3版本中，字符串是以Unicode编码的，Python的字符串支持多语言
print('包含中文的str')
#对于单个字符的编码，Python提供了ord()函数获取字符的整数表示，chr()函数把编码转换为对应的字符：
ord('A')
ord('中')
ord('a')
chr(66)
chr(25991)
#如果知道字符的整数编码，还可以用十六进制这么写str
'\u4e2d\u6587'
#两种写法完全是等价的。
#由于Python的字符串类型是str，在内存中以Unicode表示，一个字符对应若干个字节。如果要在网络上传输，或者保存到磁盘上，就需要把str变为以字节为单位的bytes。
#Python对bytes类型的数据用带b前缀的单引号或双引号表示：
x = b'ABC'
#要注意区分'ABC'和b'ABC'，前者是str，后者虽然内容显示得和前者一样，但bytes的每个字符都只占用一个字节。
#以Unicode表示的str通过encode()方法可以编码为指定的bytes，例如：
'ABC' .encode('ascii')
'中文' .encode('utf-8')
#纯英文的str可以用ASCII编码为bytes，内容是一样的，含有中文的str可以用UTF-8编码为bytes。含有中文的str无法用ASCII编码，因为中文编码的范围超过了ASCII编码的范围，Python会报错。
'中文'.encode('ascii')
 #Traceback (most recent call last):
 #File "<stdin>", line 1, in <module>
 #UnicodeEncodeError: 'ascii' codec can't encode characters in position 0-1: ordinal not in range(128)\

#在bytes中，无法显示为ASCII字符的字节，用\x##显示。
#反过来，如果我们从网络或磁盘上读取了字节流，那么读到的数据就是bytes。要把bytes变为str，就需要用decode()方法：
b'abc'.decode('ascii')
b'\xe4\xb8\xe6\x96\x87'.decode('utf-8')
#如果bytes中包含无法解码的字节，decode()方法会报错：
b'\xe4\xb8\xad\x96\x87'.decode('utf-8')
#Traceback (most recent call last):
  #File "<stdin>", line 1, in <module>
  #UnicodeDecodeError: 'utf-8' codec can't decode byte 0x96 in position 3: invalid start byte

#如果bytes中只有一小部分无效的字节，可以传入errors='ignore'忽略错误的字节：
b'\xe4\xb8\xad\xff'.decode('utf-8',errors='ignore')
#要计算str包含多少个字符，可以用len()函数：
len('abc')
len('中文')
len('先帝创业未半而中道崩殂，今天下三分，益州疲弊')
#len()函数计算的是str的字符数，如果换成bytes，len()函数就计算字节数：
len(b'abc')
len(b'\xe4\xb8\xad\xe6\x96\x87')
len('中文语言' .encode('utf-8'))
len(b'\xe4\xb8\xad\xe6\x96\x87'.decode('utf-8'))
#可见，1个中文字符经过UTF-8编码后通常会占用3个字节，而1个英文字符只占用1个字节。
#在操作字符串时，我们经常遇到str和bytes的互相转换。为了避免乱码问题，应当始终坚持使用UTF-8编码对str和bytes进行转换。
#由于Python源代码也是一个文本文件，所以，当你的源代码中包含中文的时候，在保存源代码时，就需要务必指定保存为UTF-8编码。当Python解释器读取源代码时，为了让它按UTF-8编码读取，我们通常在文件开头写上这两行：
 #!/usr/bin/env python3
 # -*- coding: utf-8 -*-
 #第一行注释是为了告诉Linux/OS X系统，这是一个Python可执行程序，Windows系统会忽略这个注释；
 #第二行注释是为了告诉Python解释器，按照UTF-8编码读取源代码，否则，你在源代码中写的中文输出可能会有乱码。
#申明了UTF-8编码并不意味着你的.py文件就是UTF-8编码的，必须并且要确保文本编辑器正在使用UTF-8 without BOM编码：
#如果.py文件本身使用UTF-8编码，并且也申明了# -*- coding: utf-8 -*-，打开命令提示符测试就可以正常显示中文：

#格式化
 #最后一个常见的问题是如何输出格式化的字符串。我们经常会输出类似'亲爱的xxx你好！你xx月的话费是xx，余额是xx'之类的字符串，而xxx的内容都是根据变量变化的，所以，需要一种简便的格式化字符串的方式。
 #在Python中，采用的格式化方式和C语言是一致的，用%实现，举例如下：
'hello, %s' % 'word'
'hi, %s, you have $%d.' % ('micheal' , 100000)
 #%运算符就是用来格式化字符串的。在字符串内部，%s表示用字符串替换，%d表示用整数替换，有几个%?占位符，后面就跟几个变量或者值，顺序要对应好。如果只有一个%?，括号可以省略。
 #常见的占位符有：

#占位符	 替换内容
#%d	    整数
#%f	    浮点数(默认保留小数点后6位，超过5位则四舍五入)
#%s	    字符串
#%x	    十六进制整数
#其中，格式化整数和浮点数还可以指定是否补0和整数与小数的位数：
print('%2d-%02d' %(3,1))
print('%d-%02d' %(3,1))
print('%d-%2d' %(3,1))
#以上可进行运行对比进行理解
print('%.2f' %3.1415926)
print('%f' %3.1415926)
#%s会把任何数据类型转换为字符串
'age: %s.Gender: %s' %(10000,True)
'age: %s Gender: %s' %(500,'中文')
#有些时候，字符串里面的%是一个普通字符怎么办？这个时候就需要转义，用%%来表示一个%：
'growth rate %d %%' % 7
'部门昨日业绩于本月业绩占比 %d %%' %8
#format()
#另一种格式化字符串的方法是使用字符串的format()方法，它会用传入的参数依次替换字符串内的占位符{0}、{1}……，不过这种方式写起来比%要麻烦得多：
'hello, {0}, 成绩提升了{1:.1f}%' . format('小花',17.125)
#f-string
#最后一种格式化字符串的方法是使用以f开头的字符串，称之为f-string，它和普通字符串不同之处在于，字符串如果包含{xxx}，就会以对应的变量替换：
r=2.5
s=3.14 * r ** 2
print(f'the area of a circle with radius {r} is {s:.2f}')
#上述代码中，{r}被变量r的值替换，{s:.2f}被变量s的值替换，并且:后面的.2f指定了格式化参数（即保留两位小数），因此，{s:.2f}的替换结果是19.62。
#小明的成绩从去年的72分提升到了今年的85分，请计算小明成绩提升的百分点，并用字符串格式化显示出'xx.x%'，只保留小数点后1位：
s1=72
s2=85
r=s2/s1*100-100
n='小花'
print('第一种占位符表示方法, %s今年成绩为%d,比去年提升的%d提升了%.1f%%'%(n,s2,s1,r))
print('第二种format表示方法， {0}今年的成绩为{1}，相比去年的{2}提升了{3:.1f}%'.format(n,s2,s1,r))
print(f'第三种f-string表示方法： {n}今年的成绩事{s2}，相对于去年的{s1}提高了{r:.1f}%')