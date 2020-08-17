from sys import argv

with open(argv[1], 'r', encoding='UTF-8') as input:
    with open(argv[2], 'w', encoding='Shift-JIS') as output:
        for line in input:
            data = line.split(',')
            if len(data) == 3: #which it always is
                expression = int(data[0])
                if expression == 0:
                    data[0] = '悲しい'
                    output.write(f'{data[0]},{data[1]},{data[2]}')
                if expression == 1:
                    data[0] = '笑い'
                    output.write(f'{data[0]},{data[1]},{data[2]}')
                if expression == 3:
                    data[0] = 'ぴっくり'
                    output.write(f'{data[0]},{data[1]},{data[2]}')
                if expression == 5:
                    data[0] = '感嘆'
                    output.write(f'{data[0]},{data[1]},{data[2]}')
                if expression == 6:
                    data[0] = 'アイスマイル'
                    output.write(f'{data[0]},{data[1]},{data[2]}')
                if expression == 8:
                    data[0] = '眩しい'
                    output.write(f'{data[0]},{data[1]},{data[2]}')
                if expression == 10:
                    data[0] = '強い'
                    output.write(f'{data[0]},{data[1]},{data[2]}')
                if expression == 11:
                    data[0] = '明確にする'
                    output.write(f'{data[0]},{data[1]},{data[2]}')
                if expression == 12:
                    data[0] = '優しい'
                    output.write(f'{data[0]},{data[1]},{data[2]}')
                if expression == 13:
                    data[0] = 'ながし'
                    output.write(f'{data[0]},{data[1]},{data[2]}')
                if expression == 15:
                    data[0] = 'キリッ'
                    output.write(f'{data[0]},{data[1]},{data[2]}')
                if expression == 16:
                    data[0] = 'ウツロ'
                    output.write(f'{data[0]},{data[1]},{data[2]}')
                if expression == 17:
                    data[0] = '考える'
                    output.write(f'{data[0]},{data[1]},{data[2]}')
                if expression == 18:
                    data[0] = 'せつな'
                    output.write(f'{data[0]},{data[1]},{data[2]}')
                if expression == 19:
                    data[0] = '元気'
                    output.write(f'{data[0]},{data[1]},{data[2]}')
                if expression == 20:
                    data[0] = 'ヤル'
                    output.write(f'{data[0]},{data[1]},{data[2]}')
                if expression == 22:
                    data[0] = 'まばたき'
                    output.write(f'{data[0]},{data[1]},{data[2]}')
                if expression == 34:
                    data[0] = 'クール'
                    output.write(f'{data[0]},{data[1]},{data[2]}')
                if expression == 36:
                    data[0] = 'くもん'
                    output.write(f'{data[0]},{data[1]},{data[2]}')
                if expression == 37:
                    data[0] = 'くつう'
                    output.write(f'{data[0]},{data[1]},{data[2]}')
                if expression == 38:
                    data[0] = 'なき'
                    output.write(f'{data[0]},{data[1]},{data[2]}')
                if expression == 39:
                    data[0] = 'なやみ'
                    output.write(f'{data[0]},{data[1]},{data[2]}')
                if expression == 40:
                    data[0] = 'ぴっくり２'
                    output.write(f'{data[0]},{data[1]},{data[2]}')
                if expression == 42:
                    data[0] = 'ウィンク２'
                    output.write(f'{data[0]},{data[1]},{data[2]}')
                if expression == 43:
                    data[0] = 'ｳｨﾝｸ２右'
                    output.write(f'{data[0]},{data[1]},{data[2]}')
                if expression == 44:
                    data[0] = 'ウィンク'
                    output.write(f'{data[0]},{data[1]},{data[2]}')
                if expression == 45:
                    data[0] = 'ウィンク右'
                    output.write(f'{data[0]},{data[1]},{data[2]}')