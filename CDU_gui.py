import customtkinter as ctk
import CircProgBar as atk
import awesometkinter as AT
import os
from PIL import Image
import random
import threading
import time 
import DaqHandler as CDUDAQ



#window 
fu = CDUDAQ.DAQ()
temp1 = fu.getTemperature()
print(temp1)


window = ctk.CTk()
window.title("Celestica RCDU")
window.config(background = AT.DEFAULT_COLOR )
window.geometry('1500x1000')

#setting path to images 

image_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "test_images")
large_test_image = ctk.CTkImage(Image.open(os.path.join(image_path, "CLS Logo.png")), size=(500, 150))

#home_frame = ctk.CTkFrame(window., corner_radius=0, fg_color="transparent")
#home_frame.grid_columnconfigure(0, weight=1)


home_frame_large_image_label = ctk.CTkLabel(window,text="",fg_color=AT.DEFAULT_COLOR , image=large_test_image)
home_frame_large_image_label.grid(row=0,column =4, padx=20, pady=10)

value = [None] * 8 
value[0] = random.randint(0,3000)
value[1] = random.randint(0,3000)
value[2] = random.randint(0,3000)


#funtion to update values 





    




frame_1 = AT.Frame3d(window)
frame_1.grid(row=1,columnspan=2,padx=5, pady=5)


bar1 = atk.RadialProgressbar(frame_1, fg='green', parent_bg=AT.DEFAULT_COLOR, size=(120,120))
bar1.grid(row=1,columnspan=2, pady=20, padx=20)

button_1 = AT.Button3d(frame_1, text='Load 1')
button_1.grid(row=2, columnspan=2, pady=20, padx=20)

#label1 = ctk.CTkLabel(frame_1, text="CTkLabel", fg_color="transparent")
label1 = AT.AutofitLabel(frame_1, text = "CTKLabel", bg= AT.DEFAULT_COLOR, fg = "white")
label1.grid(row=3, columnspan=2, pady=20, padx=20)

frame_2 = AT.Frame3d(window)
frame_2.grid(row=1,columnspan=2,column = 2, padx=5, pady=5)


bar2 = atk.RadialProgressbar(frame_2, fg='green', parent_bg=AT.DEFAULT_COLOR, size=(120,120))
bar2.grid(row=1,columnspan=2, column = 2, pady=20, padx=20)

button_2 = AT.Button3d(frame_2, text='Load 2')
button_2.grid(row=2, columnspan=2,column = 2, pady=20, padx=20)

label2 = AT.AutofitLabel(frame_2, text = "CTKLabel", bg= AT.DEFAULT_COLOR, fg = "white")
label2.grid(row=3, columnspan=2, column = 2, pady=20, padx=20)

frame_3 = AT.Frame3d(window)
frame_3.grid(row=1,columnspan=2,column = 4, padx=5, pady=5)


bar3 = atk.RadialProgressbar(frame_3, fg='green', parent_bg=AT.DEFAULT_COLOR, size=(120,120))
bar3.grid(row=1,columnspan=2, column = 4, pady=20, padx=20)

button_3 = AT.Button3d(frame_3, text='Load 3')
button_3.grid(row=2, columnspan=2,column = 4, pady=20, padx=20)

frame_4 = AT.Frame3d(window)
frame_4.grid(row=1,columnspan=2,column = 5, padx=5, pady=5)

bar4 = atk.RadialProgressbar(frame_4, fg='green', parent_bg=AT.DEFAULT_COLOR, size=(120,120))
bar4.grid(row=1,columnspan=2, column = 5, pady=20, padx=20)

button_4 = AT.Button3d(frame_4, text='Load 4')
button_4.grid(row=2, columnspan=2,column = 5, pady=20, padx=20)



def updatebutton_function():
    bar1.set(value[0])
    bar2.set(value[1])
    bar3.set(value[2])
    bar4.set(value[3])
#ctk.set_appearance_mode('dark')
def updateValues(): 
    threading.Timer(1,updateValues).start()
    value[0] = random.randint(0,3000)
    value[1] = random.randint(0,3000)
    value[2] = random.randint(0,3000)
    value[3] = random.randint(0,3000)
    print("updated values")
    updatebutton_function()

def updateTemperature(): 
    temp = fu.getTemperature()
    
    
def updateTemperatureVals():
    temp = fu.getTemperature()
    label1.configure(text=str(float(temp[0]))+" C")
    label2.configure(text=str(float(temp[1]))+" C")
    threading.Timer(1,updateTemperatureVals).start()
    
    
    

    


# update every second time is in ms 

#window.after(1000, updatebutton_function)



#run 
updateTemperatureVals()
updateValues()
window.mainloop()




