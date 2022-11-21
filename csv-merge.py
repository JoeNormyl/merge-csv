

# Import Modules
import os
import pandas as pd
import search


# Set File Path


def set_file_path():
    # Confirm current woring directory path
    pth = (os.path.expanduser('~')+'/')
    # Prompt user for csv source directory or use working
    usr_pth = input(
        f"Current path is {pth}. Specify path to directory for file access or type current to stay here ")
    # Update path variable
    if usr_pth == "current":
        return pth
    else:
        usr_pth = pth+usr_pth+"/"
        print(f"The path is now {usr_pth}")
        return usr_pth


def verify(lst, cnt):

    usr_verify = str(input(f"Do you want to merge {cnt} files? y or n "))
    if usr_verify == "y":
        merge(lst)
    else:
        res = search.search(lst)
        cnt = search.cnt_files(res)
        verify(res, cnt)


# Merge listed CSVs


def merge(lst):
    file_list = [path + n for n in lst]
    csv_list = []
    # Get user input for name of merged file and add csv file extension
    output_name = str(
        input("What do you want to call the merged file? ")+".csv")
    print(output_name)

# reads each (sorted) file in file_list, converts it to pandas DF and appends it to the csv_list
    for file in sorted(file_list):
        csv_list.append(pd.read_csv(file, encoding='unicode_escape').assign(
            File_Name=os.path.basename(file)))

# merges single pandas DFs into a single DF, index is refreshed

    csv_merged = pd.concat(csv_list, ignore_index=True)


# Single DF is saved to the path in CSV format, without index column
    csv_merged.to_csv(path + output_name, index=False)

    print(f"Merge Complete. File saved in {path}{output_name}")


# Set File Path
filetype = (".CSV", ".csv")
path = set_file_path()

# Generate list of csv files
file_list = search.create_file_list(path, filetype)

# Display initial list
current_count = search.cnt_files(file_list)

# Verify Input and Merge
verify(file_list, current_count)

##### TO DO####

# Allow user to type specific file names or search
# Add checks for exit, affirmative and negative response and search
# Add listener for exit or esc
# Restart function listener
# Help function listener
# Change output directory
# Create init function to run
# Create error handling and "no such directory" catch
# Implement terminal logs for debugging

# Wishlist
# Track and manage all downloaded CSVs and create internal file structure
# Play cool sound when merge is complete
# GUI interface
# Come up with cool name
# publish... for sale?
