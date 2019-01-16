import os
import shutil

def main():
    # The following dictionary will allow us to map extensions to the destination folder names
    extension_to_category = {}
    os.chdir("FilesToSort")
    for filename in os.listdir('.'):
        if os.path.isdir(filename):
            continue

        extension = filename.split('.')[-1]
        if extension not in extension_to_category:
            category = input("What category would you like to sort {} files into? ".format(extension))
            extension_to_category[extension] = category
            try:
                os.mkdir(category)
            except FileExistsError:
                print("File exists")
                pass
        os.rename(filename, "{}/{}".format(extension_to_category[extension], filename))


main()
