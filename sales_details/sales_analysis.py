import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the CSV
df = pd.read_csv("data/sales.csv")

# Convert OrderDate to datetime
df['OrderDate'] = pd.to_datetime(df['OrderDate'])

# Create a Total_Sales column
df['Total_Sales'] = df['Quantity'] * df['Price']

# Extract month
df['Month'] = df['OrderDate'].dt.month_name()

# Group by month
monthly_sales = df.groupby('Month')['Total_Sales'].sum().sort_values()

# Show result in terminal
print("Monthly Sales:\n", monthly_sales)

# Plot chart
plt.figure(figsize=(8,5))
sns.barplot(x=monthly_sales.index, y=monthly_sales.values)
plt.title("Monthly Sales")
plt.ylabel("Sales in ₹")
plt.xlabel("Month")
plt.tight_layout()
plt.show()
