import psutil, os, logging, time, threading, json, prettytable
from simple_term_menu import TerminalMenu


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

def exit_program():
    clear_consol()
    print("You choose to exit!\n")
    print(input("Tryck Enter för att avsluta..."))

def main_menu():
    options = ["entry 1", "entry 2", "entry 3"]
    terminal_menu = TerminalMenu(options)
    menu_entry_index = terminal_menu.show()
    print(f"You have selected {options[menu_entry_index]}!")
    alarms = []
    while True:
        print_menu()
        choice = input("Choose a number(1-5): ")
        match choice:
            case "1":
                pass
            case "2":
                pass
            case "3":
                pass
            case "4":
                pass
            case "5":
                pass
        exit_program()
        sys.exit()
        choice = input("\nVälj ett alternativ i Menyn (1-6)")

        if choice == "1":
            print("Start Overview! skall lägga in funktion")


        break
if __name__ == "__main__":
    main_menu()