import boto3
import pandas as pd
from sqlalchemy import create_engine
import os

S3_BUCKET = os.getenv("S3_BUCKET")
S3_KEY = os.getenv("S3_KEY")

RDS_HOST = os.getenv("RDS_HOST")
RDS_USER = os.getenv("RDS_USER")
RDS_PASS = os.getenv("RDS_PASS")
RDS_DB = os.getenv("RDS_DB")
RDS_TABLE = os.getenv("RDS_TABLE")

GLUE_DB = os.getenv("GLUE_DB")
GLUE_TABLE = os.getenv("GLUE_TABLE")
GLUE_S3_PATH = os.getenv("GLUE_S3_PATH")

s3 = boto3.client("s3", region_name="ap-south-1")

print("Downloading from S3...")
s3.download_file(S3_BUCKET, S3_KEY, "data.csv")

df = pd.read_csv("data.csv")

try:
    print("Uploading to RDS...")

    engine = create_engine(
        f"mysql+pymysql://{RDS_USER}:{RDS_PASS}@{RDS_HOST}:3306/{RDS_DB}"
    )

    df.to_sql(RDS_TABLE, engine, if_exists="replace", index=False)

    print("Data inserted into RDS")

except Exception as e:
    print("RDS failed, switching to Glue")

    glue = boto3.client("glue", region_name="ap-south-1")

    glue.create_table(
        DatabaseName=GLUE_DB,
        TableInput={
            "Name": GLUE_TABLE,
            "StorageDescriptor": {
                "Columns": [{"Name": c, "Type": "string"} for c in df.columns],
                "Location": GLUE_S3_PATH,
            },
        },
    )

    print("Glue fallback table created")
