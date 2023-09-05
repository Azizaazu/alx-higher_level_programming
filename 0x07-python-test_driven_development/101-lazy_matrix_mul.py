#!/usr/bin/python3.5
""" Function multiplies 2 matrices """
import numpy as np

def lazy_matrix_mul(m_a, m_b):
    """ Multiplies 2 matrices

    Args:
        m_a: matrix a
        m_b: matrix b

    Returns:
        result of the multiplication
    """
    return (np.matmul(m_a, m_b))
