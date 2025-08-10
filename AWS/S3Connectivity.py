'''
Assignment:
1.  Read the data from mysql table and write on to s3 in a csv file

S3 URI:

bucket_name = bucket-june-batch/
file_key = employees_data/emp_detail.csv

'''

import pandas as pd
import boto3
from io import StringIO

# Initiate a session with aws
s3 = boto3.client("s3")

def read_data_from_s3(bucket_name,file_key):
    response = s3.get_object(Bucket=bucket_name,Key=file_key)
    csv_content = response['Body'].read().decode('utf-8')
    data_csv = StringIO(csv_content)
    df = pd.read_csv(data_csv)
    print(df)
    return df



def write_data_to_s3(df,bucket_name,file_key):
    csv_buffer = StringIO()
    df.to_csv(csv_buffer,index=False)
    s3.put_object(Bucket=bucket_name,Key=file_key,Body=csv_buffer.getvalue())



# Calling the function
bucket_name = "bucket-june-batch"
file_key_src = "employees_data/emp_detail.csv"
file_key_tgt = "employees_data/emp_tgt.csv"
df = read_data_from_s3(bucket_name,file_key_src)

write_data_to_s3(df,bucket_name,file_key_tgt)

