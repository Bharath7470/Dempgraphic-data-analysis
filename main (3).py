# main.py
from demographic_data_analyzer import calculate_demographic_data

if __name__ == "__main__":
    result = calculate_demographic_data()
    for key, value in result.items():
        print(f"{key}:\n{value}\n")