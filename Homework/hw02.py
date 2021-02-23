import math

#TODO: Fill out the Purpose, Input Parameter(s), and Return Value
# for each of the two functions below in comments, and then write
# additional functions for parts B and C, and fill out the same information
# for those functions as well.

#Remember, you must place a # before any comment, or it will be
# interpreted as Python code, and will probably cause errors.

# Example function for background reading

def nickels_to_cents(nickels):
    '''
    Purpose: Converts from a certain number of nickels to
            how many cents we have

    Input Parameter(s):
        nickels: The number of nickels we have

    Return Value:
        the amount of cents we have
    '''
    total_cents = nickels * 5
    return total_cents

# Part A: Two functions that you should add documentation to
def celsius_to_fahrenheit(celsius):
    '''
    Purpose: Converts degrees Celsius to degrees fahrenheit
    Input Parameter(s):
        celsius: Intial temperature
    Return Value:
        degrees in fahrenheit 
    '''
    fahr = (celsius * 9 / 5) + 32
    return fahr

def surface_area_sphere(radius):
    '''
    Purpose: Find the surface area of sphere
    Input Parameter(s):
        radius: the length from the center to the edge of the sphere
    Return Value:
        the total surface area of the sphere
    '''
    pi = 3.14159
    rsquared = radius * radius
    area = pi * 4.0 * rsquared
    return area

# Part B: Write out a few simple conversions

def circumference_circle(radius):
    '''
    Purpose: Find the circumferences of a circle
    Input Parameter(s):
        radius: the length from the center to the edge of the circle
    Return Value:
        circumference of the circle
    '''

    return 2 * math.pi * radius

def grams_to_ounces(grams):
    '''
    Purpose: Converts grams to ounces
    Input Parameter(s):
        grams: convert a certain amount of grams to ounces
    Return Value:
        total amount of ounces 
    '''

    return grams * 0.035274

def seconds_to_hours(seconds):
    '''
    Purpose: Converts seconds to hours 
    Input Parameter(s):
        seconds: convert a certain amount of seconds to hours
    Return Value:
        total amount of hours
    '''

    return seconds / 3600

# Part C: Calculate distance based on time and average speed

def calc_distance(minutes, speed):
    '''
    Purpose: Calculate the distanced traveled by using speed and time 
    Input Parameter(s):
        minutes: amounts of minutes traveled
        speed: magnitude of speed
    Return Value:
        the total distance traveled
    '''
    return (minutes / 60) * speed
