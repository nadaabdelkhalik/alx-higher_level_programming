#!/usr/bin/python3

def add_integer(a, b=98):
    if not (isinstance(a, int) or isinstance(a, float)):
        raise TypeError("a must be an integer or b must be an integer")
    a = int(a)
    b = int(b)
    return a + b
if __name__ == "__main__":
    import doctest
    doctest.testmod()
