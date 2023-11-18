import boto3
import snowflake.connector


def format_data(df):
    n = len(df)
    import uuid
    guid = str(uuid.uuid4())
    entries = {'Details':{'IdType':'CustomerId',
                          'VintageBatchId':guid,
                          'VintageOperatorId':"email",
                          'VintageRequestReason':'Automated vintage batch testing'},
                          'Entries':[]
                          }
    source_dict = df.to_dict('dict')
    for i in range(n):
        # item = {source_dict['CUSTOMERID'][i]:source_dict['APP_DATE'][i].strftime("%Y-%m-%dT%H:%M:%S")}
        item = {}
        item['Id'] = source_dict['CUSTOMERID'][i]
        item['Date'] = source_dict['REPORT_DATE'][i].strftime("%Y-%m-%dT%H:%M:%S")
        entries['Entries'].append(item)
    return entries


ssm = boto3.client('ssm',region_name='us-east-1')
username = ssm.get_parameter(Name = "/SNOWFLAKE/USER_ID", WithDecryption=True)["Parameter"]["Value"]
password = ssm.get_parameter(Name = "/SNOWFLAKE/PASSWORD", WithDecryption=True)["Parameter"]["Value"]
account = ssm.get_parameter(Name = "/SNOWFLAKE/ACCOUNT", WithDecryption=True)["Parameter"]["Value"]

conn= snowflake.connector.connect(user=username,password=password, account=account)

cursor = conn.cursor()

query = '''
SELECT TOP 10 A.FUNDED_DATE AS REPORT_DATE, d.customerid
from BE_ANALYTICS_OPS.FLRA_ANLYTCS.ad_call1_a a
inner join be_analytics_ops.flra_anlytcs.ad_Call1_b b on UPPER(a.applicationid) = UPPER(b.applicationid)
inner join be_analytics_ops.flra_anlytcs.ad_Call1_c c on UPPER(a.applicationid) = UPPER(c.applicationid)
left join BE_DW.PUBLIC.VW_DIMAPPLICATION d on UPPER(a.applicationid) = UPPER(d.applicationid)
'''

cursor.execute(query)

result_dict = cursor.fetch_pandas_all().to_dict('dict')

print(result_dict)