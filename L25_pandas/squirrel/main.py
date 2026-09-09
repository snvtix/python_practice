import pandas as pd
from collections import Counter

data = pd.read_csv("L25_pandas/squirrel/2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

data_dict = Counter(data["Primary Fur Color"])

pd_dict = {
    "Fur Color": ["Grey", "Cinnamon", "Black"],
    "Count": [data_dict["Grey"], data_dict["Cinnamon"], data_dict["Black"]]
}

df = pd.DataFrame(pd_dict)
df.to_csv("L25_pandas/squirrel/squirrel.csv")

print(data_dict)



