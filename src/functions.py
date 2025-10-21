import psutil, os, logging, time, threading, json, prettytable
from simple_term_menu import TerminalMenu
from storage import save, load
from prettytable import PrettyTable

alarms = load()


def clear_consol():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')


def display_system_status():
    cpu = psutil.cpu_percent(interval=1)
    mem = psutil.virtual_memory()
    
    if os.name == 'nt':
        path = 'C:\\'
    else:
        path = '/'

    disk = psutil.disk_usage(path)

    table = PrettyTable()
    table.field_names = ["Component", "Usage", "Details"]
    table.add_row(["CPU Usage", f"{cpu}%", "-"])
    table.add_row(["Memory Usage", f"{mem.percent}%", f"{mem.used / (1024**3):.2f} GB / {mem.total / (1024**3):.2f} GB"])
    table.add_row(["Disk Usage", f"{disk.percent}%", f"{disk.used / (1024**3):.2f} GB / {disk.total / (1024**3):.2f} GB"])

    print(table)
    
    input("\nTryck Enter för att återgå till menyn...")




def print_menu(options):
    print("=" * 24)
    print("==== Systemoverview ====")
    print("=" * 24)
    
    for i in enumerate(options):
        print(f"{i + 1}. {options}")

def get_numeric_menu_choice(options):
    for i in enumerate(options):
        print(f"{i + 1}. {options}")

    choice = input("\nChoose a number: ")
    if choice.isdigit():
        choice_num = int(choice)

        if 1 <= choice_num <= len(options):
            return choice_num - 1
        else:
            print("❌Invalid Choice! Number outside of range.")
    else:
        print("❌Invalid input! Have to be a number.")
    time.sleep(1)
    return None

# def enter_input():
#     print(input)


def exit_program():
    clear_consol()
    print("You choose to exit!\n")
    print(input("Tryck Enter för att avsluta..."))