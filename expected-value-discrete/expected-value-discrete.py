import numpy as np

def expected_value_discrete(x, p):
    """
    Returns: float expected value
    """
    x=np.array(x)
    p=np.array(p)

    if x.shape != p.shape:
        raise ValueError("Shapes of x and p must match")
        
    if (1-np.sum(p) > 0.000001):
        raise ValueError("probabilities don't sum to 1")


    return np.sum(x*p)
        
