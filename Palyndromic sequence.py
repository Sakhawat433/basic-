#for i in range(1,10001):
    #s = str(i)
    #if s==s[::-1]:
        #print(s)

for num in range(11, 1001):
    original = num  
    rnum = 0
    while num > 0:
        r = num % 10
        num = num // 10
        rnum = rnum * 10 + r

    if original == rnum:
        print(original,end=",")
