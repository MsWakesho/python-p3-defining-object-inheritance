class Vehicle:
    def __init__(self,wheel_size,wheel_number):
        self.wheel_size= wheel_size
        self.wheel_number = wheel_number
# go and fill_up_tank,these are instance methods.
    def go(self):
        return "vrrrrrrrooom!"
    
    def fill_up_talk(self):
        return "filling up!"
