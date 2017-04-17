x, y = (raw_input().split())
x, y = int(x), int(y)
diff = x - y
if diff % 10 == 9:
    diff = diff - 1

else:
    diff = diff + 1
print diff