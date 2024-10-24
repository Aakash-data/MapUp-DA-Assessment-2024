{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "d62e9097-1b74-4431-8719-244c3280da03",
   "metadata": {},
   "outputs": [],
   "source": [
    "def reverse_by_n(lst, n):\n",
    "    result = []\n",
    "    i = 0\n",
    "    while i < len(lst):\n",
    "        \n",
    "        group = []\n",
    "        for j in range(min(n, len(lst) - i)):\n",
    "            group.append(lst[i + j])\n",
    "        \n",
    "        result.extend(group[::-1])\n",
    "        i += n\n",
    "    return result\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "ed4b2fa0-d250-4859-a757-0d1764aaa9ce",
   "metadata": {},
   "outputs": [],
   "source": [
    "def reverse_by_n(lst, n):\n",
    "    result = []\n",
    "    i = 0\n",
    "    while i < len(lst):\n",
    "        \n",
    "        group = []\n",
    "        for j in range(min(n, len(lst) - i)):\n",
    "            group.append(lst[i + j])\n",
    "        \n",
    "        result.extend(group[::-1])\n",
    "        i += n\n",
    "    return result\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "70f0ec11-535c-4999-a6fd-875d44530e4e",
   "metadata": {},
   "outputs": [],
   "source": [
    "def flatten_dict(d, parent_key='', sep='.'):\n",
    "    items = []\n",
    "    for k, v in d.items():\n",
    "        new_key = f\"{parent_key}{sep}{k}\" if parent_key else k\n",
    "        if isinstance(v, dict):\n",
    "            items.extend(flatten_dict(v, new_key, sep=sep).items())\n",
    "        elif isinstance(v, list):\n",
    "            for i, item in enumerate(v):\n",
    "                items.extend(flatten_dict(item, f\"{new_key}[{i}]\", sep=sep).items())\n",
    "        else:\n",
    "            items.append((new_key, v))\n",
    "    return dict(items)\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "e099c2da-884b-4c9a-8478-be161812edfe",
   "metadata": {},
   "outputs": [],
   "source": [
    "from itertools import permutations\n",
    "\n",
    "def unique_permutations(lst):\n",
    "    return [list(p) for p in set(permutations(lst))]\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "7a06699d-2cf2-419b-ae90-ef534c2d87a3",
   "metadata": {},
   "outputs": [],
   "source": [
    "import re\n",
    "\n",
    "def find_all_dates(text):\n",
    "\n",
    "    date_pattern = r'\\b\\d{2}-\\d{2}-\\d{4}\\b|\\b\\d{2}/\\d{2}/\\d{4}\\b|\\b\\d{4}\\.\\d{2}\\.\\d{2}\\b'\n",
    "    return re.findall(date_pattern, text)\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "0b1be2e0-41b0-48b6-8c09-713af1446209",
   "metadata": {},
   "outputs": [],
   "source": [
    "import polyline\n",
    "import pandas as pd\n",
    "from geopy.distance import geodesic\n",
    "\n",
    "def decode_polyline_to_df(polyline_str):\n",
    "    \n",
    "    coordinates = polyline.decode(polyline_str)\n",
    "   \n",
    "    df = pd.DataFrame(coordinates, columns=['latitude', 'longitude'])\n",
    "    \n",
    "    distances = [0]\n",
    "    for i in range(1, len(df)):\n",
    "        point1 = (df.loc[i-1, 'latitude'], df.loc[i-1, 'longitude'])\n",
    "        point2 = (df.loc[i, 'latitude'], df.loc[i, 'longitude'])\n",
    "        distances.append(geodesic(point1, point2).meters)\n",
    "    df['distance'] = distances\n",
    "    return df\n",
    "\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "06e7e7c0-46ab-47c4-9e4c-5279465cd683",
   "metadata": {},
   "outputs": [],
   "source": [
    "def rotate_and_transform(matrix):\n",
    "    n = len(matrix)\n",
    "    rotated = [[matrix[n-j-1][i] for j in range(n)] for i in range(n)]\n",
    "    \n",
    "    transformed = []\n",
    "    for i in range(n):\n",
    "        row = []\n",
    "        for j in range(n):\n",
    "            row_sum = sum(rotated[i]) + sum(rotated[k][j] for k in range(n)) - 2 * rotated[i][j]\n",
    "            row.append(row_sum)\n",
    "        transformed.append(row)\n",
    "    return transformed\n",
    "\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "2d5d4059-2c5c-48e1-956b-471e0e957947",
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd\n",
    "\n",
    "def check_time_coverage(df):\n",
    "    \n",
    "    df['start'] = pd.to_datetime(df['startDay'] + ' ' + df['startTime'])\n",
    "    df['end'] = pd.to_datetime(df['endDay'] + ' ' + df['endTime'])\n",
    "    \n",
    "    results = df.groupby(['id', 'id_2']).apply(lambda g: check_full_coverage(g))\n",
    "    return results\n",
    "\n",
    "def check_full_coverage(group):\n",
    "    pass\n"
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
