
initial_balance = float(input("Enter initial balance: ₹"))
deposit_amount = float(input("Enter deposit amount: ₹"))

new_balance = initial_balance + deposit_amount

print(f"New Balance after deposit: ₹{new_balance}")



initial_balance = float(input("Enter initial balance: ₹"))
deposit_amount = float(input("Enter deposit amount: ₹"))

new_balance = initial_balance + deposit_amount
print(f"New Balance after deposit: ₹{new_balance}")

withdraw_amount = float(input("Enter withdrawal amount: ₹"))

final_balance = new_balance - withdraw_amount
print(f"Final Balance: ₹{final_balance}")