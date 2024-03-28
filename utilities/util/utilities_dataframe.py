import numpy as np


def filter_by_col_values(df, *args):
    filtered_data = df
    for value in args:
        filtered_data = filtered_data[np.isin(filtered_data[value[0]], value[1])]
    return filtered_data

