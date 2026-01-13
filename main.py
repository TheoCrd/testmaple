import numpy as np

def calculate_statistics(data):
    """Calculate basic statistics: mean, median, and standard deviation."""
    mean = np.mean(data)
    median = np.median(data)
    std_dev = np.std(data)
    return mean, median, std_dev