from sys import argv

with open(argv[1], 'r', encoding='UTF-8') as input:
    with open(argv[2], 'w', encoding='Shift-JIS') as output:
        for line in input:
            data = line.split(',')
            expression = int(data[0])
            if len(data) == 3: #which it always is
                if expression == 3: #which it always is
                    data[0] = 'まばたき'
                    output.write(f'{data[0]},{data[1]},{data[2]}')