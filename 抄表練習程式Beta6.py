import tkinter as tk
from tkinter import *
import math,random
main_window=tk.Tk()
#main_window.attributes("-alpha",0.8)
canvas = tk.Canvas(main_window, bg='skyblue',  width=800,height=200)
Ox=40#表燈起始座標
Oy=40
rad=72#表燈半徑
cw=[270,306,342,18,54,90,126,162,198,234] #順時鐘角度
ucw=[270,234,198,162,126,90,54,18,342,306]#逆時鐘角度
pc=[0,1,2,3,4,5,6,7,8,9] #PC 數字鍵盤
hc=[0,7,8,9,4,5,6,1,2,3] #HC 數字鍵盤
setting=[True,True,False,True] #預設值
        #數字 刻度 PC鍵 字體

default=3 #個位數 指數比例 0~9

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
def circle_num():
    font_size ,num_position = int(rad/3) ,int(rad/4.5)
    if (setting[3]):
        font_type="Arial Black"
    else:
        font_type="Bahnschrift SemiBold"
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
# def 中心點+中心圓圈
def central_dot(Ox,Oy,color):
    dot_size=int(rad/24)
    cir_size = int(rad/3.6)
    x=Ox+rad
    y=Oy+rad
    for i in range(5):
        p = i*rad*2
        cir = canvas.create_oval(x-cir_size+p,y-cir_size,x+cir_size+p,y+cir_size,fill='black')
        cen = canvas.create_oval(x-dot_size+p,y-dot_size,x+dot_size+p,y+dot_size,fill=color)

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
    main_window.title("台灣電力公司 TAI POWER - 抄 表 練 習 程 式 V1.0")
    main_window.geometry('800x300')
    label = tk.Label(main_window,text="抄 表 練 習 程 式 v1.0",bg = 'yellow',font=('Arial Black',15)).place(x=0,y=0)
    #label = canvas.create_text(180,20,text="抄 表 練 習 程 式 Beta6",font=('Arial Black',20))
    circle_frame(Ox,Oy)
    central_dot(Ox,Oy,"white")
    if setting[1]:circle_ptr()
    if setting[0]:circle_num()
    #circle_num('Bahnschrift SemiBold')
    canvas.pack()

def clear(): #清除表燈
    circle_frame(Ox,Oy)
    central_dot(Ox,Oy,"white")
    if setting[1]:circle_ptr()
    if setting[0]:circle_num()

initial()


def setor_ptr(): #是否顯示刻度
    if(setting[1]):
        setting[1]=False;
    else:
        setting[1]=True;
    initial()

def setor_num(): #是否顯示數字
    if(setting[0]):
        setting[0]=False;
    else:
        setting[0]=True;
    initial()

def setor_font(): #切換字型
    if(setting[3]):
        setting[3]=False;
    else:
        setting[3]=True;
    initial()

def setor_HCkeymode(): #切換HC鍵盤
    if(setting[2]):
        setting[2]=False;
    else:
        setting[2]=True;
    initial()

def switch_HC(index): #HC 鍵盤模擬器
    for i in range(5):
        index[i]=hc[int(index[i])];
    return index

ans = [0,0,0,0,0]    #答案 初始化
index2 = [0,0,0,0,0] #題目 初始化

def start(): #開始出題
    clear()
    b=random.randint(0,99999)
    b=str(b).zfill(5)
    a=list(b)
    for i in range(5):
        index2[i]=int(a[i])
    pointer(inx(index2))
    print(index2,"題目")


def check(event): #檢查指數
    input_index=(text_box.get())
    label_var.set(input_index)
    if(setting[2]):label_var.set(switch_HC(list(str(input_index))))
    b=list(str(input_index))
    if(setting[2]):b=switch_HC(b)
    for i in range(5):
        ans[i]=int(b[i])
    print(ans,"你的答案")
    if(ans==index2):
        show_String = tk.Label(main_window,textvariable = label_var, bg='lightGreen')
        print("collect")
        start()
    else:
        show_String = tk.Label(main_window,textvariable = label_var, bg='red')
        print("wrong")
    show_String.place(x=350,y=220)
    text_box.delete(0,10)


label_var = tk.StringVar()
label_var.set("<---按下Start 開始!  輸入指數後 請按ENTER!")
show_String = tk.Label(main_window,textvariable = label_var, bg='lightGreen')
show_String.place(x=350,y=220)

start_btn = tk.Button(main_window,text="START",command=start)
main_window.bind('<Return>', check)
text_box = tk.Entry(main_window,width=5)
text_box.place(x=350,y=240)
start_btn.place(x=280,y=220)

ptr_chkbox=Checkbutton(main_window, text="不顯示刻度", command = setor_ptr ).place(x=60,y=210)
num_chkbox=Checkbutton(main_window, text="不顯示數字", command = setor_num ).place(x=60,y=240)
HC_chkbox=Checkbutton(main_window, text="模擬HC數字鍵盤", command = setor_HCkeymode ).place(x=60,y=270)
font_chkbox=Checkbutton(main_window, text="Arial Black/Bahnschrift SemiBold", command = setor_font ).place(x=180,y=270)

main_window.resizable(0,0)
main_window.mainloop()
