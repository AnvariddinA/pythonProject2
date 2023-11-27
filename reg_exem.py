from tkinter import *
from tkinter import ttk
import winreg
bg_color=''

keyValue = r'Software\\KIUF'
key=winreg.OpenKey(winreg.HKEY_CURRENT_USER, keyValue, access=winreg.KEY_ALL_ACCESS,)
c1=winreg.QueryValueEx(key, 'bg_color')
print(c1)
if c1:
    bg_color=c1[0]
print(bg_color)


root = Tk()
root.title("Windows Reasrt")
root.geometry("250x200")
root.config(bg=bg_color)
position = {"padx":6, "pady":6, "anchor":NW}
colors=["red", "blue", "yellow", "green"]
selected_color=StringVar()
header = ttk.Label(text="Rang tanlang")
header.pack(**position)

def select():
    header.config(text=f"Tanlangan rang {selected_color.get() }")
    root.configure(bg=selected_color.get())
    winreg.SetValueEx(key, 'bg_color',0,winreg.REG_SZ,selected_color.get())

for color in colors:
    color_btn=ttk.Radiobutton(text=color,value=color, variable=selected_color, command=select)
    color_btn.pack(**position)


root.mainloop()

if key:
    winreg.CloseKey(key)

