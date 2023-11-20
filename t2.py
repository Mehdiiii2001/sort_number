import time

start = time.time()

Input = [12.8, -8, 88, -8.1, 100, -45, 12.9]

n = len(Input)

for i in range(n):
    for j in range(0, n-i-1):
        if Input[j] > Input[j+1]:
            Input[j] , Input[j+1] = Input[j+1], Input[j]

print(Input)

print("Run Time: " + str( time.time() - start ))