import psutil, os, logging, time, threading, json, prettytable
from simple_term_menu import TerminalMenu
from functions import print_menu, exit_program

try:
    from simple_term_menu import TerminalMenu
    USE_TERMINAL_MENU = True
except ImportError:
    USE_TERMINAL_MENU = False

def print_menu():
    print("-" * 24)
    print("---- Systemoverview ----")
    print("-" * 24)
    print("\n1. System overview")
    print("2. Start Surveillance")
    print("3. Check Alarms")
    print("4. Remove Alarms ")
    print("5. Check Alarms")
    print("6. ")


#def list_alarms()
options = ["System Overview", "Start Surveillance", "Check Alarms", "Remove Alarms", "Exit"]

def main_menu():
    alarms = []
    while True:
        if use_terminal_menu:
            from simple_term_menu import TerminalMenu
            terminal_menu = TerminalMenu(options)
            choice_index = terminal_menu.show()
        else:
            print_menu(options)
            choice = input("Choose a number: ")
            if choice.isdigit():
                choice_index = int(choice) - 1
            else:
                print("Invalid input!")
                continue
        match choice:
            case "0":
                pass
            case "1":
                pass
            case "2":
                pass
            case "3":
                pass
            case "4":
                pass
        exit_program()
        sys.exit()
        choice = input("\nVälj ett alternativ i Menyn (1-6)")

        if choice == "1":
            print("Start Overview! skall lägga in funktion")


        break
if __name__ == "__main__":
    main_menu()