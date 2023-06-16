red = int(input(), 16)
green = int(input(), 16)
blue = int(input(), 16)
qt_green = (red // green) ** 2
if qt_green == 0:
    print(1)
else:
    resp = (qt_green * ((green // blue) ** 2)) + qt_green + 1
    z = hex(resp)[2:]
    print(z)