import time
start = time.time()

primelist = [2,3,5,7,11,13,17,19]
LCM = 1

for x in primelist:
    y = 1
    while 20 > y*x:
        y = y*x
        LCM = LCM *x

end = time.time()
print(end - start)
print(LCM)
