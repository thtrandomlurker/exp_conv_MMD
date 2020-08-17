from sys import argv

frame_count = int(0)

with open(argv[1], 'r', encoding='Shift-JIS') as input:
    with open(f'{argv[1][:-4]}_fixed.csv', 'w', encoding='Shift-JIS') as output:
        get_len = input.readlines()
        frame_count = int(len(get_len))
        
with open(argv[1], 'r', encoding='Shift-JIS') as input:
    with open(f'{argv[1][:-4]}_fixed.csv', 'w', encoding='Shift-JIS') as output:
        output.write('Vocaloid Motion Data 0002,0\n')
        output.write('MIKU\n')
        output.write('0\n')
        output.write(f'{frame_count}\n')
        for line in input:
            output.write(line)
            
        output.write('0\n')
        