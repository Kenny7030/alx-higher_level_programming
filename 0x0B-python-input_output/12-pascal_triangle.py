#!/usr/bin/python3
"""This module defines a Pascal's Triangle function."""


def pascal_triangle(n):
    """Generates Pascal's Triangle of size n as a list of lists."""
    if n <= 0:
        return []

    triangles = [[1]]  # Initialize with the first row [1]
    
    while len(triangles) != n:
        last_row = triangles[-1]  # Get the last row in the triangle
        new_row = [1]  # Initialize a new row with the first element as 1
        
        # Generate the new row by summing adjacent elements from the last row
        for i in range(len(last_row) - 1):
            new_row.append(last_row[i] + last_row[i + 1])
        
        new_row.append(1)  # Add the last element as 1
        
        triangles.append(new_row)  # Add the new row to the triangle
        
    return triangles

