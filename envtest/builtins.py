import numpy as np
from scipy.ndimage import gaussian_filter
from scipy import misc
import pandas as pd  

__all__ = ['rand_array', 'smooth_image', 'my_mat_solve', 'summarize_csv']


def rand_array(shape):
    return np.random.rand(*shape)

def smooth_image(a, sigma=1):
    return gaussian_filter(a, sigma=sigma)

def my_mat_solve(A, b):
    return A.inv()*b

def summarize_csv(file_path):
    """
    Reads a CSV file and returns a summary of its contents.
    
    Args:
        file_path (str): The path to the CSV file.
        
    Returns:
        dict: A dictionary containing the summary (count, mean, std, etc.)
    """
    df = pd.read_csv(file_path)
    
    # Return a summary of the DataFrame
    return {
        'columns': df.columns.tolist(),
        'count': df.count().to_dict(),
        'mean': df.mean(numeric_only=True).to_dict(),
        'std': df.std(numeric_only=True).to_dict(),
    }
