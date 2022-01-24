#!/usr/bin/python3
import numpy as np

"""
Multiply 2 matrix using Numpy
"""

def lazy_matrix_mul(m_a, m_b):
    """
    Multiply 2 array using Numpy
    Args:
        m_a (list of list): Matrix one.
        m_b (list of list): Matrix two.
    """
    return np.matmul(m_a, m_b)
