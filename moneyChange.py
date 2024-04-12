#找錢問題
a = int(input()) #客人消費金額
x = 1000 - a

n1 = x // 500
n2 = (x % 500) // 100
n3 = (x % 500 % 100) // 50
n4 = (x % 500 % 100 % 50) // 10
n5 = (x % 500 % 100 % 50 % 10) // 5
n6 = x % 500 % 100 % 50 % 10 % 5
s = "" #空字串

if n1>0 and (n2>0 or n3>0 or n4>0 or n5>0 or n6>0):
    s += "500, " + str(n1) + "; "
elif n1>0:
    s += "500, " + str(n1)

if n2>0 and (n3>0 or n4>0 or n5>0 or n6>0):
    s += "100, " + str(n2) + "; "
elif n2>0:
    s += "100, " + str(n2)

if n3>0 and (n4>0 or n5>0 or n6>0):
    s += "50, " + str(n3) + "; "
elif n3>0:
    s += "50, " + str(n3)

if n4>0 and (n5>0 or n6>0):
    s += "10, " + str(n4) + "; "
elif n4>0:
    s += "10, " + str(n4)

if n5>0 and n6>0:
    s += "5, " + str(n5) + "; "
elif n5>0:
    s += "5, " + str(n5)

if n6 != 0:
    s += "1, " + str(n6)

print(s) 
