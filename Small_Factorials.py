# Beginner - small factorials
n = raw_input()
n = int(n)
lst = []
lst2 = []
fact = 1
for i in range(0, n):
    x = (int(raw_input()))
    lst.append(x)
    for k in range(1,x+1):
        fact = fact * k
    lst2.append(fact)
    fact = 1

for elem in lst2:
    print elem
