import codecs

with codecs.open('template.svg','r','utf8') as file:
    card_template = file.read()
    

with codecs.open('students.txt', 'r', 'utf8') as file:
    students = file.readlines()


cnt = 1
for name in students:
    card_file_name = 'guest-{}.svg'.format(cnt)
    cnt = cnt+1
    
    with codecs.open(card_file_name, 'w', 'utf8') as file:
        file.write(card_template.replace('NAME', name))
    
    print('File {} created.'.format(card_file_name))
