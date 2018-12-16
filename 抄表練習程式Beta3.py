import tkinter as tk
import math
#from PIL import Image,ImageTK,ImageSequence
main_window=tk.Tk()
#main_window.attributes("-alpha",1.0)
canvas = tk.Canvas(main_window, bg='skyblue',  width=800,height=200)
Ox=40
Oy=40
rad=72

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


def circle_num(font_type):
    font_size ,num_position = int(rad/3.6) ,int(rad/4.8)
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

def circle_frame(x,y):
    for i in range(5):
        p= i*rad*2
        cir1 = canvas.create_oval(x+p,y,x+p+rad*2,y+rad*2,fill='silver')
        cir1 = canvas.create_oval(x+p+1,y+1,x+p+rad*2-1,y+rad*2-1,fill='silver')


def central_dot(Ox,Oy,color):
    dot_size=int(rad/24)
    cir_size = int(rad/4.8)
    x=Ox+rad
    y=Oy+rad
    for i in range(5):
        p = i*rad*2
        cir = canvas.create_oval(x-cir_size+p,y-cir_size,x+cir_size+p,y+cir_size,fill='black')
        cen = canvas.create_oval(x-dot_size+p,y-dot_size,x+dot_size+p,y+dot_size,fill=color)
        #central_dot(Ox,Oy,"white")#for temp use
        canvas.pack()


def initial():
    main_window.title("台灣電力公司 TAI POWER")
    main_window.geometry('800x300')
    label = tk.Label(main_window,text="抄 表 練 習 程 式 Beta3",bg = 'yellow',font=('Arial Black',15)).place(x=0,y=0)
    #label = canvas.create_text(180,20,text="抄 表 練 習 程 式 Beta3",font=('Arial Black',20))
    circle_frame(Ox,Oy)
    central_dot(Ox,Oy,"white")
    circle_ptr()
    circle_num('Arial Black')
    #circle_num('Bahnschrift SemiBold')
    

  


initial()


angle=[20,40,60,80,100]
def pointer():
    a=10
    
di=0
i=120
p=1*rad*2
x=Ox+rad
y=Oy+rad
p_size= int(rad/4.8) # pointer width size
pp_size = int(rad/36) # pointer tail width size
dotsize=3 # temply use

radi=math.radians(0+di+(i))
right=math.radians(0+di+(i)+90)
left=math.radians(0+di+(i)-90)

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
y2=  y+v_rsin

RR_rcos=pp_size*math.cos(right)
RR_rsin=pp_size*math.sin(right)
#cir_ptr= canvas.create_oval(x1+RR_rcos-2,y1+RR_rsin-2,x2+RR_rcos+2,y2+RR_rsin+2,fill='blue')

RL_rcos=pp_size*math.cos(left)
RL_rsin=pp_size*math.sin(left)
#cir_ptr= canvas.create_oval(x1+RL_rcos-2,y1+RL_rsin-2,x2+RL_rcos+2,y2+RL_rsin+2,fill='white')

points = [ x1+RL_rcos,y1+RL_rsin  , x1+RR_rcos,y1+RR_rsin ,  p+x+r_rcos,y+r_rsin , p+x+l_rcos,y+l_rsin ]
triangle = canvas.create_polygon(points,fill='black')
central_dot(Ox,Oy,"white")#for temp use



label_var = tk.StringVar()
label_var.set("test")
test_String = tk.Label(main_window,textvariable = label_var, bg='yellow')
test_String.place(x=350,y=220)

def clickOK():
    label_var.set(index.get())
    #circle_frame(Ox,Oy)
    #central_dot(Ox,Oy,int(index.get()))
    
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
