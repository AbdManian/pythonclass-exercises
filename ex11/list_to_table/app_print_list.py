import print_list

def file_to_list(filename):
    with open(filename, 'r') as f:
        lines = f.readlines()
    
    lines = list(map(str.strip, lines))

    return lines

if __name__ == '__main__':

    names = file_to_list('sample_data.txt')
    table = print_list.list_to_table(names)
    for l in table:
        print(l)