names = [
    'Abd',
    'Hassan',
    'Mohammad',
    'Javad',
    'Maryam',
    'Jack'
]

with open('sample.txt', 'w') as f:
    for name in names:
        f.write("{}\n".format(name))


