import sys 

import pandas as pd

print ('arguments', sys.argv)

month = int(sys.argv[1])

df = pd.DataFrame({"day": [1, 2], "passenger": [10, 20]})
df['month'] = month

print(f'Running pipelilne for month {month}')

df.to_parquet(f"output_month{month}.parquet")