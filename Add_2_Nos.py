# Beginners -Add Two Numbers
n = int(raw_input())
lst = []
for i in range(0,n):
    x, y = raw_input().split()
    x, y = int(x), int(y)
    lst.append(x+y)

for x in lst:
    print x
