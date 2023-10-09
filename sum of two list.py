a=int(input("enter the limit"))
b = []
c = []
sum=[]
for i in range(0,a):
    element=int(input())
    b.append(element)
print("first list is",b)
for i in range(0,a):
    element=int(input())
    c.append(element)
print("second",c)
for i in range(0,len(b)):
    sum.append(b[i]+c[i])
print("sum",sum)
