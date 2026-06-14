print("Welcome to the World cup 2026 Winner Simulator!")

while True:
    print("\n---Main Menu---")
    print("1. Enter Country")
    print("2. Check upcoming matches")
    print("3. Exit")

    choice = input("Enter your choice (1-3): ").strip()
    #exiting prgramm
    if choice == "3":
        print("Thank you for using the World Cup 2026 Winner Simulator. Goodbye!")
        break
    elif choice == "2":
        print("\nUpcoming Matches:")
        print("1. Team A vs Team B - Date: 2026-11-21")
        print("2. Team C vs Team D - Date: 2026-11-22")
        print("3. Team E vs Team F - Date: 2026-11-23")
    elif choice == "1":
        country = input("Enter the name of the country you think will win: ").strip()
        print(f"You have selected {country} as the winner of the World Cup 2026!")

        if country_input.lower() in contenders:
            winner = random.choice([country_input, "another contender"])

            if winner == country_input:
                print(f"Congratulations! {country_input} has won the World Cup 2026!")
                print("ending simulator...")
                break
            else:
                print(f"Unfortunately, {country_input} did not win. The winner is {winner}.")
                print("Try again for the next World Cup!")
        else:
            print(f"{country_input} is not a recognized contender for the World Cup 2026. Please try again.")
    else:
        print("Invalid choice. Please select a valid option (1-3).")
        