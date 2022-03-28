#字符串内部既包含'又包含"怎么办？可以用转义字符\来标识，比如：
print('I\'m ok.')
#转义字符\可以转义很多字符，比如\n表示换行，\t表示制表符，字符\本身也要转义，所以\\表示的字符就是\
print('i\'m learning\npython.')
print('\\\n\\')
#字符串里面有很多字符都需要转义，就需要加很多\，为了简化，Python还允许用r''表示''内部的字符串默认不转义，
print('\\\t\\')
print(r'\\\t\\')
#字符串内部有很多换行，用\n写在一行里不好阅读，为了简化，Python允许用'''...'''的格式表示多行内容
print('''line1
...line2
...line3''')
#多行字符串'''...'''还可以在前面加上r使用
print(r'''hello, \n world''')
#布尔值和布尔代数的表示完全一致，一个布尔值只有True、False两种值，要么是True，要么是False
#or运算是或运算，只要其中有一个为True，or运算结果就是True
True and True
True and False
3>2
3>5
False and False
5>3 or 1>3
#not运算是非运算，它是一个单目运算符，把True变成False，False变成True
not True
not False
not 1>2
#布尔值经常用在条件判断中
if age >=18:
   print('adult')
else:
   print('teenager')