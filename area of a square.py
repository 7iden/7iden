import math

def walk():
    w = float(input('The first side of the square in cm : '))
    return w
def height():
    h = float(input('The other side of the square in cm : '))
    return h
def main():
    w=walk()
    h=height()
    s=w*h
    return s
print('Perimeter of a square',main(),'cm^2')
input('Press Enter to close the window')
