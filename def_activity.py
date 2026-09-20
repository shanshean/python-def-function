#def keyword is used to define user-defined functions. Functions help organize codes
#into reusable blocks, making programs easier to read, maintain, and reuse. 
#Defining a function does not execute it. The function find only when it is called
#using it's name followed by parenthesis. 

def calculate_rent_balance(monthly_rent, payments):
"""calculates the rent balance of the tenant and the payment amount for each month using for-in."""
	months = ["August", "September", "October", "November", "December"]
	total_rent = monthly_rent * len(months)
	total_paid = sum(payments)
	balance = total_rent - total_paid

#Output formatted by yours truly \ > . < //
print("\n")
print("⋆˚꩜｡RENT RECORDs - August to December⋆‧°𓏲ּ𝄢")
print("\n")
print(f"Total Rent Owed: {total_rent:.2f}")
print(f"Total Rent Paid: {total_paid:.2f}")
print(f"Balance: {balance:.2f}")

return balance 

#Asking the tenant the amount of monthly rent
	monthly_rent = float(input("Enter monthly rent amount: "))

#Loop for months. Inputing monthly payment and defining the month. 
#It is to calculate each payment and summing up the total rent.
payment = []
for month in ["August", "September", "October", "November", "December"]:
	payment = float(input(f"Enter payment for {month}: "))
	payments.append(payment)

#Calling/invoking the def function with the collected rent balance
	calculate_rent_balance(monthly_rent, payments)