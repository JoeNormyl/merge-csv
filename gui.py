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
            size=(40, 20),
            key="-FILE_LIST-",
            font=list_font,
            text_color="light blue"
        )
    ],
    [pg.Text("Choose a file from the list", size=(50, 1), font=head_font)],
    [pg.Text("Click Add button when finished", size=(50, 1), font=head_font)],
    [pg.Push(), pg.Button("Select", pad=5,)]
]

file_viewer_column = [

    [pg.Text("File name: ", size=(70, 3), key="-TOUT-", font=head_font)],
    [pg.Multiline(size=(70, 30), key="-TEXT-", font=list_font)],
    [pg.Button("Merge"), pg.Button("Clear All")]
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
    print("window launched")
    event, values = window.read()

    if event == pg.WIN_CLOSED or event == "Exit":
        break

    elif event == "-FOLDER-":
        folder_location = values["-FOLDER-"]
        logging.debug(f"Folder selection: {folder_location}")
        try:
            files = os.listdir(folder_location)

        except:
            files = []

        file_names = [
            file for file in files
            if os.path.isfile(os.path.join(folder_location, file)) and file.lower().endswith(".csv")
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
