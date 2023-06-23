
"""
CREDITS
Forest theme by rdbende
License: MIT license
Source: https://github.com/rdbende/ttk-widget-factory

PyTube3 Module Tutorial
Source: https://towardsdatascience.com/build-a-youtube-downloader-with-python-8ef2e6915d97
"""
from pytube import YouTube
import webbrowser
import tkinter.messagebox as msg

import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.option_add("*tearOff", False)

root.columnconfigure(index=0, weight=1)
root.columnconfigure(index=1, weight=1)
root.columnconfigure(index=2, weight=1)
root.rowconfigure(index=0, weight=1)
root.rowconfigure(index=1, weight=1)
root.rowconfigure(index=2, weight=1)

# A style and icon
style = ttk.Style(root)
root.iconbitmap(f"./icon.ico")
root.title("Youtube Link Converter")

# Downloaded tcl and theme from azure on github! Such a good theme Mr Rai, I'd recommend to use if you ever use Tkinter
root.tk.call('source', 'forest-dark.tcl')
style.theme_use('forest-dark')

option_menu_list = ["", "File Extentions", ".webm", ".mp4",".mp3"]

# These are the control variables I used (similar to the spritesheets from my game Twisted Empress and my Image Manipulator)
a = tk.IntVar(value=1)
d = tk.IntVar(value=2)
e = tk.StringVar(value=option_menu_list[1])
f = tk.BooleanVar()
g = tk.DoubleVar(value=75.0)
h = tk.BooleanVar()

# Create a Frame for the Checkbuttons
check_frame = ttk.LabelFrame(root, text="Output", padding=(20, 10))
check_frame.grid(row=0, column=0, padx=(20, 10), pady=(20, 10), sticky="nsew")

# Checkbuttons
check_1 = ttk.Radiobutton(check_frame, text="Video", variable=a,value=1)
check_1.grid(row=0, column=0, padx=5, pady=10, sticky="nsew")
check_2 = ttk.Radiobutton(check_frame, text="Audio", variable=a,value=2)
check_2.grid(row=1, column=0, padx=5, pady=10, sticky="nsew")

# Separator
separator = ttk.Separator(root)
separator.grid(row=1, column=0, padx=(20, 10), pady=10, sticky="ew")

# Create a Frame for the Radiobuttons
radio_frame = ttk.LabelFrame(root, text="Resolution", padding=(20, 10))
radio_frame.grid(row=2, column=0, padx=(20, 10), pady=10, sticky="nsew")

# Radiobuttons
radio_1 = ttk.Radiobutton(radio_frame, text="High", variable=d, value=1)
radio_1.grid(row=0, column=0, padx=5, pady=10, sticky="nsew")
radio_2 = ttk.Radiobutton(radio_frame, text="Medium", variable=d, value=2)
radio_2.grid(row=1, column=0, padx=5, pady=10, sticky="nsew")
radio_3 = ttk.Radiobutton(radio_frame, text="Low", variable=d, value=3)
radio_3.grid(row=2, column=0, padx=5, pady=10, sticky="nsew")

# Create a Frame for input widgets
widgets_frame = ttk.Frame(root, padding=(0, 0, 0, 10))
widgets_frame.grid(row=0, column=1, padx=10, pady=(30, 10), sticky="nsew", rowspan=3)
widgets_frame.columnconfigure(index=0, weight=1)

# Entry
entry = ttk.Entry(widgets_frame)
entry.insert(0, "Enter YT Link")
entry.grid(row=0, column=0, padx=5, pady=(0, 10), sticky="ew")


# OptionMenu
optionmenu = ttk.OptionMenu(widgets_frame, e, *option_menu_list)
optionmenu.grid(row=5, column=0, padx=5, pady=10, sticky="nsew")
def open_link():
    url = entry.get()
    if "youtube" in url:
        webbrowser.open_new_tab(url)
    else:
       msg.showinfo("Error","Incorrect Link! Must be a link to a youtube video!") 

# Button
button = ttk.Button(widgets_frame, text="Open Link",command=open_link)
button.grid(row=6, column=0, padx=5, pady=10, sticky="nsew")


#Downloads the file. NOTE: it's extremely buggy with the github module and sometimes it does not work. I have got it to work on my computer
#However on the school computer it does not work. Hopefully it works for you. I have not found a way after a while to solve this problem.
def download():
    url = entry.get()
    if "youtube" in url:
        print("downloading...")
        link = YouTube(url)
        if a.get() == 1: #Video Only
            link.streams.filter(only_video=True)
        elif a.get() == 2: #Audio Only
            link.streams.filter(only_audio=True)
        print(d.get())
        if d.get() == 1:
            output = link.streams.get_highest_resolution()
        elif d.get() == 2:
            pass#output = link.streams[len(link.streams)/2]
        else:
            output = link.streams.get_lowest_resolution()
        output.download()
        print("downloaded")
    #
    else:
       msg.showinfo("Error","Incorrect Link! Must be a link to a youtube video!") 
    
# Accentbutton
accentbutton = ttk.Button(widgets_frame, text="Download", style="Accent.TButton",command=download)
accentbutton.grid(row=7, column=0, padx=5, pady=10, sticky="nsew")

# Panedwindow
paned = ttk.PanedWindow(root)
paned.grid(row=0, column=2, pady=(25, 5), sticky="nsew", rowspan=3)

# Pane #1
pane_1 = ttk.Frame(paned)
paned.add(pane_1, weight=1)

# Pane #2
pane_2 = ttk.Frame(paned)
paned.add(pane_2, weight=3)

# Sizegrip
sizegrip = ttk.Sizegrip(root)
sizegrip.grid(row=100, column=100, padx=(0, 5), pady=(0, 5))

# Center the window, and set minsize
root.update()
root.minsize(root.winfo_width(), root.winfo_height())
x_cordinate = int((root.winfo_screenwidth()/2) - (root.winfo_width()/2))
y_cordinate = int((root.winfo_screenheight()/2) - (root.winfo_height()/2))
root.geometry("+{}+{}".format(x_cordinate, y_cordinate))

# Start the main loop
root.mainloop()