import math
import time
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
map = {
    "coefficient": [1, 5, 3, 4, 89, 8],
    "a": 10,
    "z": 90,
}
result = []
result.append(map["coefficient"][-1])
n = len(map["coefficient"])
for i in range(1, n):
    result.append(0)
#以上是计算的准备工作，不计入时间

#计算开始
timeStart = time.time()
for j in range(n-2, -1, -1):
    for i in range(n-j-1, 0, -1):
        result[i] = (map["z"]-map["a"])*result[i]+result[i-1]
    result[0] = (map["z"]-map["a"])*result[0]+map["coefficient"][j]

for z in range(0, n):
    result[z] = result[z]*math.factorial(z)
#计算结束

timeEnd = time.time()
showResult(result, map)
print("消耗时间:"+str(timeEnd-timeStart))
print("第二种代码实现")
