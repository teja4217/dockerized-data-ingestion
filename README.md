# Dockerized Data Ingestion Project

## Objective
This project automates data ingestion from Amazon S3 to Amazon RDS using a Dockerized Python application.

If RDS becomes unavailable, the application automatically switches to AWS Glue Data Catalog.

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

---

## Architecture

S3 → Dockerized Python App → RDS  
                ↓  
          AWS Glue Fallback

---

## Project Workflow

1. CSV file uploaded to Amazon S3
2. Docker container downloads CSV
3. Python application reads CSV using Pandas
4. Data inserted into Amazon RDS MySQL
5. If RDS fails, AWS Glue fallback activates
6. Glue table created automatically

---

## Docker Build Command

```bash
docker build -t project3 .
```

---

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

## AWS Services Used

- Amazon S3
- Amazon RDS
- AWS Glue
- IAM
- EC2
- Docker

---

## Output

- Data successfully inserted into RDS
- Glue fallback activated during database failure

---

## Skills Demonstrated

- Docker Containerization
- AWS Cloud Integration
- Python Automation
- ETL Pipeline
- Fault Tolerance
- Data Engineering Basics
- DevOps Practices

---

## Author

Tejas Ingawale
