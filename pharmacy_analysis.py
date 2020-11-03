import pandas as pd
import matplotlib.pyplot as plt


file = "pharmacy_data.txt"

df = pd.read_table(file, header=None)

print(df)

print(df[1].max(), df[1].min(), df[1].mean(), df[1].median())

print(df.sort_values(1, ascending=False).head(20))

print(df.sort_values(1, ascending=False).tail(20))

img1 = plt.figure()

df[1].hist(bins=25)

plt.show()

img1.savefig("img1.png")

low_limit = df[df[1] <= 3000]

img2 = plt.figure()

low_limit[1].hist()

plt.show()

img2.savefig("img2.png")

high_limit = df[df[1] > 3000]

img3 = plt.figure()

high_limit[1].hist()

plt.show()

img3.savefig("img3.png")

very_low_limit = df[df[1] < 100]

img4 = plt.figure()

very_low_limit[1].hist()

plt.show()

img4.savefig("img4.png")