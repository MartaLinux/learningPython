def split_and_join(line):
    # write your code here
    line_str = line.split(" ")
    line_str = "-".join(line)
    return line.replace(" ", "-")

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)