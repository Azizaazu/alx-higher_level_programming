0. If it's not tested it doesn't work
All your files, classes and methods must be unit tested and be PEP 8 validated.
1. Base class
Write the first class Base:

Create a folder named models with an empty file __init__.py inside - with this file, the folder will become a Python package

Create a file named models/base.py:

Class Base:
private class attribute __nb_objects = 0
class constructor: def __init__(self, id=None)::
if id is not None, assign the public instance attribute id with this argument value - you can assume id is an integer and you don’t need to test the type of it
otherwise, increment __nb_objects and assign the new value to the public instance attribute id
This class will be the “base” of all other classes in this project. The goal of it is to manage id attribute in all your future classes and to avoid duplicating the same code (by extension, same bugs)
.
.
.
19. File to instances
Update the class Base by adding the class method def load_from_file(cls): that returns a list of instances:

The filename must be: <Class name>.json - example: Rectangle.json
If the file doesn’t exist, return an empty list
Otherwise, return a list of instances - the type of these instances depends on cls (current class using this method)
You must use the from_json_string and create methods (implemented previously)
.
.
.
21. Let's draw it
Update the class Base by adding the static method def draw(list_rectangles, list_squares): that opens a window and draws all the Rectangles and Squares:

You must use the Turtle graphics module
To install it: sudo apt-get install python3-tk
To make the GUI available outside your vagrant machine, add this line in your Vagrantfile: config.ssh.forward_x11 = true
No constraints for color, shape etc… be creative!
