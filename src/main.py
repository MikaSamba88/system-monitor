import os, logging, time

import psutil
from prettytable import PrettyTable


from functions import print_menu, exit_program, display_system_status, clear_consol
from storage import save, load
from alarms import Alarm, AlarmManager
from monitoring import Monitor

manager = AlarmManager()

try:
    from simple_term_menu import TerminalMenu
    USE_TERMINAL_MENU = True
except ImportError:
    USE_TERMINAL_MENU = False

options = ["Start Monitoring", "List Active Monitoring", "Create Alarms", "Show Alarms", "Start monitoring Mode", "Remove Alarms", "Exit"]


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
                print("Start Monitoring selected: ")
                Monitor.start_monitoring()
            case 1:
                print("List Active Monitoring selected: ")
                Monitor.list_active_monitoring()
            case 2:
                print("Create Alarms selected: ")
                try:
                    alarm_type = input("Enter alarm type (cpu/memory/disk): ").lower()
                    level = int(input("Enter alarm level (1-100): "))
                    manager.add_alarms(alarm_type, level)
                except ValueError:
                    print("You must enter a number between 1 and 100.")
                    input("Press Enter to continue...")
            case 3:
                print("Show Alarms selected")
                print("\nConfigured Alarms:")
                manager.list_alarms()
                input("Press Enter to continue to main manu...")
            case 4:
                print("Start Monitoring Mode selected")
                Monitor.monitoring_mode()
            case 5:
                print("Remove Alarms selected")
                manager.remove_alarm()
                input("Press Enter to return to main manu...")
            case 6:
                exit_program()
                break

if __name__ == "__main__":
    main_menu()
