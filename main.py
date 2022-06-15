#!/opt/homebrew/bin/python3

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import requests
# matplotlib inline

def get_nba_data():
    api_url = 'https://www.balldontlie.io/api/v1/players'
    params = {
        'per_page': 100
    }
    x = requests.get(api_url, params = params).json()
    return x

nba_player_data = get_nba_data()['data']
nba_df = pd.DataFrame(nba_player_data)
# breakpoint()

# sample_df = pd.read_csv('sample-data.csv')
# breakpoint()

np.random.seed(42)
x = np.random.normal(size=1000)

plt.hist(nba_df['height_feet'], density=True, bins=2)  # density=False would make counts
# plt.ylabel('height_inches')
# plt.xlabel('height_feet')
plt.show(block = True)