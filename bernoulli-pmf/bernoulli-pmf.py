import numpy as np

def bernoulli_pmf_and_moments(x: list, p: float) -> dict:
    """
    Returns a dictionary with pmf, mean, and variance.
    """
    pmf = []

    for val in x:
        if val == 0:
            pmf.append(float(1 - p))
        else:
            pmf.append(float(p))

    return {
        "pmf": np.array(pmf),
        "mean": float(p),
        "variance": float(p * (1 - p))
    }