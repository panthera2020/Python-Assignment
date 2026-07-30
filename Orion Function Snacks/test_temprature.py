from temperature import temp 

print('Determine if the room is too hot or cold')

print()

user_temprature_input = float(input('Enter temprature of room: '))

user_celcius_or_farenheit_input = input('Enter C for celcius or F for Farenheit: ')

system_advice = (temp(user_temprature_input, user_celcius_or_farenheit_input))

print()

print(system_advice)