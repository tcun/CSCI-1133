def anonymize(user, domain):
    '''
    Purpose: Partially replace the user portion of an email with ***** to add anonymize it
    Input Parameter(s): 
        user (String) is the name portion of the email
        domain (String) is the domain of the website that the email is associated with
    Return Value: Returns a string with '*****' between the first and last character of the user
    '''
    return user.replace(user[1:-1], '*****') + domain

def list_swap(vals, idx1, idx2):
    '''
    Purpose: Swap two index positions within a list
    Input Parameter(s): 
        vals (list) List of whatever values
        idx1 (integer) Position of the first index
        idx2 (integer) Position of the second index
    Return Value: returns the newly swapped vals list value
    '''
    temp = vals[idx1]
    vals[idx1] = vals[idx2]
    vals[idx2] = temp
    return vals

def codename(first, last, code):
    '''
    Purpose: To code an inputed first and last name into a given code 
    Input Parameter(s):
        first (String) First name 
        last (String) Last name
        code (Dictionary) Dictionary of letters accosiated with codes
    Return Value: Returns a string that has been coded using the last intials of each name 
    '''
    return code[first[-1]] + " " + code[last[-1]]

def cross(u, v):
    '''
    Purpose: To code an inputed first and last name into a given code 
    Input Parameter(s):
        u (List) List of first vector values
        v (List) List of second vector values
    Return Value: A new list of vectors after cross product
    '''
    x = 0
    y = 1
    z = 2
    return [(u[y]*v[z] - u[z]*v[y]), (u[z]*v[x] - u[x]*v[z]), (u[x]*v[y] - u[y]*v[x])]




