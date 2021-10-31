import pyarrow.parquet as pq
import os


print(os.getcwd())

# os.chdir('Ch02/02_03/')
table = pq.read_table('taxi.parquet')

df = table.to_pandas()

df.dtypes
df.head()
