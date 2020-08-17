from sys import argv

prev_MOUTH = int(0)
prev_VALUE = float(0)
prev_exists_count = int(0)

frame_count = int(0)

with open(argv[1], 'r') as input:
    with open(f'{argv[1][:-4]}_convert.csv', 'w') as output:
        while True:
            line1 = input.readlines(1)
            line2 = input.readlines(1)
            print(line1)
            
            if line1[0] == '#end\n':
                break
                
            elif line1[0] != '#end':
            
                time_leadin = line1[0].split('(')
                time_fix = time_leadin[1].split(')')
                
                mouth_anim_leadin = line2[0].split('(')
                mouth_anim_values = mouth_anim_leadin[1].split(',')
                mouth_anim_end_fix = mouth_anim_values[4].split(')')
                
                ID = mouth_anim_values[2]
                Raw_Trans = mouth_anim_values[3]
                Raw_Value = mouth_anim_end_fix[0]
                Raw_Time = time_fix[0]
                Frame = int(int(Raw_Time) * 60 / 100000)
                Trans = int(int(int(Raw_Trans) / 10) / 2)
                Value = float(int(Raw_Value) / 1000)
                
                
                if prev_exists_count == 0:
                    output.write(f'{ID},{Frame},{float(0)}\n')
                    output.write(f'{ID},{Frame + Trans},{float(Value)}\n')
                    prev_MOUTH = int(ID)
                    prev_VALUE = float(Value)
                    prev_FRAME = int(Frame)
                    prev_exists_count = 1
                        
                    frame_count += 1
                    
                elif prev_exists_count == 1:
                    if ID == prev_MOUTH:
                        output.write(f'{prev_MOUTH},{Frame},{prev_VALUE}\n')
                        output.write(f'{prev_MOUTH},{Frame + Trans},{Value}\n')
                    
                        frame_count += 2
                    elif ID != prev_MOUTH:
                        output.write(f'{prev_MOUTH},{Frame},{prev_VALUE}\n')
                        output.write(f'{prev_MOUTH},{Frame + Trans},0.0\n')
                        output.write(f'{ID},{Frame},{float(0)}\n')
                        output.write(f'{ID},{Frame + Trans},{float(Value)}\n')
                    
                        frame_count += 4
                    
                    prev_MOUTH = int(ID)
                    prev_VALUE = float(Value)
                    prev_FRAME = int(Frame)