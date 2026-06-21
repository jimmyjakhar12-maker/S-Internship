# Dockerized Python Application

## Overview
This project demonstrates a simple Dockerized Python application using the official Python 3.12 Slim image. The application prints the current Python version and current date & time inside the Docker container.

## Project Structure

```text
docker-python-app/
│
├── app.py
├── Dockerfile
├── requirements.txt
├── README.md
└── screenshot.png
```

## Build the Docker Image


```bash
docker build -t python-time-app .
```

## Run the Docker Container

```bash
docker run --rm python-time-app
```

## Sample Output

```text
Python Version: 3.12.x
Current Date and Time: 2026-06-18 22:30:15.123456
```

## Sample Output Screenshot
![Docker Output](./screenshot 2026-06-18 225257.png)

## Base Image

```text
python:3.12-slim
```

## Author

Jatin Jakhar

