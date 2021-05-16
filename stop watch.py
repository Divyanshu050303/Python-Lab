from tkinter import *
from tkinter.ttk import *
s=h=m=stp=0
def start():
    global s, h, m
    s+=1
    if s==60:
        s=0
        m+=1
    if m==60:
        m=0
        h+=1
    if stp==0:
        lbl=Label(root, text="%i:%i:%i" %(h, m, s), font=("arial", 30, "bold"), foreground='red')
        lbl.after(300, start)
        lbl.place(x=50, y=60)
def stop():
    global stp
    stp=1
root=Tk()
style=Style()
root.title("Stop watch")
root.geometry("250x160")
root.resizable(False, False)
root.configure(bg="yellow")
style.configure('Tbutton', font=('arial', 10, 'bold'), boderwidth='5')
button1=Button(root, text="start", command=start).place(x=10, y=10)
button2=Button(root, text="stop", command=stop).place(x=160, y=10)

root.mainloop()