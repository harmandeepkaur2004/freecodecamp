import pandas as pd

def demographic_data_analyzer():
    # Load the data
    df = pd.read_csv("adult.data.csv")

    # 1. Number of each race represented in this dataset
    race_count = df['race'].value_counts()

    # 2. Average age of men
    average_age_men = round(df[df['sex'] == 'Male']['age'].mean(), 1)

    # 3. Percentage with a Bachelor's degree
    percentage_bachelors = round((df['education'] == 'Bachelors').mean() * 100, 1)

    # 4. Percentage with higher education that earn >50K
    higher_education = df[df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])]
    lower_education = df[~df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])]

    higher_education_rich = round((higher_education['salary'] == '>50K').mean() * 100, 1)
    lower_education_rich = round((lower_education['salary'] == '>50K').mean() * 100, 1)

    # 5. Minimum number of hours a person works per week
    min_work_hours = df['hours-per-week'].min()

    # 6. Percentage of people working min hours who earn >50K
    num_min_workers = df[df['hours-per-week'] == min_work_hours]
    rich_percentage = round((num_min_workers['salary'] == '>50K').mean() * 100, 1)

    # 7. Country with highest % of >50K earners
    rich_country_counts = df[df['salary'] == '>50K']['native-country'].value_counts()
    total_country_counts = df['native-country'].value_counts()
    rich_country_percentage = (rich_country_counts / total_country_counts * 100).round(1)

    highest_earning_country = rich_country_percentage.idxmax()
    highest_earning_country_percentage = rich_country_percentage.max()

    # 8. Most popular occupation for those who earn >50K in India
    top_IN_occupation = df[(df['native-country'] == 'India') & (df['salary'] == '>50K')]['occupation'].value_counts().idxmax()

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage': highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }
