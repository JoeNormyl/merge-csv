##### TO DO####

# Create search funcitonality
# help function listener
# Change output directory

### Wishlist 
#Track and manage all downloaded CSVs and create internal file structure

# Merge Multiple 1M Rows CSV files
import os
import pandas as pd

# Set File Path


def set_file_path():
    # Confirm current woring directory path
    pth = (os.path.expanduser( '~')+'/')
    # Prompt user for csv source directory or use working
    usr_pth = input(f"Current path is {pth}. Specify path to directory for file access or type current to stay here ")
    if usr_pth == "current":
        return pth
    else:
        usr_pth = pth+usr_pth+"/"
        print(f"The path is now {usr_pth}")
        return usr_pth

    # Update path variable

# Creates list of files matching user input (starts with)


def create_file_list():

    # Get user input for files startswith string
    sw_str = str(input("What do the files start with? "))

    # Get user input for name of merged file
    output_name = str(
        input("What do you want to call the merged file? ")+".csv")
    print(output_name)

    # Create list with files to merge based on user input
    file_list = [f for f in os.listdir(path) if f.startswith(sw_str)]

    return file_list, output_name

# Counts and prints all items on a list


def cnt_files(lst):
    cnt = str(len(lst))
    print(f"There are {cnt} to be merged. File names are: ")
    for n in lst:
        print(n)

# Verify with user input whether to merge


def verify(lst):
    usr_verify = str(input("Do you want to merge all these files? y or n "))
    if usr_verify == "y":
        merge(lst)
    else:
        search(lst)

# Addiional Search Within Results

def search(lst):
    # Prompt user for additional search term
        usr_srch =input("Search within results. Type additional search term or type n to exit: ")
        if usr_srch == "n":
            print("Then there is no pleasing you")
            quit()
    # assign files to list if they contain user search term
        file_lst = ([item for item in lst if usr_srch in item])
        cnt_files(file_lst)
        verify(file_lst)


# Merge listed CSVs


def merge(lst):
    file_list = [path + n for n in lst]
    csv_list = []

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
path = set_file_path()

# Run Name List for Start
file_list, output_name = create_file_list()

# Display initial list
cnt_files(file_list)

# Verify Input and Merge
verify(file_list)


# Verify Merge
# if usr_verify == "n" or "N":
#     usr_verify = str(
#         input("Search within results. Type additional search term or type N to exit: "))
# #     print(usr_verify)
# # Secondary Search

#    # If no exit program
#    ###### THE PROBLEM IS HERE######
#    if usr_verify == "N":
#         print("Then there is no pleasing you")
#     else:
#         # 2d. Searching name_list for user search term and narrowing list to only items containing it
#         name_list = [n for n in name_list if name_list.count(usr_verify) > 0]
#         print("There are now " + cnt_files +
#               " to be merged. Now the file names are: ")
#     for n in name_list:
#         print(n)
#     usr_verify = str(input("Do you want to merge all these files? Y or N "))
#     if usr_verify == "" or "exit" or "no" or "No" or "NO" or "n" or "N" or "quit":
#         print("Then there is no pleasing you")
#         quit()
#         # If yes continue and merge
# if usr_verify == "y" or "yes":
#     # 3. creates empty list to include the content of each file converted to pandas DF
#
# #print(f"Make sure CSV files to be merged are in the {pth}Files directory. ")
#     if input(f"Ready to continue? y or n ") == "n":
#         print(f"Please move CSVs to the Files directory at {pth}Files")
#         quit()
#     else:
#         return pth
#
#

