n1=int(input("enter index= "))
n2=int(input("enter index= "))
n3=int(input("enter index= "))

if(n1<n2):
    if(n3<n2):
         print("large is",n2)  
    else:
        print("large is",n3)
elif(n1<n3):
     print("large is",n3)
else:
     print("large is",n1)
