import argparse
import re
from highlighter import coloring


def grep(filename, regex, highlight=None):
    """Grep utility for printing lines in a file with regex matches.

    Args:
        filename (str): Path of file to be checked.
        regex (str): Lines with regular expression matches will be
            printed.
        highlight (str, optional): Bash color code. Defaults to None.
    """

    with open(filename, 'r') as file:
        lines = file.readlines()
    for line in lines:
        matches = re.findall(re.escape(regex), line)
        if matches:
            if highlight:
                print(coloring({1: regex}, {1: highlight}, line))
            else:
                print(line)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("filename", help="filename/path to file")
    parser.add_argument("regex", help="Regular expression used to "
                        "search text. Remember quotes around regex.")
    parser.add_argument("--highlight", help="highlight parts matching"
                        " regex")
    args = parser.parse_args()
    grep(args.filename, args.regex, args.highlight)
