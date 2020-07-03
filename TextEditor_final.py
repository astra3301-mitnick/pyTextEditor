from tkinter import *
from tkinter import filedialog,simpledialog
from tkinter.scrolledtext import ScrolledText
from tkinter import messagebox
from tkinter.ttk import *
import tkinter.messagebox
import re

root = Tk()
root.title('TEXT EDITOR')

textEditor = ScrolledText(root, width=100, height=50)
filename = ""

def newFile():
    global filename
    if len(textEditor.get('1.0', END+'-1c'))>0:
        if messagebox.askyesno("SAVE" ,"Do you wanna save this file?"):
            saveFile()
        else:
            textEditor.delete(0.0, END)
    root.title("TEXT EDITOR")

def saveFile():
    f = filedialog.asksaveasfile(mode='w', defaultextention='.txt')
    if f!= None:
        data = textEditor.get('1.0', END)
    try:
        f.write(data)
    except:
        messagebox.showerror(title="Oops!!", message="Unable to save this  file!")

def saveAs():
    f = filedialog.asksaveasfile(mode='w',defaultextension='.txt') 
    t = textEditor.get(0.0, END)
    try:
        f.write(t.rstrip())
    except:
        messagebox.showerror(title="Oops!!", message="Unable to save file!")

def openFile():
    f = filedialog.askopenfile(parent=root, mode='r')
    t = f.read()
    textEditor.delete(0.0, END)
    textEditor.insert(0.0, t)

def about():
    label = messagebox.showinfo("About", "Jus another textEditor \n All copyrights to Rahul reserved!")

def randomDopeClicks(event):
    textEditor.tag_config('Found', background='white', foreground='grey')

def find_text():
    textEditor.tag_remove('Found' , '1.0', END)
    find = simpledialog.askstring("Find", "Enter Text:")
    if find:
        idx = '1.0'
    while 1:
        idx = textEditor.search(find, idx, nocase=1,stopindex=END)
        if not idx:
            break
        lastidx = '%s+%dc' % (idx, len(find))
        textEditor.tag_add('Found', idx, lastidx)
        idx = lastidx
    textEditor.tag_config('Found', foreground='white', background='black')
    textEditor.bind("<1>", randomDopeClicks)

    t = textEditor.get('1.0', END)
    occurance = t.upper().count(find.upper())

    if occurance > 0:
        label = messagebox.showinfo("Find", find +"  has multiple occurances:" +  str(occurance))
    else:
        label = messagebox.showinfo("Find", "No Results")

def view_text():
    label = messagebox.showinfo("Text", "Welcome to text editor")

def exit():


#creating menu
    tkinter.messagebox.showinfo("Windows Error", "Are you sure wanna exit?")
    answer = tkinter.messagebox.askquestion("Exit ", "Do you still wish to exit without saving?")
    if answer == "yes":
        root.destroy()
    else:
        saveAs()
MainMenu = Menu(root)
root.config(menu=MainMenu)

mainFile = Menu(MainMenu)
MainMenu.add_cascade(label='File', menu=mainFile)
mainFile.add_command(label='New Doc', command=newFile)
mainFile.add_command(label='Open', command=openFile)
mainFile.add_command(label='Save', command=saveFile)
mainFile.add_command(label='Save As...', command=saveAs)
mainFile.add_separator()
mainFile.add_command(label='Exit', command=exit)

edit = Menu(MainMenu)
MainMenu.add_cascade(label='Edit', menu=edit)
edit.add_command(label='Undo')
edit.add_command(label='Redo')
edit.add_command(label='Cut')
edit.add_command(label='Copy')
edit.add_command(label='Paste')

mainView = Menu(MainMenu)
MainMenu.add_cascade(label='View', menu=mainView)
mainView.add_command(label='Text', command=view_text)


findCase = Menu(MainMenu)
MainMenu.add_cascade(label='Find', menu=findCase)
findCase.add_command(label='Find', command=find_text)

about = Menu(MainMenu)
MainMenu.add_cascade(label='About', menu=about)
about.add_command(label='About', command=about)




#adding icons

frame1=Frame(root)
frame1.pack()
Image1 = PhotoImage(file='new_file.gif')
l1 = Label(frame1, text='New file')
b1 = Button(frame1, image=Image1, command=newFile)
b1.grid(row=0, column=0)
l1.grid(row=1, column=0)
Image2 = PhotoImage(file='open_file.gif')
b2 = Button(frame1, image=Image2, command=openFile)
l2 = Label(frame1, text='Open file')
b2.grid(row=0, column=1)
l2.grid(row=1, column=1)
Image5 = PhotoImage(file='save.gif')
b5 = Button(frame1, image=Image5, command=saveAs)
l5 = Label(frame1, text='Save')
b5.grid(row=0, column=2)
l5.grid(row=1, column=2)
Image6 = PhotoImage(file='about.gif')
b6 = Button(frame1, image=Image6, command=about)
l6 = Label(frame1, text='About')
b6.grid(row=0, column=3)
l6.grid(row=1, column=3)
Image7 = PhotoImage(file='find_text.gif')
b7 = Button(frame1, image=Image7, command=find_text)
l7 = Label(frame1, text='Find text')
b7.grid(row=0, column=4)
l7.grid(row=1, column=4)

textEditor.pack()
root.mainloop()