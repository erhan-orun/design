import random
import tkinter as tk
from tkinter import ttk
from tkinter import *
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import tkinter
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
import numpy as np
from pyModbusTCP.client import ModbusClient
import pymongo
from itertools import count

L2 = ModbusClient(host="192.40.50.107", port=10010, unit_id=1, auto_open=True)

L2.open()

regs = L2.read_holding_registers(0, 100)
if regs:
    print(regs)
else:
    print("read error")

n = 0
data_count = 0

for n in range(50):
    data_count = n * 2
    regs[data_count], regs[data_count + 1] = regs[data_count + 1], regs[data_count]

dec_array = regs

print(regs)
print("----------------------------")
data_bytes = np.array(dec_array, dtype=np.uint16)
data_as_float = data_bytes.view(dtype=np.float32)

print(data_as_float)

start = 1
start_range = 50


def get_random_number():
    return random.uniform(1, 160)


value = [[num for num in range(start, start + start_range)],
         [num for num in range(start, start + start_range)],
         data_as_float]

data = np.array(value).T.tolist()
# print(data)

products = data
arr = []
for product in products:
    vals = {}
    vals["_id"] = int(product[0])
    vals["Sensor No"] = str(int(product[1]))
    vals["Temp"] = str(round(product[2], 2))
    arr.append(vals)
print(arr)

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["Modbus_Database"]

myclient.drop_database('Modbus_Database')

"""
obj_to_insert = {
    'field1': [list(arr) for arr in obj['field1']],
    'field2': list(obj['field2'])
}
"""

mycol = mydb["collection1"]

record_data = arr
data1 = mycol.insert_many(record_data)

myquery1 = {'Sensor No': '2'}

print(data1)

# for data_find in mycol.find():
#    print(data_find)
mydoc = mycol.find(myquery1)
print("----------")
for x in mydoc:
    print(x)




"""
print(myclient.list_database_names())

print(mydb.list_collection_names())
"""

"""
for x in mycol.find():
  print(x)
"""

"""
x = mycol.find_one()

print(x)
"""

root = tk.Tk()
root.title("Sensor's Temperatures °C")
root.grid()

figure1 = plt.figure()
plt.style.use('fivethirtyeight')
ax = figure1.add_subplot(1, 1, 1)  # C
xs = []
ys = []

index = count()


def animate(i, xs, ys):
    temp_c = round(get_random_number(), 2)

    # Add x and y to lists
    xs.append(next(index))
    ys.append(temp_c)

    ax.clear()
    ax.plot(xs, ys, color='blue', marker='o', markerfacecolor='red')

    plt.xticks(rotation=45, ha='right')
    plt.subplots_adjust(bottom=0.30)
    plt.title('Temperature over Time')
    plt.ylabel('Temperature °C')
    plt.xlim(1, 50)


canvas = FigureCanvasTkAgg(figure1, master=root)
canvas.draw()
canvas.get_tk_widget().pack(side=tkinter.RIGHT, fill=tkinter.BOTH, expand=1)

toolbar = NavigationToolbar2Tk(canvas, root)
toolbar.update()
canvas.get_tk_widget().pack(side=tkinter.RIGHT, fill=tkinter.BOTH, expand=1)

ani = animation.FuncAnimation(figure1, animate, fargs=(xs, ys), interval=1000)

treev = ttk.Treeview(root)

treev.pack(side='left', fill=tkinter.BOTH)

verscrlbar = ttk.Scrollbar(root,
                           orient="vertical",
                           command=treev.yview)

treev.configure(xscrollcommand=verscrlbar.set)

treev["columns"] = ("1", "2", "3")

treev['show'] = 'headings'

treev.column("1", width=40, minwidth=30, anchor='c')
treev.column("2", width=120, minwidth=30, anchor='c')
treev.column("3", width=120, minwidth=30, anchor='c')

treev.heading("1", text="ID")
treev.heading("2", text="Sensor No")
treev.heading("3", text="Temperature °C")

start_range = 0

for record in data:
    treev.insert("", index='end', iid=start_range, values=(int(record[0]), int(record[1]), record[2]))
    start_range += 1

treev = ttk.Style()
treev.configure('Treeview', rowheight=30)


def _quit():
    root.quit()
    root.destroy()


menu = Menu(root)
root.config(menu=menu)
filemenu = Menu(menu)
menu.add_cascade(label='File', menu=filemenu)
filemenu.add_command(label='New')
filemenu.add_command(label='Open...')
filemenu.add_separator()
filemenu.add_command(label='Exit', command=_quit)
helpmenu = Menu(menu)
menu.add_cascade(label='Help', menu=helpmenu)
helpmenu.add_command(label='About')

ip = Label(root, text="TCP/IP").pack(side=TOP)
e1 = Entry(root).pack(side=TOP)
host = Label(root, text=" PORT").pack(side=TOP)
e2 = Entry(root).pack(side=TOP)
submit = Button(root, text="Connect").pack(side=TOP)

root.mainloop()
