import time

start = time.time()

def bubbleSort(arr):

    n = len(arr)

    for i in range(n):

        for j in range(0, n-i-1):

            if arr[j] > arr[j+1] :

                arr[j], arr[j+1] = arr[j+1], arr[j]

arr = [23 , -11 , 18 , 8 , -38, 9.9, 9.91, -38.7, 999.852447, 1000, 78.1, 25487, -120478]

bubbleSort(arr)
print ("Sorted array is:")

print(arr)

print("Run Time: " + str( time.time() - start ))