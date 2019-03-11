def isIn(char, aStr):
    '''
    char: a single character
    aStr: an alphabetized string
    returns: True if char is in aStr; False otherwise
    '''
    # Your code here

    len_o_str = len(aStr)
    middle_idx = len_o_str//2

    if (len_o_str == 1 and (char != aStr)) or not len_o_str:
        return False
    elif char == aStr[middle_idx]:
        return True
    elif char < aStr[middle_idx]:
        return isIn(char, aStr[:middle_idx])
    else:
        return isIn(char, aStr[middle_idx:])

lestr = 'fuyitokokoyama'

print(isIn('a', sorted(lestr)))
print(isIn('a', ''))
