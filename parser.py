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
        for variable in range(0, len(return_list)) :
            return_list[variable].addItem(int(line[variable]))
    


    for variable in range(0, len(return_list)) :
        print return_list[variable].title
        print return_list[variable].mylist
    
    return return_list

def strip_and_split(line):
    line = line.rstrip('\n')
    line = line.split('\t')
    return line