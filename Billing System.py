# first week python project
# Rastuarent Billing system
input("Name of the customer: ")
bill_amount = float(input("Enter the Bill amount: "))
tip = bill_amount * 0.10
print("the 10% tip from your bill is" , tip)
GTS = bill_amount * 0.20
print("the 20% Gts from your bill is" , GTS)
total_bill = bill_amount + tip + GTS 
print("your total amount is: ", total_bill )
customer_amount = float(input("customer Give RS:"))
remaining_amount= customer_amount - total_bill
print("Remaining amount is RS:" , remaining_amount)