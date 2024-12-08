def replace_nan_values(value):
    if str(value) != 'nan':
        value = str(value)
    else:
        value = ''
    return value
