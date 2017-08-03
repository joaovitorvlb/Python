import SimpleCV

display = SimpleCV.Display()
cam = SimpleCV.Camera()

while display.isNotDone():
    img = cam.getImage().flipHorizontal()
    lines = img.findLines()
    if (lines):
        lines.draw((255,0,0))
    img.show()
