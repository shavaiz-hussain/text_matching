import re
import shutil

import numpy as np


# LEVENSTAIN
def levenshtein_ratio_and_distance(s, t):
    rows = len(s) + 1
    cols = len(t) + 1
    distance = np.zeros((rows, cols), dtype=int)
    for i in range(1, rows):
        for k in range(1, cols):
            distance[i][0] = i
            distance[0][k] = k

    for col in range(1, cols):
        for row in range(1, rows):
            if s[row - 1] == t[col - 1]:
                cost = 0  # SAME CHARACTER
            else:
                cost = 2  # SAME CHARACTER
            distance[row][col] = min(
                distance[row - 1][col] + 1,  # DELETE
                distance[row][col - 1] + 1,  # INSERT
                distance[row - 1][col - 1] + cost,
            )

    # CALCULATE DISTANCE TOTALS
    ratio = ((len(s) + len(t)) - distance[rows - 1][cols - 1]) / (len(s) + len(t))
    return ratio if ratio <= 0 else round(ratio * 100)
