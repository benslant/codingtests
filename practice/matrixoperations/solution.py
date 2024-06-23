from typing import List
from dataclasses import dataclass
import numpy as np

@dataclass
class IncrementOp():
    row: int
    col: int

def matrixoperations(n_rows: int, m_columns: int, increment_ops: List[IncrementOp]) -> int:
    matrix = np.array([([0] * m_columns)]*n_rows)
    for op in increment_ops:
        for row in range(op.row):
            for col in range(op.col):
                matrix[row, col] += 1 
    np.unique(matrix, return_counts=True)
    values, counts = np.unique(matrix, return_counts=True)
    max = values[counts == counts.max()]

    for idx, count in enumerate(counts):
        if values[idx] > 0: return values[idx]
    raise