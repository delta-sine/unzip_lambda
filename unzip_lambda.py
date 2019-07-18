#!/Library/Frameworks/Python.framework/Versions/3.6/bin/python3
import zipfile
import boto3
import pandas
import io
import os

#Create S3 client
s3 = boto3.client('s3')
bucket='celgene-data'

def zip_to_df(b, k):
    zip_file = io.BytesIO(s3.get_object(Bucket=b, Key=k)['Body'].read())
    df_list = []
    with zipfile.ZipFile(zip_file, 'r') as z:
        for f in z.namelist():
            df_list.append(pandas.read_csv(io.BytesIO(z.read(f))))
    return df_list

df_1= zip_to_df(bucket, 'alkirempi.zip')[0]
df_2 = zip_to_df(bucket,'countries-of-the-world.zip')[0]

print(df_1)
print(df_1)
