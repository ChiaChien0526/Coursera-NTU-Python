# 報童問題(第四週 Q1練習題)

c = int(input()) #進貨成本
r = int(input()) #零售價格
N = int(input()) #需求個數
q = int(input()) #訂貨量

p = [] #各訂購量機率
for i in range(N+1):
    p.append(float(input()))

profit = 0 #預期利潤
p_q = 1 #訂購q個的機率

for j in range(N+1):
    if j < q:
        profit += (r * j - q * c) * p[j] #訂購0 ~ q-1個的利潤
        p_q -= p[j]
    else:
        profit += (r * j - q * c) * p_q #訂購q個的利潤
        break

print(int(profit))
