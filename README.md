## **Project Name**: Image File Converter

## **Description**:

This is a Python program designed to convert image files between PNG and JPG formats on macOS. It features a user-friendly graphical interface (GUI) for easy navigation and selection of files.

In the course of my career of over 5 years working as a video editor and producer, I frequently needed to convert image files for various projects. This often involved using different random applications, sometimes processing one file at a time. To automate this process, I developed a Python application with a user-friendly interface that automates the conversion of both PNG to JPG and JPG to PNG files. Now, you can convert multiple images across different directories in one go.

### Features:

* Converts PNG to JPG
* Converts JPG to PNG
* Folder selection
* Option to include subdirectories
* User-friendly graphical interface

### Installation

**Prerequisites:**

* **Python 3.x:** Ensure Python is installed on your system. You can download it from [https://www.python.org/downloads/](https://www.python.org/downloads/)
* **pip (optional):** If you don't have pip installed, open your terminal and run the following command:
  ```bash
  python -m ensurepip --upgrade
  ```

**Installing the Image File Converter:**
1. Download the project files.
2. Open your terminal and navigate to the project directory.
3. Install the required library using pip:
 ```bash
  pip install --user -U pillow tk
  ```

### Usage:

1. Run the script (`python image_file_converter.py`).
2. Click "Browse Folder" to select the directory containing your image files.
3. Choose whether to include subdirectories for conversion using the checkbox.
4. Click "Convert PNG to JPG" or "Convert JPG to PNG" depending on your desired conversion.

The application will process the files and save the converted images in the same directory.

### Author: Carlos Izoton Filho
