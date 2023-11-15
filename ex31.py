N=int(input("enter nomber:"))
while N<2:
    N=int(input("enter nomber:"))
Upp=0
Up=1
print("the terms of the Fibonacci sequence are:")
print(Upp)
print(Up)
for i in range(N-1):
    U=Upp+Up
    print(U)
    Upp=Up
    Up=U