from tkinter import *
from tkinter.font import *
from tkinter import messagebox
from unit_converter import *

def calc_unit():
    unit_from=listbox_from.get(ACTIVE)
    unit_to=listbox_to.get(ACTIVE)
    value_from=int(entry_from.get())

    my_cnv=unit_converter(unit_from,unit_to,value_from)
    #entry_to.delete(0,END)
    #entry_to=insert(END,my_cnv.cnvunits())

    # if unit_from=='centimeter':
    #     if unit_to=='centimeter':
    #         result=value_from
    
    entry_to.delete(0,END)
    entry_to.insert(END,my_cnv.cnvunits())


window=Tk()
my_font=Font(family='chshm',size=18)
pad_x=5
pad_y=5

label_from=Label(window,text='from',font=my_font)
label_to=Label(window,text='to',font=my_font)
label_from.grid(row=0,column=0,sticky=W,padx=pad_x,pady=pad_y)
label_to.grid(row=0,column=1,sticky=W)

entry_from=Entry(window,font=my_font,fg='red')
entry_to=Entry(window,font=my_font,fg='red')
entry_from.grid(row=1,column=0,padx=pad_x,pady=pad_y)
entry_to.grid(row=1,column=1,padx=pad_x,pady=pad_y)

listbox_from=Listbox(window,exportselection=False,font=my_font)
listbox_to=Listbox(window,exportselection=False,font=my_font)
listbox_from.grid(row=2,column=0,padx=pad_x,pady=pad_y)
listbox_to.grid(row=2,column=1,padx=pad_x,pady=pad_y)
listbox_from.insert(END,'centimeter')
listbox_from.insert(END,'meter')
listbox_from.insert(END,'kilometer')
listbox_from.insert(END,'mile')
listbox_from.insert(END,'yard')
listbox_to.insert(END,'centimeter')
listbox_to.insert(END,'meter')
listbox_to.insert(END,'kilometer')
listbox_to.insert(END,'mile')
listbox_to.insert(END,'yard')

btn=Button(window,text='calc',font=my_font,command=calc_unit)
btn.grid(row=3,column=0,columnspan=2,sticky=W+E,padx=pad_x,pady=pad_y)


window.mainloop()