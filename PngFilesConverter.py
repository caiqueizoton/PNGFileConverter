#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import os, glob
from PIL import Image

# Function to convert PNG image files in a directory
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

# Request the user to provide directory path containing the files for conversion
while True:
    file_path = input('Enter the path to the directory containing PNG files for conversion:')      
    if os.path.isdir(file_path):
    # If path is valid, exit loop and proceede
        break
    else:
        print ('Path is invalid. Please try again.')

# Set a default value for the inclusion of subdirectories
subdir_choice = 'no'

# Check for the presence of subdirectories and ask the user whether to include them in the conversion
for root, directories, files in os.walk(file_path):
    if directories:
        while True:
            subdir_choice = input('Do you want to include sub directories in the conversion? yes/no').strip().lower()
            if subdir_choice != 'yes' and subdir_choice != 'no':
                print ('Invalid input. Please enter "yes" to include subdirectories or "no" to exclude them.')
            else:
                break
        # After a successful interaction, exit the loop
        break
                
# Generate a list of image files, considering subdirectory inclusion choice
if subdir_choice == 'yes':
    contents_dir = glob.glob(file_path + '/**/*.png', recursive=True)
elif subdir_choice == 'no':
    contents_dir = glob.glob(file_path + '/*.png', recursive=False)

# Call the conversion function with the selected image files
converter_function(contents_dir)

