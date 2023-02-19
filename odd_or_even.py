user = int(input("number of  inputs :  "))
odd_count = 0
even_count = 0

for i in range(0, user+1):
    x = int(input("Enter the numbers : "))

    if (x % 2 == 0 ):
        even_count = even_count + 1
    else:
        odd_count = odd_count + 1
print("Even Count : ", even_count)
print("Odd Count : ", odd_count)            
