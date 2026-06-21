from pyspark.sql import SparkSession

# Create Spark Session
spark = SparkSession.builder \
    .appName("EmployeeRDDProcessing") \
    .getOrCreate()

sc = spark.sparkContext

# Read CSV as RDD
rdd = sc.textFile("data/employees.csv")

# Remove header
header = rdd.first()
data_rdd = rdd.filter(lambda row: row != header)

# Convert to tuple
employee_rdd = data_rdd.map(
    lambda x: (
        int(x.split(",")[0]),      # id
        x.split(",")[1],           # name
        x.split(",")[2],           # department
        int(x.split(",")[3])       # salary
    )
)

print("\n===== Employees Sorted By Salary Descending =====")

sorted_salary = employee_rdd.sortBy(
    lambda x: x[3],
    ascending=False
)

for emp in sorted_salary.collect():
    print(emp)

print("\n===== Total Salary By Department =====")

department_salary = (
    employee_rdd
    .map(lambda x: (x[2], x[3]))
    .reduceByKey(lambda a, b: a + b)
)

for dept in department_salary.collect():
    print(dept)

print("\n===== Top 3 Highest Paid Employees =====")

top3 = sorted_salary.take(3)

for emp in top3:
    print(emp)

# Save Top 3 Employees
top3_rdd = sc.parallelize(
    [",".join(map(str, emp)) for emp in top3]
)

top3_rdd.saveAsTextFile("output/top_3_employees")

spark.stop()