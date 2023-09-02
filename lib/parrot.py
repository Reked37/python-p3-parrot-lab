def parrot(variable='no pass'):
    if variable == 'no pass':
        squawk = 'Squawk!'
        print(squawk)
        return squawk
    else:
        print(variable)
        return variable
