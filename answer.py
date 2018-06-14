'''
Q1. Create a dict with name and mobile number.
Define a GUI interface using tkinter
and pack the label and create a scrollbar
to scroll the list of keys in the dictionary.

Q2. In the same tkinter file as created above,
create a function to insert items into the dictionary.
'''

from tkinter import *

root=Tk()

def add():
    
    dic1={}
    key=keyE.get()
    value=valueE.get()
    dic1[key]=value
    
    for i in dic1:
        listB.insert(END,i)
        keyE.delete(0,'end')
        valueE.delete(0,'end')
        keyE.focus()

lbl_1=Label(root,text="Enter Name:")
lbl_1.grid(row=1,column=0)

lbl_2=Label(root,text="Enter Mobile Number:")
lbl_2.grid(row=2,column=0)

keyE=Entry(root)
keyE.grid(row=1,column=1)

valueE=Entry(root)
valueE.grid(row=2,column=1)

addB=Button(root,text='ADD',command=add)
addB.grid(row=3,column=1)

listB=Listbox(root,height=6,width=35)
listB.grid(row=4,column=0,rowspan=8,columnspan=2)

sb=Scrollbar(root)
sb.grid(row=4,column=1,sticky='e')

listB.configure(yscrollcommand=sb.set)
sb.configure(command=listB.yview)

root.mainloop()
