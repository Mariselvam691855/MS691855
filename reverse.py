s = (input("Enter a word : "))
str = ""


for i in s:
    str = i + str
print (str)
 

 
print("The original word is : ", end="")
print(s)
 
print("The reversed word is : ", end="")
print(str)