# datasci_9_data_pre

HHA 507 Assignment #9

# Data Cleaning and Transformation Plan

## Description of the Datasets

The NYPD Complaint Data Dataset contains all valid felony, misdemeanor, and violation crimes reported to the New York City Police Department (NYPD) for all complete quarters so far this year (2023). There are a total of 36 columns with ~415,000 rows of data. Some examples of the columns are borough name (of where the incident occurred), complaint day (the day the complaint was made), complaint time (the time the complaint was made), level of offense, and demographic information about the victim and suspect. This dataset contains string, integers, floats, and data & time. 

- Independent / Predictor variables: borough, jurisdiction, law category, location of crime, offense description, victim age
- Dependent / Target variables: victim race

The Student Weight Status Category Reporting Dataset contains weight status category data (underweight, healthy weight, overweight or obese, based on BMI-for-age percentile). The dataset includes separate estimates of the percent of students overweight, obese and overweight or obese for all reportable grades within the county and/or region and by grade groups (elementary and middle/high). There are a total of 15 columns with ~32,000 rows of data. Some examples of the columns are number of students overweight, number of students obese, grade level, and sex. This dataset contains string, integers, and floats.

- Independent / Predictor variables: county, grade category, sex
- Dependent / Target variables: number of obese students

## Intended Learning Task

Both datasets were intended to be used for regression.

## Steps to Clean and Transform Data

1. Remove any white space or special characters
2. Drop columns that are not going to be used
3. Identify any rows with missing data and drop those rows
4. Check that the data types of each column are correct (make sure that categorical columns are converted into string)
5. Detect any outliers that are part of the dataset. Determine what to do with the outliers depending on how they affect the rest of the dataset.

## Documentation of Steps to Clean and Transform Data

1. Uploaded the dataset into the repository
2. Converted the .csv file into a .pkl file
3. Removed white spaces and special columns that were in the column names
4. Dropped columns that had a lot of missing values because that would affect my interpretation of the data. I also dropped columns that I believed had similar information to another column; there's no reason to have more than one column with the same information.
5. Identified rows that had missing information like "(null)" or "NaN" and dropped them from the dataset
6. Checked that the data types were accurate for each column, especially in ensuring that categorical columns were converted into objects
7. Used an Ordinal Encoder code for each of the columns to create .csv files where each unique value was given a number to correspond to
8. Scaled the data using ```scaler.transform(X)```
9. Split the data into train, test, and value
10. Created a baseline model using DummyClassifier
11. Created a logistic regression models with the train and value variables from the data splitting step
