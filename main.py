import tkinter as tk
import tkinter.scrolledtext as st
from tkinter import *
from tkinter import filedialog
from tkinter import font
from tkinter import ttk
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
    popup.resizable(False, False)

    tk.Label(popup, text="Saving...").pack(expand=True)
    popup.after(1500, popup.destroy)

# change font here
def font_popup(event=None):
    if event is None:
        popup = tk.Toplevel(root)
        popup.title("Fonts")
        # make window appear on center of screen

        # Get screen size
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()

        # Count center of screen
        x = (screen_width // 2) - (250 // 2)
        y = (screen_height // 2) - (100 // 2)
        popup.geometry(f"250x100+{x}+{y}")
        popup.resizable(False, False)

        # Current text editor font
        f = font.Font(font=textEditor.cget("font"))

        # Font type
        tk.Label(popup, text="Fonts").grid(row=0, column=0,padx=5, pady=5)
        fonts = sorted(font.families())
        fontchoosen = ttk.Combobox(popup, width=27, values=fonts,font=('Tahoma',8,'normal'))
        fontchoosen.current(fonts.index(f.actual("family")))
        fontchoosen.grid(column=1, row=0)

        # Font size
        tk.Label(popup, text="Size").grid(row=1, column=0, padx=5, pady=5)
        fontsize = tk.Text(popup, height=1, width=30, font=('Tahoma',8,'normal'))
        fontsize.insert('0.0', str(f.actual("size")))
        fontsize.grid(column=1, row=1)

        # Button
        (tk.Button(popup, text="Change", command=lambda :[textEditor.configure(
            font = tk.font.Font(family=fontchoosen.get(), size=int(fontsize.get('1.0',tk.END)), weight="normal")),popup.destroy()])
                     .grid(row=2, column=0, columnspan=2, pady=5))
    else:
        if event.keysym == "equal":
            f = font.Font(font=textEditor.cget("font"))
            fontsize = int(f.actual("size"))+1
            textEditor.configure(font=tk.font.Font(family=f.actual("family"), size=int(fontsize)))
        else:
            f = font.Font(font=textEditor.cget("font"))
            fontsize = int(f.actual("size")) - 1
            textEditor.configure(font=tk.font.Font(family=f.actual("family"), size=int(fontsize)))
# Status bar
def update_status(event=None):
    current_font = font.Font(font=textEditor.cget("font"))
    line, col = textEditor.index("insert").split(".")
    status.config(
        text=f"Ln {line}, Col {col} | {current_font.actual("family")} {current_font.actual("size")} "
    )
def poll_cursor():
    update_status()
    root.after(100, poll_cursor)




#save and open
def closeWindow():
    if len(textEditor.get('0.0', tk.END)) > 1:
        title = root.title().split()[2]
        if title != 'New':
            f = open(title)
            if textEditor.get('0.0', tk.END) == f.read():
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
def save(event=None):
    if root.title().split()[2] == 'New':
        filename = filedialog.asksaveasfile(initialfile='Untitled.txt',
                              defaultextension=".txt", filetypes=[("All Files", "*.*"),
                            ("Text Documents", "*.txt")])
        if filename:
            save_popup()
            with open(filename.name, "a") as f:
                f.write(textEditor.get('0.0', tk.END))
            root.title("Text Editor "+str(filename.name))
        else:
            # do nothing
            pass
    else:
        save_popup()
        with open(root.title().split()[2], "w") as f:
            f.write(textEditor.get('0.0', tk.END))
        root.title("Text Editor "+str(root.title().split()[2]))
def load(event=None):
    if len(textEditor.get('0.0', tk.END)) > 1:
        title = root.title().split()[2]
        if title != 'New':
            f = open(title)
            if textEditor.get('0.0', tk.END) == f.read():
                textEditor.delete('0.0', tk.END)
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
                    textEditor.delete('0.0', tk.END)
                    filename = filedialog.askopenfilename(initialdir="/",
                                                          title="Select a File",
                                                          filetypes=(("Text files",
                                                                      "*.*"),
                                                                     ("all files",
                                                                      "*.*")))
                    fileOpen = open(filename)
                    root.title("Text Editor " + fileOpen.name)
                    textEditor.insert(tk.END, fileOpen.read())
                else:
                    save()
                    textEditor.delete('0.0', tk.END)
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
                textEditor.delete('0.0', tk.END)
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
                textEditor.delete('0.0', tk.END)
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
        textEditor.delete('0.0', tk.END)
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
# File here
file = Menu(menubar, tearoff = 0)
menubar.add_cascade(label ='File', menu = file)
file.add_command(label ='Open...', command = load)
file.add_command(label ='Save', command = save)
# Edit here
edit = Menu(menubar, tearoff = 0)
menubar.add_cascade(label ='Edit', menu = edit)
edit.add_command(label ='Fonts', command = font_popup)

root.config(menu = menubar)

#body session
body = tk.Frame(root)
textEditor = st.ScrolledText(body)
textEditor.configure(font = tk.font.Font(family="Arial", size=14, weight="normal"))
textEditor.pack(fill="both",expand=True)
body.pack(fill="both",expand=True)
body.pack_propagate(False)


# Footer session
footer = tk.Frame(root)
tk.Label(footer, text = "Text Editor 1.0").pack(side = tk.LEFT)
status = tk.Label(footer, text = textEditor.index("insert"))
status.pack(side = tk.RIGHT)
footer.pack(fill="x", side=tk.BOTTOM)

#window event

# save project shortcut
root.bind("<Control-s>",save)
# zoom in & out text editor shortcut
root.bind("<Control-=>",font_popup)
root.bind("<Control-_>",font_popup)
# open file
root.bind("<Control-o>",load)

root.protocol("WM_DELETE_WINDOW",closeWindow)
# status bar function
poll_cursor()
root.mainloop()
