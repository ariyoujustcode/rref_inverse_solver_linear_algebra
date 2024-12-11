"""
Ari Marine
Professor Wang
Math3326
Bonus Points RREF
"""


def rowReduceEF(matrix):
    rowCount = len(matrix)
    columnCount = len(matrix[0])
    lead = 0

    for r in range(rowCount):
        if lead >= columnCount:
            return matrix
        i = r
        while matrix[i][lead] == 0:
            i += 1
            if i == rowCount:
                i = r
                lead += 1
                if lead == columnCount:
                    return matrix
        # Swap rows i and r
        matrix[i], matrix[r] = matrix[r], matrix[i]

        # Normalize row r
        pivotValue = matrix[r][lead]
        matrix[r] = [rowElement / float(pivotValue) for rowElement in matrix[r]]

        # Make other rows have 0 in the lead column
        for i in range(rowCount):
            if i != r:
                pivotValue = matrix[i][lead]
                matrix[i] = [
                    iv - pivotValue * rowValue
                    for rowValue, iv in zip(matrix[r], matrix[i])
                ]
        lead += 1

    return matrix


def printMatrix(matrix):
    for row in matrix:
        print([round(x, 2) for x in row])


def getMatrixFromUser():
    """Get matrix dimensions"""
    rows = int(input("Enter the number of rows: "))
    cols = int(input("Enter the number of columns: "))

    # Create an empty matrix
    matrix = []

    # Get each row
    for i in range(rows):
        print(f"Enter row {i + 1} (space-separated values):")
        row = list(
            map(float, input().split())
        )  # Convert input string to list of floats

        # Alert user to enter correct number of columns
        if len(row) != cols:
            print(f"Error: You must enter exactly {cols} values for this row.")
            return None

        # Add row to matrix
        matrix.append(row)

    return matrix


if __name__ == "__main__":
    matrix = getMatrixFromUser()

    if matrix:
        print("\nOriginal Matrix:")
        printMatrix(matrix)

        matrix = rowReduceEF(matrix)

        print("\nRREF of the Matrix:")
        printMatrix(matrix)
