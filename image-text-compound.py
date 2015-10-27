from Tkinter import *

root=Tk()

logo=PhotoImage(file='images/python_logo_small.gif')
explation = '''At present, only GIF and PPM/PGM
formats are supported, but an interface 
exists to allow additional image file
formats to be added easily.'''

w=Label(root,
		justify=LEFT,
		compound=LEFT,
		padx=10,
		text=explation,
		image=logo).pack(side='right')

root.mainloop()