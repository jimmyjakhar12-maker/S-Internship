# Employee Data Processing Using PySpark RDD

## Project Overview

This project demonstrates the use of Apache Spark RDDs to process employee data efficiently. The application reads employee records from a CSV file, performs various data processing operations using RDD transformations and actions, and saves the results to an output directory.

The project is containerized using Docker, making it easy to build and run in any environment without additional setup.

---

## Objectives

The project performs the following operations:

1. Read employee data from a CSV file using PySpark RDDs.
2. Sort employees by salary in descending order.
3. Calculate the total salary paid in each department.
4. Identify the top 3 highest-paid employees.
5. Save the top 3 employees to an output file.
6. Run the complete application inside a Docker container.

---

## Technologies Used

- Python 3.11
- Apache Spark (PySpark 3.5.1)
- Docker
- Java (JDK)

---

## Project Structure

```text
employee-rdd-project/
│
├── data/
│   └── employees.csv
│
├── output/
│   └── top_3_employees/
│
├── employee_rdd.py
├── requirements.txt
├── Dockerfile
├── README.md
└── .gitignore
```

---

## Dataset

File: `data/employees.csv`

```csv
id,name,department,salary
1,Amit,IT,55000
2,Rahul,HR,40000
3,Neha,IT,65000
4,Priya,Finance,70000
5,Karan,IT,50000
6,Simran,HR,45000
7,Rohit,Finance,60000
```

---

## Operations Performed

### 1. Sort Employees by Salary

Employees are sorted in descending order based on salary.

### 2. Department-wise Salary Calculation

The total salary paid in each department is calculated using RDD transformations.

### 3. Top 3 Highest-Paid Employees

The application identifies the three employees with the highest salaries.

### 4. Save Output

The top three employees are saved to:

```text
output/top_3_employees
```

---

## Prerequisites

Before running the project locally, ensure that the following are installed:

- Python 3.11 or later
- Java JDK 8 or higher
- Apache Spark (optional when using Docker)
- Docker Desktop

---

## Running the Project Locally

### Step 1: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 2: Run the Application

```bash
python employee_rdd.py
```

---

## Docker Setup

### Build Docker Image

```bash
docker build -t employee-rdd .
```

### Run Docker Container

```bash
docker run --rm employee-rdd
```

---

## Sample Output

### Employees Sorted by Salary (Descending)

```text
(4, 'Priya', 'Finance', 70000)
(3, 'Neha', 'IT', 65000)
(7, 'Rohit', 'Finance', 60000)
(1, 'Amit', 'IT', 55000)
(5, 'Karan', 'IT', 50000)
(6, 'Simran', 'HR', 45000)
(2, 'Rahul', 'HR', 40000)
```

### Total Salary by Department

```text
('IT', 170000)
('HR', 85000)
('Finance', 130000)
```

### Top 3 Highest-Paid Employees

```text
(4, 'Priya', 'Finance', 70000)
(3, 'Neha', 'IT', 65000)
(7, 'Rohit', 'Finance', 60000)
```

---

## Key Learning Outcomes

- Understanding Apache Spark RDD operations.
- Using transformations and actions in PySpark.
- Performing distributed data processing.
- Containerizing applications with Docker.
- Managing project dependencies and deployment.

---
