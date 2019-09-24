# PyxAlchemy
Image Manipulation

### The Problem:

One night I found I was facing a project of scaling and web-optimizing hundreds of images that were not ready to be uploaded to the internet. Doing them one by one was going to take a very long time.

### The Solution:

This program will take a large batch of .jpg files and scale them all down to a specified height and width (keeping the aspect ratio in tact), and then use ImageMagick to optimize/compress the images to a light weight capacity. 

### Details:

This program uses the **pgmagick** package on pypi: https://pypi.org/project/pgmagick/ to handle the scaling of the images.

pgmagick documentation: https://pgmagick.readthedocs.io/en/latest/tutorial.html#installation

GitHub: https://github.com/hhatto/pgmagick

Below I explain exactly how I got this to work on my system.

## Installation Instructions

The following works on **Ubuntu 18.04** using **Python 3.6.8**

Clone the repository

```
git clone https://github.com/JasonLABS/PyxAlchemy.git
```

Change directories into the project: 

```bash
cd PyxAlchemy
```

Before installing pgmagick, you need to install two dependencies. They are discussed more in the pgmagick documentation mentioned above:

**GraphicsMagick(Magick++)** : graphing library. 1.3.5 and higher version.

**Boost.Python** : wrap C++ code. 1.40 and higher version.

The documentation mentions to install the package *python-magick* to install these to libraries, however this did not work for me. The following did work for me: 

```
sudo apt update
sudo apt install libboost-python-dev
sudo apt install libgraphicsmagick++1-dev
```

Install your virtual environment. My personal preference is **venv**, and can be installed on Ubuntu 18.04 with the following:

```bash
sudo apt update && sudo apt install python3-venv
```

Set up your virtual environment: 

```python
python3 -m venv venv
```

Activate your environment: 

```bash
source venv/bin/activate
```

Upgrade pip, setuptools, and wheel:

```python
pip install --upgrade pip setuptools wheel
```

Then pip install: 

```
pip install --upgrade pgmagick
```


## How To

Make sure the file 'program.py' has executable permissions, and run: 

```bash
./program.py
```

The first time you run the program, it will check if you have the proper directories created. If not, it will create them for you.

After it sets up your environment, the program will give the next instructions and exit. 

**Put all .jpg images in the 'load_images_here' folder.**

This is a 'non-destructive' image editor. It will leave the original files as they are in the 'load_images_here' folder, and will push them through the 'pre_processed' folder and once they are fully processed they will be available in the 'processed' folder, ready to be used in your web project. 

Currently, this program only works on images that end with the extension '.jpg'. It has not been tested with variations such as, '.JPG', '.jpeg', etc...

If your image files have spaces in the name, this program will replace the spaces with an underscore '_', so a file called, 'see john run.jpg' will turn into 'see_john_run.jpg'. This is done because the commands used don't seem to know how to deal with spaces in file names. There may be a better way to do this.

run:
```
./program.py
```

It will ask you what scale you want the images scaled to. If you want them no wider than 1000px and no taller than 1000px you would put in '1000x1000'. It will keep the aspect ratio of the image and scale it down to the appropriate height and width. 

It will also ask what image quality to use. I have found 85 usually provides good compression with minimal quality loss. 

It will scale the images, web optimize them using ImageMagick which is already installed on Ubuntu 18.04, and put them in the "processed" folder where they are ready for pickup.

The new files will be prefixed with 'op_sc#'. The 'op' stands for optimized, and the 'sc' stands for scaled, and the '#' is the number of the photo. If there were more the number would increment from 0 on up. 

For example:

```
see john run.jpg 
see jane swim.jpg
```

will turn into :

```
op_sc0_see_john_run.jpg
op_sc1_see_jane_swim.jpg
```

## To Do
- Convert from .png to .jpg
- Convert .JPG, .jpeg, etc to ... .jpg