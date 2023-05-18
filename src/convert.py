from os.path import splitext

def convert_gcode(gcode_file):
    '''
    create a new gcode file which only contains move instructions.
    
    gcode_file: path to gcode file to be converted.
    
    returns:
        path to new gcode file.
    '''
    # load g code file and read line by line
    # pick only G1 instructions.
    filename=splitext(gcode_file)[0]
    gcode = []
    with open(gcode_file, 'r') as f:
        for line in f:
            if line.startswith('G1 '):
                gcode.append(line)
                
    # save the g code file as a new file
    with open(f"{filename}_converted.g", 'w') as f:
        for line in gcode:
            f.write(line)

    return f"{filename}_converted.g"