import pandas as pd
from p_wrangling.m_wrangling import suitable_skills

def stack_filter(tech):
    main_df = pd.read_csv('results/complete_df.csv')

    main_df['suitable'] = main_df['stack'].apply(lambda x: suitable_skills(x, tech))

    tech_found = main_df[main_df['suitable'] == True]
    tech_found.drop(columns=['suitable'], inplace=True)

    if len(tech_found) > 1:
        tech_found_df = tech_found.to_csv('data/tech_filter_df.csv', index=False)
        return tech_found_df
    if len(tech_found) < 1:
        raise ValueError("Sorry, we don't have people here! Check your search")

def profile_filter(profile):
    tech_df = pd.read_csv('data/tech_filter_df.csv')

    for i in tech_df['profile']:
        if profile.lower() in i.lower():
            profile_found = tech_df[tech_df['profile'] == i]
            profile_found_df = profile_found.to_csv('data/profile_filter_df.csv', index=False)
            return profile_found_df
        elif profile == 'all':
            profile_found_df = tech_df.to_csv('data/profile_filter_df.csv', index=False)
            return profile_found_df
    else:
        raise ValueError('Please choose a valid profile (programmer, analyst/programmer, testing, mobile, data...)')

def level_filter(level):
    profile_df = pd.read_csv('data/profile_filter_df.csv')

    for i in profile_df['level']:
        if level in i:
            level_found = profile_df[profile_df['level'] == i]
            level_found_df = level_found.to_csv('data/level_filter_df.csv', index=False)
            return level_found_df
        elif level == 'all':
            level_found_df = tech_df.to_csv('data/level_filter_df.csv', index=False)
            return level_found_df
    else:
        raise ValueError('Please choose a valid level (junior, senior, expert or all)')

def location_filter(city):
    level_df = pd.read_csv('data/level_filter_df.csv')
    for i in level_df['location']:
        if city in i:
            city_found = level_df[level_df['location'] == i]
            city_found_df = city_found.to_csv('data/filtered_df.csv', index=False)
            return city_found_df
        elif city == 'all':
            city_found_df = level_df.to_csv('results/filtered_df.csv', index=False)
            return city_found_df
    else:
        raise ValueError("We don't have people in this location, please choose another one")

def reporting():

    stack_filter()
    profile_filter()
    level_filter()
    location_filter()