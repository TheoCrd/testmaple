import numpy as np

def calculate_statistics(data):
    """Calculate basic statistics: mean, median, and standard deviation."""
    mean = np.mean(data)
    median = np.median(data)
    std_dev = np.std(data)
    return mean, median, std_dev


if __name__ == "__main__":
    sample_data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    mean, median, std_dev = calculate_statistics(sample_data)
    print(f"Mean: {mean}, Median: {median}, Standard Deviation: {std_dev}")