from Tkinter import *

root=Tk()

w=Label(root, text='Red Sun',bg='red',fg='white')
w.pack(fill=X,padx=10,pady=10)
w=Label(root,text='Green Grass',bg='green',fg='black')
w.pack(fill=X,padx=10,pady=10)
w=Label(root,text='Blue Sky',bg='blue',fg='white')
w.pack(fill=X,padx=10,pady=10,ipady=10)

mainloop()