""" Determine the time of the day in seconds """

print('Enter the time of the day')

hours = int(input('Hours: '))

print()

minute = int(input('Minutes: '))

print()

seconds = int(input('Seconds: '))

def seconds_since_midnight(hours, minutes, seconds):
	hour_in_seconds = hours * 3600
	minutes_in_seconds = minutes * 60
	return hour_in_seconds + minutes_in_seconds + seconds

print(seconds_since_midnight(hours, minute, seconds))