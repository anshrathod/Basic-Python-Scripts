from executionTime import ExecutionTime
import random

print("Test Program Started")
	
timer = ExecutionTime()

# Sample operation 1 to measure time for
one_list = list()
two_list = list()
three_list = list()
demo_list = [random.randint(1, 7685) for num in
           range(1, 1000000) if num % 2 == 0]

print('Execution Time For Operation 1 :{} seconds.'.format(timer.duration()))

timer2 = ExecutionTime()

# Sample operation 2 to measure time for
one_list = list()
two_list = list()
three_list = list()
four_list = list()
five_list = list()
six_list = list()
seven_list = list()
eight_list = list()
demo_list = [random.randint(1, 9999997766) for num in
           range(1, 1000000) if num % 2 == 0]
		   
print('Execution Time For Operation 2 :{} seconds.'.format(timer2.duration()))