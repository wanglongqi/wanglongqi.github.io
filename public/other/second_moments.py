def second_moments(self):
    """The second moments of area of the polygon.

    Returns
    =======

    Ix, Iy, Ixy : Second moments of area

    Examples
    ========

    >>> from sympy import Point, Polygon, S
    >>> from numpy import arange
    >>> p=[(cos(i),sin(i)) for i in arange(6)/S.One/3*pi]
    >>> poly = Polygon(*p)
    >>> second_moments(poly)
        (5*sqrt(3)/16, 5*sqrt(3)/16, 0)

    """
    xc, yc = self.centroid.args
    Ix, Iy, Ixy = 0, 0, 0
    args = self.args
    for i in xrange(len(args)):
        x1, y1 = args[i - 1].args
        x2, y2 = args[i].args
        x1 -= xc; x2 -= xc
        y1 -= yc; y2 -= yc
        v = x1*y2 - x2*y1
        Ix += v*(y1*y1 + y1*y2 +y2*y2)
        Iy += v*(x1*x1 + x1*x2 +x2*x2)
        Ixy += v*(x1*y2 + 2*x1*y1 + 2*x2*y2 + x2*y1)
    Ix /= 12
    Iy /= 12
    Ixy /= 24
    return (Ix, Iy, Ixy)
