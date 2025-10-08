from storage import save, load
alarm = load()

class Alarm():
    def __init__(self, typ, level):
        self.typ = typ
        self.level = level
    
    def __repr__(self):
        return f"{self.typ} larm {self.level}%"
    
    