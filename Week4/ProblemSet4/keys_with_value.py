def keysWithValue(aDict, target):
    '''
    aDict: a dictionary
    target: an integer
    '''
    ledict = {}
    for key, value in aDict.items():
        if value == target:
            ledict[key] = value
    ledict_sorted = sorted(ledict.items(), key=lambda x: x[0])
    return [x[0] for x in ledict_sorted]

if __name__ == '__main__':
    assert keysWithValue({3: 2, 2: 1, 7: 2}, 2) == [3, 7]
    assert keysWithValue({3: 1, 6: 3, 9: 4}, 2) == []
    assert keysWithValue({14: 7, 12: 4, 2: 5, 7: 14, 4: 5}, 14) == [7]

