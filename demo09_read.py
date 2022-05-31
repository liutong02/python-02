# #读取文件
# f = open('a.txt','r')
# # result = f.read()
# # print(result)
# # #写文件
# # f = open('a.txt','w')
# # f.write("hello php\n")
# # f.write("hello java")
# #按行读取
# while True:
#     line = f.readline()
#     print(line,end='')
#     if not line:
#         break
# #方法二
# for x in f.readlines():
#     print(x)
#异常 try ... except语句
def div(x,y):
    try:
        z = x / y
        return z
    except Exception as e:
        print('不能为0')
print(div(6,3))
print(div(6,0))
print(div(6,2))

if __name__ == '__main__':
    print(div(9,8))