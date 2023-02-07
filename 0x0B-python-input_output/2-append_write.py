#!/usr/bin/python3


def append_write(filename="", text=""):
    """Write string to file (append mode)
    Args:
        filename (str): string of path to file
        text (str): string to write to file
    Returns:
        number of characters written
    """
    with open(filename, mode="a", encoding="utf-8") as f:
        return (f.write(text))
