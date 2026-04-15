# PROG 1.2 Adding 2 Numbers Measuring Time
import time
start=time.time()
first_num= 100
second_num = 100
total_num = first_num + second_num
end=time.time()
time_taken = (start - end) * 1000000
print(f"The Result of adding {first_num} and {second_num} is {total_num}")
print(f"--- {time_taken} micro seconds ---")