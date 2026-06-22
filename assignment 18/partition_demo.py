from pyspark.sql import SparkSession

spark = SparkSession.builder \
    .appName("Assignment18") \
    .getOrCreate()

# Create 5 million records with 6 partitions
df = spark.range(0, 5000000, 1, 6)

print("\n=== Initial Partitions ===")
print(df.rdd.getNumPartitions())

# Increase to 12 partitions
df_rep = df.repartition(12)

print("\n=== After Repartition(12) ===")
print(df_rep.rdd.getNumPartitions())

# Reduce to 3 partitions
df_coal = df_rep.coalesce(3)

print("\n=== After Coalesce(3) ===")
print(df_coal.rdd.getNumPartitions())

df_coal.show(10)

spark.stop()