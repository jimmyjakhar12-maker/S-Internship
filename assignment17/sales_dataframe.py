from pyspark.sql import SparkSession
from pyspark.sql.functions import col
import shutil
import os

# Create Spark Session
spark = SparkSession.builder \
    .appName("Sales DataFrame Analysis") \
    .getOrCreate()

# Read CSV File
df = spark.read.csv(
    "data/sales.csv",
    header=True,
    inferSchema=True
)

print("\n===== Original Dataset =====")
df.show()

# Sort products by sales descending
print("\n===== Products Sorted By Sales Descending =====")
sorted_df = df.orderBy(col("sales").desc())
sorted_df.show()

# Top 3 products by sales
print("\n===== Top 3 Products =====")
top3_df = sorted_df.limit(3)
top3_df.show()

# Filter products with sales > 80000
print("\n===== Products With Sales Greater Than 80000 =====")
filtered_df = df.filter(col("sales") > 80000)
filtered_df.show()

# Remove output folder if exists
output_path = "output/high_sales_products"

if os.path.exists(output_path):
    shutil.rmtree(output_path)

# Save filtered data as CSV
filtered_df.coalesce(1) \
    .write \
    .mode("overwrite") \
    .option("header", True) \
    .csv(output_path)

print(f"\nFiltered output saved to: {output_path}")

spark.stop()