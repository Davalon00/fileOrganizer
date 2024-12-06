import os
from tkinter.filedialog import askdirectory

#Promp user to select a folder
path = askdirectory(title="Select a folder")

#Dictionary of folders and their extensions
#UPDATE TO FIT YOUR NEEDS
folders = {
    "Images": [".apng", ".png", ".avif", ".jpg", ".jpeg", ".jfif", ".pjpeg", ".pjp", ".svg", ".webp"],
    "Spreadsheets": [".csv", ".xls", ".xlsx", ".ods", ".imp", ".gsheet"],
    "Videos": [".webm", ".mkv", ".flv", ".vob", ".ogv", ".ogg", ".rrc", ".gif", ".gifv", ".mng", ".mov", ".mod", ".qt", ".avi", ".wmv", ".yuv", ".rm", ".asf", ".amv", ".mp4", ".m4v", ".m4p", ".mpg", ".mpeg", ".mp2", ".mpe", ".mpv", ".svi", ".3gp", ".3g2", ".mxf", ".roq", ".nsv", ".flv", ".f4v", ".f4p", ".f4a", ".f4b"],
    "Text files": [".asc", ".doc", ".docx", ".rtf", ".msg", ".pdf", ".txt", ".wpd", ".wps"],
}


file_list = os.listdir(path)

for file in file_list:
    #separates all files extensions
    name, extension = os.path.splitext(f"{path}/{file}")

    #check folders for file extension
    for folder in folders:
        if extension in folders[folder]:

            #creates folder if necessary
            if not os.path.exists(f"{path}/{folder}"):
                os.mkdir(f"{path}/{folder}")

            #move file to new folder
            os.rename(f"{path}/{file}", f"{path}/{folder}/{file}")

print("Files organized successfully")