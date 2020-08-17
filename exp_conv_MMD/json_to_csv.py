import json
import os
from sys import argv

count = int(0)
frame_count = int(0)

prev_exists_count = 0

with open(argv[1], 'r') as input:
    data = json.load(input)
    max = len(data['Dex'])
    
    prev_EXP = int(0)
    prev_VALUE = float(0)
    prev_FRAME = int(0)
    
    while True:
        vmd_str = """\
"""
        if count > int(max - 1):
            break
        elif count <= int(max - 1):
            for i in data['Dex'][count]['Main']:
                Frame = i['F']
                ID = i['I']
                Value = i['V']
                Trans = i['T']
            
                if prev_exists_count == 0:
                    vmd_str += f'{ID},{Frame},{float(Value)}\n'
                    prev_EXP = int(ID)
                    prev_VALUE = int(Value)
                    prev_FRAME = int(Frame)
                    prev_exists_count = 1
                    
                    frame_count += 1
                
                elif prev_exists_count == 1:
                    if ID == prev_EXP:
                        vmd_str += f'{prev_EXP},{Frame},{prev_VALUE}\n'
                        vmd_str += f'{prev_EXP},{Frame + Trans},{Value}\n'
                    
                        frame_count += 2
                    elif ID != prev_EXP:
                        vmd_str += f'{prev_EXP},{Frame},{prev_VALUE}\n'
                        vmd_str += f'{prev_EXP},{Frame + Trans},0.0\n'
                        vmd_str += f'{ID},{Frame},{float(0)}\n'
                        vmd_str += f'{ID},{Frame + Trans},{float(Value)}\n'
                    
                        frame_count += 4
                    
                    prev_EXP = ID
                    prev_VALUE = Value
                    prev_FRAME = Frame
            
            vmd_str += '0\n'
                
            vmd_str += 'cut & paste these lines at the top, then delete this line\n'
            vmd_str += 'Vocaloid Motion Data 0002,0\n'
            vmd_str += 'FlyingSpirits Model\n'
            vmd_str += '0\n'
            vmd_str += f'{frame_count}\n'
        
            with open(f'{argv[1][:-5]}_index({count})_Main.csv', 'w') as output:
                output.write(vmd_str)
        
            count += 1
            
count = int(0)
frame_count = int(0)

prev_exists_count = 0

with open(argv[1], 'r') as input:
    data = json.load(input)
    max = len(data['Dex'])
    
    prev_EXP = int(0)
    prev_VALUE = float(0)
    prev_FRAME = int(0)
    
    while True:
        vmd_str = """\
"""
        if count > int(max - 1):
            break
        elif count <= int(max - 1):
            for i in data['Dex'][count]['Eyes']:
                Frame = i['F']
                ID = i['I']
                Value = i['V']
                Trans = i['T']
            
                if prev_exists_count == 0:
                    vmd_str += f'{ID},{Frame},{float(Value)}\n'
                    prev_EXP = int(ID)
                    prev_VALUE = int(Value)
                    prev_FRAME = int(Frame)
                    prev_exists_count = 1
                    
                    frame_count += 1
                
                elif prev_exists_count == 1:
                    if ID == prev_EXP:
                        vmd_str += f'{prev_EXP},{Frame},{prev_VALUE}\n'
                        vmd_str += f'{prev_EXP},{Frame + Trans},{Value}\n'
                    
                        frame_count += 2
                    elif ID != prev_EXP:
                        vmd_str += f'{prev_EXP},{Frame},{prev_VALUE}\n'
                        vmd_str += f'{prev_EXP},{Frame + Trans},0.0\n'
                        vmd_str += f'{ID},{Frame},{float(0)}\n'
                        vmd_str += f'{ID},{Frame + Trans},{float(Value)}\n'
                    
                        frame_count += 4
                    
                    prev_EXP = ID
                    prev_VALUE = Value
                    prev_FRAME = Frame
            
            vmd_str += '0\n'
                
            vmd_str += 'cut & paste these lines at the top, then delete this line\n'
            vmd_str += 'Vocaloid Motion Data 0002,0\n'
            vmd_str += 'FlyingSpirits Model\n'
            vmd_str += '0\n'
            vmd_str += f'{frame_count}\n'
        
            with open(f'{argv[1][:-5]}_index({count})_Eyes.csv', 'w') as output:
                output.write(vmd_str)
        
            count += 1
        
        