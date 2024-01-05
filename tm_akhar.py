import os
import random

list1 = [random.randint(1, 100) for _ in range(5)]
list2 = [random.randint(1, 100) for _ in range(5)]
list3 = [random.randint(1, 100) for _ in range(5)]

sum_list1 = sum(list1)
sum_list2 = sum(list2)
sum_list3 = sum(list3)

file_path = "sum_lists.txt"

with open(file_path, "w") as file:
    file.write(f"Sum of List 1: {sum_list1}\n")
    file.write(f"Sum of List 2: {sum_list2}\n")
    file.write(f"Sum of List 3: {sum_list3}\n")

print(f"The sums have been saved in {file_path}")