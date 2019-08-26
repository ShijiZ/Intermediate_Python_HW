import numpy as np

def list_is_in(list1, list2):
    '''
    returns a list that contains boolean values showing whether element in
    list1 is shown in list2.

    Parameters
    ----------
    list1 : list
        the target list to be checked
    
    list2 : list
        the whitelist
        
    Returns
    -------
    is_in : list
        the list showing whether element in list1 is shown in list2.
    '''

    set2 = set(list2)
    is_in = []
    for i in list1:
        if i in set2:
            is_in.append(True)
        else:
            is_in.append(False)
    return is_in


def mean_normalize(array):
    '''
    returns the normalized array of the temperature data with reference
    to each station.

    Parameters
    ----------
    array : 2d_array
        the original array of the temperature data, in which each column
        is a different weather stations, and each row is an hourly 
        temperature measurement.
        
    Returns
    -------
    normalized_array : 2d_array
        the normalized array, in which each data is calculated by subtracting
        the mean of the temperature data for each station from that stations 
        data, and then divided by the stations std
    '''

    std_array = np.std(array, axis=0)
    mean_array = np.mean(array, axis=0)
    normalized_array = (array - mean_array)/std_array
    return normalized_array


class temperature_model:
    '''
    A class to model temperature file

    Parameters
    ----------
    filepath : str
        the file path to the target file
    '''

    def __init__(self, filepath):
        self.filepath = filepath
        self.my_array = np.loadtxt(filepath, delimiter=',')
    
    def mean_normalize(self):
        '''
        returns the normalized array of the temperature data with reference
        to each station.
        '''
        my_array_T = self.my_array.T
        std_array_T = np.std(my_array_T, axis=0)
        mean_array_T = np.mean(my_array_T, axis=0)
        normalized_array_T = (my_array_T - mean_array_T)/std_array_T
        normalized_array = normalized_array_T.T

        return normalized_array