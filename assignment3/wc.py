#!/usr/bin/env python

import sys

def main():
    """Main function to count number of lines, words, and characters, for all
    the given arguments 'filenames' given.

    A for-loop goes through the array of arguments given to wc.py when run from
    from the terminal. Inside the loop each argument will be 'open' for
    read-only. Our needed variables will be made and a 'with' will be called
    containing the open files. A for-loop will go through each line of a file.
    The counting of lines, words, characters, and spaces will be done in this
    loop. To get the count of the lines we count one '1' on each iteration.
    We split the lines at spaces ' ' and count the length to find the
    wordcount. We find the count of the characters by finding the length of the
    line and subtracting the amout of spaces in the line and subtract to
    count for the newline at the end of each line. At the end we print the
    result as a human-readable string to the default output.

    Note:
        The 'with' keyword is being used as it will clean the file-opening
            regardless of the code gets done, or if it fails, gets interrupted,
            or exceptions are thrown.

    Args:
        argv(array): Array containing all arguments given as strings.
        Expecting filenames or filepaths.

    Attributes:
        lineCounter (int): Variable to keep track of the number of lines
        wordCounter (int): Variable to keep track of the number of words
        characterCounter (int): Variable to keep track of the number of characters
        spaces (int): Variable to keep track of the number of spaces

    """
    if __name__ == "__main__":
        for path in sys.argv[1:]:
            file = open(path, 'r')
            lineCounter = wordCounter = characterCounter = spaces = 0
            with file as f:
                for line in f:
                    lineCounter+=1
                    wordCounter+= len(line.split())
                    characterCounter+=len(line)-line.count(' ')-line.count('\n')
                    spaces += line.count(' ')
            print(f"{lineCounter} {wordCounter} {characterCounter} {path}")

main()
