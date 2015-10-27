from Tkinter import *
master=Tk()
whatever_you_do='Whatever you do will be insignificant, but it is very import that you do it.\n(Mahatma Gandi)'
msg=Message(master,text=whatever_you_do)
msg.config(bg='lightgreen',font=('times',24,'italic'))
msg.pack()
mainloop()