import numpy as np

def covariance_matrix(X: list) -> np.ndarray:
    """
    Returns the covariance matrix as a NumPy array.
    """
    # Write code here
    X = np.array(X,dtype = float)
    means = np.mean(X,axis = 0)
    centered = X - means
    cov_mat = (centered.T @ centered)/(X.shape[0] - 1)
    return cov_mat