import os
import PySimpleGUI as sg
from datetime import datetime
import csv_merge
import logging

# logging.basicConfig(level=logging.DEBUG)

# Set Theme
sg.theme("GreenTan")
# pg.theme_previewer()
# theme_list = pg.theme_list()
# print(theme_list)

# Styling Variables
# fonts = sg.Text.fonts_installed_list()
# print(fonts)
title_font = ("Arial", 30)
head_font = ("Arial", 14)
button_font = ("files", 12)
files_font = ("Helvetica", 12)
list_font = ("Helvetica", 12)

# Create Layout
layout = [
    # Display Title
    [sg.Push(), sg.Text("Mergetown 2.0", font=title_font, pad=(30, 15)), sg.Push()],
    # Display Browse Instructions
    [sg.Push(), sg.Text("Please select directory where CSVs are located:", pad=20,
                        font=head_font, justification="c"), sg.Push()],
    # Display Browse Folder Button
    [
        sg.In(size=(46, 8), expand_y=False, enable_events=True,
              key="-DIRECTORY-", font=button_font, pad=12,),
        sg.FolderBrowse(auto_size_button=True, pad=12,
                        font=files_font, ),
    ],
    [sg.Text("Select Files from List Below", font=head_font)],
    # Display ListBox for File Selection
    [sg.Listbox(
        values=[],
        enable_events=True,
        size=(66, 10),
        auto_size_text=False,
        key="-FILE_LIST-",
        pad=(10, 10),
        font=list_font,
        select_mode=sg.SELECT_MODE_MULTIPLE)],
    [sg.Text("",
             font=head_font, key="-CONFIRM_HEADER-")],
    [sg.Text("", font=files_font, key="-CONFIRM_TEXT-")],
    [sg.InputText(key="-OUTPUT_NAME-", visible=False)],
    [sg.Button(
        "Merge Now", key="-MERGE-", font=button_font, visible=False)]

]

# Create Window
window = sg.Window("Merge Selector", layout, size=(
    600, 750), element_justification="c")

# Display Window using while loop
while True:
    event, values = window.read()

    # End Loop when window closed or if event Key == "Cancel"
    if event == "Cancel" or event == sg.WIN_CLOSED or event == "Exit":
        break


# Get path from User Selection
    elif event == "-DIRECTORY-":
        dir_location = values["-DIRECTORY-"]
        logging.debug(f"Folder selection: {dir_location}\n")
# Generate File List from User Selected Path
        try:
            files = os.listdir(dir_location)
            logging.debug(f"Directory Selection: {dir_location}\n")
        except:
            files = []
# Loop thru CSV files at Path and add to file_list
        file_list = [
            file for file in files
            if os.path.isfile(os.path.join(dir_location, file)) and file.lower().endswith(".csv")
        ]

        logging.debug(
            f"Updating Window with selected files. \nPulling in {file_list}\n")
# Update window to show file list in ListBox
        window["-FILE_LIST-"].update(file_list)


# Display confirmation text of number of files to be merged
    elif event == "-FILE_LIST-" and len(values["-FILE_LIST-"]):
        file_count = len(values["-FILE_LIST-"])
        window["-MERGE-"].update(visible=True)
        window["-OUTPUT_NAME-"].update(visible=True)
        window["-CONFIRM_TEXT-"].update(
            f"Enter name of output CSV abd click to merge {file_count} files")
        if file_count < 1:
            window["-MERGE-"].update(visible=False)
            window["-OUTPUT_NAME-"].update(visible=False)

    elif event == "-MERGE-":
        dir_location = str(values["-DIRECTORY-"])+"/"
        file_list = values["-FILE_LIST-"]
        name = values["-OUTPUT_NAME-"]
        logging.debug(
            f"Path is {dir_location}\nFile list is {file_list}\nFile name will be {name}")
        if not name:
            name = "Merged CSV" + str(datetime.now())
        csv_merge.merge(file_list, dir_location, name)
        print("MERGED")
        window["-DIRECTORY-"].update("")
        window["-FILE_LIST-"].update([])
        window["-CONFIRM_HEADER-"].update("")
        window["-CONFIRM_TEXT-"].update("[]")
        window["-OUTPUT_NAME-"].update([])

# Name new file aand confirm file list

# create CSV, clear inputs and restart/exit
