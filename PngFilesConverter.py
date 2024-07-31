#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import tkinter as tk
from tkinter import filedialog, messagebox
import os, glob
from PIL import Image

# Convert PNG files to JPG format
def png_converter_function():
    contents_dir = subdir_choice("png")
    for items in contents_dir:
        f, e = os.path.splitext(items)
        converted_items = f + ".jpg"
        if items != converted_items:
            try:
                with Image.open(items) as im:
                    rgb_im = im.convert('RGB')
                    rgb_im.save(converted_items)
            except OSError:
                print("Cannot convert", items)
    print("Conversion concluded.")

# Convert JPG files to PNG format
def jpg_converter_function():
    contents_dir = subdir_choice("jpg")
    for items in contents_dir:
        f, e = os.path.splitext(items)
        converted_items = f + ".png"
        if items != converted_items:
            try:
                with Image.open(items) as im:
                    im.save(converted_items)
            except OSError:
                print("Cannot convert", items)
    print("Conversion concluded.")
    
# Select and display the folder path in the UI
def browse_folder():
    global contents_dir
    contents_dir = filedialog.askdirectory()
    # Insert path on textbox
    directory_path.delete(0, tk.END)
    directory_path.insert(0, contents_dir)
    return contents_dir

# Determine whether to include image files from subdirectories in the conversion
def subdir_choice(extension):
    file_path = directory_path.get()
    if var1.get() == 1:
        contents_dir = glob.glob(file_path + ('/**/*.') + extension, recursive=True)
    else:
        contents_dir = glob.glob(file_path + ('/*.') + extension, recursive=False)
    return contents_dir

# Set up the GUI
window = tk.Tk()
window.title("Image Files Converter")
window.geometry('520x270')

# Button to browse and select a folder
browse_button = tk.Button(window, text="Browse Folder", command=browse_folder)
browse_button.grid(row=0, column=0, padx=10, pady=10, columnspan=2)

# Label and entry field for displaying the selected directory path
tk.Label(window, text="Directory Path:").grid(row=1, column=0, padx=10, pady=10, sticky='e')
directory_path = tk.Entry(window, width=40)
directory_path.grid(row=1, column=1, padx=10, pady=10)

# Checkbox to include or exclude subdirectories in the conversion
var1 = tk.IntVar()
c1 = tk.Checkbutton(window, text='Include Subdirectories', variable=var1, onvalue=1, offvalue=0)
c1.grid(row=2, column=0, padx=10, pady=10, columnspan=2)

# Button to start conversion from PNG to JPG format
tk.Button(window, text="Convert PNG to JPG", command=png_converter_function).grid(row=3, column=0, padx=10, pady=10, columnspan=2)

# Button to start conversion from JPG to PNG format
tk.Button(window, text="Convert JPG to PNG", command=jpg_converter_function).grid(row=4, column=0, padx=10, pady=10, columnspan=2)

window.mainloop()

