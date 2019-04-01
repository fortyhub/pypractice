#!/usr/bin/env python

list = ['baozi','mantou','ji','ya','apple']

list.append('miantiao')
list.pop(-1)
#栈的实现
print(list)

list.append('mifen')
del list[0]
print(list)
del list[0]
print(list)

print(list.index('ji'))

list.insert(2,'zhu')

print(list)