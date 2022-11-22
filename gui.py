# Updating windows after event
import os
import PySimpleGUI as pg
import csv_merge

# Styling Variables
title_font = ("Arial", 20)
head_font = ("Arial", 14)

# Step 1:Set theme
pg.theme("darkteal10")

# Step 2: Create layout
file_list_column = [
    [
        pg.Text("Select Directory: ", font=head_font)
    ],
    [

        pg.In(size=(30, 1), enable_events=True, key="-FOLDER-"),
        pg.FolderBrowse(),
    ],
    [
        pg.Listbox(
            values=[],
            enable_events=True,
            size=(50, 20),
            key="-FILE_LIST-"
        )
    ]
]
file_viewer_column = [
    [pg.Text("Choose a file from the list", size=(50, 1))],
    [pg.Text("File name: ", size=(70, 3), key="-TOUT-")],
    [pg.Multiline(size=(70, 30), key="-TEXT-")],
    [pg.Button("Merge"), pg.Button("Clear All")]
]

layout = [
    [
        pg.Column(file_list_column),
        pg.VSeperator(),
        pg.Column(file_viewer_column)]]

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
        try:
            files = os.listdir(folder_location)
        except:
            files = []

        file_names = [
            file for file in files
            if os.path.isfile(os.path.join(folder_location, file)) and file.lower().endswith((".txt", ".csv", ".json", ".py"))
        ]
        window["-FILE_LIST-"].update(file_names)

    elif event == "-FILE_LIST-" and len(values["-FILE_LIST-"]) > 0:
        selected_file = values["-FILE_LIST-"][0]
        with open(os.path.join(folder_location, selected_file)) as file:
            try:
                lines = file.read()
            except:
                lines = "Unable to read content. Please try again."
            window["-TOUT-"].update(os.path.join(folder_location,
                                    selected_file))
            window["-TEXT-"].update(lines)

    elif event == "Merge" and len(values["-FILE_LIST-"]) > 0:
        selected_file = values["-FILE_LIST-"][0]
        with open(os.path.join(folder_location, selected_file), "w") as file:
            file.write(values["-TEXT-"])

# Step 5: Close window
window.close()
exit()
