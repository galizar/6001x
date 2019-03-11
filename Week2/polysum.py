from math import tan, pi

def polysum(n, s):
    """ Calculates the sum of the area and the square of the
        perimeter of the polygon.

        n: int, number of sides of the polygon
        s: int, length of each side of the polygon
    """
    boundary_length = n*s
    area = (1/4 * n * pow(s, 2) / (tan( pi/n ))
    return round(area + boundary_length**2, 4)

