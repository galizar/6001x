def lessThan4(aList):
    '''
    aList: a list of strings
    '''
    return [item for item in aList if len(item) < 4]

if __name__ == '__main__':
    assert lessThan4(['hola', 'sol', 'aloa', 'ello', 'govnor', 'lua']) == ['sol', 'lua']
    assert lessThan4(['hola', 'aloa', 'govnor']) == []
    assert lessThan4(['hola', 'aloa', 'lua', 'ello']) == ['lua']


