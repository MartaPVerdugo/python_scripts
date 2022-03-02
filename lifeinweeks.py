from typing import List
# Calculate how many days, weeks and months you have left until 90 years old
age = input("What is your current age?")


def count_life(my_age: int) -> int:
    years_left_to_90 = 90 - my_age
    year = int("365")
    weeks = int("52")
    months = int("12")
    my_days_remaining = (year * years_left_to_90)
    my_weeks_remaining = (weeks * years_left_to_90)
    my_months_remaining = (months * years_left_to_90)
    return my_days_remaining


def main():
    my_age = int(age)
    my_days_remaining = count_life(my_age)
    my_weeks_remaining = count_life(my_age)
    my_months_remaining = count_life(my_age)
    print(f"You have {my_days_remaining} days, {my_weeks_remaining} weeks and {my_months_remaining} months left.")


if __name__ == '__main__':
    main()