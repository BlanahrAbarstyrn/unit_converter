from clear_screen import clear_screen
from conversion_formulas import pound_to_kilo_converson, inches_to_mm_conversion, fahr_to_cels_conversion


def main_menu():
    clear_screen()
    print("\n* * * * * * * * * * WELCOME TO THE UNIT CONVERSION TOOL * * * * * * * * * *\n")
    print("\n1) Inches to Millimeters")
    print("\n2) Fahrenheit to Celcius")
    print("\n3) Pounds to Kilograms\n")

    while True:
        try:
            user_input = int(input("\nInput the menu number for the conversion you'd like to do: "))
            if user_input >= 1 and user_input <= 3:
                break
            else:
                print("\nInvalid input. Please try again.")
        except ValueError:
            print("\nInvalid input. Please try again.")
    menu_input_check(user_input)


def inch_to_mm_menu():
    while True:
        try:
            user_input = float(input("\nEnter a number in inches: "))
            result = inches_to_mm_conversion(user_input)
            print(f"\n{user_input} inches is equal to {result} millimeters\n")
            break
        except ValueError:
            print("\nInvalid input. Please try again.")


def fahr_to_celc_menu():
    while True:
        try:
            user_input = float(input("\nEnter a number in Fahrenheit: "))
            result = fahr_to_cels_conversion(user_input)
            print(f"\n{user_input} Fahrenheit is equal to {result} Celsius\n")
            break
        except ValueError:
            print("\nInvalid input. Please try again.")


def pound_to_kilo_menu():
    while True:
        try:
            user_input = float(input("\nEnter a number in pounds: "))
            result = pound_to_kilo_converson(user_input)
            print(f"\n{user_input} pounds is equal to {result} kilograms\n")
            break
        except ValueError:
            print("\nInvalid input. Please try again.")


def menu_input_check(user_input):
    if user_input == 1:
        inch_to_mm_menu()
    elif user_input == 2:
        fahr_to_celc_menu()
    else:
        pound_to_kilo_menu()