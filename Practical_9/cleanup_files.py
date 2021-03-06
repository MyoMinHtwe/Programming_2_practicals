"""
CP1404/CP5632 Practical
Demos of various os module examples
"""
import shutil
import os


def main():
    """Demo of os module functions."""
    print("Starting directory is: {}".format(os.getcwd()))

    # Change to desired directory
    os.chdir('Lyrics/Christmas')

    # Print a list of all files in current directory
    print("Files in {}:\n{}\n".format(os.getcwd(), os.listdir('.')))

    # Make a new directory
    # The next time you run this, it will crash if the directory exists
    # TODO: Use exception handling to avoid the crash (just pass)
    try:
        os.mkdir('temp')
    except FileExistsError:
        pass


    # Loop through each file in the (current) directory
    for filename in os.listdir('.'):
        # Ignore directories, just process files
        # print("File name: {}".format(filename))
        if os.path.isdir(filename):
            continue

        new_name = get_fixed_filename(filename)
        print("Renaming {} to {}".format(filename, new_name))


        # TODO: Try these options one at a time
        # Option 1: rename file to new name - in place
        os.rename(filename, new_name)

        # Option 2: move file to new place, with new name
        # shutil.move(filename, 'temp/' + new_name)

    # Process all subdirectories using os.walk()
    os.chdir('..')  # '..' means to go 'up' one directory
    lyrics_path = os.getcwd()  # store the path so we can get back to it
    for directory_name, subdirectories, filenames in os.walk('.'):
        print("Directory:", directory_name)
        print("\tcontains subdirectories:", subdirectories)
        print("\tand files:", filenames)
        print("(Current working directory is: {})".format(os.getcwd()))

        # TODO: change into the directory and print the current working directory
        # then change back to the lyrics_path
        # Note: if you get this wrong, walk will stop short,
        # so you need to check it still walks through all subdirectories

        # TODO: add a loop (in between directory changes) to rename the files


def get_fixed_filename(filename):
    """Return a 'fixed' version of filename."""
    filename = filename.replace(" ", "_").replace(".TXT", ".txt")
    filename = filename.split('.')[0]

    new_name= ''
    for index in range(len(filename) - 1):
        if filename[index].islower() and filename[index + 1].isupper():
            new_name += filename[index] + '_'
        else:
            new_name += filename[index]

    new_name += '.txt'

    return new_name

def demo_walk():
    """Process all subdirectories using os.walk()."""
    os.chdir('Lyrics')
    for directory_name, subdirectories, filenames in os.walk('.'):
        print("Directory:", directory_name)
        print("\tcontains subdirectories:", subdirectories)
        print("\tand files:", filenames)
        print("(Current working directory is: {})".format(os.getcwd()))

        # TODO: add a loop to rename the files
        for filename in filenames:
            full_name = os.path.join(directory_name, filename)
            new_name = os.path.join(directory_name, get_fixed_filename(filename))
            os.rename(full_name, new_name)


main()