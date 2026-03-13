import pandas as pd

data = {
    "Name": ["Alice", "Bob", "Charlie", "David"],
    "Score": [95, 92, 78, 85],
    "Passed": [True, True, False, True],
    "Category": ["A", "A", "B", "B"]
}

df = pd.DataFrame(data)

selected = df[["Name", "Score"]]


high_performing = selected[df["Score"] > 90]

print("High-performing students:")
print(high_performing.to_string(index=False))
