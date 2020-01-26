import sys


def diff(original_file, modified_file):
    """Compare two files and print differences to stdout and file.

    The results will be saved to 'diff_output.txt'.

    The first file will be viewed as the original file, while the
    second will be checked for changed compared to the first file. If
    a line has been deleted a '- ' will be added to the line. If a line
    has been added it will be printed with a '+ '. If a line is not
    changed at all a '0 ' will be added.

    Args:
        original_file (str): Path to original file.
        modified_file (str): Path to the file to be checked.
    """
    o_list = []
    m_list = []
    with open(original_file, 'r') as o_file:
        o_list = o_file.readlines()
    with open(modified_file, 'r') as m_file:
        m_list = m_file.readlines()

    with open("diff_output.txt", "w") as diff_out:
        i = 0   # Line index original file.
        g = 0   # Counts removed lines in modified file.
        for i in range(len(o_list)):
            if(i <= len(m_list)):
                if o_list[i] == m_list[i-g]:
                    print("0 ", o_list[i])
                    diff_out.write("0 " + o_list[i])

                elif not o_list[i] in m_list:
                    print("- ", o_list[i])
                    diff_out.write("- " + o_list[i])
                    g += 1
                elif not m_list[i] in o_list:
                    print("+ ", m_list[i])
                    diff_out.write("+ " + m_list[i])
                else:
                    print("- ", o_list[i])
                    print("+ ", m_list[i])
                    diff_out.write("- " + o_list[i])
                    diff_out.write("+ " + m_list[i])

        if i <= len(m_list):
            for k in range(i, len(m_list)):
                if not m_list[k] in o_list:
                    print("+ ", m_list[k])
                    diff_out.write("+ " + m_list[k])


if __name__ == "__main__":
    diff(sys.argv[1], sys.argv[2])
