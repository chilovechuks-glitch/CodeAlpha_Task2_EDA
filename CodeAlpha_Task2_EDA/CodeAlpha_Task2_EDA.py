# ============================================================
# CodeAlpha Internship - Task 2: Exploratory Data Analysis
# Dataset: Books to Scrape
# ============================================================
# EDA Questions:
# 1. What is the distribution of book ratings?
# 2. What is the distribution of book prices?
# 3. Do higher-rated books have higher average prices?
# 4. Is there a relationship between book price and rating?
# 5. Are there any missing values or duplicate records?
# 6. Are there any unusual price values or outliers?
# 7. What is the availability status of the books?
import pandas as pd
import matplotlib.pyplot as plt
# ============================================================
# 1. Load Dataset
# ============================================================
df = pd.read_csv("CodeAlpha_Books_Dataset.csv")

print(df.head())
# ============================================================
# 2. Explore Dataset Structure
# ============================================================
print("\nDataset Shape:")
print(df.shape)

print("\nColumn Names:")
print(df.columns.tolist())

print("\nData Types:")
print(df.dtypes)
# ============================================================
# 3. Data Quality Checks
# ============================================================
print("\nMissing Values:")
print(df.isnull().sum())
print("\nDuplicate Rows:")
print(df.duplicated().sum())
# ============================================================
# 4. Descriptive Statistics
# ============================================================
print("\nDescriptive Statistics:")
print(df[["Price", "Rating"]].describe())
# ============================================================
# 5. Rating Analysis
# ============================================================
print("\nRating Counts:")
print(df["Rating"].value_counts().sort_index())
# ============================================================
# 6. Rating Distribution Visualization
# ============================================================
plt.figure(figsize=(8, 5))
df["Rating"].value_counts().sort_index().plot(kind="bar")
plt.title("Distribution of Book Ratings")
plt.xlabel("Rating")
plt.ylabel("Number of Books")
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()
# ============================================================
# 7. Price Distribution Visualization
# ============================================================
plt.figure(figsize=(8, 5))
plt.hist(df["Price"], bins=20, edgecolor="black")
plt.title("Distribution of Book Prices")
plt.xlabel("Price (£)")
plt.ylabel("Number of Books")
plt.tight_layout()
plt.show()
# ============================================================
# 8. Average Price by Rating
# ============================================================
avg_price_by_rating = df.groupby("Rating")["Price"].mean()
print("\nAverage Price by Rating:")
print(avg_price_by_rating)
plt.figure(figsize=(8, 5))
avg_price_by_rating.plot(kind="bar")
plt.title("Average Book Price by Rating")
plt.xlabel("Rating")
plt.ylabel("Average Price (£)")
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()
# ============================================================
# 9. Price-Rating Correlation
# ============================================================
correlation = df["Price"].corr(df["Rating"])
print("\nPrice-Rating Correlation:")
print(round(correlation, 3))
# ============================================================
# 10. Price vs Rating Visualization
# ============================================================
plt.figure(figsize=(8, 5))
plt.scatter(df["Price"], df["Rating"], alpha=0.6)
plt.title("Book Price vs Rating")
plt.xlabel("Price (£)")
plt.ylabel("Rating")
plt.yticks([1, 2, 3, 4, 5])
plt.tight_layout()
plt.show()
# ============================================================
# 11. Availability Analysis
# ============================================================
print("\nAvailability Counts:")
print(df["Availability"].value_counts())
# ============================================================
# 12. Price Outlier Analysis
# ============================================================
print("\nPrice Outlier Analysis:")
Q1 = df["Price"].quantile(0.25)
Q3 = df["Price"].quantile(0.75)
IQR = Q3 - Q1
lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR
outliers = df[
    (df["Price"] < lower_bound) |
    (df["Price"] > upper_bound)
]
print(f"Q1: £{Q1:.2f}")
print(f"Q3: £{Q3:.2f}")
print(f"IQR: £{IQR:.2f}")
print(f"Lower Bound: £{lower_bound:.2f}")
print(f"Upper Bound: £{upper_bound:.2f}")
print(f"Number of Price Outliers: {len(outliers)}")
# ============================================================
# 13. Final EDA Summary
# ============================================================
print("\n" + "=" * 50)
print("EDA SUMMARY")
print("=" * 50)
print(f"Total Books: {len(df)}")
print(f"Average Price: £{df['Price'].mean():.2f}")
print(f"Average Rating: {df['Rating'].mean():.2f}")
print(f"Minimum Price: £{df['Price'].min():.2f}")
print(f"Maximum Price: £{df['Price'].max():.2f}")
print(f"Price-Rating Correlation: {correlation:.3f}")
print(f"Duplicate Rows: {df.duplicated().sum()}")
print(f"Price Outliers: {len(outliers)}")
print(f"Books In Stock: {(df['Availability'] == 'In stock').sum()}")