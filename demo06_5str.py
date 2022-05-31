# 格式化字符：%s
# 格式化整数：%d
# 格式化浮点数：%f

my_str = "my name is %s" % ('tong')
print(my_str)
my_str1 = "张三 今年 %d" % (23)
print(my_str1)
my_str2 = "一斤苹果 %f 元" % (4.33)
print(my_str2)
#%m.nf m显示长度 n表示小数位数 -号代表左对齐 前面+0 空格用0代替
my_str3 = "一斤苹果 %05.2f 元" % (6.77)
print(my_str3)
#format格式化两个参数 "{}{}".format 如果{}里加数字 就代表后面加入参数的顺序 关键词参数"{x}".format(x='值')
my_str4 = "今天星期{} 张三 今年 {}岁".format('一','5')
print(my_str4)
my_str5 = "今天星期{x} 张三 今年 {y}岁".format(x ='hello' ,y ='word')
print(my_str5)

#链接字符串 join
astr = "-"
bstr = astr.join("wold")
print(bstr)
#分割字符串split
cstr = "hellowordpythonjava"
dstr = cstr.split("o")
print(dstr)
#查找字符串 find找到返回最小索引 找不到返回-1
ee = "hellowrold"
print(ee.find('o'))
print(ee.find('p'))
#查找以xxx结尾的字符串endswith
ff = '测试报告.doc'
if ff.endswith('oc'):
    print('他是一个word文件')
#替换字符串
# dd = 'hellowrold'
# dd = ee.replace()
# 12. 输入一行字符，分别统计出其中英文字母、空格、数字和其它字符的个数。
gg = 'vjsf gkadLDVHY 26348O91574'
zf = 0
kg = 0
sz = 0
other = 0
for x in gg:
    if x.isalpha():       #判断是不是字符
        zf += 1
    elif x.isdigit():      #判断是不是数字
        sz += 1
    elif x.isspace():       #判断是不是空格
        kg += 1
    else:
        other += 1
print(zf)
print(sz)
print(kg)
print(other)

#列表推导式 1-10打印奇数

print('='* 30)
for x in range(1,11):
    if x % 2:
        print(x)
hh = [x for x in range(1,11) if x % 2]
print(hh)

# for x in range(1,10):
#     for y in range(1,10):
#         print(x,'*',y,'=',x*y,end='\t')

tt = [x,'*',y,'=',x*y,end='\t' for x in range(1,10) for y in range(1,10)]
print(tt)