#
# a = 2+3
# b = 725
#
# print(not a < 7)
#
# score = 76
# if score >90:
#     print('优')
# elif score>75:
#     print('良')
# elif score>60:
#     print('及格')
# else:
#     print('不及格')
#
# for x in range(1,11,2):
#     if x == 5:
#         continue
#     print(x)
# lst = [234]
# lst1 = ['red',1,1,2,3]
#
# lst1.append('blak')
# print(lst1)
# print(lst1.count(1))
# print(lst1.index(3))
#
# lst1.extend(lst)
# lst1.remove(2)
# lst1.reverse()
# print(lst1)
#
# # c = {'city':'北京','age':22,'name':'cc'}
# # print(c)
# # print(c['name'])
# # # print(c.get['name'])
# # print('name' in c)
# # print(c.keys())
# # for x in c.keys():
# #     print(x)
# # print(c.values())
# # print(c.items())
#
# # 1. 输入a,b,c,d4个整数，计算a+b-c*d的结果
# #a = input('请输入数字:')
#  # b = input('请输入数字:')
#  # c = input('请输入数字:')
#  # d = input('请输入数字:')
#  # print(int(a)+int(b)-int(c)*int(d))
# # 2. 打印1~100内被3整除的所有数的和 。
# # sum = 0
# # for x in range(0,101):
# #     if x % 3 == 0:
# #         sum += x
# # print(sum)
# # 3. 使用range()输出1~10内的所有奇数 。
# for x in  range(1,11,2):
#     print(x)
# # 4. 打印1~100所有偶数的和 减去 所有奇数的和 的值
# sum1 = 0
# sum2 = 0
# for x in range(1,101):
#     if x % 2 == 0:
#         sum1 += x
#     else:
#         sum2 += x
# print(sum1-sum2)
#  # 5. 求1+2+3+...+100的和
# sum = 0
# for x in range(1,101):
#     sum += x
# print(sum)
# # 6. 判断一个数n能同时被3和5整除
# # n = input('请输入一个值:')
# # n = int(n)
# # if n%3 ==0 and n% 5 == 0:
# #     print('可以')
# # else:
# #     print('不行')
#
# # 7. 定义一个整数变量，判断该变量值是否是1-100内的某个数，如果是打印出来
# # e = input('请输入数值')
# # e = int(e)
# # for x in range(0,101):
# #     if x==e:
# #         print('是')
# # #         方法2
# # if 0 < e < 100:
# #     print('是')
# # else:
# #     print('不是')
# # 8. 输入三个整数x,y,z，请把这三个数由小到大输出。备注：输入方法：input()
#  x = input('请输入数值')
#  y = input('请输入数值')
#  z = input('请输入数值')
#  x = int(x)
#  y = int(y)
#  z = int(z)
#  lst1 = [x,y,z]
#  print(lst1)
#  lst1.sort()
#  print(lst1)
# # 9. 利用条件运算符的嵌套来完成此题：学习成绩>=90分的同学用A表示，60-89分之间的用B表示，
# # 60分以下的用C表示。备注：需要使用input()方法
# r = input()
# r = int(r)
# if r >= 90:
#     print('a')
# elif r >= 60:
#     print('b')
# else:
#     print('c')
#
# # 10. 将一个列表的数据复制到另一个列表中。
# l1 = [1,2]
# l2 = [78,9]
# l2.extend(l1)
# print(l2)
# # 11. 输出 9*9 乘法口诀表
#
# for x in range(1,10):
#     for y in range(1,10):
#         print(x,'*',y,'=',x*y,end='\t')
#     print

#索引
#切片：名字[start:end:step],start代表位置，默认0开始，end代表结束位置，默认列表长度，step代表步长

zz = ['red', 'ff', 'blue', 2, 3, 4]
ww = 'red','ff','blue',2,3,4
print(ww)
print(ww[2])
print(zz[1])
print(zz[-1])
print(zz[1:3:1])
print(zz[::1])
print(zz[2:])

#序列的相加 相乘
alst = [1,2]
blst = [3,4]
clst = alst + blst
print(clst)
dlst = alst *2
print(dlst)

elst = [None] * 3
print(elst)
#循环序列中的索引和值
zz1 = ['red', 'ff', 'blue', 2, 3, 4]
for x,y in enumerate(zz1):
    print(x,'=======',y)
gg = str(zz)
print(gg)
print(type(gg))
