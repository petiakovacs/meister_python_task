# Task

Write a Python script, with a README file where you:

- Test if the data of the previous table (or the augmented version of it) has any
days without new sign-ups

- Has less than 5% of null values in the country column

- Bonus: There's unit tests for the Python code

## Project structure

- **data** folder: contains the csv file
- **test_data** folder: in the data folder, contains the data for the unit tests


## Code Functionality

This project consists of two code files: `main.py` and `test_main.py`.

## Functions in main.py

`main.py` contains several functions that load data from a CSV file and perform some data analysis.

### `load_data(file_path: str) -> pd.DataFrame`

This function loads data from a CSV file and returns a Pandas DataFrame. It also adds a new column, `reg_date`, which is the `registration_date` column converted to a date format.

### `find_no_reg_dates(df: pd.DataFrame) -> list`

This function finds the dates with no new registrations in the DataFrame. It first determines the minimum and maximum registration dates, creates a date range from these dates, and then checks for each date in the range if there were any new registrations. The function returns a list of dates with no new registrations.

### `has_no_reg_dates(df: pd.DataFrame) -> bool`

This function returns True if there are dates in the DataFrame with no new registrations, and False otherwise. It makes use of the `find_no_reg_dates()` function.

### `count_no_reg_dates(df: pd.DataFrame) -> int`

This function returns the number of dates with no new registrations in the DataFrame. It also makes use of the `find_no_reg_dates()` function.

### `calculate_null_percentage(df: pd.DataFrame, column: str) -> float`

This function calculates the percentage of null values in a given column of the DataFrame.

### `has_less_than_5_percent_null(df: pd.DataFrame, column: str) -> bool`

This function returns True if a given column of the DataFrame has less than 5% null values, and False otherwise. It makes use of the `calculate_null_percentage()` function.

### `main() -> None`

This function is the entry point of the program. It loads the data from the CSV file using the `load_data()` function, checks if there are any dates with no new registrations using the `has_no_reg_dates()` function, and prints out the result. It also checks if the country column has less than 5% null values using the `has_less_than_5_percent_null()` function, and prints out the result.

## Functions in test_main.py

The test_main.py file contains unit tests for the functions in main.py.

### `setUp()`

The setUp() function sets up the test data by loading the test CSV files into Pandas DataFrames.

### `test_no_reg_dates()`

This test checks if the `has_no_reg_dates()` function correctly identifies dates with no new registrations in the test data.

### `test_reg_every_day()`

This test checks if the `has_no_reg_dates()` function correctly identifies that there are no dates with no new registrations in the test data where there were new registrations every day.

### `test_no_null_country()`

This test checks if the `has_less_than_5_percent_null()` function correctly identifies that the country column has less than 5% null values in the test data.

### `test_null_country()`

This test checks if the `has_less_than_5_percent_null()` function correctly identifies that the country column has 5% or more null values in the test data.

### `test_calculate_null_percentage()`\

This test checks if the `calculate_null_percentage()` function correctly calculates the percentage of null values in a given column of the test data.

## Test data

Test data were created in separate csv files, each file contains 5 rows.

- test_data_no_null_country.csv
  - Every country has value
- test_data_no_reg_every_day.csv
  - There are 2 dates without new registration
- test_data_null_countries.csv
  - 20% missing data in country column
- test_data_reg_every_day.csv
  - Data with registration every day