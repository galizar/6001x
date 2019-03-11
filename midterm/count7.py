def count7(N, count=0):
    '''
    N: a non-negative integer
    '''
    if N // 10 == 0:
        if N % 10 == 7:
            return count + 1
        return count

    elif N % 10 == 7:
        return count7(N // 10, count=count+1)

    else:
        return count7(N // 10, count=count)


if __name__ == '__main__':
    assert count7(567) == 1
    assert count7(333) == 0
    assert count7(452477) == 2
