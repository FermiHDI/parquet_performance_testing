<p align="left">
  <img src="https://github.com/FermiHDI/images/blob/main/logos/FermiHDI%20Logo%20Hz%20-%20Dark.png?raw=true" width="500" alt="logo"/> 
</p>

# FermiHDI Parquet Performance Testing
A simple Python based test of the parquet file format and Panda Dataframes using numpy and pyarrow.  This test will create an dataframe of random integers which are then saved to parquet file format using different compressions. It will also perfrom some mutations on the Dataframe as a base line as to the cost of IO to storage using the Parquet File format.

This test can be modified with any sample dataset to see the impact of different compressions and IO with that sample dataset

## License

UNLICENSED - Private </br>
ALL RIGHTS RESERVED </br>
© COPYRIGHT 2023 FERMIHDI LIMITED </br>

## Sample Output
```
|                                                                    |   Time (Seconds) |   Size (Megabytes) |   Ratio (%) |
|--------------------------------------------------------------------|------------------|--------------------|-------------|
| Generated 125000000 64 Bit Integers In 7812500 Rows And 16 Columns |                  |            953.674 |             |
| Dataframe: (7812500, 16)                                           |                  |            953.674 |             |
|                                                                    |                  |                    |             |
| Write Tests                                                        |                  |                    |             |
| Writing Raw Parquet File                                           |         3.87194  |            987.813 |  -3.57972   |
| Writing Snappy Compressed Parquet File                             |         4.5448   |            987.863 |  -0.0050003 |
| Writing GZip Compressed Parquet File                               |        25.7669   |            985.98  |   0.185602  |
| Writing Brotli Compressed Parquet File                             |         9.82364  |            983.587 |   0.427864  |
| Writing lz4 Compressed Parquet File                                |         3.85868  |            991.689 |  -0.392315  |
| Writing zStd Compressed Parquet File                               |         4.06438  |            986.864 |   0.0960559 |
|                                                                    |                  |                    |             |
| Read Tests                                                         |                  |                    |             |
| Reading Raw Parquet File                                           |         0.966345 |                    |             |
| Reading Snappy Compressed Parquet File                             |         1.00242  |                    |             |
| Reading GZip Compressed Parquet File                               |         0.884566 |                    |             |
| Reading Brotli Compressed Parquet File                             |         0.932898 |                    |             |
| Reading lz4 Compressed Parquet File                                |         0.883964 |                    |             |
| Reading zStd Compressed Parquet File                               |         0.885487 |                    |             |
|                                                                    |                  |                    |             |
| Dataframe Mutation Tests                                           |                  |                    |             |
| Copying A DataFrame                                                |         0.17332  |                    |             |
| Deep Copying Of A DataFrame                                        |         0.130979 |                    |             |
| Calculating A New DataFrame Column                                 |         0.033687 |                    |             |
| Calculating A New DataFrame Column Using If Else                   |         0.009812 |                    |             |
| Calculating A New DataFrame Column Using Multiple Conditions       |         0.38175  |                    |             |
| Removing A DataFrame Column                                        |         0.226546 |                    |             |
| Removing A DataFrame Row                                           |         0.368838 |                    |             |
| Removing DataFrame Rows Based On Condition                         |         0.507558 |                    |             |
```

## Commands
usage: test.py [-h] [--intSize INTSIZE] [--rows ROWS] [--columns COLUMNS]
-h, --help         show this help message and exit
--intSize INTSIZE  Size of the integer
--rows ROWS        Number of rows
--columns COLUMNS  Number of columns

## To Run:
```
python3 test.py
```

## To Build Docker Image:
```
docker buildx build -t parquet_test .
```

## To Run Docker Image:
```
docker run -it -v .:/app_demo parquet_test
```