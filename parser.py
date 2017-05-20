from datastruct import titled_list

def parse_file(fd):
    return_list = []

    firstline = fd.readline()
    firstline = strip_and_split(firstline)
    for variable in firstline :
        return_list.append(titled_list(variable))
    
    lines = fd.readlines()

    for line in lines :
        line = strip_and_split(line)
        for idx, struct in enumerate(return_list) :
            struct.addItem(int(line[idx]))
    
    return return_list

def strip_and_split(line):
    line = line.rstrip('\n')
    line = line.split('\t')
    return line