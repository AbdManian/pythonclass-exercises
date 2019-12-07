########################################################################
# Calculate number of required carpet rolls and total price based on 
#   cut list in "sample.txt"
#
# Format of file is  x y [Optional comment]
#   X is width of the room (in meter)
#   Y is Height of the room (in meter)
#   All text after Y is comment (Information about the room for example)
#   Also lines start with '#' consider as comment and will be ignored
# Note: White spaces are allowed in the file
########################################################################



# Target carpet specifications (format is meter and Toman)
carpet_roll_length = 10
carpet_roll_width = 1.5
carpet_price_per_m2 = 74000


# Open the cut-list file 
cut_list_file = open('sample.txt', 'r')

# Read all lines from cut_list_file
cut_list_lines = cut_list_file.readlines()

# Convert file lines to the list of (x, y) values 
cut_list = []
for _line in cut_list_lines:
    line = _line.strip()

    if line and not line.startswith('#'):
        items = line.split()
        cut_list.append(
            (float(items[0]), float(items[1])) )

# Cut list is ready. Perform the calculations:

###########################################################################################
########## Place your code here ###########################################################

total_area = 0
for x, y in cut_list:
    area = x * y
    total_area += area
print(total_area)

roll_area = carpet_roll_length * carpet_roll_width

print("roll area = {}".format(roll_area))


num_rolls = 
