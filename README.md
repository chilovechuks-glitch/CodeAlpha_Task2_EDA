\# CodeAlpha Task 2: Exploratory Data Analysis (EDA)



\## Project Overview



This project was completed as part of my CodeAlpha internship.



The objective of this task was to perform Exploratory Data Analysis (EDA) on a dataset containing information about 1,000 books collected from the Books to Scrape website.



The analysis focuses on understanding the structure of the dataset, identifying patterns and trends, checking data quality, analyzing book prices and ratings, and detecting potential anomalies.



\## Dataset



The dataset contains \*\*1,000 books\*\* and the following five columns:



\* \*\*Title\*\* – Name of the book

\* \*\*Price\*\* – Book price in pounds (£)

\* \*\*Rating\*\* – Book rating from 1 to 5

\* \*\*Availability\*\* – Availability status of the book

\* \*\*URL\*\* – Link to the book's webpage



\## EDA Questions



The analysis was guided by the following questions:



1\. What is the distribution of book ratings?

2\. What is the distribution of book prices?

3\. Do higher-rated books have higher average prices?

4\. Is there a relationship between book price and rating?

5\. Are there any missing values or duplicate records?

6\. Are there unusual price values or outliers?

7\. What is the availability status of the books?



\## Tools and Technologies



\* Python

\* Pandas

\* Matplotlib

\* VS Code

\* Jupyter/Python environment



\## Analysis Performed



\### 1. Dataset Structure



The dataset contains:



\* \*\*1,000 rows\*\*

\* \*\*5 columns\*\*



The data types include strings, integers, and floating-point numbers.



\### 2. Data Quality Checks



The dataset was checked for missing values and duplicate records.



Results:



\* Missing values: \*\*0\*\*

\* Duplicate rows: \*\*0\*\*



This indicates that the dataset was complete for the variables analyzed and contained no duplicate records.



\### 3. Descriptive Statistics



Key statistics:



| Metric         | Result |

| -------------- | -----: |

| Average Price  | £35.07 |

| Average Rating |   2.92 |

| Minimum Price  | £10.00 |

| Maximum Price  | £59.99 |



\### 4. Rating Analysis



The distribution of ratings was:



| Rating | Number of Books |

| -----: | --------------: |

|      1 |             226 |

|      2 |             196 |

|      3 |             203 |

|      4 |             179 |

|      5 |             196 |



A bar chart was created to visualize the rating distribution.



\### 5. Price Analysis



The book prices range from \*\*£10.00 to £59.99\*\*, with an average price of \*\*£35.07\*\*.



A histogram was created to examine the distribution of book prices.



\### 6. Average Price by Rating



The average price for each rating was calculated:



| Rating | Average Price |

| -----: | ------------: |

|      1 |        £34.56 |

|      2 |        £34.81 |

|      3 |        £34.69 |

|      4 |        £36.09 |

|      5 |        £35.37 |



The differences in average prices across rating groups are relatively small.



\### 7. Price and Rating Relationship



The Pearson correlation between price and rating was calculated as:



\*\*0.028\*\*



This value is very close to zero, indicating \*\*very little linear relationship\*\* between book price and rating in this dataset.



A scatter plot was created to visualize the relationship.



Correlation describes association and should not be interpreted as evidence of causation.



\### 8. Availability Analysis



All 1,000 books in the dataset were listed as:



\*\*In stock\*\*



No unavailable books were identified.



\### 9. Outlier Analysis



The Interquartile Range (IQR) method was used to identify potential price outliers.



Results:



\* Q1: \*\*£22.11\*\*

\* Q3: \*\*£47.46\*\*

\* IQR: \*\*£25.35\*\*

\* Lower bound: \*\*-£15.92\*\*

\* Upper bound: \*\*£85.48\*\*

\* Price outliers: \*\*0\*\*



No price values were identified as outliers using this method.



\## Visualizations



The following visualizations were created using Matplotlib:



1\. \*\*Distribution of Book Ratings\*\*

2\. \*\*Distribution of Book Prices\*\*

3\. \*\*Average Book Price by Rating\*\*

4\. \*\*Book Price vs Rating\*\*



\## Key Findings



\* The dataset contains \*\*1,000 books\*\* across five variables.

\* There are \*\*no missing values\*\* and \*\*no duplicate records\*\*.

\* Book prices range from \*\*£10.00 to £59.99\*\*.

\* The average book price is \*\*£35.07\*\*.

\* The average rating is \*\*2.92 out of 5\*\*.

\* All 1,000 books were listed as \*\*in stock\*\*.

\* No price outliers were detected using the IQR method.

\* The price-rating correlation of \*\*0.028\*\* indicates very little linear relationship between price and rating.

\* Average prices across rating groups are relatively similar.



\## Conclusion



The Exploratory Data Analysis provided an overview of the structure, quality, distributions, and relationships within the Books to Scrape dataset.



The analysis found that the dataset is complete, contains no duplicate records, and has no price outliers based on the IQR method. Book prices varied from £10.00 to £59.99, while ratings ranged from 1 to 5.



The very low price-rating correlation suggests that book price and rating have very little linear association in this dataset.



This project strengthened practical skills in data inspection, data quality checking, descriptive statistics, statistical analysis, and data visualization using Python.



\## Files



\* `CodeAlpha\_Books\_Dataset.csv` – Cleaned dataset used for analysis

\* `CodeAlpha\_Task2\_EDA.py` – Python EDA script

\* `README.md` – Project documentation



