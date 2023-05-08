import pandas as pd

CSV_FILE_PATH = 'data/original_data.csv'
NULL_CHECK_COL = 'country'

def load_data(file_path: str) -> pd.DataFrame:
    """Loads data from a CSV file and returns a pandas dataframe."""
    df = pd.read_csv(file_path)
    df['reg_date'] = pd.to_datetime(df['registration_date']).dt.date
    return df

def find_no_reg_dates(df: pd.DataFrame) -> list:
    """Finds dates with no new registrations."""
    min_dt = df['reg_date'].min()
    max_dt = df['reg_date'].max()
    date_range = pd.date_range(min_dt, max_dt)
    no_reg_dates = [date.date() for date in date_range if df[df['reg_date'] == date.date()].empty]
    return no_reg_dates

def has_no_reg_dates(df: pd.DataFrame) -> bool:
    """Checks if the dataset has dates without new registration"""
    return bool(find_no_reg_dates(df))

def count_no_reg_dates(df: pd.DataFrame) -> int:
    """Counts the dates without registration"""
    return int(len(find_no_reg_dates(df)))

def calculate_null_percentage(df: pd.DataFrame, column: str) -> float:
    """Calculates the percentage of null values in a column."""
    num_null_values = df[column].isna().sum()
    total_rows = df.shape[0]
    null_percentage = (num_null_values / total_rows) * 100
    return null_percentage

def has_less_than_5_percent_null(df: pd.DataFrame, column: str) -> bool:
    """Checks if a column has less than 5% null values."""
    null_percentage = calculate_null_percentage(df, column)
    return null_percentage < 5


def main() -> None:
    try:
        df = load_data(CSV_FILE_PATH)

        has_no_reg_dates_bool = has_no_reg_dates(df)

        if has_no_reg_dates_bool:
            no_reg_dates_cnt = count_no_reg_dates(df)
            print(f'There are {no_reg_dates_cnt} days without new registrations.')
        else:
            print("There were new registrations every day.")

        null_percentage = calculate_null_percentage(df, NULL_CHECK_COL)
        has_less_than_5_pct_null = has_less_than_5_percent_null(df,NULL_CHECK_COL)

        if has_less_than_5_pct_null:
            print(f'{NULL_CHECK_COL} column has less than 5% null values.')
        else:
            print(f'The {NULL_CHECK_COL} column has 5 or more percentage null values -> {null_percentage}%')

    except Exception as e:
        print("An error occurred:", e)

if __name__ == '__main__':
    main()
