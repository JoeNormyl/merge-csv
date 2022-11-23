# Updating windows after event
import os
import PySimpleGUI as pg
import csv_merge
import logging

logging.basicConfig(level=logging.DEBUG)

# Styling Variables
title_font = ("Arial", 30)
head_font = ("Arial", 16)
browse_font = ("Arial", 16)
list_font = ("Arial", 16)

# Step 1:Set theme
pg.theme("default1")

# Step 2: Create layout
title_row = [
    [
        pg.Text("Welcome to Mergetown", font=title_font, justification="c"),
    ]
]
file_list_column = [
    [pg.Text("Select Directory: ", font=head_font)],
    [
        pg.In(size=(29, 3), enable_events=True,
              key="-FOLDER-", font=browse_font),
        pg.FolderBrowse(size=(8, 1)),
    ],
    [
        pg.Listbox(
            values=[],
            enable_events=True,
            size=(60, 30),
            key="-FILE_LIST-",
            font=list_font,
            text_color="light blue",
            select_mode=pg.SELECT_MODE_MULTIPLE
        )
    ],
    [pg.Text("Choose a file from the list", size=(50, 1), font=head_font)],
    [pg.Text("Click Add button when finished", size=(50, 1), font=head_font)],
    [pg.Push(), pg.Button("Select", key="-SELECT-", pad=5,)]
]

file_viewer_column = [

    [pg.Text("File name: ", size=(70, 3), key="-TOUT-", font=head_font)],
    [pg.Listbox(values=[], enable_events=True, size=(80, 30), key="-SELECTEDLIST-",
                font=list_font, select_mode=pg.SELECT_MODE_MULTIPLE)],
    [pg.Button("Remove", key="-REMOVE-"), pg.Button("Clear All"),
     pg.Push(), pg.Button("Merge")]
]

layout = [
    [
        pg.Stretch(),
        pg.Column(title_row),
        pg.Stretch()
    ],
    [
        pg.Column(file_list_column),
        pg.VSeperator(),
        pg.Column(file_viewer_column)]
]

# Step 3: Create Window
window = pg.Window("File Viewer", layout)

# Step 4: Event loop
folder_location = ""

while True:
    event, values = window.read()

    if event == pg.WIN_CLOSED or event == "Exit":
        break

    elif event == "-FOLDER-":
        folder_location = values["-FOLDER-"]
        logging.debug(f"Folder selection: {folder_location}\n")
        try:
            files = os.listdir(folder_location)
            print(files)

        except:
            files = []

        file_names = [
            file for file in files
            if os.path.isfile(os.path.join(folder_location, file)) and file.lower().endswith(".csv")
        ]
        logging.debug(
            f"Updating Window with selected files. \nPulling in {file_names}\n")
        window["-FILE_LIST-"].update(file_names)

    elif event == "-SELECT-" and len(values["-FILE_LIST-"]) > 0:
        file_names = [file for file in values["-FILE_LIST-"]]
        logging.debug(f"Select Pressed. Pulling in {file_names}\n")
        window["-SELECTEDLIST-"].update(file for file in file_names)

    elif event == "Merge" and len(values["-FILE_LIST-"]) > 0:
        path = values["-FILE_LIST-"]
        selected_files = values["-FILE_LIST-"]
        logging.debug(
            f"Merge Clicked. \nFiles in Selected Pane are {selected_files} \nPath is {path}")
        window["-SELECTEDLIST-"].update("Merged")
        # csv_merge.merge(selected_files, path)

    elif event == "-REMOVE-":
        logging.debug(
            f"All Values: {values}")
        file_list = values["-SELECTEDLIST-"]
        remove_list = [file for file in values["-SELECTEDLIST-"]]
        selected_files = [
            file for file in values["-SELECTEDLIST-"] if values[file] == False]
        logging.debug(
            f"Remove Clicked \nCurrent File list: {file_list} \nRemoving Files: {remove_list} \nRemaining Files: {selected_files}")
        window["-SELECTEDLIST-"].update(selected_files)
        # window["-SELECTEDLIST-"].set_value(selected_files)

    elif event == "Clear All":
        selected_files = []
        logging.debug(
            f"Remove Clicked - Right Pane Cleared")
        window["-SELECTEDLIST-"].update(selected_files)


# Step 5: Close window
window.close()
exit()
