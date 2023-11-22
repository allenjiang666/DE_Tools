import uuid
import boto3
import snowflake.connector
import pandas as pd
import json


def format_data(df, email):
    guid = str(uuid.uuid4())
    batch_dict = {'Details':{'IdType':'CustomerId',
                          'VintageBatchId':guid,
                          'VintageOperatorId':email,
                          'VintageRequestReason':'Automated vintage batch testing'},
                          }
    
    df['DATE'] = pd.to_datetime(df['DATE']).dt.strftime("%Y-%m-%dT%H:%M:%S")
    df.columns = df.columns.str.capitalize()
    source_entries = df.to_dict('records')
    
    batch_dict['Entries']=source_entries
    return batch_dict
    
            

def get_data(user_input:str):

    ssm = boto3.client('ssm',region_name='us-east-1')
    username = ssm.get_parameter(Name = "/SNOWFLAKE/USER_ID", WithDecryption=True)["Parameter"]["Value"]
    password = ssm.get_parameter(Name = "/SNOWFLAKE/PASSWORD", WithDecryption=True)["Parameter"]["Value"]
    account = ssm.get_parameter(Name = "/SNOWFLAKE/ACCOUNT", WithDecryption=True)["Parameter"]["Value"]

    conn= snowflake.connector.connect(user=username,password=password, account=account)

    cursor = conn.cursor()

    cursor.execute(user_input["query"])

    df = cursor.fetch_pandas_all()

    file_type = user_input["file_path"].split('.')[-1]

    if file_type =='json':

        batch_dict = format_data(df, user_input['email'])
        
        # create an S3 client
        s3 = boto3.client('s3')

        # convert the dictionary to JSON string
        json_str = json.dumps(batch_dict)

        # upload the JSON string to S3 bucket
        
        response = s3.put_object(Bucket=user_input["bucket"], Key=user_input["file_path"], Body=json_str)

        if response['ResponseMetadata']['HTTPStatusCode'] == 200:
            return json_str, file_type


    if file_type == 'csv':
            
        with open('temp.csv', 'w') as f:
            df.to_csv(f, index=False)

        with open('temp.csv', 'r') as f:
            csv_str = f.read()

        response = s3.put_object(Bucket=user_input["bucket"], Key=user_input["file_path"], Body=csv_str)
        
        return json_str, file_type
