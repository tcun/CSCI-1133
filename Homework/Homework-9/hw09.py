def total_hours(fname, employee):
    '''
    Purpose: Gives the total hours worked according to the person and .csv file 
    Input Parameters: 
        fname (string): Name of the file (.csv)
        employee (string): Whichever employee that needs to be checked   
    Return Value: Returns the key associated with the employee name in employee_dict, which is there total hours
    '''
    
    employee_dict = {}
    try:
        with open(fname, 'r') as fp:
            text_list = fp.readlines()
        
            for i in range(1, len(text_list)):
                name_and_hour = text_list[i].split(",")
                employee_dict[name_and_hour[0]] = 0
            for i in range(1, len(text_list)):
                name_and_hour = text_list[i].split(",")
                employee_dict[name_and_hour[0]] += int(name_and_hour[1])
            
        try:
            return(employee_dict[employee])
        except KeyError:
            return 0
    except FileNotFoundError: 
        return -1

# print(total_hours('hours2.csv', 'Dean'))

def add_docstring(fname):
    '''
    Purpose: To add placeholder documentation right after every defintion of a function
    Input Parameters: 
        fname (string): name of file 
    Return Value: the number of times the placeholder was added
    '''
    docstring ="    '''\n    Purpose: FILL ME IN\n    Input Parameters: FILL ME IN\n    Return Value: FILL ME IN    \n    '''\n"
    try:
        counter = 0
        with open(fname, "r") as fn:
            with open("docstring_" + fname, "w") as fp:
                lines = fn.readlines()
                for i in range(len(lines)):
                    line = lines[i]
                    fp.write(line)
                    try:
                        if line[0:3] == "def":
                            fp.write(docstring)
                            # print(lines)
                            counter += 1
                    except IndexError:
                        pass
        return counter
    except FileNotFoundError: 
        return -1

# add_docstring("foo.py")
# add_docstring("queue_things.py")
add_docstring("nested_loop.py")

def  widen_model(fname_in, fname_out):
    '''
    Purpose: To widen an .obj by a factor of 2 
    Input Parameters: 
        fname_in (string): name of the original file 
        fname_out (string): name of the new widened file 
    Return Value: Returns the number of times each vertices that was edited 
    '''
    try:
        counter = 0
        with open(fname_in, 'r') as fp:
            vertices_and_faces = fp.readlines()
            
            for i in range(len(vertices_and_faces)):
                indexes = vertices_and_faces[i].split()
                if indexes[0] == 'v':
                    indexes[1] = str(float(indexes[1])*2)
                    vertices_and_faces[i] = ' '.join(indexes) + "\n"
                    counter += 1
            with open(fname_out, 'w') as fp:
                fp.writelines(vertices_and_faces)
                fp.close()
        return counter
    except FileNotFoundError: 
        return -1

widen_model('triforce.obj', 'triforce_widened.obj')