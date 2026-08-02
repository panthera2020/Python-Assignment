""" Modified Average Function """

def average(number, *args):
	return (sum(args) + number) / (len(args) + 1)

print(average())