from storage import save, load
from functions import *


class Alarm:
    def __init__(self, alarm_type, level):
        self.type = alarm_type
        self.level = level
    
    def __repr__(self):
        return f"{self.type.capitalize()} larm {self.level}%"
    
class AlarmManager:
    def __init__(self):
        alarms = load()
        self.alarms = alarms if alarms else {"cpu": [], "memory": [], "disk": []}

    def add_alarms(self, alarm_type, level):
        if alarm_type not in self.alarms:
            print("❌Wrong Alarm type")
            return
        if not isinstance(level, int) or not (0 < level <= 100):
            print("❌Alarm has to be set between 1 and 100.")
            return
        self.alarms[alarm_type].append(level)
        self.alarms[alarm_type].sort()
        save(self.alarms)
        print(f"✅{alarm_type.capitalize()} Alarm added: {level}%")

    def list_alarms(self):
        index = 1
        for alarm_type, levels in self.alarms.items():
            for level in levels:
                print(f"{index}. {Alarm(alarm_type, level)}")
                index += 1
        if index == 1:
            print("No Alarms is set!")
    
    def remove_alarm(self):
        while True:
            clear_consol()
            heading_print()
            print("\nActive Alarms:")
            index_map = {}
            index = 1

            for alarm_type, levels in self.alarms.items():
                for level in levels:
                    print(f"{index}. {alarm_type.capitalize()} Alarm on: {level}%")
                    index_map[index] = (alarm_type, level)
                    index += 1

            if not index_map:
                print("No Alarms to remove!\n")
                return
            
            try:
                choice = int(input("\nChoose a Alarm to remove:"))
                if choice not in index_map:
                    print("UnValid choice!")
                    return
                
                alarm_type, level = index_map[choice]
                self.alarms[alarm_type].remove(level)
                save(self.alarms)
                print(f"❌Removed {alarm_type.capitalize()} larm {level}%")
                input("\nPress Enter to continue...")
            except ValueError:
                print("It must be a number.")
        