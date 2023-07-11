# -*- coding: utf-8 -*-
"""
Created on Sun Jul  9 21:15:36 2023

@author: barry
"""

# import pandas, tkinter, subprocess, sys, and fieldialog

import pandas as pd
import subprocess
import sys
import tkinter as tk
from tkinter import filedialog

#This creates a "FileSelectorGUI" class to handle the GUI operations. The "__init__" method initializes the GUI window and sets initial path variables to None.
#The create_buttons method creates three buttons: 
#"Select File 1", "Select File 2", and "Save as". 
#Each button is associated with a respective command method that handles the file selection.

#The select_file1, select_file2, and select_output_path methods use the filedialog module to 
#open file explorer dialogs for selecting paths. 
#The selected paths are stored in these path variables (file_pathaging, file_pathapproval, and output_path).

#When you run this code, the GUI window will display three buttons. 
#Clicking each button will open the file explorer dialog to select the respective file or output path. 
#The selected paths will be stored in their corresponding variables, these will be used in further operations.

class FileSelectorGUI:
    def __init__(self):
        self.root = tk.Tk()
        self.file_pathaging = None
        self.file_pathapproval = None
        self.output_path = None

        self.create_buttons()
        self.root.mainloop()

    def create_buttons(self):
        button1 = tk.Button(self.root, text="Select Aging Spreadsheet", command=self.select_file1)
        button1.pack()

        button2 = tk.Button(self.root, text="Select Approval Spreadsheet", command=self.select_file2)
        button2.pack()

        button3 = tk.Button(self.root, text="Save as", command=self.select_output_path)
        button3.pack()

    def select_file1(self):
        self.file_pathaging = filedialog.askopenfilename()
        return self.file_pathaging

    def select_file2(self):
        self.file_pathapproval = filedialog.askopenfilename()
        return self.file_pathapproval

    def select_output_path(self):
        self.output_path = filedialog.asksaveasfilename()
        return self.output_path
    
# Get the file paths

# Create an instance of the FileSelectorGUI class
file_selector = FileSelectorGUI()

# Access the selected file paths
e1_path = file_selector.file_pathaging
e2_path = file_selector.file_pathapproval
e3_path = file_selector.output_path    

# reading files
e1 = pd.read_excel(e1_path)
e2 = pd.read_excel(e2_path)

# rename e2 title column and drop first 15 characters
e2 = e2.rename(columns={'Title': 'invoiceid'})
e2['invoiceid'] = e2['invoiceid'].str[15:]

# for e1 merge vendor and invoice to invoiceid
e1["invoiceid"] = e1['Vendor'].astype(str) +" "+ e1['Invoice']

# Should prep the spreadsheet to avoid this issue. Will comment out later.
e1 = e1.rename(columns={'Unnamed: 7': 'Due Date'})
e1.head()

# merging dataframes
e3 = e1[["invoiceid","Due Date"]].merge(e2[["invoiceid","Status"]],on="invoiceid",how="left")

# replace NaN with "Not Uploaded" since NaN means it was missing from the approval spreadsheet.
e3[['Status']] = e3[['Status']].fillna('Not Uploaded')

# export to output path
e3.to_csv(e3_path)
sys.exit()  