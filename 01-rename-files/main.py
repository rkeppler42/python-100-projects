import os
from datetime import datetime


def main() -> None:
    """Rename all files in the 'files' directory by appending the current date.
    """
    directory = 'files'
    filenames = os.listdir(directory)
    day = datetime.now().strftime("%Y-%m-%d")

    for filename in filenames:
        filepath = os.path.join(directory, filename)
        name, ext = os.path.splitext(filename)
        new_filepath = f"{name}-{day}{ext}"
        new_filepath = os.path.join(directory, new_filepath)
        os.rename(filepath, new_filepath)
        print(f"Renamed '{filename}' to '{name}-{day}{ext}'")

    print("File renaming completed.")



if __name__ == '__main__':
    main()
