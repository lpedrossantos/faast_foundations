import argparse
from life_expectancy.region import Region
from life_expectancy.strategy_clean import StrategyClean
from life_expectancy.strategy_filter import StrategyFilter
from life_expectancy.strategy_load import StrategyLoad
from life_expectancy.strategy_save import StrategySave
from life_expectancy.context import Context

def main() -> None:
    """
    This function executes the main steps of
    the script:
    1st: Defines the parser and region argument
    2nd: Loads the data
    3rd: Cleans the Data
    4th: Saves the data
    """
    parser = argparse.ArgumentParser(description='input users.')
    parser.add_argument('--region', action='store', default=Region.PT)
    parser.add_argument('--file_path', action='store', default='./data/eu_life_expectancy_raw.tsv')
    parser.add_argument('--clean', action='store', default='y')
    args, _ = parser.parse_known_args()

    #Define Context
    context = Context()

    #Load Data
    context.set_strategy(StrategyLoad())
    df = context.run_strategy(input_path=args.file_path)

    #Clean Data
    if args.clean == 'y':
        context.set_strategy(StrategyClean())
        df = context.run_strategy(input_dataframe=df)

    #Filter Data
    context.set_strategy(StrategyFilter())
    df_filtered = context.run_strategy(input_dataframe=df, input_region=args.region)

    #Save Data
    context.set_strategy(StrategySave())
    context.run_strategy(
        input_dataframe=df_filtered, 
        input_path=f'./data/{args.region.lower()}_life_expectancy.csv'
    )

if __name__ == "__main__": # pragma: no cover
    main()
