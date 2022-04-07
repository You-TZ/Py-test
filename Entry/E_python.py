'''
Author: your name
Date: 2022-04-07 08:56:42
LastEditTime: 2022-04-07 09:16:30
LastEditors: Please set LastEditors
Description: 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
FilePath: \Py-test\Entry\E_python.py
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