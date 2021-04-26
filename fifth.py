import string
import tkinter as tk
from tkinter import ttk
from tkinter import *
from pandas import DataFrame
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import random
from itertools import count
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

'''
from pyModbusTCP.client import ModbusClient

c = ModbusClient(host="192.40.50.107", port=10010, unit_id=1, auto_open=True)

c.open()

regs = c.read_holding_registers(0, 10)
if regs:
    print(regs)
else:
    print("read error")
'''


def get_random_number():
    return random.uniform(1, 180)


def get_random_string(length):
    result_str = ''.join(random.choice(string.ascii_letters) for i in range(length))
    return result_str


data = [
    [1, get_random_string(3), round(get_random_number(), 2)],
    [2, get_random_string(3), round(get_random_number(), 2)],
    [3, get_random_string(3), round(get_random_number(), 2)],
    [4, get_random_string(3), round(get_random_number(), 2)],
    [5, get_random_string(3), round(get_random_number(), 2)],
    [6, get_random_string(3), round(get_random_number(), 2)],
    [7, get_random_string(3), round(get_random_number(), 2)],
    [8, get_random_string(3), round(get_random_number(), 2)],
    [9, get_random_string(3), round(get_random_number(), 2)],
    [10, get_random_string(3), round(get_random_number(), 2)],
    [11, get_random_string(3), round(get_random_number(), 2)],
    [12, get_random_string(3), round(get_random_number(), 2)],
    [13, get_random_string(3), round(get_random_number(), 2)],
    [14, get_random_string(3), round(get_random_number(), 2)],
    [15, get_random_string(3), round(get_random_number(), 2)],
]

data1 = {'Machine': [data[0][1], data[1][1], data[2][1], data[3][1], data[4][1], data[5][1], data[6][1], data[7][1],
                     data[8][1], data[9][1], data[10][1], data[11][1], data[12][1], data[13][1], data[14][1]],
         'Temperature': [data[0][2], data[1][2], data[2][2], data[3][2], data[4][2], data[5][2], data[6][2], data[7][2],
                         data[8][2], data[9][2], data[10][2], data[11][2], data[12][2], data[13][2], data[14][2]]
         }
df1 = DataFrame(data1, columns=['Machine', 'Temperature'])

data2 = {'Machine': [data[0][1], data[1][1], data[2][1], data[3][1], data[4][1], data[5][1], data[6][1], data[7][1],
                     data[8][1], data[9][1], data[10][1], data[11][1], data[12][1], data[13][1], data[14][1]],
         'Temperature': [data[0][2], data[1][2], data[2][2], data[3][2], data[4][2], data[5][2], data[6][2], data[7][2],
                         data[8][2], data[9][2], data[10][2], data[11][2], data[12][2], data[13][2], data[14][2]]
         }
df2 = DataFrame(data2, columns=['Machine', 'Temperature'])

root = tk.Tk()
root.title("Machine's Temperatures")
root.grid()
# root.geometry("1200x1200")

plt.style.use('fivethirtyeight')

x_vals = []
y_vals = []

index = count()


def animate(i):
    x_vals.append(get_random_string(3))
    y_vals.append(round(get_random_number(), 2))

    plt.plot(x_vals, y_vals)


ani = FuncAnimation(plt.gcf(), animate, interval=1000)

plt.tight_layout()
plt.show()

menu = Menu(root)
root.config(menu=menu)
filemenu = Menu(menu)
menu.add_cascade(label='File', menu=filemenu)
filemenu.add_command(label='New')
filemenu.add_command(label='Open...')
filemenu.add_separator()
filemenu.add_command(label='Exit', command=root.quit)
helpmenu = Menu(menu)
menu.add_cascade(label='Help', menu=helpmenu)
helpmenu.add_command(label='About')

w = Label(root, text="Machine's Temperatures")
w.grid(row=13, column=0)

# Creating tkinter window

# root.resizable(width=1, height=1)

# Using treeview widget
# treev = ttk.Treeview(root, selectmode='browse')
treev = ttk.Treeview(root)

# Calling pack method w.r.to treeview
treev.grid(row=14, column=0)

# Constructing vertical scrollbar
# with treeview
verscrlbar = ttk.Scrollbar(root,
                           orient="vertical",
                           command=treev.yview)

# Calling pack method w.r.to verical
# scrollbar
verscrlbar.grid(row=14, column=1)

# Configuring treeview
treev.configure(xscrollcommand=verscrlbar.set)

# Defining number of columns
treev["columns"] = ("1", "2", "3")

# Defining heading
treev['show'] = 'headings'

# Assigning the width and anchor to  the
# respective columns
treev.column("1", width=60, minwidth=40, anchor='c')
treev.column("2", width=160, minwidth=40, anchor='c')
treev.column("3", width=160, minwidth=40, anchor='c')

# Assigning the heading names to the
# respective columns
treev.heading("1", text="ID")
treev.heading("2", text="Machine")
treev.heading("3", text="Temperature")

count = 0
for record in data:
    treev.insert("", index='end', iid=count, values=(record[0], record[1], record[2]))
    count += 1

treev = ttk.Style()
treev.configure('Treeview', rowheight=40)

v = IntVar()
w = Label(root, text=" -Master/Slave- ")
w.grid(row=0, column=0)
Radiobutton(root, text='Master', variable=v, value=1).grid(row=1, column=0)
Radiobutton(root, text='Slave', variable=v, value=2).grid(row=2, column=0)

Label(root, text='Poll Time').grid(row=3)
Label(root, text='Response Time').grid(row=5)
e1 = Entry(root)
e2 = Entry(root)
e1.grid(row=4, column=0)
e2.grid(row=6, column=0)

w = Label(root, text=" -Communications Mode- ")
w.grid(row=0, column=9)

Radiobutton(root, text='ASCII         ', variable=v, value=3).grid(row=1, column=9)
Radiobutton(root, text='Binary/RTU', variable=v, value=4).grid(row=2, column=9)

Radiobutton(root, text='TCP/IP     ', variable=v, value=5).grid(row=9, column=9)

Label(root, text='COM Port').grid(row=3, column=9)
w = Spinbox(root, from_=0, to=10)
w.grid(row=3, column=10)
Label(root, text='BaudRate').grid(row=4, column=9)
w = Spinbox(root, from_=0, to=10)
w.grid(row=4, column=10)
Label(root, text='Data Bits').grid(row=5, column=9)
w = Spinbox(root, from_=0, to=10)
w.grid(row=5, column=10)
Label(root, text='Parity').grid(row=6, column=9)
w = Spinbox(root, from_=0, to=10)
w.grid(row=6, column=10)
Label(root, text='Stop Bits').grid(row=7, column=9)
w = Spinbox(root, from_=0, to=10)
w.grid(row=7, column=10)

Label(root, text='IP Address').grid(row=10, column=9)
Label(root, text='Port').grid(row=11, column=9)
e3 = Entry(root)
e4 = Entry(root)
e3.grid(row=10, column=10)
e4.grid(row=11, column=10)

w = Label(root, text=" -ModBus- ")
w.grid(row=0, column=11)

w = Label(root, text="    Address")
w.grid(row=1, column=11)

Radiobutton(root, text='', variable=v, value=6).grid(row=2, column=11)
Radiobutton(root, text='', variable=v, value=7).grid(row=3, column=11)
Radiobutton(root, text='', variable=v, value=8).grid(row=4, column=11)
Radiobutton(root, text='', variable=v, value=9).grid(row=5, column=11)
Radiobutton(root, text='', variable=v, value=10).grid(row=6, column=11)

e5 = Entry(root)
e6 = Entry(root)
e7 = Entry(root)
e8 = Entry(root)
e9 = Entry(root)
e5.grid(row=2, column=12)
e6.grid(row=3, column=12)
e7.grid(row=4, column=12)
e8.grid(row=5, column=12)
e9.grid(row=6, column=12)

var1 = IntVar()
Checkbutton(root, text='Function 6 For Single Registers', variable=var1).grid(row=9, column=11)

"""
c = ModbusClient(host="192.40.50.107", port=10010, unit_id=1, auto_open=True)

c.open()

regs = c.read_holding_registers(0, 2)
if regs:
    print(regs)
else:
    print("read error")
"""

root.mainloop()
