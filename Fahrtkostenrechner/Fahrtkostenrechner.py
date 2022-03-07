from tkinter import *

root = Tk()
root.geometry("500x300")
root.title("Fahrtkostenrechner")
root.resizable(0,0)

#main function
def Rechnung(Verbrauch_in_l_pro_1_km):
    output_text.set("")
    #get values
    Fahrtweite = entry_Fahrtweite_in_km.get()
    Spritpreis_pro_l = entry_Spritpreis_in_euronen.get()
    #calculate.
    SpritVerbraucht = float(Fahrtweite) * float(Verbrauch_in_l_pro_1_km)
    Endpreis = float(Spritpreis_pro_l) * SpritVerbraucht
    input_var = f"{round(Endpreis, 3)}€"
    output_text.set(input_var)

#button functions -> change fuel consumption (custom?)
def Opel_Meriva():
    Verbrauch_in_l_pro_1_km = 0.075
    Rechnung(Verbrauch_in_l_pro_1_km)

def Dacia_Logan():
    Verbrauch_in_l_pro_1_km = 0.067
    Rechnung(Verbrauch_in_l_pro_1_km)

def benutzerdef_verbrauch():
    Verbrauch_in_1_pro_100_km = entry_benutzerdef_verbrauch.get()
    Verbrauch_in_l_pro_1_km = float(Verbrauch_in_1_pro_100_km) / 100
    Rechnung(Verbrauch_in_l_pro_1_km)

output_text = StringVar()
 
#driving distance
label_Fahrtweite_in_km = Label(root, text = "Fahrtweite in KM:")
label_Fahrtweite_in_km.pack(side = TOP)
entry_Fahrtweite_in_km = Entry(root, width=20, font=('arial', 13))
entry_Fahrtweite_in_km.pack(side = TOP)

empty_Label_1 = Label(root, text = "")
empty_Label_1.pack(side=TOP)

#gas prices
label_Spritpreis_in_euronen = Label(root, text = "Spritpreis in Euronen (€):")
label_Spritpreis_in_euronen.pack(side = TOP)
entry_Spritpreis_in_euronen = Entry(root, width=20, font=('arial', 13))
entry_Spritpreis_in_euronen.pack(side = TOP)

empty_Label_2 = Label(root, text = "")
empty_Label_2.pack(side=TOP)

#fuel consumption
label_benutzerdef_verbrauch = Label(root, text = "Benutzerdefinierter Verbrauch in L/100km (optional):")
label_benutzerdef_verbrauch.pack(side = TOP)
entry_benutzerdef_verbrauch = Entry(root, width=20, font=('arial', 13))
entry_benutzerdef_verbrauch.pack(side = TOP)

empty_Label_2 = Label(root, text = "")
empty_Label_2.pack(side=TOP)

#output
ausgabe_frame = Frame(root, width=1000, height=50, bd=0, highlightbackground="black", highlightcolor="black", highlightthickness=2)
ausgabe_frame.pack()
ausgabe_field = Entry(ausgabe_frame, font=('arial', 13, 'bold'), textvariable=output_text, width=1000, bg="#eee", bd=0, justify=RIGHT).pack(ipady=10)

empty_Label_3 = Label(root, text = "")
empty_Label_3.pack(side=TOP)

#Buttons
btns_frame = Frame(root, width=1000, height=272.5, bg="grey")
btns_frame.pack()
generate_Meriva = Button(btns_frame, text = "Opel Meriva", command = Opel_Meriva).grid(column = 0, row = 1)
generate_custom = Button(btns_frame, text = "Benutzerdefinierter Verbrauch", command = benutzerdef_verbrauch).grid(column = 1, row = 1)
generate_Logan = Button(btns_frame, text = "Dacia Logan", command = Dacia_Logan).grid(column = 2, row = 1)

root.mainloop()