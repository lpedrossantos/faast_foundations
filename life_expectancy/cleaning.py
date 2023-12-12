import pandas as pd
import re

import argparse



parser = argparse.ArgumentParser(description='filters data by region.')
parser.add_argument('--region', action='store', default='PT')
args, _ = parser.parse_known_args()


def clean_data(region=args.region):
    data = pd.read_csv('./life_expectancy/data/eu_life_expectancy_raw.tsv', sep= '\,|\t', header=0, engine='python')
    data = data.melt(id_vars=['unit', 'sex', 'age', 'geo\\time'])
    data = data.rename(columns={'geo\\time' : 'region', 'variable': 'year'})
    data.value = data.value.apply(lambda x: None if ':' in x else x).str.replace(r'[^0-9.]', '', regex=True)
    data = data.astype({'year': int, 'value': float})
    data = data.dropna()
    data_only_pt = data[data['region'] == region]
    data_only_pt.to_csv('./life_expectancy/data/pt_life_expectancy.csv', index=False)



if __name__ == "__main__": # pragma: no cover
    clean_data()



