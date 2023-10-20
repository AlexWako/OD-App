def remove_link(file):
    with open(file, 'r') as file:
        lines = file.readlines()
    lines = lines[:-1]
    return lines

def get_link(file):
    with open(file, 'r') as file:
        lines = file.readlines()
    return lines[-1]

def remove_new_line(pagelist):
    return_list = []
    for i in range(len(pagelist)):
        return_list.append(pagelist[i].replace("\n", ""))
    return return_list
