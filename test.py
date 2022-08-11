import csv


def parse_line(lines: list[str]):
    return lines[2]


def write_error_file(path: str, line: str):
    with open(path, "a") as f:
        f.write(line)
        f.write("\n")


with open("data.csv") as f:
    for line in csv.reader(f):
        try:
            print(parse_line(line))
        except:
            write_error_file("error.txt", ",".join(line))
            continue
