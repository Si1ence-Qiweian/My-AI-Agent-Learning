# ======= 练习1: 个人名片 =======
name = "小明"
age = 20
city = "杭州"
print(f"我叫{name}, {age}岁, 来自{city}。")

# ======= 练习2: 四则运算 =======
a = 17
b = 5
print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a // b)
print(a % b)

# ======= 练习3: 摄氏转华氏 =======
c = 37
F = c * 9 / 5 + 32
print(f"{c}℃ = {F}℉")

# ======= 练习4: 奇偶判断 =======
n = 17
if n % 2 == 0:
    print(f"{n} 是偶数")
else: print(f"{n} 是奇数")

n = 20
if n % 2 == 0:
    print(f"{n} 是偶数")
else: print(f"{n} 是奇数")

# ======= 练习5: 成绩等级 =======
score = 78
if score >= 90: grade = "A"
elif score >= 80: grade = "B"
elif score >= 60: grade = "C"
else: grade = "D"
print(f"成绩 {score}, 等级 {grade}")

# ======= 练习6: 打印1 到 10 =======
for i in range(1, 11):
    print(i)

# ======= 练习7: 求1 到 100 的和 =======
sum = 0
for i in range(0, 101):
    sum = sum + i
print(sum)

# ======= 练习8: 求1 到 100 的偶数和 =======
sum = 0
for i in range(1, 101):
    if i % 2 == 0:
        sum = sum + i
print(sum)

# ======= 练习9: 倒计时 =======
n = 5
while n > 0:
    print(n)
    n -= 1
print("发射！")

# ======= 练习10: 打印 5x5 星号矩形 =======
for _ in range(5):
    print("*" * 5)

