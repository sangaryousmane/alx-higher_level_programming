#!/usr/bin/python3
def matrix_mul(m_a, m_b):
    """
    This function takes two matrices, m_a and m_b, and returns their product.
    The matrices must be validated with the following requirements:
    - m_a and m_b must be a list of lists of integers or floats.
    - If m_a or m_b is not a list, it raises a TypeError
    - If m_a or m_b is not a list of lists, it raises a TypeError
    - If m_a or m_b is empty (it means: = [] or = [[]]), it raises a ValueError
    - If m_a and m_b can’t be multiplied, it raises a ValueError

    Args:
      m_a (list): The first matrix.
      m_b (list): The second matrix.

    Returns:
      list: The product of m_a and m_b.
    """
    if not isinstance(m_a, list) or not isinstance(m_b, list):
        raise TypeError("m_a must be a list or m_b must be a list")
    if not all(isinstance(row, list) for row in m_a):
        raise TypeError("m_a must be a list of lists")
    if not all(isinstance(row, list) for row in m_b):
        raise TypeError("m_b must be a list of lists")
    if m_a == [] or m_a == [[]]:
        raise ValueError("m_a can't be empty")
    if m_b == [] or m_b == [[]]:
        raise ValueError("m_b can't be empty")
    if not all(isinstance(num, (int, float)) for r in m_a for num in r):
        raise TypeError("m_a should contain only integers or floats")
    if not all(isinstance(num, (int, float)) for r in m_b for num in r):
        raise TypeError("m_b should contain only integers or floats")
    if not all(len(row) == len(m_a[0]) for row in m_a):
        raise TypeError("each row of m_a must be of the same size")
    if not all(len(row) == len(m_b[0]) for row in m_b):
        raise TypeError("each row of m_b must be of the same size")
    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    result = [[0 for _ in range(len(m_b[0]))] for _ in range(len(m_a))]
    for i in range(len(m_a)):
        for j in range(len(m_b[0])):
            for k in range(len(m_b)):
                result[i][j] += m_a[i][k] * m_b[k][j]
    return result
