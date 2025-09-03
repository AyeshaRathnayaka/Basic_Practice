#check whether a given number is even or odd
No1=int(input("enter an integer : "))
if No1 / 2 == 0 :
    print("Even")
else:
    print("Odd")







 # input marks and display whether the student passed or failed (Pass mark = 40).
Mark = int(input("Mark : "))
if Mark > 40:
    print("Pass")
else:
    print("Fail")









#convert Celsius temperature into Fahrenheit.

Celcius= float(input("Celsius temperature :"))
Fahrenheit=float(Celcius*9/5+32)
print("Fahrenheit is : " + str(Fahrenheit))






#find the largest among three numbers
No1=input("First Number : ")
No2=input("Second Number : ")
No3=input("Third Number: ")

if No1>No2>No3 :
    print("Largest Number is "+ str(No1))
elif No1<No2<No3 :
    print("Largest Number is "+ str(No3))
elif No2<No3<No1 :
    print("Largest Number is "+ str(No1))
elif No2>No3>No1 :
    print("Largest Number is " + str(No2))
elif No3<No1<No2 :
    print("Largest Number is " + str(No2))
else:
    print("Largest Number is "+ str(No3))