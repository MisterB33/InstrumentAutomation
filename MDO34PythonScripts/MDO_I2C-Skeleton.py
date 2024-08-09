import time # std module
from datetime import datetime 
import pyvisa as visa # http://github.com/hgrecco/pyvisa
import matplotlib.pyplot as plt # http://matplotlib.org/
import numpy as np # http://www.numpy.org/

visa_address = 'TCPIP0::10.110.4.27::inst0::INSTR'
fileSaveLocation = r'C:/Users/us62019230/Documents/' # Folder on your PC where to save image


rm = visa.ResourceManager()
scope = rm.open_resource(visa_address)
scope.timeout = 30000 # ms
scope.encoding = 'latin_1'
scope.read_termination = '\n'
scope.write_termination = None
scope.write('*cls') # clear ESR

scope.write('*rst') # reset 


scope.write('select:CH2 ON ')
#scope.write('FPANEL:PRESS CH2')
scope.write('select:CH1 ON')




#cope.write('autoset EXECUTE') # autoset
#3 = time.perf_counter()
# = scope.query('*opc?') # sync
#4 = time.perf_counter()
#rint('autoset time: {} s'.format(t4 - t3))

scope.write('header 0')
scope.write('data:encdg SRIBINARY')


#scope.write('FPANEL:PRESS CH1')
#scope.write('data:source CH3')
#scope.write('FPANEL:PRESS CH3')





#Hor = scope.query('HORizontal:SCAle?')
#print("Horizantal scale value is: "+str(Hor))




#scope.write('CH2:TERmination Fifty')
#scope.write('CH1:TERmination Fifty')
scope.write('CH1:SCAle 1000E-3')
scope.write('CH2:SCAle 1000E-3')
scope.write('HORizontal:SCAle 1E-6')
#Vert = scope.query('CH3:SCAle?')
#print("Vertical scale value is: "+str(Vert))

scope.write('TRIGGER:A:TYPE EDGe')
scope.write('TRIGGER:A:EDGE:SOURCE CH2')
scope.write('TRIGger:A:EDGE:COUPling DC')
scope.write('TRIGger:A:EDGE:SLOpe RISE')
scope.write('TRIGger:A:LEVel:CH2 .9') # ECL sets it to preset 


scope.write('acquire:state OFF') # stop
scope.write('acquire:stopafter SEQUENCE') # single
scope.write('acquire:state ON') # run

time.sleep(5.0)

scope.write('MEASUrement:IMMed:SOUrce CH2') 
scope.write('MEASUrement:IMMed:TYPe Frequency')
value = scope.query(':MEASUrement:IMMed:VALue?') 
units = scope.query(':MEASUrement:IMMed:Units?')
print("Frequency value is:"+str(value)+str(units).replace('"',""))


scope.write('MEASUrement:IMMed:SOUrce CH2') 
scope.write('MEASUrement:IMMed:TYPe PWidth')
value = scope.query(':MEASUrement:IMMed:VALue?') 
units = scope.query(':MEASUrement:IMMed:Units?')
print("High Period value is:"+str(value)+str(units).replace('"',""))

scope.write('MEASUrement:IMMed:SOUrce CH2') 
scope.write('MEASUrement:IMMed:TYPe NWidth')
value = scope.query(':MEASUrement:IMMed:VALue?') 
units = scope.query(':MEASUrement:IMMed:Units?')
print("Low Period value is:"+str(value)+str(units).replace('"',"")) 

scope.write('MEASUrement:IMMed:SOUrce CH2') 
scope.write('MEASUrement:IMMed:TYPe Maximum')
value = scope.query(':MEASUrement:IMMed:VALue?') 
units = scope.query(':MEASUrement:IMMed:Units?')
print("SCL Vmax value is:"+str(value)+str(units).replace('"',""))

scope.write('MEASUrement:IMMed:SOUrce CH2') 
scope.write('MEASUrement:IMMed:TYPe Minimum')
value = scope.query(':MEASUrement:IMMed:VALue?') 
units = scope.query(':MEASUrement:IMMed:Units?')
print("SCL Vmin value is:"+str(value)+str(units).replace('"',"")) 

scope.write('MEASUrement:IMMed:SOUrce CH2') 
scope.write('MEASUrement:IMMed:TYPe HIGH')
value = scope.query(':MEASUrement:IMMed:VALue?') 
units = scope.query(':MEASUrement:IMMed:Units?')
print("SCL Vih value is:"+str(value)+str(units).replace('"',"")) 

scope.write('MEASUrement:IMMed:SOUrce CH2')
scope.write('MEASUrement:IMMed:TYPe LOW')
value = scope.query(':MEASUrement:IMMed:VALue?') 
units = scope.query(':MEASUrement:IMMed:Units?')
print("SCL Vil value is:"+str(value)+str(units).replace('"',""))

scope.write('MEASUrement:IMMed:SOUrce CH1') 
scope.write('MEASUrement:IMMed:TYPe Maximum')
value = scope.query(':MEASUrement:IMMed:VALue?') 
units = scope.query(':MEASUrement:IMMed:Units?')
print("SDA Vmax value is:"+str(value)+str(units).replace('"',""))

scope.write('MEASUrement:IMMed:SOUrce CH1') 
scope.write('MEASUrement:IMMed:TYPe Minimum')
value = scope.query(':MEASUrement:IMMed:VALue?') 
units = scope.query(':MEASUrement:IMMed:Units?')
print("SDA Vmin value is:"+str(value)+str(units).replace('"',"")) 

scope.write('MEASUrement:IMMed:SOUrce CH1') 
scope.write('MEASUrement:IMMed:TYPe HIGH')
value = scope.query(':MEASUrement:IMMed:VALue?') 
units = scope.query(':MEASUrement:IMMed:Units?')
print("SDA Vih value is:"+str(value)+str(units).replace('"',"")) 

scope.write('MEASUrement:IMMed:SOUrce CH1')
scope.write('MEASUrement:IMMed:TYPe LOW')
value = scope.query(':MEASUrement:IMMed:VALue?') 
units = scope.query(':MEASUrement:IMMed:Units?')
print("SDA Vil value is:"+str(value)+str(units).replace('"',""))

scope.write('MEASUrement:IMMed:SOUrce CH2') 
scope.write('MEASUrement:IMMed:TYPe Rise')
value = scope.query(':MEASUrement:IMMed:VALue?') 
units = scope.query(':MEASUrement:IMMed:Units?')
print("SLC Rise Time value is:"+str(value)+str(units).replace('"',""))


scope.write('MEASUrement:IMMed:SOUrce CH2') 
scope.write('MEASUrement:IMMed:TYPe FaLL')
value = scope.query(':MEASUrement:IMMed:VALue?') 
units = scope.query(':MEASUrement:IMMed:Units?')
print("SLC Fall Time value is:"+str(value)+str(units).replace('"',""))  


scope.write('MEASUrement:IMMed:SOUrce CH1') 
scope.write('MEASUrement:IMMed:TYPe Rise')
value = scope.query(':MEASUrement:IMMed:VALue?') 
units = scope.query(':MEASUrement:IMMed:Units?')
print("SDA Rise Time value is:"+str(value)+str(units).replace('"',""))


scope.write('MEASUrement:IMMed:SOUrce CH1') 
scope.write('MEASUrement:IMMed:TYPe FaLL')
value = scope.query(':MEASUrement:IMMed:VALue?') 
units = scope.query(':MEASUrement:IMMed:Units?')
print("SDA Fall Time value is:"+str(value)+str(units).replace('"',""))    

print('Saving Screen shot....')

scope.write("SAVe:IMAGe:FILEFormat PNG")
scope.write("SAVe:IMAGe:INKSaver OFF")
scope.write("HARDCopy STARt")
imgData = scope.read_raw()

# Generate a filename based on the current Date & Time
dt = datetime.now()
fileName = dt.strftime("%Y%m%d_%H%M%S.png")

imgFile = open(fileSaveLocation + fileName, "wb")
imgFile.write(imgData)
imgFile.close()

print("Screen Shot Saved")

scope.close()

rm.close()

