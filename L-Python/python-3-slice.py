'''
Author: your name
Date: 2022-03-23 09:05:47
LastEditTime: 2022-03-23 11:18:24
LastEditors: Please set LastEditors
Description: 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
FilePath: \sss\python-3-slice.py
'''

#取一个list或tuple的部分元素是非常常见的操作。比如，一个list如下：
L = ['Michael','Sarah','Tracy','Bob','Jack']
#取前3个元素，应该怎么做？
#笨办法：
[L[0],L[1],L[2]]
#之所以是笨办法是因为扩展一下，取前N个元素就没辙了。
#取前N个元素，也就是索引为0-(N-1)的元素，可以用循环：
r = []
n = 3
for i in range(n):
    r.append(L[i])
r
#对这种经常取指定索引范围的操作，用循环十分繁琐，因此，Python提供了切片（Slice）操作符，能大大简化这种操作。
#对应上面的问题，取前3个元素，用一行代码就可以完成切片：
L[0:3]
#L[0:3]表示，从索引0开始取，直到索引3为止，但不包括索引3。即索引0，1，2，正好是3个元素。
#如果第一个索引是0，还可以省略：
L[:4]
#也可以从索引1开始，取出2个元素出来：
L[1:3]
#类似的，既然Python支持L[-1]取倒数第一个元素，那么它同样支持倒数切片，试试：
L[-1]
L[-2:]
L[-2:-1]
#记住倒数第一个元素的索引是-1。
#切片操作十分有用。我们先创建一个0-99的数列：
L =list(range(100))
L
L[:10]
L[-10:]
L[-30:-20]
L[10:20]
#前10个数，每2个取一个：
L[:10:2]
#所有数，每5个取一个
L[::5]
#甚至什么都不写，只写[:]就可以原样复制一个list：
L[:]
#tuple也是一种list，唯一区别是tuple不可变。
# 因此，tuple也可以用切片操作，只是操作的结果仍是tuple：
(0,1,2,3,4,5)[:3]
#字符串'xxx'也可以看成是一种list，每个元素就是一个字符。
# 因此，字符串也可以用切片操作，只是操作结果仍是字符串：
'ABCDEF'[:3]
'ABCDEFGH'[::2]

#练习
#利用切片操作，实现一个trim()函数，去除字符串首尾的空格，注意不要调用str的strip()方法：

def tria(s):
    if len(s)* "" == s:
        s=""
        return s
    while s[0] == "":
        s = s[1:]
    while s[-1] == "":
        s = s[:-1]
    return s

def res(s):
    while s[:1] == "":
        s = s[1:]
    while s[-1:] == "":
        s = s[-1:]
    return s

def tria(s):
     start = 0
     end = 1
     if len(s) != 0: #空字符串直接返回空
        while start <= len(s)-1: #从左往右遍历字符串，记录下第一个非空格字符的位置。
          #如果全为空格，则计数器数值为字符串的长度
            if s[start] == " ":
              start = start + 1
            else:
              break
        if start == len(s):
            s = "" #如果计数器数值为字符串的长度，则返回空
        else:
            while end <= len(s): #从右到左遍历字符串，记录下第二个非空格字符的位置
                if s[-end] == " ":
                   end = end + 1
                else:
                    break
            s = s[start:len(s)-end+1] #对字符串切片，第一个的位置为start,最后一个非空格
                                      #字符的位置为字符串的长度减去end
     return s

# 测试:
if tria('hello  ') != 'hello':
    print('测试失败!')
elif tria('  hello') != 'hello':
    print('测试失败!')
elif tria('  hello  ') != 'hello':
    print('测试失败!')
elif tria('  hello  world  ') != 'hello  world':
    print('测试失败!')
elif tria("") != "":
    print('测试失败!')
elif tria('    ') != "":
    print('测试失败!')
else:
    print('测试成功!')

l = (' ABCDEF ')
len(l)
l[1:6]


def tria(s):
     start = 0
     end = 1
     if len(s) != 0: #空字符串直接返回空
        while start <= len(s)-1:    #从左往右遍历字符串，记录下第一个非空格字符的位置。如果全为空格，则计数器数值为字符串的长度
            if s[start] == " ":
                start = start + 1
            else:
                break
        if start == len(s):
            s = ""  #如果计数器数值为字符串的长度，则返回空
        else:
            while end <= len(s):    #从右到左遍历字符串，记录下第一个非空格字符的位置
                if s[-end] == " ":
                    end = end + 1
                else:
                    break
            s = s[start:len(s)-end+1]   #对字符串切片，第一个的位置为start，最后一个非空格字符的位置为字符串的长度减去end
     return s
if tria('hello  ') != 'hello':
    print('测试失败!')
elif tria('  hello') != 'hello':
    print('测试失败!')
elif tria('  hello  ') != 'hello':
    print('测试失败!')
elif tria('  hello  world  ') != 'hello  world':
    print('测试失败!')
elif tria("") != "":
    print('测试失败!')
elif tria('    ') != "":
    print('测试失败!')
else:
    print('测试成功!')


def  trt(v):
     start = 0
     end  = 1
     if len(v) != 0:
        while start <= len(v)-1:
            if v[start] == "":
                 start = start + 1
            else:
                break
        if start == len(v):
            v = ""
        else:
            while end <= len(v):
                if v[-end] == "":
                    end = end + 1
                else:
                    break
            v = v[start:len(v)-end+1]
     return v
if trt('hello  ') !='hello':
    print('测试失败1')
elif trt('  hello') != 'hello':
    print('测试失败2')
elif trt('  hello  ') != 'hello':
    print('测试失败3')
elif trt(' hello world  ') !='hello world':
    print('测试失败4')
elif trt('') !='':
    print('测试失败5')
elif trt('    ') !='':
    print('测试失败6')
else:
    print('测试成功！')

def trim(s):
    start = 0

    end = 1

    if len(s) != 0: #空字符串直接返回空

        while start <= len(s)-1:    #从左往右遍历字符串，记录下第一个非空格字符的位置。如果全为空格，则计数器数值为字符串的长度

            if s[start] == " ":

                start = start + 1

            else:

                break

        if start == len(s):

            s = ""  #如果计数器数值为字符串的长度，则返回空

        else:

            while end <= len(s):    #从右到左遍历字符串，记录下第一个非空格字符的位置

                if s[-end] == " ":

                    end = end + 1

                else:

                    break

            s = s[start:len(s)-end+1]   #对字符串切片，第一个的位置为start，最后一个非空格字符的位置为字符串的长度减去end

    return s
# 测试:
if trim('hello  ') != 'hello':
    print('测试失败!')
elif trim('  hello') != 'hello':
    print('测试失败!')
elif trim('  hello  ') != 'hello':
    print('测试失败!')
elif trim('  hello  world  ') != 'hello  world':
    print('测试失败!')
elif trim('') != '':
    print('测试失败!')
elif trim('    ') != '':
    print('测试失败!')
else:
    print('测试成功!')

def tut(k):
    start = 0

    end = 1

    if len(k) != 0:

        while start <= len(k)-1:

            if k[start] == ' ':

                start = start + 1
            
            else:

                break

        if start == len(k):

            k = ''

        else:

            while end <= len(k):

                if k[-end] == ' ':

                    end = end + 1
                
                else:

                    break

            k =k[start:len(k)-end+1]
        
    return k

# 测试:
if tut('hello  ') != 'hello':
    print('测试失败!')
elif tut('  hello') != 'hello':
    print('测试失败!')
elif tut('  hello  ') != 'hello':
    print('测试失败!')
elif tut('  hello  world  ') != 'hello  world':
    print('测试失败!')
elif tut('') != '':
    print('测试失败!')
elif tut('    ') != '':
    print('测试失败!')
else:
    print('测试成功!')

