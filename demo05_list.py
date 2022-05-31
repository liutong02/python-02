
alst = [] #定义空列表
blst = [11,23,'hds',None]

print(alst)
print(blst)

#循环列表
for x in blst:
    print("列表中的值:",x)
clst = ['red','black','yellow']

#在列表末尾添加新的元素 list.append(odj) odj=元素
clst.append('blue')
print(clst)

#从列表某个位置插入某个元素 list.insert(inedx,odj)
clst.insert(2,'hello')
print(clst)

for x in range(2,10,2):
    print(x)

#元祖不可以修改

tp1 = ()
tp2 = (1,11,1.2)
print(tp1)
print(tp2)

#字典
#字典的定义：变量名 = {key1:value1,key2:value2}

dct1 = {}
dct2 = {'a':1,'b':2}
print(dct1)
print(dct2)

#查找 dict[‘键名‘] 或 dict.get(‘键名‘) 这个查询没有的值不会报错
# 更新dict[‘键名‘] = 值
print(dct2['b'])
print(dct2.get('d'))
dct2['b'] = 12
print(dct2)

a = 0
if a:
    print(a)
c = 'hello'
# 2. 打印1~100内被3整除的所有数的和 。
sum = 0
for x in range(0,101,3):
    sum += x
print(sum)

# 3. 使用range()输出1~10内的所有奇数 。
# 4. 打印1~100所有偶数的和 减去 所有奇数的和 的值
# 5. 求1+2+3+...+100的和
# 6. 判断一个数n能同时被3和5整除