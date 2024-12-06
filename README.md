# File Organizer Script

This Python script organizes files in a selected folder based on their extensions. The script groups files into predefined categories (e.g., Images, Videos, Text files) by moving them into corresponding subfolders. The user is prompted to select the folder to organize using a file dialog.

## Requirements

- Python 3.x
- `tkinter` (for the file dialog)

> `tkinter` is usually included by default in most Python distributions. If it's not installed, you can install it using your package manager, depending on your operating system.

## How it Works

1. The user is prompted to select a folder using a graphical file dialog.
2. The script reads the list of files in the selected folder.
3. It checks the file extension and moves each file into one of the predefined subfolders based on its type (e.g., Images, Spreadsheets, Videos, or Text files).
4. If a required subfolder does not exist, the script creates it.
5. The files are then moved into their respective subfolders, organized by file type.

## Folder Structure

The script organizes files into subfolders within the selected folder based on their extension. Here are the predefined categories:

- **Images**: Includes formats like `.png`, `.jpg`, `.svg`, etc.
- **Spreadsheets**: Includes formats like `.csv`, `.xls`, `.xlsx`, etc.
- **Videos**: Includes formats like `.mp4`, `.mkv`, `.avi`, etc.
- **Text files**: Includes formats like `.txt`, `.doc`, `.pdf`, etc.

Example folder structure after running the script:

```
selected_folder/
│
├── Images/
│   ├── image1.png
│   └── image2.jpg
│
├── Spreadsheets/
│   ├── data.csv
│   └── report.xlsx
│
├── Videos/
│   ├── movie.mp4
│   └── clip.mkv
│
└── Text files/
    ├── document.txt
    └── readme.pdf
```

## Script Details

### 1. Prompt User for Folder Selection

```python
path = askdirectory(title="Select a folder")
```

This opens a file dialog that lets the user select the folder to organize.

### 2. Dictionary of Folders and Extensions

Edit this Dictionary to suit your needs

```python
folders = {
    "Images": [".apng", ".png", ".avif", ".jpg", ".jpeg", ".jfif", ".pjpeg", ".pjp", ".svg", ".webp"],
    "Spreadsheets": [".csv", ".xls", ".xlsx", ".ods", ".imp", ".gsheet"],
    "Videos": [".webm", ".mkv", ".flv", ".vob", ".ogv", ".ogg", ".rrc", ".gif", ".gifv", ".mng", ".mov", ".mod", ".qt", ".avi", ".wmv", ".yuv", ".rm", ".asf", ".amv", ".mp4", ".m4v", ".m4p", ".mpg", ".mpeg", ".mp2", ".mpe", ".mpv", ".svi", ".3gp", ".3g2", ".mxf", ".roq", ".nsv", ".flv", ".f4v", ".f4p", ".f4a", ".f4b"],
    "Text files": [".asc", ".doc", ".docx", ".rtf", ".msg", ".pdf", ".txt", ".wpd", ".wps"],
}
```

This dictionary maps file types (based on extensions) to their corresponding folder names.

### 3. Organize Files into Folders

```python
for file in file_list:
    name, extension = os.path.splitext(f"{path}/{file}")
    
    for folder in folders:
        if extension in folders[folder]:
            if not os.path.exists(f"{path}/{folder}"):
                os.mkdir(f"{path}/{folder}")
            os.rename(f"{path}/{file}", f"{path}/{folder}/{file}")
```

The script loops through all files in the selected folder, checks their extension, creates the necessary subfolders if they don’t exist, and moves the files to the appropriate subfolder.

### 4. Confirmation Message
After the process is completed, a message is printed to confirm the successful organization of files.

```python
print("Files organized successfully")
```

