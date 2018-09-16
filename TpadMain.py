from tkinter import *
from tkinter.filedialog import askopenfilename, asksaveasfile
import tkinter.messagebox

def readFile(filename):
    fr = open(filename,"r")
    text = fr.read()
    return text


def openFile():
    try:
        filedata = askopenfilename(filetypes=(("Text File","*.txt"),("All Files","*")),title="Select a file")
        if filedata !='':
            text = readFile(filedata)
            textdisplay.insert(END, text)
            status.config(text=filedata+" Has Opened")
    except:
        tkinter.messagebox.showerror("Error","Unsupported Format")



def saveFiles():
    savefile = asksaveasfile(mode="w", defaultextension=".txt")
    savetext = str(textdisplay.get(0.0,END))
    savefile.write(savetext)
    savefile.close()
    status.config(text="File Saved")


def create_window():
    root = Tk()
    root.title("Tpad")
    root.geometry("500x600")

    menu = Menu(root)
    root.config(menu=menu)

    filemenu = Menu(menu)
    menu.add_cascade(label="File", menu=filemenu)
    filemenu.add_command(label="New...", command=create_window)
    filemenu.add_command(label="Open...", command=openFile)
    filemenu.add_command(label="Save...", command=saveFiles)
    filemenu.add_separator()
    filemenu.add_command(label="Exit", command=root.quit)

    textdisplay = Text(root)
    textdisplay.pack(fill=BOTH, expand=1)

    status = Label(root,text="status",relief=SUNKEN, anchor=W)
    status.pack(fill = X,side=BOTTOM, padx=1)

    root.mainloop()



root = Tk()
root.title("Tpad")
root.geometry("500x600")

menu = Menu(root)
root.config(menu=menu)

filemenu = Menu(menu)
menu.add_cascade(label="File", menu=filemenu)
filemenu.add_command(label="New...", command=create_window)
filemenu.add_command(label="Open...", command=openFile)
filemenu.add_command(label="Save...", command=saveFiles)
filemenu.add_separator()
filemenu.add_command(label="Exit",command=root.quit)

textdisplay = Text(root)
textdisplay.pack(fill=BOTH, expand=1)

status = Label(root,text="status",relief=SUNKEN, anchor=W)
status.pack(fill = X,side=BOTTOM, padx=1)

root.mainloop()
