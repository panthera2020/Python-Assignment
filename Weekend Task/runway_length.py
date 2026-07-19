""" Determine the runaway length """

# Collect airplance accleration a, and speed v
# Calculate runway length
# Display minimum runway lenght

print('Find runawy length')

a = float(input('Enter acceleration: '))

v = float(input('Enter speed: '))

print()

length = (v **2) / (2 * a)

print('The minimum runaway legth for this airplane is ', length)