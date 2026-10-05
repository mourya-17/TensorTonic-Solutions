from collections import Counter
import numpy as np

def mean_median_mode(x: list) -> dict:
    """
    Returns a dictionary with mean, median, and mode.
    """
    mean_val = np.mean(x)
    median_val = np.median(x)

    count_val = Counter(x)
    mode_val = count_val.most_common(1)[0][0]

    return {
        "mean": float(mean_val),
        "median": float(median_val),
        "mode": float(mode_val)
    }