import math
def walk():
    w=float(input('The side of the triangle in cm : '))
    return w
def height():
    h=float(input('The height of the triangle in cm : '))
    return h
def main():
    w=walk()
    h=height()
    s = 1/2*w*h
    return s
print('Area of the triangle', main() ,'cm')
input('Press Enter to close the window')

