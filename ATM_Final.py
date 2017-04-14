#ATM 
val, bal = raw_input().split()
val, bal = int(val),float(bal)
if (0 < val <= 2000)and (0 < bal <= 20000):
    if (val % 5 == 0) and (bal > (val + 0.5)):
        print (" %.2f " % (bal-val-0.5))
    else:
        print (" %.2f " % bal)
