from PIL import Image
import tkinter as tk
from tkinter import filedialog

# function that turns the image to black and white
def blackandwhite(inputimg, outputimg):
    # opens the image
    image = Image.open(inputimg)
    # converts the image to RGB mode in case of alpha channel
    if image.mode == 'RGBA':
        image = image.convert('RGB')
    # converts to grayscale
    bw_image = image.convert('L')
    # saves the b/w image
    bw_image.save(outputimg)

# function that rotates the image vertically
def imagerotation(inputimage, outputimage):
    # opens the image
    image = Image.open(inputimage)
    # converts the image to RGB mode in case of alpha channel
    if image.mode == 'RGBA':
        image = image.convert('RGB')
    # flips the image vertically 
    vertimage = image.transpose(method=Image.FLIP_LEFT_RIGHT)
    # saves the flipped image
    vertimage.save(outputimage)

# function using tkinter to let the user choose an image to edit
def openWindow():
    root = tk.Tk()
    root.withdraw()
    # hides the main window  
    root.attributes("-topmost", True)  
    # so that the file explorer window will show on top
    file_path = filedialog.askopenfilename(title="Select an image")
    root.destroy()  
    # closes the window
    return file_path