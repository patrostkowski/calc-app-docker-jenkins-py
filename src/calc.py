#!/usr/bin/env python3

import sys
import numpy as np
# Program make a simple calculator

dd = 0

# This function adds two numbers
def add(x, y):
	return x + y

# This function subtracts two numbers
def subtract(x, y):
	return x - y

# This function multiplies two numbers
def multiply(x, y):
	return x * y

# This function divides two numbers
def divide(x, y):
	return x / y

def power(x, y):
	return np.power(x, y)


print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")
print("5.Power")
print("q.Exit")

def main():
	while True:
		# Take input from the user
		choice = input("Enter choice(1/2/3/4/5): ")
		# Check if choice is one of the four options
		if choice in ('1', '2', '3', '4', '5'):
			num1 = float(input("Enter first number: "))
			num2 = float(input("Enter second number: "))
			if choice == '1':
				print(num1, "+", num2, "=", add(num1, num2))
			elif choice == '2':
				print(num1, "-", num2, "=", subtract(num1, num2))
			elif choice == '3':
				print(num1, "*", num2, "=", multiply(num1, num2))
			elif choice == '4':
				print(num1, "/", num2, "=", divide(num1, num2))
			elif choice == '5':
				print(num1, "^(", num2, ") =", power(num1, num2))
			break
		elif choice == 'q':
			sys.exit(0)
			break
		else:
			print("Invalid Input")
			sys.exit(1)

if __name__ == "__main__":
	main()
	sys.exit(0)
