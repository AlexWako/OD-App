def create_file_int_list(file, list):
    with open(file, 'w') as file:
        for item in list:
            if item != None:
                file.write(str(item) + "\n")
            else:
                continue
    file.close()
    return True

def update_file_int_list(file, list):
    with open(file, 'a') as file:
        for item in list:
            if item != None:
                file.write(str(item) + "\n")
            else:
                continue
    file.close()
    return True

def remove_lines(file, lines = 1):
    with open(file, 'r') as file:
        lines = file.readlines()
    with open(file, 'w') as file:
        lines = lines[:-(lines)]
        file.write(lines)
    file.close()
    return True