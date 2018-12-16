import tkinter as tk
import math,random
main_window=tk.Tk()
#main_window.attributes("-alpha",0.8)
canvas = tk.Canvas(main_window, bg='skyblue',  width=800,height=200)
Ox=40
Oy=40
rad=72
cw=[270,306,342,18,54,90,126,162,198,234]
ucw=[270,234,198,162,126,90,54,18,342,306]
default=1

#def指數轉成角度
def inx(index):
    angle = [0,0,0,0,0]
    for i in range(5):
        if(i%2==0):
            ans = cw[index[i]]
            if i<4:ans = ans+(3.6*index[i+1])
            if i==4: ans = ans+(3.6*default)
            angle[i]=ans
        else:
            ans = ucw[index[i]]
            if i<4:ans = ans-(3.6*index[i+1])
            angle[i]=ans
    return angle
#def 圓圈刻度
def circle_ptr():
    for c in range(5):
        p = c*rad*2
        for i in range(10):
            di=18
            x=Ox+rad
            y=Oy+rad
            dotsize=2
            radi=math.radians(0+di+(i*36))
            rcos=rad*math.cos(radi)
            rsin=rad*math.sin(radi)
            cir_ptr= canvas.create_oval(p+x+rcos-dotsize,y+rsin-dotsize,p+x+rcos+dotsize,y+rsin+dotsize,fill='black')
#def 圓圈 阿拉伯數字
def circle_num(font_type):
    font_size ,num_position = int(rad/3) ,int(rad/4.5)
    di,x,y = 270,Ox+rad,Oy+rad
    for c in range(5):
        p = c*rad*2
        for i in range(10):
            radi=math.radians(0+di+(i*36))
            if c==1 or c==3:
                radi=math.radians(0+di-(i*36))
            rcos=(rad-num_position)*math.cos(radi)
            rsin=(rad-num_position)*math.sin(radi)
            cir_num= canvas.create_text(p+x+rcos,y+rsin,text=str(i),font=(font_type,font_size))
#def 5個圓圈框框
def circle_frame(x,y):
    for i in range(5):
        p= i*rad*2
        cir1 = canvas.create_oval(x+p,y,x+p+rad*2,y+rad*2,fill='silver')
        cir1 = canvas.create_oval(x+p+1,y+1,x+p+rad*2-1,y+rad*2-1,fill='silver')
# def 中心點 中心圓圈
def central_dot(Ox,Oy,color):
    dot_size=int(rad/24)
    cir_size = int(rad/3.6)
    x=Ox+rad
    y=Oy+rad
    for i in range(5):
        p = i*rad*2
        cir = canvas.create_oval(x-cir_size+p,y-cir_size,x+cir_size+p,y+cir_size,fill='black')
        cen = canvas.create_oval(x-dot_size+p,y-dot_size,x+dot_size+p,y+dot_size,fill=color)
        #central_dot(Ox,Oy,"white")#for temp use
        canvas.pack()
# def 指針指向器
def pointer(degree):  # array input!
    for c in range(5):
        i=degree[c]
        p=c*rad*2
        x=Ox+rad
        y=Oy+rad
        p_size= int(rad/3.6) # pointer width size
        pp_size = int(rad/36) # pointer tail width size
        #dotsize=3 # temply use
        radi=math.radians(i)
        right=math.radians(i+90)
        left=math.radians(i-90)
    
        v_rcos=(rad-4)*math.cos(radi)
        v_rsin=(rad-4)*math.sin(radi)
        #cir_ptr= canvas.create_oval(p+x-dotsize,y-dotsize,p+x+dotsize,y+dotsize,fill='green')
        r_rcos=p_size*math.cos(right)
        r_rsin=p_size*math.sin(right)
        #right_ptr= canvas.create_oval(p+x+r_rcos-dotsize,y+r_rsin-dotsize,p+x+r_rcos+dotsize,y+r_rsin+dotsize,fill='gold')
        l_rcos=p_size*math.cos(left)
        l_rsin=p_size*math.sin(left)
        #left_ptr= canvas.create_oval(p+x+l_rcos-dotsize,y+l_rsin-dotsize,p+x+l_rcos+dotsize,y+l_rsin+dotsize,fill='gold')
        rcos=rad*math.cos(radi)
        rsin=rad*math.sin(radi)
        #cir_ptr= canvas.create_oval(p+x+v_rcos-dotsize,y+v_rsin-dotsize,p+x+v_rcos+dotsize,y+v_rsin+dotsize,fill='red')
        
        x1=p+x+v_rcos
        y1=  y+v_rsin
        x2=p+x+v_rcos
        y2=  y+v_rsin # for pointer tail use
        
        RR_rcos=pp_size*math.cos(right)
        RR_rsin=pp_size*math.sin(right)
        #cir_ptr= canvas.create_oval(x1+RR_rcos-2,y1+RR_rsin-2,x2+RR_rcos+2,y2+RR_rsin+2,fill='blue')
        
        RL_rcos=pp_size*math.cos(left)
        RL_rsin=pp_size*math.sin(left)
        #cir_ptr= canvas.create_oval(x1+RL_rcos-2,y1+RL_rsin-2,x2+RL_rcos+2,y2+RL_rsin+2,fill='white')
        
        points = [ x1+RL_rcos,y1+RL_rsin  , x1+RR_rcos,y1+RR_rsin ,  p+x+r_rcos,y+r_rsin , p+x+l_rcos,y+l_rsin ]
        triangle = canvas.create_polygon(points,fill='black')
        central_dot(Ox,Oy,"gold")#for temp use
# def 初始化
def initial():
    main_window.title("台灣電力公司 TAI POWER")
    main_window.geometry('800x300')
    label = tk.Label(main_window,text="抄 表 練 習 程 式 Beta4",bg = 'yellow',font=('Arial Black',15)).place(x=0,y=0)
    #label = canvas.create_text(180,20,text="抄 表 練 習 程 式 Beta4",font=('Arial Black',20))
    circle_frame(Ox,Oy)
    central_dot(Ox,Oy,"white")
    circle_ptr()
    circle_num('Arial Black')
    #circle_num('Bahnschrift SemiBold')

def clear():
    circle_frame(Ox,Oy)
    central_dot(Ox,Oy,"white")
    circle_ptr()
    circle_num('Arial Black')

initial()


label_var = tk.StringVar()
label_var.set("test")
show_String = tk.Label(main_window,textvariable = label_var, bg='green')
show_String.place(x=350,y=220)
input_index=''
def clickOK():
    
    clear()
    b=random.randint(10000,99999)
    #a=list(str(input_index))
    a=list(str(b))
    index2 = [0,0,0,0,0]
    for i in range(5):
        index2[i]=int(a[i])
    
    pointer(inx(index2))
    print(index2)
    label_var.set(b)#temp use
    input_index=(index.get())

    
button = tk.Button(main_window,text="ENTER",command=clickOK)

index = tk.Entry(main_window,width=5)
index.place(x=350,y=240)
button.place(x=350,y=260)

main_window.resizable(0,0)
main_window.mainloop()

#frame=tk.PhotoImage(file='R:/12345.png')
#ptr_1=tk.PhotoImage(file='R:/pointer.png')
#label_f=tk.Label(main_window,image=frame)
#label_f.frame=frame
#label_f.place(x=10,y=30) 
#label_p1 = tk.Label(main_window,image=ptr_1)
#label_p1.frame=ptr_1
#label_p1.place(x=78,y=70)
