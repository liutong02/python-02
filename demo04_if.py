#条件语句
"""
格式
if 条件：
    代码（如果是真 执行这个代码 ）
 else
    代码（如果是假 执行这个代码 ）
"""

a = 10
if a <13:
    print("a是小于13的数")
else:
    print("a是大于13的数")

"""
if 条件判断1:    
代码
1elif 条件判断2:    
代码
2elif 条件判断3： 
代码
3else:    代码4
"""
score = 82
if score > 90:
    print("优秀")
elif score >80:
    print("良")
elif score >60:
    print("及格")
else:
    print("不及格")

if score >70 and score <90:
    print("良")

if 1.1:
    print("hello1")
if a:
    print("hello02")

