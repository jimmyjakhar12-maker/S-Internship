# Assignment 18 - PySpark Partition Management

## Objective

This assignment demonstrates partition management in Apache Spark using PySpark.

The application:

1. Creates a DataFrame containing 5 million records using `spark.range()`.
2. Displays the initial number of partitions.
3. Increases the number of partitions to 12 using `repartition()`.
4. Reduces the number of partitions to 3 using `coalesce()`.
5. Displays sample records from the final DataFrame.

---

## Technologies Used

- Python 3.11
- Apache Spark (PySpark)
- Docker
- OpenJDK 21

---

## Project Structure

```text
assessment-18/
│
├── partition_demo.py
├── requirements.txt
├── Dockerfile
├── README.md
└── output/
    └── screenshot.png
```

---

## PySpark Code

The application performs the following operations:

```python
# Generate 5 million records
df = spark.range(5000000)

# Check initial partitions
print(df.rdd.getNumPartitions())

# Increase partitions
df_repartitioned = df.repartition(12)

# Reduce partitions
df_coalesced = df_repartitioned.coalesce(3)
```

---

## Understanding Partition Operations

### Repartition()

- Used to increase or decrease partitions.
- Performs a full data shuffle.
- Useful for balancing data across partitions.

Example:

```python
df.repartition(12)
```

---

### Coalesce()

- Primarily used to reduce partitions.
- Avoids a full shuffle.
- More efficient than repartition for reducing partitions.

Example:

```python
df.coalesce(3)
```

---

## Running Locally

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
python partition_demo.py
```

---

## Running with Docker

Build Docker image:

```bash
docker build -t assessment18 .
```

Run Docker container:

```bash
docker run --rm assessment18
```

---

## Sample Output

```text
=== Initial Partitions ===
12

=== After Repartition(12) ===
12

=== After Coalesce(3) ===
3
```

---

## Output Screenshot

![Output Screenshot](output/screenshot.png)

---

## Key Learnings

- Understanding Spark partitions.
- Difference between repartition() and coalesce().
- Managing distributed data efficiently.
- Running PySpark applications inside Docker containers.

---
