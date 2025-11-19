import pandas as pd

def calculate_demographic_data():
    # Read data from file
    df = pd.read_csv("adult.data.csv")

    # 1. Count of each race
    race_count = df['race'].value_counts()

    # 2. Average age of men
    average_age_men = round(df[df['sex'] == 'Male']['age'].mean(), 1)

    # 3. Percentage with Bachelor's degree
    percentage_bachelors = round((df['education'] == 'Bachelors').mean() * 100, 1)

    # 4. Advanced education filter
    advanced_education = ['Bachelors', 'Masters', 'Doctorate']
    higher_edu = df[df['education'].isin(advanced_education)]
    lower_edu = df[~df['education'].isin(advanced_education)]

    # 5. Percentage of >50K earners with advanced education
    higher_edu_rich = round((higher_edu['salary'] == '>50K').mean() * 100, 1)

    # 6. Percentage of >50K earners without advanced education
    lower_edu_rich = round((lower_edu['salary'] == '>50K').mean() * 100, 1)

    # 7. Minimum hours per week
    min_hours = df['hours-per-week'].min()

    # 8. Percentage of >50K earners among those who work min hours
    min_workers = df[df['hours-per-week'] == min_hours]
    rich_min_workers = round((min_workers['salary'] == '>50K').mean() * 100, 1)

    # 9. Country with highest % of >50K earners
    country_salary_ratio = df[df['salary'] == '>50K']['native-country'].value_counts() / df['native-country'].value_counts()
    highest_earning_country = country_salary_ratio.idxmax()
    highest_earning_country_percentage = round(country_salary_ratio.max() * 100, 1)

    # 10. Most popular occupation for >50K earners in India
    top_IN_occupation = df[(df['native-country'] == 'India') & (df['salary'] == '>50K')]['occupation'].value_counts().idxmax()

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_edu_rich,
        'lower_education_rich': lower_edu_rich,
        'min_work_hours': min_hours,
        'rich_percentage_min_hours': rich_min_workers,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage': highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }