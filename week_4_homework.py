def raise_to_power(n):
    '''returns a function that will raise any number to the nth power.

    Parameters
    ----------
    n : int, float
        the power
    
    Returns
    -------
    power_func : function
        the function hat will raise any number to the nth power
    
    '''

    def power_func(x):
        '''returns the nth power of x.

        Parameters
        ----------        
        x : int, float
            the base
    
        Returns
        -------
        result : int, float
            the nth power of x
        '''
        result = x**n
        return result
    
    return power_func


def file_writer(filepath):
    '''return a function that will write a string to filepath
    
    Parameters
    ----------
    filepath : str
        the filepath that will be created and appended
    
    Returns
    -------
    write_to_file : function
        the function that will write a string to filepath  
    
    '''

    def write_to_file(string):
        '''write string to filepath specified by file_writer()
        
        Parameters
        ----------
        string : str
            the contents that will be appended to filepath
        
        Returns
        -------
        None
        
        '''

        with open(filepath, 'a') as my_file:
            my_file.write(string)
    
    return write_to_file


def word_n_of_each_line(n):
    '''Returns a generator function that generate the nth word from each line of the file.
    
    Parameters
    ----------
    n : int
        specify the nth word to be generated
    
    Returns
    -------
    lines_of_the_file : function
        the generator function that generate the nth word from each line of the file
    '''

    def lines_of_the_file(filepath):
        '''Generate the nth word from each line of the file
    
        Parameters
        ----------
        filepath : string
            the file path of the target file

        Yields
        -------
        nth_word : string
            the nth word of any line in the file
        '''

        # First, open the file
        with open(filepath, 'r') as my_file:
            # Loop through the lines
            for line in my_file:
                line = line.strip()  # strip whitespace from the line
                words = line.split()  # split the line into words
                if len(words) >= n: # non-empty line
                    nth_word = words[n-1]
                    yield nth_word
                else: # empty line
                    continue
    
    return lines_of_the_file