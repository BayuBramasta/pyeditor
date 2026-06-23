import tkinter as tk
from tkinter import *
from tkinter import filedialog
from tkinter.messagebox import *


#Pop up & something
def save_popup():
    popup = tk.Toplevel(root)
    popup.title("Info")
    # make window appear on center of screen

    # Get screen size
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    # Count center of screen
    x = (screen_width // 2) - (250 // 2)
    y = (screen_height // 2) - (100 // 2)
    popup.geometry(f"250x100+{x}+{y}")

    tk.Label(popup, text="Saving...").pack(expand=True)
    popup.after(1500, popup.destroy)

#save and open
def closeWindow():
    if len(textEditor.get('1.0', tk.END)) > 1:
        title = root.title().split()[2]
        if title != 'New':
            f = open(title)
            if textEditor.get('1.0', tk.END) == f.read():
                root.destroy()
            else:
                alert = askyesno('Warning', "Are you sure?")
                if alert:
                    root.destroy()
                else:
                    save()
        else:
            alert = askyesno('Warning', "Are you sure?")
            if alert:
                root.destroy()
            else:
                save()
    else:
        root.destroy()
def save():
    if root.title().split()[2] == 'New':
        filename = filedialog.asksaveasfile(initialfile='Untitled.txt',
                              defaultextension=".txt", filetypes=[("All Files", "*.*"),
                            ("Text Documents", "*.txt")])
        save_popup()
        with open(filename.name, "a") as f:
            f.write(textEditor.get('1.0', tk.END))
        root.title("Text Editor "+str(filename.name))
    else:
        save_popup()
        with open(root.title().split()[2], "w") as f:
            f.write(textEditor.get('1.0', tk.END))
        root.title("Text Editor "+str(root.title().split()[2]))
def load():
    if len(textEditor.get('1.0', tk.END)) > 1:
        title = root.title().split()[2]
        if title != 'New':
            f = open(title)
            if textEditor.get('1.0', tk.END) == f.read():
                textEditor.delete('1.0', tk.END)
                filename = filedialog.askopenfilename(initialdir="/",
                                                      title="Select a File",
                                                      filetypes=(("Text files",
                                                                  "*.txt*"),
                                                                 ("all files",
                                                                  "*.*")))
                fileOpen = open(filename)
                root.title("Text Editor " + fileOpen.name)
                textEditor.insert(tk.END, fileOpen.read())
            else:
                alert = askyesno('Warning', "Are you sure?")
                if alert:
                    textEditor.delete('1.0', tk.END)
                    filename = filedialog.askopenfilename(initialdir="/",
                                                          title="Select a File",
                                                          filetypes=(("Text files",
                                                                      "*.txt*"),
                                                                     ("all files",
                                                                      "*.*")))
                    fileOpen = open(filename)
                    root.title("Text Editor " + fileOpen.name)
                    textEditor.insert(tk.END, fileOpen.read())
                else:
                    save()
                    textEditor.delete('1.0', tk.END)
                    filename = filedialog.askopenfilename(initialdir="/",
                                                          title="Select a File",
                                                          filetypes=(("Text files",
                                                                      "*.txt*"),
                                                                     ("all files",
                                                                      "*.*")))
                    fileOpen = open(filename)
                    root.title("Text Editor " + fileOpen.name)
                    textEditor.insert(tk.END, fileOpen.read())
        else:
            alert = askyesno('Warning', "Are you sure?")
            if alert:
                textEditor.delete('1.0', tk.END)
                filename = filedialog.askopenfilename(initialdir="/",
                                                      title="Select a File",
                                                      filetypes=(("Text files",
                                                                  "*.txt*"),
                                                                 ("all files",
                                                                  "*.*")))
                fileOpen = open(filename)
                root.title("Text Editor " + fileOpen.name)
                textEditor.insert(tk.END, fileOpen.read())
            else:
                save()
                textEditor.delete('1.0', tk.END)
                filename = filedialog.askopenfilename(initialdir="/",
                                                      title="Select a File",
                                                      filetypes=(("Text files",
                                                                  "*.txt*"),
                                                                 ("all files",
                                                                  "*.*")))
                fileOpen = open(filename)
                root.title("Text Editor " + fileOpen.name)
                textEditor.insert(tk.END, fileOpen.read())
    else:
        textEditor.delete('1.0', tk.END)
        filename = filedialog.askopenfilename(initialdir="/",
                                              title="Select a File",
                                              filetypes=(("Text files",
                                                          "*.txt*"),
                                                         ("all files",
                                                          "*.*")))
        fileOpen = open(filename)
        root.title("Text Editor " + fileOpen.name)
        textEditor.insert(tk.END, fileOpen.read())


#initialize window
root = tk.Tk()
root.title("Text Editor New Files")
# make window appear on center of screen

# Get screen size
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# Count center of screen
x = (screen_width // 2) - (1200 // 2)
y = (screen_height // 2) - (600 // 2)


root.geometry(f"1200x600+{x}+{y}")

#define frame

# Menubar
menubar = Menu(root)
file = Menu(menubar, tearoff = 0)
menubar.add_cascade(label ='File', menu = file)
file.add_command(label ='Open...', command = load)
file.add_command(label ='Save', command = save)
root.config(menu = menubar)

#body session
body = tk.Frame(root)
textEditor = tk.Text(body)
textEditor.pack(fill="both",expand=True)
body.pack(fill="both",expand=True)

#window event
root.protocol("WM_DELETE_WINDOW",closeWindow)
root.mainloop()

