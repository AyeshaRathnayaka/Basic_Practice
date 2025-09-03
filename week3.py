#find the largest among three numbers
No1=input("First Number : ")
No2=input("Second Number : ")
No3=input("Third Number: 1")

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














