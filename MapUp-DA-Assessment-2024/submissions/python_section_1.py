def reverse_by_n(lst, n):
    result = []
    i = 0
    while i < len(lst):
        
        group = []
        for j in range(min(n, len(lst) - i)):
            group.append(lst[i + j])
        
        result.extend(group[::-1])
        i += n
    return result

def reverse_by_n(lst, n):
    result = []
    i = 0
    while i < len(lst):
        
        group = []
        for j in range(min(n, len(lst) - i)):
            group.append(lst[i + j])
        
        result.extend(group[::-1])
        i += n
    return result

def flatten_dict(d, parent_key='', sep='.'):
    items = []
    for k, v in d.items():
        new_key = f"{parent_key}{sep}{k}" if parent_key else k
        if isinstance(v, dict):
            items.extend(flatten_dict(v, new_key, sep=sep).items())
        elif isinstance(v, list):
            for i, item in enumerate(v):
                items.extend(flatten_dict(item, f"{new_key}[{i}]", sep=sep).items())
        else:
            items.append((new_key, v))
    return dict(items)

from itertools import permutations

def unique_permutations(lst):
    return [list(p) for p in set(permutations(lst))]

import re

def find_all_dates(text):

    date_pattern = r'\b\d{2}-\d{2}-\d{4}\b|\b\d{2}/\d{2}/\d{4}\b|\b\d{4}\.\d{2}\.\d{2}\b'
    return re.findall(date_pattern, text)


import polyline
import pandas as pd
from geopy.distance import geodesic

def decode_polyline_to_df(polyline_str):
    
    coordinates = polyline.decode(polyline_str)
   
    df = pd.DataFrame(coordinates, columns=['latitude', 'longitude'])
    
    distances = [0]
    for i in range(1, len(df)):
        point1 = (df.loc[i-1, 'latitude'], df.loc[i-1, 'longitude'])
        point2 = (df.loc[i, 'latitude'], df.loc[i, 'longitude'])
        distances.append(geodesic(point1, point2).meters)
    df['distance'] = distances
    return df


def rotate_and_transform(matrix):
    n = len(matrix)
    rotated = [[matrix[n-j-1][i] for j in range(n)] for i in range(n)]
    
    transformed = []
    for i in range(n):
        row = []
        for j in range(n):
            row_sum = sum(rotated[i]) + sum(rotated[k][j] for k in range(n)) - 2 * rotated[i][j]
            row.append(row_sum)
        transformed.append(row)
    return transformed


import pandas as pd

def check_time_coverage(df):
    
    df['start'] = pd.to_datetime(df['startDay'] + ' ' + df['startTime'])
    df['end'] = pd.to_datetime(df['endDay'] + ' ' + df['endTime'])
    
    results = df.groupby(['id', 'id_2']).apply(lambda g: check_full_coverage(g))
    return results

def check_full_coverage(group):
    pass