Test is with a 2D array of 32 bit integers in 16 columns

File            Bytes               Compression To_Raw
Raw Data        0,500,000,000 Bytes
raw.parquet     1,035,797,309 Bytes             207.2%
snappy.parquet  1,035,849,101 Bytes +00.005%    207.2%
brotli.parquet  1,031,365,501 Bytes -00.4%      206.3%
gzip.parquet    1,033,874,813 Bytes -00.2%      206.8%
lz4.parquet     1,039,860,893 Bytes +00.4%      208.0%
zstd.parquet    1,034,802,365 Bytes -00.1%      207.0%

To Run:
python3 test.py

To Build Docker Image:
docker buildx build -t parquet_test .

To Run Docker Image:
docker run -it -v .:/app_demo parquet_test
