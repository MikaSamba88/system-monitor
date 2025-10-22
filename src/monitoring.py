import psutil, os, time, threading
from prettytable import PrettyTable
from functions import *
from alarms import *


class Monitor:
    monitoring_active = False

    @classmethod
    def start_monitoring(cls):
        cls.monitoring_active = True
        print("Monitoring started")
        input("\nPress Enter to return to the main manu...")
    
    @classmethod
    def list_active_monitoring(cls):
        os.system("cls" if os.name == "nt" else "clear")
        print("=" * 24)
        print("==== Systemoverview ====")
        print("=" * 24)
        print("\n=== Active Monitoring ===\n")

        if not cls.monitoring_active:
            print("No monitoring is active.")
            input("\nPress Enter to continue...")
        else:
            display_system_status()

    @classmethod
    def monitoring_mode(cls, manager):
        if not cls.monitoring_active:
            print("Cannot start monitoring mode. No monitoring Active.")
            input("\nPress Enter to return to main...")
            return

        print("Press control + C to stop and return to main menu.\n")
        try:
            while True:
                cpu = psutil.cpu_percent(interval=2)
                memory = psutil.virtual_memory().percent
                disk = psutil.disk_usage('/').percent
                print(f"CPU: {cpu}% | Memory: {memory}% | Disk: {disk}%")
                time.sleep(1)

                for level in manager.alarms['cpu']:
                    if cpu >= level:
                        alarm_sound()
                        print(f"🚨 Warning! CPU is using {cpu}%, Alarm set at {level} 🚨")

                for level in manager.alarms['memory']:
                    if memory >= level:
                        alarm_sound()
                        print(f"🚨 Warning! Memory is using {memory}%, Alarm set at {level} 🚨")

                for level in manager.alarms['disk']:
                    if disk >= level:
                        alarm_sound()
                        print(f"🚨 Warning! Disk is using {disk}%, Alarm set at {level} 🚨")
                time.sleep(1)
                clear_consol()

        except KeyboardInterrupt:
            print("\nMonitoring mode stopped. Returing to main menu...")
            time.sleep(1)
