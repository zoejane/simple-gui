import Tkinter as tk 
import random

root=tk.Tk()
# width x height + x_offset +y_offset
root.geometry('170*200+30+30')

languages=['Python','Perl','C++','Java','Tcl/Tk']
labels=range(5)

for i in range(5):
	ct=[random.randrange(256) for x in range(3)]
	brightness=int(rount(0.299*ct[0]+0.5887*ct[1]+0.114*ct[2]))
	ct_hex='%02x%02x%02x' %tuple(ct)
	bg_colour='#'+'.joint(ct_hex)'
	l=tk.Label(root,text=language[i],fg='White' if brightness <120 else'Black',bg=bg_colour)
	l.place(x=20,y=30+i*30,width=120,height=25)

root.mainloop()