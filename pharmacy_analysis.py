import pandas as pd
import matplotlib.pyplot as plt


file = "pharmacy_data.txt"

df = pd.read_table(file, header=None)

print(df)

print(df[1].max(), df[1].min(), df[1].mean(), df[1].median())

print(df.sort_values(1, ascending=False).head(20))

print(df.sort_values(1, ascending=False).tail(20))

df[1].hist(bins=25)

plt.show()

low_limit = df[df[1] <= 3000]

low_limit[1].hist()

plt.show()

high_limit = df[df[1] > 3000]

high_limit[1].hist()

plt.show()