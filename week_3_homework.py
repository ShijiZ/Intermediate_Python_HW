def all_the_kwags(**kwags):
    '''Returns the number of keyword arguments passed.

    Parameters
    ----------
    **kwags : keyword arguments
        any number of keyword arguments
    
    Returns
    -------
    result : int
        number of keyword arguments passed.
    
    '''

    result = len(kwags)   
    return result


def almost_fibonacci(N):
    '''Generate the Fibonacci series starting at 0 and 1.
    
    Parameters
    ----------
    N : int
        specifiy the first N numbers of the fibonacci-like sequence
    
    Yields
    -------
    i : int
        the numbers of the fibonacci-like sequence
    
    '''

    # We start by seeding 0, 1 and i as the first three numbers
    i_prev_prev, i_prev, i = 0, 1, 1
    yield i_prev_prev  # we yield 0 first
    yield i_prev       # then yield 1
    # now in the following loop, we yield "i" and then calculate i_next by
    # summing the two previous
    for _ in range(N-2):
        yield i
        # we use tuple unpacking to update the variables in one line. This way
        # we do not need to define an i_next variable.
        i, i_prev, i_prev_prev = i + i_prev + i_prev_prev, i, i_prev


def first_word_of_each_line(filepath):
    """Generate the first word from each line of the file
    
    Parameters
    ----------
    filepath : string
        the file path of the target file
    
    Yields
    -------
    first_word : string
        the first word of any line in the file

    """
    
    # First, open the file
    with open(filepath, 'r') as my_file:
        # Loop through the lines
        for line in my_file:
            line = line.strip()  # strip whitespace from the line
            words = line.split()  # split the line into words

            if len(words) > 0: # non-empty line
                first_word = words[0]
                yield first_word
            else: # empty line
                continue 
