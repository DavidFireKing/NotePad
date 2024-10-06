import tkinter as tk
import tkinter.filedialog as fd
import tkinter.messagebox as tkm

from pyexpat.errors import messages

window = tk.Tk()
window.title("NotePad")
window.geometry("400x400")
window.iconbitmap("resource/Notepad.ico")

content_text = tk.Text(window, wrap="word", bg="black", fg="white")
content_text.place(x = 0, y = 0, relwidth = 1, relheight = 1)
main_menu = tk.Menu(window)
window.configure(menu = main_menu, bg="silver")
file_menu = tk.Menu(main_menu, tearoff=0)
main_menu.add_cascade(label = "File", menu = file_menu)

file_label = tk.Label(window, text="New File", bg="black", fg="white")
file_label.place(relx=0.01, rely=0.99, anchor="sw")

new_file_icon = tk.PhotoImage(file = "resource/new_file.gif")
open_file_icon = tk.PhotoImage(file = "resource/open_file.gif")
save_file_icon = tk.PhotoImage(file = "resource/save_file.gif")


def open_file():
    global file_name
    file_name = fd.askopenfilename()
    file_label["text"] = "File: " + file_name
    with open(file_name, encoding = "utf-8") as file:
        text = file.read()
        content_text.delete(1.0, "end")
        content_text.insert(1.0, text)
    window.title(f"NotePad: {file_name}")

def save_text_to_file():
    text = content_text.get(1.0, "end")
    with open(file_name, "w", encoding="utf-8") as file:
        file.write(text)

def save_as_file():
    global file_name
    file_name = fd.asksaveasfile().name
    file_label["text"] = "File: " + file_name
    save_text_to_file()
    window.title(f"NotePad: {file_name}")

def save_file():
    global file_name
    tkm.showinfo("Saving file...", f"Saving text replacing in {file_name}")
    if file_name == "":
        save_as_file()

    else:
        save_text_to_file()

def new_file():
    user_answer = tkm.askokcancel("Making new file...", "Are you sure? The unsaved text will be deleted.")
    if user_answer == True:
        global file_name
        file_name = ""
        file_label["text"] = "New file "
        content_text.delete(1.0, "end")
        window.title(f"NotePad: Unsaved file")

def info_about():
    tkm.showinfo("About:", "Version: 1.00\nDeveloper: SosiskaSunrise")

file_menu.add_command(label = "New File", image=new_file_icon, compound="left", command = new_file)
file_menu.add_command(label = "Open", image=open_file_icon, compound="left", command = open_file)
file_menu.add_command(label = "Save", image=save_file_icon, compound="left", command = save_file)
file_menu.add_command(label = "Save As", image=save_file_icon, compound="left", command = save_as_file)

def info_help():
    tkm.showinfo("Help", "New = Create a new file\nOpen = Open .txt file\nSave = Save opened .txt file\nSave as = Save file with new name")

edit_menu = tk.Menu(main_menu, tearoff=0)
info_menu = tk.Menu(main_menu, tearoff=0)

info_menu.add_command(label = "Help", command = info_help)
info_menu.add_command(label = "About the programm", command = info_about)

edit_menu.add_command(label = "Copy")
edit_menu.add_command(label = "Cut")
edit_menu.add_command(label = "Paste")
edit_menu.add_command(label = "Delete")

main_menu.add_cascade(label = "Edit", menu = edit_menu)
main_menu.add_cascade(label = "About", menu = info_menu)


# Закодировано

""" with open("Example.txt", encoding = "utf-8") as file:
    # print(file.read())

    print()

    for line in file:
        print(f"String required from text. {line}")

with open("Example.txt", "a", encoding="utf-8") as file:
    file.write("\nnew text")
"""


window.mainloop()