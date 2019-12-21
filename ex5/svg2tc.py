# Convert SVG path to the Turtle Command format
import sys
import os
import xml.etree.ElementTree as ET

svg_file = 'Tracing.svg'
if len(sys.argv) >= 2:
    svg_file = sys.argv[1]

tree = ET.parse(svg_file)
root = tree.getroot()

tc_file = os.path.splitext(svg_file)[0] + '.tc'

path_list = []

for x in root:
    if 'path' in x.tag:
        path_list.append(x.attrib['d'])


f = open(tc_file, 'w')

for path in path_list:
    for cmd in path.split():
        if cmd.upper() in 'MHVL':
            f.write('\n')
        f.write(' ' + cmd)
    f.write('\n')

    
f.close()


print(tc_file)
