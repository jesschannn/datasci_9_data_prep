# datasci_9_data_pre

HHA 507 Assignment #9

# Data Cleaning and Transformation Plan

## Description of the Datasets

The NYPD Complaint Data Dataset contains all valid felony, misdemeanor, and violation crimes reported to the New York City Police Department (NYPD) for all complete quarters so far this year (2023). There are a total of 36 columns with ~415,000 rows of data. Some examples of the columns are borough name (of where the incident occurred), complaint day (the day the complaint was made), complaint time (the time the complaint was made), level of offense, and demographic information about the victim and suspect. This dataset contains string, integers, floats, and data & time. 

- Independent / Predictor variables:
- Dependent / Target variables:

The Student Weight Status Category Reporting Dataset contains weight status category data (underweight, healthy weight, overweight or obese, based on BMI-for-age percentile). The dataset includes separate estimates of the percent of students overweight, obese and overweight or obese for all reportable grades within the county and/or region and by grade groups (elementary and middle/high). There are a total of 15 columns with ~32,000 rows of data. Some examples of the columns are number of students overweight, number of students obese, grade level, and sex. This dataset contains string, integers, and floats.

- Independent / Predictor variables:
- Dependent / Target variables:

## Intended Learning Task

## Steps to Clean and Transform Data

1. Remove any white space or special characters
2. Identify any rows with missing data and drop those rows
3. Check that the data types of each column are correct (make sure that categorical columns are converted into string)
4. Detect any outliers that are part of the dataset. Determine what to do with the outliers depending on how they affect the rest of the dataset.