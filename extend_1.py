import math
import time

def Horner(map):
    coefficient = map["coefficient"]
    a = map["a"]
    z = map["z"]
    b = []
    Max = len(coefficient)
    b.append(coefficient[-1])
    for i in range(Max-2, -1, -1):
        b.append(b[-1]*(z-a)+coefficient[i])

    b.reverse()
    return b

def showResult(result, map):
    length = len(result)
    print("z=" + str(map['z']))
    for i in range(0, length):
        if i == 0:
            print("f(z)的函数值:"+str(result[0]))
        else:
            print("f(z)的"+str(i)+"阶倒数的函数值:"+str(result[i]))


#函数一些参数，每一项的次数[a0, a1, a2, a3,...],
#f(x)=求和aj*(z-a)^j,j=0,1,2,3,4...
#初始函数条件
map={
    "coefficient": [1, 5, 3, 4, 89, 8],
    "a": 10,
    "z": 90,
}
#函数最多可以求steps阶导
steps = len(map["coefficient"])-1
i = 0
result = []
#以上计算的准备工作


#计算开始
timeStart = time.time()
while i <= steps:
    b = Horner(map)
    map['coefficient'] = b[1:]
    result.append(math.factorial(i)*b[0])
    i = 1 + i
#计算结束
timeEnd = time.time()

showResult(result, map)
print("消耗时间:"+str(timeEnd-timeStart))
print("第一种代码实现")