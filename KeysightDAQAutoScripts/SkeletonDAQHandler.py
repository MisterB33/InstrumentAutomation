#Majid Reza Barghi 
#Keysight DAQ Skeleton Code on how to configure the relays and Temperature for multiple channels 

import pyvisa as visa 


#Place your Visa ID Here 

VISA_ID ="TCPIP0::10.110.117.26::INSTR" 


#setting up Py Visa 
class DAQ:
    def __init__(self,verbose ,visa_address=VISA_ID):
        self.visa_address = visa_address
        self.rm = visa.ResourceManager()
        self.myDAQ = self.rm.open_resource(self.visa_address)
        self.relay1 = False ; 
        self.relay2 = False ; 
        if verbose:
            print("Sucessful connection...")
#Return State of Tray     
    def getStateOfTray1(self):
        return self.relay1
    def getStateOfTray2(self):
        return self.relay2 
#Example of how to triger the Relay to Close 
    def turnOnTray1(self):
        self.myDAQ.write("ROUT:ClOS (@202)")
        self.relay1 = True 
        print("success")
#Example of how to triger the Relay to Open 
    def turnOffTray1(self): 
        self.myDAQ.write("ROUT:OPEN (@202)")
        print("tray turned off")
        self.relay1 = False
    
    def turnOnTray2(self):
        self.relay2 = True
        print("sucess")
        self.myDAQ.write("ROUT:CLOS (@201)")
    def turnOffTray2(self):
        self.relay2 = False
        print(' tray 2 turned off')
        self.myDAQ.write("ROUT:OPEN (@201)")
#This function will collect data from channels 1-8 in tray 1 of the mux         
    def getTemperature(self,verbose = False):
        self.myDAQ.write("CONFigure:TEMPerature:TCouple K,1,(@101:108)")
        self.myDAQ.write("UNIT:TEMPerature C")
        self.myDAQ.write("ROUTe:SCAN (@101:108)")
        self.myDAQ.write("ROUTe:MONitor (@101:108)")
        self.myDAQ.write("ROUTe:MONitor:STATe 1")
        self.myDAQ.write("TRIGger:SOURce BUS")
        self.myDAQ.write("INITiate")
        self.myDAQ.write("*TRG")
        dataset = self.myDAQ.query("FETCh?")
        dataset = dataset.strip("\n")
        TempData = dataset.split(",")
        FloatTempData = [float(string) for string in TempData]
        if verbose:
            print(FloatTempData)
        return FloatTempData