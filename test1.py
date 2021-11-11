import time

start=time.time()
amount_of_cubic=0

for number in range(100,1000):
    a=number//100
    b=(number-a*100)//10
    c=number-a*100-b*10

    if(a**3+b**3+c**3) == number:
        print(number)
        amount_of_cubic+=1

print("there is exactly {} cubic armstrong numbers ".format(amount_of_cubic))

end=time.time()
print("time spent:", end-start)