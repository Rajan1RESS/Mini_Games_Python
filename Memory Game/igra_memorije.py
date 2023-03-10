import tkinter as tk
from tkinter import DISABLED, Frame, Image, Label, Menu, messagebox
import random
from tkinter import font
from tkinter.font import NORMAL


window = tk.Tk()
window.resizable(False,False)
window.title('Igra Memorije - Rajan Miletić')
window.geometry("532x580")
window.configure(bg='lightyellow')

parovi = ['\u26BD','\u231A','\u26C4','\u2615','\u26A1','\u2B50']
parovi_duzina = len(parovi)

kraj_igre = 0
dict_cards = {}
clicked_cards = 0
brojac = 0

prva_karta = ""
druga_karta = ""
fonts = ['Ariel','48','bold']


frame1 = Frame(window,bg='lightyellow')
frame1.pack()

d1 = tk.Button(frame1,width="3",height="1",bg='lightblue',font=(fonts),borderwidth=0,command=lambda:klik(d1))
d1.grid(row=0,column=0,padx=5, pady=5)
dict_cards[d1] = ""

d2 = tk.Button(frame1,width="3",height="1",bg='lightblue',font=(fonts),borderwidth=0,command=lambda:klik(d2))
d2.grid(row=0,column=1,padx=5, pady=5)
dict_cards[d2] = ""

d3 = tk.Button(frame1,width="3",height="1",bg='lightblue',font=(fonts),borderwidth=0,command=lambda:klik(d3))
d3.grid(row=0,column=2,padx=5, pady=5)
dict_cards[d3] = ""

d4 = tk.Button(frame1,width="3",height="1",bg='lightblue',font=(fonts),borderwidth=0,command=lambda:klik(d4))
d4.grid(row=0,column=3,padx=5, pady=5)
dict_cards[d4] = ""

d5 = tk.Button(frame1,width="3",height="1",bg='lightblue',font=(fonts),borderwidth=0,command=lambda:klik(d5))
d5.grid(row=1,column=0,padx=5, pady=5)
dict_cards[d5] = ""

d6 = tk.Button(frame1,width="3",height="1",bg='lightblue',font=(fonts),borderwidth=0,command=lambda:klik(d6))
d6.grid(row=1,column=1,padx=5, pady=5)
dict_cards[d6] = ""

d7 = tk.Button(frame1,width="3",height="1",bg='lightblue',font=(fonts),borderwidth=0,command=lambda:klik(d7))
d7.grid(row=1,column=2,padx=5, pady=5)
dict_cards[d7] = ""

d8 = tk.Button(frame1,width="3",height="1",bg='lightblue',font=(fonts),borderwidth=0,command=lambda:klik(d8))
d8.grid(row=1,column=3,padx=5, pady=5)
dict_cards[d8] = ""

d9 = tk.Button(frame1,width="3",height="1",bg='lightblue',font=(fonts),borderwidth=0,command=lambda:klik(d9))
d9.grid(row=2,column=0,padx=5, pady=5)
dict_cards[d9] = ""

d10 = tk.Button(frame1,width="3",height="1",bg='lightblue',font=(fonts),borderwidth=0,command=lambda:klik(d10))
d10.grid(row=2,column=1,padx=5, pady=5)
dict_cards[d10] = ""

d11 = tk.Button(frame1,width="3",height="1",bg='lightblue',font=(fonts),borderwidth=0,command=lambda:klik(d11))
d11.grid(row=2,column=2,padx=5, pady=5)
dict_cards[d11] = ""

d12 = tk.Button(frame1,width="3",height="1",bg='lightblue',font=(fonts),borderwidth=0,command=lambda:klik(d12))
d12.grid(row=2,column=3,padx=5, pady=5)
dict_cards[d12] = ""

frame2 = Frame(window,bg='lightyellow')
frame2.pack()

score = Label(frame2,font=15,text="Broj pokusaja: "+ str(0),bg='lightyellow')
score.grid(row=0,column=0,pady=20)

reset = tk.Button(frame2,width="12",height="2",font=15,text="Nova igra",command=lambda:reset())
reset.grid(row=1,column=0)


def random_text():
    pojavljivanja = {'\u26BD':0,'\u231A':0,'\u26C4':0,'\u2615':0,'\u26A1':0,'\u2B50':0}

    for karta in dict_cards:

        if len(parovi) > 0:
            random.shuffle(parovi)
            x = parovi[0]
            dict_cards[karta] = x
            pojavljivanja[x] = pojavljivanja[x] + 1

            if pojavljivanja[x] == 2:
                parovi.remove(x)
    

def klik(dugme):
    global clicked_cards
    global prva_karta
    global druga_karta
    global brojac

    clicked_cards = clicked_cards + 1

    if clicked_cards == 1:
        prva_karta = dugme
        dugme.configure(text=dict_cards[dugme],state=DISABLED)

    if clicked_cards == 2:
        druga_karta = dugme
        dugme.configure(text=dict_cards[dugme],state=DISABLED)      
        brojac = brojac + 1
        score.config(text = f"Broj pokusaja: {brojac}")  

        window.after(500,provjera_istih)


def provjera_istih():
    global clicked_cards
    global prva_karta
    global druga_karta
    global kraj_igre
    global parovi_duzina

    if druga_karta['text'] != prva_karta['text']:
        prva_karta.configure(text=" ",state="normal")
        druga_karta.configure(text=" ",state="normal")
    else:
        kraj_igre = kraj_igre + 1

    if kraj_igre == parovi_duzina:
        messagebox.showinfo("Kraj","Čestitamo, uspješno ste spojili sve parove sličica u "+str(brojac)+" poteza" )


    clicked_cards = 0

random_text()    

def reset():
    global dict_cards,brojac,kraj_igre
    global parovi

    d1.configure(text=" ",state="normal")
    d2.configure(text=" ",state="normal")
    d3.configure(text=" ",state="normal")
    d4.configure(text=" ",state="normal")
    d5.configure(text=" ",state="normal")
    d6.configure(text=" ",state="normal")
    d7.configure(text=" ",state="normal")
    d8.configure(text=" ",state="normal")
    d9.configure(text=" ",state="normal")
    d10.configure(text=" ",state="normal")
    d11.configure(text=" ",state="normal")
    d12.configure(text=" ",state="normal")
    
    parovi = ['\u26BD','\u231A','\u26C4','\u2615','\u26A1','\u2B50']
    random.shuffle(parovi)

    pojavljivanja = {'\u26BD':0,'\u231A':0,'\u26C4':0,'\u2615':0,'\u26A1':0,'\u2B50':0}

    brojac = 0
    kraj_igre = 0
    score.config(text = f"Broj pokusaja: {brojac}")
    random_text()    


window.mainloop()