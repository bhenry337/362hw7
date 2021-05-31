def fizzbuzz():

	print(1, end='')

	for x in range(2,101):
		if (x % 3 == 0):
			print(" Fizz", end='')

			if (x % 5 == 0):
				print("Buzz", end='')
			pass

		elif (x % 5 == 0):
			print(" Buzz", end='')

		else:
			print("", x, end='')

	pass