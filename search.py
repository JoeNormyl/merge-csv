import os
# Creates list of files matching user input (starts with)


def create_file_list(pth, type):
    # Create list with files to merge based on user input
    file_lst = ([item for item in os.listdir(pth)
                if item.endswith(type)])
    return file_lst

# Counts and prints all items on a list


def cnt_files(lst):
    cnt = str(len(lst))
    print(f"There are {cnt} to be merged.")
    print(f"File names are: ")
    for n in lst:
        print(n)
    return (cnt)


# Take input to search through a file list


def search(lst):
    # Prompt user for additional search term

    usr_srch = input(
        "Search within results. Type additional search term or type exit to exit: ")
    if usr_srch == "exit":
        print("Then there is no pleasing you")
        quit()
    # assign files to list if they contain user search term
    file_lst = ([item for item in lst if usr_srch in item])
    print("SEARCH MODULE COMPLETE")
    # if len(file_lst) == 0:
    #     print(f"No files found matching search. Please try again ")
    return file_lst
