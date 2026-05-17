# Dockerized AWS ETL Pipeline with RDS Failover to AWS Glue

## Project Overview

This project demonstrates a cloud-native ETL pipeline built using AWS services and Docker.

The application automatically:
- Reads CSV data from Amazon S3
- Processes CSV using Python & Pandas
- Inserts records into Amazon RDS MySQL
- Automatically switches to AWS Glue if RDS becomes unavailable

This project demonstrates automation, fault tolerance, Docker containerization, and AWS cloud integration.

---

## Architecture

S3 → Dockerized Python Application → Amazon RDS
                    ↓
              AWS Glue Fallback

---

## Technologies Used

- AWS S3
- AWS RDS MySQL
- AWS Glue
- Docker
- Python
- Pandas
- SQLAlchemy
- Boto3
- Linux

---

## Features

- Automated ETL pipeline
- Dockerized Python application
- CSV ingestion from S3
- Amazon RDS integration
- AWS Glue failover support
- Fault-tolerant design
- Cloud-native workflow

---

## Docker Build Command

```bash
docker build -t project3 .
```

## Docker Run Command

```bash
docker run \
-e S3_BUCKET=project3-bucket-rohit \
-e S3_KEY=students.csv \
-e RDS_HOST=database-2.xxxxx.ap-south-1.rds.amazonaws.com \
-e RDS_USER=admin \
-e RDS_PASS=password \
-e RDS_DB=project3db \
-e RDS_TABLE=students \
-e GLUE_DB=project3_glue_db \
-e GLUE_TABLE=students \
-e GLUE_S3_PATH=s3://project3-bucket-rohit/ \
project3
```

---

## Workflow

1. CSV file uploaded to Amazon S3
2. Docker container downloads CSV
3. Python application reads CSV using Pandas
4. Data inserted into Amazon RDS MySQL
5. If RDS fails, AWS Glue fallback activates
6. Glue table created automatically

---

## Skills Demonstrated

- Docker
- AWS Cloud
- Amazon S3
- Amazon RDS
- AWS Glue
- Python Automation
- ETL Pipelines
- Cloud Integration
- Fault Tolerance
- DevOps Practices

---

## Project Outcome

Successfully implemented a Dockerized ETL pipeline that securely transfers data from Amazon S3 to Amazon RDS with automatic fallback to AWS Glue during database failure scenarios.

---

## Author

Tejas Ingawale
