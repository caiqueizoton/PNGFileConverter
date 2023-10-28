#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import os, glob
from PIL import Image

# Function to convert image files in a directory
def converter_function(contents_directory):
    for items in (contents_directory):
            f, e = os.path.splitext(items)
            converted_items = f + ".jpg"
            if items != converted_items:
                try:
                    with Image.open(items) as im:
                        rgb_im = im.convert('RGB')
                        rgb_im.save(converted_items)
                except OSError:
                    print("cannot convert", items)
    print ("Conversion concluded.")

# Prompt the user for path to directory with files to be converted
while True:
    file_path = input('Enter the path to the file or directory containing multiple files to be converted:')      
    if os.path.exists(file_path):
    # If path is valid, exit loop and proceede
        break
    else:
        print ('Path is invalid. Please try again.')

# Prompt the user to include subdirectories in the conversion
for root, directories, files in os.walk(file_path):
    if directories:
        while True:
            subdir_choice = input('Do you want to include sub directories in the conversion? yes/no').strip().lower()
            if subdir_choice != 'yes' and subdir_choice != 'no':
                print ('Invalid input. Please enter "yes" or "no".')
            else:
                break
                
# Generate a list of image files, considering subdirectory inclusion choice
if subdir_choice == 'yes':
    contents_dir = glob.glob(file_path + '/**/*.png', recursive=True)
elif subdir_choice == 'no':
    contents_dir = glob.glob(file_path + '/*.png', recursive=False)

# Call the conversion function with the selected image files
converter_function(contents_dir)

