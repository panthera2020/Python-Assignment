""" Determine cost of Trip """

# Collect user driving distance
# Collect fuel efficiency in miles per gallon
# Collect price per gallon
# Calculate cost of driving, driving distance divided by fuel efficiency multiplied by price per gallon
# Display cos of driving

print('Cost of driving')

user_distance = float(input('Enter driving distance: '))

fuel_efficiency = float(input('Enter fuel efficiency(m/gall): '))

price_per_gallon = float(input('Enter price per gallon: '))

print()

cost_of_driving = (user_distance / fuel_efficiency) * price_per_gallon

print('The cost of driving is ', cost_of_driving)