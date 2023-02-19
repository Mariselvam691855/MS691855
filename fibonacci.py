user = int(input("Enter the number : "))
num1 = 0
num2 = 1

for i in range(0, user+1):
    if num1>50:
        break
    
    print(num1)

    num3 = num1 + num2

    num1 = num2
    num2 = num3
  