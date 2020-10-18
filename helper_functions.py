from math import sqrt

# This will serve as an estimation of the distance from florianópolis to other cities
def heuristic_value():
    lst = []
    lst = [0, 7.9, 17.4, 15.3, 31.2, 40.7, 42.6, 46.3, 44.1, 23.4,
    42.8, 46.4, 28.6, 25.4, 24.8]
    return lst


# Ditance from cities to neihgbor
def calculate_connections():
    lst  = [[10], [10, 6.9, 23.9, 24.2, 16.9],[13.9, 24.5, 6.9], [29.3, 16.9, 15.7, 31.7],
    [29.3, 32.4], [32.4, 31.7, 14.7],[14.7,10.2], [10.2, 25.6], [25.6, 27],[24.2, 9.8, 34.2, 15.7],[27.1, 14.6, 27, 34.2],
     [26.9, 14.6],[6.2, 26.9, 22.9], [24.5, 19, 22.9, 27.1, 9.8, 23.9],[13.9,6.2,19]]
    return lst
