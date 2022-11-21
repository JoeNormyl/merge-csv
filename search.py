def search(lst):
    # Prompt user for additional search term
    print(f"File names are: ")
    for n in lst:
        print(n)
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
