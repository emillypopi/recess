# BILL SPLIT CALCULATOR
print ("==RECEIPT==")
print ("--------------------------")
#TOTAL BILL
while True:
    try:
        total_bill = float(input("Enter the total bill amount: "))
        if total_bill < 0:
            print("Total bill cannot be negative. Please enter a valid amount.")
            continue
        break
    except ValueError:
        print("Invalid input. Please enter a valid numberfor the total bill.")
#NUMBER OF PEOPLE
while True:
    try:
        num_people = int(input("Enter the number of people splitting the bill: "))
        if num_people <= 0:
            print("Number of people must be a positive integer. Please enter a valid number.")
            continue
        break
    except ValueError:
        print("Invalid input. Please enter a whole number")
#tip percentage
while True:
    tip_choice = input("Choose a tip percentage (10, 15, 20 or custom): ").strip().lower()
    if tip_choice == "10":
        tip_percentage = 10.0
        break
    elif tip_choice == "15":
        tip_percentage = 15.0
        break
    elif tip_choice == "20":
        tip_percentage = 20.0
        break
    elif tip_choice == "custom":
        while True:
            try:
                tip_percentage = float(input("Enter the custom tip percentage: "))
                if tip_percentage < 0:
                    print("Tip percentage cannot be negative. Please enter a valid amount.")
                    continue
                break
            except ValueError:
                print("Invalid input. Please enter a valid number for the tip percentage.")
        break
    else:
        print("Invalid choice. Please enter 10, 15, 20, or custom.")
#CALCULATIONS
tip_amount = total_bill * (tip_percentage / 100)
final_bill = total_bill + tip_amount
amount_per_person = final_bill / num_people

print ("\n" +"="*30)
print ("    RECEIPT   ")
print ("="*30)
print(f"Total Bill: ${total_bill:.2f}")
print(f"Tip ({tip_percentage}%): ${tip_amount:.2f}")
print(f"Final Bill: ${final_bill:.2f}")
print(f"Amount per Person: ${amount_per_person:.2f}")
print ("="*30)