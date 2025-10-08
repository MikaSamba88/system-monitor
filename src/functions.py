import psutil, os, logging, time, threading, json, prettytable
from simple_term_menu import TerminalMenu
from storage import save, load
from prettytable import PrettyTable

alarms = load()

def add_alarm():
    pass

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



def list_alarms():
    pass




def add_alarms():
    pass



def print_menu():
    print("=" * 24)
    print("==== Systemoverview ====")
    print("=" * 24)
    print("\n1. System overview")
    print("2. Start Surveillance")
    print("3. Check Alarms")
    print("4. Remove Alarms ")
    print("5. Check Alarms")
    print("6. ")


def exit_program():
    clear_consol()
    print("You choose to exit!\n")
    print(input("Tryck Enter för att avsluta..."))