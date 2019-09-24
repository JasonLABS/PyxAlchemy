#!venv/bin/python
import os, shutil
from pgmagick import Image
from os import listdir
from os.path import isfile, join


def main():
    print_header()
    setup_environment()
    image_process()
    da_smush()


def print_header():
    print("----------------------")
    print("      JasonLABS")
    print("      PyxAlchemy")
    print("      Version 1")
    print("----------------------")
    print("")


def setup_environment():
    environment_is_setup = True
    print("Setting up environment...")
    if not os.path.exists('load_images_here'):
        os.mkdir('load_images_here')
        environment_is_setup = False
        print("The directory 'load_images_here' has been created. ")
    else:
        environment_is_setup = True

    if not os.path.exists('pre_processed'):
        os.mkdir('pre_processed')
        environment_is_setup = False
        print("The directory 'pre_processed' has been created. ")
    else:
        environment_is_setup = True

    if not os.path.exists('processed'):
        os.mkdir('processed')
        environment_is_setup = False
        print("The directory 'processed' has been created. ")
    else:
        environment_is_setup = True

    if environment_is_setup is False:
        print(
            "Your environment is now set up. Please load images into the 'load_images_here' folder and run program again.")
        exit()


def image_process():
    # If you change directory of loaded images, change this variable
    # it will change the directory for the rest of this function.
    # the '/' is important at the end of the file name.
    load_images_here = 'load_images_here/'

    files = [f for f in listdir(load_images_here) if isfile(join(load_images_here + '.', f))]
    # files.remove('program.py')
    # files.remove('README.md')

    print(files)

    num = 0
    i = 0

    image_scale = input("Scale in px. Ex: 1000x1000 \n")

    for file in files:
        new_filename = file
        no_spaces_true = True
        if ' ' in file:
            no_spaces_true = False
            print("Found spaces...")
            file_no_space = file.replace(' ', '_')
            new_filename = file_no_space
            print("replaced spaces....")
            print("writing..." + file + ' -> ' + file_no_space)
            file = load_images_here + file
            file_no_space = load_images_here + file_no_space
            shutil.copy(file, file_no_space)
            print("New File is written.")
            file = file_no_space
        print(file)
        if no_spaces_true == True:
            im = Image(load_images_here + file)
        else:
            im = Image(file)
        im.quality(100)
        im.scale(image_scale)
        # im.sharpen(1.0) # This doesn't seem to help. Keeping it for further research
        im.write('pre_processed/sc' + str(num) + '_' + new_filename)  # 'sc' in this line indicates 'scaled'
        if no_spaces_true == False:
            clean_up = "rm " + file_no_space
            os.system(clean_up)
        num += 1
        i += 1


def da_smush():
    # I found the following code for the 'files' variable on: https://stackoverflow.com/a/3207973
    files = [f for f in listdir('pre_processed/') if isfile(join('pre_processed/', f))]

    img_quality = 0
    img_quality = input("What image quality to use? 85 usually provides good results: \n")

    for file in files:
        # This is an imagemagick command. It should be on linux systems
        command = "convert pre_processed/" + file + " -sampling-factor 4:2:0 -strip -quality " + img_quality + " -interlace JPEG -colorspace sRGB " + "processed/op_" + file

        os.system(command)

        print("Your image has been processed: " + file)

    clean_up = "rm pre_processed/*"
    os.system(clean_up)


if __name__ == '__main__':
    main()
