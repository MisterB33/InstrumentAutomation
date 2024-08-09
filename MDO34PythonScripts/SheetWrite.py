import time # std module
from datetime import datetime 
import pyvisa as visa # http://github.com/hgrecco/pyvisa
import matplotlib.pyplot as plt # http://matplotlib.org/
import numpy as np # http://www.numpy.org/



import os.path

import google.auth
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from google_auth_oauthlib.flow import InstalledAppFlow

SCOPES = ["https://www.googleapis.com/auth/spreadsheets"]

def update_values(spreadsheet_id, range_name, value_input_option,values):
  creds = None
  # The file token.json stores the user's access and refresh tokens, and is
  # created automatically when the authorization flow completes for the first
  # time.
  if os.path.exists("token.json"):
    creds = Credentials.from_authorized_user_file("token.json", SCOPES)
   #If there are no (valid) credentials available, let the user log in.
  if not creds or not creds.valid:
    if creds and creds.expired and creds.refresh_token:
        creds.refresh(Request())
    else:
        flow = InstalledAppFlow.from_client_secrets_file("credentials.json", SCOPES)
        creds = flow.run_local_server(port=0)
    with open("token.json", "w") as token:
        token.write(creds.to_json())

  # pylint: disable=maybe-no-member
  try:
    service = build("sheets", "v4", credentials=creds)
    #values = [
    #    [
    #      "Blah"  # Cell values ...
    #    ],["Blah"],["Blah"],["Blah"],["Blah"],["Blah"],["Blah"],["Blah"],["Blah"],["Blah"],["Blah"],["Blah"],["Blah"],["Blah"],["Blah"],["Blah"],["Blah"]
        # Additional rows ...
    #]
    body = {"values": values}
    result = (
        service.spreadsheets()
        .values()
        .update(
            spreadsheetId=spreadsheet_id,
            range=range_name,
            valueInputOption=value_input_option,
            body=body,
        )
        .execute()
    )
    print(f"{result.get('updatedCells')} cells updated.")
    return result
  except HttpError as error:
    print(f"An error occurred: {error}")
    return error


if __name__ == "__main__":
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
    scope.write('select:CH1 ON')

    scope.write('header 0')
    scope.write('data:encdg SRIBINARY')



#scope.write('CH2:TERmination Fifty')
#scope.write('CH1:TERmination Fifty')
    scope.write('CH1:SCAle 1000E-3')
    scope.write('CH2:SCAle 1000E-3')
    scope.write('HORizontal:SCAle 10E-6')


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
    value1 = scope.query(':MEASUrement:IMMed:VALue?') 
    units1 = scope.query(':MEASUrement:IMMed:Units?')
    print("Frequency value is:"+str(value1)+str(units1).replace('"',""))


    scope.write('MEASUrement:IMMed:SOUrce CH2') 
    scope.write('MEASUrement:IMMed:TYPe PWidth')
    value2 = scope.query(':MEASUrement:IMMed:VALue?') 
    units2 = scope.query(':MEASUrement:IMMed:Units?')
    print("High Period value is:"+str(value2)+str(units2).replace('"',""))

    scope.write('MEASUrement:IMMed:SOUrce CH2') 
    scope.write('MEASUrement:IMMed:TYPe NWidth')
    value3 = scope.query(':MEASUrement:IMMed:VALue?') 
    units3 = scope.query(':MEASUrement:IMMed:Units?')
    print("Low Period value is:"+str(value3)+str(units3).replace('"',"")) 

    scope.write('MEASUrement:IMMed:SOUrce CH2') 
    scope.write('MEASUrement:IMMed:TYPe Maximum')
    value4 = scope.query(':MEASUrement:IMMed:VALue?') 
    units4 = scope.query(':MEASUrement:IMMed:Units?')
    print("SCL Vmax value is:"+str(value4)+str(units4).replace('"',""))

    scope.write('MEASUrement:IMMed:SOUrce CH2') 
    scope.write('MEASUrement:IMMed:TYPe Minimum')
    value5 = scope.query(':MEASUrement:IMMed:VALue?') 
    units5 = scope.query(':MEASUrement:IMMed:Units?')
    print("SCL Vmin value is:"+str(value5)+str(units5).replace('"',"")) 

    scope.write('MEASUrement:IMMed:SOUrce CH2') 
    scope.write('MEASUrement:IMMed:TYPe HIGH')
    value6 = scope.query(':MEASUrement:IMMed:VALue?') 
    units6 = scope.query(':MEASUrement:IMMed:Units?')
    print("SCL Vih value is:"+str(value6)+str(units6).replace('"',"")) 

    scope.write('MEASUrement:IMMed:SOUrce CH2')
    scope.write('MEASUrement:IMMed:TYPe LOW')
    value7 = scope.query(':MEASUrement:IMMed:VALue?') 
    units7 = scope.query(':MEASUrement:IMMed:Units?')
    print("SCL Vil value is:"+str(value7)+str(units7).replace('"',""))

    scope.write('MEASUrement:IMMed:SOUrce CH1') 
    scope.write('MEASUrement:IMMed:TYPe Maximum')
    value8 = scope.query(':MEASUrement:IMMed:VALue?') 
    units8 = scope.query(':MEASUrement:IMMed:Units?')
    print("SDA Vmax value is:"+str(value8)+str(units8).replace('"',""))
    
    scope.write('MEASUrement:IMMed:SOUrce CH1') 
    scope.write('MEASUrement:IMMed:TYPe Minimum')
    value9 = scope.query(':MEASUrement:IMMed:VALue?') 
    units9 = scope.query(':MEASUrement:IMMed:Units?')
    print("SDA Vmin value is:"+str(value9)+str(units9).replace('"',"")) 
    
    scope.write('MEASUrement:IMMed:SOUrce CH1') 
    scope.write('MEASUrement:IMMed:TYPe HIGH')
    value10 = scope.query(':MEASUrement:IMMed:VALue?') 
    units10 = scope.query(':MEASUrement:IMMed:Units?')
    print("SDA Vih value is:"+str(value10)+str(units10).replace('"',"")) 

    scope.write('MEASUrement:IMMed:SOUrce CH1')
    scope.write('MEASUrement:IMMed:TYPe LOW')
    value11 = scope.query(':MEASUrement:IMMed:VALue?') 
    units11 = scope.query(':MEASUrement:IMMed:Units?')
    print("SDA Vil value is:"+str(value11)+str(units11).replace('"',""))

    scope.write('MEASUrement:IMMed:SOUrce CH2') 
    scope.write('MEASUrement:IMMed:TYPe Rise')
    value12 = scope.query(':MEASUrement:IMMed:VALue?') 
    units12 = scope.query(':MEASUrement:IMMed:Units?')
    print("SLC Rise Time value is:"+str(value12)+str(units12).replace('"',""))


    scope.write('MEASUrement:IMMed:SOUrce CH2') 
    scope.write('MEASUrement:IMMed:TYPe FaLL')
    value13 = scope.query(':MEASUrement:IMMed:VALue?') 
    units13 = scope.query(':MEASUrement:IMMed:Units?')
    print("SLC Fall Time value is:"+str(value13)+str(units13).replace('"',""))  


    scope.write('MEASUrement:IMMed:SOUrce CH1') 
    scope.write('MEASUrement:IMMed:TYPe Rise')
    value14 = scope.query(':MEASUrement:IMMed:VALue?') 
    units14 = scope.query(':MEASUrement:IMMed:Units?')
    print("SDA Rise Time value is:"+str(value14)+str(units14).replace('"',""))


    scope.write('MEASUrement:IMMed:SOUrce CH1') 
    scope.write('MEASUrement:IMMed:TYPe FaLL')
    value15 = scope.query(':MEASUrement:IMMed:VALue?') 
    units15 = scope.query(':MEASUrement:IMMed:Units?')
    print("SDA Fall Time value is:"+str(value15)+str(units15).replace('"',""))    

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
    
    data = [
        [str(value1)+str(units1).replace('"',"")],
        [str(value2)+str(units2).replace('"',"")],
        [str(value3)+str(units3).replace('"',"")],
        [str(value4)+str(units4).replace('"',"")],
        [str(value5)+str(units5).replace('"',"")],
        [str(value6)+str(units6).replace('"',"")],
        [str(value7)+str(units7).replace('"',"")],
        [str(value8)+str(units8).replace('"',"")],
        [str(value9)+str(units9).replace('"',"")],
        [str(value10)+str(units10).replace('"',"")],
        [str(value11)+str(units11).replace('"',"")],
        [str(value12)+str(units12).replace('"',"")],
        [str(value13)+str(units13).replace('"',"")],
        [str(value14)+str(units14).replace('"',"")],
        [str(value15)+str(units15).replace('"',"")],
        ["BLah"],
        ["Blah"]
        # Additional rows ...
    ]

    rm.close()
    #Call the update function to update to sheet 
    update_values("1WrW5aJBcb1NHwmRm1FiYAPY9yuzubNQSp5VkB2i0-No","MezzI2C!C147:C163","USER_ENTERED",data)