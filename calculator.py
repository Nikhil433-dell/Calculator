print("welcome to my first programme")
num1 = input("give me the first number = ")
num2 = input("give me the second number = ")
sign = input("enter the sign = ")
num1 = int(num1)
num2 = int(num2)
if sign == "+":
    print(num1+num2)
elif sign == "-":
    print(num1-num2)
elif sign == "*":
    print(num1*num2)
elif sign == "/":
    print(num1/num2)
elif sign == "**":
    print(num1**num2)
elif sign == "//":
    print(num1//num2)
elif sign == "%":
    print(num1%num2)
else:
    print("sorry but your value of sign is wrong")
         

