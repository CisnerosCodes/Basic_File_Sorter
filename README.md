---

# 📂 File Sorter

This Python script automatically organizes and sorts files from a specified directory (such as your `Downloads` folder) into categorized folders based on file type. It helps keep your files tidy by detecting file extensions using the [`filetype`](https://pypi.org/project/filetype/) library.

---

## 🔧 Features

- Automatically detects file types using `filetype`
- Sorts files into predefined categories
- Creates destination folders if they don't exist
- Handles unknown or unclassified files by placing them into a **"To be Sorted"** folder

---

## 📁 Folder Categories

| Category             | File Extensions         |
|----------------------|-------------------------|
| Academic             | `xlsx`                  |
| Resume & Career      | *(currently empty)*     |
| Images & Media       | `jpg`, `png`, `gif`     |
| Software & Setup     | `exe`, `msi`            |
| Personal             | *(currently empty)*     |
| Work & Professional  | *(currently empty)*     |
| To be Sorted         | *(unknown file types)*  |

---

## 🚀 How It Works

1. The script scans all files in the specified `directory`.
2. Each file's type is detected using the `filetype` library.
3. Based on the file extension, the file is moved to the appropriate subfolder under `destination_directory`.
4. Files that don’t match any predefined category are placed in the **"To be Sorted"** folder for manual review.

---

## 🛠️ Setup

1. **Install Requirements:**

```bash
pip install filetype
```

2. **Update Paths (if needed):**

In the script, modify the following variables to match your local setup:

```python
directory = r"C:\Users\user\Downloads"
destination_directory = r"C:\Users\user\Downloads\sorted_files"
```

3. **Run the Script:**

```bash
python file_sorter.py
```

---

## 📌 Notes

- Empty category lists (e.g. `"Resume & Career": []`) act as placeholders for future file types.
- You can add more file extensions to any category as needed.
- Files that can’t be identified by the `filetype` library will default to the "To be Sorted" folder.

---

## 📎 Example Output

```
Moved: budget.xlsx -> Academic
Moved: image001.jpg -> Images & Media
Moved: setup_installer.exe -> Software & Setup
Moved: randomfile.xyz -> To be Sorted
```

---

## 📬 Contributing

Feel free to improve the script by:
- Adding more file extensions
- Creating a config file for easier customization
- Implementing a GUI

---

## 🧠 Author

Adrian — Passionate about coding tools that bring clarity and order to everyday tasks.

---
