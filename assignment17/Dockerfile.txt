FROM python:3.11

RUN apt-get update && \
    apt-get install -y default-jdk

RUN pip install pyspark==3.5.1

WORKDIR /app

COPY . .

CMD ["python", "sales_dataframe.py"]