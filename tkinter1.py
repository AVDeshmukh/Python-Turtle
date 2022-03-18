from tkinter import *
import tkinter.messagebox
import tkinter.ttk
groot=Tk()

tkinter.messagebox.showinfo("Tic Tac Toe","Welcome")
def anu():
	label1=Label(groot,text="You have done huge mistake")
	label1.pack()



button1=Button(groot,text='a' ,command=anu)
#button1.grid(row=1,column=0)
button1.pack()
button2=Button(groot,command=anu)
#button2.grid(row=1,column=1)
button2.pack()





















groot.mainloop()