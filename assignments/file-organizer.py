import os
import shutil
from datetime import datetime

def organize_files_by_type():
    try:
        user_path = input("Enter the path of the directory you want to organize (e.g., ~/Downloads): ").strip()
        directory = os.path.expanduser(user_path)

        if not os.path.isdir(directory):
            raise NotADirectoryError("The path you entered is not a valid directory.")

        print(f"Organizing files in: {directory}")
        print(os.listdir(directory))

        for filename in os.listdir(directory):
            file_path = os.path.join(directory, filename)

            if os.path.isfile(file_path):
                ext = os.path.splitext(filename)[1].lower().strip(".") or "unknown"

                print(os.path.splitext(filename))
                print(type (os.path.splitext(filename)))


                folder_path = os.path.join(directory, f"{ext}_files")
                os.makedirs(folder_path, exist_ok=True)

                timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
                name, extension = os.path.splitext(filename)

                print("**************")
                print(extension)
                print("**************")


                new_filename = f"{name}{timestamp}{extension}"
                new_path = os.path.join(folder_path, new_filename)

                shutil.move(file_path, new_path)
                print(f"Moved: {filename} → {new_path}")

    except NotADirectoryError as e:
        print(e)
    except Exception as e:
        print(f"Something went wrong: {e}")

organize_files_by_type()
