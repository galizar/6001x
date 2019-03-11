def flatten(aList):
    '''
    aList: a list
    Returns a copy of aList, which is a flattened version of aList
    '''
    lelist = []
    for item in aList:
        if type(item) == list:
            lelist += flatten(item)
        else:
            lelist.append(item)
    return lelist

if __name__ == '__main__':
    assert flatten([['hola', 'ciao'], 'sayonara', ['ello', ['hallo', ['bonjour']]]]) == ['hola', 'ciao', 'sayonara', 'ello', 'hallo', 'bonjour']
