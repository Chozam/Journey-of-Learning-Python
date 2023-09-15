import pandas as pd
import random as rdm

data = pd.read_csv("./data/french_words.csv")
to_learn = data.to_dict(orient="records")
acak = rdm.choice(to_learn)
print(to_learn)

