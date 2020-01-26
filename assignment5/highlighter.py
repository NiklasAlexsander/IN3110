import sys
import re


def get_syntax_and_theme(syntax, theme):
    """Get syntax and color theme from files.

    Args:
        syntax (str): Path of syntax-file.
        theme (str): Path of theme-file.

    Returns:
        tuple: Dicts with regex and color theme.
    """
    regex_dict = {}
    theme_dict = {}
    with open(syntax, 'r') as syntax_file:
        for line in syntax_file.readlines():
            found_regex = re.findall(r'".*:', line)[0]
            found_comment = re.findall('": .*', line)[0]
            regex_dict[found_comment[3:]] = found_regex[1:-2]

    with open(theme, 'r') as theme_file:
        for line in theme_file:
            found_color_sequence = re.findall(r": .*", line)[0]
            found_comment = re.findall(".*:", line)[0]
            theme_dict[found_comment[:-1]] = found_color_sequence[2:]
    return regex_dict, theme_dict


def coloring(regexes, themes, s):
    """Print highlighted regex matches in source to stdout.

    Regex matches inside other regex matches will be highlighted.

        Args:
            regexes (dict): Names as key, regexes as value.
            themes (dict): Names as key, colors as value.
            s (str): String to be highlighted.

    """

    # Get regex match positions:
    positions = []
    end_color = '0'     # Could alternatively be input in theme file.
    for name, pattern in regexes.items():
        start_color = themes[name]
        for match in re.finditer(
                pattern, s, re.MULTILINE):
            positions.append((match.span(), (start_color, end_color)))
    positions = sorted(positions)

    color_positions = []
    for i in range(len(positions)):
        (p_start, p_end), (c_start, c_end) = positions[i]
        # Check if span is inside other span:
        for (_, p_), (c_, _) in reversed(positions[0:i]):
            if p_ > p_end:
                c_end = c_
                break
        color_positions.append((p_start, c_start))
        color_positions.append((p_end, c_end))

    cp = sorted(color_positions)
    parts = ["\033[{}m".format(i[1]) + s[i[0]:j[0]]
             for i, j in zip(cp, cp[1:] + [(None, None)])]

    print(s[0:cp[0][0]] + ''.join(parts))


if __name__ == "__main__":
    regexes, themes = get_syntax_and_theme(sys.argv[1], sys.argv[2])
    with open(sys.argv[3], 'r') as infile:
        s = infile.read()
    coloring(regexes, themes, s)
