import os
import tkinter as tk
from tkinter import filedialog

# Function to rename files
def rename_files(folder_path, new_name, log_text):
    i = 1
    for filename in os.listdir(folder_path):
        new_filename = f'{new_name}_{i}{os.path.splitext(filename)[1]}'
        os.rename(os.path.join(folder_path, filename), os.path.join(folder_path, new_filename))
        log_text.insert(tk.END, f'Renamed {filename} to {new_filename}\n')
        i += 1

# Create the main window
root = tk.Tk()
root.title('Quick Rename by Pawbies')

# Set icon (you may need to adjust the path)
root.iconbitmap('D:/BStuff/paw.ico')

# Make window non-resizable
root.resizable(False, False)

# Create widgets
folder_label = tk.Label(root, text='Folder Path: ')
folder_entry = tk.Entry(root, width=50)
browse_button = tk.Button(root, text='Browse', command=lambda: folder_entry.insert(0, filedialog.askdirectory()))
name_label = tk.Label(root, text='New Name: ')
name_entry = tk.Entry(root, width=50)
rename_button = tk.Button(root, text='Rename All', command=lambda: rename_files(folder_entry.get(), name_entry.get(), log_text))
log_text = tk.Text(root, height=10, width=50)
usage_label = tk.Label(root, text="Usage: Select the folder holding your files, input new name for all \nthe files, then click 'Rename All' to make all files in that \nfolder have a name like {file_name}_{file_number}")

# Place widgets
folder_label.grid(row=0, column=0)
folder_entry.grid(row=0, column=1)
browse_button.grid(row=0, column=2)
name_label.grid(row=1, column=0)
name_entry.grid(row=1, column=1)
rename_button.grid(row=1, column=2)
log_text.grid(row=2, columnspan=3)
usage_label.grid(row=3, columnspan=3)

# Run the Tkinter event loop
root.mainloop()
