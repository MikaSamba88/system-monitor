import os, logging, time, sys

import psutil
from prettytable import PrettyTable


from functions import *
from storage import *
from alarms import *
from monitoring import *

class SystemOverviewApp:
    def __init__(self):
        self.manager = AlarmManager()

        try:
            from simple_term_menu import TerminalMenu
            self.USE_TERMINAL_MENU = True
        except ImportError:
            self.USE_TERMINAL_MENU = False

        self.options = ["1. Start Monitoring", 
                   "2. List Active Monitoring",
                   "3. Create Alarms",
                   "4. Show Alarms", 
                   "5. Start monitoring Mode",
                   "6. Remove Alarms",
                   "7. Logg",
                   "8. Exit"]
        
        self.alarm_menu = ["1. CPU Alarm",
                           "2. Memory Alarm",
                           "3. Disk Alarm",
                           "4. Back to Main Menu"]
    def handle_alarm_creation():
        while True:
            try:
                level = int(input("Set % Alarm (1-100): "))
                return level
            except ValueError:
                print("❌ Wrong input! Must be an integer between 1- 100. ❌")
                input("Press Enter to Continue...")
                clear_consol()
    def create_alarms_menu():
        alarm_type_map = {
            0: "cpu",
            1: "memory",
            2: "disk"
        }
        

    def run_menu(self):
        while True:
            clear_consol()
            print("=" * 24)
            print("==== Systemoverview ====")
            print("=" * 24)
            print("Choose an alternative:\n")
            
            if self.USE_TERMINAL_MENU:
                terminal_menu = TerminalMenu(self.options)
                choice_index = terminal_menu.show()
            else:
                print_menu()
                choice = input("Välj ett nummer: ")
                if choice.isdigit() and 1 <= int(choice) <= len(self.options):
                    choice_index = int(choice) - 1
                else:
                    print("Felaktig inmatning!")
                    continue

            print(f"\nYou chose: {self.options[choice_index]}\n")               
            match choice_index:
                case 0:
                    print("Start Monitoring selected: ")
                    Monitor.start_monitoring()
                case 1:
                    print("List Active Monitoring selected: ")
                    Monitor.list_active_monitoring()
                case 2:
                    print("Create Alarms selected: ")
                    self.create_alarms_menu()
                case 3:
                    print("Show Alarms selected")
                    print("\nConfigured Alarms:")
                    self.manager.list_alarms()
                    input("Press Enter to continue to main manu...")
                case 4:
                    print("Start Monitoring Mode selected")
                    Monitor.monitoring_mode()
                case 5:
                    print("Remove Alarms selected")
                    self.manager.remove_alarm()
                    input("Press Enter to return to main manu...")
                case 6:
                    pass
                case 7:
                    exit_program()
                    break

if __name__ == "__main__":
    app = SystemOverviewApp()
    app.run_menu()
