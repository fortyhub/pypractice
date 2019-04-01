#!/usr/bin/env python

# 有这么一个情景，你是个厨师，我是顾客，你做好了五碗饭（一次只能做一碗）
# 放在桌子上，我去吃（只能按你上的顺序吃，不然第一碗就凉了），记录每一步
# 我吃的时候桌子上的饭还有几碗和是第几次做的饭。


#队列实现
meal = ['one','two','there','four','five']

for i in range(len(meal)):
    del meal[0]
    print("桌上还有"+str(len(meal))+"碗")
    print("现在吃的是第"+str(i+1)+"次做的饭")

#栈实现
meal_1 = ['one','two','there','four','five']
meal_2 = []

for j in range(1,3):
    if len((eval('meal_'+str(j)))) == 0:
        null_list = eval('meal_'+str(j))

for num in range(0,5):
    pass

#啊  睡了  就是取出meal_？中的后面几个  写入空list  循环往复。取出栈的第一个，必须先取出后几个。就这样~