# A very simple BMI calculator just for fun
print("請輸入您的身高：")
height=float(input())

print("請輸入您的體重：")
weight=float(input())

BMI=weight/(height/100)**2

print("您的BMI為",round(BMI, 2))
if BMI<18.5:
    print("體重過輕")
elif BMI<24:
    print("體重正常")
else:
    print("體重過重")
