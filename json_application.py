import json
import os
from tkinter import *
from tkinter import filedialog
from tkinter import ttk
dir_path = os.path.dirname(os.path.realpath(__file__))
arr = []
arr_pd = []
arr_name = []
arr_all_name = []
def openfile():
    filename = filedialog.askopenfilenames(initialdir="/", title="Open File", filetypes=(("JSON files", "*.json"), ("All files", "*.*")))
    arr.append(filename)

def show_1():
    arr_pd.append(e1.get())
    arr_name.append(e2.get())
    arr_all_name.append(e3.get())
    # with open(dir_path + '/last.json', 'w', encoding='utf8') as json_f:
    #     json.dump(print_info(find_key(e1.get())), json_f, ensure_ascii=False)

master = Tk()
master.geometry("500x250")

rows = 0
while rows < 50:
    master.rowconfigure(rows, weight=1)
    master.columnconfigure(rows, weight=1)
    rows += 1
nb=ttk.Notebook(master)
nb.grid(row=1, column=0, columnspan=50, rowspan=49, sticky='NESW')
main_page = ttk.Frame(nb)
nb.add(main_page, text='Main')
page1 = ttk.Frame(nb)
nb.add(page1, text='Tab1')
page2 = ttk.Frame(nb)
nb.add(page2, text='Tab2')
m_l = Label(main_page, text = "To work with all files go to Tab1.\n\nTo work with the specified one go to Tab2")
m_l.config(font=("Courier", 14))
m_l.place(x=5, y=50)
b1 = Button(page1, text = "Show_path", command = openfile)
b1.place(x=5, y=65)
b1.config(height= 1, width=20)
l1 = Label(page2, text="Number of the Voting:")
# l1.pack(side=LEFT)
l1.place(x=5, y=60)
e1= Entry(page2, bd=5)
# e1.pack(side=RIGHT)
e1.place(x=205.6, y=60)
b2 = Button(page2, text = "Show", command = show_1)
b2.place(x=5, y=100)
b2.config(height= 1, width=20)
l2 = Label(page2, text="Please name the file of chosen json:")
# l2.pack(side = LEFT)
l2.place(x=5, y=21)
e2 = Entry(page2, bd=5)
# e2.pack(side=RIGHT)
e2.place(x=205.5, y=21)
l3 = Label(page1, text="Please name the file of all data:")
# l3.pack(side=LEFT)
l3.place(x=5, y = 21)
e3 = Entry(page1, bd=5)
# e3.pack(side=RIGHT)
e3.place(x=205.5, y=21)
# print(openfile())


master.mainloop()
arr = list(arr[0][i : i+1] for i in range(0, len(arr[0])))
# for i in range(len(arr)):
# print (arr[i][0])
def collect_all_data(arr):
    arr_fin = []
    for i in range(len(arr)):
        with open(arr[i][0], encoding='utf-8') as f:
            data = json.loads(f.read())
            data = [data]
            arr_fin.append(data)
    return arr_fin

# print(collect_all_data(arr))

with open(dir_path + '/' + arr_all_name[0] + '.json', 'w', encoding='utf8') as json_f:
    json.dump(collect_all_data(arr), json_f, ensure_ascii=False)


with open(dir_path + '/' + arr_all_name[0] + '.json', encoding='utf-8') as data_file:
    data = json.loads(data_file.read())

def find_key(val):
    for i in range(len(data)):
        if (data[i][0]["PD_NPP"] == str(val)):
            return i

def print_info(ind):
    return data[ind][0]

with open(dir_path + '/' + arr_name[0] +'.json', 'w', encoding='utf8') as json_f:
    json.dump(print_info(find_key(arr_pd[0])), json_f, ensure_ascii=False)