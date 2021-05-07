from p_wrangling.m_wrangling import wrangling
from p_reporting.m_reporting import stack_filter, profile_filter, level_filter, location_filter
from p_analysis.m_analysis import analysis
import warnings
warnings.filterwarnings("ignore")

def main():
    wrangling()

    analysis()

    first_filter = list(map(str, input("Choose technology/technologies: ").strip().split()))
    stack_filter(first_filter)

    second_filter = input("Choose profile: ")
    profile_filter(second_filter)

    third_filter = input("Choose level: ")
    level_filter(third_filter)

    fourth_filter = input("Choose location: ")
    location_filter(fourth_filter)

    print("You'll find your requested dataframe in 'results' folder. Thank you!")


if __name__ == '__main__':
    main()