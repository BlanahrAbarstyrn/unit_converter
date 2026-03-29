import sys
from clear_screen import *
from conversion_formulas import *

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


def inch_to_mm_menu():
    while True:
        try:
            user_input = float(input("\nEnter a number in inches: "))
            result = inches_to_mm_conversion(user_input)
            print(f"\n{user_input} inches is equal to {result} millimeters\n")
            while True:
                print("\nY = yes, N = no, M = return to main menu")
                continue_input = input("\nDo another conversion? (Y/N/M) ")
                match continue_input:
                    case "Y" | "y":
                        inch_to_mm_menu()
                    case "M" | "m":
                        main_menu()
                    case _:
                        sys.exit()
        except ValueError:
            print("\nInvalid input. Please try again.")


def fahr_to_cels_menu():
    while True:
        try:
            user_input = float(input("\nEnter a number in Fahrenheit: "))
            result = fahr_to_cels_conversion(user_input)
            print(f"\n{user_input} Fahrenheit is equal to {result} Celsius\n")
            while True:
                print("\nY = yes, N = no, M = return to main menu")
                continue_input = input("\nDo another conversion? (Y/N/M) ")
                match continue_input:
                    case "Y" | "y":
                        fahr_to_cels_menu()
                    case "M" | "m":
                        main_menu()
                    case _:
                        sys.exit()
        except ValueError:
            print("\nInvalid input. Please try again.")


def pound_to_kilo_menu():
    while True:
        try:
            user_input = float(input("\nEnter a number in pounds: "))
            result = pound_to_kilo_converson(user_input)
            print(f"\n{user_input} pounds is equal to {result} kilograms\n")
            while True:
                print("\nY = yes, N = no, M = return to main menu")
                continue_input = input("\nDo another conversion? (Y/N/M) ")
                match continue_input:
                    case "Y" | "y":
                        pound_to_kilo_menu()
                    case "M" | "m":
                        main_menu()
                    case _:
                        sys.exit()
        except ValueError:
            print("\nInvalid input. Please try again.")


def mph_to_kmh_menu():
    while True:
        try:
            user_input = float(input("\nEnter a number in miles per hour: "))
            result = mph_to_kmh_conversion(user_input)
            print(f"\n{user_input} miles per hour is equal to {result} kilometers per hour\n")
            while True:
                print("\nY = yes, N = no, M = return to main menu")
                continue_input = input("\nDo another conversion? (Y/N/M) ")
                match continue_input:
                    case "Y" | "y":
                        mph_to_kmh_menu()
                    case "M" | "m":
                        main_menu()
                    case _:
                        sys.exit()
        except ValueError:
            print("\nInvalid input. Please try again.")


def knot_to_mph_menu():
    while True:
        try:
            user_input = float(input("\nEnter a number in knots: "))
            result = knots_mph_conversion(user_input)
            print(f"\n{user_input} knots is equal to {result} miles per hour\n")
            while True:
                print("\nY = yes, N = no, M = return to main menu")
                continue_input = input("\nDo another conversion? (Y/N/M) ")
                match continue_input:
                    case "Y" | "y":
                        knot_to_mph_menu()
                    case "M" | "m":
                        main_menu()
                    case _:
                        sys.exit()
        except ValueError:
            print("\nInvalid input. Please try again.")


def menu_input_check(user_input: int):
    match user_input:
        case 1:
            inch_to_mm_menu()
        case 2:
            fahr_to_cels_menu()
        case 3:
            pound_to_kilo_menu()
        case 4:
            mph_to_kmh_menu()
        case 5:
            knot_to_mph_menu()
        case _:
            sys.exit()