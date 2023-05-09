import tkinter

window = tkinter.Tk()
window.geometry("500x500")
window.config(background="Pink")
window.title("👩🏼‍💻")

label = tkinter.Label(text="This is a text for experimental usage.")
label.config(background="dark blue",foreground="#DEFE28")
label.pack(side="top")

def click_button():
    userInput = entry.get()
    print(userInput)

button = tkinter.Button(text="This is a button", command=click_button)
button.pack()
# button.place(x=0, y=0)
# button.grid(row=0, column=0)

entry = tkinter.Entry(width=20)
entry.pack()
window.mainloop()