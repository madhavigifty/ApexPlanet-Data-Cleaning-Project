# Sales Dataset Data Cleaning and Wrangling Project

## Overview

This project focuses on cleaning and preprocessing a sales dataset using Python and Pandas. The goal is to identify and resolve data quality issues, perform feature engineering, and prepare the dataset for further analysis.

## Dataset Information

* Total Records: 1000
* Original Columns: 12
* Final Columns: 14

## Data Quality Issues Identified

* 20 missing values in the Age column
* 13 missing values in the City column
* 8 duplicate Order IDs
* No duplicate rows

## Cleaning and Transformation Steps

* Filled missing Age values using the mean
* Filled missing City values using the mode
* Converted Order_Date to datetime format
* Created Age_Group column
* Created Month column
* Saved the cleaned dataset

## Tools and Libraries

* Python
* Pandas
* OpenPyXL

## Output

The final dataset contains no missing values and is ready for analysis and visualization.
