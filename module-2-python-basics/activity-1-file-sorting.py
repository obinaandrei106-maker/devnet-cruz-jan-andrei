"""
Module 2 — Activity: File Sorting with os and shutil
Student: Cruz, Jan Andrei O.
Date: September 25, 2026

============================================
WHAT DID YOU BUILD? (explain in your own words)
============================================
I made a Python program that can organize files automatically. The program checks the files inside 
a folder and puts them into different folders depending on their file type.
I decided to sort the files by their file extension. For example, .jpg and .png files go into the 
Images folder, while .pdf, .docx, and .txt files go into the Documents folder. If the program finds 
a file type that I did not include, it puts the file in an Others folder.


============================================
KEY VOCABULARY
============================================
- os module: I use this to work with files and folders on my computer.
- shutil module: I use this when I need to move or copy files.
- file path: This tells Python where a file or folder is located.
- directory: This is basically a folder where files are stored.
(add more as needed)


============================================
YOUR SCRIPT
============================================
Paste the code you already wrote for this activity below.
"""

import os 
import shutil 

source_folder = "files" 

folders = { 
    "Images": [".jpg", ".jpeg", ".png", ".gif"], 
    "Documents": [".pdf", ".docx", ".txt"], 
    "Videos": [".mp4", ".avi", ".mkv"] } 

    for folder in folders: 
        folder_path = os.path.join(source_folder, folder) 
        os.makedirs(folder_path, exist_ok=True) 
         
    for filename in os.listdir(source_folder): 
        file_path = os.path.join(source_folder, filename)  
        if os.path.isdir(file_path): continue  
        extension = os.path.splitext(filename)[1].lower() 
        moved = False 
        for folder, extensions in folders.items(): 
            if extension in extensions: 
                destination = os.path.join(source_folder, folder, filename) 
                shutil.move(file_path, destination) 
                print(f"Moved {filename} to {folder}") 
                moved = True 
                break  
                if not moved: 
                    others_folder = os.path.join(source_folder, "Others") 
                    os.makedirs(others_folder, exist_ok=True) 
                    destination = os.path.join(others_folder, filename) 
                    shutil.move(file_path, destination) 
                    print(f"Moved {filename} to Others") 
                    print("File sorting complete!")
"""
============================================
A MISTAKE I MADE (or one I want to avoid)
============================================
One mistake I want to avoid is putting the wrong folder path in the program. 
If the folder does not exist or I type the path incorrectly, the program will 
not be able to find my files. I also learned that I should be careful when testing 
the program because it actually moves the files. I should test it with sample files 
first instead of using important files.

============================================
HOW THIS CONNECTS TO SOMETHING ELSE
============================================
[optional: how is this similar to what real automation scripts do?
think about your own gradebook/attendance workflow — could something
like this save you time there?]
"""
