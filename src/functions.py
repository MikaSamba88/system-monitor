import psutil, os, logging, time, threading, json, prettytable
from simple_term_menu import TerminalMenu




#def list_alarms()


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


def exit_program():
    clear_consol()
    print("You choose to exit!\n")
    print(input("Tryck Enter för att avsluta..."))