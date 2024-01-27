#!/usr/bin/python3

def say_my_name(first_name, last_name=""):
    """
    Prints My name is <first name> <last name>
    Args:
        first_name (str): first name
        last_name (str): last name
    Raises:
        TypeError: if first_name or last_name are not strings
    """
    if not isinstance(first_name, str) :
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str) :
        raise TypeError("last_name must be a string")
    full_name = f"My name is {first_name} {last_name}" if last_name else f"My name is {first_name}"
    print(full_name)


if __name__ == "__main__":
    import doctest
    doctest.testmod()
