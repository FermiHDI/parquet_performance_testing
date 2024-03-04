FROM python:3.10.5-slim-buster
WORKDIR /app_demo
COPY ./requirements.txt /app_demo/
COPY ./test.py /app_demo/
RUN pip install -r requirements.txt
ENTRYPOINT [ "python3", "test.py"]
CMD ["--intSize=64","--rows=7812500","--columns=16"]