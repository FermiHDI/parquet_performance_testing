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
|                                                                    |   Time (Seconds) |   Size (Megabytes) |     Ratio (%) |
|--------------------------------------------------------------------|------------------|--------------------|---------------|
| Generated 125000000 64 Bit Integers In 7812500 Rows And 16 Columns |                  |            953.674 |               |
| Dataframe: (7812500, 16)                                           |                  |            953.674 |               |
|                                                                    |                  |                    |               |
| Write Tests                                                        |                  |                    |               |
| Writing Raw Parquet File                                           |          3.45274 |            987.813 |      -3.57972 |
| Writing Snappy Compressed Parquet File                             |          3.79007 |            987.863 |   -0.00500021 |
| Writing GZip Compressed Parquet File                               |          25.0899 |             985.98 |      0.185605 |
| Writing Brotli Compressed Parquet File                             |          9.71139 |            983.587 |      0.427864 |
| Writing lz4 Compressed Parquet File                                |          3.93752 |            991.689 |     -0.392315 |
| Writing zStd Compressed Parquet File                               |          4.42556 |            986.864 |     0.0960559 |
| Writing CSV File                                                   |          63.1686 |            2428.36 |      -154.632 |
| Writing zip Compressed CSV File                                    |          198.334 |            1166.94 |       51.9453 |
| Writing gzip Compressed CSV File                                   |          203.886 |            1166.94 |       51.9453 |
| Writing bz2 Compressed CSV File                                    |          223.469 |            1075.57 |       55.7079 |
| Writing tar Compressed CSV File                                    |          50.9034 |            2428.37 |      -0.00041 |
|                                                                    |                  |                    |               |
| Read Tests                                                         |                  |                    |               |
| Reading Raw Parquet File                                           |         0.958191 |                    |               |
| Reading Snappy Compressed Parquet File                             |         0.970616 |                    |               |
| Reading GZip Compressed Parquet File                               |         0.926079 |                    |               |
| Reading Brotli Compressed Parquet File                             |         0.988539 |                    |               |
| Reading lz4 Compressed Parquet File                                |         0.961599 |                    |               |
| Reading zStd Compressed Parquet File                               |         0.906938 |                    |               |
| Reading Uncompressed CSV File                                      |          2.48883 |                    |               |
| Reading zip Compressed CSV File                                    |          7.97299 |                    |               |
| Reading gzip Compressed CSV File                                   |          33.1109 |                    |               |
| Reading bz2 Compressed CSV File                                    |          107.859 |                    |               |
| Reading tar Compressed CSV File                                    |          2.68874 |                    |               |
|                                                                    |                  |                    |               |
| Dataframe Mutation Tests                                           |                  |                    |               |
| Copying A DataFrame                                                |         0.220021 |                    |               |
| Deep Copying Of A DataFrame                                        |         0.150804 |                    |               |
| Calculating A New DataFrame Column                                 |         0.043409 |                    |               |
| Calculating A New DataFrame Column Using If Else                   |         0.009444 |                    |               |
| Calculating A New DataFrame Column Using Multiple Conditions       |         0.431748 |                    |               |
| Removing A DataFrame Column                                        |         0.280244 |                    |               |
| Removing A DataFrame Row                                           |         0.387414 |                    |               |
| Removing DataFrame Rows Based On Condition                         |         0.930942 |                    |               |
```

## Commands
```
usage: test.py [-h] [--intSize INTSIZE] [--rows ROWS] [--columns COLUMNS]
-h, --help              show this help message and exit
--intSize INTSIZE       Size of the integer
--rows ROWS             Number of rows
--columns COLUMNS       Number of columns
--dataset DATASET       Location of a custom parquet file to use
--intColumn1 INTCOLUMN1 Column of custom dataset that is an int type
--intColumn2 INTCOLUMN2 Column of custom dataset that is an int type
--intColumn3 INTCOLUMN3 Column of custom dataset that is an int type
```

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