import pandas as pd

def calculate_distance_matrix(file_path):
    
    df = pd.read_csv(file_path)
    ids = sorted(df['id_start'].append(df['id_end']).unique())
    distance_matrix = pd.DataFrame(index=ids, columns=ids, data=float('inf'))
    for id_ in ids:
        distance_matrix.at[id_, id_] = 0
    for _, row in df.iterrows():
        id_start, id_end, distance = row['id_start'], row['id_end'], row['distance']
        distance_matrix.at[id_start, id_end] = distance
        distance_matrix.at[id_end, id_start] = distance  
    
    for k in ids:
        for i in ids:
            for j in ids:
                if distance_matrix.at[i, j] > distance_matrix.at[i, k] + distance_matrix.at[k, j]:
                    distance_matrix.at[i, j] = distance_matrix.at[i, k] + distance_matrix.at[k, j]
    
    return distance_matrix


def find_ids_within_ten_percentage_threshold(unrolled_df, reference_id):
    
    ref_distances = unrolled_df[unrolled_df['id_start'] == reference_id]['distance']
    avg_distance = ref_distances.mean()
    
    
    lower_threshold = avg_distance * 0.9
    upper_threshold = avg_distance * 1.1
    
    
    ids_within_threshold = unrolled_df[
        (unrolled_df['distance'] >= lower_threshold) & 
        (unrolled_df['distance'] <= upper_threshold)
    ]['id_start'].unique()
    
    return sorted(ids_within_threshold)


def calculate_toll_rate(unrolled_df):
    rate_coefficients = {
        'moto': 0.8,
        'car': 1.2,
        'rv': 1.5,
        'bus': 2.2,
        'truck': 3.6
    }
    
    for vehicle, rate in rate_coefficients.items():
        unrolled_df[vehicle] = unrolled_df['distance'] * rate
    
    return unrolled_df

import datetime

def calculate_time_based_toll_rates(toll_rate_df):
    
    weekday_discounts = [
        ((datetime.time(0, 0), datetime.time(10, 0)), 0.8),
        ((datetime.time(10, 0), datetime.time(18, 0)), 1.2),
        ((datetime.time(18, 0), datetime.time(23, 59, 59)), 0.8),
    ]
    weekend_discount = 0.7

    
    rows = []
    for _, row in toll_rate_df.iterrows():
        id_start, id_end = row['id_start'], row['id_end']
        for day in ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']:
            for (start_time, end_time), factor in (weekday_discounts if day in ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday'] else [(None, None, weekend_discount)]):
                adjusted_row = row.copy()
                adjusted_row['start_day'] = day
                adjusted_row['end_day'] = day
                adjusted_row['start_time'] = start_time if start_time else datetime.time(0, 0)
                adjusted_row['end_time'] = end_time if end_time else datetime.time(23, 59, 59)
                
                for vehicle in ['moto', 'car', 'rv', 'bus', 'truck']:
                    adjusted_row[vehicle] *= factor
                
                rows.append(adjusted_row)
    
    return pd.DataFrame(rows)