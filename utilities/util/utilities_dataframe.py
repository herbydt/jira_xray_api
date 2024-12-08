import numpy as np


def filter_by_col_values(df, *args):
    filtered_data = df
    for value in args:
        filtered_data = filtered_data[np.isin(filtered_data[value[0]], value[1])]
    return filtered_data

def get_result_generic(data, result_column, *args):
    try:
        filtered_data = data
        for value in args:
            filtered_data = filtered_data[filtered_data[value[0]] == value[1]]
        return filtered_data[result_column].values[0]
    except IndexError:
        return 0.00
    except KeyError:
        return 0.00