from  tkinter import * # tkinterdan her şeyi çeker
from tkinter import messagebox # tkinterdan sadece mesaagebox fonksiyonu çeker
from time import * # time modülünden her şeyi çeker

pencere = Tk() #pencere objesine Tk class ı eşitliyoruz.

pencere.title("Python Programlama Tkinter") # pencerenin başlığı Python Programlama Tkinter
pencere.geometry("500x250")

uygulama = Frame(pencere)
uygulama.grid()

def dialog():
    var = messagebox.showinfo("Uyarı", "PythonProgramlama" )
    print(var)
    sleep(2)
    yok = messagebox.askyesnocancel("hata","uyarıaldınız")
    if yok == True:
        return dialog()

button1 = Button(uygulama,text="Mesaj Ver", width=20,command=dialog)
button1.grid(padx=110,pady=80) #buttonun x ekseninden 110 birim, y ekseninden 80 birim uzakta olacağını bildirir.

pencere.mainloop()