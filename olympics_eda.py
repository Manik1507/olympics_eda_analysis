# Olympic Medals Data Analysis

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv('olympic_medals.csv')  # Replace with correct file

# Basic info
print(df.head())
print(df['Team'].nunique(), "countries participated")

# Total medals by country
medals = df.groupby('Team')['Medal'].count().sort_values(ascending=False).head(10)
sns.barplot(x=medals.values, y=medals.index)
plt.title("Top 10 Countries by Total Olympic Medals")
plt.xlabel("Total Medals")
plt.ylabel("Country")
plt.show()

# Medals by sport
sports = df['Sport'].value_counts().head(10)
sns.barplot(x=sports.values, y=sports.index)
plt.title("Most Popular Olympic Sports (by Medals Awarded)")
plt.show()
