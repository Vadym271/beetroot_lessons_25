def count_lines(name):
    with open(name) as f:
        lines = f.readlines()
    return len(lines)

def count_chars(name):
    with open(name) as f:
        text = f.read()
    return len(text)

def test(name):
    lines_num = count_lines(name)
    char_num = count_chars(name)
    print(char_num, "chars")
    print(lines_num, "lines")

test("enter your file")
