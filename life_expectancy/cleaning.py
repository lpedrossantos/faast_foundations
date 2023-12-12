import argparse
import pandas as pd

parser = argparse.ArgumentParser(description='filters data by region.')
parser.add_argument('--region', action='store', default='PT')
args, _ = parser.parse_known_args()

def clean_data(region=args.region):
    """
    This function loads and cleans the data from eu_life_expectancy_raw dataset and saves the cleaned dataset on the data folder.
    By default filters for the PT region but it can also be filter for another region by passing the command line argument --region
    
    Args:
        region: Type of Country to filter dataset
    
    Returns:
        None
    """
    data = pd.read_csv(
        './life_expectancy/data/eu_life_expectancy_raw.tsv', 
        sep= r'\,|\t', 
        header=0, 
        engine='python'
    )

    data = data.melt(id_vars=['unit', 'sex', 'age', 'geo\\time'])

    data = data.rename(columns={'geo\\time' : 'region', 'variable': 'year'})

    data.value = data.value.apply(lambda x: None if ':' in x else x)
    data.value = data.value.str.replace(r'[^0-9.]', '', regex=True)

    data = data.astype({'year': int, 'value': float})

    data = data.dropna()

    data_only_pt = data[data['region'] == region]

    data_only_pt.to_csv('./life_expectancy/data/pt_life_expectancy.csv', index=False)

if __name__ == "__main__": # pragma: no cover
    clean_data()
