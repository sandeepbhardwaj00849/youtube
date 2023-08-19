import numpy as np
from tkinter import *
from PIL import Image, ImageTk
import os
import colorsys
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)

first_time = 1
relaunch = 0

def mouse_event(event):
    x_pointer = min_x+event.xdata*(x_range/width)
    y_pointer =(max_y-event.ydata*(y_range/height))
    
    x_min_entry.delete(0,END)
    x_max_entry.delete(0,END)
    y_max_entry.delete(0,END)
    
    x_min_entry.insert(0,str(x_pointer-x_range/10))
    x_max_entry.insert(0,str(x_pointer+x_range/10))
    y_max_entry.insert(0,str(y_pointer+y_range/10))
    draw_newton_fractal()


def reset_params():
    x_min_entry.delete(0,END)
    x_max_entry.delete(0,END)
    y_max_entry.delete(0,END)
    width_entry.delete(0,END)
    
    x_min_entry.insert(0,"-2.5")
    x_max_entry.insert(0,"2.5")
    y_max_entry.insert(0,"1.5")
    width_entry.insert(0, "300")
    draw_newton_fractal()



# defining function on which iteration process is applied
def n_function(z):
    return z**3 - complex(1,0)

# derivative of above function
def n_deriv(z):
    return 3*(z**2)

#different roots of above function
roots = [complex(1,0),complex(-0.5,np.sqrt(3)/2),complex(-0.5,-1*np.sqrt(3)/2)]

# here you can set desired value of colors you want
colors = [(255,200,50),(200,255,50),(50,50,255)]



fig, ax = plt.subplots()
fig.suptitle("Newton's fractal")
plt.subplots_adjust(left = 0, right = 1)

def draw_newton_fractal():
    global fig,ax,min_x,max_x,max_y,x_range,y_range,height,width,canvas,first_time,img,relaunch
    precision = int(precision_entry.get())
    width = int(width_entry.get())
    aspect_ratio = float(aspect_ratio_entry.get())
    height = int(width/aspect_ratio)

    min_x = float(x_min_entry.get())
    max_x = float(x_max_entry.get())
    max_y = float(y_max_entry.get())

    x_range = (max_x-min_x)
    y_range = x_range/aspect_ratio
    
    
    img = Image.new('RGB', (width,height),color = 'black')
    pixels = img.load()



    for col_no in range(width):
        for row_no in range(height):
            x = min_x+col_no*(x_range/width)
            y = -(max_y-row_no*(y_range/height))

            z0 = complex(x,y)
            for i in range(precision):
                z0 = z0 - n_function(z0)/n_deriv(z0)
                tolerance = 0.0001
                for j in range(len(roots)):
                    difference = z0 - roots[j]

                    if(abs(difference.real)<tolerance and abs(difference.imag)<tolerance):
                        pixels[col_no,row_no]=colors[j]
                        break
                    
                
    ax.clear()
    ax.imshow(img)
    ax.set_axis_off()
    cid = fig.canvas.mpl_connect('button_press_event',mouse_event)
    
    if first_time == 1:
        first_time=0
        plt.ion()
        canvas = FigureCanvasTkAgg(fig,master=root)
        canvas.get_tk_widget().place(x=500,y=80)
        toolbar = NavigationToolbar2Tk(canvas,root)
        toolbar.update()

    else:
        pass
    



def open_photo():
    img.save('mb.png')
    os.system('mb.png')


    
root=Tk()
root.geometry('1500x880')
root.title("Fractal Visualizer : Sandeep Bhardwaj")

label = Label(root, text="Fractal Visualizer - By Sandeep Bhardwaj", bd="3", font=("Times New Roman",16))
label.place(x=10,y=10)

precision_label = Label(root, text="Precision ")
precision_label.place(x=10,y=100)

precision_entry = Entry(root)
precision_entry.insert(END, "25")
precision_entry.place(x=200,y=100)

width_label = Label(root, text="Width")
width_label.place(x=10,y=140)

width_entry = Entry(root)
width_entry.insert(END, "300")
width_entry.place(x=200,y=140)

ar_label = Label(root, text="Aspect-ratio(w/h) ")
ar_label.place(x=10,y=180)

aspect_ratio_entry = Entry(root)
aspect_ratio_entry.insert(END, "1.7777")
aspect_ratio_entry.place(x=200,y=180)

x_min_label = Label(root, text="Minimum X ")
x_min_label.place(x=10,y=220)

x_min_entry = Entry(root)
x_min_entry.insert(END, "-2.5")
x_min_entry.place(x=200,y=220)

x_max_label = Label(root, text="Maximum X ")
x_max_label.place(x=10,y=260)

x_max_entry = Entry(root)
x_max_entry.insert(END, "2.5")
x_max_entry.place(x=200,y=260)


y_max_label = Label(root, text="Maximum Y ")
y_max_label.place(x=10,y=300)

y_max_entry = Entry(root)
y_max_entry.insert(END, "1.5")
y_max_entry.place(x=200,y=300)




draw_button = Button(root, text=" Draw Newton's Fractal ", width = "20", height = "1", command=draw_newton_fractal)
draw_button.place(x=20,y=630)


open_photo_button = Button(root, text=" Open Photo in App ", width = "20", height = "1", command=open_photo)
open_photo_button.place(x=270,y=630)

reset_params_button = Button(root, text=" Reset View  ", width = "20", height = "1", command=reset_params)
reset_params_button.place(x=20,y=700)

draw_newton_fractal()

root.mainloop()
