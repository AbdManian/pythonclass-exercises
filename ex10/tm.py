import sys


def user_interface():
    if len(sys.argv) < 3:
        print(
            "Invalid number of arguments.\n"
            "Usage: tmaker.py InputFile ColumnNum\n")
        exit(-1)

    file_name, column_num = sys.argv[1:3]


    try:
        column_num = int(column_num)
    except ValueError:
        print("Invalid column number!")
        exit(-1)

    try:
        with open(file_name, 'r') as f:
            lines = f.readlines()
    except FileNotFoundError:
        print("File not found!")
        exit(-1)

    return column_num, lines, file_name


def group_list(l, group_num):
    res = []
    for _ in range(group_num):
        res.append([])

    for i, data in enumerate(l):
        res[i % group_num].append(data)

    return res


def divide_list(l, div_num):
    cnt = (len(l) + div_num - 1)//div_num
    res = []
    for i in range(cnt):
        res.append(l[i*div_num:(i+1)*div_num])
    return res


def create_row(row_list, size_list):
    res = []
    for r in row_list:
        row = []
        for i, data in enumerate(r):
            row.append(data.ljust(size_list[i]))
        res.append("".join(row))
    return res


def max_len(str_list):
    return max(map(lambda x: len(x), str_list))


column_num, lines, file_name = user_interface()


#  Strip strings, Filter Comments remove empty text lines

lines = map(lambda x: x.strip(), lines)
lines = filter(lambda x: not x.startswith('#'), lines)
lines = list(filter(None, lines))

columns = group_list(lines, column_num)
rows = divide_list(lines, column_num)

columns_size = list(map(max_len, columns))


with open(file_name + '.table', 'w') as f:
    for x in create_row(rows, columns_size):
        f.write(x + '\n')
        print(x)

