from tkinter import *

root = Tk()
root.title('PPT Calculator')
root.geometry('1000x800')
root.resizable(width=FALSE, height=FALSE)


# create all of the main containers
frame0=LabelFrame(root,width=400)
frame1=LabelFrame(root,text='Input',width=400,height=300)
frame2=LabelFrame(root,text='Dap an',width=400)

# layout all of the main containers
root.grid_columnconfigure(0, weight=1)
root.grid_rowconfigure(2, weight=1)

frame0.grid(row=0,sticky='ew',padx=10,pady=10)
frame1.grid(row=1,sticky='ew',padx=10,pady=10)
frame2.grid(row=2,sticky='nsew',padx=10,pady=10)
# create the widgets for the frame0
li1=[
    'Phuong phap nhan doi',
    'Phuong phap day cung'
]
clickButton=StringVar()
clickButton.set(li1[0])
drop1=OptionMenu(frame0,clickButton,*li1)
drop1.config(width = 50)
label1f0=Label(frame0,text='Chon phuong phap: ')

# layout the widgets in the frame0
drop1.grid(row=0,column=1)
Button(frame0,text='Enter').grid(row=0,column=2)
Label(frame0,text='test').grid(row=1)
label1f0.grid(row=0,column=0)

# create the widgets for the frame1
entry1f1=Entry(frame1,width=120)
text1f1=Label(frame1,text='Nhap phuong trinh f(x): ')

# layout the widgets in the frame1
text1f1.grid(row=0,column=0)
entry1f1.grid(row=0,column=1)

# create the widgets for the frame2
frame2.grid_columnconfigure(1, weight=1)
frame2.grid_rowconfigure(0, weight=1)

text1f2=Label(frame2,text='Cac buoc lam ')
framedapan=LabelFrame(frame2)
text1fdapan=Label(framedapan,text='Cac buoc lam ')

# layout the widgets in the frame2
text1f2.grid(row=0,column=0,sticky='n')
framedapan.grid(row=0,column=1,sticky='nsew')
text1fdapan.pack()

root.mainloop()