import random
from tkinter import *

root = Tk()
root.geometry("312x80")
root.resizable(0, 0)
root.title("Farbengenerator")

#format RGB to Hex
def rgb2hex(r,g,b):
    global varWertHex
    varWertHex = "#{:02x}{:02x}{:02x}".format(r,g,b)

#main function
def randomFarbe():
    global varWertHex
    #reset variables 'n list
    listFarbenWerte = ["R:", "G:" ,"B:"]
    varColourWert = varInputText = ""
    #main code
    for x in listFarbenWerte[:3]:
        #generate random color
        varColourWert = random.randrange(0, 255)
        #save color / add color to list
        listFarbenWerte.append(varColourWert)
        #add new color to output string
        varInputText = f"{varInputText}  {str(x)} {str(varColourWert)}"

    rgb2hex(listFarbenWerte[3],listFarbenWerte[4],listFarbenWerte[5])
    #set Output and main background color
    output_text.set(f"{varInputText} Hex: {varWertHex}")
    root.configure(background=f"{varWertHex}")

varWertHex = output_text = StringVar()

#tkinter stuff
input_frame = Frame(root, width=1000, height=50, bd=0, highlightbackground="black", highlightcolor="black", highlightthickness=2)
input_frame.pack(side=TOP)
input_field = Entry(input_frame, font=('arial', 13, 'bold'), textvariable=output_text, width=1000, bg="#eee", bd=0, justify=RIGHT).pack(ipady=10)

btns_frame = Frame(root, width=1000, height=272.5, bg="grey")
btns_frame.pack()
generate = Button(btns_frame, text = "Drücke hier für eine zufällige Farbe!", command = randomFarbe).grid(column = 0, row = 1)

root.mainloop()
