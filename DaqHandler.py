import pyvisa as visa # http://github.com/hgrecco/pyvisa



class DAQ:
    def __init__(self, visa_address="TCPIP0::10.110.4.83::INSTR"):
        self.visa_address = visa_address
        self.rm = visa.ResourceManager()
        self.myDAQ = self.rm.open_resource(self.visa_address)
        print("Sucessful connection...")
#visa_address = 'TCPIP0::10.110.4.83::INSTR'
#rm = visa.ResourceManager()

#myDAQ = rm.open_resource(visa_address)


    def getTemperature(self):
        Temp = [None] * 8 
        self.myDAQ.write("CONFigure:TEMPerature:TCouple DEFault,1,(@101:107)")
        self.myDAQ.write("UNIT:TEMPerature C")
        self.myDAQ.write("ROUTe:SCAN (@101)")
        self.myDAQ.write("ROUTe:MONitor (@101)")
        self.myDAQ.write("ROUTe:MONitor:STATe 1")
        self.myDAQ.write("TRIGger:SOURce BUS")
        self.myDAQ.write("INITiate")
        self.myDAQ.write("*TRG")
        Temp[0] = self.myDAQ.query("FETCh?")
        self.myDAQ.write("ROUTe:SCAN (@107)")
        self.myDAQ.write("ROUTe:MONitor (@107)")
        self.myDAQ.write("ROUTe:MONitor:STATe 1")
        self.myDAQ.write("TRIGger:SOURce BUS")
        self.myDAQ.write("INITiate")
        self.myDAQ.write("*TRG")
        Temp[1] = self.myDAQ.query("FETCh?")
        return Temp




