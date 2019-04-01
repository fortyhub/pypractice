#!/usr/bin/env python

import json

#dumps()方法把数据类型转化成字符串
a = [{'姓名': 'Kaina', '年龄': 22, '职业': '销售员', '工资': 5000}]
print(type(a))
b = json.dumps(a)
print(type(b))

#dump()方法把数据类型转化成字符串并存储在文件中

with open("aim.json","a",encoding='utf-8') as f:
    a = [{'姓名': 'Kaina', '年龄': 22, '职业': '销售员', '工资': 5000}]
    print(type(a))
    '''
    1.消除乱码ensure_ascii=False
    2.把数据类型转换成字符串并存储在文件中
    '''
    b = json.dump(a,f,ensure_ascii=False)
    print('数据写入完毕')

#loads与load
json_data = open('test.json',encoding='utf-8').read()
print(type(json_data))
data = json.loads(json_data)
print(type(data))
print(data)

for item in data:
    print(item)

with open('test.json',encoding='utf-8') as f:
    data = json.load(f)
    for dict_data in data:
        print(dict_data)

#获取字典某一键对应的值
f = open('test.json',encoding='utf-8')
data = json.load(f)
for dict_data in data:
    print(dict_data['姓名'],'工资='+str(dict_data['工资']))