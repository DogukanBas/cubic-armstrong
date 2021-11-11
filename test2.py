import time

start=time.time()
amount_of_cubic=0

for a in range(1,10):
    for b in range(10):
        for c in range(10):
            number=a**3+b**3+c**3
            x=number//100
            if x>9:  #if it is already over 3 digits we dont need c to increase more
                break
            y = (number - 100 * x) // 10
            z = number - x * 100 - y * 10
            if (x==a) and (y==b) and(z==c):
                amount_of_cubic+=1
                print(number)

end=time.time()

print("there is exactly {} cubic armstrong numbers ".format(amount_of_cubic))
print("time spent:",end-start)