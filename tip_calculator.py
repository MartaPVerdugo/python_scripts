# If the bill was $150.00, split between 5 people, with 12% tip.

# Each person should pay (150.00 / 5) * 1.12 = 33.6
# Format the result to 2 decimal places = 33.60

# Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

# Write your code below this line 👇

print("Welcome to the tip calculator.")
total_bill = float(input("What was the total bill? "))
tip_input = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
number_people = int(input("How many people to split the bill? "))


def calculate_total_person(total_bill: float) -> float:
    percentage_tip = tip_input / 100
    tip = total_bill * percentage_tip
    total_bill_with_tip = total_bill + tip
    amount_per_person = total_bill_with_tip / number_people
    amount_per_person_rounded = round(amount_per_person, 2)
    return amount_per_person_rounded


def main():
    amount_per_person_rounded = calculate_total_person(total_bill)
    print(f"Each person should pay: {amount_per_person_rounded}")


if __name__ == '__main__':
    main()
