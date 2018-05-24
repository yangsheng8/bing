#内置数据结构

'''
List(列表)
[var1,var2,var3,...]

Tuple(元组)-- 内部的值不能改变, 只读List
（var1，var2,var3，...）

Sets(集合)
{var1,var2,var3,...} --集合内部元素不能重复

Dictionary(字典)
{key1:var1,key2:var2,key3:var3,...}

'''
# #列表
# list  = ['abcd',123,3.14,True]

# print(list)
# print(list[0])
# print(list[3])

# list2 =['list2str',100]
# #通过+合并List
# print(list + list2)

# #修改指定元素
# list[0] ='ABCD'

# #修改指定范围,[1:3]起始下标，结束下标，不包括结束下标
# list[1:3] = [777,5.20]

# print(list)
# print ("Count for 777 : ",list.count(777))

'''
1、List写在方括号之间，元素用逗号隔开。
2、和字符串一样，list可以被索引和切片。
3、List 可以使用+操作进行拼接。
4、List中的元素是可以改变的。
'''


#元组
'''
1、与字符串一样，元组的元素不能修改。
2、元组也可以被索引和切片，方法一样。
3、注意构造包含0或1个元素的元组的特殊语法规则。
4、元组也可以使用+操作符进行拼接。
'''

# #元组里面的List是可以被改变的
# tuple = ("abc",123,3.14,True,['ABA',222,False])
# print(tuple)
# print(tuple[2])
# print(tuple[1:3]) #切片，输出
# print(tuple *3)#元组的内容输出3次

# '''
# string 元组 列表 都属于序列
# 可以用于for 
# '''

# #序列可以用在for循环中
# for a in tuple:
#     print(a)


#集合
'''
集合（set）是一个无序不重复元素的序列。
基本功能是进行成员关系测试和删除重复元素。
可以使用大括号{} 或者 set() 函数创建集合
'''

#重复只显示最后一个
set1 = {"Tom","Marry","Jack","Rose","Tom"}


# print(set1)

# if "Jack" in set1 :
#     print("Jack In Set1")
# else:
#     print("Jack not in Set1")

# set2 = set("abcdefg")
# set3 = set("1234abc")

# print(set2)
# print(set3)

# print(set2 - set3) #差集  defg
# print(set2 | set3) #并集  1234abcdefg
# print(set2 & set3) #交集  abc
# print(set2 ^ set3) #交集不存在的元素   1234defg

#字典
'''
字典是一种映射类型，字典用"{ }" 标识，它是一个无序的键（key）: 值（value）对集合。
键（key）必须使用不可变类型。
在同一个字典中，键（key）必须是唯一的。
'''

dict = {}
dict['key1'] = 1
dict['key2'] = 'a'
dict[100] = "bc"

print(dict)
print(dict['key1'])
print(dict[100])

