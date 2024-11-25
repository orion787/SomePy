import os

# Function 1: Get a list of file names in the current directory
def list_files():
    """
    Lists all files in the current directory.
    """
    # Get the list of all items in the current directory
    all_items = os.listdir()
    # Filter only the files (not directories)
    file_list = []
    for item in all_items:
        if os.path.isfile(item):
            file_list.append(item)
    return file_list

# Function 2: Sort the file names by their length
def sort_files(file_list):
    """
    Sorts file names by their length.
    """
    # Use a simple sorting loop for clarity
    for i in range(len(file_list)):
        for j in range(len(file_list) - i - 1):
            if len(file_list[j]) > len(file_list[j + 1]):
                # Swap the elements if they are out of order
                file_list[j], file_list[j + 1] = file_list[j + 1], file_list[j]
    return file_list

# Function 3: Combine listing and sorting
def process_files():
    """
    Lists files in the current directory and sorts them by name length.
    """
    # Step 1: Get the list of files
    files = list_files()
    print("Files in the current directory:")
    print(files)

    # Step 2: Sort the files by name length
    sorted_files = sort_files(files)
    print("\nFiles sorted by name length:")
    print(sorted_files)

# Run the process
process_files()
