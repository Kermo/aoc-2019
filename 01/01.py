import math

with open("input.txt") as f:
	data = f.read().splitlines()
	
def count_fuel_amount(data):
	sum = 0
	
	for line in data:
		sum = sum + math.floor(int(line) / 3) - 2
	
	return sum

def count_new_fuel_amount(data):
	sum = 0
	
	for line in data:
		fuel_amount = math.floor(int(line) / 3) - 2
		sum = sum + fuel_amount
		while fuel_amount > 0:
			fuel_amount = math.floor(fuel_amount / 3) - 2
			if fuel_amount > 0:
				sum = sum + fuel_amount
	
	return sum

print("Part 1: " + str(count_fuel_amount(data)))
print("Part 2: " + str(count_new_fuel_amount(data)))
