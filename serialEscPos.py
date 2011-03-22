import serial

class serialEscPos:
    def __init__(self):
        self.serial = serial.Serial(0,19200) #bit cludgy but wth!
        self.serial.write("\x1B\x40")
        
    def println(self,text):
        self.serial.write(text)
        self.serial.write("\n")
        
    def cut(self):
        self.serial.write("\x1DV0")
    
    def useSlip(self):
        self.serial.write("\x1B\x63\x30\x04")
        
    def ff(self):
        self.serial.write("\x0c")
        
    def useRoll(self):
        self.serial.write("\x1B\x63\x30\x01")
    
    def newslip(self): #convenience function really
        self.useRoll()
        self.useSlip()
        
    def left(self):
        self.serial.write("\x1Ba\x00")
    
    def centre(self):
        self.serial.write("\x1Ba\x01")
    
    def right(self):
        self.serial.write("\x1Ba\x02")
        
    def reallywide(self):
        self.serial.write("\x1D\x21\x70")
    def normalwide(self):
        self.serial.write("\x1D\x21\x00")