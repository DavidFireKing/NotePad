import tkinter as tk
import tkinter.filedialog as fd

window = tk.Tk()
window.title("NotePad")
window.geometry("400x400")

content_text = tk.Text(window, wrap="word", bg="black", fg="white")
content_text.place(x = 0, y = 0, relwidth = 1, relheight = 1)

main_menu = tk.Menu(window)
window.configure(menu = main_menu, bg="silver")
file_menu = tk.Menu(main_menu, tearoff=0)
main_menu.add_cascade(label = "File", menu = file_menu)

new_file_icon = tk.PhotoImage(file = "resource/new_file.gif")
open_file_icon = tk.PhotoImage(file = "resource/open_file.gif")
save_file_icon = tk.PhotoImage(file = "resource/save_file.gif")


def open_file():
    file_name = fd.askopenfilename()
    with open(file_name, encoding = "utf-8") as file:
        text = file.read()
        content_text.delete(1.0, "end")
        content_text.insert(1.0, text)


def save_as_file():
    file_name = fd.askopenfilename()
    text = content_text.get(1.0, "end")
    with open(file_name, "w", encoding = "utf-8") as file:
        file.write(text)

def save_file():
    save_as_file()

def new_file():
    content_text.delete(1.0, "end")

file_menu.add_command(label = "New File", image=new_file_icon, compound="left", command = new_file)
file_menu.add_command(label = "Open", image=open_file_icon, compound="left", command = open_file)
file_menu.add_command(label = "Save", image=save_file_icon, compound="left", command = save_file)
file_menu.add_command(label = "Save As", image=save_file_icon, compound="left", command = save_as_file)


edit_menu = tk.Menu(main_menu, tearoff=0)

edit_menu.add_command(label = "Copy")
edit_menu.add_command(label = "Cut")
edit_menu.add_command(label = "Paste")
edit_menu.add_command(label = "Delete")

main_menu.add_cascade(label = "Edit", menu = edit_menu)


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