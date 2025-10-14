import psutil, os, time
from prettytable import PrettyTable
from functions import display_system_status

class Monitor:
    monitoring_active = False

    @classmethod
    def start_monitoring(cls):
        cls.monitoring_active = True
        print("Monitoring started")
        input("Press Enter to return to the main manu...")
    
    @classmethod
    def list_active_monitoring(cls):
        os.system("cls" if os.name == "nt" else "clear")
        print("=" * 24)
        print("==== Systemoverview ====")
        print("=" * 24)
        print("=== Active Monitoring ===\n")

        if not cls.monitoring_active:
            print("No monitoring is active.")
        else:
            cpu = psutil.cpu_percent(interval=1)
            print(f"CPU Usage: {cpu}%")

            memory = psutil.virtual_memory()
            used_gb = memory.used / (1024 ** 3)
            total_gb = memory.total / (1024 ** 3)
            print(f"Memory Usage: {memory.percent}% ({used_gb:.1f} GB out of {total_gb:.1f} GB used)")

            disk = psutil.disk_usage('/')
            used_disk = disk.used / (1024 ** 3)
            total_disk = disk.total / (1024 ** 3)
            print(f"Disk Usage:{disk.percent}% ({used_disk:.0f} GB out of {total_disk:.0f} GB used)")

        input("\nPress Enter to continue...")

    @classmethod
    def monitoring_mode(cls):
        if not cls.monitoring_active:
            print("Cannot start monitoring mode. No monitoring Active.")
            input("\nPress Enter to return to main...")
            return

        print("Monitoring mode started. Press control + C to stop and return to main menu.\n")
        try:
            while True:
                cpu = psutil.cpu_percent(interval=2)
                memory = psutil.virtual_memory().percent
                disk = psutil.disk_usage('/').percent
                print(f"CPU: {cpu}% | Memory: {memory}% | Disk: {disk}%")
                time.sleep(2)
        except KeyboardInterrupt:
            print("\nMonitoring mode stopped. Returing to main menu...")
            time.sleep(1)
