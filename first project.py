from tkinter import *
root=Tk()
root.geometry("400x600")
#root.maxsize(400, 600)
root.minsize(400, 600)
photo=PhotoImage(file="luckey thakur.png")
label=Label(image=photo)
label.pack()
root.mainloop()