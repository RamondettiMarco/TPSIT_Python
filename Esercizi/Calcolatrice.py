from tkinter import *

finestra = Tk()
finestra.title("Calcolatrice Python")
finestra.geometry("400x400+75+100")

coloreSfondoB = "black"
coloreScrittaB = "white"

coloreScritta = "white"
coloreSfondo = "blue"

add1 = DoubleVar()
add2 = DoubleVar()


def somma():
    sommaV = IntVar()
    sommaV = (add1.get() + add2.get())
    testo = Label(finestra, text= sommaV, fg = coloreScritta, bg = coloreSfondo, font = ("Helvetica", 22)).pack()
    
def moltiplicazione():
    sommaV = IntVar()
    sommaV = (add1.get() * add2.get())
    testo = Label(finestra, text= sommaV, fg = coloreScritta, bg = coloreSfondo, font = ("Helvetica", 22)).pack()
    
def divisione():
    sommaV = IntVar()
    try:
        sommaV = (add1.get() / add2.get())
        testo = Label(finestra, text= sommaV, fg = coloreScritta, bg = coloreSfondo, font = ("Helvetica", 22)).pack()
    except(ZeroDivisionError):
        testo = Label(finestra, text= "Divizione per Zero!", fg = coloreScritta, bg = coloreSfondo, font = ("Helvetica", 22)).pack()
        
        
def sottrazoine():
    sommaV = IntVar()
    sommaV = (add1.get() - add2.get())
    testo = Label(finestra, text= sommaV, fg = coloreScritta, bg = coloreSfondo, font = ("Helvetica", 22)).pack()
 
#Inserimento numeri   
Add1 = Entry(finestra, textvariable = add1).pack(fill = X)
a = Label(text = "-----------------------------------------").pack(fill = X)
Add2 = Entry(finestra, textvariable = add2).pack(fill = X)
a = Label(text = "-----------------------------------------").pack(fill = X)


#Bottoni
Somma = Button(text = "Somma", bg = coloreSfondoB, fg = coloreScrittaB, command = somma).pack(anchor = E, fill = X)
Moltiplicazione = Button(text = "Moltiplicazione", bg = coloreSfondoB, fg = coloreScrittaB, command = moltiplicazione).pack(anchor = E, fill = X)
Divisione = Button(text = "Divisione", bg = coloreSfondoB, fg = coloreScrittaB, command = divisione).pack(anchor = E, fill = X)
Sottrazione = Button(text = "Sottrazione", bg = coloreSfondoB, fg = coloreScrittaB, command = sottrazoine).pack(anchor = E, fill = X)

finestra.mainloop()