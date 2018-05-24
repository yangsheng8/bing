#流程控制

"""
if condition_1:
    statement_block_1
elif condition_2:
    statement_block_2
else:
    statement_block_3
"""

var1 = 20
if var1:
    print("var1:",var1)

var2 = False
if var2:
    print("var2:",var2)

print("end")

print("===========================================");

# var3 = 10
# if var3<10:
#     print("小于10！")
# elif var3 == 10:
#     print("等于10！")
# else:
#     print("大于10")


print("循环语句===========================================");

#while循环语句
"""
while 判断条件：
    语句
"""
# n  = 100
# sum = 0
# counter = 1
# while counter <= n:
#     sum += counter
#     counter +=1

# print("sum:",sum)

# print("死循环语句===========================================");
# while True:
#     mun = int(input("请输入一个数字:"))
#     print("输入的数字是:",mun)

# print("循环结束！")


# counter = 0
# while counter <3:
#     print('counter:',counter)
#     counter+=1
# else:
#     print("else counter:",counter)

#for 循环语句
"""
for <variable> in <sequence>:
    <statements>
"""

# for a in [1,2,3,4,5,6,7]:
#     print("a = ",a)
# else:
#     print("a > 7!")

'''
range() 函数
'''
for a in range(0,5):
    print("a1 =",a)

for a in range(3,5):
    print("a2 = ",a)

#加上步长，2 就是每输出一个值，加2 在输出。
for a in range(1,6,2):
    print("a3 = ",a)