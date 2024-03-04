import numpy as np
import pandas as pd
from tabulate import tabulate
from datetime import datetime 
import os
import argparse

parser = argparse.ArgumentParser(description='Test Dataframe IO Usage.')
parser.add_argument("--intSize", help="Size of the integer", type=int, default=64)
parser.add_argument("--rows", help="Number of rows", type=int, default=7812500)
parser.add_argument("--columns", help="Number of columns", type=int, default=16)
args = parser.parse_args()
parser.print_help()

intSize = int(args.intSize)
rows = int(args.rows)
columns = int(args.columns)
maxNumber = (2**(intSize-1)) - 1

Table = []

print("\n")
print("intSize ", type(intSize), " ", intSize)
print("rows ", type(rows), " ", rows)
print("columns ", type(columns), " ", columns)
print("maxNumber ", type(maxNumber), " ", maxNumber)
print("\n")
print("Generating Random data \"np.random.randint(0, (2^intSize), size=(rows,columns))\" ...")
print (rows*columns*(intSize//8)/(1024**2), " Megabytes of data in ", rows, " Rows & ", columns, " Columns of ", intSize, " bit Integers")
Table.append(["Generated Data", None, rows*columns*(intSize//8)/(1024**2), None])

start = datetime.now()
np_array = np.random.randint(0, maxNumber, size=(rows,columns))
columns = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P"]
df = pd.DataFrame(data=np_array, columns=columns)
end = (datetime.now() - start).total_seconds()
print("Process took", end, " sec")
print("The Dataframe is using ", df.memory_usage(deep=True).sum()/1024**2, " MB of memory")
print("Dataframe shape: ", df.shape)
print("The Dataframe Types are: ", df.dtypes)
print("First 10 Rows of the Dataframe are: ")
print(df.head(10))
print("\n")
Table.append(["Raw Data", None, df.memory_usage(deep=True).sum()/1024**2, None])

print("Writing Raw Parquet File From Dataframe...")
start = datetime.now()
df.to_parquet(path="raw.parquet", engine="pyarrow", compression=None)
raw_end = (datetime.now() - start).total_seconds()
print("Process took", raw_end, " sec")
raw_file_size = os.path.getsize('raw.parquet')
print("File Size is :", raw_file_size/1024**2, " MB\n")
Table.append(["Writing Raw Parquet File", raw_end, raw_file_size/1024**2, (100-((raw_file_size/df.memory_usage(deep=True).sum())*100))])

print("Writing snappy Compressed Parquet File From Dataframe...")
start = datetime.now()
df.to_parquet(path="snappy.parquet", engine="pyarrow", compression="snappy")
snappy_end = (datetime.now() - start).total_seconds()
print("Process took", snappy_end, " sec")
snappy_file_size = os.path.getsize('snappy.parquet')
print("File Size is :", snappy_file_size/1024**2, " MB\n")
Table.append(["Writing Snappy Compressed Parquet File",snappy_end,snappy_file_size/1024**2,100-((snappy_file_size/raw_file_size)*100)])

print("Writing gzip Compressed Parquet File From Dataframe...")
start = datetime.now()
df.to_parquet(path="gzip.parquet", engine="pyarrow", compression="gzip")
gzip_end = (datetime.now() - start).total_seconds()
print("Process took", gzip_end, " sec")
gzip_file_size = os.path.getsize('gzip.parquet')
print("File Size is :", gzip_file_size/1024**2, " MB\n")
Table.append(["Writing GZip Compressed Parquet File", gzip_end, gzip_file_size/1024**2, 100-((gzip_file_size/raw_file_size)*100)])

print("Writing brotli Compressed Parquet File From Dataframe...")
start = datetime.now()
df.to_parquet(path="brotli.parquet", engine="pyarrow", compression="brotli")
brotli_end = (datetime.now() - start).total_seconds()
print("Process took", brotli_end, " sec")
brotli_file_size = os.path.getsize('brotli.parquet')
print("File Size is :", brotli_file_size/1024**2, " MB\n")
Table.append(["Writing Brotli Compressed Parquet File", brotli_end, brotli_file_size/1024**2, 100-((brotli_file_size/raw_file_size)*100)])

print("Writing lz4 Compressed Parquet File From Dataframe...")
start = datetime.now()
df.to_parquet(path="lz4.parquet", engine="pyarrow", compression="lz4")
lz4_end = (datetime.now() - start).total_seconds()
print("Process took", lz4_end, " sec")
lz4_file_size = os.path.getsize('lz4.parquet')
print("File Size is :", lz4_file_size/1024**2, " MB\n")
Table.append(["Writing lz4 Compressed Parquet File", lz4_end, lz4_file_size/1024**2, 100-((lz4_file_size/raw_file_size)*100)])

print("Writing zstd Compressed Parquet File From Dataframe...")
start = datetime.now()
df.to_parquet(path="zstd.parquet", engine="pyarrow", compression="zstd")
zstd_end = (datetime.now() - start).total_seconds()
print("Process took", zstd_end, " sec")
zstd_file_size = os.path.getsize('zstd.parquet')
print("File Size is :", zstd_file_size/1024**2, " MB\n")
Table.append(["Writing zStd Compressed Parquet File", zstd_end, zstd_file_size/1024**2, 100-((zstd_file_size/raw_file_size)*100)])

print("\n\nRead Tests\n\n")

print("Reading raw Parquet File Into A Dataframe...")
del df
start = datetime.now()
df = pd.read_parquet("raw.parquet", engine="pyarrow")
raw_read_end = (datetime.now() - start).total_seconds()
print("Process took", raw_read_end, " sec\n")
Table.append(["Reading Raw Parquet File", raw_read_end, None, None])

print("Reading snappy Compressed Parquet File Into A Dataframe...")
del df
start = datetime.now()
df = pd.read_parquet("snappy.parquet", engine="pyarrow")
snappy_read_end = (datetime.now() - start).total_seconds()
print("Process took", snappy_read_end, " sec\n")
Table.append(["Reading Snappy Compressed Parquet File", snappy_read_end, None, None])

print("Reading gzip Compressed Parquet File Into A Dataframe...")
del df
start = datetime.now()
df = pd.read_parquet("gzip.parquet", engine="pyarrow")
gzip_read_end = (datetime.now() - start).total_seconds()
print("Process took", gzip_read_end, " sec\n")
Table.append(["Reading GZip Compressed Parquet File", gzip_read_end, None, None])

print("Reading brotli Compressed Parquet File Into A Dataframe...")
del df
start = datetime.now()
df = pd.read_parquet("brotli.parquet", engine="pyarrow")
brotli_read_end = (datetime.now() - start).total_seconds()
print("Process took", brotli_read_end, " sec\n")
Table.append(["Reading Brotli Compressed Parquet File", brotli_read_end, None, None])

print("Reading lz4 Compressed Parquet File Into A Dataframe...")
del df
start = datetime.now()
df = pd.read_parquet("lz4.parquet", engine="pyarrow")
lz4_read_end = (datetime.now() - start).total_seconds()
print("Process took", lz4_read_end, " sec\n")
Table.append(["Reading lz4 Compressed Parquet File", lz4_read_end, None, None])

print("Reading zstd Compressed Parquet File Into A Dataframe...")
del df
start = datetime.now()
df = pd.read_parquet("zstd.parquet", engine="pyarrow")
zstd_read_end = (datetime.now() - start).total_seconds()
print("Process took", zstd_read_end, " sec\n")
Table.append(["Reading zStd Compressed Parquet File", zstd_read_end, None, None])

print("\n\nProcessing Tests\n\n")

print("Testing Copying A DataFrame")
start = datetime.now()
df2 = df.copy()
copy_end = (datetime.now() - start).total_seconds()
print("Process took", copy_end, " sec\n")
del df2
Table.append(["Copying A DataFrame", copy_end, None, None])

print("Testing Deep Copying Of A DataFrame")
start = datetime.now()
df2 = df.copy(deep=True)
deep_copy_end = (datetime.now() - start).total_seconds()
print("Process took", deep_copy_end, " sec\n")
del df2
Table.append(["Deep Copying Of A DataFrame", deep_copy_end, None, None])

print("Testing Calculating A New DataFrame Column")
print("The Dataframe's Entry Shape is: ", df.shape)
start = datetime.now()
df["New"] = df["A"] + df["B"] + df["C"]
nc_end = (datetime.now() - start).total_seconds()
print("The Dataframe's Exit Shape is: ", df.shape)
print("Process took", nc_end, " sec\n")
Table.append(["Calculating A New DataFrame Column", nc_end, None, None])

print("Testing Calculating A New DataFrame Column Using If Else")
print("The Dataframe's Entry Shape is: ", df.shape)
start = datetime.now()
df["New2"] = np.where(df["A"] > 10, True, False)
if_add_end = (datetime.now() - start).total_seconds()
print("The Dataframe's Exit Shape is: ", df.shape)
print("Process took", if_add_end, " sec\n")
Table.append(["Calculating A New DataFrame Column Using If Else", if_add_end, None, None])

conditions = [(df["A"] <= 10), (df["A"] > 10) & (df["A"] <= 20), (df["A"] > 20)]
values = ["Tier_1", "Tier_2", "Tier_3"]
print("Testing Calculating A New DataFrame Column Using Multiple Conditions")
print("The Dataframe's Entry Shape is: ", df.shape)
start = datetime.now()
df["New3"] = np.select(conditions, values)
con_add_end = (datetime.now() - start).total_seconds()
print("The Dataframe's Exit Shape is: ", df.shape)
print("Process took", con_add_end, " sec\n")
Table.append(["Calculating A New DataFrame Column Using Multiple Conditions", con_add_end, None, None])

print("Testing Removing A DataFrame Column")
print("The Dataframe's Entry Shape is: ", df.shape)
start = datetime.now()
df.drop(["New3"], axis=1, inplace=True)
rc_end = (datetime.now() - start).total_seconds()
print("The Dataframe's Exit Shape is: ", df.shape)
print("Process took", rc_end, " sec\n")
Table.append(["Removing A DataFrame Column", rc_end, None, None])

print("Testing Removing A DataFrame Row")
print("The Dataframe's Entry Shape is: ", df.shape)
start = datetime.now()
df.drop([10], inplace=True)
rr_end = (datetime.now() - start).total_seconds()
print("The Dataframe's Exit Shape is: ", df.shape)
print("Process took", rr_end, " sec\n")
Table.append(["Removing A DataFrame Row", rr_end, None, None])

print("Testing Removing A DataFrame Row Based On Condition")
print("The Dataframe's Entry Shape is: ", df.shape)
start = datetime.now()
indexs = df[(df["A"] >= 20) & (df["A"] <= 30000)].index
df.drop(indexs, inplace=True)
con_rr_end = (datetime.now() - start).total_seconds()
print("The Dataframe's Exit Shape is: ", df.shape)
print("Process took", con_rr_end, " sec\n")
Table.append(["Removing A DataFrame Row Based On Condition", con_rr_end, None, None])

del df
print("\nDone")
print("Results:")
print(tabulate(Table, headers=[" ", "Time (Seconds)", "Size (Megabytes)", "Ratio (%)"], tablefmt="fancy_grid"))

exit(0)