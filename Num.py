num = int(input("Enter a number:"))

def check_number(num):
	if num % 2 == 0:
		print(f"{num} is an even number.")
	else:
		print(f"{num} is an odd number.")
		
check_number(num)