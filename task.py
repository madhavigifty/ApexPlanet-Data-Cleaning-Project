#.\myenv\Scripts\Activate.ps1
import pandas as pd

# Read the Excel file
df = pd.read_excel("ApexPlanet_DataAnalytics_Dataset.xlsx")

# Show first 5 rows
print(df.head())

# Show dataset information
print(df.info())

# Show missing values
print("missing values",df.isnull().sum())

#checking for the duplicates
print("Duplicate rows",df.duplicated().sum())

#checking duplicate ordered id's
print("duplicated ordered id's",df["Order_ID"].duplicated().sum())

#fill missing values
df["Age"]=df["Age"].fillna(df["Age"].mean())
df["City"]=df["City"].fillna(df["City"].mode()[0])

print("after",df.isnull().sum())

#date is in str formate change to proper one 
df["Order_Date"]=pd.to_datetime(df["Order_Date"])
print(df.dtypes)

#creating age column
def  age_group(age):
    if age<25:
        return "Young"
    elif age<45:
        return "Adult"
    else:
        return "Senior"

df["Age_Group"]=df["Age"].apply(age_group)

#creating month column
df["Month"] = df["Order_Date"].dt.month_name()

#saving the cleaned dataset
df.to_excel("cleaned_sales_dataset.xlsx", index=False)

print("Dataset saved successfully!")


print("Dataset Shape:", df.shape)
print("Missing Values:")
print(df.isnull().sum())