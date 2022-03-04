import re
import math

s = 0
str = "There is no hate without fear. Hate is crystallized fear, fear' s  dividend, fear objectivized. We hate what we fear and so where hate is,  fear is lurking. ."
str = re.sub("[.,']",'',str)
dic = {}
all_sign = len(str)

for per in str:

    if per not in dic:
        dic[per] = 1
    else:
        dic[per] += 1
a = 0
for i in dic:
    a += 1
    p = round(dic[i]/all_sign,6)

    if i == " ":
        print("空格的频率：",p,end=" ")
    else :
        print("{}的频率：".format(i), p,end="   ")

    if a % 3 == 0:
        print("")
    s += (p) * ((math.log(p)/(math.log(2))))
s = -s
print('信息熵：',s)