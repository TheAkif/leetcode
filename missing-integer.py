def missingInteger(A):
    """_summary_

    Args:
        A (_type_): _description_
    """

    A = sorted([x for x in A if x > 0])
    
    x = 1

    for i in range(0,len(A)):
        if(x < A[i]):
            return x
        x = A[i] + 1
    
    return x
