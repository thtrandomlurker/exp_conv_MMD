from sys import argv

with open(argv[1], 'r', encoding='UTF-8') as input:
    with open(argv[2], 'w', encoding='Shift-JIS') as output:
        for line in input:
            data = line.split(',')
            mouth = int(data[0])
            if mouth == 0:
                data[0] = 'あ'
                output.write(f'{data[0]},{data[1]},{data[2]}')
            if mouth == 1:
                data[0] = 'え'
                output.write(f'{data[0]},{data[1]},{data[2]}')
            if mouth == 10:
                data[0] = 'い'
                output.write(f'{data[0]},{data[1]},{data[2]}')
            if mouth == 2:
                data[0] = 'お'
                output.write(f'{data[0]},{data[1]},{data[2]}')
            if mouth == 11:
                data[0] = 'う'
                output.write(f'{data[0]},{data[1]},{data[2]}')
            if mouth == 8:
                data[0] = 'dummy'
                output.write(f'{data[0]},{data[1]},{data[2]}')