def get_int(message):
	while True:
		try:
			value = int(input(message))
			if value > 0:
				return value
			else:
				print("Please enter a positive integer.")
		except ValueError:
			print("Please enter a valid integer.")
