import pandas as pd


data = {
    "Name": ["Alice", "Bob", "Charlie", "David", "Eva", "Frank", "Grace"],
    "Age": [23, 25, 22, 24, 26, 23, 27],
    "Score": [88, 92, 79, 85, 95, 67, 90],
    "Label": ["Pass", "Pass", "Pass", "Pass", "Pass", "Fail", "Pass"]
}


df = pd.DataFrame(data)


print("First 5 rows:")
print(df.head())
print()


print("Dataset Info:")
df.info()
print()


filtered_rows = df[df["Score"] > 80]

print("Filtered rows (Score > 80):")
print(filtered_rows)
