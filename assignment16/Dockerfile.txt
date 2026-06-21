FROM python:3.11

RUN apt-get update && \
    apt-get install -y default-jdk

ENV JAVA_HOME=/usr/lib/jvm/default-java

RUN pip install pyspark==3.5.1

WORKDIR /app

COPY . .

CMD ["python", "employee_rdd.py"]