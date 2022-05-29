from tkinter import *
from tkinter import messagebox,filedialog,colorchooser
from PIL import ImageGrab
import time
root = Tk()
root.title("WB Paint")
menu0=Menu(root)
root.config(menu=menu0)

farbg="white"
fra = Canvas(root,width=100, height=33,bg="black")
c = Canvas(root,width=550, height=550,bg=farbg)
c.pack(fill=BOTH,expand="True")
l = Label(bg="white")
l.pack(side="right")
fra.pack(side="bottom")

def hrubka():
    global width
    width=w1.get()
def farba():
    global far
    far=str(entry2.get())

def white(event):
    global far
    far = str("white")
def grey(event):
    global far
    far = str("grey")
def brown(event):
    global far
    far = str("brown")
def black(event):
    global far
    far = str("black")
def red(event):
    global far
    far = str("red")
def khaki(event):
    global far
    far = str("khaki")
def yellow(event):
    global far
    far = str("yellow")
def green(event):
    global far
    far = str("green")
def lime(event):
    global far
    far = str("lime")
def cyan(event):
    global far
    far = str("cyan")
def navy(event):
    global far
    far = str("navy")
def blue(event):
    global far
    far = str("blue")
def plum(event):
    global far
    far = str("plum")
def purple(event):
    global far
    far = str("purple")
def pink(event):
    global far
    far = str("pink")
def gold(event):
    global far
    far = str("gold")

def vymaz():
    c.delete("all")
def rubber():
    global object
    object = "r"
def ciara():
    global object
    object = "c"
def drawings():
    global object
    object = "d"
def trojuholnik():
    global object
    object = "t"
def oval():
    global object
    object = "o"
def motion(event):
  l["text"]="x: " + str(event.x)+" y: "+str(event.y)
  return
    
def draw_line(event):
    global click_number
    global x1,y1,dr
    if object == "c":
        if click_number==0:
            x1=event.x
            y1=event.y
            click_number=1
        
        else:
            x2=event.x
            y2=event.y
            try:
                c.create_line(x1,y1,x2,y2,w=width,fill=far,smooth=TRUE)
            except TclError:
                messagebox.showerror("Invalid Color", "Color you have set is invalid!\nPlease set new one.")
            click_number=0
            dr="dy"
    if object == "t":
        if click_number==0:
            x1=event.x
            y1=event.y
            click_number=1

        elif click_number==1:
            x2=event.x
            y2=event.y
            try:
                c.create_rectangle(x1,y1,x2,y2,w=width,fill=far, outline=far)
            except TclError:
                messagebox.showerror("Invalid Color", "Color you have set is invalid!\nPlease set new one.")
            click_number=0
            dr="dy"
    if object == "o":
        if click_number==0:
            x1=event.x
            y1=event.y
            click_number=1
        elif click_number==1:
            x2=event.x
            y2=event.y
            try:
                c.create_oval(x1,y1,x2,y2,w=width, outline=far)
                print("drawing oval")
            except TclError:
                messagebox.showerror("Invalid Color", "Color you have set is invalid!\nPlease set new one.")
            click_number=0
            dr="dy"

def drawing(event):
    global dr
    if object == "d":
        x1=event.x
        y1=event.y
        try:
            c.create_oval(x1-width,y1-width,x1+width,y1+width,fill=far, outline=far)
            dr="dy"
        except TclError:
            messagebox.showerror("Invalid Color", "Color you have set is invalid!\nPlease set new one.")
     
    elif object == "r":
        x1=event.x
        y1=event.y
        c.create_oval(x1-width,y1-width,x1+width,y1+width,fill="white", outline="white")
        dr="dy"

def undo():
    items_stack = list(c.find("all"))
    try:
        last_item_id = items_stack.pop()
    except IndexError:
        return
    c.delete(last_item_id)
def undo1(event):
    items_stack = list(c.find("all"))
    try:
        last_item_id = items_stack.pop()
    except IndexError:
        return
    c.delete(last_item_id)

def getter():
    global sp
    x=root.winfo_rootx()+c.winfo_x()
    y=root.winfo_rooty()+c.winfo_y()
    x1=x+c.winfo_width()
    y1=y+c.winfo_height()
    time.sleep(0.29)
    img=ImageGrab.grab().crop((x,y,x1,y1))

    f = filedialog.asksaveasfile(filetypes=(("Portable Network Graphics (*.png)", "*.png"),
                                        ("All Files (*.*)", "*.*")),
                             mode='wb',
                             defaultextension='.png')
    print(f"Saving Directory: {f}")
    if f is None:
        return
    sp = "s"
    filename = f.name
    extension = filename.rsplit('.', 1)[-1]
    
    img.save(f, extension)
    f.close()

def color_picker():
    global far
    clr = colorchooser.askcolor(title="Select Color")
    far = clr[1]

def bg_color_picker():
    global farbg
    clr_bg = colorchooser.askcolor(title="Select Background Color")
    farbg = clr_bg[1]

def on_closing():
    if sp == "s":
        root.destroy()
    elif sp=="nots":
        if messagebox.askokcancel("File not saved!", "Do you want to quit without saving?"):
            root.destroy()
    elif dr=="dy":
        if messagebox.askokcancel("File not saved!", "Do you want to quit without saving?"):
            root.destroy()
    else:
        root.destroy()
root.protocol("WM_DELETE_WINDOW", on_closing)

subMenu=Menu(menu0)
subMenu = Menu(menu0, tearoff=0)
menu0.add_cascade(label="File",menu=subMenu)
subMenu.add_command(label="New File",command=vymaz)
subMenu.add_command(label="Save As",command=getter)
subMenu=Menu(menu0)
subMenu = Menu(menu0, tearoff=0)
menu0.add_cascade(label="Drawing Tools",menu=subMenu)
subMenu.add_command(label="Line",command=ciara)
subMenu.add_command(label="Rectangle",command=trojuholnik)
subMenu.add_command(label="Oval",command=oval)
subMenu.add_separator()
subMenu.add_command(label="Drawing",command=drawings)
subMenu.add_separator()
subMenu.add_command(label="Color Picker",command=color_picker)
subMenu.add_command(label="Backgorund Color Picker",command=bg_color_picker)
subMenu.add_command(label="Rubber",command=rubber)
subMenu=Menu(menu0)
subMenu = Menu(menu0, tearoff=0)
menu0.add_cascade(label="Edit",menu=subMenu)
subMenu.add_command(label="Undo     Shift+Z",command=undo)
subMenu.add_separator()
subMenu.add_command(label="Delete All",command=vymaz)
subMenu.add_command(label="Exit", command=root.destroy)

B = Canvas(fra,width=12,height=12,bg="black")
G = Canvas(fra,width=12,height=12,bg="grey")
Br = Canvas(fra,width=12,height=12,bg="brown")
R = Canvas(fra,width=12,height=12,bg="red")
K = Canvas(fra,width=12,height=12,bg="khaki")
Y = Canvas(fra,width=12,height=12,bg="yellow")
Gr = Canvas(fra,width=12,height=12,bg="green")
L = Canvas(fra,width=12,height=12,bg="lime")
C = Canvas(fra,width=12,height=12,bg="cyan")
N = Canvas(fra,width=12,height=12,bg="navy")
Bl = Canvas(fra,width=12,height=12,bg="blue")
P = Canvas(fra,width=12,height=12,bg="plum")
Pr = Canvas(fra,width=12,height=12,bg="purple")
Pi = Canvas(fra,width=12,height=12,bg="pink")
Wh = Canvas(fra,width=12,height=12,bg="white")
Gl = Canvas(fra,width=12,height=12,bg="gold")


B.grid(row=0,column=0)
G.grid(row=1,column=0)
Br.grid(row=0,column=1)
R.grid(row=1,column=1)
K.grid(row=0,column=2)
Y.grid(row=1,column=2)
Gr.grid(row=0,column=3)
L.grid(row=1,column=3)
C.grid(row=0,column=4)
N.grid(row=1,column=4)
Bl.grid(row=0,column=5)
P.grid(row=1,column=5)
Pr.grid(row=0,column=6)
Pi.grid(row=1,column=6)
Wh.grid(row=1,column=7)
Gl.grid(row=0,column=7)

but1 = Button(text="set width",command=hrubka)


w1=Scale(root,from_=0,to=100,orient=HORIZONTAL)
w1.pack(side="left")
but1.pack(side="left")


c.bind("<Button-1>",draw_line)
root.bind_all("<Shift-Z>",undo1)
c.bind('<B1-Motion>',drawing)
c.bind('<Motion>',motion)

B.bind("<Button-1>",black)
G.bind("<Button-1>",grey)
Br.bind("<Button-1>",brown)
R.bind("<Button-1>",red)
K.bind("<Button-1>",khaki)
Y.bind("<Button-1>",yellow)
Gr.bind("<Button-1>",green)
L.bind("<Button-1>",lime)
C.bind("<Button-1>",cyan)
N.bind("<Button-1>",navy)
Bl.bind("<Button-1>",blue)
P.bind("<Button-1>",plum)
Pr.bind("<Button-1>",purple)
Pi.bind("<Button-1>",pink)
Wh.bind("<Button-1>",white)
Gl.bind("<Button-1>",gold)


"""
photo = PhotoImage(file="filip.png")
c.create_image(0,0,image=photo,anchor=NW)
"""
click_number=0
width=2
far="black"
object="c"
sp="not"
dr="dn"
root.mainloop()
