import math

sum = 0
k = 0
H = 0
list_sum = [0]

list = [0.11,0.21,0.01,0.23,0.23,0.10]
list.sort(reverse=True)

for i in range(len(list)):
    #求和
    sum += list[i]
    if sum != 1:
        list_sum.append(round(sum,2))


    # 编码位数
    count = math.ceil((math.log(1/list[i])/(math.log(2))))

    #最终编码
    list_final = []
    c = list_sum[i]
    for item in range(count):

        a = c * 2
        s = math.floor(a)

        list_final.append(s)
        if s == 1:
            a -= s
            c = a
        else :
            c = a

    list_final = [str(i) for i in list_final]
    b = ''.join(list_final)

    #平均码长
    k = k + list[i]*count

    #平均信息量
    H = H + list[i]*(math.log(1/list[i])/math.log(2))
    print("出事概率：{:.2f}， 求和结果：{:.2f}， 编码位数：{}， 最终编码：{}".format(list[i],list_sum[i],count,b))
print("平均信息量：",H)
print("平均码长:",k)
print("编码效率：",H/k)


