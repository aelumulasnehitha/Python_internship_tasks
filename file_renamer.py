import os

folder_path = input("Enter the folder path: ")

if not os.path.exists(folder_path):
    print("Folder not found.")
else:
    files = os.listdir(folder_path)

    count = 1

    for file in files:
        old_path = os.path.join(folder_path, file)

        if os.path.isfile(old_path):
            extension = os.path.splitext(file)[1]

            new_name = f"file_{count}{extension}"
            new_path = os.path.join(folder_path, new_name)

            os.rename(old_path, new_path)

            print(f"{file} -> {new_name}")

            count += 1

    print("All files renamed successfully!")