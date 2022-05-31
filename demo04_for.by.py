#for循环语句
"""
格式
for 循环变量 in 序列
    代码块

"""
my_str = "abfdef"
for h in my_str:
    print(h)
print("===========")
a = 1
while a<=5:
    a+=1
    print(a)
#计算1-100的和

sum = 0
a = 1
while a <=100:
    sum += a
    a += 1
print(sum)

"""
range(start,end,step)
start:代表数列的开始索引，包括开始索引。此参数若省略，默认从0开始
end：代表数列的结束索引，不包括结束索引，必填
step:步长，每次跳跃的步数 。此参数若不填写，默认步长为1
"""
#打印1-10的数字
for h in range(11):
    print(h)

print("===========")

#break语句断开循环    continue语句进行跳出本次循环（循环1-10 遇到7跳过）
#循环1-10 当遇到7退出循环
for x in range(1,10,1):
    print(x)
    if x == 7:
        break
for x in range(1,10,1):
    if x == 7:
        continue
    print(x)
