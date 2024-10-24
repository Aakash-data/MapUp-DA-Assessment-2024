{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "648703b8-da84-45d0-a551-f5903ee9702c",
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd\n",
    "\n",
    "def calculate_distance_matrix(file_path):\n",
    "    \n",
    "    df = pd.read_csv(file_path)\n",
    "    ids = sorted(df['id_start'].append(df['id_end']).unique())\n",
    "    distance_matrix = pd.DataFrame(index=ids, columns=ids, data=float('inf'))\n",
    "    for id_ in ids:\n",
    "        distance_matrix.at[id_, id_] = 0\n",
    "    for _, row in df.iterrows():\n",
    "        id_start, id_end, distance = row['id_start'], row['id_end'], row['distance']\n",
    "        distance_matrix.at[id_start, id_end] = distance\n",
    "        distance_matrix.at[id_end, id_start] = distance  \n",
    "    \n",
    "    for k in ids:\n",
    "        for i in ids:\n",
    "            for j in ids:\n",
    "                if distance_matrix.at[i, j] > distance_matrix.at[i, k] + distance_matrix.at[k, j]:\n",
    "                    distance_matrix.at[i, j] = distance_matrix.at[i, k] + distance_matrix.at[k, j]\n",
    "    \n",
    "    return distance_matrix\n",
    "\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "bd370781-ffe0-43ba-9bf9-c9b95f026424",
   "metadata": {},
   "outputs": [],
   "source": [
    "def find_ids_within_ten_percentage_threshold(unrolled_df, reference_id):\n",
    "    \n",
    "    ref_distances = unrolled_df[unrolled_df['id_start'] == reference_id]['distance']\n",
    "    avg_distance = ref_distances.mean()\n",
    "    \n",
    "    \n",
    "    lower_threshold = avg_distance * 0.9\n",
    "    upper_threshold = avg_distance * 1.1\n",
    "    \n",
    "    \n",
    "    ids_within_threshold = unrolled_df[\n",
    "        (unrolled_df['distance'] >= lower_threshold) & \n",
    "        (unrolled_df['distance'] <= upper_threshold)\n",
    "    ]['id_start'].unique()\n",
    "    \n",
    "    return sorted(ids_within_threshold)\n",
    "\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "687b7ef7-99fc-4611-a074-0c1f75dacc86",
   "metadata": {},
   "outputs": [],
   "source": [
    "def calculate_toll_rate(unrolled_df):\n",
    "    rate_coefficients = {\n",
    "        'moto': 0.8,\n",
    "        'car': 1.2,\n",
    "        'rv': 1.5,\n",
    "        'bus': 2.2,\n",
    "        'truck': 3.6\n",
    "    }\n",
    "    \n",
    "    for vehicle, rate in rate_coefficients.items():\n",
    "        unrolled_df[vehicle] = unrolled_df['distance'] * rate\n",
    "    \n",
    "    return unrolled_df\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "87443cc0-78f0-46be-9504-cdb388ec09b8",
   "metadata": {},
   "outputs": [],
   "source": [
    "import datetime\n",
    "\n",
    "def calculate_time_based_toll_rates(toll_rate_df):\n",
    "    \n",
    "    weekday_discounts = [\n",
    "        ((datetime.time(0, 0), datetime.time(10, 0)), 0.8),\n",
    "        ((datetime.time(10, 0), datetime.time(18, 0)), 1.2),\n",
    "        ((datetime.time(18, 0), datetime.time(23, 59, 59)), 0.8),\n",
    "    ]\n",
    "    weekend_discount = 0.7\n",
    "\n",
    "    \n",
    "    rows = []\n",
    "    for _, row in toll_rate_df.iterrows():\n",
    "        id_start, id_end = row['id_start'], row['id_end']\n",
    "        for day in ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']:\n",
    "            for (start_time, end_time), factor in (weekday_discounts if day in ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday'] else [(None, None, weekend_discount)]):\n",
    "                adjusted_row = row.copy()\n",
    "                adjusted_row['start_day'] = day\n",
    "                adjusted_row['end_day'] = day\n",
    "                adjusted_row['start_time'] = start_time if start_time else datetime.time(0, 0)\n",
    "                adjusted_row['end_time'] = end_time if end_time else datetime.time(23, 59, 59)\n",
    "                \n",
    "                for vehicle in ['moto', 'car', 'rv', 'bus', 'truck']:\n",
    "                    adjusted_row[vehicle] *= factor\n",
    "                \n",
    "                rows.append(adjusted_row)\n",
    "    \n",
    "    return pd.DataFrame(rows)\n",
    "\n"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
