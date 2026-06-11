#E-COMMERCE PLATFORM
print("======================================")
print("WELCOME TO THE E-COMMERCE PLATFORM")
print("======================================")
#authentication
users = [
    ("admin", "admin12", "admin"),
    ("customer1", "cust123", "customer"),
    ("cashier1", "cash123", "cashier")
]
logged_in = False
user_role = ""

print("\n--- Please Login ---")
while not logged_in:
    username_input = input("Enter username: ").strip()
    password_input = input("Enter password: ").strip()
    for username, password, role in users:
        if username_input == username and password_input == password:
            logged_in = True
            user_role = role
            print(f"Login successful! Welcome, {username_input} ({user_role})")
            break
    if not logged_in:
            print("Invalid credentials. Please try again.")
            print("-"*40)

# role-based access control
if user_role == "admin":
    print("[Access Granted] Full admin rights enabled. Loading system configuration...")
elif user_role == "customer":
    print("[Access Granted] Shopping cart checkout loaded. Enjoy your items!")
elif user_role == "cashier":
    print("[Access Granted] Terminal checkout loaded. restricted backend access enabled.")

# control structure
while True:
    try:
        subtotal = float(input("\nEnter the subtotal amount ($): "))
        if subtotal < 0:
            print("Subtotal must be a positive number. Please try again.")
            continue
        break
    except ValueError:
        print("Invalid input. Please enter a valid number.")

coupon_code = input("Enter coupon code (or press Enter to skip): ").strip()
discount_rate = 0.0

if coupon_code != "":
    if coupon_code == "SAVE10":
        print("-> Coupon applied: 10% off")
        discount_rate = 0.10
    elif coupon_code == "SAVE20":
        print("-> Coupon applied: 20% off")
        discount_rate = 0.20
    else:
        print("-> Invalid coupon code. No discount applied.")

if discount_rate == 0.0:
    if subtotal >= 200:
        print("-> Automatic High-Spender tier discount applied: 15% off")
        discount_rate = 0.15
    elif subtotal >= 100:
        print("-> Automatic Mid-Spender tier discount applied: 5% off")
        discount_rate = 0.05
    else:
        print("-> No automatic discount applied.")

# location-based tax rates
print("\n--- Select Location for Tax Calculation ---")
print("1. Kampala (Standard - 5%)")
print("2. Entebbe (Luxury/City - 12%)")
print("3. Jinja (Exempt - 0%)")

while True:
    tax_choice = input("Enter location choice (1-3): ").strip()
    if tax_choice == "1":
        tax_rate = 0.05
        break
    elif tax_choice == "2":
        tax_rate = 0.12
        break
    elif tax_choice == "3":
        tax_rate = 0.0
        break
    else:
        print("Invalid choice. Please select a valid location (1-3).")

# final price calculation
discount_amount = subtotal * discount_rate
discounted_price = subtotal - discount_amount
tax_amount = discounted_price * tax_rate
total_price = discounted_price + tax_amount

# receipt generation
print("\n" + "=" * 40)
print("           FINAL RECEIPT     ")
print("=" * 40)
print(f"logged-in user role: {user_role}")
print(f"Subtotal: ${subtotal:.2f}")
print(f"Discount Applied: -${discount_amount:.2f} ({discount_rate*100:.0f}%)")
print(f"Tax Amount:        +${tax_amount:.2f} ({tax_rate*100:.0f}%)")
print("-" * 40)
print(f"Total Price:       ${total_price:.2f}")
print("=" * 40)
print("Thank you for shopping with us!")