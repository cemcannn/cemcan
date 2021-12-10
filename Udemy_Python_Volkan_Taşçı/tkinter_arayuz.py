from tkinter import *
pencere = Tk()
# Aşağıda buton tanımlama işlemi yapıyoruz.
rakam1 = Button(text = "buton1", fg="red",bg="yellow") # 1. buton fg = foreground, bg = background
rakam2 = Button(text = "buton2", fg="blue",bg="yellow")
rakam3 = Button(text = "buton3", fg="green",bg="yellow")

rakam1.pack() # Butonu pack fonksiyonu ile ekrana alıyorsun.
rakam2.pack()
rakam3.pack(side = LEFT) # Butonu sola ya da sağa almak için side ile ekrandaki yerini belirleyebiliyoruz.

yazi = Label(text = "merhaba dünya")

yazi.pack(side = BOTTOM)
pencere.mainloop() # Pencerenin oluşturulup sürekli ekranda kalması için mainloop fonksiyonu kullanılır.