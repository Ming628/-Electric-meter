import tkinter as tk
main_window=tk.Tk()


def initial():
    
    main_window.title("台灣電力公司 TAI POWER")
    main_window.geometry('800x300')
    label = tk.Label(main_window,text="抄 表 練 習 程 式 Beta2",bg = 'SkyBlue')
    label.pack()
    frame=tk.PhotoImage(file='R:/12345.png')
    #main_window.attributes("-alpha",1.0)
    label_f=tk.Label(main_window,image=frame)
    label_f.frame=frame
    label_f.pack()



initial()

label_var = tk.StringVar()
label_var.set("test")
test_String = tk.Label(main_window,textvariable = label_var, bg='yellow')
test_String.pack()

def clickOK():
    label_var.set(index.get())
    
button = tk.Button(main_window,text="ENTER",command=clickOK)

index = tk.Entry(main_window,width=5)
index.pack()
button.pack()

main_window.resizable(0,0)
main_window.mainloop()
