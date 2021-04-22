def join(queue, student):
    '''
    Purpose: FILL ME IN
    Input Parameters: FILL ME IN
    Return Value: FILL ME IN    
    '''
    queue.append(student)
    print(student, "has joined the queue.")

def kick(queue):
    '''
    Purpose: FILL ME IN
    Input Parameters: FILL ME IN
    Return Value: FILL ME IN    
    '''
    next = queue.pop(0)
    print(next+", it is your turn.")

def position(queue, student):
    '''
    Purpose: FILL ME IN
    Input Parameters: FILL ME IN
    Return Value: FILL ME IN    
    '''
    print(student, "is in position", queue.index(student)+1)
    return None

def display(queue):
    '''
    Purpose: FILL ME IN
    Input Parameters: FILL ME IN
    Return Value: FILL ME IN    
    '''
    place = 1
    for student in queue:
        print(place, student)
        place += 1
