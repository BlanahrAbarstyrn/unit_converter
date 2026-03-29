import os

def clear_screen():
    # Check for installed operating system name
    if os.name == 'nt': # windows
        _ = os.system('cls')
    else: # linux / macOS
        _ = os.system('clear')