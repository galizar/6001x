def mult(a, b):
    if b == 1: # base case
        return a
    else:
        return a + mult(a, b - 1) # recursive step
