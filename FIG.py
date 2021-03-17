import os
import glob
import tkinter as tk
import csv
from tkinter.filedialog import askopenfilename, asksaveasfilename, askdirectory

def open_file():
    #Choose file directory to get info of files
    filepath = askdirectory()
    #csv headers
    with open(os.getcwd() +'/'+'FileInfo.csv', 'a') as summary:
        summary.write('File Name,File Size,File Type' + '\n') 

    #Loop through and add to csv file
    for file in glob.iglob(filepath+'/*'):
        filename = os.path.basename(file)
        filesize = os.path.getsize(file)
        extension = os.path.splitext(filename)[1]
        with open(os.getcwd() +'/'+'FileInfo.csv', 'a') as summary:
            summary.write(str(filename) + ',' + str(int(filesize / 1024)) + " KB" + ',' + extension + '\n')

    if not filepath:
        return
    txt_edit.delete(1.0, tk.END)
    with open(os.getcwd() +'/'+'FileInfo.csv', "r") as input_file:
        text = input_file.read()
        txt_edit.insert(tk.END, text)
    window.title(f"F.I.G - {'Looking at files in: '+filepath + '  &  File info saved in: '+os.getcwd()}")
    

def save_file():
    #Save as .txt file
    filepath = asksaveasfilename(
        defaultextension="txt",
        filetypes=[("CSV Files", "*.csv"),("Text Files", "*.txt"), ("All Files", "*.*")],
    )
    if not filepath:
        return
    
    with open(filepath, "w") as output_file:
        text = txt_edit.get(1.0, tk.END)
        output_file.write(text)
    window.title(f"F.I.G - {'File infos saved in: '+filepath}")

#GUI
window = tk.Tk()
window.title("File Info Getter - F.I.G")
window.rowconfigure(0, minsize=500, weight=1)
window.columnconfigure(1, minsize=500, weight=1)

txt_edit = tk.Text(window)
fr_buttons = tk.Frame(window, relief=tk.RAISED, bd=2)
btn_open = tk.Button(fr_buttons, text="Choose Folder", command=open_file)
btn_save = tk.Button(fr_buttons, text="Save As .txt", command=save_file)

btn_open.grid(row=0, column=0, sticky="ew", padx=5, pady=5)
btn_save.grid(row=1, column=0, sticky="ew", padx=5)

fr_buttons.grid(row=0, column=0, sticky="ns")
txt_edit.grid(row=0, column=1, sticky="nsew")

window.mainloop()