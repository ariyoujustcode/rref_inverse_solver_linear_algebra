
"""
Ari Marine
Professor Wang
Math3326
Bonus Points: Inverse of Matrix
"""

import numpy as np

# Function to calculate inverse
def inverse_matrix(A):
    try:
        # Attempt to calculate the inverse
        A_inv = np.linalg.inv(A)
        return A_inv
    except np.linalg.LinAlgError:
        # This will occur if the matrix is singular (not invertible)
        return "Matrix is not invertible."

# Function to take user input for the matrix
def get_user_matrix():
    try:
        n = int(input("Enter the size of the square matrix (n x n): "))
        print(f"Enter the {n}x{n} matrix values row by row, separated by spaces:")
        matrix = []
        for i in range(n):
            row = list(map(float, input(f"Row {i+1}: ").split()))
            if len(row) != n:
                raise ValueError(f"Row {i+1} must have {n} elements.")
            matrix.append(row)
        return np.array(matrix)
    except ValueError as e:
        print(f"Input Error: {e}")
        return None

if __name__ == "__main__":
    A = get_user_matrix()
    
    if A is not None:
        print("\nMatrix A:")
        print(A)
        print("\nInverse of A:")
        result = inverse_matrix(A)
        if isinstance(result, str):
            print(result)  # Matrix is not invertible
        else:
            print(result)
