#Beginner - Turbo Sort
n = int(raw_input())
lst = []
for i in range(0,n):
    x=int(raw_input())
    lst.append(x)
lst.sort()
for x in lst:
    print x