import sys
from clear_screen import *
from conversion_formulas import *
from typing import Callable


def main_menu():
    clear_screen()
    print("\n* * * * * * * * * * WELCOME TO THE UNIT CONVERSION TOOL * * * * * * * * * *\n")
    print("\n1) Inches to Millimeters")
    print("\n2) Fahrenheit to Celcius")
    print("\n3) Pounds to Kilograms")
    print("\n4) mph to km/h")
    print("\n5) knots to mph")
    print("\n6) quit program\n")

    while True:
        try:
            user_input = int(input("\nInput the menu number for the conversion you'd like to do: "))
            if user_input >= 1 and user_input <= 6:
                break
            else:
                print("\nInvalid input. Please try again.")
        except ValueError:
            print("\nInvalid input. Please try again.")
    menu_input_check(user_input)


def menu_input_check(user_input: int):
    match user_input:
        case 1:
            conversion_validation(1, "inches", "millimeters", inches_to_mm_conversion)
        case 2:
            conversion_validation(2, "Fahrenheit", "Celsius", fahr_to_cels_conversion)
        case 3:
            conversion_validation(3, "pounds", "kilograms", pound_to_kilo_converson)
        case 4:
            conversion_validation(4, "miles per hour", "kilometers per hour", mph_to_kmh_conversion)
        case 5:
            conversion_validation(5, "knots", "miles per hour", knots_mph_conversion)
        case _:
            sys.exit()


def conversion_validation(menu_selection: int, convert_from: str, convert_to: str, conversion_function: Callable[[float], float]):
    while True:
        try:
            user_input = float(input(f"\nEnter a number in {convert_from}: "))
            result = conversion_function(user_input)
            print(f"\n{user_input} {convert_from} is equal to {result} {convert_to}\n")
            while True:
                print("\nY = yes, N = no, M = return to main menu")
                continue_input = input("\nDo another conversion? (Y/N/M) ")
                match continue_input:
                    case "Y" | "y":
                        menu_input_check(menu_selection)
                    case "M" | "m":
                        main_menu()
                    case _:
                        sys.exit()
        except ValueError:
            print("\nInvalid input. Please try again.")