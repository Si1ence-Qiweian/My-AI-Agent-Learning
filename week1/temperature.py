def celsius_to_fahrenheit(celsius: float) -> float:
    fahrenheit = celsius * 9 / 5 + 32
    return fahrenheit
def fahrenheit_to_celsius(fahrenheit: float) -> float:
    celsius = (fahrenheit - 32) * 5 / 9
    return celsius
def main():
    print("Temperature tansasor")
    print("1: celsius_to_fahrenheit")
    print("2: fahrenheit_to_celsius")
    mod = input("请选择1 或 2:")
    if mod == "1":
        celsius = float(input("输入摄氏温度:"))
        farenheit = celsius_to_fahrenheit(celsius)
        print(f"{celsius}℃ = {farenheit}℉")
    elif mod == "2":
        farenheit = float(input("输入华氏温度:"))
        celsius = fahrenheit_to_celsius(farenheit)
        print(f"{farenheit}℉ = {celsius}℃")
    else:
        print("只能输入1 或 2")
if __name__ == "__main__":
    main()