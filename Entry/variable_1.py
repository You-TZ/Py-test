'''
Author: your name
Date: 2022-04-27 09:57:39
LastEditTime: 2022-04-27 09:57:39
LastEditors: Please set LastEditors
Description: 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
FilePath: \Py-test\Entry\variable.py
'''
print('HELLO WORLD')

#变量

message = 'Hello Python World'

print(message)

message = 'Hello Python Crash Course world'

print(message)

# 在程序中可随时修改变量的值，而Python将始终记录变量的最新值。

#字符串

name = 'ada lovelace'

print(name.title())

# title()以首字母大写的方式显示每个单词，即将每个单词的首字母都改为大写

# 改为全部大写或全部小写

name = 'Ada Lovelace'

print(name.upper())

print(name.lower())

# 合并(拼接)字符串

first_name = 'ada'

last_name = 'lovelace'

full_name = first_name + ' ' + last_name

print(full_name)

print('Hello,' + full_name.title()+ ' !')

message = 'Hello,' + full_name.title() + ' !'

print(message)

# 制表符和换行符

print('\tPython')  #\t制表符

print('Language:\nPython\nC\nJavaScript') # \n换行符

print('Language: \n\tPython\n\tC\n\tJavaScript')

#删除空白

favorite_language = 'python '

favorite_language

favorite_language.rstrip()  #暂时删除

favorite_language  

# 若要永久删除，必须将删除操作的结果存回到变量中：

favorite_language = 'python '

favorite_language = favorite_language.rstrip()

favorite_language

#剔除字符串的开头空白或同时剔除字符串俩端的空白

favorite_language = '  python  '

favorite_language.rstrip()  #删除末尾空白

favorite_language.lstrip()  #删除开头空白

favorite_language.strip()  #删除俩端空白

#数字

# 整数

2+3

3-2

2*3

3/2

# 俩个乘号代表乘方运算

3 ** 2

3 ** 3

10 ** 6

2 + 3 * 4

(2 + 3) **4

# 浮点数

0.1 + 0.1

0.2 + 0.2

2 * 0.1

2 * 0.2

# 注意，包含的小数位数可能是不确定的

0.2 + 0.1

3 * 0.1

#使用函数str()避免类型错误

age = 25 

message = 'Happy' + str(age) + 'rd Birthday'

message

import this

from debugpy import debug_this_thread