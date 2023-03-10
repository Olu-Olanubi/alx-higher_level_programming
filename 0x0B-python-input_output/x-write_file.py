#!/usr/bin/python3


def write_file(filename="", text=""):
    """writes a string to a text file (UTF8)
       and returns the number of characters written
    Args:
        filename (str): string of path to file
        text (str): text to be written to file
    Returns:
        number of lines in file
    """
    with open(filename, mode="w", encoding="utf-8") as f:
        f.write(text)

    with open(filename, mode="r", encoding="utf-8") as f:
        return(len(f.read()))
