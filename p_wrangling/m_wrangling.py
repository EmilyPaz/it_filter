import pandas as pd
import re

def upgrading_dataset():
    """
    creating new column, reordering columns and showing up the largest strings
    """
    encoded_data = pd.read_csv('data/encoded_data.csv')

    levels = []

    for i in encoded_data['experience'].astype('float'):
        if i <= 2.5:
            levels.append('junior')
        elif i > 2.5 and i <= 7:
            levels.append('senior')
        elif i > 7:
            levels.append('expert')
        else:
            levels.append('undefined')

    encoded_data['level'] = levels

    cols = list(encoded_data.columns)
    cols = cols[-2:] + cols[:-2]
    encoded_data = encoded_data[cols]

    pd.set_option('display.max_colwidth', None)

    processed_df = encoded_data.to_csv('data/processed_df.csv', index=False)

    return processed_df

def suitable_skills(stack, tech):
    main_df = pd.read_csv('data/processed_df.csv')

    lst_stack = [i.lower() for i in main_df['stack']]
    main_df['stack'] = lst_stack

    main_df.to_csv('data/main_df.csv', index=False)

    for word in tech:
        rex = re.compile(f"\\b{word.lower()}\\b")
        result = len(rex.findall(stack.lower())) > 0
    if result:
        return True
    else:
        return False

def wrangling():
    upgrading_dataset()



