import numpy as np

def compute_r_squared(data, predictions):
    # Write a function that, given two input numpy arrays, 'data', and 'predictions,'
    # returns the coefficient of determination, R^2, for the model that produced 
    # predictions.
    # 
    # Numpy has a couple of functions -- np.mean() and np.sum() --
    # that you might find useful, but you don't have to use them.

    # YOUR CODE GOES HERE
    r_squared = 1 - np.sum((data - predictions)**2)/np.sum((data - np.mean(data))**2)

    return r_squared


if __name__ == '__main__':
    print compute_r_squared(np.array([1,2,3]), np.array([1, 2, 3]))
