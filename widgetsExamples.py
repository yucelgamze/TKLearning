from tkinter import *

window = Tk()
window.geometry("600x800")
window.config(background="Pink")
window.title("👩🏼‍💻")


label = Label(text="This is a text for experimental usage.")
label.config(background="dark blue",foreground="#DEFE28")
label.pack(side="top")


def clicked_button(row,column):
    print("Row: {}".format(row), " Column:{}".format(column))


buttons = [[0, 0, 0],
           [0, 0, 0],
           [0, 0, 0]]

frame = Frame(window)
frame.pack()

for row in range(3):
    for column in range(3):
        buttons[row][column] = Button(frame, text= "", highlightbackground='#FA006E', font=('didot',40),
                                     width=5, height=2, command=lambda row=row, column=column : clicked_button(row,column))
        buttons[row][column].grid(row=row, column=column)


def scale_selected(value):
    print(value)
scale = Scale(from_=0,to=10,command=scale_selected)
scale.pack(side="bottom")

def spinbox_selected():
    print(spinbox.get())
spinbox =Spinbox(from_=0, to=20,command=spinbox_selected)
spinbox.pack(side="bottom")

def checkbutton_selected():
    print(check_state.get())
check_state = IntVar()
checkbutton = Checkbutton(text="just checking...",variable=check_state, command=checkbutton_selected)
checkbutton.pack(side="bottom")

def radio_selected():
    print(radioButtonVar.get())
radioButtonVar = IntVar()
radioButton = Radiobutton(text="1. option", value=10, variable=radioButtonVar,command=radio_selected, bg="DeepPink")
radioButton2 = Radiobutton(text="2. option", value=20, variable=radioButtonVar,command=radio_selected, bg="DeepPink")
radioButton3 = Radiobutton(text="3. option", value=30, variable=radioButtonVar,command=radio_selected, bg="DeepPink")
radioButton.pack()
radioButton2.pack()
radioButton3.pack()

def listbox_selected(event):
    print(listBox.get(listBox.curselection()))
listBox = Listbox()
name_list = ["Jenniffer", "Emma", "Dana", "Jake", "John"]
for i in range(len(name_list)):
    listBox.insert(i, name_list[i])
listBox.pack()
listBox.bind('<<ListboxSelect>>',listbox_selected)
window.mainloop()