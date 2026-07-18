""" 7% Investment return """

# calculate the amount on deposit for each year 
# add this to the initial deposit for each years
# Display how much you'll have for each year

principal = 1000

amount_on_deposit_in_ten_years = principal * ((1 + 0.07) **10)

amount_on_deposit_in_twenty_years = principal * ((1 + 0.07) **20)

amount_on_deposit_in_thirty_years = principal * ((1 + 0.07) **30)

print('Amount in 10years: ', 1000 + amount_on_deposit_in_ten_years)

print('Amount in 20years: ', 1000 + amount_on_deposit_in_twenty_years)

print('Amount in 30years: ', 1000 + amount_on_deposit_in_thirty_years)