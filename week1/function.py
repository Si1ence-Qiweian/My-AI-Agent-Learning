# ======= 练习1: 加法函数 =======
def add(a, b):
    return a + b
print(add(3, 4))

# ======= 练习2: 判断偶数 =======
def is_even(n):
    if n % 2 == 0:
        return True
    else:
        return False
print(is_even(10))
print(is_even(7))

# ======= 练习3: 三个数中的最大值 =======
def max_of_three(a, b, c):
    max_val = a
    if b > max_val:
        max_val = b
        if c > max_val:
            max_val = c
    return max_val
print(max_of_three(3, 9, 5))

# ======= 练习4: 统计元音字母 =======
def count_vowels(text):
    text = text.lower()
    vowels = "aeiou"
    count = 0
    for char in text:
        if char in vowels:
            count += 1
    return count
print(count_vowels("hello, world!"))
print(count_vowels("AEIOU"))

# ======= 练习5: 摄氏转华氏 =======
def celsius_to_fahrenheit(celcius):
    fahrenheit = celcius * 9 /5 + 32
    return fahrenheit
print(celsius_to_fahrenheit(37))
print(celsius_to_fahrenheit(100))

# ======= 练习6: FizzBuzz函数化 =======
def fizzbuzz(n):
    if n % 15 == 0:
        return "FizzBuzz"
    elif n % 5 == 0:
        return "Buzz"
    elif n % 3 == 0:
        return "Fizz"
    else:
        return n
for i in range(1, 31):
    print(fizzbuzz(i))