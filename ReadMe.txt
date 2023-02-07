This project applies Image Processing theories to an artistic application. This project is used to transform a given image into a colourful, stylized version, similar to Andy Warhol's painting of Marilyn Monroe.

To use this project, you need to have Python3 installed on your device. This project also uses the numpy library and opencv library. To install both, run the following command in your terminal:

pip install opencv-python

and this should install the opencv image processing library.

There are two versions of this project
Retro Colour Scheme.py 
Retro Colour Scheme - RGB.py

The first version takes the input image and changes the colours based on the darkness (Value using HSV representation) to a set of predefined colours. From light to dark, pixels are converted to this order of colours: White, Yellow, Orange, Red, Purple, Blue, Navy Blue, Black. Each colour being darker than the previous.

The second version takes the input image and changes the colours based on the darkness (Value using HSV representation) and the colour (Hue using HSV representation) to a set of predefined colours. Each pixel is converted to a different shade of red, green, and blue depending on how dark the pixel is. The colour is decided based on limits attached to the Hue values of each pixel.

To run either version, change the name of the source image - find the comment near the top of the file - or use my preset image for testing first.