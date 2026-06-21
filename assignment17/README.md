# Sales Data Analysis Using PySpark DataFrame

## Project Overview

This project demonstrates data analysis using Apache Spark DataFrames.

The application reads sales data from a CSV file and performs:

- Sorting products by sales in descending order
- Finding the top 3 products with highest sales
- Filtering products with sales greater than 80,000
- Saving filtered records as CSV

The project is containerized using Docker.

---

## Technologies Used

- Python 3.11
- Apache Spark (PySpark 3.5.1)
- Docker
- Java JDK

---

## Dataset

File:

```text
data/sales.csv
```

Contains product sales information.

---

## Project Structure

```text
sales-dataframe-project/
│
├── data/
│   └── sales.csv
│
├── output/
│   └── high_sales_products/
│
├── sales_dataframe.py
├── requirements.txt
├── Dockerfile
├── README.md
└── .gitignore
```

---

## Operations Performed

### 1. Sort Products by Sales

Products are sorted in descending order using:

```python
orderBy(col("sales").desc())
```

### 2. Top 3 Products

Displays the products having the highest sales.

### 3. Filter High Sales Products

Filters products whose sales are greater than 80,000.

### 4. Save Output

Filtered products are saved as CSV files.

---

## Running Locally

Install dependencies:

```bash
pip install -r requirements.txt
```

Run application:

```bash
python sales_dataframe.py
```

---

## Docker Build

```bash
docker build -t sales-dataframe .
```

---

## Docker Run

```bash
docker run --rm sales-dataframe
```

---

## Expected Results

### Top 3 Products

- Laptop
- TV
- Mobile

### High Sales Products

- Laptop
- Mobile
- TV
- Bed

Output is stored in:

```text
output/high_sales_products
```

---

## Learning Outcomes

- PySpark DataFrames
- DataFrame Transformations
- Filtering and Sorting
- CSV Data Processing
- Docker Containerization

---
