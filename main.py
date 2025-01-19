import os
import shutil
import filetype

# Folder path to sort
directory = r"C:\Users\user\Downloads"  # Replace with your folder path
destination_directory = r"C:\Users\user\Downloads\sorted_files"

folders = {
    "Academic": ["xlsx"],
    "Resume & Career": [],
    "Images & Media": ["jpg", "png", "gif"],
    "Software & Setup": ["exe", "msi"],
    "Personal": [],
    "Work & Professional": [],
    "To be Sorted": []
}

# Create category folders in the destination directory if they don't exist
for folder in folders:
    new_folder = os.path.join(destination_directory, folder)
    os.makedirs(new_folder, exist_ok=True)


def get_file_type(filepath):
    """Detect file type using filetype library"""
    kind = filetype.guess(filepath)
    if kind is None:
        return None  # If filetype can't detect, return None
    return kind.extension


def sort_files():
    """Sort files based on their extensions"""
    for file in os.listdir(directory):  # Loop through files in the source directory
        file_path = os.path.join(directory, file)  # Full path to the file

        # Skip directories
        if os.path.isdir(file_path):
            continue

        # Get the file extension using filetype library
        file_extension = get_file_type(file_path)

        # Check if a file type was detected
        if file_extension is None:
            category = "To be Sorted"  # If no file type is detected, move to "To be Sorted"
        else:
            # Check if the file extension matches any category in the folders dictionary
            category = None
            for category_name, extensions in folders.items():  # Renamed `folder` to `category_name`
                if file_extension in extensions or (not extensions and category == "To be Sorted"):
                    category = category_name
                    break

        # If no category was found, move the file to the "To be Sorted" folder
        if category is None:
            category = "To be Sorted"

        # Move the file to the corresponding category folder
        destination_path = os.path.join(destination_directory, category, file)
        shutil.move(file_path, destination_path)
        print(f"Moved: {file} -> {category}")


# Call the function to start sorting the files
sort_files()
