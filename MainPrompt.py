from editFunctions import blackandwhite, imagerotation, openWindow
# imports the functions from the editFunctions file
   

print("Welcome to the Image Editor! ")
selectionimage = input('Press x to choose an image!\n')
if selectionimage == 'x':
  picture = openWindow()
# opens a file explorer window, so that the user
# can choose an image to edit
    
print("What would you like to do with the image?")
choice = input("1-Black and White \n2-Rotate\n")

# choice between turning the image b/w or rotating it
if choice == '1':
      blackandwhite(picture, 'blackwhite.jpg')
    
if choice == '2':
      imagerotation(picture, 'rotatedimage.jpg')
