import tkinter as tk

root = tk.Tk()
#root.attributes("-alpha",1.0)
root.title("台灣電力公司 TAI POWER")
root.geometry('800x300')
label = tk.Label(root,text="抄 表 練 習 程 式 Beta",bg = 'SkyBlue')
label.pack()
frame=tk.PhotoImage(file='R:/12345.png')
label_f=tk.Label(root,image=frame)
label_f.frame=frame
label_f.pack()


label_var = tk.StringVar()
label_var.set("test")
test_String = tk.Label(root,textvariable = label_var, bg='yellow')
test_String.pack()


def clickOK():
    label_var.set(index.get())
    
button = tk.Button(root,text="ENTER",command=clickOK)


index = tk.Entry(root,width=5)
index.pack()
button.pack()

root.mainloop()     
