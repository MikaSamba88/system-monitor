import psutil, os, logging, time, threading, json, prettytable
from simple_term_menu import TerminalMenu
from functions import print_menu, exit_program, display_system_status, clear_consol
from storage import save, load
from alarms import alarm
from prettytable import PrettyTable


try:
    from simple_term_menu import TerminalMenu
    USE_TERMINAL_MENU = True
except ImportError:
    USE_TERMINAL_MENU = False

options = ["System Overview", "Start Surveillance", "Add Alarms", "Check Alarms", "Remove Alarms", "Exit"]


def main_menu():
    while True:
        clear_consol()
        print("=" * 24)
        print("==== Systemoverview ====")
        print("=" * 24)
        print("Choose an alternative:\n")
        
        if USE_TERMINAL_MENU:
            terminal_menu = TerminalMenu(options)
            choice_index = terminal_menu.show()
        else:
            print_menu()
            choice = input("Välj ett nummer: ")
            if choice.isdigit() and 1 <= int(choice) <= len(options):
                choice_index = int(choice) - 1
            else:
                print("Felaktig inmatning!")
                continue

        print(f"\nYou chose: {options[choice_index]}\n")               
        match choice_index:
            case 0:
                display_system_status()
            case 1:
                print("Start Surveillance selected")
            case 2:
                print("Add Alarm")
                alarm()
            case 3:
                print("Check Alarms selected: ")
            case 4:
                print("Remove Alarms selected")
            case 5:
                exit_program()
                break

if __name__ == "__main__":
    main_menu()
