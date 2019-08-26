import math

def count_uppercase_letters(my_string):
    '''Returns the number of uppercase letters in a given string.

    Parameters
    ----------
    my_string : string
        this input string
    
    Returns
    -------
    upper_count : int
        number of uppercase letters in the string
    
    '''

    upper_count = 0
    for letter in my_string:
        if letter.istitle():
            upper_count += 1
    
    return upper_count


def interleave_lists(list_1, list_2):
    '''Interleave the items of 2 lists with the same length

    Parameters
    ----------
    list_1 : list
        this is the first input list
    
    list_2 : list
        this is the second input list

    Returns
    -------
    result : list
        result list generated
    
    '''

    result = []
    for i in range(len(list_1)):
        result.append(list_1[i])
        result.append(list_2[i])
    return result


def cylinder_stats(radius, height):
    '''Returns the surface area and the volume of a cylinder
    given its radius and height

     Parameters
    ----------
    radius : int, float
        this is the radius of the cylinder
    
    height : int, float
        this is the height of the cylinder

    Returns
    -------
    surface_area : int, float
        this is the surface area of the cylinder

    volume : int, float
        this is the volume of the cylinder
    
    '''

    surface_area = 2 * math.pi * radius * (height + radius)
    volume = math.pi * radius**2 * height
    return surface_area, volume